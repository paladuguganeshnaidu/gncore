"""
Utilities for discovering, loading, and searching NGCore skills.
"""

from pathlib import Path

BASE = Path(__file__).parent
SKILLS_DIR = BASE / "skills"


def load(name: str) -> str:
    """Load a skill markdown file by its name."""
    for file in SKILLS_DIR.glob("*.md"):
        if file.stem.endswith(name):
            return file.read_text(encoding="utf-8")

    raise FileNotFoundError(f"Skill '{name}' not found.")


def list_skills() -> list[str]:
    """Return a sorted list of available skill names."""
    return sorted(
        file.stem.split("-", 1)[1]
        for file in SKILLS_DIR.glob("*.md")
    )


def search(keyword: str) -> list[str]:
    """Search skill markdown files for a keyword.

    Args:
        keyword: The term to look for in skill contents.

    Returns:
        A list of skill names that contain the keyword.
    """
    keyword = keyword.lower()
    results: list[str] = []

    for file in SKILLS_DIR.glob("*.md"):
        text = file.read_text(encoding="utf-8")

        if keyword in text.lower():
            results.append(file.stem)

    return results
