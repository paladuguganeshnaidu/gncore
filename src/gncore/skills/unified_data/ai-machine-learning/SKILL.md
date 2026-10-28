---
name: ai-machine-learning
description: "Frame, train, evaluate, improve, and monitor machine-learning or LLM systems with leakage-safe evidence."
license: MIT
---

# GNCore AI and Machine Learning

## Select the work from the user's intent

Define the target, intended use, data availability, metric, baseline, and compute constraints. Choose preprocessing, training, evaluation, improvement, LLM evaluation, retrieval, fine-tuning, or release monitoring. Keep training, tuning, and held-out evaluation boundaries explicit.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Check splits, leakage, baselines, reproducibility, segment errors, uncertainty, cost, and serving constraints. Never invent a completed training or evaluation run.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `ml-problem-framing` | Decide whether a machine learning approach fits the task, data, constraints, and failure costs. |
| `ml-dataset-audit` | Audit dataset provenance, schema, representativeness, label quality, leakage, and split strategy. |
| `ml-preprocessing-pipeline` | Build deterministic preprocessing that prevents leakage and preserves training-to-serving parity. |
| `ml-model-train` | Implement a reproducible model training run with configuration, baseline, checkpoints, and evaluation. |
| `ml-model-evaluation` | Evaluate model quality, uncertainty, subgroup behavior, and representative errors against a baseline. |
| `ml-model-improvement` | Improve a model through controlled experiments with a fixed evaluation protocol and root-cause analysis. |
| `ml-llm-evaluation` | Evaluate an LLM feature with representative tasks, rubrics, adversarial cases, latency, and cost. |
| `ml-rag` | Build and evaluate retrieval-augmented answers with source access controls and abstention. |
| `ml-finetuning` | Assess fine-tuning suitability and prepare a controlled, leakage-safe fine-tuning workflow. |
| `ml-release-monitor` | Prepare a model release with provenance, compatibility, rollback, and drift monitoring gates. |

## Focused procedures

### ML Problem Framing (`ml-problem-framing`)

Define prediction or generation target, users, action, baseline, data rights, latency/cost limits, error costs, and non-ML alternatives. Set measurable acceptance and stop criteria before choosing a model.

### ML Dataset Audit (`ml-dataset-audit`)

Profile source, labels, duplicates, missingness, time coverage, sensitive fields, and collection process. Group splits by user/entity/time where needed; preserve raw data and document exclusion rules.

### ML Preprocessing Pipeline (`ml-preprocessing-pipeline`)

Fit learned transforms only on training data, persist the pipeline, validate schema and edge cases, and compare transformed distributions across splits. Track every row or column excluded and why.

### ML Model Training Run (`ml-model-train`)

Inspect framework and hardware, establish baseline, lock data split and metric, set seed and run metadata, and checkpoint safely. Do not launch expensive compute or overwrite artifacts without explicit user authorization.

### ML Model Evaluation (`ml-model-evaluation`)

Use a held-out split untouched by tuning, task-appropriate metrics, confidence estimates where practical, and error slices. State sample limits and do not infer safety or production readiness from aggregate scores.

### ML Improvement Loop (`ml-model-improvement`)

Rank hypotheses from observed errors, change one factor at a time, track config and artifacts, compare against baseline, diagnose regressions, fix or revert, then rerun focused and regression evaluations until gates pass or a blocker remains.

### LLM Evaluation Suite (`ml-llm-evaluation`)

Create a privacy-safe eval set, use deterministic checks where possible, score subjective quality with a rubric, and record model/prompt/tool versions. Separate benchmark performance from real-world safety claims.

### RAG Grounding Workflow (`ml-rag`)

Preserve source identity and permissions through ingestion and retrieval; measure retrieval separately from answer quality; cite evidence; test missing, conflicting, stale, and unauthorized sources; abstain when support is insufficient.

### Model Fine-Tuning Plan (`ml-finetuning`)

Compare prompt, retrieval, and fine-tuning alternatives; verify dataset rights and de-identification; deduplicate and split before training; define eval and rollback. Require approval before paid training or external data upload.

### Model Release and Monitoring (`ml-release-monitor`)

Link code, data, config, artifact, eval, serving contract, and owner. Gate release on tested rollback and monitoring for quality, latency, cost, and drift; do not deploy without explicit authorization.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [ljagiello/ctf-skills / ctf-ai-ml](research/ljagiello-ctf-skills-ctf-ai-ml/GUIDE.md): MIT.
- [affaan-m/ecc / ml-adoption-playbook](research/affaan-m-ecc-ml-adoption-playbook/GUIDE.md): MIT.
- [dotnet/skills / technology-selection](research/dotnet-skills-technology-selection/GUIDE.md): MIT.
- [k-dense-ai/scientific-agent-skills / scikit-learn](research/k-dense-ai-scientific-agent-skills-scikit-learn/GUIDE.md): MIT.
- [k-dense-ai/scientific-agent-skills / aeon](research/k-dense-ai-scientific-agent-skills-aeon/GUIDE.md): MIT.
- [k-dense-ai/scientific-agent-skills / shap](research/k-dense-ai-scientific-agent-skills-shap/GUIDE.md): MIT.
- [langchain-ai/deepagents / cuml-machine-learning](research/langchain-ai-deepagents-cuml-machine-learning/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
