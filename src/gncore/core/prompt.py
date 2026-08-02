"""Prompt composition for stage execution."""

from __future__ import annotations

from dataclasses import dataclass

from gncore.state.models import ProjectState

from .stages import StageDefinition


@dataclass(frozen=True, slots=True)
class PromptInput:
    """Inputs required to build a provider prompt."""

    stage: StageDefinition
    skill: str
    user_prompt: str
    context: str
    previous_outputs: dict[str, str]
    execution_history: list[dict[str, object]] | None = None
    state: ProjectState | None = None


class PromptBuilder:
    """Combine skills, requirements, context, and prior outputs."""

    def build(self, prompt_input: PromptInput) -> str:
        """Return a single provider-ready prompt with explicit boundaries."""
        sections = [
            self._section("GNCore Execution Contract", self._contract()),
            self._section("Selected Stage", self._stage_summary(prompt_input.stage)),
            self._section("Project State", self._state_summary(prompt_input.state)),
            self._section("Reusable Skill Markdown", prompt_input.skill),
            self._section("User Project Requirements", prompt_input.user_prompt),
            self._section("Persistent Project Context", prompt_input.context),
            self._section("Dependency Artifacts", self._format_outputs(prompt_input.previous_outputs)),
            self._section("Execution History", self._format_history(prompt_input.execution_history)),
            self._section("Required Response", self._response_requirements(prompt_input.stage)),
        ]
        return "\n\n".join(sections).strip() + "\n"

    @staticmethod
    def _contract() -> str:
        return (
            "GNCore orchestrates one software engineering stage at a time. "
            "Use the selected skill as the stage policy, preserve prior context, "
            "and produce only the artifact requested for this stage."
        )

    @staticmethod
    def _stage_summary(stage: StageDefinition) -> str:
        dependencies = ", ".join(str(item) for item in stage.dependencies) or "none"
        return (
            f"id: {stage.id}\n"
            f"name: {stage.name}\n"
            f"dependencies: {dependencies}\n"
            f"output_filename: {stage.output_filename}"
        )

    @staticmethod
    def _state_summary(state: ProjectState | None) -> str:
        if state is None:
            return "No persisted project state was provided."
        completed = ", ".join(str(item) for item in state.completed_stages) or "none"
        failed = ", ".join(str(item) for item in state.failed_stages) or "none"
        return (
            f"project_name: {state.project_name}\n"
            f"provider: {state.provider}\n"
            f"completed_stages: {completed}\n"
            f"failed_stages: {failed}\n"
            f"current_stage: {state.current_stage}\n"
            f"created_at: {state.created_at}\n"
            f"updated_at: {state.updated_at}"
        )

    @staticmethod
    def _section(title: str, body: str) -> str:
        return f"## {title}\n{body.strip()}"

    @staticmethod
    def _format_outputs(outputs: dict[str, str]) -> str:
        if not outputs:
            return "No previous stage outputs are available."
        return "\n\n".join(f"### {name}\n{content.strip()}" for name, content in outputs.items())

    @staticmethod
    def _response_requirements(stage: StageDefinition) -> str:
        return (
            f"Write the complete {stage.name} stage artifact. "
            f"The artifact will be stored as .gncore/outputs/{stage.output_filename}. "
            "Do not claim to execute provider communication or deployment steps."
        )

    @staticmethod
    def _format_history(history: list[dict[str, object]] | None) -> str:
        """Format execution history for provider prompts."""
        if not history:
            return "No execution history is available."
        lines = []
        for event in history[-20:]:
            event_type = event.get("type", "unknown")
            timestamp = event.get("timestamp", "unknown")
            details = event.get("details", {})
            lines.append(f"- {timestamp}: {event_type} {details}")
        return "\n".join(lines)
