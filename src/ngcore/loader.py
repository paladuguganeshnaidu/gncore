from pathlib import Path

BASE = Path(__file__).parent


def load(name: str) -> str:
    """
    Load a markdown skill.
    """

    for file in (BASE / "skills").glob("*.md"):

        if file.stem.endswith(name):

            return file.read_text(
                encoding="utf-8"
            )

    raise FileNotFoundError(
        f"Skill '{name}' not found."
    )