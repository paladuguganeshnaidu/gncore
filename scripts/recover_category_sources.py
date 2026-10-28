"""Recover registry-rate-limited candidates from their public GitHub sources."""

from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import re
import shutil
import urllib.request

import yaml

from research_categories import ROOT, WORK, github


def raw(repo, revision, path):
    request = urllib.request.Request(f"https://raw.githubusercontent.com/{repo}/{revision}/{path}", headers={"User-Agent": "GNCore-source-review"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def recover_repo(repo, items):
    container = WORK / "github-recovery" / repo.replace("/", "--")
    record_path = container / "inventory.json"
    if record_path.exists():
        return json.loads(record_path.read_text(encoding="utf-8"))
    container.mkdir(parents=True, exist_ok=True)
    try:
        revision = github(f"repos/{repo}/commits/HEAD")["sha"]
        tree = github(f"repos/{repo}/git/trees/{revision}?recursive=1")
        blobs = [p["path"] for p in tree["tree"] if p["type"] == "blob"]
        entrypoints = [p for p in blobs if p.endswith("SKILL.md")]
        notices = {}
        for path in blobs:
            if "/" not in path and re.fullmatch(r"(licen[cs]e|notice|copying)(\.[^/]*)?", path, re.I):
                notices[path] = raw(repo, revision, path).decode("utf-8", errors="replace")
        recovered = []
        for item in items:
            name = item["name"]
            normalize = lambda value: re.sub(r"[^a-z0-9]", "", value.lower())
            matches = sorted([p for p in entrypoints if normalize(Path(p).parent.name) == normalize(name)], key=lambda p: (len(Path(p).parts), p))
            if not matches and len(entrypoints) == 1:
                matches = entrypoints
            if not matches:
                recovered.append({**item, "status": "not-found-in-source-tree", "revision": revision, "tree_truncated": tree.get("truncated", False)})
                continue
            path = matches[0]
            entrypoint_data = raw(repo, revision, path)
            try:
                metadata = yaml.safe_load(entrypoint_data.decode("utf-8-sig").split("---", 2)[1])
            except (IndexError, UnicodeError, yaml.YAMLError):
                recovered.append({**item, "status": "invalid-source-entrypoint", "revision": revision})
                continue
            prefix = str(Path(path).parent).replace("\\", "/")
            prefix = "" if prefix == "." else prefix + "/"
            selected = [p for p in blobs if p.startswith(prefix)]
            if not prefix:
                selected = [p for p in selected if p == "SKILL.md" or p.startswith(("references/", "scripts/", "assets/", "rules/")) or re.match(r"(LICENSE|NOTICE|COPYING)", p, re.I)]
            destination = container / name
            destination.mkdir(parents=True, exist_ok=True)
            hashes = {}
            def copy(path):
                relative = path[len(prefix):]
                if ".." in Path(relative).parts or ":" in relative or "\\" in relative:
                    raise ValueError("Unsafe repository path")
                target = destination / relative
                content = entrypoint_data if path == matches[0] else raw(repo, revision, path)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
                return relative, hashlib.sha256(content).hexdigest()
            with ThreadPoolExecutor(max_workers=3) as pool:
                for relative, digest in pool.map(copy, selected):
                    hashes[relative] = digest
            recovered.append({"repository": repo, "name": name, "revision": revision, "source_path": path, "source_url": f"https://github.com/{repo}/blob/{revision}/{path}", "staged": str(destination), "metadata": metadata, "file_sha256": hashes, "notices": notices, "status": "downloaded-for-review", "download_method": "public-github-pinned-source"})
        record = {"repository": repo, "revision": revision, "skills": recovered}
    except Exception as error:
        record = {"repository": repo, "skills": [{**item, "status": "source-unavailable", "error": str(error)} for item in items]}
    record_path.write_text(json.dumps(record, indent=2, ensure_ascii=False, default=str), encoding="utf-8", newline="\n")
    return record


if __name__ == "__main__":
    path = WORK / "candidates.json"
    inventory = json.loads(path.read_text(encoding="utf-8"))
    repos = {}
    for item in inventory["downloads"]:
        if item["status"] == "downloaded-for-review" or not re.fullmatch(r"[\w.-]+/[\w.-]+", item["repository"]) or not re.fullmatch(r"[\w.-]+", item["name"]):
            continue
        repos.setdefault(item["repository"], []).append(item)
    replacements = {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(recover_repo, repo, items): repo for repo, items in repos.items()}
        for count, future in enumerate(as_completed(futures), 1):
            record = future.result()
            for item in record["skills"]:
                replacements[(item["repository"], item["name"])] = item
            print(f"Reviewed GitHub source {count}/{len(futures)}: {record['repository']}", flush=True)
    inventory["downloads"] = [replacements.get((i["repository"], i["name"]), i) for i in inventory["downloads"]]
    path.write_text(json.dumps(inventory, indent=2, ensure_ascii=False, default=str), encoding="utf-8", newline="\n")
    print("Downloaded snapshots:", sum(r["status"] == "downloaded-for-review" for r in inventory["downloads"]))
