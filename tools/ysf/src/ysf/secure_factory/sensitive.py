"""Sensitive-value detection and safe redaction for source and evidence."""

from __future__ import annotations

import hashlib
import re
import zipfile
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from ysf.secure_factory.models import FactoryFailure, GateResult


@dataclass(frozen=True)
class SensitiveFinding:
    kind: str
    line: int
    fingerprint: str
    location: str

    def safe_dict(self) -> dict[str, str | int]:
        return {
            "kind": self.kind,
            "line": self.line,
            "fingerprint": self.fingerprint,
            "location": self.location,
        }


_PRIVATE_KEY = "-----BEGIN " + "PRIVATE KEY-----"
_OTP_AUTH = "otp" + "auth://"
_DATA_IMAGE = "data:image/" + r"(?:png|jpeg);base64,"
_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("PRIVATE_KEY", re.compile(re.escape(_PRIVATE_KEY))),
    (
        "SECRET_VALUE",
        re.compile(
            r"(?i)\b(?:api[_-]?key|access[_-]?token|password|client[_-]?secret)"
            r"\s*[:=]\s*[\"']?([A-Za-z0-9_./+=-]{16,})"
        ),
    ),
    ("PII_EMAIL", re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")),
    ("ICCID", re.compile(r"(?<!\d)89\d{17,20}(?!\d)")),
    ("LPA", re.compile(r"(?i)\bLPA:1\$[^\s$]{3,}\$[^\s]{4,}")),
    ("QR_PAYLOAD", re.compile(rf"(?i)(?:{_OTP_AUTH}|{_DATA_IMAGE})")),
)


def _fingerprint(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def scan_text(text: str, *, location: str) -> list[SensitiveFinding]:
    """Return metadata-only findings; never retain the matched value."""

    findings: list[SensitiveFinding] = []
    for kind, pattern in _PATTERNS:
        for match in pattern.finditer(text):
            value = match.group(0)
            findings.append(
                SensitiveFinding(
                    kind=kind,
                    line=text.count("\n", 0, match.start()) + 1,
                    fingerprint=_fingerprint(value),
                    location=location,
                )
            )
    return findings


def scan_bytes(data: bytes, *, location: str) -> list[SensitiveFinding]:
    return scan_text(data.decode("utf-8", errors="ignore"), location=location)


def scan_path(path: Path, *, location: str | None = None) -> list[SensitiveFinding]:
    """Scan a regular file and every regular member of a ZIP/wheel."""

    if path.is_symlink() or not path.is_file():
        raise FactoryFailure("FAIL_SCAN_INPUT", "Leak-scan input is not a regular file.")
    label = location or path.name
    if not zipfile.is_zipfile(path):
        return scan_bytes(path.read_bytes(), location=label)
    findings: list[SensitiveFinding] = []
    with zipfile.ZipFile(path) as archive:
        for info in archive.infolist():
            mode = info.external_attr >> 16
            if info.is_dir():
                continue
            if mode & 0o170000 == 0o120000:
                raise FactoryFailure(
                    "FAIL_ARCHIVE_SYMLINK",
                    "Candidate archive contains a symbolic-link member.",
                )
            findings.extend(
                scan_bytes(
                    archive.read(info),
                    location=f"{label}!{info.filename}",
                )
            )
    return findings


def require_no_sensitive_values(paths: Iterable[Path]) -> GateResult:
    findings: list[SensitiveFinding] = []
    for path in paths:
        findings.extend(scan_path(path))
    if findings:
        raise FactoryFailure(
            "FAIL_SENSITIVE_VALUE",
            "Sensitive or prohibited value detected; raw value suppressed.",
            details={"findings": [item.safe_dict() for item in findings]},
        )
    return GateResult(
        gate="sensitive_data",
        result="PASS",
        message="No prohibited value detected.",
        details={"scanned_file_count": len(list(paths)) if isinstance(paths, list) else None},
    )


def redact_text(text: str) -> str:
    """Replace every detected value with a stable type-only marker."""

    redacted = text
    for kind, pattern in _PATTERNS:
        redacted = pattern.sub(f"<REDACTED:{kind}>", redacted)
    return redacted
