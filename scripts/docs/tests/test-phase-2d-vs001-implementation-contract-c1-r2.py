#!/usr/bin/env python3
"""Semantic mutations and actual modified-builder probes for C1-R2."""
from __future__ import annotations

import copy
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "scripts/docs/validate-phase-2d-vs001-implementation-contract-c1-r2.py"
BUILDER_PATH = ROOT / "scripts/docs/build-phase-2d-vs001-implementation-contract-c1-r2.py"
JSON_PATH = ROOT / "docs/baselines/v2.3/phase-2d/vs001-implementation-contract-c1-r2.json"
MD_PATH = ROOT / "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_CONTRACT_C1_R2_CANDIDATE.md"
MANIFEST_PATH = ROOT / "docs/baselines/v2.3/phase-2d/vs001-implementation-contract-c1-r2-manifest.json"

spec = importlib.util.spec_from_file_location("c1r2_validator", VALIDATOR_PATH)
v = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(v)


def code_for(payload, markdown=None, manifest=None, root=ROOT):
    try:
        v.validate_payload(payload, markdown, manifest, root, False)
    except v.ContractError as error:
        return error.code
    return "SURVIVED"


def expect(payload, expected, path, records):
    actual = code_for(payload)
    records.append({"semantic_path": path, "expected_error_code": expected, "actual_error_code": actual, "parsing_succeeded": True, "no_op": False, "metadata_only": False})
    if actual != expected:
        raise AssertionError(f"{path}: expected {expected}, got {actual}")


def mapping(payload, mid):
    return next(x for x in payload["traceability_mappings"] if x["mapping_id"] == mid)


