#!/usr/bin/env python3
"""Monitoring du dépôt manssuetude-ai-ki.

Vérifie :
1. Les liens vers ce dépôt (jsDelivr ou raw.githubusercontent.com) pointent vers des fichiers qui existent.
2. Le point d'entrée system-prompt.md est bien lisible en ligne (dépôt public, branche main).
3. Chaque commission listée dans system-prompt.md a son fichier dans commissions/.
4. Les templates du Drive (commun/documents.md) sont accessibles par lien, sans connexion.
5. Les autres liens externes répondent.
6. Aucun tiret cadratin dans les fichiers, sauf la mention « (—) » qui l'interdit.

Sortie : code 1 si au moins une erreur, avec un résumé lisible dans les logs
et dans le résumé de l'exécution GitHub Actions.
"""
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_RAW = "https://cdn.jsdelivr.net/gh/Manssuetude/manssuetude-ai-ki@main/"
REPO_RAW_GH = "https://raw.githubusercontent.com/Manssuetude/manssuetude-ai-ki/main/"
PURGE = "https://purge.jsdelivr.net/gh/Manssuetude/manssuetude-ai-ki@main/"
ENTRY_URL = REPO_RAW + "system-prompt.md"
UA = {"User-Agent": "Mozilla/5.0 (manssuetude-ai-ki monitoring)"}

URL_RE = re.compile(r"https?://[^\s)\]<>|`\"']+")
DRIVE_ID_RE = re.compile(r"\b[0-9A-Za-z_-]{25,}\b")

errors: list[str] = []
warnings: list[str] = []
ok: list[str] = []


def md_files():
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def fetch(url: str, timeout: int = 20):
    """Retourne (code HTTP, URL finale) après redirections."""
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, url
    except Exception as e:  # réseau, DNS, délai
        return 0, f"{url} ({e.__class__.__name__})"


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def check_repo_links():
    for f in md_files():
        text = f.read_text(encoding="utf-8")
        for m in URL_RE.finditer(text):
            url = m.group(0).rstrip(".,;:")
            prefix = next((p for p in (REPO_RAW, REPO_RAW_GH) if url.startswith(p)), None)
            if not prefix:
                continue
            if text[m.end():m.end() + 1] == "<":  # modèle du type commissions/<fichier>.md
                continue
            target = ROOT / url[len(prefix):]
            if target.is_file():
                ok.append(f"Lien interne OK : {url[len(prefix):]} (dans {rel(f)})")
            else:
                errors.append(f"Lien interne cassé dans {rel(f)} : {url}")


def check_entry_online():
    code, final = fetch(ENTRY_URL)
    if code == 0:
        warnings.append("jsDelivr injoignable depuis cette machine, lecture en ligne non vérifiée")
    elif code == 200:
        ok.append("system-prompt.md lisible en ligne")
    else:
        errors.append(f"system-prompt.md illisible en ligne (HTTP {code}) : dépôt privé, renommé ou branche changée ?")


def check_commission_files():
    text = (ROOT / "system-prompt.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\|\s*([^|]+?)\s*\|\s*([a-z0-9_-]+\.md)\s*\|", text, re.M)
    if not rows:
        errors.append("Aucune commission trouvée dans le tableau de system-prompt.md")
    for name, fname in rows:
        if (ROOT / "commissions" / fname).is_file():
            ok.append(f"Commission {name} : commissions/{fname} présent")
        else:
            errors.append(f"Commission {name} : fichier commissions/{fname} manquant")


def check_drive_templates():
    path = ROOT / "commun" / "documents.md"
    ids = list(dict.fromkeys(DRIVE_ID_RE.findall(path.read_text(encoding="utf-8"))))
    if not ids:
        errors.append("Aucun ID Drive trouvé dans commun/documents.md")
    for fid in ids:
        public, unreachable = False, True
        for url in (f"https://drive.google.com/file/d/{fid}/view",
                    f"https://drive.google.com/drive/folders/{fid}"):
            code, final = fetch(url)
            if code != 0:
                unreachable = False
            if code == 200 and "accounts.google.com" not in final:
                public = True
                break
        if unreachable:
            warnings.append(f"Drive injoignable depuis cette machine, template non vérifié : {fid}")
        elif public:
            ok.append(f"Template Drive accessible par lien : {fid}")
        else:
            errors.append(f"Template Drive inaccessible sans connexion (supprimé ou partage modifié) : {fid}")


def check_external_links():
    seen = set()
    for f in md_files():
        for url in URL_RE.findall(f.read_text(encoding="utf-8")):
            url = url.rstrip(".,;:")
            if url.startswith((REPO_RAW, REPO_RAW_GH)) or "drive.google.com" in url or "docs.google.com" in url or url in seen:
                continue
            seen.add(url)
            code, _ = fetch(url)
            if code == 0:
                warnings.append(f"Lien externe injoignable depuis cette machine : {url}")
            elif 200 <= code < 400:
                ok.append(f"Lien externe OK : {url}")
            else:
                errors.append(f"Lien externe en erreur (HTTP {code}) dans {rel(f)} : {url}")


def check_em_dash():
    for f in md_files():
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if "—" in line.replace("(—)", ""):
                errors.append(f"Tiret cadratin dans {rel(f)}, ligne {i}")


def purge_cdn():
    """Sur GitHub Actions, vide le cache jsDelivr pour que les modifications soient en ligne tout de suite."""
    if not os.environ.get("GITHUB_ACTIONS"):
        return
    for f in md_files():
        code, _ = fetch(PURGE + rel(f))
        if code == 200:
            ok.append(f"Cache jsDelivr vidé : {rel(f)}")
        else:
            warnings.append(f"Cache jsDelivr non vidé (HTTP {code}) : {rel(f)}")


def main():
    purge_cdn()
    for check in (check_repo_links, check_entry_online, check_commission_files,
                  check_drive_templates, check_external_links, check_em_dash):
        check()

    report = ["## Monitoring manssuetude-ai-ki", ""]
    report.append(f"**{len(errors)} erreur(s)**, {len(warnings)} avertissement(s), {len(ok)} vérification(s) réussie(s)")
    if errors:
        report += ["", "### Erreurs"] + [f"- {e}" for e in errors]
    if warnings:
        report += ["", "### Avertissements"] + [f"- {w}" for w in warnings]
    report += ["", "<details><summary>Vérifications réussies</summary>", ""]
    report += [f"- {o}" for o in ok] + ["", "</details>"]
    out = "\n".join(report)
    print(out)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(out + "\n")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
