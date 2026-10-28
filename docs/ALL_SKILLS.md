# GNCore skill catalog

GNCore 6.0.0 contains **60 adaptive category skills**, preserving **553 workflows**. The **30 professional domains** each retain ten workflows in one category entrypoint.

Install a category under `.agents/skills/`, then describe the outcome to a compatible host AI. Its single entrypoint selects the relevant workflows; supporting references are loaded only when needed.

## Primary categories

| Category | Skill ID | Workflows | Use it for |
| --- | --- | --- | --- |
| `ai-engineering` | `ai-engineering` | 4 | Build and evaluate LLM applications, retrieval systems, prompts, and model-assisted user workflows. |
| `ai-machine-learning` | `ai-machine-learning` | 10 | Frame, train, evaluate, improve, and monitor machine-learning or LLM systems with leakage-safe evidence. |
| `analytics` | `analytics` | 1 | Define and evaluate product analytics, instrumentation, funnels, retention, and decision metrics. |
| `automation` | `automation` | 1 | Design and implement reliable automations with explicit inputs, state, retries, ownership, and recovery. |
| `backend-engineering` | `web-backend` | 61 | Build and improve backend services, APIs, persistence, integrations, AI systems, delivery, and observability in the selected stack. |
| `business-communications` | `business-communications` | 10 | Draft and edit executive briefs, emails, updates, policies, reports, crisis messages, and localized business content. |
| `business-operations` | `business-operations` | 10 | Improve operating processes, procedures, capacity, controls, quality, continuity, and automation. |
| `business-strategy` | `business-strategy` | 10 | Evaluate strategy, market entry, portfolios, pricing, scenarios, and business transformation. |
| `cloud` | `cloud` | 2 | Evaluate cloud architecture and cost choices against workload, reliability, security, and operational constraints. |
| `cloud-devops-sre` | `cloud-devops-sre` | 10 | Design and operate infrastructure, delivery pipelines, containers, Kubernetes, SLOs, observability, and capacity. |
| `code-engineering` | `code-build` | 66 | Build, investigate, review, test, refactor, and verify software across languages using task-appropriate workflows. |
| `company-leadership` | `company-leadership` | 10 | Prepare executive decisions, operating reviews, board materials, and cross-functional commitments. |
| `content` | `content` | 2 | Plan, adapt, translate, and maintain content around audience needs, factual accuracy, and channel constraints. |
| `customer-success-support` | `customer-success-support` | 10 | Triage customer issues and prepare responses, escalations, onboarding, health reviews, and renewals. |
| `cybersecurity` | `cybersecurity` | 10 | Assess threats, code risks, vulnerabilities, incidents, identity, cloud controls, and security validation plans. |
| `data` | `data` | 2 | Inspect, transform, analyze, and move data through reproducible pipelines with explicit contracts. |
| `data-analytics` | `data-analytics` | 10 | Answer business questions with reproducible data audits, SQL, metrics, cohorts, experiments, forecasts, and dashboards. |
| `data-engineering` | `data-engineering` | 3 | Design databases, data pipelines, and governance with explicit schemas, ownership, lineage, and quality controls. |
| `data-science` | `data-science` | 7 | Clean and analyze data with reproducible SQL, statistics, experiments, visualizations, and spatial methods. |
| `design` | `design` | 2 | Conduct UX research and build design systems around real tasks, semantic tokens, components, and accessible interaction. |
| `design-ux` | `design-ux` | 10 | Design and evaluate user flows, wireframes, visual systems, content, prototypes, accessibility, and handoffs. |
| `developer-tools` | `developer-tools` | 1 | Design and improve command-line interfaces with predictable commands, output, exit codes, and safe file behavior. |
| `devops` | `devops` | 2 | Improve delivery workflows and Kubernetes operations with reproducible configuration, observability, and recovery. |
| `documentation` | `documentation` | 2 | Write and maintain technical and API documentation from verified behavior, examples, and audience needs. |
| `ecommerce-retail` | `ecommerce-retail` | 10 | Improve retail catalogs, merchandising, conversion, pricing, inventory, campaigns, reviews, returns, and store operations. |
| `education` | `education` | 1 | Create accurate, accessible learning content with clear objectives, examples, practice, and feedback. |
| `education-learning` | `education-learning` | 10 | Design objectives, lessons, curricula, assessments, study materials, tutoring, and accessible learning experiences. |
| `entrepreneurship` | `entrepreneurship` | 10 | Evaluate venture ideas, customer evidence, MVP scope, business models, runway, fundraising, and go-to-market choices. |
| `finance-accounting` | `finance-accounting` | 10 | Prepare financial models, reconciliations, budgets, forecasts, close support, and variance explanations. |
| `game-development` | `game-development` | 1 | Build and improve game mechanics, interactions, state, assets, and performance in the existing engine. |
| `general` | `general` | 8 | Clarify, plan, implement, review, document, or prepare a scoped project outcome. |
| `healthcare-operations` | `healthcare-operations` | 10 | Support healthcare intake, scheduling, quality, capacity, privacy, policies, audits, and administrative improvement. |
| `legal-compliance` | `legal-compliance` | 10 | Organize legal intake, contract obligations, compliance evidence, policy gaps, and review materials. |
| `machine-learning` | `machine-learning` | 23 | Develop reproducible machine-learning workflows from data preparation and training to evaluation, optimization, and serving. |
| `marketing-growth` | `marketing-growth` | 10 | Plan and evaluate positioning, brand, campaigns, content, acquisition, lifecycle, and marketing investment. |
| `mobile-development` | `mobile-development` | 1 | Build mobile application flows with platform-appropriate navigation, state, permissions, accessibility, and lifecycle handling. |
| `operations` | `operations` | 1 | Investigate operational incidents and coordinate containment, recovery, communication, and follow-up from evidence. |
| `pdf-documents` | `pdf-documents` | 10 | Extract, create, combine, split, OCR, fill, review, and verify PDF documents and redactions. |
| `people-human-resources` | `people-human-resources` | 10 | Support role design, hiring, onboarding, development, performance, workforce planning, and employee policies. |
| `presentations-powerpoint` | `presentations-powerpoint` | 10 | Create and refine presentations with a clear storyline, visual hierarchy, accurate charts, and verified layouts. |
| `procurement-vendor` | `procurement-vendor` | 10 | Prepare sourcing requirements, RFPs, vendor comparisons, due diligence, negotiations, and vendor lifecycle plans. |
| `product` | `product` | 1 | Investigate user problems and validate product opportunities before committing to a solution. |
| `product-management` | `product-management` | 10 | Discover product opportunities and turn them into requirements, experiments, roadmaps, and launch decisions. |
| `professional-services` | `professional-services` | 2 | Prepare contract-review and financial-analysis support with traceable sources, assumptions, and review boundaries. |
| `project-program-management` | `project-program-management` | 10 | Plan, coordinate, recover, and close projects with explicit dependencies, capacity, and decisions. |
| `python` | `python` | 4 | Build, profile, package, and migrate Python libraries while preserving public APIs and supported runtimes. |
| `quality-assurance` | `quality-assurance` | 4 | Audit accessibility and performance, plan tests, and connect requirements to verifiable acceptance evidence. |
| `quality-engineering` | `quality-engineering` | 10 | Design risk-based test strategies, automation, end-to-end and contract checks, and release evidence. |
| `release-engineering` | `release-engineering` | 1 | Prepare a software release with consistent versions, tested artifacts, migration notes, and a reviewable delivery plan. |
| `research` | `research` | 1 | Synthesize evidence into a clear answer with source provenance, uncertainty, and decision-relevant conclusions. |
| `research-market-intelligence` | `research-market-intelligence` | 10 | Investigate markets, competitors, customers, literature, surveys, and evidence with traceable sources. |
| `sales-revenue` | `sales-revenue` | 10 | Research accounts, qualify opportunities, prepare sales conversations, proposals, forecasts, and renewals. |
| `security` | `security` | 2 | Review web security and privacy boundaries using concrete code paths, data flows, and source-backed requirements. |
| `software-engineering` | `software-engineering` | 10 | Design, implement, debug, review, refactor, migrate, and release scoped software changes. |
| `spreadsheets` | `spreadsheets` | 10 | Build, audit, clean, analyze, visualize, forecast, and automate spreadsheets with correct formulas and readable models. |
| `supply-chain-logistics` | `supply-chain-logistics` | 10 | Plan demand, sourcing, suppliers, inventory, warehouses, transport, resilience, and supply-chain performance. |
| `testing` | `testing` | 5 | Design and run unit, integration, end-to-end, automation, and performance tests for important software behavior. |
| `web-development` | `web-development` | 2 | Build scoped web features and improve technical SEO using the repository's existing frontend and backend stack. |
| `web-frontend` | `web-frontend` | 40 | Build or redesign a complete web interface, automatically choosing an appropriate visual direction unless the user specifies one. |
| `word-documents` | `word-documents` | 10 | Create, edit, format, review, and prepare accessible Word documents, reports, templates, forms, and redlines. |

