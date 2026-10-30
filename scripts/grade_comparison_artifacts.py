"""Run bounded, independently specified tests on inspected generated artifacts.

This is a narrow AST allowlist and time-limited child process, not a general
security sandbox. Imported upstream helpers are never executed.
"""
from __future__ import annotations
import argparse
import ast
import json
import math
from pathlib import Path
import subprocess
import string
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_MODULES = {"math", "decimal", "fractions"}
SAFE_CALLS = {"abs","all","any","bool","callable","object","dict","divmod","enumerate","filter","float","int","isinstance","iter","len","list","map","max","min","next","pow","range","reversed","round","set","sorted","str","sum","tuple","type","zip","ValueError","TypeError","AssertionError","fn","Decimal","Fraction"}
SAFE_ATTRIBUTES = {"exp","log","log1p","isfinite","isnan","isinf","fsum","sqrt","inf","nan","append","extend","sort","copy","quantize","to_integral_value","is_finite","numerator","denominator","ROUND_HALF_UP","ROUND_HALF_EVEN"}
FORBIDDEN_NAMES = {"open","eval","exec","compile","globals","locals","getattr","setattr","delattr","vars","dir","input","breakpoint","help","__import__","__builtins__"}


def inspect_source(source):
    tree = ast.parse(source)
    definitions = {n.name for n in ast.walk(tree) if isinstance(n,ast.FunctionDef)}
    # An empty local int subclass is a useful numeric-contract fixture, not a
    # general permission to execute class bodies, decorators or metaclasses.
    safe_classes=set()
    for node in ast.walk(tree):
        if isinstance(node,ast.ClassDef):
            if len(node.bases)!=1 or not isinstance(node.bases[0],ast.Name) or node.bases[0].id!='int' or node.keywords or node.decorator_list or not all(isinstance(item,ast.Pass) for item in node.body):
                raise ValueError("unsupported class fixture")
            safe_classes.add(node.name)
    public_imports={"math":{"exp","log","log1p","isfinite","isnan","isinf","fsum","sqrt"},"decimal":{"Decimal","ROUND_HALF_UP","ROUND_HALF_EVEN"},"fractions":{"Fraction"}}
    imported_calls=set()
    for node in tree.body:
        if not isinstance(node,(ast.FunctionDef,ast.Import,ast.ImportFrom,ast.Assign,ast.AnnAssign)) and not (isinstance(node,ast.Expr) and isinstance(node.value,ast.Constant) and isinstance(node.value.value,str)):
            raise ValueError("unexpected top-level executable statement")
    for node in ast.walk(tree):
        if isinstance(node,(ast.AsyncFunctionDef,ast.Global,ast.Nonlocal,ast.With,ast.AsyncWith)):
            raise ValueError("unsupported construct for this pure function fixture")
        if isinstance(node,ast.Name) and node.id in FORBIDDEN_NAMES:
            raise ValueError("forbidden name")
        if isinstance(node,ast.Attribute):
            error_type_name=(node.attr=="__name__" and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id=="type" and len(node.value.args)==1)
            error_type_name = error_type_name or (node.attr=="__name__" and isinstance(node.value,ast.Name) and node.value.id in {"expected_exc", "exception_type", "expected"})
            literal_format = False
            if node.attr == 'format' and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                try:
                    parts = list(string.Formatter().parse(node.value.value))
                    literal_format = all(field is None or ((field == '' or field.isdecimal()) and '{' not in spec and '}' not in spec) for _, field, spec, _ in parts)
                except ValueError:
                    pass
            if not error_type_name and not literal_format and (node.attr.startswith("_") or node.attr not in SAFE_ATTRIBUTES):
                raise ValueError("unsupported attribute")
        if isinstance(node,ast.Import):
            if any(a.name not in ALLOWED_MODULES for a in node.names):
                raise ValueError("non-allowlisted import")
        if isinstance(node,ast.ImportFrom) and (node.level or node.module not in ALLOWED_MODULES or any(a.name=="*" for a in node.names)):
            raise ValueError("non-allowlisted import")
        if isinstance(node,ast.ImportFrom):
            if any(a.name not in public_imports[node.module] for a in node.names):
                raise ValueError("unsupported imported symbol")
            imported_calls.update(a.asname or a.name for a in node.names)
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id not in SAFE_CALLS | definitions | imported_calls | safe_classes:
            raise ValueError(f"unsupported call: {node.func.id}")
        if isinstance(node,ast.Call) and not isinstance(node.func,(ast.Name,ast.Attribute)):
            raise ValueError("unsupported callable expression")
    return {"imports": [ast.unparse(n) for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom))], "functions":sorted(definitions)}


def close(actual, expected):
    if isinstance(expected,(list,tuple)):
        return isinstance(actual,(list,tuple)) and len(actual)==len(expected) and all(close(a,b) for a,b in zip(actual,expected))
    if isinstance(expected,float):
        return isinstance(actual,(int,float)) and math.isfinite(actual) and math.isclose(actual,expected,rel_tol=1e-7,abs_tol=1e-8)
    return type(actual) is type(expected) and actual==expected


