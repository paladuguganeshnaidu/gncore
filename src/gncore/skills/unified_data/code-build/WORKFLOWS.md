# GNCore Software Engineering: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### GNCore Grill Me (`code-grill-me`)

Identify decisions that materially change scope, contracts or feasibility and ask a short prioritized set of questions. Use repository evidence to answer routine choices yourself. Record settled decisions, assumptions and actual blockers without turning the task into an unbounded interview.

Technical reference: [attributed source guide](references/code-grill-me/UPSTREAM.md).

### GNCore Research (`code-research`)

Search code, call sites, installed versions and primary documentation for the concrete technical question. Reproduce the uncertain behavior in a small fixture when possible and separate observations from inference. Deliver a cited recommendation with compatibility limits rather than a generic technology list.

Technical reference: [attributed source guide](references/code-research/UPSTREAM.md).

### GNCore Prototype (`code-prototype`)

Choose the single assumption the prototype should test and define an observable result. Build the smallest executable vertical slice with clearly marked simulated boundaries. Record what the experiment establishes, what remains untested and which prototype shortcuts must change before production use.

Technical reference: [attributed source guide](references/code-prototype/UPSTREAM.md).

### GNCore Domain Modeling (`code-domain-modeling`)

Extract entities, values, invariants, lifecycle transitions and ownership from actual examples. Test shared vocabulary against awkward cases and identify bounded contexts before assigning service boundaries. Produce a model that clarifies code decisions, not a diagram detached from behavior.

Technical reference: [attributed source guide](references/code-domain-modeling/UPSTREAM.md).

### GNCore Decision Mapping (`code-decision-mapping`)

List decisions that materially affect the requested outcome. For each, record options, constraints, dependencies, reversibility, owner, and the evidence needed to choose. Resolve choices already implied by repository conventions; ask about only decisions that affect scope or correctness. Deliver a decision map and a concrete next implementation step, without treating every preference as a blocker.

### GNCore Search First (`code-search-first`)

Inspect repository symbols, dependencies and existing utilities before adding a new implementation. Compare the closest existing path against the needed contract and reuse or extend it when it fits. Record the concrete gap if new code or a dependency is justified.

Technical reference: [attributed source guide](references/code-search-first/UPSTREAM.md).

### GNCore Product Lens (`code-product-lens`)

Connect the proposed feature to a specific user problem, current workaround and measurable outcome. Use supplied evidence and identify the cheapest useful uncertainty test. Keep product assumptions explicit without replacing the user's authorized implementation task with an unsolicited strategy exercise.

Technical reference: [attributed source guide](references/code-product-lens/UPSTREAM.md).

### GNCore Architecture Decision Records (`code-architecture-decision-records`)

Capture the concrete decision, constraints, viable alternatives and consequences with links to code or evidence. State the chosen boundary and reversal/migration cost. Follow the repository's ADR numbering/index conventions and avoid recording routine implementation trivia as architecture policy.

Technical reference: [attributed source guide](references/code-architecture-decision-records/UPSTREAM.md).

### GNCore Blueprint (`code-blueprint`)

Split a substantial change into reviewable outcomes with dependencies, acceptance evidence and enough call-path/context information to resume later. Sequence uncertain boundaries early and keep the plan mutable as evidence changes. Do not assume delegation, universal approval gates or a new project structure.

Technical reference: [attributed source guide](references/code-blueprint/UPSTREAM.md).

### GNCore Architecture (`code-architecture`)

Map public behavior, module boundaries and the information each module hides. Propose a smaller stable interface for a concrete change and compare call-site complexity before/after. Document the tradeoff and verify contracts rather than adding abstract layers for their own sake.

Technical reference: [attributed source guide](references/code-architecture/UPSTREAM.md).

### GNCore Improve Architecture (`code-improve-architecture`)

Find a specific coupling or shallow-module problem in current call paths. Choose a bounded deepening/refactor, preserve behavior with representative regressions and migrate callers in a reviewable sequence. Explain the reduced change surface with concrete before/after examples.

