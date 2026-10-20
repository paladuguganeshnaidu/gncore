# Developer Guide

GNCore contains a curated skill catalog and tools for searching and exporting it. It intentionally does not include integrations that scan or modify assistant applications.

## Add or edit a skill

Add specialist definitions in `src/gncore/skills/library.py` or a domain workflow in `src/gncore/skills/domains.py`. Keep IDs stable, descriptions concise, and instructions scoped to one task. Use `validate_skill_definition()` and preserve the shared requirements for evidence, clear assumptions, safe boundaries, verification, and honest reporting.

Regenerate the full catalog after changing definitions:

```bash
python scripts/generate_skill_catalog.py
```

## CLI changes

The CLI is limited to `list`, `search`, `show`, `export`, and `version`. Listing, searching, and showing are read-only. `export` writes only the ZIP explicitly named by the caller. Do not add application detection, installation, MCP configuration, model calls, hidden network access, or persistent state.

## Verify changes

```bash
python -m pip install -e ".[test]"
python -m pytest -q
python -m compileall -q src tests
git diff --check
```

Keep tests focused on public API behavior, catalog integrity, portable output format, and the guarantee that catalog commands do not create application configuration.
