from __future__ import annotations

import shutil
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest
import yaml

from ysf.governance_baseline.validator import (
    EXPECTED_ALLOWLIST,
    EXPECTED_BASE_COMMIT,
    EXPECTED_CANDIDATE_PATH,
    EXPECTED_README_PATH,
    EXPECTED_WRAPPER_PATH,
    main,
    validate_candidate_semantics,
    validate_governance_baseline,
)
from ysf.secure_factory.models import FactoryFailure

Mutation = Callable[[Path], None]


def _repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


def _workspace(tmp_path: Path) -> Path:
    source = _repository_root()
    root = tmp_path / "repository"
    for relative in sorted(EXPECTED_ALLOWLIST):
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / relative, target)
    traceability = Path("docs/v3/r1/g00/s01/traceability-baseline.yaml")
    target = root / traceability
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source / traceability, target)
    return root


def _assert_failure(tmp_path: Path, code: str, mutation: Mutation) -> None:
    root = _workspace(tmp_path)
    mutation(root)
    with pytest.raises(FactoryFailure) as captured:
        validate_governance_baseline(root)
    assert captured.value.code == code


def _append(relative: str, value: str) -> Mutation:
    def mutate(root: Path) -> None:
        path = root / relative
        path.write_text(path.read_text(encoding="utf-8") + value, encoding="utf-8")

    return mutate


def _replace(relative: str, old: str, new: str) -> Mutation:
    def mutate(root: Path) -> None:
        path = root / relative
        text = path.read_text(encoding="utf-8")
        assert old in text
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    return mutate


