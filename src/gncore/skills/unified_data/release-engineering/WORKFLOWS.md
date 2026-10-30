# GNCore Release Engineering: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Release Readiness Review (`release-readiness`)

Inspect the release scope, version, changelog, artifacts, compatibility matrix, known issues, and rollback plan. Verify required checks and distinguish passed from skipped. Check migrations and external dependencies for rollout sequencing. Do not publish or deploy without authorization. End with a go/no-go recommendation tied to evidence and unresolved risks.

### Artifact integrity and promotion (`release-artifact-integrity`)

For each intended wheel/source/platform target, build from the accepted tree, inspect metadata/resources/entrypoints, record hashes and install outside the checkout. For Python distributions, verify the wheel built from the produced source archive. Promote the same verified bytes to authorized destinations; distinct platform artifacts may legitimately differ. Retain source/CI/artifact identity and report unavailable destination verification rather than implying publication.
