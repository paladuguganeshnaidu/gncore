"""Stage registry definitions for GNCore workflows."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class StageDefinition:
    """Metadata that describes one executable engineering stage."""

    id: int
    name: str
    skill_path: Path
    dependencies: tuple[int, ...]
    output_filename: str


class StageRegistry:
    """Central registry for all GNCore engineering stages."""

    def __init__(self, stages: tuple[StageDefinition, ...]) -> None:
        """Create a registry from unique stage definitions."""
        self._stages_by_id = self._index_stages(stages)

    @staticmethod
    def _index_stages(stages: tuple[StageDefinition, ...]) -> dict[int, StageDefinition]:
        indexed: dict[int, StageDefinition] = {}
        for stage in stages:
            if stage.id in indexed:
                raise ValueError(f"Duplicate stage id: {stage.id}")
            indexed[stage.id] = stage
        return indexed

    def all(self) -> tuple[StageDefinition, ...]:
        """Return all registered stages in display order."""
        return tuple(self._stages_by_id[key] for key in sorted(self._stages_by_id))

    def get(self, stage_id: int) -> StageDefinition:
        """Return one stage definition by id."""
        try:
            return self._stages_by_id[stage_id]
        except KeyError as exc:
            raise KeyError(f"Unknown stage id: {stage_id}") from exc

    def menu_lines(self) -> list[str]:
        """Return stage labels formatted for the interactive menu."""
        return [f"{stage.id} {stage.name}" for stage in self.all()]


def _skills_root() -> Path:
    """Return the existing markdown skill directory."""
    return Path(__file__).resolve().parents[2] / "ngcore" / "skills"


def default_stage_registry() -> StageRegistry:
    """Build the default GNCore developer workflow stage registry."""
    skills_root = _skills_root()
    return StageRegistry(
        (
            StageDefinition(1, "Planning", skills_root / "03-plan.md", (), "planning.md"),
            StageDefinition(2, "Architecture", skills_root / "04-architect.md", (1,), "architecture.md"),
            StageDefinition(3, "Design", skills_root / "05-design.md", (1, 2), "design.md"),
            StageDefinition(4, "Frontend", skills_root / "07-build.md", (1, 2, 3), "frontend.md"),
            StageDefinition(5, "Backend", skills_root / "07-build.md", (1, 2), "backend.md"),
            StageDefinition(6, "Database", skills_root / "04-architect.md", (1, 2, 5), "database.md"),
            StageDefinition(7, "Testing", skills_root / "13-test.md", (1, 2, 4, 5), "testing.md"),
            StageDefinition(8, "Security Audit", skills_root / "10-security.md", (1, 2, 4, 5), "security-audit.md"),
            StageDefinition(9, "Documentation", skills_root / "16-document.md", (1, 2, 4, 5), "documentation.md"),
            StageDefinition(10, "Deployment", skills_root / "17-deploy.md", (1, 2, 7, 8), "deployment.md"),
        )
    )
