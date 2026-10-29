---
name: web-frontend
description: "Build complete responsive web interfaces and choose an appropriate visual direction from the product brief."
license: Apache-2.0 AND MIT
---

# GNCore Web Frontend

Version: 7.0.0rc1

## Choose the work

Honor explicit visual choices and preserve the existing brand. Otherwise choose one direction from audience, content density, and primary action; do not mix every installed style. Reuse the actual stack and components.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Working routes and components with real content, semantic design tokens, keyboard focus, responsive layouts, and relevant loading, empty, error, success and permission states.

Exercise the primary journey and invalid input. Check narrow/wide layouts, overflow, zoom, focus order and reduced motion. Run the repository build; distinguish actual browser evidence from proposed checks.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

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

## Anticipate failure and verify the boundary

Infer one coherent visual direction from audience, content and primary action when the user omits a style; preserve explicit brand choices. Implement the full journey before polish: named controls, validation, loading/error/empty/success states and selected-value confirmation. Hidden custom controls still need a visible focus indicator on their visible wrapper. Use a focusable status target deliberately if moving focus. Render and exercise keyboard and narrow layouts; CSS inspection or a proposed checklist is not browser evidence, and visual taste has no objective percentage score. Prototype feedback must describe only the action actually implemented: do not say an email, calendar invite or external booking was sent when the page only updates local state.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `web-front-design` | Build or restyle a web interface with a deliberate visual identity and complete interaction states. |
| `web-front-ui-ux` | Choose evidence-based UI patterns, palettes, typography, and layouts using a searchable local design library. |
| `web-front-react` | Improve React and Next.js rendering, data fetching, and bundle performance using measured bottlenecks. |
| `web-front-guidelines` | Review a web interface against current interface guidelines and report actionable file and line findings. |
| `web-front-shadcn` | Add and customize shadcn/ui components within an existing React application and theme. |
| `web-front-minimalism` | Create restrained web interfaces with clear hierarchy, deliberate whitespace, and essential controls. |
| `web-front-swiss` | Build Swiss and International Style web layouts using typographic hierarchy and disciplined grids. |
| `web-front-editorial` | Design magazine and editorial web experiences with strong reading rhythm, type, and image relationships. |
| `web-front-luxury` | Create premium web experiences through typography, art direction, restrained detail, and polished interaction. |
| `web-front-agentic` | Design AI task interfaces that expose progress, editable intent, results, and recovery controls. |
| `web-front-maximalism` | Build expressive maximalist web interfaces with rich layers and a readable visual hierarchy. |
| `web-front-taste` | Art-direct a distinctive frontend using researched compositions and iterative browser inspection. |
| `web-front-neobrutalism` | Create neo-brutalist web UI with bold borders, flat color, and direct, usable controls. |
| `web-front-industrial` | Build industrial brutalist web interfaces with structural grids, utility typography, and exposed function. |
| `web-front-futuristic` | Create futuristic and Y2K-inspired interfaces with deliberate technical typography and spatial depth. |
| `web-front-retro` | Create nostalgic web interfaces with era-specific typography, palettes, and graphic treatments. |
| `web-front-collage` | Build paper and scrapbook web compositions with tactile layers and coherent reading order. |
| `web-front-doodle` | Create playful hand-drawn web interfaces with readable type and controlled visual irregularity. |
| `web-front-bento` | Organize web content in a responsive bento grid with purposeful card sizes and hierarchy. |
| `web-front-glass` | Build glass and translucent web surfaces with readable contrast and affordable rendering costs. |
| `web-front-neumorphism` | Create soft inset and raised web surfaces while keeping control states accessible. |
| `web-front-claymorphism` | Create playful clay-like web surfaces with rounded geometry and tactile depth. |
| `web-front-aurora` | Create aurora and gradient web treatments with controlled color transitions and readable content. |
| `web-front-cyberpunk` | Build neon and cyberpunk web interfaces with disciplined glow, dark surfaces, and clear interaction states. |
| `web-front-threejs` | Implement immersive Three.js and WebGL web experiences with explicit asset and rendering budgets. |
| `web-front-r3f` | Build React Three Fiber scenes with clear React and render-loop ownership and proper cleanup. |
| `web-front-scrollytelling` | Build scroll-driven narratives with GSAP ScrollTrigger and resilient responsive behavior. |
| `web-front-kinetic-type` | Animate web typography with purposeful timing while preserving readable text and reduced-motion access. |
| `web-front-organic` | Create warm organic web interfaces using earth tones, natural rhythm, and tactile accents. |
| `web-front-design-system` | Define web design tokens, component contracts, and state specifications that fit an existing product. |
| `web-front-styling` | Style responsive web components using Tailwind, semantic tokens, and accessible primitives. |
| `web-front-composition` | Refactor React component APIs using composition, clear state ownership, and version-compatible context patterns. |
| `web-front-gsap` | Implement GSAP tweens and responsive animation with explicit lifecycle and interruption handling. |
| `web-front-motion-performance` | Profile and improve animation rendering cost without changing intended behavior. |
| `web-front-motion-review` | Review web animation timing, easing, continuity, and interaction feedback with actionable findings. |
| `web-front-testing` | Test important local web user journeys with Playwright and observable browser evidence. |
| `web-front-browser` | Inspect and exercise web interfaces through agent-browser snapshots, selectors, and screenshots. |
| `web-front-find-skills` | Find frontend skills and compare candidates by scope, source, compatibility, and license. |
| `web-front-accessibility` | Implement and verify responsive, keyboard-accessible web interfaces and assistive-technology semantics. |
| `web-front` | Route a web frontend task to the relevant GNCore design, component, motion, or browser workflow. |

