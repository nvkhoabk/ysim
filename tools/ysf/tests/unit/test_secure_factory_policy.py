from __future__ import annotations

from pathlib import Path
from subprocess import CompletedProcess

import pytest

from ysf.secure_factory.models import FactoryFailure
from ysf.secure_factory.policy import (
    EXACT_ALLOWLIST,
    changed_paths,
    mutation_paths,
    parse_porcelain_z,
    require_regular_files,
    validate_approval_and_ruleset,
    validate_changed_paths,
    validate_external_effect_policy,
    validate_relative_path,
    verify_policy_self_protection,
)


def test_porcelain_parser_handles_untracked_and_rename() -> None:
    records = parse_porcelain_z(b"?? AGENTS.md\0R  new.txt\0old.txt\0")
    assert records == {"AGENTS.md", "new.txt", "old.txt"}


@pytest.mark.parametrize("path", ["../escape", "/absolute", "a/../b", "a\\b", ""])
def test_unsafe_path_is_rejected(path: str) -> None:
    with pytest.raises(FactoryFailure):
        validate_relative_path(path)


def test_unapproved_path_is_rejected(tmp_path: Path) -> None:
    with pytest.raises(FactoryFailure) as captured:
        validate_changed_paths(tmp_path, {"not-approved.txt"})
    assert captured.value.code == "FAIL_UNAPPROVED_PATH"


