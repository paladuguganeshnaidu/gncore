"""Compile explicit internal-cycle reviews; missing evidence is never a pass."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'web-results/improvement-cycle-1'

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def compile_reviews():
    rubrics = {r['id']: r for r in read(ROOT/'benchmarks/comparison/rubrics.json')}
    notes = read(ROOT/'benchmarks/improvement-cycle-1/review-notes.json')['reviews']
    runs = []
    for profile in ('baseline', 'reference', 'candidate', 'control'):
        folder = OUT/'runs'/profile
        response_path = folder/'response.json'
        answers = {a['id']: a for a in read(response_path)['answers']}
        assert set(notes[profile]) == set(answers), profile
        cases = []
        for case_id, answer in sorted(answers.items()):
            note = notes[profile][case_id]
            assert note['basis'].strip() and isinstance(note['fail'], dict)
            failures = dict(note['fail'])
            pending = set()
            na = {'c4'} if case_id == 'H14' else set()
            browser = None
            if case_id == 'H30':
                browser = read(folder/'H30-browser.json')
                checks = {c['name']: c for c in browser['checks']}
                needed = {'c3': ['initially_disabled', 'invalid_email_disabled', 'valid_inputs_enable'],
                          'c4': ['selected_values_confirmation'], 'c5': ['radio_focus_visible'],
                          'c6': ['narrow_no_overflow']}
                for key, names in needed.items():
                    if any(n not in checks or checks[n]['passed'] is None for n in names):
                        pending.add(key)
                    elif any(checks[n]['passed'] is False for n in names):
                        failures[key] = '; '.join(checks[n]['evidence'] for n in names if not checks[n]['passed'])
            execution = None
            if case_id in {'H04','H22','H28'}:
                execution = read(folder/(case_id+'-tests.json'))
                if execution.get('error') or execution['passed'] != execution['total']:
                    assert failures, ('Executed failure needs an explicit reviewed rubric mapping', profile, case_id)
            criteria = []
            for check in rubrics[case_id]['checks']:
                key = check['id']
                status = 'not-applicable' if key in na else 'not-measured' if key in pending else 'fail' if key in failures else 'pass'
                reason = ('No remote side effect exists in this stale-writer fixture.' if key in na else
                          '390px viewport could not be established through the available browser API.' if key in pending else
                          failures.get(key, note['basis']))
                criteria.append({**check, 'status':status, 'evidence':reason})
            total = sum(c['status'] in {'pass','fail'} for c in criteria)
            passed = sum(c['status']=='pass' for c in criteria)
            cases.append({'id':case_id,'category':rubrics[case_id]['category'],'passed':passed,'total':total,
                          'percent':100*passed/total, 'complete':not pending, 'checks':criteria,
                          'execution':execution, 'browser':browser, 'review_note':note['basis']})
        total=sum(c['total'] for c in cases); passed=sum(c['passed'] for c in cases)
        runs.append({'profile':profile,'cases':cases,'passed':passed,'total':total,'percent':100*passed/total,
                     'response_sha256':hashlib.sha256(response_path.read_bytes()).hexdigest()})
    result={'schema_version':1,'target_percent':95,'runs':runs,'valid_for_fair_comparison':False,
            'interpretation':'DEVELOPMENT ONLY: some test agents inherited parent history. Percentages are withdrawn from quality comparisons; the replacement isolated block is incomplete. Actual artifact executions retain their narrow test scope.'}
    (OUT/'review-results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    with (OUT/'category-results.csv').open('w',newline='',encoding='utf-8') as handle:
        writer=csv.writer(handle);writer.writerow(['category','condition','passed','measured','percent','complete'])
        for run in runs:
            for case in run['cases']:
                writer.writerow([case['category'],run['profile'],case['passed'],case['total'],f"{case['percent']:.1f}",case['complete']])
    print(json.dumps([{k:r[k] for k in ('profile','passed','total','percent')} for r in runs],indent=2))
    return result

if __name__=='__main__':compile_reviews()
