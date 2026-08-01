"""
Public API for loading NGCore skills and combining them with user prompts.
"""

from .loader import load


def create_skill(name: str):
    """Create a wrapper that loads a named skill and attaches a prompt."""

    def wrapper(prompt: str) -> dict[str, str]:
        """Load the skill markdown and return it with the user's prompt.

        Args:
            prompt: User request.

        Returns:
            Dictionary containing the skill markdown and user prompt.
        """
        return {
            "skill": load(name),
            "prompt": prompt,
        }

    return wrapper


think = create_skill("think")
research = create_skill("research")
plan = create_skill("plan")
architect = create_skill("architect")
design = create_skill("design")
scaffold = create_skill("scaffold")
build = create_skill("build")
integrate = create_skill("integrate")
review = create_skill("review")
security = create_skill("security")
performance = create_skill("performance")
accessibility = create_skill("accessibility")
test = create_skill("test")
debug = create_skill("debug")
refactor = create_skill("refactor")
document = create_skill("document")
deploy = create_skill("deploy")
verify = create_skill("verify")
git = create_skill("git")
