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
gncore export (--skills <id>... | --specific <id> | --all) [--directory <path> | --output <file.zip>] [--dry-run]
gncore verify [--directory <path>]
gncore recover [--directory <path>] --journal <journal.json>
gncore evaluate (--validate | --list | --case <id>) [--corpus <cases.json>] [--response <result.json> --artifacts <directory>]
gncore version
```

Directory export defaults to `.agents/skills/`. ZIP and directory exports include all manifest-declared support files and notices. Aliases that resolve to the same category are consolidated into one output folder; duplicate identical input IDs remain an error.

`gncore.planning.frontend_plan()` returns a deterministic starting theme, rationale, constraints, required states, and checks. It preserves explicit themes and an existing brand, infers from product signals otherwise, and makes no model or browser calls.

Theme precedence is explicit `--theme`, then an explicitly named style in the brief, then an existing brand, then product inference. Negative style and gradient constraints apply to every path, including explicit inputs and fallbacks. Contradictions raise `ValueError` rather than returning a prohibited theme. The parser supports bounded English patterns, documented spelling aliases such as `britalisim`, multiword styles, negative lists, and motion phrases such as “not animated” and “without movement”; it is not a general language model.

`gncore.installation` exposes `install_skills(root, payloads, version=..., dry_run=False, legacy=None)`, `verify_installation(root)`, and `recover_installation(root, journal)`. Payloads map canonical skill IDs to relative file paths and bytes. These functions operate only on the specified project installation and retain backups; see [installation behavior](INSTALLATION.md).

`gncore.evaluation` exposes `load_corpus(path=None)`, `validate_corpus(corpus)`, and `evaluate_response(case, response, artifact_root)`. Corpus loading validates coverage and catalog references. Evaluation checks recorded selection, declared decisions, and artifact presence, leaving semantic review pending and tool checks unexecuted. See [evaluation format and limits](EVALUATION.md).
