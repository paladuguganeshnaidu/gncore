# GNCore skill catalog

GNCore 7.0.0rc1 contains **30 developer category skills** and **374 active workflows**, organized into **6 developer capability groups**.

Install a category under `.agents/skills/`, then describe the outcome to a compatible host AI. Its single entrypoint selects the relevant workflows; supporting references are loaded only when needed.

## Primary categories

| Category | Skill ID | Workflows | Use it for |
| --- | --- | --- | --- |
| `ai-engineering` | `ai-engineering` | 6 | Build LLM applications, retrieval and tool-using agents with grounded outputs and measurable task outcomes. |
| `automation` | `automation` | 2 | Implement restartable developer automations with bounded inputs, retries and observable failure recovery. |
| `cloud-devops-sre` | `cloud-devops-sre` | 15 | Build delivery pipelines, cloud infrastructure, containers, Kubernetes and reliable service operations. |
| `code-build` | `code-build` | 85 | Implement, diagnose, review and refactor software across languages while preserving public behavior. |
| `computer-vision` | `computer-vision` | 5 | Build vision datasets, augmentation, detection/segmentation and image inference with task-appropriate evaluation. |
| `cybersecurity` | `cybersecurity` | 12 | Review application, dependency, cloud and agent security using concrete attack paths and scoped evidence. |
| `data-engineering` | `data-engineering` | 4 | Build schema-aware, observable batch/streaming pipelines with restart, reconciliation and lineage. |
| `data-science` | `data-science` | 18 | Analyze data, statistics and experiments with correct grain, reproducibility and honest uncertainty. |
| `databases` | `databases` | 5 | Design relational schemas, SQL, transactions, indexes and reversible data migrations. |
| `deep-learning` | `deep-learning` | 9 | Engineer reproducible deep-learning training, checkpointing, fine-tuning and distributed optimization. |
| `design-ux` | `design-ux` | 12 | Design developer-facing and product interfaces, flows, accessible interaction and reusable component systems. |
| `developer-research` | `developer-research` | 4 | Investigate technical options, papers, APIs and reproducible engineering experiments from primary evidence. |
| `developer-tools` | `developer-tools` | 2 | Build reliable CLIs, developer workflows, editor integrations and local tooling. |
| `distributed-systems` | `distributed-systems` | 4 | Design and implement concurrency, queues, replication and failure recovery across service boundaries. |
| `documentation` | `documentation` | 3 | Write technical references, tutorials, API documentation and migration guides from verified software behavior. |
| `embedded-systems` | `embedded-systems` | 4 | Build firmware, peripheral interfaces and constrained-device software with explicit timing and hardware boundaries. |
| `game-development` | `game-development` | 1 | Build playable game mechanics, simulation state, assets and measured runtime performance. |
| `machine-learning` | `machine-learning` | 21 | Develop classical ML and time-series experiments with leakage-safe splits, baselines and deployment-relevant evaluation. |
| `mlops` | `mlops` | 10 | Package, serve, monitor and roll back models with reproducible artifacts and explicit promotion gates. |
| `mobile-development` | `mobile-development` | 1 | Build mobile applications with lifecycle-safe state, offline behavior and platform-appropriate interaction. |
| `natural-language-processing` | `natural-language-processing` | 5 | Build tokenization, text classification, sequence labeling and language-model adaptation pipelines. |
| `neural-networks` | `neural-networks` | 6 | Design and debug neural networks through tensor contracts, gradient checks, loss semantics and tiny-batch experiments. |
| `observability` | `observability` | 7 | Instrument and diagnose services using actionable logs, metrics, traces and service objectives. |
| `performance-engineering` | `performance-engineering` | 5 | Profile and optimize software using repeatable latency, throughput and memory measurements. |
| `python` | `python` | 3 | Build, profile, package and migrate Python applications and libraries with reproducible environments. |
| `release-engineering` | `release-engineering` | 2 | Prepare tested software releases, reproducible artifacts, migrations and approval-ready publication plans. |
| `systems-programming` | `systems-programming` | 4 | Build Rust, C/C++ and native components with explicit ownership, ABI and resource lifetimes. |
| `testing` | `testing` | 19 | Design and implement unit, integration, contract, end-to-end and performance verification. |
| `web-backend` | `web-backend` | 60 | Implement backend services, APIs, integrations and framework features with explicit contracts and failure behavior. |
| `web-frontend` | `web-frontend` | 40 | Build complete responsive web interfaces and choose an appropriate visual direction from the product brief. |

## Developer domains

| Domain | Category skills | Active workflows |
| --- | --- | --- |
| Web and Applications | `web-frontend`, `web-backend`, `design-ux`, `mobile-development`, `game-development` | 114 |
| AI and Machine Learning | `machine-learning`, `neural-networks`, `deep-learning`, `computer-vision`, `natural-language-processing`, `mlops`, `ai-engineering` | 62 |
| Data and Databases | `data-engineering`, `data-science`, `databases` | 27 |
| Systems and Performance | `systems-programming`, `embedded-systems`, `distributed-systems`, `performance-engineering` | 17 |
| Delivery and Reliability | `cloud-devops-sre`, `cybersecurity`, `observability`, `testing`, `release-engineering` | 55 |
| Developer Workflow | `code-build`, `python`, `developer-tools`, `documentation`, `automation`, `developer-research` | 99 |

## Complete workflow map

These IDs remain CLI/API compatibility aliases. Exporting aliases from one category produces one merged category folder. Primary category names take precedence over older generic names when they collide.

### GNCore AI Engineering (`ai-engineering`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `llm-evaluation` | `ai-engineering` | Evaluate an LLM Workflow | Measure an LLM feature with representative cases, explicit rubrics, failure analysis, and repeatable comparisons. |
| `llm-app` | `ai-engineering` | LLM Application Engineering | Implement reliable LLM features with structured outputs, bounded tools, privacy, and graceful failure handling. |
| `rag` | `ai-engineering` | Retrieval-Augmented Generation | Build a grounded retrieval workflow with traceable sources, chunking tests, and abstention on missing evidence. |
| `prompt-engineering` | `ai-engineering` | Prompt Engineering | Improve prompts against explicit tasks and evaluations while preserving tool and safety boundaries. |
| `ai-tool-contracts` | `ai-engineering` | Tool contracts and bounded agents | Tool contracts and bounded agents. |
| `ai-retrieval-evaluation` | `ai-engineering` | Retrieval and grounding evaluation | Retrieval and grounding evaluation. |

### GNCore Automation (`automation`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `workflow-automation` | `automation` | Workflow Automation | Automate a repetitive workflow with bounded inputs, safe retries, idempotency, and clear human checkpoints. |
| `automation-resume` | `automation` | Resume after partial execution | Resume after partial execution. |

