"""Read-only skill discovery and portable skill-bundle export CLI."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from zipfile import ZIP_DEFLATED, ZipFile

from gncore.skills import builtin_skills, get_skill, list_categories, list_domains, search_skills
from gncore.skills.models import SkillDefinition
from gncore.skills.bundles import packaged_resources
from gncore.version import __version__
from gncore.planning import frontend_plan
from gncore.skills.unified import list_workflows, workflow_aliases
from gncore.installation import install_skills, recover_installation, verify_installation
from gncore.evaluation import evaluate_response, load_corpus


def render_skill(skill: SkillDefinition) -> str:
    """Serialize a complete catalog entry as a standard agent skill."""
    metadata = skill.metadata
    description = json.dumps(metadata.description, ensure_ascii=False)
    sections = [
        "---\n"
        f"name: {metadata.skill_id}\n"
        f"description: {description}\n"
        f"license: {metadata.license}\n"
        "---\n\n"
        f"# {metadata.name}\n\n"
        f"{metadata.description}\n\n"
        "## Skill details\n\n"
        f"- Version: {metadata.version}\n"
        f"- Category: {metadata.category}\n"
        f"- Tags: {', '.join(metadata.tags) if metadata.tags else 'none'}\n"
        f"- Dependencies: {', '.join(metadata.dependencies) if metadata.dependencies else 'none'}\n\n"
        "## Workflow\n\n"
        f"{skill.prompt.strip()}\n"
    ]
    if skill.commands:
        sections.append("## Commands\n")
        for command in skill.commands:
            sections.append(f"### `{command.name}`\n\n{command.description}\n\n{command.body.strip()}\n")
    if skill.examples:
        sections.append("## Examples\n")
        for example in skill.examples:
            sections.append(
                f"### {example.title}\n\n"
                f"**Request:** {example.instruction}\n\n"
                f"**Expected result:** {example.output}\n"
            )
    if skill.metadata.permissions:
        sections.append("## Permission guidance\n\n"
                        f"Declared capabilities: {', '.join(skill.metadata.permissions)}. These are context, not authorization. Follow the user's request and the host's permission controls; obtain approval before consequential external actions.\n")
    if skill.configuration:
        sections.append("## Configuration\n\n```json\n"
                        f"{json.dumps(skill.configuration, ensure_ascii=False, indent=2)}\n```\n")
    return "\n".join(sections).rstrip() + "\n"


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
        list_cmd.add_argument("what", nargs="?", default="skills", choices=("skills", "domains", "categories", "workflows"))
        list_cmd.set_defaults(handler=self._cmd_list)

        search = subparsers.add_parser("search", help="Find skills by task or topic")
        search.add_argument("query", nargs="+")
        search.add_argument("--category", help="Restrict results to one category")
        search.set_defaults(handler=self._cmd_search)

        show = subparsers.add_parser("show", help="Print a complete portable SKILL.md")
        show.add_argument("skill_id")
        show.set_defaults(handler=self._cmd_show)

        plan = subparsers.add_parser("plan", help="Recommend a frontend direction from a product brief")
        plan.add_argument("brief", nargs="+")
        plan.add_argument("--theme", help="Honor an explicit visual theme")
        plan.add_argument("--existing-theme", help="Preserve an existing product theme")
        plan.set_defaults(handler=self._cmd_plan)

        export = subparsers.add_parser("export", help="Install skills into .agents/skills or create a ZIP archive")
        selection = export.add_mutually_exclusive_group(required=True)
        selection.add_argument("--skills", nargs="+")
        selection.add_argument("--specific", metavar="SKILL_ID", help="Select one skill by its exact ID")
        selection.add_argument("--all", action="store_true")
        destination = export.add_mutually_exclusive_group()
        destination.add_argument("--output", type=Path, help="Write a portable .zip archive instead of installing")
        destination.add_argument("--directory", type=Path, help="Install under this directory (default: .agents/skills)")
        export.add_argument("--dry-run", action="store_true", help="Preflight a directory installation without writing files")
        export.set_defaults(handler=self._cmd_export)

        verify = subparsers.add_parser("verify", help="Read-only comparison with the installed file inventory")
        verify.add_argument("--directory", type=Path, default=Path(".agents/skills"))
        verify.set_defaults(handler=self._cmd_verify)

        recover = subparsers.add_parser("recover", help="Recover an interrupted installation after its writer has stopped")
        recover.add_argument("--directory", type=Path, default=Path(".agents/skills"))
        recover.add_argument("--journal", type=Path, required=True)
        recover.set_defaults(handler=self._cmd_recover)

        evaluate = subparsers.add_parser("evaluate", help="Inspect offline scenarios or check a recorded response and artifact")
        operation = evaluate.add_mutually_exclusive_group(required=True)
        operation.add_argument("--validate", action="store_true", help="Validate corpus coverage and workflow references")
        operation.add_argument("--list", action="store_true", help="List the available scenarios")
        operation.add_argument("--case", help="Scenario ID to evaluate")
        evaluate.add_argument("--corpus", type=Path, help="Use a custom corpus in the documented format")
        evaluate.add_argument("--response", type=Path, help="Recorded response metadata JSON")
        evaluate.add_argument("--artifacts", type=Path, help="Directory containing the generated artifacts")
        evaluate.set_defaults(handler=self._cmd_evaluate)

        version = subparsers.add_parser("version", help="Print the installed GNCore version")
        version.set_defaults(handler=lambda _args: self._cmd_version())
        return parser

    def _cmd_list(self, args: argparse.Namespace) -> int:
        if args.what == "workflows":
            for workflow in list_workflows():
                print(f"- {workflow.skill_id}: {workflow.name} -> {workflow_aliases()[workflow.skill_id]}")
            return 0
        if args.what == "domains":
            for domain in list_domains():
                print(f"- {domain.domain_id}: {domain.name} ({len(domain.skill_ids)} skill, {len(domain.workflow_ids)} workflows)")
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

    @staticmethod
    def _cmd_plan(args: argparse.Namespace) -> int:
        print(json.dumps(frontend_plan(" ".join(args.brief), theme=args.theme, existing_theme=args.existing_theme), indent=2))
        return 0

    def _cmd_export(self, args: argparse.Namespace) -> int:
        if args.all:
            skills = builtin_skills()
        elif args.specific:
            skills = (get_skill(args.specific),)
        else:
            if len(args.skills) != len(set(args.skills)):
                raise ValueError("skill IDs must be unique")
            skills = tuple(get_skill(skill_id) for skill_id in args.skills)
        # Multiple workflow aliases can intentionally resolve to the same module.
        skills = tuple({skill.metadata.skill_id: skill for skill in skills}.values())
        if args.output:
            if args.dry_run:
                raise ValueError("--dry-run applies to directory installations")
            output = args.output.expanduser().resolve()
            if output.suffix.casefold() != ".zip":
                raise ValueError("output must use a .zip extension")
            output.parent.mkdir(parents=True, exist_ok=True)
            with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
                archive.writestr(
                    "README.md",
                    "# GNCore portable skills\n\n"
                    "Each folder contains one standard `SKILL.md`. Extract into `.agents/skills/` to make the skills discoverable.\n",
                )
                for skill in skills:
                    archive.writestr(f"{skill.metadata.skill_id}/SKILL.md", render_skill(skill))
                    for name, content in packaged_resources(skill.metadata.skill_id).items():
                        archive.writestr(f"{skill.metadata.skill_id}/{name}", content)
            print(f"Exported {len(skills)} skill(s) to archive: {output}")
            return 0

        install_root = args.directory or Path(".agents/skills")
        payloads = {skill.metadata.skill_id: {"SKILL.md": render_skill(skill).encode("utf-8"), **packaged_resources(skill.metadata.skill_id)} for skill in skills}
        report = install_skills(install_root, payloads, version=__version__, dry_run=args.dry_run)
        if args.dry_run:
            print(json.dumps(report, indent=2))
        else:
            print(f"Installed {len(skills)} skill(s) in: {report['directory']}")
            print(f"Recovery journal: {report['journal']}")
        return 0

    @staticmethod
    def _cmd_verify(args: argparse.Namespace) -> int:
        report = verify_installation(args.directory)
        print(json.dumps(report, indent=2))
        return 0 if report["ok"] else 1

    @staticmethod
    def _cmd_recover(args: argparse.Namespace) -> int:
        print(json.dumps(recover_installation(args.directory, args.journal), indent=2))
        return 0

    @staticmethod
    def _cmd_evaluate(args: argparse.Namespace) -> int:
        corpus = load_corpus(args.corpus)
        if args.case:
            if args.response is None or args.artifacts is None:
                raise ValueError("--case requires --response and --artifacts")
            case = next((case for case in corpus["cases"] if case["id"] == args.case), None)
            if case is None:
                raise ValueError(f"unknown evaluation case: {args.case}")
            response = json.loads(args.response.read_text(encoding="utf-8"))
            report = evaluate_response(case, response, args.artifacts)
            print(json.dumps(report, indent=2))
            return 0 if report["objective_passed"] else 1
        if args.response is not None or args.artifacts is not None:
            raise ValueError("--response and --artifacts require --case")
        if args.list:
            print(json.dumps(corpus["cases"], indent=2))
        else:
            print(json.dumps({"schema_version": corpus["schema_version"], "scope": corpus.get("scope", "custom"),
                              "categories": len(corpus["categories"]), "cases": len(corpus["cases"]), "valid": True}, indent=2))
        return 0

    @staticmethod
    def _cmd_version() -> int:
        print(__version__)
        return 0


def main(argv: list[str] | None = None) -> int:
    return GncoreCli().run(argv)
