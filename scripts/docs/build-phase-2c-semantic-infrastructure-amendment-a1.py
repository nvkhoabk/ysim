#!/usr/bin/env python3
"""Build deterministic Phase 2C semantic infrastructure amendment A1 artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

import semantic_infrastructure_amendment_a1 as core


ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"

OUTPUTS = {
    "docs/baselines/v2.3/phase-2/PHASE_2C_SEMANTIC_INFRASTRUCTURE_AMENDMENT_A1.md": "markdown",
    "docs/baselines/v2.3/phase-2/semantic-infrastructure-generic-set-types-a1.json": "types",
    "docs/baselines/v2.3/phase-2/semantic-infrastructure-mutation-isolation-a1.json": "mutation",
    "docs/baselines/v2.3/phase-2/semantic-infrastructure-brd-ws-14-r031-example-a1.json": "example",
    "docs/baselines/v2.3/phase-2/semantic-infrastructure-c4-impact-register-a1.json": "impact",
    "docs/baselines/v2.3/phase-2/semantic-infrastructure-amendment-a1-regressions.json": "regressions",
    "docs/baselines/v2.3/phase-2/semantic-infrastructure-amendment-a1-manifest.json": "manifest",
}

TOOLING = [
    "scripts/docs/build-phase-2c-semantic-infrastructure-amendment-a1.py",
    "scripts/docs/semantic_infrastructure_amendment_a1.py",
    "scripts/docs/validate-phase-2c-semantic-infrastructure-amendment-a1.py",
    "scripts/docs/tests/test-phase-2c-semantic-infrastructure-amendment-a1.py",
]


def ref(namespace: str, identifier: str, semantic_type: str, source_type: str, source_id: str,
        resolver_id: str, resolver_inputs: list[str], resolver_output: str, origin_type: str,
        origin_id: str, allowed_targets: list[str]) -> dict[str, Any]:
    return {
        "namespace": namespace,
        "identifier": identifier,
        "semantic_type": semantic_type,
        "authoritative_source": {
            "source_type": source_type,
            "source_id": source_id,
            "version_source": "FIELD.IMPACT_VERSION",
        },
        "resolver_contract": {
            "resolver_id": resolver_id,
            "version": "1.0.0-amendment.a1",
            "input_types": resolver_inputs,
            "output_type": resolver_output,
            "deterministic": True,
        },
        "lifecycle": {"status": "ACTIVE", "version": "2.3"},
        "origin": {"origin_type": origin_type, "origin_id": origin_id},
        "provenance": {
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_section": "30. Configuration Dependency Graph",
            "source_lines": "L815-L855",
            "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
            "accepted_type_model_disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
            "inference": False,
        },
        "allowed_target_types": allowed_targets,
        "inference": False,
    }


def type_amendment() -> dict[str, Any]:
    accepted_catalog = json.loads((P2 / "operator-binding-semantic-types.json").read_text())
    accepted_types = accepted_catalog["types"]
    allowed_type_parameters = sorted(accepted_types)
    reference_target_types = sorted(
        type_id for type_id, definition in accepted_types.items()
        if definition["kind"] == "SYMBOLIC_REFERENCE" and type_id != "REFERENCE_ID"
    )
    expected_origins = ["APPROVED_DECISION", "CANONICAL_REGISTRY", "VERSIONED_POLICY", "VERSIONED_CONFIGURATION", "SOURCE_LITERAL", "SYNTHETIC_MODEL_FIXTURE"]
    observed_origins = ["RUNTIME_OBSERVED", "EVIDENCE_OBJECT", "SYNTHETIC_MODEL_FIXTURE"]
    operators = []
    for operator_id, expected_name, relation in (
        ("SET_EQUALS", "expected_set", "SEMANTIC_SET_EQUALITY"),
        ("SET_CONTAINS", "required_members", "SEMANTIC_SET_CONTAINS"),
        ("SET_EXCLUDES", "prohibited_members", "SEMANTIC_SET_EXCLUDES"),
    ):
        operators.append({
            "operator_id": operator_id,
            "accepted_base_version": "1.0.0-candidate.2",
            "amendment_version": "1.1.0-amendment.a1",
            "type_signature": f"{operator_id}<T>",
            "type_parameter": "T",
            "observed_binding_name": "actual_set",
            "expected_binding_name": expected_name,
            "observed_type": "RUNTIME_SET_REF<T>",
            "expected_type": "CANONICAL_SET_REF<T>",
            "resolver_output_type": "SET_OF<T>",
            "comparison_relation": relation,
            "expected_origins": expected_origins,
            "observed_origins": observed_origins,
            "invariants": [
                "EXPECTED_AND_OBSERVED_USE_IDENTICAL_T",
                "EXPECTED_AND_OBSERVED_ORIGIN_IDS_DIFFER",
                "EXPECTED_AND_OBSERVED_RESOLVERS_DIFFER",
                "EXPECTED_AND_OBSERVED_AUTHORITIES_DIFFER",
                "EVERY_REFERENCE_MEMBER_HAS_EXPLICIT_TARGET_TYPE",
                "NO_PROSE_OR_SCHEMA_DERIVED_IDENTIFIERS",
                "ALL_RESOLVERS_ARE_DETERMINISTIC_AND_VERSIONED",
            ],
        })
    return {
        "artifact": "V23-P2C-GENERIC-SET-TYPE-AMENDMENT-A1",
        "candidate_id": core.CANDIDATE_ID,
        "status": "CANDIDATE",
        "approval_status": "PENDING_HUMAN_APPROVAL",
        "amendment_version": "1.0.0-candidate.1",
        "additive_to": {
            "accepted_operator_binding_type_model_commit": core.BASE_COMMIT,
            "accepted_semantic_oracle_model_commit": core.ORACLE_COMMIT,
        },
        "accepted_type_catalog_version": accepted_catalog["version"],
        "allowed_type_parameters": allowed_type_parameters,
        "reference_target_types": reference_target_types,
        "heterogeneous_reference_rule": {
            "type_parameter": "REFERENCE_ID",
            "member_target_type_required": True,
            "implicit_union_forbidden": True,
            "enum_coercion_forbidden": True,
        },
        "operators": operators,
        "prohibited_member_or_identifier_shapes": [
            "WHOLE_SENTENCE", "PROSE_LABEL", "WHOLE_REQUIREMENT", "SCHEMA_PROPERTY_NAME",
            "OPERATOR_FIELD_NAME", "EXPECTED_SET", "ACTUAL_SET", "PLACEHOLDER_DEFAULT",
        ],
    }


def example() -> dict[str, Any]:
    targets = ["CONFIGURATION_KEY", "CAPABILITY_ID"]
    return {
        "artifact": "V23-P2C-BRD-WS-14-R031-TYPED-REFERENCE-EXAMPLE-A1",
        "candidate_id": core.CANDIDATE_ID,
        "status": "READ_ONLY_MODEL_VALIDATION_EXAMPLE",
        "requirement_id": "BRD-WS-14-R031",
        "source_statement": "Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Capability bị ảnh hưởng.",
        "source_context": {
            "dependency_graph_uses": ["IMPACT_ANALYSIS", "UPGRADE_PLANNING", "VALIDATION", "ROLLBACK", "PUBLISH_CHECKING"],
            "accepted_type_model_disposition": "SET_EQUALS over dependency-graph resolved expected Configuration/Capability IDs and independently reported impact IDs",
            "source_clarification_required": False,
        },
        "operator_id": "SET_EQUALS",
        "operator_version": "1.1.0-amendment.a1",
        "type_parameter": "REFERENCE_ID",
        "expected_set": ref(
            "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE", "AFFECTED_NODE_REFERENCES",
            "CANONICAL_SET_REF<REFERENCE_ID>", "VERSIONED_CONFIGURATION", "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
            "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES", ["CONFIGURATION_KEY", "HASH"],
            "SET_OF<REFERENCE_ID>", "VERSIONED_CONFIGURATION", "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION", targets,
        ),
        "actual_set": ref(
            "YSIM.CONFIGURATION_IMPACT_ANALYSIS.NODE_REFERENCE", "REPORTED_AFFECTED_NODE_REFERENCES",
            "RUNTIME_SET_REF<REFERENCE_ID>", "EVIDENCE_OBJECT", "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
            "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES", ["EVIDENCE_OBJECT_REF"],
            "SET_OF<REFERENCE_ID>", "RUNTIME_OBSERVED", "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT", targets,
        ),
        "required_evidence_fields": [
            "FIELD.CHANGED_CONFIGURATION_ID", "FIELD.DEPENDENCY_GRAPH", "FIELD.AFFECTED_CONFIGURATION_IDS",
            "FIELD.AFFECTED_CAPABILITY_IDS", "FIELD.IMPACT_VERSION",
        ],
        "expected_observed_independence": {
            "expected_authority": "VERSIONED_CONFIGURATION_DEPENDENCY_GRAPH",
            "observed_authority": "IMPACT_ANALYSIS_EVIDENCE_OBJECT",
            "origin_ids_must_differ": True,
            "resolver_ids_must_differ": True,
        },
        "inference": False,
    }


def mutation_contract(alias: dict[str, Any]) -> dict[str, Any]:
    return {
        "artifact": "V23-P2C-CANONICAL-MUTATION-ISOLATION-CONTRACT-A1",
        "candidate_id": core.CANDIDATE_ID,
        "status": "CANDIDATE",
        "contract_version": "1.0.0-candidate.1",
        "canonicalization": {
            "encoding": "UTF-8",
            "ensure_ascii": False,
            "sort_object_keys": True,
            "separators": [",", ":"],
            "unicode_normalization": "NONE",
            "line_endings": "NONE_IN_COMPACT_JSON",
        },
        "invariants": [
            "CANONICAL_SERIALIZED_FIXTURE_BYTES_ARE_THE_ONLY_MUTATION_INPUT",
            "EVERY_MUTATION_PARSES_A_FRESH_OBJECT_GRAPH",
            "EXACTLY_ONE_JSON_POINTER_OPERATION_IS_APPLIED",
            "GENERATOR_OBJECT_REFERENCES_ARE_NEVER_REUSED",
            "TARGET_MUST_EXIST",
            "NO_OP_MUTATIONS_ARE_REJECTED",
            "ALL_CHANGED_LEAVES_MUST_BE_AT_OR_BELOW_THE_DECLARED_TARGET",
            "SIBLING_AND_MIRRORED_PATH_CHANGES_ARE_REJECTED",
            "FIXTURE_IDENTITY_AND_PROVENANCE_REMAIN_UNCHANGED_UNLESS_EXPLICITLY_TARGETED",
            "MUTANT_HASH_IS_COMPUTED_FROM_CANONICAL_POST_MUTATION_BYTES",
            "EXCEPTIONS_AND_INVALID_MUTATIONS_ARE_NOT_KILLED",
        ],
        "independent_validator_contract": [
            "READ_STORED_CANONICAL_FIXTURE_BYTES",
            "PARSE_FRESH",
            "APPLY_STORED_MUTATION_DEFINITION",
            "CANONICAL_SERIALIZE",
            "HASH",
            "COMPARE_WITH_STORED_MUTANT_HASH",
        ],
        "mandatory_alias_regression": alias,
    }


def preservation() -> dict[str, Any]:
    ref = core.C4_REF + "^3"
    lines = subprocess.check_output(["git", "ls-tree", "-r", ref], cwd=ROOT, text=True).splitlines()
    inventory = []
    for line in lines:
        meta, path = line.split("\t", 1)
        _, object_type, object_sha = meta.split()
        raw = subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)
        inventory.append({"path": path, "object_type": object_type, "blob_sha": object_sha, "sha256": hashlib.sha256(raw).hexdigest()})
    return {
        "backup_ref": core.C4_REF,
        "backup_object": core.git_output("rev-parse", core.C4_REF),
        "untracked_content_commit": core.git_output("rev-parse", core.C4_REF + "^3"),
        "tree_sha": core.git_output("rev-parse", core.C4_REF + "^3^{tree}"),
        "base_commit": core.BASE_COMMIT,
        "generated_aggregate": core.C4_AGGREGATE,
        "inventory_count": len(inventory),
        "inventory": inventory,
        "reproduction": "VALID_BYTE_IDENTICAL_12_OF_12",
    }


def markdown(preserve: dict[str, Any], impact: dict[str, Any], alias: dict[str, Any]) -> str:
    return f"""# Phase 2C Semantic Infrastructure Amendment A1

