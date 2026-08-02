"""Provider-independent stage execution engine for GNCore."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import json
from time import perf_counter
import logging

from gncore.core.prompt import PromptBuilder, PromptInput
from gncore.core.stages import StageDefinition, StageRegistry
from gncore.providers.base import Provider, ProviderResponse
from gncore.skills.loader import SkillLoader
from gncore.state.manager import ProjectStateManager
from gncore.state.models import ProjectState
from gncore.utils.logging import LoggerFactory


class MissingSkillError(RuntimeError):
    """Raised when a stage's configured markdown skill cannot be loaded."""


class DependencyError(RuntimeError):
    """Raised when a required stage output is not available."""


class StateError(RuntimeError):
    """Raised when project state or required project input is invalid."""


class ProviderError(RuntimeError):
    """Raised when the configured provider fails during execution."""


@dataclass(frozen=True, slots=True)
class ExecutionResult:
    """Result returned after one stage execution."""

    success: bool
    stage: str
    provider: str
    output_file: Path
    duration: float
    timestamp: datetime
    tokens: int | None = None


class ExecutionEngine:
    """Execute one registered engineering stage at a time."""

    def __init__(
        self,
        registry: StageRegistry,
        state_manager: ProjectStateManager,
        skill_loader: SkillLoader,
        prompt_builder: PromptBuilder,
        provider: Provider,
        logger_factory: LoggerFactory | None = None,
    ) -> None:
        """Create an execution engine from explicit dependencies."""
        self.registry = registry
        self.state_manager = state_manager
        self.skill_loader = skill_loader
        self.prompt_builder = prompt_builder
        self.provider = provider
        self.logger = self._create_logger(logger_factory or LoggerFactory())

    def execute(self, stage_id: int) -> ExecutionResult:
        """Execute one stage and persist output, state, history, and logs."""
        started_at = datetime.now(timezone.utc)
        start_counter = perf_counter()
        stage = self._stage(stage_id)
        state = self._state()
        self._record_start(stage, state, started_at)
        try:
            result = self._execute_stage(stage, state, start_counter)
        except Exception as exc:
            self.state_manager.fail_stage(stage.id)
            self._record_failure(stage, started_at, start_counter, exc)
            raise
        self._record_success(result, stage, started_at)
        return result

    def _execute_stage(
        self,
        stage: StageDefinition,
        state: ProjectState,
        start_counter: float,
    ) -> ExecutionResult:
        skill = self._skill(stage)
        user_prompt = self._user_prompt()
        dependency_outputs = self._dependency_outputs(stage, state)
        self.state_manager.select_stage(stage.id)
        final_prompt = self._prompt(stage, state, skill, user_prompt, dependency_outputs)
        self._cache_prompt(stage, final_prompt)
        response = self._provider_response(final_prompt)
        self._validate_response(stage, response)
        output_file = self._save_output(stage, response)
        self.state_manager.complete_stage(stage.id)
        result = self._result(stage, response, output_file, start_counter)
        self._save_metadata(stage, response, result)
        return result

    def _stage(self, stage_id: int) -> StageDefinition:
        try:
            return self.registry.get(stage_id)
        except KeyError as exc:
            raise DependencyError(str(exc)) from exc

    def _state(self) -> ProjectState:
        try:
            return self.state_manager.load()
        except Exception as exc:
            raise StateError(f"Unable to load project state: {exc}") from exc

    def _skill(self, stage: StageDefinition) -> str:
        try:
            return self.skill_loader.load(stage.skill_path)
        except FileNotFoundError as exc:
            raise MissingSkillError(f"Missing skill for stage '{stage.name}': {stage.skill_path}") from exc

    def _user_prompt(self) -> str:
        try:
            return self.state_manager.prompt()
        except FileNotFoundError as exc:
            raise StateError(f"Missing user prompt file: {self.state_manager.prompt_file}") from exc

    def _dependency_outputs(self, stage: StageDefinition, state: ProjectState) -> dict[str, str]:
        outputs: dict[str, str] = {}
        for dependency_id in stage.dependencies:
            dependency = self._stage(dependency_id)
            self._ensure_dependency_completed(dependency, state)
            outputs[dependency.output_filename] = self._required_output(dependency)
        return outputs

    @staticmethod
    def _ensure_dependency_completed(dependency: StageDefinition, state: ProjectState) -> None:
        if dependency.id not in state.completed_stages:
            raise DependencyError(f"Stage '{dependency.name}' must be completed before this stage can run")

    def _required_output(self, dependency: StageDefinition) -> str:
        output_file = self.state_manager.output_file(dependency.output_filename)
        if not output_file.is_file():
            raise DependencyError(
                f"Stage '{dependency.name}' must be completed before its output can be used: {output_file}"
            )
        return output_file.read_text(encoding="utf-8")

    def _prompt(
        self,
        stage: StageDefinition,
        state: ProjectState,
        skill: str,
        user_prompt: str,
        dependency_outputs: dict[str, str],
    ) -> str:
        current_state = ProjectState(
            project_name=state.project_name,
            provider=state.provider,
            completed_stages=list(state.completed_stages),
            failed_stages=list(state.failed_stages),
            current_stage=stage.id,
            created_at=state.created_at,
            updated_at=state.updated_at,
        )
        return self.prompt_builder.build(
            PromptInput(
                stage=stage,
                skill=skill,
                user_prompt=user_prompt,
                context=self.state_manager.context(),
                previous_outputs=dependency_outputs,
                execution_history=self.state_manager.history(),
                state=current_state,
            )
        )

    def _cache_prompt(self, stage: StageDefinition, final_prompt: str) -> None:
        prompt_file = self.state_manager.prompt_cache_file(stage.output_filename)
        prompt_file.write_text(final_prompt, encoding="utf-8")

    def _provider_response(self, final_prompt: str) -> ProviderResponse:
        try:
            return self.provider.run(final_prompt)
        except Exception as exc:
            raise ProviderError(f"Provider execution failed: {exc}") from exc

    @staticmethod
    def _validate_response(stage: StageDefinition, response: ProviderResponse) -> None:
        if not response.content.strip():
            raise ProviderError(f"Provider returned empty output for stage '{stage.name}'")

    def _save_output(self, stage: StageDefinition, response: ProviderResponse) -> Path:
        output_file = self.state_manager.output_file(stage.output_filename)
        output_file.write_text(response.content, encoding="utf-8")
        return output_file

    def _result(
        self,
        stage: StageDefinition,
        response: ProviderResponse,
        output_file: Path,
        start_counter: float,
    ) -> ExecutionResult:
        return ExecutionResult(
            success=True,
            stage=stage.name,
            provider=response.provider_name,
            output_file=output_file,
            duration=perf_counter() - start_counter,
            timestamp=datetime.now(timezone.utc),
            tokens=self._tokens(response),
        )

    def _save_metadata(self, stage: StageDefinition, response: ProviderResponse, result: ExecutionResult) -> None:
        metadata_file = self.state_manager.metadata_file(stage.output_filename)
        data = {
            "stage": result.stage,
            "provider": result.provider,
            "success": result.success,
            "duration": result.duration,
            "timestamp": result.timestamp.isoformat(),
            "output_file": str(result.output_file),
            "tokens": result.tokens,
            "provider_metadata": response.metadata,
        }
        metadata_file.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    @staticmethod
    def _tokens(response: ProviderResponse) -> int | None:
        token_value = response.metadata.get("tokens")
        return int(token_value) if token_value is not None else None

    def _create_logger(self, logger_factory: LoggerFactory) -> logging.Logger:
        return logger_factory.create(self.state_manager.gncore_dir / "logs")

    def _record_start(self, stage: StageDefinition, state: ProjectState, started_at: datetime) -> None:
        self.state_manager.append_history("execution_started", {"stage_id": stage.id, "provider": state.provider})
        self.logger.info("stage=%s provider=%s start=%s", stage.name, state.provider, started_at.isoformat())

    def _record_success(self, result: ExecutionResult, stage: StageDefinition, started_at: datetime) -> None:
        self.state_manager.append_history(
            "execution_succeeded",
            {"stage_id": stage.id, "output_file": str(result.output_file), "duration": result.duration},
        )
        self.logger.info(
            "stage=%s provider=%s start=%s finish=%s duration=%.6f output_file=%s success=True",
            result.stage,
            result.provider,
            started_at.isoformat(),
            result.timestamp.isoformat(),
            result.duration,
            result.output_file,
        )

    def _record_failure(
        self,
        stage: StageDefinition,
        started_at: datetime,
        start_counter: float,
        exc: Exception,
    ) -> None:
        finished_at = datetime.now(timezone.utc)
        duration = perf_counter() - start_counter
        self.state_manager.append_history("execution_failed", {"stage_id": stage.id, "error": str(exc)})
        self.logger.error(
            "stage=%s start=%s finish=%s duration=%.6f success=False error=%s",
            stage.name,
            started_at.isoformat(),
            finished_at.isoformat(),
            duration,
            exc,
        )
