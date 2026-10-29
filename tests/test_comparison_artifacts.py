import importlib.util
from pathlib import Path

import pytest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("comparison_artifacts",ROOT/"scripts/grade_comparison_artifacts.py")
grader=importlib.util.module_from_spec(spec)
spec.loader.exec_module(grader)


def test_numeric_benchmark_catches_the_actual_truncation_and_float_failure():
    wrong='def total_cents(prices, discount_percent):\n    return int(sum(prices)*(1-discount_percent/100))\n'
    report=grader.run_tests("code-build","development",wrong)
    results={item['test']:item['passed'] for item in report['tests']}
    assert results['normal']
    assert not results['half_cent_up']
    assert not results['large_exact_integer']
    assert report['passed'] < report['total']


def test_mutation_score_does_not_reward_a_checker_that_fails_everything():
    report=grader.run_tests("testing","holdout","def check_contract(fn):\n    assert False\n")
    assert report['passed']==0
    assert all(not item['passed'] for item in report['tests'])


@pytest.mark.parametrize('source',[
    "import os\ndef total_cents(prices, discount_percent): return 0",
    "def check_contract(fn):\n    open('sensitive-file')",
    "from math import __loader__ as exp\ndef check_contract(fn):\n    exp()",
    "def check_contract(fn):\n    return fn.__globals__",
])
def test_fixture_inspection_rejects_unrelated_capabilities_before_execution(source):
    with pytest.raises(ValueError):grader.inspect_source(source)


def test_common_pure_numeric_operations_remain_available():
    info=grader.inspect_source("from math import exp\ndef allocate_cents(total, weights):\n    if type(total) is not int: raise TypeError()\n    return [divmod(total, len(weights))[0]]\n")
    assert info['functions']==['allocate_cents']
