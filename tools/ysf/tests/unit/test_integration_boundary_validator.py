from __future__ import annotations

import hashlib
import json
import os
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest
import yaml

from ysf.integration_boundary import validator
from ysf.integration_boundary.validator import (
    EXPECTED_ALLOWLIST,
    EXPECTED_ALLOWLIST_ORDER,
    EXPECTED_ARTIFACT_PATHS,
    EXPECTED_BASE_SHA,
    EXPECTED_BRANCH,
    EXPECTED_ORIGIN_SHA256,
    EXPECTED_REQUIREMENTS,
    EXPECTED_SCOPE_DECISIONS,
    EXPECTED_STABLE_READ,
    load_snapshot_contract,
    main,
    validate_integration_boundary,
)
from ysf.secure_factory.models import FactoryFailure


def repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


def run_git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def synthetic_origin() -> str:
    return "git" + chr(64) + "github-ysim:nvkhoabk/ysim.git"


def synthetic_git_email() -> str:
    return "ysim-s04-test" + chr(64) + "example.invalid"


def commit(root: Path, message: str) -> None:
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=YSim S04 Test",
            "-c",
            f"user.email={synthetic_git_email()}",
            "commit",
            "--quiet",
            "--amend",
            "--no-edit",
        ],
        check=True,
        capture_output=True,
    )
    assert message


def clone_workspace(path: Path) -> Path:
    source = repository_root()
    subprocess.run(
        ["git", "clone", "--quiet", "--local", str(source), str(path)],
        check=True,
        capture_output=True,
    )
    run_git(path, "remote", "set-url", "origin", synthetic_origin())
    if run_git(path, "branch", "--show-current") != EXPECTED_BRANCH:
        run_git(path, "checkout", "--quiet", EXPECTED_BRANCH)
    return path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot_contract(root: Path) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "repository": {
            "identity": "nvkhoabk/ysim",
            "origin_sha256": EXPECTED_ORIGIN_SHA256,
            "branch": EXPECTED_BRANCH,
        },
        "topology": {
            "base_sha": EXPECTED_BASE_SHA,
            "base_tree": validator.EXPECTED_BASE_TREE,
            "parent_sha": validator.EXPECTED_CORRECTIVE_PARENT_SHA,
            "expected_head_sha": run_git(root, "rev-parse", "HEAD"),
            "expected_head_tree": run_git(root, "rev-parse", "HEAD^{tree}"),
            "base_to_head_commit_count": 2,
            "parent_to_head_commit_count": 1,
        },
        "changed_paths": sorted(EXPECTED_ALLOWLIST),
        "authorized_paths": sorted(EXPECTED_ALLOWLIST),
        "file_modes": {path: "100644" for path in sorted(EXPECTED_ALLOWLIST)},
        "artifact_digests": {
            path: sha256(root / path) for path in EXPECTED_ARTIFACT_PATHS
        },
        "requirements": list(EXPECTED_REQUIREMENTS),
        "scope_decisions": dict(EXPECTED_SCOPE_DECISIONS),
        "safety": {
            "providers": "OFF",
            "email_mode": "NON_RELAYING",
            "external_effect_budget": "DENY_ALL",
        },
        "knowledge": {
            "source": "CURRENT_DOCS_IN_MEMORY",
            "tracked_factory_index_allowed": False,
            **validator._fresh_knowledge(root),
        },
        "branch_coverage": {
            "source_package": "ysf.integration_boundary",
            "metric": "COVERED_BRANCHES_DIVIDED_BY_VALID_BRANCHES",
            "minimum_percent": 90.0,
            "branches_covered": 9,
            "branches_valid": 10,
            "branch_rate": 0.9,
            "percent": 90.0,
        },
        "stable_read": dict(EXPECTED_STABLE_READ),
    }


def refresh_identity(
    root: Path, contract: dict[str, Any], *, refresh_knowledge: bool = True
) -> dict[str, Any]:
    updated = deepcopy(contract)
    updated["topology"]["expected_head_sha"] = run_git(root, "rev-parse", "HEAD")
    updated["topology"]["expected_head_tree"] = run_git(root, "rev-parse", "HEAD^{tree}")
    updated["artifact_digests"] = {
        path: sha256(root / path) for path in EXPECTED_ARTIFACT_PATHS
    }
    if refresh_knowledge:
        updated["knowledge"] = {
            "source": "CURRENT_DOCS_IN_MEMORY",
            "tracked_factory_index_allowed": False,
            **validator._fresh_knowledge(root),
        }
    return updated


