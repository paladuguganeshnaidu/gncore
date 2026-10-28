"""Inventory requested upstream skills without executing their contents."""

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import subprocess
import tempfile

SOURCES = {
    "anthropics/skills": ["frontend-design", "webapp-testing"],
    "nextlevelbuilder/ui-ux-pro-max-skill": ["ui-ux-pro-max", "design-system", "ui-styling"],
    "vercel-labs/agent-skills": ["vercel-react-best-practices", "web-design-guidelines", "vercel-composition-patterns"],
    "shadcn/ui": ["shadcn"],
    "leonxlnx/taste-skill": ["minimalist-ui", "high-end-visual-design", "design-taste-frontend", "industrial-brutalist-ui"],
    "zeke/swiss-design-skill": ["swiss-design"],
    "bergside/awesome-design-skills": ["editorial", "agentic", "expressive", "neobrutalism", "futuristic", "retro", "paper", "doodle", "bento", "neumorphism", "claymorphism", "gradient", "neon", "terracotta"],
    "iart-ai/web-animation-skills": ["glassmorphism"],
    "freshtechbro/claudedesignskills": ["threejs-webgl", "react-three-fiber"],
    "greensock/gsap-skills": ["gsap-scrolltrigger", "gsap-core", "gsap-performance"],
    "iart-ai/kinetic-typography-skills": ["kinetic-typography"],
    "emilkowalski/skills": ["review-animations"],
    "vercel-labs/agent-browser": ["agent-browser"],
    "vercel-labs/skills": ["find-skills"],
}


def git(*args):
    result = subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def inspect(repo):
    destination = Path(tempfile.gettempdir()) / "gncore-upstream-skills" / repo.replace("/", "--")
    try:
        if not (destination / ".git").exists():
            git("clone", "--filter=blob:none", "--depth", "1", "--no-checkout", f"https://github.com/{repo}.git", str(destination))
        revision = git("-C", str(destination), "rev-parse", "HEAD").strip()
        files = git("-C", str(destination), "ls-tree", "-r", "--name-only", "HEAD").splitlines()
        skills = []
        candidates = set(SOURCES[repo]) | {name.removeprefix("vercel-") for name in SOURCES[repo]}
        if repo == "leonxlnx/taste-skill":
            candidates.add("taste-skill")
        for path in files:
            if path.endswith("SKILL.md") and Path(path).parent.name in candidates:
                content = git("-C", str(destination), "show", f"HEAD:{path}")
                name = re.search(r"(?m)^name:\s*(.+)$", content)
                skills.append({"path": path, "name": name.group(1).strip().strip("\"'") if name else None})
        licenses = [p for p in files if re.search(r"(^|/)(LICENSE|LICENCE|NOTICE|COPYING)(\.[^/]*)?$", p, re.I)]
        return {"repo": repo, "revision": revision, "checkout": str(destination), "requested": SOURCES[repo], "skills": skills, "licenses": licenses}
    except Exception as error:
        return {"repo": repo, "requested": SOURCES[repo], "error": str(error)}


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(inspect, SOURCES))
    output = Path(__file__).resolve().parents[1] / ".work" / "upstream-inventory.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))
