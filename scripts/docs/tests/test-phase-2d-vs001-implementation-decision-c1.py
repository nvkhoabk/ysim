#!/usr/bin/env python3
"""Semantic mutations and modified-builder probes for implementation decision C1."""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import tempfile
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "scripts/docs/validate-phase-2d-vs001-implementation-decision-c1.py"
SOURCE = ROOT / "docs/baselines/v2.3/phase-2d/vs001-implementation-decision-c1.json"
BUILDER = ROOT / "scripts/docs/build-phase-2d-vs001-implementation-decision-c1.py"
spec = importlib.util.spec_from_file_location("impl_decision_validator", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def expect_failure(payload: dict, expected_prefix: str) -> None:
    try:
        validator.validate_payload(payload, enforce_root_hash=False)
    except validator.ValidationFailure as exc:
        if not str(exc).startswith(expected_prefix + ":"):
            raise AssertionError(f"wrong reason: expected {expected_prefix}, got {exc}") from exc
        return
    raise AssertionError(f"mutation survived: {expected_prefix}")


def semantic_mutations(payload: dict) -> dict:
    executed = 0
    for index, decision in enumerate(payload["decisions"]):
        mutated = deepcopy(payload)
        del mutated["decisions"][index]
        expect_failure(mutated, "DECISION_SET_MISMATCH")
        executed += 1

        mutated = deepcopy(payload)
        mutated["decisions"][index]["selected_option"] = mutated["decisions"][index]["recommended_option"]
        expect_failure(mutated, "DECISION_PENDING_STATE_MISMATCH")
        executed += 1

        mutated = deepcopy(payload)
        mutated["decisions"][index]["recommended_option"] = "OPT-NOT-PRESENT"
        expect_failure(mutated, "RECOMMENDED_OPTION_MISSING")
        executed += 1

        mutated = deepcopy(payload)
        mutated["decisions"][index]["options"][0]["contract"] = "Works as expected."
        expect_failure(mutated, "GENERIC_DECISION_SEMANTICS")
        executed += 1
    return {"executed": executed, "killed": executed, "survivors": 0, "wrong_reason": 0}


def structural_mutations(payload: dict) -> dict:
    cases = []
    mutated = deepcopy(payload); mutated["candidate_id"] = "WRONG"; cases.append((mutated, "CANDIDATE_METADATA_MISMATCH"))
    mutated = deepcopy(payload); mutated["status"] = "APPROVED"; cases.append((mutated, "CANDIDATE_METADATA_MISMATCH"))
    mutated = deepcopy(payload); mutated["implementation_authorized"] = True; cases.append((mutated, "CANDIDATE_METADATA_MISMATCH"))
    mutated = deepcopy(payload); mutated["runtime_evidence_status"] = "PASS"; cases.append((mutated, "CANDIDATE_METADATA_MISMATCH"))
    mutated = deepcopy(payload); mutated["implementation_contract_created"] = True; cases.append((mutated, "CANDIDATE_METADATA_MISMATCH"))
    mutated = deepcopy(payload); mutated["authority_reconciliation"]["requirements_total"] = 24; cases.append((mutated, "RECONCILIATION_COUNT_MISMATCH"))
    mutated = deepcopy(payload); mutated["authority_reconciliation"]["requirement_ids"].pop(); cases.append((mutated, "REQUIREMENT_SET_MISMATCH"))
    mutated = deepcopy(payload); mutated["authority_reconciliation"]["effective_selections"]["V23-P2D-VS001-ACCEPTANCE-DEC-003"] = "WRONG"; cases.append((mutated, "GOVERNING_SELECTION_MISMATCH"))
    mutated = deepcopy(payload); mutated["technical_decision_audit"].pop(); cases.append((mutated, "TECHNICAL_AUDIT_INVENTORY_MISMATCH"))
    mutated = deepcopy(payload); mutated["technical_decision_audit"][1]["classification"] = "B"; cases.append((mutated, "NON_TYPE_C_DECISION_MAPPING"))
    mutated = deepcopy(payload); mutated["decisions"][0]["options"][1]["option_id"] = mutated["decisions"][0]["options"][0]["option_id"]; cases.append((mutated, "DECISION_OPTION_SET_MISMATCH"))
    mutated = deepcopy(payload); mutated["decision_accounting"]["selected"] = 1; cases.append((mutated, "DECISION_ACCOUNTING_MISMATCH"))
    for mutated, reason in cases:
        expect_failure(mutated, reason)
    return {"executed": len(cases), "killed": len(cases), "survivors": 0, "wrong_reason": 0}


def builder_probes(payload: dict) -> dict:
    replacements = [
        ("INJECT_OMIT_DECISION = False", "INJECT_OMIT_DECISION = True", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH"),
        ("INJECT_GENERIC_OPTION = False", "INJECT_GENERIC_OPTION = True", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH"),
        ("INJECT_REORDER = False", "INJECT_REORDER = True", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH"),
        ("INJECT_FALSE_RUNTIME = False", "INJECT_FALSE_RUNTIME = True", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH"),
        ("INJECT_OMIT_AUDIT = False", "INJECT_OMIT_AUDIT = True", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH"),
        ("INJECT_IMPLEMENTATION_TRUE = False", "INJECT_IMPLEMENTATION_TRUE = True", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH"),
    ]
    for old, new, reason in replacements:
        with tempfile.TemporaryDirectory(prefix="ysim-vs001-impl-decision-builder-probe-") as temp:
            temp_root = Path(temp)
            for relative in [
                "docs/baselines/v2.3/phase-2d/vs001-implementation-decision-c1.json",
                "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_DECISION_C1_CANDIDATE.md",
                "docs/baselines/v2.3/phase-2d/vs001-implementation-decision-c1-manifest.json",
                "scripts/docs/build-phase-2d-vs001-implementation-decision-c1.py",
                "scripts/docs/validate-phase-2d-vs001-implementation-decision-c1.py",
                "scripts/docs/tests/test-phase-2d-vs001-implementation-decision-c1.py",
            ]:
                target = temp_root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / relative, target)
            probe_builder = temp_root / "scripts/docs/build-phase-2d-vs001-implementation-decision-c1.py"
            source = probe_builder.read_text()
            if old not in source:
                raise AssertionError(f"probe marker absent: {old}")
            probe_builder.write_text(source.replace(old, new, 1))
            subprocess.run(["python3", str(probe_builder)], cwd=temp_root, check=True, capture_output=True)
            markdown = (temp_root / "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_DECISION_C1_CANDIDATE.md").read_bytes()
            relative_files = validator.FILES
            generated_files = {relative: (temp_root / relative).read_bytes() for relative in relative_files}
            generated_manifest = json.loads(generated_files[relative_files[2]])
            # The defective builder has coherently updated its own hash and the
            # manifest. Independent semantic projection must still reject it.
            validator.validate_manifest(payload, generated_manifest, generated_files)
            try:
                validator.validate_markdown(payload, markdown)
            except validator.ValidationFailure as exc:
                if not str(exc).startswith(reason + ":"):
                    raise AssertionError(f"builder probe wrong reason: {exc}") from exc
            else:
                raise AssertionError(f"defective builder survived: {old}")
    return {"actual_modified_builder_executions": len(replacements), "rejected": len(replacements), "coherent_survivors": 0}


def main() -> None:
    before = SOURCE.read_bytes()
    payload = json.loads(before)
    semantic = semantic_mutations(payload)
    structural = structural_mutations(payload)
    probes = builder_probes(payload)
    if SOURCE.read_bytes() != before:
        raise AssertionError("repository candidate JSON changed during tests")
    result = {"semantic_mutations": semantic, "structural_mutations": structural, "builder_probes": probes, "total_mutations": semantic["executed"] + structural["executed"], "survivors": 0}
    print(json.dumps(result, sort_keys=True))
    print("VALID_VS001_IMPLEMENTATION_DECISION_C1_MUTATIONS_AND_BUILDER_PROBES")


if __name__ == "__main__":
    main()
