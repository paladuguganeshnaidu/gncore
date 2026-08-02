"""Command-line interface for GNCore."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from gncore.core.managers import AdapterManager, BackupManager, ConfigurationManager, DiagnosticsManager, Installer, RollbackManager, SkillManager, Validator, VersionManager
from gncore.utilities.logging import setup_logging


class GncoreCli:
    def __init__(self) -> None:
        self.adapter_manager = AdapterManager()
        self.skill_manager = SkillManager()
        self.configuration_manager = ConfigurationManager()
        self.validator = Validator(self.adapter_manager)
        self.installer = Installer(self.adapter_manager, self.skill_manager, self.configuration_manager, self.validator)
        self.backup_manager = BackupManager(self.adapter_manager)
        self.rollback_manager = RollbackManager(self.adapter_manager)
        self.diagnostics_manager = DiagnosticsManager(self.adapter_manager, self.validator)
        self.version_manager = VersionManager()

    def run(self, argv: list[str] | None = None) -> int:
        setup_logging()
        parser = self._build_parser()
        args = parser.parse_args(argv)
        if not hasattr(args, "handler"):
            parser.print_help()
            return 0
        return args.handler(args)

    def _build_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(prog="gncore", description="Universal AI Skill Installer")
        subparsers = parser.add_subparsers(dest="command")

        activate = subparsers.add_parser("activate", help="Install GNCore skills into selected applications")
        self._add_application_selection(activate)
        activate.add_argument("--skills", nargs="*", default=None)
        activate.set_defaults(handler=self._cmd_activate)

        deactivate = subparsers.add_parser("deactivate", help="Remove GNCore from selected applications")
        self._add_application_selection(deactivate)
        deactivate.set_defaults(handler=self._cmd_deactivate)

        update = subparsers.add_parser("update", help="Reinstall the current GNCore bundle")
        self._add_application_selection(update)
        update.add_argument("--skills", nargs="*", default=None)
        update.set_defaults(handler=self._cmd_update)

        doctor = subparsers.add_parser("doctor", help="Check environment and installation health")
        doctor.set_defaults(handler=self._cmd_doctor)

        list_cmd = subparsers.add_parser("list", help="List supported applications or built-in skills")
        list_cmd.add_argument("what", nargs="?", default="apps", choices=["apps", "skills", "installed"])
        list_cmd.set_defaults(handler=self._cmd_list)

        install = subparsers.add_parser("install", help="Install a single skill or a skill set")
        install.add_argument("skill_ids", nargs="*", default=None)
        self._add_application_selection(install)
        install.set_defaults(handler=self._cmd_install)

        uninstall = subparsers.add_parser("uninstall", help="Uninstall from selected applications")
        self._add_application_selection(uninstall)
        uninstall.set_defaults(handler=self._cmd_uninstall)

        backup = subparsers.add_parser("backup", help="Create a zip archive of installed GNCore bundles")
        backup.add_argument("--output", type=Path, default=None)
        backup.set_defaults(handler=self._cmd_backup)

        restore = subparsers.add_parser("restore", help="Restore a GNCore backup archive")
        restore.add_argument("archive", type=Path)
        restore.set_defaults(handler=self._cmd_restore)

        validate = subparsers.add_parser("validate", help="Validate installed application bundles")
        self._add_application_selection(validate)
        validate.set_defaults(handler=self._cmd_validate)

        version = subparsers.add_parser("version", help="Print the installed GNCore version")
        version.set_defaults(handler=self._cmd_version)

        return parser

    def _add_application_selection(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--all", action="store_true", help="Target all supported applications")
        parser.add_argument("--apps", nargs="*", default=None, help="Explicit application keys to target")

    def _select_applications(self, args: argparse.Namespace) -> tuple[str, ...]:
        if args.apps:
            return tuple(args.apps)
        if args.all:
            return tuple(adapter.key for adapter in self.adapter_manager.adapters)

        detected = self.adapter_manager.detected(Path.cwd())
        if not detected:
            return tuple(adapter.key for adapter in self.adapter_manager.adapters)

        print("Detected Applications")
        for index, adapter in enumerate(detected, start=1):
            print(f"{index}. {adapter.name}")
        print(f"{len(detected) + 1}. Install Everywhere")

        if not sys.stdin.isatty():
            return tuple(adapter.key for adapter in detected)

        choice = input("Select applications: ").strip()
        if not choice or choice == str(len(detected) + 1):
            return tuple(adapter.key for adapter in self.adapter_manager.adapters)

        selected_keys: list[str] = []
        for raw_index in choice.replace(",", " ").split():
            index = int(raw_index)
            if 1 <= index <= len(detected):
                selected_keys.append(detected[index - 1].key)
        return tuple(dict.fromkeys(selected_keys))

    def _cmd_activate(self, args: argparse.Namespace) -> int:
        application_keys = self._select_applications(args)
        reports = self.installer.activate(application_keys, Path.cwd(), args.skills)
        self._print_reports("Activated", reports)
        return 0

    def _cmd_deactivate(self, args: argparse.Namespace) -> int:
        application_keys = self._select_applications(args)
        self.installer.uninstall(application_keys, Path.cwd())
        print("Deactivated GNCore for:")
        for key in application_keys:
            print(f"- {key}")
        return 0

    def _cmd_update(self, args: argparse.Namespace) -> int:
        application_keys = self._select_applications(args)
        reports = self.installer.update(application_keys, Path.cwd(), args.skills)
        self._print_reports("Updated", reports)
        return 0

    def _cmd_doctor(self, args: argparse.Namespace) -> int:
        report = self.diagnostics_manager.report(Path.cwd())
        print("GNCore Diagnostics")
        for application in report["applications"]:
            status = "detected" if application["detected"] else "missing"
            writable = "writable" if application["writable"] else "read-only"
            print(f"- {application['name']}: {status}, {writable}, root={application['config_root']}")
        return 0

    def _cmd_list(self, args: argparse.Namespace) -> int:
        if args.what == "skills":
            for skill in self.skill_manager.skills:
                print(f"- {skill.metadata.skill_id}: {skill.metadata.name} ({skill.metadata.version})")
            return 0
        if args.what == "installed":
            config = self.configuration_manager.load()
            print("Installed Applications:")
            for key in config.selected_applications:
                print(f"- {key}")
            return 0

        for summary in self.adapter_manager.summaries(Path.cwd()):
            state = "detected" if summary.detected else "not detected"
            print(f"- {summary.name}: {state} at {summary.config_root}")
        return 0

    def _cmd_install(self, args: argparse.Namespace) -> int:
        application_keys = self._select_applications(args)
        skill_ids = tuple(args.skill_ids) if args.skill_ids else None
        reports = self.installer.install(application_keys, skill_ids, Path.cwd())
        self._print_reports("Installed", reports)
        return 0

    def _cmd_uninstall(self, args: argparse.Namespace) -> int:
        application_keys = self._select_applications(args)
        self.installer.uninstall(application_keys, Path.cwd())
        print("Uninstalled GNCore from:")
        for key in application_keys:
            print(f"- {key}")
        return 0

    def _cmd_backup(self, args: argparse.Namespace) -> int:
        archive = self.backup_manager.create(args.output, Path.cwd())
        print(f"Backup created: {archive.path}")
        return 0

    def _cmd_restore(self, args: argparse.Namespace) -> int:
        self.rollback_manager.restore(args.archive, Path.cwd())
        print(f"Restored: {args.archive}")
        return 0

    def _cmd_validate(self, args: argparse.Namespace) -> int:
        application_keys = self._select_applications(args)
        reports = self.validator.validate(application_keys, Path.cwd())
        for report in reports:
            print(f"{report.application}: {'valid' if report.valid else 'invalid'}")
            for issue in report.issues:
                print(f"- {issue.severity}: {issue.message}")
        if any(not report.valid for report in reports):
            return 1
        return 0

    def _cmd_version(self, args: argparse.Namespace) -> int:
        print(self.version_manager.show())
        return 0

    def _print_reports(self, label: str, reports) -> None:
        for report in reports:
            status = "verified" if report.verified else "pending"
            print(f"{label} {report.application} ({status})")
            for skill_id in report.installed:
                print(f"- {skill_id}")
            for issue in report.details:
                print(f"! {issue}")


def main(argv: list[str] | None = None) -> int:
    return GncoreCli().run(argv)