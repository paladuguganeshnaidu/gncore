---
name: code-qa
description: "Validate a software change against acceptance criteria and reproduce observable regressions."
---

# GNCore Qa

Translate the feature brief or bug report into observable acceptance cases. Exercise the main journey and relevant permission, failure, empty, concurrency, or recovery cases. Record exact setup, inputs, commands, and outcomes. For a failure, isolate a reproducible case and distinguish implementation defects from environment limitations. Fix and retest when requested; report checks not performed rather than treating missing evidence as a pass.

## Detailed guidance

See [SOURCE.md](SOURCE.md) for the verified missing source name and the original replacement's license.

## GNCore execution scope

Follow the actual request and available repository conventions; this workflow does not require an external plugin or a particular issue tracker.

Keep the existing language, stack, public contracts, and user changes unless the requested task calls for a migration. Use a test, build, analysis, or manual check appropriate to the risk and report its actual outcome. Distinguish prepared artifacts from completed external actions.

See [SOURCE.md](SOURCE.md) for attribution, modifications, and retained license notices.
