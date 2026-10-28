---
name: code-insecure-defaults
description: "Find unsafe configuration defaults and fail-open behavior in application code and deployment configuration."
---

# GNCore Insecure Defaults

Trace configuration values from defaults and environment parsing into sensitive operations. Look for development credentials, debug exposure, permissive origin or network rules, disabled verification, unchecked authorization, and fail-open error handling. Demonstrate the reachable unsafe condition in a local test where practical. Propose a secure default and an explicit opt-in for legitimate development cases; preserve a documented migration path and retest both allowed and denied behavior.

## Detailed guidance

See [SOURCE.md](SOURCE.md) for the verified missing source name and the original replacement's license.

## GNCore execution scope

Follow the actual request and available repository conventions; this workflow does not require an external plugin or a particular issue tracker.

Keep the existing language, stack, public contracts, and user changes unless the requested task calls for a migration. Use a test, build, analysis, or manual check appropriate to the risk and report its actual outcome. Distinguish prepared artifacts from completed external actions.

See [SOURCE.md](SOURCE.md) for attribution, modifications, and retained license notices.
