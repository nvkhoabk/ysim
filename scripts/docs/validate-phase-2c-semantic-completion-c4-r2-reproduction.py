#!/usr/bin/env python3
"""Independently reproduce C4-R2 fixtures and all 531 executions.

This module intentionally does not import the C4-R2 generator or its mutation
helpers. Mutation is reconstructed from stored canonical fixture bytes.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

import operator_binding_type_checker as checker


ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"
FIXTURES = P2 / "semantic-completion-c4-r2-fixtures.json"
EXECUTIONS = P2 / "semantic-completion-c4-r2-execution-results.json"


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(value if isinstance(value, bytes) else canonical(value)).hexdigest()


def decode_pointer(pointer: str) -> list[str]:
    if not isinstance(pointer, str) or not pointer.startswith("/") or pointer == "/":
        raise AssertionError("INVALID_JSON_POINTER")
    return [item.replace("~1", "/").replace("~0", "~") for item in pointer[1:].split("/")]


def locate(document: Any, pointer: str) -> Any:
    current = document
    for token in decode_pointer(pointer):
        if not isinstance(current, dict) or token not in current:
            raise AssertionError("MISSING_MUTATION_TARGET")
        current = current[token]
    return current


def assign(document: Any, pointer: str, replacement: Any) -> None:
    tokens = decode_pointer(pointer)
    current = document
    for token in tokens[:-1]:
        if not isinstance(current, dict) or token not in current:
            raise AssertionError("MISSING_MUTATION_TARGET")
        current = current[token]
    if not isinstance(current, dict) or tokens[-1] not in current:
        raise AssertionError("MISSING_MUTATION_TARGET")
    current[tokens[-1]] = copy.deepcopy(replacement)


def leaf_differences(left: Any, right: Any, prefix: str = "") -> list[str]:
    if type(left) is not type(right):
        return [prefix or "/"]
    if isinstance(left, dict):
        result: list[str] = []
        for key in sorted(set(left) | set(right)):
            child = f"{prefix}/{key}"
            if key not in left or key not in right:
                result.append(child)
            else:
                result.extend(leaf_differences(left[key], right[key], child))
        return result
    if isinstance(left, list):
        if len(left) != len(right):
            return [prefix or "/"]
        result: list[str] = []
        for index in range(len(left)):
            result.extend(leaf_differences(left[index], right[index], f"{prefix}/{index}"))
        return result
    return [] if left == right else [prefix or "/"]


def replacement_for(original: dict[str, Any], mutation: dict[str, Any]) -> Any:
    current = copy.deepcopy(locate(original, mutation["target"]))
    kind = mutation["mutation_kind"]
    if kind == "SEMANTIC_DIFFERENCE":
        generic = checker._generic_inner(current.get("semantic_type", "")) if isinstance(current, dict) else None
        if generic and generic[0] == "SET_OF":
            if not current.get("members"):
                raise AssertionError("EMPTY_MUTATION_SET")
            member = current["members"][0]
            member["identifier"] = member["identifier"] + ".MUTANT"
            allowlist = member.get("authoritative_source", {}).get("allowed_identifiers")
            if isinstance(allowlist, list):
                allowlist.append(member["identifier"])
        elif isinstance(current, dict) and current.get("semantic_type") == "BOOLEAN":
            current["value"] = not current["value"]
        elif isinstance(current, dict) and current.get("semantic_type") == "TIMESTAMP":
            current["value"] = "2026-07-17T00:00:00+07:00"
        elif isinstance(current, dict) and isinstance(current.get("value"), (int, float)):
            current["value"] = current["value"] + 1
        elif isinstance(current, dict) and isinstance(current.get("identifier"), str):
            current["identifier"] = current["identifier"] + ".MUTANT"
            allowlist = current.get("authoritative_source", {}).get("allowed_identifiers")
            if isinstance(allowlist, list):
                allowlist.append(current["identifier"])
        else:
            raise AssertionError("UNSUPPORTED_SEMANTIC_MUTATION_TARGET")
        return current
    if kind == "ORIGIN_COLLISION":
        return locate(original, "/validation_fixture/comparison/expected/origin/origin_id")
    if kind == "EVIDENCE_OBJECT_REMOVED":
        return {"missing": True}
    raise AssertionError("UNKNOWN_MUTATION")


def independently_mutate(fixture_bytes: bytes, mutation: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    original = json.loads(fixture_bytes)
    if canonical(original) != fixture_bytes:
        raise AssertionError("NONCANONICAL_FIXTURE_INPUT")
    protected = (original.get("fixture_id"), original.get("fixture_sha256"), canonical(original.get("source_provenance")))
    replacement = replacement_for(original, mutation)
    if replacement == locate(original, mutation["target"]):
        raise AssertionError("NO_OP_MUTATION")
    mutant = json.loads(fixture_bytes)
    assign(mutant, mutation["target"], replacement)
    differences = leaf_differences(original, mutant)
    target = mutation["target"].rstrip("/")
    if not differences or not all(item == target or item.startswith(target + "/") for item in differences):
        raise AssertionError("MUTATION_ESCAPED_TARGET")
    after = (mutant.get("fixture_id"), mutant.get("fixture_sha256"), canonical(mutant.get("source_provenance")))
    if after != protected:
        raise AssertionError("FIXTURE_IDENTITY_OR_PROVENANCE_CHANGED")
    return mutant, differences


def validate_r031(vf: dict[str, Any], types: dict[str, Any]) -> None:
    if vf.get("operator_id") != "SET_EQUALS" or vf.get("generic_set_type_parameter") != "REFERENCE_ID":
        raise checker.TypeModelError("R031_OPERATOR_OR_PARAMETER")
    expected_ref, observed_ref = vf["bindings"]["expected_set"], vf["bindings"]["actual_set"]
    requirements = [
        (expected_ref, "CANONICAL_SET_REF<REFERENCE_ID>", "VERSIONED_CONFIGURATION", "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE", "AFFECTED_NODE_REFERENCES", "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES"),
        (observed_ref, "RUNTIME_SET_REF<REFERENCE_ID>", "RUNTIME_OBSERVED", "YSIM.CONFIGURATION_IMPACT_ANALYSIS.NODE_REFERENCE", "REPORTED_AFFECTED_NODE_REFERENCES", "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES"),
    ]
    for ref, semantic_type, origin, namespace, identifier, resolver in requirements:
        if ref.get("semantic_type") != semantic_type or ref.get("origin", {}).get("origin_type") != origin:
            raise checker.TypeModelError("R031_REFERENCE_TYPE_OR_ORIGIN")
        if (ref.get("namespace"), ref.get("identifier"), ref.get("resolver_contract", {}).get("resolver_id")) != (namespace, identifier, resolver):
            raise checker.TypeModelError("R031_REFERENCE_IDENTITY")
        if set(ref.get("allowed_target_types", [])) != {"CONFIGURATION_KEY", "CAPABILITY_ID"}:
            raise checker.TypeModelError("R031_TARGET_TYPES")
        if ref.get("resolver_contract", {}).get("output_type") != "SET_OF<REFERENCE_ID>":
            raise checker.TypeModelError("R031_RESOLVER_OUTPUT")
    if expected_ref["origin"]["origin_id"] == observed_ref["origin"]["origin_id"]:
        raise checker.TypeModelError("R031_ORIGIN_COLLISION")
    for side, origin in (("expected", "VERSIONED_CONFIGURATION"), ("observed", "RUNTIME_OBSERVED")):
        value = vf["comparison"][side]
        if value.get("semantic_type") != "SET_OF<REFERENCE_ID>" or value.get("origin", {}).get("origin_type") != origin:
            raise checker.TypeModelError("R031_COMPARISON_TYPE")
        for member in value.get("members", []):
            if member.get("semantic_type") != "REFERENCE_ID" or member.get("target_type") not in {"CONFIGURATION_KEY", "CAPABILITY_ID"}:
                raise checker.TypeModelError("R031_MEMBER_TYPE")
    if vf["comparison"]["expected"]["origin"]["origin_id"] == vf["comparison"]["observed"]["origin"]["origin_id"]:
        raise checker.TypeModelError("R031_COMPARISON_ORIGIN_COLLISION")
    checker.validate_value(vf.get("evidence_object"), "EVIDENCE_OBJECT_REF", ["EVIDENCE_OBJECT", "SYNTHETIC_MODEL_FIXTURE"], types, "evidence_object")


def evaluate(vf: dict[str, Any], schemas: dict[str, Any], types: dict[str, Any]) -> tuple[str, str | None]:
    try:
        if vf.get("generic_set_type_parameter") == "REFERENCE_ID":
            validate_r031(vf, types)
            expected = {(x["target_type"], x["identifier"]) for x in vf["comparison"]["expected"]["members"]}
            observed = {(x["target_type"], x["identifier"]) for x in vf["comparison"]["observed"]["members"]}
            return ("PASS", None) if expected == observed else ("FAIL", "comparison")
        schema = schemas[vf["operator_id"]]
        checker.validate_fixture(vf, schema, types)
        return ("PASS", None) if checker.evaluate_fixture(vf, schema, types) else ("FAIL", "comparison")
    except (checker.TypeModelError, AssertionError, KeyError) as exc:
        return "FAIL", str(exc)


def main() -> int:
    fixture_payload = json.loads(FIXTURES.read_text())
    execution_payload = json.loads(EXECUTIONS.read_text())
    types = json.loads((P2 / "operator-binding-semantic-types.json").read_text())
    schemas = {item["operator_id"]: item for item in json.loads((P2 / "operator-binding-schemas.json").read_text())["schemas"]}
    fixtures = {item["fixture_id"]: item for item in fixture_payload["fixtures"]}
    if fixture_payload["fixture_count"] != len(fixtures) or len(fixtures) != 177:
        raise AssertionError("FIXTURE_ACCOUNTING")
    for fixture in fixtures.values():
        body = {key: value for key, value in fixture.items() if key not in {"fixture_id", "fixture_sha256"}}
        if digest(body) != fixture["fixture_sha256"]:
            raise AssertionError("FIXTURE_HASH:" + fixture["fixture_id"])
        if evaluate(fixture["validation_fixture"], schemas, types) != ("PASS", None):
            raise AssertionError("FIXTURE_BASELINE:" + fixture["fixture_id"])

    rows = execution_payload["results"]
    if execution_payload["execution_result_count"] != len(rows) or len(rows) != 531:
        raise AssertionError("EXECUTION_ACCOUNTING")
    kinds: dict[str, int] = {}
    for stored in rows:
        fixture = fixtures[stored["fixture_id"]]
        if fixture["fixture_sha256"] != stored["fixture_sha256"]:
            raise AssertionError("FIXTURE_LINK:" + stored["execution_id"])
        mutation = stored["mutation_definition"]
        if digest(mutation) != stored["mutation_definition_sha256"]:
            raise AssertionError("MUTATION_DEFINITION_HASH:" + stored["execution_id"])
        mutant, paths = independently_mutate(canonical(fixture), mutation)
        if digest(mutant) != stored["mutated_fixture_sha256"]:
            raise AssertionError("MUTANT_HASH:" + stored["execution_id"])
        if paths != stored["changed_paths"]:
            raise AssertionError("MUTATION_PATHS:" + stored["execution_id"])
        baseline = evaluate(fixture["validation_fixture"], schemas, types)
        mutated = evaluate(mutant["validation_fixture"], schemas, types)
        if baseline != ("PASS", None) or mutated[0] != "FAIL":
            raise AssertionError("EXECUTION_OUTCOME:" + stored["execution_id"])
        if stored["baseline_evaluation"] != baseline[0] or stored["mutant_evaluation"] != mutated[0] or stored["failed_identifier"] != mutated[1]:
            raise AssertionError("STORED_RESULT_NOT_REPRODUCED:" + stored["execution_id"])
        if stored["actual_detection"] != "MODEL_CONFORMANCE_REJECTED" or stored["runtime_execution"] is not False:
            raise AssertionError("FALSE_RUNTIME_CLAIM:" + stored["execution_id"])
        kinds[mutation["mutation_kind"]] = kinds.get(mutation["mutation_kind"], 0) + 1
    if kinds != {"SEMANTIC_DIFFERENCE": 177, "ORIGIN_COLLISION": 177, "EVIDENCE_OBJECT_REMOVED": 177}:
        raise AssertionError("MUTATION_KIND_ACCOUNTING")
    mandatory = next(item for item in rows if item["execution_id"] == "EXEC.P2C-C4-FX-61047493F1B6BF01933A-M1")
    if mandatory["mutated_fixture_sha256"] != "23f0cd102050f812c1da9aae80b21421d17b1ae146f2f557ba1182bfc194ca00":
        raise AssertionError("MANDATORY_ISOLATED_HASH")
    if mandatory["mutated_fixture_sha256"] == "e9aa0328aced18ee1d6c181b6a0b1039423764202aaedb92488955a82fea6711":
        raise AssertionError("ALIASED_HASH_ACCEPTED")
    print("PASS — INDEPENDENT_C4_R2_FIXTURE_REPRODUCTION 177/177")
    print("PASS — INDEPENDENT_C4_R2_EXECUTION_REPRODUCTION 531/531")
    print("PASS — MUTATION_KINDS 177/177/177; SURVIVORS 0")
    print("PASS — MANDATORY_ALIAS_REGRESSION ISOLATED_HASH")
    print("PASS — RUNTIME_MUTATION_SCORE N/A_NOT_EXECUTED")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, checker.TypeModelError, KeyError, json.JSONDecodeError) as exc:
        print("FAIL — " + str(exc))
        raise SystemExit(1)
