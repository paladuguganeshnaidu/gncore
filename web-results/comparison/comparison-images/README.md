# Comparison tables as images

Prepared 29 October 2026 from the saved pilot. This presentation adds no new benchmark runs or performance claims.

- **gncore-complete-comparison-table-full-hd.png:** exact 1920x1080 table covering all 30 categories, original/reference/initial-revised conditions in both IDEs, named reference guides, GNCore capabilities and measurement limits.
- **gncore-executive-comparison-table-full-hd.png:** exact 1920x1080 practical-result and product-characteristic tables, with the separate final adaptive follow-up.
- The matching **-4k.png** images are 3840x2160 for zooming, printing or presentation.
- SVG versions preserve vector text/shapes. complete-comparison-table.csv provides the category data and exact source revisions/URLs.
- image-provenance.json records the input review hash and output image hashes/dimensions.

## Interpretation

Percentages count applicable task checks or explicit code fixtures. The main category table uses the initial revised trial; final code-build, performance and frontend entrypoints were changed later and have separately labeled adaptive results. UI cells remain incomplete rather than receiving a fabricated score.

Published references are a task-specific collection from 14 pinned repositories, not one competing application. An individual publisher's full catalog was not evaluated. The standalone OpenAI/Codex catalog and Plotly-specific skills were not benchmarked; they have no invented competitive score. GNCore capability facts do not imply competing tools lack similar capabilities.

The overall 29-category manual scores are 168/173 versus 158/173 in VS Code and 147/173 versus 132/173 in Antigravity for revised/reference conditions. These are observations from one unblinded batch per condition with no repeated inference/no-added-skill control. They do not establish universal speed, cost, security, beauty or future reliability.

Reproduce with scripts/render_comparison_tables.py using the existing Matplotlib environment. The script reads saved evidence, not live provider APIs. Retain all labels and limitations when sharing these images.