### GNCore Cloud, DevOps and SRE (`cloud-devops-sre`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `cloud-architecture` | `cloud-devops-sre` | Cloud Architecture | Design a cloud deployment around explicit reliability, security, operations, and cost constraints. |
| `cost-optimization` | `cloud-devops-sre` | Cloud Cost Optimization | Find measurable cloud cost reductions while protecting reliability and workload correctness. |
| `cloud-architecture-review` | `cloud-devops-sre` | Cloud Architecture Review | Compare cloud designs against workload, reliability, security, cost, and operational constraints. |
| `cloud-infrastructure-code` | `cloud-devops-sre` | Infrastructure as Code | Author or review infrastructure changes with plan inspection, least privilege, and rollback. |
| `cloud-ci-cd` | `cloud-devops-sre` | CI/CD Pipeline | Improve a delivery pipeline with reproducibility, least privilege, useful gates, and rollback. |
| `cloud-container` | `cloud-devops-sre` | Container Build and Hardening | Build a reproducible container with a minimal attack surface and reliable runtime behavior. |
| `cloud-kubernetes` | `cloud-devops-sre` | Kubernetes Workload Review | Review Kubernetes workloads for availability, resource bounds, identity, health, and rollout safety. |
| `cloud-slo` | `cloud-devops-sre` | SLO and Error Budget | Define service-level indicators and objectives that reflect user-visible reliability. |
| `cloud-observability` | `cloud-devops-sre` | Service Observability | Instrument service behavior with actionable metrics, structured logs, and traces. |
| `cloud-incident` | `cloud-devops-sre` | SRE Incident Management | Manage a reliability incident through impact assessment, safe mitigation, verification, and learning. |
| `cloud-capacity` | `cloud-devops-sre` | Capacity and Load Plan | Plan service capacity using measured demand, bottleneck data, growth uncertainty, and failure headroom. |
| `cloud-cost` | `cloud-devops-sre` | Cloud Cost Optimization | Reduce measurable infrastructure spend while protecting service objectives and recovery options. |
| `devops` | `cloud-devops-sre` | DevOps Engineering | Improve build and delivery workflows with reproducible steps, safe rollout, and actionable failure signals. |
| `kubernetes` | `cloud-devops-sre` | Kubernetes Engineering | Author Kubernetes resources with least privilege, clear health behavior, and safe rollout settings. |
| `incident-response` | `cloud-devops-sre` | Incident Response | Triage incidents from evidence, reduce impact safely, and preserve a clear timeline and follow-up. |

### GNCore Software Engineering (`code-build`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `code-grill-me` | `code-build` | GNCore Grill Me | Clarify a coding or product request through focused questions that expose assumptions and missing decisions. |
| `code-research` | `code-build` | GNCore Research | Investigate a technical question using repository evidence and relevant primary sources. |
| `code-prototype` | `code-build` | GNCore Prototype | Build a scoped prototype that tests a specific technical or product assumption. |
| `code-domain-modeling` | `code-build` | GNCore Domain Modeling | Model domain concepts, invariants, ownership, and language before changing service boundaries. |
| `code-decision-mapping` | `code-build` | GNCore Decision Mapping | Map unresolved implementation decisions, dependencies, options, and evidence needed to choose. |
| `code-search-first` | `code-build` | GNCore Search First | Search the existing codebase and relevant documentation before adding dependencies or implementing duplicate functionality. |
| `code-product-lens` | `code-build` | GNCore Product Lens | Validate the why before building through four product diagnostics — a YC-style product diagnostic that produces PRODUCT-BRIEF.md with a go/no-go recommendation, a founder review scoring product-market-fit signals, a user journey audit measuring time-to-value, and ICE feature prioritization. |
| `code-architecture-decision-records` | `code-build` | GNCore Architecture Decision Records | Capture architectural decisions as numbered ADR markdown files in docs/adr/ with context, alternatives considered, consequences, and an index README. |
| `code-blueprint` | `code-build` | GNCore Blueprint | Turn a one-line objective into a step-by-step construction plan for multi-session, multi-agent engineering projects: one-PR-sized steps with self-contained context briefs, dependency graph with parallel-step detection, adversarial review gate, and plan mutation protocol. |
| `code-architecture` | `code-build` | GNCore Architecture | Shared vocabulary for designing deep modules. |
| `code-improve-architecture` | `code-build` | GNCore Improve Architecture | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| `code-quality` | `code-build` | GNCore Quality | Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. |
| `code-codebase-onboarding` | `code-build` | GNCore Codebase Onboarding | Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry points, conventions, and a starter CLAUDE.md. |
| `code-plankton-code-quality` | `code-build` | GNCore Plankton Code Quality | Write-time code quality enforcement using Plankton — auto-formatting, linting, and Claude-powered fixes on every file edit via hooks. |
| `code-code-review` | `code-build` | GNCore Code Review | Review a code diff for correctness, local coding standards, and alignment with its originating specification. |
| `code-request-refactor-plan` | `code-build` | GNCore Request Refactor Plan | Plan a behavior-preserving refactor with explicit scope, sequencing, and regression checks. |
| `code-code-improver` | `code-build` | GNCore Code Improver | Run a bounded review-and-fix loop over a specified code target with evidence and scope controls. |
| `code-code-maturity-assessor` | `code-build` | GNCore Code Maturity Assessor | Systematic code maturity assessment using Trail of Bits' 9-category framework. |
| `code-tdd` | `code-build` | GNCore Tdd | Implement a behavior change through meaningful failing tests, a focused fix, and relevant regressions. |
| `code-tdd-workflow` | `code-build` | GNCore Tdd Workflow | Test-driven development workflow: write a failing test first, watch it fail, implement the smallest change to green, then refactor with 80%+ coverage across unit, integration, and E2E tests. |
| `code-e2e-testing` | `code-build` | GNCore E2E Testing | Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies. |
| `code-ai-regression-testing` | `code-build` | GNCore Ai Regression Testing | Regression testing strategies for AI-assisted development. |
| `code-module-regression` | `code-build` | GNCore Module Regression | Govern cross-module regression in large repositories with a REGRESSION.md ledger that records each module's downstream consumers and executable acceptance command. |
| `code-property-based-testing` | `code-build` | GNCore Property Based Testing | Writes, reviews, and debugs property-based tests — Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. |
| `code-coverage-analysis` | `code-build` | GNCore Coverage Analysis | Measures and interprets what a fuzzing campaign actually reaches, using llvm-cov, lcov, or a fuzzer's own coverage output. |
| `code-debugging` | `code-build` | GNCore Debugging | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| `code-verification-before-completion` | `code-build` | GNCore Verification Before Completion | Verify the requested software outcome with fresh command output before reporting completion. |
| `code-diagnosing-bugs` | `code-build` | GNCore Diagnosing Bugs | Diagnosis loop for hard bugs and performance regressions. |
| `code-qa` | `code-build` | GNCore Qa | Validate a software change against acceptance criteria and reproduce observable regressions. |
| `code-verification-loop` | `code-build` | GNCore Verification Loop | Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, security grep, and diff review — then produce a PASS/FAIL verification report. |
| `code-security-review` | `code-build` | GNCore Security Review | Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing payment/sensitive features. |
| `code-agent-security-hardening` | `code-build` | GNCore Agent Security Hardening | Security hardening guidance for AI agent frameworks that process untrusted content, invoke tools, write workspace files, manage runtime identifiers, or handle credentials. |
| `code-sharp-edges` | `code-build` | GNCore Sharp Edges | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. |
| `code-insecure-defaults` | `code-build` | GNCore Insecure Defaults | Find unsafe configuration defaults and fail-open behavior in application code and deployment configuration. |
| `code-differential-review` | `code-build` | GNCore Differential Review | Performs security-focused differential review of code changes. |
| `code-semgrep` | `code-build` | GNCore Semgrep | Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset through scripts/run-scans.sh, which batches the semgrep processes and writes scans.json, and merges the output to SARIF. |
| `code-codeql` | `code-build` | GNCore Codeql | Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. |
| `code-sarif-parsing` | `code-build` | GNCore Sarif Parsing | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. |
| `code-supply-chain-risk-auditor` | `code-build` | GNCore Supply Chain Risk Auditor | Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upstreams, npm publisher concentration, and install-time script execution. |
| `code-git-workflow` | `code-build` | GNCore Git Workflow | Git workflow patterns including branching strategies, commit conventions, keeping history clean and readable, tidying local commits before merging, merge vs rebase, conflict resolution, and collaborative development best practices for teams of all sizes. |
| `code-delivery-gate` | `code-build` | GNCore Delivery Gate | Stop hook that blocks Claude from finishing until quality checks pass. |
| `code-cost-tracking` | `code-build` | GNCore Cost Tracking | Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log. |
| `code-post-patch-validation` | `code-build` | GNCore Post Patch Validation | Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, root-cause variants, behavior preservation, regressions, and newly introduced security failures. |
| `code-mutation-testing` | `code-build` | GNCore Mutation Testing | Configures mewt or muton campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. |
| `code-deep-research` | `code-build` | GNCore Deep Research | Produce cited research reports from multiple web sources using firecrawl and exa MCP tools — plan sub-questions, search and deep-read sources, then synthesize findings with inline citations and confidence levels. |
| `code-research-ops` | `code-build` | GNCore Research Ops | Evidence-first current-state research workflow for ECC. |
| `code-product-capability` | `code-build` | GNCore Product Capability | Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and unresolved decisions before multi-service work starts. |
| `code-to-prd` | `code-build` | GNCore To Prd | Turn a product idea into a scoped requirements document with user outcomes and acceptance criteria. |
| `code-to-spec` | `code-build` | GNCore To Spec | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. |
| `code-to-tickets` | `code-build` | GNCore To Tickets | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in one file per ticket locally, or native blocking links on a real tracker). |
| `code-writing-plans` | `code-build` | GNCore Writing Plans | Use when you have a spec or requirements for a multi-step task, before touching code |
| `code-executing-plans` | `code-build` | GNCore Executing Plans | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available |
| `code-requesting-code-review` | `code-build` | GNCore Requesting Code Review | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `code-receiving-code-review` | `code-build` | GNCore Receiving Code Review | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation |
| `code-implement` | `code-build` | GNCore Implement | Implement a piece of work based on a spec or set of tickets. |
| `code-implement-spec` | `code-build` | GNCore Implement Spec | Implement the result of /to-spec and /to-tickets in code. |
| `code-python` | `code-build` | GNCore Python | Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintainable Python applications. |
| `code-python-testing` | `code-build` | GNCore Python Testing | Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization, and coverage requirements. |
| `code-webapp-testing` | `code-build` | GNCore Webapp Testing | Toolkit for interacting with and testing local web applications using Playwright. |
| `code-regression-hunt` | `code-build` | GNCore Regression Hunt | Use when investigating regressions in PRs or commits, coordinating a regression campaign, or resuming saved progress. |
| `code-brainstorming` | `code-build` | GNCore Brainstorming | Explore unresolved software design choices and agree on a practical direction when the brief needs clarification. |
| `code-using-git-worktrees` | `code-build` | GNCore Using Git Worktrees | Isolate concurrent coding work in Git worktrees while preserving uncommitted changes and repository conventions. |
| `code-subagent-driven-development` | `code-build` | GNCore Subagent Driven Development | Coordinate authorized coding subagents on separable work with explicit interfaces and integration checks. |
| `code-finishing-a-development-branch` | `code-build` | GNCore Finishing A Development Branch | Prepare a completed development branch for review, integration, or cleanup according to the user's chosen workflow. |
| `code-workflow-setup` | `code-build` | GNCore Workflow Setup | Configure the requested coding workflow's repository context, issue-tracker references, and local skill conventions. |
| `code-build` | `code-build` | GNCore General Coding Workflow | Plan, implement, debug, and verify a software task in its existing language and stack. |
| `requirements` | `code-build` | Requirements Clarifier | Collects scope, constraints, acceptance criteria, and open questions before implementation starts. |
| `architecture` | `code-build` | Architecture Designer | Defines system boundaries, interfaces, and implementation constraints. |
| `implementation` | `code-build` | Implementation Builder | Writes production-grade code with minimal duplication and explicit types. |
| `review` | `code-build` | Code Reviewer | Finds defects, regressions, and missing coverage before release. |
| `testing` | `testing` | Testing Specialist | Designs and validates tests for the changed slice. |
| `security` | `cybersecurity` | Security Reviewer | Assesses secrets handling, unsafe file access, and privilege boundaries. |
| `documentation` | `documentation` | Documentation Writer | Produces concise user and developer documentation that matches the implementation. |
| `release` | `code-build` | Release Manager | Coordinates versioning, packaging, and verification for shipping. |
| `product-discovery` | `code-build` | Product Discovery | Turn a product idea into a testable problem statement, user evidence plan, and scoped first release. |
| `software-feature` | `code-build` | Software Feature Delivery | Deliver a scoped software feature using local conventions and verifiable acceptance criteria. |
| `software-architecture` | `code-build` | Software Architecture Decision | Compare architecture options against constraints, operations, reversibility, and lifecycle cost. |
| `software-code-review` | `code-build` | Software Code Review | Review a code change for correctness, security, maintainability, and missing regression coverage. |
| `software-debugging` | `code-build` | Software Debugging | Diagnose a software failure from reproducible evidence and verify the smallest safe fix. |
| `software-refactor` | `code-build` | Safe Refactoring | Refactor a bounded code area while preserving its documented behavior and public contracts. |
| `software-api-contract` | `code-build` | Software API Contract | Define and verify an API contract across request, response, errors, versioning, and consumers. |
| `software-dependency` | `code-build` | Dependency Change Review | Assess and implement a dependency change with compatibility, security, and rollback evidence. |
| `software-performance` | `code-build` | Software Performance Optimization | Find a measured software bottleneck and optimize it without regressing correctness. |
| `software-migration` | `code-build` | Software Migration Plan | Plan a staged migration with compatibility gates, data safety, and rollback criteria. |
| `software-release` | `code-build` | Software Release Candidate | Prepare a software release with reproducible artifacts, verified changes, and rollback readiness. |

