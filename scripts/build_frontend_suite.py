"""Build attributed GNCore entrypoints from the staged upstream collection.

Existing upstream documents and resources remain intact. Only GNCore-owned
entrypoints, provenance, the manifest, and original fallback workflows are written.
"""

from __future__ import annotations

import json
from pathlib import Path
import shutil

import yaml

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / "src/gncore/skills/frontend_data"

# Requested upstream name, GNCore suffix, focused description, implementation guidance.
SPECS = [
    ("frontend-design", "design", "Build or restyle a web interface with a deliberate visual identity and complete interaction states.", "Ground the visual direction in the actual product and audience. Establish typography, layout, palette, and a primary action before implementing the requested page. Use real content and inspect the finished interface in a browser."),
    ("ui-ux-pro-max", "ui-ux", "Choose evidence-based UI patterns, palettes, typography, and layouts using a searchable local design library.", "Use the bundled search script and data to compare patterns appropriate to the product. Check accessibility and task flow before aesthetic polish. Record the selected direction and implement it in the current framework."),
    ("vercel-react-best-practices", "react", "Improve React and Next.js rendering, data fetching, and bundle performance using measured bottlenecks.", "Inspect framework versions and a baseline. Read the relevant async, bundle, server, or rendering rules rather than loading every rule. Preserve request isolation and verify that any optimization changes measured behavior without changing correctness."),
    ("web-design-guidelines", "guidelines", "Review a web interface against current interface guidelines and report actionable file and line findings.", "Fetch the guideline source identified in UPSTREAM.md and review the requested files. Tie findings to actual code and user impact. If the source is unavailable, state that limitation and distinguish local checks from a current guideline audit."),
    ("shadcn", "shadcn", "Add and customize shadcn/ui components within an existing React application and theme.", "Inspect components.json, framework, aliases, installed primitives, and Tailwind version. Choose compatible registry components, preserve local customizations, and verify controlled state, keyboard interactions, focus restoration, and theme tokens."),
    ("minimalist-ui", "minimalism", "Create restrained web interfaces with clear hierarchy, deliberate whitespace, and essential controls.", "Reduce competing emphasis rather than hiding necessary actions. Use a compact type scale, a neutral surface system, and one purposeful accent. Align content to a consistent grid; give primary and secondary actions distinct weight. Preserve explicit loading, empty, error, and success states. Check long labels, zoom, keyboard focus, and narrow screens."),
    ("swiss-design", "swiss", "Build Swiss and International Style web layouts using typographic hierarchy and disciplined grids.", "Define column and baseline relationships, a legible grotesk type hierarchy, and deliberate asymmetric composition. Use alignment and scale to organize content. Keep reading order and interaction order coherent when the grid collapses on small screens."),
    ("editorial", "editorial", "Design magazine and editorial web experiences with strong reading rhythm, type, and image relationships.", "Choose a readable text measure, display hierarchy, captions, and image proportions around the actual story. Build responsive article and index layouts with intentional pacing and clear navigation."),
    ("high-end-visual-design", "luxury", "Create premium web experiences through typography, art direction, restrained detail, and polished interaction.", "Choose a distinct material or editorial direction appropriate to the brand. Use deliberate type contrast, image cropping, restrained color, and consistent spacing rather than adding decoration to every surface. Keep prices, navigation, and purchase actions easy to find. Budget image weight and motion; verify mobile composition and reduced-motion behavior. Use licensed imagery and avoid invented customer or award claims."),
    ("agentic", "agentic", "Design AI task interfaces that expose progress, editable intent, results, and recovery controls.", "Make the task goal, inputs, running state, and result visible. Separate proposals from completed actions, show meaningful progress and recoverable errors, and provide cancel or edit controls where supported. Avoid implying actions succeeded without tool evidence."),
    ("expressive", "maximalism", "Build expressive maximalist web interfaces with rich layers and a readable visual hierarchy.", "Choose a coherent motif, palette, and focal point for each section. Use layering, oversized type, and texture to reinforce content; preserve legible body text and predictable navigation across screen sizes."),
    ("design-taste-frontend", "taste", "Art-direct a distinctive frontend using researched compositions and iterative browser inspection.", "Use the bundled direction library and references to select a product-specific composition. Inspect helper scripts before running them and resolve their paths from the installed skill folder. Iterate on observed screenshots without replacing the user's chosen design system."),
    ("neobrutalism", "neobrutalism", "Create neo-brutalist web UI with bold borders, flat color, and direct, usable controls.", "Define border, shadow, spacing, and type tokens. Use offset shadows and strong block geometry consistently, preserving distinguishable focus, disabled, and error states without using color as the only signal."),
    ("industrial-brutalist-ui", "industrial", "Build industrial brutalist web interfaces with structural grids, utility typography, and exposed function.", "Choose a functional visual vocabulary: squared geometry, ruled divisions, strong labels, restrained material tones, and numerals suited to scanning. Use density according to the task and collapse secondary detail on narrow screens without losing access. Distinguish interactive controls from decorative hardware motifs. Check contrast, focus, overflow, and long technical values; avoid distressed textures behind body text."),
    ("futuristic", "futuristic", "Create futuristic and Y2K-inspired interfaces with deliberate technical typography and spatial depth.", "Pick a specific visual era and use its geometry, display type, metallic or luminous surfaces, and motion consistently. Keep ordinary text, controls, and responsive navigation readable beneath the effects."),
    ("retro", "retro", "Create nostalgic web interfaces with era-specific typography, palettes, and graphic treatments.", "Choose an era and build a coherent type, color, and illustration system around it. Keep semantic controls and modern interaction feedback; do not reproduce obsolete usability problems as decoration."),
    ("paper", "collage", "Build paper and scrapbook web compositions with tactile layers and coherent reading order.", "Use paper surfaces, cutout imagery, and controlled overlap with a clear content hierarchy. Keep labels selectable, text contrast stable, and decorative layers outside pointer and keyboard interaction paths."),
    ("doodle", "doodle", "Create playful hand-drawn web interfaces with readable type and controlled visual irregularity.", "Use sketch marks and imperfect outlines as accents around a stable layout. Keep body typography readable and ensure handmade-looking controls retain clear labels, hit areas, focus states, and disabled behavior."),
    ("bento", "bento", "Organize web content in a responsive bento grid with purposeful card sizes and hierarchy.", "Rank content before choosing spans. Use card sizes to reflect importance, preserve useful reading order when stacked, and avoid fixed heights that clip translated text or changing data."),
    ("glassmorphism", "glass", "Build glass and translucent web surfaces with readable contrast and affordable rendering costs.", "Use translucency sparingly over controlled backgrounds. Define opaque fallbacks, borders, and focus treatments. Test changing imagery, light and dark themes, blur support, reduced transparency where available, and performance on constrained devices."),
    ("neumorphism", "neumorphism", "Create soft inset and raised web surfaces while keeping control states accessible.", "Use paired highlights and shadows on restrained surfaces. Add borders, labels, and explicit focus indicators so controls do not depend on subtle shadows to communicate affordance or state."),
    ("claymorphism", "claymorphism", "Create playful clay-like web surfaces with rounded geometry and tactile depth.", "Define a restrained radius and shadow system, use dimensional accents for emphasis, and keep content surfaces calm. Check legibility, visual weight, and interaction state differences at small sizes."),
    ("gradient", "aurora", "Create aurora and gradient web treatments with controlled color transitions and readable content.", "Choose gradient stops from the product palette and define a stable text-bearing surface. Check contrast across every stop and fallback; keep animated gradients optional and measure their rendering cost."),
    ("neon", "cyberpunk", "Build neon and cyberpunk web interfaces with disciplined glow, dark surfaces, and clear interaction states.", "Use luminous accents to guide attention rather than outline every element. Keep body text sharp, avoid flashing effects, and distinguish focus, errors, and active controls beyond hue alone."),
    ("threejs-webgl", "threejs", "Implement immersive Three.js and WebGL web experiences with explicit asset and rendering budgets.", "Inspect the existing renderer and dependencies. Budget draw calls, texture sizes, device pixel ratio, and asset loading; handle resize, context loss, disposal, and an accessible non-WebGL fallback."),
    ("react-three-fiber", "r3f", "Build React Three Fiber scenes with clear React and render-loop ownership and proper cleanup.", "Keep React state changes outside high-frequency frame work where possible. Reuse resources, dispose owned geometry and materials, suspend expensive assets deliberately, and test loading, fallback, and reduced-motion states."),
    ("gsap-scrolltrigger", "scrollytelling", "Build scroll-driven narratives with GSAP ScrollTrigger and resilient responsive behavior.", "Map the narrative to ordinary document flow before pinning or scrubbing. Register plugins, scope animation ownership, refresh after layout changes, and clean up on navigation. Preserve content access and a reduced-motion experience."),
    ("kinetic-typography", "kinetic-type", "Animate web typography with purposeful timing while preserving readable text and reduced-motion access.", "Keep semantic text available to assistive technology when splitting visible glyphs. Handle font loading, line wrapping, interruption, and reduced motion. Review timing with real copy and preserve content access when animation is disabled."),
    ("terracotta", "organic", "Create warm organic web interfaces using earth tones, natural rhythm, and tactile accents.", "Use warm neutral surfaces, a terracotta accent, and a readable display/body type relationship. Let natural shapes support content without obscuring text, hit areas, or predictable navigation."),
    ("design-system", "design-system", "Define web design tokens, component contracts, and state specifications that fit an existing product.", "Map primitive tokens to semantic roles and component tokens. Specify themes, typography, spacing, interaction states, and migration from existing values. Use the web design references; load slide-related material only for an explicit presentation task."),
    ("ui-styling", "styling", "Style responsive web components using Tailwind, semantic tokens, and accessible primitives.", "Inspect the installed styling versions and reuse the current token and component system. Compose consistent variants and responsive behavior. Validate dark mode, focus, loading, validation, and long content without importing unrelated canvas workflows."),
    ("vercel-composition-patterns", "composition", "Refactor React component APIs using composition, clear state ownership, and version-compatible context patterns.", "Identify the concrete source of prop proliferation or duplicated state. Read the relevant composition rules and use explicit variants or compound components only where they improve the caller API. Preserve behavior and confirm the project's React version."),
    ("gsap-core", "gsap", "Implement GSAP tweens and responsive animation with explicit lifecycle and interruption handling.", "Use the installed GSAP version and scope animation ownership to the component or page. Choose tweens, timelines, and matchMedia according to the requested effect. Clean up on unmount, respect reduced motion, and preserve a library the user already chose."),
    ("gsap-performance", "motion-performance", "Profile and improve animation rendering cost without changing intended behavior.", "Capture a representative animation trace before optimizing. Identify layout, paint, compositing, or JavaScript costs; reduce the dominant cost and compare under the same conditions. Budget promoted layers and avoid claiming a frame rate without measurements."),
    ("review-animations", "motion-review", "Review web animation timing, easing, continuity, and interaction feedback with actionable findings.", "Observe the actual interaction and relevant implementation. Check purpose, interruption, entry and exit, perceived response, and reduced motion. Report concrete changes tied to the observed sequence and distinguish measured behavior from design judgment."),
    ("webapp-testing", "testing", "Test important local web user journeys with Playwright and observable browser evidence.", "Inspect the app's existing test setup and start it using the supported command. Cover the requested journey with role/name selectors, deterministic fixtures, and observable assertions. Capture failures and rerun relevant checks after fixing causes."),
    ("agent-browser", "browser", "Inspect and exercise web interfaces through agent-browser snapshots, selectors, and screenshots.", "Check whether agent-browser is available and use its documented snapshot and reference workflow. Work within the requested browser session and task. Verify the resulting UI state and report screenshots or commands as evidence; do not infer success from an attempted click."),
    ("find-skills", "find-skills", "Find frontend skills and compare candidates by scope, source, compatibility, and license.", "Search for the actual missing capability, inspect source entrypoints and maintenance signals, and compare relevant candidates. Distinguish discovery from installation; install only within the user's requested scope and preserve attribution when adapting."),
]

