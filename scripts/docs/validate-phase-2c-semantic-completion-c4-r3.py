#!/usr/bin/env python3
"""Validate C4-R3 manifest, technical-core lock, decisions and boundaries."""
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2];P2=ROOT/"docs/baselines/v2.3/phase-2"
R2_REF="refs/ysim-backups/v2.3/phase-2c-semantic-completion-c4-r2-decision-incomplete"
MAN=P2/"semantic-completion-c4-r3-manifest.json"

def req(x,m):
    if not x: raise AssertionError(m)

def main():
    m=json.loads(MAN.read_text());req(m["candidate_id"]=="V23-P2C-SEMANTIC-COMPLETION-C4-R3" and m["status"]=="CANDIDATE" and m["approval_status"]=="PENDING_HUMAN_APPROVAL","identity")
    req(m["r2_preservation"]["backup_object"]==subprocess.check_output(["git","rev-parse",R2_REF],cwd=ROOT,text=True).strip(),"R2 ref")
    req(m["r2_preservation"]["index_tree"]==subprocess.check_output(["git","rev-parse",R2_REF+"^{tree}"],cwd=ROOT,text=True).strip(),"R2 tree")
    for p,h in m["per_file_sha256_excluding_manifest"].items(): req(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,"hash:"+p)
    for p in m["technical_core"]["byte_identical_paths"]: req((ROOT/p).read_bytes()==subprocess.check_output(["git","show",R2_REF+":"+p],cwd=ROOT),"core changed:"+p)
    delta=json.loads((P2/"semantic-completion-c4-r2-mutation-delta.json").read_text());req(delta["derived_primary_category_counts"]=={"R031_TYPED_FIXTURE_CHANGE":9,"SCHEMA_IDENTIFIER_NORMALIZATION":81,"MUTATION_ISOLATION_RECOMPUTATION":294,"UNCHANGED":147,"UNEXPECTED_CHANGE":0},"delta")
    fixtures=json.loads((P2/"semantic-completion-c4-r2-fixtures.json").read_text());executions=json.loads((P2/"semantic-completion-c4-r2-execution-results.json").read_text());contracts=json.loads((P2/"semantic-completion-c4-r2-custom-contracts.json").read_text());procedures=json.loads((P2/"semantic-completion-c4-r2-procedures.json").read_text())
    req((len(contracts["contracts"]),sum(len(x["assertions"]) for x in contracts["contracts"]),len(fixtures["fixtures"]),len(executions["results"]),len(procedures["procedures"]))==(59,79,177,531,156),"core counts")
    req(executions["runtime_mutation_score"] is None and executions["survived"]==0,"runtime/survivors")
    r=subprocess.run([sys.executable,str(ROOT/"scripts/docs/validate-phase-2c-semantic-completion-c4-r3-decisions.py")],cwd=ROOT,text=True,capture_output=True);print(r.stdout,end="");req(r.returncode==0,"decision validator")
    r=subprocess.run([sys.executable,str(ROOT/"scripts/docs/validate-phase-2c-semantic-completion-c4-r2-reproduction.py")],cwd=ROOT,text=True,capture_output=True);print(r.stdout,end="");req(r.returncode==0,"execution reproduction")
    r=subprocess.run([sys.executable,str(ROOT/"scripts/docs/build-phase-2c-semantic-completion-c4-r3.py"),"--check"],cwd=ROOT,text=True,capture_output=True);print(r.stdout,end="");req(r.returncode==0,"determinism")
    changed=set(subprocess.check_output(["git","diff","--name-only","522442635eb0df24dd5de0d42dad84656a5920e0"],cwd=ROOT,text=True).splitlines())|set(subprocess.check_output(["git","ls-files","--others","--exclude-standard"],cwd=ROOT,text=True).splitlines())
    req(changed<=set(m["exact_inventory"]),"unexpected path");req(not any(p.startswith(("docs/BRD/","docs/UXF/")) for p in changed),"source changed")
    print("PASS — VALID_PHASE_2C_SEMANTIC_COMPLETION_C4_R3")
    print("PASS — TECHNICAL_CORE_BYTE_IDENTICAL 59/79/177/531/156")
    return 0
if __name__=="__main__":
    try: raise SystemExit(main())
    except (AssertionError,KeyError,json.JSONDecodeError,subprocess.CalledProcessError) as e: print("FAIL — "+str(e));raise SystemExit(1)
