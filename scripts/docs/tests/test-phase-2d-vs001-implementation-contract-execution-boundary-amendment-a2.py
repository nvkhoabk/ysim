#!/usr/bin/env python3
"""Semantic mutations and coherent modified-builder probes for amendment A2."""
from __future__ import annotations

import copy
import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "scripts/docs/validate-phase-2d-vs001-implementation-contract-execution-boundary-amendment-a2.py"
BUILDER_PATH = ROOT / "scripts/docs/build-phase-2d-vs001-implementation-contract-execution-boundary-amendment-a2.py"
JSON_PATH = ROOT / "docs/baselines/v2.3/phase-2d/vs001-implementation-contract-execution-boundary-amendment-a2.json"

spec = importlib.util.spec_from_file_location("a1_r2_validator", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(validator)


def mutate(name: str, expected: str, change) -> dict[str, object]:
    payload = copy.deepcopy(BASE)
    before = validator.canonical(payload)
    change(payload)
    after = validator.canonical(payload)
    if before == after:
        raise AssertionError(f"{name}: no-op")
    try:
        validator.validate_payload(payload, CONTRACT)
    except validator.AmendmentError as exc:
        if exc.code != expected:
            raise AssertionError(f"{name}: expected {expected}, got {exc.code}: {exc}") from exc
        return {"name": name, "semantic_path_changed": True, "expected": expected, "actual": exc.code, "parsing": "PASS", "no_op": False, "metadata_only": False}
    raise AssertionError(f"{name}: survived")


def coherent_builder_probe(name: str, old: str, new: str, expected: str) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="ysim-a2-builder-probe-") as tmp_name:
        tmp = Path(tmp_name)
        for rel in (validator.BUILDER_REL, validator.VALIDATOR_REL, validator.TEST_REL):
            target = tmp / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, target)
        builder = tmp / validator.BUILDER_REL
        source = builder.read_text(encoding="utf-8")
        if old not in source:
            raise AssertionError(f"{name}: probe target absent")
        builder.write_text(source.replace(old, new, 1), encoding="utf-8", newline="\n")
        env = dict(os.environ)
        env["A2_GIT_ROOT"] = str(ROOT)
        completed = subprocess.run(["python3", str(builder), "--output-root", str(tmp)], cwd=ROOT, env=env, text=True, capture_output=True)
        if completed.returncode != 0:
            raise AssertionError(f"{name}: modified builder did not execute: {completed.stderr or completed.stdout}")
        try:
            validator.validate_files(tmp)
        except validator.AmendmentError as exc:
            if exc.code != expected:
                raise AssertionError(f"{name}: expected {expected}, got {exc.code}: {exc}") from exc
            return {"name": name, "builder_executed": True, "coherent_json_markdown_manifest": True, "expected": expected, "actual": exc.code, "survivor": False, "parse_error": False}
        raise AssertionError(f"{name}: coherent defective builder survived")


def support_artifact(payload: dict[str, object]) -> dict[str, object]:
    return next(x for x in payload["evidence_file_catalog"] if x["artifact_category"] == "EXECUTION_SUPPORT_ARTIFACT")


def second_support_artifact(payload: dict[str, object]) -> dict[str, object]:
    return [x for x in payload["evidence_file_catalog"] if x["artifact_category"] == "EXECUTION_SUPPORT_ARTIFACT"][1]


def support_record(payload: dict[str, object]) -> dict[str, object]:
    return payload["support_record_catalog"][0]


def docker_support(payload: dict[str, object]) -> dict[str, object]:
    return next(x for x in payload["support_record_catalog"] if x["support_kind"] == "DOCKER_BEFORE_AFTER_PRESERVATION")


def other_support_path_same_batch(payload: dict[str, object], record: dict[str, object]) -> str:
    return next(x["path"] for x in payload["evidence_file_catalog"] if x["artifact_category"] == "EXECUTION_SUPPORT_ARTIFACT" and x["producer_batch"] == record["producer_batch"] and x["path"] != record["artifact_file_path"])


