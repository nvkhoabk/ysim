#!/usr/bin/env python3
"""Validate Operator Binding Type Model C1 independently of its generator."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any, Callable

import operator_binding_type_checker as checker

ROOT=Path(__file__).resolve().parents[2]
P2=ROOT/"docs/baselines/v2.3/phase-2"
BASE="77d10a8c3ccb2e7795724fd1c82cdbea36c54e2e"
CANDIDATE="V23-P2C-OPERATOR-BINDING-TYPE-MODEL-C1"


def fail(message: str) -> None:
    raise SystemExit("FAIL — "+message)


def load(name: str) -> dict[str, Any]:
    return json.loads((P2/name).read_text())


def git_json(spec: str) -> dict[str, Any]:
    return json.loads(subprocess.check_output(["git","show",spec],cwd=ROOT))


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def aggregate(items: dict[str, bytes]) -> str:
    digest=hashlib.sha256()
    for path in sorted(items):digest.update(path.encode()+b"\0"+items[path]+b"\0")
    return digest.hexdigest()


def valid_fixture(schema: dict[str, Any], catalog: dict[str, Any]) -> dict[str, Any]:
    bindings={}
    for index,definition in enumerate(schema["bindings"]):
        origin=definition["allowed_origins"][0]
        bindings[definition["name"]]=checker.typed_value(definition["semantic_type"],origin,f"BINDING.{schema['operator_id']}.{index}",identifier=f"{schema['operator_id']}.{definition['name'].upper()}")
    semantic_type=schema["comparison_contract"]["semantic_type"]
    expected=checker.typed_value(semantic_type,"CANONICAL_REGISTRY",f"EXPECTED.{schema['operator_id']}",identifier=f"{schema['operator_id']}.VALUE")
    observed=checker.typed_value(semantic_type,"RUNTIME_OBSERVED",f"OBSERVED.{schema['operator_id']}",identifier=f"{schema['operator_id']}.VALUE")
    if "resolver_contract" in observed:observed["resolver_contract"]["resolver_id"]="OBSERVE."+semantic_type.replace("<",".").replace(">","")
    evidence=checker.typed_value("EVIDENCE_OBJECT_REF","EVIDENCE_OBJECT",f"EVIDENCE.{schema['operator_id']}",identifier=f"{schema['operator_id']}.EVIDENCE")
    return {"operator_id":schema["operator_id"],"bindings":bindings,"comparison":{"expected":expected,"observed":observed},"evidence_object":evidence}


def must_fail(fn: Callable[[], Any], code: str) -> None:
    try:fn()
    except checker.TypeModelError:return
    fail(f"adversarial test did not fail:{code}")


def mutate_identifier(value: dict[str, Any]) -> None:
    generic=checker._generic_inner(value["semantic_type"])
    if generic and generic[0]=="SET_OF":
        member=value["members"][0];member["identifier"]="MUTATED.2"
        source=member.get("authoritative_source",{})
        if "allowed_identifiers" in source:source["allowed_identifiers"].append("MUTATED.2")
    elif value["semantic_type"] in checker.PRIMITIVES:
        if value["semantic_type"]=="BOOLEAN":value["value"]=not value["value"]
        elif value["semantic_type"]=="TIMESTAMP":value["value"]="2026-07-16T00:00:00+07:00"
        else:value["value"]+=1
    else:
        value["identifier"]="MUTATED.2"
        source=value.get("authoritative_source",{})
        if "allowed_identifiers" in source:source["allowed_identifiers"].append("MUTATED.2")


def run_adversarial(schema: dict[str, Any], catalog: dict[str, Any]) -> list[dict[str, str]]:
    base=valid_fixture(schema,catalog)
    checker.validate_fixture(base,schema,catalog)
    if not checker.evaluate_fixture(base,schema,catalog):fail(f"valid comparison failed:{schema['operator_id']}")
    results=[{"test_id":"VALID_INDEPENDENTLY_SOURCED_FIXTURE","result":"PASS"}]
    case=copy.deepcopy(base);case["comparison"]={"expected":"The requirement is satisfied.","observed":"The requirement is satisfied."}
    must_fail(lambda:checker.validate_fixture(case,schema,catalog),"SENTENCE_COPY_EXPECTED_OBSERVED");results.append({"test_id":"SENTENCE_COPY_EXPECTED_OBSERVED","result":"FAIL_CLOSED"})
    case=copy.deepcopy(base);first=schema["bindings"][0]["name"];case["bindings"][first]="The complete requirement statement is true."
    must_fail(lambda:checker.validate_fixture(case,schema,catalog),"WHOLE_REQUIREMENT_AS_SCALAR");results.append({"test_id":"WHOLE_REQUIREMENT_AS_SCALAR","result":"FAIL_CLOSED"})
    case=copy.deepcopy(base);case["bindings"][first]={"semantic_type":"SET_OF<FIELD_ID>","members":["A sentence used as a member."],"origin":{"origin_type":"CANONICAL_REGISTRY","origin_id":"SET.BAD"},"provenance":{"source_fingerprint":"A"*64,"inference":False}}
    must_fail(lambda:checker.validate_fixture(case,schema,catalog),"SENTENCE_AS_SET_MEMBER");results.append({"test_id":"SENTENCE_AS_SET_MEMBER","result":"FAIL_CLOSED"})
    case=copy.deepcopy(base);target=checker.typed_value("STATE_ID","CANONICAL_REGISTRY",f"EXPECTED.{schema['operator_id']}.UNKNOWN",identifier="UNKNOWN.STATE");target["authoritative_source"]["allowed_identifiers"]=["KNOWN.STATE"];case["comparison"]["expected"]=target
    must_fail(lambda:checker.validate_fixture(case,schema,catalog),"UNKNOWN_ENUM_OR_STATE");results.append({"test_id":"UNKNOWN_ENUM_OR_STATE","result":"FAIL_CLOSED"})
    case=copy.deepcopy(base);symbolic=next((name for name,value in case["bindings"].items() if "resolver_contract" in value),None)
    if symbolic is None:symbolic="evidence_object";case["evidence_object"].pop("resolver_contract")
    else:case["bindings"][symbolic].pop("resolver_contract")
    must_fail(lambda:checker.validate_fixture(case,schema,catalog),"MISSING_AUTHORITATIVE_RESOLVER");results.append({"test_id":"MISSING_AUTHORITATIVE_RESOLVER","result":"FAIL_CLOSED"})
    case=copy.deepcopy(base);case["comparison"]["observed"]["origin"]["origin_id"]=case["comparison"]["expected"]["origin"]["origin_id"]
    must_fail(lambda:checker.validate_fixture(case,schema,catalog),"SAME_EXPECTED_OBSERVED_ORIGIN");results.append({"test_id":"SAME_EXPECTED_OBSERVED_ORIGIN","result":"FAIL_CLOSED"})
    case=copy.deepcopy(base);case["evidence_object"]="observed:EVIDENCE_FIELD_PRESENT:evidence_object"
    must_fail(lambda:checker.validate_fixture(case,schema,catalog),"EVIDENCE_LABEL_AS_OBJECT");results.append({"test_id":"EVIDENCE_LABEL_AS_OBJECT","result":"FAIL_CLOSED"})
    case=copy.deepcopy(base);definition=schema["bindings"][0];wrong="TENANT_ID" if definition["semantic_type"]!="TENANT_ID" else "ENTITY_ID";case["bindings"][definition["name"]]["semantic_type"]=wrong
    must_fail(lambda:checker.validate_fixture(case,schema,catalog),"WRONG_TYPED_IDENTIFIER");results.append({"test_id":"WRONG_TYPED_IDENTIFIER","result":"FAIL_CLOSED"})
    case=copy.deepcopy(base);mutate_identifier(case["comparison"]["observed"]);checker.validate_fixture(case,schema,catalog)
    if checker.evaluate_fixture(case,schema,catalog):fail(f"real difference undetected:{schema['operator_id']}")
    results.append({"test_id":"REAL_MUTATED_DIFFERENCE","result":"DETECTED"})
    return results


def main() -> int:
    manifest=load("operator-binding-type-model-manifest.json");types=load("operator-binding-semantic-types.json");schemas=load("operator-binding-schemas.json");disp=load("operator-binding-type-dispositions.json");decisions=load("operator-binding-source-clarification-decisions.json");matrix=load("operator-binding-type-adversarial-matrix.json")
    if (manifest["candidate_id"],manifest["status"],manifest["approval_status"],manifest["next_gate"])!=(CANDIDATE,"CANDIDATE","PENDING_HUMAN_APPROVAL","HUMAN_OPERATOR_BINDING_TYPE_MODEL_AND_SOURCE_CLARIFICATION_APPROVAL"):fail("candidate identity")
    generated={}
    for path,expected in manifest["file_sha256"].items():
        data=(ROOT/path).read_bytes()
        if sha(data)!=expected:fail("payload hash "+path)
        generated[path]=data
    if aggregate(generated)!=manifest["generated_payload_aggregate_sha256"]:fail("generated aggregate")
    accepted=git_json(f"{BASE}:docs/baselines/v2.3/phase-2/oracle-operator-catalog.json")
    accepted_by={item["operator_id"]:item for item in accepted["operators"]};schema_by={item["operator_id"]:item for item in schemas["schemas"]}
    if schemas["schema_count"]!=40 or set(schema_by)!=set(accepted_by):fail("40 operator schema coverage")
    for op,schema in schema_by.items():
        if not set(accepted_by[op]["required_bindings"])<={item["name"] for item in schema["bindings"]}:fail("accepted binding completeness "+op)
        if any(not item["semantic_type"] or not item["allowed_origins"] or not item["resolver_required"] and item["semantic_type"] not in checker.PRIMITIVES for item in schema["bindings"]):fail("schema details "+op)
    if not {"ENTITY_ID","REFERENCE_ID","STATE_ID","EVIDENCE_OBJECT_REF"}<=set(types["types"]):fail("semantic type catalog")
    mandatory_fields={
      "AUDIT_IMMUTABLE":{"audit_record","protected_fields","before_hash","after_hash","immutability_boundary"},
      "REFERENCE_TARGET_VALID":{"reference","target_id","target_type","registry_source","allowed_lifecycle_states"},
      "POLICY_OUTCOME_EQUALS":{"policy","policy_version","policy_inputs","expected_outcome"},
      "CONFIGURATION_PRECEDENCE":{"configuration_key","source_values","source_versions","precedence_order","resolved_source","resolved_value"},
      "CONFIGURATION_RESOLVES":{"configuration_key","configuration_sources","source_versions","resolved_source","expected_value"},
    }
    for op,names in mandatory_fields.items():
        if not names<={item["name"] for item in schema_by[op]["bindings"]}:fail("mandatory semantic fields "+op)
    actual_rows=[]
    for schema in schemas["schemas"]:actual_rows.append({"operator_id":schema["operator_id"],"tests":run_adversarial(schema,types)})
    if sum(len(row["tests"]) for row in actual_rows)!=400:fail("adversarial accounting")
    if matrix["operator_count"]!=40 or matrix["total_tests"]!=400 or {row["operator_id"] for row in matrix["rows"]}!=set(schema_by):fail("adversarial matrix")
    if disp["record_count"]!=59 or len({item["requirement_id"] for item in disp["records"]})!=59:fail("59 dispositions")
    if disp["counts"]!={"COMPOUND_AST_REQUIRED":6,"CORRECTABLE_WITH_APPROVED_TYPE_MODEL":35,"OPERATOR_REMAP_REQUIRED":12,"SOURCE_CLARIFICATION_REQUIRED":6}:fail("disposition totals")
    if any(item["regeneration_applied"] or not item["recommended_operator_composition"] or not item["correct_semantic_types"] for item in disp["records"]):fail("terminal disposition detail")
    mandatory={"BRD-WS-02-R003","BRD-WS-07-R014","BRD-WS-08-R004","BRD-WS-14-R031","EP-17-002"}
    if {item["requirement_id"] for item in disp["records"] if item["mandatory_audit_record"]}!=mandatory:fail("mandatory record coverage")
    if decisions["decision_count"]!=6 or decisions["selected_count"] or len(decisions["decisions"])!=6:fail("clarification accounting")
    for item in decisions["decisions"]:
        if item["approval_status"]!="PENDING_HUMAN_APPROVAL" or item["selected_option"] is not None or len(item["options"])!=2 or not item["recommended"]:fail("decision pending/options "+item["requirement_id"])
        if any(not option["source_wording"] or not option["consequence"] for option in item["options"]):fail("decision wording "+item["requirement_id"])
    refs={
      "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c3-r1-rejected^2^{tree}":"92fb9de65f2fd6b5be888a271ab4ab245798eb9d",
      "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c3-blocked^{tree}":"19bf019617e5f6672a45b85247bdea9d9103b73f",
      "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c2-blocked^{tree}":"6973e1f4b09b59198d3eb2103dbc9e381125a480",
      "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c1-blocked^{tree}":"3241762b05565c813a590df4032c2587d9c14f3e",
      "refs/ysim-backups/v2.3/phase-2c-document-baseline-c4-blocked^2^{tree}":"ef678c7da248f3595ac01cd585355469b12d76b0",
      "refs/ysim-backups/v2.3/phase-2c-semantic-oracle-model-c1-rejected^{tree}":"e7fe153e8402ca9d7a3ec7832a9d1df9f438a3bf",
    }
    for spec,tree in refs.items():
        if subprocess.check_output(["git","rev-parse",spec],cwd=ROOT,text=True).strip()!=tree:fail("backup ref "+spec)
    changed=subprocess.check_output(["git","diff","--name-only",BASE],cwd=ROOT,text=True).splitlines()
    if any(path.startswith(("docs/BRD/","docs/UXF/")) for path in changed):fail("BRD/UXF boundary")
    print("PASS — VALID_OPERATOR_BINDING_TYPE_MODEL_C1")
    print("PASS — OPERATOR_SCHEMAS 40/40")
    print("PASS — ADVERSARIAL_TYPE_TESTS 400/400 sentence_copy_rejected=40/40")
    print("PASS — DISPOSITIONS 59/59")
    print("PASS — SOURCE_CLARIFICATION_DECISIONS 6/6 PENDING")
    return 0


if __name__=="__main__":raise SystemExit(main())
