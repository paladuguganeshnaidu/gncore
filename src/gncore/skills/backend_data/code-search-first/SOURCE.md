# Source and modifications

GNCore adaptation of [affaan-m/ecc / search-first](https://github.com/affaan-m/ecc/blob/25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b/skills/search-first/SKILL.md).

Revision: `25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b`.

Upstream metadata:

```json
{
  "name": "search-first",
  "description": "Research-before-coding workflow: search npm/PyPI, MCP servers, skills, and GitHub for existing tools before writing custom code, then adopt, extend, or build. Launches the researcher agent for non-trivial needs. Use when starting a feature, adding a dependency or integration, or about to write a utility that may already exist.",
  "metadata": {
    "origin": "ECC"
  }
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: See retained upstream notices and metadata. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
