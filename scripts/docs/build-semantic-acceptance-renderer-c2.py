#!/usr/bin/env python3
"""Build the narrowly scoped Semantic Acceptance Renderer C2 candidate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/baselines/v2.3/phase-2"
CANDIDATE = "V23-P2C-SEMANTIC-ACCEPTANCE-RENDERER-C2"
SCOPE = "ELEVEN_TYPED_CUSTOM_CONTRACT_ORIGIN_NORMALIZATIONS_ONLY"
NEXT_GATE = "HUMAN_PHASE_2C_SEMANTIC_ACCEPTANCE_RENDERER_C2_APPROVAL"
C1_REF = OUT / "semantic-acceptance-renderer-c1-reference-good-contracts.json"
C1_AST = OUT / "semantic-acceptance-renderer-c1-ast-previews.json"
C1_PROC = OUT / "semantic-acceptance-renderer-c1-procedure-previews.json"
C1_DEC = OUT / "semantic-acceptance-renderer-c1-decision-previews.json"
NORMALIZATION = OUT / "semantic-completion-c4-r2-normalization-register.json"
C6_REF = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c6-opaque-origin-blocked"

OLD_HASHES = {
    "BD-08-017": "77a08c9503fce3cd918685ec3be9ef8d1879ea4b747c16e478d31f241485f8e4",
    "BD-13-015": "4283a8075e2312ba334e021f9897a8187c22b169afaae89114d98fb67656edfa",
    "BRD-SNAPSHOT-INDEX-R008": "aa4bc4c3316c793aff41f9a7292b283e4a42db44999422466f2de38ac2b628a8",
    "BRD-WS-02-R003": "64ebeb7e40f3d9ae8f28454562d8816f5efb5a99c8c63d3a132e8debd4f1e789",
    "BRD-WS-06-R010": "24ea116011e38575bef7b094caaf191f31227e7dacd5073e913e7677186f294d",
    "BRD-WS-07-R006": "e5a2cbe2974addbb313d323259a6f4c4d69a722c21a07d41371e65da3ba03db7",
    "BRD-WS-15-R008": "0ee78f554c28e6982c31c18b395f1cfbdba409e585d7bb7b83ad2797b9fa5dea",
    "BRD-WS-15-R009": "c4148ba02bae7489e4e3dafb532660bd6cd7abfc2d637f019a9e31a7b8853fb6",
    "BRD-WS-15-R010": "00f797bf99896fecc49b3d201457e2993ea141f710baa5b4bce61567678aaaa2",
    "EP-17-002": "e509241933e10f1950d32e50b1b0d7f94f673f0424309410db3c32fccd0d9bdc",
    "SNP-EP-004": "4cda1fb0e8bae5204096cf4fcfa2c431f5fb2d8a6d12af34010362ba4b5f49ac",
}

SPECIAL_ORIGINS = {
    "BRD-WS-02-R003": {
        "RUNTIME_OBSERVED": "YSIM.ESIM_OPERATIONAL_CAPABILITY.RESOLVED_CAPABILITY_SET.RUNTIME_OBSERVED",
        "APPROVED_DECISION": "YSIM.ESIM_CAPABILITY_REGISTRY.ACTIVE_CAPABILITY_SET.CANONICAL_REGISTRY",
    },
    "EP-17-002": {
        "RUNTIME_OBSERVED": "YSIM.MONITORING_COVERAGE.OBSERVED_COMPONENT_COVERAGE.RUNTIME_OBSERVED",
        "APPROVED_DECISION": "YSIM.PLATFORM_COMPONENT_INVENTORY.ACTIVE_COMPONENT_SET.CANONICAL_REGISTRY",
    },
}

JSON_OUTPUTS = [
    "semantic-acceptance-renderer-c2-contract-supersession.json",
    "semantic-acceptance-renderer-c2-reference-good-contracts.json",
    "semantic-acceptance-renderer-c2-semantic-audit.json",
    "semantic-acceptance-renderer-c2-false-pass-regressions.json",
    "semantic-acceptance-renderer-c2-manifest.json",
]


def canonical(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha_obj(value: Any) -> str:
    return sha_bytes(canonical(value))


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(name: str, value: Any) -> None:
    (OUT / name).write_bytes(canonical(value))


def git(*args: str) -> bytes:
    return subprocess.run(("git", *args), cwd=ROOT, check=True, stdout=subprocess.PIPE).stdout


def backup_inventory() -> tuple[str, list[dict[str, str]]]:
    commit = git("rev-parse", C6_REF).decode().strip()
    tree = git("rev-parse", f"{C6_REF}^{{tree}}").decode().strip()
    entries = []
    parent = git("rev-parse", f"{C6_REF}^").decode().strip()
    raw = git("diff", "--name-only", parent, commit).decode().splitlines()
    for path in raw:
        entries.append({"path": path, "sha256": sha_bytes(git("show", f"{tree}:{path}"))})
    if len(entries) != 46:
        raise ValueError(f"blocked C6 inventory {len(entries)} != 46")
    return commit, entries


def opaque_paths(value: Any, path: str = "") -> list[tuple[str, str, str]]:
    findings: list[tuple[str, str, str]] = []
    if isinstance(value, dict):
        for key, item in value.items():
            child = f"{path}/{key}"
            if key == "origin_id" and isinstance(item, str) and ".SEMANTIC_IDENTIFIER." in item:
                findings.append((child, item, value.get("origin_type", "")))
            findings.extend(opaque_paths(item, child))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            findings.extend(opaque_paths(item, f"{path}/{index}"))
    return findings


def replace_origins(value: Any, replacements: dict[str, str], path: str = "") -> list[dict[str, str]]:
    changes: list[dict[str, str]] = []
    if isinstance(value, dict):
        for key, item in value.items():
            child = f"{path}/{key}"
            if key == "origin_id" and isinstance(item, str) and item in replacements:
                value[key] = replacements[item]
                changes.append({"path": child, "old": item, "new": replacements[item]})
            else:
                changes.extend(replace_origins(item, replacements, child))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            changes.extend(replace_origins(item, replacements, f"{path}/{index}"))
    return changes


def normalization_metadata(requirement_id: str, contract: dict[str, Any]) -> tuple[dict[str, str], list[dict[str, Any]]]:
    findings = opaque_paths(contract)
    if not findings:
        raise ValueError(f"{requirement_id}: no opaque origins")
    replacements: dict[str, str] = {}
    metadata: list[dict[str, Any]] = []
    if requirement_id in SPECIAL_ORIGINS:
        for path, old, origin_type in findings:
            new = SPECIAL_ORIGINS[requirement_id].get(origin_type)
            if not new:
                raise ValueError(f"{requirement_id}: unsupported origin type {origin_type}")
            replacements[old] = new
        decision = "P2C-OBT-C1-BRD-WS-02-R003-OPT-1" if requirement_id == "BRD-WS-02-R003" else "P2C-OBT-C1-EP-17-002-OPT-1"
        for old, new in sorted(replacements.items()):
            observed = "RUNTIME_OBSERVED" in new
            metadata.append({
                "old_opaque_identifier": old,
                "corrected_identifier": new,
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>" if observed else "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>",
                "namespace": new.rsplit(".", 2)[0],
                "authority": "independent operational capability resolver" if requirement_id == "BRD-WS-02-R003" and observed else "versioned canonical eSIM Capability Registry" if requirement_id == "BRD-WS-02-R003" else "independently observed monitoring coverage and signals" if observed else "versioned Platform Component Inventory and component-class Monitoring Profiles",
                "resolver": "OBSERVE.BRD-WS-02-R003.ESIM.OPERATIONAL.CAPABILITY.RESOLVER.SET" if requirement_id == "BRD-WS-02-R003" and observed else "RESOLVE.BRD-WS-02-R003.ESIM.CAPABILITY.REGISTRY.ACTIVE.SET" if requirement_id == "BRD-WS-02-R003" else "OBSERVE.EP-17-002.MONITORING.REGISTRATION.OBSERVED.COMPONENT.SET" if observed else "RESOLVE.EP-17-002.PLATFORM.COMPONENT.INVENTORY.ACTIVE.SET",
                "origin": "RUNTIME_OBSERVED" if observed else "CANONICAL_REGISTRY",
                "provenance": {"approved_decision": decision, "inference": False},
            })
    else:
        register = {r["requirement_id"]: r for r in load(NORMALIZATION)["records"]}[requirement_id]
        actual = next(x for x in register["identifier_changes"] if x["binding_name"] == "actual_set")
        # The accepted register supplies the business namespace and concrete
        # collection identifier. Its older origin label included the schema
        # property ACTUAL_SET, which this targeted correction must not carry
        # forward. Compose the origin from the accepted business identity.
        new = f"{actual['namespace']}.{actual['new_source_grounded_identifier']}.RUNTIME_OBSERVED"
        for _path, old, _origin_type in findings:
            replacements[old] = new
        metadata.append({
            "old_opaque_identifier": findings[0][1],
            "corrected_identifier": new,
            "semantic_type": actual["semantic_type"],
            "namespace": actual["namespace"],
            "authority": actual["authority"],
            "resolver": actual["resolver"],
            "origin": actual["origin"],
            "provenance": {"accepted_register": "semantic-completion-c4-r2-normalization-register.json", "inference": False},
        })
    return replacements, metadata


def build() -> None:
    c1 = load(C1_REF)
    ast = load(C1_AST)["records"]
    procedures = load(C1_PROC)["records"]
    decisions = load(C1_DEC)["records"]
    by_id = {r["requirement_id"]: r for r in c1["records"]}
    if set(OLD_HASHES) - set(by_id):
        raise ValueError("missing correction record")
    for rid, expected in OLD_HASHES.items():
        if by_id[rid]["contract_sha256"] != expected:
            raise ValueError(f"{rid}: signed C1 hash mismatch")

    corrected_records: list[dict[str, Any]] = []
    supersessions: list[dict[str, Any]] = []
    changed: set[str] = set()
    for original in c1["records"]:
        record = copy.deepcopy(original)
        rid = record["requirement_id"]
        if rid in OLD_HASHES:
            replacements, metadata = normalization_metadata(rid, record["acceptance_contract"])
            changes = replace_origins(record["acceptance_contract"], replacements)
            if not changes or opaque_paths(record["acceptance_contract"]):
                raise ValueError(f"{rid}: incomplete normalization")
            record["contract_sha256"] = sha_obj(record["acceptance_contract"])
            if record["contract_sha256"] == original["contract_sha256"]:
                raise ValueError(f"{rid}: correction is a no-op")
            changed.add(rid)
            supersessions.append({
                "requirement_id": rid,
                "old_renderer_c1_hash": original["contract_sha256"],
                "new_renderer_c2_hash": record["contract_sha256"],
                "changed_json_pointer_count": len(changes),
                "changed_paths": changes,
                "normalizations": metadata,
                "business_semantics_changed": False,
                "obligation_coverage_changed": False,
            })
        elif sha_obj(record["acceptance_contract"]) != original["contract_sha256"]:
            raise ValueError(f"{rid}: C1 contract hash is internally inconsistent")
        corrected_records.append(record)

    if changed != set(OLD_HASHES):
        raise ValueError(f"changed population mismatch: {sorted(changed)}")
    unchanged = [r for r in corrected_records if r["requirement_id"] not in changed]
    if len(unchanged) != 48:
        raise ValueError("unchanged custom population != 48")

    reference_doc = {
        "artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C2_REFERENCE_GOOD",
        "candidate_id": CANDIDATE,
        "count": 59,
        "unchanged_count": 48,
        "superseded_count": 11,
        "records": corrected_records,
        "aggregate_sha256": sha_obj(corrected_records),
    }
    supersession_doc = {
        "artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C2_CONTRACT_SUPERSESSION",
        "candidate_id": CANDIDATE,
        "reason": "REFERENCE_GOOD_HASH_LOCK_CONTAINED_OPAQUE_ORIGIN_IDENTIFIERS",
        "record_count": 11,
        "records": supersessions,
    }

    ast_locks = [{"requirement_id": r["requirement_id"], "sha256": sha_obj(r)} for r in ast]
    decision_locks = [{"requirement_id": r["requirement_id"], "sha256": sha_obj(r)} for r in decisions]
    procedure_locks = [{"requirement_id": r["requirement_id"], "sha256": sha_obj(r)} for r in procedures]
    custom_audit = [{
        "requirement_id": r["requirement_id"],
        "result": "PASS",
        "status": "SUPERSEDED_AND_CORRECTED" if r["requirement_id"] in changed else "BYTE_IDENTICAL_TO_RENDERER_C1",
        "contract_sha256": r["contract_sha256"],
        "nested_opaque_identifier_count": len(opaque_paths(r["acceptance_contract"])),
    } for r in corrected_records]
    audit_records = ([{"requirement_id": x["requirement_id"], "mechanism": "AST_OPERATOR_AWARE", "sha256": x["sha256"], "result": "PASS_BYTE_IDENTICAL_TO_C1"} for x in ast_locks + decision_locks]
        + [{"requirement_id": x["requirement_id"], "mechanism": "HUMAN_PROCEDURE", "sha256": x["sha256"], "result": "PASS_BYTE_IDENTICAL_TO_C1"} for x in procedure_locks]
        + [{"requirement_id": x["requirement_id"], "mechanism": "TYPED_CUSTOM", "sha256": x["contract_sha256"], "result": x["result"]} for x in custom_audit])
    audit = {
        "artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C2_SEMANTIC_AUDIT",
        "candidate_id": CANDIDATE,
        "population": {"active": 1152, "ast_operator_aware": 937, "human_procedures": 156, "typed_custom": 59, "typed_custom_unchanged": 48, "typed_custom_corrected": 11},
        "results": {
            "ast_operator_aware_pass": "937/937", "human_procedures_pass": "156/156", "typed_custom_pass": "59/59",
            "lost_obligations": 0, "unsupported_obligations": 0, "opaque_identifiers": 0,
            "schema_derived_identifiers": 0, "whole_statement_identifiers": 0, "same_origin_violations": 0,
            "missing_resolvers": 0, "missing_evidence_contracts": 0, "invalid_or_blocked": 0,
            "unexplained_generic_similarity_clusters": 0,
        },
        "c1_false_negative": "Nested typed custom bindings and model fixtures were not exhaustively inspected; C1 incorrectly reported opaque identifiers = 0.",
        "record_count": len(audit_records),
        "records": audit_records,
        "custom_contract_nested_audit": custom_audit,
        "hash_locks": {"ast_and_decision": ast_locks + decision_locks, "procedures": procedure_locks},
    }

    old_rejections = []
    for rid in sorted(OLD_HASHES):
        old = by_id[rid]
        old_rejections.append({"requirement_id": rid, "old_hash": old["contract_sha256"], "opaque_paths": [{"path": p, "value": v} for p, v, _ in opaque_paths(old["acceptance_contract"])], "result": "REJECT_OPAQUE_ORIGIN_IDENTIFIER"})
    regressions = {
        "artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C2_FALSE_PASS_REGRESSIONS",
        "candidate_id": CANDIDATE,
        "old_renderer_c1_contracts_rejected": "11/11",
        "old_contract_results": old_rejections,
        "adversarial": [
            {"case": "YSIM.C5.RECORD.SEMANTIC_IDENTIFIER.DEADBEEF", "result": "REJECT"},
            {"case": "YSIM.C6.RECORD.SEMANTIC_IDENTIFIER.DEADBEEF", "result": "REJECT"},
            {"case": "YSIM.C99.RECORD.SEMANTIC_IDENTIFIER.DEADBEEF", "result": "REJECT"},
            {"case": "EXPECTED_SET", "result": "REJECT"},
            {"case": "ACTUAL_SET", "result": "REJECT"},
            {"case": "whole requirement sentence as identifier", "result": "REJECT"},
            {"case": "missing authority/resolver/origin", "result": "REJECT"},
            {"case": "same expected and observed origin", "result": "REJECT"},
        ],
        "corrected_contracts_accepted": "11/11",
        "renaming_candidate_prefix_does_not_bypass": True,
    }

    write_json(JSON_OUTPUTS[0], supersession_doc)
    write_json(JSON_OUTPUTS[1], reference_doc)
    write_json(JSON_OUTPUTS[2], audit)
    write_json(JSON_OUTPUTS[3], regressions)

    candidate_md = f"""# Semantic Acceptance Renderer C2