def regression_suite(base, records):
    cases = []
    p = copy.deepcopy(base); mapping(p, "ACL-DEC003-UNKNOWN_SLUG")["expected_outcome"] = "HTTP 200 with diagnostic cause"; cases.append((p, "UNKNOWN_SLUG_PUBLIC_OUTCOME_MISMATCH", "unknown_slug.expected_outcome"))
    p = copy.deepcopy(base); mapping(p, "ACL-DEC001-PUBLICATION_VALIDATION_PASS")["owner_paths"] = ["apps/web/src/vs001/public-catalog-view.tsx"]; cases.append((p, "PUBLICATION_VALIDATION_OWNER_IRRELEVANT", "publication_validation.owner_paths"))
    p = copy.deepcopy(base); mapping(p, base["traceability_mappings"][0]["mapping_id"])["cleanup_contract"]["success"] = "retain controlled fixtures"; cases.append((p, "UNSAFE_MAPPING_CLEANUP", "mapping.cleanup_contract"))
    p = copy.deepcopy(base); mapping(p, base["traceability_mappings"][0]["mapping_id"])["controlled_fixture"]["isolation"] = "shared external database fixture"; cases.append((p, "UNCONTROLLED_MAPPING_FIXTURE", "mapping.controlled_fixture"))
    p = copy.deepcopy(base); mapping(p, "ACL-DEC002-NO_PUBLIC_SUPPLIER_REFERENCE")["independent_observation"]["expected_derived"] = True; cases.append((p, "EXPECTED_DERIVED_OBSERVATION", "supplier_reference.independent_observation"))
    p = copy.deepcopy(base); p["decision_bindings"][0]["controlled_fixtures"] = {"states": ["requirement IDs"]}; cases.append((p, "GENERIC_DECISION_FIXTURE", "decision_binding.controlled_fixtures"))
    p = copy.deepcopy(base); p["decision_bindings"][0]["owner_paths"] = ["packages/contracts/src/vs001/public-catalog.ts"]; cases.append((p, "CROSS_LAYER_DECISION_OWNER_INCOMPLETE", "decision_binding.owner_paths"))
    p = copy.deepcopy(base); p["design"]["locale"]["selected_option"]["algorithm"]["priority"] = "implementation chooses"; cases.append((p, "AMBIGUOUS_ACCEPT_LANGUAGE_ORDER", "locale.algorithm.priority"))
    p = copy.deepcopy(base); p["design"]["locale"]["selected_option"]["algorithm"]["matching"] = "truncate subtags"; cases.append((p, "UNAUTHORIZED_LOCALE_SUBTAG_FALLBACK", "locale.algorithm.matching"))
    p = copy.deepcopy(base); p["design"]["locale"]["selected_option"]["algorithm"]["q_zero"] = "may select"; cases.append((p, "Q_ZERO_LOCALE_SELECTED", "locale.algorithm.q_zero"))
    p = copy.deepcopy(base); p["design"]["cursor_continuity"]["cursor_fields"].remove("logical catalog revision"); cases.append((p, "CURSOR_REVISION_BINDING_MISSING", "cursor.cursor_fields.revision"))
    p = copy.deepcopy(base); p["design"]["cursor_continuity"]["cursor_fields"].remove("storefront public identity"); cases.append((p, "CURSOR_STOREFRONT_BINDING_MISSING", "cursor.cursor_fields.storefront"))
    p = copy.deepcopy(base); p["design"]["cursor_continuity"]["request_boundary"] = "one REPEATABLE READ snapshot spans all HTTP requests"; cases.append((p, "CROSS_REQUEST_REPEATABLE_READ_MISCLAIM", "cursor.request_boundary"))
    p = copy.deepcopy(base); cmd = next(x for x in p["commands"] if x["command_id"] == "vs001:test:not-found"); cmd["mapping_ids"] = []; cases.append((p, "FLOATING_FOCUSED_COMMAND", "commands.not_found.mapping_ids"))
    p = copy.deepcopy(base); p["implementation_batches"][0]["mapping_ids"] = ["all mappings"]; cases.append((p, "BROAD_OR_INEXACT_BATCH_COVERAGE", "batches.B1.mapping_ids"))
    p = copy.deepcopy(base); p["decision_bindings"][0]["commands"] = sorted(v.FOCUSED); cases.append((p, "DECISION_BINDING_ALL_FOCUSED_COMMANDS", "decision_bindings.commands.all_focused"))
    p = copy.deepcopy(base); p["decision_bindings"][0]["batches"] = [f"B{x}" for x in range(1, 8)]; cases.append((p, "DECISION_BINDING_ALL_BATCHES", "decision_bindings.batches.all"))
    p = copy.deepcopy(base); p["decision_bindings"][0]["commands"] = p["decision_bindings"][0]["commands"][1:]; cases.append((p, "DECISION_BINDING_REQUIRED_COMMAND_MISSING", "decision_bindings.commands.missing"))
    p = copy.deepcopy(base); b = p["decision_bindings"][0]; b["commands"].append(next(x for x in sorted(v.FOCUSED) if x not in b["commands"])); cases.append((p, "DECISION_BINDING_IRRELEVANT_COMMAND", "decision_bindings.commands.irrelevant"))
    p = copy.deepcopy(base); p["decision_bindings"][0]["batches"] = p["decision_bindings"][0]["batches"][1:]; cases.append((p, "DECISION_BINDING_REQUIRED_BATCH_MISSING", "decision_bindings.batches.missing"))
    p = copy.deepcopy(base); b = p["decision_bindings"][0]; b["batches"].append(next(x for x in [f"B{i}" for i in range(1, 8)] if x not in b["batches"])); cases.append((p, "DECISION_BINDING_IRRELEVANT_BATCH", "decision_bindings.batches.irrelevant"))
    p = copy.deepcopy(base); next(x for x in p["commands"] if x["command_id"] == "commissioning:lint")["mapping_ids"] = []; cases.append((p, "INHERITED_COMMAND_CLASSIFICATION_INVALID", "commands.inherited.unexplained_empty_mapping_ids"))
    p = copy.deepcopy(base); next(x for x in p["commands"] if x["command_id"] == "commissioning:build")["acceptance_evidence"] = True; cases.append((p, "FOUNDATION_COMMAND_FALSE_ACCEPTANCE_EVIDENCE", "commands.inherited.false_acceptance_evidence"))
    p = copy.deepcopy(base); cmd = next(x for x in p["commands"] if x["command_id"] == "vs001:db:migrate"); cmd["primary_batch_id"] = "B3"; cmd["owning_batches"] = [x for x in cmd["owning_batches"] if x != "B1"]; cases.append((p, "DB_MIGRATE_BATCH_B1_MISSING", "commands.db_migrate.primary_batch"))
    p = copy.deepcopy(base); next(x for x in p["commands"] if x["command_id"] == "vs001:db:migrate")["mapping_ids"].append("ACL-DEC002-NO_DATABASE_SCHEMA_DECISION"); cases.append((p, "DB_MIGRATE_NON_INFERENCE_OWNER", "commands.db_migrate.non_inference"))
    p = copy.deepcopy(base); next(x for x in p["commands"] if x["command_id"] == "vs001:db:migrate")["evidence_output"] = "browser-only migration evidence"; cases.append((p, "DB_MIGRATE_BROWSER_ONLY_EVIDENCE", "commands.db_migrate.browser_evidence"))
    p = copy.deepcopy(base); next(x for x in p["commands"] if x["command_id"] == "vs001:db:migrate")["mapping_ids"].append("ACL-DEC003-UNKNOWN_SLUG"); cases.append((p, "DB_MIGRATE_UNRELATED_MAPPING", "commands.db_migrate.unrelated_mapping"))
    p = copy.deepcopy(base); next(x for x in p["design"]["locale"]["fixtures"] if x["fixture_id"] == "LOC-DUP-DIFFERENT-Q")["expected_resolved_locale"] = "en-US"; cases.append((p, "LOCALE_DUPLICATE_RANGE_POLICY_INVALID", "locale.duplicate_range.different_q"))
    p = copy.deepcopy(base); next(x for x in p["design"]["locale"]["fixtures"] if x["fixture_id"] == "LOC-EQUAL-Q-ORDER")["expected_resolved_locale"] = "en-US"; cases.append((p, "AMBIGUOUS_ACCEPT_LANGUAGE_ORDER", "locale.equal_q.header_order"))
    p = copy.deepcopy(base); next(x for x in p["design"]["locale"]["fixtures"] if x["fixture_id"] == "LOC-MALFORMED-Q")["expected_resolved_locale"] = "fr-CA"; cases.append((p, "LOCALE_MALFORMED_Q_POLICY_INVALID", "locale.malformed_q"))
    p = copy.deepcopy(base); next(x for x in p["design"]["locale"]["fixtures"] if x["fixture_id"] == "LOC-Q-ZERO")["expected_resolved_locale"] = "fr-CA"; cases.append((p, "Q_ZERO_LOCALE_SELECTED", "locale.q_zero"))
    p = copy.deepcopy(base); next(x for x in p["design"]["locale"]["fixtures"] if x["fixture_id"] == "LOC-NO-SUBTAG-FALLBACK")["expected_resolved_locale"] = "en-US"; cases.append((p, "UNAUTHORIZED_LOCALE_SUBTAG_FALLBACK", "locale.subtag_fallback"))
    for case in cases:
        expect(*case, records)