- Candidate: `{core.CANDIDATE_ID}`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_APPROVAL`
- Scope: `OPERATOR_GENERIC_SET_TYPING_AND_CANONICAL_MUTATION_ISOLATION`
- Next gate: `HUMAN_PHASE_2C_SEMANTIC_INFRASTRUCTURE_AMENDMENT_APPROVAL`

## Additive baseline relationship

This amendment is additive to Semantic Oracle Model C2 commit `{core.ORACLE_COMMIT}` and Operator Binding Type Model C1 accepted commit `{core.BASE_COMMIT}`. It does not replace or mutate either accepted payload.

## Generic set typing

`SET_EQUALS<T>`, `SET_CONTAINS<T>`, and `SET_EXCLUDES<T>` bind canonical expected sets and independently observed runtime sets using the same `T`. Heterogeneous business-object references use `REFERENCE_ID` with an explicit target type; they are never coerced to enums.

## Canonical mutation isolation

Canonical fixture bytes are parsed fresh for every mutation. One JSON Pointer operation is allowed, all changed leaves must remain under that target, and mirrored or aliased side effects are rejected.

The mandatory regression produces `{alias['isolated_hash']}` and rejects the historical two-path result `{alias['aliased_hash']}`.

## Preserved blocked C4 impact

- Backup object: `{preserve['backup_object']}`
- Content tree: `{preserve['tree_sha']}`
- C4 aggregate: `{preserve['generated_aggregate']}`
- Semantic/origin mutant hashes requiring future regeneration: `{impact['vulnerable_hash_count']}`
- Evidence-removal hashes reproduced without change: `{impact['reproduced_hash_count']}`

No C4 artifact is regenerated or overwritten by this amendment.

## Non-claims

- `NOT_C4_DOCUMENT_BASELINE_APPROVAL`
- `NOT_BRD_UXF_REMEDIATION`
- `NOT_RUNTIME_ADAPTER_VALIDATION`
- `NOT_RUNTIME_MUTATION_SCORE`
- `NOT_YADF_AUTHORIZATION`
- `NOT_PRODUCTION_IMPLEMENTATION`
- `NOT_APPROVAL_OF_27_PENDING_DECISIONS`
"""


def build() -> dict[str, bytes]:
    types = type_amendment()
    typed_example = example()
    core.validate_generic_set_contract(typed_example, types)
    alias = core.alias_regression()
    if alias["isolated_hash"] != alias["required_isolated_hash"] or alias["aliased_hash"] != alias["required_rejected_hash"] or not alias["aliased_result_rejected"]:
        raise RuntimeError("ALIAS_REGRESSION_FAILED")
    impact = core.impact_audit()
    if impact["vulnerable_hash_count"] != 354 or impact["reproduced_hash_count"] != 177:
        raise RuntimeError("C4_IMPACT_ACCOUNTING_FAILED")
    adversarial = core.adversarial_results(types, typed_example)
    if any(item["result"] != "PASS" for item in adversarial):
        raise RuntimeError("ADVERSARIAL_SET_TYPE_TEST_FAILED")
    preserve = preservation()
    if preserve["backup_object"] != core.C4_OBJECT or preserve["tree_sha"] != core.C4_TREE or preserve["inventory_count"] != 12:
        raise RuntimeError("C4_PRESERVATION_IDENTITY_FAILED")

    mutation = mutation_contract(alias)
    impact_artifact = {
        "artifact": "V23-P2C-C4-READ-ONLY-MIGRATION-IMPACT-A1",
        "candidate_id": core.CANDIDATE_ID,
        "preserved_c4": preserve,
        "operator_type_contracts_affected": ["SET_EQUALS<T>", "SET_CONTAINS<T>", "SET_EXCLUDES<T>"],
        "fixture_count_audited": impact["fixture_count"],
        "execution_count_audited": impact["execution_count"],
        "execution_summary": impact["counts"],
        "execution_hashes_requiring_future_regeneration": impact["vulnerable_hash_count"],
        "execution_hashes_reproduced": impact["reproduced_hash_count"],
        "expected_semantic_changes": ["BRD-WS-14-R031 uses REFERENCE_ID set members with explicit CONFIGURATION_KEY/CAPABILITY_ID targets"],
        "expected_hash_only_changes": ["354 C4 SEMANTIC_DIFFERENCE/ORIGIN_COLLISION mutant hashes after alias isolation"],
        "records_requiring_source_clarification": [],
        "c4_artifacts_written": False,
        "execution_impacts": impact["execution_impacts"],
    }
    regressions = {
        "artifact": "V23-P2C-SEMANTIC-INFRASTRUCTURE-AMENDMENT-A1-REGRESSIONS",
        "candidate_id": core.CANDIDATE_ID,
        "generic_set_adversarial_count": len(adversarial),
        "generic_set_adversarial_results": adversarial,
        "alias_regression": alias,
        "c4_impact_summary": impact["counts"],
        "result": "PASS",
    }

    values: dict[str, Any] = {
        "markdown": markdown(preserve, impact, alias),
        "types": types,
        "mutation": mutation,
        "example": typed_example,
        "impact": impact_artifact,
        "regressions": regressions,
    }
    encoded: dict[str, bytes] = {}
    for path, key in OUTPUTS.items():
        if key == "manifest":
            continue
        value = values[key]
        encoded[path] = value.encode("utf-8") if isinstance(value, str) else json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8") + b"\n"

    aggregate = hashlib.sha256()
    for path in sorted(encoded):
        aggregate.update(path.encode("utf-8") + b"\0" + encoded[path] + b"\0")

    inventory = sorted(list(OUTPUTS) + TOOLING)
    signed_hashes = {path: hashlib.sha256(data).hexdigest() for path, data in encoded.items()}
    for path in TOOLING:
        target = ROOT / path
        if not target.exists():
            raise RuntimeError("MISSING_TOOLING:" + path)
        signed_hashes[path] = hashlib.sha256(target.read_bytes()).hexdigest()
    manifest = {
        "candidate_id": core.CANDIDATE_ID,
        "status": "CANDIDATE",
        "approval_status": "PENDING_HUMAN_APPROVAL",
        "approval_scope": "OPERATOR_GENERIC_SET_TYPING_AND_CANONICAL_MUTATION_ISOLATION",
        "accepted_input_commits": {
            "semantic_oracle_model_c2": core.ORACLE_COMMIT,
            "operator_binding_type_model_c1": core.BASE_COMMIT,
        },
        "amendment_relationship": "ADDITIVE_DOES_NOT_SUPERSEDE_ACCEPTED_ARTIFACTS",
        "superseded_behavior": [
            "SET_OPERATORS_FIXED_TO_CANONICAL_ENUM_VALUE",
            "MUTATION_OF_GENERATOR_OBJECT_GRAPH_WITH_SHARED_REFERENCES",
        ],
        "preserved_c4": preserve,
        "counts": {
            "amended_operators": 3,
            "adversarial_tests": len(adversarial),
            "c4_fixtures_audited": impact["fixture_count"],
            "c4_executions_audited": impact["execution_count"],
            "vulnerable_hashes": impact["vulnerable_hash_count"],
            "reproduced_evidence_hashes": impact["reproduced_hash_count"],
        },
        "exact_file_inventory": inventory,
        "signed_file_hashes_excluding_self_referential_manifest": dict(sorted(signed_hashes.items())),
        "generated_payload_aggregate_sha256": aggregate.hexdigest(),
        "git_identity": {
            "staged_tree": "RECORDED_AT_HUMAN_GATE_FROM_GIT_INDEX",
            "git_content_aggregate": "RECORDED_AT_HUMAN_GATE_FROM_GIT_INDEX",
            "self_reference_rule": "THE_MANIFEST_CANNOT_EMBED_THE_HASH_OF_A_GIT_TREE_OR_AGGREGATE_THAT_INCLUDES_ITS_OWN_BYTES",
        },
        "non_claims": [
            "NOT_C4_DOCUMENT_BASELINE_APPROVAL", "NOT_BRD_UXF_REMEDIATION", "NOT_RUNTIME_ADAPTER_VALIDATION",
            "NOT_RUNTIME_MUTATION_SCORE", "NOT_YADF_AUTHORIZATION", "NOT_PRODUCTION_IMPLEMENTATION",
            "NOT_APPROVAL_OF_27_PENDING_DECISIONS",
        ],
        "next_gate": "HUMAN_PHASE_2C_SEMANTIC_INFRASTRUCTURE_AMENDMENT_APPROVAL",
    }
    manifest_path = "docs/baselines/v2.3/phase-2/semantic-infrastructure-amendment-a1-manifest.json"
    encoded[manifest_path] = json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2).encode("utf-8") + b"\n"
    return encoded


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = build()
    mismatches = []
    for path, data in outputs.items():
        target = ROOT / path
        if args.check:
            if not target.exists() or target.read_bytes() != data:
                mismatches.append(path)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    if mismatches:
        print("FAIL — NONDETERMINISTIC_AMENDMENT_A1: " + ", ".join(mismatches))
        return 1
    print("PASS — DETERMINISTIC_SEMANTIC_INFRASTRUCTURE_AMENDMENT_A1" if args.check else f"GENERATED — {core.CANDIDATE_ID} — {len(outputs)} artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
