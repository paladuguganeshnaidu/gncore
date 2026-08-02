"""Typed state models for GNCore project metadata."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def utc_now_iso() -> str:
    """Return the current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


@dataclass(slots=True)
class ProjectState:
    """Persistent state stored in a project's .gncore/state.json file."""

    project_name: str
    provider: str
    completed_stages: list[int] = field(default_factory=list)
    failed_stages: list[int] = field(default_factory=list)
    current_stage: int | None = None
    created_at: str = field(default_factory=utc_now_iso)
    updated_at: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> dict[str, Any]:
        """Serialize the state to JSON-compatible data."""
        return {
            "project_name": self.project_name,
            "provider": self.provider,
            "completed_stages": self.completed_stages,
            "failed_stages": self.failed_stages,
            "current_stage": self.current_stage,
            "timestamps": {"created_at": self.created_at, "updated_at": self.updated_at},
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ProjectState":
        """Deserialize state from JSON-compatible data."""
        timestamps = data.get("timestamps", {})
        return cls(
            project_name=str(data["project_name"]),
            provider=str(data["provider"]),
            completed_stages=[int(item) for item in data.get("completed_stages", [])],
            failed_stages=[int(item) for item in data.get("failed_stages", [])],
            current_stage=data.get("current_stage"),
            created_at=str(timestamps.get("created_at", utc_now_iso())),
            updated_at=str(timestamps.get("updated_at", utc_now_iso())),
        )
