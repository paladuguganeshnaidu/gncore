# Security policy — website-builder-elite

This file governs the **framework itself** (the prompts in `skills/`, `agents/`, `context/`, `templates/`) — not the security posture of any application this framework is used to build. For the latter, see `skills/10-security.md`, which is the gate every generated codebase must pass.

## Scope: what counts as a reportable framework defect

A reportable defect is anything in this repository's skill files, agent definitions, or templates that would cause Claude (or another model following this framework) to **produce insecure output** or **skip a security check it claims to perform**. Examples:

- A skill's process or checklist that omits a check `10-security.md` claims to cover (e.g., an injection class, an auth failure mode).
- Wording anywhere in `skills/` that could be read as license to ship an unresolved Critical/High finding without the explicit user risk-acceptance `10-security.md` requires.
- A template or example that itself demonstrates an insecure pattern (hardcoded secrets, unparameterized queries, disabled certificate validation, etc.) — the framework should never model the mistake it tells the Security Engineer role to catch.
- A gap between what a Quality Gate claims to verify and what the process steps above it actually instruct the model to check.

This is not the place to report a security bug in a *specific website* an instance of this framework built — that's a bug in that project's own repository, triaged there via `10-security.md`/`14-debug.md`, not here.

## How to report

Open an issue in this repository describing the specific file, line(s), and the concrete insecure output or skipped check the wording would produce. If the finding is sensitive enough that a public issue would itself be an uplift (unlikely for a prompt-only repo, but possible if a template embeds a real credential or a working exploit chain by mistake), mark it clearly as sensitive in the title and a maintainer will follow up privately before any public disclosure.

## Response-time commitment

- **Acknowledgment:** within 5 business days of the issue being opened.
- **Triage (confirmed defect vs. not applicable):** within 10 business days.
- **Fix or documented mitigation merged:** within 30 days for a confirmed defect that could cause insecure output in generated code; no fixed SLA for lower-severity documentation/clarity issues, but they are not closed silently — they get a stated resolution or an explicit "won't fix, because" note, the same standard `10-security.md` holds generated findings to.

## Relationship to `skills/10-security.md`

`agents/AGENTS.md`'s Security Engineer row states that role cannot decide to ship a Critical/High finding unresolved, even if asked. That no-silent-waiver rule is defined and enforced in `skills/10-security.md`'s own "Stopping conditions" section for *generated projects*. This file is the equivalent commitment for defects *in the framework's own prompts* — the same principle, one level up.