def test_exact_stage_scope_is_required(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text("safe", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        validate_changed_paths(
            tmp_path, {"AGENTS.md"}, expected={"AGENTS.md", "scripts/v3-r1-s00.sh"}
        )
    assert captured.value.details["missing"] == ["scripts/v3-r1-s00.sh"]


def test_symlink_changed_path_is_rejected(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.write_text("safe", encoding="utf-8")
    (tmp_path / "AGENTS.md").symlink_to(target)
    with pytest.raises(FactoryFailure) as captured:
        validate_changed_paths(tmp_path, {"AGENTS.md"})
    assert captured.value.code == "FAIL_SYMLINK_PATH"


def test_policy_source_and_executable_allowlists_match(tmp_path: Path) -> None:
    policy = tmp_path / "policy.md"
    policy.write_text(
        "## Exact allowlist\n\n```text\n" + "\n".join(EXACT_ALLOWLIST) + "\n```\n",
        encoding="utf-8",
    )
    assert verify_policy_self_protection(policy).passed
    policy.write_text("## Exact allowlist\n\n```text\nAGENTS.md\n```\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        verify_policy_self_protection(policy)
    assert captured.value.code == "FAIL_POLICY_SELF_CHECK"


def test_git_status_and_branch_diff_paths(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    calls = iter(
        [
            CompletedProcess([], 0, b"AGENTS.md\0", b""),
            CompletedProcess([], 0, b"?? scripts/v3-r1-s00.sh\0", b""),
        ]
    )
    monkeypatch.setattr(
        "ysf.secure_factory.policy.subprocess.run", lambda *args, **kwargs: next(calls)
    )
    assert mutation_paths(tmp_path) == {"AGENTS.md", "scripts/v3-r1-s00.sh"}

    monkeypatch.setattr(
        "ysf.secure_factory.policy.subprocess.run",
        lambda *args, **kwargs: CompletedProcess([], 5, b"", b""),
    )
    with pytest.raises(FactoryFailure) as captured:
        changed_paths(tmp_path)
    assert captured.value.code == "FAIL_GIT_STATUS"
    with pytest.raises(FactoryFailure) as captured:
        mutation_paths(tmp_path)
    assert captured.value.code == "FAIL_GIT_DIFF"


def test_porcelain_and_policy_format_errors(tmp_path: Path) -> None:
    for payload in (b"bad\0", b"R  new.txt\0"):
        with pytest.raises(FactoryFailure) as captured:
            parse_porcelain_z(payload)
        assert captured.value.code == "FAIL_GIT_STATUS_FORMAT"
    policy = tmp_path / "policy.md"
    policy.write_text("# missing allowlist\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        verify_policy_self_protection(policy)
    assert captured.value.code == "FAIL_POLICY_SELF_CHECK"


def test_regular_file_requirement(tmp_path: Path) -> None:
    regular = tmp_path / "AGENTS.md"
    regular.write_text("safe", encoding="utf-8")
    require_regular_files(tmp_path, ["AGENTS.md"])
    with pytest.raises(FactoryFailure) as captured:
        require_regular_files(tmp_path, ["scripts/v3-r1-s00.sh"])
    assert captured.value.code == "FAIL_SOURCE_FILE"
    link = tmp_path / "scripts/v3-r1-s00.sh"
    link.parent.mkdir()
    link.symlink_to(regular)
    with pytest.raises(FactoryFailure) as captured:
        require_regular_files(tmp_path, ["scripts/v3-r1-s00.sh"])
    assert captured.value.code == "FAIL_SOURCE_FILE"


def test_immutable_corpus_positive_and_failures(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    tracked = b"\0".join(f"docs/BRD/{index}.md".encode() for index in range(31)) + b"\0"
    calls = iter(
        [
            CompletedProcess([], 0, b"", b""),
            CompletedProcess([], 0, tracked, b""),
        ]
    )
    monkeypatch.setattr(
        "ysf.secure_factory.policy.subprocess.run", lambda *args, **kwargs: next(calls)
    )
    from ysf.secure_factory.policy import verify_immutable_corpus

    assert verify_immutable_corpus(tmp_path).passed

    monkeypatch.setattr(
        "ysf.secure_factory.policy.subprocess.run",
        lambda *args, **kwargs: CompletedProcess([], 0, b" M docs/BRD/a.md\0", b""),
    )
    with pytest.raises(FactoryFailure) as captured:
        verify_immutable_corpus(tmp_path)
    assert captured.value.code == "FAIL_IMMUTABLE_CORPUS"

    calls = iter(
        [
            CompletedProcess([], 0, b"", b""),
            CompletedProcess([], 0, b"docs/BRD/a.md\0", b""),
        ]
    )
    monkeypatch.setattr(
        "ysf.secure_factory.policy.subprocess.run", lambda *args, **kwargs: next(calls)
    )
    with pytest.raises(FactoryFailure) as captured:
        verify_immutable_corpus(tmp_path)
    assert captured.value.code == "FAIL_IMMUTABLE_CORPUS_COUNT"


def test_approval_ruleset_and_external_effect_policy_fail_closed() -> None:
    contract = "337519fcf7d08104ba0e53cbf33dcc4b4a75ec32aac18601cb097c778aa0ae35"
    ruleset = {
        "enforcement": "active",
        "target": "refs/heads/v3/main",
        "bypass_actors": [],
        "required_status_checks": [
            "S00 / policy",
            "S00 / test",
            "S00 / build-candidate",
            "S00 / verify-candidate",
        ],
    }
    assert validate_approval_and_ruleset(
        approval_digest=contract,
        reviewed_commit="a" * 40,
        current_commit="a" * 40,
        ruleset=ruleset,
    ).passed
    for field, code in (
        ("approval", "FAIL_APPROVAL_DIGEST"),
        ("review", "FAIL_STALE_REVIEW"),
        ("ruleset", "FAIL_RULESET_MISMATCH"),
    ):
        values = {
            "approval_digest": contract,
            "reviewed_commit": "a" * 40,
            "current_commit": "a" * 40,
            "ruleset": ruleset,
        }
        if field == "approval":
            values["approval_digest"] = "0" * 64
        elif field == "review":
            values["current_commit"] = "b" * 40
        else:
            values["ruleset"] = {**ruleset, "bypass_actors": ["synthetic"]}
        with pytest.raises(FactoryFailure) as captured:
            validate_approval_and_ruleset(**values)
        assert captured.value.code == code

    controls = {
        "YSF_EXTERNAL_EFFECT_BUDGET": "DENY_ALL",
        "YSF_PROVIDERS": "OFF",
        "YSF_EMAIL_MODE": "NON_RELAYING",
    }
    assert validate_external_effect_policy(controls).passed
    with pytest.raises(FactoryFailure) as captured:
        validate_external_effect_policy({**controls, "YSF_PROVIDER_TARGET": "SYNTHETIC"})
    assert captured.value.code == "FAIL_EXTERNAL_EFFECT_POLICY"
