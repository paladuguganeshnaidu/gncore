---
name: cloud-devops-sre
description: "Design and operate infrastructure, delivery pipelines, containers, Kubernetes, SLOs, observability, and capacity."
license: MIT
---

# GNCore Cloud, DevOps, and SRE

## Select the work from the user's intent

Inspect workload, topology, infrastructure definitions, service objectives, current incidents, and operating constraints. Choose architecture review, infrastructure code, CI/CD, containers, orchestration, reliability, observability, incidents, capacity, or cost work. Make rollback and ownership explicit.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Validate configuration and a local or staging path where possible. Verify failure handling, recovery assumptions, resource estimates, and the actual deployment state.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
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

## Focused procedures

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

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
