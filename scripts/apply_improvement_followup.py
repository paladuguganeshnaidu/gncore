"""Apply one reviewed, bounded follow-up; preserve the first candidate inputs."""
import hashlib
import json
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'web-results/improvement-cycle-1'
path=ROOT/'catalog/category-completion-checks.json'

def main():
    snapshot=OUT/'first-candidate-guides'
    if snapshot.exists():
        raise SystemExit('Follow-up already applied; preserve original input snapshots.')
    snapshot.mkdir()
    for folder in (ROOT/'src/gncore/skills/unified_data').iterdir():
        if folder.is_dir():
            (snapshot/folder.name).mkdir()
            for name in ('SKILL.md','WORKFLOWS.md'):
                shutil.copyfile(folder/name,snapshot/folder.name/name)
    data=json.loads(path.read_text(encoding='utf-8'))
    additions={
      'cloud-devops-sre': 'Before delivering a rollout plan, state the credential delivery boundary: a managed identity or authorized runtime secret store, no embedded credentials in artifacts, and redaction from logs. Naming least privilege alone does not cover credential exposure.',
      'documentation': 'Give a self-contained example a reader can copy. If the wire schema is incomplete, clearly label every assumption or supply a runnable offline mock/client example that preserves the known contract; do not imply unverified wire compatibility or leave the only example as non-runnable placeholder prose.',
      'systems-programming': 'Write the actual ABI rules rather than saying to document them: whether null is permitted at zero length, required alignment and checked length arithmetic, who owns each allocation, caller lifetime obligations, and a specific failure/status convention that prevents unwinding across the boundary. Mark unspecified foreign guarantees as assumptions.'
    }
    changes=[]
    for category, instruction in additions.items():
        before=list(data[category])
        data[category].append(instruction)
        changes.append({'category':category,'before':before,'after':data[category],
                        'reason':'First candidate replay omitted a concrete completion boundary; adaptive correction, not unseen evidence.',
                        'first_guide_sha256':hashlib.sha256((snapshot/category/'SKILL.md').read_bytes()).hexdigest()})
    path.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    (OUT/'focused-guidance-changes.json').write_text(json.dumps(changes,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
