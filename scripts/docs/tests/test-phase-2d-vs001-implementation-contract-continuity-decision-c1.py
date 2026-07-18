#!/usr/bin/env python3
"""Focused semantic mutations for the continuity decision pack."""
from __future__ import annotations
import copy,importlib.util,json,os,shutil,subprocess,tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location("continuity_validator",ROOT/"scripts/docs/validate-phase-2d-vs001-implementation-contract-continuity-decision-c1.py")
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)

def killed(base,mutate,code):
    p=copy.deepcopy(base);mutate(p)
    try:v.validate(p,check_files=False)
    except v.DecisionError as e:
        if code!=str(e).split(":",1)[0]:raise AssertionError(f"wrong reason: expected {code}, got {e}")
        return
    raise AssertionError(f"survived: {code}")

def semantic_mutations(p):
    loc=lambda q:next(x for x in q["decisions"] if x["decision_id"].endswith("001"))
    snap=lambda q:next(x for x in q["decisions"] if x["decision_id"].endswith("002"))
    cases=[
      (lambda q:loc(q).update({"selected_option":"OPT-QORDER-EXACT-THEN-STOREFRONT-DEFAULT"}),"HUMAN_SELECTION_NOT_NULL"),
      (lambda q:loc(q)["options"].pop(),"OPTION_INVENTORY_OR_RECOMMENDATION_MISMATCH"),
      (lambda q:q["authority"].update({"canonical_blob_sha256":"0"*64}),"DECLARED_AUTHORITY_HASH_MISMATCH"),
      (lambda q:next(o for o in loc(q)["options"] if o["option_id"]==loc(q)["recommended_option"])["algorithm"].update({"priority":"use arbitrary server order"}),"LOCALE_SEMANTIC_MISMATCH"),
      (lambda q:next(o for o in loc(q)["options"] if o["option_id"]==loc(q)["recommended_option"])["algorithm"].update({"q_zero":"q=0 is preferred"}),"LOCALE_SEMANTIC_MISMATCH"),
      (lambda q:next(o for o in snap(q)["options"] if o["option_id"]==snap(q)["recommended_option"])["contract"].update({"request_snapshot":"one PostgreSQL transaction automatically spans every HTTP request"}),"SNAPSHOT_CONTINUITY_SEMANTIC_MISMATCH"),
      (lambda q:next(o for o in snap(q)["options"] if o["option_id"]==snap(q)["recommended_option"])["contract"].update({"cleanup":"retain the server snapshot forever"}),"SNAPSHOT_CONTINUITY_SEMANTIC_MISMATCH"),
      (lambda q:q.update({"implementation_authorized":True}),"FALSE_AUTHORIZATION_OR_RUNTIME_CLAIM"),
      (lambda q:q.update({"runtime_evidence_status":"PASS"}),"FALSE_AUTHORIZATION_OR_RUNTIME_CLAIM"),
    ]
    for mutate,code in cases:killed(p,mutate,code)
    return len(cases)

def builder_probes():
    probes=[
      ('for g in p["authority_gap_findings"]:', 'for g in p["authority_gap_findings"][:1]:',"MARKDOWN_GAP_PROJECTION_MISSING"),
      ('for d in p["decisions"]:', 'for d in p["decisions"][:1]:',"MARKDOWN_OPTION_PROJECTION_MISSING"),
      ('for o in d["options"]:', 'for o in d["options"][:2]:',"MARKDOWN_OPTION_PROJECTION_MISSING"),
    ]
    for n,(old,new,code) in enumerate(probes,1):
      with tempfile.TemporaryDirectory(prefix=f"continuity-builder-probe-{n}-") as td:
        root=Path(td)
        for rel in v.FILES:
          dst=root/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,dst)
        bp=root/v.BUILDER_REL;src=bp.read_text();assert old in src;bp.write_text(src.replace(old,new,1),newline="\n")
        subprocess.run(["python3",str(bp)],cwd=root,check=True,stdout=subprocess.DEVNULL)
        p=json.loads((root/v.JSON_REL).read_bytes())
        try:v.validate(p,root,True)
        except v.DecisionError as e:
          if str(e).split(":",1)[0]!=code:raise AssertionError(f"probe {n} wrong reason: {e}")
          continue
        raise AssertionError(f"builder probe {n} survived")
    return len(probes)

def main():
    p=json.loads((ROOT/v.JSON_REL).read_bytes());v.validate(p,check_files=True)
    m=semantic_mutations(p);b=builder_probes()
    print("VALID_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_CONTINUITY_DECISION_C1_TESTS",json.dumps({"semantic_mutations":m,"modified_builder_probes":b,"killed":m+b,"survivors":0,"wrong_reason":0,"no_op":0},sort_keys=True))
if __name__=="__main__":main()