### GNCore Computer Vision (`computer-vision`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `computer-vision` | `computer-vision` | Computer Vision | Build vision workflows with robust image handling, leakage-safe splits, and task-appropriate evaluation. |
| `cv-dataset-audit` | `computer-vision` | Vision dataset integrity | Vision dataset integrity. |
| `cv-geometric-transforms` | `computer-vision` | Image and annotation transforms | Image and annotation transforms. |
| `cv-detection-metrics` | `computer-vision` | Detection and segmentation evaluation | Detection and segmentation evaluation. |
| `cv-inference-parity` | `computer-vision` | Image inference parity | Image inference parity. |

### GNCore Cybersecurity (`cybersecurity`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `cyber-threat-model` | `cybersecurity` | Threat Model | Map assets, trust boundaries, threats, controls, and residual risk for a bounded system. |
| `cyber-secure-code` | `cybersecurity` | Secure Code Review | Review a code change for exploitable input, identity, authorization, secret, and data-flow flaws. |
| `cyber-vulnerability-triage` | `cybersecurity` | Vulnerability Triage | Prioritize a reported vulnerability using affected assets, exploitability, exposure, and impact evidence. |
| `cyber-incident-response` | `cybersecurity` | Cyber Incident Response | Coordinate defensive incident response with containment, evidence preservation, and recovery gates. |
| `cyber-identity-access` | `cybersecurity` | Identity and Access Review | Review identities and permissions for least privilege, lifecycle, ownership, and audit evidence. |
| `cyber-cloud-review` | `cybersecurity` | Cloud Security Review | Assess cloud configuration against an explicit threat model and approved security baseline. |
| `cyber-security-controls` | `cybersecurity` | Security Control Evidence | Map supplied evidence to security control requirements with traceable, bounded conclusions. |
| `cyber-phishing` | `cybersecurity` | Phishing Response Triage | Triage a suspected phishing report and provide safe containment and user guidance. |
| `cyber-secret-response` | `cybersecurity` | Exposed Secret Response | Respond to a potentially exposed credential without echoing or spreading the secret. |
| `cyber-security-test-plan` | `cybersecurity` | Authorized Security Test Plan | Define a bounded security test plan with written authorization, targets, limits, and stop conditions. |
| `web-security` | `cybersecurity` | Web Security Engineering | Review web features for input, session, authorization, and output-handling vulnerabilities. |
| `privacy-review` | `cybersecurity` | Privacy Review | Reduce privacy risk by tracing personal data, purpose, access, retention, and user control. |

