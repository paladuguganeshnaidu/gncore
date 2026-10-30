# GNCore MLOps: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Reproducible ML Experiments (`experiment-tracking`)

Capture the source revision, dataset/version, configuration, seed, dependencies, model identifier, metrics, and artifact location. Keep secrets out of logs. Make repeated runs distinguishable and avoid overwriting artifacts. Use the repository's existing tracker; add a new service only when requested.

### Model Serving and Inference APIs (`model-serving`)

Trace model loading and inference lifecycle, validate inputs and output shapes, set appropriate timeouts and resource limits, and preserve version identity. Handle cold starts and model errors explicitly. Do not deploy, expose endpoints, or change production configuration unless requested. Measure latency and memory before claiming capacity.

### MLOps and Model Release (`mlops`)

Trace training data, code, dependencies, model artifact, evaluation, and serving contract. Define reproducible build metadata, compatibility checks, rollback path, and monitoring for drift and failures. Keep credentials outside artifacts. Do not deploy, promote, or alter production traffic without explicit authorization. Separate offline evidence from live performance and define an owner for alerts.

### Machine Learning Experiment Tracking (`ml-experiment-tracking`)

Define the question and baseline before changing code. Record data version, split, code revision, config, seed, environment, metrics, and artifact path for every run. Compare like with like and account for randomness. Keep experiments isolated and avoid overwriting outputs. Do not introduce a tracking service or upload sensitive data without approval.

### Model Documentation (`model-card`)

Use only verified project evidence for training data, method, metrics, and provenance. State intended and excluded uses, evaluation setup, subgroup coverage, limitations, monitoring, and update cadence. Mark unknowns plainly. Do not infer consent, representativeness, fairness, or regulatory status without evidence.

### Edge and Hardware-Constrained ML (`hardware-ml`)

Identify target processor, runtime, memory, latency, power, and accuracy requirements. Measure an unoptimized baseline on representative inputs. Compare quantization or compression with task metrics and worst-case behavior; verify supported operators and numerical drift. Keep original artifacts and provide a rollback path. Do not claim deployment readiness from desktop measurements.

### Model artifact and provenance (`mlops-artifact-contract`)

Bundle model and preprocessing state with input schema, dependency versions, data/split identity and verified evaluation. Hash files and round-trip the bundle in a clean environment. Keep credentials and unnecessary training records outside the artifact.

### Prediction service contract (`mlops-serving-contract`)

Validate feature names/order, dtype, missingness and batch bounds before inference. Use the artifact's exact preprocessing and test predictions against an offline fixture. Define load failures, timeouts and incompatible model/schema errors without silently changing predictions.

### Drift and model monitoring (`mlops-drift-monitoring`)

Separate input drift, label/target changes, prediction drift and service reliability. Define reference windows, delayed-label availability, thresholds and an accountable response. Test a synthetic shifted fixture; do not label input drift alone as measured accuracy degradation.

### Model promotion and rollback (`mlops-promotion-rollback`)

Compare candidate and baseline on the same accepted evaluation set and compatibility checks. Prepare canary/shadow criteria, immutable model identities and a tested rollback path. Keep actual production promotion and traffic changes pending deployment authorization.
