# Source and modifications

GNCore adaptation of [redis/agent-skills / redis-search](https://github.com/redis/agent-skills/blob/a84871d065f398fed55e1633f66b66f731eb4e2b/skills/redis-search/SKILL.md).

Revision: `a84871d065f398fed55e1633f66b66f731eb4e2b`.

Upstream metadata:

```json
{
  "name": "redis-search",
  "description": "Redis Search guidance covering FT.CREATE schema design, field type selection (TEXT, TAG, NUMERIC, GEO, GEOSHAPE, VECTOR, JSON path), DIALECT 2 query syntax, FT.SEARCH / FT.AGGREGATE / FT.HYBRID command selection, vector similarity with HNSW or FLAT, hybrid retrieval combining lexical and vector ranking, RAG pipelines, zero-downtime index updates via aliases, and debugging with FT.PROFILE and FT.EXPLAIN. Use when defining a search index on Hash or JSON documents, writing FT.SEARCH queries with filters, sorting, aggregation, or vector KNN, tuning HNSW parameters, building a RAG retrieval pipeline, or troubleshooting slow or empty search results.",
  "license": "MIT",
  "metadata": {
    "author": "Redis, Inc.",
    "version": "1.0.0"
  }
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: See retained upstream notices and metadata. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
