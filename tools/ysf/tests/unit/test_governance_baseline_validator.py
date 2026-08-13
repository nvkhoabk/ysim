from __future__ import annotations

import inspect
import shutil
import subprocess
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest
import yaml

from ysf.governance_baseline import validator
from ysf.governance_baseline.validator import (
    EXPECTED_ALLOWLIST,
    EXPECTED_BASE_COMMIT,
    EXPECTED_CANDIDATE_PATH,
    EXPECTED_README_PATH,
    EXPECTED_SOURCE_DOCX_PATH,
    EXPECTED_WRAPPER_PATH,
    main,
    validate_candidate_semantics,
    validate_governance_baseline,
    verify_authoritative_standards_source,
)
from ysf.secure_factory.models import FactoryFailure

Mutation = Callable[[Path], None]
RECEIPT_PATH = "docs/v3/r1/g00/s02/acceptance-receipt.yaml"
SPEC_PATH = "docs/v3/r1/g00/s02/package-spec.yaml"
PROVENANCE_PATH = "docs/v3/r1/g00/s02/standards/standards-provenance.yaml"
TRACEABILITY_PATH = "docs/v3/r1/g00/s01/traceability-baseline.yaml"


def _repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


def _run(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
    )


def _synthetic_git_email() -> str:
    return "ysim-test" + "@" + "example.invalid"


def _copy_governance_files(root: Path) -> None:
    source = _repository_root()
    for relative in sorted(EXPECTED_ALLOWLIST | {TRACEABILITY_PATH}):
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / relative, target)


def _content_workspace(tmp_path: Path) -> Path:
    root = tmp_path / "content-repository"
    _copy_governance_files(root)
    return root


