# Source and modifications

GNCore adaptation of [affaan-m/ecc / python-patterns](https://github.com/affaan-m/ecc/blob/25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b/skills/python-patterns/SKILL.md).

Revision: `25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b`.

Upstream metadata:

```json
{
  "name": "python-patterns",
  "description": "Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintainable Python applications. Use when writing or reviewing Python code and idiomatic structure, typing, or PEP 8 is in question.",
  "metadata": {
    "origin": "ECC"
  }
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: See retained upstream notices and metadata. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
