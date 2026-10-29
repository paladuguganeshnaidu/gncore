"""Download all registry candidates found for each category as inert snapshots."""

from concurrent.futures import ThreadPoolExecutor, as_completed
import base64
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import time
import urllib.parse
import urllib.request

import yaml

from research_categories import ROOT, WORK, QUERIES


def get(url):
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "GNCore-category-research"})
            with urllib.request.urlopen(request, timeout=35) as response:
                return json.load(response)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(1 + attempt)


def search(category):
    output = WORK / "search" / f"{category}.json"
    if output.exists():
        record = json.loads(output.read_text(encoding="utf-8"))
    else:
        query = QUERIES.get(category, category.replace("-", " "))
        url = "https://skills.sh/api/search?" + urllib.parse.urlencode({"q": query, "limit": 8})
        data = get(url)
        record = {"category": category, "query": query, "searched_at": "2026-10-28", "search_url": url, "candidates": data.get("skills", [])}
    record["selected"] = record["candidates"]
    record["selection_basis"] = "All returned candidates are downloaded for review. Downloading is not endorsement or permission to redistribute."
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2), encoding="utf-8", newline="\n")
    return record


def download(item):
    repo = item["source"]
    name = item.get("skillId") or item["name"]
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", repo) or not re.fullmatch(r"[\w.-]+", name):
        return {"repository": repo, "name": name, "status": "invalid-source-identifier"}
    target = WORK / "snapshots" / repo.replace("/", "--") / name
    record_path = target.parent / f"{name}.snapshot.json"
    if record_path.exists():
        return json.loads(record_path.read_text(encoding="utf-8"))
    url = f"https://skills.sh/api/download/{repo}/{name}"
    try:
        payload = get(url)
        target.mkdir(parents=True, exist_ok=True)
        digests = {}
        for file in payload.get("files", []):
            name_in_archive = file.get("path", "")
            path = PurePosixPath(name_in_archive)
            if not name_in_archive or path.is_absolute() or ".." in path.parts or ":" in name_in_archive or "\\" in name_in_archive:
                raise ValueError("Unsafe source snapshot path")
            destination = target.joinpath(*path.parts)
            content = file.get("contents", file.get("content", ""))
            content = content.encode("utf-8") if isinstance(content, str) else bytes(content)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
            digests[name_in_archive] = hashlib.sha256(content).hexdigest()
        candidates = sorted(target.rglob("SKILL.md"), key=lambda p: len(p.parts))
        if not candidates:
            raise ValueError("No SKILL.md in returned snapshot")
        entrypoint = candidates[0]
        metadata = yaml.safe_load(entrypoint.read_text(encoding="utf-8-sig").split("---", 2)[1])
        record = {"repository": repo, "name": name, "snapshot_hash": payload.get("hash"), "source_url": f"https://github.com/{repo}", "download_url": url, "staged": str(entrypoint.parent), "metadata": metadata, "file_sha256": digests, "status": "downloaded-for-review"}
        record_path.write_text(json.dumps(record, indent=2, default=str), encoding="utf-8", newline="\n")
        return record
    except Exception as error:
        return {"repository": repo, "name": name, "download_url": url, "status": "download-unavailable", "error": str(error)}


def license_for(repo):
    output = WORK / "licenses" / (repo.replace("/", "--") + ".json")
    if output.exists():
        return json.loads(output.read_text(encoding="utf-8"))
    result = subprocess.run(["gh", "api", f"repos/{repo}/license"], capture_output=True, text=True, encoding="utf-8", timeout=90)
    record = {"repository": repo, "status": "not-supplied"}
    if result.returncode == 0:
        data = json.loads(result.stdout)
        record.update({"status": "supplied", "path": data.get("path"), "sha": data.get("sha"), "license": data.get("license"), "text": base64.b64decode(data.get("content", "")).decode("utf-8", errors="replace")})
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2), encoding="utf-8", newline="\n")
    return record


if __name__ == "__main__":
    legacy = json.loads((WORK / "legacy-catalog.json").read_text(encoding="utf-8"))
    categories = sorted({s["metadata"]["category"] for s in legacy})
    searches, failures = [], []
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(search, category): category for category in categories}
        for future in as_completed(futures):
            category = futures[future]
            try:
                searches.append(future.result())
            except Exception as error:
                failures.append({"category": category, "error": str(error)})
    items = {(i["source"], i.get("skillId") or i["name"]): i for r in searches for i in r["candidates"] if i.get("source")}
    print(f"Searched {len(searches)}/{len(categories)} categories; downloading all {len(items)} distinct candidates", flush=True)
    downloads = []
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = [pool.submit(download, item) for item in items.values()]
        for number, future in enumerate(as_completed(futures), 1):
            downloads.append(future.result())
            if number % 25 == 0 or number == len(futures):
                print(f"Downloaded/reviewed {number}/{len(futures)} candidate responses", flush=True)
    repositories = sorted({r["repository"] for r in downloads if r["status"] == "downloaded-for-review"})
    licenses = []
    with ThreadPoolExecutor(max_workers=5) as pool:
        for record in pool.map(license_for, repositories):
            licenses.append(record)
    result = {"searched_at": "2026-10-28", "searches": searches, "downloads": downloads, "licenses": licenses, "failures": failures}
    (WORK / "candidates.json").write_text(json.dumps(result, indent=2, ensure_ascii=False, default=str), encoding="utf-8", newline="\n")
    print(f"Complete: {sum(r['status'] == 'downloaded-for-review' for r in downloads)} downloaded snapshots; {len(failures)} search failures", flush=True)
