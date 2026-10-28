# Source and modifications

GNCore adaptation of [trailofbits/skills / code-improver](https://github.com/trailofbits/skills/blob/bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3/plugins/code-improver/skills/code-improver/SKILL.md).

Revision: `bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3`.

Upstream metadata:

```json
{
  "name": "code-improver",
  "description": "Runs an autonomous review-and-fix improvement loop over any code target — a skill, plugin, module, or directory — using a reviewer the user names: any installed skill or agent. Keeps a cross-round findings ledger, escalates when fixes stop converging, and guards scope mechanically. Use when asked to 'improve this code until review passes', 'run an improvement loop with <reviewer>', or to iterate review-and-fix with a specific reviewer. For skills prefer the skill-improver entry; for a branch prefer pr-improver.",
  "argument-hint": "<TARGET_PATH> --reviewer <agent-or-skill-name> --scope <globs> [--max-rounds N]",
  "allowed-tools": "Bash Glob Read TaskOutput TaskStop Workflow"
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: CC-BY-SA-4.0. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