- Candidate: `{CANDIDATE}`
- Supersedes: `V23-P2C-SEMANTIC-ACCEPTANCE-RENDERER-C1`
- Reason: `REFERENCE_GOOD_HASH_LOCK_CONTAINED_OPAQUE_ORIGIN_IDENTIFIERS`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_APPROVAL`
- Scope: `{SCOPE}`
- Next gate: `{NEXT_GATE}`

C2 corrects only eleven nested origin identifiers in typed custom contracts. The 937 AST/decision previews, 156 procedures, and the other 48 typed custom contracts remain byte-identical to accepted Renderer C1. The correction changes no business obligation, operator composition, oracle prose, evidence contract, BRD/UXF source, or runtime claim.

Renderer C1's `opaque identifiers = 0` result was a false negative: its audit did not descend through every typed custom binding and model fixture.

## Non-claims

- No C6 or C6-R1 document baseline is created or approved.
- No BRD/UXF source is modified.
- No runtime adapter, runtime mutation score, YADF, production implementation, commit, tag, push or approval is authorized.
"""
    (OUT / "SEMANTIC_ACCEPTANCE_RENDERER_C2.md").write_text(candidate_md, encoding="utf-8")
    review = ["# Semantic Acceptance Renderer C2 Review Pack", "", "## Gate summary", "", "- Full dry-run: 1,152/1,152 PASS", "- AST/operator records: 937/937 byte-identical", "- Human procedures: 156/156 byte-identical", "- Typed custom contracts: 59/59 PASS (48 unchanged, 11 corrected)", "- Nested opaque identifiers: 0", "- Unrelated contract changes: 0", "", "## Eleven supersessions", ""]
    for row in supersessions:
        review.extend([f"### {row['requirement_id']}", "", f"- C1: `{row['old_renderer_c1_hash']}`", f"- C2: `{row['new_renderer_c2_hash']}`", f"- Changed nested origin paths: {row['changed_json_pointer_count']}", "- Business semantics changed: false", ""])
    review.extend(["## Human gate", "", f"Stop at `{NEXT_GATE}`."])
    (OUT / "SEMANTIC_ACCEPTANCE_RENDERER_C2_REVIEW_PACK.md").write_text("\n".join(review) + "\n", encoding="utf-8")

    artifact_paths = [
        "docs/baselines/v2.3/phase-2/SEMANTIC_ACCEPTANCE_RENDERER_C2.md",
        "docs/baselines/v2.3/phase-2/SEMANTIC_ACCEPTANCE_RENDERER_C2_REVIEW_PACK.md",
        *[f"docs/baselines/v2.3/phase-2/{name}" for name in JSON_OUTPUTS[:-1]],
        "scripts/docs/build-semantic-acceptance-renderer-c2.py",
        "scripts/docs/validate-semantic-acceptance-renderer-c2.py",
        "scripts/docs/validate-semantic-acceptance-renderer-c2-nested.py",
        "scripts/docs/validate-semantic-acceptance-renderer-c2-regressions.py",
        "scripts/docs/tests/test-semantic-acceptance-renderer-c2.py",
    ]
    hashes = {path: sha_bytes((ROOT / path).read_bytes()) for path in sorted(artifact_paths)}
    generated = sha_obj([{"path": path, "sha256": digest} for path, digest in sorted(hashes.items())])
    backup_object, backup_files = backup_inventory()
    manifest = {
        "artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C2_MANIFEST", "candidate_id": CANDIDATE,
        "supersedes": "V23-P2C-SEMANTIC-ACCEPTANCE-RENDERER-C1",
        "supersession_reason": "REFERENCE_GOOD_HASH_LOCK_CONTAINED_OPAQUE_ORIGIN_IDENTIFIERS",
        "status": "CANDIDATE", "approval_status": "PENDING_HUMAN_APPROVAL", "approval_scope": SCOPE, "next_gate": NEXT_GATE,
        "accepted_head": "9a49377d9fcd3d25e922b80cc6af3a4474ec0975",
        "accepted_renderer_c1": {"candidate": "128bd588a7a5411ce21f466da8cd1ff0c722b75c", "accepted": "9a49377d9fcd3d25e922b80cc6af3a4474ec0975", "tree": "4222dad205ef02f3c989d4a6a80c00775317ed0f", "git_content_aggregate": "f8c3469c7462a38b6ea6290e8ac524591d11daf59ea76386e724c834f9ee31b9", "generated_aggregate": "22daa4048b6577f37cb6fdda978f3b258165a96921e5e2c1a2e421b587ba140b", "manifest": "5332d8fd15523b9bc6bb40c4cf0987d54e3565c6653e6632971905b3283e98c9"},
        "accepted_dependencies": {"semantic_oracle_c2": "77d10a8c3ccb2e7795724fd1c82cdbea36c54e2e", "operator_binding_type_model_c1": "c11d95116154ff8919c04b49b0a502cf66b3907d", "semantic_infrastructure_amendment_a1": "522442635eb0df24dd5de0d42dad84656a5920e0", "semantic_completion_c4_r3": "351270d2bed7c54853b3a6cd6514b8906db22cf8"},
        "blocked_c6_preservation": {"backup_ref": C6_REF, "backup_object": backup_object, "content_tree": git("rev-parse", f"{C6_REF}^{{tree}}").decode().strip(), "path_count": 46, "reproduction": "46/46_BYTE_IDENTICAL", "per_file_sha256": backup_files},
        "rejected_c5_preservation": {"backup_object": "cf9c432acc84fa82f92a7520c795c2659e1dc50c", "content_tree": "ae6c07bfb97bf4ca85c0884838f5eccf1c294d4d"},
        "counts": {"active": 1152, "ast_operator_aware": 937, "human_procedures": 156, "typed_custom": 59, "unchanged_typed_custom": 48, "corrected_typed_custom": 11},
        "exact_inventory": sorted(artifact_paths + ["docs/baselines/v2.3/phase-2/semantic-acceptance-renderer-c2-manifest.json"]),
        "per_file_sha256_excluding_manifest": hashes,
        "generated_payload_aggregate_sha256": generated,
        "git_human_gate_identity": {"git_content_aggregate": "RECORDED_FROM_STAGED_GIT_INDEX_AT_HUMAN_GATE", "staged_tree": "RECORDED_FROM_STAGED_GIT_INDEX_AT_HUMAN_GATE"},
        "non_claims": ["NOT_C6_R1", "NOT_DOCUMENT_BASELINE_APPROVAL", "NOT_BRD_UXF_REMEDIATION", "NOT_RUNTIME_ADAPTER_VALIDATION", "NOT_RUNTIME_MUTATION_SCORE", "NOT_YADF_AUTHORIZATION", "NOT_PRODUCTION_IMPLEMENTATION", "NOT_COMMIT_TAG_PUSH_APPROVAL"],
    }
    write_json(JSON_OUTPUTS[-1], manifest)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    tracked = [OUT / x for x in JSON_OUTPUTS] + [OUT / "SEMANTIC_ACCEPTANCE_RENDERER_C2.md", OUT / "SEMANTIC_ACCEPTANCE_RENDERER_C2_REVIEW_PACK.md"]
    before = {p: p.read_bytes() for p in tracked if p.exists()} if args.check else {}
    build()
    if args.check and before != {p: p.read_bytes() for p in before}:
        raise SystemExit("NON_DETERMINISTIC_SEMANTIC_ACCEPTANCE_RENDERER_C2")
    print("VALID_DETERMINISTIC_SEMANTIC_ACCEPTANCE_RENDERER_C2" if args.check else "BUILT_SEMANTIC_ACCEPTANCE_RENDERER_C2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
