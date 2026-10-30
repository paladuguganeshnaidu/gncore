# GNCore Machine Learning: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

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

### Model Evaluation (`model-evaluation`)

Choose metrics from the real decision and class balance, not convenience. Keep tuning data separate from final test data, report sample counts and split rules, compare with a baseline, and inspect important error slices. Quantify uncertainty when feasible. Do not present a single score as proof of generalization or fairness.

### Feature Engineering Practice (`feature-engineering-practice`)

For each feature, define its meaning, availability time, source, missing-value semantics, and serving computation. Ensure it uses only information available at prediction time. Fit learned transforms on training data; preserve train/serve parity. Check leakage, drift, cardinality, and subgroup effects. Keep feature logic reproducible and document dropped or transformed columns.

### Time-Series Modeling (`time-series`)

Inspect frequency, time zone, gaps, revisions, horizon, and forecast origin. Use rolling or forward-chaining evaluation, never random splits. Compare with seasonal-naive baselines and ensure every feature is available at forecast time. Report horizon-specific error and uncertainty; avoid extrapolating beyond evidence. Preserve temporal ordering in preprocessing and backtests.
