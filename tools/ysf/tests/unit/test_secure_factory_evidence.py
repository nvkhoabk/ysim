from __future__ import annotations

import json
from pathlib import Path

import pytest

from ysf.secure_factory.evidence import (
    EvidenceLedger,
    build_manifest,
    digest_file,
    verify_manifest,
    write_exclusive,
)
from ysf.secure_factory.models import FactoryFailure, FileDigest


def test_ledger_is_append_only_and_execution_id_is_unique(tmp_path: Path) -> None:
    checkout = tmp_path / "repo"
    checkout.mkdir()
    output = tmp_path / "evidence"
    ledger = EvidenceLedger(output, checkout, "V3-R1-S00-TEST-0001")
    ledger.append({"result": "STARTED"})
    ledger.append({"result": "PASS"})
    lines = ledger.ledger_path.read_text(encoding="utf-8").splitlines()
    assert [json.loads(line)["result"] for line in lines] == ["STARTED", "PASS"]
    with pytest.raises(FactoryFailure) as captured:
        EvidenceLedger(output, checkout, "V3-R1-S00-TEST-0001")
    assert captured.value.code == "FAIL_EXECUTION_ID_REUSE"


def test_evidence_file_cannot_be_overwritten(tmp_path: Path) -> None:
    checkout = tmp_path / "repo"
    checkout.mkdir()
    ledger = EvidenceLedger(tmp_path / "out", checkout, "V3-R1-S00-TEST-0002")
    ledger.write_json("result.json", {"result": "PASS"})
    with pytest.raises(FactoryFailure) as captured:
        ledger.write_json("result.json", {"result": "OTHER"})
    assert captured.value.code == "FAIL_EVIDENCE_OVERWRITE"


def test_evidence_rejects_prohibited_value(tmp_path: Path) -> None:
    checkout = tmp_path / "repo"
    checkout.mkdir()
    ledger = EvidenceLedger(tmp_path / "out", checkout, "V3-R1-S00-TEST-0003")
    value = "synthetic" + ".person" + "@example.test"
    with pytest.raises(FactoryFailure) as captured:
        ledger.write_json("unsafe.json", {"owner": value})
    assert captured.value.code == "FAIL_EVIDENCE_REDACTION"


def test_manifest_detects_tamper(tmp_path: Path) -> None:
    artifact = tmp_path / "artifact.bin"
    artifact.write_bytes(b"first")
    records = build_manifest(tmp_path, ["artifact.bin"])
    assert verify_manifest(tmp_path, records).passed
    artifact.write_bytes(b"second")
    with pytest.raises(FactoryFailure) as captured:
        verify_manifest(tmp_path, records)
    assert captured.value.code == "FAIL_MANIFEST_TAMPER"


def test_manifest_rejects_duplicate_paths(tmp_path: Path) -> None:
    artifact = tmp_path / "artifact.bin"
    artifact.write_bytes(b"data")
    record = build_manifest(tmp_path, ["artifact.bin"])[0]
    with pytest.raises(FactoryFailure) as captured:
        verify_manifest(tmp_path, [record, FileDigest(**record.to_dict())])
    assert captured.value.code == "FAIL_MANIFEST_DUPLICATE"


def test_invalid_execution_id_and_output_location_fail_closed(tmp_path: Path) -> None:
    checkout = tmp_path / "repo"
    checkout.mkdir()
    with pytest.raises(FactoryFailure) as captured:
        EvidenceLedger(tmp_path / "out", checkout, "bad")
    assert captured.value.code == "FAIL_EXECUTION_ID"
    with pytest.raises(FactoryFailure) as captured:
        EvidenceLedger(checkout / "output", checkout, "V3-R1-S00-TEST-0004")
    assert captured.value.code == "FAIL_OUTPUT_INSIDE_CHECKOUT"


def test_manifest_inputs_must_be_single_regular_files(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.write_bytes(b"data")
    link = tmp_path / "link"
    link.symlink_to(target)
    with pytest.raises(FactoryFailure) as captured:
        digest_file(link, relative_path="link")
    assert captured.value.code == "FAIL_MANIFEST_INPUT"

    hardlink = tmp_path / "hardlink"
    hardlink.hardlink_to(target)
    with pytest.raises(FactoryFailure) as captured:
        digest_file(target, relative_path="target")
    assert captured.value.code == "FAIL_MANIFEST_INPUT"


def test_exclusive_writer_and_ledger_append_reject_unsafe_records(
    tmp_path: Path,
) -> None:
    path = tmp_path / "record.json"
    write_exclusive(path, b"{}\n")
    with pytest.raises(FactoryFailure) as captured:
        write_exclusive(path, b"{}\n")
    assert captured.value.code == "FAIL_EVIDENCE_OVERWRITE"

    checkout = tmp_path / "repo"
    checkout.mkdir()
    ledger = EvidenceLedger(tmp_path / "out", checkout, "V3-R1-S00-TEST-0005")
    unsafe = "synthetic" + ".person" + "@example.test"
    with pytest.raises(FactoryFailure) as captured:
        ledger.append({"owner": unsafe})
    assert captured.value.code == "FAIL_EVIDENCE_REDACTION"
