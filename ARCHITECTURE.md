# Architecture

GNCore is a standard-library Python catalog and portable skill exporter. Host agents supply models, tools and permissions.

`catalog/categories.json` is the canonical authoring input for 30 developer entrypoints and 374 workflows. `scripts/build_catalog.py` deterministically renders `src/gncore/skills/unified_data/`, including per-resource SHA-256 digests and entrypoint hashes. Retained attributed references are versioned files beside their owner skill. A routine offline build performs no research and uses no hidden cache.

Each `SKILL.md` holds task selection, completion boundaries and the workflow map. The agent reads only the matching section of the declared, hashed `WORKFLOWS.md` resource, then any needed source references. Keeping that resource beside the entrypoint preserves relative reference paths. This reduces unconditional entrypoint bytes; it does not establish model-token, cost or latency savings.

`catalog/category-completion-checks.json` supplies category-specific correctness boundaries. Ten reviewed procedure refinements retain their prior/current SHA-256 values and reasons in `quality_revision` and the migration ledger's `quality_revisions`. Historical preserved/rewritten/retired accounting stays intact; current procedure preservation is verified against the applicable revision.

`skills/library.py` provides discovery, six developer domains and migration-aware lookup. `skills/unified.py` exposes workflow metadata and lookup aliases. `skills/migration.json` accounts for all phase-one IDs. Primary and historical category aliases take precedence over colliding generic workflow names.

`skills/bundles.py` checks packaged entrypoint/resource hashes and path boundaries before export. `installation.py` preflights, stages and verifies directory changes, records inventories, retains backups and restores interrupted switches. Retiring old categories is explicit and preserves modified/unmanaged content.

`planning.py` implements the frontend direction helper. `routing.py` provides local explainable developer hints and optional explicit context. Neither calls a model or executes an agent.

`evaluation.py` validates corpus/recorded artifacts and leaves semantic and external-tool checks pending. `catalog/evaluation_specs.py` plus `base_evaluations.json` rebuild the 90-case corpus offline. `audit.py` checks merge accounting, hashes, entrypoint links and Python helper syntax without executing imported helpers.

`benchmarks/improvement-cycle-1/PROTOCOL.md` describes the separate adaptive regression block. Raw four-condition responses, explicit manual decisions, executed fixtures, browser observations and focused corrections live under `web-results/improvement-cycle-1`. Historical IDE evidence remains separate. A task-check percentage is neither production reliability nor a claim of vendor superiority.

`scripts/build_website.py` builds a static Cloudflare Pages preview from the same accepted manifest. `web/assets/` preserves GNCore's existing brand assets. Publication is separate from generation.
