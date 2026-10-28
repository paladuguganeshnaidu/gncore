---
name: ai-engineering
description: "Build and evaluate LLM applications, retrieval systems, prompts, and model-assisted user workflows."
license: Apache-2.0 AND MIT
---

# GNCore Ai Engineering

## Select the work from the user's intent

Define the useful task, trusted inputs, retrieval sources, tool boundaries, latency and spending limits, and failure handling. Use representative positive, negative, adversarial, and ambiguous cases. Separate source evidence from model-generated claims and bound tool retries and external actions.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Evaluate task success, retrieval relevance, groundedness, permissions, failure recovery, latency, and cost against a baseline. Do not infer correctness from fluent output alone.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `llm-evaluation` | Measure an LLM feature with representative cases, explicit rubrics, failure analysis, and repeatable comparisons. |
| `llm-app` | Implement reliable LLM features with structured outputs, bounded tools, privacy, and graceful failure handling. |
| `rag` | Build a grounded retrieval workflow with traceable sources, chunking tests, and abstention on missing evidence. |
| `prompt-engineering` | Improve prompts against explicit tasks and evaluations while preserving tool and safety boundaries. |

## Focused procedures

### Evaluate an LLM Workflow (`llm-evaluation`)

Define user tasks, failure severity, and acceptance thresholds before changing prompts or models. Build a representative, privacy-safe eval set; include edge cases and adversarial inputs. Use deterministic checks where possible and blinded human review for subjective quality. Track model/version, prompt, tools, latency, and cost. Do not present small or synthetic evals as proof of safety or broad reliability.

### LLM Application Engineering (`llm-app`)

Inspect provider APIs and existing architecture. Validate structured outputs, bound tool permissions and iteration, handle timeouts/rate limits, and provide a useful fallback. Minimize sensitive prompt data and avoid logging secrets. Ground claims in retrieved evidence when using RAG, cite provenance, and distinguish model output from verified facts. Never execute generated code or external actions without an explicit authorization path.

### Retrieval-Augmented Generation (`rag`)

Inspect corpus rights, freshness, access controls, and query patterns. Preserve source IDs and metadata through chunking and retrieval; enforce permissions before generation. Evaluate retrieval recall and answer grounding separately using representative questions. Cite retrieved sources and abstain when evidence is insufficient. Avoid indexing secrets or restricted content; make reindexing bounded and reversible.

### Prompt Engineering (`prompt-engineering`)

Define desired behavior, failure modes, and a small representative evaluation set before editing. Make instructions concise, scoped, and testable; resolve conflicting priorities explicitly. Avoid brittle examples and hidden assumptions. Compare revisions on the same cases and include adversarial inputs. Never claim a prompt alone guarantees factuality, privacy, or safety.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [addyosmani/agent-skills / frontend-ui-engineering](research/addyosmani-agent-skills-frontend-ui-engineering/GUIDE.md): MIT.
- [affaan-m/ecc / ai-first-engineering](research/affaan-m-ecc-ai-first-engineering/GUIDE.md): MIT.
- [github/awesome-copilot / ai-prompt-engineering-safety-review](research/github-awesome-copilot-ai-prompt-engineering-safety-review/GUIDE.md): MIT.
- [langchain-ai/langchain-skills / eval-engineering](research/langchain-ai-langchain-skills-eval-engineering/GUIDE.md): MIT.
- [rohitg00/ai-engineering-from-scratch / start-learning](research/rohitg00-ai-engineering-from-scratch-start-learning/GUIDE.md): MIT.
- [langchain-ai/langchain-skills / langsmith-online-eval-engineering](research/langchain-ai-langchain-skills-langsmith-online-eval-engineering/GUIDE.md): MIT.
- [mastra-ai/mastra / react-best-practices](research/mastra-ai-mastra-react-best-practices/GUIDE.md): Apache-2.0.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
