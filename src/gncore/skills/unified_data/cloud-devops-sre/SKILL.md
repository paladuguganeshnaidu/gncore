---
name: cloud-devops-sre
description: "Build delivery pipelines, cloud infrastructure, containers, Kubernetes and reliable service operations."
license: MIT
---

# GNCore Cloud, DevOps and SRE

Version: 7.0.0rc1

## Choose the work

Inspect workload, deployment boundaries, existing infrastructure state and recovery requirements. Prefer reversible changes with explicit health and rollout signals.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Reviewable infrastructure or pipeline configuration, service objectives, ownership, observability and rollback/runbook details.

Validate configuration and staging behavior, failed rollout recovery, resource limits and meaningful health checks. Keep plan, applied infrastructure and production traffic changes distinct.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Infer compatibility, secret handling and recovery needs even when the brief mentions only deployment. Stage additive schema/config changes before switching consumers; bound backfill and exposure, and gate promotion on workload-specific errors, latency, lag and resource limits over a defined window. Use least-privilege identities and keep credentials out of images and logs. Application rollback does not reverse changed data; retain a compatible path and rehearse recovery before destructive contraction.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `cloud-architecture` | Design a cloud deployment around explicit reliability, security, operations, and cost constraints. |
| `cost-optimization` | Find measurable cloud cost reductions while protecting reliability and workload correctness. |
| `cloud-architecture-review` | Compare cloud designs against workload, reliability, security, cost, and operational constraints. |
| `cloud-infrastructure-code` | Author or review infrastructure changes with plan inspection, least privilege, and rollback. |
| `cloud-ci-cd` | Improve a delivery pipeline with reproducibility, least privilege, useful gates, and rollback. |
| `cloud-container` | Build a reproducible container with a minimal attack surface and reliable runtime behavior. |
| `cloud-kubernetes` | Review Kubernetes workloads for availability, resource bounds, identity, health, and rollout safety. |
| `cloud-slo` | Define service-level indicators and objectives that reflect user-visible reliability. |
| `cloud-observability` | Instrument service behavior with actionable metrics, structured logs, and traces. |
| `cloud-incident` | Manage a reliability incident through impact assessment, safe mitigation, verification, and learning. |
| `cloud-capacity` | Plan service capacity using measured demand, bottleneck data, growth uncertainty, and failure headroom. |
| `cloud-cost` | Reduce measurable infrastructure spend while protecting service objectives and recovery options. |
| `devops` | Improve build and delivery workflows with reproducible steps, safe rollout, and actionable failure signals. |
| `kubernetes` | Author Kubernetes resources with least privilege, clear health behavior, and safe rollout settings. |
| `incident-response` | Triage incidents from evidence, reduce impact safely, and preserve a clear timeline and follow-up. |

## Focused procedures

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

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
