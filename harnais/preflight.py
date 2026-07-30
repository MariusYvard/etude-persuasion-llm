#!/usr/bin/env python3
"""
Preflight des acces API.

Verifie que le .env est en place et que chaque fournisseur repond.
N'affiche jamais une cle, meme partiellement masquee.

Usage :
    python harnais/preflight.py

Aucune dependance externe, stdlib uniquement.
"""

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
ENV = RACINE / ".env"

VERT = "\033[32m"
ROUGE = "\033[31m"
JAUNE = "\033[33m"
GRIS = "\033[90m"
RAZ = "\033[0m"


def charger_env(chemin: Path) -> dict:
    """Parseur .env minimal. Ignore commentaires et lignes vides."""
    if not chemin.exists():
        print(f"{ROUGE}Aucun .env trouve a {chemin}{RAZ}")
        print(f"  Copier .env.example vers .env puis renseigner les valeurs.")
        sys.exit(1)
    valeurs = {}
    for ligne in chemin.read_text(encoding="utf-8").splitlines():
        ligne = ligne.strip()
        if not ligne or ligne.startswith("#") or "=" not in ligne:
            continue
        cle, _, val = ligne.partition("=")
        valeurs[cle.strip()] = val.strip().strip("'\"")
    return valeurs


def appel(url: str, entetes: dict) -> tuple:
    """Retourne (ok, detail). Ne remonte jamais le contenu des entetes."""
    requete = urllib.request.Request(url, headers=entetes)
    try:
        with urllib.request.urlopen(requete, timeout=20) as reponse:
            corps = json.loads(reponse.read().decode("utf-8"))
            donnees = corps.get("data") or corps.get("models") or []
            return True, f"{len(donnees)} modeles visibles"
    except urllib.error.HTTPError as err:
        if err.code in (401, 403):
            return False, f"HTTP {err.code}, cle refusee ou droits insuffisants"
        return False, f"HTTP {err.code}"
    except Exception as err:
        return False, f"{type(err).__name__}"




CONTROLES = [
    (
        "Anthropic",
        "ANTHROPIC_API_KEY",
        lambda k: appel(
            "https://api.anthropic.com/v1/models",
            {"x-api-key": k, "anthropic-version": "2023-06-01"},
        ),
    ),
    (
        "OpenAI",
        "OPENAI_API_KEY",
        lambda k: appel(
            "https://api.openai.com/v1/models",
            {"Authorization": f"Bearer {k}"},
        ),
    ),
    (
        "Mistral",
        "MISTRAL_API_KEY",
        lambda k: appel(
            "https://api.mistral.ai/v1/models",
            {"Authorization": f"Bearer {k}"},
        ),
    ),
    (
        "Alibaba",
        "ALIBABA_API_KEY",
        lambda k: appel(
            os.environ.get("ALIBABA_BASE_URL", "").rstrip("/") + "/models",
            {"Authorization": f"Bearer {k}"},
        ),
    ),
    (
        "NVIDIA",
        "NVIDIA_API_KEY",
        lambda k: appel(
            "https://integrate.api.nvidia.com/v1/models",
            {"Authorization": f"Bearer {k}"},
        ),
    ),
]

# Parametres qui doivent etre identiques pour les cinq generateurs.
# Un ecart ici confond effet de famille et effet de decodage.
PARAMS_PARTAGES = ["GEN_TEMPERATURE", "GEN_TOP_P", "GEN_REASONING_EFFORT"]

# Verification que les identifiants configures existent reellement cote fournisseur.
# Un identifiant plausible mais inexistant ne se voit qu'au premier appel de production.
CIBLES = [
    ("GEN_MODEL_ANTHROPIC", "Anthropic", "ANTHROPIC_API_KEY",
     "https://api.anthropic.com/v1/models",
     lambda k: {"x-api-key": k, "anthropic-version": "2023-06-01"}),
    ("GEN_MODEL_OPENAI", "OpenAI", "OPENAI_API_KEY",
     "https://api.openai.com/v1/models",
     lambda k: {"Authorization": f"Bearer {k}"}),
    ("GEN_MODEL_MISTRAL", "Mistral", "MISTRAL_API_KEY",
     "https://api.mistral.ai/v1/models",
     lambda k: {"Authorization": f"Bearer {k}"}),
    # $ALIBABA_BASE_URL est resolu a l'usage, pas ici : CIBLES est construit
    # avant que le .env ne soit charge dans os.environ.
    ("GEN_MODEL_ALIBABA", "Alibaba", "ALIBABA_API_KEY",
     "$ALIBABA_BASE_URL/models",
     lambda k: {"Authorization": f"Bearer {k}"}),
    # Cinquieme generateur servi par NVIDIA et non par son editeur.
    ("GEN_MODEL_MOONSHOT", "NVIDIA", "NVIDIA_API_KEY",
     "https://integrate.api.nvidia.com/v1/models",
     lambda k: {"Authorization": f"Bearer {k}"}),
]

