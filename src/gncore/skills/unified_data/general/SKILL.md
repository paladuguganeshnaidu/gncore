---
name: general
description: "Clarify, plan, implement, review, document, or prepare a scoped project outcome."
license: Apache-2.0 AND MIT
---

# GNCore General

## Select the work from the user's intent

Select the actual deliverable first: brief, architecture, implementation, review, tests, documentation, or release preparation. Scale planning to uncertainty and risk. Keep unresolved decisions explicit without turning routine choices into blockers.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Trace each acceptance criterion to an artifact or observed check. Separate prepared changes from published, merged, or deployed changes.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `requirements` | Collects scope, constraints, acceptance criteria, and open questions before implementation starts. |
| `architecture` | Defines system boundaries, interfaces, and implementation constraints. |
| `implementation` | Writes production-grade code with minimal duplication and explicit types. |
| `review` | Finds defects, regressions, and missing coverage before release. |
| `testing` | Designs and validates tests for the changed slice. |
| `security` | Assesses secrets handling, unsafe file access, and privilege boundaries. |
| `documentation` | Produces concise user and developer documentation that matches the implementation. |
| `release` | Coordinates versioning, packaging, and verification for shipping. |

## Focused procedures

### Requirements Clarifier (`requirements`)

Your job is to turn a rough request into a precise implementation brief.
Ask for missing constraints, surface risks early, capture acceptance criteria, and refuse to guess on critical decisions.
Prefer short, direct questions and summarize the result as a checklist the next skill can execute.

### Architecture Designer (`architecture`)

Convert requirements into a clean, typed architecture.
Define modules, ownership boundaries, data flow, invariants, and failure handling.
Choose the simplest design that can be extended without duplicating logic.

### Implementation Builder (`implementation`)

Implement the agreed design directly, keep code explicit and typed, and avoid speculative abstractions.
Make the smallest change that satisfies the contract, then verify it with targeted tests or checks.

### Code Reviewer (`review`)

Look for correctness issues, API mismatches, risky assumptions, and missing tests.
State concrete findings first, then give a short summary of residual risk.

### Testing Specialist (`testing`)

Create targeted unit and integration tests that fail before the fix and pass after it.
Prefer clear fixture setup and assertions that verify the observable behavior, not implementation details.

### Security Reviewer (`security`)

Check for unsafe writes, path traversal, secret leakage, and privilege escalation.
Treat file-system code as hostile-input code and require explicit validation.

### Documentation Writer (`documentation`)

Document the actual command surface, file layout, and operational behavior.
Avoid marketing language and keep examples runnable.

### Release Manager (`release`)

Ensure packaging metadata is correct, the distribution is reproducible, and release notes reflect the shipped behavior.
Confirm that the repository is publishable before marking the release complete.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [software-mansion/argent / argent-react-native-app-workflow](research/software-mansion-argent-argent-react-native-app-workflow/GUIDE.md): Apache-2.0.
- [somnio-software/somnio-ai-tools / workflow-builder](research/somnio-software-somnio-ai-tools-workflow-builder/GUIDE.md): MIT.
- [everyinc/compound-engineering-plugin / ce-plan](research/everyinc-compound-engineering-plugin-ce-plan/GUIDE.md): MIT.
- [siviter-xyz/dot-agent / software-engineer](research/siviter-xyz-dot-agent-software-engineer/GUIDE.md): MIT.
- [zlanqing/codex-claude-academic-skills / office-academic-skill](research/zlanqing-codex-claude-academic-skills-office-academic-skill/GUIDE.md): MIT.
- [smallnest/goal-workflow / smell](research/smallnest-goal-workflow-smell/GUIDE.md): MIT.
- [joellewis/finance_skills / financial-planning-workflow](research/joellewis-finance-skills-financial-planning-workflow/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
