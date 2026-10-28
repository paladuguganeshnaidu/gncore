# Source and modifications

GNCore adaptation of [affaan-m/ecc / product-lens](https://github.com/affaan-m/ecc/blob/25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b/skills/product-lens/SKILL.md).

Revision: `25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b`.

Upstream metadata:

```json
{
  "name": "product-lens",
  "description": "Validate the why before building through four product diagnostics — a YC-style product diagnostic that produces PRODUCT-BRIEF.md with a go/no-go recommendation, a founder review scoring product-market-fit signals, a user journey audit measuring time-to-value, and ICE feature prioritization. Use when pressure-testing product direction, choosing between features, sanity-checking a launch, or converting a vague idea into a product brief.",
  "metadata": {
    "origin": "ECC"
  }
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: See retained upstream notices and metadata. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
