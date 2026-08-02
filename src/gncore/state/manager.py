"""Project initialization and state persistence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import ProjectState, utc_now_iso


class ProjectStateManager:
    """Manage the .gncore directory for a target project."""

    def __init__(self, project_dir: Path) -> None:
        """Create a manager for a project directory."""
        self.project_dir = project_dir
        self.gncore_dir = project_dir / ".gncore"
        self.prompt_file = project_dir / "prompt.md"

    def initialize(self, project_name: str, provider: str) -> ProjectState:
        """Create required GNCore files and return the persisted state."""
        self._create_directories()
        state = self._load_or_create_state(project_name, provider)
        self._write_json("config.json", {"project_name": project_name, "provider": provider})
        self._write_json("history.json", self._read_json("history.json", []))
        self._ensure_text("context.md", f"# {project_name} Context\n")
        self._ensure_project_prompt(project_name)
        self.save(state)
        return state

    def select_stage(self, stage_id: int) -> ProjectState:
        """Persist a selected current stage and append a history event."""
        state = self.load()
        state.current_stage = stage_id
        self.save(state)
        self.append_history("stage_selected", {"stage_id": stage_id})
        return state

    def complete_stage(self, stage_id: int) -> ProjectState:
        """Mark a stage complete and persist the updated project state."""
        state = self.load()
        if stage_id not in state.completed_stages:
            state.completed_stages.append(stage_id)
        if stage_id in state.failed_stages:
            state.failed_stages.remove(stage_id)
        state.current_stage = None
        self.save(state)
        self.append_history("stage_completed", {"stage_id": stage_id})
        return state

    def fail_stage(self, stage_id: int) -> ProjectState:
        """Mark a stage failed and persist the updated project state."""
        state = self.load()
        if stage_id not in state.failed_stages:
            state.failed_stages.append(stage_id)
        state.current_stage = None
        self.save(state)
        self.append_history("stage_failed", {"stage_id": stage_id})
        return state

    def history(self) -> list[dict[str, Any]]:
        """Return execution history events."""
        return list(self._read_json("history.json", []))

    def append_history(self, event_type: str, details: dict[str, Any]) -> None:
        """Append a timestamped event to history.json."""
        events = self._read_json("history.json", [])
        events.append({"type": event_type, "details": details, "timestamp": utc_now_iso()})
        self._write_json("history.json", events)

    def save(self, state: ProjectState) -> None:
        """Persist project state to state.json."""
        state.updated_at = utc_now_iso()
        self._write_json("state.json", state.to_dict())

    def load(self) -> ProjectState:
        """Load project state from state.json."""
        return ProjectState.from_dict(self._read_json("state.json", {}))

    def context(self) -> str:
        """Return project context markdown."""
        return (self.gncore_dir / "context.md").read_text(encoding="utf-8")

    def prompt(self) -> str:
        """Return the user project prompt markdown."""
        return self.prompt_file.read_text(encoding="utf-8")

    def write_prompt(self, prompt: str) -> None:
        """Persist the user project prompt markdown."""
        self.prompt_file.write_text(prompt.strip() + "\n", encoding="utf-8")

    def output_file(self, output_filename: str) -> Path:
        """Return the path for a stage output file."""
        return self.gncore_dir / "outputs" / output_filename

    def prompt_cache_file(self, output_filename: str) -> Path:
        """Return the path for a cached final prompt."""
        return self.gncore_dir / "prompt-cache" / output_filename

    def metadata_file(self, output_filename: str) -> Path:
        """Return the path for execution metadata."""
        return self.gncore_dir / "metadata" / output_filename.replace(".md", ".json")

    def previous_outputs(self) -> dict[str, str]:
        """Return all saved stage outputs keyed by filename."""
        output_dir = self.gncore_dir / "outputs"
        return {path.name: path.read_text(encoding="utf-8") for path in sorted(output_dir.glob("*.md"))}

    def _create_directories(self) -> None:
        self.project_dir.mkdir(parents=True, exist_ok=True)
        self.gncore_dir.mkdir(exist_ok=True)
        (self.gncore_dir / "outputs").mkdir(exist_ok=True)
        (self.gncore_dir / "artifacts").mkdir(exist_ok=True)
        (self.gncore_dir / "prompt-cache").mkdir(exist_ok=True)
        (self.gncore_dir / "metadata").mkdir(exist_ok=True)
        (self.gncore_dir / "logs").mkdir(exist_ok=True)

    def _load_or_create_state(self, project_name: str, provider: str) -> ProjectState:
        state_file = self.gncore_dir / "state.json"
        if state_file.exists():
            return ProjectState.from_dict(self._read_json("state.json", {}))
        return ProjectState(project_name=project_name, provider=provider)

    def _ensure_text(self, filename: str, default: str) -> None:
        path = self.gncore_dir / filename
        if not path.exists():
            path.write_text(default, encoding="utf-8")

    def _ensure_project_prompt(self, project_name: str) -> None:
        if not self.prompt_file.exists():
            self.write_prompt(f"# {project_name} Requirements")

    def _read_json(self, filename: str, default: Any) -> Any:
        path = self.gncore_dir / filename
        if not path.exists():
            return default
        return json.loads(path.read_text(encoding="utf-8"))

    def _write_json(self, filename: str, data: Any) -> None:
        path = self.gncore_dir / filename
        path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
