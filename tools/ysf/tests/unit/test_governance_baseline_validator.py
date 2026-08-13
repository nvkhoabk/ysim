from __future__ import annotations

import copy
import hashlib
import inspect
import json
import os
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
    EXPECTED_INPUT_MANIFEST_PATH,
    EXPECTED_README_PATH,
    EXPECTED_SOURCE_DOCX_PATH,
    EXPECTED_WRAPPER_PATH,
    load_snapshot_contract,
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
FIRST_S02_COMMIT = "9bec3979ce3c74da66848ce53efd03f11739d5e2"
R1_CORRECTIVE_COMMIT = "f2b3904b364ae38df1a7a6dbe999741636e69a0a"
R2_CORRECTIVE_COMMIT = "d10b2e9881d0d085cb5c0b172c9af83cbc45193a"
R3_WRITE_SUBSET = {
    "docs/v3/r1/g00/s02/MANIFEST.sha256",
    "docs/v3/r1/g00/s02/README.md",
    "docs/v3/r1/g00/s02/package-spec.yaml",
    "tools/ysf/src/ysf/governance_baseline/validator.py",
    "tools/ysf/tests/unit/test_governance_baseline_validator.py",
}


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


def _commit_at(root: Path, message: str, timestamp: int) -> None:
    environment = {
        **os.environ,
        "GIT_AUTHOR_DATE": f"2000-01-01T00:00:{timestamp:02d}Z",
        "GIT_COMMITTER_DATE": f"2000-01-01T00:00:{timestamp:02d}Z",
    }
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=YSim Test",
            "-c",
            f"user.email={_synthetic_git_email()}",
            "commit",
            "--quiet",
            "-m",
            message,
        ],
        check=True,
        capture_output=True,
        env=environment,
    )


def _apply_commit_delta(root: Path, old: str, new: str, timestamp: int) -> None:
    patch = subprocess.run(
        ["git", "-C", str(_repository_root()), "diff", "--binary", old, new],
        check=True,
        capture_output=True,
    ).stdout
    subprocess.run(
        ["git", "-C", str(root), "apply", "--index", "--binary", "-"],
        input=patch,
        check=True,
        capture_output=True,
    )
    _commit_at(root, f"test: materialize {new[:7]}", timestamp)


def _snapshot_contract(root: Path) -> dict[str, Any]:
    def identity(revision: str) -> str:
        return _run(root, "rev-parse", revision).stdout.strip()

    modes: dict[str, str] = {}
    for relative in sorted(EXPECTED_ALLOWLIST):
        record = _run(root, "ls-tree", "HEAD", "--", relative).stdout
        modes[relative] = record.split(" ", 1)[0]
    return {
        "schema_version": 1,
        "repository": {
            "identity": "nvkhoabk/ysim",
            "origin": "git@github-ysim:nvkhoabk/ysim.git",
            "branch": validator.EXPECTED_BRANCH,
        },
        "topology": {
            "base_sha": EXPECTED_BASE_COMMIT,
            "base_tree": validator.EXPECTED_BASE_TREE,
            "corrective_parent_sha": identity("HEAD^"),
            "corrective_parent_tree": identity("HEAD^^{tree}"),
            "expected_head_sha": identity("HEAD"),
            "expected_head_tree": identity("HEAD^{tree}"),
            "base_to_head_commit_count": 4,
            "parent_to_head_commit_count": 1,
        },
        "changed_paths": sorted(EXPECTED_ALLOWLIST),
        "file_modes": modes,
        "authoritative_inputs": {
            "docx": {
                "path": EXPECTED_SOURCE_DOCX_PATH.as_posix(),
                "size_bytes": validator.EXPECTED_SOURCE_DOCX_SIZE,
                "sha256": validator.EXPECTED_SOURCE_DOCX_SHA256,
            },
            "manifest": {
                "path": EXPECTED_INPUT_MANIFEST_PATH.as_posix(),
                "size_bytes": validator.EXPECTED_INPUT_MANIFEST_SIZE,
                "sha256": validator.EXPECTED_INPUT_MANIFEST_SHA256,
            },
        },
        "standards": {
            "provenance_path": validator.EXPECTED_PROVENANCE_PATH.as_posix(),
            "provenance_sha256": hashlib.sha256(
                (root / validator.EXPECTED_PROVENANCE_PATH).read_bytes()
            ).hexdigest(),
            "bindings": [
                {
                    **dict(validator.EXPECTED_STANDARD_BINDINGS[0]),
                    "source_body_ranges": [[352, 521]],
                    "redacted_source_blocks": [],
                },
                {
                    **dict(validator.EXPECTED_STANDARD_BINDINGS[1]),
                    "source_body_ranges": [[522, 581]],
                    "redacted_source_blocks": [],
                },
                {
                    **dict(validator.EXPECTED_STANDARD_BINDINGS[2]),
                    "source_body_ranges": [[582, 760]],
                    "redacted_source_blocks": [700],
                },
            ],
        },
    }


