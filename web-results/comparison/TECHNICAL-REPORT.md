# GNCore: experiment, evidence and limits

## What this tells you

This is a practical pilot of GNCore and a published reference for each of its 30 developer categories. Original Microsoft VS Code and Antigravity were tested separately. The charts show real saved answers, executed code tests and browser observations; a missing measurement stays gray. Development and holdout tasks are different and must not be subtracted to claim an improvement.

## How to read a percentage

A result of 5/6 (83%) means five of six specific checks passed on one task. It does not mean the skill is 83% intelligent, an application is 83% secure, or that future tasks have an 83% success probability. The 95% line is an improvement target, never a value filled into the data.

## Results currently supported

All 30 categories have saved answers in both IDEs. The main comparison uses the same holdout tasks for original GNCore, published references and the revised trial. Twenty-nine categories are fully reviewed; the web interface category still needs rendered checks. The four landscape sheets show every category, raw counts and percentages.

Development tasks were used to find weaknesses; holdout tasks were reserved for the next evaluation. The final three-case follow-up uses already known tasks and is reported separately.

## Did the revised trial do better?

On the same holdout tasks, the 29 fully reviewed non-UI categories passed164/173 checks (94.8%) before and168/173 (97.1%) in the revised VS Code trial; the published references passed158/173 (91.3%). Antigravity passed140/173 (80.9%) before and147/173 (85.0%) in the revised trial; references passed132/173 (76.3%). These are single unblinded pilot observations, not statistically established gains or a universal ranking. Many individual categories remain below95%, and the initial revised trial is not the final three-entrypoint follow-up.

## What changed

All 30 GNCore entrypoints gained original, domain-specific failure-prevention guidance. The work addresses recoverable retries, safe migration boundaries, model/data correctness, reproducible builds and visible UI focus. Existing workflows and upstream license notices remain intact. A text change is an implemented improvement to guidance; only a comparable held-out result can support an outcome-improvement claim.

## A passing test suite still missed a bug

VS Code's initial revised allocation code passed all16 frozen cases but failed three added mixed-remainder cases. The original answer and failures are retained. These exploratory tests were added after inspecting the bug and are reported separately, not disguised as predeclared coverage. This is why100% on a small fixture cannot certify general correctness.

antigravity-gncore-after-holdout: 3/3 added allocation cases passed.

antigravity-gncore-before-holdout: 3/3 added allocation cases passed.

antigravity-gncore-final-followup-holdout: 3/3 added allocation cases passed.

antigravity-reference-holdout: 3/3 added allocation cases passed.

vscode-gncore-after-holdout: 0/3 added allocation cases passed.

vscode-gncore-before-holdout: 3/3 added allocation cases passed.

vscode-gncore-final-followup-holdout: 3/3 added allocation cases passed.

vscode-reference-holdout: 3/3 added allocation cases passed.

## What remains uncertain

There is one task variant per category and no repeated-trial estimate. Manual scoring is unblinded. The whole-library batch can create cross-task context and retrieval effects. Copilot Auto can choose models; these results cannot isolate a skill's causal effect from model knowledge. Final code-build, performance and frontend guidance changed after the first revised trial and receive a separate adaptive follow-up. The frontend style section was restored after a generation regression. These known-task follow-ups are not spliced into the original holdout scores. Browser use became disabled after the development tests; missing holdout UI evidence remains gray. This is not a broad ranking of publishers or a security certification. Visual beauty was not assigned a fabricated percentage.

## Final guidance: separate follow-up

Antigravity: 16/16 frozen allocation tests passed.

Antigravity: 3/3 exploratory allocation tests passed.

Antigravity: arithmetic is correct. The performance answer still omits throughput coverage. Browser behavior remains unmeasured.

VS Code: 16/16 frozen allocation tests passed.

VS Code: 3/3 exploratory allocation tests passed.

VS Code: arithmetic is correct. The performance answer still omits throughput coverage. Browser behavior remains unmeasured.

