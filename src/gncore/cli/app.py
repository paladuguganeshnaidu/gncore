"""Command-line interface for GNCore."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import sys

from gncore.core.executor import ExecutionEngine, ExecutionResult
from gncore.core.prompt import PromptBuilder
from gncore.core.stages import StageDefinition, StageRegistry, default_stage_registry
from gncore.core.workflow import StagePreparation, StageWorkflow
from gncore.providers.factory import ProviderFactory
from gncore.providers.mock import MockProvider
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
        """Create the CLI with a central stage registry."""
        self.registry = registry or default_stage_registry()
        self.provider_factory = ProviderFactory()

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
        manager = ProjectStateManager(project_dir)
        manager.initialize(project_name, provider)
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
        """Run the CLI, initializing or executing based on user input."""
        args = self._parse_args(argv)
        if args.command == "init":
            self._run_init(args)
            return
        if self._has_startup_args(args):
            result = self.execute_stage(self._config_from_args(args), self._selection_from_args(args))
            self._print_execution_result(result)
            return
        self._run_dashboard(Path.cwd())

    def _run_init(self, args: argparse.Namespace) -> None:
        project_dir = args.project_directory or Path.cwd()
        project_name = args.project_name or project_dir.name
        manager = self.init_project(project_dir, project_name, args.provider)
        print(f"{Ansi.GREEN}Initialized GNCore project at {manager.gncore_dir}{Ansi.RESET}")
        print(f"Write requirements in {manager.prompt_file}")

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
        subparsers = parser.add_subparsers(dest="command")
        init_parser = subparsers.add_parser("init")
        init_parser.add_argument("--project-name")
        init_parser.add_argument("--project-directory", type=Path)
        init_parser.add_argument("--provider", default="mock")
        parser.add_argument("--project-name")
        parser.add_argument("--project-directory", type=Path)
        parser.add_argument("--provider", default="mock")
        parser.add_argument("--stage", type=int)
        parser.add_argument("--prompt", default="")
        return parser.parse_args(argv)

    @staticmethod
    def _has_startup_args(args: argparse.Namespace) -> bool:
        return args.project_name is not None or args.project_directory is not None or args.stage is not None

    @staticmethod
    def _config_from_args(args: argparse.Namespace) -> CliConfig:
        if args.project_name is None or args.project_directory is None or args.stage is None:
            raise SystemExit("--project-name, --project-directory, and --stage are required together")
        return CliConfig(args.project_name, args.project_directory, args.provider)

    @staticmethod
    def _selection_from_args(args: argparse.Namespace) -> CliSelection:
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