def _local_branch_exists(root: Path, branch: str) -> bool:
    return (
        subprocess.run(
            ["git", "-C", str(root), "show-ref", "--verify", f"refs/heads/{branch}"],
            check=False,
            capture_output=True,
        ).returncode
        == 0
    )


def _api_workspace(
    tmp_path: Path, *, prepare_existing_s02_branch: bool = False
) -> tuple[Path, dict[str, Any]]:
    tmp_path.mkdir(parents=True, exist_ok=True)
    root = tmp_path / "observed-repository"
    _run(
        tmp_path,
        "clone",
        "--quiet",
        "--no-hardlinks",
        "--no-checkout",
        str(_repository_root()),
        str(root),
    )
    _run(root, "switch", "--quiet", "--detach", EXPECTED_BASE_COMMIT)
    if prepare_existing_s02_branch and not _local_branch_exists(root, validator.EXPECTED_BRANCH):
        _run(root, "branch", validator.EXPECTED_BRANCH, EXPECTED_BASE_COMMIT)
    if _local_branch_exists(root, validator.EXPECTED_BRANCH):
        _run(root, "branch", "-D", validator.EXPECTED_BRANCH)
    _run(root, "switch", "--quiet", "-c", validator.EXPECTED_BRANCH)
    _apply_commit_delta(root, EXPECTED_BASE_COMMIT, FIRST_S02_COMMIT, 1)
    assert _run(root, "rev-parse", "HEAD^{tree}").stdout.strip() == (
        "2afccaaceb57f3255cb3bad91fd0bdf4d16eb5a7"
    )
    _apply_commit_delta(root, FIRST_S02_COMMIT, R1_CORRECTIVE_COMMIT, 2)
    assert _run(root, "rev-parse", "HEAD^{tree}").stdout.strip() == (
        "e5e2c8d0b9f4a3e7565473ae8007871f3b6863f8"
    )
    _apply_commit_delta(root, R1_CORRECTIVE_COMMIT, R2_CORRECTIVE_COMMIT, 3)
    assert _run(root, "rev-parse", "HEAD^{tree}").stdout.strip() == (
        "ee65f7334e931013e510c6950014021fffcd560a"
    )
    _copy_governance_files(root)
    _run(root, "remote", "set-url", "origin", "git@github-ysim:nvkhoabk/ysim.git")
    _run(root, "add", "--", *sorted(EXPECTED_ALLOWLIST))
    staged = {
        path for path in _run(root, "diff", "--cached", "--name-only").stdout.splitlines() if path
    }
    assert staged == R3_WRITE_SUBSET
    _commit_at(root, "test: materialize S02 corrective R3", 4)
    assert int(_run(root, "rev-list", "--count", f"{EXPECTED_BASE_COMMIT}..HEAD").stdout) == 4
    assert int(_run(root, "rev-list", "--count", "HEAD^..HEAD").stdout) == 1
    assert not _run(root, "status", "--porcelain=v1", "--untracked-files=all").stdout
    assert {
        path
        for path in _run(
            root, "diff", "--name-only", f"{EXPECTED_BASE_COMMIT}...HEAD"
        ).stdout.splitlines()
        if path
    } == set(EXPECTED_ALLOWLIST)
    return root, _snapshot_contract(root)


def test_api_workspace_supports_absent_and_existing_local_s02_branch(tmp_path: Path) -> None:
    absent_root, absent_contract = _api_workspace(tmp_path / "absent")
    present_root, present_contract = _api_workspace(
        tmp_path / "present", prepare_existing_s02_branch=True
    )
    for root, contract in (
        (absent_root, absent_contract),
        (present_root, present_contract),
    ):
        assert _run(root, "branch", "--show-current").stdout.strip() == validator.EXPECTED_BRANCH
        assert int(_run(root, "rev-list", "--count", f"{EXPECTED_BASE_COMMIT}..HEAD").stdout) == 4
        assert set(contract["changed_paths"]) == EXPECTED_ALLOWLIST


