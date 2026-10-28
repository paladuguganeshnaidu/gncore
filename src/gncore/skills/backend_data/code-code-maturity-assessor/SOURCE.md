# Source and modifications

GNCore adaptation of [trailofbits/skills / code-maturity-assessor](https://github.com/trailofbits/skills/blob/bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md).

Revision: `bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3`.

Upstream metadata:

```json
{
  "name": "code-maturity-assessor",
  "description": "Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing, then produces a scorecard with evidence-based ratings and a priority-ordered roadmap. Use when assessing or scoring the maturity of a smart contract or blockchain codebase, producing a maturity scorecard or evaluation, or judging how mature, well-tested, or well-documented such a project is against a rubric."
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: CC-BY-SA-4.0. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
