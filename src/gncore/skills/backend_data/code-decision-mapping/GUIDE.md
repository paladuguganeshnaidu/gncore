---
name: code-decision-mapping
description: "Map unresolved implementation decisions, dependencies, options, and evidence needed to choose."
---

# GNCore Decision Mapping

List decisions that materially affect the requested outcome. For each, record options, constraints, dependencies, reversibility, owner, and the evidence needed to choose. Resolve choices already implied by repository conventions; ask about only decisions that affect scope or correctness. Deliver a decision map and a concrete next implementation step, without treating every preference as a blocker.

## Detailed guidance

See [SOURCE.md](SOURCE.md) for the verified missing source name and the original replacement's license.

## GNCore execution scope

Follow the actual request and available repository conventions; this workflow does not require an external plugin or a particular issue tracker.

Keep the existing language, stack, public contracts, and user changes unless the requested task calls for a migration. Use a test, build, analysis, or manual check appropriate to the risk and report its actual outcome. Distinguish prepared artifacts from completed external actions.

See [SOURCE.md](SOURCE.md) for attribution, modifications, and retained license notices.
