"""Research one reviewed upstream candidate per GNCore category.

Search results are evidence, not instructions. Only portable skill directories
are staged; source hooks and executables are never run. All search candidates,
selection reasons, immutable revisions, failures, and license decisions are kept.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import urllib.parse
import urllib.request

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work/category-research"


def request_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": "GNCore-category-research"})
    with urllib.request.urlopen(request, timeout=90) as response:
        return json.load(response)


def github(path):
    result = subprocess.run(["gh", "api", path], capture_output=True, text=True, encoding="utf-8", timeout=120)
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    return json.loads(result.stdout)


TRUSTED = {"anthropics", "vercel-labs", "supabase", "cloudflare", "redis", "getsentry", "learning-commons-org"}
QUERIES = {
    "general": "software workflow", "company-leadership": "executive leadership",
    "people-human-resources": "human resources hiring", "word-documents": "docx",
    "pdf-documents": "pdf", "presentations-powerpoint": "powerpoint pptx",
    "spreadsheets": "xlsx spreadsheet", "web-frontend": "frontend design",
    "backend-engineering": "backend architecture", "code-engineering": "coding standards",
    "healthcare-operations": "healthcare operations", "professional-services": "contract review",
    "legal-compliance": "legal compliance", "cloud-devops-sre": "sre observability",
    "data-analytics": "data analysis", "business-communications": "business writing",
    "quality-engineering": "test strategy", "design-ux": "ux design",
}


def search(category):
    path = WORK / "search" / f"{category}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    query = QUERIES.get(category, category.replace("-", " "))
    data = request_json("https://skills.sh/api/search?" + urllib.parse.urlencode({"q": query, "limit": 8}))
    candidates = []
    for item in data.get("skills", []):
        repo = item.get("source", "")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
            continue
        owner = repo.split("/")[0].lower()
        score = min(int(item.get("installs", 0)), 100000) / 10000 + (30 if owner in TRUSTED else 0)
        candidates.append({**item, "review_score": score})
    candidates.sort(key=lambda item: -item["review_score"])
    record = {"category": category, "query": query, "searched_at": "2026-10-28", "search_url": "https://skills.sh/api/search?" + urllib.parse.urlencode({"q": query, "limit": 8}), "candidates": candidates, "selected": candidates[:1], "selection_basis": "One relevant source candidate per category, preferring primary publishers; installation counts are a discovery signal, not a quality certification."}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2), encoding="utf-8", newline="\n")
    return record


def download(repo, names):
    container = WORK / "sources" / repo.replace("/", "--")
    output = container / "inventory.json"
    if output.exists():
        return json.loads(output.read_text(encoding="utf-8"))
    container.mkdir(parents=True, exist_ok=True)
    metadata = github(f"repos/{repo}")
    revision = github(f"repos/{repo}/commits/{metadata['default_branch']}")["sha"]
    checkout = Path(installer._download_repo_zip(*repo.split("/"), revision, str(container)))
    notices = {}
    for path in checkout.iterdir():
        if path.is_file() and re.fullmatch(r"(licen[cs]e|notice|copying)(\.[^/]*)?", path.name, re.I):
            notices[path.name] = path.read_text(encoding="utf-8-sig", errors="replace")
    all_skills = []
    for path in checkout.rglob("SKILL.md"):
        if path.is_symlink():
            continue
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8-sig").split("---", 2)[1])
        except (IndexError, UnicodeError, yaml.YAMLError):
            continue
        if isinstance(data, dict) and data.get("name"):
            all_skills.append((path, data))
    selected = []
    for name in sorted(names):
        matches = sorted([(p, m) for p, m in all_skills if m["name"] == name or p.parent.name == name], key=lambda pair: len(pair[0].parts))
        if not matches:
            selected.append({"name": name, "status": "not-found-at-pinned-revision"})
            continue
        path, data = matches[0]
        supplied = dict(notices)
        for file in path.parent.iterdir():
            if file.is_file() and re.fullmatch(r"(licen[cs]e|notice|copying)(\.[^/]*)?", file.name, re.I):
                supplied[file.name] = file.read_text(encoding="utf-8-sig", errors="replace")
        license_hint = str(data.get("license", "")) + "\n" + "\n".join(supplied.values())
        permitted = bool(re.search(r"MIT License|Permission is hereby granted|Apache License|Apache-2\.0|Attribution-ShareAlike 4\.0|CC-BY-SA-4\.0|BSD [23]-Clause|Creative Commons Attribution 4\.0", license_hint, re.I)) and not re.search(r"proprietary|all rights reserved.*without", str(data.get("license", "")), re.I)
        target = container / "installed" / name
        installer._validate_skill(str(path.parent), str(checkout))
        if not target.exists():
            installer._copy_skill(str(path.parent), str(target))
        selected.append({"name": name, "path": path.relative_to(checkout).as_posix(), "metadata": data, "staged": str(target), "notices": supplied, "status": "licensed-reference" if permitted else "research-only-license-not-cleared"})
    record = {"repository": repo, "revision": revision, "license_metadata": metadata.get("license"), "skills": selected}
    output.write_text(json.dumps(record, indent=2, ensure_ascii=False, default=str), encoding="utf-8", newline="\n")
    return record


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "src"))
    from gncore.skills.library import legacy_skills
    categories = sorted({s.metadata.category for s in legacy_skills()})
    # Preserve the pre-consolidation catalog, independently of future runtime APIs.
    snapshot = WORK / "legacy-catalog.json"
    WORK.mkdir(parents=True, exist_ok=True)
    if not snapshot.exists():
        snapshot.write_text(json.dumps([s.to_dict() for s in legacy_skills()], indent=2), encoding="utf-8", newline="\n")
    searches = []
    failures = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(search, category): category for category in categories}
        for future in as_completed(futures):
            category = futures[future]
            try:
                record = future.result()
                searches.append(record)
                print(f"Searched {category}: {len(record['candidates'])} candidates", flush=True)
            except Exception as error:
                failures.append({"category": category, "error": str(error)})
    sources = {}
    for record in searches:
        for candidate in record["selected"]:
            sources.setdefault(candidate["source"], set()).add(candidate.get("skillId") or candidate["name"])
    # Also inspect the primary business and education collections identified in web research.
    sources.setdefault("learning-commons-org/agent-skills", set()).update({"k12-lesson-plan-creation", "k12-lesson-differentiation"})
    helper = Path.home() / ".codex/skills/.system/skill-installer/scripts/install-skill-from-github.py"
    sys.path.insert(0, str(helper.parent))
    spec = importlib.util.spec_from_file_location("category_installer", helper)
    installer = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = installer
    spec.loader.exec_module(installer)
    downloads = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(download, repo, names): repo for repo, names in sources.items()}
        for future in as_completed(futures):
            repo = futures[future]
            try:
                record = future.result()
                downloads.append(record)
                print(f"Downloaded {repo}: {len(record['skills'])} selected skills", flush=True)
            except Exception as error:
                failures.append({"repository": repo, "error": str(error)})
                print(f"Source unavailable {repo}: {error}", flush=True)
    output = {"searched_at": "2026-10-28", "searches": sorted(searches, key=lambda r: r["category"]), "sources": downloads, "failures": failures}
    (WORK / "inventory.json").write_text(json.dumps(output, indent=2, ensure_ascii=False, default=str), encoding="utf-8", newline="\n")
    print(f"Research complete: {len(searches)}/{len(categories)} categories, {len(downloads)} source repositories, {len(failures)} recorded failures")
