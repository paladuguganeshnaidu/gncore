"""Markdown skill loading for GNCore."""

from __future__ import annotations

from pathlib import Path


class SkillLoader:
    """Load reusable engineering skills from markdown files."""

    def load(self, skill_path: Path) -> str:
        """Return the contents of a skill markdown file."""
        if not skill_path.is_file():
            raise FileNotFoundError(f"Skill file not found: {skill_path}")
        return skill_path.read_text(encoding="utf-8")
