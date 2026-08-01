---
name: 06-scaffold
description: Generates the project skeleton — file structure, configs, tooling, empty modules matching architecture.md's boundaries — and proves it builds/installs cleanly before any feature code is written.
---

## Role
Backend Engineer + Frontend Engineer (joint pass — scaffolding spans both).

## Inputs
- `context/architecture.md`
- `context/design-system.md`

## Outputs
- The project skeleton on disk.
- `context/dependency-manifest.md`: every package, pinned version, and why (link to `research-notes.md` where relevant).
- `context/style-guide.md`: initialized with the conventions the scaffold establishes (naming, folder layout, import order).

## Process
1. Generate the file structure matching `architecture.md`'s module boundaries exactly — don't invent a different structure because it's more familiar.
2. Install pinned, current dependency versions (verified in `02-research.md` where version-sensitive). Never use an unpinned `latest`/`*` version range for anything security- or build-critical.
3. Wire up linting, formatting, type-checking, and a test runner from the start — these are not optional add-ons in `13-test.md`, they need to exist before `07-build.md` writes the first feature.
4. Generate a design-tokens file/config directly from `design-system.md` so `07-build.md` references tokens, not magic values.
5. Set up environment variable handling (`.env.example` with names only, never real values) for anything `08-integrate.md` will need.
6. **Prove the skeleton actually builds and installs with zero errors before declaring this stage done.** Run the install and build/dev commands for real.
7. Initialize the repo (see `19-git.md`) with the first commit.

## Quality Gate
- [ ] Project installs with zero errors.
- [ ] Project builds/runs with zero errors (empty state is fine — no features yet).
- [ ] Every dependency is pinned to a specific version and listed in `dependency-manifest.md`.
- [ ] Lint/format/type-check/test tooling is configured and runnable, even with nothing to check yet.
- [ ] `.env.example` exists with no real secret values.
- [ ] File structure matches `architecture.md`'s module boundaries.

## Stopping conditions
Do not proceed to `07-build.md` on a scaffold that doesn't build cleanly. If a chosen dependency fails to install/resolve, that's routed to `14-debug.md` immediately, not worked around silently with a different unreviewed package.

**Execution mode:** if the session has real shell/install access, this gate runs in Verified mode — the install/build commands are actually executed. If it does not, this gate runs in Reasoned mode — a static review of the generated configs, lockfiles, and scripts for internal consistency, with the limitation stated plainly rather than a claimed "builds with zero errors" that was never run. See `README.md`'s "Execution requirements" section.

## Handoff
```
STAGE: 06-scaffold
ROLE: Backend Engineer / Frontend Engineer
STATUS: pass | pass (reasoned, not executed)
ARTIFACT(S) WRITTEN: project skeleton, context/dependency-manifest.md, context/style-guide.md
GATE RESULT: <per checklist above>
ESCALATIONS: none
NEXT: 07-build
```