def run_tests(category, split, source):
    compute_start=time.perf_counter()
    inspection=inspect_source(source)
    namespace={}
    exec(compile(source,"<generated-artifact>","exec"),namespace)
    records=[]
    def check(name,operation,expected):
        try:
            actual=operation()
            passed=close(actual,expected)
            error=None
        except Exception as exc:
            actual=None;passed=False;error=type(exc).__name__+": "+str(exc)[:180]
        records.append({"test":name,"passed":passed,"expected":repr(expected),"actual":repr(actual),"error":error})
    def raises(name,fn,args,kind):
        def operation():
            try: fn(*args)
            except kind: return True
            except Exception: return False
            return False
        check(name,operation,True)

    if category=="code-build" and split=="development":
        fn=namespace["total_cents"]
        for name,args,expected in [
            ("normal",([100,200],10),270),("half_cent_up",([1],50),1),
            ("aggregate_before_rounding",([1,2],50),2),("empty",([],10),0),
            ("full_discount",([1234],100),0),("zero_discount",([1234],0),1234),
            ("large_exact_integer",([9007199254740993],0),9007199254740993),
            ("round_half_up",([5],10),5)]:
            check(name,lambda args=args:fn(*args),expected)
        for i,args in enumerate([(None,0),((1,2),0),([True],0),([1.5],0),(["1"],0),([1],True),([1],1.5)]):
            raises(f"wrong_type_{i}",fn,args,TypeError)
        for i,args in enumerate([([-1],0),([1],-1),([1],101)]): raises(f"invalid_range_{i}",fn,args,ValueError)
    elif category=="code-build":
        fn=namespace["allocate_cents"]
        def oracle(total,weights):
            denominator=sum(weights)
            result=[total*w//denominator for w in weights]
            ranks=sorted(range(len(weights)),key=lambda i:(-(total*weights[i]%denominator),i))
            for i in ranks[:total-sum(result)]:result[i]+=1
            return result
        for name,total,weights in [("equal_tie",100,[1,1,1]),("proportional",7,[1,2]),("first_index_tie",1,[1,1]),("zero",0,[3,4]),("large_exact",10**18+1,[1,3,5]),("single",17,[8])]:
            check(name,lambda total=total,weights=weights:fn(total,weights),oracle(total,weights))
        for i,args in enumerate([(True,[1]),(1.0,[1]),(1,(1,2)),(1,[False]),(1,[1.1]),(None,[1])]):raises(f"wrong_type_{i}",fn,args,TypeError)
        for i,args in enumerate([(-1,[1]),(1,[]),(1,[0]),(1,[-2])]):raises(f"invalid_range_{i}",fn,args,ValueError)
    elif category=="neural-networks":
        binary=split=="development"
        fn=namespace["binary_loss_grad" if binary else "categorical_loss_grad"]
        if binary:
            def oracle(logits,targets):
                loss=sum(max(z,0)-z*y+math.log1p(math.exp(-abs(z))) for z,y in zip(logits,targets))/len(logits)
                def sigmoid(z):return 1/(1+math.exp(-z)) if z>=0 else math.exp(z)/(1+math.exp(z))
                return loss,[(sigmoid(z)-y)/len(logits) for z,y in zip(logits,targets)]
            samples=[("zeros",[0.,0.],[0,1]),("normal",[1.,-2.],[1,0]),("extreme_correct",[1000.,-1000.],[1,0]),("extreme_wrong",[1000.,-1000.],[0,1]),("unequal_batch",[.2,-.4,1.1],[1,0,1])]
            invalid=[([],[]),([0.],[0,1]),([float('nan')],[1]),([float('inf')],[0]),([0.],[2])]
        else:
            def oracle(logits,labels):
                losses=[];gradients=[]
                for row,label in zip(logits,labels):
                    shift=max(row);exps=[math.exp(z-shift) for z in row];total=sum(exps)
                    losses.append(shift+math.log(total)-row[label])
                    gradients.append([(value/total-(i==label))/len(logits) for i,value in enumerate(exps)])
                return sum(losses)/len(logits),gradients
            samples=[("zeros",[[0.,0.],[0.,0.]],[1,0]),("normal",[[3.,1.,-1.]],[2]),("extreme_correct",[[1000.,-1000.],[-1000.,1000.]],[0,1]),("extreme_wrong",[[1000.,-1000.],[-1000.,1000.]],[1,0]),("unequal_batch",[[.2,-.4,1.1],[.3,.1,-.2]],[2,0])]
            invalid=[([],[]),([[0.,0.]],[0,1]),([[0.,0.],[1.]],[0,0]),([[0.]],[0]),([[0.,0.]],[True]),([[0.,0.]],[1.0]),([[0.,0.]],[2]),([[float('nan'),0.]],[0])]
        for name,logits,labels in samples:check(name,lambda logits=logits,labels=labels:fn(logits,labels),oracle(logits,labels))
        for i,args in enumerate(invalid):raises(f"invalid_input_{i}",fn,args,ValueError)
        def numerical():
            logits=([.2,-.4,1.1] if binary else [[.2,-.4,1.1],[.3,.1,-.2]])
            labels=([1,0,1] if binary else [2,0]);eps=1e-5
            _,grad=fn(logits,labels)
            positions=[(None,i) for i in range(len(logits))] if binary else [(i,j) for i,row in enumerate(logits) for j in range(len(row))]
            for i,j in positions:
                values=logits if i is None else logits[i]
                original=values[j]
                try:
                    values[j]=original+eps;plus=fn(logits,labels)[0]
                    values[j]=original-eps;minus=fn(logits,labels)[0]
                finally:values[j]=original
                analytic=grad[j] if i is None else grad[i][j]
                if not math.isclose((plus-minus)/(2*eps),analytic,rel_tol=1e-5,abs_tol=1e-7):return False
            return True
        check("central_difference_gradients",numerical,True)
    elif category=="testing":
        checker=namespace["check_contract"]
        if split=="development":
            def correct(value):
                if type(value) is not int:raise TypeError()
                return max(0,min(100,value))
            def constant(value):
                correct(value);return 0
            def identity(value):
                correct(value);return value
            def lower(value):
                correct(value);return max(1,min(100,value))
            def upper(value):
                correct(value);return max(0,min(99,value))
            def boolean(value):
                if isinstance(value,bool):return int(value)
                return correct(value)
            def floating(value):
                if isinstance(value,float):return max(0,min(100,value))
                return correct(value)
        else:
            def correct(value):
                if isinstance(value,bool) or not isinstance(value,int):raise TypeError()
                if not 1<=value<=65535:raise ValueError()
                return value
            def constant(value):correct(value);return 80
            def identity(value):
                if type(value)is not int:raise TypeError()
                return value
            def lower(value):
                if value==0:return 0
                return correct(value)
            def upper(value):
                if value==65536:return value
                return correct(value)
            def boolean(value):
                if isinstance(value,bool):return int(value)
                return correct(value)
            def floating(value):
                if isinstance(value,float) and 1<=value<=65535:return value
                return correct(value)
        def accepts():checker(correct);return True
        check("accepts_correct_implementation",accepts,True)
        valid=records[-1]["passed"]
        for name,mutant in [("constant",constant),("identity",identity),("lower",lower),("upper",upper),("boolean",boolean),("floating",floating)]:
            def detects(mutant=mutant):
                if not valid:return False
                try:checker(mutant)
                except Exception:return True
                return False
            check("detects_"+name,detects,True)
    else:
        raise ValueError("No executable fixture for this category")
    return {"category":category,"split":split,"passed":sum(r["passed"] for r in records),"total":len(records),"tests":records,"inspection":inspection,"compute_seconds":time.perf_counter()-compute_start,
            "scope":"Actual generated pure-function/test code executed in an isolated child; no IDE execution or production claim."}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source",type=Path)
    parser.add_argument("--category",required=True,choices=["code-build","neural-networks","testing"])
    parser.add_argument("--split",required=True,choices=["development","holdout"])
    parser.add_argument("--output",type=Path)
    parser.add_argument("--child",action="store_true")
    parser.add_argument("--timeout",type=int,default=30,choices=range(10,61),help="Wall-clock allowance including Windows process startup; pure function compute is separately limited")
    args=parser.parse_args()
    if args.child:
        import os
        import threading
        timer=threading.Timer(5,lambda:os._exit(124))
        timer.daemon=True
        timer.start()
        try:report=run_tests(args.category,args.split,args.source.read_text(encoding="utf-8"))
        except Exception as exc:report={"category":args.category,"split":args.split,"passed":0,"total":0,"error":type(exc).__name__+": "+str(exc)[:300]}
        finally:timer.cancel()
        print(json.dumps(report,indent=2));return
    inspect_source(args.source.read_text(encoding="utf-8"))
    command=[sys.executable,"-I","-S",str(Path(__file__).resolve()),str(args.source.resolve()),"--category",args.category,"--split",args.split,"--child"]
    start=time.monotonic()
    try:
        result=subprocess.run(command,cwd=args.source.parent,capture_output=True,text=True,encoding="utf-8",timeout=args.timeout)
        if result.returncode==124:
            report={"category":args.category,"split":args.split,"passed":0,"total":0,"error":"Pure-function compute exceeded 5 seconds"}
        else:
            report=json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        report={"category":args.category,"split":args.split,"passed":0,"total":0,"error":f"Child process exceeded {args.timeout} seconds including startup"}
    report['child_wall_seconds']=time.monotonic()-start
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
