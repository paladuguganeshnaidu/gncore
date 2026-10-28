"""Stage verified upstream skill folders using the bundled installer helpers.

Run after inspect_frontend_sources.py. Temporary checkouts and downloaded
instructions are data; this script never executes their scripts or hooks.
"""

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def stage(record):
    selected = {}
    for requested in record["requested"]:
        matches = [s for s in record["skills"] if s["name"] == requested]
        if matches:
            selected[requested] = matches[0]["path"].removesuffix("/SKILL.md")
    paths = list(selected.values())
    destination = ROOT / ".work" / "imports" / record["repo"].replace("/", "--")
    result = subprocess.run([sys.executable, str(helper), "--repo", record["repo"], "--ref", record["revision"], "--method", "download", "--path", *paths, "--dest", str(destination)], capture_output=True, text=True, timeout=300)
    if result.returncode:
        raise RuntimeError(result.stderr)
    licenses = {}
    for path in record["licenses"]:
        if "/" not in path:
            url = f'https://raw.githubusercontent.com/{record["repo"]}/{record["revision"]}/{path}'
            with urllib.request.urlopen(url, timeout=60) as response:
                licenses[path] = response.read().decode("utf-8")
    if record["repo"] == "vercel-labs/agent-skills":
        url = f'https://raw.githubusercontent.com/{record["repo"]}/{record["revision"]}/README.md'
        with urllib.request.urlopen(url, timeout=60) as response:
            licenses["REPOSITORY-README.md"] = response.read().decode("utf-8")
    record["root_license_text"] = licenses
    record["staged"] = {name: str(destination / Path(path).name) for name, path in selected.items()}
    print(f'{record["repo"]}: {len(selected)}/{len(record["requested"])} requested skill folders staged', flush=True)
    return record


if __name__ == "__main__":
    helper = Path.home() / ".codex/skills/.system/skill-installer/scripts/install-skill-from-github.py"
    sys.path.insert(0, str(helper.parent))
    records = json.loads((ROOT / ".work/upstream-inventory.json").read_text(encoding="utf-8"))
    with ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(stage, records))
    (ROOT / ".work/staged-inventory.json").write_text(json.dumps(records, indent=2), encoding="utf-8")
