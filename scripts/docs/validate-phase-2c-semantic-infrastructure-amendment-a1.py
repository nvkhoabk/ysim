#!/usr/bin/env python3
"""Validate Phase 2C semantic infrastructure amendment A1."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import semantic_infrastructure_amendment_a1 as core


ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def load_json(path: str) -> dict[str, Any]:
    return json.loads((ROOT / path).read_text())


def backup_json(path: str) -> dict[str, Any]:
    return json.loads(subprocess.check_output(["git", "show", f"{core.C4_REF}^3:{path}"], cwd=ROOT))


def get_pointer(value: Any, pointer: str) -> Any:
    require(pointer.startswith("/"), "invalid pointer")
    current = value
    for raw in pointer.split("/")[1:]:
        key = raw.replace("~1", "/").replace("~0", "~")
        require(isinstance(current, dict) and key in current, "missing target")
        current = current[key]
    return current


def set_pointer(value: Any, pointer: str, replacement: Any) -> None:
    parts = pointer.split("/")[1:]
    require(bool(parts), "invalid pointer")
    current = value
    for raw in parts[:-1]:
        key = raw.replace("~1", "/").replace("~0", "~")
        require(isinstance(current, dict) and key in current, "missing target")
        current = current[key]
    key = parts[-1].replace("~1", "/").replace("~0", "~")
    require(isinstance(current, dict) and key in current, "missing target")
    current[key] = copy.deepcopy(replacement)


def independent_replacement(fixture: dict[str, Any], mutation: dict[str, Any]) -> Any:
    current = copy.deepcopy(get_pointer(fixture, mutation["target"]))
    kind = mutation["mutation_kind"]
    if kind == "SEMANTIC_DIFFERENCE":
        if isinstance(current, dict) and current.get("semantic_type", "").startswith("SET_OF<"):
            member = current["members"][0]
            member["identifier"] += ".MUTANT"
            allowed = member.get("authoritative_source", {}).get("allowed_identifiers")
            if isinstance(allowed, list):
                allowed.append(member["identifier"])
        elif isinstance(current, dict) and current.get("semantic_type") == "BOOLEAN":
            current["value"] = not current["value"]
        elif isinstance(current, dict) and current.get("semantic_type") == "TIMESTAMP":
            current["value"] = "2026-07-17T00:00:00+07:00"
        elif isinstance(current, dict) and isinstance(current.get("value"), (int, float)):
            current["value"] += 1
        else:
            require(isinstance(current, dict) and isinstance(current.get("identifier"), str), "unsupported semantic target")
            current["identifier"] += ".MUTANT"
            allowed = current.get("authoritative_source", {}).get("allowed_identifiers")
            if isinstance(allowed, list):
                allowed.append(current["identifier"])
        return current
    if kind == "ORIGIN_COLLISION":
        return get_pointer(fixture, "/validation_fixture/comparison/expected/origin/origin_id")
    if kind == "EVIDENCE_OBJECT_REMOVED":
        return {"missing": True}
    raise AssertionError("unknown mutation")


def independent_changed_paths(left: Any, right: Any, path: str = "") -> list[str]:
    if type(left) is not type(right):
        return [path or "/"]
    if isinstance(left, dict):
        rows = []
        for key in sorted(set(left) | set(right)):
            child = f"{path}/{key}"
            if key not in left or key not in right:
                rows.append(child)
            else:
                rows.extend(independent_changed_paths(left[key], right[key], child))
        return rows
    if isinstance(left, list):
        if len(left) != len(right):
            return [path or "/"]
        rows = []
        for index, pair in enumerate(zip(left, right)):
            rows.extend(independent_changed_paths(pair[0], pair[1], f"{path}/{index}"))
        return rows
    return [] if left == right else [path or "/"]


def independent_mutate(fixture_bytes: bytes, mutation: dict[str, Any]) -> tuple[bytes, list[str]]:
    fixture = json.loads(fixture_bytes)
    require(canonical(fixture) == fixture_bytes, "fixture not canonical")
    identity = (fixture.get("fixture_id"), fixture.get("fixture_sha256"), canonical(fixture.get("source_provenance")))
    replacement = independent_replacement(fixture, mutation)
    require(replacement != get_pointer(fixture, mutation["target"]), "no-op")
    mutant = json.loads(fixture_bytes)
    set_pointer(mutant, mutation["target"], replacement)
    paths = independent_changed_paths(fixture, mutant)
    target = mutation["target"].rstrip("/")
    require(paths and all(path == target or path.startswith(target + "/") for path in paths), "mutation escaped target")
    require(identity == (mutant.get("fixture_id"), mutant.get("fixture_sha256"), canonical(mutant.get("source_provenance"))), "identity changed")
    return canonical(mutant), paths


def validate_independent_impact(impact: dict[str, Any]) -> None:
    fixtures_payload = backup_json("docs/baselines/v2.3/phase-2/semantic-completion-c4-fixtures.json")
    executions_payload = backup_json("docs/baselines/v2.3/phase-2/semantic-completion-c4-execution-results.json")
    fixtures = {item["fixture_id"]: item for item in fixtures_payload["fixtures"]}
    registered = {item["execution_id"]: item for item in impact["execution_impacts"]}
    counts = {kind: {"total": 0, "matched": 0, "vulnerable": 0} for kind in ("SEMANTIC_DIFFERENCE", "ORIGIN_COLLISION", "EVIDENCE_OBJECT_REMOVED")}
    for execution in executions_payload["results"]:
        fixture_bytes = canonical(fixtures[execution["fixture_id"]])
        mutant_bytes, paths = independent_mutate(fixture_bytes, execution["mutation_definition"])
        actual_hash = sha(mutant_bytes)
        matched = actual_hash == execution["mutated_fixture_sha256"]
        kind = execution["mutation_definition"]["mutation_kind"]
        counts[kind]["total"] += 1
        counts[kind]["matched" if matched else "vulnerable"] += 1
        stored = registered[execution["execution_id"]]
        require(stored["isolated_hash"] == actual_hash and stored["changed_paths"] == paths, "impact row mismatch")
    require(counts == impact["execution_summary"], "impact summary mismatch")
    require(counts["SEMANTIC_DIFFERENCE"] == {"total": 177, "matched": 0, "vulnerable": 177}, "semantic impact")
    require(counts["ORIGIN_COLLISION"] == {"total": 177, "matched": 0, "vulnerable": 177}, "origin impact")
    require(counts["EVIDENCE_OBJECT_REMOVED"] == {"total": 177, "matched": 177, "vulnerable": 0}, "evidence impact")


def load_builder():
    path = ROOT / "scripts/docs/build-phase-2c-semantic-infrastructure-amendment-a1.py"
    spec = importlib.util.spec_from_file_location("amendment_builder_validation", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    manifest = load_json("docs/baselines/v2.3/phase-2/semantic-infrastructure-amendment-a1-manifest.json")
    types = load_json("docs/baselines/v2.3/phase-2/semantic-infrastructure-generic-set-types-a1.json")
    mutation = load_json("docs/baselines/v2.3/phase-2/semantic-infrastructure-mutation-isolation-a1.json")
    example = load_json("docs/baselines/v2.3/phase-2/semantic-infrastructure-brd-ws-14-r031-example-a1.json")
    impact = load_json("docs/baselines/v2.3/phase-2/semantic-infrastructure-c4-impact-register-a1.json")
    regressions = load_json("docs/baselines/v2.3/phase-2/semantic-infrastructure-amendment-a1-regressions.json")

    require(manifest["candidate_id"] == core.CANDIDATE_ID and manifest["status"] == "CANDIDATE", "candidate identity")
    require(manifest["approval_status"] == "PENDING_HUMAN_APPROVAL", "candidate approval state")
    require(manifest["accepted_input_commits"] == {"semantic_oracle_model_c2": core.ORACLE_COMMIT, "operator_binding_type_model_c1": core.BASE_COMMIT}, "accepted inputs")
    require(subprocess.check_output(["git", "rev-parse", core.C4_REF], cwd=ROOT, text=True).strip() == core.C4_OBJECT, "C4 object")
    require(subprocess.check_output(["git", "rev-parse", core.C4_REF + "^3^{tree}"], cwd=ROOT, text=True).strip() == core.C4_TREE, "C4 tree")

    require(len(types["operators"]) == 3, "generic operator count")
    core.validate_generic_set_contract(example, types)
    adversarial = core.adversarial_results(types, example)
    require(len(adversarial) == 30 and all(item["result"] == "PASS" for item in adversarial), "adversarial tests")
    require(regressions["generic_set_adversarial_results"] == adversarial, "stored adversarial results")

    alias = mutation["mandatory_alias_regression"]
    require(alias["isolated_hash"] == "23f0cd102050f812c1da9aae80b21421d17b1ae146f2f557ba1182bfc194ca00", "isolated hash")
    require(alias["aliased_hash"] == "e9aa0328aced18ee1d6c181b6a0b1039423764202aaedb92488955a82fea6711", "aliased hash")
    require(alias["aliased_result_rejected"] is True, "alias rejection")
    validate_independent_impact(impact)

    builder = load_builder()
    first = builder.build()
    second = builder.build()
    require(first == second, "two deterministic generations differ")
    for path, data in first.items():
        require((ROOT / path).read_bytes() == data, "generated payload differs:" + path)

    for path, expected in manifest["signed_file_hashes_excluding_self_referential_manifest"].items():
        require(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected, "signed file hash:" + path)
    aggregate = hashlib.sha256()
    generated = {path: data for path, data in first.items() if not path.endswith("manifest.json")}
    for path in sorted(generated):
        aggregate.update(path.encode("utf-8") + b"\0" + generated[path] + b"\0")
    require(aggregate.hexdigest() == manifest["generated_payload_aggregate_sha256"], "generated aggregate")

    changed = set(subprocess.check_output(["git", "diff", "--name-only", core.BASE_COMMIT], cwd=ROOT, text=True).splitlines())
    untracked = set(subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"], cwd=ROOT, text=True).splitlines())
    observed = changed | untracked
    require(observed <= set(manifest["exact_file_inventory"]), "unexpected changed path")
    require(not any(path.startswith("docs/BRD/") or path.startswith("docs/UXF/") for path in observed), "BRD/UXF changed")
    require(set(manifest["non_claims"]) == {
        "NOT_C4_DOCUMENT_BASELINE_APPROVAL", "NOT_BRD_UXF_REMEDIATION", "NOT_RUNTIME_ADAPTER_VALIDATION",
        "NOT_RUNTIME_MUTATION_SCORE", "NOT_YADF_AUTHORIZATION", "NOT_PRODUCTION_IMPLEMENTATION",
        "NOT_APPROVAL_OF_27_PENDING_DECISIONS",
    }, "non-claims")

    print("PASS — GENERIC_SET_OPERATOR_TYPE_AMENDMENT 3/3")
    print("PASS — BRD_WS_14_R031_TYPED_REFERENCE_EXAMPLE")
    print("PASS — GENERIC_SET_ADVERSARIAL_TESTS 30/30")
    print("PASS — CANONICAL_MUTATION_ALIAS_REGRESSION")
    print("PASS — INDEPENDENT_C4_IMPACT_AUDIT 354_VULNERABLE 177_REPRODUCED")
    print("PASS — DETERMINISTIC_AMENDMENT_GENERATION 2/2")
    print("PASS — VALID_PHASE_2C_SEMANTIC_INFRASTRUCTURE_AMENDMENT_A1")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, core.AmendmentError, KeyError, json.JSONDecodeError) as exc:
        print("FAIL — " + str(exc))
        raise SystemExit(1)