def update_manifest_record(root: Path, relative: str) -> None:
    manifest = root / validator.MANIFEST_PATH
    records = manifest.read_text(encoding="utf-8").splitlines()
    suffix = f"  {relative}"
    replacement = f"{sha256(root / relative)}{suffix}"
    manifest.write_text(
        "\n".join(replacement if line.endswith(suffix) else line for line in records) + "\n",
        encoding="utf-8",
    )


def write_yaml(path: Path, value: Any) -> None:
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")


def assert_failure(root: Path, contract: dict[str, Any], code: str) -> None:
    with pytest.raises(FactoryFailure) as captured:
        validate_integration_boundary(root, contract)
    assert captured.value.code == code


def test_exact_repository_package_passes() -> None:
    root = repository_root()
    result = validate_integration_boundary(root, snapshot_contract(root))
    assert result["result"] == "PASS"
    assert result["checkpoint"] == "V3-R1-G00-S04"
    assert result["requirements"] == list(EXPECTED_REQUIREMENTS)
    assert result["scope_decisions"] == EXPECTED_SCOPE_DECISIONS
    assert result["providers"] == "OFF"
    assert result["email_mode"] == "NON_RELAYING"
    assert result["external_effect_budget"] == "DENY_ALL"


def test_api_cli_output_is_identical_at_two_absolute_roots(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    first = clone_workspace(tmp_path / "first")
    second = clone_workspace(tmp_path / "second")
    contract = snapshot_contract(first)
    first_result = validate_integration_boundary(first, contract)
    second_result = validate_integration_boundary(second, contract)
    assert first_result == second_result
    contract_path = tmp_path / "snapshot-contract-v2.yaml"
    write_yaml(contract_path, contract)
    assert main(
        ["--repository-root", str(first), "--snapshot-contract", str(contract_path), "--json"]
    ) == 0
    first_output = capsys.readouterr().out
    assert main(
        ["--repository-root", str(second), "--snapshot-contract", str(contract_path), "--json"]
    ) == 0
    second_output = capsys.readouterr().out
    assert first_output == second_output
    assert json.loads(first_output) == first_result


@pytest.mark.parametrize(
    "key",
    [
        "schema_version",
        "repository",
        "topology",
        "changed_paths",
        "authorized_paths",
        "file_modes",
        "artifact_digests",
        "requirements",
        "scope_decisions",
        "safety",
        "knowledge",
        "branch_coverage",
        "stable_read",
    ],
)
def test_snapshot_contract_missing_keys_fail_closed(key: str) -> None:
    root = repository_root()
    contract = snapshot_contract(root)
    contract.pop(key)
    assert_failure(root, contract, "FAIL_SNAPSHOT_CONTRACT")


def test_snapshot_contract_extra_key_and_schema_version_fail_closed() -> None:
    root = repository_root()
    extra = snapshot_contract(root)
    extra["extra"] = True
    assert_failure(root, extra, "FAIL_SNAPSHOT_CONTRACT")
    wrong = snapshot_contract(root)
    wrong["schema_version"] = 1
    assert_failure(root, wrong, "FAIL_SNAPSHOT_CONTRACT")


@pytest.mark.parametrize(
    ("section", "field", "value"),
    [
        ("repository", "identity", "other/repository"),
        ("repository", "origin_sha256", "0" * 64),
        ("repository", "branch", "wrong-branch"),
        ("topology", "base_sha", "0" * 40),
        ("topology", "base_tree", "0" * 40),
        ("topology", "parent_sha", "0" * 40),
        ("topology", "base_to_head_commit_count", 3),
        ("topology", "parent_to_head_commit_count", 2),
        ("safety", "providers", "ON"),
        ("safety", "email_mode", "RELAYING"),
        ("safety", "external_effect_budget", "ALLOW"),
        ("knowledge", "source", "TRACKED_INDEX"),
        ("knowledge", "tracked_factory_index_allowed", True),
        ("knowledge", "duplicate_document_codes", 1),
        ("branch_coverage", "source_package", "ysf"),
        ("branch_coverage", "minimum_percent", 89.0),
        ("stable_read", "nofollow", False),
    ],
)
def test_snapshot_contract_weakened_fields_fail_closed(
    section: str, field: str, value: object
) -> None:
    root = repository_root()
    contract = snapshot_contract(root)
    contract[section][field] = value
    assert_failure(root, contract, "FAIL_SNAPSHOT_CONTRACT")


@pytest.mark.parametrize(
    "kind",
    [
        "changed-missing",
        "changed-extra",
        "changed-reordered",
        "authorized-missing",
        "authorized-extra",
        "mode",
        "artifact-missing",
        "artifact-extra",
        "artifact-malformed",
        "requirements-extra",
        "requirements-reordered",
        "decision-extra",
        "decision-wrong",
    ],
)
def test_snapshot_scope_negative_matrix(kind: str) -> None:
    root = repository_root()
    contract = snapshot_contract(root)
    if kind == "changed-missing":
        contract["changed_paths"].pop()
    elif kind == "changed-extra":
        contract["changed_paths"].append("unexpected.txt")
    elif kind == "changed-reordered":
        contract["changed_paths"].reverse()
    elif kind == "authorized-missing":
        contract["authorized_paths"].pop()
    elif kind == "authorized-extra":
        contract["authorized_paths"].append("unexpected.txt")
    elif kind == "mode":
        contract["file_modes"][EXPECTED_ALLOWLIST_ORDER[0]] = "100755"
    elif kind == "artifact-missing":
        contract["artifact_digests"].pop(EXPECTED_ARTIFACT_PATHS[0])
    elif kind == "artifact-extra":
        contract["artifact_digests"]["unexpected"] = "0" * 64
    elif kind == "artifact-malformed":
        contract["artifact_digests"][EXPECTED_ARTIFACT_PATHS[0]] = "bad"
    elif kind == "requirements-extra":
        contract["requirements"].append("V3-R1-REL-001")
    elif kind == "requirements-reordered":
        contract["requirements"].reverse()
    elif kind == "decision-extra":
        contract["scope_decisions"]["V3-R1-REL-007"] = "DEFER"
    else:
        contract["scope_decisions"]["V3-R1-REL-001"] = "INCLUDE"
    assert_failure(root, contract, "FAIL_SNAPSHOT_CONTRACT")


@pytest.mark.parametrize(
    ("covered", "valid", "rate", "percent"),
    [
        (89, 100, 0.89, 89.0),
        (101, 100, 1.01, 101.0),
        (90, 0, 0.9, 90.0),
        (90, 100, 0.8999, 90.0),
        (90, 100, 0.9, 90.1),
        (90.0, 100, 0.9, 90.0),
    ],
)
def test_branch_coverage_contract_fails_closed(
    covered: object, valid: object, rate: object, percent: object
) -> None:
    root = repository_root()
    contract = snapshot_contract(root)
    contract["branch_coverage"].update(
        branches_covered=covered,
        branches_valid=valid,
        branch_rate=rate,
        percent=percent,
    )
    assert_failure(root, contract, "FAIL_SNAPSHOT_CONTRACT")


def test_repository_dirty_origin_branch_and_head_fail_closed(tmp_path: Path) -> None:
    root = clone_workspace(tmp_path / "dirty")
    contract = snapshot_contract(root)
    (root / "untracked.txt").write_text("synthetic", encoding="utf-8")
    assert_failure(root, contract, "FAIL_DIRTY_WORKTREE")

    root = clone_workspace(tmp_path / "origin")
    contract = snapshot_contract(root)
    run_git(root, "remote", "set-url", "origin", "https://github.com/other/repository.git")
    assert_failure(root, contract, "FAIL_REPOSITORY_IDENTITY")

    root = clone_workspace(tmp_path / "branch")
    contract = snapshot_contract(root)
    run_git(root, "branch", "-m", "wrong-branch")
    assert_failure(root, contract, "FAIL_REPOSITORY_IDENTITY")

    root = clone_workspace(tmp_path / "head")
    contract = snapshot_contract(root)
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=YSim S04 Test",
            "-c",
            f"user.email={synthetic_git_email()}",
            "commit",
            "--quiet",
            "--allow-empty",
            "-m",
            "test extra head",
        ],
        check=True,
        capture_output=True,
    )
    assert_failure(root, contract, "FAIL_HEAD_IDENTITY")


