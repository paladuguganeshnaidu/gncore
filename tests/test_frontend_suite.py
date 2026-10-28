import importlib.util
from pathlib import Path

import pytest

from gncore.planning import frontend_plan


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
