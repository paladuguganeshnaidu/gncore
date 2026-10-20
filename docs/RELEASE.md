# Release Workflow

1. Confirm the package version is synchronized in `pyproject.toml` and `src/gncore/version.py`; add release notes to `CHANGELOG.md`.
2. Check the catalog invariants: 403 unique skills, 30 domain packs, and 10 workflows per pack.
3. Run the test suite, source compilation, and `git diff --check`.
4. Build wheel and source distributions, verify them with Twine, and install the wheel in a fresh virtual environment.
5. Push the verified release commit to `main`, then push the matching `v<version>` tag. The tag starts `.github/workflows/publish.yml`, which reruns tests, build, and wheel smoke checks before publishing to PyPI.
6. Confirm the workflow succeeds and verify the released version on PyPI before announcing it.

A PyPI release requires the repository's `pypi` environment and `PYPI_API_TOKEN` secret. Do not publish an artifact if the workflow reports failed tests or missing credentials.