def test_changed_path_mode_and_symlink_fail_closed(tmp_path: Path) -> None:
    root = clone_workspace(tmp_path / "extra")
    contract = snapshot_contract(root)
    (root / "unexpected.txt").write_text("synthetic", encoding="utf-8")
    run_git(root, "add", "unexpected.txt")
    commit(root, "test unexpected path")
    contract = refresh_identity(root, contract)
    assert_failure(root, contract, "FAIL_FILE_ALLOWLIST")

    root = clone_workspace(tmp_path / "mode")
    contract = snapshot_contract(root)
    (root / validator.README_PATH).chmod(0o755)
    run_git(root, "add", validator.README_PATH)
    commit(root, "test mode")
    contract = refresh_identity(root, contract)
    assert_failure(root, contract, "FAIL_FILE_MODE")

    root = clone_workspace(tmp_path / "symlink")
    contract = snapshot_contract(root)
    readme = root / validator.README_PATH
    readme.unlink()
    readme.symlink_to(root / validator.SPEC_PATH)
    run_git(root, "add", validator.README_PATH)
    commit(root, "test symlink")
    contract = refresh_identity(root, contract, refresh_knowledge=False)
    assert_failure(root, contract, "FAIL_PATH_SAFETY")


@pytest.mark.parametrize(
    ("relative", "code"),
    [
        (validator.BASELINE_PATH, "FAIL_PACKAGE_BASELINE"),
        (validator.SCOPE_PATH, "FAIL_SCOPE_DECISIONS"),
        (validator.SPEC_PATH, "FAIL_PACKAGE_SPEC"),
        (validator.PROVENANCE_PATH, "FAIL_SOURCE_PROVENANCE"),
    ],
)
def test_artifact_identity_mutation_fails_closed(
    tmp_path: Path, relative: str, code: str
) -> None:
    root = clone_workspace(tmp_path / relative.rsplit("/", 1)[-1])
    contract = snapshot_contract(root)
    document = yaml.safe_load((root / relative).read_text(encoding="utf-8"))
    document["checkpoint"] = "V3-R1-G00-OTHER"
    write_yaml(root / relative, document)
    run_git(root, "add", relative)
    commit(root, "test artifact mutation")
    contract = refresh_identity(root, contract)
    assert_failure(root, contract, code)


