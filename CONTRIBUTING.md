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
- Prefer explicit dataclasses and `Path`-based filesystem code.
- Avoid duplicating adapter logic outside the shared base class.
- Update tests when changing public commands or bundle layout.

## Documentation

Update the README and the relevant docs whenever you change the CLI, adapter contract, or bundled skill format.