### GNCore Data Engineering (`data-engineering`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `data-analysis` | `data-engineering` | Data Analysis | Answer data questions with reproducible calculations, clear definitions, and honest uncertainty. |
| `data-pipelines` | `data-engineering` | Data Pipeline Engineering | Build reliable, observable data pipelines with explicit schemas, retries, and idempotency. |
| `data-pipeline` | `data-engineering` | Data Pipeline Engineering | Build observable, restartable pipelines with explicit schemas, idempotency, and data-quality checks. |
| `data-governance` | `data-engineering` | Data Governance | Define practical ownership, quality, access, lineage, and retention controls for a data asset. |

### GNCore Data Science (`data-science`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `product-analytics` | `data-science` | Product Analytics | Define product metrics and event instrumentation that answer a decision without collecting unnecessary data. |
| `analytics-question` | `data-science` | Analytics Question Plan | Translate a business question into a measurable analysis plan and data requirements. |
| `analytics-data-audit` | `data-science` | Data Quality Audit | Audit analytical data for missingness, duplication, validity, freshness, and grain. |
| `analytics-sql` | `data-science` | Business SQL Analysis | Write a traceable SQL analysis with correct grain, joins, time handling, and reconciliation. |
| `analytics-dashboard` | `data-science` | Decision Dashboard | Design a dashboard around a recurring decision with clear metrics, filters, and data freshness. |
| `analytics-metric-tree` | `data-science` | Metric Tree | Decompose a business outcome into leading drivers and measurable operational inputs. |
| `analytics-cohort` | `data-science` | Cohort Analysis | Compare cohort behavior with consistent definitions, exposure windows, and censoring treatment. |
| `analytics-experiment` | `data-science` | Business Experiment Analysis | Analyze an experiment with assignment, exposure, predeclared outcomes, and uncertainty checks. |
| `analytics-forecast` | `data-science` | Business Forecast Analysis | Build a business forecast from history, drivers, scenarios, and out-of-sample checks. |
| `analytics-insight-brief` | `data-science` | Executive Analytics Brief | Turn analysis into a concise decision brief with traceable evidence and caveats. |
| `analytics-data-contract` | `data-science` | Analytics Data Contract | Specify ownership, schema, quality, freshness, and change handling for an analytics dataset. |
| `clean-data` | `data-science` | Clean a Dataset | Audit and clean a dataset with explicit, reversible rules for missing values, duplicates, types, and outliers. |
| `analyze` | `data-science` | Analyze Data | Answer a data question with reproducible analysis, explicit assumptions, and evidence tied to the provided data. |
| `sql-analysis` | `data-science` | SQL Analysis | Write correct, reviewable SQL for analytics while guarding against join fanout and misleading aggregates. |
| `data-visualization` | `data-science` | Data Visualization | Create clear charts that faithfully represent the underlying data and its uncertainty. |
| `statistics` | `data-science` | Statistical Analysis | Choose and interpret statistical methods with assumptions, uncertainty, and practical effects stated clearly. |
| `ab-testing` | `data-science` | A/B Test Analysis | Analyze controlled experiments with valid assignment checks, predeclared metrics, and practical uncertainty. |
| `geospatial-analysis` | `data-science` | Geospatial Analysis | Analyze spatial data with explicit coordinate systems, units, geometry validity, and privacy controls. |

### GNCore Databases and SQL (`databases`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `database-design` | `databases` | Database Design | Design safe relational data models, queries, and migrations that preserve integrity and performance. |
| `db-transaction-invariants` | `databases` | Transaction and concurrency invariants | Transaction and concurrency invariants. |
| `db-query-plans` | `databases` | Query plan and index analysis | Query plan and index analysis. |
| `db-expand-contract` | `databases` | Expand/backfill/contract migration | Expand/backfill/contract migration. |
| `db-backup-restore` | `databases` | Backup restoration evidence | Backup restoration evidence. |

### GNCore Deep Learning (`deep-learning`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `fine-tuning` | `deep-learning` | Model Fine-Tuning | Plan or implement a parameter-efficient or full fine-tuning workflow with controlled data and cost. |
| `pytorch-training` | `deep-learning` | PyTorch Training | Implement PyTorch training loops with correct device, optimizer, checkpoint, and evaluation handling. |
| `tensorflow-training` | `deep-learning` | TensorFlow and Keras Training | Build TensorFlow/Keras training workflows with explicit data, callbacks, and evaluation behavior. |
| `deep-learning` | `deep-learning` | Deep Learning Engineering | Develop deep learning code with explicit tensor shapes, stable optimization, and reproducible evaluation. |
| `dl-checkpoint-resume` | `deep-learning` | Checkpoint and resume equivalence | Checkpoint and resume equivalence. |
| `dl-mixed-precision` | `deep-learning` | Mixed precision correctness | Mixed precision correctness. |
| `dl-gradient-accumulation` | `deep-learning` | Gradient accumulation | Gradient accumulation. |
| `dl-distributed-training` | `deep-learning` | Distributed training correctness | Distributed training correctness. |
| `dl-transfer-learning` | `deep-learning` | Transfer learning and freezing | Transfer learning and freezing. |

### GNCore UX and Design Systems (`design-ux`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `ux-research` | `design-ux` | UX Research | Plan and synthesize ethical user research that ties observations to product decisions. |
| `design-system` | `design-ux` | Design System Engineering | Extend a design system with accessible tokens and reusable components that fit existing conventions. |
| `design-ux-audit` | `design-ux` | UX Usability Audit | Audit a user flow for task clarity, feedback, recovery, cognitive load, and accessibility. |
| `design-user-flow` | `design-ux` | User Flow Design | Map a user journey with entry points, decisions, states, errors, and successful completion. |
| `design-wireframe` | `design-ux` | Wireframe Specification | Specify a wireframe around user priorities, information hierarchy, and responsive states. |
| `design-minimal` | `design-ux` | Minimalist UI Direction | Create a restrained interface with clear hierarchy, intentional whitespace, and accessible controls. |
| `design-expressive` | `design-ux` | Expressive UI Direction | Create a distinctive, layered interface without sacrificing navigation, readability, or accessibility. |
| `design-system-component` | `design-ux` | Design System Component | Specify a reusable design-system component with API, states, semantics, and adoption guidance. |
| `design-content` | `design-ux` | UX Content Design | Write interface text that helps users understand choices, status, errors, and recovery. |
| `design-prototype` | `design-ux` | Prototype Test Plan | Create a prototype test plan that resolves a specific interaction or comprehension question. |
| `design-accessibility` | `design-ux` | Accessible Interaction Design | Design keyboard, screen-reader, motion, contrast, and touch behavior into an interaction. |
| `design-handoff` | `design-ux` | Design to Engineering Handoff | Prepare a design handoff with behavior, states, assets, responsive rules, and unresolved questions. |

### GNCore Technical Research (`developer-research`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `research-synthesis` | `developer-research` | Research Synthesis | Synthesize supplied or sourced evidence with provenance, disagreement, and uncertainty kept visible. |
| `research-api-compatibility` | `developer-research` | API and dependency compatibility | API and dependency compatibility. |
| `research-paper-reproduction` | `developer-research` | Research result reproduction | Research result reproduction. |
| `research-technical-decision` | `developer-research` | Evidence-backed technical decision | Evidence-backed technical decision. |

### GNCore Developer Tools (`developer-tools`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `cli-design` | `developer-tools` | CLI Engineering | Design command-line tools with predictable arguments, clear errors, safe defaults, and scriptable output. |
| `tooling-reproducible-env` | `developer-tools` | Reproducible developer environments | Reproducible developer environments. |