def main() -> None:
    global BASE, CONTRACT
    BASE = json.loads(JSON_PATH.read_bytes())
    CONTRACT, _ = validator.accepted_contract()
    validator.validate_payload(BASE, CONTRACT)
    mutations = [
        mutate("EMPTY_FILE_CONTAINMENT", "A2_ARTIFACT_EMPTY_CONTAINMENT", lambda p: support_artifact(p).update({"contained_mapping_lineage_record_ids": [], "contained_support_record_ids": [], "contained_support_revalidation_record_ids": []})),
        mutate("UNKNOWN_SUPPORT_ID", "A2_SUPPORT_UNKNOWN_ID", lambda p: support_artifact(p)["contained_support_record_ids"].append("SUP-UNKNOWN")),
        mutate("SUPPORT_ID_REUSED", "A2_SUPPORT_ID_REUSED", lambda p: second_support_artifact(p)["contained_support_record_ids"].append(support_artifact(p)["contained_support_record_ids"][0])),
        mutate("SUPPORT_WRONG_FILE", "A2_SUPPORT_WRONG_FILE", lambda p: support_record(p).update({"artifact_file_path": other_support_path_same_batch(p, support_record(p))})),
        mutate("SUPPORT_POINTER_OUTSIDE_NAMESPACE", "A2_SUPPORT_POINTER_NAMESPACE", lambda p: support_record(p).update({"record_pointer": "/records/not-support"})),
        mutate("SUPPORT_PRODUCER_UNSCHEDULED", "A2_SUPPORT_PRODUCER_UNSCHEDULED", lambda p: support_record(p).update({"producer_batch": "B7" if support_record(p)["producer_batch"] != "B7" else "B1"})),
        mutate("SUPPORT_PATH_UNAUTHORIZED", "A2_SUPPORT_PATH_UNAUTHORIZED", lambda p: support_record(p).update({"artifact_file_path": "artifacts/vs001/unauthorized/support.json"})),
        mutate("SUPPORT_CONTENT_IDENTITY_MISSING", "A2_SUPPORT_CONTENT_IDENTITY", lambda p: support_record(p).update({"content_sha256_or_git_blob_requirement": ""})),
        mutate("SUPPORT_CLEANUP_MISSING", "A2_SUPPORT_CLEANUP_MISSING", lambda p: support_record(p).update({"cleanup_evidence_record_id": None})),
        mutate("SUPPORT_B7_ROUTE_MISSING", "A2_SUPPORT_B7_ROUTE_MISSING", lambda p: support_record(p).update({"b7_support_revalidation_record_id": None})),
        mutate("COMMAND_ZERO_EXECUTABLE_RECORDS", "A2_COMMAND_ZERO_EXECUTABLE_RECORDS", lambda p: next(x for x in p["command_path_record_closure"] if x["command_id"] == "vs001:audit:docker").update({"mapping_lineage_record_ids_produced": [], "support_record_ids_produced": [], "support_revalidation_record_ids_produced": [], "executable_record_count": 0, "orphan": True})),
        mutate("SUPPORT_ONLY_FALSE_ACCEPTANCE", "A2_SUPPORT_ONLY_FALSE_ACCEPTANCE", lambda p: support_record(p).update({"direct_acceptance_evidence": True})),
        mutate("B7_SUPPORT_UNION_OMITS_RECORD", "A2_B7_SUPPORT_UNION_INCOMPLETE", lambda p: p["b7_dual_revalidation_contract"]["execution_support_union"]["source_support_record_ids"].pop()),
        mutate("B7_MAPPING_IGNORES_SUPPORT", "A2_B7_MAPPING_WITHOUT_SUPPORT", lambda p: p["b7_dual_revalidation_contract"].update({"final_mapping_closure_requires_complete_support_union": False})),
        mutate("STORED_SUPPORT_PASS", "A2_SUPPORT_STORED_PASS_REPLAY", lambda p: support_record(p).update({"runtime_status": "PASS"})),
        mutate("CATEGORY_CHANGED_TO_EVADE_CONTAINMENT", "A2_ARTIFACT_CATEGORY", lambda p: support_artifact(p).update({"artifact_category": "MAPPING_EVIDENCE_ARTIFACT"})),
        mutate("MANIFEST_SUPPORT_REMOVED", "A2_MANIFEST_SUPPORT_LINEAGE_MISSING", lambda p: p["support_record_catalog"].remove(next(x for x in p["support_record_catalog"] if x["artifact_file_path"].endswith("candidate-manifest.json")))),
        mutate("DOCKER_SUPPORT_RETARGETED", "A2_DOCKER_SUPPORT_PRODUCER", lambda p: docker_support(p).update({"producer_command_id": "vs001:batch:validate"})),
        mutate("WRONG_MAPPING_LINEAGE_PRODUCER", "A2_LINEAGE_PRODUCER", lambda p: p["evidence_lineage_requirements"][0].update({"producer_command_id": "vs001:audit:docker"})),
        mutate("PACKAGE_SCRIPT_RETARGET", "A2_PACKAGE_SCRIPT_TARGET", lambda p: p["package_script_bindings"][0].update({"exact_command_string": "node scripts/commissioning/audit-versions.mjs", "target_executable_file": "scripts/commissioning/audit-versions.mjs"})),
        mutate("FUTURE_API_PATH_IN_B1", "A2_B1_FUTURE_BATCH_PRODUCT_PATH_LEAKAGE", lambda p: (p["path_authorization"][0]["PRODUCT_IMPLEMENTATION_PATH"].append("apps/api/src/vs001/public-catalog.controller.ts"), p["path_authorization"][0]["exact_authorized_paths"].append("apps/api/src/vs001/public-catalog.controller.ts"), p["path_authorization"][0]["exact_authorized_paths"].sort())),
        mutate("AUTHORIZE_LOCKFILE", "A2_PROTECTED_PATH", lambda p: (p["path_authorization"][0]["exact_authorized_paths"].append("pnpm-lock.yaml"), p["path_authorization"][0]["exact_authorized_paths"].sort())),
        mutate("REMOVE_B4_PROVISIONAL", "A2_BATCH_PROVISIONAL_MISMATCH", lambda p: p["seven_batch_matrix"][3]["per_batch_provisional_evidence_mapping_ids"].pop()),
        mutate("TOP_LEVEL_RUNTIME_PASS", "A2_RUNTIME_CLAIM", lambda p: p.update({"runtime_evidence_status": "PASS"})),
    ]

    probes = [
        coherent_builder_probe("EMPTY_ARTIFACT_CONTAINMENT", '"evidence_file_catalog": evidence_files,', '"evidence_file_catalog": (lambda rows: (next(x for x in rows if x["artifact_category"] == "EXECUTION_SUPPORT_ARTIFACT")["contained_support_record_ids"].clear() or rows))(evidence_files),', "A2_ARTIFACT_EMPTY_CONTAINMENT"),
        coherent_builder_probe("UNFROZEN_CMDREC_REINTRODUCED", '"support_record_catalog": support_records,', '"unfrozen_support_reference": "CMDREC-B1-vs001-audit-docker", "support_record_catalog": support_records,', "A2_UNFROZEN_CMDREC"),
        coherent_builder_probe("SUPPORT_ID_REUSED", '"support_record_catalog": support_records,', '"support_record_catalog": (lambda rows: (evidence_files[1]["contained_support_record_ids"].append(evidence_files[0]["contained_support_record_ids"][0]) or rows))(support_records),', "A2_SUPPORT_ID_REUSED"),
        coherent_builder_probe("SUPPORT_RECORD_REMOVED", '"support_record_catalog": support_records,', '"support_record_catalog": support_records[1:],', "A2_SUPPORT_CATALOG_POPULATION"),
        coherent_builder_probe("COMMAND_ZERO_RECORDS", '"command_path_record_closure": command_closure,', '"command_path_record_closure": (lambda rows: (rows[0].update({"mapping_lineage_record_ids_produced": [], "support_record_ids_produced": [], "support_revalidation_record_ids_produced": [], "executable_record_count": 0, "orphan": True}) or rows))(command_closure),', "A2_COMMAND_ZERO_EXECUTABLE_RECORDS"),
        coherent_builder_probe("B7_SUPPORT_UNION_INCOMPLETE", '"source_support_record_ids": sorted(x["support_record_id"] for x in support_records)', '"source_support_record_ids": sorted(x["support_record_id"] for x in support_records)[:-1]', "A2_B7_SUPPORT_UNION_INCOMPLETE"),
        coherent_builder_probe("DOCKER_SUPPORT_PRODUCER_CHANGED", 'support_records.sort(key=lambda row: row["support_record_id"])', 'next(x for x in support_records if x["support_kind"] == "DOCKER_BEFORE_AFTER_PRESERVATION")["producer_command_id"] = "vs001:batch:validate"\n    support_records.sort(key=lambda row: row["support_record_id"])', "A2_DOCKER_SUPPORT_PRODUCER"),
        coherent_builder_probe("CLEANUP_SUPPORT_REMOVED", 'record["cleanup_evidence_record_id"] = cleanup_support_by_batch[record["producer_batch"]]', 'record["cleanup_evidence_record_id"] = None', "A2_SUPPORT_CLEANUP_MISSING"),
        coherent_builder_probe("MANIFEST_SUPPORT_LINEAGE_REMOVED", '"support_record_catalog": support_records,', '"support_record_catalog": [x for x in support_records if not x["artifact_file_path"].endswith("candidate-manifest.json")],', "A2_MANIFEST_SUPPORT_LINEAGE_MISSING"),
        coherent_builder_probe("COHERENT_ARTIFACT_CATEGORY_CHANGE", '"evidence_file_catalog": evidence_files,', '"evidence_file_catalog": (lambda rows: (next(x for x in rows if x["artifact_category"] == "EXECUTION_SUPPORT_ARTIFACT").update({"artifact_category": "MAPPING_EVIDENCE_ARTIFACT"}) or rows))(evidence_files),', "A2_ARTIFACT_CATEGORY"),
        coherent_builder_probe("STORED_SUPPORT_PASS", '"support_record_catalog": support_records,', '"support_record_catalog": (lambda rows: (rows[0].update({"runtime_status": "PASS"}) or rows))(support_records),', "A2_SUPPORT_STORED_PASS_REPLAY"),
        coherent_builder_probe("MAPPING_CLOSURE_WITHOUT_SUPPORT", '"final_mapping_closure_requires_complete_support_union": True', '"final_mapping_closure_requires_complete_support_union": False', "A2_B7_MAPPING_WITHOUT_SUPPORT"),
    ]

    report = {"semantic_mutations": {"executed": len(mutations), "killed": len(mutations), "survivors": 0, "wrong_reason": 0, "no_op": 0, "metadata_only": 0, "parse_error": 0}, "modified_builder_probes": {"executed": len(probes), "rejected": len(probes), "coherent_survivors": 0, "wrong_reason": 0, "no_op": 0, "parse_error": 0}, "total_checks": len(mutations) + len(probes), "results": mutations, "probes": probes}
    print(json.dumps(report, sort_keys=True))
    print("PASS_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2_TESTS")


if __name__ == "__main__":
    main()
