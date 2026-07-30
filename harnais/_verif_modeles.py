import json, urllib.request, pathlib

env = {}
for l in pathlib.Path(".env").read_text(encoding="utf-8").splitlines():
    l = l.strip()
    if l and not l.startswith("#") and "=" in l:
        k, _, v = l.partition("=")
        env[k.strip()] = v.strip().strip("'").strip('"')

def liste(url, entetes):
    try:
        req = urllib.request.Request(url, headers=entetes)
        with urllib.request.urlopen(req, timeout=25) as r:
            d = json.loads(r.read().decode())
            return [m.get("id") or m.get("name") for m in (d.get("data") or d.get("models") or [])]
    except Exception as e:
        return ["ERREUR " + type(e).__name__]

a = liste("https://api.anthropic.com/v1/models",
          {"x-api-key": env.get("ANTHROPIC_API_KEY", ""), "anthropic-version": "2023-06-01"})
o = liste("https://api.openai.com/v1/models",
          {"Authorization": "Bearer " + env.get("OPENAI_API_KEY", "")})
m = liste("https://api.mistral.ai/v1/models",
          {"Authorization": "Bearer " + env.get("MISTRAL_API_KEY", "")})

for cible, dispo, nom in [("claude-opus-5", a, "Anthropic"),
                          ("gpt-5.6-terra", o, "OpenAI"),
                          ("mistral-medium-3-5", m, "Mistral")]:
    if cible in dispo:
        print("  OK      " + nom + " : " + cible)
    else:
        print("  ABSENT  " + nom + " : " + cible)
        racine = cible.split("-")[0]
        proches = [str(x) for x in dispo if x and racine in str(x)][:8]
        print("          disponibles proches : " + ", ".join(proches))