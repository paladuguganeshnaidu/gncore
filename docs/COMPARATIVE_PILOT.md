# Comparative pilot and release review

Prepared 29 October 2026 for GNCore 7.0.0rc1. Publication is held.

## What was actually run

Ten complete IDE responses cover 300 category-task answers: four development runs and six holdout runs, separately in original Microsoft VS Code and Antigravity IDE. Two additional fresh-session follow-ups cover three changed entrypoints each. Published references map all30 categories to14 pinned public repositories, including Anthropic, Microsoft, Google, Hugging Face, Vercel and specialist maintainers. Exact revisions, licenses and hashes accompany the results.

Pure generated Python artifacts were inspected and executed against frozen fixtures. Four development web pages were exercised in the real browser. Held-out and final-follow-up page behavior remains unmeasured because local browser access became disabled. No production cloud, GPU, device, native sanitizer or full-project security result is claimed.

The complete Python3.12 package suite passed148 tests with one skip using temporary test files outside the sync folder. A synced-folder run passed147, failed one and skipped one on a Windows access-denied journal replacement. Both logs are retained; the competing process has not been identified. Atomic journal replacement now has bounded transient-lock retries and tests preserving the previous journal on permanent failure.

## What the numbers mean

Each percentage is passed checks divided by applicable checks on the supplied task. Manual grading is unblinded, with one evaluator and one batch conversation per condition. Copilot Auto is not a model pin. There are no repeated-trial estimates or no-added-skill controls. These results do not establish statistical superiority or isolate a skill's causal effect.

On identical holdout tasks, excluding the unmeasured UI category, VS Code passed164/173 checks before,158/173 with published references, and168/173 with the initial revised candidate. Antigravity passed140/173,132/173 and147/173 respectively. Some categories remain below95%; that goal is not a reporting rule. Development and holdout scores must not be subtracted as if they were the same task.

The initial revised VS Code allocation artifact passed16 frozen tests but failed all three added regression cases. Final known-task follow-ups pass16 frozen and3 exploratory allocation cases in both IDEs. Both final arithmetic answers are correct, while broader performance coverage still omits part of one criterion. The original VS Code neural-network artifact fails an extreme-logit case (13/14); revised and reference artifacts pass14/14 on that fixture. All original failures remain visible.

## What changed in the library

All30 entrypoints gained original guidance for domain-specific failure prevention and verification. All374 workflow objects, supporting resources and licenses are preserved against cd77d82. A frontend generation regression temporarily omitted existing visual modes; they were restored and checked. Final code-build, performance-engineering and frontend guidance differs from the initial revised trial and has separately labeled adaptive evidence. Twenty-seven other entrypoints match that trial. Imported source authorship and obligations remain applicable.

Routing was not improved by this comparative pass. The prior router corpus result remains18/30 normal scenarios, and host discovery depends on the agent's settings. Exporting skills does not guarantee that an IDE loaded or obeyed them.

## Read and reproduce

- [Plain-language report](../web-results/comparison/EXECUTIVE-REPORT.md) and [technical report](../web-results/comparison/TECHNICAL-REPORT.md).
- [Protocol](../benchmarks/comparison/PROTOCOL.md), frozen tasks/rubrics and explicit review notes under benchmarks/comparison.
- [Category scores](../web-results/comparison/category-scores.csv), [failed checks](../web-results/comparison/failed-checks.csv), source snapshots and raw runs under web-results/comparison.
- Landscape PNG/SVG/PDF scorecards under web-results/comparison/charts. Gray means unmeasured; the95% line is a goal only.

Reporting can be regenerated with scripts/compile_comparison_reviews.py followed by scripts/report_comparison.py using Matplotlib, NumPy and ReportLab. This regenerates plots from saved evidence; it does not repeat IDE inference.

## Publication decision

Review the actual artifacts and remaining limitations before authorizing GitHub, PyPI or the live website. The candidate remains7.0.0rc1. The local benchmark website page is a preview. Do not advertise that every category exceeds95%, that the pilot is independently audited, or that the live package/site was updated.

Build once from the accepted source commit; verify exact wheel/sdist code, all skill resources, clean installation outside the checkout, metadata and a portable skill ZIP. Record SHA-256 identities and promote those same bytes through the existing GitHub/PyPI workflow. Run hosted CI on the accepted commit before tagging. Publish the website only after registry/release verification and explicit owner approval; retain prior source/site commits for recovery. A faulty PyPI release requires a corrected version rather than overwriting files.