def _refresh_contract_identity(root: Path, contract: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(contract)
    result["topology"]["corrective_parent_sha"] = _run(root, "rev-parse", "HEAD^").stdout.strip()
    result["topology"]["corrective_parent_tree"] = _run(
        root, "rev-parse", "HEAD^^{tree}"
    ).stdout.strip()
    result["topology"]["expected_head_sha"] = _run(root, "rev-parse", "HEAD").stdout.strip()
    result["topology"]["expected_head_tree"] = _run(root, "rev-parse", "HEAD^{tree}").stdout.strip()
    return result


def _amend(root: Path) -> None:
    _run(root, "add", "-A")
    environment = {
        **os.environ,
        "GIT_COMMITTER_DATE": "2000-01-01T00:00:04Z",
    }
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=YSim Test",
            "-c",
            f"user.email={_synthetic_git_email()}",
            "commit",
            "--quiet",
            "--amend",
            "--no-edit",
        ],
        check=True,
        capture_output=True,
        env=environment,
    )


def _write_contract(path: Path, contract: dict[str, Any]) -> None:
    path.write_text(yaml.safe_dump(contract, sort_keys=False), encoding="utf-8")


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
        "repository_root_contract",
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
        "repository_root_contract": (
            "absolute_path_required",
            "symlink_components_allowed",
            "git_top_level_must_equal_repository_root",
            "identity_boundary",
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
        (
            ("repository_root_contract", "identity_boundary"),
            "CALLER_SUPPLIED_OBSERVATIONS",
        ),
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
    _content_failure(tmp_path, "FAIL_GOVERNING_STANDARDS", _set_yaml(PROVENANCE_PATH, path, value))


@pytest.mark.parametrize("field", ["code", "version", "extract_path", "extract_sha256"])
def test_standard_binding_rejects_wrong_identity(tmp_path: Path, field: str) -> None:
    def mutate(root: Path) -> None:
        document = _load(root, PROVENANCE_PATH)
        document["standards"][0][field] = "WRONG"
        _write(root, PROVENANCE_PATH, document)

    _content_failure(tmp_path, "FAIL_GOVERNING_STANDARDS", mutate)


def test_authoritative_inputs_reproduce_all_extracts(
    tmp_path: Path,
) -> None:
    root, contract = _api_workspace(tmp_path)
    result = verify_authoritative_standards_source(root, contract)
    assert result["source_sha256"] == validator.EXPECTED_SOURCE_DOCX_SHA256
    assert result["input_manifest_sha256"] == (validator.EXPECTED_INPUT_MANIFEST_SHA256)
    assert result["standard_count"] == 3
    assert result["env_block_700_rule_preserved"] is True
    assert result["personal_mailbox_values_redacted"] is True
    assert result["result"] == "PASS"


@pytest.mark.parametrize(
    ("target", "kind", "code"),
    [
        ("docx", "missing", "FAIL_AUTHORITATIVE_STANDARDS_SOURCE"),
        ("docx", "digest", "FAIL_AUTHORITATIVE_STANDARDS_SOURCE"),
        ("docx", "file_symlink", "FAIL_AUTHORITATIVE_STANDARDS_SOURCE"),
        ("docx", "parent_symlink", "FAIL_AUTHORITATIVE_STANDARDS_SOURCE"),
        ("manifest", "missing", "FAIL_AUTHORITATIVE_INPUT_MANIFEST"),
        ("manifest", "digest", "FAIL_AUTHORITATIVE_INPUT_MANIFEST"),
        ("manifest", "membership", "FAIL_AUTHORITATIVE_INPUT_MANIFEST"),
    ],
)
def test_authoritative_input_negative_matrix(
    tmp_path: Path,
    target: str,
    kind: str,
    code: str,
) -> None:
    root, contract = _api_workspace(tmp_path / "repository")
    evidence = tmp_path / "evidence"
    evidence.mkdir()
    docx = evidence / EXPECTED_SOURCE_DOCX_PATH.name
    manifest = evidence / EXPECTED_INPUT_MANIFEST_PATH.name
    shutil.copy2(EXPECTED_SOURCE_DOCX_PATH, docx)
    shutil.copy2(EXPECTED_INPUT_MANIFEST_PATH, manifest)
    contract["authoritative_inputs"]["docx"]["path"] = docx.as_posix()
    contract["authoritative_inputs"]["manifest"]["path"] = manifest.as_posix()
    if kind == "missing":
        (docx if target == "docx" else manifest).unlink()
    elif kind == "digest":
        contract["authoritative_inputs"][target]["sha256"] = "0" * 64
    elif kind == "file_symlink":
        docx.unlink()
        docx.symlink_to(EXPECTED_SOURCE_DOCX_PATH)
    elif kind == "parent_symlink":
        linked = tmp_path / "linked-evidence"
        linked.symlink_to(evidence, target_is_directory=True)
        contract["authoritative_inputs"]["docx"]["path"] = (linked / docx.name).as_posix()
    else:
        manifest.write_text("0" * 64 + f"  {docx.name}\n", encoding="utf-8")
        contract["authoritative_inputs"]["manifest"]["size_bytes"] = manifest.stat().st_size
        contract["authoritative_inputs"]["manifest"]["sha256"] = hashlib.sha256(
            manifest.read_bytes()
        ).hexdigest()
    with pytest.raises(FactoryFailure) as captured:
        verify_authoritative_standards_source(root, contract)
    assert captured.value.code == code


@pytest.mark.parametrize("kind", ["altered", "omitted_rule", "wrong_marker", "mailbox"])
def test_env_redacted_extract_negative_matrix(tmp_path: Path, kind: str) -> None:
    root, contract = _api_workspace(tmp_path)
    extract = root / validator.EXPECTED_STANDARD_BINDINGS[2]["extract_path"]
    text = extract.read_text(encoding="utf-8")
    if kind == "altered":
        text += "altered\n"
    elif kind == "omitted_rule":
        text = (
            "\n".join(
                line for line in text.splitlines() if "Sandbox recipients are limited" not in line
            )
            + "\n"
        )
    elif kind == "wrong_marker":
        text = text.replace("<REDACTED:PERSONAL_MAILBOX:01>", "<REDACTED:MAILBOX>")
    else:
        synthetic = "reviewer" + "@" + "example.invalid"
        text = text.replace("<REDACTED:PERSONAL_MAILBOX:01>", synthetic)
    extract.write_text(text, encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        verify_authoritative_standards_source(root, contract)
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
def test_content_surfaces_fail_closed(tmp_path: Path, code: str, mutation: Mutation) -> None:
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
            candidate + "\n### V3-R1-GOV-001 — Duplicate\n\n**Decision:** `REFINE`\n",
            "FAIL_GOVERNANCE_REQUIREMENT_IDS",
        ),
        (
            candidate.replace("**Decision:** `REFINE`", "**Decision:** `DEFER`", 1),
            "FAIL_GOVERNANCE_DECISION",
        ),
        (candidate.replace("REFERENCE_ONLY/FUTURE", "FUTURE"), "FAIL_DEFERRED_BOUNDARY"),
        (candidate + "\nAI Store Generator is IMPLEMENTED\n", "FAIL_FORBIDDEN_STATUS_CLAIM"),
        (
            candidate.replace("## 6. Cross-requirement validation gates", "## 6. Removed"),
            "FAIL_MARKDOWN_STRUCTURE",
        ),
    )
    for text, code in changes:
        with pytest.raises(FactoryFailure) as captured:
            validate_candidate_semantics(text)
        assert captured.value.code == code


