---
name: web-backend
description: "Build and improve backend services, APIs, persistence, integrations, AI systems, delivery, and observability in the selected stack."
license: Apache-2.0 AND CC-BY-SA-4.0 AND MIT
---

# GNCore Backend Engineering

## Select the work from the user's intent

Follow the request from validation and authentication through domain rules, transactions, external calls, background work, and telemetry. Select the actual framework and relevant specialist modes. Define contracts, ownership, failure semantics, retry boundaries, and operational constraints.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Verify success, invalid input, denied access, relevant concurrency or idempotency cases, and failure recovery. Use measured evidence for performance claims and distinguish local checks from deployed outcomes.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `web-backend-patterns` | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. |
| `web-backend-api-design` | REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs. |
| `web-backend-hexagonal-architecture` | Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, and testable use-case orchestration across TypeScript, Java, Kotlin, and Go services. |
| `web-backend-error-handling` | Patterns for robust error handling across TypeScript, Python, and Go. |
| `web-backend-contract-first` | Coordinate frontend/backend or service-to-service work through one authoritative machine-checkable contract (OpenAPI, AsyncAPI, Protocol Buffers, or JSON Schema), with generated consumer types and contract-verified integration. |
| `web-backend-api-connector-builder` | Build a new API connector or provider by matching the target repo's existing integration pattern exactly. |
| `web-backend-spec-to-code-compliance` | Check code against the documentation that specifies it - which requirements hold, which the code contradicts, which are absent, and what the code does that no document mentions. |
| `web-backend-supabase-postgres-best-practices` | Postgres best practices maintained by Supabase, for Postgres running anywhere. |
| `web-backend-postgres-patterns` | PostgreSQL database patterns for query optimization, schema design, indexing, and security. |
| `web-backend-database-migrations` | Safe, reversible database migration patterns: forward-only production changes, expand-contract zero-downtime renames, concurrent indexes, batched backfills, and per-tool workflows for PostgreSQL, Prisma, Drizzle, Kysely, Django, and golang-migrate. |
| `web-backend-benchmark` | Measure performance baselines and detect regressions across browser Core Web Vitals (LCP, INP, CLS, page weight), API endpoint latency percentiles, and build/test feedback times, with before/after comparison stored in git-tracked .ecc/benchmarks JSON. |
| `web-backend-benchmark-optimization-loop` | Convert 'make it faster' requests into a bounded measured optimization loop — baseline first, generate one-hypothesis variants, benchmark each against a correctness gate, and promote the fastest safe variant with reproducible commands. |
| `web-backend-latency-critical-systems` | Optimize and verify latency-sensitive systems — realtime dashboards, market data feeds, streaming agents, execution gateways, queues, and caches — by tracking p50/p95/p99 latency, freshness age, and queue depth, mapping hot paths, and running live readbacks. |
| `web-backend-redis-patterns` | Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection management for production applications. |
| `web-backend-deployment-patterns` | Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, and production readiness checklists for web applications. |
| `web-backend-docker` | Docker and Docker Compose patterns for local development, hardened CLI installer harnesses, container security, networking, volumes, and multi-service orchestration. |
| `web-backend-github-ops` | GitHub repository operations, automation, and management. |
| `web-backend-sentry-instrument` | Instrument an application with Sentry — detect the platform, install and initialize the SDK if needed, and wire up any signal — error monitoring, tracing/performance, logging, metrics, profiling, session replay, user feedback, cron check-ins, uptime monitors for the deployed app, and AI/LLM monitoring (agent runs, token cost, and conversations for... |
| `web-backend-sentry-debug-issue` | Debug and fix a Sentry issue — find it (by link, ID, or search), pull full context (stack trace, breadcrumbs, trace, logs), optionally run Seer root-cause / autofix, apply the code fix, and resolve it via a `Fixes PROJECT-NAME-12A` commit/PR. |
| `web-backend-production-audit` | Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what breaks in prod?" questions without sending repo data to an external audit service. |
| `web-backend-agentic-engineering` | Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing. |
| `web-backend-mcp-server-patterns` | Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HTTP. |
| `web-backend-agent-eval` | Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate, cost, time, and consistency metrics. |
| `web-backend-cost-aware-llm-pipeline` | Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt caching. |
| `web-backend-mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. |
| `web-backend-agents-sdk` | Build, debug, or review Cloudflare Agents SDK applications using the agents package. |
| `web-backend-building-ai-agent-on-cloudflare` | Build a scoped AI agent on Cloudflare with explicit state, tool boundaries, bindings, and evaluation cases. |
| `web-backend-fastapi` | Build FastAPI endpoints, Pydantic models, dependencies, and streaming responses using version-compatible APIs. |
| `web-backend-fastapi-patterns` | FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, authentication, authorization, transactional service layers, and testing with httpx and pytest. |
| `web-backend-django` | Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and production-grade Django apps. |
| `web-backend-django-security` | Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS prevention, and secure deployment configurations. |
| `web-backend-django-tdd` | Django testing strategies with pytest-django, TDD methodology, factory_boy, mocking, coverage, and testing Django REST Framework APIs. |
| `web-backend-django-verification` | Run the full Django verification loop — environment check, mypy/ruff/black linting, migration safety, pytest with coverage targets, pip-audit and bandit security scans, settings and logging review, and diff review — producing a phased pass/fail report before release or PR. |
| `web-backend-nestjs-patterns` | NestJS architecture patterns for modules, controllers, providers, DTO validation, guards, interceptors, config, and production-grade TypeScript backends. |
| `web-backend-springboot-patterns` | Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, and logging. |
| `web-backend-springboot-security` | Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and dependency security in Java Spring Boot services. |
| `web-backend-springboot-tdd` | Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo. |
| `web-backend-springboot-verification` | Run the full Spring Boot verification loop — Maven or Gradle build, SpotBugs, PMD, and Checkstyle static analysis, unit and Testcontainers integration tests with JaCoCo coverage, OWASP dependency and secret scans, and diff review — producing a pass/fail readiness report. |
| `web-backend-golang-patterns` | Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go applications. |
| `web-backend-golang-testing` | Go testing patterns including table-driven tests, subtests, benchmarks, fuzzing, and test coverage. |
| `web-backend-laravel-patterns` | Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and API resources for production apps. |
| `web-backend-laravel-security` | Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API security, and secure deployment configurations. |
| `web-backend-laravel-tdd` | Laravel testing strategies with PHPUnit, Pest, model factories, HTTP tests, Sanctum authentication testing, mocking, and coverage. |
| `web-backend-laravel-verification` | Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security scans, and deployment readiness. |
| `web-backend-supabase` | Implement or debug Supabase database, authentication, storage, and realtime features using current product documentation. |
| `web-backend-redis-core` | Core Redis modeling guidance — choose the right data structure (String, Hash, List, Set, Sorted Set, JSON, Stream, Vector Set) and use consistent colon-separated key names. |
| `web-backend-redis-connections` | Redis client and connection guidance covering connection pooling, multiplexing, pipelining, client-side caching with RESP3, avoiding slow commands (KEYS, SMEMBERS, HGETALL), and tuning socket timeouts. |
| `web-backend-redis-security` | Redis security guidance covering authentication (requirepass and ACL users), TLS, ACL-based least-privilege access control, restricting network exposure via bind and protected-mode, firewall rules, and disabling dangerous commands. |
| `web-backend-redis-observability` | Redis observability guidance — which metrics to monitor (memory, connections, hit ratio, ops/sec, rejected connections), which built-in commands to reach for during incident triage (SLOWLOG, INFO, MEMORY DOCTOR, CLIENT LIST, FT.PROFILE), and when to use the Redis Insight GUI. |
| `web-backend-redis-search` | Redis Search guidance covering FT.CREATE schema design, field type selection (TEXT, TAG, NUMERIC, GEO, GEOSHAPE, VECTOR, JSON path), DIALECT 2 query syntax, FT.SEARCH / FT.AGGREGATE / FT.HYBRID command selection, vector similarity with HNSW or FLAT, hybrid retrieval combining lexical and vector ranking, RAG pipelines, zero-downtime index updates via... |
| `web-backend-redis-semantic-cache` | Redis LangCache guidance for semantic caching of LLM responses on Redis Cloud — calling search/set via the SDK or REST API, tuning the similarity threshold, separating caches per task type, and filtering with custom attributes. |
| `web-backend-vercel-optimize` | Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited Astro apps. |
| `web-backend-cloudflare` | Discover and choose Cloudflare products for apps, APIs, AI agents, storage, networking, and security. |
| `web-backend-workers-best-practices` | Cloudflare Workers best practices for production applications. |
| `web-backend-wrangler` | Run or troubleshoot Wrangler CLI commands in projects that have a wrangler.jsonc, wrangler.json, or wrangler.toml file, including local development, Previews, deployment, and resource management. |
| `web-backend-durable-objects` | Build, debug, or review Cloudflare Durable Objects code for persistent state and coordination. |
| `web-backend-workers-profiling` | Profile or debug CPU usage and memory allocation in deployed Cloudflare Workers and Durable Objects. |
| `web-backend` | Route a backend task to the appropriate architecture, API, database, stack, security, or operations workflow. |
| `web-backend-codequality` | Improve backend correctness and maintainability across boundaries, data handling, concurrency, and error paths. |
| `web-backend-security` | Review and repair backend authentication, object authorization, input handling, session, and secret boundaries. |
| `web-backend-observability` | Design and verify useful service logs, traces, metrics, and alert signals with bounded overhead. |

## Focused procedures

### GNCore Patterns (`web-backend-patterns`)

Trace request boundaries, domain rules, persistence, dependencies, and failure modes in the current system. Choose interfaces and ownership boundaries appropriate to the actual service and explain concrete tradeoffs before changing architecture.

For task-specific technical depth, read [the attributed source guide](references/web-backend-patterns/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Api Design (`web-backend-api-design`)

Trace request boundaries, domain rules, persistence, dependencies, and failure modes in the current system. Choose interfaces and ownership boundaries appropriate to the actual service and explain concrete tradeoffs before changing architecture.

For task-specific technical depth, read [the attributed source guide](references/web-backend-api-design/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Hexagonal Architecture (`web-backend-hexagonal-architecture`)

Trace request boundaries, domain rules, persistence, dependencies, and failure modes in the current system. Choose interfaces and ownership boundaries appropriate to the actual service and explain concrete tradeoffs before changing architecture.

For task-specific technical depth, read [the attributed source guide](references/web-backend-hexagonal-architecture/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Error Handling (`web-backend-error-handling`)

Trace request boundaries, domain rules, persistence, dependencies, and failure modes in the current system. Choose interfaces and ownership boundaries appropriate to the actual service and explain concrete tradeoffs before changing architecture.

For task-specific technical depth, read [the attributed source guide](references/web-backend-error-handling/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Contract First (`web-backend-contract-first`)

Inspect producers, consumers, schemas, authentication, and compatibility requirements. Make validation, status codes, error envelopes, pagination, and idempotency explicit when relevant; verify implementation against the agreed contract.

For task-specific technical depth, read [the attributed source guide](references/web-backend-contract-first/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Api Connector Builder (`web-backend-api-connector-builder`)

Inspect producers, consumers, schemas, authentication, and compatibility requirements. Make validation, status codes, error envelopes, pagination, and idempotency explicit when relevant; verify implementation against the agreed contract.

For task-specific technical depth, read [the attributed source guide](references/web-backend-api-connector-builder/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Spec To Code Compliance (`web-backend-spec-to-code-compliance`)

Inspect producers, consumers, schemas, authentication, and compatibility requirements. Make validation, status codes, error envelopes, pagination, and idempotency explicit when relevant; verify implementation against the agreed contract.

For task-specific technical depth, read [the attributed source guide](references/web-backend-spec-to-code-compliance/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Supabase Postgres Best Practices (`web-backend-supabase-postgres-best-practices`)

Inspect the schema, query patterns, consistency rules, and migration tooling. Preserve transaction and authorization boundaries; use representative query plans or migration checks and account for rollback, existing data, and concurrent writes.

For task-specific technical depth, read [the attributed source guide](references/web-backend-supabase-postgres-best-practices/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Postgres Patterns (`web-backend-postgres-patterns`)

Inspect the schema, query patterns, consistency rules, and migration tooling. Preserve transaction and authorization boundaries; use representative query plans or migration checks and account for rollback, existing data, and concurrent writes.

For task-specific technical depth, read [the attributed source guide](references/web-backend-postgres-patterns/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Database Migrations (`web-backend-database-migrations`)

Inspect the schema, query patterns, consistency rules, and migration tooling. Preserve transaction and authorization boundaries; use representative query plans or migration checks and account for rollback, existing data, and concurrent writes.

For task-specific technical depth, read [the attributed source guide](references/web-backend-database-migrations/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Benchmark (`web-backend-benchmark`)

Establish a representative baseline and workload before optimizing. Identify the dominant latency, throughput, contention, or resource cost; change a measured bottleneck and compare under the same conditions while preserving correctness.

For task-specific technical depth, read [the attributed source guide](references/web-backend-benchmark/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Benchmark Optimization Loop (`web-backend-benchmark-optimization-loop`)

Establish a representative baseline and workload before optimizing. Identify the dominant latency, throughput, contention, or resource cost; change a measured bottleneck and compare under the same conditions while preserving correctness.

For task-specific technical depth, read [the attributed source guide](references/web-backend-benchmark-optimization-loop/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Latency Critical Systems (`web-backend-latency-critical-systems`)

Establish a representative baseline and workload before optimizing. Identify the dominant latency, throughput, contention, or resource cost; change a measured bottleneck and compare under the same conditions while preserving correctness.

For task-specific technical depth, read [the attributed source guide](references/web-backend-latency-critical-systems/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Redis Patterns (`web-backend-redis-patterns`)

Establish a representative baseline and workload before optimizing. Identify the dominant latency, throughput, contention, or resource cost; change a measured bottleneck and compare under the same conditions while preserving correctness.

For task-specific technical depth, read [the attributed source guide](references/web-backend-redis-patterns/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Deployment Patterns (`web-backend-deployment-patterns`)

Inspect the build, runtime, configuration, dependency pinning, and current delivery workflow. Prepare reproducible changes and validate a local or staging path; preserve secret boundaries and distinguish a prepared rollout from an actual authorized deployment.

For task-specific technical depth, read [the attributed source guide](references/web-backend-deployment-patterns/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Docker (`web-backend-docker`)

Inspect the build, runtime, configuration, dependency pinning, and current delivery workflow. Prepare reproducible changes and validate a local or staging path; preserve secret boundaries and distinguish a prepared rollout from an actual authorized deployment.

For task-specific technical depth, read [the attributed source guide](references/web-backend-docker/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Github Ops (`web-backend-github-ops`)

Inspect the build, runtime, configuration, dependency pinning, and current delivery workflow. Prepare reproducible changes and validate a local or staging path; preserve secret boundaries and distinguish a prepared rollout from an actual authorized deployment.

For task-specific technical depth, read [the attributed source guide](references/web-backend-github-ops/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Sentry Instrument (`web-backend-sentry-instrument`)

Trace existing logs, traces, metrics, error grouping, and incident context. Instrument useful boundaries with redaction and bounded cardinality; correlate observed failures to code and verify signals without inventing production access or outcomes.

For task-specific technical depth, read [the attributed source guide](references/web-backend-sentry-instrument/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Sentry Debug Issue (`web-backend-sentry-debug-issue`)

Trace existing logs, traces, metrics, error grouping, and incident context. Instrument useful boundaries with redaction and bounded cardinality; correlate observed failures to code and verify signals without inventing production access or outcomes.

For task-specific technical depth, read [the attributed source guide](references/web-backend-sentry-debug-issue/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Production Audit (`web-backend-production-audit`)

Trace existing logs, traces, metrics, error grouping, and incident context. Instrument useful boundaries with redaction and bounded cardinality; correlate observed failures to code and verify signals without inventing production access or outcomes.

For task-specific technical depth, read [the attributed source guide](references/web-backend-production-audit/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Agentic Engineering (`web-backend-agentic-engineering`)

Define model and tool boundaries, typed inputs, state ownership, failure handling, and evaluation cases. Bound retries, latency, and spending; preserve authorization around external actions and verify useful task outcomes rather than evaluating model prose alone.

For task-specific technical depth, read [the attributed source guide](references/web-backend-agentic-engineering/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Mcp Server Patterns (`web-backend-mcp-server-patterns`)

Define model and tool boundaries, typed inputs, state ownership, failure handling, and evaluation cases. Bound retries, latency, and spending; preserve authorization around external actions and verify useful task outcomes rather than evaluating model prose alone.

For task-specific technical depth, read [the attributed source guide](references/web-backend-mcp-server-patterns/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Agent Eval (`web-backend-agent-eval`)

Define model and tool boundaries, typed inputs, state ownership, failure handling, and evaluation cases. Bound retries, latency, and spending; preserve authorization around external actions and verify useful task outcomes rather than evaluating model prose alone.

For task-specific technical depth, read [the attributed source guide](references/web-backend-agent-eval/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Cost Aware Llm Pipeline (`web-backend-cost-aware-llm-pipeline`)

Define model and tool boundaries, typed inputs, state ownership, failure handling, and evaluation cases. Bound retries, latency, and spending; preserve authorization around external actions and verify useful task outcomes rather than evaluating model prose alone.

For task-specific technical depth, read [the attributed source guide](references/web-backend-cost-aware-llm-pipeline/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Mcp Builder (`web-backend-mcp-builder`)

Define model and tool boundaries, typed inputs, state ownership, failure handling, and evaluation cases. Bound retries, latency, and spending; preserve authorization around external actions and verify useful task outcomes rather than evaluating model prose alone.

For task-specific technical depth, read [the attributed source guide](references/web-backend-mcp-builder/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Agents Sdk (`web-backend-agents-sdk`)

Define model and tool boundaries, typed inputs, state ownership, failure handling, and evaluation cases. Bound retries, latency, and spending; preserve authorization around external actions and verify useful task outcomes rather than evaluating model prose alone.

For task-specific technical depth, read [the attributed source guide](references/web-backend-agents-sdk/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Building Ai Agent On Cloudflare (`web-backend-building-ai-agent-on-cloudflare`)

Inspect the selected Workers and Agents SDK versions, Wrangler configuration, bindings, authentication, state storage, and model provider. Implement the requested agent interaction with typed tool inputs, bounded retries, cancellation, and durable state only where needed. Keep provider credentials in the platform secret mechanism. Verify a useful task, a tool error, and an unauthorized request locally; prepare deployment instructions without claiming a deployed service unless deployment was requested and verified.

### GNCore Fastapi (`web-backend-fastapi`)

Inspect Python, framework, validation, database, and test versions before choosing APIs. Implement typed boundaries and explicit error handling using the current project conventions; verify the requested behavior with framework-appropriate tests.

For task-specific technical depth, read [the attributed source guide](references/web-backend-fastapi/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Fastapi Patterns (`web-backend-fastapi-patterns`)

Inspect Python, framework, validation, database, and test versions before choosing APIs. Implement typed boundaries and explicit error handling using the current project conventions; verify the requested behavior with framework-appropriate tests.

For task-specific technical depth, read [the attributed source guide](references/web-backend-fastapi-patterns/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Django (`web-backend-django`)

Inspect Python, framework, validation, database, and test versions before choosing APIs. Implement typed boundaries and explicit error handling using the current project conventions; verify the requested behavior with framework-appropriate tests.

For task-specific technical depth, read [the attributed source guide](references/web-backend-django/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Django Security (`web-backend-django-security`)

Inspect Python, framework, validation, database, and test versions before choosing APIs. Implement typed boundaries and explicit error handling using the current project conventions; verify the requested behavior with framework-appropriate tests.

For task-specific technical depth, read [the attributed source guide](references/web-backend-django-security/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Django Tdd (`web-backend-django-tdd`)

Inspect Python, framework, validation, database, and test versions before choosing APIs. Implement typed boundaries and explicit error handling using the current project conventions; verify the requested behavior with framework-appropriate tests.

For task-specific technical depth, read [the attributed source guide](references/web-backend-django-tdd/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Django Verification (`web-backend-django-verification`)

Inspect Python, framework, validation, database, and test versions before choosing APIs. Implement typed boundaries and explicit error handling using the current project conventions; verify the requested behavior with framework-appropriate tests.

For task-specific technical depth, read [the attributed source guide](references/web-backend-django-verification/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Nestjs Patterns (`web-backend-nestjs-patterns`)

Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.

For task-specific technical depth, read [the attributed source guide](references/web-backend-nestjs-patterns/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Springboot Patterns (`web-backend-springboot-patterns`)

Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.

For task-specific technical depth, read [the attributed source guide](references/web-backend-springboot-patterns/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Springboot Security (`web-backend-springboot-security`)

Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.

For task-specific technical depth, read [the attributed source guide](references/web-backend-springboot-security/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Springboot Tdd (`web-backend-springboot-tdd`)

Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.

For task-specific technical depth, read [the attributed source guide](references/web-backend-springboot-tdd/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Springboot Verification (`web-backend-springboot-verification`)

Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.

For task-specific technical depth, read [the attributed source guide](references/web-backend-springboot-verification/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Golang Patterns (`web-backend-golang-patterns`)

Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.

For task-specific technical depth, read [the attributed source guide](references/web-backend-golang-patterns/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Golang Testing (`web-backend-golang-testing`)

Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.

For task-specific technical depth, read [the attributed source guide](references/web-backend-golang-testing/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Laravel Patterns (`web-backend-laravel-patterns`)

Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.

For task-specific technical depth, read [the attributed source guide](references/web-backend-laravel-patterns/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Laravel Security (`web-backend-laravel-security`)

Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.

For task-specific technical depth, read [the attributed source guide](references/web-backend-laravel-security/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Laravel Tdd (`web-backend-laravel-tdd`)

Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.

For task-specific technical depth, read [the attributed source guide](references/web-backend-laravel-tdd/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Laravel Verification (`web-backend-laravel-verification`)

Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.

For task-specific technical depth, read [the attributed source guide](references/web-backend-laravel-verification/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Supabase (`web-backend-supabase`)

Inspect the actual database or cache topology, client lifecycle, access controls, query workload, and operational constraints. Verify consistency, expiry, isolation, and failure behavior with representative local cases; keep credentials and sensitive data out of logs.

For task-specific technical depth, read [the attributed source guide](references/web-backend-supabase/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Redis Core (`web-backend-redis-core`)

Inspect the actual database or cache topology, client lifecycle, access controls, query workload, and operational constraints. Verify consistency, expiry, isolation, and failure behavior with representative local cases; keep credentials and sensitive data out of logs.

For task-specific technical depth, read [the attributed source guide](references/web-backend-redis-core/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Redis Connections (`web-backend-redis-connections`)

Inspect the actual database or cache topology, client lifecycle, access controls, query workload, and operational constraints. Verify consistency, expiry, isolation, and failure behavior with representative local cases; keep credentials and sensitive data out of logs.

For task-specific technical depth, read [the attributed source guide](references/web-backend-redis-connections/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Redis Security (`web-backend-redis-security`)

Inspect the actual database or cache topology, client lifecycle, access controls, query workload, and operational constraints. Verify consistency, expiry, isolation, and failure behavior with representative local cases; keep credentials and sensitive data out of logs.

For task-specific technical depth, read [the attributed source guide](references/web-backend-redis-security/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Redis Observability (`web-backend-redis-observability`)

Inspect the actual database or cache topology, client lifecycle, access controls, query workload, and operational constraints. Verify consistency, expiry, isolation, and failure behavior with representative local cases; keep credentials and sensitive data out of logs.

For task-specific technical depth, read [the attributed source guide](references/web-backend-redis-observability/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Redis Search (`web-backend-redis-search`)

Inspect the actual database or cache topology, client lifecycle, access controls, query workload, and operational constraints. Verify consistency, expiry, isolation, and failure behavior with representative local cases; keep credentials and sensitive data out of logs.

For task-specific technical depth, read [the attributed source guide](references/web-backend-redis-search/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Redis Semantic Cache (`web-backend-redis-semantic-cache`)

Inspect the actual database or cache topology, client lifecycle, access controls, query workload, and operational constraints. Verify consistency, expiry, isolation, and failure behavior with representative local cases; keep credentials and sensitive data out of logs.

For task-specific technical depth, read [the attributed source guide](references/web-backend-redis-semantic-cache/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Vercel Optimize (`web-backend-vercel-optimize`)

Inspect the selected platform's deployment configuration, runtime limits, bindings, and existing observability. Use version-compatible APIs, validate locally, and state which deployment or production checks remain unperformed.

For task-specific technical depth, read [the attributed source guide](references/web-backend-vercel-optimize/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Cloudflare (`web-backend-cloudflare`)

Inspect the selected platform's deployment configuration, runtime limits, bindings, and existing observability. Use version-compatible APIs, validate locally, and state which deployment or production checks remain unperformed.

For task-specific technical depth, read [the attributed source guide](references/web-backend-cloudflare/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Workers Best Practices (`web-backend-workers-best-practices`)

Inspect the selected platform's deployment configuration, runtime limits, bindings, and existing observability. Use version-compatible APIs, validate locally, and state which deployment or production checks remain unperformed.

For task-specific technical depth, read [the attributed source guide](references/web-backend-workers-best-practices/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Wrangler (`web-backend-wrangler`)

Inspect the selected platform's deployment configuration, runtime limits, bindings, and existing observability. Use version-compatible APIs, validate locally, and state which deployment or production checks remain unperformed.

For task-specific technical depth, read [the attributed source guide](references/web-backend-wrangler/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Durable Objects (`web-backend-durable-objects`)

Inspect the selected platform's deployment configuration, runtime limits, bindings, and existing observability. Use version-compatible APIs, validate locally, and state which deployment or production checks remain unperformed.

For task-specific technical depth, read [the attributed source guide](references/web-backend-durable-objects/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Workers Profiling (`web-backend-workers-profiling`)

Inspect the selected platform's deployment configuration, runtime limits, bindings, and existing observability. Use version-compatible APIs, validate locally, and state which deployment or production checks remain unperformed.

For task-specific technical depth, read [the attributed source guide](references/web-backend-workers-profiling/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands.

### GNCore Backend Workflow (`web-backend`)

Trace the request through routing, validation, authentication, domain rules, persistence, background work, and observability as applicable. Select only the matching stack and the specialist skills needed for the request. Implement the scoped service behavior and verify its success, failure, and permission paths. Use existing infrastructure and interfaces unless the user requests a change.

### GNCore Backend Code Quality (`web-backend-codequality`)

Inspect a representative request or job path before refactoring. Check validation at boundaries, authorization at sensitive operations, ownership of transactions and state, cancellation and timeout behavior, and error propagation. Prefer clear interfaces and explicit invariants over generic abstraction layers. Make a focused improvement and verify relevant observable behavior; use the code quality, review, contract, or stack workflow that addresses the actual problem.

### GNCore Backend Security (`web-backend-security`)

Trace untrusted input and identity through each sensitive operation. Check object-level authorization, injection-safe queries, output handling, session and CSRF controls where relevant, and redacted failures. Reproduce concrete issues locally and verify allowed and denied cases after fixing them. Distinguish a scoped review from a claim that the whole service is secure.

### GNCore Backend Observability (`web-backend-observability`)

Identify service entrypoints, external calls, background jobs, and meaningful failure boundaries. Reuse existing telemetry conventions, propagate correlation context, redact sensitive values, and bound label cardinality. Verify a representative success and failure path emits useful signals. Use Sentry-specific workflows only for Sentry projects; separate local verification from evidence from a connected production system.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [wshobson/agents / nodejs-backend-patterns](research/wshobson-agents-nodejs-backend-patterns/GUIDE.md): MIT.
- [wshobson/agents / architecture-patterns](research/wshobson-agents-architecture-patterns/GUIDE.md): MIT.
- [wshobson/agents / dotnet-backend-patterns](research/wshobson-agents-dotnet-backend-patterns/GUIDE.md): MIT.
- [affaan-m/ecc / backend-patterns](research/affaan-m-ecc-backend-patterns/GUIDE.md): MIT.
- [affaan-m/ecc / springboot-patterns](research/affaan-m-ecc-springboot-patterns/GUIDE.md): MIT.
- [affaan-m/ecc / nestjs-patterns](research/affaan-m-ecc-nestjs-patterns/GUIDE.md): MIT.
- [vercel/vercel-plugin / create-a-backend](research/vercel-vercel-plugin-create-a-backend/GUIDE.md): Apache-2.0.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
