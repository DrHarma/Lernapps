#!/usr/bin/env python3
"""Findet HTML-Apps und erstellt die Übersicht ohne zusätzliche Bibliotheken."""
import json
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import quote
ROOT = Path(__file__).resolve().parent.parent
SUBJECTS = {"chemie": "Chemie", "biologie": "Biologie", "molab": "MoLab", "sonstige-apps": "Sonstige Apps"}
class Metadata(HTMLParser):
    def __init__(self):
        super().__init__(); self.in_title = False; self.title = []; self.description = ""
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title": self.in_title = True
        if tag == "meta" and attrs.get("name", "").lower() == "description":
            self.description = attrs.get("content", "")
    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
    def handle_data(self, data):
        if self.in_title: self.title.append(data)
def build():
    apps = []
    for folder, subject in SUBJECTS.items():
        for path in sorted((ROOT / folder).rglob("*")):
            if not path.is_file() or path.suffix.lower() not in (".html", ".htm"): continue
            rel = path.relative_to(ROOT)
            parser = Metadata(); parser.feed(path.read_text(encoding="utf-8-sig"))
            year = rel.parts[1].upper() if folder in ("chemie", "biologie") and len(rel.parts) > 2 else ""
            title = " ".join("".join(parser.title).split()) or path.stem.replace("-", " ").capitalize()
            apps.append(dict(title=title, subject=subject, year=year, description=parser.description, path=quote(rel.as_posix(), safe="/")))
    apps.sort(key=lambda a: (list(SUBJECTS.values()).index(a["subject"]), a["year"], a["title"].casefold()))
    (ROOT / "apps.js").write_text("window.UNTERRICHTS_APPS = " + json.dumps(apps, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")
    return apps
if __name__ == "__main__":
    print(f"{len(build())} Apps erfasst.")