## Focused procedures

### GNCore Design (`web-front-design`)

Ground the visual direction in the actual product and audience. Establish typography, layout, palette, and a primary action before implementing the requested page. Use real content and inspect the finished interface in a browser.

For relevant technical detail, read [the attributed source guide](references/web-front-design/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Ui Ux (`web-front-ui-ux`)

Use the bundled search script and data to compare patterns appropriate to the product. Check accessibility and task flow before aesthetic polish. Record the selected direction and implement it in the current framework.

For relevant technical detail, read [the attributed source guide](references/web-front-ui-ux/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore React (`web-front-react`)

Inspect framework versions and a baseline. Read the relevant async, bundle, server, or rendering rules rather than loading every rule. Preserve request isolation and verify that any optimization changes measured behavior without changing correctness.

For relevant technical detail, read [the attributed source guide](references/web-front-react/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Guidelines (`web-front-guidelines`)

Fetch the guideline source identified in UPSTREAM.md and review the requested files. Tie findings to actual code and user impact. If the source is unavailable, state that limitation and distinguish local checks from a current guideline audit.

For relevant technical detail, read [the attributed source guide](references/web-front-guidelines/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Shadcn (`web-front-shadcn`)

Inspect components.json, framework, aliases, installed primitives, and Tailwind version. Choose compatible registry components, preserve local customizations, and verify controlled state, keyboard interactions, focus restoration, and theme tokens.

For relevant technical detail, read [the attributed source guide](references/web-front-shadcn/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Minimalism (`web-front-minimalism`)

Reduce competing emphasis rather than hiding necessary actions. Use a compact type scale, a neutral surface system, and one purposeful accent. Align content to a consistent grid; give primary and secondary actions distinct weight. Preserve explicit loading, empty, error, and success states. Check long labels, zoom, keyboard focus, and narrow screens.

### GNCore Swiss (`web-front-swiss`)

Define column and baseline relationships, a legible grotesk type hierarchy, and deliberate asymmetric composition. Use alignment and scale to organize content. Keep reading order and interaction order coherent when the grid collapses on small screens.

For relevant technical detail, read [the attributed source guide](references/web-front-swiss/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Editorial (`web-front-editorial`)

Choose a readable text measure, display hierarchy, captions, and image proportions around the actual story. Build responsive article and index layouts with intentional pacing and clear navigation.

For relevant technical detail, read [the attributed source guide](references/web-front-editorial/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Luxury (`web-front-luxury`)

Choose a distinct material or editorial direction appropriate to the brand. Use deliberate type contrast, image cropping, restrained color, and consistent spacing rather than adding decoration to every surface. Keep prices, navigation, and purchase actions easy to find. Budget image weight and motion; verify mobile composition and reduced-motion behavior. Use licensed imagery and avoid invented customer or award claims.

### GNCore Agentic (`web-front-agentic`)

Make the task goal, inputs, running state, and result visible. Separate proposals from completed actions, show meaningful progress and recoverable errors, and provide cancel or edit controls where supported. Avoid implying actions succeeded without tool evidence.

For relevant technical detail, read [the attributed source guide](references/web-front-agentic/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Maximalism (`web-front-maximalism`)

Choose a coherent motif, palette, and focal point for each section. Use layering, oversized type, and texture to reinforce content; preserve legible body text and predictable navigation across screen sizes.

For relevant technical detail, read [the attributed source guide](references/web-front-maximalism/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Taste (`web-front-taste`)

Use the bundled direction library and references to select a product-specific composition. Inspect helper scripts before running them and resolve their paths from the installed skill folder. Iterate on observed screenshots without replacing the user's chosen design system.

For relevant technical detail, read [the attributed source guide](references/web-front-taste/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Neobrutalism (`web-front-neobrutalism`)

Define border, shadow, spacing, and type tokens. Use offset shadows and strong block geometry consistently, preserving distinguishable focus, disabled, and error states without using color as the only signal.

For relevant technical detail, read [the attributed source guide](references/web-front-neobrutalism/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Industrial (`web-front-industrial`)

Choose a functional visual vocabulary: squared geometry, ruled divisions, strong labels, restrained material tones, and numerals suited to scanning. Use density according to the task and collapse secondary detail on narrow screens without losing access. Distinguish interactive controls from decorative hardware motifs. Check contrast, focus, overflow, and long technical values; avoid distressed textures behind body text.

### GNCore Futuristic (`web-front-futuristic`)

Pick a specific visual era and use its geometry, display type, metallic or luminous surfaces, and motion consistently. Keep ordinary text, controls, and responsive navigation readable beneath the effects.

For relevant technical detail, read [the attributed source guide](references/web-front-futuristic/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Retro (`web-front-retro`)

Choose an era and build a coherent type, color, and illustration system around it. Keep semantic controls and modern interaction feedback; do not reproduce obsolete usability problems as decoration.

For relevant technical detail, read [the attributed source guide](references/web-front-retro/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Collage (`web-front-collage`)

Use paper surfaces, cutout imagery, and controlled overlap with a clear content hierarchy. Keep labels selectable, text contrast stable, and decorative layers outside pointer and keyboard interaction paths.

For relevant technical detail, read [the attributed source guide](references/web-front-collage/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Doodle (`web-front-doodle`)

Use sketch marks and imperfect outlines as accents around a stable layout. Keep body typography readable and ensure handmade-looking controls retain clear labels, hit areas, focus states, and disabled behavior.

For relevant technical detail, read [the attributed source guide](references/web-front-doodle/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Bento (`web-front-bento`)

Rank content before choosing spans. Use card sizes to reflect importance, preserve useful reading order when stacked, and avoid fixed heights that clip translated text or changing data.

For relevant technical detail, read [the attributed source guide](references/web-front-bento/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Glass (`web-front-glass`)

Use translucency sparingly over controlled backgrounds. Define opaque fallbacks, borders, and focus treatments. Test changing imagery, light and dark themes, blur support, reduced transparency where available, and performance on constrained devices.

For relevant technical detail, read [the attributed source guide](references/web-front-glass/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Neumorphism (`web-front-neumorphism`)

Use paired highlights and shadows on restrained surfaces. Add borders, labels, and explicit focus indicators so controls do not depend on subtle shadows to communicate affordance or state.

For relevant technical detail, read [the attributed source guide](references/web-front-neumorphism/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Claymorphism (`web-front-claymorphism`)

Define a restrained radius and shadow system, use dimensional accents for emphasis, and keep content surfaces calm. Check legibility, visual weight, and interaction state differences at small sizes.

For relevant technical detail, read [the attributed source guide](references/web-front-claymorphism/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Aurora (`web-front-aurora`)

Choose gradient stops from the product palette and define a stable text-bearing surface. Check contrast across every stop and fallback; keep animated gradients optional and measure their rendering cost.

For relevant technical detail, read [the attributed source guide](references/web-front-aurora/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Cyberpunk (`web-front-cyberpunk`)

Use luminous accents to guide attention rather than outline every element. Keep body text sharp, avoid flashing effects, and distinguish focus, errors, and active controls beyond hue alone.

For relevant technical detail, read [the attributed source guide](references/web-front-cyberpunk/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Threejs (`web-front-threejs`)

Inspect the existing renderer and dependencies. Budget draw calls, texture sizes, device pixel ratio, and asset loading; handle resize, context loss, disposal, and an accessible non-WebGL fallback.

For relevant technical detail, read [the attributed source guide](references/web-front-threejs/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore R3F (`web-front-r3f`)

Keep React state changes outside high-frequency frame work where possible. Reuse resources, dispose owned geometry and materials, suspend expensive assets deliberately, and test loading, fallback, and reduced-motion states.

For relevant technical detail, read [the attributed source guide](references/web-front-r3f/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Scrollytelling (`web-front-scrollytelling`)

Map the narrative to ordinary document flow before pinning or scrubbing. Register plugins, scope animation ownership, refresh after layout changes, and clean up on navigation. Preserve content access and a reduced-motion experience.

For relevant technical detail, read [the attributed source guide](references/web-front-scrollytelling/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Kinetic Type (`web-front-kinetic-type`)

Keep semantic text available to assistive technology when splitting visible glyphs. Handle font loading, line wrapping, interruption, and reduced motion. Review timing with real copy and preserve content access when animation is disabled.

For relevant technical detail, read [the attributed source guide](references/web-front-kinetic-type/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Organic (`web-front-organic`)

Use warm neutral surfaces, a terracotta accent, and a readable display/body type relationship. Let natural shapes support content without obscuring text, hit areas, or predictable navigation.

For relevant technical detail, read [the attributed source guide](references/web-front-organic/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Design System (`web-front-design-system`)

Map primitive tokens to semantic roles and component tokens. Specify themes, typography, spacing, interaction states, and migration from existing values. Use the web design references; load slide-related material only for an explicit presentation task.

For relevant technical detail, read [the attributed source guide](references/web-front-design-system/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Styling (`web-front-styling`)

Inspect the installed styling versions and reuse the current token and component system. Compose consistent variants and responsive behavior. Validate dark mode, focus, loading, validation, and long content without importing unrelated canvas workflows.

For relevant technical detail, read [the attributed source guide](references/web-front-styling/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Composition (`web-front-composition`)

Identify the concrete source of prop proliferation or duplicated state. Read the relevant composition rules and use explicit variants or compound components only where they improve the caller API. Preserve behavior and confirm the project's React version.

For relevant technical detail, read [the attributed source guide](references/web-front-composition/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Gsap (`web-front-gsap`)

Use the installed GSAP version and scope animation ownership to the component or page. Choose tweens, timelines, and matchMedia according to the requested effect. Clean up on unmount, respect reduced motion, and preserve a library the user already chose.

For relevant technical detail, read [the attributed source guide](references/web-front-gsap/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Motion Performance (`web-front-motion-performance`)

Capture a representative animation trace before optimizing. Identify layout, paint, compositing, or JavaScript costs; reduce the dominant cost and compare under the same conditions. Budget promoted layers and avoid claiming a frame rate without measurements.

For relevant technical detail, read [the attributed source guide](references/web-front-motion-performance/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Motion Review (`web-front-motion-review`)

Observe the actual interaction and relevant implementation. Check purpose, interruption, entry and exit, perceived response, and reduced motion. Report concrete changes tied to the observed sequence and distinguish measured behavior from design judgment.

For relevant technical detail, read [the attributed source guide](references/web-front-motion-review/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Testing (`web-front-testing`)

Inspect the app's existing test setup and start it using the supported command. Cover the requested journey with role/name selectors, deterministic fixtures, and observable assertions. Capture failures and rerun relevant checks after fixing causes.

For relevant technical detail, read [the attributed source guide](references/web-front-testing/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Browser (`web-front-browser`)

Check whether agent-browser is available and use its documented snapshot and reference workflow. Work within the requested browser session and task. Verify the resulting UI state and report screenshots or commands as evidence; do not infer success from an attempted click.

For relevant technical detail, read [the attributed source guide](references/web-front-browser/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Find Skills (`web-front-find-skills`)

Search for the actual missing capability, inspect source entrypoints and maintenance signals, and compare relevant candidates. Distinguish discovery from installation; install only within the user's requested scope and preserve attribution when adapting.

For relevant technical detail, read [the attributed source guide](references/web-front-find-skills/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Responsive Accessibility (`web-front-accessibility`)

Inspect semantic structure, labels, tab order, visible focus, dialog focus ownership, validation messages, zoom, touch targets, and reduced-motion behavior. Test real user tasks at narrow and wide widths with long content. Apply relevant WCAG criteria when requested, and distinguish automated checks from manual or assistive-technology checks. Do not claim conformance without evidence.

### GNCore Frontend Workflow (`web-front`)

Inspect the product, existing stack, requested deliverable, and available skill folders. Choose the smallest useful set from the catalog below: typically one visual direction and the engineering or testing workflow the task needs. Read those SKILL.md files and only their task-relevant references. Implement the complete requested feature and verify the observable result. Do not load every style or change the user's chosen stack.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
