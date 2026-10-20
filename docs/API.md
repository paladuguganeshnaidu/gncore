# API Reference

GNCore's public API is limited to the skill catalog and portable serialization. It has no application discovery, installation, configuration, model execution, or orchestration API.

## Catalog

```python
from gncore import get_skill, list_categories, list_domains, search_skills

skill = get_skill("train")
matches = search_skills("pytorch model", category="machine-learning")
categories = list_categories()
domains = list_domains()
```

- `builtin_skills()` returns the immutable tuple of 403 built-in skill definitions.
- `get_skill(skill_id)` returns one skill or raises `KeyError`.
- `search_skills(query, category=None)` returns ranked matches across IDs, names, descriptions, categories, and tags.
- `list_categories()` returns sorted category names.
- `list_domains()` returns 30 domain records, each with its ten skill IDs.
- `validate_skill_definition(skill)` returns a tuple of validation issues; an empty tuple indicates valid metadata and instructions.
- `render_skill(skill)` serializes a skill as a portable `SKILL.md` document with YAML frontmatter.

`SkillDefinition` contains metadata, prompt instructions, examples, command guidance, and optional configuration. The types are available from `gncore` and `gncore.skills.models`.

## CLI

- `gncore list [skills|domains|categories]`
- `gncore search <terms> [--category <name>]`
- `gncore show <skill-id>` prints the portable `SKILL.md` content.
- `gncore export --skills <id>... --output <file.zip>` writes selected skill folders to a ZIP.
- `gncore export --all --output <file.zip>` exports the complete catalog.
- `gncore version`

Export only writes to the explicitly selected output path. The ZIP has one `<skill-id>/SKILL.md` per skill and a README. The user copies those folders into an assistant's documented skills directory.
