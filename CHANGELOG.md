# Changelog

## 5.1.0

- Make `gncore export` install complete skills to `.agents/skills/` by default.
- Add `--specific` for selecting one skill and `--directory` for a custom install path.
- Keep ZIP export available through an explicit `--output` option.
- Include commands, examples, and permission guidance in generated `SKILL.md` files.

## 5.0.0

- Reframed GNCore as a portable skill catalog and prompt export tool.
- Removed application detection, adapters, installation and removal, MCP setup, persistent configuration, diagnostics, and backup/restore orchestration.
- Replaced application-target commands with focused catalog commands: list, search, show, export, and version.
- Added portable `SKILL.md` ZIP export for selected skills or the full catalog.
- This is a breaking change from 4.x: application-management APIs and commands are removed.

## 4.0.0

- Added 30 curated company and professional domain packs with 10 focused workflows each (300 added skills), including C-suite roles, Word, PDF, PowerPoint, spreadsheets, and broad business/technical operations.
- Added public `list_domains()` API and `gncore list domains` discovery command.
- Applied a shared inspect, plan, implement, test, fix, retest, and report contract with bounded completion criteria and evidence-based reporting.
- Added domain catalog integrity and CLI discovery coverage.
- Prepared package metadata and documentation for 4.0.0.

## 3.1.0

- Added focused skill collections for web engineering and design, machine learning, Python, data work, and testing.
- Added searchable skill catalog functions to the Python API and category browsing to the CLI.
- Added native VS Code Copilot and Google Antigravity skill installation with user and workspace scopes.
- Added native VS Code Codex/Claude, Claude Code, Codex CLI, and Gemini CLI skill targets plus ChatGPT upload ZIP export.
- Expanded the catalog with slash-invoked ML workflows and specialist skills across AI, data, cloud, security, mobile, product, research, and QA.
- Added shared native-folder ownership so uninstalling one agent target preserves skills still managed for another target.
- Added managed-file ownership checks and task-focused accuracy rules to the skill prompts.

## 3.0.0

- Replaced the workflow-engine design with a universal AI Skill Installer.
- Added typed adapter, installer, validator, backup, rollback, diagnostics, and configuration managers.
- Added built-in skills and adapter support for VS Code Chat, GitHub Copilot Chat, Claude Desktop, Claude Code, Cursor, Windsurf, Continue.dev, Gemini CLI, and OpenAI Codex CLI.
- Switched packaging to Hatchling and Python 3.10+.
- Added the new CLI surface: activate, deactivate, update, doctor, list, install, uninstall, backup, restore, validate, and version.
