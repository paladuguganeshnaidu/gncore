---
name: code-build
description: "Build, investigate, review, test, refactor, and verify software across languages using task-appropriate workflows."
license: Apache-2.0 AND CC-BY-SA-4.0 AND MIT
---

# GNCore Code Engineering

## Select the work from the user's intent

Choose a workflow from the requested outcome and uncertainty. Reuse the repository's conventions, inspect relevant call paths, and preserve public contracts and user changes. Use diagnosis before speculative fixes, contracts before cross-service changes, and meaningful tests for behavior that can regress.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Run the relevant build, type, test, lint, analysis, or reproduction checks. Keep review findings evidence-based and fix causes without weakening assertions. Additional agents are optional and require support and authorization.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

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
| `code-blueprint` | Turn a one-line objective into a step-by-step construction plan for multi-session, multi-agent engineering projects: one-PR-sized steps with self-contained context briefs, dependency graph with parallel-step detection, adversarial review gate, and plan mutation protocol. |
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
| `code-tdd-workflow` | Test-driven development workflow: write a failing test first, watch it fail, implement the smallest change to green, then refactor with 80%+ coverage across unit, integration, and E2E tests. |
| `code-e2e-testing` | Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies. |
| `code-ai-regression-testing` | Regression testing strategies for AI-assisted development. |
| `code-module-regression` | Govern cross-module regression in large repositories with a REGRESSION.md ledger that records each module's downstream consumers and executable acceptance command. |
| `code-property-based-testing` | Writes, reviews, and debugs property-based tests — Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. |
| `code-coverage-analysis` | Measures and interprets what a fuzzing campaign actually reaches, using llvm-cov, lcov, or a fuzzer's own coverage output. |
| `code-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `code-verification-before-completion` | Verify the requested software outcome with fresh command output before reporting completion. |
| `code-diagnosing-bugs` | Diagnosis loop for hard bugs and performance regressions. |
| `code-qa` | Validate a software change against acceptance criteria and reproduce observable regressions. |
| `code-verification-loop` | Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, security grep, and diff review — then produce a PASS/FAIL verification report. |
| `code-security-review` | Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features. |
| `code-agent-security-hardening` | Security hardening guidance for AI agent frameworks that process untrusted content, invoke tools, write workspace files, manage runtime identifiers, or handle credentials. |
| `code-sharp-edges` | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. |
| `code-insecure-defaults` | Find unsafe configuration defaults and fail-open behavior in application code and deployment configuration. |
| `code-differential-review` | Performs security-focused differential review of code changes. |
| `code-semgrep` | Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset through scripts/run-scans.sh, which batches the semgrep processes and writes scans.json, and merges the output to SARIF. |
| `code-codeql` | Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. |
| `code-sarif-parsing` | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. |
| `code-supply-chain-risk-auditor` | Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upstreams, npm publisher concentration, and install-time script execution. |
| `code-git-workflow` | Git workflow patterns including branching strategies, commit conventions, keeping history clean and readable, tidying local commits before merging, merge vs rebase, conflict resolution, and collaborative development best practices for teams of all sizes. |
| `code-delivery-gate` | Stop hook that blocks Claude from finishing until quality checks pass. |
| `code-cost-tracking` | Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log. |
| `code-post-patch-validation` | Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, root-cause variants, behavior preservation, regressions, and newly introduced security failures. |
| `code-mutation-testing` | Configures mewt or muton campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. |
| `code-deep-research` | Produce cited research reports from multiple web sources using firecrawl and exa MCP tools — plan sub-questions, search and deep-read sources, then synthesize findings with inline citations and confidence levels. |
| `code-research-ops` | Evidence-first current-state research workflow for ECC. |
| `code-product-capability` | Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and unresolved decisions before multi-service work starts. |
| `code-to-prd` | Turn a product idea into a scoped requirements document with user outcomes and acceptance criteria. |
| `code-to-spec` | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. |
| `code-to-tickets` | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in one file per ticket locally, or native blocking links on a real tracker). |
| `code-writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |
| `code-executing-plans` | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available |
| `code-requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `code-receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation |
| `code-implement` | Implement a piece of work based on a spec or set of tickets. |
| `code-implement-spec` | Implement the result of /to-spec and /to-tickets in code. |
| `code-python` | Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintainable Python applications. |
| `code-python-testing` | Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization, and coverage requirements. |
| `code-webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. |
| `code-regression-hunt` | Use when investigating regressions in PRs or commits, coordinating a regression campaign, or resuming saved progress. |
| `code-brainstorming` | Explore unresolved software design choices and agree on a practical direction when the brief needs clarification. |
| `code-using-git-worktrees` | Isolate concurrent coding work in Git worktrees while preserving uncommitted changes and repository conventions. |
| `code-subagent-driven-development` | Coordinate authorized coding subagents on separable work with explicit interfaces and integration checks. |
| `code-finishing-a-development-branch` | Prepare a completed development branch for review, integration, or cleanup according to the user's chosen workflow. |
| `code-workflow-setup` | Configure the requested coding workflow's repository context, issue-tracker references, and local skill conventions. |
| `code-build` | Plan, implement, debug, and verify a software task in its existing language and stack. |

## Focused procedures

### GNCore Grill Me (`code-grill-me`)

Establish the requested outcome, current behavior, constraints, acceptance criteria, and unresolved architectural choices. Use repository evidence before proposing changes; produce the brief or decision artifact requested rather than automatically moving into implementation.

For task-specific technical depth, read [the attributed source guide](references/code-grill-me/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Research (`code-research`)

Establish the requested outcome, current behavior, constraints, acceptance criteria, and unresolved architectural choices. Use repository evidence before proposing changes; produce the brief or decision artifact requested rather than automatically moving into implementation.

For task-specific technical depth, read [the attributed source guide](references/code-research/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Prototype (`code-prototype`)

Establish the requested outcome, current behavior, constraints, acceptance criteria, and unresolved architectural choices. Use repository evidence before proposing changes; produce the brief or decision artifact requested rather than automatically moving into implementation.

For task-specific technical depth, read [the attributed source guide](references/code-prototype/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Domain Modeling (`code-domain-modeling`)

Establish the requested outcome, current behavior, constraints, acceptance criteria, and unresolved architectural choices. Use repository evidence before proposing changes; produce the brief or decision artifact requested rather than automatically moving into implementation.

For task-specific technical depth, read [the attributed source guide](references/code-domain-modeling/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Decision Mapping (`code-decision-mapping`)

List decisions that materially affect the requested outcome. For each, record options, constraints, dependencies, reversibility, owner, and the evidence needed to choose. Resolve choices already implied by repository conventions; ask about only decisions that affect scope or correctness. Deliver a decision map and a concrete next implementation step, without treating every preference as a blocker.

### GNCore Search First (`code-search-first`)

Establish the requested outcome, current behavior, constraints, acceptance criteria, and unresolved architectural choices. Use repository evidence before proposing changes; produce the brief or decision artifact requested rather than automatically moving into implementation.

For task-specific technical depth, read [the attributed source guide](references/code-search-first/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Product Lens (`code-product-lens`)

Establish the requested outcome, current behavior, constraints, acceptance criteria, and unresolved architectural choices. Use repository evidence before proposing changes; produce the brief or decision artifact requested rather than automatically moving into implementation.

For task-specific technical depth, read [the attributed source guide](references/code-product-lens/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Architecture Decision Records (`code-architecture-decision-records`)

Establish the requested outcome, current behavior, constraints, acceptance criteria, and unresolved architectural choices. Use repository evidence before proposing changes; produce the brief or decision artifact requested rather than automatically moving into implementation.

For task-specific technical depth, read [the attributed source guide](references/code-architecture-decision-records/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Blueprint (`code-blueprint`)

Establish the requested outcome, current behavior, constraints, acceptance criteria, and unresolved architectural choices. Use repository evidence before proposing changes; produce the brief or decision artifact requested rather than automatically moving into implementation.

For task-specific technical depth, read [the attributed source guide](references/code-blueprint/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Architecture (`code-architecture`)

Trace request boundaries, domain rules, persistence, dependencies, and failure modes in the current system. Choose interfaces and ownership boundaries appropriate to the actual service and explain concrete tradeoffs before changing architecture.

For task-specific technical depth, read [the attributed source guide](references/code-architecture/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Improve Architecture (`code-improve-architecture`)

Trace request boundaries, domain rules, persistence, dependencies, and failure modes in the current system. Choose interfaces and ownership boundaries appropriate to the actual service and explain concrete tradeoffs before changing architecture.

For task-specific technical depth, read [the attributed source guide](references/code-improve-architecture/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Quality (`code-quality`)

Understand local conventions and the behavior that must survive the change. Identify concrete correctness, maintainability, or complexity problems, make a scoped improvement, and verify observable behavior; avoid cosmetic churn and speculative abstractions.

For task-specific technical depth, read [the attributed source guide](references/code-quality/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Codebase Onboarding (`code-codebase-onboarding`)

Understand local conventions and the behavior that must survive the change. Identify concrete correctness, maintainability, or complexity problems, make a scoped improvement, and verify observable behavior; avoid cosmetic churn and speculative abstractions.

For task-specific technical depth, read [the attributed source guide](references/code-codebase-onboarding/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Plankton Code Quality (`code-plankton-code-quality`)

Understand local conventions and the behavior that must survive the change. Identify concrete correctness, maintainability, or complexity problems, make a scoped improvement, and verify observable behavior; avoid cosmetic churn and speculative abstractions.

For task-specific technical depth, read [the attributed source guide](references/code-plankton-code-quality/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Code Review (`code-code-review`)

Understand local conventions and the behavior that must survive the change. Identify concrete correctness, maintainability, or complexity problems, make a scoped improvement, and verify observable behavior; avoid cosmetic churn and speculative abstractions.

For task-specific technical depth, read [the attributed source guide](references/code-code-review/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Request Refactor Plan (`code-request-refactor-plan`)

Inspect the current implementation, callers, and regression coverage. State the concrete maintainability problem and the observable behaviors that must remain unchanged. Propose a sequence of small changes with touched modules, compatibility boundaries, and checks for each step. Flag data migrations or API breaks explicitly. Deliver the requested plan; implement it only when implementation is within the user's request.

### GNCore Code Improver (`code-code-improver`)

Understand local conventions and the behavior that must survive the change. Identify concrete correctness, maintainability, or complexity problems, make a scoped improvement, and verify observable behavior; avoid cosmetic churn and speculative abstractions.

For task-specific technical depth, read [the attributed source guide](references/code-code-improver/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Code Maturity Assessor (`code-code-maturity-assessor`)

Understand local conventions and the behavior that must survive the change. Identify concrete correctness, maintainability, or complexity problems, make a scoped improvement, and verify observable behavior; avoid cosmetic churn and speculative abstractions.

For task-specific technical depth, read [the attributed source guide](references/code-code-maturity-assessor/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Tdd (`code-tdd`)

Select tests from the requested behavior and relevant failure risks. Reproduce a bug or demonstrate a meaningful failing case where appropriate, implement the change, and run focused regressions without weakening assertions or claiming unrun tests passed.

For task-specific technical depth, read [the attributed source guide](references/code-tdd/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Tdd Workflow (`code-tdd-workflow`)

Select tests from the requested behavior and relevant failure risks. Reproduce a bug or demonstrate a meaningful failing case where appropriate, implement the change, and run focused regressions without weakening assertions or claiming unrun tests passed.

For task-specific technical depth, read [the attributed source guide](references/code-tdd-workflow/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore E2E Testing (`code-e2e-testing`)

Select tests from the requested behavior and relevant failure risks. Reproduce a bug or demonstrate a meaningful failing case where appropriate, implement the change, and run focused regressions without weakening assertions or claiming unrun tests passed.

For task-specific technical depth, read [the attributed source guide](references/code-e2e-testing/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Ai Regression Testing (`code-ai-regression-testing`)

Select tests from the requested behavior and relevant failure risks. Reproduce a bug or demonstrate a meaningful failing case where appropriate, implement the change, and run focused regressions without weakening assertions or claiming unrun tests passed.

For task-specific technical depth, read [the attributed source guide](references/code-ai-regression-testing/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Module Regression (`code-module-regression`)

Select tests from the requested behavior and relevant failure risks. Reproduce a bug or demonstrate a meaningful failing case where appropriate, implement the change, and run focused regressions without weakening assertions or claiming unrun tests passed.

For task-specific technical depth, read [the attributed source guide](references/code-module-regression/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Property Based Testing (`code-property-based-testing`)

Select tests from the requested behavior and relevant failure risks. Reproduce a bug or demonstrate a meaningful failing case where appropriate, implement the change, and run focused regressions without weakening assertions or claiming unrun tests passed.

For task-specific technical depth, read [the attributed source guide](references/code-property-based-testing/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Coverage Analysis (`code-coverage-analysis`)

Select tests from the requested behavior and relevant failure risks. Reproduce a bug or demonstrate a meaningful failing case where appropriate, implement the change, and run focused regressions without weakening assertions or claiming unrun tests passed.

For task-specific technical depth, read [the attributed source guide](references/code-coverage-analysis/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Debugging (`code-debugging`)

Reproduce the reported behavior with the smallest useful case, collect evidence, and distinguish hypotheses from causes. Trace the failure through the actual system, make a focused fix, and verify the reproduction plus relevant regressions before reporting completion.

For task-specific technical depth, read [the attributed source guide](references/code-debugging/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Verification Before Completion (`code-verification-before-completion`)

Reproduce the reported behavior with the smallest useful case, collect evidence, and distinguish hypotheses from causes. Trace the failure through the actual system, make a focused fix, and verify the reproduction plus relevant regressions before reporting completion.

For task-specific technical depth, read [the attributed source guide](references/code-verification-before-completion/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Diagnosing Bugs (`code-diagnosing-bugs`)

Reproduce the reported behavior with the smallest useful case, collect evidence, and distinguish hypotheses from causes. Trace the failure through the actual system, make a focused fix, and verify the reproduction plus relevant regressions before reporting completion.

For task-specific technical depth, read [the attributed source guide](references/code-diagnosing-bugs/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Qa (`code-qa`)

Translate the feature brief or bug report into observable acceptance cases. Exercise the main journey and relevant permission, failure, empty, concurrency, or recovery cases. Record exact setup, inputs, commands, and outcomes. For a failure, isolate a reproducible case and distinguish implementation defects from environment limitations. Fix and retest when requested; report checks not performed rather than treating missing evidence as a pass.

### GNCore Verification Loop (`code-verification-loop`)

Reproduce the reported behavior with the smallest useful case, collect evidence, and distinguish hypotheses from causes. Trace the failure through the actual system, make a focused fix, and verify the reproduction plus relevant regressions before reporting completion.

For task-specific technical depth, read [the attributed source guide](references/code-verification-loop/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Security Review (`code-security-review`)

Map relevant trust boundaries and attacker-controlled input in the requested code. Tie findings to reachable paths and impact, preserve authorization and secret handling, and verify mitigations locally without expanding into unauthorized live-target testing.

For task-specific technical depth, read [the attributed source guide](references/code-security-review/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Agent Security Hardening (`code-agent-security-hardening`)

Map relevant trust boundaries and attacker-controlled input in the requested code. Tie findings to reachable paths and impact, preserve authorization and secret handling, and verify mitigations locally without expanding into unauthorized live-target testing.

For task-specific technical depth, read [the attributed source guide](references/code-agent-security-hardening/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Sharp Edges (`code-sharp-edges`)

Map relevant trust boundaries and attacker-controlled input in the requested code. Tie findings to reachable paths and impact, preserve authorization and secret handling, and verify mitigations locally without expanding into unauthorized live-target testing.

For task-specific technical depth, read [the attributed source guide](references/code-sharp-edges/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Insecure Defaults (`code-insecure-defaults`)

Trace configuration values from defaults and environment parsing into sensitive operations. Look for development credentials, debug exposure, permissive origin or network rules, disabled verification, unchecked authorization, and fail-open error handling. Demonstrate the reachable unsafe condition in a local test where practical. Propose a secure default and an explicit opt-in for legitimate development cases; preserve a documented migration path and retest both allowed and denied behavior.

### GNCore Differential Review (`code-differential-review`)

Map relevant trust boundaries and attacker-controlled input in the requested code. Tie findings to reachable paths and impact, preserve authorization and secret handling, and verify mitigations locally without expanding into unauthorized live-target testing.

For task-specific technical depth, read [the attributed source guide](references/code-differential-review/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Semgrep (`code-semgrep`)

Check available tool versions and project language support, scope the scan, and inspect the rules or query pack before execution. Triage results against reachable code and report commands, evidence, false positives, and analysis limits rather than treating every alert as a confirmed vulnerability.

For task-specific technical depth, read [the attributed source guide](references/code-semgrep/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Codeql (`code-codeql`)

Check available tool versions and project language support, scope the scan, and inspect the rules or query pack before execution. Triage results against reachable code and report commands, evidence, false positives, and analysis limits rather than treating every alert as a confirmed vulnerability.

For task-specific technical depth, read [the attributed source guide](references/code-codeql/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Sarif Parsing (`code-sarif-parsing`)

Check available tool versions and project language support, scope the scan, and inspect the rules or query pack before execution. Triage results against reachable code and report commands, evidence, false positives, and analysis limits rather than treating every alert as a confirmed vulnerability.

For task-specific technical depth, read [the attributed source guide](references/code-sarif-parsing/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Supply Chain Risk Auditor (`code-supply-chain-risk-auditor`)

Check available tool versions and project language support, scope the scan, and inspect the rules or query pack before execution. Triage results against reachable code and report commands, evidence, false positives, and analysis limits rather than treating every alert as a confirmed vulnerability.

For task-specific technical depth, read [the attributed source guide](references/code-supply-chain-risk-auditor/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Git Workflow (`code-git-workflow`)

Inspect the build, runtime, configuration, dependency pinning, and current delivery workflow. Prepare reproducible changes and validate a local or staging path; preserve secret boundaries and distinguish a prepared rollout from an actual authorized deployment.

For task-specific technical depth, read [the attributed source guide](references/code-git-workflow/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Delivery Gate (`code-delivery-gate`)

Evaluate the requested change against concrete acceptance checks, regression evidence, operating costs, and recovery plans. Report passed checks separately from unknowns; prepare a reviewable result without implying authorization to publish, deploy, or merge.

For task-specific technical depth, read [the attributed source guide](references/code-delivery-gate/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Cost Tracking (`code-cost-tracking`)

Evaluate the requested change against concrete acceptance checks, regression evidence, operating costs, and recovery plans. Report passed checks separately from unknowns; prepare a reviewable result without implying authorization to publish, deploy, or merge.

For task-specific technical depth, read [the attributed source guide](references/code-cost-tracking/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Post Patch Validation (`code-post-patch-validation`)

Evaluate the requested change against concrete acceptance checks, regression evidence, operating costs, and recovery plans. Report passed checks separately from unknowns; prepare a reviewable result without implying authorization to publish, deploy, or merge.

For task-specific technical depth, read [the attributed source guide](references/code-post-patch-validation/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Mutation Testing (`code-mutation-testing`)

Evaluate the requested change against concrete acceptance checks, regression evidence, operating costs, and recovery plans. Report passed checks separately from unknowns; prepare a reviewable result without implying authorization to publish, deploy, or merge.

For task-specific technical depth, read [the attributed source guide](references/code-mutation-testing/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Deep Research (`code-deep-research`)

Turn the actual question into a bounded investigation with primary sources and repository evidence. Separate findings, hypotheses, decisions, and proposed experiments; produce the requested product brief, specification, or actionable tickets without expanding the product scope.

For task-specific technical depth, read [the attributed source guide](references/code-deep-research/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Research Ops (`code-research-ops`)

Turn the actual question into a bounded investigation with primary sources and repository evidence. Separate findings, hypotheses, decisions, and proposed experiments; produce the requested product brief, specification, or actionable tickets without expanding the product scope.

For task-specific technical depth, read [the attributed source guide](references/code-research-ops/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Product Capability (`code-product-capability`)

Turn the actual question into a bounded investigation with primary sources and repository evidence. Separate findings, hypotheses, decisions, and proposed experiments; produce the requested product brief, specification, or actionable tickets without expanding the product scope.

For task-specific technical depth, read [the attributed source guide](references/code-product-capability/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore To Prd (`code-to-prd`)

Describe the target users, current problem, desired outcome, scope, and explicit non-goals from the supplied context. Define functional behavior, key user journeys, constraints, dependencies, measurable acceptance criteria, and open decisions. Separate observed evidence from assumptions. Keep implementation details only where they constrain the product; avoid invented market claims, delivery estimates, or approvals.

### GNCore To Spec (`code-to-spec`)

Turn the actual question into a bounded investigation with primary sources and repository evidence. Separate findings, hypotheses, decisions, and proposed experiments; produce the requested product brief, specification, or actionable tickets without expanding the product scope.

For task-specific technical depth, read [the attributed source guide](references/code-to-spec/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore To Tickets (`code-to-tickets`)

Turn the actual question into a bounded investigation with primary sources and repository evidence. Separate findings, hypotheses, decisions, and proposed experiments; produce the requested product brief, specification, or actionable tickets without expanding the product scope.

For task-specific technical depth, read [the attributed source guide](references/code-to-tickets/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Writing Plans (`code-writing-plans`)

Use the requested plan or specification as the acceptance boundary, inspect the relevant code, and implement reviewable increments. Keep plans proportional to complexity, preserve user changes, and use additional agents only when supported and authorized for the current task.

For task-specific technical depth, read [the attributed source guide](references/code-writing-plans/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Executing Plans (`code-executing-plans`)

Use the requested plan or specification as the acceptance boundary, inspect the relevant code, and implement reviewable increments. Keep plans proportional to complexity, preserve user changes, and use additional agents only when supported and authorized for the current task.

For task-specific technical depth, read [the attributed source guide](references/code-executing-plans/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Requesting Code Review (`code-requesting-code-review`)

Use the requested plan or specification as the acceptance boundary, inspect the relevant code, and implement reviewable increments. Keep plans proportional to complexity, preserve user changes, and use additional agents only when supported and authorized for the current task.

For task-specific technical depth, read [the attributed source guide](references/code-requesting-code-review/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Receiving Code Review (`code-receiving-code-review`)

Use the requested plan or specification as the acceptance boundary, inspect the relevant code, and implement reviewable increments. Keep plans proportional to complexity, preserve user changes, and use additional agents only when supported and authorized for the current task.

For task-specific technical depth, read [the attributed source guide](references/code-receiving-code-review/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Implement (`code-implement`)

Use the requested plan or specification as the acceptance boundary, inspect the relevant code, and implement reviewable increments. Keep plans proportional to complexity, preserve user changes, and use additional agents only when supported and authorized for the current task.

For task-specific technical depth, read [the attributed source guide](references/code-implement/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Implement Spec (`code-implement-spec`)

Use the requested plan or specification as the acceptance boundary, inspect the relevant code, and implement reviewable increments. Keep plans proportional to complexity, preserve user changes, and use additional agents only when supported and authorized for the current task.

For task-specific technical depth, read [the attributed source guide](references/code-implement-spec/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Python (`code-python`)

Inspect Python, framework, validation, database, and test versions before choosing APIs. Implement typed boundaries and explicit error handling using the current project conventions; verify the requested behavior with framework-appropriate tests.

For task-specific technical depth, read [the attributed source guide](references/code-python/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Python Testing (`code-python-testing`)

Inspect Python, framework, validation, database, and test versions before choosing APIs. Implement typed boundaries and explicit error handling using the current project conventions; verify the requested behavior with framework-appropriate tests.

For task-specific technical depth, read [the attributed source guide](references/code-python-testing/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Webapp Testing (`code-webapp-testing`)

Exercise the relevant user journey or changed boundary, compare expected and actual behavior, and isolate any regression to a reproducible case. Prefer deterministic fixtures and observable outcomes over timing sleeps or implementation-mirroring assertions.

For task-specific technical depth, read [the attributed source guide](references/code-webapp-testing/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Regression Hunt (`code-regression-hunt`)

Exercise the relevant user journey or changed boundary, compare expected and actual behavior, and isolate any regression to a reproducible case. Prefer deterministic fixtures and observable outcomes over timing sleeps or implementation-mirroring assertions.

For task-specific technical depth, read [the attributed source guide](references/code-regression-hunt/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Brainstorming (`code-brainstorming`)

Choose a workflow proportional to the requested change. Explore unresolved product decisions when needed, isolate parallel changes safely, and finish with a concrete reviewable result. Repository setup changes and external branch actions must remain within the user's actual request.

For task-specific technical depth, read [the attributed source guide](references/code-brainstorming/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Using Git Worktrees (`code-using-git-worktrees`)

Choose a workflow proportional to the requested change. Explore unresolved product decisions when needed, isolate parallel changes safely, and finish with a concrete reviewable result. Repository setup changes and external branch actions must remain within the user's actual request.

For task-specific technical depth, read [the attributed source guide](references/code-using-git-worktrees/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Subagent Driven Development (`code-subagent-driven-development`)

Choose a workflow proportional to the requested change. Explore unresolved product decisions when needed, isolate parallel changes safely, and finish with a concrete reviewable result. Repository setup changes and external branch actions must remain within the user's actual request.

For task-specific technical depth, read [the attributed source guide](references/code-subagent-driven-development/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Finishing A Development Branch (`code-finishing-a-development-branch`)

Choose a workflow proportional to the requested change. Explore unresolved product decisions when needed, isolate parallel changes safely, and finish with a concrete reviewable result. Repository setup changes and external branch actions must remain within the user's actual request.

For task-specific technical depth, read [the attributed source guide](references/code-finishing-a-development-branch/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Workflow Setup (`code-workflow-setup`)

Choose a workflow proportional to the requested change. Explore unresolved product decisions when needed, isolate parallel changes safely, and finish with a concrete reviewable result. Repository setup changes and external branch actions must remain within the user's actual request.

For task-specific technical depth, read [the attributed source guide](references/code-workflow-setup/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore General Coding Workflow (`code-build`)

Inspect the relevant source, current behavior, user request, and repository instructions. Choose the smallest useful set of coding skills for the task: requirements or architecture for unresolved design, the actual stack for implementation, and a suitable testing or debugging workflow for verification. Build the complete requested result, preserve unrelated work, and report concrete evidence. Do not load all installed skills for every task.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [mattpocock/skills / codebase-design](research/mattpocock-skills-codebase-design/GUIDE.md): MIT.
- [mattpocock/skills / code-review](research/mattpocock-skills-code-review/GUIDE.md): MIT.
- [affaan-m/ecc / coding-standards](research/affaan-m-ecc-coding-standards/GUIDE.md): MIT.
- [affaan-m/ecc / java-coding-standards](research/affaan-m-ecc-java-coding-standards/GUIDE.md): MIT.
- [affaan-m/ecc / cpp-coding-standards](research/affaan-m-ecc-cpp-coding-standards/GUIDE.md): MIT.
- [github/awesome-copilot / write-coding-standards-from-file](research/github-awesome-copilot-write-coding-standards-from-file/GUIDE.md): MIT.
- [sickn33/agentic-awesome-skills / cc-skill-coding-standards](research/sickn33-agentic-awesome-skills-cc-skill-coding-standards/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
