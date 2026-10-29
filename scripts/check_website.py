"""Validate generated static pages, asset/anchor links and Cloudflare redirects."""

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.refs, self.ids, self.titles, self.canonical = [], set(), 0, []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "title":
            self.titles += 1
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href"))
        for key in ("href", "src"):
            if key in attrs:
                self.refs.append(attrs[key])


def check(root):
    root = root.resolve()
    pages = {path: Page(path.read_text(encoding="utf-8")) for path in root.rglob("*.html")}
    issues, checked = [], 0
    for path, page in pages.items():
        if page.titles != 1 or len(page.canonical) != 1:
            issues.append(f"invalid title/canonical: {path.relative_to(root)}")
        for raw in page.refs:
            url = urlsplit(raw)
            if url.scheme or url.netloc:
                continue
            candidate = (root / unquote(url.path).lstrip("/")) if url.path.startswith("/") else path.parent / unquote(url.path)
            if not url.path:
                candidate = path
            if candidate.is_dir():
                candidate = candidate / "index.html"
            candidate = candidate.resolve()
            checked += 1
            if not candidate.is_relative_to(root) or not candidate.is_file():
                issues.append(f"missing local reference: {path.relative_to(root)} -> {raw}")
            elif url.fragment and candidate in pages and unquote(url.fragment) not in pages[candidate].ids:
                issues.append(f"missing anchor: {path.relative_to(root)} -> {raw}")
    redirects = (root / "_redirects").read_text(encoding="utf-8").splitlines()
    seen = set()
    for line in redirects:
        source, target, code = line.split()
        if source in seen or source == target or code != "301" or len(line) > 1000:
            issues.append(f"invalid redirect: {line}")
        seen.add(source)
        if not (root / target.lstrip("/") / "index.html").is_file():
            issues.append(f"missing redirect target: {target}")
    if len(redirects) > 2000:
        issues.append("static Cloudflare redirect limit exceeded")
    ET.parse(root / "sitemap.xml")
    catalog = json.loads((root / "assets/catalog.json").read_text(encoding="utf-8"))
    if catalog["categories"] != len(catalog["skills"]) or catalog["workflows"] != sum(len(s["workflows"]) for s in catalog["skills"]):
        issues.append("website catalog counts do not reconcile")
    return {"ok": not issues, "html_pages": len(pages), "local_links_checked": checked, "redirects_checked": len(redirects),
            "categories": catalog["categories"], "workflows": catalog["workflows"], "issues": issues}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, nargs="?", default=Path(__file__).resolve().parents[1] / "website")
    args = parser.parse_args()
    report = check(args.directory)
    print(json.dumps(report, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
