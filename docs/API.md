# API

```python
from gncore import (
    builtin_skills, get_skill, list_categories, list_domains,
    list_workflows, render_skill, search_skills, validate_skill_definition,
)
```

- `builtin_skills()` returns the 60 adaptive category definitions.
- `get_skill(id)` returns a primary category or resolves a legacy workflow alias; unknown IDs raise `KeyError`.
- `list_categories()` returns the 60 category names.
- `list_domains()` returns 30 professional domains. Each has one primary `skill_ids` entry and ten `workflow_ids`.
- `list_workflows(category=None)` returns metadata for the 553 retained workflows, optionally filtered by category name.
- `search_skills(query, category=None)` returns ranked primary categories and considers their workflow names and descriptions.
- `render_skill(skill)` creates a portable entrypoint with discovery and license frontmatter.
- `validate_skill_definition(skill)` returns validation issues; an empty tuple indicates valid metadata and nonempty instructions.

Definitions include `SkillMetadata`, `SkillDefinition`, `SkillDomain`, `SkillCommand`, and `SkillExample`. Metadata includes a license expression. Skill content describes host-agent work; it does not execute an AI model.

## CLI

```text
gncore list [skills|categories|domains|workflows]
gncore search <terms> [--category <category>]
gncore show <id>
gncore plan <brief> [--theme <theme>] [--existing-theme <theme>]
gncore export (--skills <id>... | --specific <id> | --all) [--directory <path> | --output <file.zip>]
gncore version
```

Directory export defaults to `.agents/skills/`. ZIP and directory exports include all manifest-declared support files and notices. Aliases that resolve to the same category are consolidated into one output folder; duplicate identical input IDs remain an error.

`gncore.planning.frontend_plan()` returns a deterministic starting theme, rationale, constraints, required states, and checks. It preserves explicit themes and an existing brand, infers from product signals otherwise, and makes no model or browser calls.
