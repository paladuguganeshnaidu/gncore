---
name: code-request-refactor-plan
description: "Plan a behavior-preserving refactor with explicit scope, sequencing, and regression checks."
---

# GNCore Request Refactor Plan

Inspect the current implementation, callers, and regression coverage. State the concrete maintainability problem and the observable behaviors that must remain unchanged. Propose a sequence of small changes with touched modules, compatibility boundaries, and checks for each step. Flag data migrations or API breaks explicitly. Deliver the requested plan; implement it only when implementation is within the user's request.

## Detailed guidance

See [SOURCE.md](SOURCE.md) for the verified missing source name and the original replacement's license.

## GNCore execution scope

Follow the actual request and available repository conventions; this workflow does not require an external plugin or a particular issue tracker.

Keep the existing language, stack, public contracts, and user changes unless the requested task calls for a migration. Use a test, build, analysis, or manual check appropriate to the risk and report its actual outcome. Distinguish prepared artifacts from completed external actions.

See [SOURCE.md](SOURCE.md) for attribution, modifications, and retained license notices.
