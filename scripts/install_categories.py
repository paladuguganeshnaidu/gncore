"""Install the complete category catalog; optionally back up managed old folders."""

import argparse
import json
from pathlib import Path
import shutil
import sys
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from gncore import GncoreCli
from gncore.skills.backend import LEGACY_BACKEND_IDS
from gncore.skills.frontend import LEGACY_FRONTEND_IDS
from gncore.skills.unified import unified_manifest, workflow_aliases


def main():
    parser = argparse.ArgumentParser(description="Install GNCore category skills in this project")
    parser.add_argument("--migrate-managed", action="store_true", help="Back up managed legacy skill folders before installing")
    args = parser.parse_args()
    workspace = Path.cwd().resolve()
    installed = (workspace / ".agents/skills").resolve()
    if not installed.is_relative_to(workspace):
        raise ValueError("Project skills directory escapes the current workspace")
    backup = (workspace / ".work/skill-install-backups" / uuid4().hex).resolve()
    names = set(workflow_aliases()) | set(LEGACY_FRONTEND_IDS) | set(LEGACY_BACKEND_IDS)
    count = 0
    if args.migrate_managed:
        for name in sorted(names):
            source = (installed / name).resolve()
            entrypoint = source / "SKILL.md"
            if not entrypoint.is_file() or "GNCore" not in entrypoint.read_text(encoding="utf-8"):
                continue
            destination = (backup / name).resolve()
            if not source.is_relative_to(installed) or not destination.is_relative_to(backup) or not backup.is_relative_to(workspace):
                raise ValueError("Migration path escaped its intended root")
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))
            count += 1
        lock_path = workspace / "skills-lock.json"
        if lock_path.exists():
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
            lock["skills"] = {name: data for name, data in lock.get("skills", {}).items() if name not in names}
            lock_path.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8", newline="\n")
    primary = {entry["id"] for entry in unified_manifest()}
    for name in primary:
        file = installed / name / "SKILL.md"
        if file.exists() and "GNCore" not in file.read_text(encoding="utf-8"):
            raise ValueError(f"Unmanaged skill would be overwritten: {name}")
    result = GncoreCli().run(["export", "--all", "--directory", str(installed)])
    if count:
        print(f"Backed up {count} managed legacy folders in {backup}")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
