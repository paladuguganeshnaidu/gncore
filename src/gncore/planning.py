"""Deterministic planning aids; host agents retain contextual design judgment."""

from __future__ import annotations

import re

THEME_ALIASES = {
    "minimal": "minimalism", "minimalist": "minimalism", "minimalism": "minimalism",
    "maximal": "maximalism", "maximalizm": "maximalism", "maximalist": "maximalism", "maximalism": "maximalism",
    "brutalism": "neobrutalism", "brutalisim": "neobrutalism", "britalisim": "neobrutalism", "neo-brutalism": "neobrutalism", "neobrutalism": "neobrutalism",
    "industrial": "industrial", "industrial-brutalism": "industrial", "swiss": "swiss",
    "editorial": "editorial", "luxury": "luxury", "premium": "luxury", "agentic": "agentic",
    "futuristic": "futuristic", "y2k": "futuristic", "retro": "retro", "collage": "collage", "paper": "collage",
    "doodle": "doodle", "bento": "bento", "glass": "glass", "glassmorphism": "glass",
    "neumorphism": "neumorphism", "clay": "claymorphism", "claymorphism": "claymorphism",
    "aurora": "aurora", "gradient": "aurora", "neon": "cyberpunk", "cyberpunk": "cyberpunk",
    "3d": "immersive-3d", "immersive-3d": "immersive-3d", "organic": "organic", "terracotta": "organic",
    "liquid-glass": "glass", "international-design": "swiss", "retro-futurism": "futuristic",
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


def _normalize(text: str) -> str:
    return re.sub(r"[\s_\-\u2010-\u2015]+", " ", text.casefold()).strip()


def _theme(text: str) -> str | None:
    normalized = _normalize(text)
    return next((canonical for alias, canonical in THEME_ALIASES.items() if _normalize(alias) == normalized), None)


def _negative_spans(text: str) -> list[tuple[int, int]]:
    # Deliberately bounded grammar, not a general natural-language interpreter.
    # Carry negation through lists, stopping at punctuation or a positive clause.
    pattern = r"\b(?:no|not(?! only\b)|without|avoid|disable|exclude|excluding|do not|don't)\b[^,.;!?\n]*"
    spans = []
    for match in re.finditer(pattern, text):
        lead = re.match(r"(?:do not|don't|no|not|without|avoid|disable|exclude|excluding)\s*(?:use\s+)?", match.group()).end()
        boundary = re.search(r"\b(?:but|instead|however|use|choose|prefer|with)\b", match.group()[lead:])
        spans.append((match.start(), match.start() + lead + boundary.start() if boundary else match.end()))
    return spans


def _theme_mentions(text: str) -> list[tuple[int, int, str, str]]:
    aliases = sorted({_normalize(alias): canonical for alias, canonical in THEME_ALIASES.items()}.items(), key=lambda pair: -len(pair[0]))
    pattern = r"\b(?:" + "|".join(re.escape(alias) for alias, _ in aliases) + r")\b"
    lookup = dict(aliases)
    return [(m.start(), m.end(), lookup[m.group()], m.group()) for m in re.finditer(pattern, text)]


def frontend_plan(brief: str, *, theme: str | None = None, existing_theme: str | None = None) -> dict[str, object]:
    """Recommend a starting direction without pretending to replace design review."""
    if not brief.strip():
        raise ValueError("a product brief is required")
    lowered = _normalize(brief)
    spans = _negative_spans(lowered)
    negative = lambda start: any(left <= start < right for left, right in spans)
    negative_text = " ".join(lowered[left:right] for left, right in spans)
    avoid_motion = bool(re.search(r"\b(?:animated|animations?|motion|movement)\b", negative_text))
    avoid_gradients = bool(re.search(r"\bgradients?\b", negative_text))
    mentions = _theme_mentions(lowered)
    excluded = {canonical for start, _, canonical, _ in mentions if negative(start)}
    if avoid_gradients:
        excluded.add("aurora")
    # Excluded words must not contribute positive product signals either.
    positive_text = lowered
    for left, right in reversed(spans):
        positive_text = positive_text[:left] + " " * (right - left) + positive_text[right:]
    words = set(re.findall(r"[a-z0-9]+", positive_text))
    selected = None
    source = "inferred"
    if theme is not None:
        selected = _theme(theme)
        if not selected:
            raise ValueError(f"unknown theme: {theme}")
        source = "explicit"
    else:
        distinctive = {"minimalist", "maximalist", "maximalism", "maximalizm", "neobrutalism", "neo brutalism", "brutalism", "brutalisim", "britalisim", "glassmorphism", "neumorphism", "claymorphism", "cyberpunk"}
        requested = set()
        for start, end, canonical, alias in mentions:
            if negative(start):
                continue
            prefix, suffix = lowered[:start], lowered[end:]
            has_label = re.search(r"\b(?:style|theme|aesthetic)\s*(?:(?:is|of)\s*|[:=]\s*)?(?:an?\s+)?$", prefix) or re.match(r"\s+(?:style|theme|aesthetic)\b", suffix)
            if has_label or alias in distinctive:
                requested.add(canonical)
        if len(requested) > 1:
            raise ValueError("conflicting theme requests; choose one primary theme or supply --theme")
        if requested:
            selected = requested.pop()
            source = "explicit"
        if not selected and existing_theme is not None:
            selected = _theme(existing_theme) or existing_theme.strip()
            if not selected:
                raise ValueError("existing theme must not be blank")
            source = "existing"
    if avoid_gradients and selected == "aurora":
        raise ValueError("the requested gradient theme conflicts with the no-gradients constraint")
    if selected in excluded:
        raise ValueError("the selected theme conflicts with an explicit style constraint")
    scores = {name: sum(weight for signal, weight in weights.items() if signal in words) for name, weights in SIGNALS.items() if name not in excluded}
    if not selected:
        allowed = [name for name in dict.fromkeys(["minimalism", "swiss", *THEME_ALIASES.values()]) if name not in excluded]
        if not allowed:
            raise ValueError("conflicting constraints exclude every available theme; choose an allowed direction")
        fallback = allowed[0]
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
