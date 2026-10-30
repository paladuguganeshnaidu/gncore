---
name: code-build
description: "Implement, diagnose, review and refactor software across languages while preserving public behavior."
license: Apache-2.0 AND CC-BY-SA-4.0 AND MIT
---

# GNCore Software Engineering

Version: 7.0.0

## Choose the work

Choose investigation, implementation, review or refactoring from the requested outcome. Inspect call sites and repository conventions. Separate a confirmed cause from a hypothesis and avoid speculative broad rewrites.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

A scoped patch or requested engineering artifact, a clear acceptance contract, and reproducible evidence for changed behavior.

Run the relevant reproduction, unit/integration checks, build or type checks. Cover the observed failure and an important boundary without copying implementation details into assertions.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Turn the behavior contract into a small counterexample before patching. Preserve API, exception types, units and mutation behavior; check language-specific type traps and exact arithmetic where totals matter. Keep the change local, then verify ordinary, zero, extreme and invalid inputs with an independent oracle. A passing example or explanation is insufficient evidence for general correctness. When a repair allocates or ranks quantities, test mixed exact and fractional shares as well as ties; conservation or a passing happy path alone does not prove the ordering rule.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Match the supplied API, exception semantics, units and mutation behavior; use an independent counterexample for the actual failure mode.
- For exact allocation/ranking, test ordering as well as conservation, mixed exact/fractional shares, stable ties and invalid inputs; do not infer general correctness from a small fixture.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `code-grill-me` | Clarify a coding or product request through focused questions that expose assumptions and missing decisions. |
| `code-research` | Investigate a technical question using repository evidence and relevant primary sources. |
| `code-prototype` | Build a scoped prototype that tests a specific technical or product assumption. |
| `code-domain-modeling` | Model domain concepts, invariants, ownership, and language before changing service boundaries. |
| `code-decision-mapping` | Map unresolved implementation decisions, dependencies, options, and evidence needed to choose. |
| `code-search-first` | Search the existing codebase and relevant documentation before adding dependencies or implementing duplicate functionality. |
| `code-product-lens` | Validate the why before building through four product diagnostics — a YC-style product diagnostic that produces PRODUCT-BRIEF.md with a go/no-go recommendation, a founder review scoring product-market-fit signals, a user journey audit measuring time-to-value, and ICE feature prioritization. |
| `code-architecture-decision-records` | Capture architectural decisions as numbered ADR markdown files in docs/adr/ with context, alternatives considered, consequences, and an index README. |
| `code-blueprint` | Plan a substantial engineering change as reviewable steps with dependencies and acceptance evidence. |
| `code-architecture` | Shared vocabulary for designing deep modules. |
| `code-improve-architecture` | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| `code-quality` | Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. |
| `code-codebase-onboarding` | Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry points, conventions, and a starter CLAUDE.md. |
| `code-plankton-code-quality` | Write-time code quality enforcement using Plankton — auto-formatting, linting, and Claude-powered fixes on every file edit via hooks. |
| `code-code-review` | Review a code diff for correctness, local coding standards, and alignment with its originating specification. |
| `code-request-refactor-plan` | Plan a behavior-preserving refactor with explicit scope, sequencing, and regression checks. |
| `code-code-improver` | Run a bounded review-and-fix loop over a specified code target with evidence and scope controls. |
| `code-code-maturity-assessor` | Systematic code maturity assessment using Trail of Bits' 9-category framework. |
| `code-tdd` | Implement a behavior change through meaningful failing tests, a focused fix, and relevant regressions. |
| `code-tdd-workflow` | Use a focused red/green/refactor loop around an observable behavior contract. |
| `code-e2e-testing` | Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies. |
| `code-ai-regression-testing` | Regression testing strategies for AI-assisted development. |
| `code-module-regression` | Govern cross-module regression in large repositories with a REGRESSION.md ledger that records each module's downstream consumers and executable acceptance command. |
| `code-property-based-testing` | Writes, reviews, and debugs property-based tests — Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. |
| `code-coverage-analysis` | Measures and interprets what a fuzzing campaign actually reaches, using llvm-cov, lcov, or a fuzzer's own coverage output. |
| `code-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `code-verification-before-completion` | Verify the requested software outcome with fresh command output before reporting completion. |
| `code-diagnosing-bugs` | Diagnosis loop for hard bugs and performance regressions. |
| `code-qa` | Validate a software change against acceptance criteria and reproduce observable regressions. |
| `code-verification-loop` | Select and run checks that expose the changed contract; investigate failures and retain evidence. |
| `code-security-review` | Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features. |
| `code-agent-security-hardening` | Security hardening guidance for AI agent frameworks that process untrusted content, invoke tools, write workspace files, manage runtime identifiers, or handle credentials. |
| `code-sharp-edges` | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. |
| `code-insecure-defaults` | Find unsafe configuration defaults and fail-open behavior in application code and deployment configuration. |
| `code-differential-review` | Performs security-focused differential review of code changes. |
| `code-semgrep` | Run and interpret a bounded, relevant Semgrep analysis using the available installation. |
| `code-codeql` | Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. |
| `code-sarif-parsing` | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. |
| `code-supply-chain-risk-auditor` | Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upstreams, npm publisher concentration, and install-time script execution. |
| `code-git-workflow` | Git workflow patterns including branching strategies, commit conventions, keeping history clean and readable, tidying local commits before merging, merge vs rebase, conflict resolution, and collaborative development best practices for teams of all sizes. |
| `code-delivery-gate` | Review acceptance and release evidence, including failures and unresolved risks. |
| `code-cost-tracking` | Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log. |
| `code-post-patch-validation` | Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, root-cause variants, behavior preservation, regressions, and newly introduced security failures. |
| `code-mutation-testing` | Configures mewt or muton campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. |
| `code-deep-research` | Produce cited research reports from multiple web sources using firecrawl and exa MCP tools — plan sub-questions, search and deep-read sources, then synthesize findings with inline citations and confidence levels. |
| `code-research-ops` | Evidence-first current-state research workflow for ECC. |
| `code-product-capability` | Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and unresolved decisions before multi-service work starts. |
| `code-to-prd` | Turn a product idea into a scoped requirements document with user outcomes and acceptance criteria. |
| `code-to-spec` | Turn agreed requirements into a local, reviewable technical specification. |
| `code-to-tickets` | Split an accepted specification into coherent deliverables with dependencies and acceptance criteria. |
| `code-writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |
| `code-executing-plans` | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available |
| `code-requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `code-receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation |
| `code-implement` | Implement a piece of work based on a spec or set of tickets. |
| `code-implement-spec` | Implement the result of /to-spec and /to-tickets in code. |
| `code-python` | Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintainable Python applications. |
| `code-python-testing` | Design Python tests around observable contracts, meaningful boundaries and isolated state. |
| `code-webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. |
| `code-regression-hunt` | Use when investigating regressions in PRs or commits, coordinating a regression campaign, or resuming saved progress. |
| `code-brainstorming` | Explore unresolved software design choices and agree on a practical direction when the brief needs clarification. |
| `code-using-git-worktrees` | Isolate concurrent coding work in Git worktrees while preserving uncommitted changes and repository conventions. |
| `code-subagent-driven-development` | Coordinate authorized coding subagents on separable work with explicit interfaces and integration checks. |
| `code-finishing-a-development-branch` | Prepare a completed development branch for review, integration, or cleanup according to the user's chosen workflow. |
| `code-workflow-setup` | Configure the requested coding workflow's repository context, issue-tracker references, and local skill conventions. |
| `code-build` | Plan, implement, debug, and verify a software task in its existing language and stack. |
| `requirements` | Collects scope, constraints, acceptance criteria, and open questions before implementation starts. |
| `architecture` | Defines system boundaries, interfaces, and implementation constraints. |
| `implementation` | Writes production-grade code with minimal duplication and explicit types. |
| `review` | Finds defects, regressions, and missing coverage before release. |
| `testing` | Designs and validates tests for the changed slice. |
| `security` | Assesses secrets handling, unsafe file access, and privilege boundaries. |
| `documentation` | Produces concise user and developer documentation that matches the implementation. |
| `release` | Coordinates versioning, packaging, and verification for shipping. |
| `product-discovery` | Turn a product idea into a testable problem statement, user evidence plan, and scoped first release. |
| `software-feature` | Deliver a scoped software feature using local conventions and verifiable acceptance criteria. |
| `software-architecture` | Compare architecture options against constraints, operations, reversibility, and lifecycle cost. |
| `software-code-review` | Review a code change for correctness, security, maintainability, and missing regression coverage. |
| `software-debugging` | Diagnose a software failure from reproducible evidence and verify the smallest safe fix. |
| `software-refactor` | Refactor a bounded code area while preserving its documented behavior and public contracts. |
| `software-api-contract` | Define and verify an API contract across request, response, errors, versioning, and consumers. |
| `software-dependency` | Assess and implement a dependency change with compatibility, security, and rollback evidence. |
| `software-performance` | Find a measured software bottleneck and optimize it without regressing correctness. |
| `software-migration` | Plan a staged migration with compatibility gates, data safety, and rollback criteria. |
| `software-release` | Prepare a software release with reproducible artifacts, verified changes, and rollback readiness. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
