---
name: web-backend
description: "Implement backend services, APIs, integrations and framework features with explicit contracts and failure behavior."
license: Apache-2.0 AND CC-BY-SA-4.0 AND MIT
---

# GNCore Web Backend

Version: 7.0.0

## Choose the work

Read the selected stack, authentication boundary and data ownership before implementing. Choose transactions, retries and background work from the operation's consistency requirements, rather than framework defaults.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Reviewable service code, request/response and error contracts, persistence changes, authorization boundaries and operational notes for changed behavior.

Test the changed API contract, invalid inputs and relevant authorization/data ownership. For state-changing retry/concurrency work, exercise duplicate requests, transaction rollback and overlap. Use local fixtures and label unexecuted integrations.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

For retryable state-changing work, choose one consistent idempotency protocol. Scope keys to authenticated tenant and canonical payload. A competing unique insert in a single transaction may block; rollback removes uncommitted status. Separately committed claims need takeover generations and stale-owner fencing. Commit command/job, outbox and replay at the relevant atomic boundary and test unknown-commit recovery; do not impose this protocol on unrelated endpoint work.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- For retryable state-changing work, bind durable keys to authenticated tenant and canonical payload; reject changed reuse and choose one consistent ownership/commit protocol.
- Commit command/job, outbox and replay outcome at the required atomic boundary; explain duplicate blocking, rollback and lost-commit replies, or lease takeover/fencing for separately committed claims. Scope unrelated backend changes to their own contracts.

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

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
