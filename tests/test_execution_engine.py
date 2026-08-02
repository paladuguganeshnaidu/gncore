from __future__ import annotations

import json
from pathlib import Path

import pytest

from gncore import (
    DependencyError,
    ExecutionEngine,
    MissingSkillError,
    MockProvider,
    PromptBuilder,
    ProjectStateManager,
    Provider,
    ProviderError,
    ProviderHealth,
    ProviderResponse,
    ProviderStatus,
    StateError,
    SkillLoader,
    StageDefinition,
    StageRegistry,
    default_stage_registry,
)


class RecordingProvider(Provider):
    """Provider test double that records the final prompt."""

    def __init__(self, content: str = "recorded output") -> None:
        self.content = content
        self.prompts: list[str] = []

    @property
    def name(self) -> str:
        return "recording"

    def run(self, prompt: str) -> ProviderResponse:
        self.prompts.append(prompt)
        return ProviderResponse(self.content, self.name, {"tokens": "42"})

    def stream(self, prompt: str):
        yield self.run(prompt).content

    def health(self) -> ProviderStatus:
        return ProviderStatus(self.name, ProviderHealth.AVAILABLE, "ok")

    def cancel(self) -> None:
        return None


class FailingProvider(Provider):
    """Provider test double that raises during execution."""

    @property
    def name(self) -> str:
        return "failing"

    def run(self, prompt: str) -> ProviderResponse:
        raise RuntimeError("provider unavailable")

    def stream(self, prompt: str):
        raise RuntimeError("provider unavailable")
        yield ""

    def health(self) -> ProviderStatus:
        return ProviderStatus(self.name, ProviderHealth.AVAILABLE, "ok")

    def cancel(self) -> None:
        return None


def _manager(tmp_path: Path) -> ProjectStateManager:
    manager = ProjectStateManager(tmp_path)
    manager.initialize("Execution", "recording")
    manager.write_prompt("# Build a serious product")
    return manager


def _engine(manager: ProjectStateManager, provider: Provider | None = None) -> ExecutionEngine:
    return ExecutionEngine(
        default_stage_registry(),
        manager,
        SkillLoader(),
        PromptBuilder(),
        provider or MockProvider(),
    )


def test_successful_execution_creates_output_and_result(tmp_path: Path) -> None:
    manager = _manager(tmp_path)
    provider = RecordingProvider("planning artifact")

    result = _engine(manager, provider).execute(1)

    assert result.success is True
    assert result.stage == "Planning"
    assert result.provider == "recording"
    assert result.tokens == 42
    assert result.output_file.read_text() == "planning artifact"
    assert manager.prompt_cache_file("planning.md").is_file()
    assert manager.metadata_file("planning.md").is_file()


def test_missing_skill_raises_clear_exception(tmp_path: Path) -> None:
    manager = _manager(tmp_path)
    registry = StageRegistry((StageDefinition(99, "Broken", tmp_path / "missing.md", (), "broken.md"),))
    engine = ExecutionEngine(registry, manager, SkillLoader(), PromptBuilder(), MockProvider())

    with pytest.raises(MissingSkillError, match="Missing skill for stage 'Broken'"):
        engine.execute(99)


def test_dependency_resolution_requires_dependency_outputs(tmp_path: Path) -> None:
    manager = _manager(tmp_path)

    with pytest.raises(DependencyError, match="Planning"):
        _engine(manager).execute(2)


def test_dependency_resolution_only_includes_declared_outputs(tmp_path: Path) -> None:
    manager = _manager(tmp_path)
    manager.output_file("planning.md").write_text("planning dependency", encoding="utf-8")
    manager.complete_stage(1)
    manager.output_file("research.md").write_text("unrelated research", encoding="utf-8")
    provider = RecordingProvider("architecture artifact")

    _engine(manager, provider).execute(2)

    assert "planning dependency" in provider.prompts[0]
    assert "unrelated research" not in provider.prompts[0]


def test_prompt_builder_receives_state_context_and_user_prompt(tmp_path: Path) -> None:
    manager = _manager(tmp_path)
    provider = RecordingProvider()

    _engine(manager, provider).execute(1)

    prompt = provider.prompts[0]
    assert "GNCore Execution Contract" in prompt
    assert "# Build a serious product" in prompt
    assert "project_name: Execution" in prompt
    assert "Reusable Skill Markdown" in prompt
    assert "Execution History" in prompt


def test_state_and_history_update_after_execution(tmp_path: Path) -> None:
    manager = _manager(tmp_path)

    _engine(manager, RecordingProvider()).execute(1)
    state = json.loads((tmp_path / ".gncore" / "state.json").read_text())
    history = json.loads((tmp_path / ".gncore" / "history.json").read_text())

    assert state["completed_stages"] == [1]
    assert state["current_stage"] is None
    assert "execution_started" in [event["type"] for event in history]
    assert "execution_succeeded" in [event["type"] for event in history]


def test_execution_logging_records_success(tmp_path: Path) -> None:
    manager = _manager(tmp_path)

    _engine(manager, RecordingProvider()).execute(1)
    log_text = (tmp_path / ".gncore" / "logs" / "gncore.log").read_text()

    assert "stage=Planning" in log_text
    assert "success=True" in log_text
    assert "output_file=" in log_text


def test_missing_prompt_raises_state_error(tmp_path: Path) -> None:
    manager = _manager(tmp_path)
    manager.prompt_file.unlink()

    with pytest.raises(StateError, match="Missing user prompt file"):
        _engine(manager, RecordingProvider()).execute(1)


def test_provider_failure_is_wrapped_and_logged(tmp_path: Path) -> None:
    manager = _manager(tmp_path)

    with pytest.raises(ProviderError, match="Provider execution failed"):
        _engine(manager, FailingProvider()).execute(1)

    state = json.loads((tmp_path / ".gncore" / "state.json").read_text())
    log_text = (tmp_path / ".gncore" / "logs" / "gncore.log").read_text()
    assert state["failed_stages"] == [1]
    assert "success=False" in log_text
