# GNCore AI Engineering: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Evaluate an LLM Workflow (`llm-evaluation`)

Define user tasks, failure severity, and acceptance thresholds before changing prompts or models. Build a representative, privacy-safe eval set; include edge cases and adversarial inputs. Use deterministic checks where possible and blinded human review for subjective quality. Track model/version, prompt, tools, latency, and cost. Do not present small or synthetic evals as proof of safety or broad reliability.

### LLM Application Engineering (`llm-app`)

Inspect provider APIs and existing architecture. Validate structured outputs, bound tool permissions and iteration, handle timeouts/rate limits, and provide a useful fallback. Minimize sensitive prompt data and avoid logging secrets. Ground claims in retrieved evidence when using RAG, cite provenance, and distinguish model output from verified facts. Never execute generated code or external actions without an explicit authorization path.

### Retrieval-Augmented Generation (`rag`)

Inspect corpus rights, freshness, access controls, and query patterns. Preserve source IDs and metadata through chunking and retrieval; enforce permissions before generation. Evaluate retrieval recall and answer grounding separately using representative questions. Cite retrieved sources and abstain when evidence is insufficient. Avoid indexing secrets or restricted content; make reindexing bounded and reversible.

### Prompt Engineering (`prompt-engineering`)

Define desired behavior, failure modes, and a small representative evaluation set before editing. Make instructions concise, scoped, and testable; resolve conflicting priorities explicitly. Avoid brittle examples and hidden assumptions. Compare revisions on the same cases and include adversarial inputs. Never claim a prompt alone guarantees factuality, privacy, or safety.

### Tool contracts and bounded agents (`ai-tool-contracts`)

Validate tool arguments/results with explicit schemas, enforce caller authority and bound steps, time and cost. Separate reasoning from side-effect execution. Replay malformed tool outputs, injection attempts, tool timeouts and exhausted budgets against local fixtures.

### Retrieval and grounding evaluation (`ai-retrieval-evaluation`)

Evaluate retrieval recall/permission filtering independently from answer grounding. Keep source IDs through chunking, include unanswerable questions and inspect citations. Use the same corpus/query set for before/after comparison and avoid treating citation presence as proof of support.
