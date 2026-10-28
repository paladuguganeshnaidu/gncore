# Adaptive frontend skill

Install `web-frontend` once and describe the site or interface you want:

```bash
gncore export --specific web-frontend
```

```text
$web-frontend Build a booking site for a small clinic.
$web-frontend Create a maximalist music festival landing page.
$web-frontend Build a premium hotel site with no animation.
```

Its single entrypoint combines the 40 earlier frontend workflows with product-context selection, theme guidance, implementation steps, and quality criteria. When the user omits a theme, it chooses a suitable direction from audience, primary task, content, and brand constraints. Explicit themes and reference images take priority. Focused changes preserve an existing design system.

Visual modes include minimalism, Swiss, editorial, luxury, agentic, maximalism, neo-brutalism, industrial, futuristic/Y2K, retro, collage/paper, doodle, bento, glass, neumorphism, claymorphism, aurora, cyberpunk, immersive 3D, scrollytelling, kinetic typography, and organic design.

Implementation guidance covers components, tokens, React composition and performance, shadcn, responsive accessibility, motion ownership, browser testing, and complete interaction states. Technical source guides and assets remain attributed supporting references rather than separate skill invocations.

The optional `gncore plan` command makes deterministic starting recommendations for local verification. It does not replace the host AI's design judgment or visual review.

All earlier `web-front-*` names remain CLI/API aliases to `web-frontend`. See [Migration](../MIGRATION.md), [Catalog](ALL_SKILLS.md), and [Source Research](SOURCE_RESEARCH.md).
