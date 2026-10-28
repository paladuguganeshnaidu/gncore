---
name: research
description: "Synthesize evidence into a clear answer with source provenance, uncertainty, and decision-relevant conclusions."
license: MIT
---

# GNCore Research

## Select the work from the user's intent

Define the research question, inclusion scope, dates, and evidence standard. Prefer primary sources and compare claims across independent evidence. Separate source facts, interpretation, estimates, and recommendations; preserve disagreements rather than smoothing them away.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Verify citations and source dates, check that each material claim is supported, and state missing evidence, methodological limits, and what would change the conclusion.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `research-synthesis` | Synthesize supplied or sourced evidence with provenance, disagreement, and uncertainty kept visible. |

## Focused procedures

### Research Synthesis (`research-synthesis`)

Translate the question into scope, date range, and evidence standard. Prioritize primary sources; record citation details and distinguish source claims from your synthesis. Compare methods and note conflicting findings, limitations, and missing evidence. Do not invent citations, quotations, or consensus. State when evidence is insufficient or likely outdated.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [mattpocock/skills / research](research/mattpocock-skills-research/GUIDE.md): MIT.
- [lllllllama/rigorpilot-skills / ai-research-explore](research/lllllllama-rigorpilot-skills-ai-research-explore/GUIDE.md): MIT.
- [lllllllama/rigorpilot-skills / ai-research-reproduction](research/lllllllama-rigorpilot-skills-ai-research-reproduction/GUIDE.md): MIT.
- [lllllllama/rigorpilot-skills / analyze-project](research/lllllllama-rigorpilot-skills-analyze-project/GUIDE.md): MIT.
- [lllllllama/rigorpilot-skills / explore-code](research/lllllllama-rigorpilot-skills-explore-code/GUIDE.md): MIT.
- [lllllllama/rigorpilot-skills / safe-debug](research/lllllllama-rigorpilot-skills-safe-debug/GUIDE.md): MIT.
- [lllllllama/rigorpilot-skills / explore-run](research/lllllllama-rigorpilot-skills-explore-run/GUIDE.md): MIT.
- [lllllllama/rigorpilot-skills / run-train](research/lllllllama-rigorpilot-skills-run-train/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