### GNCore Distributed Systems (`distributed-systems`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `dist-idempotency` | `distributed-systems` | Idempotent operations | Idempotent operations. |
| `dist-queues` | `distributed-systems` | Queue delivery and recovery | Queue delivery and recovery. |
| `dist-consistency` | `distributed-systems` | Consistency and stale writers | Consistency and stale writers. |
| `dist-timeouts` | `distributed-systems` | Timeouts, backoff and retry budgets | Timeouts, backoff and retry budgets. |

### GNCore Documentation (`documentation`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `documentation-translation` | `documentation` | Technical Localization | Adapt technical content across languages while preserving product meaning, UI limits, and verified terminology. |
| `technical-writing` | `documentation` | Technical Writing | Write accurate, task-oriented technical documentation with runnable examples and clear prerequisites. |
| `documentation-api` | `documentation` | API Documentation | Document API behavior from the implementation and contract, with examples users can reproduce. |

### GNCore Embedded Systems (`embedded-systems`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `embedded-state-machine` | `embedded-systems` | Firmware state machines | Firmware state machines. |
| `embedded-protocols` | `embedded-systems` | Peripheral protocol integration | Peripheral protocol integration. |
| `embedded-timing` | `embedded-systems` | Timers and interrupt boundaries | Timers and interrupt boundaries. |
| `embedded-memory` | `embedded-systems` | Constrained memory and firmware builds | Constrained memory and firmware builds. |

### GNCore Game Development (`game-development`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `game-development` | `game-development` | Game Development | Implement game features with deterministic state transitions, responsive input, and measurable performance. |

### GNCore Machine Learning (`machine-learning`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `ml-problem-framing` | `machine-learning` | ML Problem Framing | Decide whether a machine learning approach fits the task, data, constraints, and failure costs. |
| `ml-dataset-audit` | `machine-learning` | ML Dataset Audit | Audit dataset provenance, schema, representativeness, label quality, leakage, and split strategy. |
| `ml-preprocessing-pipeline` | `machine-learning` | ML Preprocessing Pipeline | Build deterministic preprocessing that prevents leakage and preserves training-to-serving parity. |
| `ml-model-train` | `machine-learning` | ML Model Training Run | Implement a reproducible model training run with configuration, baseline, checkpoints, and evaluation. |
| `ml-model-evaluation` | `machine-learning` | ML Model Evaluation | Evaluate model quality, uncertainty, subgroup behavior, and representative errors against a baseline. |
| `ml-model-improvement` | `machine-learning` | ML Improvement Loop | Improve a model through controlled experiments with a fixed evaluation protocol and root-cause analysis. |
| `ml-llm-evaluation` | `machine-learning` | LLM Evaluation Suite | Evaluate an LLM feature with representative tasks, rubrics, adversarial cases, latency, and cost. |
| `ml-rag` | `machine-learning` | RAG Grounding Workflow | Build and evaluate retrieval-augmented answers with source access controls and abstention. |
| `ml-finetuning` | `machine-learning` | Model Fine-Tuning Plan | Assess fine-tuning suitability and prepare a controlled, leakage-safe fine-tuning workflow. |
| `ml-release-monitor` | `machine-learning` | Model Release and Monitoring | Prepare a model release with provenance, compatibility, rollback, and drift monitoring gates. |
| `machine-learning` | `machine-learning` | Machine Learning Workflow | Develop a scoped machine learning feature, from data inspection and baseline selection through evaluation. |
| `model-training` | `machine-learning` | Model Training | Set up or improve a reproducible model training run with clear configuration, checkpoints, and evaluation. |
| `train` | `machine-learning` | Train a Machine Learning Model | Build and run a reproducible model training workflow with a baseline, tracked configuration, and held-out evaluation. |
| `preprocess` | `machine-learning` | Preprocess Machine Learning Data | Design a repeatable preprocessing pipeline that preserves schema, prevents leakage, and records transformations. |
| `evaluate` | `machine-learning` | Evaluate a Model | Evaluate model quality with leakage-safe splits, task-appropriate metrics, baselines, and error analysis. |
| `improve` | `machine-learning` | Improve a Machine Learning Model | Find evidence-based model improvements through error analysis and controlled experiments against a fixed baseline. |
| `data-preparation` | `machine-learning` | ML Data Preparation | Prepare reproducible model datasets while preventing leakage and preserving provenance. |
| `feature-engineering` | `machine-learning` | Feature Engineering | Build features that are valid at prediction time and reproducible across training and inference. |
| `model-evaluation` | `machine-learning` | Model Evaluation | Evaluate model quality with valid splits, suitable metrics, uncertainty, and error analysis. |
| `feature-engineering-practice` | `machine-learning` | Feature Engineering Practice | Create leakage-safe, interpretable features that match the model's serving-time information. |
| `time-series` | `machine-learning` | Time-Series Modeling | Analyze and forecast time-indexed data with temporal splits, leakage controls, and useful uncertainty. |

### GNCore MLOps (`mlops`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `experiment-tracking` | `mlops` | Reproducible ML Experiments | Make model experiments traceable across code, data, configuration, environment, and artifacts. |
| `model-serving` | `mlops` | Model Serving and Inference APIs | Package model inference behind a reliable API with validation, resource limits, and observable behavior. |
| `mlops` | `mlops` | MLOps and Model Release | Package, register, and monitor models with reproducible artifacts and explicit release gates. |
| `ml-experiment-tracking` | `mlops` | Machine Learning Experiment Tracking | Make model experiments comparable with consistent splits, metrics, configuration, and artifact provenance. |
| `model-card` | `mlops` | Model Documentation | Document a model's intended use, data provenance, evaluation, limitations, and deployment assumptions. |
| `hardware-ml` | `mlops` | Edge and Hardware-Constrained ML | Adapt inference to constrained hardware using measured latency, memory, and accuracy tradeoffs. |
| `mlops-artifact-contract` | `mlops` | Model artifact and provenance | Model artifact and provenance. |
| `mlops-serving-contract` | `mlops` | Prediction service contract | Prediction service contract. |
| `mlops-drift-monitoring` | `mlops` | Drift and model monitoring | Drift and model monitoring. |
| `mlops-promotion-rollback` | `mlops` | Model promotion and rollback | Model promotion and rollback. |

### GNCore Mobile Development (`mobile-development`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `mobile-app` | `mobile-development` | Mobile App Engineering | Implement mobile features with reliable navigation, offline behavior, accessibility, and platform conventions. |

### GNCore NLP and Language Pipelines (`natural-language-processing`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `nlp` | `natural-language-processing` | Natural Language Processing | Build NLP pipelines that respect language, label quality, privacy, and task-specific evaluation. |
| `nlp-token-alignment` | `natural-language-processing` | Token and label alignment | Token and label alignment. |
| `nlp-text-classification` | `natural-language-processing` | Text classification baseline | Text classification baseline. |
| `nlp-sequence-modeling` | `natural-language-processing` | Sequence masks and generation | Sequence masks and generation. |
| `nlp-evaluation` | `natural-language-processing` | Language and task evaluation | Language and task evaluation. |

### GNCore Neural Networks (`neural-networks`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `nn-tensor-contracts` | `neural-networks` | Tensor and target contracts | Tensor and target contracts. |
| `nn-gradient-check` | `neural-networks` | Gradient verification | Gradient verification. |
| `nn-training-debug` | `neural-networks` | Diagnose a stalled training step | Diagnose a stalled training step. |
| `nn-loss-semantics` | `neural-networks` | Loss and activation semantics | Loss and activation semantics. |
| `nn-initialization` | `neural-networks` | Initialization and signal flow | Initialization and signal flow. |
| `nn-evaluation-modes` | `neural-networks` | Evaluation and validation isolation | Evaluation and validation isolation. |

