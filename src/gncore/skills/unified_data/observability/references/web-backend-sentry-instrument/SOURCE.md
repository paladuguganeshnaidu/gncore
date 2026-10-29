# Source and modifications

GNCore adaptation of [getsentry/plugin-codex / sentry-instrument](https://github.com/getsentry/plugin-codex/blob/8832fafe9b061151b80c34e7752bc3553de9f68a/plugins/sentry/skills/sentry-instrument/SKILL.md).

Revision: `8832fafe9b061151b80c34e7752bc3553de9f68a`.

Upstream metadata:

```json
{
  "name": "sentry-instrument",
  "description": "Instrument an application with Sentry — detect the platform, install and initialize the SDK if needed, and wire up any signal — error monitoring, tracing/performance, logging, metrics, profiling, session replay, user feedback, cron check-ins, uptime monitors for the deployed app, and AI/LLM monitoring (agent runs, token cost, and conversations for OpenAI, Anthropic, Vercel AI, LangChain, Google GenAI, Pydantic AI, Laravel AI, Mastra, Eve, Flue, Pi Durable, the Cloudflare Agents SDK, and Workers AI). Use to add Sentry to a project or to capture more than errors.",
  "license": "Apache-2.0"
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: See retained upstream notices and metadata. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
