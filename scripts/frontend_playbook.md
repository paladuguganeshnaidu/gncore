## Visual direction from an idea

Treat the brief as a product brief, not a request to name a theme. Identify the audience, primary task, content volume, brand constraints, device context, and intended emotion. If the user supplied enough to build, state a short design rationale and proceed. Ask only when an unknown materially changes the product, integration, or acceptance criteria.

An explicit style or reference image takes priority over defaults. Preserve the current brand and design system for a focused feature unless the user requests a redesign. Recognize common spellings such as minimal/minimalist/minimalism, maximalism/maximalizm, and brutalism/brutalisim. Interpret constraints such as “no gradients” or “no animation” as constraints, not requests for those styles.

When no style is named, choose one primary direction using the table. Select type, palette, spacing, geometry, imagery, density, and motion as a coherent system. A layout pattern such as bento can support an editorial or minimalist direction; it does not require mixing every aesthetic.

| Product evidence | Useful starting direction | Implementation consequence |
| --- | --- | --- |
| Dense work, analytics, settings, administration | Minimalist or Swiss | Strong alignment, compact but legible density, clear state and action hierarchy |
| Articles, journalism, publishing, long-form stories | Editorial | Readable measure, strong headline/body contrast, captions, deliberate reading rhythm |
| Premium hospitality, jewelry, craftsmanship, luxury goods | Luxury/editorial | Art-directed imagery, restrained palette, purposeful type contrast, calm pacing |
| Children's products or a playful learning experience | Clay or doodle accents | Expressive shapes around a stable layout, readable body text, clear touch targets |
| Creative studio, festival, music, expressive portfolio | Maximalist or neo-brutalist | A strong motif and focal point, controlled overlap, readable navigation |
| Technical tools, industrial products, utilitarian control panels | Industrial or Swiss | Structured grids, clear labels, useful numerals, direct controls |
| AI task delegation or agent workspaces | Agentic | Editable intent, progress, results, cancellation and recovery, clear action boundaries |
| Futuristic or gaming identity | Futuristic/cyberpunk when justified | Controlled luminous accents, sharp text, predictable ordinary controls |
| Natural materials, sustainability, wellness identity | Organic | Warm surfaces, natural rhythm, tactile accents, verified contrast |
| No strong visual cues | Restrained product-specific direction | Let actual content, a deliberate type choice, and one characteristic motif establish identity |

For a new project, define a small token system before broad styling: semantic surfaces and text, primary/secondary actions, status colors, a readable type scale, spacing, radius, border, shadow, and motion. Use existing tokens when the project already has them. Choose licensed assets and avoid fabricated customers, ratings, awards, or product claims.

## Available visual modes

- Minimalism: remove competing emphasis; preserve necessary controls and feedback. Use whitespace and alignment instead of hiding functionality.
- Swiss: use a disciplined column/baseline system, clear grotesk typography, and deliberate asymmetry. Preserve reading order when stacking.
- Editorial: compose real text and imagery around a reading experience, with useful captions, a stable measure, and intentional section rhythm.
- Luxury: emphasize material, imagery, typography, and small consistent details. Keep prices, navigation, and purchase actions easy to find.
- Agentic: make intent, tools, running state, proposals, completed actions, evidence, and recovery distinguishable.
- Maximalism: use a coherent motif, rich layers, and deliberate focal points. Keep body text and ordinary actions readable.
- Neo-brutalism: use flat color, strong borders, offset shadows, and direct controls consistently. Maintain explicit focus and error states.
- Industrial brutalism: use ruled structure, utility typography, restrained material tones, and functional density. Keep decoration out of control semantics.
- Futuristic/Y2K: select a specific visual vocabulary; keep ordinary text and interaction accessible beneath spatial or metallic effects.
- Retro: choose a coherent era through typography, palette, and graphics while preserving modern interaction behavior.
- Collage/paper: layer tactile surfaces and cutouts without breaking reading order, text selection, pointer access, or keyboard access.
- Doodle: use irregular marks as accents around a stable layout. Preserve labels, hit areas, and discoverable state.
- Bento: size and group modules by content priority. Allow translated text, changing data, and narrow-screen stacking without clipping.
- Glass: use controlled backgrounds, explicit borders and contrast, an opaque fallback, and a limited blur budget.
- Neumorphism: add visible affordances and focus beyond subtle shadows; raised and inset effects must not be the only state signal.
- Claymorphism: use a restrained radius/depth system and a calm text-bearing surface beneath playful dimensional accents.
- Aurora/gradient: control stop colors and text-bearing surfaces; verify contrast across stops and keep animated gradients optional.
- Neon/cyberpunk: use glow as emphasis, keep text sharp, avoid flashing, and distinguish state beyond hue.
- Immersive 3D: justify the scene as part of the experience; provide loading, fallback, resize, resource disposal, and a device budget.
- Scrollytelling: make the story readable in ordinary document flow, then add scoped pinning or scrubbing with cleanup and reduced motion.
- Kinetic typography: preserve semantic text when splitting glyphs; handle font loading, line wrapping, interruption, and reduced motion.
- Organic: use warm or natural surfaces and rhythms without obscuring text, controls, or predictable navigation.

## Build a complete product slice

1. Inspect the existing framework, runtime versions, component primitives, design tokens, routes, state ownership, and relevant APIs. Reuse the actual project structure.
2. Build the requested user journey with real content and data contracts. Include loading, empty, error, success, validation, and permission states where applicable.
3. Use semantic HTML and established accessible primitives. Define keyboard interaction and focus ownership for dialogs, menus, forms, and other composite controls.
4. Design narrow and wide layouts intentionally. Check long labels, changed data, translated text, zoom, touch, and overflow rather than relying on a single screenshot size.
5. Choose motion for purpose, frequency, and context. Support interruption and cleanup; prefer reduced movement when requested or indicated by user preferences.
6. Profile an actual bottleneck before optimizing. Bound image weight, render work, animation cost, data waterfalls, and third-party code according to the project.
7. Verify the main journey through the available browser or test setup. Review screenshots, console output, network failures, accessibility behavior, and responsive states when those tools are available.

## Completion evidence

Deliver the implemented artifact, the chosen direction and why it fits, and the checks actually run. A successful build does not prove visual quality; a screenshot does not prove behavior. Fix observed issues and rerun the relevant checks. If browser or rendering tools are unavailable, state the limit and complete the checks that are available instead of inventing visual verification.

## Representative requests

- “Build a dashboard for a small clinic.” Infer a clear, restrained information hierarchy with readable scheduling and task states; do not ask the user to choose a style name before building.
- “Make a maximalist landing page for a music festival.” Follow the explicit expressive direction, use real event content, and preserve ticket and navigation usability.
- “A premium hotel site, no animation.” Use an appropriate luxury/editorial direction with art-directed images and calm typography; keep the no-animation constraint.
- “Add settings to this existing app.” Preserve its existing theme, component system, and navigation; implement the complete settings behavior.
