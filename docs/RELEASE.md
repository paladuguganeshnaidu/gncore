# Release Workflow

1. Update the version in `src/gncore/version.py` and `pyproject.toml` together.
2. Run `python -m pytest -q` and `python -m compileall src tests`.
3. Verify the CLI with `gncore list apps` and `gncore activate --apps cursor`.
4. Update `CHANGELOG.md` with the shipping notes.
5. Build a source distribution and wheel with Hatchling.
6. Publish the artifacts to PyPI after the CI workflow passes.

The release process should never ship a version that fails validation or leaves the installer in an inconsistent state.