def test_baseline_safety_and_scope_disposition_fail_closed(tmp_path: Path) -> None:
    root = clone_workspace(tmp_path / "baseline-safety")
    contract = snapshot_contract(root)
    baseline = yaml.safe_load((root / validator.BASELINE_PATH).read_text(encoding="utf-8"))
    baseline["safety"]["providers"] = "ON"
    write_yaml(root / validator.BASELINE_PATH, baseline)
    run_git(root, "add", validator.BASELINE_PATH)
    commit(root, "test baseline safety")
    contract = refresh_identity(root, contract)
    assert_failure(root, contract, "FAIL_PACKAGE_BASELINE")

    root = clone_workspace(tmp_path / "scope-disposition")
    contract = snapshot_contract(root)
    scope = yaml.safe_load((root / validator.SCOPE_PATH).read_text(encoding="utf-8"))
    scope["decisions"][0]["retained_state"] = "SOURCE_APPROVED"
    write_yaml(root / validator.SCOPE_PATH, scope)
    run_git(root, "add", validator.SCOPE_PATH)
    commit(root, "test scope disposition")
    contract = refresh_identity(root, contract)
    assert_failure(root, contract, "FAIL_SCOPE_DECISIONS")


def test_recovery_knowledge_and_provenance_bindings_fail_closed(tmp_path: Path) -> None:
    root = clone_workspace(tmp_path / "package-counts")
    contract = snapshot_contract(root)
    package = yaml.safe_load((root / validator.SPEC_PATH).read_text(encoding="utf-8"))
    package["validation_gates"]["knowledge_input"]["observed_final_counts"][
        "index_documents"
    ] = 124
    write_yaml(root / validator.SPEC_PATH, package)
    run_git(root, "add", validator.SPEC_PATH)
    commit(root, "test recovery knowledge binding")
    contract = refresh_identity(root, contract)
    assert_failure(root, contract, "FAIL_PACKAGE_SPEC")

    root = clone_workspace(tmp_path / "recovery-provenance")
    contract = snapshot_contract(root)
    provenance = yaml.safe_load((root / validator.PROVENANCE_PATH).read_text(encoding="utf-8"))
    provenance["safe_stop_recovery"]["revised_write_allowlist_count"] = 15
    write_yaml(root / validator.PROVENANCE_PATH, provenance)
    run_git(root, "add", validator.PROVENANCE_PATH)
    commit(root, "test recovery provenance binding")
    contract = refresh_identity(root, contract)
    assert_failure(root, contract, "FAIL_SOURCE_PROVENANCE")


