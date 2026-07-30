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


def verifier_local(url: str) -> tuple:
    if not url:
        return None, "non configure"
    return appel(url.rstrip("/") + "/api/tags", {})


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
        "Google",
        "GEMINI_API_KEY",
        lambda k: appel(
            f"https://generativelanguage.googleapis.com/v1beta/models?key={k}",
            {},
        ),
    ),
]

# Parametres qui doivent etre identiques pour les trois generateurs.
# Un ecart ici confond effet de famille et effet de decodage.
PARAMS_PARTAGES = ["GEN_TEMPERATURE", "GEN_TOP_P"]

MODELES_ATTENDUS = [
    "GEN_MODEL_ANTHROPIC",
    "GEN_MODEL_OPENAI",
    "GEN_MODEL_MISTRAL",
    "JUDGE_LOCAL_MODEL",
]


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

    print("\nJuge local, famille D")
    ok, detail = verifier_local(env.get("JUDGE_LOCAL_ENDPOINT", ""))
    if ok is None:
        print(f"  {JAUNE}o{RAZ} {GRIS}{detail}{RAZ}")
    else:
        marque = f"{VERT}v{RAZ}" if ok else f"{ROUGE}x{RAZ}"
        print(f"  {marque} endpoint    {GRIS}{detail}{RAZ}")
        if not ok:
            echecs += 1

    print("\nIdentifiants de modeles, a figer avant production")
    for var in MODELES_ATTENDUS:
        val = env.get(var, "")
        marque = f"{VERT}v{RAZ}" if val else f"{JAUNE}o{RAZ}"
        affichage = val if val else "non renseigne"
        print(f"  {marque} {var:<22} {GRIS}{affichage}{RAZ}")
        if not val:
            echecs += 1

    print("\nParametres d'echantillonnage, identiques pour les trois generateurs")
    for var in PARAMS_PARTAGES:
        val = env.get(var, "")
        marque = f"{VERT}v{RAZ}" if val else f"{JAUNE}o{RAZ}"
        affichage = val if val else "non renseigne"
        print(f"  {marque} {var:<22} {GRIS}{affichage}{RAZ}")
        if not val:
            echecs += 1

    print()
    if echecs:
        print(f"{JAUNE}{echecs} point(s) a regler avant la production.{RAZ}\n")
        return 1
    print(f"{VERT}Tous les acces repondent et les parametres sont figes.{RAZ}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
