from __future__ import annotations

import json
from pathlib import Path

from gncore import (
    CliConfig,
    CliSelection,
    GncoreCli,
    MockProvider,
    ProjectStateManager,
    PromptBuilder,
    PromptInput,
    SkillLoader,
    StageWorkflow,
    default_stage_registry,
)


def test_cli_banner_contains_required_stage_menu() -> None:
    banner = GncoreCli().banner()

    assert "GNCore" in banner
    assert "AI Software Engineering Framework" in banner
    assert "Project Name:" in banner
    assert "10 Deployment" in banner


def test_project_initialization_creates_required_files(tmp_path: Path) -> None:
    manager = ProjectStateManager(tmp_path)

    state = manager.initialize("Example", "mock")

    assert state.project_name == "Example"
    assert (tmp_path / ".gncore" / "config.json").is_file()
    assert (tmp_path / ".gncore" / "state.json").is_file()
    assert (tmp_path / ".gncore" / "history.json").is_file()
    assert (tmp_path / ".gncore" / "outputs").is_dir()
    assert (tmp_path / ".gncore" / "logs").is_dir()
    assert (tmp_path / ".gncore" / "context.md").is_file()
    assert (tmp_path / "prompt.md").is_file()
    assert (tmp_path / ".gncore" / "artifacts").is_dir()
    assert (tmp_path / ".gncore" / "prompt-cache").is_dir()
    assert (tmp_path / ".gncore" / "metadata").is_dir()


def test_stage_selection_updates_state_and_history(tmp_path: Path) -> None:
    manager = ProjectStateManager(tmp_path)
    manager.initialize("Example", "mock")

    state = manager.select_stage(2)
    history = json.loads((tmp_path / ".gncore" / "history.json").read_text())

    assert state.current_stage == 2
    assert history[-1]["type"] == "stage_selected"
    assert history[-1]["details"] == {"stage_id": 2}


def test_stage_registry_is_single_source_for_menu_and_metadata() -> None:
    registry = default_stage_registry()
    stage = registry.get(2)

    assert stage.name == "Architecture"
    assert stage.output_filename == "architecture.md"
    assert registry.menu_lines()[0] == "1 Planning"


def test_skill_loader_loads_existing_markdown_without_duplication() -> None:
    stage = default_stage_registry().get(1)

    skill = SkillLoader().load(stage.skill_path)

    assert "ngcore" in stage.skill_path.parts
    assert "skills" in stage.skill_path.parts
    assert "plan" in skill.lower()


def test_prompt_builder_combines_all_inputs_with_execution_contract(tmp_path: Path) -> None:
    manager = ProjectStateManager(tmp_path)
    state = manager.initialize("Example", "mock")
    stage = default_stage_registry().get(1)

    prompt = PromptBuilder().build(
        PromptInput(
            stage=stage,
            skill="Skill content",
            user_prompt="Build an app",
            context="Existing context",
            previous_outputs={"research.md": "Prior research"},
            state=state,
        )
    )

    assert "GNCore Execution Contract" in prompt
    assert "Skill content" in prompt
    assert "Build an app" in prompt
    assert "Existing context" in prompt
    assert "Prior research" in prompt
    assert "output_filename: planning.md" in prompt


def test_stage_workflow_assembles_prompt_and_updates_state(tmp_path: Path) -> None:
    manager = ProjectStateManager(tmp_path)
    manager.initialize("Example", "mock")
    workflow = StageWorkflow(default_stage_registry(), manager, SkillLoader(), PromptBuilder())

    preparation = workflow.prepare_stage(1, "Create a payments product")

    assert preparation.state.current_stage == 1
    assert preparation.stage.output_filename == "planning.md"
    assert "Create a payments product" in preparation.prompt


def test_mock_provider_returns_typed_response() -> None:
    response = MockProvider().run("hello")

    assert response.provider_name == "mock"
    assert response.metadata["prompt_length"] == "5"


def test_cli_initialization_writes_log(tmp_path: Path) -> None:
    GncoreCli().initialize(CliConfig("Example", tmp_path, "mock"))

    assert (tmp_path / ".gncore" / "logs" / "gncore.log").is_file()


def test_cli_prepare_stage_initializes_project_and_prompt(tmp_path: Path) -> None:
    cli = GncoreCli()

    preparation = cli.prepare_stage(
        CliConfig("Example", tmp_path, "mock"),
        CliSelection(stage_id=1, user_prompt="Plan a release"),
    )

    assert preparation.state.current_stage == 1
    assert "Plan a release" in preparation.prompt
    assert (tmp_path / ".gncore" / "state.json").is_file()


def test_cli_execute_stage_creates_stage_output(tmp_path: Path) -> None:
    result = GncoreCli().execute_stage(
        CliConfig("Example", tmp_path, "mock"),
        CliSelection(stage_id=1, user_prompt="Plan a release"),
    )

    assert result.success is True
    assert result.output_file == tmp_path / ".gncore" / "outputs" / "planning.md"
    assert result.output_file.is_file()