def test_manifest_missing_extra_malformed_and_digest_fail_closed(tmp_path: Path) -> None:
    for kind in ("missing", "extra", "malformed", "digest"):
        root = clone_workspace(tmp_path / kind)
        contract = snapshot_contract(root)
        manifest = root / validator.MANIFEST_PATH
        lines = manifest.read_text(encoding="utf-8").splitlines()
        if kind == "missing":
            lines.pop()
        elif kind == "extra":
            lines.append(f"{'0' * 64}  unexpected.txt")
        elif kind == "malformed":
            lines[0] = "malformed"
        else:
            lines[0] = f"{'0' * 64}  {lines[0].split('  ', 1)[1]}"
        manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
        run_git(root, "add", validator.MANIFEST_PATH)
        commit(root, f"test manifest {kind}")
        contract = refresh_identity(root, contract)
        assert_failure(root, contract, "FAIL_PACKAGE_MANIFEST")


def test_external_artifact_and_knowledge_digest_mismatch_fail_closed() -> None:
    root = repository_root()
    contract = snapshot_contract(root)
    contract["artifact_digests"][validator.SPEC_PATH] = "0" * 64
    assert_failure(root, contract, "FAIL_SNAPSHOT_ARTIFACT")
    contract = snapshot_contract(root)
    contract["knowledge"]["relationships"] += 1
    assert_failure(root, contract, "FAIL_KNOWLEDGE")


def test_sensitive_changed_source_is_rejected_with_redacted_details(tmp_path: Path) -> None:
    root = clone_workspace(tmp_path / "sensitive")
    contract = snapshot_contract(root)
    target = root / validator.README_PATH
    prohibited = "api_" + "key=" + "abcdefghijklmnop"
    target.write_text(target.read_text(encoding="utf-8") + prohibited, encoding="utf-8")
    update_manifest_record(root, validator.README_PATH)
    run_git(root, "add", validator.README_PATH, validator.MANIFEST_PATH)
    commit(root, "test sensitive source")
    contract = refresh_identity(root, contract)
    with pytest.raises(FactoryFailure) as captured:
        validate_integration_boundary(root, contract)
    assert captured.value.code == "FAIL_SENSITIVE_VALUE"
    assert prohibited not in str(captured.value.details)


def test_stable_reader_rejects_aliases_with_controlled_failure(tmp_path: Path) -> None:
    root_descriptor = validator._open_absolute_directory(tmp_path, "FAIL_TEST")
    before = len(tuple(Path("/proc/self/fd").iterdir()))
    aliases = (
        ".",
        "",
        "./",
        "./.",
        "foo/",
        "foo//bar",
        "foo/.",
        "foo/..",
        "/absolute",
        "../traversal",
        "malformed\x00path",
    )
    try:
        for _ in range(500):
            for alias in aliases:
                with pytest.raises(FactoryFailure) as captured:
                    validator._stable_read_relative(root_descriptor, alias, "FAIL_ALIAS")
                assert captured.value.code == "FAIL_ALIAS"
        after = len(tuple(Path("/proc/self/fd").iterdir()))
        assert after == before
    finally:
        os.close(root_descriptor)