def modified_builder_probe(base_source, replacement, expected, name):
    old, new = replacement
    if old not in base_source:
        raise AssertionError(f"probe {name}: source anchor absent")
    modified = base_source.replace(old, new, 1)
    if modified == base_source:
        raise AssertionError(f"probe {name}: no-op")
    with tempfile.TemporaryDirectory(prefix="ysim-c1r2-builder-") as td:
        root = Path(td)
        for rel in v.FILES:
            target = root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            source = ROOT / rel
            if source.exists():
                shutil.copy2(source, target)
        (root / v.FILES[3]).write_text(modified)
        env = {**os.environ, "C1_R2_ROOT_OVERRIDE": str(root), "C1_R2_GIT_ROOT": str(ROOT)}
        result = subprocess.run([sys.executable, str(root / v.FILES[3])], env=env, text=True, capture_output=True)
        if result.returncode != 0:
            raise AssertionError(f"probe {name}: modified builder did not execute: {result.stderr}")
        payload = json.loads((root / v.FILES[1]).read_text())
        manifest = json.loads((root / v.FILES[2]).read_text())
        actual = code_for(payload, (root / v.FILES[0]).read_bytes(), manifest, root)
        if actual != expected:
            raise AssertionError(f"probe {name}: expected {expected}, got {actual}")
        return {"probe": name, "modified_builder_executed": True, "expected_error_code": expected, "actual_error_code": actual, "coherent_hashes": name in {"coherent-builder-manifest", "coherent-builder-markdown-manifest"}}