Technical reference: [attributed source guide](references/code-improve-architecture/UPSTREAM.md).

### GNCore Quality (`code-quality`)

Review the changed code against local naming, error handling, API clarity and maintainability conventions. Prioritize defects or complexity with concrete consequences and preserve behavior while improving it. Run the relevant formatter/type/lint/tests without weakening their rules to make the diff pass.

Technical reference: [attributed source guide](references/code-quality/UPSTREAM.md).

### GNCore Codebase Onboarding (`code-codebase-onboarding`)

Trace entrypoints, important data/control paths, build/test commands and extension boundaries in the current revision. Produce a concise evidence-linked map and a verified starter task. Do not silently install hooks or rewrite the host agent's configuration as part of learning the codebase.

Technical reference: [attributed source guide](references/code-codebase-onboarding/UPSTREAM.md).

### GNCore Plankton Code Quality (`code-plankton-code-quality`)

Use Plankton only if the project requests or already configures it; inspect its actual executable and supported settings. Diagnose formatter/linter or hook failures at the configured boundary and verify their effect on a fixture. Do not assume a Claude-specific hook exists in another host.

Technical reference: [attributed source guide](references/code-plankton-code-quality/UPSTREAM.md).

### GNCore Code Review (`code-code-review`)

Inspect the complete changed behavior and relevant callers/specification. Report actionable correctness, compatibility, security or performance findings with file/line evidence and a failure scenario. Separate definite defects from questions and style preferences; do not invent findings to fill a quota.

Technical reference: [attributed source guide](references/code-code-review/UPSTREAM.md).

### GNCore Request Refactor Plan (`code-request-refactor-plan`)

Inspect the current implementation, callers, and regression coverage. State the concrete maintainability problem and the observable behaviors that must remain unchanged. Propose a sequence of small changes with touched modules, compatibility boundaries, and checks for each step. Flag data migrations or API breaks explicitly. Deliver the requested plan; implement it only when implementation is within the user's request.

### GNCore Code Improver (`code-code-improver`)

Bound the review target and define which checks establish correct behavior. Fix the highest-impact observed issue, rerun relevant checks and inspect the resulting diff. Stop when acceptance is met or unchanged failures need new evidence; do not repeatedly rewrite clean code for cosmetic variety.

Technical reference: [attributed source guide](references/code-code-improver/UPSTREAM.md).

### GNCore Code Maturity Assessor (`code-code-maturity-assessor`)

Evaluate the supplied repository against explicit dimensions such as correctness evidence, operational ownership, dependency hygiene and maintainability. Cite observable evidence and missing evidence for each assessment. Do not equate a numerical rubric score with certification or compare incompatible project scopes.

Technical reference: [attributed source guide](references/code-code-maturity-assessor/UPSTREAM.md).

### GNCore Tdd (`code-tdd`)

Write a behavioral regression that fails for the intended reason, implement the smallest contract-correct change and refactor after green. Cover an important boundary beyond the initial happy path. Use TDD where it clarifies behavior rather than adding mirror tests for trivial reversible edits.

Technical reference: [attributed source guide](references/code-tdd/UPSTREAM.md).

### GNCore Tdd Workflow (`code-tdd-workflow`)

Plan the test boundary and fixtures before changing behavior. Keep a red/green/refactor loop around user-visible contracts and integration risks, with deterministic cleanup. Choose coverage based on meaningful failure paths rather than enforcing an arbitrary percentage as proof of quality.

Technical reference: [attributed source guide](references/code-tdd-workflow/UPSTREAM.md).

### GNCore E2E Testing (`code-e2e-testing`)

Select a critical user journey, deterministic setup and isolated test identity. Assert visible state through accessible selectors, wait for conditions and clean up side effects. Capture browser/environment evidence and error paths; avoid fixed sleeps and assertions coupled only to CSS classes.

Technical reference: [attributed source guide](references/code-e2e-testing/UPSTREAM.md).

### GNCore Ai Regression Testing (`code-ai-regression-testing`)