def _assert_api_failure(root: Path, contract: dict[str, Any], expected_code: str) -> None:
    reached_assertion = False
    try:
        validate_governance_baseline(root, contract)
    except FactoryFailure as failure:
        reached_assertion = True
        assert failure.code == expected_code
    assert reached_assertion, "security probe did not reach its intended assertion"


def test_public_api_exact_snapshot_and_cli_parity(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    root, contract = _api_workspace(tmp_path)
    assert tuple(inspect.signature(validate_governance_baseline).parameters) == (
        "repository_root",
        "snapshot_contract",
    )
    summary = validate_governance_baseline(root, contract)
    assert summary["result"] == "PASS"
    assert summary["sensitive_data"] == "PASS"
    assert summary["changed_paths"] == sorted(EXPECTED_ALLOWLIST)
    assert summary["authoritative_standards_source"]["result"] == "PASS"
    contract_path = tmp_path / "snapshot.yaml"
    _write_contract(contract_path, contract)
    assert load_snapshot_contract(contract_path) == contract
    assert (
        main(
            [
                "--repository-root",
                str(root),
                "--snapshot-contract",
                str(contract_path),
                "--json",
            ]
        )
        == 0
    )
    cli = capsys.readouterr().out
    api = json.dumps(summary, sort_keys=True) + "\n"
    assert cli.encode("utf-8") == api.encode("utf-8")
    with pytest.raises(SystemExit) as captured:
        main(["--repository-root", str(root), "--json"])
    assert captured.value.code == 2


def test_same_exact_snapshot_passes_at_two_disposable_absolute_roots(
    tmp_path: Path,
) -> None:
    first_root, first_contract = _api_workspace(tmp_path / "first")
    second_root, second_contract = _api_workspace(tmp_path / "second")
    assert first_root.is_absolute() and second_root.is_absolute()
    assert first_root != second_root
    assert (
        _run(first_root, "rev-parse", "HEAD").stdout
        == _run(second_root, "rev-parse", "HEAD").stdout
    )
    assert (
        _run(first_root, "rev-parse", "HEAD^{tree}").stdout
        == _run(second_root, "rev-parse", "HEAD^{tree}").stdout
    )
    assert first_contract == second_contract
    first = validate_governance_baseline(first_root, first_contract)
    second = validate_governance_baseline(second_root, second_contract)
    assert json.dumps(first, sort_keys=True).encode("utf-8") == json.dumps(
        second, sort_keys=True
    ).encode("utf-8")


def test_public_api_rejects_symlink_subdirectory_relative_and_wrong_branch_roots(
    tmp_path: Path,
) -> None:
    root, contract = _api_workspace(tmp_path / "repository")
    link = tmp_path / "repository-link"
    link.symlink_to(root, target_is_directory=True)
    _assert_api_failure(link, contract, "FAIL_REPOSITORY_ROOT")
    _assert_api_failure(Path("/"), contract, "FAIL_REPOSITORY_ROOT")
    _assert_api_failure(tmp_path / ".." / tmp_path.name, contract, "FAIL_REPOSITORY_ROOT")
    _assert_api_failure(tmp_path / "missing-repository", contract, "FAIL_REPOSITORY_ROOT")
    regular_file = tmp_path / "not-a-repository-directory"
    regular_file.write_text("synthetic", encoding="utf-8")
    _assert_api_failure(regular_file, contract, "FAIL_REPOSITORY_ROOT")
    _assert_api_failure(root / "docs", contract, "FAIL_ENVIRONMENT_IDENTITY")
    _assert_api_failure(Path("relative-repository"), contract, "FAIL_REPOSITORY_ROOT")
    _run(root, "branch", "-m", "wrong-branch")
    _assert_api_failure(root, contract, "FAIL_ENVIRONMENT_IDENTITY")
    with pytest.raises(FactoryFailure) as captured:
        validator._observed_modes(root, {"missing-from-tree.txt"})
    assert captured.value.code == "FAIL_FILE_MODE"


@pytest.mark.parametrize(
    ("mutation", "code"),
    [
        (lambda value: value.pop("standards"), "FAIL_SNAPSHOT_CONTRACT"),
        (lambda value: value.update({"unexpected": True}), "FAIL_SNAPSHOT_CONTRACT"),
        (
            lambda value: value["topology"].update({"expected_head_sha": "0" * 40}),
            "FAIL_HEAD_IDENTITY",
        ),
        (
            lambda value: value["topology"].update({"expected_head_tree": "0" * 40}),
            "FAIL_HEAD_TREE",
        ),
        (
            lambda value: value["topology"].update({"corrective_parent_sha": "0" * 40}),
            "FAIL_CORRECTIVE_PARENT",
        ),
        (
            lambda value: value["topology"].update({"base_to_head_commit_count": 2}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["topology"].update({"parent_to_head_commit_count": 2}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["topology"].update({"base_sha": "0" * 40}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["topology"].update({"base_tree": "0" * 40}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["changed_paths"].append("fabricated.txt"),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["file_modes"].update({EXPECTED_README_PATH.as_posix(): "100755"}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["standards"]["bindings"][2].update(
                {"source_body_ranges": [[582, 699], [701, 760]]}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["standards"]["bindings"][2].update({"redacted_source_blocks": []}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["standards"]["bindings"][0].update({"code": "WRONG"}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["standards"]["bindings"][0].update({"version": "0.0.0"}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["standards"]["bindings"][0].update({"extract_path": "wrong.txt"}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["standards"]["bindings"][0].update({"extract_sha256": "0" * 64}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
    ],
)
def test_snapshot_contract_negative_matrix(
    tmp_path: Path,
    mutation: Callable[[dict[str, Any]], Any],
    code: str,
) -> None:
    root, contract = _api_workspace(tmp_path)
    mutation(contract)
    _assert_api_failure(root, contract, code)


def test_public_api_rejects_dirty_unexpected_sensitive_symlink_and_mode(
    tmp_path: Path,
) -> None:
    root, contract = _api_workspace(tmp_path / "dirty")
    (root / "dirty.txt").write_text("dirty", encoding="utf-8")
    _assert_api_failure(root, contract, "FAIL_DIRTY_WORKTREE")

    root, contract = _api_workspace(tmp_path / "unexpected")
    (root / "unexpected.txt").write_text("unexpected", encoding="utf-8")
    _amend(root)
    _assert_api_failure(root, _refresh_contract_identity(root, contract), "FAIL_FILE_ALLOWLIST")

    root, contract = _api_workspace(tmp_path / "sensitive")
    readme = root / EXPECTED_README_PATH
    prohibited = "pass" + "word=" + "abcdefghijklmnop"
    readme.write_text(readme.read_text(encoding="utf-8") + prohibited, encoding="utf-8")
    _amend(root)
    _assert_api_failure(root, _refresh_contract_identity(root, contract), "FAIL_SENSITIVE_VALUE")

    root, contract = _api_workspace(tmp_path / "symlink")
    candidate = root / EXPECTED_CANDIDATE_PATH
    candidate.unlink()
    candidate.symlink_to(root / EXPECTED_WRAPPER_PATH)
    _amend(root)
    _assert_api_failure(root, _refresh_contract_identity(root, contract), "FAIL_PATH_SAFETY")

    root, contract = _api_workspace(tmp_path / "mode")
    (root / EXPECTED_README_PATH).chmod(0o755)
    _amend(root)
    _assert_api_failure(root, _refresh_contract_identity(root, contract), "FAIL_FILE_MODE")


def test_public_api_rejects_replacement_extra_commit_wrong_origin_and_parent(
    tmp_path: Path,
) -> None:
    root, contract = _api_workspace(tmp_path / "replacement")
    _run(root, "reset", "--soft", EXPECTED_BASE_COMMIT)
    _commit_at(root, "test: forbidden replacement commit", 5)
    _assert_api_failure(root, _refresh_contract_identity(root, contract), "FAIL_COMMIT_TOPOLOGY")

    root, contract = _api_workspace(tmp_path / "extra")
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=YSim Test",
            "-c",
            f"user.email={_synthetic_git_email()}",
            "commit",
            "--quiet",
            "--allow-empty",
            "-m",
            "test: forbidden extra head",
        ],
        check=True,
        capture_output=True,
    )
    _assert_api_failure(root, _refresh_contract_identity(root, contract), "FAIL_COMMIT_TOPOLOGY")

    root, contract = _api_workspace(tmp_path / "origin")
    _run(root, "remote", "set-url", "origin", "https://github.com/other/repository.git")
    _assert_api_failure(root, contract, "FAIL_ENVIRONMENT_IDENTITY")

    root, contract = _api_workspace(tmp_path / "parent")
    contract["topology"]["corrective_parent_tree"] = "0" * 40
    _assert_api_failure(root, contract, "FAIL_CORRECTIVE_PARENT")


def test_snapshot_contract_loader_rejects_symlink(
    tmp_path: Path,
) -> None:
    _, contract = _api_workspace(tmp_path / "repository")
    actual = tmp_path / "actual.yaml"
    link = tmp_path / "contract.yaml"
    _write_contract(actual, contract)
    link.symlink_to(actual)
    with pytest.raises(FactoryFailure) as captured:
        load_snapshot_contract(link)
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"
    with pytest.raises(FactoryFailure) as captured:
        load_snapshot_contract(tmp_path / "missing.yaml")
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"


@pytest.mark.parametrize(
    "mutation",
    [
        lambda value: value.update({"schema_version": "1"}),
        lambda value: value["repository"].update({"identity": "wrong/repository"}),
        lambda value: value["topology"].update({"expected_head_sha": "malformed"}),
        lambda value: value["authoritative_inputs"]["docx"].update({"size_bytes": 1}),
        lambda value: value["standards"].update({"provenance_path": "wrong.yaml"}),
    ],
)
def test_snapshot_contract_schema_type_and_binding_fail_closed(
    tmp_path: Path,
    mutation: Callable[[dict[str, Any]], Any],
) -> None:
    _, contract = _api_workspace(tmp_path)
    mutation(contract)
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_snapshot_contract(contract)
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"


def test_external_file_and_redaction_defenses(
    tmp_path: Path,
) -> None:
    relative = Path("relative")
    with pytest.raises(FactoryFailure) as captured:
        validator._read_external_regular_file(relative, code="FAIL_EXTERNAL")
    assert captured.value.code == "FAIL_EXTERNAL"

    directory = tmp_path / "directory"
    directory.mkdir()
    with pytest.raises(FactoryFailure) as captured:
        validator._read_external_regular_file(directory, code="FAIL_EXTERNAL")
    assert captured.value.code == "FAIL_EXTERNAL"

    regular = tmp_path / "regular"
    regular.write_bytes(b"safe")
    with pytest.raises(FactoryFailure) as captured:
        validator._read_external_regular_file(regular, code="FAIL_EXTERNAL", expected_size=5)
    assert captured.value.code == "FAIL_EXTERNAL"

    malformed = tmp_path / "malformed.yaml"
    malformed.write_text("[invalid", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        load_snapshot_contract(malformed)
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"

    with pytest.raises(FactoryFailure) as captured:
        validator._redact_env_block(["unexpected source block"])
    assert captured.value.code == "FAIL_AUTHORITATIVE_STANDARDS_SOURCE"

    root, contract = _api_workspace(tmp_path / "provenance")
    contract["standards"]["provenance_sha256"] = "0" * 64
    _assert_api_failure(root, contract, "FAIL_GOVERNING_STANDARDS")


def test_render_and_candidate_immutability_defensive_branches(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    other = validator.ElementTree.Element("other")
    empty_table = validator.ElementTree.Element(
        "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl"
    )
    assert validator._render_docx_block(other, namespace) == []
    assert validator._render_docx_block(empty_table, namespace) == []

    root = _content_workspace(tmp_path)
    candidate = root / EXPECTED_CANDIDATE_PATH
    data = candidate.read_bytes().replace(
        b"CANDIDATE_FOR_HUMAN_ACCEPTANCE", b"CANDIDATE_FOR_HUMAN_ACCEPTANCX", 1
    )
    candidate.write_bytes(data)
    monkeypatch.setattr(validator, "EXPECTED_CANDIDATE_SHA256", hashlib.sha256(data).hexdigest())
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_candidate(root)
    assert captured.value.code == "FAIL_CANDIDATE_IMMUTABILITY"


def test_cli_failure_and_plain_success_share_security_boundary(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root, contract = _api_workspace(tmp_path)
    contract_path = tmp_path / "snapshot.yaml"
    _write_contract(contract_path, contract)
    assert main(["--repository-root", str(root), "--snapshot-contract", str(contract_path)]) == 0
    assert capsys.readouterr().out == "V3-R1-G00-S02 validation PASS\n"
    monkeypatch.setenv("WSL_DISTRO_NAME", "WRONG")
    assert (
        main(
            [
                "--repository-root",
                str(root),
                "--snapshot-contract",
                str(contract_path),
                "--json",
            ]
        )
        == 1
    )
    assert '"code": "FAIL_ENVIRONMENT_IDENTITY"' in capsys.readouterr().out


def test_integration_isolation_fixture_has_canonical_invariants() -> None:
    fixture = _repository_root() / "tools/ysf/tests/integration/conftest.py"
    text = fixture.read_text(encoding="utf-8")
    assert "_canonical_snapshot(canonical) == before" in text
    assert 'git", "clone' in text
    assert 'os.chdir(repository / "tools/ysf")' in text
