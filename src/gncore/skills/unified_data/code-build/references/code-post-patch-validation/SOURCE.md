# Source and modifications

GNCore adaptation of [trailofbits/skills / post-patch-validation](https://github.com/trailofbits/skills/blob/bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3/plugins/post-patch-validation/skills/post-patch-validation/SKILL.md).

Revision: `bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3`.

Upstream metadata:

```json
{
  "name": "post-patch-validation",
  "description": "Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, root-cause variants, behavior preservation, regressions, and newly introduced security failures. Use after a patch exists and before accepting, merging, or reporting it as fixed; also use when an AI-generated patch, remediation commit, pull request, or proposed upstream fix needs adversarial post-patch validation across any language.\n",
  "allowed-tools": "Read Write Edit Grep Glob Bash Workflow"
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: CC-BY-SA-4.0. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
