"""Install categories transactionally; preserve unrecognized/custom legacy files."""

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from gncore import builtin_skills, render_skill, __version__
from gncore.installation import install_skills, recover_installation
from gncore.skills.bundles import bundle_resources, packaged_resources
from gncore.skills.library import legacy_skills


def legacy_payloads():
    """Only exact known exports can be migrated automatically.

    Historical installations differing from this version stay in place for
    review, even if their content happens to contain the word GNCore.
    """
    result = {}
    for skill in legacy_skills():
        name = skill.metadata.skill_id
        resources = bundle_resources("frontend_data", name) or bundle_resources("backend_data", name)
        result[name] = {"SKILL.md": render_skill(skill).encode("utf-8"), **resources}
    return result


def main():
    parser = argparse.ArgumentParser(description="Install GNCore category skills in this project")
    parser.add_argument("--migrate-managed", action="store_true", help="Migrate byte-identical known legacy exports, retaining a full backup")
    parser.add_argument("--dry-run", action="store_true", help="Report changes and conflicts without writing files")
    parser.add_argument("--recover", type=Path, metavar="JOURNAL", help="Recover an interrupted transaction after its writer has stopped")
    args = parser.parse_args()
    installed = Path.cwd() / ".agents/skills"
    try:
        if args.recover:
            if args.dry_run or args.migrate_managed:
                raise ValueError("recovery cannot be combined with installation options")
            result = recover_installation(installed, args.recover)
        else:
            payloads = {s.metadata.skill_id: {"SKILL.md": render_skill(s).encode("utf-8"), **packaged_resources(s.metadata.skill_id)} for s in builtin_skills()}
            result = install_skills(installed, payloads, version=__version__, dry_run=args.dry_run,
                                    legacy=legacy_payloads() if args.migrate_managed else None)
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, OSError) as error:
        print(f"gncore: error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
