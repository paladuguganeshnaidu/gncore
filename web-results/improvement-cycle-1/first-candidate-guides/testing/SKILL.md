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

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Deterministic tests, fixtures, environment assumptions and a result report distinguishing passed, failed, skipped and unexecuted coverage.

Demonstrate the test catches a meaningful failure. Verify cleanup, independence and realistic boundary cases; do not weaken assertions or silently suppress failures.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Derive assertions from independent observable contracts rather than the implementation's wording. Check that the suite accepts a known-correct implementation before measuring deliberate mutants, and distinguish caught defects from false rejections. Cover meaningful boundaries, exception semantics and state transitions with deterministic setup/cleanup. Report actual passed/failed/skipped cases and unexecuted integration coverage; do not turn an always-failing test into a high bug-catching score.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Derive observable assertions from an independent contract and meaningful failure transitions; a corrected oracle needs contract evidence, not a desire for green CI.
- For mutation evaluation, first accept a known-correct implementation, then count caught mutants and false rejections separately. Record actual failures/skips and unavailable integration coverage.

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

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
