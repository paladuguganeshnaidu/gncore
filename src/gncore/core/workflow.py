"""Stage preparation workflow for GNCore."""

from __future__ import annotations

from dataclasses import dataclass

from gncore.core.prompt import PromptBuilder, PromptInput
from gncore.core.stages import StageDefinition, StageRegistry
from gncore.skills.loader import SkillLoader
from gncore.state.manager import ProjectStateManager
from gncore.state.models import ProjectState


@dataclass(frozen=True, slots=True)
class StagePreparation:
    """Artifacts produced when a user selects a stage."""

    state: ProjectState
    stage: StageDefinition
    prompt: str


class StageWorkflow:
    """Coordinate stage selection, skill loading, and prompt assembly."""

    def __init__(
        self,
        registry: StageRegistry,
        state_manager: ProjectStateManager,
        skill_loader: SkillLoader,
        prompt_builder: PromptBuilder,
    ) -> None:
        """Create a workflow from its explicit collaborators."""
        self.registry = registry
        self.state_manager = state_manager
        self.skill_loader = skill_loader
        self.prompt_builder = prompt_builder

    def prepare_stage(self, stage_id: int, user_prompt: str) -> StagePreparation:
        """Select a stage and return the assembled provider prompt."""
        stage = self.registry.get(stage_id)
        state = self.state_manager.select_stage(stage_id)
        skill = self.skill_loader.load(stage.skill_path)
        prompt = self.prompt_builder.build(
            PromptInput(
                stage=stage,
                skill=skill,
                user_prompt=user_prompt,
                context=self.state_manager.context(),
                previous_outputs=self.state_manager.previous_outputs(),
                state=state,
            )
        )
        return StagePreparation(state=state, stage=stage, prompt=prompt)
