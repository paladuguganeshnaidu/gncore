"""Read-only skill discovery and portable skill-bundle export CLI."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from zipfile import ZIP_DEFLATED, ZipFile

from gncore.skills import builtin_skills, get_skill, list_categories, list_domains, search_skills
from gncore.skills.models import SkillDefinition
from gncore.version import __version__


def render_skill(skill: SkillDefinition) -> str:
    """Serialize one catalog entry as a portable SKILL.md file."""
    metadata = skill.metadata
    description = json.dumps(metadata.description, ensure_ascii=False)
    return (
        "---\n"
        f"name: {metadata.skill_id}\n"
        f"description: {description}\n"
        "---\n\n"
        f"# {metadata.name}\n\n"
        f"{metadata.description}\n\n"
        f"{skill.prompt.strip()}\n"
    )


class GncoreCli:
    """Expose catalog commands without detecting or modifying AI applications."""

    def run(self, argv: list[str] | None = None) -> int:
        parser = self._build_parser()
        try:
            args = parser.parse_args(argv)
        except SystemExit as error:
            return int(error.code)
        if args.command is None:
            parser.print_help()
            return 0
        try:
            return args.handler(args)
        except (KeyError, ValueError, OSError) as error:
            print(f"gncore: error: {error}", file=sys.stderr)
            return 2

    def _build_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            prog="gncore",
            description="Search, inspect, and export portable AI skills.",
        )
        subparsers = parser.add_subparsers(dest="command")

        list_cmd = subparsers.add_parser("list", help="List skills, domains, or categories")
        list_cmd.add_argument("what", nargs="?", default="skills", choices=("skills", "domains", "categories"))
        list_cmd.set_defaults(handler=self._cmd_list)

        search = subparsers.add_parser("search", help="Find skills by task or topic")
        search.add_argument("query", nargs="+")
        search.add_argument("--category", help="Restrict results to one category")
        search.set_defaults(handler=self._cmd_search)

        show = subparsers.add_parser("show", help="Print a complete portable SKILL.md")
        show.add_argument("skill_id")
        show.set_defaults(handler=self._cmd_show)

        export = subparsers.add_parser("export", help="Write selected skills to a portable ZIP archive")
        selection = export.add_mutually_exclusive_group(required=True)
        selection.add_argument("--skills", nargs="+")
        selection.add_argument("--all", action="store_true")
        export.add_argument("--output", type=Path, required=True, help="Destination .zip file")
        export.set_defaults(handler=self._cmd_export)

        version = subparsers.add_parser("version", help="Print the installed GNCore version")
        version.set_defaults(handler=lambda _args: self._cmd_version())
        return parser

    def _cmd_list(self, args: argparse.Namespace) -> int:
        if args.what == "domains":
            for domain in list_domains():
                print(f"- {domain.domain_id}: {domain.name} ({len(domain.skill_ids)} skills)")
                print(f"  {domain.description}")
            return 0
        if args.what == "categories":
            for category in list_categories():
                print(f"- {category}")
            return 0
        for skill in builtin_skills():
            metadata = skill.metadata
            print(f"- {metadata.skill_id}: {metadata.name} [{metadata.category}]")
        return 0

    def _cmd_search(self, args: argparse.Namespace) -> int:
        matches = search_skills(" ".join(args.query), category=args.category)
        if not matches:
            print(f"No skills found for: {' '.join(args.query)}")
            return 0
        for skill in matches:
            metadata = skill.metadata
            print(f"- {metadata.skill_id}: {metadata.name} [{metadata.category}]")
            print(f"  {metadata.description}")
        return 0

    def _cmd_show(self, args: argparse.Namespace) -> int:
        print(render_skill(get_skill(args.skill_id)), end="")
        return 0

    def _cmd_export(self, args: argparse.Namespace) -> int:
        skills = builtin_skills() if args.all else tuple(get_skill(skill_id) for skill_id in args.skills)
        skill_ids = [skill.metadata.skill_id for skill in skills]
        if len(skill_ids) != len(set(skill_ids)):
            raise ValueError("skill IDs must be unique")
        output = args.output.expanduser().resolve()
        if output.suffix.casefold() != ".zip":
            raise ValueError("output must use a .zip extension")
        output.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
            archive.writestr(
                "README.md",
                "# GNCore portable skills\n\n"
                "Each folder contains one standard `SKILL.md`. Copy only the skills you want into an assistant's documented skills directory. "
                "GNCore does not detect, configure, or modify AI applications.\n",
            )
            for skill in skills:
                archive.writestr(f"{skill.metadata.skill_id}/SKILL.md", render_skill(skill))
        print(f"Exported {len(skills)} skill(s): {output}")
        return 0

    @staticmethod
    def _cmd_version() -> int:
        print(__version__)
        return 0


def main(argv: list[str] | None = None) -> int:
    return GncoreCli().run(argv)
