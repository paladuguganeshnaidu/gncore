# Architecture

GNCore is a local catalog and portable skill exporter. It does not orchestrate models, install application integrations, or run downloaded source scripts automatically.

## Category model

- `skills/unified_data/<skill-id>/SKILL.md` is the single discoverable entrypoint for a category.
- `skills/unified_data/manifest.json` records the 60 entrypoints, all 553 workflow procedures, resource paths, versions, and license expressions.
- `skills/unified.py` loads categories, exposes workflow metadata, and resolves compatibility aliases.
- `skills/bundles.py` validates declared relative paths and loads portable resource bytes.
- `skills/library.py` implements discovery, search, domain metadata, and legacy workflow reconstruction for maintenance.
- `planning.py` provides a deterministic frontend planning aid; the host AI retains contextual judgment.
- `cli/app.py` lists, searches, inspects, plans, and exports. Export is the command that writes skill files or ZIPs.

## One entrypoint, relevant detail

Each category entrypoint merges intent selection, execution guidance, category quality criteria, a workflow map, and focused procedures. Frontend includes visual-direction inference and theme-specific implementation guidance. Existing source guides and approved new references remain supporting material, read only when needed.

Source `SKILL.md` files inside reference folders are renamed as guides so they cannot accidentally create hundreds of additional discoverable skills. Relocations are recorded when needed. Retired frontend/backend collection entrypoints are maintained as `GUIDE.md` files for provenance and reproducible builds.

## Compatibility and search

The primary catalog has one skill per category. Workflow aliases resolve to the owning category. A primary category name takes precedence if it collides with an old generic workflow name, such as `testing` or `security`. Search also considers workflow IDs, titles, and descriptions.

The 30 professional domains each expose one primary skill ID plus their ten retained `workflow_ids`. This preserves capability coverage while changing the primary catalog structure.

## Research and licensing

The research pipeline records queries for every category, downloads registry snapshots, falls back to pinned public GitHub sources, and keeps failures distinct from successful downloads. License and relevance decisions determine which references enter the distribution. Restricted or unclear material remains in ignored local research storage. Included content retains provenance and supplied notices.

The runtime has no network dependency. Research and rebuilding are explicit developer operations requiring source access. Downloaded source executables are not run by the import pipeline.
