# Phase-two release preparation

Candidate: **7.0.0rc1**. This is a major catalog migration and an explicit prerelease. The source, wheel/source archive, portable skill ZIP and website preview must agree on 30 categories and 374 workflows.

## Prepared scope

Thirty developer categories replace the mixed catalog. New dedicated areas cover neural networks, deep learning, vision, NLP, MLOps, databases, native/embedded/distributed systems, performance, observability and technical research. The migration ledger accounts for 553 earlier workflows. Original references retain their authorship and terms.

## Publication stages after owner approval

1. **GitHub source:** push the prepared `codex/phase2-developer-skills` branch. Run the configured platform/runtime matrix against the exact commit and resolve failures before tagging. Merge the accepted release commit into the default branch so the manual publishing workflow is available.
2. **GitHub release:** create `v7.0.0rc1` as a prerelease and attach the accepted wheel, source archive, skill ZIP, release notes and SHA-256 manifest. Do not rebuild different bytes for another destination.
3. **PyPI:** dispatch `publish.yml` for the exact accepted version/ref with explicit owner confirmation; it downloads the GitHub assets and checks SHA-256 instead of rebuilding. Publish only the verified wheel/source artifacts through the existing project publisher. Prefer the configured trusted-publishing identity; do not put credentials in source. Verify [public metadata](https://pypi.org/project/gncore/) and file hashes before calling the version available. PyPI explains the required identity/permission setup in [its trusted-publishing guide](https://docs.pypi.org/trusted-publishers/using-a-publisher/).
4. **Website:** the `gncoresite` repository supplies the existing Cloudflare Pages site. Its prepared preview uses the same manifest, updated commands/catalog, migration redirects and labeled candidate state. After package/GitHub verification, generate the publication form, push the approved website commit, verify Cloudflare deployment and exercise representative public routes.

The new source has not been pushed, tagged or uploaded by preparation. The live website is unchanged. Approval should name the candidate version and destinations; it authorizes the concrete reviewed artifacts rather than an unspecified future change.

## Rollback and observations

Keep the previous website/source commit. Preserve installation inventories/backups and custom retired folders. A published PyPI file is immutable; if a published candidate is faulty, stop promotion, consider yanking it with owner approval and prepare a corrected version instead of overwriting it.

The observed public package during preparation was 5.1.0; the earlier 6.0 source branch was not a public release. A future stable 7.0.0 promotion needs acceptance of prerelease feedback and updated verification, not just a version-number edit.

## Release notes

- Focus the library on developer work: 30 categories, 374 workflows and six capability groups.
- Preserve 319 technical workflows, rewrite 116 repeated procedures, and add 55 original workflows.
- Retire 234 nondeveloper workflows with explicit migration outcomes.
- Add dedicated neural-network/deep-learning/vision/NLP/MLOps and native/embedded/distributed systems guidance.
- Add offline reproducible authoring, source/resource digests, full-category evaluation scenarios, explainable routing and safe managed retirement.
- Synchronize the GNCore website catalog, installation commands and migration paths with the package.

See [verification evidence](PHASE2_VERIFICATION.md) before approving publication. Complete agent outputs for every scenario and unavailable hardware/provider integrations are not certified by structural checks.