### GNCore Observability (`observability`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `web-backend-sentry-instrument` | `observability` | GNCore Sentry Instrument | Instrument an application with Sentry — detect the platform, install and initialize the SDK if needed, and wire up any signal — error monitoring, tracing/performance, logging, metrics, profiling, session replay, user feedback, cron check-ins, uptime monitors for the deployed app, and AI/LLM monitoring (agent runs, token cost, and conversations for... |
| `web-backend-sentry-debug-issue` | `observability` | GNCore Sentry Debug Issue | Debug and fix a Sentry issue — find it (by link, ID, or search), pull full context (stack trace, breadcrumbs, trace, logs), optionally run Seer root-cause / autofix, apply the code fix, and resolve it via a `Fixes PROJECT-NAME-12A` commit/PR. |
| `web-backend-observability` | `observability` | GNCore Backend Observability | Design and verify useful service logs, traces, metrics, and alert signals with bounded overhead. |
| `obs-structured-events` | `observability` | Structured diagnostic events | Structured diagnostic events. |
| `obs-metrics-alerts` | `observability` | Metrics and actionable alerts | Metrics and actionable alerts. |
| `obs-trace-context` | `observability` | Trace propagation | Trace propagation. |
| `obs-incident-diagnosis` | `observability` | Evidence-led incident diagnosis | Evidence-led incident diagnosis. |

### GNCore Performance Engineering (`performance-engineering`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `python-performance` | `performance-engineering` | Python Performance | Profile Python hotspots and improve measured runtime or memory without changing semantics. |
| `perf-benchmark-design` | `performance-engineering` | Comparable benchmark design | Comparable benchmark design. |
| `perf-memory-profile` | `performance-engineering` | Memory and allocation diagnosis | Memory and allocation diagnosis. |
| `perf-tail-latency` | `performance-engineering` | Tail latency and saturation | Tail latency and saturation. |
| `perf-regression` | `performance-engineering` | Performance regression review | Performance regression review. |

### GNCore Python (`python`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `python-library` | `python` | Python Library Engineering | Design maintainable Python packages with stable APIs, typing, packaging, and clear examples. |
| `python-packaging` | `python` | Python Packaging | Package a Python library with clear APIs, reproducible builds, supported versions, and clean installation behavior. |
| `python-migration` | `python` | Python Upgrade and Migration | Migrate Python code or dependencies in a controlled way with compatibility evidence and a rollback path. |

### GNCore Release Engineering (`release-engineering`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `release-readiness` | `release-engineering` | Release Readiness Review | Check a release candidate against explicit acceptance, compatibility, security, rollback, and communication gates. |
| `release-artifact-integrity` | `release-engineering` | Artifact integrity and promotion | Artifact integrity and promotion. |

### GNCore Systems Programming (`systems-programming`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `systems-ownership` | `systems-programming` | Ownership and resource lifetime | Ownership and resource lifetime. |
| `systems-ffi` | `systems-programming` | FFI and ABI boundaries | FFI and ABI boundaries. |
| `systems-safe-arithmetic` | `systems-programming` | Integer and buffer boundaries | Integer and buffer boundaries. |
| `systems-concurrency` | `systems-programming` | Native concurrency | Native concurrency. |

### GNCore Testing (`testing`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `accessibility-audit` | `testing` | Accessibility Audit | Inspect a user flow for keyboard, screen reader, visual, and cognitive accessibility barriers. |
| `performance-audit` | `testing` | Performance Audit | Find and verify the largest performance bottlenecks before changing code or infrastructure. |
| `test-strategy` | `testing` | Test Strategy | Choose a balanced test plan that catches important failures at the lowest practical level. |
| `requirements-to-tests` | `testing` | Requirements to Acceptance Tests | Turn requirements into observable acceptance cases that cover success, failure, boundaries, and permissions. |
| `qa-test-strategy` | `testing` | Test Strategy | Choose a risk-based test mix that verifies behavior at the lowest effective level. |
| `qa-test-design` | `testing` | Test Case Design | Turn a behavior contract into clear positive, negative, boundary, and state-transition tests. |
| `qa-automation` | `testing` | Test Automation | Build maintainable test automation with stable setup, deterministic data, and actionable failures. |
| `qa-e2e` | `testing` | End-to-End User Journey Test | Verify a critical user journey across the application with realistic but isolated data. |
| `qa-api-contract` | `testing` | API Contract Testing | Check API compatibility, validation, authorization, and error contracts between services. |
| `qa-performance` | `testing` | Performance Test Plan | Measure a service against representative load, latency, throughput, and resource objectives. |
| `qa-accessibility` | `testing` | Accessibility Test Pass | Test a flow for keyboard operation, semantics, focus, labels, zoom, and assistive technology support. |
| `qa-defect-triage` | `testing` | Defect Triage | Classify and prioritize a defect using reproducibility, user impact, scope, and workaround evidence. |
| `qa-release-gate` | `testing` | Release Quality Gate | Evaluate release evidence against agreed quality gates and make residual risk visible. |
| `qa-flaky-test` | `testing` | Flaky Test Investigation | Find the cause of an intermittent test failure and confirm a stable correction. |
| `unit-testing` | `testing` | Unit Testing | Write fast, deterministic unit tests around public behavior and edge cases. |
| `integration-testing` | `testing` | Integration Testing | Verify interactions between real components while isolating external services and state. |
| `end-to-end-testing` | `testing` | End-to-End Testing | Validate critical user journeys across the running application with stable, accessible assertions. |
| `test-automation` | `testing` | Test Automation Engineering | Create maintainable CI test workflows with clear triggers, artifacts, and failure signals. |
| `performance-testing` | `testing` | Performance and Load Testing | Design controlled load tests that measure latency, throughput, and saturation safely. |

