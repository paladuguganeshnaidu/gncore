---
name: machine-learning
description: "Develop reproducible machine-learning workflows from data preparation and training to evaluation, optimization, and serving."
license: Apache-2.0 AND MIT
---

# GNCore Machine Learning

## Select the work from the user's intent

Identify target, data grain, split strategy, baseline, framework, hardware, and compute budget. Fit transforms on training data, preserve held-out evaluation, and control experiments with explicit configuration and data versions. Use error analysis to choose the next experiment.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Check leakage, tensor or schema contracts, class imbalance, metric choice, baseline comparisons, reproducibility, segment errors, and serving cost. State runs not executed and metrics not measured.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `machine-learning` | Develop a scoped machine learning feature, from data inspection and baseline selection through evaluation. |
| `model-training` | Set up or improve a reproducible model training run with clear configuration, checkpoints, and evaluation. |
| `train` | Build and run a reproducible model training workflow with a baseline, tracked configuration, and held-out evaluation. |
| `preprocess` | Design a repeatable preprocessing pipeline that preserves schema, prevents leakage, and records transformations. |
| `evaluate` | Evaluate model quality with leakage-safe splits, task-appropriate metrics, baselines, and error analysis. |
| `improve` | Find evidence-based model improvements through error analysis and controlled experiments against a fixed baseline. |
| `data-preparation` | Prepare reproducible model datasets while preventing leakage and preserving provenance. |
| `feature-engineering` | Build features that are valid at prediction time and reproducible across training and inference. |
| `fine-tuning` | Plan or implement a parameter-efficient or full fine-tuning workflow with controlled data and cost. |
| `model-evaluation` | Evaluate model quality with valid splits, suitable metrics, uncertainty, and error analysis. |
| `experiment-tracking` | Make model experiments traceable across code, data, configuration, environment, and artifacts. |
| `model-serving` | Package model inference behind a reliable API with validation, resource limits, and observable behavior. |
| `pytorch-training` | Implement PyTorch training loops with correct device, optimizer, checkpoint, and evaluation handling. |
| `tensorflow-training` | Build TensorFlow/Keras training workflows with explicit data, callbacks, and evaluation behavior. |
| `deep-learning` | Develop deep learning code with explicit tensor shapes, stable optimization, and reproducible evaluation. |
| `nlp` | Build NLP pipelines that respect language, label quality, privacy, and task-specific evaluation. |
| `computer-vision` | Build vision workflows with robust image handling, leakage-safe splits, and task-appropriate evaluation. |
| `mlops` | Package, register, and monitor models with reproducible artifacts and explicit release gates. |
| `ml-experiment-tracking` | Make model experiments comparable with consistent splits, metrics, configuration, and artifact provenance. |
| `feature-engineering-practice` | Create leakage-safe, interpretable features that match the model's serving-time information. |
| `time-series` | Analyze and forecast time-indexed data with temporal splits, leakage controls, and useful uncertainty. |
| `model-card` | Document a model's intended use, data provenance, evaluation, limitations, and deployment assumptions. |
| `hardware-ml` | Adapt inference to constrained hardware using measured latency, memory, and accuracy tradeoffs. |

## Focused procedures

### Machine Learning Workflow (`machine-learning`)

Help with the machine learning task the user describes. Inspect available data, code, and constraints before choosing an approach. Explain the baseline and evaluation metric, preserve reproducibility, and avoid leaking target information. Keep changes limited to the requested workflow. Do not download data, train expensive models, alter production pipelines, or replace existing modeling choices without explicit direction. Report assumptions, results, and limitations.

### Model Training (`model-training`)

Help carry out the model training task the user describes. Inspect the current training code and hardware/runtime constraints first. Prefer a small reproducible configuration, explicit seeds where supported, documented data splits, and an evaluation step. Do not launch long or costly training jobs, overwrite checkpoints, change datasets, or modify deployment settings unless the user explicitly requests it. Make the smallest relevant code change and explain how to run the training command.

### Train a Machine Learning Model (`train`)

