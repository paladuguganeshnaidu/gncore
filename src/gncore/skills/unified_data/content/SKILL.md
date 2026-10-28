---
name: content
description: "Plan, adapt, translate, and maintain content around audience needs, factual accuracy, and channel constraints."
license: MIT
---

# GNCore Content

## Select the work from the user's intent

Identify audience, purpose, desired action, brand voice, source material, and content lifecycle. Preserve meaning and approved terminology while adapting structure, depth, language, and distribution format. Treat localization as a context-sensitive adaptation rather than literal substitution.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Check facts, claims, links, tone, readability, terminology, and culturally dependent examples. Separate drafts from published content.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `content-strategy` | Plan clear, consistent content around a specific audience, task, evidence, and publishing goal. |
| `documentation-translation` | Adapt technical content across languages while preserving product meaning, UI limits, and verified terminology. |

## Focused procedures

### Content Strategy (`content-strategy`)

Identify audience, intent, channel, evidence, and desired action. Organize content around reader questions, use plain language, and preserve source attribution. Flag claims needing verification and avoid unsupported health, legal, or financial promises. Provide an outline, publication checklist, and success measure appropriate to the channel.

### Technical Localization (`documentation-translation`)

Identify source locale, target locale, audience, and approved glossary. Preserve code, placeholders, links, units, legal meaning, and formatting tokens. Flag ambiguous source text instead of guessing. Use locale-appropriate dates and numbers; do not translate identifiers. Verify UI length and right-to-left behavior when relevant.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [microsoft/azure-skills / azure-aigateway](research/microsoft-azure-skills-azure-aigateway/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