def _api_workspace(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    tmp_path.mkdir(parents=True, exist_ok=True)
    root = tmp_path / "observed-repository"
    _run(tmp_path, "clone", "--quiet", "--no-hardlinks", str(_repository_root()), str(root))
    _copy_governance_files(root)
    _run(root, "remote", "set-url", "origin", "git@github-ysim:nvkhoabk/ysim.git")
    _run(root, "add", "--", *sorted(EXPECTED_ALLOWLIST))
    _run(
        root,
        "-c",
        "user.name=YSim Test",
        "-c",
        f"user.email={_synthetic_git_email()}",
        "commit",
        "--quiet",
        "-m",
        "test: materialize observed S02 correction",
    )
    monkeypatch.setattr(validator, "EXPECTED_CANONICAL_ROOT", root.resolve())
    return root


def _content_failure(tmp_path: Path, code: str, mutation: Mutation) -> None:
    root = _content_workspace(tmp_path)
    mutation(root)
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_content(root, EXPECTED_ALLOWLIST)
    assert captured.value.code == code


def _load(root: Path, relative: str) -> dict[str, Any]:
    value = yaml.safe_load((root / relative).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _write(root: Path, relative: str, value: dict[str, Any]) -> None:
    (root / relative).write_text(
        yaml.safe_dump(value, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )


def _parent(document: dict[str, Any], path: tuple[str, ...]) -> tuple[dict[str, Any], str]:
    current = document
    for part in path[:-1]:
        value = current[part]
        assert isinstance(value, dict)
        current = value
    return current, path[-1]


def _remove_yaml(relative: str, path: tuple[str, ...]) -> Mutation:
    def mutate(root: Path) -> None:
        document = _load(root, relative)
        parent, key = _parent(document, path)
        del parent[key]
        _write(root, relative, document)

    return mutate


def _set_yaml(relative: str, path: tuple[str, ...], value: Any) -> Mutation:
    def mutate(root: Path) -> None:
        document = _load(root, relative)
        parent, key = _parent(document, path)
        parent[key] = value
        _write(root, relative, document)

    return mutate


def _extra_yaml(relative: str, path: tuple[str, ...]) -> Mutation:
    def mutate(root: Path) -> None:
        document = _load(root, relative)
        current: dict[str, Any] = document
        for part in path:
            value = current[part]
            assert isinstance(value, dict)
            current = value
        current["unexpected"] = "FORBIDDEN"
        _write(root, relative, document)

    return mutate


def _append(relative: str, text: str) -> Mutation:
    def mutate(root: Path) -> None:
        target = root / relative
        target.write_text(target.read_text(encoding="utf-8") + text, encoding="utf-8")

    return mutate


def _replace(relative: str, old: str, new: str) -> Mutation:
    def mutate(root: Path) -> None:
        target = root / relative
        text = target.read_text(encoding="utf-8")
        assert old in text
        target.write_text(text.replace(old, new, 1), encoding="utf-8")

    return mutate


def _commit(root: Path, message: str = "test: mutate observed evidence") -> None:
    _run(root, "add", "-A")
    _run(
        root,
        "-c",
        "user.name=YSim Test",
        "-c",
        f"user.email={_synthetic_git_email()}",
        "commit",
        "--quiet",
        "-m",
        message,
    )


PACKAGE_REQUIRED_PATHS = tuple(
    (key,)
    for key in (
        "schema_version",
        "package_id",
        "package_version",
        "checkpoint",
        "repository",
        "worktree_entry_mode",
        "requirement_ids",
        "environment_scope",
        "execution_os",
        "development_shell",
        "canonical_repo_root",
        "approval_mode",
        "payment_owner_mode",
        "money_ledger_impact",
        "manifest",
        "allowed_paths",
        "safe_stop",
    )
) + tuple(
    (parent, key)
    for parent, keys in {
        "required_baseline": ("branch", "commit", "tree"),
        "maturity_transition": (
            "from",
            "refined_requirements_to",
            "deferred_requirements_to",
        ),
        "governing_standards": (
            "provenance_path",
            "authoritative_source_sha256",
            "bindings",
        ),
        "mutations": (
            "source",
            "runtime",
            "external_provider",
            "customer_communication",
            "scheduler",
        ),
        "safety": ("providers", "external_effect_budget", "email_mode"),
        "candidate": ("path", "size_bytes", "sha256"),
        "governed_wrapper": ("path", "document_code", "human_accepted"),
        "exit_criteria": ("validation", "next_action"),
    }.items()
    for key in keys
)

RECEIPT_REQUIRED_PATHS = tuple(
    (key,) for key in ("schema_version", "receipt_id", "checkpoint")
) + tuple(
    (parent, key)
    for parent, keys in {
        "document": (
            "id",
            "version",
            "path",
            "size_bytes",
            "sha256",
            "candidate_bytes_immutable",
            "candidate_status_preserved",
            "candidate_human_acceptance_field_preserved",
            "governed_wrapper_path",
            "governed_wrapper_human_accepted",
        ),
        "human_acceptance": (
            "decision",
            "statement",
            "source",
            "acceptance_timestamp_utc",
            "receipt_created_at_utc",
        ),
        "governance_decisions": tuple(f"V3-R1-GOV-{index:03d}" for index in range(1, 13)),
        "deferred_boundary": ("V3-R1-GOV-011", "V3-R1-GOV-012"),
        "scope": (
            "accepted_content",
            "accepted_bytes",
            "governed_wrapper_human_accepted",
            "implementation_claimed",
            "operational_claimed",
        ),
        "authorization_boundaries": (
            "merge",
            "tag",
            "release",
            "deployment",
            "production_activation",
            "provider_action",
            "payment",
            "fulfillment",
            "customer_communication",
            "scheduler",
            "business_external_effects",
        ),
    }.items()
    for key in keys
)


def test_exact_content_package_passes(tmp_path: Path) -> None:
    summary = validator._validate_content(_content_workspace(tmp_path), EXPECTED_ALLOWLIST)
    assert summary["result"] == "PASS"
    assert summary["requirements_total"] == 12
    assert summary["refine_total"] == 10
    assert summary["defer_total"] == 2
    assert summary["providers"] == "OFF"
    assert summary["external_effect_budget"] == "DENY_ALL"
    assert summary["email_mode"] == "NON_RELAYING"


@pytest.mark.parametrize("path", PACKAGE_REQUIRED_PATHS, ids=lambda value: ".".join(value))
def test_every_package_spec_field_is_required(tmp_path: Path, path: tuple[str, ...]) -> None:
    _content_failure(tmp_path, "FAIL_PACKAGE_SPEC", _remove_yaml(SPEC_PATH, path))


@pytest.mark.parametrize(
    "path",
    [
        (),
        ("required_baseline",),
        ("maturity_transition",),
        ("governing_standards",),
        ("mutations",),
        ("safety",),
        ("candidate",),
        ("governed_wrapper",),
        ("exit_criteria",),
    ],
    ids=lambda value: "top" if not value else ".".join(value),
)
def test_package_spec_rejects_extra_keys(tmp_path: Path, path: tuple[str, ...]) -> None:
    _content_failure(tmp_path, "FAIL_PACKAGE_SPEC", _extra_yaml(SPEC_PATH, path))


@pytest.mark.parametrize(
    ("path", "value"),
    [
        (("required_baseline", "commit"), "0" * 40),
        (("required_baseline", "tree"), "0" * 40),
        (("maturity_transition", "refined_requirements_to"), "IMPLEMENTED"),
        (("maturity_transition", "deferred_requirements_to"), "OPERATIONAL"),
        (("worktree_entry_mode",), "MERGE"),
        (("exit_criteria", "validation"), "DELIVERED"),
        (("exit_criteria", "next_action"), "PROMOTE_AND_DEPLOY"),
        (("safe_stop",), "MERGE"),
        (("safety", "providers"), "ON"),
        (("safety", "external_effect_budget"), "ALLOW"),
        (("safety", "email_mode"), "RELAYING"),
        (("allowed_paths",), ["fabricated.txt"]),
    ],
)
def test_package_spec_rejects_bypass_values(
    tmp_path: Path, path: tuple[str, ...], value: Any
) -> None:
    _content_failure(tmp_path, "FAIL_PACKAGE_SPEC", _set_yaml(SPEC_PATH, path, value))


@pytest.mark.parametrize("path", RECEIPT_REQUIRED_PATHS, ids=lambda value: ".".join(value))
def test_every_receipt_field_is_required(tmp_path: Path, path: tuple[str, ...]) -> None:
    _content_failure(tmp_path, "FAIL_ACCEPTANCE_RECEIPT", _remove_yaml(RECEIPT_PATH, path))


@pytest.mark.parametrize(
    "path",
    [
        (),
        ("document",),
        ("human_acceptance",),
        ("governance_decisions",),
        ("deferred_boundary",),
        ("scope",),
        ("authorization_boundaries",),
    ],
    ids=lambda value: "top" if not value else ".".join(value),
)
def test_receipt_rejects_extra_keys(tmp_path: Path, path: tuple[str, ...]) -> None:
    _content_failure(tmp_path, "FAIL_ACCEPTANCE_RECEIPT", _extra_yaml(RECEIPT_PATH, path))


@pytest.mark.parametrize(
    ("path", "value"),
    [
        (("receipt_id",), "WRONG"),
        (("checkpoint",), "WRONG"),
        (("document", "path"), EXPECTED_WRAPPER_PATH.as_posix()),
        (("document", "size_bytes"), 1),
        (("document", "sha256"), "0" * 64),
        (("human_acceptance", "decision"), "MERGE"),
        (("governance_decisions", "V3-R1-GOV-001"), "IMPLEMENTED"),
        (("governance_decisions", "V3-R1-GOV-011"), "REFINE"),
        (("deferred_boundary", "V3-R1-GOV-011"), "DELIVERED"),
        (("scope", "accepted_bytes"), "WRAPPER"),
        (("scope", "implementation_claimed"), True),
        (("scope", "operational_claimed"), True),
        (("authorization_boundaries", "merge"), True),
        (("authorization_boundaries", "release"), True),
        (("authorization_boundaries", "deployment"), True),
        (("authorization_boundaries", "business_external_effects"), True),
    ],
)
def test_receipt_rejects_identity_scope_and_authorization_bypasses(
    tmp_path: Path, path: tuple[str, ...], value: Any
) -> None:
    _content_failure(tmp_path, "FAIL_ACCEPTANCE_RECEIPT", _set_yaml(RECEIPT_PATH, path, value))


@pytest.mark.parametrize(
    ("path", "value"),
    [
        (("source", "sha256"), "0" * 64),
        (("source", "physical_input_path"), "/wrong/source.docx"),
        (("extraction", "method_id"), "UNVERIFIED"),
        (("standards",), []),
        (("scope", "candidate_bytes_modified"), True),
    ],
)
def test_standards_provenance_rejects_wrong_binding(
    tmp_path: Path, path: tuple[str, ...], value: Any
) -> None:
    _content_failure(
        tmp_path, "FAIL_GOVERNING_STANDARDS", _set_yaml(PROVENANCE_PATH, path, value)
    )


@pytest.mark.parametrize("field", ["code", "version", "extract_path", "extract_sha256"])
def test_standard_binding_rejects_wrong_identity(tmp_path: Path, field: str) -> None:
    def mutate(root: Path) -> None:
        document = _load(root, PROVENANCE_PATH)
        document["standards"][0][field] = "WRONG"
        _write(root, PROVENANCE_PATH, document)

    _content_failure(tmp_path, "FAIL_GOVERNING_STANDARDS", mutate)


def test_authoritative_docx_reproduces_all_extracts(tmp_path: Path) -> None:
    root = _content_workspace(tmp_path)
    result = verify_authoritative_standards_source(root, EXPECTED_SOURCE_DOCX_PATH)
    assert result == {
        "source_path": EXPECTED_SOURCE_DOCX_PATH.as_posix(),
        "source_sha256": validator.EXPECTED_SOURCE_DOCX_SHA256,
        "standard_count": 3,
        "result": "PASS",
    }
    altered = tmp_path / "altered.docx"
    altered.write_bytes(EXPECTED_SOURCE_DOCX_PATH.read_bytes() + b"altered")
    with pytest.raises(FactoryFailure) as captured:
        verify_authoritative_standards_source(root, altered)
    assert captured.value.code == "FAIL_AUTHORITATIVE_STANDARDS_SOURCE"


@pytest.mark.parametrize(
    ("code", "mutation"),
    [
        ("FAIL_CANDIDATE_DIGEST", _append(EXPECTED_CANDIDATE_PATH.as_posix(), "altered")),
        ("FAIL_UNRESOLVED_PLACEHOLDER", _append(EXPECTED_README_PATH.as_posix(), "\nTODO\n")),
        (
            "FAIL_FORBIDDEN_STATUS_CLAIM",
            _append(EXPECTED_README_PATH.as_posix(), "\nBusiness Factory is OPERATIONAL\n"),
        ),
        (
            "FAIL_ACCEPTANCE_OVERCLAIM",
            _append(EXPECTED_WRAPPER_PATH.as_posix(), "\nThe wrapper is Human-Accepted.\n"),
        ),
        (
            "FAIL_MARKDOWN_LINK",
            _append(EXPECTED_README_PATH.as_posix(), "\n[escape](../../../../../../../outside)\n"),
        ),
    ],
)
def test_content_surfaces_fail_closed(
    tmp_path: Path, code: str, mutation: Mutation
) -> None:
    _content_failure(tmp_path, code, mutation)


def test_manifest_and_changed_path_checks_fail_closed(tmp_path: Path) -> None:
    root = _content_workspace(tmp_path)
    manifest = root / validator.MANIFEST_PATH
    manifest.write_text(manifest.read_text(encoding="utf-8") + "malformed\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_content(root, EXPECTED_ALLOWLIST)
    assert captured.value.code == "FAIL_PACKAGE_MANIFEST"

    with pytest.raises(FactoryFailure) as captured:
        validator._validate_content(root, EXPECTED_ALLOWLIST | {"unexpected.txt"})
    assert captured.value.code == "FAIL_FILE_ALLOWLIST"


@pytest.mark.parametrize("kind", ["unsafe", "missing", "digest", "duplicate"])
def test_manifest_matrix_fails_closed(tmp_path: Path, kind: str) -> None:
    root = _content_workspace(tmp_path)
    manifest = root / validator.MANIFEST_PATH
    lines = manifest.read_text(encoding="utf-8").splitlines()
    if kind == "unsafe":
        lines[0] = lines[0].split("  ", 1)[0] + "  ../outside"
    elif kind == "missing":
        lines.pop()
    elif kind == "digest":
        lines[0] = "0" * 64 + "  " + lines[0].split("  ", 1)[1]
    else:
        lines.append(lines[0])
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_content(root, EXPECTED_ALLOWLIST)
    assert captured.value.code == "FAIL_PACKAGE_MANIFEST"


def test_candidate_missing_and_invalid_yaml_fail_closed(tmp_path: Path) -> None:
    root = _content_workspace(tmp_path / "candidate")
    (root / EXPECTED_CANDIDATE_PATH).unlink()
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_content(root, EXPECTED_ALLOWLIST)
    assert captured.value.code == "FAIL_CANDIDATE_DIGEST"

    root = _content_workspace(tmp_path / "yaml")
    (root / RECEIPT_PATH).write_text("[invalid", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_content(root, EXPECTED_ALLOWLIST)
    assert captured.value.code == "FAIL_ACCEPTANCE_RECEIPT"


def test_traceability_metadata_wrapper_and_extract_fail_closed(tmp_path: Path) -> None:
    mutations = (
        (
            "FAIL_TRACEABILITY_BINDING",
            _set_yaml(TRACEABILITY_PATH, ("requirements",), []),
        ),
        (
            "FAIL_DOCUMENT_METADATA",
            _replace(
                EXPECTED_WRAPPER_PATH.as_posix(),
                "document_code: V3-R1-G00-S02-GOVERNANCE-BASELINE-WRAPPER",
                "document_code: WRONG",
            ),
        ),
        (
            "FAIL_WRAPPER_BINDING",
            lambda root: (root / EXPECTED_WRAPPER_PATH).write_text(
                "---\ndocument_code: V3-R1-G00-S02-GOVERNANCE-BASELINE-WRAPPER\n"
                "document_set: V3-R1-G00-S02\nversion: 0.1.0-candidate.1\n"
                "status: FROZEN\nlanguage: en\n---\n",
                encoding="utf-8",
            ),
        ),
        (
            "FAIL_GOVERNING_STANDARDS",
            _append(
                "docs/v3/r1/g00/s02/standards/04_RELEASE_STANDARD_1.27.1.txt",
                "altered",
            ),
        ),
    )
    for index, (code, mutation) in enumerate(mutations):
        _content_failure(tmp_path / str(index), code, mutation)


def test_defensive_type_helpers_fail_closed(tmp_path: Path) -> None:
    with pytest.raises(FactoryFailure) as captured:
        validator._mapping([], "FAIL_TYPE", "mapping")
    assert captured.value.code == "FAIL_TYPE"
    with pytest.raises(FactoryFailure) as captured:
        validator._sequence("text", "FAIL_TYPE", "sequence")
    assert captured.value.code == "FAIL_TYPE"
    missing = tmp_path / "missing.yaml"
    with pytest.raises(FactoryFailure) as captured:
        validator._load_yaml(missing, "FAIL_YAML")
    assert captured.value.code == "FAIL_YAML"


def test_candidate_semantics_reject_duplicates_decisions_and_status() -> None:
    candidate = (_repository_root() / EXPECTED_CANDIDATE_PATH).read_text(encoding="utf-8")
    changes = (
        (
            candidate
            + "\n### V3-R1-GOV-001 — Duplicate\n\n**Decision:** `REFINE`\n",
            "FAIL_GOVERNANCE_REQUIREMENT_IDS",
        ),
        (
            candidate.replace("**Decision:** `REFINE`", "**Decision:** `DEFER`", 1),
            "FAIL_GOVERNANCE_DECISION",
        ),
        (candidate.replace("REFERENCE_ONLY/FUTURE", "FUTURE"), "FAIL_DEFERRED_BOUNDARY"),
        (candidate + "\nAI Store Generator is IMPLEMENTED\n", "FAIL_FORBIDDEN_STATUS_CLAIM"),
        (
            candidate.replace(
                "## 6. Cross-requirement validation gates", "## 6. Removed"
            ),
            "FAIL_MARKDOWN_STRUCTURE",
        ),
    )
    for text, code in changes:
        with pytest.raises(FactoryFailure) as captured:
            validate_candidate_semantics(text)
        assert captured.value.code == code


def test_public_api_derives_observed_evidence_and_matches_cli(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    root = _api_workspace(tmp_path, monkeypatch)
    assert tuple(inspect.signature(validate_governance_baseline).parameters) == (
        "repository_root",
    )
    summary = validate_governance_baseline(root)
    assert summary["result"] == "PASS"
    assert summary["sensitive_data"] == "PASS"
    assert summary["changed_paths"] == sorted(EXPECTED_ALLOWLIST)
    assert main(["--repository-root", str(root), "--json"]) == 0
    cli = capsys.readouterr().out
    assert '"result": "PASS"' in cli
    assert '"sensitive_data": "PASS"' in cli


def test_public_api_rejects_dirty_and_fabricated_changed_paths(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = _api_workspace(tmp_path, monkeypatch)
    (root / "dirty.txt").write_text("dirty", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        validate_governance_baseline(root)
    assert captured.value.code == "FAIL_DIRTY_WORKTREE"
    (root / "dirty.txt").unlink()

    (root / "unexpected.txt").write_text("safe unexpected path", encoding="utf-8")
    _commit(root)
    with pytest.raises(FactoryFailure) as captured:
        validate_governance_baseline(root)
    assert captured.value.code == "FAIL_FILE_ALLOWLIST"


def test_public_api_rejects_sensitive_data_and_symlink(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    sensitive_root = _api_workspace(tmp_path / "sensitive", monkeypatch)
    readme = sensitive_root / EXPECTED_README_PATH
    prohibited_value = "pass" + "word=" + "abcdefghijklmnop"
    readme.write_text(
        readme.read_text(encoding="utf-8") + f"\n{prohibited_value}\n",
        encoding="utf-8",
    )
    _commit(sensitive_root)
    with pytest.raises(FactoryFailure) as captured:
        validate_governance_baseline(sensitive_root)
    assert captured.value.code == "FAIL_SENSITIVE_VALUE"

    symlink_root = _api_workspace(tmp_path / "symlink", monkeypatch)
    candidate = symlink_root / EXPECTED_CANDIDATE_PATH
    candidate.unlink()
    candidate.symlink_to(symlink_root / EXPECTED_WRAPPER_PATH)
    _commit(symlink_root)
    with pytest.raises(FactoryFailure) as captured:
        validate_governance_baseline(symlink_root)
    assert captured.value.code == "FAIL_PATH_SAFETY"


def test_public_api_rejects_wrong_base_sha_and_tree(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = _api_workspace(tmp_path, monkeypatch)
    monkeypatch.setattr(
        validator,
        "EXPECTED_BASE_COMMIT",
        _run(root, "rev-parse", "HEAD").stdout.strip(),
    )
    with pytest.raises(FactoryFailure) as captured:
        validate_governance_baseline(root)
    assert captured.value.code == "FAIL_BASE_TREE"

    monkeypatch.setattr(validator, "EXPECTED_BASE_COMMIT", EXPECTED_BASE_COMMIT)
    monkeypatch.setattr(validator, "EXPECTED_BASE_TREE", "0" * 40)
    with pytest.raises(FactoryFailure) as captured:
        validate_governance_baseline(root)
    assert captured.value.code == "FAIL_BASE_TREE"


def test_public_api_rejects_wrong_repository_identity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = _api_workspace(tmp_path, monkeypatch)
    _run(root, "remote", "set-url", "origin", "https://github.com/other/repository.git")
    with pytest.raises(FactoryFailure) as captured:
        validate_governance_baseline(root)
    assert captured.value.code == "FAIL_ENVIRONMENT_IDENTITY"


def test_cli_verifies_authoritative_source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = _api_workspace(tmp_path, monkeypatch)
    assert main(
        [
            "--repository-root",
            str(root),
            "--authoritative-standards-source",
            str(EXPECTED_SOURCE_DOCX_PATH),
            "--json",
        ]
    ) == 0
    assert '"authoritative_standards_source"' in capsys.readouterr().out

    assert main(["--repository-root", str(root)]) == 0
    assert capsys.readouterr().out == "V3-R1-G00-S02 validation PASS\n"

    monkeypatch.setenv("WSL_DISTRO_NAME", "WRONG")
    assert main(["--repository-root", str(root), "--json"]) == 1
    assert '"code": "FAIL_ENVIRONMENT_IDENTITY"' in capsys.readouterr().out


def test_integration_isolation_fixture_has_canonical_invariants() -> None:
    fixture = _repository_root() / "tools/ysf/tests/integration/conftest.py"
    text = fixture.read_text(encoding="utf-8")
    assert "_canonical_snapshot(canonical) == before" in text
    assert "git\", \"clone" in text
    assert "os.chdir(repository / \"tools/ysf\")" in text
