---
name: code-build
description: "Implement, diagnose, review and refactor software across languages while preserving public behavior."
license: Apache-2.0 AND CC-BY-SA-4.0 AND MIT
---

# GNCore Software Engineering

Version: 7.0.0rc1

## Choose the work

Choose investigation, implementation, review or refactoring from the requested outcome. Inspect call sites and repository conventions. Separate a confirmed cause from a hypothesis and avoid speculative broad rewrites.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

A scoped patch or requested engineering artifact, a clear acceptance contract, and reproducible evidence for changed behavior.

Run the relevant reproduction, unit/integration checks, build or type checks. Cover the observed failure and an important boundary without copying implementation details into assertions.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

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

## Focused procedures

### GNCore Grill Me (`code-grill-me`)

Identify decisions that materially change scope, contracts or feasibility and ask a short prioritized set of questions. Use repository evidence to answer routine choices yourself. Record settled decisions, assumptions and actual blockers without turning the task into an unbounded interview.

For relevant technical detail, read [the attributed source guide](references/code-grill-me/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Research (`code-research`)

Search code, call sites, installed versions and primary documentation for the concrete technical question. Reproduce the uncertain behavior in a small fixture when possible and separate observations from inference. Deliver a cited recommendation with compatibility limits rather than a generic technology list.

For relevant technical detail, read [the attributed source guide](references/code-research/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Prototype (`code-prototype`)

Choose the single assumption the prototype should test and define an observable result. Build the smallest executable vertical slice with clearly marked simulated boundaries. Record what the experiment establishes, what remains untested and which prototype shortcuts must change before production use.

For relevant technical detail, read [the attributed source guide](references/code-prototype/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Domain Modeling (`code-domain-modeling`)

Extract entities, values, invariants, lifecycle transitions and ownership from actual examples. Test shared vocabulary against awkward cases and identify bounded contexts before assigning service boundaries. Produce a model that clarifies code decisions, not a diagram detached from behavior.

For relevant technical detail, read [the attributed source guide](references/code-domain-modeling/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Decision Mapping (`code-decision-mapping`)

List decisions that materially affect the requested outcome. For each, record options, constraints, dependencies, reversibility, owner, and the evidence needed to choose. Resolve choices already implied by repository conventions; ask about only decisions that affect scope or correctness. Deliver a decision map and a concrete next implementation step, without treating every preference as a blocker.

### GNCore Search First (`code-search-first`)

Inspect repository symbols, dependencies and existing utilities before adding a new implementation. Compare the closest existing path against the needed contract and reuse or extend it when it fits. Record the concrete gap if new code or a dependency is justified.

For relevant technical detail, read [the attributed source guide](references/code-search-first/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Product Lens (`code-product-lens`)

Connect the proposed feature to a specific user problem, current workaround and measurable outcome. Use supplied evidence and identify the cheapest useful uncertainty test. Keep product assumptions explicit without replacing the user's authorized implementation task with an unsolicited strategy exercise.

For relevant technical detail, read [the attributed source guide](references/code-product-lens/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Architecture Decision Records (`code-architecture-decision-records`)

Capture the concrete decision, constraints, viable alternatives and consequences with links to code or evidence. State the chosen boundary and reversal/migration cost. Follow the repository's ADR numbering/index conventions and avoid recording routine implementation trivia as architecture policy.

For relevant technical detail, read [the attributed source guide](references/code-architecture-decision-records/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Blueprint (`code-blueprint`)

Split a substantial change into reviewable outcomes with dependencies, acceptance evidence and enough call-path/context information to resume later. Sequence uncertain boundaries early and keep the plan mutable as evidence changes. Do not assume delegation, universal approval gates or a new project structure.

For relevant technical detail, read [the attributed source guide](references/code-blueprint/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Architecture (`code-architecture`)

Map public behavior, module boundaries and the information each module hides. Propose a smaller stable interface for a concrete change and compare call-site complexity before/after. Document the tradeoff and verify contracts rather than adding abstract layers for their own sake.

For relevant technical detail, read [the attributed source guide](references/code-architecture/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Improve Architecture (`code-improve-architecture`)

Find a specific coupling or shallow-module problem in current call paths. Choose a bounded deepening/refactor, preserve behavior with representative regressions and migrate callers in a reviewable sequence. Explain the reduced change surface with concrete before/after examples.

For relevant technical detail, read [the attributed source guide](references/code-improve-architecture/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Quality (`code-quality`)

Review the changed code against local naming, error handling, API clarity and maintainability conventions. Prioritize defects or complexity with concrete consequences and preserve behavior while improving it. Run the relevant formatter/type/lint/tests without weakening their rules to make the diff pass.

For relevant technical detail, read [the attributed source guide](references/code-quality/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Codebase Onboarding (`code-codebase-onboarding`)

Trace entrypoints, important data/control paths, build/test commands and extension boundaries in the current revision. Produce a concise evidence-linked map and a verified starter task. Do not silently install hooks or rewrite the host agent's configuration as part of learning the codebase.

For relevant technical detail, read [the attributed source guide](references/code-codebase-onboarding/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Plankton Code Quality (`code-plankton-code-quality`)

Use Plankton only if the project requests or already configures it; inspect its actual executable and supported settings. Diagnose formatter/linter or hook failures at the configured boundary and verify their effect on a fixture. Do not assume a Claude-specific hook exists in another host.

For relevant technical detail, read [the attributed source guide](references/code-plankton-code-quality/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Code Review (`code-code-review`)

Inspect the complete changed behavior and relevant callers/specification. Report actionable correctness, compatibility, security or performance findings with file/line evidence and a failure scenario. Separate definite defects from questions and style preferences; do not invent findings to fill a quota.

For relevant technical detail, read [the attributed source guide](references/code-code-review/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Request Refactor Plan (`code-request-refactor-plan`)

Inspect the current implementation, callers, and regression coverage. State the concrete maintainability problem and the observable behaviors that must remain unchanged. Propose a sequence of small changes with touched modules, compatibility boundaries, and checks for each step. Flag data migrations or API breaks explicitly. Deliver the requested plan; implement it only when implementation is within the user's request.

### GNCore Code Improver (`code-code-improver`)

Bound the review target and define which checks establish correct behavior. Fix the highest-impact observed issue, rerun relevant checks and inspect the resulting diff. Stop when acceptance is met or unchanged failures need new evidence; do not repeatedly rewrite clean code for cosmetic variety.

For relevant technical detail, read [the attributed source guide](references/code-code-improver/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Code Maturity Assessor (`code-code-maturity-assessor`)

Evaluate the supplied repository against explicit dimensions such as correctness evidence, operational ownership, dependency hygiene and maintainability. Cite observable evidence and missing evidence for each assessment. Do not equate a numerical rubric score with certification or compare incompatible project scopes.

For relevant technical detail, read [the attributed source guide](references/code-code-maturity-assessor/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Tdd (`code-tdd`)

Write a behavioral regression that fails for the intended reason, implement the smallest contract-correct change and refactor after green. Cover an important boundary beyond the initial happy path. Use TDD where it clarifies behavior rather than adding mirror tests for trivial reversible edits.

For relevant technical detail, read [the attributed source guide](references/code-tdd/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Tdd Workflow (`code-tdd-workflow`)

Plan the test boundary and fixtures before changing behavior. Keep a red/green/refactor loop around user-visible contracts and integration risks, with deterministic cleanup. Choose coverage based on meaningful failure paths rather than enforcing an arbitrary percentage as proof of quality.

For relevant technical detail, read [the attributed source guide](references/code-tdd-workflow/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore E2E Testing (`code-e2e-testing`)

Select a critical user journey, deterministic setup and isolated test identity. Assert visible state through accessible selectors, wait for conditions and clean up side effects. Capture browser/environment evidence and error paths; avoid fixed sleeps and assertions coupled only to CSS classes.

For relevant technical detail, read [the attributed source guide](references/code-e2e-testing/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Ai Regression Testing (`code-ai-regression-testing`)

Version representative prompts, tool fixtures and expected observable outcomes before changing model-assisted behavior. Compare constraint compliance and task completion on the same inputs, preserving failure traces. Separate nondeterministic semantic review from deterministic schema/tool checks.

For relevant technical detail, read [the attributed source guide](references/code-ai-regression-testing/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Module Regression (`code-module-regression`)

Map the changed module's downstream consumers and public contracts. Add targeted regressions at the affected boundary and run representative consumer checks; retain an acceptance-command ledger only when it helps the repository. Do not assume every module needs the same end-to-end suite.

For relevant technical detail, read [the attributed source guide](references/code-module-regression/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Property Based Testing (`code-property-based-testing`)

State an invariant independent of the implementation and define valid generators plus invalid boundaries. Compare against a simple oracle or metamorphic relation and retain minimized counterexamples. Avoid generators that exclude the failure class or properties that merely restate the code.

For relevant technical detail, read [the attributed source guide](references/code-property-based-testing/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Coverage Analysis (`code-coverage-analysis`)

Use coverage to find unexercised branches relevant to the change, then inspect their failure impact. Add meaningful inputs/assertions for important gaps and explain remaining exclusions. A high line percentage is not evidence that assertions detect defects.

For relevant technical detail, read [the attributed source guide](references/code-coverage-analysis/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Debugging (`code-debugging`)

Reproduce the failure and trace the responsible state/data transition before editing. Form a specific hypothesis, use the smallest discriminating probe and fix the confirmed cause. Keep the original reproduction and a boundary regression to demonstrate the problem is resolved.

For relevant technical detail, read [the attributed source guide](references/code-debugging/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Verification Before Completion (`code-verification-before-completion`)

Match each completion claim to an actually run command, observed artifact or explicit unavailable check. Re-run affected checks after a fix and inspect the final diff. Keep local success, remote CI, deployment and published availability as distinct evidence states.

For relevant technical detail, read [the attributed source guide](references/code-verification-before-completion/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Diagnosing Bugs (`code-diagnosing-bugs`)

Gather the failing input, expected contract, environment/revision and full error context. Narrow the issue by testing competing explanations and relevant callers. Deliver a reproducible diagnosis or a clearly bounded unresolved hypothesis instead of claiming a speculative patch fixed it.

For relevant technical detail, read [the attributed source guide](references/code-diagnosing-bugs/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Qa (`code-qa`)

Translate the feature brief or bug report into observable acceptance cases. Exercise the main journey and relevant permission, failure, empty, concurrency, or recovery cases. Record exact setup, inputs, commands, and outcomes. For a failure, isolate a reproducible case and distinguish implementation defects from environment limitations. Fix and retest when requested; report checks not performed rather than treating missing evidence as a pass.

### GNCore Verification Loop (`code-verification-loop`)

Select checks that expose the changed contract, run them, inspect failure causes and make a focused correction. Repeat only when the new change or evidence justifies it. Preserve useful logs and stop an unchanged failing cycle to investigate the missing dependency or assumption.

For relevant technical detail, read [the attributed source guide](references/code-verification-loop/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Security Review (`code-security-review`)

Trace attacker-controlled input through trust and authorization boundaries to concrete sinks. Reproduce reachable abuse paths safely and prioritize findings by impact and prerequisites. Verify the fix with negative authorization/input cases without scanning unrelated live systems.

For relevant technical detail, read [the attributed source guide](references/code-security-review/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Agent Security Hardening (`code-agent-security-hardening`)

Map model input, retrieved content, tool authority, secrets and side-effect boundaries. Treat untrusted instructions as data, validate tool contracts and bound execution. Test injection, unauthorized tool arguments, secret leakage and retry/budget exhaustion with local fixtures.

For relevant technical detail, read [the attributed source guide](references/code-agent-security-hardening/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Sharp Edges (`code-sharp-edges`)

Inspect public APIs and configuration for defaults or combinations that invite a dangerous mistake. Demonstrate a plausible caller error and propose a safer interface, invariant or diagnostic. Distinguish misuse resistance from a confirmed exploitable vulnerability.

For relevant technical detail, read [the attributed source guide](references/code-sharp-edges/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Insecure Defaults (`code-insecure-defaults`)

Trace configuration values from defaults and environment parsing into sensitive operations. Look for development credentials, debug exposure, permissive origin or network rules, disabled verification, unchecked authorization, and fail-open error handling. Demonstrate the reachable unsafe condition in a local test where practical. Propose a secure default and an explicit opt-in for legitimate development cases; preserve a documented migration path and retest both allowed and denied behavior.

### GNCore Differential Review (`code-differential-review`)

Compare baseline and changed revisions around trust boundaries, validation, state transitions and changed dependencies. Trace security consequences through callers and tests; report only findings supported by a concrete changed behavior and attack or failure scenario.

For relevant technical detail, read [the attributed source guide](references/code-differential-review/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Semgrep (`code-semgrep`)

Check the installed Semgrep version, language support and relevant rules before a bounded local scan. Validate representative matches and false positives against code paths, record command/rule versions and preserve machine-readable findings. Do not treat scanner silence as proof of security.

For relevant technical detail, read [the attributed source guide](references/code-semgrep/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Codeql (`code-codeql`)

Confirm CodeQL support, compiler/database build requirements and query scope for the target language. Build or inspect an authorized local database and run appropriate queries; triage results against actual source/sinks and record limitations when extraction or a language/toolchain is unavailable.

For relevant technical detail, read [the attributed source guide](references/code-codeql/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Sarif Parsing (`code-sarif-parsing`)

Parse SARIF with schema/version awareness, preserving rule IDs, severity, artifact URIs and physical locations. Resolve paths within the intended workspace and handle missing locations/duplicate results explicitly. Test a small known SARIF fixture rather than trusting a tool-specific field layout.

For relevant technical detail, read [the attributed source guide](references/code-sarif-parsing/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Supply Chain Risk Auditor (`code-supply-chain-risk-auditor`)

Inventory direct/transitive dependencies and their exact lockfile identities, sources and install-time behavior. Prioritize provenance, maintenance and reachable security risks with evidence. Keep license and vulnerability review distinct and do not run unknown dependency scripts to assess them.

For relevant technical detail, read [the attributed source guide](references/code-supply-chain-risk-auditor/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Git Workflow (`code-git-workflow`)

Inspect branch and working-tree state, stage only the intended files and prepare a reviewable commit history. Preserve unrelated edits and verify the diff and relevant checks. Distinguish a local commit from a pushed branch or merged change; do not rewrite shared history implicitly.

For relevant technical detail, read [the attributed source guide](references/code-git-workflow/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Delivery Gate (`code-delivery-gate`)

Gather the actual acceptance, compatibility, security, artifact and rollback evidence for this change. Report passed, failed, skipped and missing checks and identify a concrete go/no-go reason. A green test suite alone does not authorize publishing or production rollout.

For relevant technical detail, read [the attributed source guide](references/code-delivery-gate/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Cost Tracking (`code-cost-tracking`)

Define the cost unit and record measured resource/provider usage with runtime/version and workload. Separate known charges, estimates and allocations, and compare like-for-like runs. Do not upload private billing data or introduce a paid tracking service without scope authorization.

For relevant technical detail, read [the attributed source guide](references/code-cost-tracking/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Post Patch Validation (`code-post-patch-validation`)

Re-run the original reproduction and tests at boundaries the patch affects, then inspect the final diff for unintended changes. Verify the patch did not weaken assertions or move the failure downstream. Preserve baseline/candidate evidence and label checks that could not be executed.

For relevant technical detail, read [the attributed source guide](references/code-post-patch-validation/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Mutation Testing (`code-mutation-testing`)

Choose important behavior and a bounded mutation scope, verify the baseline suite, then inspect surviving meaningful mutants. Improve assertions or fixtures for real gaps; classify equivalent/unsupported mutants instead of gaming a percentage. Keep expensive or environment-mutating runs explicitly scoped.

For relevant technical detail, read [the attributed source guide](references/code-mutation-testing/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Deep Research (`code-deep-research`)

Frame the engineering uncertainty and identify primary sources, relevant code and a reproducible experiment. Compare contradictory evidence by version/method and retain citations. Deliver a decision with limits and next evidence, not an exhaustive uncited survey.

For relevant technical detail, read [the attributed source guide](references/code-deep-research/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Research Ops (`code-research-ops`)

Record the research question, source/version provenance, retrieval date, reproduction inputs and unresolved claims so another maintainer can repeat the work. Separate a cached source observation from a fresh review and do not silently overwrite accepted evidence.

For relevant technical detail, read [the attributed source guide](references/code-research-ops/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Product Capability (`code-product-capability`)

Trace a requested capability through actual user flows, code, data, integrations and operational dependencies. Mark implemented, partial and missing behavior with evidence. Propose a bounded completion path without describing documentation or a mocked screen as a working backend feature.

For relevant technical detail, read [the attributed source guide](references/code-product-capability/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore To Prd (`code-to-prd`)

Describe the target users, current problem, desired outcome, scope, and explicit non-goals from the supplied context. Define functional behavior, key user journeys, constraints, dependencies, measurable acceptance criteria, and open decisions. Separate observed evidence from assumptions. Keep implementation details only where they constrain the product; avoid invented market claims, delivery estimates, or approvals.

### GNCore To Spec (`code-to-spec`)

Convert agreed requirements into explicit actors, inputs, state transitions, public contracts and acceptance examples. Surface contradictions and material unresolved decisions before implementation. Preserve user choices and distinguish normative behavior from illustrative implementation suggestions.

For relevant technical detail, read [the attributed source guide](references/code-to-spec/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore To Tickets (`code-to-tickets`)

Split an accepted specification into coherent deliverables with dependencies, scope exclusions and observable acceptance. Keep each ticket independently understandable and connect it to the parent requirement. Avoid arbitrary task fragmentation or creating external issues unless requested.

For relevant technical detail, read [the attributed source guide](references/code-to-tickets/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Writing Plans (`code-writing-plans`)

Inspect the relevant code paths and risks, then sequence reviewable implementation outcomes with concrete validation. Resolve routine choices from repository context and keep actual blockers explicit. Do not substitute a long plan for authorized implementation work.

For relevant technical detail, read [the attributed source guide](references/code-writing-plans/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Executing Plans (`code-executing-plans`)

Reconcile the supplied plan with the current working tree, execute the next dependency-ready outcome and verify it. Update the plan when evidence invalidates an assumption, preserving the intended goal. Report concrete results rather than ticking steps whose artifacts do not exist.

For relevant technical detail, read [the attributed source guide](references/code-executing-plans/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Requesting Code Review (`code-requesting-code-review`)

Prepare the actual diff, behavior/specification context and validation evidence for a reviewer. State the decisions or risks that need attention and provide a reproducible example when helpful. Do not send external review requests or messages unless the user authorized them.

For relevant technical detail, read [the attributed source guide](references/code-requesting-code-review/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Receiving Code Review (`code-receiving-code-review`)

Reproduce or inspect each review claim against the contract and current code. Fix substantiated issues with focused regressions, explain disagreements with evidence and rerun affected checks. Do not accept an incorrect change merely because it was requested by another reviewer.

For relevant technical detail, read [the attributed source guide](references/code-receiving-code-review/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Implement (`code-implement`)

Trace the requested behavior through callers and existing conventions, implement the complete scoped change and validate meaningful success/failure cases. Preserve public contracts and unrelated user work; state unavailable integration evidence instead of replacing real behavior with an undisclosed mock.

For relevant technical detail, read [the attributed source guide](references/code-implement/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Implement Spec (`code-implement-spec`)

Map specification requirements to code paths and acceptance cases, implement the dependency-ready slice and verify contract/error behavior. Track unmet or contradictory requirements explicitly. Do not broaden the feature or change specified semantics just to fit an easier implementation.

For relevant technical detail, read [the attributed source guide](references/code-implement-spec/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Python (`code-python`)

Inspect the supported Python versions and public contract, implement idiomatic modules with explicit error/data boundaries and avoid unnecessary dependencies. Verify relevant behavior and clean imports under the declared runtime rather than relying on the developer's editable environment.

For relevant technical detail, read [the attributed source guide](references/code-python/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Python Testing (`code-python-testing`)

Choose unit or integration boundaries around the actual Python contract, use isolated temporary state and test normal, invalid and regression cases. Parameterize meaningful variations and verify cleanup. Mock external boundaries without replacing the behavior the test is supposed to establish.

For relevant technical detail, read [the attributed source guide](references/code-python-testing/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Webapp Testing (`code-webapp-testing`)

Run the actual web application with isolated data, exercise a representative journey and assert user-visible outcomes. Check console/network errors, invalid input and relevant states; retain browser/environment evidence. Do not claim visual or interaction validation from a successful server start alone.

For relevant technical detail, read [the attributed source guide](references/code-webapp-testing/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Regression Hunt (`code-regression-hunt`)

Use baseline/candidate behavior, failing inputs and change history to narrow a regression, employing bisection only when revisions are reproducible. Preserve a minimal reproduction and identify the first meaningful behavioral change before proposing the fix.

For relevant technical detail, read [the attributed source guide](references/code-regression-hunt/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Brainstorming (`code-brainstorming`)

Explore a small set of viable approaches against the user's constraints and current repository. Identify the uncertain tradeoff and choose a useful next experiment or implementation direction. Keep explicit user decisions intact and avoid an approval ritual for ordinary reversible work.

For relevant technical detail, read [the attributed source guide](references/code-brainstorming/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Using Git Worktrees (`code-using-git-worktrees`)

Inspect branch/worktree state and create an isolated checkout only when it helps protect existing work or separate concurrent changes. Use a nonconflicting branch and verify the worktree path. Do not delete user worktrees, rewrite history or assume multiple agents are authorized.

For relevant technical detail, read [the attributed source guide](references/code-using-git-worktrees/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Subagent Driven Development (`code-subagent-driven-development`)

Delegate only when the host supports it and the task authorizes delegation. Give independent work a bounded contract and minimal context, integrate results through actual diff/test review and keep shared mutations coordinated. Complete the work directly when delegation is unavailable or unauthorized.

For relevant technical detail, read [the attributed source guide](references/code-subagent-driven-development/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Finishing A Development Branch (`code-finishing-a-development-branch`)

Inspect the final diff, working tree and validation evidence, then prepare the requested commit/review/release material. Keep push, merge, tag and publication states explicit and honor existing authorization. Do not discard uncommitted work as part of cleanup.

For relevant technical detail, read [the attributed source guide](references/code-finishing-a-development-branch/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Workflow Setup (`code-workflow-setup`)

Inspect which workflow tools and conventions the project actually requests and preserve existing settings. Prepare a minimal reviewable configuration and verify its commands on a fixture. Do not install unrelated hooks, global agents or mandatory approvals from a source author's personal setup.

For relevant technical detail, read [the attributed source guide](references/code-workflow-setup/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore General Coding Workflow (`code-build`)

Inspect the relevant source, current behavior, user request, and repository instructions. Choose the smallest useful set of coding skills for the task: requirements or architecture for unresolved design, the actual stack for implementation, and a suitable testing or debugging workflow for verification. Build the complete requested result, preserve unrelated work, and report concrete evidence. Do not load all installed skills for every task.

### Requirements Clarifier (`requirements`)

Your job is to turn a rough request into a precise implementation brief.
Ask for missing constraints, surface risks early, capture acceptance criteria, and refuse to guess on critical decisions.
Prefer short, direct questions and summarize the result as a checklist the next skill can execute.

### Architecture Designer (`architecture`)

Convert requirements into a clean, typed architecture.
Define modules, ownership boundaries, data flow, invariants, and failure handling.
Choose the simplest design that can be extended without duplicating logic.

### Implementation Builder (`implementation`)

Implement the agreed design directly, keep code explicit and typed, and avoid speculative abstractions.
Make the smallest change that satisfies the contract, then verify it with targeted tests or checks.

### Code Reviewer (`review`)

Look for correctness issues, API mismatches, risky assumptions, and missing tests.
State concrete findings first, then give a short summary of residual risk.

### Testing Specialist (`testing`)

Create targeted unit and integration tests that fail before the fix and pass after it.
Prefer clear fixture setup and assertions that verify the observable behavior, not implementation details.

### Security Reviewer (`security`)

Check for unsafe writes, path traversal, secret leakage, and privilege escalation.
Treat file-system code as hostile-input code and require explicit validation.

### Documentation Writer (`documentation`)

Document the actual command surface, file layout, and operational behavior.
Avoid marketing language and keep examples runnable.

### Release Manager (`release`)

Ensure packaging metadata is correct, the distribution is reproducible, and release notes reflect the shipped behavior.
Confirm that the repository is publishable before marking the release complete.

### Product Discovery (`product-discovery`)

Separate user problem, evidence, assumptions, and proposed solution. Identify target users, current alternatives, constraints, and measurable outcome. Rank unknowns by risk and propose the cheapest test that can resolve them. Define a narrow first release with explicit exclusions and acceptance criteria. Do not present guesses as user research.

### Software Feature Delivery (`software-feature`)

Trace the feature through interfaces and data flow, define observable behavior, make the smallest coherent change, add boundary tests, and run targeted regressions. Preserve unrelated user work and report exact checks.

### Software Architecture Decision (`software-architecture`)

Capture context, quality attributes, constraints, alternatives, trade-offs, failure modes, and a decision owner. Prefer incremental reversible choices and validate assumptions with a small implementation where useful.

### Software Code Review (`software-code-review`)

Inspect the full diff and relevant callers, identify concrete reproducible findings with severity and file locations, and separate defects from preferences. Confirm fixes with targeted regression checks.

### Software Debugging (`software-debugging`)

Reproduce or isolate the failing condition, inspect logs and state, form testable hypotheses, and narrow the cause before editing. Add a regression test, fix the root cause, and rerun the failure and impacted checks.

### Safe Refactoring (`software-refactor`)

Capture behavior with tests or characterization, identify callers, make small mechanical steps, and run tests after each risky step. Avoid unrelated redesign and compare externally observable behavior before and after.

### Software API Contract (`software-api-contract`)

Inspect actual consumers, validate schemas and authorization boundaries, specify error semantics and compatibility, and test contract fixtures. Flag breaking behavior and provide a migration path.

### Dependency Change Review (`software-dependency`)

Check supported versions, changelog, transitive effects, license policy, lockfile behavior, and known vulnerabilities. Change only needed packages, run affected tests, and record rollback and compatibility results.

### Software Performance Optimization (`software-performance`)

Establish repeatable workload and baseline, profile the critical path, estimate impact and resource trade-offs, then change one bottleneck. Rerun correctness tests and comparable benchmarks; report uncertainty.

### Software Migration Plan (`software-migration`)

Inventory dependencies and consumers, define target and interim states, map changes and data movement, and stage by reversible boundaries. Test backward compatibility and rollback before production cutover.

### Software Release Candidate (`software-release`)

Check version, diff, changelog, build provenance, tests, dependency locks, supported platforms, migrations, and known issues. Separate passed, skipped, and blocked gates; do not publish without authorization.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
