from __future__ import annotations

import copy
import hashlib
import inspect
import json
import os
import subprocess
import tomllib
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest
import yaml

from ysf.configuration_access_control import validator
from ysf.configuration_access_control.validator import (
    EXPECTED_ALLOWLIST,
    EXPECTED_BASE_SHA,
    EXPECTED_BRANCH,
    EXPECTED_CHANGED_PATHS,
    EXPECTED_CORRECTIVE_PARENT_SHA,
    EXPECTED_CORRECTIVE_PARENT_TREE,
    load_snapshot_contract,
    main,
    validate_configuration_access_control,
)
from ysf.secure_factory.models import FactoryFailure

Mutation = Callable[[Path], None]
ACCEPTED_S03_SHA = "168efc707cde042ef0459a2bd92f177617c4a25b"
ACCEPTED_S03_TREE = "6126508cf1fdae163dbf9ccc43684a567fa6c7e1"
S04_CHANGED_SHARED_PATH = "tools/ysf/tests/integration/test_build_knowledge.py"
R5_WRITE_SUBSET = frozenset(
    {
        "docs/v3/r1/g00/s03/MANIFEST.sha256",
        "docs/v3/r1/g00/s03/README.md",
        "docs/v3/r1/g00/s03/package-spec.yaml",
        "docs/v3/r1/g00/s03/source-provenance.yaml",
        "tools/ysf/src/ysf/configuration_access_control/validator.py",
        "tools/ysf/tests/unit/test_configuration_access_control_validator.py",
    }
)
AUTHORITATIVE_PATHS = {
    "docs/v3/r1/g00/s01/traceability-baseline.yaml",
    "docs/BRD/BRD-WS-14.md",
    "docs/BRD/BRD-WS-16.md",
    "factory/releases/v3-r1-g00-s02-governance-requirements-baseline/YSim_V3_R1_G00_S02_Governance_Requirements_Baseline_v0.1.0-candidate.1.md",
    "docs/v3/r1/g00/s02/acceptance-receipt.yaml",
    "docs/v3/r1/g00/s02/package-spec.yaml",
    "docs/v3/r1/g00/s02/standards/standards-provenance.yaml",
}


def repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


