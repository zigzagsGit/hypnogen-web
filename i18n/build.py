"""Injecte les dictionnaires i18n/*.json dans index.html, entre /*I18N-BEGIN*/ et /*I18N-END*/.
Après toute modification d'un dictionnaire : python3 i18n/src_fr.py (pour le français) puis python3 i18n/build.py"""
import json, os, re
ici = os.path.dirname(os.path.abspath(__file__)); racine = os.path.dirname(ici)
LANGUES = ["fr", "en", "de", "es", "it"]
d = {c: json.load(open(os.path.join(ici, c + ".json"), encoding="utf-8")) for c in LANGUES}
ref = d["fr"]
for c, x in d.items():   # même jeu de clés partout
    assert x["t"].keys() == ref["t"].keys(), (c, set(x["t"]) ^ set(ref["t"]))
    assert x["seances"].keys() == ref["seances"].keys(), c
bloc = "/*I18N-BEGIN*/\nconst I18N=" + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + ";\n/*I18N-END*/"
p = os.path.join(racine, "index.html"); s = open(p, encoding="utf-8").read()
s, n = re.subn(r"/\*I18N-BEGIN\*/.*?/\*I18N-END\*/", lambda m: bloc, s, flags=re.S)
assert n == 1
open(p, "w", encoding="utf-8").write(s)
print("index.html :", ", ".join(LANGUES), "—", len(bloc) // 1024, "Ko de textes")
