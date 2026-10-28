---
name: quality-assurance
description: "Audit accessibility and performance, plan tests, and connect requirements to verifiable acceptance evidence."
license: MIT
---

# GNCore Quality Assurance

## Select the work from the user's intent

Identify the requested audit or validation scope, supported environments, baseline, and acceptance criteria. Use measurable checks and representative user tasks. Distinguish an accessibility, performance, or test-strategy review from a whole-product certification.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Record commands, environments, observed outcomes, reproducible failures, and unperformed manual checks. Compare performance under the same conditions and tie findings to concrete behavior.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `accessibility-audit` | Inspect a user flow for keyboard, screen reader, visual, and cognitive accessibility barriers. |
| `performance-audit` | Find and verify the largest performance bottlenecks before changing code or infrastructure. |
| `test-strategy` | Choose a balanced test plan that catches important failures at the lowest practical level. |
| `requirements-to-tests` | Turn requirements into observable acceptance cases that cover success, failure, boundaries, and permissions. |

## Focused procedures

### Accessibility Audit (`accessibility-audit`)

Walk the actual flow using semantic structure, keyboard only, visible focus, zoom/reflow, labels, errors, and relevant assistive technology when available. Record reproducible steps, affected users, and evidence. Prioritize barriers by impact and task completion. Map findings to applicable criteria only when checked; do not claim full conformance from a partial audit.

### Performance Audit (`performance-audit`)

Capture a baseline under stated hardware, data, and load conditions. Profile before optimizing and identify the critical path. Change one bottleneck at a time, preserve correctness, and compare repeated measurements. Include tail latency and resource cost when relevant. Do not claim improvement without measured before/after evidence or scale workload beyond safe limits.

### Test Strategy (`test-strategy`)

Map changed behavior to risks and contracts. Prefer focused unit tests for logic, integration tests for boundaries, and a small number of end-to-end tests for critical journeys. Include failure paths, permissions, and data invariants. Avoid brittle implementation assertions and duplicated coverage. Report what is covered, what is unverified, and the exact commands run.

### Requirements to Acceptance Tests (`requirements-to-tests`)

Extract actors, preconditions, inputs, expected outcomes, and constraints. Rewrite vague statements as observable behaviors and identify contradictions or missing decisions. Cover normal, boundary, error, permission, and recovery paths. Link cases to requirement IDs where available. Do not treat implementation details as acceptance criteria unless they are contractual.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [daffy0208/ai-dev-standards / quality-assurance](research/daffy0208-ai-dev-standards-quality-assurance/GUIDE.md): MIT.
- [schneidenbach/skills / relentless-quality-assurance](research/schneidenbach-skills-relentless-quality-assurance/GUIDE.md): MIT.
- [schneidenbach/skills / relentless-quality-assurance-and-fixes](research/schneidenbach-skills-relentless-quality-assurance-and-fixes/GUIDE.md): MIT.
- [github/awesome-copilot / breakdown-test](research/github-awesome-copilot-breakdown-test/GUIDE.md): MIT.
- [jezweb/claude-skills / ai-image-generator](research/jezweb-claude-skills-ai-image-generator/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