Version representative prompts, tool fixtures and expected observable outcomes before changing model-assisted behavior. Compare constraint compliance and task completion on the same inputs, preserving failure traces. Separate nondeterministic semantic review from deterministic schema/tool checks.

Technical reference: [attributed source guide](references/code-ai-regression-testing/UPSTREAM.md).

### GNCore Module Regression (`code-module-regression`)

Map the changed module's downstream consumers and public contracts. Add targeted regressions at the affected boundary and run representative consumer checks; retain an acceptance-command ledger only when it helps the repository. Do not assume every module needs the same end-to-end suite.

Technical reference: [attributed source guide](references/code-module-regression/UPSTREAM.md).

### GNCore Property Based Testing (`code-property-based-testing`)

State an invariant independent of the implementation and define valid generators plus invalid boundaries. Compare against a simple oracle or metamorphic relation and retain minimized counterexamples. Avoid generators that exclude the failure class or properties that merely restate the code.

Technical reference: [attributed source guide](references/code-property-based-testing/UPSTREAM.md).

### GNCore Coverage Analysis (`code-coverage-analysis`)

Use coverage to find unexercised branches relevant to the change, then inspect their failure impact. Add meaningful inputs/assertions for important gaps and explain remaining exclusions. A high line percentage is not evidence that assertions detect defects.

Technical reference: [attributed source guide](references/code-coverage-analysis/UPSTREAM.md).

### GNCore Debugging (`code-debugging`)

Reproduce the failure and trace the responsible state/data transition before editing. Form a specific hypothesis, use the smallest discriminating probe and fix the confirmed cause. Keep the original reproduction and a boundary regression to demonstrate the problem is resolved.

Technical reference: [attributed source guide](references/code-debugging/UPSTREAM.md).

### GNCore Verification Before Completion (`code-verification-before-completion`)

Match each completion claim to an actually run command, observed artifact or explicit unavailable check. Re-run affected checks after a fix and inspect the final diff. Keep local success, remote CI, deployment and published availability as distinct evidence states.

Technical reference: [attributed source guide](references/code-verification-before-completion/UPSTREAM.md).

### GNCore Diagnosing Bugs (`code-diagnosing-bugs`)

Gather the failing input, expected contract, environment/revision and full error context. Narrow the issue by testing competing explanations and relevant callers. Deliver a reproducible diagnosis or a clearly bounded unresolved hypothesis instead of claiming a speculative patch fixed it.

Technical reference: [attributed source guide](references/code-diagnosing-bugs/UPSTREAM.md).

### GNCore Qa (`code-qa`)

Translate the feature brief or bug report into observable acceptance cases. Exercise the main journey and relevant permission, failure, empty, concurrency, or recovery cases. Record exact setup, inputs, commands, and outcomes. For a failure, isolate a reproducible case and distinguish implementation defects from environment limitations. Fix and retest when requested; report checks not performed rather than treating missing evidence as a pass.

### GNCore Verification Loop (`code-verification-loop`)

Select checks that expose the changed contract, run them, inspect failure causes and make a focused correction. Repeat only when the new change or evidence justifies it. Preserve useful logs and stop an unchanged failing cycle to investigate the missing dependency or assumption.

Technical reference: [attributed source guide](references/code-verification-loop/UPSTREAM.md).

### GNCore Security Review (`code-security-review`)

Trace attacker-controlled input through trust and authorization boundaries to concrete sinks. Reproduce reachable abuse paths safely and prioritize findings by impact and prerequisites. Verify the fix with negative authorization/input cases without scanning unrelated live systems.

Technical reference: [attributed source guide](references/code-security-review/UPSTREAM.md).

### GNCore Agent Security Hardening (`code-agent-security-hardening`)

Map model input, retrieved content, tool authority, secrets and side-effect boundaries. Treat untrusted instructions as data, validate tool contracts and bound execution. Test injection, unauthorized tool arguments, secret leakage and retry/budget exhaustion with local fixtures.

Technical reference: [attributed source guide](references/code-agent-security-hardening/UPSTREAM.md).

### GNCore Sharp Edges (`code-sharp-edges`)

