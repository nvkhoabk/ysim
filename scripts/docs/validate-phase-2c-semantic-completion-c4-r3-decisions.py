#!/usr/bin/env python3
"""Independent decision-contract audit for C4-R3; does not import the generator."""

from __future__ import annotations

import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any


ROOT=Path(__file__).resolve().parents[2]
HEAD="522442635eb0df24dd5de0d42dad84656a5920e0"
P2=ROOT/"docs/baselines/v2.3/phase-2"
DEC=P2/"semantic-completion-c4-r3-decision-contract-options.json"
AUD=P2/"semantic-completion-c4-r3-decision-audit.json"
DEP=P2/"semantic-completion-c4-r3-dependency-overlap-register.json"
PROV=P2/"semantic-completion-c4-r3-source-provenance-register.json"


def req(ok: bool, message: str) -> None:
    if not ok: raise AssertionError(message)


def load(path: Path) -> dict[str,Any]: return json.loads(path.read_text())


def git_source(path: str) -> list[str]:
    return subprocess.check_output(["git","show",f"{HEAD}:{path}"],cwd=ROOT,text=True).splitlines()


def all_refs(node: dict[str,Any]):
    yield from node["expected_bindings"].values();yield from node["observed_bindings"].values()
    yield node["expected_assertion"];yield node["observed_assertion"];yield node["evidence_contract"]["evidence_object"]


def validate_ref(ref: dict[str,Any], label: str) -> None:
    required={"namespace","identifier","semantic_type","cardinality","authoritative_source","resolver","origin","provenance","inference"}
    req(required<=set(ref),"binding fields:"+label);req(ref["inference"] is False,"binding inference:"+label)
    req(all(ref[k] for k in ("namespace","identifier","semantic_type","authoritative_source","resolver","origin","provenance")),"binding empty:"+label)
    req(ref["resolver"].get("resolver_id") and ref["resolver"].get("version") and ref["resolver"].get("output"),"resolver:"+label)
    req(ref["origin"].get("origin_id") and ref["origin"].get("origin_type"),"origin:"+label)


def validate_contract(contract: dict[str,Any], schemas: dict[str,Any], decision: dict[str,Any]) -> None:
    req(contract["inference"] is False and contract["verification_mode"]=="MODEL_CONFORMANCE_DEFINED_RUNTIME_ADAPTER_PENDING","contract mode")
    obligations={x["obligation_id"] for x in contract["obligations"]};covered=[]
    req(obligations and contract["ast_nodes"],"empty AST")
    for node in contract["ast_nodes"]:
        req(node["operator_id"] in schemas,"unsupported operator:"+node["operator_id"]);schema=schemas[node["operator_id"]]
        expected_required={b["name"] for b in schema["bindings"] if not set(b["allowed_origins"])<={"RUNTIME_OBSERVED","EVIDENCE_OBJECT","SYNTHETIC_MODEL_FIXTURE"}}
        observed_required={b["name"] for b in schema["bindings"] if set(b["allowed_origins"])<={"RUNTIME_OBSERVED","EVIDENCE_OBJECT","SYNTHETIC_MODEL_FIXTURE"}}
        req(set(node["expected_bindings"])==expected_required,"expected schema bindings:"+node["node_id"])
        req(set(node["observed_bindings"])==observed_required,"observed schema bindings:"+node["node_id"])
        for name,ref in [(k,v) for k,v in node["expected_bindings"].items()]+[(k,v) for k,v in node["observed_bindings"].items()]: validate_ref(ref,node["node_id"]+":"+name)
        validate_ref(node["expected_assertion"],node["node_id"]+":expected");validate_ref(node["observed_assertion"],node["node_id"]+":observed")
        req(node["expected_comparison_binding"]==node["expected_assertion"] and node["observed_comparison_binding"]==node["observed_assertion"],"comparison bindings")
        req(node["expected_origin"]["origin_id"]!=node["observed_origin"]["origin_id"],"same origin:"+node["node_id"])
        ev=node["evidence_contract"];validate_ref(ev["evidence_object"],node["node_id"]+":evidence")
        req(len(ev["required_fields"])>=5 and ev["expected_collection_origin"]!=ev["observed_collection_origin"],"evidence completeness")
        req(node["positive_oracle"] and node["negative_oracle"].get("prohibited_state") and node["boundary_oracle"].get("left")!=node["boundary_oracle"].get("right"),"oracles")
        req(node["runtime_adapter"]["status"]=="SLICE_RUNTIME_ADAPTER_REQUIRED" and node["runtime_adapter"]["runtime_evidence_executed"] is False,"runtime claim")
        covered.extend(node["covers_obligations"])
        forbidden={"ACTUAL_SET","EXPECTED_SET","REQUIRED_MEMBERS","PROHIBITED_MEMBERS","EXPECTED_OUTCOME","ACTUAL_VALUE","EXPECTED_VALUE"}
        for ref in all_refs(node): req(not any(token in ref["identifier"].split(".") for token in forbidden),"schema-derived identifier:"+ref["identifier"])
    req(set(covered)==obligations and set(contract["obligation_coverage"])==obligations,"obligation loss/injection:"+decision["decision_id"])
    req("runtime" in contract["acceptance_implication"].lower(),"acceptance implication")