## Professional domains

| Domain | Primary skill | Retained workflows |
| --- | --- | --- |
| Company Leadership | `company-leadership` | 10 |
| Business Strategy | `business-strategy` | 10 |
| Product Management | `product-management` | 10 |
| Project and Program Management | `project-program-management` | 10 |
| Business Operations | `business-operations` | 10 |
| Sales and Revenue | `sales-revenue` | 10 |
| Marketing and Growth | `marketing-growth` | 10 |
| Finance and Accounting | `finance-accounting` | 10 |
| People and Human Resources | `people-human-resources` | 10 |
| Customer Success and Support | `customer-success-support` | 10 |
| Legal and Compliance Support | `legal-compliance` | 10 |
| Procurement and Vendor Management | `procurement-vendor` | 10 |
| Entrepreneurship and New Ventures | `entrepreneurship` | 10 |
| Software Engineering | `software-engineering` | 10 |
| Data Analytics and Intelligence | `data-analytics` | 10 |
| AI and Machine Learning | `ai-machine-learning` | 10 |
| Cybersecurity | `cybersecurity` | 10 |
| Cloud, DevOps, and SRE | `cloud-devops-sre` | 10 |
| Quality Engineering and Testing | `quality-engineering` | 10 |
| Design, UX, and Accessibility | `design-ux` | 10 |
| Microsoft Word and DOCX Documents | `word-documents` | 10 |
| PDF Documents | `pdf-documents` | 10 |
| Presentations and PowerPoint | `presentations-powerpoint` | 10 |
| Spreadsheets and Excel | `spreadsheets` | 10 |
| Research and Market Intelligence | `research-market-intelligence` | 10 |
| Education and Learning | `education-learning` | 10 |
| Healthcare Operations | `healthcare-operations` | 10 |
| E-commerce and Retail | `ecommerce-retail` | 10 |
| Business Communications | `business-communications` | 10 |
| Supply Chain and Logistics | `supply-chain-logistics` | 10 |

## Complete workflow map

These IDs remain CLI/API compatibility aliases. Exporting aliases from one category produces one merged category folder. Primary category names take precedence over older generic names when they collide.

### GNCore Ai Engineering (`ai-engineering`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `llm-evaluation` | `ai-engineering` | Evaluate an LLM Workflow | Measure an LLM feature with representative cases, explicit rubrics, failure analysis, and repeatable comparisons. |
| `llm-app` | `ai-engineering` | LLM Application Engineering | Implement reliable LLM features with structured outputs, bounded tools, privacy, and graceful failure handling. |
| `rag` | `ai-engineering` | Retrieval-Augmented Generation | Build a grounded retrieval workflow with traceable sources, chunking tests, and abstention on missing evidence. |
| `prompt-engineering` | `ai-engineering` | Prompt Engineering | Improve prompts against explicit tasks and evaluations while preserving tool and safety boundaries. |

### GNCore AI and Machine Learning (`ai-machine-learning`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `ml-problem-framing` | `ai-machine-learning` | ML Problem Framing | Decide whether a machine learning approach fits the task, data, constraints, and failure costs. |
| `ml-dataset-audit` | `ai-machine-learning` | ML Dataset Audit | Audit dataset provenance, schema, representativeness, label quality, leakage, and split strategy. |
| `ml-preprocessing-pipeline` | `ai-machine-learning` | ML Preprocessing Pipeline | Build deterministic preprocessing that prevents leakage and preserves training-to-serving parity. |
| `ml-model-train` | `ai-machine-learning` | ML Model Training Run | Implement a reproducible model training run with configuration, baseline, checkpoints, and evaluation. |
| `ml-model-evaluation` | `ai-machine-learning` | ML Model Evaluation | Evaluate model quality, uncertainty, subgroup behavior, and representative errors against a baseline. |
| `ml-model-improvement` | `ai-machine-learning` | ML Improvement Loop | Improve a model through controlled experiments with a fixed evaluation protocol and root-cause analysis. |
| `ml-llm-evaluation` | `ai-machine-learning` | LLM Evaluation Suite | Evaluate an LLM feature with representative tasks, rubrics, adversarial cases, latency, and cost. |
| `ml-rag` | `ai-machine-learning` | RAG Grounding Workflow | Build and evaluate retrieval-augmented answers with source access controls and abstention. |
| `ml-finetuning` | `ai-machine-learning` | Model Fine-Tuning Plan | Assess fine-tuning suitability and prepare a controlled, leakage-safe fine-tuning workflow. |
| `ml-release-monitor` | `ai-machine-learning` | Model Release and Monitoring | Prepare a model release with provenance, compatibility, rollback, and drift monitoring gates. |

### GNCore Analytics (`analytics`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `product-analytics` | `analytics` | Product Analytics | Define product metrics and event instrumentation that answer a decision without collecting unnecessary data. |

### GNCore Automation (`automation`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `workflow-automation` | `automation` | Workflow Automation | Automate a repetitive workflow with bounded inputs, safe retries, idempotency, and clear human checkpoints. |