Both final allocation answers pass the added regressions, and both arithmetic answers give22.4 and28ms correctly. A known-task follow-up cannot establish generalization. The original VS Code baseline also exposed an extreme-logit neural-network failure (13/14 tests); initial revised and reference answers passed14/14 on that fixture. Earlier failures remain in the evidence.

## Package and installation checks

The complete Python3.12 package suite passed148 tests with one skip when temporary test files were outside the sync folder. A run inside the synced repository passed147, failed one and skipped one after Windows access-denied journal replacement. Both logs remain. Bounded atomic replacement retries and permanent-failure preservation tests were added; the competing process was not identified. This does not prove every synced-folder installation succeeds.

## Release decision

Keep release publication on hold while reviewing the evidence and remaining failures. Prepare and verify package and website artifacts before asking the owner for GitHub, PyPI and website publication approval.

## Experimental design

The frozen before revision is cd77d82. Sixty synthetic tasks and six checks per task were frozen before instruction improvements: 30 development and 30 holdout cases. Published guides cover 30 mappings from 14 repositories. Exact commits, entrypoint/support hashes, root and skill-specific license metadata are in source-snapshots.json. References were not relicensed as GNCore, and imported helpers were not executed.

## Measurement and grading

Raw copied IDE responses are preserved, schema-validated and expanded into standalone generated artifacts. Eligible pure Python functions are inspected, checked with a narrow AST allowlist and run under an isolated child process with a five-second compute limit and separate Windows startup allowance. This is not a general security sandbox. Security findings and repairs are manually reviewed against seeded snippets; safe-control false positives are separate. The generated HTML is exercised in the real in-app browser at a 390px viewport, including invalid input, enabling, confirmation and visible radio focus.

## Scoring details

Six frozen criteria per case are reviewed with explicit evidence. Two conditional development criteria are inapplicable in every arm: mutation retry identity for a read-only feed and dataset splitting for a hand-token-alignment example. The stale-writer holdout has no remote operation, so its unknown-remote-outcome check is also inapplicable in every arm. These exclusions are stated in the compiler. Percentages use applicable checks, with raw denominators visible. Missing or incomplete runs are not zero and are not silently averaged into a passing score. Functional tests, security recall, false positives and manual decisions remain different metrics. Overall raw-check totals weight each check equally; category rows expose the denominator differences.

## Reproduction

Run scripts/compile_comparison_reviews.py, then scripts/report_comparison.py in an environment with Matplotlib, NumPy and ReportLab. Grading fixtures and immutable tasks are under benchmarks/comparison. Use scripts/import_comparison_response.py for a newly captured response, then scripts/grade_comparison_artifacts.py for inspected eligible artifacts. IDE inference itself requires the recorded fresh-session protocol and account/model availability; rerunning a reporting script does not reproduce the inference.

## Limitations and threats to validity

The references are task-relevant examples rather than every publisher's best possible configuration. Some are narrower than the category. Offline guide-conditioned tasks do not exercise cloud deployment, hardware, GPU training, full tool integrations or complete project workflows. All 30 tasks share one conversation per condition, so they are not independent per-skill trials. Output budgets and varied document sizes can affect coverage. No no-added-skill control or repeated trials should be claimed unless a corresponding saved run exists. Small percentage differences are not evidence of statistical superiority.

## Source map

ai-engineering: anthropics/skills / skills/mcp-builder/SKILL.md / ca45fc496a3436251f191354091d557da31c15b5 / https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/skills/mcp-builder/SKILL.md

automation: temporalio/skill-temporal-developer / SKILL.md / 5f5a94d448d53e0d535a7369bf9cb7248620a0bf / https://github.com/temporalio/skill-temporal-developer/blob/5f5a94d448d53e0d535a7369bf9cb7248620a0bf/SKILL.md

cloud-devops-sre: google/skills / skills/cloud/gke-reliability/SKILL.md / 81b0e8f8f40513c31b3388e600506e8b48a85bc2 / https://github.com/google/skills/blob/81b0e8f8f40513c31b3388e600506e8b48a85bc2/skills/cloud/gke-reliability/SKILL.md