def git(root: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def synthetic_git_email() -> str:
    return "ysim-s03" + "@" + "example.invalid"


def commit(root: Path, message: str, timestamp: int, *, amend: bool = False) -> None:
    environment = {
        **os.environ,
        "GIT_AUTHOR_DATE": f"2000-01-01T00:00:{timestamp:02d}Z",
        "GIT_COMMITTER_DATE": f"2000-01-01T00:00:{timestamp:02d}Z",
    }
    command = [
        "git",
        "-C",
        str(root),
        "-c",
        "user.name=YSim S03 Test",
        "-c",
        f"user.email={synthetic_git_email()}",
        "commit",
        "--quiet",
    ]
    if amend:
        command.extend(("--amend", "--no-edit"))
    else:
        command.extend(("-m", message))
    subprocess.run(
        command,
        check=True,
        capture_output=True,
        env=environment,
    )


def accepted_s03_blob(relative: str) -> bytes:
    source = repository_root()
    assert git(source, "rev-parse", f"{ACCEPTED_S03_SHA}^{{tree}}") == ACCEPTED_S03_TREE
    entry = subprocess.run(
        ["git", "-C", str(source), "ls-tree", "-z", ACCEPTED_S03_SHA, "--", relative],
        check=True,
        capture_output=True,
    ).stdout
    assert entry.endswith(b"\0") and entry.count(b"\0") == 1
    metadata, observed_path = entry[:-1].split(b"\t", 1)
    mode, object_type, object_sha = metadata.decode("ascii").split(" ")
    assert mode == "100644"
    assert object_type == "blob"
    assert observed_path.decode("utf-8") == relative
    content = subprocess.run(
        ["git", "-C", str(source), "cat-file", "blob", object_sha],
        check=True,
        capture_output=True,
    ).stdout
    observed_sha = subprocess.run(
        ["git", "-C", str(source), "hash-object", "--stdin"],
        input=content,
        check=True,
        capture_output=True,
    ).stdout.decode("ascii").strip()
    assert observed_sha == object_sha
    return content


def copy_package(root: Path) -> None:
    for relative in sorted(EXPECTED_ALLOWLIST | AUTHORITATIVE_PATHS):
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(accepted_s03_blob(relative))


def content_workspace(tmp_path: Path) -> Path:
    root = tmp_path / "content"
    copy_package(root)
    return root


def accepted_s03_workspace(tmp_path: Path) -> Path:
    root = tmp_path / "accepted-s03"
    git(tmp_path, "clone", "--quiet", "--no-hardlinks", str(repository_root()), str(root))
    git(root, "switch", "--quiet", "--detach", ACCEPTED_S03_SHA)
    assert git(root, "rev-parse", "HEAD^{tree}") == ACCEPTED_S03_TREE
    return root


def test_s03_fixture_uses_accepted_tree_not_current_s04_bytes(tmp_path: Path) -> None:
    accepted = accepted_s03_blob(S04_CHANGED_SHARED_PATH)
    current = (repository_root() / S04_CHANGED_SHARED_PATH).read_bytes()
    assert current != accepted
    root = content_workspace(tmp_path)
    assert (root / S04_CHANGED_SHARED_PATH).read_bytes() == accepted
    assert hashlib.sha256(current).digest() != hashlib.sha256(accepted).digest()


def snapshot_contract(root: Path) -> dict[str, Any]:
    paths = sorted(EXPECTED_CHANGED_PATHS)
    authorized = sorted(EXPECTED_ALLOWLIST)
    modes = {
        relative: git(root, "ls-tree", "HEAD", "--", relative).split(" ", 1)[0]
        for relative in authorized
    }
    artifacts = {
        relative: hashlib.sha256((root / relative).read_bytes()).hexdigest()
        for relative in validator.EXPECTED_ARTIFACT_PATHS
    }
    return {
        "schema_version": 2,
        "repository": {
            "identity": "nvkhoabk/ysim",
            "origin": "git@github-ysim:nvkhoabk/ysim.git",
            "branch": EXPECTED_BRANCH,
        },
        "topology": {
            "base_sha": EXPECTED_BASE_SHA,
            "base_tree": validator.EXPECTED_BASE_TREE,
            "corrective_parent_sha": EXPECTED_CORRECTIVE_PARENT_SHA,
            "corrective_parent_tree": EXPECTED_CORRECTIVE_PARENT_TREE,
            "expected_head_sha": git(root, "rev-parse", "HEAD"),
            "expected_head_tree": git(root, "rev-parse", "HEAD^{tree}"),
            "base_to_head_commit_count": 6,
            "parent_to_head_commit_count": 1,
        },
        "changed_paths": paths,
        "authorized_paths": authorized,
        "file_modes": modes,
        "artifact_digests": artifacts,
        "validation_boundaries": {
            "knowledge_input": copy.deepcopy(validator.EXPECTED_KNOWLEDGE_BOUNDARY),
            "branch_coverage": copy.deepcopy(validator.EXPECTED_BRANCH_COVERAGE_BOUNDARY),
            "stable_read": copy.deepcopy(validator.EXPECTED_STABLE_READ_BOUNDARY),
        },
    }


def api_workspace(tmp_path: Path) -> tuple[Path, dict[str, Any]]:
    tmp_path.mkdir(parents=True, exist_ok=True)
    root = tmp_path / "repository"
    git(tmp_path, "clone", "--quiet", "--no-hardlinks", str(repository_root()), str(root))
    git(root, "switch", "--quiet", "--detach", EXPECTED_CORRECTIVE_PARENT_SHA)
    if (
        subprocess.run(
            ["git", "-C", str(root), "show-ref", "--verify", f"refs/heads/{EXPECTED_BRANCH}"],
            check=False,
            capture_output=True,
        ).returncode
        == 0
    ):
        git(root, "branch", "-D", EXPECTED_BRANCH)
    git(root, "switch", "--quiet", "-c", EXPECTED_BRANCH)
    copy_package(root)
    git(root, "add", "--", *sorted(EXPECTED_ALLOWLIST))
    assert set(git(root, "diff", "--cached", "--name-only").splitlines()) == set(R5_WRITE_SUBSET)
    commit(root, "test: materialize exact S03 corrective R5 source", 1)
    git(root, "remote", "set-url", "origin", "git@github-ysim:nvkhoabk/ysim.git")
    assert git(root, "rev-parse", "HEAD^") == EXPECTED_CORRECTIVE_PARENT_SHA
    assert git(root, "rev-parse", "HEAD^^{tree}") == EXPECTED_CORRECTIVE_PARENT_TREE
    assert int(git(root, "rev-list", "--count", f"{EXPECTED_BASE_SHA}..HEAD")) == 6
    assert int(git(root, "rev-list", "--count", f"{EXPECTED_CORRECTIVE_PARENT_SHA}..HEAD")) == 1
    assert not git(root, "status", "--porcelain=v1", "--untracked-files=all")
    assert set(git(root, "diff", "--name-only", f"{EXPECTED_BASE_SHA}...HEAD").splitlines()) == set(
        EXPECTED_CHANGED_PATHS
    )
    return root, snapshot_contract(root)


def refresh_identity(root: Path, contract: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(contract)
    result["topology"]["expected_head_sha"] = git(root, "rev-parse", "HEAD")
    result["topology"]["expected_head_tree"] = git(root, "rev-parse", "HEAD^{tree}")
    return result


def write_contract(path: Path, contract: dict[str, Any]) -> None:
    path.write_text(yaml.safe_dump(contract, sort_keys=False), encoding="utf-8")


def assert_failure(root: Path, contract: dict[str, Any], code: str) -> None:
    reached = False
    try:
        validate_configuration_access_control(root, contract)
    except FactoryFailure as failure:
        reached = True
        assert failure.code == code
    assert reached, "negative probe did not reach its intended assertion"


def load(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def write(path: Path, value: dict[str, Any]) -> None:
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")


def test_exact_content_package_passes(tmp_path: Path) -> None:
    root = accepted_s03_workspace(tmp_path)
    assert validator._validate_package(root)["result"] == "PASS"
    assert validator._validate_provenance(root)["result"] == "PASS"
    assert validator._validate_baseline(root)["requirement_count"] == 5
    assert validator._validate_manifest(root)["result"] == "PASS"
    validator._validate_documents(root)


@pytest.mark.parametrize(
    ("path", "key", "value", "code", "call"),
    [
        (validator.SPEC_PATH, "maturity_target", "IMPLEMENTED", "FAIL_PACKAGE_SPEC", "package"),
        (validator.SPEC_PATH, "candidate_model", "RAW", "FAIL_PACKAGE_SPEC", "package"),
        (validator.SPEC_PATH, "unexpected", True, "FAIL_PACKAGE_SPEC", "package"),
        (validator.PROVENANCE_PATH, "unexpected", True, "FAIL_SOURCE_PROVENANCE", "provenance"),
        (validator.BASELINE_PATH, "status", "OPERATIONAL", "FAIL_S03_BASELINE", "baseline"),
        (validator.BASELINE_PATH, "candidate_model", "RAW", "FAIL_S03_BASELINE", "baseline"),
    ],
)
def test_package_baseline_and_provenance_fail_closed(
    tmp_path: Path, path: str, key: str, value: object, code: str, call: str
) -> None:
    root = content_workspace(tmp_path)
    target = root / path
    document = load(target)
    document[key] = value
    write(target, document)
    selected = {
        "package": validator._validate_package,
        "provenance": validator._validate_provenance,
        "baseline": validator._validate_baseline,
    }[call]
    with pytest.raises(FactoryFailure) as captured:
        selected(root)
    assert captured.value.code == code


def test_requirement_statement_and_provenance_blob_mutations_fail_closed(tmp_path: Path) -> None:
    root = content_workspace(tmp_path / "requirement")
    baseline = load(root / validator.BASELINE_PATH)
    baseline["requirements"][0]["statement"] = "broadened"
    write(root / validator.BASELINE_PATH, baseline)
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_baseline(root)
    assert captured.value.code == "FAIL_S03_REQUIREMENTS"

    root = content_workspace(tmp_path / "provenance")
    provenance = load(root / validator.PROVENANCE_PATH)
    provenance["brd_sources"][0]["git_blob_sha"] = "0" * 40
    write(root / validator.PROVENANCE_PATH, provenance)
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_provenance(root)
    assert captured.value.code == "FAIL_SOURCE_PROVENANCE"

    root = content_workspace(tmp_path / "corrective-r2")
    provenance = load(root / validator.PROVENANCE_PATH)
    provenance["corrective_r2"]["knowledge_input"]["service"]["sha256"] = "0" * 64
    write(root / validator.PROVENANCE_PATH, provenance)
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_provenance(root)
    assert captured.value.code == "FAIL_SOURCE_PROVENANCE"


def test_package_fresh_knowledge_and_branch_metric_bindings_fail_closed(tmp_path: Path) -> None:
    mutations = (
        ("branch_coverage", "minimum_percent", 89.0),
        ("branch_coverage", "metric", "AGGREGATE_COVERAGE"),
        ("branch_coverage", "source_package", "ysf"),
        ("knowledge_input", "tracked_factory_index_allowed", True),
        ("knowledge_input", "source", "TRACKED_FACTORY_INDEX"),
        ("knowledge_input", "builder", "other.builder"),
        ("knowledge_input", "source_glob", "factory/index/documents.json"),
        ("knowledge_input", "expected_integration_count", 1),
    )
    for gate, field, value in mutations:
        root = content_workspace(tmp_path / f"{gate}-{field}")
        package = load(root / validator.SPEC_PATH)
        package["validation_gates"][gate][field] = value
        write(root / validator.SPEC_PATH, package)
        with pytest.raises(FactoryFailure) as captured:
            validator._validate_package(root)
        assert captured.value.code == "FAIL_PACKAGE_SPEC"


@pytest.mark.parametrize("kind", ["malformed", "missing", "duplicate", "digest", "unsafe"])
def test_manifest_negative_matrix(tmp_path: Path, kind: str) -> None:
    root = content_workspace(tmp_path)
    manifest = root / validator.MANIFEST_PATH
    lines = manifest.read_text(encoding="utf-8").splitlines()
    if kind == "malformed":
        lines.append("malformed")
    elif kind == "missing":
        lines.pop()
    elif kind == "duplicate":
        lines.append(lines[0])
    elif kind == "digest":
        lines[0] = "0" * 64 + "  " + lines[0].split("  ", 1)[1]
    else:
        lines[0] = lines[0].split("  ", 1)[0] + "  ../outside"
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_manifest(root)
    assert captured.value.code == "FAIL_PACKAGE_MANIFEST"


def test_public_api_cli_parity_and_two_disposable_roots(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    first, first_contract = api_workspace(tmp_path / "first")
    second, second_contract = api_workspace(tmp_path / "second")
    assert tuple(inspect.signature(validate_configuration_access_control).parameters) == (
        "repository_root",
        "snapshot_contract",
    )
    assert git(first, "rev-parse", "HEAD") == git(second, "rev-parse", "HEAD")
    assert first_contract == second_contract
    first_output = validate_configuration_access_control(first, first_contract)
    second_output = validate_configuration_access_control(second, second_contract)
    assert first_output == second_output
    contract_path = tmp_path / "snapshot.yaml"
    write_contract(contract_path, first_contract)
    assert (
        main(
            [
                "--repository-root",
                str(first),
                "--snapshot-contract",
                str(contract_path),
                "--json",
            ]
        )
        == 0
    )
    cli = capsys.readouterr().out
    assert cli.encode() == (json.dumps(first_output, sort_keys=True) + "\n").encode()
    with pytest.raises(SystemExit) as captured:
        main(["--repository-root", str(first)])
    assert captured.value.code == 2


@pytest.mark.parametrize(
    ("mutation", "code"),
    [
        (lambda value: value.pop("topology"), "FAIL_SNAPSHOT_CONTRACT"),
        (lambda value: value.update({"extra": True}), "FAIL_SNAPSHOT_CONTRACT"),
        (lambda value: value.update({"schema_version": 1}), "FAIL_SNAPSHOT_CONTRACT"),
        (lambda value: value.update({"repository": []}), "FAIL_SNAPSHOT_CONTRACT"),
        (lambda value: value["repository"].pop("branch"), "FAIL_SNAPSHOT_CONTRACT"),
        (
            lambda value: value["repository"].update({"unexpected": True}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["repository"].update({"identity": "other/repo"}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (lambda value: value["topology"].update({"base_sha": "0" * 40}), "FAIL_SNAPSHOT_CONTRACT"),
        (lambda value: value["topology"].update({"base_tree": "0" * 40}), "FAIL_SNAPSHOT_CONTRACT"),
        (
            lambda value: value["topology"].update({"expected_head_sha": "0" * 40}),
            "FAIL_HEAD_IDENTITY",
        ),
        (
            lambda value: value["topology"].update({"expected_head_tree": "0" * 40}),
            "FAIL_HEAD_TREE",
        ),
        (
            lambda value: value["topology"].update({"base_to_head_commit_count": 2}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["topology"].update({"parent_to_head_commit_count": "1"}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["topology"].update({"corrective_parent_sha": "0" * 40}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["topology"].update({"corrective_parent_tree": "0" * 40}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (lambda value: value["changed_paths"].append("unexpected"), "FAIL_SNAPSHOT_CONTRACT"),
        (
            lambda value: value["changed_paths"].append(value["changed_paths"][0]),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (lambda value: value["changed_paths"].reverse(), "FAIL_SNAPSHOT_CONTRACT"),
        (
            lambda value: value["changed_paths"].__setitem__(0, "../unsafe"),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["authorized_paths"].remove(
                "tools/ysf/tests/integration/test_secure_factory_pipeline.py"
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["authorized_paths"].append("fabricated/path.py"),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["authorized_paths"].append(value["authorized_paths"][0]),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (lambda value: value["authorized_paths"].reverse(), "FAIL_SNAPSHOT_CONTRACT"),
        (
            lambda value: value["authorized_paths"].__setitem__(0, "../unsafe"),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["file_modes"].pop(
                "tools/ysf/tests/integration/test_secure_factory_pipeline.py"
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["file_modes"].update({"fabricated/path.py": "100644"}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["file_modes"].update({validator.README_PATH: "100755"}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["file_modes"].update(
                {"tools/ysf/tests/integration/test_secure_factory_pipeline.py": "100755"}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["artifact_digests"].pop(validator.SPEC_PATH),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["artifact_digests"].update({"unexpected": "0" * 64}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["artifact_digests"].update({validator.SPEC_PATH: "wrong"}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["artifact_digests"].update({validator.SPEC_PATH: "0" * 64}),
            "FAIL_SNAPSHOT_ARTIFACT",
        ),
        (
            lambda value: value["artifact_digests"].update({validator.MANIFEST_PATH: "0" * 64}),
            "FAIL_SNAPSHOT_ARTIFACT",
        ),
        (
            lambda value: value["artifact_digests"].update({validator.PROVENANCE_PATH: "0" * 64}),
            "FAIL_SNAPSHOT_ARTIFACT",
        ),
        (
            lambda value: value["validation_boundaries"].pop("knowledge_input"),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"].update({"unexpected": {}}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"].update({"knowledge_input": []}),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["knowledge_input"].update(
                {"tracked_factory_index_allowed": True}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["knowledge_input"].update(
                {"source": "TRACKED_FACTORY_INDEX"}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["knowledge_input"].update(
                {"builder": "other.builder"}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["knowledge_input"].update(
                {"source_glob": "factory/index/documents.json"}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["knowledge_input"].update(
                {"expected_document_count": 123}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["knowledge_input"].pop(
                "expected_relationship_count"
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["knowledge_input"].update(
                {"unexpected": 1}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["knowledge_input"].update(
                {"expected_integration_count": "0"}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["branch_coverage"].update(
                {"metric": "AGGREGATE_COVERAGE"}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["branch_coverage"].update(
                {"metric": "LINE_COVERAGE"}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["branch_coverage"].update(
                {"source_package": "ysf"}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["branch_coverage"].update(
                {"minimum_percent": 89.0}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["branch_coverage"].update(
                {"minimum_percent": "90.0"}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["branch_coverage"].pop("source_package"),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["branch_coverage"].update(
                {"unexpected": True}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"].pop("stable_read"),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["stable_read"].update(
                {"empty_parts_rejected": False}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["stable_read"].update(
                {"raw_exception_escape_allowed": True}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
        (
            lambda value: value["validation_boundaries"]["stable_read"].update(
                {"minimum_descriptor_cycles": 64}
            ),
            "FAIL_SNAPSHOT_CONTRACT",
        ),
    ],
)
def test_snapshot_contract_negative_matrix(
    tmp_path: Path,
    mutation: Callable[[dict[str, Any]], Any],
    code: str,
) -> None:
    root, contract = api_workspace(tmp_path)
    mutation(contract)
    assert_failure(root, contract, code)


@pytest.mark.parametrize(
    "artifact_path",
    [validator.SPEC_PATH, validator.MANIFEST_PATH, validator.PROVENANCE_PATH],
)
def test_actual_artifact_bytes_must_match_external_digest(
    tmp_path: Path, artifact_path: str
) -> None:
    root, contract = api_workspace(tmp_path)
    target = root / artifact_path
    target.write_bytes(target.read_bytes() + b"\n")
    git(root, "add", "--", artifact_path)
    commit(root, "test: mutate tracked artifact bytes", 2, amend=True)
    assert_failure(root, refresh_identity(root, contract), "FAIL_SNAPSHOT_ARTIFACT")


def test_artifact_replacement_after_capture_fails_final_snapshot_readback(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, contract = api_workspace(tmp_path)
    original = validator._validate_snapshot_artifact_digests
    target = root / validator.SPEC_PATH

    def replace_after_capture(
        observed_root: Path,
        observed_contract: Any,
        snapshot: Any,
    ) -> dict[str, str]:
        target.write_bytes(target.read_bytes() + b"\n")
        return original(observed_root, observed_contract, snapshot)

    monkeypatch.setattr(validator, "_validate_snapshot_artifact_digests", replace_after_capture)
    assert_failure(root, contract, "FAIL_DIRTY_WORKTREE")


def test_contract_boundary_cannot_be_made_consistent_with_mutated_package_or_provenance(
    tmp_path: Path,
) -> None:
    root, contract = api_workspace(tmp_path / "package")
    package = load(root / validator.SPEC_PATH)
    package["validation_gates"]["branch_coverage"]["minimum_percent"] = 89.0
    write(root / validator.SPEC_PATH, package)
    git(root, "add", "--", validator.SPEC_PATH)
    commit(root, "test: weaken package boundary", 2, amend=True)
    contract = refresh_identity(root, contract)
    contract["artifact_digests"][validator.SPEC_PATH] = hashlib.sha256(
        (root / validator.SPEC_PATH).read_bytes()
    ).hexdigest()
    contract["validation_boundaries"]["branch_coverage"]["minimum_percent"] = 89.0
    assert_failure(root, contract, "FAIL_SNAPSHOT_CONTRACT")

    root, contract = api_workspace(tmp_path / "provenance")
    provenance = load(root / validator.PROVENANCE_PATH)
    provenance["corrective_r3"]["external_snapshot_contract"]["knowledge_input"][
        "tracked_factory_index_allowed"
    ] = True
    write(root / validator.PROVENANCE_PATH, provenance)
    git(root, "add", "--", validator.PROVENANCE_PATH)
    commit(root, "test: weaken provenance boundary", 2, amend=True)
    contract = refresh_identity(root, contract)
    contract["artifact_digests"][validator.PROVENANCE_PATH] = hashlib.sha256(
        (root / validator.PROVENANCE_PATH).read_bytes()
    ).hexdigest()
    assert_failure(root, contract, "FAIL_SOURCE_PROVENANCE")


def test_root_contract_missing_malformed_and_symlink_fail_closed(tmp_path: Path) -> None:
    root, contract = api_workspace(tmp_path / "repo")
    assert_failure(Path("relative"), contract, "FAIL_REPOSITORY_ROOT")
    link = tmp_path / "link"
    link.symlink_to(root, target_is_directory=True)
    assert_failure(link, contract, "FAIL_REPOSITORY_ROOT")
    assert_failure(root / "docs", contract, "FAIL_REPOSITORY_IDENTITY")
    actual = tmp_path / "actual.yaml"
    write_contract(actual, contract)
    linked_contract = tmp_path / "linked.yaml"
    linked_contract.symlink_to(actual)
    with pytest.raises(FactoryFailure) as captured:
        load_snapshot_contract(linked_contract)
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"
    contract_directory = tmp_path / "contract-directory"
    contract_directory.mkdir()
    nested_contract = contract_directory / "snapshot.yaml"
    write_contract(nested_contract, contract)
    linked_directory = tmp_path / "linked-directory"
    linked_directory.symlink_to(contract_directory, target_is_directory=True)
    with pytest.raises(FactoryFailure) as captured:
        load_snapshot_contract(linked_directory / "snapshot.yaml")
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"
    non_directory_parent = tmp_path / "not-a-directory"
    non_directory_parent.write_text("synthetic", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        load_snapshot_contract(non_directory_parent / "snapshot.yaml")
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"
    directory_contract = tmp_path / "directory-contract"
    directory_contract.mkdir()
    with pytest.raises(FactoryFailure) as captured:
        load_snapshot_contract(directory_contract)
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"
    malformed = tmp_path / "malformed.yaml"
    malformed.write_text("[invalid", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        load_snapshot_contract(malformed)
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"
    with pytest.raises(FactoryFailure) as captured:
        load_snapshot_contract(tmp_path / "missing.yaml")
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"


def test_stable_descriptor_reader_rejects_final_and_parent_replacement(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "stable-root"
    parent = root / "parent"
    parent.mkdir(parents=True)
    target = parent / "target.yaml"
    target.write_bytes(b"value: original\n")
    root_descriptor = validator._open_absolute_directory(root, "FAIL_TEST")
    original_reader = validator._read_descriptor_bytes

    def replace_final(descriptor: int) -> bytes:
        target.rename(parent / "original.yaml")
        target.write_bytes(b"value: replacement\n")
        return original_reader(descriptor)

    monkeypatch.setattr(validator, "_read_descriptor_bytes", replace_final)
    with pytest.raises(FactoryFailure) as captured:
        validator._stable_read_relative(root_descriptor, "parent/target.yaml", "FAIL_STABLE")
    assert captured.value.code == "FAIL_STABLE"
    os.close(root_descriptor)

    root = tmp_path / "parent-root"
    parent = root / "parent"
    parent.mkdir(parents=True)
    target = parent / "target.yaml"
    target.write_bytes(b"value: original\n")
    root_descriptor = validator._open_absolute_directory(root, "FAIL_TEST")

    def replace_parent(descriptor: int) -> bytes:
        parent.rename(root / "original-parent")
        parent.mkdir()
        (parent / "target.yaml").write_bytes(b"value: replacement\n")
        return original_reader(descriptor)

    monkeypatch.setattr(validator, "_read_descriptor_bytes", replace_parent)
    with pytest.raises(FactoryFailure) as captured:
        validator._stable_read_relative(root_descriptor, "parent/target.yaml", "FAIL_STABLE")
    assert captured.value.code == "FAIL_STABLE"
    os.close(root_descriptor)


def test_stable_descriptor_reader_rejects_in_read_mutation_and_contract_replacement(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    target = tmp_path / "mutable.bin"
    target.write_bytes(b"a" * 4096)
    root_descriptor = validator._open_absolute_directory(tmp_path, "FAIL_TEST")
    original_reader = validator._read_descriptor_bytes

    def truncate_during_read(descriptor: int) -> bytes:
        target.write_bytes(b"changed")
        return original_reader(descriptor)

    monkeypatch.setattr(validator, "_read_descriptor_bytes", truncate_during_read)
    with pytest.raises(FactoryFailure) as captured:
        validator._stable_read_relative(root_descriptor, target.name, "FAIL_STABLE")
    assert captured.value.code == "FAIL_STABLE"
    os.close(root_descriptor)

    contract = tmp_path / "contract.yaml"
    contract.write_text("schema_version: 2\n", encoding="utf-8")

    def replace_contract(descriptor: int) -> bytes:
        contract.rename(tmp_path / "contract-original.yaml")
        contract.write_text("schema_version: 1\n", encoding="utf-8")
        return original_reader(descriptor)

    monkeypatch.setattr(validator, "_read_descriptor_bytes", replace_contract)
    with pytest.raises(FactoryFailure) as captured:
        load_snapshot_contract(contract)
    assert captured.value.code == "FAIL_SNAPSHOT_CONTRACT"


@pytest.mark.parametrize(
    "relative",
    [
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
    ],
)
def test_stable_reader_rejects_malformed_aliases_with_controlled_failure(
    tmp_path: Path, relative: str
) -> None:
    root_descriptor = validator._open_absolute_directory(tmp_path, "FAIL_TEST")
    before = len(tuple(Path("/proc/self/fd").iterdir()))
    try:
        for _ in range(500):
            with pytest.raises(FactoryFailure) as captured:
                validator._stable_read_relative(root_descriptor, relative, "FAIL_ALIAS_PATH")
            assert captured.value.code == "FAIL_ALIAS_PATH"
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
    for _ in range(500):
        assert (
            validator._stable_read_relative(root_descriptor, "target", "FAIL_STABLE") == b"stable"
        )
        with pytest.raises(FactoryFailure) as captured:
            validator._stable_read_relative(root_descriptor, "linked", "FAIL_STABLE")
        assert captured.value.code == "FAIL_STABLE"
    after = len(tuple(Path("/proc/self/fd").iterdir()))
    os.close(root_descriptor)
    assert after == before


def test_stable_reader_requires_linux_and_head_blob_equality(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(validator.platform, "system", lambda: "Other")
    with pytest.raises(FactoryFailure) as captured:
        validator._open_absolute_directory(tmp_path, "FAIL_TEST")
    assert captured.value.code == "FAIL_ENVIRONMENT_IDENTITY"
    monkeypatch.setattr(validator.platform, "system", lambda: "Linux")

    root, _ = api_workspace(tmp_path / "blob")
    target = root / validator.README_PATH
    target.write_bytes(target.read_bytes() + b"\n")
    with validator._ValidationSnapshot(root) as snapshot:
        with pytest.raises(FactoryFailure) as captured:
            snapshot.read(validator.README_PATH)
    assert captured.value.code == "FAIL_WORKTREE_BLOB"


def test_contract_mapping_is_frozen_before_repository_validation(tmp_path: Path) -> None:
    root, contract = api_workspace(tmp_path)

    class MutatingContract(dict[str, Any]):
        def items(self) -> Any:
            captured_items = tuple(super().items())
            self.clear()
            self["fabricated_after_capture"] = True
            return captured_items

    supplied = MutatingContract(contract)
    result = validate_configuration_access_control(root, supplied)
    assert result["result"] == "PASS"
    assert supplied == {"fabricated_after_capture": True}


def test_sensitive_scan_reuses_captured_bytes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, _ = api_workspace(tmp_path)
    with validator._ValidationSnapshot(root) as snapshot:
        snapshot.capture_all(sorted(EXPECTED_ALLOWLIST))

        def unexpected_reopen(*_args: object, **_kwargs: object) -> bytes:
            raise AssertionError("sensitive scan reopened a captured pathname")

        monkeypatch.setattr(validator, "_stable_read_relative", unexpected_reopen)
        assert validator._scan_snapshot(snapshot, set(EXPECTED_CHANGED_PATHS)) == "PASS"


def test_trusted_validation_source_has_no_path_content_reopen() -> None:
    source = inspect.getsource(validator)
    assert ".read_text(" not in source
    assert ".read_bytes(" not in source
    assert "require_no_sensitive_values" not in source
    assert "scan_bytes(snapshot.read(relative)" in source


@pytest.mark.parametrize(
    ("kind", "expected_code"),
    [
        ("tracked-data-file", "FAIL_COVERAGE_ISOLATION"),
        ("missing-ignore", "FAIL_COVERAGE_ISOLATION"),
        ("broad-ignore", "FAIL_COVERAGE_ISOLATION"),
        ("branch-disabled", "FAIL_COVERAGE_ISOLATION"),
        ("source-weakened", "FAIL_COVERAGE_ISOLATION"),
        ("threshold-weakened", "FAIL_COVERAGE_ISOLATION"),
    ],
)
def test_coverage_state_isolation_negative_matrix(
    tmp_path: Path, kind: str, expected_code: str
) -> None:
    root = content_workspace(tmp_path)
    pyproject_path = root / "tools/ysf/pyproject.toml"
    gitignore_path = root / ".gitignore"
    if kind in {"missing-ignore", "broad-ignore"}:
        lines = gitignore_path.read_text(encoding="utf-8").splitlines()
        lines = [line for line in lines if line != "/tools/ysf/.coverage.runtime.*"]
        if kind == "broad-ignore":
            lines.append("/tools/ysf/.coverage*")
        gitignore_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    else:
        text = pyproject_path.read_text(encoding="utf-8")
        replacements = {
            "tracked-data-file": ('data_file = ".coverage.runtime"', 'data_file = ".coverage"'),
            "branch-disabled": ("branch = true", "branch = false"),
            "source-weakened": ('source = ["ysf"]', 'source = ["other"]'),
            "threshold-weakened": ("fail_under = 90", "fail_under = 89"),
        }
        old, new = replacements[kind]
        pyproject_path.write_text(text.replace(old, new), encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_coverage_isolation(root)
    assert captured.value.code == expected_code


def test_coverage_state_isolation_configuration_is_exact() -> None:
    root = repository_root()
    result = validator._validate_coverage_isolation(root)
    assert result == {
        "result": "PASS",
        "data_file": ".coverage.runtime",
        "environment_override_required": False,
        "tracked_coverage_mutation_allowed": False,
    }
    configuration = tomllib.loads((root / "tools/ysf/pyproject.toml").read_text(encoding="utf-8"))
    assert configuration["tool"]["coverage"]["run"] == {
        "branch": True,
        "source": ["ysf"],
        "data_file": ".coverage.runtime",
    }


def test_dirty_origin_branch_and_sensitive_fail_closed(tmp_path: Path) -> None:
    root, contract = api_workspace(tmp_path / "dirty")
    (root / "dirty.txt").write_text("dirty", encoding="utf-8")
    assert_failure(root, contract, "FAIL_DIRTY_WORKTREE")

    root, contract = api_workspace(tmp_path / "origin")
    git(root, "remote", "set-url", "origin", "https://github.com/other/repository.git")
    assert_failure(root, contract, "FAIL_REPOSITORY_IDENTITY")

    root, contract = api_workspace(tmp_path / "branch")
    git(root, "branch", "-m", "wrong-branch")
    assert_failure(root, contract, "FAIL_REPOSITORY_IDENTITY")

    root, contract = api_workspace(tmp_path / "sensitive")
    readme = root / validator.README_PATH
    prohibited = "api_" + "key=" + "abcdefghijklmnop"
    readme.write_text(readme.read_text(encoding="utf-8") + prohibited, encoding="utf-8")
    git(root, "add", "--", validator.README_PATH)
    commit(root, "test: sensitive delta", 2, amend=True)
    assert_failure(root, refresh_identity(root, contract), "FAIL_SENSITIVE_VALUE")


def test_unexpected_mode_symlink_replacement_and_extra_commit_fail_closed(
    tmp_path: Path,
) -> None:
    root, contract = api_workspace(tmp_path / "unexpected")
    (root / "unexpected.txt").write_text("unexpected", encoding="utf-8")
    git(root, "add", "unexpected.txt")
    commit(root, "test: unexpected path", 2, amend=True)
    assert_failure(root, refresh_identity(root, contract), "FAIL_FILE_ALLOWLIST")

    root, contract = api_workspace(tmp_path / "mode")
    (root / validator.README_PATH).chmod(0o755)
    git(root, "add", validator.README_PATH)
    commit(root, "test: mode drift", 2, amend=True)
    assert_failure(root, refresh_identity(root, contract), "FAIL_FILE_MODE")

    root, contract = api_workspace(tmp_path / "unchanged-integration-mode")
    integration = root / "tools/ysf/tests/integration/test_secure_factory_pipeline.py"
    integration.chmod(0o755)
    git(root, "add", str(integration.relative_to(root)))
    commit(root, "test: unchanged bound mode drift", 2, amend=True)
    assert_failure(root, refresh_identity(root, contract), "FAIL_FILE_MODE")

    root, contract = api_workspace(tmp_path / "symlink")
    readme = root / validator.README_PATH
    readme.unlink()
    readme.symlink_to(root / validator.SPEC_PATH)
    git(root, "add", validator.README_PATH)
    commit(root, "test: symlink drift", 2, amend=True)
    assert_failure(root, refresh_identity(root, contract), "FAIL_PATH_SAFETY")

    root, contract = api_workspace(tmp_path / "artifact-symlink")
    package = root / validator.SPEC_PATH
    package.unlink()
    package.symlink_to(root / validator.PROVENANCE_PATH)
    git(root, "add", validator.SPEC_PATH)
    commit(root, "test: artifact symlink", 2, amend=True)
    assert_failure(root, refresh_identity(root, contract), "FAIL_PATH_SAFETY")

    root, contract = api_workspace(tmp_path / "gitlink")
    readme = root / validator.README_PATH
    readme.unlink()
    readme.mkdir()
    git(
        root,
        "update-index",
        "--add",
        "--cacheinfo",
        f"160000,{EXPECTED_CORRECTIVE_PARENT_SHA},{validator.README_PATH}",
    )
    commit(root, "test: gitlink drift", 2, amend=True)
    assert_failure(root, refresh_identity(root, contract), "FAIL_PATH_SAFETY")

    root, contract = api_workspace(tmp_path / "replacement")
    readme = root / validator.README_PATH
    readme.write_text(readme.read_text(encoding="utf-8") + "\nsource change\n", encoding="utf-8")
    git(root, "add", validator.README_PATH)
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=YSim S03 Test",
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
    assert_failure(root, contract, "FAIL_HEAD_IDENTITY")

    root, contract = api_workspace(tmp_path / "extra")
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=YSim S03 Test",
            "-c",
            f"user.email={synthetic_git_email()}",
            "commit",
            "--quiet",
            "--allow-empty",
            "-m",
            "test: extra head",
        ],
        check=True,
        capture_output=True,
    )
    assert_failure(root, contract, "FAIL_HEAD_IDENTITY")


def test_plain_cli_failure_uses_same_boundary(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    root, contract = api_workspace(tmp_path)
    contract["topology"]["expected_head_sha"] = "0" * 40
    contract_path = tmp_path / "snapshot.yaml"
    write_contract(contract_path, contract)
    assert main(["--repository-root", str(root), "--snapshot-contract", str(contract_path)]) == 1
    payload = json.loads(capsys.readouterr().out)
    assert payload["code"] == "FAIL_HEAD_IDENTITY"
    assert payload["result"] == "FAIL"


def test_defensive_helpers_fail_closed(tmp_path: Path) -> None:
    with pytest.raises(FactoryFailure) as captured:
        validator._mapping([], "FAIL_TYPE", "mapping")
    assert captured.value.code == "FAIL_TYPE"
    with pytest.raises(FactoryFailure) as captured:
        validator._sequence("text", "FAIL_TYPE", "sequence")
    assert captured.value.code == "FAIL_TYPE"
    with pytest.raises(FactoryFailure) as captured:
        validator._load_yaml(tmp_path / "missing.yaml", "FAIL_YAML")
    assert captured.value.code == "FAIL_YAML"
    with pytest.raises(FactoryFailure) as captured:
        validator._run_git(tmp_path, "rev-parse", "HEAD")
    assert captured.value.code == "FAIL_REPOSITORY_IDENTITY"
    with pytest.raises(FactoryFailure) as captured:
        validator._git_file_sha256(tmp_path, "missing", "path")
    assert captured.value.code == "FAIL_SOURCE_PROVENANCE"
    with pytest.raises(FactoryFailure) as captured:
        validator._safe_relative_parts("", "FAIL_PATH")
    assert captured.value.code == "FAIL_PATH"
    with pytest.raises(FactoryFailure) as captured:
        validator._open_absolute_directory(Path("relative"), "FAIL_PATH")
    assert captured.value.code == "FAIL_PATH"
    with pytest.raises(FactoryFailure) as captured:
        validator._stable_read_absolute(Path("relative"), "FAIL_PATH")
    assert captured.value.code == "FAIL_PATH"
    with pytest.raises(FactoryFailure) as captured:
        validator._git_file_bytes(tmp_path, "missing", "path", "FAIL_GIT_BYTES")
    assert captured.value.code == "FAIL_GIT_BYTES"
    with pytest.raises(FactoryFailure) as captured:
        validator._load_yaml_bytes(b"\xff", "FAIL_YAML", "invalid")
    assert captured.value.code == "FAIL_YAML"
    invalid_toml_root = content_workspace(tmp_path / "invalid-toml")
    (invalid_toml_root / "tools/ysf/pyproject.toml").write_bytes(b"[invalid")
    with pytest.raises(FactoryFailure) as captured:
        validator._validate_coverage_isolation(invalid_toml_root)
    assert captured.value.code == "FAIL_COVERAGE_ISOLATION"
    assert hashlib.sha256(b"safe").hexdigest() != "0" * 64
