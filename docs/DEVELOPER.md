# Developer guide

## Edit category behavior

Maintain the GNCore-authored category descriptions, decision guidance, and quality criteria in `scripts/category_blueprints.py`. Frontend art direction and workflow guidance live in `scripts/frontend_playbook.md`; deterministic planning cases live in `planning.py` and its tests.

`scripts/build_unified_categories.py` merges category guidance and the legacy workflow inventory, preserves existing source references, applies license/relevance decisions to new candidates, and writes the 60 category entrypoints and manifest. The runtime reads the committed data directly; normal installation does not require a rebuild or network access.

## Research and rebuild

Install the optional Python `skills` extra for YAML parsing and use authenticated GitHub access where needed. All source downloads are treated as inert data.

The research scripts record queries, candidates, snapshots or immutable revisions, file hashes, unavailable sources, and supplied notices under ignored `.work/category-research/`. `download_category_candidates.py` searches all categories and downloads all returned candidates. `recover_category_sources.py` falls back to public GitHub source trees for registry failures.

Keep restricted and unclear-license material out of distribution. Preserve authorship, notices, and applicable share-alike terms for included material. The public research reports record source identities and review decisions without redistributing rejected content.

```bash
python scripts/download_category_candidates.py
python scripts/recover_category_sources.py
python scripts/build_unified_categories.py
python scripts/generate_skill_catalog.py
python -m pytest -q
```

For a fresh research workspace, capture the legacy inventory from `gncore.skills.library.legacy_skills()` or run `research_categories.py` to initialize it before the full candidate pipeline. Earlier frontend/backend builders maintain retired reference guides; they are not primary skill installers.

## Validate changes

Check capability preservation across all 553 workflow IDs, exactly 60 discoverable entrypoints, alias collisions, exports, resource paths, source notices, and representative planning behavior. Run the skill-creator validator when available. Build the distributions, check metadata, and install the wheel into a clean directory before release work.

Upstream helper runtimes are independent from GNCore's supported Python versions. Compile and test GNCore's own code separately from vendored supporting tools, and disclose unperformed execution checks.
