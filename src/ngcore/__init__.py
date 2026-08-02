"""
NGCore

A dynamic AI skill orchestration framework for prompt engineering,
context-driven development, and reusable markdown-based workflows.
"""

from .core import (
    think,
    research,
    plan,
    architect,
    design,
    scaffold,
    build,
    integrate,
    review,
    security,
    performance,
    accessibility,
    test,
    debug,
    refactor,
    document,
    deploy,
    verify,
    git,
)

from .loader import (
    list_skills,
    search,
)
from .compat import Loader, NgCore

__version__ = "1.0.0"

__all__ = [
    "think",
    "research",
    "plan",
    "architect",
    "design",
    "scaffold",
    "build",
    "integrate",
    "review",
    "security",
    "performance",
    "accessibility",
    "test",
    "debug",
    "refactor",
    "document",
    "deploy",
    "verify",
    "git",
    "list_skills",
    "search",
    "Loader",
    "NgCore",
]