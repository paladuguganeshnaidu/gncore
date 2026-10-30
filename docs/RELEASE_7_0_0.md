# GNCore 7.0.0 production release

## Scope

GNCore 7.0.0 ships 30 adaptive developer guides, 374 workflows and 1,660 declared resources. Original GNCore writing remains MIT-licensed; retained reference guides and tools keep their source-specific licenses. This version includes the documented major catalog migration from the older mixed catalog.

The website adds a themed benchmark highlight on its landing page and a detailed `/benchmarks/` page. Seven chart families, raw denominators, an accessible all-category table, CSV/JSON exports and PDF reports make the measurements inspectable.

## Claims and measurement boundaries

The historical IDE pilot is dated 29 October 2026 and predates this release. Its revised trial recorded 168/173 applicable review criteria in VS Code and 147/173 in Antigravity across 29 fully reviewed non-UI categories. Published references and the baseline use the same tasks within each host. Review was unblinded, the trial was not repeated, and the model was not fixed in Copilot Auto. These observations do not establish current-release accuracy, causal improvement or vendor-wide superiority.

The all-category chart retains unmeasured frontend browser outcomes. Security results describe six seeded findings and four safe controls in a manual fixture, with no executed exploit. Code fixtures, later exploratory failures, routing diagnostics, instruction-file sizes and warm local timings are separate measures. Withdrawn development quality comparisons and adaptive follow-up scores are excluded from the historical pilot totals.

## Promotion sequence

1. Rebuild catalog/evaluation inputs and benchmark assets; reconcile public values to retained evidence. Check all website links and redirects, the desktop/mobile presentation, navigation, filtering and downloads.
2. Run local package tests and the configured multi-platform CI matrix on the exact source revision. A skipped check remains skipped.
3. Build the source archive, build the wheel from that archive, check distribution metadata and contents, and install outside the checkout. Export and verify all resources from the accepted wheel.
4. Record the accepted source revision, artifact names, SHA-256 digests, CI run and verification results in a release record. Create the GitHub release with those exact bytes.
5. Publish those Python artifacts through the existing PyPI trusted-publishing workflow. Verify the registry version and distribution hashes.
6. Generate the published website with the verified release state, push the existing `gncoresite` production branch, and verify the Cloudflare Pages deployment plus representative public routes.

The owner authorized publication in the current release request. This document describes the release process; the release record, registry and deployment state establish which steps actually completed.

## Recovery

Keep the previous website production revision and historical package release. If publication is partial, stop promotion and report the completed destinations. Never overwrite registry files. A package fix requires a new version; a faulty website can revert to its previous source revision. Installation migration keeps recovery inventories and backups and preserves custom or untracked skill files.

## Reproduction

Use `python scripts/build_catalog.py --check`, `python scripts/build_evaluations.py --check`, `python -m gncore audit`, and `python -m gncore evaluate --validate` for structural checks. The benchmark figure builder is `scripts/build_public_benchmarks.py`; its optional reporting dependencies are Matplotlib and NumPy. Public data snapshots contain source fingerprints. The full historical experimental evidence lives in the Git repository, while source distributions retain the website-ready chart data.
