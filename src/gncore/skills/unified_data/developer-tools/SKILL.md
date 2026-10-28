---
name: developer-tools
description: "Design and improve command-line interfaces with predictable commands, output, exit codes, and safe file behavior."
license: Apache-2.0 AND MIT
---

# GNCore Developer Tools

## Select the work from the user's intent

Inspect current CLI conventions, scripts, callers, and platform support. Define argument grammar, help, stdout/stderr behavior, machine-readable output, exit codes, and mutation boundaries. Keep commands composable and avoid hidden state or implicit destructive behavior.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Test representative success, invalid input, missing files, paths with spaces, duplicate selections, and error output. Verify actual written paths and cross-platform assumptions.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `cli-design` | Design command-line tools with predictable arguments, clear errors, safe defaults, and scriptable output. |

## Focused procedures

### CLI Engineering (`cli-design`)

Inspect established command patterns and automation needs. Use explicit options, stable exit codes, actionable errors, and non-interactive behavior for scripts. Make destructive actions opt-in and support dry-run when useful. Keep stdout machine-readable when promised and send diagnostics to stderr. Test help, invalid input, and representative success/failure cases.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [samber/developer-relations-skills / devrel-analytics](research/samber-developer-relations-skills-devrel-analytics/GUIDE.md): MIT.
- [jeffallan/claude-skills / cli-developer](research/jeffallan-claude-skills-cli-developer/GUIDE.md): MIT.
- [jeffallan/claude-skills / mcp-developer](research/jeffallan-claude-skills-mcp-developer/GUIDE.md): MIT.
- [openai/skills / chatgpt-apps](research/openai-skills-chatgpt-apps/GUIDE.md): Apache-2.0.
- [browserbase/skills / agent-experience](research/browserbase-skills-agent-experience/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