# Sondes d'echantillonnage. Le preflight verifiait que les valeurs sont figees
# au .env, pas qu'un fournisseur les accepte. Un fournisseur qui ignore
# silencieusement temperature ou top_p ferait tomber le critere 3 sans alerte.
#
# Test retenu, comportemental plutot que declaratif : plusieurs tirages a
# temperature 0 puis a la temperature de production. Si le nombre de sorties
# distinctes n'augmente pas, le parametre n'est pas honore.
SONDE_PROMPT = "Invente un mot qui n'existe pas. Reponds par ce seul mot."
SONDE_TIRAGES = 4


def _post(url: str, entetes: dict, charge: dict) -> str:
    corps = json.dumps(charge).encode("utf-8")
    entetes = dict(entetes)
    entetes["Content-Type"] = "application/json"
    requete = urllib.request.Request(url, data=corps, headers=entetes, method="POST")
    with urllib.request.urlopen(requete, timeout=60) as reponse:
        rep = json.loads(reponse.read().decode("utf-8"))
    if "content" in rep:  # forme Anthropic
        return "".join(b.get("text", "") for b in rep["content"]).strip()
    return rep["choices"][0]["message"]["content"].strip()


def sonde(nom: str, url: str, entetes: dict, modele: str, temp: float) -> set:
    """Retourne l'ensemble des sorties distinctes sur SONDE_TIRAGES appels."""
    anthropic = "anthropic.com" in url
    sorties = set()
    for _ in range(SONDE_TIRAGES):
        charge = {"model": modele, "max_tokens": 12, "temperature": temp,
                  "messages": [{"role": "user", "content": SONDE_PROMPT}]}
        if not anthropic:
            charge["top_p"] = 1.0
        sorties.add(_post(url, entetes, charge))
    return sorties


def identifiants(url: str, entetes: dict) -> list:
    try:
        requete = urllib.request.Request(url, headers=entetes)
        with urllib.request.urlopen(requete, timeout=25) as reponse:
            corps = json.loads(reponse.read().decode("utf-8"))
            donnees = corps.get("data") or corps.get("models") or []
            return [m.get("id") or m.get("name") for m in donnees]
    except Exception:
        return []

GENERATEURS_ATTENDUS = [
    "GEN_MODEL_ANTHROPIC",
    "GEN_MODEL_OPENAI",
    "GEN_MODEL_MISTRAL",
    "GEN_MODEL_ALIBABA",
    "GEN_MODEL_MOONSHOT",
]

# Lignee du modele de base, pas simple prefixe d'editeur.
#
# Piege : chez NVIDIA, "nvidia/llama-3.3-nemotron-super-49b" est un derive de Llama
# et "nvidia/mistral-nemo-minitron-8b" un derive de Mistral. Un controle par prefixe
# les classerait en famille "nvidia" et laisserait passer un juge Mistral-derive
# notant les sorties du generateur Mistral. Le nom du modele prime sur l'editeur.
LIGNEES = ("llama", "mistral", "mixtral", "gemma", "phi", "qwen", "yi",
           "deepseek", "granite", "jamba", "dbrx", "palmyra", "nemotron",
           "kimi", "glm", "minimax", "step", "zamba", "sea-lion", "claude", "gpt")


# Provenance d'alignement, pas de siege social de l'hebergeur. Sert deux
# controles : le panel de juges ne peut pas etre monoculturel (H3 mesure un
# biais culturel), et les generateurs doivent couvrir au moins deux provenances
# faute de quoi le contraste 5 n'a pas de bras de comparaison.
PROVENANCE = {
    "deepseek": "CN", "kimi": "CN", "glm": "CN", "minimax": "CN",
    "yi": "CN", "step": "CN", "qwen": "CN",
    "llama": "US", "nemotron": "US", "phi": "US", "gemma": "US",
    "dbrx": "US", "granite": "US", "palmyra": "US", "zamba": "US",
    "jamba": "IL", "sea-lion": "SG",
    "claude": "US", "gpt": "US", "mistral": "FR",
}


def lignee(ident: str) -> str:
    bas = ident.lower()
    nom = bas.split("/", 1)[1] if "/" in bas else bas
    for l in LIGNEES:
        if l in nom:
            return l
    return bas.split("/")[0] if "/" in bas else nom.split("-")[0]


