"""Download pinned comparator data without installing or executing its helpers."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "benchmarks/comparison/references.json"
DESTINATION = ROOT / ".work/benchmark-v2/sources"


def git(arguments, cwd, *, stdin=None):
    environment = os.environ.copy()
    environment["GIT_TERMINAL_PROMPT"] = "0"
    result = subprocess.run(["git", *arguments], cwd=cwd, input=stdin, capture_output=True,
                            text=True, encoding="utf-8", errors="replace", env=environment, timeout=300)
    if result.returncode:
        raise RuntimeError(result.stderr[-2500:])
    return result.stdout.strip()


def download(group):
    repo, entries, record_only = group
    assert re.fullmatch(r"[\w.-]+/[\w.-]+", repo)
    revisions = {e["revision"] for e in entries}
    assert len(revisions) == 1
    revision = revisions.pop()
    assert re.fullmatch(r"[0-9a-f]{40}", revision)
    destination = DESTINATION / repo.replace("/", "--")
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        if record_only:
            raise FileNotFoundError(destination)
        git(["clone", "--depth=1", "--filter=blob:none", "--no-checkout", f"https://github.com/{repo}.git", str(destination)], ROOT)
    else:
        actual = git(["remote", "get-url", "origin"], destination)
        assert actual == f"https://github.com/{repo}.git", (repo, actual)
    paths = sorted({str(PurePosixPath(e["entrypoint"]).parent) for e in entries})
    assert all(".." not in PurePosixPath(p).parts and not PurePosixPath(p).is_absolute() for p in paths)
    if not record_only:
        git(["sparse-checkout", "init", "--cone"], destination)
        git(["sparse-checkout", "set", "--stdin"], destination, stdin="\n".join(paths)+"\n")
        git(["fetch", "--depth=1", "origin", revision], destination)
        git(["checkout", "--detach", revision], destination)
    assert git(["rev-parse", "HEAD"], destination) == revision
    summaries = []
    for entry in entries:
        folder = destination / PurePosixPath(entry["entrypoint"]).parent
        digests = {}
        for path in sorted(folder.rglob("*")):
            if path.is_file() and not any(part in {".git", "__pycache__"} for part in path.relative_to(folder).parts):
                assert not path.is_symlink(), path
                digests[path.relative_to(folder).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        text = (destination / entry["entrypoint"]).read_text(encoding="utf-8")
        import yaml
        frontmatter = yaml.safe_load(text.split("---", 2)[1]) if text.startswith("---") else {}
        summaries.append({**entry, "entrypoint_sha256": digests["SKILL.md"],
                          "entrypoint_license": frontmatter.get("license", "Not declared here; preserve repository and local notices"),
                          "local_snapshot": destination.relative_to(ROOT).as_posix(),
                          "support_file_count": len(digests)-1, "resource_sha256": digests,
                          "entrypoint_characters": len(text), "helpers_executed": False})
    print(f"Pinned {repo}: {len(entries)} category mappings", flush=True)
    return summaries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=4, choices=range(1,5))
    parser.add_argument("--record-only", action="store_true", help="Verify and fingerprint already pinned local sources without network or checkout changes")
    args = parser.parse_args()
    groups = {}
    for entry in json.loads(REFERENCES.read_text(encoding="utf-8")):
        groups.setdefault(entry["repo"], []).append(entry)
    records = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for batch in pool.map(download, [(repo,entries,args.record_only) for repo,entries in groups.items()]):
            records.extend(batch)
    output = ROOT / "web-results/comparison/source-snapshots.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(sorted(records, key=lambda e:e["category"]),indent=2)+"\n",encoding="utf-8")
    print(f"Recorded {len(records)} category mappings. No reference helpers executed.")


if __name__ == "__main__":
    main()