def main() -> int:
    decisions=load(DEC);audit=load(AUD);deps=load(DEP);prov=load(PROV)
    schemas={x["operator_id"]:x for x in json.loads(subprocess.check_output(["git","show",f"{HEAD}:docs/baselines/v2.3/phase-2/operator-binding-schemas.json"],cwd=ROOT))["schemas"]}
    rows=decisions["decisions"];req(len(rows)==decisions["decision_count"]==27,"decision count");req(decisions["selected_count"]==0,"selected count")
    req(len({x["decision_id"] for x in rows})==len({x["requirement_id"] for x in rows})==27,"decision identity")
    results=Counter()
    for d in rows:
        req(d["selected_option"] is None and d["status"]==d["approval_status"]=="PENDING_HUMAN_APPROVAL","selection status")
        src=d["source_provenance"];start,end=map(int,src["source_lines"].removeprefix("L").split("-L"));actual="\n".join(git_source(src["source_document"])[start-1:end])
        req(actual==src["exact_source_excerpt"]==d["exact_source_excerpt"],"source range:"+d["decision_id"])
        req(src["inference"] is False and src["source_fingerprint"],"source provenance")
        option_ids=[o["option_id"] for o in d["available_options"]];req(len(option_ids)==len(set(option_ids))>=2,"option identity")
        req(d["recommended_option"] in option_ids,"recommended option")
        for option in d["available_options"]:
            req(option.get("consequence") and option.get("inference") is False,"truthful option consequence")
            if "provisional_contract" in option: validate_contract(option["provisional_contract"],schemas,d)
            else: req(option.get("human_procedure"),"option missing AST/procedure")
            if option.get("source_edit_required"):
                req(option.get("source_clarification") or option.get("creates_business_semantics") is True,"source-edit disclosure")
        rec=next(o for o in d["available_options"] if o["option_id"]==d["recommended_option"])
        if d["audit_result"]=="SAFE_TO_APPROVE_RECOMMENDED_OPTION": req("provisional_contract" in rec,"safe recommendation lacks AST")
        elif d["audit_result"]=="BUSINESS_DECISION_OPTION_READY": req(d["decision_id"].endswith(("004","013")) and len(d["available_options"])==3,"business options")
        else: raise AssertionError("unready audit result:"+d["decision_id"])
        req(d["non_inferences"] and d["runtime_adapter_impact"]=="REMAINS_PENDING","decision nonclaims")
        results[d["audit_result"]]+=1
    req(results==Counter({"SAFE_TO_APPROVE_RECOMMENDED_OPTION":25,"BUSINESS_DECISION_OPTION_READY":2}),"audit distribution")
    req(audit["distribution"]=={"SAFE_TO_APPROVE_RECOMMENDED_OPTION":25,"BUSINESS_DECISION_OPTION_READY":2,"REQUIRES_ALTERNATIVE_OPTION":0,"REQUIRES_INDIVIDUAL_HUMAN_REVIEW":0,"INVALID_OR_BLOCKED":0},"stored audit")
    req(all(audit[k]==0 for k in ("false_option_effect_claims","missing_recommended_ast_or_binding","incorrect_source_ranges","lost_obligations","unresolved_overlaps","hidden_runtime_claims","hidden_yadf_authorizations")),"audit gates")
    req(deps["unresolved_overlaps"]==0 and deps["dependency_order"]==["P2C-SC-C1-DEC-021","P2C-SC-C1-DEC-022","P2C-SC-C1-DEC-026","P2C-SC-C1-DEC-027"],"dependency ordering")
    req(prov["record_count"]==27 and prov["incorrect_ranges"]==0 and all(x["result"]=="PASS_EXACT_GIT_OBJECT_RANGE" for x in prov["records"]),"provenance register")
    print("PASS — C4_R3_DECISIONS 27/27 COMPLETE")
    print("PASS — SAFE_RECOMMENDATIONS 25 BUSINESS_OPTION_PACKS 2")
    print("PASS — SOURCE_RANGES 27/27 AST_BINDINGS_ORIGINS_RESOLVERS_EVIDENCE COMPLETE")
    print("PASS — FALSE_OPTION_EFFECTS 0 LOST_OBLIGATIONS 0 UNRESOLVED_OVERLAPS 0")
    return 0


if __name__=="__main__":
    try: raise SystemExit(main())
    except (AssertionError,KeyError,json.JSONDecodeError,subprocess.CalledProcessError) as exc:
        print("FAIL — "+str(exc));raise SystemExit(1)
