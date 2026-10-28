---
name: design
description: "Conduct UX research and build design systems around real tasks, semantic tokens, components, and accessible interaction."
license: Apache-2.0 AND MIT
---

# GNCore Design

## Select the work from the user's intent

Choose research or system design from the requested deliverable. Ground decisions in user tasks and existing product constraints. For research, define questions, participants, and evidence limits; for systems, connect primitive tokens to semantic roles and component state contracts.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Check evidence quality, consistency, keyboard and assistive-technology behavior, themes, content edge cases, and whether a component can be used predictably by its callers.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `ux-research` | Plan and synthesize ethical user research that ties observations to product decisions. |
| `design-system` | Extend a design system with accessible tokens and reusable components that fit existing conventions. |

## Focused procedures

### UX Research (`ux-research`)

Define the decision and research question before selecting a method. Recruit representative participants, use neutral prompts, obtain consent, and minimize personal data. Distinguish direct observation from interpretation; preserve contradictory evidence. Summarize themes with confidence and limitations, then map findings to testable design changes. Never invent participant quotes or counts.

### Design System Engineering (`design-system`)

Inspect existing tokens, components, naming, accessibility states, and consumers. Reuse established primitives; add the smallest composable API. Define default, hover, focus, disabled, error, and responsive behavior as relevant. Validate contrast and interaction semantics. Document migration or deprecation when a public component contract changes.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [anthropics/skills / frontend-design](research/anthropics-skills-frontend-design/GUIDE.md): Apache-2.0.
- [designed-by-ai/skills / design-mobile-apps](research/designed-by-ai-skills-design-mobile-apps/GUIDE.md): MIT.
- [mattpocock/skills / grill-me](research/mattpocock-skills-grill-me/GUIDE.md): MIT.
- [mattpocock/skills / grill-with-docs](research/mattpocock-skills-grill-with-docs/GUIDE.md): MIT.
- [mattpocock/skills / prototype](research/mattpocock-skills-prototype/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
