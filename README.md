# GNCore

GNCore is a Python library and CLI for discovering and installing reusable AI agent skills. Its 403 skills cover 30 domain packs and are distributed as standard `SKILL.md` folders.

## Install

```bash
python -m pip install gncore
```

## Discover and use skills

```bash
gncore list domains
gncore search "machine learning training"
gncore show train
gncore export --skills train evaluate
```

By default, `export` installs the selected skills into `.agents/skills/<skill-id>/SKILL.md` in the current project. Agent tools that discover `.agents/skills/` can load the instructions, examples, and commands from these folders.

Install one skill by its exact ID, install the full catalog, or choose another destination:

```bash
gncore export --specific design-ux-audit
gncore export --all
gncore export --skills train --directory ./my-agent/skills
```

To retain the portable ZIP workflow, pass `--output` explicitly:

```bash
gncore export --skills train evaluate --output ml-skills.zip
```

The Python API can be used directly:

```python
from gncore import get_skill, list_domains, search_skills

skill = get_skill("train")
print(skill.prompt)
print([domain.name for domain in list_domains()])
print([item.metadata.skill_id for item in search_skills("clean data")])
```

Browse the [complete skill catalog](docs/ALL_SKILLS.md).

## CLI

- `gncore list [skills|domains|categories]`
- `gncore search <terms> [--category <name>]`
- `gncore show <skill-id>`
- `gncore export (--skills <id>... | --specific <id> | --all) [--directory <path> | --output <file.zip>]`
- `gncore version`

## Development

```bash
python -m pip install -e ".[test]"
python -m pytest -q
python scripts/generate_skill_catalog.py
```

See [Architecture](ARCHITECTURE.md), [Usage](docs/USAGE.md), [API](docs/API.md), and [Developer Guide](docs/DEVELOPER.md).

## License

MIT. See [LICENSE](LICENSE).
