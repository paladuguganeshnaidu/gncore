# Local verification — 2026-10-28

> Historical phase-one record. The developer-focused phase-two scope and current publication state are in [the phase-two release plan](PHASE2_RELEASE.md). This record does not describe the current active catalog.

## Reliability upgrade batch

The first implementation batch completes GN-01 and GN-02 and supplies the GN-03 pilot format and cases. The remaining roadmap items are tracked separately in [UPGRADE_PLAN.md](UPGRADE_PLAN.md).

| Check | Result |
| --- | --- |
| Full automated suite | 90 passed, 1 skipped |
| Installation tests after the final path-scanning refinement | 27 passed, 1 skipped |
| Pilot coverage and workflow references | 36 cases across 12 categories validated |
| Actual project installation | All 60 categories adopted with a retained backup; 5,716 tracked files intact, no missing, modified, or unmanaged files |
| Documentation lint | 23 files, zero issues |
| Planner regressions | Excluded fallbacks, negative motion, multiword styles, documented misspellings, precedence, and contradictions checked |
| Installation failure coverage | Unmanaged collisions, customized files, temporary-looking user filenames, stale resources, staging/switch failures, corrupt state, Unicode paths, actual process exit, concurrent edits, and recovery checked |

The skipped test requires creating a symlink, which is unavailable to this Windows account. The existing CI matrix remains responsible for runtime checks on supported Python versions and platforms. The evaluation corpus's complete agent tasks, browser/renderer checks, and subjective quality reviews have not been executed by the structural runner; they remain explicitly pending.

## Initial category rewrite

The GNCore 6 category rewrite was checked locally on Windows with Python 3.14.7.

| Check | Result |
| --- | --- |
| Full automated test suite | 35 passed |
| Frontend tests after the final constraint refinement | 16 passed |
| Primary skills / categories | 60 / 60 |
| Retained workflow procedures | 553 |
| Professional domains | 30, each retaining ten workflows |
| Skill-format validation | All 60 entrypoints passed in UTF-8 mode |
| Native Codex project discovery | 60 category skills |
| Resource comparison | 5,656 files matched across source, installed project copies, clean wheel, and portable ZIP |
| Distribution metadata | Wheel and source archive passed Twine checks |
| Runtime source checks | Compilation passed; 14 runtime files parsed with Python 3.10 syntax rules |
| Markdown and staged changes | Passed checks; preserved upstream formatting is excluded from whitespace rewriting |

The portable ZIP was exported from a clean installation of `gncore-6.0.0-py3-none-any.whl`, with the source checkout excluded from that import path. Its SHA-256 is `c6ee54098c05ef5cfa4d8c867b7d48ee962cf5fccaa5143bb4138aecc48416d9`.

The project migration backed up 167 managed legacy skill folders under ignored local storage before installing the 60 primary categories. Research covered all 60 categories, returned 426 distinct candidates, and downloaded 369 available snapshots. Unavailable sources and license/relevance exclusions are recorded in the source-research report.

These checks verify concrete software and packaging behavior. They do not certify every possible AI response, every upstream executable, subjective visual quality, or all professional-domain judgments. Platform-specific runtime matrices are configured in CI; this local report does not claim those remote runs passed. No package publishing tag was created by this task.
