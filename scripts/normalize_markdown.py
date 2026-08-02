from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent


def normalize(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    lines = text.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    out: list[str] = []
    in_frontmatter = False
    in_fence = False

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if idx == 0 and stripped == '---':
            in_frontmatter = True
            out.append(line)
            continue
        if in_frontmatter:
            out.append(line)
            if stripped == '---':
                in_frontmatter = False
                out.append('')
            continue

        if re.match(r'^```', stripped):
            if not in_fence:
                if out and out[-1].strip() and not re.match(r'^```', out[-1].strip()):
                    out.append('')
                out.append('```text' if stripped == '```' else line)
                in_fence = True
            else:
                out.append(line)
                in_fence = False
            continue

        if in_fence:
            out.append(line)
            continue

        if re.match(r'^\s{0,3}#{1,6}\s', line):
            if out and out[-1].strip() and not re.match(r'^```', out[-1].strip()):
                out.append('')
            out.append(line)
            if idx < len(lines) - 1 and lines[idx + 1].strip() and not re.match(r'^\s{0,3}#{1,6}\s', lines[idx + 1]) and not re.match(r'^```', lines[idx + 1].strip()):
                out.append('')
            continue

        if re.match(r'^\s*(?:[-*+]\s|\d+\.\s)', line):
            if out and out[-1].strip() and not re.match(r'^\s*(?:[-*+]\s|\d+\.\s)', out[-1]) and not re.match(r'^\s{0,3}#{1,6}\s', out[-1]) and not re.match(r'^```', out[-1].strip()):
                out.append('')
            out.append(line)
            continue

        out.append(line)

    cleaned = '\n'.join(out).strip() + '\n'
    path.write_text(cleaned, encoding='utf-8')


if __name__ == '__main__':
    for path in sorted(ROOT.rglob('*.md')):
        if 'test-env' in path.as_posix() or '.git' in path.as_posix():
            continue
        normalize(path)