Inspect public APIs and configuration for defaults or combinations that invite a dangerous mistake. Demonstrate a plausible caller error and propose a safer interface, invariant or diagnostic. Distinguish misuse resistance from a confirmed exploitable vulnerability.

Technical reference: [attributed source guide](references/code-sharp-edges/UPSTREAM.md).

### GNCore Insecure Defaults (`code-insecure-defaults`)

Trace configuration values from defaults and environment parsing into sensitive operations. Look for development credentials, debug exposure, permissive origin or network rules, disabled verification, unchecked authorization, and fail-open error handling. Demonstrate the reachable unsafe condition in a local test where practical. Propose a secure default and an explicit opt-in for legitimate development cases; preserve a documented migration path and retest both allowed and denied behavior.

### GNCore Differential Review (`code-differential-review`)

Compare baseline and changed revisions around trust boundaries, validation, state transitions and changed dependencies. Trace security consequences through callers and tests; report only findings supported by a concrete changed behavior and attack or failure scenario.

Technical reference: [attributed source guide](references/code-differential-review/UPSTREAM.md).

### GNCore Semgrep (`code-semgrep`)

Check the installed Semgrep version, language support and relevant rules before a bounded local scan. Validate representative matches and false positives against code paths, record command/rule versions and preserve machine-readable findings. Do not treat scanner silence as proof of security.

Technical reference: [attributed source guide](references/code-semgrep/UPSTREAM.md).

### GNCore Codeql (`code-codeql`)

Confirm CodeQL support, compiler/database build requirements and query scope for the target language. Build or inspect an authorized local database and run appropriate queries; triage results against actual source/sinks and record limitations when extraction or a language/toolchain is unavailable.

Technical reference: [attributed source guide](references/code-codeql/UPSTREAM.md).

### GNCore Sarif Parsing (`code-sarif-parsing`)

Parse SARIF with schema/version awareness, preserving rule IDs, severity, artifact URIs and physical locations. Resolve paths within the intended workspace and handle missing locations/duplicate results explicitly. Test a small known SARIF fixture rather than trusting a tool-specific field layout.

Technical reference: [attributed source guide](references/code-sarif-parsing/UPSTREAM.md).

### GNCore Supply Chain Risk Auditor (`code-supply-chain-risk-auditor`)

Inventory direct/transitive dependencies and their exact lockfile identities, sources and install-time behavior. Prioritize provenance, maintenance and reachable security risks with evidence. Keep license and vulnerability review distinct and do not run unknown dependency scripts to assess them.

Technical reference: [attributed source guide](references/code-supply-chain-risk-auditor/UPSTREAM.md).

### GNCore Git Workflow (`code-git-workflow`)

Inspect branch and working-tree state, stage only the intended files and prepare a reviewable commit history. Preserve unrelated edits and verify the diff and relevant checks. Distinguish a local commit from a pushed branch or merged change; do not rewrite shared history implicitly.

Technical reference: [attributed source guide](references/code-git-workflow/UPSTREAM.md).

### GNCore Delivery Gate (`code-delivery-gate`)

Gather the actual acceptance, compatibility, security, artifact and rollback evidence for this change. Report passed, failed, skipped and missing checks and identify a concrete go/no-go reason. A green test suite alone does not authorize publishing or production rollout.

Technical reference: [attributed source guide](references/code-delivery-gate/UPSTREAM.md).

### GNCore Cost Tracking (`code-cost-tracking`)

Define the cost unit and record measured resource/provider usage with runtime/version and workload. Separate known charges, estimates and allocations, and compare like-for-like runs. Do not upload private billing data or introduce a paid tracking service without scope authorization.

Technical reference: [attributed source guide](references/code-cost-tracking/UPSTREAM.md).

### GNCore Post Patch Validation (`code-post-patch-validation`)

Re-run the original reproduction and tests at boundaries the patch affects, then inspect the final diff for unintended changes. Verify the patch did not weaken assertions or move the failure downstream. Preserve baseline/candidate evidence and label checks that could not be executed.

Technical reference: [attributed source guide](references/code-post-patch-validation/UPSTREAM.md).

