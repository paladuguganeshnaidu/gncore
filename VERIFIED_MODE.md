# Verification Guide

GNCore packages skill instructions; the host assistant supplies the model and tools. Verify the catalog and exported content locally:

```bash
python -m pip install -e ".[test]"
python -m pytest -q
python -m compileall -q src tests
python -m gncore version
python -m gncore list domains
python -m gncore search "clean data"
python -m gncore show train
python -m gncore export --skills train evaluate --output skills.zip
```

The tests check unique valid skill definitions, 30 domains with ten workflows apiece, discovery and search, and portable ZIP contents. Inspect an exported `SKILL.md` and then use the host application's documented method to load it. GNCore does not verify whether an assistant loaded a skill or whether a model response is accurate.

For release checks, see [docs/RELEASE.md](docs/RELEASE.md).
