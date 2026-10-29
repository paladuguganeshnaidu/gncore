# Contributing

## Development setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[test,skills]"
```

## Validation

Run the test suite before opening a pull request:

```bash
python -m pytest -q
python -m compileall -q -x '(frontend_data|backend_data|unified_data)' src tests
```

## Code style

- Keep changes small and typed.
- Keep the public API focused on the skill catalog and portable skill format.
- Do not add application detection, configuration edits, model calls, or orchestration features.
- Update tests when changing public commands or exported `SKILL.md` structure.

## Documentation

Update the README and relevant docs when changing the CLI or portable skill format.

Canonical guidance lives in `catalog/categories.json`. Run `scripts/build_catalog.py --check`, `scripts/build_evaluations.py --check` and `gncore audit` alongside relevant tests. Preserve one primary entrypoint per active developer category and an explicit migration outcome for retired/moved IDs. Source notices and applicable licenses remain intact. See `docs/DEVELOPER.md` for offline authoring and release preparation.
