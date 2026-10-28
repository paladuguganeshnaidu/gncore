"""Deterministic planning aids; host agents retain contextual design judgment."""

from __future__ import annotations

import re

THEME_ALIASES = {
    "minimal": "minimalism", "minimalist": "minimalism", "minimalism": "minimalism",
    "maximal": "maximalism", "maximalizm": "maximalism", "maximalist": "maximalism", "maximalism": "maximalism",
    "brutalism": "neobrutalism", "brutalisim": "neobrutalism", "neo-brutalism": "neobrutalism", "neobrutalism": "neobrutalism",
    "industrial": "industrial", "industrial-brutalism": "industrial", "swiss": "swiss",
    "editorial": "editorial", "luxury": "luxury", "premium": "luxury", "agentic": "agentic",
    "futuristic": "futuristic", "y2k": "futuristic", "retro": "retro", "collage": "collage", "paper": "collage",
    "doodle": "doodle", "bento": "bento", "glass": "glass", "glassmorphism": "glass",
    "neumorphism": "neumorphism", "clay": "claymorphism", "claymorphism": "claymorphism",
    "aurora": "aurora", "gradient": "aurora", "neon": "cyberpunk", "cyberpunk": "cyberpunk",
    "3d": "immersive-3d", "immersive-3d": "immersive-3d", "organic": "organic", "terracotta": "organic",
}

SIGNALS = {
    "swiss": {"analytics": 3, "dashboard": 3, "admin": 3, "data": 2, "technical": 2, "b2b": 2},
    "editorial": {"magazine": 5, "journalism": 5, "article": 4, "publishing": 4, "journal": 4, "story": 2},
    "luxury": {"luxury": 5, "premium": 4, "jewelry": 5, "jewellery": 5, "hotel": 4, "craftsmanship": 4, "watch": 3},
    "claymorphism": {"children": 4, "kids": 4, "toy": 5, "playful": 3},
    "maximalism": {"festival": 4, "music": 3, "creative": 2, "expressive": 4},
    "industrial": {"industrial": 5, "factory": 4, "manufacturing": 4, "control": 2},
    "agentic": {"agent": 4, "agents": 4, "delegation": 4, "assistant": 3, "workflow": 1},
    "organic": {"natural": 3, "sustainable": 3, "sustainability": 3, "botanical": 5, "gardening": 4},
    "futuristic": {"gaming": 3, "esports": 4, "futuristic": 5},
    "minimalism": {"clinic": 5, "patient": 5, "healthcare": 5, "scheduling": 3, "settings": 3, "documentation": 2},
}


def frontend_plan(brief: str, *, theme: str | None = None, existing_theme: str | None = None) -> dict[str, object]:
    """Recommend a starting direction without pretending to replace design review."""
    if not brief.strip():
        raise ValueError("a product brief is required")
    words = set(re.findall(r"[a-z0-9]+", brief.casefold()))
    lowered = brief.casefold()
    avoid_motion = bool(re.search(r"\b(no|without|avoid|disable)\s+(animation|animations|motion)\b", lowered))
    avoid_gradients = bool(re.search(r"\b(no|without|avoid)\s+gradients?\b", lowered))
    excluded = {
        canonical for alias, canonical in THEME_ALIASES.items()
        if re.search(r"\b(?:no|not|without|avoid)\s+(?:a\s+)?" + re.escape(alias) + r"\b", lowered)
    }
    selected = None
    source = "inferred"
    if theme:
        selected = THEME_ALIASES.get(theme.casefold().strip())
        if not selected:
            raise ValueError(f"unknown theme: {theme}")
        source = "explicit"
    else:
        requested = re.search(r"\b(?:style|theme|aesthetic)\s*(?:is|:|=|of)?\s*([a-z0-9-]+)", lowered)
        if requested:
            selected = THEME_ALIASES.get(requested.group(1))
            source = "explicit" if selected else "inferred"
        if not selected:
            for word in ("minimalist", "maximalist", "maximalism", "maximalizm", "neobrutalism", "neo-brutalism", "brutalism", "brutalisim", "glassmorphism", "neumorphism", "claymorphism", "cyberpunk"):
                match = re.search(r"\b" + re.escape(word) + r"\b", lowered)
                if match and THEME_ALIASES[word] not in excluded:
                    selected = THEME_ALIASES[word]
                    source = "explicit"
                    break
        if not selected and existing_theme:
            selected = THEME_ALIASES.get(existing_theme.casefold().strip(), existing_theme.strip())
            source = "existing"
    if avoid_gradients and selected == "aurora":
        raise ValueError("the requested gradient theme conflicts with the no-gradients constraint")
    if selected in excluded:
        raise ValueError("the selected theme conflicts with an explicit style constraint")
    scores = {name: sum(weight for signal, weight in weights.items() if signal in words) for name, weights in SIGNALS.items() if name not in excluded}
    if not selected:
        fallback = "minimalism" if "minimalism" not in excluded else "swiss"
        selected = max(scores, key=scores.get) if any(scores.values()) else fallback
    return {
        "skill_id": "web-frontend", "theme": selected, "selection": source,
        "rationale": "Honor the supplied theme." if source == "explicit" else "Preserve the existing product theme." if source == "existing" else "Use the product audience, content, and primary task as a starting direction; confirm quality through implementation and review.",
        "motion": "none" if avoid_motion else "purposeful-with-reduced-motion-alternative",
        "gradients": "avoid" if avoid_gradients else "only-if-consistent-with-direction",
        "excluded_styles": sorted(excluded),
        "required_states": ["loading", "empty", "error", "success", "validation", "permission-when-applicable"],
        "checks": ["primary-user-journey", "narrow-and-wide-layouts", "keyboard-and-focus", "content-overflow", "relevant-build-and-tests"],
    }