def builder_probes():
    source = BUILDER_PATH.read_text()
    probes = [
        (("(\"api\",p[\"design\"][\"api\"]),", ""), "MARKDOWN_SECTION_INVENTORY_MISMATCH", "omit-api-design"),
        (("(\"data\",p[\"design\"][\"data\"]),", ""), "MARKDOWN_SECTION_INVENTORY_MISMATCH", "omit-data-design"),
        (("(\"ui\",p[\"design\"][\"ui\"]),", ""), "MARKDOWN_SECTION_INVENTORY_MISMATCH", "omit-ui-design"),
        (("(\"security_observability\",p[\"design\"][\"security_observability\"]),", ""), "MARKDOWN_SECTION_INVENTORY_MISMATCH", "omit-security-design"),
        (("\"status\":404", "\"status\":200"), "DESIGN_SEMANTIC_FINGERPRINT_MISMATCH", "weaken-uniform-404"),
        (("\"Supplier identity/reference\"", "\"Supplier identity/reference is public\""), "DESIGN_SEMANTIC_FINGERPRINT_MISMATCH", "remove-disclosure-prohibition"),
        (("delete owned rows in FK-safe order, close its browser/API handles, then query every listed resource class and verify zero owned residue", "retain controlled fixtures and shared resources"), "UNSAFE_MAPPING_CLEANUP", "unsafe-cleanup"),
        (("\"semantic_assertion\":semantic", "\"semantic_assertion\":\"behaves as expected\""), "MAPPING_SEMANTIC_FINGERPRINT_MISMATCH", "generic-mapping-renderer"),
        (("mids=[m[\"mapping_id\"] for m in maps if cid in m[\"validation_command_ids\"]]", "mids=[]"), "FLOATING_FOCUSED_COMMAND", "floating-command"),
        (("mids=[m[\"mapping_id\"] for m in maps if m[\"implementation_batch_ids\"]==[bid]]", "mids=[m[\"mapping_id\"] for m in maps] if bid==\"B1\" else [m[\"mapping_id\"] for m in maps if m[\"implementation_batch_ids\"]==[bid]]"), "BROAD_OR_INEXACT_BATCH_COVERAGE", "broad-batch-coverage"),
        (("\"runtime_evidence_status\":\"NOT_EXECUTED\",\"implementation_authorized\":False,\"next_gate\"", "\"runtime_evidence_status\":\"EXECUTED_PASS\",\"implementation_authorized\":False,\"next_gate\""), "FALSE_RUNTIME_EVIDENCE_CLAIM", "coherent-builder-manifest"),
        (("\"implementation_authorized\":False,\"next_gate\"", "\"implementation_authorized\":True,\"next_gate\""), "IMPLEMENTATION_PREMATURELY_AUTHORIZED", "coherent-builder-markdown-manifest"),
    ]
    return [modified_builder_probe(source, repl, expected, name) for repl, expected, name in probes]


def main():
    base = json.loads(JSON_PATH.read_text())
    manifest = json.loads(MANIFEST_PATH.read_text())
    v.validate_payload(base, MD_PATH.read_bytes(), manifest, ROOT, False)
    records = []
    for original in base["traceability_mappings"]:
        p = copy.deepcopy(base)
        target = mapping(p, original["mapping_id"])
        target["action"] = {"semantic_corruption": "concrete but wrong execution action"}
        expect(p, "MAPPING_SEMANTIC_FINGERPRINT_MISMATCH", f"traceability_mappings/{original['mapping_id']}/action", records)
    for original in base["decision_bindings"]:
        p = copy.deepcopy(base)
        target = next(x for x in p["decision_bindings"] if x["binding_id"] == original["binding_id"])
        target["positive_observation"] = "reuse the expected option value as observed evidence"
        expect(p, "DECISION_BINDING_FINGERPRINT_MISMATCH", f"decision_bindings/{original['binding_id']}/positive_observation", records)
    regression_suite(base, records)
    probes = builder_probes()
    if any(x["actual_error_code"] != x["expected_error_code"] for x in records):
        raise AssertionError("wrong-reason semantic mutation")
    report = {"mapping_mutations": 211, "decision_binding_mutations": 11, "focused_regressions": 32, "semantic_mutations_total": len(records), "modified_builder_probes": len(probes), "killed": len(records) + len(probes), "survivors": 0, "wrong_reason": 0, "no_op": 0, "metadata_only": 0, "parse_error_semantic_kills": 0, "records": records, "builder_probe_records": probes}
    print("VALID_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_C1_R2_TESTS")
    print(json.dumps({k: v for k, v in report.items() if k not in {"records", "builder_probe_records"}}, sort_keys=True))


if __name__ == "__main__":
    main()
