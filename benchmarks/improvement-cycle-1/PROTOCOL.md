# GNCore improvement cycle 1

Prepared29 October2026. Goal: improve all30 domains against observed failures, retain honest measurements and deliver one graph, a complete minimal table and an explanatory PDF. A95% threshold is a target, never an imposed result.

## Development evidence

The prior IDE pilot provides41 failed/unmeasured rows across19 categories in the initial revised trial. Three static review passes covered ten categories each. Their recommendations concern scope expansion, specific correctness invariants, contradictory discovery text and excessive unconditional context. They are development review, not an external independent audit.

## Implemented intervention

Freeze the current source guides before editing. Add task-specific completion boundaries to all30 domains. Move focused procedures into a declared, hashed WORKFLOWS.md resource, preserving all374 IDs and retained upstream resources. Correct ten procedures and eight discovery summaries, with explicit before/after hashes and reasons; historical phase-one migration accounting is retained separately from these quality refinements.

## Separate internal evaluation block

- Replay the30 frozen H01–H30 tasks already used in the IDE pilot. This is **adaptive regression evaluation on known tasks**, not unseen generalization.
- Four conditions: current baseline, matched published reference, revised candidate, and no-added-skill control.
- Each condition uses three fresh agent sessions of ten tasks. These are batch conversations, not30 independent per-category trials. Model identity is inherited from the host but no fixed served-model ID is recorded.
- The task/schema, answer-length guidance and batch grouping are held constant. Agent dispatch wording differs to identify the condition: the candidate explicitly follows its new WORKFLOWS routing, and the control forbids reading installed skills. Prompts are not byte-identical. No grading keys, prior answers, suspected failures or intended solutions are supplied to evaluation agents.
- Ordinary answers target150–230 words, versus the historical IDE pilot's shorter budget. Do not compare raw percentages across these different host/protocol blocks as if only the skill changed.
- Preserve all raw JSON answers. Generated artifacts are inspected before bounded execution; model agents do not execute artifacts or external actions.
- The existing six-criterion rubric remains frozen. H14c4 is inapplicable in all arms because the supplied fixture has no remote effect. UI checks require actual rendering; missing browser access remains unmeasured.
- Manual grading is unblinded and single-evaluator. Assertions/independent code fixtures take priority where available. There are no repeated-inference estimates or statistical superiority claims.

The port oracle originally rejected integer subclasses although the task excludes only booleans from integers. Correct that oracle uniformly and retain the rejected baseline result. Also permit inspected empty local integer subclasses and literal error-message formatting in the bounded artifact inspector; neither is a skill improvement. All four conditions use the corrected final fixture/inspector. The browser's documented390px override returned without establishing a narrow viewport (observed1280px); keep H30c6 unmeasured in every condition.

## Improvement loop and stop rule

Run the full candidate pass after source/structure checks. Analyze actual failures; make narrowly justified corrections and retest affected boundaries, retaining each earlier result. At most two additional focused adaptive correction passes in this cycle. Stop when relevant checks pass or no justified correction can be verified with available tools. A plateau, unavailable tool or residual failure is reported; do not keep sampling until a lucky response exceeds95%.

On a six-check category rubric, exceeding95% requires all six checks. This coarse fraction is not a reliability probability. Do not fill missing categories or infer production, security, GPU, hardware or deployment performance from a synthetic task.

## Publication and ownership

This is an internal GNCore engineering report, not a vendor-certified leaderboard or publisher endorsement. Matched upstream skills remain attributed and retain their own license terms; downloading and adapting permitted content does not make it exclusively GNCore-owned. Keep old evidence immutable. No GitHub/PyPI/website publication is authorized by this cycle alone.

## Protocol repair: fresh-context validation

Some development dispatches inherited the parent history. That can reveal earlier analysis/answers, so their scores are retained only as development evidence. After the guide corrections, freeze the candidate and run exactly one balanced four-condition validation with fork_turns=none for every ten-task batch. Use the same dispatch template except input/output paths. No additional source tuning or score-target resampling within this block. Review model answers with masked condition labels where possible and actual executed fixtures/browser evidence. Preserve any residual misses and open390px check.
