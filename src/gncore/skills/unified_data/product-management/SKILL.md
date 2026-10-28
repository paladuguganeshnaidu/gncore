---
name: product-management
description: "Discover product opportunities and turn them into requirements, experiments, roadmaps, and launch decisions."
license: MIT
---

# GNCore Product Management

## Select the work from the user's intent

Start with the user problem and current workaround. Select discovery, specification, prioritization, experimentation, launch, feedback, or lifecycle work from the requested outcome. Distinguish customer observations from proposed solutions and measures of outcome from counts of shipped features.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Link scope and acceptance cases to the problem. Check edge cases, instrumentation, accessibility, dependencies, success measures, and a decision rule for the next iteration.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `product-opportunity` | Turn customer and business evidence into a scoped product opportunity. |
| `product-requirements` | Write testable product requirements and acceptance criteria for a scoped feature. |
| `product-roadmap` | Build an outcome-led roadmap that exposes dependencies, confidence, and trade-offs. |
| `product-discovery-sprint` | Plan a short discovery cycle that resolves the riskiest product assumptions. |
| `product-prioritization` | Prioritize feature requests using customer value, evidence, cost, and strategic fit. |
| `product-experiment` | Design product experiments with a clear hypothesis, metric, guardrails, and decision rule. |
| `product-launch` | Coordinate launch readiness across product, engineering, support, sales, and communications. |
| `product-feedback` | Synthesize product feedback into traceable themes without overstating frequency. |
| `product-lifecycle` | Assess adoption, retention, quality, and investment choices for an existing product. |
| `product-metrics` | Define a product metric with an unambiguous event, population, denominator, and owner. |

## Focused procedures

### Product Opportunity Brief (`product-opportunity`)

Define the user, unmet need, current workaround, evidence, strategic fit, expected outcome, alternatives, and top unknowns. Separate interview observations from assumptions and propose the cheapest useful validation.

### Product Requirements (`product-requirements`)

Specify actors, outcomes, constraints, functional behavior, edge cases, accessibility, privacy, and success measures. Flag conflicts and unresolved decisions; avoid prescribing implementation unless it is a product constraint.

### Product Roadmap (`product-roadmap`)

Connect roadmap themes to strategic outcomes and customer evidence. Show confidence, sequence, dependencies, capacity, and deliberate non-goals; avoid presenting speculative dates as commitments.

### Product Discovery Sprint (`product-discovery-sprint`)

State the decision to make, riskiest assumptions, research method, participant criteria, prototype, evidence threshold, and decision date. Keep discovery methods ethical and avoid claiming validation from weak samples.

### Feature Prioritization (`product-prioritization`)

Normalize requests into underlying needs, estimate reach and impact with confidence, include engineering and maintenance cost, and identify opportunity cost. Record the rationale and revisit when evidence changes.

### Product Experiment Design (`product-experiment`)

Define eligible population, assignment unit, exposure, primary outcome, guardrails, duration, sample constraints, and stopping rule. Check for interference, privacy concerns, and instrumentation defects before interpreting results.

### Product Launch Readiness (`product-launch`)

Confirm target users, release scope, feature flags, migration, documentation, support coverage, analytics, rollback, and launch owner. Mark every gate as verified, blocked, or not applicable with evidence.

### Customer Feedback Synthesis (`product-feedback`)

Deduplicate evidence, preserve source and segment, distinguish frequency from severity, and include counterexamples. Link themes to decisions and note sampling bias and unrepresented users.

### Product Lifecycle Review (`product-lifecycle`)

Review cohort behavior, customer value, reliability, support load, cost, strategic relevance, and alternatives. Recommend sustain, improve, migrate, or sunset with customer impact and a reversible transition plan.

### Product Metrics Definition (`product-metrics`)

Specify metric formula, unit, time window, source events, exclusions, segmentation, owner, and known biases. Check that the metric reflects user value and cannot easily be improved by harmful behavior.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [affaan-m/ecc / returns-reverse-logistics](research/affaan-m-ecc-returns-reverse-logistics/GUIDE.md): MIT.
- [alirezarezvani/claude-skills / product-skills](research/alirezarezvani-claude-skills-product-skills/GUIDE.md): MIT.
- [freshtechbro/claudedesignskills / react-three-fiber](research/freshtechbro-claudedesignskills-react-three-fiber/GUIDE.md): MIT.
- [wondelai/skills / improve-business](research/wondelai-skills-improve-business/GUIDE.md): MIT.
- [zeropointrepo/youtube-skills / youtube-full](research/zeropointrepo-youtube-skills-youtube-full/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
