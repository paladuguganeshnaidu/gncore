---
name: analytics
description: "Define and evaluate product analytics, instrumentation, funnels, retention, and decision metrics."
license: MIT
---

# GNCore Analytics

## Select the work from the user's intent

Start with the decision and user behavior to measure. Specify events, entities, properties, time windows, eligibility, identity rules, and denominators. Inspect instrumentation before interpreting changes and distinguish acquisition, activation, engagement, retention, and revenue questions.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Check event completeness, duplicate or delayed events, cohort definitions, tracking changes, selection bias, and whether a metric can be gamed.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `product-analytics` | Define product metrics and event instrumentation that answer a decision without collecting unnecessary data. |

## Focused procedures

### Product Analytics (`product-analytics`)

Start with the decision and user outcome, then define event grain, actor, timestamp, properties, denominator, and exclusions. Check identity stitching, consent, retention, and duplicate events. Prefer a small event schema with stable names and versioning. Validate counts end to end and document known blind spots. Avoid collecting sensitive attributes without a clear, approved need.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [coreyhaines31/marketingskills / analytics](research/coreyhaines31-marketingskills-analytics/GUIDE.md): MIT.
- [coreyhaines31/marketingskills / analytics-tracking](research/coreyhaines31-marketingskills-analytics-tracking/GUIDE.md): MIT.
- [amplitude/mcp-marketplace / discover-analytics-patterns](research/amplitude-mcp-marketplace-discover-analytics-patterns/GUIDE.md): MIT.
- [amplitude/mcp-marketplace / add-analytics-instrumentation](research/amplitude-mcp-marketplace-add-analytics-instrumentation/GUIDE.md): MIT.
- [samber/developer-relations-skills / devrel-analytics](research/samber-developer-relations-skills-devrel-analytics/GUIDE.md): MIT.
- [getcargohq/cargo-skills / cargo-analytics](research/getcargohq-cargo-skills-cargo-analytics/GUIDE.md): MIT.
- [nomadamas/k-skill / lck-analytics](research/nomadamas-k-skill-lck-analytics/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
