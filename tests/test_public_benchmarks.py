"""Reconcile public claims with the actual category rows and retained evidence."""
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def test_public_pilot_totals_reconcile_and_missing_ui_is_not_zero():
    data=json.loads((ROOT/'web/benchmarks/benchmark-data.json').read_text())
    assert len(data['categories'])==180
    for total in data['totals']:
        rows=[r for r in data['categories'] if (r['host'],r['profile'])==(total['host'],total['profile'])]
        assert len(rows)==30
        ui=next(r for r in rows if r['category']=='web-frontend')
        assert not ui['complete'] and ui['percent'] is None
        measured=[r for r in rows if r['complete'] and r['category']!='web-frontend']
        assert len(measured)==29
        assert sum(r['passed'] for r in measured)==total['passed']
        assert sum(r['total'] for r in measured)==total['total']==173
        assert abs(total['percent']-100*total['passed']/total['total'])<1e-10
    assert all(r['safe_controls_flagged']==0 and r['found']==r['seeded']==6 for r in data['security'])

def test_public_evidence_sources_are_identifiable_and_preserved():
    data=json.loads((ROOT/'web/benchmarks/benchmark-data.json').read_text())
    assert 'Historical' in data['pilot_label'] and len(data['limitations'])>=5
    assert next(r for r in data['routing'] if r['kind']=='normal')['matched']==18
    assert len(data['footprint'])==30
    for relative,digest in data['sources'].items():
        source=ROOT/relative
        # Full raw trial evidence is in Git; source distributions keep the chart snapshot.
        if source.exists():assert hashlib.sha256(source.read_bytes()).hexdigest()==digest,relative
    review=ROOT/'web-results/comparison/review-results.json'
    if review.exists():
        raw=json.loads(review.read_text())
        for row in data['categories']:
            run=next(r for r in raw['runs'] if r['host']==row['host'] and r['profile']==row['profile'] and r['split']=='holdout')
            case=next(c for c in run['cases'] if c['category']==row['category'])
            assert (row['passed'],row['total'],row['complete'])==(case['passed'],case['total'],case['complete'])
