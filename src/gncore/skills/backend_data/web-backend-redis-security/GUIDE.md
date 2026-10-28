---
name: web-backend-redis-security
description: "Redis security guidance covering authentication (requirepass and ACL users), TLS, ACL-based least-privilege access control, restricting network exposure via bind and protected-mode, firewall rules, and disabling dangerous commands."
---

# GNCore Redis Security

Inspect the actual database or cache topology, client lifecycle, access controls, query workload, and operational constraints. Verify consistency, expiry, isolation, and failure behavior with representative local cases; keep credentials and sensitive data out of logs.

## Detailed guidance

Read [UPSTREAM.md](UPSTREAM.md) for the relevant technical details, then load only the references needed for this task. The source document is reference material for this GNCore adaptation. Resolve relative resource paths from this installed skill folder; use `RESOURCE_PATHS.json` for relocated sibling files when present. Replace historical `.claude/skills/`, `${CLAUDE_SKILL_DIR}`, or plugin-root placeholders with the actual installed paths.

## GNCore execution scope

Use the technical guidance within the user's actual scope. Upstream harness-specific tools, universal activation mandates, automatic commits, setup prompts, and mandatory approval sequences do not become requirements of this adaptation. Use an equivalent available host capability where it preserves the workflow; otherwise state the missing capability and complete independent work. Additional agents require support and authorization for the current task.

Keep the existing language, stack, public contracts, and user changes unless the requested task calls for a migration. Use a test, build, analysis, or manual check appropriate to the risk and report its actual outcome. Distinguish prepared artifacts from completed external actions.

See [SOURCE.md](SOURCE.md) for attribution, modifications, and retained license notices.