code-build: obra/superpowers / skills/systematic-debugging/SKILL.md / 2ce8aa15d05bd57213e6f746f953aafb7ded7a8b / https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/systematic-debugging/SKILL.md

computer-vision: huggingface/skills / skills/huggingface-vision-trainer/SKILL.md / fabc634a893f62ad5c2039830397efa35fa62715 / https://github.com/huggingface/skills/blob/fabc634a893f62ad5c2039830397efa35fa62715/skills/huggingface-vision-trainer/SKILL.md

cybersecurity: affaan-m/ecc / skills/security-review/SKILL.md / 25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b / https://github.com/affaan-m/ecc/blob/25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b/skills/security-review/SKILL.md

data-engineering: K-Dense-AI/scientific-agent-skills / skills/polars/SKILL.md / 5f2bc0341354fd5590aef76a533ada1e1e5b4e62 / https://github.com/K-Dense-AI/scientific-agent-skills/blob/5f2bc0341354fd5590aef76a533ada1e1e5b4e62/skills/polars/SKILL.md

data-science: K-Dense-AI/scientific-agent-skills / skills/statistical-analysis/SKILL.md / 5f2bc0341354fd5590aef76a533ada1e1e5b4e62 / https://github.com/K-Dense-AI/scientific-agent-skills/blob/5f2bc0341354fd5590aef76a533ada1e1e5b4e62/skills/statistical-analysis/SKILL.md

databases: supabase/agent-skills / skills/supabase-postgres-best-practices/SKILL.md / c9be0e931b7930f7d02126d04774d904c381e7d7 / https://github.com/supabase/agent-skills/blob/c9be0e931b7930f7d02126d04774d904c381e7d7/skills/supabase-postgres-best-practices/SKILL.md

deep-learning: K-Dense-AI/scientific-agent-skills / skills/pytorch-lightning/SKILL.md / 5f2bc0341354fd5590aef76a533ada1e1e5b4e62 / https://github.com/K-Dense-AI/scientific-agent-skills/blob/5f2bc0341354fd5590aef76a533ada1e1e5b4e62/skills/pytorch-lightning/SKILL.md

design-ux: microsoft/skills / .github/skills/frontend-design-review/SKILL.md / 00d66a64919edca5bca2c673373444e36a4b5461 / https://github.com/microsoft/skills/blob/00d66a64919edca5bca2c673373444e36a4b5461/.github/skills/frontend-design-review/SKILL.md

developer-research: K-Dense-AI/scientific-agent-skills / skills/scientific-critical-thinking/SKILL.md / 5f2bc0341354fd5590aef76a533ada1e1e5b4e62 / https://github.com/K-Dense-AI/scientific-agent-skills/blob/5f2bc0341354fd5590aef76a533ada1e1e5b4e62/skills/scientific-critical-thinking/SKILL.md

developer-tools: affaan-m/ecc / skills/git-workflow/SKILL.md / 25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b / https://github.com/affaan-m/ecc/blob/25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b/skills/git-workflow/SKILL.md

distributed-systems: cloudflare/skills / skills/durable-objects/SKILL.md / 49a31e0b3229ccdffe4944be9c61bc7481d1d432 / https://github.com/cloudflare/skills/blob/49a31e0b3229ccdffe4944be9c61bc7481d1d432/skills/durable-objects/SKILL.md

documentation: anthropics/skills / skills/doc-coauthoring/SKILL.md / ca45fc496a3436251f191354091d557da31c15b5 / https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/skills/doc-coauthoring/SKILL.md

embedded-systems: beriberikix/zephyr-agent-skills / skills/zephyr-foundations/SKILL.md / ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce / https://github.com/beriberikix/zephyr-agent-skills/blob/ed63cdfb8cdfbeb5946ea39c33f4aa6bcf3a5cce/skills/zephyr-foundations/SKILL.md

