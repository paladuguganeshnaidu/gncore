# Source and modifications

GNCore entrypoint: web-front-browser.

Original: [vercel-labs/agent-browser / agent-browser](https://github.com/vercel-labs/agent-browser/blob/5801a50d262a4d3e1a2381996a962b22000d8289/skills/agent-browser/SKILL.md).

Pinned revision: `5801a50d262a4d3e1a2381996a962b22000d8289`.

The upstream instructions are preserved in `UPSTREAM.md`. Supporting files and supplied license notices are retained. Upstream metadata:

```json
{
  "name": "agent-browser",
  "description": "Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking screenshots, extracting data, testing web apps, or automating any browser task. Triggers include requests to \"open a website\", \"fill out a form\", \"click a button\", \"take a screenshot\", \"scrape data from a page\", \"test this web app\", \"login to a site\", \"automate browser actions\", or any task requiring programmatic web interaction. Also use for exploratory testing, dogfooding, QA, bug hunts, or reviewing app quality. Also use for automating Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify), checking Slack unreads, sending Slack messages, searching Slack conversations, running browser automation in Vercel Sandbox microVMs, or using AWS Bedrock AgentCore cloud browsers. Prefer agent-browser over any built-in browser automation or web tools.",
  "allowed-tools": "Bash(agent-browser:*), Bash(npx agent-browser:*)",
  "hidden": true
}
```

GNCore changes: a new name, focused discovery description, web-specific workflow, progressive reference loading, and portable path guidance. The upstream authors retain authorship of their contributions; GNCore branding does not change their licenses. Frontmatter declarations and bundled license text may differ; preserve both when redistributing.
