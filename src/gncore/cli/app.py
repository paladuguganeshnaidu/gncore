"""Command-line interface for GNCore."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from gncore.config import ConfigError
from gncore.core.executor import ExecutionEngine, ExecutionResult
from gncore.core.prompt import PromptBuilder
from gncore.core.stages import StageDefinition, StageRegistry, default_stage_registry
from gncore.core.workflow import StagePreparation, StageWorkflow
from gncore.providers.catalog import discover_providers, provider_by_name
from gncore.providers.credentials import CredentialError
from gncore.providers.factory import ProviderFactory
from gncore.runtime import GncoreRuntime, ProjectValidationError
from gncore.skills.loader import SkillLoader
from gncore.state.manager import ProjectStateManager
from gncore.state.models import ProjectState
from gncore.utils.logging import LoggerFactory


class Ansi:
    """ANSI colors used by the terminal interface."""

    GREEN = "\033[32m"
    RED = "\033[31m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


@dataclass(frozen=True, slots=True)
class CliConfig:
    """User-provided CLI startup values."""

    project_name: str
    project_directory: Path
    provider: str


@dataclass(frozen=True, slots=True)
class CliSelection:
    """A selected stage and project prompt from CLI input."""

    stage_id: int
    user_prompt: str = ""


class GncoreCli:
    """Render and execute GNCore terminal workflows."""

    def __init__(self, registry: StageRegistry | None = None) -> None:
        self.registry = registry or default_stage_registry()
        self.provider_factory = ProviderFactory()
        self.runtime = GncoreRuntime(self.registry)

    def banner(self) -> str:
        """Return the product banner and stage menu."""
        lines = [
            "=================================================",
            f"{Ansi.BOLD}{Ansi.CYAN}GNCore{Ansi.RESET}",
            "AI Software Engineering Framework",
            "=================================================",
            "Project Name:",
            "Project Directory:",
            "Provider:",
            "Choose Stage",
            *self.registry.menu_lines(),
        ]
        return "\n".join(lines)

    def init_project(self, project_dir: Path, project_name: str, provider: str) -> ProjectStateManager:
        """Initialize GNCore files in a project directory."""
        self.runtime.init(project_dir, project_name, provider)
        manager = ProjectStateManager(project_dir)
        LoggerFactory().create(manager.gncore_dir / "logs").info("Initialized GNCore project '%s'", project_name)
        return manager

    def initialize(self, config: CliConfig) -> ProjectStateManager:
        """Initialize the project state directory and log startup."""
        return self.init_project(config.project_directory, config.project_name, config.provider)

    def prepare_stage(self, config: CliConfig, selection: CliSelection) -> StagePreparation:
        """Initialize a project, select a stage, and assemble its prompt."""
        manager = self.initialize(config)
        if selection.user_prompt:
            manager.write_prompt(selection.user_prompt)
        workflow = StageWorkflow(self.registry, manager, SkillLoader(), PromptBuilder())
        return workflow.prepare_stage(selection.stage_id, manager.prompt())

    def execute_stage(self, config: CliConfig, selection: CliSelection) -> ExecutionResult:
        """Initialize a project and execute one stage with the configured provider."""
        manager = self.initialize(config)
        if selection.user_prompt:
            manager.write_prompt(selection.user_prompt)
        provider = self.provider_factory.create(config.provider)
        engine = ExecutionEngine(self.registry, manager, SkillLoader(), PromptBuilder(), provider)
        return engine.execute(selection.stage_id)

    def run(self, argv: list[str] | None = None) -> None:
        """Run the CLI, dispatching to modern subcommands or legacy stage flags."""
        args = self._parse_args(argv)
        try:
            if args.command is None:
                if self._has_legacy_stage_args(args):
                    result = self.execute_stage(self._legacy_config_from_args(args), self._legacy_selection_from_args(args))
                    self._print_execution_result(result)
                    return
                args.parser.print_help()
                return
            handler = getattr(self, f"_cmd_{args.command.replace('-', '_')}")
            handler(args)
        except (ConfigError, CredentialError, ProjectValidationError, ValueError, RuntimeError) as exc:
            print(f"{Ansi.RED}Error:{Ansi.RESET} {exc}", file=sys.stderr)
            raise SystemExit(1) from exc

    def _cmd_init(self, args: argparse.Namespace) -> None:
        project_dir = self._project_dir(args)
        project_name = args.project_name or project_dir.name
        config = self.runtime.init(project_dir, project_name, args.provider)
        print(f"{Ansi.GREEN}Initialized GNCore project at {project_dir / '.gncore'}{Ansi.RESET}")
        print(f"Provider: {config.selected_provider} ({config.provider_kind})")
        print(f"Write requirements in {project_dir / 'prompt.md'}")

    def _cmd_run(self, args: argparse.Namespace) -> None:
        project_dir = self._project_dir(args)
        results = self.runtime.run(project_dir)
        self._print_run_results(results, project_dir)

    def _cmd_dashboard(self, args: argparse.Namespace) -> None:
        project_dir = self._project_dir(args)
        self._run_dashboard(project_dir)

    def _cmd_stage(self, args: argparse.Namespace) -> None:
        project_dir = self._project_dir(args)
        self._run_dashboard(project_dir)

    def _cmd_resume(self, args: argparse.Namespace) -> None:
        project_dir = self._project_dir(args)
        results = self.runtime.resume(project_dir)
        self._print_run_results(results, project_dir)

    def _cmd_doctor(self, args: argparse.Namespace) -> None:
        project_dir = self._project_dir(args)
        issues = self.runtime.doctor(project_dir)
        if not issues:
            print(f"{Ansi.GREEN}OK{Ansi.RESET}: project, config, provider, git, and credentials checks passed")
            return
        print(f"{Ansi.RED}Problems found:{Ansi.RESET}")
        for issue in issues:
            print(f"- {issue.field}: {issue.message}")
        raise SystemExit(1)

    def _cmd_provider(self, args: argparse.Namespace) -> None:
        project_dir = self._project_dir(args)
        command = args.provider_command
        if command == "list":
            self._print_provider_list(project_dir)
            return
        if command == "use":
            config = self.runtime.provider_select(project_dir, args.name)
            print(f"Selected provider: {config.selected_provider} ({config.provider_kind})")
            return
        if command == "detect":
            config = self.runtime.provider_detect(project_dir)
            print(f"Detected provider: {config.selected_provider} ({config.provider_kind})")
            return
        if command == "health":
            name = args.name
            if name is None:
                name = self.runtime.load_config(project_dir).selected_provider
            provider = provider_by_name(name)
            status = provider.create().health()
            print(f"{provider.name}: {status.health.value} - {status.message}")
            return
        raise SystemExit("provider subcommand required")

    def _cmd_config(self, args: argparse.Namespace) -> None:
        project_dir = self._project_dir(args)
        command = args.config_command
        if command == "show":
            config = self.runtime.config_show(project_dir)
            print(json.dumps(config.to_dict(), indent=2, sort_keys=True))
            return
        if command == "set":
            config = self.runtime.load_config(project_dir)
            if args.provider:
                config.update_provider(provider_by_name(args.provider))
            if args.project_name:
                config.project_name = args.project_name
            self.runtime.write_config(project_dir, config)
            print(json.dumps(config.to_dict(), indent=2, sort_keys=True))
            return
        if command == "validate":
            issues = self.runtime.config_validate(project_dir)
            if not issues:
                print(f"{Ansi.GREEN}OK{Ansi.RESET}: config is valid")
                return
            for issue in issues:
                print(f"- {issue.field}: {issue.message}")
            raise SystemExit(1)
        raise SystemExit("config subcommand required")

    def _cmd_auth(self, args: argparse.Namespace) -> None:
        command = args.auth_command
        if command == "login":
            token = args.token or input("Token: ").strip()
            self.runtime.auth_set(args.provider, token)
            print(f"Stored credential for {args.provider}")
            return
        if command == "logout":
            self.runtime.auth_delete(args.provider)
            print(f"Removed credential for {args.provider}")
            return
        if command == "status":
            token = self.runtime.auth_get(args.provider)
            if token:
                print(f"{args.provider}: credential available")
            else:
                print(f"{args.provider}: no credential found")
                raise SystemExit(1)
            return
        raise SystemExit("auth subcommand required")

    def _cmd_version(self, args: argparse.Namespace) -> None:
        print(self.runtime.version())

    def _cmd_update(self, args: argparse.Namespace) -> None:
        if args.dry_run:
            print(f"Would run: {sys.executable} -m pip install --upgrade gncore")
            return
        result = self.runtime.update()
        if result is not None:
            print(result.stdout or "Updated gncore")

    def _print_provider_list(self, project_dir: Path) -> None:
        try:
            selected = self.runtime.load_config(project_dir).selected_provider
        except Exception:
            selected = None
        for provider in discover_providers():
            status = provider.create().health()
            marker = "*" if provider.name == selected else " "
            print(f"{marker} {provider.name:14} {provider.kind.value:5} {status.health.value:11} {status.message}")

    def _print_run_results(self, results: list[ExecutionResult], project_dir: Path) -> None:
        if not results:
            print(f"{Ansi.YELLOW}No remaining stages to run.{Ansi.RESET}")
            return
        for result in results:
            print(f"{Ansi.GREEN}Success{Ansi.RESET}: {result.stage}")
            print(f"Provider: {result.provider}")
            print(f"Output File: {result.output_file}")
            print(f"Duration: {result.duration:.6f}s")
        final_state = ProjectStateManager(project_dir).load()
        if not final_state.current_stage:
            print(f"{Ansi.GREEN}Workflow complete.{Ansi.RESET}")

    def _run_dashboard(self, project_dir: Path) -> None:
        manager = ProjectStateManager(project_dir)
        if not manager.gncore_dir.exists():
            print(f"{Ansi.YELLOW}GNCore project not initialized. Run: gncore init{Ansi.RESET}")
            return
        state = manager.load()
        print(self.dashboard(state, manager))
        if sys.stdin.isatty():
            self._interactive_loop(manager, state)

    def dashboard(self, state: ProjectState, manager: ProjectStateManager) -> str:
        """Return a colored dashboard with provider and stage progress."""
        provider = self.provider_factory.create(state.provider)
        status = provider.health()
        lines = [
            "=================================================",
            f"{Ansi.BOLD}{Ansi.CYAN}GNCore{Ansi.RESET}",
            "AI Software Engineering Framework",
            "=================================================",
            "Project",
            state.project_name,
            "Provider",
            f"{state.provider} ({status.health.value})",
            "Current Progress",
            *self._progress_lines(state),
            "-------------------------------------------------",
            "Choose Stage",
            *self.registry.menu_lines(),
            "0 Exit",
        ]
        return "\n".join(lines)

    def _interactive_loop(self, manager: ProjectStateManager, state: ProjectState) -> None:
        while True:
            choice = input("Stage: ").strip()
            if choice == "0":
                return
            result = self.execute_stage(
                CliConfig(state.project_name, manager.project_dir, state.provider),
                CliSelection(int(choice)),
            )
            self._print_execution_result(result)
            state = manager.load()
            print(self.dashboard(state, manager))

    def _progress_lines(self, state: ProjectState) -> list[str]:
        return [self._progress_line(stage, state) for stage in self.registry.all()]

    @staticmethod
    def _progress_line(stage: StageDefinition, state: ProjectState) -> str:
        if stage.id in state.completed_stages:
            return f"{stage.name}\n{Ansi.GREEN}Completed{Ansi.RESET}"
        if stage.id in state.failed_stages:
            return f"{stage.name}\n{Ansi.RED}Failed{Ansi.RESET}"
        return f"{stage.name}\n{Ansi.YELLOW}Pending{Ansi.RESET}"

    @staticmethod
    def _parse_args(argv: list[str] | None) -> argparse.Namespace:
        parser = argparse.ArgumentParser(prog="gncore", add_help=True)
        parser.set_defaults(parser=parser)
        subparsers = parser.add_subparsers(dest="command")

        init_parser = subparsers.add_parser("init", help="Initialize a GNCore project")
        init_parser.add_argument("project_directory", nargs="?", type=Path)
        init_parser.add_argument("--project-name")
        init_parser.add_argument("--provider")

        run_parser = subparsers.add_parser("run", help="Run the workflow from the current project state")
        run_parser.add_argument("project_directory", nargs="?", type=Path)

        dashboard_parser = subparsers.add_parser("dashboard", help="Open the interactive stage dashboard")
        dashboard_parser.add_argument("project_directory", nargs="?", type=Path)

        stage_parser = subparsers.add_parser("stage", help="Open the interactive stage dashboard")
        stage_parser.add_argument("project_directory", nargs="?", type=Path)

        resume_parser = subparsers.add_parser("resume", help="Resume an interrupted workflow")
        resume_parser.add_argument("project_directory", nargs="?", type=Path)

        doctor_parser = subparsers.add_parser("doctor", help="Check project health and prerequisites")
        doctor_parser.add_argument("project_directory", nargs="?", type=Path)

        provider_parser = subparsers.add_parser("provider", help="Inspect and select providers")
        provider_parser.add_argument("project_directory", nargs="?", type=Path)
        provider_sub = provider_parser.add_subparsers(dest="provider_command", required=True)
        provider_sub.add_parser("list", help="List discovered providers")
        provider_use = provider_sub.add_parser("use", help="Select a provider")
        provider_use.add_argument("name")
        provider_detect = provider_sub.add_parser("detect", help="Auto-detect the best available provider")
        provider_detect.add_argument("project_directory", nargs="?", type=Path)
        provider_health = provider_sub.add_parser("health", help="Show provider health")
        provider_health.add_argument("name", nargs="?")

        config_parser = subparsers.add_parser("config", help="Inspect or edit project config")
        config_parser.add_argument("project_directory", nargs="?", type=Path)
        config_sub = config_parser.add_subparsers(dest="config_command", required=True)
        config_sub.add_parser("show", help="Print config as JSON")
        config_set = config_sub.add_parser("set", help="Update config values")
        config_set.add_argument("--provider")
        config_set.add_argument("--project-name")
        config_sub.add_parser("validate", help="Validate project config")

        auth_parser = subparsers.add_parser("auth", help="Manage provider credentials")
        auth_sub = auth_parser.add_subparsers(dest="auth_command", required=True)
        auth_login = auth_sub.add_parser("login", help="Store a provider token securely")
        auth_login.add_argument("provider")
        auth_login.add_argument("--token")
        auth_logout = auth_sub.add_parser("logout", help="Remove a stored provider token")
        auth_logout.add_argument("provider")
        auth_status = auth_sub.add_parser("status", help="Check whether a provider token is available")
        auth_status.add_argument("provider")

        subparsers.add_parser("version", help="Print the installed gncore version")
        update_parser = subparsers.add_parser("update", help="Upgrade gncore with pip")
        update_parser.add_argument("--dry-run", action="store_true")

        parser.add_argument("--project-name")
        parser.add_argument("--project-directory", type=Path)
        parser.add_argument("--provider", default="mock")
        parser.add_argument("--stage", type=int)
        parser.add_argument("--prompt", default="")
        return parser.parse_args(argv)

    @staticmethod
    def _project_dir(args: argparse.Namespace) -> Path:
        return getattr(args, "project_directory", None) or Path.cwd()

    @staticmethod
    def _has_legacy_stage_args(args: argparse.Namespace) -> bool:
        return args.project_name is not None or args.project_directory is not None or args.stage is not None

    @staticmethod
    def _legacy_config_from_args(args: argparse.Namespace) -> CliConfig:
        if args.project_name is None or args.project_directory is None or args.stage is None:
            raise SystemExit("--project-name, --project-directory, and --stage are required together")
        return CliConfig(args.project_name, args.project_directory, args.provider)

    @staticmethod
    def _legacy_selection_from_args(args: argparse.Namespace) -> CliSelection:
        return CliSelection(stage_id=args.stage, user_prompt=args.prompt)

    @staticmethod
    def _print_execution_result(result: ExecutionResult) -> None:
        print(f"{Ansi.GREEN}Success{Ansi.RESET}: {result.stage}")
        print(f"Provider: {result.provider}")
        print(f"Output File: {result.output_file}")
        print(f"Duration: {result.duration:.6f}s")


def main() -> None:
    """Console-script entry point."""
    GncoreCli().run(sys.argv[1:])