### GNCore Web Backend (`web-backend`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `web-backend-patterns` | `web-backend` | GNCore Patterns | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. |
| `web-backend-api-design` | `web-backend` | GNCore Api Design | REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs. |
| `web-backend-hexagonal-architecture` | `web-backend` | GNCore Hexagonal Architecture | Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, and testable use-case orchestration across TypeScript, Java, Kotlin, and Go services. |
| `web-backend-error-handling` | `web-backend` | GNCore Error Handling | Patterns for robust error handling across TypeScript, Python, and Go. |
| `web-backend-contract-first` | `web-backend` | GNCore Contract First | Coordinate frontend/backend or service-to-service work through one authoritative machine-checkable contract (OpenAPI, AsyncAPI, Protocol Buffers, or JSON Schema), with generated consumer types and contract-verified integration. |
| `web-backend-api-connector-builder` | `web-backend` | GNCore Api Connector Builder | Build a new API connector or provider by matching the target repo's existing integration pattern exactly. |
| `web-backend-spec-to-code-compliance` | `web-backend` | GNCore Spec To Code Compliance | Check code against the documentation that specifies it - which requirements hold, which the code contradicts, which are absent, and what the code does that no document mentions. |
| `web-backend-supabase-postgres-best-practices` | `web-backend` | GNCore Supabase Postgres Best Practices | Postgres best practices maintained by Supabase, for Postgres running anywhere. |
| `web-backend-postgres-patterns` | `web-backend` | GNCore Postgres Patterns | PostgreSQL database patterns for query optimization, schema design, indexing, and security. |
| `web-backend-database-migrations` | `web-backend` | GNCore Database Migrations | Safe, reversible database migration patterns: forward-only production changes, expand-contract zero-downtime renames, concurrent indexes, batched backfills, and per-tool workflows for PostgreSQL, Prisma, Drizzle, Kysely, Django, and golang-migrate. |
| `web-backend-benchmark` | `web-backend` | GNCore Benchmark | Measure performance baselines and detect regressions across browser Core Web Vitals (LCP, INP, CLS, page weight), API endpoint latency percentiles, and build/test feedback times, with before/after comparison stored in git-tracked .ecc/benchmarks JSON. |
| `web-backend-benchmark-optimization-loop` | `web-backend` | GNCore Benchmark Optimization Loop | Convert 'make it faster' requests into a bounded measured optimization loop — baseline first, generate one-hypothesis variants, benchmark each against a correctness gate, and promote the fastest safe variant with reproducible commands. |
| `web-backend-latency-critical-systems` | `web-backend` | GNCore Latency Critical Systems | Optimize and verify latency-sensitive systems — realtime dashboards, market data feeds, streaming agents, execution gateways, queues, and caches — by tracking p50/p95/p99 latency, freshness age, and queue depth, mapping hot paths, and running live readbacks. |
| `web-backend-redis-patterns` | `web-backend` | GNCore Redis Patterns | Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection management for production applications. |
| `web-backend-deployment-patterns` | `web-backend` | GNCore Deployment Patterns | Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, and production readiness checklists for web applications. |
| `web-backend-docker` | `web-backend` | GNCore Docker | Docker and Docker Compose patterns for local development, hardened CLI installer harnesses, container security, networking, volumes, and multi-service orchestration. |
| `web-backend-github-ops` | `web-backend` | GNCore Github Ops | GitHub repository operations, automation, and management. |
| `web-backend-production-audit` | `web-backend` | GNCore Production Audit | Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what breaks in prod?" questions without sending repo data to an external audit service. |
| `web-backend-agentic-engineering` | `web-backend` | GNCore Agentic Engineering | Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing. |
| `web-backend-mcp-server-patterns` | `web-backend` | GNCore Mcp Server Patterns | Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HTTP. |
| `web-backend-agent-eval` | `web-backend` | GNCore Agent Eval | Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate, cost, time, and consistency metrics. |
| `web-backend-cost-aware-llm-pipeline` | `web-backend` | GNCore Cost Aware Llm Pipeline | Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt caching. |
| `web-backend-mcp-builder` | `web-backend` | GNCore Mcp Builder | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. |
| `web-backend-agents-sdk` | `web-backend` | GNCore Agents Sdk | Build, debug, or review Cloudflare Agents SDK applications using the agents package. |
| `web-backend-building-ai-agent-on-cloudflare` | `web-backend` | GNCore Building Ai Agent On Cloudflare | Build a scoped AI agent on Cloudflare with explicit state, tool boundaries, bindings, and evaluation cases. |
| `web-backend-fastapi` | `web-backend` | GNCore Fastapi | Build FastAPI endpoints, Pydantic models, dependencies, and streaming responses using version-compatible APIs. |
| `web-backend-fastapi-patterns` | `web-backend` | GNCore Fastapi Patterns | FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, authentication, authorization, transactional service layers, and testing with httpx and pytest. |
| `web-backend-django` | `web-backend` | GNCore Django | Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and production-grade Django apps. |
| `web-backend-django-security` | `web-backend` | GNCore Django Security | Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS prevention, and secure deployment configurations. |
| `web-backend-django-tdd` | `web-backend` | GNCore Django Tdd | Django testing strategies with pytest-django, TDD methodology, factory_boy, mocking, coverage, and testing Django REST Framework APIs. |
| `web-backend-django-verification` | `web-backend` | GNCore Django Verification | Run the full Django verification loop — environment check, mypy/ruff/black linting, migration safety, pytest with coverage targets, pip-audit and bandit security scans, settings and logging review, and diff review — producing a phased pass/fail report before release or PR. |
| `web-backend-nestjs-patterns` | `web-backend` | GNCore Nestjs Patterns | NestJS architecture patterns for modules, controllers, providers, DTO validation, guards, interceptors, config, and production-grade TypeScript backends. |
| `web-backend-springboot-patterns` | `web-backend` | GNCore Springboot Patterns | Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, and logging. |
| `web-backend-springboot-security` | `web-backend` | GNCore Springboot Security | Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and dependency security in Java Spring Boot services. |
| `web-backend-springboot-tdd` | `web-backend` | GNCore Springboot Tdd | Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo. |
| `web-backend-springboot-verification` | `web-backend` | GNCore Springboot Verification | Run the full Spring Boot verification loop — Maven or Gradle build, SpotBugs, PMD, and Checkstyle static analysis, unit and Testcontainers integration tests with JaCoCo coverage, OWASP dependency and secret scans, and diff review — producing a pass/fail readiness report. |
| `web-backend-golang-patterns` | `web-backend` | GNCore Golang Patterns | Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go applications. |
| `web-backend-golang-testing` | `web-backend` | GNCore Golang Testing | Go testing patterns including table-driven tests, subtests, benchmarks, fuzzing, and test coverage. |
| `web-backend-laravel-patterns` | `web-backend` | GNCore Laravel Patterns | Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and API resources for production apps. |
| `web-backend-laravel-security` | `web-backend` | GNCore Laravel Security | Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API security, and secure deployment configurations. |
| `web-backend-laravel-tdd` | `web-backend` | GNCore Laravel Tdd | Laravel testing strategies with PHPUnit, Pest, model factories, HTTP tests, Sanctum authentication testing, mocking, and coverage. |
| `web-backend-laravel-verification` | `web-backend` | GNCore Laravel Verification | Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security scans, and deployment readiness. |
| `web-backend-supabase` | `web-backend` | GNCore Supabase | Implement or debug Supabase database, authentication, storage, and realtime features using current product documentation. |
| `web-backend-redis-core` | `web-backend` | GNCore Redis Core | Core Redis modeling guidance — choose the right data structure (String, Hash, List, Set, Sorted Set, JSON, Stream, Vector Set) and use consistent colon-separated key names. |
| `web-backend-redis-connections` | `web-backend` | GNCore Redis Connections | Redis client and connection guidance covering connection pooling, multiplexing, pipelining, client-side caching with RESP3, avoiding slow commands (KEYS, SMEMBERS, HGETALL), and tuning socket timeouts. |
| `web-backend-redis-security` | `web-backend` | GNCore Redis Security | Redis security guidance covering authentication (requirepass and ACL users), TLS, ACL-based least-privilege access control, restricting network exposure via bind and protected-mode, firewall rules, and disabling dangerous commands. |
| `web-backend-redis-observability` | `web-backend` | GNCore Redis Observability | Redis observability guidance — which metrics to monitor (memory, connections, hit ratio, ops/sec, rejected connections), which built-in commands to reach for during incident triage (SLOWLOG, INFO, MEMORY DOCTOR, CLIENT LIST, FT.PROFILE), and when to use the Redis Insight GUI. |
| `web-backend-redis-search` | `web-backend` | GNCore Redis Search | Redis Search guidance covering FT.CREATE schema design, field type selection (TEXT, TAG, NUMERIC, GEO, GEOSHAPE, VECTOR, JSON path), DIALECT 2 query syntax, FT.SEARCH / FT.AGGREGATE / FT.HYBRID command selection, vector similarity with HNSW or FLAT, hybrid retrieval combining lexical and vector ranking, RAG pipelines, zero-downtime index updates via... |
| `web-backend-redis-semantic-cache` | `web-backend` | GNCore Redis Semantic Cache | Redis LangCache guidance for semantic caching of LLM responses on Redis Cloud — calling search/set via the SDK or REST API, tuning the similarity threshold, separating caches per task type, and filtering with custom attributes. |
| `web-backend-vercel-optimize` | `web-backend` | GNCore Vercel Optimize | Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited Astro apps. |
| `web-backend-cloudflare` | `web-backend` | GNCore Cloudflare | Discover and choose Cloudflare products for apps, APIs, AI agents, storage, networking, and security. |
| `web-backend-workers-best-practices` | `web-backend` | GNCore Workers Best Practices | Cloudflare Workers best practices for production applications. |
| `web-backend-wrangler` | `web-backend` | GNCore Wrangler | Run or troubleshoot Wrangler CLI commands in projects that have a wrangler.jsonc, wrangler.json, or wrangler.toml file, including local development, Previews, deployment, and resource management. |
| `web-backend-durable-objects` | `web-backend` | GNCore Durable Objects | Build, debug, or review Cloudflare Durable Objects code for persistent state and coordination. |
| `web-backend-workers-profiling` | `web-backend` | GNCore Workers Profiling | Profile or debug CPU usage and memory allocation in deployed Cloudflare Workers and Durable Objects. |
| `web-backend` | `web-backend` | GNCore Backend Workflow | Route a backend task to the appropriate architecture, API, database, stack, security, or operations workflow. |
| `web-backend-codequality` | `web-backend` | GNCore Backend Code Quality | Improve backend correctness and maintainability across boundaries, data handling, concurrency, and error paths. |
| `web-backend-security` | `web-backend` | GNCore Backend Security | Review and repair backend authentication, object authorization, input handling, session, and secret boundaries. |
| `web-development` | `web-backend` | Web Development | Plan and implement a focused web feature using the repository's existing framework, patterns, and tests. |
| `seo-audit` | `web-backend` | SEO Audit | Improve technical and content discoverability using crawlable structure and verifiable search metadata. |

