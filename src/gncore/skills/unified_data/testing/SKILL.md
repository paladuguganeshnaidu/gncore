---
name: testing
description: "Design and implement unit, integration, contract, end-to-end and performance verification."
license: MIT
---

# GNCore Testing

Version: 7.0.0rc1

## Choose the work

Choose test boundaries by failure impact. Assert observable behavior, isolate side effects and use real components where the integration itself is the contract.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Deterministic tests, fixtures, environment assumptions and a result report distinguishing passed, failed, skipped and unexecuted coverage.

Demonstrate the test catches a meaningful failure. Verify cleanup, independence and realistic boundary cases; do not weaken assertions or silently suppress failures.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Derive assertions from independent observable contracts rather than the implementation's wording. Check that the suite accepts a known-correct implementation before measuring deliberate mutants, and distinguish caught defects from false rejections. Cover meaningful boundaries, exception semantics and state transitions with deterministic setup/cleanup. Report actual passed/failed/skipped cases and unexecuted integration coverage; do not turn an always-failing test into a high bug-catching score.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `accessibility-audit` | Inspect a user flow for keyboard, screen reader, visual, and cognitive accessibility barriers. |
| `performance-audit` | Find and verify the largest performance bottlenecks before changing code or infrastructure. |
| `test-strategy` | Choose a balanced test plan that catches important failures at the lowest practical level. |
| `requirements-to-tests` | Turn requirements into observable acceptance cases that cover success, failure, boundaries, and permissions. |
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
| `unit-testing` | Write fast, deterministic unit tests around public behavior and edge cases. |
| `integration-testing` | Verify interactions between real components while isolating external services and state. |
| `end-to-end-testing` | Validate critical user journeys across the running application with stable, accessible assertions. |
| `test-automation` | Create maintainable CI test workflows with clear triggers, artifacts, and failure signals. |
| `performance-testing` | Design controlled load tests that measure latency, throughput, and saturation safely. |

## Focused procedures

### Accessibility Audit (`accessibility-audit`)

Walk the actual flow using semantic structure, keyboard only, visible focus, zoom/reflow, labels, errors, and relevant assistive technology when available. Record reproducible steps, affected users, and evidence. Prioritize barriers by impact and task completion. Map findings to applicable criteria only when checked; do not claim full conformance from a partial audit.

### Performance Audit (`performance-audit`)

Capture a baseline under stated hardware, data, and load conditions. Profile before optimizing and identify the critical path. Change one bottleneck at a time, preserve correctness, and compare repeated measurements. Include tail latency and resource cost when relevant. Do not claim improvement without measured before/after evidence or scale workload beyond safe limits.

### Test Strategy (`test-strategy`)

Map changed behavior to risks and contracts. Prefer focused unit tests for logic, integration tests for boundaries, and a small number of end-to-end tests for critical journeys. Include failure paths, permissions, and data invariants. Avoid brittle implementation assertions and duplicated coverage. Report what is covered, what is unverified, and the exact commands run.

### Requirements to Acceptance Tests (`requirements-to-tests`)

Extract actors, preconditions, inputs, expected outcomes, and constraints. Rewrite vague statements as observable behaviors and identify contradictions or missing decisions. Cover normal, boundary, error, permission, and recovery paths. Link cases to requirement IDs where available. Do not treat implementation details as acceptance criteria unless they are contractual.

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

### Unit Testing (`unit-testing`)

Identify the contract and boundaries of one unit. Test normal, boundary, invalid, and regression cases with clear arrange/act/assert structure. Mock only external boundaries, not the behavior under test. Keep tests deterministic and assert meaningful outputs or side effects; never loosen assertions to silence a failure.

### Integration Testing (`integration-testing`)

Choose the smallest integration path that crosses the relevant boundary. Use isolated temporary state or disposable fixtures, cover failure and cleanup behavior, and keep credentials and production endpoints out of tests. Distinguish environment failures from product failures in the report.

### End-to-End Testing (`end-to-end-testing`)

Select journeys by user impact and risk. Assert user-visible outcomes and accessibility semantics, use unique test data and deterministic setup, and clean up created state. Prefer waiting on a real condition over fixed sleeps. Report browser, environment, and skipped coverage accurately.

### Test Automation Engineering (`test-automation`)

Inspect existing CI conventions and execution limits. Run the fastest useful checks early, parallelize only independent jobs, cache only safe reproducible artifacts, and preserve failure output. Do not make a check advisory or suppress errors merely to get a green pipeline.

### Performance and Load Testing (`performance-testing`)

Define workload, concurrency, duration, target environment, and success thresholds before running. Use a staging or explicitly approved target and ramp traffic gradually. Capture percentiles, errors, resource saturation, and test conditions. Do not stress production or claim capacity from an uncontrolled run.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
