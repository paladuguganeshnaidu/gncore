# Source and modifications

GNCore entrypoint: web-front-shadcn.

Original: [shadcn/ui / shadcn](https://github.com/shadcn/ui/blob/96da9cc7f1aa10580a3741664e2a77c721206c00/skills/shadcn/SKILL.md).

Pinned revision: `96da9cc7f1aa10580a3741664e2a77c721206c00`.

The upstream instructions are preserved in `UPSTREAM.md`. Supporting files and supplied license notices are retained. Upstream metadata:

```json
{
  "name": "shadcn",
  "description": "Manages shadcn components and projects — adding, searching, fixing, debugging, styling, and composing UI, including chat interfaces. Provides project context, component docs, and usage examples. Applies when working with shadcn/ui, component registries, presets, --preset codes, or any project with a components.json file. Also triggers for \"shadcn init\", \"create an app with --preset\", \"switch to --preset\", and for building a design system or applying a DESIGN.md or brand spec to shadcn/ui.",
  "user-invocable": false,
  "allowed-tools": "Bash(npx shadcn@latest *), Bash(pnpm dlx shadcn@latest *), Bash(bunx --bun shadcn@latest *)"
}
```

GNCore changes: a new name, focused discovery description, web-specific workflow, progressive reference loading, and portable path guidance. The upstream authors retain authorship of their contributions; GNCore branding does not change their licenses. Frontmatter declarations and bundled license text may differ; preserve both when redistributing.