def test_stable_reader_closes_descriptors_and_rejects_symlinks(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.write_bytes(b"stable")
    linked = tmp_path / "linked"
    linked.symlink_to(target)
    root_descriptor = validator._open_absolute_directory(tmp_path, "FAIL_TEST")
    before = len(tuple(Path("/proc/self/fd").iterdir()))
    try:
        for _ in range(500):
            assert (
                validator._stable_read_relative(root_descriptor, "target", "FAIL_STABLE")
                == b"stable"
            )
            with pytest.raises(FactoryFailure) as captured:
                validator._stable_read_relative(root_descriptor, "linked", "FAIL_STABLE")
            assert captured.value.code == "FAIL_STABLE"
        after = len(tuple(Path("/proc/self/fd").iterdir()))
        assert after == before
    finally:
        os.close(root_descriptor)


def test_stable_reader_rejects_final_parent_and_in_read_replacement(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    for kind in ("final", "parent", "truncate"):
        root = tmp_path / kind
        parent = root / "parent"
        parent.mkdir(parents=True)
        target = parent / "target.yaml"
        target.write_bytes(b"value: original\n")
        descriptor = validator._open_absolute_directory(root, "FAIL_TEST")
        original = validator._read_descriptor_bytes

        def mutate(
            opened: int,
            *,
            case: str = kind,
            active_root: Path = root,
            active_parent: Path = parent,
            active_target: Path = target,
            reader: Any = original,
        ) -> bytes:
            if case == "final":
                active_target.rename(active_parent / "original.yaml")
                active_target.write_bytes(b"value: replacement\n")
            elif case == "parent":
                active_parent.rename(active_root / "original-parent")
                active_parent.mkdir()
                (active_parent / "target.yaml").write_bytes(b"value: replacement\n")
            else:
                active_target.write_bytes(b"changed")
            return reader(opened)

        monkeypatch.setattr(validator, "_read_descriptor_bytes", mutate)
        with pytest.raises(FactoryFailure) as captured:
            validator._stable_read_relative(descriptor, "parent/target.yaml", "FAIL_STABLE")
        assert captured.value.code == "FAIL_STABLE"
        os.close(descriptor)
        monkeypatch.setattr(validator, "_read_descriptor_bytes", original)


def test_snapshot_requires_exact_head_blob_and_contract_file_is_nofollow(
    tmp_path: Path
) -> None:
    root = clone_workspace(tmp_path / "blob")
    target = root / validator.README_PATH
    target.write_bytes(target.read_bytes() + b"\n")
    with validator._ValidationSnapshot(root) as snapshot:
        with pytest.raises(FactoryFailure) as captured:
            snapshot.read(validator.README_PATH)
    assert captured.value.code == "FAIL_WORKTREE_BLOB"

    contract_path = tmp_path / "contract.yaml"
    write_yaml(contract_path, {"schema_version": 2})
    linked = tmp_path / "linked.yaml"
    linked.symlink_to(contract_path)
    with pytest.raises(FactoryFailure) as captured:
        load_snapshot_contract(linked)
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"


def test_root_and_defensive_helpers_fail_closed(tmp_path: Path) -> None:
    root = repository_root()
    contract = snapshot_contract(root)
    assert_failure(Path("relative"), contract, "FAIL_REPOSITORY_ROOT")
    link = tmp_path / "root-link"
    link.symlink_to(root, target_is_directory=True)
    assert_failure(link, contract, "FAIL_REPOSITORY_ROOT")
    with pytest.raises(FactoryFailure) as captured:
        validator._mapping([], "FAIL_TYPE", "mapping")
    assert captured.value.code == "FAIL_TYPE"
    with pytest.raises(FactoryFailure) as captured:
        validator._sequence("text", "FAIL_TYPE", "sequence")
    assert captured.value.code == "FAIL_TYPE"
    with pytest.raises(FactoryFailure) as captured:
        validator._run_git(tmp_path, "rev-parse", "HEAD")
    assert captured.value.code == "FAIL_REPOSITORY_IDENTITY"


def test_cli_failure_uses_same_safe_boundary(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    root = repository_root()
    contract = snapshot_contract(root)
    contract["topology"]["expected_head_sha"] = "0" * 40
    path = tmp_path / "contract.yaml"
    write_yaml(path, contract)
    assert main(["--repository-root", str(root), "--snapshot-contract", str(path), "--json"]) == 1
    output = json.loads(capsys.readouterr().out)
    assert output["result"] == "FAIL"
    assert output["code"] == "FAIL_HEAD_IDENTITY"


def test_contract_defensive_type_and_consistency_branches_fail_closed() -> None:
    root = repository_root()
    contract = snapshot_contract(root)
    contract["changed_paths"] = [1]
    assert_failure(root, contract, "FAIL_SNAPSHOT_CONTRACT")
    contract = snapshot_contract(root)
    contract["changed_paths"][0] = "../unsafe"
    assert_failure(root, contract, "FAIL_SNAPSHOT_CONTRACT")
    contract = snapshot_contract(root)
    contract["topology"]["expected_head_sha"] = "malformed"
    assert_failure(root, contract, "FAIL_SNAPSHOT_CONTRACT")
    contract = snapshot_contract(root)
    contract["knowledge"]["relationships"] = -1
    assert_failure(root, contract, "FAIL_SNAPSHOT_CONTRACT")
    contract = snapshot_contract(root)
    contract["knowledge"]["index_documents"] += 1
    assert_failure(root, contract, "FAIL_SNAPSHOT_CONTRACT")


def test_low_level_stable_and_yaml_defensive_branches(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(validator.platform, "system", lambda: "Other")
    with pytest.raises(FactoryFailure) as captured:
        validator._open_absolute_directory(tmp_path, "FAIL_TEST")
    assert captured.value.code == "FAIL_ENVIRONMENT_IDENTITY"
    monkeypatch.setattr(validator.platform, "system", lambda: "Linux")

    with pytest.raises(FactoryFailure) as captured:
        validator._open_absolute_directory(Path("relative"), "FAIL_TEST")
    assert captured.value.code == "FAIL_TEST"
    with pytest.raises(FactoryFailure) as captured:
        validator._open_absolute_directory(tmp_path / "missing", "FAIL_TEST")
    assert captured.value.code == "FAIL_TEST"
    with pytest.raises(FactoryFailure) as captured:
        validator._git_file_bytes(tmp_path, "missing", "path", "FAIL_BLOB")
    assert captured.value.code == "FAIL_BLOB"
    with pytest.raises(FactoryFailure) as captured:
        validator._load_yaml_bytes(b"[invalid", "FAIL_YAML", "synthetic")
    assert captured.value.code == "FAIL_YAML"

    target = tmp_path / "target"
    target.write_bytes(b"stable")
    descriptor = validator._open_absolute_directory(tmp_path, "FAIL_TEST")
    try:
        snapshot_value = validator._stable_read_relative(descriptor, "target", "FAIL_TEST")
        assert snapshot_value == b"stable"
    finally:
        os.close(descriptor)


def test_snapshot_cache_capture_and_fresh_knowledge_defensive_branches(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = clone_workspace(tmp_path / "cache")
    with validator._ValidationSnapshot(root) as snapshot:
        snapshot.capture_all([validator.README_PATH])
        assert snapshot.read(validator.README_PATH) == snapshot.read(validator.README_PATH)

    monkeypatch.setattr(validator, "build_document_index", lambda _root: {"documents": None})
    with pytest.raises(FactoryFailure) as captured:
        validator._fresh_knowledge(root)
    assert captured.value.code == "FAIL_KNOWLEDGE"

    monkeypatch.setattr(
        validator,
        "build_document_index",
        lambda _root: {"documentCount": 0, "documents": []},
    )

    def invalid_documents(_documents: object) -> None:
        raise ValueError("synthetic")

    monkeypatch.setattr(validator, "validate_documents", invalid_documents)
    with pytest.raises(FactoryFailure) as captured:
        validator._fresh_knowledge(root)
    assert captured.value.code == "FAIL_KNOWLEDGE"


def test_plain_cli_success_branch(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    root = repository_root()
    path = tmp_path / "contract.yaml"
    write_yaml(path, snapshot_contract(root))
    assert main(["--repository-root", str(root), "--snapshot-contract", str(path)]) == 0
    assert capsys.readouterr().out == "V3-R1-G00-S04 validation PASS\n"
