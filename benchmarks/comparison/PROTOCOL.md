# GNCore comparative evaluation protocol

Prepared 29 October 2026. This protocol defines measurements before improving the candidate from the comparison results.

## Question

On the same bounded developer tasks, does loading GNCore improve observable outcomes relative to a relevant, version-pinned published skill? Where does it fail, and does a focused instruction change help on a separate task variant?

The desired 90–95% range is an engineering goal, never a required reported score. Missing runs, inaccessible tools and weak results remain visible. A skill's publisher, popularity or instruction length is not a performance measurement.

## Conditions and isolation

1. Freeze GNCore before changes at local commit `cd77d82`.
2. Select the closest task-relevant published reference for each of the 30 categories. Record publisher, full source revision, entrypoint/resource hashes, source URL, scope and license notices. No suitable match means not measured, not zero.
3. Run a development task variant with the frozen GNCore and reference conditions. Improve GNCore using observed failures and source review.
4. Run a separate frozen holdout variant with the original GNCore, reference and improved GNCore. Do not feed the original answers, grading key or review conclusions to the evaluation agent.
5. Include no-added-skill controls on representative tasks where available, so base-model knowledge is not mistaken for a skill effect.

Use isolated workspaces outside the GNCore ancestor tree, fresh conversations, the same host setup, task inputs, response schema and output budget within each block. Provide only that condition's skill files and necessary supporting resources. Never execute imported helpers automatically. Keep grading material outside evaluation workspaces.

Antigravity and original Microsoft VS Code are separate blocks. Record their executable versions, visible model labels and any inability to pin the underlying model. Copilot Auto is not a fixed model; do not describe its comparisons as a controlled model experiment. Do not pool different IDE/model blocks into a claim about one intrinsic skill score.

## Measurements

- **Correct task decisions:** passed factual/engineering checks divided by applicable checks. Every task has a frozen rubric; retain pass/fail evidence for each item. These are task-check percentages, not a universal intelligence or performance rating.
- **Bugs found:** distinct seeded defects correctly identified divided by seeded defects in the reviewed fixture. Also report safe controls incorrectly flagged and missed defects. This is fixture recall, not real-world security assurance.
- **Repair correctness:** independent executable input/output cases passed by the generated patch. Inspect generated code before execution; use isolated, bounded local execution and retain actual test logs.
- **Interface behavior:** actual rendered-page checks for required interactions, keyboard use, labels and narrow-screen overflow. Keep design observations separate from functional/accessibility test counts. No unsupported percentage for visual beauty.
- **Engineering quality:** explicit, independently reviewable checks for contracts, failure recovery, testability, numerical/data correctness and honest evidence claims. Do not award points for merely mentioning the rubric's words.
- **Context and runtime cost:** report only actually observed measurements. Approximate text size is not model token usage, billing or inference latency. Missing telemetry stays unavailable.

The main scorecard shows raw numerators/denominators alongside percentages and a separate row for every category. Overall raw-check totals give each applicable criterion equal weight; the few conditional exclusions create slightly different category denominators, which remain visible. This reporting detail supersedes the initial equal-category summary intention; category-level comparisons remain the primary evidence. Scores from different types of tests are not silently added into one “efficiency” number. Report test coverage, missing runs and host/model limitations beside the result.

## Recorded execution deviations

- Whole-library packs were placed in a nested, isolated Git workspace under the ignored work directory, rather than physically outside the GNCore ancestor path. Grading keys and prior answers are excluded, but this is not a filesystem security boundary. Explicit prompts forbid unrelated project access. One VS Code read request still prompted for file permission; the owner handled it.
- The first revised pack accidentally omitted the existing frontend visual-mode section. It was restored, and the initial frontend entrypoint plus pack fingerprint are retained in `web-results/comparison/initial-candidate`. Later code-build and performance-engineering additions address observed allocation and arithmetic errors. Those three changed entrypoints receive a separately labeled adaptive follow-up; its known-task results are not spliced into the original unseen holdout totals.
- The original 16-case allocation fixture missed mixed exact/fractional remainder ordering. Three additional exploratory cases were added after inspecting a failure and are applied consistently to all eligible conditions. Frozen and exploratory test results remain separate, while the manual contract review records the observed error.
- Local browser use became disabled in Work settings after the four development-page tests. Holdout UI checks remain not measured; static inspection is not substituted for a rendered test.
- No repeated inference trials or no-added-skill controls have yet been captured. Do not claim a causal skill effect, independent trials, or statistical superiority.
- Original holdout responses were collected after the initial revised/reference holdouts. Fresh sessions and frozen original packs were used, but run order was not randomized; provider state, caching and other time effects are uncontrolled.

## Interpretation and improvement

Use observed development failures to make concise, transferable instruction changes. Help the user by inferring necessary engineering work from their brief, stating reasonable defaults and surfacing consequential omissions; retain scope and authorization boundaries. Avoid adding the exact expected benchmark answers or unnecessary universal checklists to every skill.

Keep development results and holdout results separate. Retests do not erase earlier failures. One task variant per category and a single model response are a pilot, not a statistically powered general ranking. If repeats are not executed, explicitly say so and do not invent confidence intervals or claim small differences are significant.

## Deliverables

Save raw prompts, versioned source records, actual responses, executable artifacts, per-check reviews and logs in the repository's `web-results/comparison` evidence bundle. Downloaded source snapshots and account-specific working data stay in ignored local storage; preserve upstream notices and do not relicense the reference skills as GNCore.

Create a readable landscape scorecard with Matplotlib, plus a plain-language report and a technical report describing the experiment, scoring, source mapping, limitations and reproducible commands. Every plotted number must resolve to a recorded result. Show not-measured cells explicitly; never fill them with assumed scores.

Publishing GitHub/PyPI releases or deploying the live website still requires the owner's separately requested publication approval.
