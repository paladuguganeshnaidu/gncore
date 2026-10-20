# Verification Guide

GNCore installs reusable skill instructions into supported assistant applications. It does not run model training, call AI providers, or execute skills by itself. Use the checks below to verify the library and an installation.

## Verify the source checkout

From the repository root, install the test extra and run the test suite:

```bash
python -m pip install -e ".[test]"
python -m pytest -q
python -m compileall -q src tests
```

Check the catalog and CLI:

```bash
python -m gncore version
python -m gncore list domains
python -m gncore list skills
python -m gncore search "clean data"
```

The catalog integrity tests verify that skill IDs are unique, definitions validate, the 30 domain packs each contain ten skills, and the expected workflows are discoverable.

## Verify an installed assistant target

Install a small selection to a project workspace, then validate the managed output. Replace `vscode-codex` with a key shown by `gncore list apps`.

```bash
gncore install company-ceo train word-draft pdf-extract ppt-create --apps vscode-codex --scope workspace
gncore validate --apps vscode-codex --scope workspace
```

Open the target assistant in that workspace and invoke one installed skill if the assistant supports native skill commands. Review its output and checks yourself. Filesystem validation confirms GNCore wrote its managed skill files; it does not confirm every assistant UI loads them or that an AI response is correct.

For release checks, see [docs/RELEASE.md](docs/RELEASE.md).
