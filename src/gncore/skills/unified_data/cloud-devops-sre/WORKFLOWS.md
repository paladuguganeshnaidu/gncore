# GNCore Cloud, DevOps and SRE: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Cloud Architecture (`cloud-architecture`)

Inspect the current provider, workload, data classification, traffic, recovery targets, team skills, and budget. Prefer managed services only when their operational and cost tradeoffs fit. Define trust boundaries, failure modes, backup/restore, and observability. Do not create resources or expose endpoints without authorization. Mark estimates and assumptions; avoid claiming compliance without evidence.

### Cloud Cost Optimization (`cost-optimization`)

Use billing and utilization evidence with a stated period and scope. Separate idle waste, rightsizing, storage lifecycle, and architecture changes. Estimate savings and service risk; identify reversibility and validation. Avoid deleting resources, reducing capacity, or purchasing commitments without approval. Measure after a change and retain rollback options.

### Cloud Architecture Review (`cloud-architecture-review`)

Clarify workload and provider, data classification, traffic, recovery targets, team skills, and budget. Trace failure domains, IAM, data movement, backup/restore, observability, and cost; mark assumptions.

### Infrastructure as Code (`cloud-infrastructure-code`)

Use existing modules and provider versions, isolate environments, validate state and drift, inspect the generated plan, and protect secrets. Do not apply or destroy live infrastructure without explicit approval.

### CI/CD Pipeline (`cloud-ci-cd`)

Trace build provenance, secrets, permissions, test stages, artifact promotion, deployment strategy, and recovery. Verify the pipeline on a safe branch or environment and preserve protected release checks.

### Container Build and Hardening (`cloud-container`)

Inspect runtime and platform needs; minimize base and copied files, run non-root, pin controlled inputs, exclude secrets, scan outputs, and test health/shutdown behavior. Do not publish images without permission.

### Kubernetes Workload Review (`cloud-kubernetes`)

Check probes, requests/limits, replicas, disruption, security context, service-account scope, network exposure, rollout and rollback. Validate rendered manifests and never apply to a live cluster without approval.

### SLO and Error Budget (`cloud-slo`)

Choose user-centric good/total events, window, target, exclusions, and data source. Validate measurement and alerting; use error budgets to guide decisions without hiding user impact.

### Service Observability (`cloud-observability`)

Start from user failure modes, define low-cardinality signals, preserve trace context, exclude secrets and personal data, and set sampling/retention. Verify telemetry against a known request and cost.

### SRE Incident Management (`cloud-incident`)

Set incident roles and timeline, assess user impact, state mitigation hypothesis, preserve evidence, and verify recovery against SLO signals. Record root-cause contributors without blame and track corrective work.

### Capacity and Load Plan (`cloud-capacity`)

Profile representative workload, identify saturation point and dependencies, model peak and failure scenarios, and define scaling thresholds. Avoid changes based only on average utilization.

### Cloud Cost Optimization (`cloud-cost`)

Use dated billing and utilization evidence, classify waste versus required headroom, estimate savings and risk, and test reversible changes. Do not delete, downsize, or purchase commitments without approval.

### DevOps Engineering (`devops`)

Inspect the current pipeline, environments, secrets, and rollback process. Make steps deterministic, least-privileged, and observable; cache only safe artifacts. Validate configuration and test a non-production path first. Do not deploy, rotate secrets, destroy resources, or change production workflows without explicit authorization. Report required credentials as names only, never values.

### Kubernetes Engineering (`kubernetes`)

Inspect cluster version, namespace, chart conventions, workload needs, and security policies. Set resource requests/limits, probes that reflect readiness, least-privilege service accounts, and safe rollout/rollback behavior. Keep secrets out of manifests. Validate manifests locally; do not apply to a live cluster or expose services publicly without explicit authorization.

### Incident Response (`incident-response`)

Establish impact, timeline, scope, and current signals from available evidence. Prioritize reversible mitigations and state expected effects before action. Preserve logs and avoid destructive cleanup or speculative changes. Separate facts from hypotheses, assign verification steps, and document recovery criteria and follow-ups. Do not perform live production actions unless explicitly authorized.