### GNCore Mutation Testing (`code-mutation-testing`)

Choose important behavior and a bounded mutation scope, verify the baseline suite, then inspect surviving meaningful mutants. Improve assertions or fixtures for real gaps; classify equivalent/unsupported mutants instead of gaming a percentage. Keep expensive or environment-mutating runs explicitly scoped.

Technical reference: [attributed source guide](references/code-mutation-testing/UPSTREAM.md).

### GNCore Deep Research (`code-deep-research`)

Frame the engineering uncertainty and identify primary sources, relevant code and a reproducible experiment. Compare contradictory evidence by version/method and retain citations. Deliver a decision with limits and next evidence, not an exhaustive uncited survey.

Technical reference: [attributed source guide](references/code-deep-research/UPSTREAM.md).

### GNCore Research Ops (`code-research-ops`)

Record the research question, source/version provenance, retrieval date, reproduction inputs and unresolved claims so another maintainer can repeat the work. Separate a cached source observation from a fresh review and do not silently overwrite accepted evidence.

Technical reference: [attributed source guide](references/code-research-ops/UPSTREAM.md).

### GNCore Product Capability (`code-product-capability`)

Trace a requested capability through actual user flows, code, data, integrations and operational dependencies. Mark implemented, partial and missing behavior with evidence. Propose a bounded completion path without describing documentation or a mocked screen as a working backend feature.

Technical reference: [attributed source guide](references/code-product-capability/UPSTREAM.md).

### GNCore To Prd (`code-to-prd`)

Describe the target users, current problem, desired outcome, scope, and explicit non-goals from the supplied context. Define functional behavior, key user journeys, constraints, dependencies, measurable acceptance criteria, and open decisions. Separate observed evidence from assumptions. Keep implementation details only where they constrain the product; avoid invented market claims, delivery estimates, or approvals.

### GNCore To Spec (`code-to-spec`)

Convert agreed requirements into explicit actors, inputs, state transitions, public contracts and acceptance examples. Surface contradictions and material unresolved decisions before implementation. Preserve user choices and distinguish normative behavior from illustrative implementation suggestions.

Technical reference: [attributed source guide](references/code-to-spec/UPSTREAM.md).

### GNCore To Tickets (`code-to-tickets`)

Split an accepted specification into coherent deliverables with dependencies, scope exclusions and observable acceptance. Keep each ticket independently understandable and connect it to the parent requirement. Avoid arbitrary task fragmentation or creating external issues unless requested.

Technical reference: [attributed source guide](references/code-to-tickets/UPSTREAM.md).

### GNCore Writing Plans (`code-writing-plans`)

Inspect the relevant code paths and risks, then sequence reviewable implementation outcomes with concrete validation. Resolve routine choices from repository context and keep actual blockers explicit. Do not substitute a long plan for authorized implementation work.

Technical reference: [attributed source guide](references/code-writing-plans/UPSTREAM.md).

### GNCore Executing Plans (`code-executing-plans`)

Reconcile the supplied plan with the current working tree, execute the next dependency-ready outcome and verify it. Update the plan when evidence invalidates an assumption, preserving the intended goal. Report concrete results rather than ticking steps whose artifacts do not exist.

Technical reference: [attributed source guide](references/code-executing-plans/UPSTREAM.md).

### GNCore Requesting Code Review (`code-requesting-code-review`)

Prepare the actual diff, behavior/specification context and validation evidence for a reviewer. State the decisions or risks that need attention and provide a reproducible example when helpful. Do not send external review requests or messages unless the user authorized them.

Technical reference: [attributed source guide](references/code-requesting-code-review/UPSTREAM.md).

### GNCore Receiving Code Review (`code-receiving-code-review`)

Reproduce or inspect each review claim against the contract and current code. Fix substantiated issues with focused regressions, explain disagreements with evidence and rerun affected checks. Do not accept an incorrect change merely because it was requested by another reviewer.

Technical reference: [attributed source guide](references/code-receiving-code-review/UPSTREAM.md).

