# Usage

Install GNCore into a Python environment:

```bash
python -m pip install gncore
```

GNCore searches and installs skill content into a project-local `.agents/skills/` directory by default. It does not change application settings.

## Find a skill

```bash
gncore list domains
gncore list skills
gncore list categories
gncore search "model training"
gncore search "presentation slides" --category presentations-powerpoint
```

Search uses the skill ID, title, description, category, and tags. It returns catalog matches; it does not invoke a model.

## Inspect a skill

```bash
gncore show train
```

The output is a complete portable `SKILL.md` document. In a compatible assistant, place it at `.agents/skills/<skill-id>/SKILL.md`; the host assistant discovers the skill and decides how to execute it using its own tools.

## Export selected skills

```bash
gncore export --skills train preprocess clean-data evaluate improve analyze
```

Each skill is installed as `.agents/skills/<skill-id>/SKILL.md` in the current directory.

Install one specific skill by exact ID or choose a different install directory:

```bash
gncore export --specific design-ux-audit
gncore export --skills train --directory ./my-agent/skills
```

## Export the complete catalog

```bash
gncore export --all
```

This installs every catalog skill under `.agents/skills/`.

## Create a ZIP archive

Pass `--output` to create an archive instead of installing directly:

```bash
gncore export --skills train evaluate --output ml-skills.zip
```

Each archive skill folder contains a complete `SKILL.md`. Extract the folders under `.agents/skills/` to make them discoverable.

## Python API

```python
from gncore import get_skill, list_domains, search_skills

train = get_skill("train")
print(train.prompt)
print(search_skills("clean data"))
print(list_domains())
```

`get_skill` raises `KeyError` for an unknown ID. `search_skills` returns ranked matches. Skill definitions and domain records are immutable dataclasses.

## Use the skill instructions well

Give the host assistant your goal, relevant context, constraints, and how you will judge the result. Skills request evidence-based planning and verification, but the host's available tools and permissions determine what it can actually do. Review its output and check report.
