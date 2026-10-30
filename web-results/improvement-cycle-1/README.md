# Revised skill build: verified work and open comparison

All 30 developer domains were revised, with 374 workflow IDs preserved. The requested greater-than-95% comparative AI-quality result is **not established**.

The complete [landscape PDF](../../output/pdf/GNCore-skill-improvement-review.pdf) contains one [1920x1080 evidence graph](verified-evidence-1920x1080.png), the [30-domain table](verified-domain-table.csv), research sources, implementation changes, actual checks and every domain's completion boundaries.

| Verified local work | Result |
| --- | --- |
| Final Python suite | 151 passed, 1 skipped |
| Catalog audit | 30 categories, 374 workflows, 1,660 resources; no issues |
| Project installation | 1,690 files; no missing/modified/unmanaged files |
| Inspected development code | 160/160 executable fixtures passed across four conditions |
| Offline UI artifacts | 20 browser checks passed; four narrow-layout checks unmeasured |
| Local distributions | Wheel built from sdist; metadata, installed import and source/resource comparisons passed |
| Fair AI comparison | Incomplete: 20 of 120 planned answers captured before account usage limit |

## What changed

- Add relevant completion boundaries in all 30 domains, including compatibility, identity, data leakage, numerical correctness, lifecycle/recovery and honest verification.
- Move detailed procedures to declared, hashed WORKFLOWS.md resources. Main entrypoint bytes decrease 43.2%; no token, cost or latency savings are claimed.
- Refine ten procedures and eight discovery summaries with explicit previous/current lineage. Preserve all existing workflow IDs, resource declarations and license obligations.
- Add focused guidance for runtime secrets, copyable examples under incomplete contracts, and concrete native null/length/error rules.

## Why quality percentages are withheld

Some initial development agents inherited parent chat history, potentially exposing prior analysis or answers. Their numeric rubric results are withdrawn from fair quality comparisons. Raw answers and decisions remain in internal-*-batch-*.json, review-results.json and final-candidate-results.json, all explicitly development-only. Actual generated-code execution and browser observations remain valid within their narrow scopes; they do not establish which guide caused success.

A replacement comparison explicitly used fork_turns=none and the same dispatch template in every condition. The account usage limit stopped it after two baseline batches (20 answers); no balanced comparison is available. See isolated/STATUS.json and isolated/input-manifest.json. No inference retries were attempted after the limit. The frozen inputs support a later continuation without tuning to a target score.

## Evidence and limitations

candidate-integrity.json and workflow-quality-changes.json retain exact merge lineage. focused-guidance-changes.json retains the adaptive text changes. final-tests.txt, final-catalog-audit.json, project-verification.json and distribution-verification.json record executed checks. Per-run executable/browser logs are under runs/. first-candidate-guides/ preserves the guides before focused correction.

Thirty pinned reference guides from fourteen repositories were downloaded and content-checked after CRLF/LF normalization; hashes and exact source links are in downloaded-reference-guides.json. They are research inputs, not exclusively GNCore-owned content. No upstream helper was executed.

The port oracle and artifact inspector required documented corrections; original rejected results remain available. Harness repairs are not skill gains. The known-task replay cannot establish unseen generalization, production reliability or vendor superiority. Historical VS Code/Antigravity results remain separate in ../comparison/; this cycle did not rerun IDE inference. Earlier natural-language routing remains 18/30. GPU, native/embedded runtime, deployed services and full accessibility remain unmeasured.

GitHub, PyPI and website publication are held. Exact-commit remote CI, broader platform/interpreter checks, completed fresh-context evaluation and remaining UI validation are still needed before release claims.
