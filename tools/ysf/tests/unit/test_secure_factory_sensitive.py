from __future__ import annotations

import zipfile
from pathlib import Path

import pytest

from ysf.secure_factory.models import FactoryFailure
from ysf.secure_factory.sensitive import (
    redact_text,
    require_no_sensitive_values,
    scan_path,
    scan_text,
)


def fixture(name: str) -> Path:
    return Path(__file__).parents[1] / "fixtures/secure_factory/noncompliant" / name


def test_synthetic_secret_and_pii_are_metadata_only() -> None:
    findings = scan_path(fixture("synthetic-secret.txt"))
    assert {item.kind for item in findings} == {
        "SECRET_VALUE",
        "PII_EMAIL",
        "PII_NAME",
        "PII_ADDRESS",
        "PII_PHONE_E164",
        "PII_GOVERNMENT_ID",
    }
    serialized = str([item.safe_dict() for item in findings])
    source = fixture("synthetic-secret.txt").read_text(encoding="utf-8").splitlines()
    assert source[1].split("=", 1)[1] not in serialized
    assert source[2].split("=", 1)[1] not in serialized


def test_synthetic_esim_and_qr_are_rejected() -> None:
    kinds = {item.kind for item in scan_path(fixture("synthetic-esim-payload.txt"))}
    assert {"ICCID", "LPA", "QR_PAYLOAD"}.issubset(kinds)


def test_redaction_removes_every_raw_match() -> None:
    text = fixture("synthetic-secret.txt").read_text(encoding="utf-8")
    redacted = redact_text(text)
    assert not scan_text(redacted, location="redacted")
    assert "<REDACTED:SECRET_VALUE>" in redacted
    assert "<REDACTED:PII_EMAIL>" in redacted


def test_compliant_fixture_passes() -> None:
    compliant = Path(__file__).parents[1] / "fixtures/secure_factory/compliant/README.txt"
    assert require_no_sensitive_values([compliant]).passed


def test_vn_phone_detector_requires_structural_sha256_context() -> None:
    synthetic_phone = "".join(("0", "3", "1" * 8))
    findings = scan_text(synthetic_phone, location="standalone-synthetic")
    assert [finding.kind for finding in findings] == ["PII_PHONE_VN"]

    digest = ("a" * 12) + synthetic_phone + ("b" * 42)
    assert len(digest) == 64
    assert scan_text(f"--hash=sha256:{digest}", location="synthetic-lock") == []
    assert scan_text(f"{digest}  artifacts/synthetic.whl", location="checksums") == []

    wrong_contexts = (
        digest,
        f"value: {digest}",
        f"sha25x:{digest}",
        f"sha256:{digest[:-1]}",
        f"sha256:{digest}a",
        f"sha256:{digest[:-1]}z",
        f"{digest}  ../escape",
    )
    for text in wrong_contexts:
        assert "PII_PHONE_VN" in {
            finding.kind for finding in scan_text(text, location="wrong-context")
        }


def test_reserved_admin_example_email_is_safe_but_other_roles_fail_closed() -> None:
    non_reserved = "".join(("seed", "@", "synthetic.localdomain"))
    reserved_admin = "".join(("admin", "@", "example.com"))
    admin_source = (
        "# 9. Demonstration Seed\n\n"
        "```yaml\n"
        "demo_user:\n"
        f"  email: {reserved_admin}\n"
        "  role: admin\n"
        "```\n"
    )
    assert not scan_text(admin_source, location="reserved-admin")

    for role in ("customer", "fulfillment"):
        other_role = admin_source.replace("role: admin", f"role: {role}")
        assert [item.kind for item in scan_text(other_role, location=role)] == [
            "PII_EMAIL"
        ]

    non_reserved_admin = admin_source.replace(reserved_admin, non_reserved)
    assert [item.kind for item in scan_text(non_reserved_admin, location="admin")] == [
        "PII_EMAIL"
    ]


@pytest.mark.parametrize(
    "duplicate_fields",
    [
        "  role: admin\n  role: admin\n",
        "  role: customer\n  role: admin\n",
        "  email: " + "duplicate" + "@" + "example.com\n  role: admin\n",
        "  email: " + "other" + "@" + "example.net\n  role: admin\n",
    ],
)
def test_ambiguous_admin_yaml_never_receives_email_exemption(
    duplicate_fields: str,
) -> None:
    non_reserved = "".join(("seed", "@", "synthetic.localdomain"))
    source = (
        "# 9. Demonstration Seed\n\n"
        "```yaml\n"
        "demo_user:\n"
        f"  email: {non_reserved}\n"
        f"{duplicate_fields}"
        "```\n"
    )
    assert "PII_EMAIL" in {
        finding.kind for finding in scan_text(source, location="ambiguous-admin")
    }


def test_malformed_admin_yaml_fails_closed() -> None:
    non_reserved = "".join(("seed", "@", "synthetic.localdomain"))
    source = (
        "# Demonstration Seed\n\n```yaml\n"
        f"demo_user: [email: {non_reserved}\n"
        "  role: admin\n```\n"
    )
    assert "PII_EMAIL" in {
        finding.kind for finding in scan_text(source, location="malformed-admin")
    }


def test_sensitive_gate_fails_without_raw_value() -> None:
    with pytest.raises(FactoryFailure) as captured:
        require_no_sensitive_values([fixture("synthetic-secret.txt")])
    assert captured.value.code == "FAIL_SENSITIVE_VALUE"
    assert "synthetic_only" not in str(captured.value.details)


def test_archive_members_are_scanned_and_symlinks_are_rejected(tmp_path: Path) -> None:
    archive = tmp_path / "candidate.whl"
    with zipfile.ZipFile(archive, "w") as output:
        output.writestr("safe.txt", "safe synthetic data")
        output.writestr("folder/", "")
    assert scan_path(archive, location="candidate") == []

    with zipfile.ZipFile(archive, "w") as output:
        info = zipfile.ZipInfo("link")
        info.create_system = 3
        info.external_attr = 0o120777 << 16
        output.writestr(info, "target")
    with pytest.raises(FactoryFailure) as captured:
        scan_path(archive)
    assert captured.value.code == "FAIL_ARCHIVE_SYMLINK"


def test_scan_input_must_be_regular(tmp_path: Path) -> None:
    with pytest.raises(FactoryFailure) as captured:
        scan_path(tmp_path / "missing")
    assert captured.value.code == "FAIL_SCAN_INPUT"
    target = tmp_path / "target"
    target.write_text("safe", encoding="utf-8")
    link = tmp_path / "link"
    link.symlink_to(target)
    with pytest.raises(FactoryFailure) as captured:
        scan_path(link)
    assert captured.value.code == "FAIL_SCAN_INPUT"


def test_private_key_marker_and_invalid_utf8_are_detected_safely() -> None:
    marker = "-----BEGIN " + "PRIVATE KEY-----"
    findings = scan_text(marker, location="memory")
    assert [finding.kind for finding in findings] == ["REAL_CREDENTIAL_PRIVATE_KEY"]
    from ysf.secure_factory.sensitive import scan_bytes

    assert scan_bytes(b"safe\xffbytes", location="bytes") == []