### GNCore Implement (`code-implement`)

Trace the requested behavior through callers and existing conventions, implement the complete scoped change and validate meaningful success/failure cases. Preserve public contracts and unrelated user work; state unavailable integration evidence instead of replacing real behavior with an undisclosed mock.

Technical reference: [attributed source guide](references/code-implement/UPSTREAM.md).

### GNCore Implement Spec (`code-implement-spec`)

Map specification requirements to code paths and acceptance cases, implement the dependency-ready slice and verify contract/error behavior. Track unmet or contradictory requirements explicitly. Do not broaden the feature or change specified semantics just to fit an easier implementation.

Technical reference: [attributed source guide](references/code-implement-spec/UPSTREAM.md).

### GNCore Python (`code-python`)

Inspect the supported Python versions and public contract, implement idiomatic modules with explicit error/data boundaries and avoid unnecessary dependencies. Verify relevant behavior and clean imports under the declared runtime rather than relying on the developer's editable environment.

Technical reference: [attributed source guide](references/code-python/UPSTREAM.md).

### GNCore Python Testing (`code-python-testing`)

Choose unit or integration boundaries around the actual Python contract, use isolated temporary state and test normal, invalid and regression cases. Parameterize meaningful variations and verify cleanup. Mock external boundaries without replacing the behavior the test is supposed to establish.

Technical reference: [attributed source guide](references/code-python-testing/UPSTREAM.md).

### GNCore Webapp Testing (`code-webapp-testing`)

Run the actual web application with isolated data, exercise a representative journey and assert user-visible outcomes. Check console/network errors, invalid input and relevant states; retain browser/environment evidence. Do not claim visual or interaction validation from a successful server start alone.

Technical reference: [attributed source guide](references/code-webapp-testing/UPSTREAM.md).

### GNCore Regression Hunt (`code-regression-hunt`)

Use baseline/candidate behavior, failing inputs and change history to narrow a regression, employing bisection only when revisions are reproducible. Preserve a minimal reproduction and identify the first meaningful behavioral change before proposing the fix.

Technical reference: [attributed source guide](references/code-regression-hunt/UPSTREAM.md).

### GNCore Brainstorming (`code-brainstorming`)

Explore a small set of viable approaches against the user's constraints and current repository. Identify the uncertain tradeoff and choose a useful next experiment or implementation direction. Keep explicit user decisions intact and avoid an approval ritual for ordinary reversible work.

Technical reference: [attributed source guide](references/code-brainstorming/UPSTREAM.md).

### GNCore Using Git Worktrees (`code-using-git-worktrees`)

Inspect branch/worktree state and create an isolated checkout only when it helps protect existing work or separate concurrent changes. Use a nonconflicting branch and verify the worktree path. Do not delete user worktrees, rewrite history or assume multiple agents are authorized.

Technical reference: [attributed source guide](references/code-using-git-worktrees/UPSTREAM.md).

### GNCore Subagent Driven Development (`code-subagent-driven-development`)

Delegate only when the host supports it and the task authorizes delegation. Give independent work a bounded contract and minimal context, integrate results through actual diff/test review and keep shared mutations coordinated. Complete the work directly when delegation is unavailable or unauthorized.

Technical reference: [attributed source guide](references/code-subagent-driven-development/UPSTREAM.md).

### GNCore Finishing A Development Branch (`code-finishing-a-development-branch`)

Inspect the final diff, working tree and validation evidence, then prepare the requested commit/review/release material. Keep push, merge, tag and publication states explicit and honor existing authorization. Do not discard uncommitted work as part of cleanup.

Technical reference: [attributed source guide](references/code-finishing-a-development-branch/UPSTREAM.md).

### GNCore Workflow Setup (`code-workflow-setup`)

Inspect which workflow tools and conventions the project actually requests and preserve existing settings. Prepare a minimal reviewable configuration and verify its commands on a fixture. Do not install unrelated hooks, global agents or mandatory approvals from a source author's personal setup.

Technical reference: [attributed source guide](references/code-workflow-setup/UPSTREAM.md).

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