def main() -> int:
    env = charger_env(ENV)
    os.environ.update(env)
    echecs = 0

    print(f"\n{GRIS}Preflight des acces, {ENV}{RAZ}\n")

    print("Acces fournisseurs")
    for nom, var, test in CONTROLES:
        cle = env.get(var, "")
        if not cle:
            print(f"  {JAUNE}o{RAZ} {nom:<10} {GRIS}{var} absente ou vide{RAZ}")
            echecs += 1
            continue
        ok, detail = test(cle)
        marque = f"{VERT}v{RAZ}" if ok else f"{ROUGE}x{RAZ}"
        print(f"  {marque} {nom:<10} {GRIS}{detail}{RAZ}")
        if not ok:
            echecs += 1

    print("\nIdentifiants de modeles, a figer avant production")
    cat_nvidia = None
    if env.get("NVIDIA_API_KEY"):
        cat_nvidia = identifiants(
            "https://integrate.api.nvidia.com/v1/models",
            {"Authorization": "Bearer " + env["NVIDIA_API_KEY"]},
        )

    dyn = sorted(k for k in env if k.startswith(("JUDGE_", "BUILDER_MODEL")))
    for var in GENERATEURS_ATTENDUS + dyn:
        val = env.get(var, "")
        if not val:
            print(f"  {JAUNE}o{RAZ} {var:<22} {GRIS}non renseigne{RAZ}")
            echecs += 1
            continue

        if var.startswith(("JUDGE_", "BUILDER_MODEL")):
            if not cat_nvidia:
                print(f"  {JAUNE}o{RAZ} {var:<22} {GRIS}{val}, catalogue NVIDIA illisible{RAZ}")
            elif val in cat_nvidia:
                print(f"  {VERT}v{RAZ} {var:<22} {GRIS}{val}, existe chez NVIDIA{RAZ}")
            else:
                print(f"  {ROUGE}x{RAZ} {var:<22} {GRIS}{val}, INTROUVABLE chez NVIDIA{RAZ}")
                echecs += 1
            continue

        cible = next((c for c in CIBLES if c[0] == var), None)
        if cible is None:
            print(f"  {VERT}v{RAZ} {var:<22} {GRIS}{val}{RAZ}")
            continue
        _, nom, var_cle, url, entetes = cible
        url = url.replace("$ALIBABA_BASE_URL",
                          env.get("ALIBABA_BASE_URL", "").rstrip("/"))
        dispo = identifiants(url, entetes(env.get(var_cle, "")))
        if not dispo:
            print(f"  {JAUNE}o{RAZ} {var:<22} {GRIS}{val}, existence non verifiable{RAZ}")
        elif val in dispo:
            print(f"  {VERT}v{RAZ} {var:<22} {GRIS}{val}, existe chez {nom}{RAZ}")
        else:
            print(f"  {ROUGE}x{RAZ} {var:<22} {GRIS}{val}, INTROUVABLE chez {nom}{RAZ}")
            echecs += 1

    print("\nDisjonction des lignees")
    juges = [v for k, v in sorted(env.items())
             if k.startswith("JUDGE_") and v]
    builders = [v for k, v in sorted(env.items())
                if k.startswith("BUILDER_MODEL") and v]
    generateurs = [env.get(k, "") for k in GENERATEURS_ATTENDUS]
    generateurs = [g for g in generateurs if g]

    lign_gen = {lignee(g) for g in generateurs}
    probleme = False

    if len(lign_gen) < len(generateurs):
        print(f"  {ROUGE}x{RAZ} deux generateurs partagent une lignee")
        print(f"    {GRIS}le plan exige {len(generateurs)} familles distinctes{RAZ}")
        probleme = True

    prov_gen = {PROVENANCE.get(lignee(g), "?") for g in generateurs}
    if len(prov_gen) < 2:
        print(f"  {ROUGE}x{RAZ} generateurs de provenance unique : {', '.join(sorted(prov_gen))}")
        print(f"    {GRIS}le contraste 5 n'a pas de bras de comparaison{RAZ}")
        probleme = True
    else:
        print(f"  {VERT}v{RAZ} provenances des generateurs : {', '.join(sorted(prov_gen))}")

    for etiquette, groupe in (("juge", juges), ("constructeur", builders)):
        for m in groupe:
            if lignee(m) in lign_gen:
                print(f"  {ROUGE}x{RAZ} {etiquette} {m}")
                print(f"    {GRIS}lignee '{lignee(m)}', identique a un generateur evalue{RAZ}")
                probleme = True

    croise = {lignee(b) for b in builders} & {lignee(j) for j in juges}
    if croise:
        print(f"  {ROUGE}x{RAZ} lignee partagee entre juges et constructeurs : {', '.join(sorted(croise))}")
        print(f"    {GRIS}un juge validerait le realisme d'un texte ecrit par sa propre lignee{RAZ}")
        probleme = True

    # Equilibre de provenance du panel. H3 mesure un biais culturel : un panel
    # d'une seule provenance confondrait la mesure avec la position d'ou l'on mesure.
    actifs = [env.get("JUDGE_MODEL_US", ""), env.get("JUDGE_MODEL_CN", "")]
    actifs = [a for a in actifs if a]
    if actifs:
        prov = {PROVENANCE.get(lignee(a), "?") for a in actifs}
        if len(prov) < 2:
            print(f"  {ROUGE}x{RAZ} juges a poids ouverts de provenance unique : {', '.join(sorted(prov))}")
            print(f"    {GRIS}H3 mesure un biais culturel, l'instrument ne peut pas etre monoculturel{RAZ}")
            probleme = True
        else:
            print(f"  {VERT}v{RAZ} provenances des juges a poids ouverts : {', '.join(sorted(prov))}")

    if probleme:
        echecs += 1
    elif juges and builders:
        print(f"  {VERT}v{RAZ} {len(juges)} juge(s), {len(builders)} constructeur(s), "
              f"lignees toutes distinctes des generateurs")
        print(f"    {GRIS}juges        : {', '.join(sorted({lignee(j) for j in juges}))}{RAZ}")
        print(f"    {GRIS}constructeurs: {', '.join(sorted({lignee(b) for b in builders}))}{RAZ}")
    else:
        print(f"  {JAUNE}o{RAZ} {GRIS}controle impossible, juges ou constructeurs non renseignes{RAZ}")

    print("\nParametres d'echantillonnage, identiques pour les cinq generateurs")
    for var in PARAMS_PARTAGES:
        val = env.get(var, "")
        marque = f"{VERT}v{RAZ}" if val else f"{JAUNE}o{RAZ}"
        affichage = val if val else "non renseigne"
        print(f"  {marque} {var:<22} {GRIS}{affichage}{RAZ}")
        if not val:
            echecs += 1

    if "--echo" in sys.argv:
        print("\nEcho des parametres, les fournisseurs les acceptent-ils vraiment")
        base_ali = env.get("ALIBABA_BASE_URL", "").rstrip("/")
        cibles = [
            ("Anthropic", "https://api.anthropic.com/v1/messages",
             {"x-api-key": env.get("ANTHROPIC_API_KEY", ""),
              "anthropic-version": "2023-06-01"}, env.get("GEN_MODEL_ANTHROPIC", "")),
            ("OpenAI", "https://api.openai.com/v1/chat/completions",
             {"Authorization": "Bearer " + env.get("OPENAI_API_KEY", "")},
             env.get("GEN_MODEL_OPENAI", "")),
            ("Mistral", "https://api.mistral.ai/v1/chat/completions",
             {"Authorization": "Bearer " + env.get("MISTRAL_API_KEY", "")},
             env.get("GEN_MODEL_MISTRAL", "")),
            ("Alibaba", base_ali + "/chat/completions",
             {"Authorization": "Bearer " + env.get("ALIBABA_API_KEY", "")},
             env.get("GEN_MODEL_ALIBABA", "")),
            ("Moonshot", "https://integrate.api.nvidia.com/v1/chat/completions",
             {"Authorization": "Bearer " + env.get("NVIDIA_API_KEY", "")},
             env.get("GEN_MODEL_MOONSHOT", "")),
        ]
        chaud = float(env.get("GEN_TEMPERATURE", "1.0"))
        for nom, url, entetes, modele in cibles:
            if not modele:
                print(f"  {JAUNE}o{RAZ} {nom:<10} {GRIS}identifiant absent{RAZ}")
                echecs += 1
                continue
            try:
                froid = sonde(nom, url, entetes, modele, 0.0)
                vif = sonde(nom, url, entetes, modele, chaud)
            except urllib.error.HTTPError as err:
                try:
                    detail = err.read().decode("utf-8", "replace")[:160].replace("\n", " ")
                except Exception:
                    detail = ""
                print(f"  {ROUGE}x{RAZ} {nom:<10} {GRIS}HTTP {err.code}, {detail}{RAZ}")
                echecs += 1
                continue
            except Exception as err:
                print(f"  {JAUNE}o{RAZ} {nom:<10} {GRIS}sonde impossible, {type(err).__name__}{RAZ}")
                continue
            detail = f"{len(froid)} sortie(s) distincte(s) a t=0, {len(vif)} a t={chaud}"
            if len(vif) > len(froid):
                print(f"  {VERT}v{RAZ} {nom:<10} {GRIS}{detail}{RAZ}")
            else:
                print(f"  {ROUGE}x{RAZ} {nom:<10} {GRIS}{detail}{RAZ}")
                print(f"    {GRIS}la temperature ne change rien, parametre vraisemblablement ignore{RAZ}")
                echecs += 1

    print()
    if echecs:
        print(f"{JAUNE}{echecs} point(s) a regler avant la production.{RAZ}\n")
        return 1
    print(f"{VERT}Tous les acces repondent et les parametres sont figes.{RAZ}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
