# Release workflow

1. Review the source, ownership, migration, and research reports. Confirm that rejected sources are absent from the distribution and included notices remain intact.
2. Synchronize the package version in `pyproject.toml`, `version.py`, publishing workflow, and tests. Version 6.0.0 changes the primary catalog structure.
3. Regenerate the catalog. Verify 60 primary category skills, 553 retained workflows, and 30 professional domains with ten workflows each.
4. Run tests, source compilation, Markdown checks, skill validation, and `git diff --check`.
5. Build the wheel and source archive, run Twine checks, and smoke-test the wheel from a clean installation. Compare exported resource bytes with the source manifest.
6. Commit and push the reviewed branch. A branch push does not publish a package.
7. After release authorization, create the matching `v<version>` tag. Verify the publishing workflow and the public PyPI metadata before announcing a release.

The publishing workflow uses the `PYPI_API_TOKEN` secret in the `pypi` GitHub environment. Never place credentials in source or artifacts. The current task authorizes pushing the completed branch, not creating a publishing tag.
