---
name: research-market-intelligence
description: "Investigate markets, competitors, customers, literature, surveys, and evidence with traceable sources."
license: MIT
---

# GNCore Research and Market Intelligence

## Select the work from the user's intent

Define the question, scope, time window, decision, and evidence threshold. Prefer primary sources and separate observations from estimates and interpretations. Select source audit, literature review, market sizing, customer or competitor research, evidence mapping, survey, briefing, or monitoring work.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Check source dates and provenance, corroborate material claims, show methodology and uncertainty, and state what the available evidence cannot establish.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `research-question` | Frame a researchable question with scope, definitions, evidence criteria, and a useful decision. |
| `research-source-audit` | Evaluate sources for authority, method, date, provenance, conflicts, and fitness for a claim. |
| `research-literature-review` | Synthesize a literature set with methods, findings, disagreement, and evidence gaps visible. |
| `research-market-size` | Estimate a market using transparent bottom-up or top-down assumptions and sensitivity ranges. |
| `research-customer` | Combine customer evidence and market signals into actionable, bounded insights. |
| `research-competitor` | Prepare a dated competitor brief from verifiable product, pricing, and positioning evidence. |
| `research-evidence-map` | Organize claims, sources, strength, disagreement, and missing evidence for a decision area. |
| `research-survey` | Design a survey with neutral wording, clear constructs, representative sampling, and privacy safeguards. |
| `research-brief` | Turn research into a concise, sourced brief with answer, confidence, implications, and open questions. |
| `research-monitor` | Track a defined topic for material source changes without overwhelming users with routine noise. |

## Focused procedures

### Research Question Design (`research-question`)

Define population, concept, time period, geography, inclusion criteria, and decision use. Identify likely source types, bias, and what evidence would disconfirm the working hypothesis.

### Source Quality Audit (`research-source-audit`)

Trace each source to its publisher and method, check date and scope, inspect primary evidence, note funding/conflicts, and match strength of wording to quality of support.

### Literature Review (`research-literature-review`)

Use explicit search and inclusion criteria, extract population/method/outcome/limitations, compare study quality, and avoid vote-counting or treating association as causation.

### Market Sizing (`research-market-size`)

Define product, customer, geography, time, and revenue basis; cite input sources; avoid overlapping segments; cross-check methods; and present ranges instead of unsupported point precision.

### Customer and Market Research (`research-customer`)

Define segment and sampling, preserve interview or survey provenance, separate stated preference from behavior, include counterexamples, and state what the sample cannot represent.

### Competitive Research Brief (`research-competitor`)

Use public or supplied sources, record observation date, compare like-for-like plans, separate product facts from inferred strategy, and identify uncertainties that affect the decision.

### Evidence Map (`research-evidence-map`)

Break broad claims into testable propositions, link each to its strongest source, grade source quality transparently, record contradictions, and mark unsupported claims plainly.

### Survey Design and Review (`research-survey`)

Map each question to a construct and decision, test comprehension, avoid double-barreled or leading items, define response options and sampling, and document nonresponse limits.

### Research Brief (`research-brief`)

Answer the stated question first, cite close to claims, distinguish established findings from synthesis, include limitations and contrary evidence, and identify decision implications and evidence gaps.

### Research Update Monitor (`research-monitor`)

Set scope, source list, review cadence, change threshold, and freshness. Compare new primary evidence with prior conclusions and report only verified material changes and their implications.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [mattpocock/skills / research](research/mattpocock-skills-research/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