### GNCore Backend Engineering (`web-backend`)

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
| `web-backend-sentry-instrument` | `web-backend` | GNCore Sentry Instrument | Instrument an application with Sentry — detect the platform, install and initialize the SDK if needed, and wire up any signal — error monitoring, tracing/performance, logging, metrics, profiling, session replay, user feedback, cron check-ins, uptime monitors for the deployed app, and AI/LLM monitoring (agent runs, token cost, and conversations for... |
| `web-backend-sentry-debug-issue` | `web-backend` | GNCore Sentry Debug Issue | Debug and fix a Sentry issue — find it (by link, ID, or search), pull full context (stack trace, breadcrumbs, trace, logs), optionally run Seer root-cause / autofix, apply the code fix, and resolve it via a `Fixes PROJECT-NAME-12A` commit/PR. |
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
| `web-backend-observability` | `web-backend` | GNCore Backend Observability | Design and verify useful service logs, traces, metrics, and alert signals with bounded overhead. |

### GNCore Business Communications (`business-communications`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `comms-executive-brief` | `business-communications` | Executive Brief | Create a concise decision brief with evidence, options, owner, and timing. |
| `comms-email` | `business-communications` | Business Email | Draft audience-appropriate business email with a clear next action. |
| `comms-stakeholder-update` | `business-communications` | Stakeholder Update | Report status, changes, blockers, decisions, and next steps. |
| `comms-policy` | `business-communications` | Internal Policy Draft | Draft policy with scope, rules, owner, exceptions, and review cadence. |
| `comms-report` | `business-communications` | Business Report | Connect evidence to conclusions and actions in a structured report. |
| `comms-crisis` | `business-communications` | Crisis Communications | Prepare a factual holding statement and update plan for an incident. |
| `comms-edit` | `business-communications` | Clarity and Tone Edit | Edit writing for clarity, audience fit, accuracy, and consistent tone. |
| `comms-meeting` | `business-communications` | Meeting Brief and Minutes | Prepare agendas and decision-focused minutes with owners and follow-ups. |
| `comms-localization` | `business-communications` | Business Content Localization | Adapt content to a locale while preserving meaning, policy, and usability. |
| `comms-quality` | `business-communications` | Communications Quality Check | Quality-check business communications before distribution. |

### GNCore Business Operations (`business-operations`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `operations-process-map` | `business-operations` | Process Mapping | Map a business process from trigger to outcome and expose waste and control gaps. |
| `operations-sop` | `business-operations` | Standard Operating Procedure | Write an actionable SOP with prerequisites, steps, decision points, and recovery paths. |
| `operations-kpi` | `business-operations` | Operations KPI Review | Analyze operational KPIs against service outcomes, baselines, and capacity limits. |
| `operations-quality` | `business-operations` | Service Quality Improvement | Reduce recurring service defects through root-cause analysis and controlled countermeasures. |
| `operations-capacity` | `business-operations` | Capacity and Queue Planning | Forecast service capacity and queues with explicit demand, throughput, and uncertainty. |
| `operations-control` | `business-operations` | Operational Control Design | Design practical controls that prevent or detect costly process failures. |
| `operations-incident` | `business-operations` | Business Operations Incident | Coordinate a non-technical operational incident and restore service with clear ownership. |
| `operations-vendor` | `business-operations` | Vendor Operations Review | Review vendor delivery against service commitments, risks, dependencies, and corrective actions. |
| `operations-continuity` | `business-operations` | Business Continuity Plan | Prepare a business continuity response for essential processes and credible disruption scenarios. |
| `operations-automation` | `business-operations` | Operations Automation Case | Assess whether an operational task is ready for safe automation and quantify its value. |

### GNCore Business Strategy (`business-strategy`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `strategy-market-entry` | `business-strategy` | Market Entry Strategy | Evaluate entry into a new market using evidence, economics, and staged commitments. |
| `strategy-portfolio` | `business-strategy` | Portfolio Prioritization | Rank business initiatives by strategic value, evidence, capacity, and opportunity cost. |
| `strategy-competitive` | `business-strategy` | Competitive Analysis | Compare competitors using verifiable evidence and decision-relevant positioning. |
| `strategy-business-model` | `business-strategy` | Business Model Review | Map a business model and test whether its value creation and capture are sustainable. |
| `strategy-scenario` | `business-strategy` | Strategic Scenario Planning | Build plausible scenarios and decision triggers for uncertain business conditions. |
| `strategy-okrs` | `business-strategy` | Strategy to OKRs | Translate strategic intent into measurable outcomes and aligned quarterly objectives. |
| `strategy-pricing` | `business-strategy` | Pricing Strategy | Analyze pricing architecture, willingness-to-pay evidence, and margin consequences. |
| `strategy-risk` | `business-strategy` | Enterprise Risk Assessment | Prioritize strategic risks by likelihood, impact, exposure, and mitigation evidence. |
| `strategy-ma` | `business-strategy` | M&A Opportunity Screen | Screen an acquisition or partnership opportunity against strategic and financial criteria. |
| `strategy-transformation` | `business-strategy` | Business Transformation Plan | Design a staged transformation with outcomes, governance, adoption, and measurable benefits. |

### GNCore Cloud (`cloud`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `cloud-architecture` | `cloud` | Cloud Architecture | Design a cloud deployment around explicit reliability, security, operations, and cost constraints. |
| `cost-optimization` | `cloud` | Cloud Cost Optimization | Find measurable cloud cost reductions while protecting reliability and workload correctness. |

### GNCore Cloud, DevOps, and SRE (`cloud-devops-sre`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
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

### GNCore Code Engineering (`code-build`)

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

### GNCore Company Leadership (`company-leadership`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `company-ceo` | `company-leadership` | CEO Decision Brief | Prepare an evidence-led CEO brief for a company-level decision. |
| `company-cfo` | `company-leadership` | CFO Review | Review financial performance, liquidity, and capital choices for executive decisions. |
| `company-coo` | `company-leadership` | COO Operating Review | Diagnose operational performance and turn bottlenecks into accountable actions. |
| `company-cto` | `company-leadership` | CTO Technology Review | Assess technology direction, engineering execution, and technical risk for leadership. |
| `company-cpo` | `company-leadership` | Chief Product Officer Review | Align product portfolio decisions with customer evidence and company outcomes. |
| `company-cmo` | `company-leadership` | Chief Marketing Officer Review | Evaluate marketing strategy, brand health, and growth investment for executives. |
| `company-chro` | `company-leadership` | Chief People Officer Review | Review workforce health, organization design, and talent risks with appropriate privacy. |
| `company-ciso` | `company-leadership` | Chief Information Security Officer Review | Brief executives on cyber risk, exposure, and risk-reduction decisions. |
| `company-board` | `company-leadership` | Board Materials Review | Prepare or review board-level materials for clarity, governance, and decision quality. |
| `company-executive-team` | `company-leadership` | Executive Team Alignment | Resolve cross-functional decisions into shared priorities, owners, and measurable commitments. |

### GNCore Content (`content`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `content-strategy` | `content` | Content Strategy | Plan clear, consistent content around a specific audience, task, evidence, and publishing goal. |
| `documentation-translation` | `content` | Technical Localization | Adapt technical content across languages while preserving product meaning, UI limits, and verified terminology. |

### GNCore Customer Success and Support (`customer-success-support`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `customer-onboarding` | `customer-success-support` | Customer Onboarding Plan | Guide a customer to a defined first outcome with owners, milestones, and adoption signals. |
| `customer-support-triage` | `customer-success-support` | Support Case Triage | Classify a support issue by impact, urgency, reproducibility, and routing evidence. |
| `customer-reply` | `customer-success-support` | Customer Support Reply | Draft a clear customer reply that addresses the issue, next action, and known limits. |
| `customer-escalation` | `customer-success-support` | Customer Escalation Brief | Prepare an escalation brief with impact, timeline, evidence, owner, and decision request. |
| `customer-health` | `customer-success-support` | Customer Health Review | Assess customer health from transparent adoption, outcome, relationship, and support signals. |
| `customer-renewal` | `customer-success-support` | Customer Renewal Risk | Build a renewal action plan grounded in value realization, stakeholder needs, and contract facts. |
| `customer-knowledge` | `customer-success-support` | Support Knowledge Article | Write a tested support article that resolves a common issue with clear prerequisites and recovery. |
| `customer-voice` | `customer-success-support` | Voice of Customer Synthesis | Combine customer evidence into actionable themes with source coverage and counterexamples. |
| `customer-service-recovery` | `customer-success-support` | Service Recovery Plan | Restore trust after a service failure through verified facts, ownership, and follow-through. |
| `customer-success-qbr` | `customer-success-support` | Customer Business Review | Prepare a customer review that connects usage, outcomes, open risks, and next-period goals. |

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

### GNCore Data (`data`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `data-analysis` | `data` | Data Analysis | Answer data questions with reproducible calculations, clear definitions, and honest uncertainty. |
| `data-pipelines` | `data` | Data Pipeline Engineering | Build reliable, observable data pipelines with explicit schemas, retries, and idempotency. |

### GNCore Data Analytics and Intelligence (`data-analytics`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `analytics-question` | `data-analytics` | Analytics Question Plan | Translate a business question into a measurable analysis plan and data requirements. |
| `analytics-data-audit` | `data-analytics` | Data Quality Audit | Audit analytical data for missingness, duplication, validity, freshness, and grain. |
| `analytics-sql` | `data-analytics` | Business SQL Analysis | Write a traceable SQL analysis with correct grain, joins, time handling, and reconciliation. |
| `analytics-dashboard` | `data-analytics` | Decision Dashboard | Design a dashboard around a recurring decision with clear metrics, filters, and data freshness. |
| `analytics-metric-tree` | `data-analytics` | Metric Tree | Decompose a business outcome into leading drivers and measurable operational inputs. |
| `analytics-cohort` | `data-analytics` | Cohort Analysis | Compare cohort behavior with consistent definitions, exposure windows, and censoring treatment. |
| `analytics-experiment` | `data-analytics` | Business Experiment Analysis | Analyze an experiment with assignment, exposure, predeclared outcomes, and uncertainty checks. |
| `analytics-forecast` | `data-analytics` | Business Forecast Analysis | Build a business forecast from history, drivers, scenarios, and out-of-sample checks. |
| `analytics-insight-brief` | `data-analytics` | Executive Analytics Brief | Turn analysis into a concise decision brief with traceable evidence and caveats. |
| `analytics-data-contract` | `data-analytics` | Analytics Data Contract | Specify ownership, schema, quality, freshness, and change handling for an analytics dataset. |

### GNCore Data Engineering (`data-engineering`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `database-design` | `data-engineering` | Database Design | Design safe relational data models, queries, and migrations that preserve integrity and performance. |
| `data-pipeline` | `data-engineering` | Data Pipeline Engineering | Build observable, restartable pipelines with explicit schemas, idempotency, and data-quality checks. |
| `data-governance` | `data-engineering` | Data Governance | Define practical ownership, quality, access, lineage, and retention controls for a data asset. |

### GNCore Data Science (`data-science`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `clean-data` | `data-science` | Clean a Dataset | Audit and clean a dataset with explicit, reversible rules for missing values, duplicates, types, and outliers. |
| `analyze` | `data-science` | Analyze Data | Answer a data question with reproducible analysis, explicit assumptions, and evidence tied to the provided data. |
| `sql-analysis` | `data-science` | SQL Analysis | Write correct, reviewable SQL for analytics while guarding against join fanout and misleading aggregates. |
| `data-visualization` | `data-science` | Data Visualization | Create clear charts that faithfully represent the underlying data and its uncertainty. |
| `statistics` | `data-science` | Statistical Analysis | Choose and interpret statistical methods with assumptions, uncertainty, and practical effects stated clearly. |
| `ab-testing` | `data-science` | A/B Test Analysis | Analyze controlled experiments with valid assignment checks, predeclared metrics, and practical uncertainty. |
| `geospatial-analysis` | `data-science` | Geospatial Analysis | Analyze spatial data with explicit coordinate systems, units, geometry validity, and privacy controls. |

### GNCore Design (`design`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `ux-research` | `design` | UX Research | Plan and synthesize ethical user research that ties observations to product decisions. |
| `design-system` | `design` | Design System Engineering | Extend a design system with accessible tokens and reusable components that fit existing conventions. |

### GNCore Design, UX, and Accessibility (`design-ux`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
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

### GNCore Developer Tools (`developer-tools`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `cli-design` | `developer-tools` | CLI Engineering | Design command-line tools with predictable arguments, clear errors, safe defaults, and scriptable output. |

### GNCore Devops (`devops`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `devops` | `devops` | DevOps Engineering | Improve build and delivery workflows with reproducible steps, safe rollout, and actionable failure signals. |
| `kubernetes` | `devops` | Kubernetes Engineering | Author Kubernetes resources with least privilege, clear health behavior, and safe rollout settings. |

### GNCore Documentation (`documentation`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `technical-writing` | `documentation` | Technical Writing | Write accurate, task-oriented technical documentation with runnable examples and clear prerequisites. |
| `documentation-api` | `documentation` | API Documentation | Document API behavior from the implementation and contract, with examples users can reproduce. |

### GNCore E-commerce and Retail (`ecommerce-retail`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `retail-catalog` | `ecommerce-retail` | Product Catalog Quality | Improve product data completeness, consistency, and variant accuracy. |
| `retail-merchandising` | `ecommerce-retail` | Retail Merchandising | Align merchandising with customer intent, stock, margin, and brand. |
| `retail-conversion` | `ecommerce-retail` | Conversion Review | Diagnose page and checkout friction with evidence and prioritized experiments. |
| `retail-pricing` | `ecommerce-retail` | Retail Pricing Analysis | Analyze prices, discounts, and margin with traceable sources. |
| `retail-inventory` | `ecommerce-retail` | Retail Inventory Operations | Review inventory signals and replenishment exceptions. |
| `retail-campaign` | `ecommerce-retail` | Retail Campaign Planning | Plan campaigns with stock, audience, creative, and measurement aligned. |
| `retail-reviews` | `ecommerce-retail` | Customer Review Synthesis | Summarize reviews without fabricating or overstating customer evidence. |
| `retail-returns` | `ecommerce-retail` | Returns and Refund Analysis | Find return patterns while preserving policy and customer fairness. |
| `retail-store-ops` | `ecommerce-retail` | Store Operations Playbook | Create store procedures with role ownership, safety checks, and escalation. |
| `retail-qa` | `ecommerce-retail` | Commerce Experience QA | Test product, cart, checkout, device, and accessibility journeys. |

### GNCore Education (`education`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `education-content` | `education` | Learning Content Design | Create learning materials with measurable outcomes, sequenced practice, accessible examples, and answer checks. |

### GNCore Education and Learning (`education-learning`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `education-learning-objectives` | `education-learning` | Learning Objectives | Write measurable learning objectives aligned with learner needs, prerequisites, practice, and assessment. |
| `education-lesson` | `education-learning` | Lesson Plan | Plan a lesson with sequenced explanation, active practice, feedback, and accessible timing. |
| `education-curriculum` | `education-learning` | Curriculum Map | Organize a curriculum into coherent progression, prerequisite links, practice, and assessment. |
| `education-assessment` | `education-learning` | Assessment Design | Create an assessment aligned to learning outcomes with clear instructions and fair scoring. |
| `education-rubric` | `education-learning` | Scoring Rubric | Develop a behavior-anchored rubric that supports consistent feedback and grading. |
| `education-study-guide` | `education-learning` | Study Guide | Create a focused study guide with key concepts, retrieval practice, examples, and self-check answers. |
| `education-tutor` | `education-learning` | Tutoring Session | Tutor a learner by diagnosing understanding, guiding practice, and adapting explanations. |
| `education-content-accessibility` | `education-learning` | Accessible Learning Material | Adapt learning content for accessible navigation, language, formats, and participation. |
| `education-feedback` | `education-learning` | Learner Feedback Synthesis | Synthesize learner feedback into evidence-based course improvements while protecting privacy. |
| `education-course-review` | `education-learning` | Course Quality Review | Review a course for alignment among objectives, instruction, practice, assessment, workload, and accessibility. |

### GNCore Entrepreneurship and New Ventures (`entrepreneurship`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `venture-idea` | `entrepreneurship` | Venture Idea Screen | Screen a venture idea by customer problem, alternatives, evidence, and founder constraints. |
| `venture-customer-interview` | `entrepreneurship` | Customer Interview Guide | Prepare non-leading interviews that test customer behavior and unmet needs. |
| `venture-mvp` | `entrepreneurship` | Minimum Viable Product Scope | Choose the smallest product experiment that can test a critical venture assumption. |
| `venture-business-model` | `entrepreneurship` | Venture Business Model | Map the venture's customer, value, channel, cost, revenue, and operating assumptions. |
| `venture-business-plan` | `entrepreneurship` | Business Plan Draft | Create a decision-focused business plan with evidence, assumptions, execution, and capital needs. |
| `venture-fundraise` | `entrepreneurship` | Fundraising Preparation | Organize fundraising narrative, evidence, materials, and diligence readiness. |
| `venture-runway` | `entrepreneurship` | Founder Runway Scenarios | Model startup runway and options under base, downside, and financing scenarios. |
| `venture-go-to-market` | `entrepreneurship` | Early Go-to-Market Test | Design a low-cost channel test for an early product with a measurable learning objective. |
| `venture-founder-agreement` | `entrepreneurship` | Founder Alignment Checklist | Surface founder-role, decision, equity, vesting, and conflict questions for professional review. |
| `venture-pivot-review` | `entrepreneurship` | Pivot or Persevere Review | Decide whether to continue, adjust, or stop a venture hypothesis from observed evidence. |

### GNCore Finance and Accounting (`finance-accounting`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `finance-budget` | `finance-accounting` | Budget Build | Build a traceable budget from operational drivers, assumptions, owners, and approved targets. |
| `finance-forecast` | `finance-accounting` | Rolling Forecast | Update a rolling forecast from actuals and current business drivers without hiding variance. |
| `finance-variance` | `finance-accounting` | Financial Variance Analysis | Explain financial variance by volume, price, mix, timing, and one-time effects. |
| `finance-cashflow` | `finance-accounting` | Cash Flow and Runway | Model cash needs and runway using explicit receipts, obligations, and timing scenarios. |
| `finance-unit-economics` | `finance-accounting` | Unit Economics | Calculate unit economics with consistent cohort, cost allocation, and contribution assumptions. |
| `finance-month-close` | `finance-accounting` | Month-End Close Checklist | Coordinate a complete month-end close with reconciliations, owners, evidence, and review. |
| `finance-controls` | `finance-accounting` | Financial Controls Review | Review financial process controls for authorization, reconciliation, evidence, and segregation. |
| `finance-investment-case` | `finance-accounting` | Investment Business Case | Build a decision-ready capital request with costs, benefits, alternatives, and sensitivity. |
| `finance-expense` | `finance-accounting` | Expense Policy Review | Assess expense submissions against supplied policy with consistent evidence and escalation. |
| `finance-report` | `finance-accounting` | Financial Report Review | Review a financial report for arithmetic, consistency, labels, source traceability, and decision clarity. |

### GNCore Game Development (`game-development`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `game-development` | `game-development` | Game Development | Implement game features with deterministic state transitions, responsive input, and measurable performance. |

### GNCore General (`general`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `requirements` | `general` | Requirements Clarifier | Collects scope, constraints, acceptance criteria, and open questions before implementation starts. |
| `architecture` | `general` | Architecture Designer | Defines system boundaries, interfaces, and implementation constraints. |
| `implementation` | `general` | Implementation Builder | Writes production-grade code with minimal duplication and explicit types. |
| `review` | `general` | Code Reviewer | Finds defects, regressions, and missing coverage before release. |
| `testing` | `testing` | Testing Specialist | Designs and validates tests for the changed slice. |
| `security` | `security` | Security Reviewer | Assesses secrets handling, unsafe file access, and privilege boundaries. |
| `documentation` | `documentation` | Documentation Writer | Produces concise user and developer documentation that matches the implementation. |
| `release` | `general` | Release Manager | Coordinates versioning, packaging, and verification for shipping. |

### GNCore Healthcare Operations (`healthcare-operations`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `healthcare-intake` | `healthcare-operations` | Healthcare Intake | Improve administrative intake completeness, routing, accessibility, and privacy. |
| `healthcare-scheduling` | `healthcare-operations` | Healthcare Scheduling | Coordinate appointments using supplied policies and patient preferences. |
| `healthcare-operations-map` | `healthcare-operations` | Healthcare Operations Map | Map administrative handoffs, delays, duplication, and ownership gaps. |
| `healthcare-quality` | `healthcare-operations` | Healthcare Quality Operations | Organize quality improvement with defined measures, owners, and review cycles. |
| `healthcare-privacy` | `healthcare-operations` | Healthcare Privacy Review | Review artifacts for privacy exposure and minimum-necessary handling. |
| `healthcare-policy` | `healthcare-operations` | Healthcare Policy Operations | Maintain operational policies with ownership, evidence, and review dates. |
| `healthcare-patient-comms` | `healthcare-operations` | Patient Administrative Communications | Write clear non-clinical communications about administrative next steps. |
| `healthcare-audit` | `healthcare-operations` | Healthcare Operations Audit | Review administrative controls and remediation with an evidence trail. |
| `healthcare-capacity` | `healthcare-operations` | Healthcare Capacity Planning | Model service capacity using operational data and explicit assumptions. |
| `healthcare-improvement` | `healthcare-operations` | Healthcare Improvement Cycle | Plan and assess a bounded operational improvement with safeguards. |

### GNCore Legal and Compliance Support (`legal-compliance`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `legal-contract-intake` | `legal-compliance` | Contract Review Intake | Extract obligations, deadlines, and questions from a supplied contract for counsel review. |
| `legal-obligation-map` | `legal-compliance` | Obligation Tracker | Turn contract or policy text into traceable obligations, owners, dates, and evidence. |
| `legal-policy-gap` | `legal-compliance` | Compliance Gap Assessment | Compare supplied controls or evidence against a named policy or framework requirement. |
| `legal-privacy-intake` | `legal-compliance` | Privacy Review Intake | Structure a privacy review by mapping purpose, data, access, retention, and user impact. |
| `legal-regulatory-watch` | `legal-compliance` | Regulatory Change Brief | Summarize a supplied regulatory update and identify affected business processes for expert review. |
| `legal-incident-hold` | `legal-compliance` | Legal Hold Coordination Checklist | Organize a preservation checklist from authorized instructions without altering source records. |
| `legal-marketing-claims` | `legal-compliance` | Marketing Claims Review | Trace public claims to substantiation and flag claims needing legal or regulatory review. |
| `legal-entity-records` | `legal-compliance` | Corporate Records Checklist | Organize entity governance records and upcoming filing or approval actions from supplied records. |
| `legal-dispute-chronology` | `legal-compliance` | Dispute Chronology | Build a source-linked chronology from supplied dispute materials for counsel review. |
| `legal-review-memo` | `legal-compliance` | Legal Review Memo Support | Draft a neutral issue-and-evidence memo for a qualified lawyer to review. |

### GNCore Machine Learning (`machine-learning`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `machine-learning` | `machine-learning` | Machine Learning Workflow | Develop a scoped machine learning feature, from data inspection and baseline selection through evaluation. |
| `model-training` | `machine-learning` | Model Training | Set up or improve a reproducible model training run with clear configuration, checkpoints, and evaluation. |
| `train` | `machine-learning` | Train a Machine Learning Model | Build and run a reproducible model training workflow with a baseline, tracked configuration, and held-out evaluation. |
| `preprocess` | `machine-learning` | Preprocess Machine Learning Data | Design a repeatable preprocessing pipeline that preserves schema, prevents leakage, and records transformations. |
| `evaluate` | `machine-learning` | Evaluate a Model | Evaluate model quality with leakage-safe splits, task-appropriate metrics, baselines, and error analysis. |
| `improve` | `machine-learning` | Improve a Machine Learning Model | Find evidence-based model improvements through error analysis and controlled experiments against a fixed baseline. |
| `data-preparation` | `machine-learning` | ML Data Preparation | Prepare reproducible model datasets while preventing leakage and preserving provenance. |
| `feature-engineering` | `machine-learning` | Feature Engineering | Build features that are valid at prediction time and reproducible across training and inference. |
| `fine-tuning` | `machine-learning` | Model Fine-Tuning | Plan or implement a parameter-efficient or full fine-tuning workflow with controlled data and cost. |
| `model-evaluation` | `machine-learning` | Model Evaluation | Evaluate model quality with valid splits, suitable metrics, uncertainty, and error analysis. |
| `experiment-tracking` | `machine-learning` | Reproducible ML Experiments | Make model experiments traceable across code, data, configuration, environment, and artifacts. |
| `model-serving` | `machine-learning` | Model Serving and Inference APIs | Package model inference behind a reliable API with validation, resource limits, and observable behavior. |
| `pytorch-training` | `machine-learning` | PyTorch Training | Implement PyTorch training loops with correct device, optimizer, checkpoint, and evaluation handling. |
| `tensorflow-training` | `machine-learning` | TensorFlow and Keras Training | Build TensorFlow/Keras training workflows with explicit data, callbacks, and evaluation behavior. |
| `deep-learning` | `machine-learning` | Deep Learning Engineering | Develop deep learning code with explicit tensor shapes, stable optimization, and reproducible evaluation. |
| `nlp` | `machine-learning` | Natural Language Processing | Build NLP pipelines that respect language, label quality, privacy, and task-specific evaluation. |
| `computer-vision` | `machine-learning` | Computer Vision | Build vision workflows with robust image handling, leakage-safe splits, and task-appropriate evaluation. |
| `mlops` | `machine-learning` | MLOps and Model Release | Package, register, and monitor models with reproducible artifacts and explicit release gates. |
| `ml-experiment-tracking` | `machine-learning` | Machine Learning Experiment Tracking | Make model experiments comparable with consistent splits, metrics, configuration, and artifact provenance. |
| `feature-engineering-practice` | `machine-learning` | Feature Engineering Practice | Create leakage-safe, interpretable features that match the model's serving-time information. |
| `time-series` | `machine-learning` | Time-Series Modeling | Analyze and forecast time-indexed data with temporal splits, leakage controls, and useful uncertainty. |
| `model-card` | `machine-learning` | Model Documentation | Document a model's intended use, data provenance, evaluation, limitations, and deployment assumptions. |
| `hardware-ml` | `machine-learning` | Edge and Hardware-Constrained ML | Adapt inference to constrained hardware using measured latency, memory, and accuracy tradeoffs. |

### GNCore Marketing and Growth (`marketing-growth`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `marketing-positioning` | `marketing-growth` | Positioning and Messaging | Develop evidence-based positioning for a defined audience and competitive context. |
| `marketing-campaign` | `marketing-growth` | Campaign Plan | Plan a campaign with audience, offer, channels, budget, measurement, and approval gates. |
| `marketing-content` | `marketing-growth` | Marketing Content Brief | Brief content creators with audience need, purpose, evidence, voice, format, and success criteria. |
| `marketing-seo` | `marketing-growth` | Search Content Audit | Audit search content for intent match, accuracy, technical discoverability, and useful next actions. |
| `marketing-lifecycle` | `marketing-growth` | Lifecycle Messaging | Design lifecycle messages that help users reach a meaningful product outcome. |
| `marketing-attribution` | `marketing-growth` | Marketing Attribution Review | Interpret marketing contribution while exposing attribution model limitations and incrementality. |
| `marketing-brand` | `marketing-growth` | Brand Consistency Review | Review brand execution for message consistency, audience fit, accessibility, and evidence. |
| `marketing-social` | `marketing-growth` | Social Media Plan | Create a platform-aware social plan with useful content, response ownership, and risk controls. |
| `marketing-budget` | `marketing-growth` | Marketing Budget Allocation | Allocate marketing budget using marginal returns, uncertainty, and strategic coverage. |
| `marketing-launch` | `marketing-growth` | Go-to-Market Launch | Coordinate market launch readiness across product, pricing, channels, enablement, and customer support. |

### GNCore Mobile Development (`mobile-development`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `mobile-app` | `mobile-development` | Mobile App Engineering | Implement mobile features with reliable navigation, offline behavior, accessibility, and platform conventions. |

### GNCore Operations (`operations`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `incident-response` | `operations` | Incident Response | Triage incidents from evidence, reduce impact safely, and preserve a clear timeline and follow-up. |

### GNCore PDF Documents (`pdf-documents`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `pdf-extract` | `pdf-documents` | PDF Text and Table Extraction | Extract text or tables from a supplied PDF while preserving page references and uncertainty. |
| `pdf-create` | `pdf-documents` | Create a PDF Deliverable | Create a clean PDF from approved source content and verify its page layout and metadata. |
| `pdf-accessibility` | `pdf-documents` | Accessible PDF Review | Review or improve PDF tags, reading order, headings, links, tables, and alternative text. |
| `pdf-merge` | `pdf-documents` | Merge PDFs | Combine approved PDFs in a defined order while preserving page integrity and source provenance. |
| `pdf-split` | `pdf-documents` | Split PDF by Page or Section | Split a PDF into named outputs using explicit page ranges or verified section boundaries. |
| `pdf-form` | `pdf-documents` | PDF Form Workflow | Inspect or create a fillable PDF form with labeled fields and reliable save behavior. |
| `pdf-ocr` | `pdf-documents` | Scanned PDF OCR | Make a scanned PDF searchable with OCR and verify text against original page images. |
| `pdf-redaction` | `pdf-documents` | PDF Redaction Review | Apply and verify permanent redaction to specifically authorized PDF content. |
| `pdf-review` | `pdf-documents` | PDF Content and Layout Review | Review PDF content, links, references, page numbering, and rendered layout before delivery. |
| `pdf-signature` | `pdf-documents` | PDF Signature Workflow Support | Prepare a PDF for an authorized signature workflow and verify fields and final artifact integrity. |

### GNCore People and Human Resources (`people-human-resources`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `people-role-design` | `people-human-resources` | Role Design | Define a role around outcomes, decision rights, essential skills, and fair selection criteria. |
| `people-job-post` | `people-human-resources` | Job Description | Draft an inclusive, accurate job description from an approved role profile. |
| `people-interview` | `people-human-resources` | Structured Interview Plan | Create a structured interview plan with job-related questions and consistent evaluation anchors. |
| `people-onboarding` | `people-human-resources` | Employee Onboarding Plan | Plan a role-specific onboarding path with access, learning, relationships, and early outcomes. |
| `people-development` | `people-human-resources` | Development Plan | Create a practical employee development plan linked to goals, strengths, and supported practice. |
| `people-performance` | `people-human-resources` | Performance Review Support | Organize performance evidence into a fair, specific, and balanced review draft. |
| `people-workforce-plan` | `people-human-resources` | Workforce Plan | Forecast workforce capacity and skills against business demand and approved scenarios. |
| `people-engagement` | `people-human-resources` | Engagement Survey Analysis | Analyze employee feedback responsibly while protecting confidentiality and avoiding false precision. |
| `people-policy` | `people-human-resources` | HR Policy Draft Review | Review an HR policy draft for clarity, internal consistency, accessibility, and escalation needs. |
| `people-offboarding` | `people-human-resources` | Employee Offboarding Checklist | Coordinate a respectful offboarding with access, knowledge transfer, property, records, and final responsibilities. |

### GNCore Presentations and PowerPoint (`presentations-powerpoint`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `ppt-storyline` | `presentations-powerpoint` | Presentation Storyline | Turn an audience, decision, and evidence set into a coherent presentation narrative. |
| `ppt-create` | `presentations-powerpoint` | Create a PowerPoint Deck | Create a presentation deck from a brief and source material with a clear storyline and consistent design. |
| `ppt-executive` | `presentations-powerpoint` | Executive Presentation | Prepare an executive deck that leads with decisions, implications, risks, and evidence. |
| `ppt-data-story` | `presentations-powerpoint` | Data Story Presentation | Explain data in slides with faithful charts, denominators, uncertainty, and a decision-relevant takeaway. |
| `ppt-visual-design` | `presentations-powerpoint` | Presentation Visual Design | Improve slide hierarchy, typography, color, alignment, and visual consistency without weakening content. |
| `ppt-edit` | `presentations-powerpoint` | Edit an Existing PPTX | Revise an existing deck while preserving intended content, theme, and editable structure. |
| `ppt-speaker-notes` | `presentations-powerpoint` | Speaker Notes and Talk Track | Write speaker notes that support a timed presentation without duplicating slide text. |
| `ppt-accessibility` | `presentations-powerpoint` | Accessible Presentation | Review a presentation for reading order, contrast, meaningful text, captions, and accessible charts. |
| `ppt-template` | `presentations-powerpoint` | PowerPoint Template Design | Create a reusable PowerPoint template with reliable masters, layouts, typography, and color tokens. |
| `ppt-deck-qa` | `presentations-powerpoint` | PowerPoint Deck QA | Run a final slide-by-slide quality pass on a saved presentation and its exported PDF. |

### GNCore Procurement and Vendor Management (`procurement-vendor`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `procurement-requirements` | `procurement-vendor` | Procurement Requirements | Translate a business need into measurable, vendor-neutral procurement requirements. |
| `procurement-rfp` | `procurement-vendor` | RFP Package | Prepare a fair request for proposal with scope, scoring, schedule, and response instructions. |
| `procurement-scorecard` | `procurement-vendor` | Vendor Scorecard | Score supplier proposals against published criteria with evidence and consistent normalization. |
| `procurement-total-cost` | `procurement-vendor` | Total Cost of Ownership | Compare vendor options across implementation, usage, support, renewal, exit, and risk costs. |
| `procurement-due-diligence` | `procurement-vendor` | Supplier Due Diligence | Coordinate risk-based supplier due diligence across security, privacy, finance, and continuity. |
| `procurement-negotiation` | `procurement-vendor` | Supplier Negotiation Plan | Prepare negotiation priorities and fallback options within approved procurement authority. |
| `procurement-onboarding` | `procurement-vendor` | Supplier Onboarding | Coordinate supplier onboarding with least-privilege access, ownership, and required control evidence. |
| `procurement-performance` | `procurement-vendor` | Supplier Performance Review | Review vendor service against contracted outcomes, service levels, and corrective actions. |
| `procurement-renewal` | `procurement-vendor` | Vendor Renewal Review | Make a renewal decision using value, risk, alternatives, usage, and notice deadlines. |
| `procurement-exit` | `procurement-vendor` | Supplier Exit Plan | Plan a controlled supplier transition that protects service, data, access, and records. |

### GNCore Product (`product`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `product-discovery` | `product` | Product Discovery | Turn a product idea into a testable problem statement, user evidence plan, and scoped first release. |

### GNCore Product Management (`product-management`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `product-opportunity` | `product-management` | Product Opportunity Brief | Turn customer and business evidence into a scoped product opportunity. |
| `product-requirements` | `product-management` | Product Requirements | Write testable product requirements and acceptance criteria for a scoped feature. |
| `product-roadmap` | `product-management` | Product Roadmap | Build an outcome-led roadmap that exposes dependencies, confidence, and trade-offs. |
| `product-discovery-sprint` | `product-management` | Product Discovery Sprint | Plan a short discovery cycle that resolves the riskiest product assumptions. |
| `product-prioritization` | `product-management` | Feature Prioritization | Prioritize feature requests using customer value, evidence, cost, and strategic fit. |
| `product-experiment` | `product-management` | Product Experiment Design | Design product experiments with a clear hypothesis, metric, guardrails, and decision rule. |
| `product-launch` | `product-management` | Product Launch Readiness | Coordinate launch readiness across product, engineering, support, sales, and communications. |
| `product-feedback` | `product-management` | Customer Feedback Synthesis | Synthesize product feedback into traceable themes without overstating frequency. |
| `product-lifecycle` | `product-management` | Product Lifecycle Review | Assess adoption, retention, quality, and investment choices for an existing product. |
| `product-metrics` | `product-management` | Product Metrics Definition | Define a product metric with an unambiguous event, population, denominator, and owner. |

### GNCore Professional Services (`professional-services`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `legal-document-review` | `professional-services` | Legal Document Review Support | Summarize a legal document's structure and flag questions for qualified counsel without giving definitive legal advice. |
| `finance-analysis` | `professional-services` | Financial Analysis Support | Structure financial calculations and scenarios with transparent inputs, formulas, and sensitivity ranges. |

### GNCore Project and Program Management (`project-program-management`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `project-charter` | `project-program-management` | Project Charter | Create a concise project charter with outcome, scope, ownership, constraints, and decision gates. |
| `project-plan` | `project-program-management` | Delivery Plan | Build an executable delivery plan with milestones, dependencies, owners, and evidence. |
| `project-status` | `project-program-management` | Project Status Brief | Produce a truthful project status update with progress, forecast, risks, and asks. |
| `project-risk-log` | `project-program-management` | Project Risk Log | Create and maintain actionable project risks, issues, assumptions, and dependencies. |
| `project-recovery` | `project-program-management` | Project Recovery Plan | Recover a troubled project by identifying root causes and rebaselining achievable outcomes. |
| `project-meeting` | `project-program-management` | Decision Meeting Preparation | Prepare a meeting agenda and decision record that uses participant time effectively. |
| `project-dependency` | `project-program-management` | Dependency Coordination | Map and resolve cross-team dependencies before they become delivery blockers. |
| `project-capacity` | `project-program-management` | Capacity and Resource Plan | Match project demand to available skills, capacity, and protected operational work. |
| `project-retro` | `project-program-management` | Project Retrospective | Run a blameless retrospective that yields specific, owned process improvements. |
| `project-closure` | `project-program-management` | Project Closure and Handoff | Close a project with accepted deliverables, operational ownership, records, and lessons. |

### GNCore Python (`python`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `python-library` | `python` | Python Library Engineering | Design maintainable Python packages with stable APIs, typing, packaging, and clear examples. |
| `python-performance` | `python` | Python Performance | Profile Python hotspots and improve measured runtime or memory without changing semantics. |
| `python-packaging` | `python` | Python Packaging | Package a Python library with clear APIs, reproducible builds, supported versions, and clean installation behavior. |
| `python-migration` | `python` | Python Upgrade and Migration | Migrate Python code or dependencies in a controlled way with compatibility evidence and a rollback path. |

### GNCore Quality Assurance (`quality-assurance`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `accessibility-audit` | `quality-assurance` | Accessibility Audit | Inspect a user flow for keyboard, screen reader, visual, and cognitive accessibility barriers. |
| `performance-audit` | `quality-assurance` | Performance Audit | Find and verify the largest performance bottlenecks before changing code or infrastructure. |
| `test-strategy` | `quality-assurance` | Test Strategy | Choose a balanced test plan that catches important failures at the lowest practical level. |
| `requirements-to-tests` | `quality-assurance` | Requirements to Acceptance Tests | Turn requirements into observable acceptance cases that cover success, failure, boundaries, and permissions. |

### GNCore Quality Engineering and Testing (`quality-engineering`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `qa-test-strategy` | `quality-engineering` | Test Strategy | Choose a risk-based test mix that verifies behavior at the lowest effective level. |
| `qa-test-design` | `quality-engineering` | Test Case Design | Turn a behavior contract into clear positive, negative, boundary, and state-transition tests. |
| `qa-automation` | `quality-engineering` | Test Automation | Build maintainable test automation with stable setup, deterministic data, and actionable failures. |
| `qa-e2e` | `quality-engineering` | End-to-End User Journey Test | Verify a critical user journey across the application with realistic but isolated data. |
| `qa-api-contract` | `quality-engineering` | API Contract Testing | Check API compatibility, validation, authorization, and error contracts between services. |
| `qa-performance` | `quality-engineering` | Performance Test Plan | Measure a service against representative load, latency, throughput, and resource objectives. |
| `qa-accessibility` | `quality-engineering` | Accessibility Test Pass | Test a flow for keyboard operation, semantics, focus, labels, zoom, and assistive technology support. |
| `qa-defect-triage` | `quality-engineering` | Defect Triage | Classify and prioritize a defect using reproducibility, user impact, scope, and workaround evidence. |
| `qa-release-gate` | `quality-engineering` | Release Quality Gate | Evaluate release evidence against agreed quality gates and make residual risk visible. |
| `qa-flaky-test` | `quality-engineering` | Flaky Test Investigation | Find the cause of an intermittent test failure and confirm a stable correction. |

### GNCore Release Engineering (`release-engineering`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `release-readiness` | `release-engineering` | Release Readiness Review | Check a release candidate against explicit acceptance, compatibility, security, rollback, and communication gates. |

### GNCore Research (`research`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `research-synthesis` | `research` | Research Synthesis | Synthesize supplied or sourced evidence with provenance, disagreement, and uncertainty kept visible. |

### GNCore Research and Market Intelligence (`research-market-intelligence`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `research-question` | `research-market-intelligence` | Research Question Design | Frame a researchable question with scope, definitions, evidence criteria, and a useful decision. |
| `research-source-audit` | `research-market-intelligence` | Source Quality Audit | Evaluate sources for authority, method, date, provenance, conflicts, and fitness for a claim. |
| `research-literature-review` | `research-market-intelligence` | Literature Review | Synthesize a literature set with methods, findings, disagreement, and evidence gaps visible. |
| `research-market-size` | `research-market-intelligence` | Market Sizing | Estimate a market using transparent bottom-up or top-down assumptions and sensitivity ranges. |
| `research-customer` | `research-market-intelligence` | Customer and Market Research | Combine customer evidence and market signals into actionable, bounded insights. |
| `research-competitor` | `research-market-intelligence` | Competitive Research Brief | Prepare a dated competitor brief from verifiable product, pricing, and positioning evidence. |
| `research-evidence-map` | `research-market-intelligence` | Evidence Map | Organize claims, sources, strength, disagreement, and missing evidence for a decision area. |
| `research-survey` | `research-market-intelligence` | Survey Design and Review | Design a survey with neutral wording, clear constructs, representative sampling, and privacy safeguards. |
| `research-brief` | `research-market-intelligence` | Research Brief | Turn research into a concise, sourced brief with answer, confidence, implications, and open questions. |
| `research-monitor` | `research-market-intelligence` | Research Update Monitor | Track a defined topic for material source changes without overwhelming users with routine noise. |

### GNCore Sales and Revenue (`sales-revenue`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `sales-account-plan` | `sales-revenue` | Strategic Account Plan | Create an account plan based on customer outcomes, stakeholders, risks, and verified activity. |
| `sales-discovery` | `sales-revenue` | Sales Discovery | Prepare neutral discovery questions that uncover customer needs, impact, constraints, and decision process. |
| `sales-qualification` | `sales-revenue` | Opportunity Qualification | Assess opportunity fit and deal risk using transparent qualification evidence. |
| `sales-pipeline` | `sales-revenue` | Pipeline Review | Inspect pipeline quality and next-step integrity to improve forecast and coaching. |
| `sales-forecast` | `sales-revenue` | Revenue Forecast | Build a revenue forecast with explicit assumptions, scenarios, and confidence. |
| `sales-proposal` | `sales-revenue` | Customer Proposal | Draft a customer proposal tied to stated needs, outcomes, scope, assumptions, and evidence. |
| `sales-negotiation` | `sales-revenue` | Commercial Negotiation Preparation | Prepare negotiation options and concession boundaries grounded in approved commercial policy. |
| `sales-objection` | `sales-revenue` | Customer Objection Response | Answer a sales objection with accurate evidence and a useful next question. |
| `sales-territory` | `sales-revenue` | Territory and Coverage Plan | Balance account coverage and sales capacity across a territory using transparent criteria. |
| `sales-renewal` | `sales-revenue` | Renewal and Expansion Plan | Protect a renewal by connecting adoption, realized outcomes, risks, and agreed next value. |

### GNCore Security (`security`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `web-security` | `security` | Web Security Engineering | Review web features for input, session, authorization, and output-handling vulnerabilities. |
| `privacy-review` | `security` | Privacy Review | Reduce privacy risk by tracing personal data, purpose, access, retention, and user control. |

### GNCore Software Engineering (`software-engineering`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `software-feature` | `software-engineering` | Software Feature Delivery | Deliver a scoped software feature using local conventions and verifiable acceptance criteria. |
| `software-architecture` | `software-engineering` | Software Architecture Decision | Compare architecture options against constraints, operations, reversibility, and lifecycle cost. |
| `software-code-review` | `software-engineering` | Software Code Review | Review a code change for correctness, security, maintainability, and missing regression coverage. |
| `software-debugging` | `software-engineering` | Software Debugging | Diagnose a software failure from reproducible evidence and verify the smallest safe fix. |
| `software-refactor` | `software-engineering` | Safe Refactoring | Refactor a bounded code area while preserving its documented behavior and public contracts. |
| `software-api-contract` | `software-engineering` | Software API Contract | Define and verify an API contract across request, response, errors, versioning, and consumers. |
| `software-dependency` | `software-engineering` | Dependency Change Review | Assess and implement a dependency change with compatibility, security, and rollback evidence. |
| `software-performance` | `software-engineering` | Software Performance Optimization | Find a measured software bottleneck and optimize it without regressing correctness. |
| `software-migration` | `software-engineering` | Software Migration Plan | Plan a staged migration with compatibility gates, data safety, and rollback criteria. |
| `software-release` | `software-engineering` | Software Release Candidate | Prepare a software release with reproducible artifacts, verified changes, and rollback readiness. |

### GNCore Spreadsheets and Excel (`spreadsheets`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `sheet-model` | `spreadsheets` | Spreadsheet Model Design | Structure a spreadsheet model with clear inputs, calculations, outputs, and traceable assumptions. |
| `sheet-formula-audit` | `spreadsheets` | Spreadsheet Formula Audit | Audit workbook formulas for broken references, inconsistencies, hard-codes, and calculation errors. |
| `sheet-clean` | `spreadsheets` | Spreadsheet Data Cleaning | Clean tabular spreadsheet data with explicit rules and before/after reconciliation. |
| `sheet-analysis` | `spreadsheets` | Spreadsheet Data Analysis | Answer an analytical question from workbook data with transparent formulas and checks. |
| `sheet-dashboard` | `spreadsheets` | Spreadsheet Dashboard | Build a decision-focused spreadsheet dashboard with stable formulas, labels, filters, and accessible visuals. |
| `sheet-pivot` | `spreadsheets` | Pivot Table Analysis | Create or review pivot analyses with verified source range, grouping, aggregation, and filter behavior. |
| `sheet-forecast` | `spreadsheets` | Spreadsheet Forecast Model | Build or audit a forecast workbook with driver-based assumptions, scenarios, and error checks. |
| `sheet-reconcile` | `spreadsheets` | Spreadsheet Reconciliation | Reconcile two data sources with stable keys, exception categories, and totals control. |
| `sheet-automation` | `spreadsheets` | Spreadsheet Automation | Automate repetitive workbook transformations with idempotent runs and safe output handling. |
| `sheet-presentation` | `spreadsheets` | Spreadsheet Presentation Cleanup | Prepare a workbook for review or print with consistent formats, frozen headers, page setup, and clear labels. |

### GNCore Supply Chain and Logistics (`supply-chain-logistics`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `supply-demand` | `supply-chain-logistics` | Demand Planning | Build a demand view with documented inputs, scenarios, and error checks. |
| `supply-sourcing` | `supply-chain-logistics` | Sourcing Strategy | Compare sourcing options for cost, quality, lead time, resilience, and compliance. |
| `supply-supplier` | `supply-chain-logistics` | Supplier Performance Review | Review supplier performance with agreed measures and corrective actions. |
| `supply-inventory` | `supply-chain-logistics` | Inventory Optimization | Identify inventory imbalances without hiding service risk. |
| `supply-warehouse` | `supply-chain-logistics` | Warehouse Operations | Improve warehouse flow, safety, accuracy, and workload visibility. |
| `supply-transport` | `supply-chain-logistics` | Transportation Planning | Plan shipments with constraints, service, cost, and exception handling visible. |
| `supply-resilience` | `supply-chain-logistics` | Supply Chain Risk Review | Assess disruption exposure, early signals, and mitigation options. |
| `supply-control-tower` | `supply-chain-logistics` | Supply Chain Exception Review | Triage exceptions by impact, owner, and next update. |
| `supply-procurement` | `supply-chain-logistics` | Purchase Order Reconciliation | Reconcile orders, receipts, invoices, and supplier records with traceable exceptions. |
| `supply-sustainability` | `supply-chain-logistics` | Supply Chain Sustainability Review | Review sustainability claims with boundaries, evidence, and data-quality limits. |

### GNCore Testing (`testing`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `unit-testing` | `testing` | Unit Testing | Write fast, deterministic unit tests around public behavior and edge cases. |
| `integration-testing` | `testing` | Integration Testing | Verify interactions between real components while isolating external services and state. |
| `end-to-end-testing` | `testing` | End-to-End Testing | Validate critical user journeys across the running application with stable, accessible assertions. |
| `test-automation` | `testing` | Test Automation Engineering | Create maintainable CI test workflows with clear triggers, artifacts, and failure signals. |
| `performance-testing` | `testing` | Performance and Load Testing | Design controlled load tests that measure latency, throughput, and saturation safely. |

### GNCore Web Development (`web-development`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `web-development` | `web-development` | Web Development | Plan and implement a focused web feature using the repository's existing framework, patterns, and tests. |
| `seo-audit` | `web-development` | SEO Audit | Improve technical and content discoverability using crawlable structure and verifiable search metadata. |

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

### GNCore Microsoft Word and DOCX Documents (`word-documents`)

| Workflow ID | Resolves to | Workflow | Use it for |
| --- | --- | --- | --- |
| `word-draft` | `word-documents` | Draft a Word Document | Create a structured Word document from a brief, source material, and intended audience. |
| `word-edit` | `word-documents` | Edit and Restructure DOCX | Edit an existing Word document for clarity and structure while preserving required content. |
| `word-format` | `word-documents` | Word Formatting Repair | Repair Word styles, spacing, headers, pagination, tables, and section layout. |
| `word-redline` | `word-documents` | Word Tracked Changes Review | Prepare or review DOCX edits with traceable changes and comments for human approval. |
| `word-accessibility` | `word-documents` | Accessible Word Document | Improve DOCX structure and accessibility for navigation, screen readers, and document reuse. |
| `word-template` | `word-documents` | Word Template Design | Create a reusable Word template with stable styles, fields, sections, and usage rules. |
| `word-report` | `word-documents` | Word Report Production | Produce a sourced report in Word with executive summary, evidence, findings, and appendices. |
| `word-merge` | `word-documents` | Word Document Merge | Combine supplied DOCX materials into one coherent document without losing provenance or structure. |
| `word-forms` | `word-documents` | Word Form Design | Design a fillable Word form with clear labels, logical completion order, and safe review. |
| `word-review` | `word-documents` | Word Final Proof and QA | Proofread a final DOCX for content consistency, references, fields, and page-level layout. |

## Use

```bash
gncore export --specific web-frontend
gncore export --skills web-backend code-build
gncore export --all --output gncore-categories.zip
gncore plan "A premium hotel website, no animation"
```

See [Source Research](SOURCE_RESEARCH.md), [Ownership](OWNERSHIP.md), and [Migration](../MIGRATION.md) for provenance, licensing, and compatibility details.
