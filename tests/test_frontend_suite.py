import importlib.util
from pathlib import Path

import pytest

from gncore.planning import THEME_ALIASES, frontend_plan


@pytest.mark.parametrize(("brief", "expected"), [
    ("A small clinic patient scheduling dashboard", "minimalism"),
    ("An analytics dashboard for B2B teams", "swiss"),
    ("A premium hotel website", "luxury"),
    ("A journalism magazine with long articles", "editorial"),
    ("A playful toy shop for kids", "claymorphism"),
    ("A music festival landing page", "maximalism"),
    ("An industrial factory control panel", "industrial"),
    ("An AI agent task delegation workspace", "agentic"),
    ("A botanical gardening store", "organic"),
    ("A website for my new project", "minimalism"),
])
def test_direction_inference_uses_product_context(brief, expected):
    plan = frontend_plan(brief)
    assert plan["theme"] == expected
    assert plan["selection"] == "inferred"


@pytest.mark.parametrize(("theme", "expected"), [("minimal", "minimalism"), ("maximalizm", "maximalism"), ("brutalisim", "neobrutalism"), ("glassmorphism", "glass")])
def test_explicit_theme_overrides_product_inference(theme, expected):
    plan = frontend_plan("A premium hotel website", theme=theme)
    assert plan["theme"] == expected and plan["selection"] == "explicit"


def test_natural_style_existing_brand_and_negative_constraints():
    assert frontend_plan("Build a maximalist page")["theme"] == "maximalism"
    assert frontend_plan("An analytics dashboard", existing_theme="Acme brand")["theme"] == "Acme brand"
    assert frontend_plan("A premium hotel, no animation")["motion"] == "none"
    assert frontend_plan("A clinic, avoid gradients")["gradients"] == "avoid"
    assert frontend_plan("A clinic without maximalism")["theme"] == "minimalism"
    assert frontend_plan("A website, not minimalist")["theme"] != "minimalism"
    with pytest.raises(ValueError, match="conflicts"):
        frontend_plan("A website, avoid minimalism", theme="minimal")
    with pytest.raises(ValueError, match="conflicts"):
        frontend_plan("A website with no gradients", theme="aurora")
    with pytest.raises(ValueError):
        frontend_plan("")


def test_attributed_r3f_helper_fix_survives_reference_migration():
    helper = Path(__file__).resolve().parents[1] / "src/gncore/skills/unified_data/web-frontend/references/web-front-r3f/scripts/component_generator.py"
    spec = importlib.util.spec_from_file_location("r3f_generator", helper)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    code = module.R3FComponentGenerator("interactive", events=["onClick", "focus"]).generate()
    assert 'onClick={(e) => console.log("click", e)}' in code
    assert 'onFocus={(e) => console.log("focus", e)}' in code
    assert "{/* Lighting */}" in module.R3FComponentGenerator("scene").generate()


@pytest.mark.parametrize("brief", [
    "A website, no minimalism and no swiss",
    "A website, avoid minimalism and swiss",
    "A dashboard without a swiss theme",
    "A website, no minimalism, no swiss, no editorial and no luxury",
    "A website, avoid gradients",
])
def test_every_fallback_respects_exclusions(brief):
    plan = frontend_plan(brief)
    assert plan["theme"] not in plan["excluded_styles"]


@pytest.mark.parametrize("phrase", ["not animated", "without movement", "do not use animation", "no motion or gradients", "avoid all animations", "disable motion"])
def test_motion_constraints(phrase):
    assert frontend_plan(f"A website, {phrase}")["motion"] == "none"


@pytest.mark.parametrize(("phrase", "expected"), [
    ("in britalisim style", "neobrutalism"),
    ("in neo brutalism style", "neobrutalism"),
    ("with theme: liquid glass", "glass"),
    ("in industrial brutalism style", "industrial"),
    ("with aesthetic of retro futurism", "futuristic"),
])
def test_multiword_and_documented_spelling(phrase, expected):
    plan = frontend_plan(f"A landing page {phrase}")
    assert plan["theme"] == expected and plan["selection"] == "explicit"


def test_precedence_and_contradictions_are_explicit():
    assert frontend_plan("A maximalist site", theme="neo brutalism", existing_theme="Acme")["theme"] == "neobrutalism"
    assert frontend_plan("A maximalist site", existing_theme="Acme")["theme"] == "maximalism"
    assert frontend_plan("A dashboard", existing_theme="Acme")["theme"] == "Acme"
    assert frontend_plan("No minimalism, but use maximalist style")["theme"] == "maximalism"
    assert frontend_plan("Not only animated, also colorful")["motion"] != "none"
    with pytest.raises(ValueError, match="conflict"):
        frontend_plan("A maximalist and minimalist site")
    with pytest.raises(ValueError, match="conflict"):
        frontend_plan("No minimalism", existing_theme="minimal")
    with pytest.raises(ValueError, match="conflict"):
        frontend_plan("No " + " or ".join(sorted(set(THEME_ALIASES.values()))))
    with pytest.raises(ValueError, match="unknown"):
        frontend_plan("A site", theme="")
