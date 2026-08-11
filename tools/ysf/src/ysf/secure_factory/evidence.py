"""Append-only evidence and digest-manifest primitives."""

from __future__ import annotations

import hashlib
import json
import os
import re
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ysf.secure_factory.environment import require_output_outside_checkout
from ysf.secure_factory.models import FactoryFailure, FileDigest, GateResult
from ysf.secure_factory.policy import validate_relative_path
from ysf.secure_factory.sensitive import require_no_sensitive_values, scan_text

_EXECUTION_ID = re.compile(r"^[A-Z0-9][A-Z0-9._-]{7,127}$")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def digest_file(path: Path, *, relative_path: str) -> FileDigest:
    validate_relative_path(relative_path)
    if path.is_symlink() or not path.is_file():
        raise FactoryFailure("FAIL_MANIFEST_INPUT", "Manifest input is not a regular file.")
    stat = path.stat()
    if stat.st_nlink != 1:
        raise FactoryFailure("FAIL_MANIFEST_INPUT", "Manifest input has multiple hard links.")
    return FileDigest(relative_path, stat.st_size, sha256_file(path))


def build_manifest(root: Path, relative_paths: Iterable[str]) -> list[FileDigest]:
    paths = sorted({validate_relative_path(path) for path in relative_paths})
    return [digest_file(root / path, relative_path=path) for path in paths]


def verify_manifest(root: Path, records: Iterable[FileDigest]) -> GateResult:
    records_list = list(records)
    names = [record.relative_path for record in records_list]
    if len(names) != len(set(names)):
        raise FactoryFailure("FAIL_MANIFEST_DUPLICATE", "Manifest contains duplicate paths.")
    for record in records_list:
        observed = digest_file(root / record.relative_path, relative_path=record.relative_path)
        if observed != record:
            raise FactoryFailure(
                "FAIL_MANIFEST_TAMPER",
                "Manifest bytes do not match the referenced artifact.",
                details={"path": record.relative_path},
            )
    return GateResult(
        gate="manifest_integrity",
        result="PASS",
        message="Artifact manifest verified.",
        details={"record_count": len(records_list)},
    )


def _safe_json_bytes(value: Any) -> bytes:
    text = json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":")) + "\n"
    findings = scan_text(text, location="evidence-json")
    if findings:
        raise FactoryFailure(
            "FAIL_EVIDENCE_REDACTION",
            "Evidence record contains a prohibited value; raw value suppressed.",
            details={"finding_kinds": sorted({item.kind for item in findings})},
        )
    return text.encode("utf-8")


def write_exclusive(path: Path, data: bytes, *, mode: int = 0o640) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o750)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(path, flags, mode)
    except FileExistsError as exc:
        raise FactoryFailure(
            "FAIL_EVIDENCE_OVERWRITE",
            "Immutable evidence path already exists.",
            details={"path": path.name},
        ) from exc
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


class EvidenceLedger:
    """One immutable execution directory with an append-only JSONL ledger."""

    def __init__(self, output_root: Path, repository_root: Path, execution_id: str) -> None:
        if not _EXECUTION_ID.fullmatch(execution_id):
            raise FactoryFailure("FAIL_EXECUTION_ID", "Execution ID is not canonical.")
        safe_root = require_output_outside_checkout(repository_root, output_root)
        safe_root.mkdir(parents=True, exist_ok=True, mode=0o750)
        self.directory = safe_root / execution_id
        try:
            self.directory.mkdir(mode=0o750)
        except FileExistsError as exc:
            raise FactoryFailure(
                "FAIL_EXECUTION_ID_REUSE",
                "Execution ID already exists and cannot be overwritten.",
            ) from exc
        self.ledger_path = self.directory / "execution-ledger.jsonl"
        write_exclusive(self.ledger_path, b"")

    def append(self, record: dict[str, Any]) -> None:
        payload = dict(record)
        payload.setdefault("timestamp_utc", datetime.now(UTC).isoformat().replace("+00:00", "Z"))
        data = _safe_json_bytes(payload)
        flags = os.O_WRONLY | os.O_APPEND
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        descriptor = os.open(self.ledger_path, flags)
        with os.fdopen(descriptor, "ab") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())

    def write_json(self, name: str, value: Any) -> Path:
        relative = validate_relative_path(name)
        path = self.directory / relative
        write_exclusive(path, _safe_json_bytes(value))
        require_no_sensitive_values([path])
        return path
