---
name: web-backend
description: "Implement backend services, APIs, integrations and framework features with explicit contracts and failure behavior."
license: Apache-2.0 AND CC-BY-SA-4.0 AND MIT
---

# GNCore Web Backend

Version: 7.0.0rc1

## Choose the work

Read the selected stack, authentication boundary and data ownership before implementing. Choose transactions, retries and background work from the operation's consistency requirements, rather than framework defaults.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Reviewable service code, request/response and error contracts, persistence changes, authorization boundaries and operational notes for changed behavior.

Test invalid input, tenant/owner isolation, duplicate requests, transaction rollback and relevant concurrent access. Use local fixtures; label unexecuted external integrations.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

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
| `web-development` | Plan and implement a focused web feature using the repository's existing framework, patterns, and tests. |
| `seo-audit` | Improve technical and content discoverability using crawlable structure and verifiable search metadata. |

## Focused procedures

### GNCore Patterns (`web-backend-patterns`)

Trace request, application/domain and persistence boundaries in the existing service. Keep business invariants independent of transport details, make failure ownership explicit and introduce a new layer only when it simplifies a real change. Verify one complete success and failure path through the chosen boundaries.

For relevant technical detail, read [the attributed source guide](references/web-backend-patterns/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Api Design (`web-backend-api-design`)

Specify resources, schemas, status/error codes, authorization, pagination and retry semantics from the consumer's task. Test invalid input, missing/forbidden resources and compatibility with current clients; do not let framework serialization defaults silently define a public contract.

For relevant technical detail, read [the attributed source guide](references/web-backend-api-design/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Hexagonal Architecture (`web-backend-hexagonal-architecture`)

Identify domain invariants and external dependencies, then define narrow ports around the dependencies that need substitution. Keep framework/ORM types in adapters, test the domain through ports and one real adapter integration, and avoid wrapping every internal function in an interface.

For relevant technical detail, read [the attributed source guide](references/web-backend-hexagonal-architecture/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Error Handling (`web-backend-error-handling`)

Classify validation, authorization, conflict, transient dependency and unexpected errors. Preserve diagnostic causes internally while returning stable public errors without secrets. Test exception-to-response mapping, transaction rollback and whether a retry can duplicate the side effect.

For relevant technical detail, read [the attributed source guide](references/web-backend-error-handling/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Contract First (`web-backend-contract-first`)

Write request/response and error examples before implementation, including absence, invalid values and authorization. Validate the schema and consumer expectations against existing versions, then implement and run contract tests so documentation and runtime behavior agree.

For relevant technical detail, read [the attributed source guide](references/web-backend-contract-first/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Api Connector Builder (`web-backend-api-connector-builder`)

Inspect the external API's authentication, pagination, rate limits and versioned schema. Implement a typed boundary with bounded retries only for safe operations, timeouts and redacted diagnostics. Replay recorded/synthetic success, malformed response, pagination and quota/error fixtures before a live call.

For relevant technical detail, read [the attributed source guide](references/web-backend-api-connector-builder/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Spec To Code Compliance (`web-backend-spec-to-code-compliance`)

Turn supplied normative requirements into traceable code paths and executable acceptance cases. Distinguish MUST behavior from optional guidance and missing specification. Report each mismatch with source location and observed behavior instead of treating a passing schema check as full compliance.

For relevant technical detail, read [the attributed source guide](references/web-backend-spec-to-code-compliance/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Supabase Postgres Best Practices (`web-backend-supabase-postgres-best-practices`)

Inspect Postgres access patterns and Supabase role/RLS boundaries. Parameterize queries, encode integrity in constraints and inspect plans before indexing. Verify authenticated and cross-tenant negative cases using the actual role model; a privileged service key must not stand in for user-policy testing.

For relevant technical detail, read [the attributed source guide](references/web-backend-supabase-postgres-best-practices/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Postgres Patterns (`web-backend-postgres-patterns`)

Choose transaction isolation, constraints and indexes from the invariant and workload. Reproduce null/uniqueness behavior, lock conflicts and the query plan in a local Postgres fixture. Keep connection lifetime and prepared-query behavior consistent with the selected driver/pool.

For relevant technical detail, read [the attributed source guide](references/web-backend-postgres-patterns/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Database Migrations (`web-backend-database-migrations`)

Use expand/backfill/validate/contract sequencing for mixed-version deployments. Make backfills bounded and restartable, state the policy for unknown values and rehearse lock/failure behavior. Separate a reversible schema change from data changes that cannot be automatically undone.

For relevant technical detail, read [the attributed source guide](references/web-backend-database-migrations/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Benchmark (`web-backend-benchmark`)

Define workload, environment, warmup, concurrency and success thresholds before measuring. Retain raw latency/error/throughput results and compare identical request/data conditions. Separate benchmark setup cost from the measured operation and avoid claiming production capacity from a local microbenchmark.

For relevant technical detail, read [the attributed source guide](references/web-backend-benchmark/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Benchmark Optimization Loop (`web-backend-benchmark-optimization-loop`)

Capture a reproducible baseline, profile the dominant cost, make one targeted change and compare both correctness and distributions on the same workload. Keep raw evidence and stop if improvement is within noise or a correctness/resource tradeoff is unacceptable.

For relevant technical detail, read [the attributed source guide](references/web-backend-benchmark-optimization-loop/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Latency Critical Systems (`web-backend-latency-critical-systems`)

Allocate an end-to-end latency budget and measure dependency, queue and serialization contributions, including tails and errors. Bound queues, deadlines and cancellation; test overload/recovery rather than optimizing only successful warm requests. Explain the conditions under which the target was measured.

For relevant technical detail, read [the attributed source guide](references/web-backend-latency-critical-systems/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Redis Patterns (`web-backend-redis-patterns`)

Choose Redis key structure, TTL, invalidation and atomicity from the cache/state contract. Define cache-miss and unavailable-cache behavior and test stale data, expiry, concurrent updates and hot-key effects. Do not turn a disposable cache into an undocumented source of truth.

For relevant technical detail, read [the attributed source guide](references/web-backend-redis-patterns/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Deployment Patterns (`web-backend-deployment-patterns`)

Prepare a staged rollout with version compatibility, meaningful health signals and rollback criteria. Validate configuration and migration order in a safe environment; keep code preparation, deployment execution and verified live traffic separate in the report.

For relevant technical detail, read [the attributed source guide](references/web-backend-deployment-patterns/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Docker (`web-backend-docker`)

Use the repository's supported base/runtime images, a minimal build context and a non-secret runtime configuration. Check multi-stage output, user/file permissions, health/startup/shutdown and resource limits. Build and run the image locally before claiming container readiness.

For relevant technical detail, read [the attributed source guide](references/web-backend-docker/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Github Ops (`web-backend-github-ops`)

Inspect workflow triggers, permissions, dependency/cache boundaries and required checks. Restrict credentials to the job that needs them and preserve actionable failure artifacts. Exercise the workflow commands locally and report remote CI separately; do not change branch rules or publish artifacts without scope authorization.

For relevant technical detail, read [the attributed source guide](references/web-backend-github-ops/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Production Audit (`web-backend-production-audit`)

Review an explicitly scoped service's configuration, dependency boundaries, resource/timeout controls, observability and recovery evidence. Link findings to reachable code/configuration and impact. Use read-only/local checks unless production access/actions are authorized; do not certify readiness from a checklist alone.

For relevant technical detail, read [the attributed source guide](references/web-backend-production-audit/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Agentic Engineering (`web-backend-agentic-engineering`)

Define the agent's task, allowed tools, state transitions and bounded execution budget. Validate tool arguments/results and isolate side effects from model suggestions. Test tool failure, hostile retrieved instructions, retry and budget exhaustion with fixtures before introducing live integrations.

For relevant technical detail, read [the attributed source guide](references/web-backend-agentic-engineering/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Mcp Server Patterns (`web-backend-mcp-server-patterns`)

Inspect the selected MCP protocol/SDK version and model resources, tools and prompts with explicit schemas and authorization. Keep transport/session lifecycle separate from domain behavior. Test invalid tool inputs, canceled requests and reconnect/cleanup paths with an available protocol client.

For relevant technical detail, read [the attributed source guide](references/web-backend-mcp-server-patterns/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Agent Eval (`web-backend-agent-eval`)

Build representative task and failure cases, define objective success and human-review rubrics, and record model/tool/configuration versions. Compare changes on the same cases and separate structure/trace validity from semantic task success. Mark unrun provider or subjective evaluations honestly.

For relevant technical detail, read [the attributed source guide](references/web-backend-agent-eval/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Cost Aware Llm Pipeline (`web-backend-cost-aware-llm-pipeline`)

Record per-request token/tool budgets, latency requirements and acceptable fallback behavior. Cache only with correct identity/freshness boundaries and route simpler work to appropriate models without weakening output validation. Measure actual provider usage when authorized; otherwise use explicit cost assumptions.

For relevant technical detail, read [the attributed source guide](references/web-backend-cost-aware-llm-pipeline/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Mcp Builder (`web-backend-mcp-builder`)

Start from the consumer operation, define small typed MCP tools and useful errors, and implement the selected SDK's lifecycle correctly. Verify schemas, authentication/authority propagation and a real local client round-trip. Publishing a server or exposing credentials is a separate authorized action.

For relevant technical detail, read [the attributed source guide](references/web-backend-mcp-builder/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Agents Sdk (`web-backend-agents-sdk`)

Confirm which Agents SDK and runtime the project actually uses. Implement explicit state/tool contracts, bounded orchestration and error handling with that version's APIs. Test deterministic tool boundaries and resume/cancellation before enabling hosted models or persistent external state.

For relevant technical detail, read [the attributed source guide](references/web-backend-agents-sdk/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Building Ai Agent On Cloudflare (`web-backend-building-ai-agent-on-cloudflare`)

Inspect the selected Workers and Agents SDK versions, Wrangler configuration, bindings, authentication, state storage, and model provider. Implement the requested agent interaction with typed tool inputs, bounded retries, cancellation, and durable state only where needed. Keep provider credentials in the platform secret mechanism. Verify a useful task, a tool error, and an unauthorized request locally; prepare deployment instructions without claiming a deployed service unless deployment was requested and verified.

### GNCore Fastapi (`web-backend-fastapi`)

Inspect the installed fastapi version and existing application conventions, especially typed request/response models, dependency overrides, generated OpenAPI and async I/O boundaries. Implement a complete scoped feature in the existing application without introducing an unrelated framework migration.

For relevant technical detail, read [the attributed source guide](references/web-backend-fastapi/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Fastapi Patterns (`web-backend-fastapi-patterns`)

Inspect the installed fastapi version and existing application conventions, especially typed request/response models, dependency overrides, generated OpenAPI and async I/O boundaries. Apply the project's conventions to the requested feature, keeping transport, domain invariants and persistence responsibilities clear.

For relevant technical detail, read [the attributed source guide](references/web-backend-fastapi-patterns/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Django (`web-backend-django`)

Inspect the installed django version and existing application conventions, especially ORM constraints/transactions, migrations, queryset ownership, middleware and server-side permissions. Implement a complete scoped feature in the existing application without introducing an unrelated framework migration.

For relevant technical detail, read [the attributed source guide](references/web-backend-django/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Django Security (`web-backend-django-security`)

Inspect the installed django version and existing application conventions, especially ORM constraints/transactions, migrations, queryset ownership, middleware and server-side permissions. Trace request identity and ownership through policy/guard checks, test cross-user access and inspect sensitive logging and configuration.

For relevant technical detail, read [the attributed source guide](references/web-backend-django-security/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Django Tdd (`web-backend-django-tdd`)

Inspect the installed django version and existing application conventions, especially ORM constraints/transactions, migrations, queryset ownership, middleware and server-side permissions. Write an observable failing request/domain regression, implement the smallest correct path and then refactor with integration evidence.

For relevant technical detail, read [the attributed source guide](references/web-backend-django-tdd/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Django Verification (`web-backend-django-verification`)

Inspect the installed django version and existing application conventions, especially ORM constraints/transactions, migrations, queryset ownership, middleware and server-side permissions. Run relevant tests, configuration/build checks and a local request round-trip; distinguish the prepared change from a deployed service.

For relevant technical detail, read [the attributed source guide](references/web-backend-django-verification/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Nestjs Patterns (`web-backend-nestjs-patterns`)

Inspect the installed nestjs version and existing application conventions, especially module/provider boundaries, validated DTOs, guards, exception filters and application lifecycle. Apply the project's conventions to the requested feature, keeping transport, domain invariants and persistence responsibilities clear.

For relevant technical detail, read [the attributed source guide](references/web-backend-nestjs-patterns/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Springboot Patterns (`web-backend-springboot-patterns`)

Inspect the installed springboot version and existing application conventions, especially service/transaction boundaries, validated request DTOs, security filters and persistence integration. Apply the project's conventions to the requested feature, keeping transport, domain invariants and persistence responsibilities clear.

For relevant technical detail, read [the attributed source guide](references/web-backend-springboot-patterns/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Springboot Security (`web-backend-springboot-security`)

Inspect the installed springboot version and existing application conventions, especially service/transaction boundaries, validated request DTOs, security filters and persistence integration. Trace request identity and ownership through policy/guard checks, test cross-user access and inspect sensitive logging and configuration.

For relevant technical detail, read [the attributed source guide](references/web-backend-springboot-security/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Springboot Tdd (`web-backend-springboot-tdd`)

Inspect the installed springboot version and existing application conventions, especially service/transaction boundaries, validated request DTOs, security filters and persistence integration. Write an observable failing request/domain regression, implement the smallest correct path and then refactor with integration evidence.

For relevant technical detail, read [the attributed source guide](references/web-backend-springboot-tdd/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Springboot Verification (`web-backend-springboot-verification`)

Inspect the installed springboot version and existing application conventions, especially service/transaction boundaries, validated request DTOs, security filters and persistence integration. Run relevant tests, configuration/build checks and a local request round-trip; distinguish the prepared change from a deployed service.

For relevant technical detail, read [the attributed source guide](references/web-backend-springboot-verification/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Golang Patterns (`web-backend-golang-patterns`)

Inspect the installed golang version and existing application conventions, especially context cancellation, error wrapping, goroutine lifetime, race checks and HTTP/database timeouts. Apply the project's conventions to the requested feature, keeping transport, domain invariants and persistence responsibilities clear.

For relevant technical detail, read [the attributed source guide](references/web-backend-golang-patterns/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Golang Testing (`web-backend-golang-testing`)

Inspect the installed golang version and existing application conventions, especially context cancellation, error wrapping, goroutine lifetime, race checks and HTTP/database timeouts. Use the native test tooling and a local/disposable fixture to exercise success, cancellation, invalid input and persistence failures.

For relevant technical detail, read [the attributed source guide](references/web-backend-golang-testing/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Laravel Patterns (`web-backend-laravel-patterns`)

Inspect the installed laravel version and existing application conventions, especially form validation, policies, Eloquent transactions, migrations, queues and lifecycle configuration. Apply the project's conventions to the requested feature, keeping transport, domain invariants and persistence responsibilities clear.

For relevant technical detail, read [the attributed source guide](references/web-backend-laravel-patterns/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Laravel Security (`web-backend-laravel-security`)

Inspect the installed laravel version and existing application conventions, especially form validation, policies, Eloquent transactions, migrations, queues and lifecycle configuration. Trace request identity and ownership through policy/guard checks, test cross-user access and inspect sensitive logging and configuration.

For relevant technical detail, read [the attributed source guide](references/web-backend-laravel-security/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Laravel Tdd (`web-backend-laravel-tdd`)

Inspect the installed laravel version and existing application conventions, especially form validation, policies, Eloquent transactions, migrations, queues and lifecycle configuration. Write an observable failing request/domain regression, implement the smallest correct path and then refactor with integration evidence.

For relevant technical detail, read [the attributed source guide](references/web-backend-laravel-tdd/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Laravel Verification (`web-backend-laravel-verification`)

Inspect the installed laravel version and existing application conventions, especially form validation, policies, Eloquent transactions, migrations, queues and lifecycle configuration. Run relevant tests, configuration/build checks and a local request round-trip; distinguish the prepared change from a deployed service.

For relevant technical detail, read [the attributed source guide](references/web-backend-laravel-verification/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Supabase (`web-backend-supabase`)

Inspect project/client versions, authenticated roles, RLS, schema migrations and privileged-key boundaries. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-supabase/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Redis Core (`web-backend-redis-core`)

Inspect key types, TTLs, atomic commands, cache versus durable-state ownership and unavailable-cache behavior. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-redis-core/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Redis Connections (`web-backend-redis-connections`)

Inspect client/pool limits, timeouts, reconnect behavior, TLS and cancellation during network failure. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-redis-connections/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Redis Security (`web-backend-redis-security`)

Inspect authentication/ACL command scope, key isolation, TLS and secret-free diagnostics. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-redis-security/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Redis Observability (`web-backend-redis-observability`)

Inspect latency, hit/miss and eviction metrics with low-cardinality labels and actionable saturation signals. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-redis-observability/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Redis Search (`web-backend-redis-search`)

Inspect index schema, query escaping, update/refresh behavior and relevance against a known document fixture. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-redis-search/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Redis Semantic Cache (`web-backend-redis-semantic-cache`)

Inspect embedding/version identity, tenant isolation, freshness, similarity threshold and false-hit evaluation. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-redis-semantic-cache/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Vercel Optimize (`web-backend-vercel-optimize`)

Inspect actual framework/build output, client/server boundaries, bundle costs, caching and measured page behavior. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-vercel-optimize/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Cloudflare (`web-backend-cloudflare`)

Inspect Workers runtime limits, bindings, request/response lifecycle and selected deployment configuration. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-cloudflare/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Workers Best Practices (`web-backend-workers-best-practices`)

Inspect runtime compatibility, async lifetime, binding usage, caching semantics and bounded resource consumption. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-workers-best-practices/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Wrangler (`web-backend-wrangler`)

Inspect installed Wrangler version, configuration schema, environment/binding names and local versus production command effects. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-wrangler/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Durable Objects (`web-backend-durable-objects`)

Inspect object identity/routing, serialized state operations, storage consistency, reconnect and eviction behavior. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-durable-objects/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Workers Profiling (`web-backend-workers-profiling`)

Inspect representative workload, CPU/wall-time distinction, runtime limits and before/after profile evidence. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

For relevant technical detail, read [the attributed source guide](references/web-backend-workers-profiling/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Backend Workflow (`web-backend`)

Trace the request through routing, validation, authentication, domain rules, persistence, background work, and observability as applicable. Select only the matching stack and the specialist skills needed for the request. Implement the scoped service behavior and verify its success, failure, and permission paths. Use existing infrastructure and interfaces unless the user requests a change.

### GNCore Backend Code Quality (`web-backend-codequality`)

Inspect a representative request or job path before refactoring. Check validation at boundaries, authorization at sensitive operations, ownership of transactions and state, cancellation and timeout behavior, and error propagation. Prefer clear interfaces and explicit invariants over generic abstraction layers. Make a focused improvement and verify relevant observable behavior; use the code quality, review, contract, or stack workflow that addresses the actual problem.

### GNCore Backend Security (`web-backend-security`)

Trace untrusted input and identity through each sensitive operation. Check object-level authorization, injection-safe queries, output handling, session and CSRF controls where relevant, and redacted failures. Reproduce concrete issues locally and verify allowed and denied cases after fixing them. Distinguish a scoped review from a claim that the whole service is secure.

### Web Development (`web-development`)

Help implement the web development task the user describes. First inspect the existing app and identify the smallest relevant change. Follow its framework, architecture, accessibility, and security conventions. State assumptions when they affect the result. Change only files needed for the requested feature; do not rewrite unrelated pages, architecture, dependencies, or configuration. Ask before broad migrations or destructive changes. Summarize changed files and any checks performed.

### SEO Audit (`seo-audit`)

Inspect rendered HTML, indexability, canonical URLs, structured data, sitemap, redirects, and page performance. Fix concrete issues in the existing framework and preserve user-facing meaning. Validate structured data syntax and avoid keyword stuffing or fabricated claims. Search rankings cannot be guaranteed; distinguish technical checks from outcome estimates.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
