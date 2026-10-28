---
name: quality-engineering
description: "Design risk-based test strategies, automation, end-to-end and contract checks, and release evidence."
license: MIT
---

# GNCore Quality Engineering and Testing

## Select the work from the user's intent

Map user journeys, change risk, interfaces, test environments, and current failure history. Choose test design, automation, E2E, contracts, performance, accessibility, defect triage, release gates, or flaky-test work. Select assertions from behavior rather than mirroring implementation.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Run relevant cases with deterministic setup, preserve useful failure artifacts, and distinguish passing checks from skipped, unavailable, or unverified coverage.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `qa-test-strategy` | Choose a risk-based test mix that verifies behavior at the lowest effective level. |
| `qa-test-design` | Turn a behavior contract into clear positive, negative, boundary, and state-transition tests. |
| `qa-automation` | Build maintainable test automation with stable setup, deterministic data, and actionable failures. |
| `qa-e2e` | Verify a critical user journey across the application with realistic but isolated data. |
| `qa-api-contract` | Check API compatibility, validation, authorization, and error contracts between services. |
| `qa-performance` | Measure a service against representative load, latency, throughput, and resource objectives. |
| `qa-accessibility` | Test a flow for keyboard operation, semantics, focus, labels, zoom, and assistive technology support. |
| `qa-defect-triage` | Classify and prioritize a defect using reproducibility, user impact, scope, and workaround evidence. |
| `qa-release-gate` | Evaluate release evidence against agreed quality gates and make residual risk visible. |
| `qa-flaky-test` | Find the cause of an intermittent test failure and confirm a stable correction. |

## Focused procedures

### Test Strategy (`qa-test-strategy`)

Map changed contracts and failure costs to unit, integration, end-to-end, accessibility, and performance checks. Prioritize boundary and recovery cases; report untested risk without padding coverage metrics.

### Test Case Design (`qa-test-design`)

Define preconditions, inputs, observable outcome, oracle, cleanup, and traceability. Use equivalence classes and realistic edge cases; avoid asserting incidental implementation details.

### Test Automation (`qa-automation`)

Use isolated fixtures, explicit waits, stable selectors, safe cleanup, and failure artifacts that exclude secrets. Eliminate flaky timing and rerun failures to distinguish product defects from harness defects.

### End-to-End User Journey Test (`qa-e2e`)

Select the highest-value journey, define checkpoints, seed deterministic state, test success and a meaningful failure path, and clean up. Avoid production accounts and fixed sleeps.

### API Contract Testing (`qa-api-contract`)

Use versioned schemas and representative consumers, test malformed and unauthorized requests, verify status and error bodies, and detect breaking changes before deployment.

### Performance Test Plan (`qa-performance`)

Set workload model, environment, warmup, duration, concurrency, percentiles, and safety limits. Compare repeatable baselines and stop before shared systems are harmed.

### Accessibility Test Pass (`qa-accessibility`)

Run automated checks and manual keyboard review, inspect focus and error announcements, test reflow/zoom, and record reproducible barriers. Do not claim full conformance from partial coverage.

### Defect Triage (`qa-defect-triage`)

Capture environment, version, steps, expected and actual result, affected users, frequency, and evidence. Separate severity from priority and avoid unsupported root-cause claims.

### Release Quality Gate (`qa-release-gate`)

Check required automated and manual evidence, unresolved defects, platform coverage, rollback, and known issues. Mark each gate passed, failed, skipped, or blocked; never equate a green pipeline with zero risk.

### Flaky Test Investigation (`qa-flaky-test`)

Collect repeated-run evidence, timestamps, ordering, shared state, network and timing dependencies. Reproduce under controlled conditions, fix the cause rather than suppressing the assertion, and demonstrate stable reruns.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [petrkindlmann/qa-skills / test-strategy](research/petrkindlmann-qa-skills-test-strategy/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
