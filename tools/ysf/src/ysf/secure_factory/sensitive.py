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
_OPENSSH_KEY = "-----BEGIN " + "OPENSSH PRIVATE KEY-----"
_OTP_AUTH = "otp" + "auth://"
_DATA_IMAGE = "data:image/" + r"(?:png|jpeg);base64,"
_QR_WIFI = "WI" + "FI:"
_QR_VCARD = "BEGIN:" + "VCARD"
_QR_PAYMENT = "bit" + "coin:"
_SHA256_HEX = re.compile(r"(?i)(?<![0-9a-f])(?:sha256:)?([0-9a-f]{64})(?![0-9a-f])")
_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("REAL_CREDENTIAL_PRIVATE_KEY", re.compile(re.escape(_PRIVATE_KEY))),
    ("REAL_CREDENTIAL_OPENSSH_KEY", re.compile(re.escape(_OPENSSH_KEY))),
    ("REAL_CREDENTIAL_CLOUD_KEY", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    (
        "REAL_CREDENTIAL_JWT",
        re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b"),
    ),
    (
        "SECRET_VALUE",
        re.compile(
            r"(?i)\b(?:api[_-]?key|access[_-]?token|password|client[_-]?secret)"
            r"\s*[:=]\s*[\"']?([A-Za-z0-9_./+=-]{16,})"
        ),
    ),
    ("PII_EMAIL", re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")),
    ("PII_PHONE_E164", re.compile(r"(?<![\w+])\+[1-9]\d{7,14}(?!\d)")),
    ("PII_PHONE_VN", re.compile(r"(?<!\d)0[35789]\d{8}(?!\d)")),
    (
        "PII_NAME",
        re.compile(
            r"(?i)\b(?:customer[_ -]?name|full[_ -]?name|legal[_ -]?name)"
            r"\s*[:=]\s*[\"']?[A-Z][A-Za-z.'-]+(?:\s+[A-Z][A-Za-z.'-]+)+"
        ),
    ),
    (
        "PII_ADDRESS",
        re.compile(
            r"(?i)\b(?:street[_ -]?address|home[_ -]?address|shipping[_ -]?address)"
            r"\s*[:=]\s*[\"']?[^,\n}{]{8,}"
        ),
    ),
    (
        "PII_GOVERNMENT_ID",
        re.compile(
            r"(?i)\b(?:passport|national[_ -]?id|citizen[_ -]?id|tax[_ -]?id)"
            r"\s*[:=]\s*[\"']?[A-Z0-9-]{6,20}"
        ),
    ),
    ("ICCID", re.compile(r"(?<!\d)89\d{17,20}(?!\d)")),
    ("LPA", re.compile(r"(?i)\bLPA:1\$[^\s$]{3,}\$[^\s]{4,}")),
    (
        "QR_PAYLOAD",
        re.compile(rf"(?i)(?:{_OTP_AUTH}|{_DATA_IMAGE}|{_QR_WIFI}|{_QR_VCARD}|{_QR_PAYMENT})"),
    ),
)


def _fingerprint(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def _inside_sha256_digest(text: str, start: int, end: int) -> bool:
    return any(
        digest.start(1) <= start and end <= digest.end(1)
        for digest in _SHA256_HEX.finditer(text)
    )


def scan_text(text: str, *, location: str) -> list[SensitiveFinding]:
    """Return metadata-only findings; never retain the matched value."""

    findings: list[SensitiveFinding] = []
    for kind, pattern in _PATTERNS:
        for match in pattern.finditer(text):
            if kind == "PII_PHONE_VN" and _inside_sha256_digest(
                text, match.start(), match.end()
            ):
                continue
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
    inputs = tuple(paths)
    findings: list[SensitiveFinding] = []
    for path in inputs:
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
        details={"scanned_file_count": len(inputs), "profile": "V3-R1-S00-PROHIBITED-V3"},
    )


def redact_text(text: str) -> str:
    """Replace every detected value with a stable type-only marker."""

    redacted = text
    for kind, pattern in _PATTERNS:
        redacted = pattern.sub(f"<REDACTED:{kind}>", redacted)
    return redacted