Inspect the dataset, task, framework, hardware, and existing pipeline before editing. Establish a simple baseline and define the target metric first. Split by entity or time when random splitting would leak information; fit preprocessing on training data only. Make seeds, hyperparameters, data version, and checkpoints explicit. Implement the requested training path, but do not launch costly or long-running jobs, download data, overwrite checkpoints, or alter production resources without clear authorization. Report the exact command, observed metrics, artifacts, and limitations; never fabricate a completed run.

### Preprocess Machine Learning Data (`preprocess`)

Inspect schema, units, missingness, target definition, split strategy, and downstream model assumptions. Create deterministic transformations fit only on training data and reuse them unchanged on validation/test data. Preserve source data; make output paths explicit and avoid silent row drops, target leakage, or irreversible coercion. Test edge cases and document each transformation, resulting schema, and unresolved data-quality issue.

### Evaluate a Model (`evaluate`)

Confirm the prediction target, intended use, split boundaries, class balance, and decision costs. Compare against a simple baseline using metrics suited to the task; report uncertainty or repeated-split variation where practical. Keep test data untouched during tuning. Inspect segment performance and representative errors without exposing sensitive examples. Distinguish measured results from estimates, state data and compute limits, and never claim fairness, robustness, or production readiness from one aggregate score.

### Improve a Machine Learning Model (`improve`)

Start from the current baseline, metric, split, and failure examples. Rank likely improvements by evidence, expected impact, and cost; change one factor per experiment where possible. Keep the evaluation set fixed and avoid tuning on test data. Track config, seed, data version, metrics, and compute. Do not run expensive experiments, replace a working model, or change serving behavior without authorization. Report wins, regressions, uncertainty, and the next best experiment.

### ML Data Preparation (`data-preparation`)

Inspect schema, label definition, missingness, duplicates, time boundaries, and source provenance before transformation. Split data before fitting learned preprocessing; keep related users, groups, or time periods together when required. Never silently drop rows or labels. Record transformations and counts so the run can be reproduced.

### Feature Engineering (`feature-engineering`)

For every candidate feature, state its source, type, availability time, and transformation. Reject features unavailable at prediction time. Fit statistics only on training data, keep train/serve transformations consistent, and compare against a baseline using the same split and metric. Add complexity only when evaluation supports it.

### Model Fine-Tuning (`fine-tuning`)

Confirm the base model, license constraints, data rights, objective, validation method, hardware, and budget. Inspect existing training code and use the least costly method that can answer the goal. Keep validation data separate, record model and tokenizer revisions, and save to a new checkpoint path. Do not launch paid or long-running jobs without explicit approval.

### Model Evaluation (`model-evaluation`)

Choose metrics from the real decision and class balance, not convenience. Keep tuning data separate from final test data, report sample counts and split rules, compare with a baseline, and inspect important error slices. Quantify uncertainty when feasible. Do not present a single score as proof of generalization or fairness.

### Reproducible ML Experiments (`experiment-tracking`)

Capture the source revision, dataset/version, configuration, seed, dependencies, model identifier, metrics, and artifact location. Keep secrets out of logs. Make repeated runs distinguishable and avoid overwriting artifacts. Use the repository's existing tracker; add a new service only when requested.

### Model Serving and Inference APIs (`model-serving`)

Trace model loading and inference lifecycle, validate inputs and output shapes, set appropriate timeouts and resource limits, and preserve version identity. Handle cold starts and model errors explicitly. Do not deploy, expose endpoints, or change production configuration unless requested. Measure latency and memory before claiming capacity.

### PyTorch Training (`pytorch-training`)

Inspect the installed PyTorch version and existing dataset/model interfaces. Set train/eval modes correctly, move batches and model to the same device, clear gradients, and use inference mode for evaluation. Save checkpoints atomically to a new path and include enough state to resume when requested. Start with a tiny smoke run before a full run.

### TensorFlow and Keras Training (`tensorflow-training`)

Inspect TensorFlow/Keras version and data pipeline semantics. Keep preprocessing consistent, avoid validation leakage, configure callbacks explicitly, and save to a new artifact path. Check output shapes and a small batch first. Do not assume GPU availability or start a long training run without user approval.

### Deep Learning Engineering (`deep-learning`)

