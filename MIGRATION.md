# Migration to GNCore 7

This major catalog revision replaces 60 mixed categories with 30 developer categories. The 30 earlier professional-domain packs are replaced by six developer capability groups; `list_domains()` now returns groups containing multiple category IDs, not ten-workflow business packs.

## What changed

- 319 technical workflow procedures remain; 116 shared procedures are rewritten with task-specific instructions.
- 55 original workflows add neural-network debugging, deep-learning operations, vision/NLP, MLOps, native/embedded systems, database correctness, performance, observability and distributed-system failure handling.
- 234 nondeveloper workflows are retired with explicit reasons. They are not silently redirected to unrelated capabilities.
- Overlapping technical categories consolidate: `software-engineering` and `general` to `code-build`; `quality-engineering`/`quality-assurance` to `testing`; `security` to `cybersecurity`; `cloud`/`devops`/`operations` to `cloud-devops-sre`; `research` to `developer-research`.
- ML modes move to dedicated categories: `nlp` to `natural-language-processing`, `computer-vision` to its own category, deep-learning/framework modes to `deep-learning`, and serving/artifact modes to `mlops`.

[migration.json](src/gncore/skills/migration.json) accounts for all 553 phase-one workflow IDs and all 60 category IDs. [The audit](docs/PHASE2_MERGE_AUDIT.json) records previous and revised procedure hashes. Historical source remains at Git commit `b9877fd`; unused heuristic-only research bundles and redundant raw collections are removed from the active distribution.

## Update a managed project

```bash
gncore export --all --prune-retired --dry-run
gncore export --all --prune-retired
gncore verify
```

Preflight happens before changes. Pruning requires an inventory-managed, byte-identical old folder; customized or untracked retired folders remain in place and are reported. Selected active categories with edited managed files stop the update. Full backups and recovery journals are retained. For old installations without a recorded inventory, preserve custom work and review the old folders explicitly before a fresh install.

Legacy technical lookups remain where their target is active. Canonical category names and historical category aliases take precedence over generic workflow IDs: `security` resolves to `cybersecurity`, while its former generic procedure is also retained inside `code-build`. `list_workflows()` describes procedure ownership; a lookup collision can therefore resolve to a broader category. Removed business IDs raise a retirement error.

The public candidate version is `7.0.0rc1` only after publication approval and verification. Prepared local files are not evidence of a PyPI release.
