"""Verify this cycle's precise procedure/resource lineage against its baseline."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'web-results/improvement-cycle-1'

def main():
    baseline=json.loads((OUT/'baseline-inputs.json').read_text())['baseline_commit']
    old=json.loads(subprocess.check_output(['git','show',baseline+':catalog/categories.json'],cwd=ROOT))
    new=json.loads((ROOT/'catalog/categories.json').read_text(encoding='utf-8'))
    old={c['id']:c for c in old['categories']}
    ledger=json.loads((ROOT/'src/gncore/skills/migration.json').read_text(encoding='utf-8'))['quality_revisions']
    changes=[]; descriptions=[]; unchanged=0; resource_count=0
    for category in new['categories']:
        prior=old[category['id']]
        assert category['resources']==prior['resources'], category['id']
        assert category['licenses']==prior['licenses'], category['id']
        workflows={w['id']:w for w in prior['workflows']}
        assert set(workflows)=={w['id'] for w in category['workflows']}
        for workflow in category['workflows']:
            previous=workflows[workflow['id']]
            if workflow['description']!=previous['description']:
                descriptions.append(workflow['id'])
            if workflow['procedure']!=previous['procedure']:
                revision=workflow['quality_revision']
                before=hashlib.sha256(previous['procedure'].encode()).hexdigest()
                after=hashlib.sha256(workflow['procedure'].encode()).hexdigest()
                assert revision['previous_procedure_sha256']==before
                assert revision['procedure_sha256']==after
                assert revision['reason'] and workflow['id'] in ledger
                changes.append(workflow['id'])
            else:unchanged+=1
        resource_count+=len(prior['resources'])
    assert len(changes)==10 and len(descriptions)==8 and unchanged==364
    report={'baseline_commit':baseline,'categories':len(new['categories']),'workflow_ids_preserved':374,
            'procedures_unchanged':unchanged,'reviewed_procedure_refinements':changes,
            'discovery_summaries_refined':descriptions,'existing_resource_declarations_preserved':resource_count,
            'existing_licenses_preserved':True,'generated_workflow_resources_added':30,
            'scope':'Current quality revisions are explicit; historical phase-one migration accounting remains separate.'}
    (OUT/'candidate-integrity.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
