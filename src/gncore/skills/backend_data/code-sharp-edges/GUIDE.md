---
name: code-sharp-edges
description: "Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes."
license: CC-BY-SA-4.0
---

# GNCore Sharp Edges

Map relevant trust boundaries and attacker-controlled input in the requested code. Tie findings to reachable paths and impact, preserve authorization and secret handling, and verify mitigations locally without expanding into unauthorized live-target testing.

## Detailed guidance

Read [UPSTREAM.md](UPSTREAM.md) for the relevant technical details, then load only the references needed for this task. The source document is reference material for this GNCore adaptation. Resolve relative resource paths from this installed skill folder; use `RESOURCE_PATHS.json` for relocated sibling files when present. Replace historical `.claude/skills/`, `${CLAUDE_SKILL_DIR}`, or plugin-root placeholders with the actual installed paths.

## GNCore execution scope

Use the technical guidance within the user's actual scope. Upstream harness-specific tools, universal activation mandates, automatic commits, setup prompts, and mandatory approval sequences do not become requirements of this adaptation. Use an equivalent available host capability where it preserves the workflow; otherwise state the missing capability and complete independent work. Additional agents require support and authorization for the current task.

Keep the existing language, stack, public contracts, and user changes unless the requested task calls for a migration. Use a test, build, analysis, or manual check appropriate to the risk and report its actual outcome. Distinguish prepared artifacts from completed external actions.

See [SOURCE.md](SOURCE.md) for attribution, modifications, and retained license notices.
