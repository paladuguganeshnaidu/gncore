# Usage

Install GNCore into a Python environment:

```bash
python -m pip install gncore
```

GNCore searches and exports skill content. It does not discover or edit VS Code, Codex, Claude, Antigravity, or other application settings. The examples below write only the ZIP path you provide.

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

The output is a complete portable `SKILL.md` document. In a compatible assistant, place the folder in that assistant's documented skills directory and call the skill by its slash name, such as `/train`. The host assistant decides how to execute the instructions using its own tools.

## Export selected skills

```bash
gncore export --skills train preprocess clean-data evaluate improve analyze --output ml-skills.zip
```

Each skill is exported as `<skill-id>/SKILL.md`, plus a bundle README. Copy only the skill folders you want into your assistant's documented skills location.

## Export the complete catalog

```bash
gncore export --all --output gncore-skills.zip
```

The archive contains 403 skills across 30 domains. It can be large; start with selected skills when you only need a few.

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