ORIGINALS = {"minimalist-ui", "high-end-visual-design", "industrial-brutalist-ui"}


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")


def main():
    records = json.loads((ROOT / ".work/staged-inventory.json").read_text(encoding="utf-8"))
    entries = []
    for requested, suffix, description, guidance in SPECS:
        record = next(r for r in records if requested in r["requested"])
        skill_id = f"web-front-{suffix}"
        target = DESTINATION / skill_id
        target.mkdir(parents=True, exist_ok=True)
        title = "GNCore " + suffix.replace("-", " ").title()
        entry = {"id": skill_id, "title": title, "description": description, "tags": ["frontend", suffix, requested], "requested": requested, "requested_repository": record["repo"]}
        if requested not in ORIGINALS:
            source = Path(record["staged"][requested])
            original = (source / "SKILL.md").read_text(encoding="utf-8")
            metadata = yaml.safe_load(original.split("---", 2)[1])
            for path in source.rglob("*"):
                if not path.is_file() or path.is_symlink():
                    continue
                relative = path.relative_to(source)
                if relative.parts[0] in {"agents", "evals", "__pycache__"} or relative.name == "README.md":
                    continue
                output = target / ("UPSTREAM.md" if relative.as_posix() == "SKILL.md" else relative)
                output.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, output)
            for filename, text in record["root_license_text"].items():
                write(target / ("UPSTREAM-" + filename), text)
            if record["repo"] == "vercel-labs/agent-skills":
                readme = ROOT / ".work/vercel-upstream-readme.md"
                if readme.exists():
                    shutil.copyfile(readme, target / "UPSTREAM-REPOSITORY-README.md")
            entry.update({"kind": "adapted", "repository": record["repo"], "revision": record["revision"], "source_path": next(s["path"] for s in record["skills"] if s["name"] == requested), "upstream_metadata": metadata})
            source_url = f'https://github.com/{entry["repository"]}/blob/{entry["revision"]}/{entry["source_path"]}'
            write(target / "SOURCE.md", f"# Source and modifications\n\nGNCore entrypoint: {skill_id}.\n\nOriginal: [{record['repo']} / {requested}]({source_url}).\n\nPinned revision: `{record['revision']}`.\n\nThe upstream instructions are preserved in `UPSTREAM.md`. Supporting files and supplied license notices are retained. Upstream metadata:\n\n```json\n{json.dumps(metadata, indent=2, ensure_ascii=False)}\n```\n\nGNCore changes: a new name, focused discovery description, web-specific workflow, progressive reference loading, and portable path guidance. The upstream authors retain authorship of their contributions; GNCore branding does not change their licenses. Frontmatter declarations and bundled license text may differ; preserve both when redistributing.\n")
            resources = "\n## Implementation references\n\nRead [UPSTREAM.md](UPSTREAM.md) for the relevant detailed workflow, then load only the references needed for this task. Its relative resource paths resolve from this installed skill folder. Replace historical `.claude/skills/<original-name>` prefixes in example commands with the absolute path to this folder. References to other upstream skills are optional material; verify availability before using them.\n\nThe GNCore scope above governs adaptation choices: preserve the user's stack, brand, deliverable, and selected tools. Upstream example palettes and library defaults are starting points.\n\nSee [SOURCE.md](SOURCE.md) for provenance and retained license notices.\n"
            if requested == "react-three-fiber":
                helper = target / "scripts/component_generator.py"
                lines = helper.read_text(encoding="utf-8").splitlines()
                patched = [line.replace("={(e)", "={{(e)").replace(", e)}", ", e)}}") if "handlers.append(f" in line else line.replace("{/*", "{{/*").replace("*/}", "*/}}") for line in lines]
                write(helper, "\n".join(patched))
                entry["patches"] = ["Escape JSX event-handler and scene-comment braces in component_generator.py f-strings so the helper compiles."]
                provenance = target / "SOURCE.md"
                write(provenance, provenance.read_text(encoding="utf-8") + "\nAdditional GNCore modification: escaped literal JSX braces in the event-handler and scene-comment f-strings in `scripts/component_generator.py`, fixing Python syntax errors. The pinned upstream version remains available at the source URL above.\n")
        else:
            entry.update({"kind": "original", "reason": "The requested upstream skill name is absent from the verified source revision.", "verified_revision": record["revision"]})
            write(target / "SOURCE.md", f"# Original GNCore workflow\n\nCopyright (c) 2026 Ganesh Naidu. Distributed under GNCore's MIT license.\n\nThe requested `{requested}` entry was not present in `{record['repo']}` at `{record['revision']}`. This workflow was written for GNCore; it is not an installation or renaming of that missing upstream skill.\n")
            shutil.copyfile(ROOT / "LICENSE", target / "LICENSE")
            resources = "\nSee [SOURCE.md](SOURCE.md) for the original workflow's provenance and license.\n"
        body = f"# {title}\n\n{guidance}\n\n## Working agreement\n\nImplement the user's requested artifact in the existing stack and design system. For a style request, apply this direction without combining every installed style. Check narrow and wide layouts, keyboard interaction, content overflow, and relevant loading or error states. Use reduced-motion alternatives for motion. Report actual checks and unresolved limitations.\n{resources}"
        write(target / "GUIDE.md", f"---\nname: {skill_id}\ndescription: {json.dumps(description)}\n---\n\n{body}")
        entries.append(entry)

    extras = [
        ("web-front-accessibility", "GNCore Responsive Accessibility", "Implement and verify responsive, keyboard-accessible web interfaces and assistive-technology semantics.", "Inspect semantic structure, labels, tab order, visible focus, dialog focus ownership, validation messages, zoom, touch targets, and reduced-motion behavior. Test real user tasks at narrow and wide widths with long content. Apply relevant WCAG criteria when requested, and distinguish automated checks from manual or assistive-technology checks. Do not claim conformance without evidence."),
        ("web-front", "GNCore Frontend Workflow", "Route a web frontend task to the relevant GNCore design, component, motion, or browser workflow.", "Inspect the product, existing stack, requested deliverable, and available skill folders. Choose the smallest useful set from the catalog below: typically one visual direction and the engineering or testing workflow the task needs. Read those SKILL.md files and only their task-relevant references. Implement the complete requested feature and verify the observable result. Do not load every style or change the user's chosen stack."),
    ]
    for skill_id, title, description, body in extras:
        target = DESTINATION / skill_id
        if skill_id == "web-front":
            body += "\n\n## Skill selection\n\n" + "\n".join(f"- `{e['id']}`: {e['description']}" for e in entries)
        write(target / "GUIDE.md", f"---\nname: {skill_id}\ndescription: {json.dumps(description)}\n---\n\n# {title}\n\n{body}\n")
        entries.append({"id": skill_id, "title": title, "description": description, "tags": ["frontend", "accessibility" if skill_id.endswith("accessibility") else "workflow"], "kind": "original"})

    for entry in entries:
        target = DESTINATION / entry["id"]
        entry["resources"] = sorted(p.relative_to(target).as_posix() for p in target.rglob("*") if p.is_file() and p.name != "SKILL.md" and "__pycache__" not in p.parts and p.suffix != ".pyc")
    write(DESTINATION / "manifest.json", json.dumps(entries, indent=2, ensure_ascii=False))
    documentation = [
        "# GNCore frontend skills", "",
        "This unreleased collection contains 40 workflows: 35 attributed adaptations of the requested upstream skills and five original GNCore workflows. The three unavailable upstream names have explicit original replacements; the remaining originals provide accessibility and skill selection.", "",
        "## Use the collection", "",
        "```bash", "gncore search web-front", "gncore show web-front-minimalism",
        "gncore export --skills web-front web-front-minimalism web-front-react web-front-testing", "```", "",
        "To install all 40 in a repository checkout for Codex:", "", "```bash",
        "npx skills add ./src/gncore/skills/frontend_data --skill '*' --agent codex --yes --copy", "```", "",
        "This is a project-local installation under `.agents/skills/`. It does not install framework dependencies, Playwright browsers, GSAP, Three.js, or the agent-browser CLI. Install those only for a project that needs them. The existing `web-development` and backend workflows remain in the catalog.", "",
        "## Requested skill mapping", "",
        "| Requested source skill | GNCore skill | Integration |", "| --- | --- | --- |",
    ]
    for entry in entries:
        if "requested" in entry:
            url = f"https://github.com/{entry['requested_repository']}"
            documentation.append(f"| [{entry['requested']}]({url}) | `{entry['id']}` | {'Attributed adaptation' if entry['kind'] == 'adapted' else 'Original replacement; upstream name unavailable'} |")
    documentation.extend([
        "", "The additional original skills are `web-front` (selection) and `web-front-accessibility`.", "",
        "## Attribution and portable resources", "",
        "Each adaptation has a GNCore-owned `SKILL.md`, preserved `UPSTREAM.md`, a `SOURCE.md` recording the source revision and metadata, and the supplied resources and license notices. The manifest in `src/gncore/skills/frontend_data/manifest.json` records every resource. Source authorship and license obligations remain intact; renaming does not make third-party material solely GNCore-authored.", "",
        "Directory and ZIP exports include these resources. Relative paths in upstream examples resolve from the installed skill directory; historical `.claude/skills/<name>` prefixes must be replaced with that directory. Reference-only upstream skills and runtime tools may need separate installation. The browser skill uses `agent-browser skills get core` to obtain instructions matching the installed CLI version.", "",
        "## Compatibility", "",
        "| Previous catalog ID | Replacement |", "| --- | --- |",
        "| `frontend-engineering` | `web-front-design` |",
        "| `ui-minimalism` | `web-front-minimalism` |",
        "| `ui-maximalism` | `web-front-maximalism` |",
        "| `responsive-accessibility` | `web-front-accessibility` |",
        "| `web-performance` | `web-front-react` |",
        "| `web-testing` | `web-front-testing` |", "",
        "Legacy lookups resolve to the new entry, which exports using its new ID. Old folders already exported into other projects are not automatically removed. The 30 existing domain packs remain unchanged. See ALL_SKILLS.md for the current complete catalog count.", "",
        "## Maintain the collection", "",
        "Edit the entrypoint workflow definitions in `scripts/build_frontend_suite.py` for the next rewrite. Upstream code and references are pinned in the manifest; review updates before replacing them. Generic `npx skills update` does not merge upstream changes into these GNCore adaptations.", "",
        "Source import uses `scripts/inspect_frontend_sources.py` followed by `scripts/stage_frontend_sources.py`, the bundled Codex installer, and GitHub network access. Install the optional `skills` Python extra for regeneration. Run `scripts/build_frontend_suite.py` against the staged inventory, regenerate the catalog, and rerun export and package checks. This import workflow expects a Codex installation; using the shipped package does not.", "",
        "This work is unreleased and retains package version 5.1.0. Complete the next rewrite and review the release version before tagging or publishing.",
    ])
    write(ROOT / "docs/FRONTEND_SKILLS.md", "\n".join(documentation))
    print(f"Built {len(entries)} GNCore frontend skills ({sum(e['kind'] == 'adapted' for e in entries)} attributed adaptations).")


if __name__ == "__main__":
    main()