### GNCore Web Frontend (`web-frontend`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `web-front-design` | `web-frontend` | GNCore Design | Build or restyle a web interface with a deliberate visual identity and complete interaction states. |
| `web-front-ui-ux` | `web-frontend` | GNCore Ui Ux | Choose evidence-based UI patterns, palettes, typography, and layouts using a searchable local design library. |
| `web-front-react` | `web-frontend` | GNCore React | Improve React and Next.js rendering, data fetching, and bundle performance using measured bottlenecks. |
| `web-front-guidelines` | `web-frontend` | GNCore Guidelines | Review a web interface against current interface guidelines and report actionable file and line findings. |
| `web-front-shadcn` | `web-frontend` | GNCore Shadcn | Add and customize shadcn/ui components within an existing React application and theme. |
| `web-front-minimalism` | `web-frontend` | GNCore Minimalism | Create restrained web interfaces with clear hierarchy, deliberate whitespace, and essential controls. |
| `web-front-swiss` | `web-frontend` | GNCore Swiss | Build Swiss and International Style web layouts using typographic hierarchy and disciplined grids. |
| `web-front-editorial` | `web-frontend` | GNCore Editorial | Design magazine and editorial web experiences with strong reading rhythm, type, and image relationships. |
| `web-front-luxury` | `web-frontend` | GNCore Luxury | Create premium web experiences through typography, art direction, restrained detail, and polished interaction. |
| `web-front-agentic` | `web-frontend` | GNCore Agentic | Design AI task interfaces that expose progress, editable intent, results, and recovery controls. |
| `web-front-maximalism` | `web-frontend` | GNCore Maximalism | Build expressive maximalist web interfaces with rich layers and a readable visual hierarchy. |
| `web-front-taste` | `web-frontend` | GNCore Taste | Art-direct a distinctive frontend using researched compositions and iterative browser inspection. |
| `web-front-neobrutalism` | `web-frontend` | GNCore Neobrutalism | Create neo-brutalist web UI with bold borders, flat color, and direct, usable controls. |
| `web-front-industrial` | `web-frontend` | GNCore Industrial | Build industrial brutalist web interfaces with structural grids, utility typography, and exposed function. |
| `web-front-futuristic` | `web-frontend` | GNCore Futuristic | Create futuristic and Y2K-inspired interfaces with deliberate technical typography and spatial depth. |
| `web-front-retro` | `web-frontend` | GNCore Retro | Create nostalgic web interfaces with era-specific typography, palettes, and graphic treatments. |
| `web-front-collage` | `web-frontend` | GNCore Collage | Build paper and scrapbook web compositions with tactile layers and coherent reading order. |
| `web-front-doodle` | `web-frontend` | GNCore Doodle | Create playful hand-drawn web interfaces with readable type and controlled visual irregularity. |
| `web-front-bento` | `web-frontend` | GNCore Bento | Organize web content in a responsive bento grid with purposeful card sizes and hierarchy. |
| `web-front-glass` | `web-frontend` | GNCore Glass | Build glass and translucent web surfaces with readable contrast and affordable rendering costs. |
| `web-front-neumorphism` | `web-frontend` | GNCore Neumorphism | Create soft inset and raised web surfaces while keeping control states accessible. |
| `web-front-claymorphism` | `web-frontend` | GNCore Claymorphism | Create playful clay-like web surfaces with rounded geometry and tactile depth. |
| `web-front-aurora` | `web-frontend` | GNCore Aurora | Create aurora and gradient web treatments with controlled color transitions and readable content. |
| `web-front-cyberpunk` | `web-frontend` | GNCore Cyberpunk | Build neon and cyberpunk web interfaces with disciplined glow, dark surfaces, and clear interaction states. |
| `web-front-threejs` | `web-frontend` | GNCore Threejs | Implement immersive Three.js and WebGL web experiences with explicit asset and rendering budgets. |
| `web-front-r3f` | `web-frontend` | GNCore R3F | Build React Three Fiber scenes with clear React and render-loop ownership and proper cleanup. |
| `web-front-scrollytelling` | `web-frontend` | GNCore Scrollytelling | Build scroll-driven narratives with GSAP ScrollTrigger and resilient responsive behavior. |
| `web-front-kinetic-type` | `web-frontend` | GNCore Kinetic Type | Animate web typography with purposeful timing while preserving readable text and reduced-motion access. |
| `web-front-organic` | `web-frontend` | GNCore Organic | Create warm organic web interfaces using earth tones, natural rhythm, and tactile accents. |
| `web-front-design-system` | `web-frontend` | GNCore Design System | Define web design tokens, component contracts, and state specifications that fit an existing product. |
| `web-front-styling` | `web-frontend` | GNCore Styling | Style responsive web components using Tailwind, semantic tokens, and accessible primitives. |
| `web-front-composition` | `web-frontend` | GNCore Composition | Refactor React component APIs using composition, clear state ownership, and version-compatible context patterns. |
| `web-front-gsap` | `web-frontend` | GNCore Gsap | Implement GSAP tweens and responsive animation with explicit lifecycle and interruption handling. |
| `web-front-motion-performance` | `web-frontend` | GNCore Motion Performance | Profile and improve animation rendering cost without changing intended behavior. |
| `web-front-motion-review` | `web-frontend` | GNCore Motion Review | Review web animation timing, easing, continuity, and interaction feedback with actionable findings. |
| `web-front-testing` | `web-frontend` | GNCore Testing | Test important local web user journeys with Playwright and observable browser evidence. |
| `web-front-browser` | `web-frontend` | GNCore Browser | Inspect and exercise web interfaces through agent-browser snapshots, selectors, and screenshots. |
| `web-front-find-skills` | `web-frontend` | GNCore Find Skills | Find frontend skills and compare candidates by scope, source, compatibility, and license. |
| `web-front-accessibility` | `web-frontend` | GNCore Responsive Accessibility | Implement and verify responsive, keyboard-accessible web interfaces and assistive-technology semantics. |
| `web-front` | `web-frontend` | GNCore Frontend Workflow | Route a web frontend task to the relevant GNCore design, component, motion, or browser workflow. |

## Use

```bash
gncore export --specific web-frontend
gncore export --skills web-backend code-build
gncore export --all --output gncore-categories.zip
gncore plan "A premium hotel website, no animation"
```

See [Source Research](SOURCE_RESEARCH.md), [Ownership](OWNERSHIP.md), and [Migration](../MIGRATION.md) for provenance, licensing, and compatibility details.