game-development: minhhoit/gamedev-agent-skills / skills/godot/godot-2d-movement/SKILL.md / b105e1cf617adf0b68ed98790a716bbb60993179 / https://github.com/minhhoit/gamedev-agent-skills/blob/b105e1cf617adf0b68ed98790a716bbb60993179/skills/godot/godot-2d-movement/SKILL.md

machine-learning: K-Dense-AI/scientific-agent-skills / skills/scikit-learn/SKILL.md / 5f2bc0341354fd5590aef76a533ada1e1e5b4e62 / https://github.com/K-Dense-AI/scientific-agent-skills/blob/5f2bc0341354fd5590aef76a533ada1e1e5b4e62/skills/scikit-learn/SKILL.md

mlops: huggingface/skills / skills/hf-cloud-sagemaker-production-defaults/SKILL.md / fabc634a893f62ad5c2039830397efa35fa62715 / https://github.com/huggingface/skills/blob/fabc634a893f62ad5c2039830397efa35fa62715/skills/hf-cloud-sagemaker-production-defaults/SKILL.md

mobile-development: vercel-labs/agent-skills / skills/react-native-skills/SKILL.md / 1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62 / https://github.com/vercel-labs/agent-skills/blob/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62/skills/react-native-skills/SKILL.md

natural-language-processing: K-Dense-AI/scientific-agent-skills / skills/transformers/SKILL.md / 5f2bc0341354fd5590aef76a533ada1e1e5b4e62 / https://github.com/K-Dense-AI/scientific-agent-skills/blob/5f2bc0341354fd5590aef76a533ada1e1e5b4e62/skills/transformers/SKILL.md

neural-networks: K-Dense-AI/scientific-agent-skills / skills/pytorch-lightning/SKILL.md / 5f2bc0341354fd5590aef76a533ada1e1e5b4e62 / https://github.com/K-Dense-AI/scientific-agent-skills/blob/5f2bc0341354fd5590aef76a533ada1e1e5b4e62/skills/pytorch-lightning/SKILL.md

observability: microsoft/skills / .github/plugins/azure-sdk-python/skills/azure-monitor-opentelemetry-py/SKILL.md / 00d66a64919edca5bca2c673373444e36a4b5461 / https://github.com/microsoft/skills/blob/00d66a64919edca5bca2c673373444e36a4b5461/.github/plugins/azure-sdk-python/skills/azure-monitor-opentelemetry-py/SKILL.md

performance-engineering: affaan-m/ecc / skills/benchmark/SKILL.md / 25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b / https://github.com/affaan-m/ecc/blob/25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b/skills/benchmark/SKILL.md

python: trailofbits/skills / plugins/modern-python/skills/modern-python/SKILL.md / 2be6433b39e009cd2b6fd3be1895f6b1faa5af9a / https://github.com/trailofbits/skills/blob/2be6433b39e009cd2b6fd3be1895f6b1faa5af9a/plugins/modern-python/skills/modern-python/SKILL.md

release-engineering: obra/superpowers / skills/finishing-a-development-branch/SKILL.md / 2ce8aa15d05bd57213e6f746f953aafb7ded7a8b / https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/finishing-a-development-branch/SKILL.md

systems-programming: trailofbits/skills / plugins/rust-review/skills/rust-review/SKILL.md / 2be6433b39e009cd2b6fd3be1895f6b1faa5af9a / https://github.com/trailofbits/skills/blob/2be6433b39e009cd2b6fd3be1895f6b1faa5af9a/plugins/rust-review/skills/rust-review/SKILL.md

testing: obra/superpowers / skills/test-driven-development/SKILL.md / 2ce8aa15d05bd57213e6f746f953aafb7ded7a8b / https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/test-driven-development/SKILL.md

web-backend: affaan-m/ecc / skills/api-design/SKILL.md / 25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b / https://github.com/affaan-m/ecc/blob/25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b/skills/api-design/SKILL.md

web-frontend: anthropics/skills / skills/frontend-design/SKILL.md / ca45fc496a3436251f191354091d557da31c15b5 / https://github.com/anthropics/skills/blob/ca45fc496a3436251f191354091d557da31c15b5/skills/frontend-design/SKILL.md