def _mutate_yaml(relative: str, path: tuple[str, ...], value: Any) -> Mutation:
    def mutate(root: Path) -> None:
        target = root / relative
        document = yaml.safe_load(target.read_text(encoding="utf-8"))
        current = document
        for part in path[:-1]:
            current = current[part]
        current[path[-1]] = value
        target.write_text(
            yaml.safe_dump(document, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )

    return mutate


def _remove_candidate(root: Path) -> None:
    (root / EXPECTED_CANDIDATE_PATH).unlink()


def _invalid_receipt_yaml(root: Path) -> None:
    (root / "docs/v3/r1/g00/s02/acceptance-receipt.yaml").write_text(
        "[invalid", encoding="utf-8"
    )


def _manifest_unsafe_path(root: Path) -> None:
    path = root / "docs/v3/r1/g00/s02/MANIFEST.sha256"
    lines = path.read_text(encoding="utf-8").splitlines()
    lines[0] = lines[0].split("  ", 1)[0] + "  ../outside.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _manifest_missing_path(root: Path) -> None:
    path = root / "docs/v3/r1/g00/s02/MANIFEST.sha256"
    lines = path.read_text(encoding="utf-8").splitlines()
    path.write_text("\n".join(lines[:-1]) + "\n", encoding="utf-8")


def _manifest_wrong_digest(root: Path) -> None:
    path = root / "docs/v3/r1/g00/s02/MANIFEST.sha256"
    lines = path.read_text(encoding="utf-8").splitlines()
    lines[0] = "0" * 64 + "  " + lines[0].split("  ", 1)[1]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_repository_governance_baseline_passes() -> None:
    summary = validate_governance_baseline(_repository_root())
    assert summary["checkpoint"] == "V3-R1-G00-S02"
    assert summary["base_commit"] == EXPECTED_BASE_COMMIT
    assert summary["candidate_size"] == 28555
    assert summary["requirements_total"] == 12
    assert summary["refine_total"] == 10
    assert summary["defer_total"] == 2
    assert summary["human_acceptance"] == "RECORDED_OUT_OF_BAND"
    assert summary["providers"] == "OFF"
    assert summary["external_effect_budget"] == "DENY_ALL"


@pytest.mark.parametrize(
    ("code", "mutation"),
    [
        (
            "FAIL_CANDIDATE_DIGEST",
            _append(EXPECTED_CANDIDATE_PATH.as_posix(), "\naltered candidate\n"),
        ),
        (
            "FAIL_UNRESOLVED_PLACEHOLDER",
            _append("docs/v3/r1/g00/s02/README.md", "\nTODO resolve this\n"),
        ),
        (
            "FAIL_FORBIDDEN_STATUS_CLAIM",
            _append(
                "docs/v3/r1/g00/s02/README.md",
                "\nBusiness Factory status: IMPLEMENTED\n",
            ),
        ),
        (
            "FAIL_ACCEPTANCE_RECEIPT",
            _mutate_yaml(
                "docs/v3/r1/g00/s02/acceptance-receipt.yaml",
                ("governance_decisions", "V3-R1-GOV-011"),
                "REFINE",
            ),
        ),
        (
            "FAIL_PACKAGE_SPEC",
            _mutate_yaml(
                "docs/v3/r1/g00/s02/package-spec.yaml",
                ("required_baseline", "tree"),
                "0" * 40,
            ),
        ),
        (
            "FAIL_MARKDOWN_LINK",
            _append("docs/v3/r1/g00/s02/README.md", "\n[Missing](missing.md)\n"),
        ),
        (
            "FAIL_PACKAGE_MANIFEST",
            _append(
                "docs/v3/r1/g00/s02/MANIFEST.sha256",
                "invalid manifest line\n",
            ),
        ),
        (
            "FAIL_TRACEABILITY_BINDING",
            _mutate_yaml(
                "docs/v3/r1/g00/s01/traceability-baseline.yaml",
                ("requirements", "0", "state"),
                "INVALID",
            ),
        ),
        ("FAIL_CANDIDATE_DIGEST", _remove_candidate),
        ("FAIL_ACCEPTANCE_RECEIPT", _invalid_receipt_yaml),
        ("FAIL_PACKAGE_MANIFEST", _manifest_unsafe_path),
        ("FAIL_PACKAGE_MANIFEST", _manifest_missing_path),
        ("FAIL_PACKAGE_MANIFEST", _manifest_wrong_digest),
    ],
)
def test_package_mutations_fail_closed(
    tmp_path: Path, code: str, mutation: Mutation
) -> None:
    if code == "FAIL_TRACEABILITY_BINDING":
        def exact_requirement_mutation(root: Path) -> None:
            target = root / "docs/v3/r1/g00/s01/traceability-baseline.yaml"
            document = yaml.safe_load(target.read_text(encoding="utf-8"))
            requirement = next(
                item
                for item in document["requirements"]
                if item["id"] == "V3-R1-GOV-001"
            )
            requirement["state"] = "INVALID"
            target.write_text(
                yaml.safe_dump(document, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )

        mutation = exact_requirement_mutation
    _assert_failure(tmp_path, code, mutation)


def test_wrong_base_sha_fails_closed(tmp_path: Path) -> None:
    root = _workspace(tmp_path)
    with pytest.raises(FactoryFailure) as captured:
        validate_governance_baseline(root, current_base_sha="0" * 40)
    assert captured.value.code == "FAIL_BASE_IDENTITY"


def test_unexpected_path_fails_closed(tmp_path: Path) -> None:
    root = _workspace(tmp_path)
    with pytest.raises(FactoryFailure) as captured:
        validate_governance_baseline(
            root,
            changed_paths=set(EXPECTED_ALLOWLIST) | {"unexpected.txt"},
        )
    assert captured.value.code == "FAIL_FILE_ALLOWLIST"


def test_duplicate_requirement_id_fails_closed() -> None:
    candidate = (_repository_root() / EXPECTED_CANDIDATE_PATH).read_text(encoding="utf-8")
    duplicate = "\n### V3-R1-GOV-001 — Duplicate\n\n**Decision:** `REFINE`\n"
    with pytest.raises(FactoryFailure) as captured:
        validate_candidate_semantics(candidate + duplicate)
    assert captured.value.code == "FAIL_GOVERNANCE_REQUIREMENT_IDS"


def test_wrong_decision_and_deferred_boundary_fail_closed() -> None:
    candidate = (_repository_root() / EXPECTED_CANDIDATE_PATH).read_text(encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        validate_candidate_semantics(
            candidate.replace("**Decision:** `REFINE`", "**Decision:** `DEFER`", 1)
        )
    assert captured.value.code == "FAIL_GOVERNANCE_DECISION"

    with pytest.raises(FactoryFailure) as captured:
        validate_candidate_semantics(candidate.replace("REFERENCE_ONLY/FUTURE", "FUTURE"))
    assert captured.value.code == "FAIL_DEFERRED_BOUNDARY"


def test_forbidden_candidate_status_claim_fails_closed() -> None:
    candidate = (_repository_root() / EXPECTED_CANDIDATE_PATH).read_text(encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        validate_candidate_semantics(candidate + "\nBusiness Factory is OPERATIONAL\n")
    assert captured.value.code == "FAIL_FORBIDDEN_STATUS_CLAIM"


def test_candidate_markdown_structure_and_repository_integration_fail_closed(
    tmp_path: Path,
) -> None:
    candidate = (_repository_root() / EXPECTED_CANDIDATE_PATH).read_text(encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        validate_candidate_semantics(
            candidate.replace("## 6. Cross-requirement validation gates", "## 6. Removed")
        )
    assert captured.value.code == "FAIL_MARKDOWN_STRUCTURE"

    _assert_failure(
        tmp_path,
        "FAIL_ACCEPTANCE_RECEIPT",
        _mutate_yaml(
            "docs/v3/r1/g00/s02/acceptance-receipt.yaml",
            ("document", "sha256"),
            "0" * 64,
        ),
    )
    _assert_failure(
        tmp_path,
        "FAIL_PACKAGE_SPEC",
        _mutate_yaml(
            "docs/v3/r1/g00/s02/package-spec.yaml",
            ("candidate", "path"),
            EXPECTED_WRAPPER_PATH.as_posix(),
        ),
    )
    _assert_failure(
        tmp_path,
        "FAIL_DOCUMENT_METADATA",
        _replace(
            EXPECTED_WRAPPER_PATH.as_posix(),
            "document_code: V3-R1-G00-S02-GOVERNANCE-BASELINE-WRAPPER\n",
            "",
        ),
    )
    _assert_failure(
        tmp_path,
        "FAIL_DOCUMENT_METADATA",
        _replace(
            EXPECTED_WRAPPER_PATH.as_posix(),
            "V3-R1-G00-S02-GOVERNANCE-BASELINE-WRAPPER",
            "V3-R1-G00-S02-README",
        ),
    )
    _assert_failure(
        tmp_path,
        "FAIL_ACCEPTANCE_OVERCLAIM",
        _append(EXPECTED_WRAPPER_PATH.as_posix(), "\nThe wrapper is Human-Accepted.\n"),
    )
    _assert_failure(
        tmp_path,
        "FAIL_ACCEPTANCE_RECEIPT",
        _mutate_yaml(
            "docs/v3/r1/g00/s02/acceptance-receipt.yaml",
            ("scope", "governed_wrapper_human_accepted"),
            True,
        ),
    )

    assert EXPECTED_README_PATH.as_posix() in EXPECTED_ALLOWLIST


def test_cli_validates_exact_worktree(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--repository-root", str(_repository_root()), "--json"]) == 0
    result = capsys.readouterr().out
    assert '"result": "PASS"' in result
    assert '"sensitive_data": "PASS"' in result

    assert main(["--repository-root", str(_repository_root())]) == 0
    assert capsys.readouterr().out == "V3-R1-G00-S02 validation PASS\n"


def test_cli_fails_closed_on_wrong_environment(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setenv("WSL_DISTRO_NAME", "WRONG")
    assert main(["--repository-root", str(_repository_root()), "--json"]) == 1
    result = capsys.readouterr().out
    assert '"code": "FAIL_ENVIRONMENT_IDENTITY"' in result
    assert '"result": "FAIL"' in result