Inspect framework versions, model inputs/outputs, tensor shapes, precision, memory limits, and baseline. Verify loss/activation compatibility, masking, gradient flow, and train/eval modes. Keep validation data out of gradient updates and log checkpoints with configuration. Do not launch GPU-intensive jobs or replace checkpoints without approval. Diagnose with a tiny batch before scaling.

### Natural Language Processing (`nlp`)

Inspect languages, tokenization, labels, privacy constraints, and intended use. Establish a simple baseline and split by user/document when duplicates could leak. Evaluate per-class and per-language behavior, not only one aggregate metric. Minimize retention of raw text and redact sensitive examples. Treat generated labels as noisy; document model and data provenance. Do not claim factuality or safety from benchmark scores alone.

### Computer Vision (`computer-vision`)

Inspect image formats, dimensions, labels, duplicate/near-duplicate groups, and provenance. Split by source, person, or scene where needed to prevent leakage. Normalize consistently and validate augmentations preserve labels. Use task-appropriate metrics and inspect representative errors. Protect biometric and personal imagery; do not download, retain, or expose images without authorization.

### MLOps and Model Release (`mlops`)

Trace training data, code, dependencies, model artifact, evaluation, and serving contract. Define reproducible build metadata, compatibility checks, rollback path, and monitoring for drift and failures. Keep credentials outside artifacts. Do not deploy, promote, or alter production traffic without explicit authorization. Separate offline evidence from live performance and define an owner for alerts.

### Machine Learning Experiment Tracking (`ml-experiment-tracking`)

Define the question and baseline before changing code. Record data version, split, code revision, config, seed, environment, metrics, and artifact path for every run. Compare like with like and account for randomness. Keep experiments isolated and avoid overwriting outputs. Do not introduce a tracking service or upload sensitive data without approval.

### Feature Engineering Practice (`feature-engineering-practice`)

For each feature, define its meaning, availability time, source, missing-value semantics, and serving computation. Ensure it uses only information available at prediction time. Fit learned transforms on training data; preserve train/serve parity. Check leakage, drift, cardinality, and subgroup effects. Keep feature logic reproducible and document dropped or transformed columns.

### Time-Series Modeling (`time-series`)

Inspect frequency, time zone, gaps, revisions, horizon, and forecast origin. Use rolling or forward-chaining evaluation, never random splits. Compare with seasonal-naive baselines and ensure every feature is available at forecast time. Report horizon-specific error and uncertainty; avoid extrapolating beyond evidence. Preserve temporal ordering in preprocessing and backtests.

### Model Documentation (`model-card`)

Use only verified project evidence for training data, method, metrics, and provenance. State intended and excluded uses, evaluation setup, subgroup coverage, limitations, monitoring, and update cadence. Mark unknowns plainly. Do not infer consent, representativeness, fairness, or regulatory status without evidence.

### Edge and Hardware-Constrained ML (`hardware-ml`)

Identify target processor, runtime, memory, latency, power, and accuracy requirements. Measure an unoptimized baseline on representative inputs. Compare quantization or compression with task metrics and worst-case behavior; verify supported operators and numerical drift. Keep original artifacts and provide a rollback path. Do not claim deployment readiness from desktop measurements.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [mindrally/skills / machine-learning](research/mindrally-skills-machine-learning/GUIDE.md): Apache-2.0.
- [sickn33/agentic-awesome-skills / machine-learning-ops-ml-pipeline](research/sickn33-agentic-awesome-skills-machine-learning-ops-ml-pipeline/GUIDE.md): MIT.
- [microsoft/azure-skills / azure-compute](research/microsoft-azure-skills-azure-compute/GUIDE.md): MIT.
- [huggingface/skills / transformers-js](research/huggingface-skills-transformers-js/GUIDE.md): Apache-2.0.
- [ljagiello/ctf-skills / ctf-ai-ml](research/ljagiello-ctf-skills-ctf-ai-ml/GUIDE.md): MIT.
- [affaan-m/ecc / mle-workflow](research/affaan-m-ecc-mle-workflow/GUIDE.md): MIT.
- [affaan-m/ecc / ml-adoption-playbook](research/affaan-m-ecc-ml-adoption-playbook/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
