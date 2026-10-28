"""Download and stage the user's backend skill sources at immutable revisions.

Uses the bundled Codex installer for archive safety and skill validation/copying.
Upstream instructions are treated as data; no downloaded script is executed.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import importlib.util
import json
from pathlib import Path
import re
import sys
import urllib.request

import yaml

from backend_requests import requests

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work/backend-import"


def fetch_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": "GNCore-skill-import"})
    with urllib.request.urlopen(request, timeout=90) as response:
        return json.load(response)


def import_repo(repo, wanted):
    destination = WORK / repo.replace("/", "--")
    record_path = destination / "inventory.json"
    if record_path.exists():
        return json.loads(record_path.read_text(encoding="utf-8"))
    destination.mkdir(parents=True, exist_ok=True)
    commit = fetch_json(f"https://api.github.com/repos/{repo}/commits/HEAD")
    revision = commit["sha"]
    checkout = Path(installer._download_repo_zip(*repo.split("/"), revision, str(destination)))
    available = []
    for path in checkout.rglob("SKILL.md"):
        if path.is_symlink():
            continue
        text = path.read_text(encoding="utf-8-sig")
        try:
            metadata = yaml.safe_load(text.split("---", 2)[1])
        except (IndexError, yaml.YAMLError):
            continue
        if isinstance(metadata, dict) and metadata.get("name"):
            available.append({"name": str(metadata["name"]), "path": path.relative_to(checkout).as_posix(), "metadata": metadata})
    selected = {}
    missing = []
    for name in wanted:
        matches = sorted((item for item in available if item["name"] == name), key=lambda item: (len(Path(item["path"]).parts), item["path"]))
        if not matches:
            missing.append(name)
            continue
        match = matches[0]
        source = checkout / match["path"]
        installer._validate_skill(str(source.parent), str(checkout))
        target = destination / "installed" / name
        if not target.exists():
            installer._copy_skill(str(source.parent), str(target))
        notices = {}
        for ancestor in [source.parent, *source.parent.parents]:
            if not ancestor.is_relative_to(checkout):
                break
            for path in ancestor.iterdir():
                if path.is_file() and re.fullmatch(r"(licen[cs]e|notice|copying)(\.[^/]*)?", path.name, re.I):
                    notices[path.relative_to(checkout).as_posix()] = path.read_text(encoding="utf-8-sig")
        # Vercel declares its repository license in README rather than a LICENSE file.
        if not notices and repo == "vercel-labs/agent-skills":
            notices["README.md"] = (checkout / "README.md").read_text(encoding="utf-8")
        selected[name] = {**match, "staged": str(target), "notices": notices}
    record = {"repository": repo, "revision": revision, "requested": wanted, "available": [{"name": a["name"], "path": a["path"]} for a in available], "selected": selected, "missing": missing}
    record_path.write_text(json.dumps(record, indent=2, ensure_ascii=False, default=str), encoding="utf-8", newline="\n")
    return record


if __name__ == "__main__":
    helper = Path.home() / ".codex/skills/.system/skill-installer/scripts/install-skill-from-github.py"
    sys.path.insert(0, str(helper.parent))
    spec = importlib.util.spec_from_file_location("gncore_backend_installer", helper)
    installer = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = installer
    spec.loader.exec_module(installer)
    sources = {}
    for entry in requests():
        sources.setdefault(entry["repository"], []).append(entry["requested"])
    records = []
    errors = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(import_repo, repo, wanted): repo for repo, wanted in sources.items()}
        for future in as_completed(futures):
            repo = futures[future]
            try:
                record = future.result()
                records.append(record)
                print(f"{repo}: {len(record['selected'])}/{len(record['requested'])} found; missing: {', '.join(record['missing']) or 'none'}", flush=True)
            except Exception as error:
                errors.append({"repository": repo, "error": str(error)})
                print(f"{repo}: ERROR {error}", flush=True)
    WORK.mkdir(parents=True, exist_ok=True)
    (WORK / "inventory.json").write_text(json.dumps({"sources": records, "errors": errors}, indent=2, ensure_ascii=False, default=str), encoding="utf-8", newline="\n")
    print(f"Requested {sum(len(v) for v in sources.values())} skills from {len(sources)} repositories; import errors: {len(errors)}")
    sys.exit(bool(errors))
