# Maintainer workflow

Use Python 3.10+ and the repository's existing environment. The catalog has no required third-party runtime dependency.

1. Edit `catalog/categories.json` for category decisions/procedures and explicit retained resource paths. This is the authoritative authoring input, not the historical phase-one import scripts.
2. Preserve reference bytes/notices and record intentional source changes. Do not execute imported helpers to inspect their license or install a skill.
3. Run `python scripts/build_catalog.py`; use `--check` in CI to detect drift. Hashes cover every declared resource and the generated entrypoint.
4. Update concrete cases in `catalog/evaluation_specs.py` or `catalog/base_evaluations.json`, then run `python scripts/build_evaluations.py`.
5. Run relevant tests, the full regression suite, `gncore audit`, format validation, package builds and clean artifact checks.
6. Run `python scripts/generate_skill_catalog.py` and `python scripts/build_website.py` to synchronize docs and website data. The default website is a labeled noindex candidate preview.

Normal rebuilds are offline and do not rely on `.work`. Retired importer scripts are historical records under `archive/phase-one-tools/`; they are not supported authoring commands. The phase-one Git commit records excluded research and retired professional content without shipping it to developer projects.

Changing generated files alone will fail reproducibility checks. Helpers have independent runtime requirements; static parsing is not a claim that every dependency/device/tool is installed. Keep completed checks and unavailable evidence explicit.

Publication requires the owner's approval after the concrete artifact/checksum/website preview is available. See [release preparation](PHASE2_RELEASE.md).
