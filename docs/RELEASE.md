# Release Workflow

1. Synchronize the package version in `pyproject.toml`, `src/gncore/version.py`, and `.github/workflows/publish.yml`; document changes in `CHANGELOG.md`.
2. Regenerate `docs/ALL_SKILLS.md` and check the catalog: 403 unique skills, 30 domains, ten workflows per domain.
3. Run tests, source compilation, and `git diff --check`.
4. Build the wheel and source distribution, verify both with Twine, and smoke-test the wheel in a clean environment.
5. Push the reviewed commit and matching `v<version>` tag. The tag starts the PyPI publishing workflow.
6. Confirm the workflow succeeded and verify the released package metadata on PyPI.

The package publishing workflow reads `PYPI_API_TOKEN` from the `pypi` GitHub environment. Keep the credential in GitHub's secret store, never in the repository. Never announce a release until the upload and public package version are confirmed.
