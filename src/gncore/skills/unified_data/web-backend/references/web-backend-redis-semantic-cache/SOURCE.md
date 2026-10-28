# Source and modifications

GNCore adaptation of [redis/agent-skills / redis-semantic-cache](https://github.com/redis/agent-skills/blob/a84871d065f398fed55e1633f66b66f731eb4e2b/skills/redis-semantic-cache/SKILL.md).

Revision: `a84871d065f398fed55e1633f66b66f731eb4e2b`.

Upstream metadata:

```json
{
  "name": "redis-semantic-cache",
  "description": "Redis LangCache guidance for semantic caching of LLM responses on Redis Cloud — calling search/set via the SDK or REST API, tuning the similarity threshold, separating caches per task type, and filtering with custom attributes. Use when caching LLM completions or RAG answers to cut API cost and latency, building a cache-aside layer in front of OpenAI / Anthropic / etc., tuning hit rate vs precision, or splitting one app's LLM workloads into multiple LangCache caches.",
  "license": "MIT",
  "metadata": {
    "author": "Redis, Inc.",
    "version": "0.1.0"
  }
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: See retained upstream notices and metadata. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
