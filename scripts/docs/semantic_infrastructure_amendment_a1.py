#!/usr/bin/env python3
"""Core checks for the Phase 2C semantic infrastructure amendment A1."""

from __future__ import annotations

import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"
CANDIDATE_ID = "V23-P2C-SEMANTIC-INFRASTRUCTURE-AMENDMENT-A1"
BASE_COMMIT = "c11d95116154ff8919c04b49b0a502cf66b3907d"
ORACLE_COMMIT = "77d10a8c3ccb2e7795724fd1c82cdbea36c54e2e"
C4_REF = "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c4-blocked"
C4_OBJECT = "24037270c435a80210ab00f1b20f2a38c92ea36f"
C4_TREE = "897079721b3e8a808f363480d554e88dc9f8f284"
C4_AGGREGATE = "f2c57653024f28f47f80bbaf2da3110bf3d80417a606382613d431db802ededc"


class AmendmentError(ValueError):
    pass


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(value if isinstance(value, bytes) else canonical(value)).hexdigest()


def git_output(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def backup_json(path: str) -> dict[str, Any]:
    raw = subprocess.check_output(["git", "show", f"{C4_REF}^3:{path}"], cwd=ROOT)
    return json.loads(raw)


def parse_generic(type_name: str) -> tuple[str, str] | None:
    match = re.fullmatch(r"(CANONICAL_SET_REF|RUNTIME_SET_REF|SET_OF)<([A-Z][A-Z0-9_]*)>", type_name)
    return (match.group(1), match.group(2)) if match else None


def _require(condition: bool, code: str) -> None:
    if not condition:
        raise AmendmentError(code)


def _looks_like_prose(value: str) -> bool:
    return bool(re.search(r"\s", value) or re.search(r"[.!?]$", value))


def validate_reference(reference: dict[str, Any], expected_type: str, allowed_origins: set[str]) -> None:
    required = {
        "namespace", "identifier", "semantic_type", "authoritative_source",
        "resolver_contract", "lifecycle", "origin", "provenance", "inference",
    }
    _require(required <= set(reference), "MISSING_REFERENCE_FIELD")
    _require(reference["semantic_type"] == expected_type, "REFERENCE_TYPE_MISMATCH")
    _require(reference["inference"] is False, "INFERENCE_FORBIDDEN")
    identifier = reference["identifier"]
    _require(isinstance(identifier, str) and identifier and not _looks_like_prose(identifier), "INVALID_IDENTIFIER_SHAPE")
    tokens = set(re.split(r"[.:-]", identifier.upper()))
    _require(not ({"EXPECTED_SET", "ACTUAL_SET", "EXPECTED", "ACTUAL"} & tokens), "SCHEMA_DERIVED_IDENTIFIER")
    _require(reference["origin"].get("origin_type") in allowed_origins, "ORIGIN_NOT_ALLOWED")
    _require(bool(reference["origin"].get("origin_id")), "MISSING_ORIGIN_ID")
    authority = reference["authoritative_source"]
    _require(bool(authority.get("source_type")) and bool(authority.get("source_id")), "MISSING_AUTHORITY")
    resolver = reference["resolver_contract"]
    _require(bool(resolver.get("resolver_id")), "MISSING_RESOLVER")
    _require(resolver.get("deterministic") is True, "NONDETERMINISTIC_RESOLVER")
    _require(bool(resolver.get("version")), "MISSING_RESOLVER_VERSION")
    _require(bool(reference["lifecycle"].get("status")) and bool(reference["lifecycle"].get("version")), "MISSING_LIFECYCLE")
    _require(reference["provenance"].get("inference") is False, "PROVENANCE_INFERENCE_FORBIDDEN")
    generic = parse_generic(expected_type)
    if generic:
        member_type = generic[1]
        for member in reference.get("resolved_members", []):
            _require(isinstance(member, dict), "INVALID_SET_MEMBER")
            _require(member.get("semantic_type") == member_type, "SET_MEMBER_TYPE_MISMATCH")
            member_id = member.get("identifier")
            _require(isinstance(member_id, str) and member_id and not _looks_like_prose(member_id), "INVALID_SET_MEMBER")
            if member_type == "REFERENCE_ID":
                _require(bool(member.get("target_type")), "MISSING_REFERENCE_TARGET_TYPE")


def validate_generic_set_contract(contract: dict[str, Any], amendment: dict[str, Any]) -> None:
    operator = contract["operator_id"]
    schemas = {item["operator_id"]: item for item in amendment["operators"]}
    _require(operator in schemas, "OPERATOR_NOT_AMENDED")
    schema = schemas[operator]
    type_parameter = contract["type_parameter"]
    _require(type_parameter in amendment["allowed_type_parameters"], "UNKNOWN_TYPE_PARAMETER")
    expected_name = schema["expected_binding_name"]
    observed_name = schema["observed_binding_name"]
    expected = contract[expected_name]
    observed = contract[observed_name]
    validate_reference(expected, f"CANONICAL_SET_REF<{type_parameter}>", set(schema["expected_origins"]))
    validate_reference(observed, f"RUNTIME_SET_REF<{type_parameter}>", set(schema["observed_origins"]))
    _require(expected["resolver_contract"].get("output_type") == f"SET_OF<{type_parameter}>", "EXPECTED_RESOLVER_OUTPUT_MISMATCH")
    _require(observed["resolver_contract"].get("output_type") == f"SET_OF<{type_parameter}>", "OBSERVED_RESOLVER_OUTPUT_MISMATCH")
    _require(expected["origin"]["origin_id"] != observed["origin"]["origin_id"], "ORIGIN_COLLISION")
    _require(expected["resolver_contract"]["resolver_id"] != observed["resolver_contract"]["resolver_id"], "RESOLVER_COLLISION")
    _require(expected["authoritative_source"]["source_id"] != observed["authoritative_source"]["source_id"], "AUTHORITY_COLLISION")
    if type_parameter == "REFERENCE_ID":
        expected_targets = set(expected.get("allowed_target_types", []))
        observed_targets = set(observed.get("allowed_target_types", []))
        _require(expected_targets == observed_targets and expected_targets, "REFERENCE_TARGET_TYPE_MISMATCH")
        allowed_targets = set(amendment["reference_target_types"])
        _require(expected_targets <= allowed_targets, "UNKNOWN_TARGET_TYPE")
    evidence = set(contract.get("required_evidence_fields", []))
    _require(evidence and all(item.startswith("FIELD.") and not _looks_like_prose(item) for item in evidence), "INVALID_EVIDENCE_FIELD")


def pointer_get(value: Any, pointer: str) -> Any:
    _require(pointer.startswith("/"), "INVALID_JSON_POINTER")
    current = value
    for token in pointer.split("/")[1:]:
        token = token.replace("~1", "/").replace("~0", "~")
        _require(isinstance(current, dict) and token in current, "MISSING_MUTATION_TARGET")
        current = current[token]
    return current


def pointer_set(value: Any, pointer: str, replacement: Any) -> None:
    parts = pointer.split("/")[1:]
    _require(bool(parts), "INVALID_JSON_POINTER")
    current = value
    for raw in parts[:-1]:
        token = raw.replace("~1", "/").replace("~0", "~")
        _require(isinstance(current, dict) and token in current, "MISSING_MUTATION_TARGET")
        current = current[token]
    key = parts[-1].replace("~1", "/").replace("~0", "~")
    _require(isinstance(current, dict) and key in current, "MISSING_MUTATION_TARGET")
    current[key] = copy.deepcopy(replacement)


def changed_paths(left: Any, right: Any, path: str = "") -> list[str]:
    if type(left) is not type(right):
        return [path or "/"]
    if isinstance(left, dict):
        rows: list[str] = []
        for key in sorted(set(left) | set(right)):
            child = f"{path}/{key}"
            if key not in left or key not in right:
                rows.append(child)
            else:
                rows.extend(changed_paths(left[key], right[key], child))
        return rows
    if isinstance(left, list):
        if len(left) != len(right):
            return [path or "/"]
        rows = []
        for index, (a, b) in enumerate(zip(left, right)):
            rows.extend(changed_paths(a, b, f"{path}/{index}"))
        return rows
    return [] if left == right else [path or "/"]


def mutation_replacement(fixture: dict[str, Any], mutation: dict[str, Any]) -> Any:
    kind = mutation["mutation_kind"]
    target = mutation["target"]
    current = copy.deepcopy(pointer_get(fixture, target))
    if kind == "SEMANTIC_DIFFERENCE":
        generic = parse_generic(current.get("semantic_type", "")) if isinstance(current, dict) else None
        if generic and generic[0] == "SET_OF":
            member = current["members"][0]
            member["identifier"] = member["identifier"] + ".MUTANT"
            allowed = member.get("authoritative_source", {}).get("allowed_identifiers")
            if isinstance(allowed, list):
                allowed.append(member["identifier"])
        elif isinstance(current, dict) and current.get("semantic_type") == "BOOLEAN":
            current["value"] = not current["value"]
        elif isinstance(current, dict) and current.get("semantic_type") == "TIMESTAMP":
            current["value"] = "2026-07-17T00:00:00+07:00"
        elif isinstance(current, dict) and "value" in current and isinstance(current["value"], (int, float)):
            current["value"] += 1
        elif isinstance(current, dict) and "identifier" in current:
            current["identifier"] = current["identifier"] + ".MUTANT"
            allowed = current.get("authoritative_source", {}).get("allowed_identifiers")
            if isinstance(allowed, list):
                allowed.append(current["identifier"])
        else:
            raise AmendmentError("UNSUPPORTED_SEMANTIC_MUTATION_TARGET")
        return current
    if kind == "ORIGIN_COLLISION":
        return pointer_get(fixture, "/validation_fixture/comparison/expected/origin/origin_id")
    if kind == "EVIDENCE_OBJECT_REMOVED":
        return {"missing": True}
    raise AmendmentError("UNKNOWN_MUTATION")


def apply_isolated_mutation(fixture_bytes: bytes, mutation: dict[str, Any]) -> tuple[bytes, list[str]]:
    fixture = json.loads(fixture_bytes)
    _require(canonical(fixture) == fixture_bytes, "NONCANONICAL_FIXTURE_INPUT")
    original_identity = (fixture.get("fixture_id"), fixture.get("fixture_sha256"), canonical(fixture.get("source_provenance")))
    replacement = mutation_replacement(fixture, mutation)
    _require(replacement != pointer_get(fixture, mutation["target"]), "NO_OP_MUTATION")
    mutant = json.loads(fixture_bytes)
    pointer_set(mutant, mutation["target"], replacement)
    diffs = changed_paths(fixture, mutant)
    _require(bool(diffs), "NO_OP_MUTATION")
    allowed_prefix = mutation["target"].rstrip("/")
    _require(all(path == allowed_prefix or path.startswith(allowed_prefix + "/") for path in diffs), "MUTATION_ISOLATION_VIOLATION")
    mutated_identity = (mutant.get("fixture_id"), mutant.get("fixture_sha256"), canonical(mutant.get("source_provenance")))
    _require(original_identity == mutated_identity, "PROTECTED_FIXTURE_IDENTITY_CHANGED")
    return canonical(mutant), diffs


def impact_audit() -> dict[str, Any]:
    fixture_payload = backup_json("docs/baselines/v2.3/phase-2/semantic-completion-c4-fixtures.json")
    execution_payload = backup_json("docs/baselines/v2.3/phase-2/semantic-completion-c4-execution-results.json")
    fixtures = {item["fixture_id"]: item for item in fixture_payload["fixtures"]}
    rows = []
    counts: dict[str, dict[str, int]] = {}
    for execution in execution_payload["results"]:
        mutation = execution["mutation_definition"]
        fixture_bytes = canonical(fixtures[execution["fixture_id"]])
        mutant_bytes, paths = apply_isolated_mutation(fixture_bytes, mutation)
        reproduced_hash = digest(mutant_bytes)
        matched = reproduced_hash == execution["mutated_fixture_sha256"]
        kind = mutation["mutation_kind"]
        bucket = counts.setdefault(kind, {"total": 0, "matched": 0, "vulnerable": 0})
        bucket["total"] += 1
        bucket["matched" if matched else "vulnerable"] += 1
        rows.append({
            "execution_id": execution["execution_id"],
            "fixture_id": execution["fixture_id"],
            "mutation_kind": kind,
            "target": mutation["target"],
            "stored_hash": execution["mutated_fixture_sha256"],
            "isolated_hash": reproduced_hash,
            "status": "REPRODUCED" if matched else "REQUIRES_FUTURE_REGENERATION",
            "changed_paths": paths,
        })
    return {
        "fixture_count": len(fixtures),
        "execution_count": len(rows),
        "counts": counts,
        "vulnerable_hash_count": sum(item["vulnerable"] for item in counts.values()),
        "reproduced_hash_count": sum(item["matched"] for item in counts.values()),
        "execution_impacts": rows,
    }


def alias_regression() -> dict[str, Any]:
    fixtures = {item["fixture_id"]: item for item in backup_json("docs/baselines/v2.3/phase-2/semantic-completion-c4-fixtures.json")["fixtures"]}
    executions = backup_json("docs/baselines/v2.3/phase-2/semantic-completion-c4-execution-results.json")["results"]
    fixture_id = "P2C-C4-FX-61047493F1B6BF01933A"
    execution_id = "EXEC.P2C-C4-FX-61047493F1B6BF01933A-M1"
    fixture = fixtures[fixture_id]
    execution = next(item for item in executions if item["execution_id"] == execution_id)
    fixture_bytes = canonical(fixture)
    isolated_bytes, isolated_paths = apply_isolated_mutation(fixture_bytes, execution["mutation_definition"])
    aliased = json.loads(fixture_bytes)
    aliased["observed_state"] = aliased["validation_fixture"]["comparison"]["observed"]
    replacement = mutation_replacement(aliased, execution["mutation_definition"])
    aliased_target = pointer_get(aliased, execution["mutation_definition"]["target"])
    _require(isinstance(aliased_target, dict) and isinstance(replacement, dict), "ALIAS_REGRESSION_TARGET_SHAPE")
    aliased_target.clear()
    aliased_target.update(replacement)
    aliased_bytes = canonical(aliased)
    aliased_paths = changed_paths(json.loads(fixture_bytes), aliased)
    target = execution["mutation_definition"]["target"]
    rejected = any(not (path == target or path.startswith(target + "/")) for path in aliased_paths)
    return {
        "fixture_id": fixture_id,
        "execution_id": execution_id,
        "target": target,
        "isolated_hash": digest(isolated_bytes),
        "required_isolated_hash": "23f0cd102050f812c1da9aae80b21421d17b1ae146f2f557ba1182bfc194ca00",
        "isolated_changed_paths": isolated_paths,
        "aliased_hash": digest(aliased_bytes),
        "required_rejected_hash": "e9aa0328aced18ee1d6c181b6a0b1039423764202aaedb92488955a82fea6711",
        "aliased_changed_paths": aliased_paths,
        "aliased_result_rejected": rejected,
    }


def adversarial_results(amendment: dict[str, Any], valid_example: dict[str, Any]) -> list[dict[str, Any]]:
    results = []
    expected_name_by_operator = {item["operator_id"]: item["expected_binding_name"] for item in amendment["operators"]}
    for operator in ("SET_EQUALS", "SET_CONTAINS", "SET_EXCLUDES"):
        base = copy.deepcopy(valid_example)
        base["operator_id"] = operator
        expected_name = expected_name_by_operator[operator]
        if expected_name != "expected_set":
            base[expected_name] = base.pop("expected_set")

        cases: list[tuple[str, Any, str | None]] = []
        cases.append(("VALID_REFERENCE_SET", copy.deepcopy(base), None))
        mismatch = copy.deepcopy(base); mismatch["type_parameter"] = "CAPABILITY_ID"
        cases.append(("MISMATCHED_T", mismatch, "REFERENCE_TYPE_MISMATCH"))
        same_origin = copy.deepcopy(base); same_origin["actual_set"]["origin"]["origin_id"] = same_origin[expected_name]["origin"]["origin_id"]
        cases.append(("SAME_ORIGIN", same_origin, "ORIGIN_COLLISION"))
        sentence = copy.deepcopy(base); sentence[expected_name]["resolved_members"] = ["All affected members are returned"]
        cases.append(("SENTENCE_SET_MEMBER", sentence, "INVALID_SET_MEMBER"))
        no_resolver = copy.deepcopy(base); del no_resolver[expected_name]["resolver_contract"]["resolver_id"]
        cases.append(("MISSING_RESOLVER", no_resolver, "MISSING_RESOLVER"))
        unknown_target = copy.deepcopy(base); unknown_target[expected_name]["allowed_target_types"] = ["UNKNOWN_TARGET"]; unknown_target["actual_set"]["allowed_target_types"] = ["UNKNOWN_TARGET"]
        cases.append(("UNKNOWN_TARGET_TYPE", unknown_target, "UNKNOWN_TARGET_TYPE"))
        schema_name = copy.deepcopy(base); schema_name[expected_name]["identifier"] = "EXPECTED_SET"
        cases.append(("SCHEMA_DERIVED_IDENTIFIER", schema_name, "SCHEMA_DERIVED_IDENTIFIER"))
        same_authority = copy.deepcopy(base); same_authority["actual_set"]["authoritative_source"]["source_id"] = same_authority[expected_name]["authoritative_source"]["source_id"]
        cases.append(("SAME_EVIDENCE_SOURCE", same_authority, "AUTHORITY_COLLISION"))
        prose_member = copy.deepcopy(base); prose_member[expected_name]["identifier"] = "The expected set equals the observed set."
        cases.append(("PROSE_LABEL", prose_member, "INVALID_IDENTIFIER_SHAPE"))
        actual_name = copy.deepcopy(base); actual_name["actual_set"]["identifier"] = "ACTUAL_SET"
        cases.append(("ACTUAL_SCHEMA_IDENTIFIER", actual_name, "SCHEMA_DERIVED_IDENTIFIER"))

        for case_id, candidate, expected_error in cases:
            actual_error = None
            try:
                validate_generic_set_contract(candidate, amendment)
            except AmendmentError as exc:
                actual_error = str(exc)
            passed = actual_error == expected_error
            results.append({
                "operator_id": operator,
                "case_id": case_id,
                "expected": "PASS" if expected_error is None else f"REJECT:{expected_error}",
                "actual": "PASS" if actual_error is None else f"REJECT:{actual_error}",
                "result": "PASS" if passed else "FAIL",
            })
    return results
