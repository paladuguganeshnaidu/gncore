# GNCore

GNCore is a portable Python library of reusable AI skills. Search the catalog, inspect a skill's instructions, or export one or more standard `SKILL.md` folders for use with an AI assistant.

**GNCore is a skills tool, not an orchestration or application-management tool.** It does not scan for AI apps, install or remove files in their configuration folders, configure MCP, run models, or trigger assistant actions. The host assistant loads a skill and provides its reasoning and tools.

## Install

```bash
python -m pip install gncore
```

## Discover and use skills

```bash
gncore list domains
gncore search "machine learning training"
gncore show train
gncore export --skills train evaluate --output ml-skills.zip
```

The ZIP contains a `SKILL.md` directory for each selected skill. Copy the skill folders to the skills directory documented by your assistant, then invoke them using the slash name when supported, such as `/train`. GNCore never writes to assistant directories.

Export the complete catalog if desired:

```bash
gncore export --all --output gncore-skills.zip
```

The Python API can be used directly:

```python
from gncore import get_skill, list_domains, search_skills

skill = get_skill("train")
print(skill.prompt)
print([domain.name for domain in list_domains()])
print([item.metadata.skill_id for item in search_skills("clean data")])
```

GNCore 5.0.0 includes 403 skills across 30 domain packs, with ten focused workflows per pack plus specialist skills. Browse the [complete skill catalog](docs/ALL_SKILLS.md).

## CLI

- `gncore list [skills|domains|categories]`
- `gncore search <terms> [--category <name>]`
- `gncore show <skill-id>`
- `gncore export (--skills <id>... | --all) --output <file.zip>`
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
