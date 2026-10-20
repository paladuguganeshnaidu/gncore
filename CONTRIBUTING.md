# Contributing

## Development setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[test]
```

## Validation

Run the test suite before opening a pull request:

```bash
python -m pytest -q
python -m compileall src tests
```

## Code style

- Keep changes small and typed.
- Keep the public API focused on the skill catalog and portable skill format.
- Do not add application detection, configuration edits, model calls, or orchestration features.
- Update tests when changing public commands or exported `SKILL.md` structure.

## Documentation

Update the README and relevant docs when changing the CLI or portable skill format.
