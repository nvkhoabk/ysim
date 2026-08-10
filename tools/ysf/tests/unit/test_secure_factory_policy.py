from __future__ import annotations

from pathlib import Path
from subprocess import CompletedProcess
from typing import Any

import pytest

from ysf.secure_factory.models import FactoryFailure
from ysf.secure_factory.policy import (
    APPROVED_CONTRACT_SHA256,
    CONTRACT_RELATIVE_PATH,
    EXACT_ALLOWLIST,
    _github_json,
    changed_paths,
    mutation_paths,
    parse_porcelain_z,
    require_regular_files,
    validate_approval_and_ruleset,
    validate_changed_paths,
    validate_external_effect_policy,
    validate_live_governance,
    validate_relative_path,
    verify_approved_contract,
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
    contract = APPROVED_CONTRACT_SHA256
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


def test_exact_contract_bytes_pass_and_tamper_or_missing_fail(tmp_path: Path) -> None:
    source = Path(__file__).resolve().parents[4] / CONTRACT_RELATIVE_PATH
    contract = tmp_path / CONTRACT_RELATIVE_PATH
    contract.parent.mkdir(parents=True)
    contract.write_bytes(source.read_bytes())
    gate = verify_approved_contract(tmp_path)
    assert gate.details == {
        "contract_path": CONTRACT_RELATIVE_PATH,
        "actual_sha256": APPROVED_CONTRACT_SHA256,
        "approved_sha256": APPROVED_CONTRACT_SHA256,
        "digest_match": True,
    }
    contract.write_bytes(contract.read_bytes() + b"\n")
    with pytest.raises(FactoryFailure) as captured:
        verify_approved_contract(tmp_path)
    assert captured.value.code == "FAIL_CONTRACT_DIGEST"
    contract.unlink()
    with pytest.raises(FactoryFailure) as captured:
        verify_approved_contract(tmp_path)
    assert captured.value.code == "FAIL_CONTRACT_SOURCE"


def _governance_payloads() -> dict[str, dict[str, Any]]:
    base = "5be8413d3c22d1345b3088424af40ca2eb9d1115"
    head = "d" * 40
    repository = "nvkhoabk/ysim"
    return {
        f"/repos/{repository}/rulesets/20583674": {
            "id": 20583674,
            "target": "branch",
            "enforcement": "active",
            "bypass_actors": [],
            "conditions": {"ref_name": {"include": ["refs/heads/v3/main"]}},
            "rules": [
                {
                    "type": "pull_request",
                    "parameters": {
                        "required_approving_review_count": 1,
                        "dismiss_stale_reviews_on_push": True,
                        "require_code_owner_review": True,
                        "required_review_thread_resolution": True,
                    },
                },
                {
                    "type": "required_status_checks",
                    "parameters": {
                        "strict_required_status_checks_policy": True,
                        "required_status_checks": [
                            {"context": "S00 / policy"},
                            {"context": "S00 / test"},
                            {"context": "S00 / build-candidate"},
                            {"context": "S00 / verify-candidate"},
                        ],
                    },
                },
            ],
        },
        f"/repos/{repository}/pulls/1": {
            "number": 1,
            "state": "open",
            "draft": True,
            "merged": False,
            "base": {"ref": "v3/main", "sha": base, "repo": {"full_name": repository}},
            "head": {
                "ref": "feature/v3-r1-g00-s00-secure-factory",
                "sha": head,
                "repo": {"full_name": repository},
            },
        },
    }


def test_live_governance_readback_binds_ruleset_and_draft_pr() -> None:
    payloads = _governance_payloads()
    gate = validate_live_governance(
        repository="nvkhoabk/ysim",
        pr_number=1,
        expected_base_ref="v3/main",
        expected_base_sha="5be8413d3c22d1345b3088424af40ca2eb9d1115",
        expected_head_ref="feature/v3-r1-g00-s00-secure-factory",
        expected_head_sha="d" * 40,
        run_id="123",
        fetch_json=lambda path: payloads[path],
    )
    assert gate.passed
    assert gate.details["github_approving_review_claimed"] is False
    assert gate.details["bypass_actor_count"] == 0


@pytest.mark.parametrize(
    ("mutation", "code"),
    [
        ("disabled", "FAIL_GOVERNANCE_MISMATCH"),
        ("bypass", "FAIL_GOVERNANCE_MISMATCH"),
        ("missing_check", "FAIL_GOVERNANCE_MISMATCH"),
        ("stale_head", "FAIL_GOVERNANCE_MISMATCH"),
        ("not_draft", "FAIL_GOVERNANCE_MISMATCH"),
    ],
)
def test_live_governance_readback_fails_closed(mutation: str, code: str) -> None:
    payloads = _governance_payloads()
    ruleset = payloads["/repos/nvkhoabk/ysim/rulesets/20583674"]
    pull = payloads["/repos/nvkhoabk/ysim/pulls/1"]
    if mutation == "disabled":
        ruleset["enforcement"] = "disabled"
    elif mutation == "bypass":
        ruleset["bypass_actors"] = [{"actor_type": "OrganizationAdmin"}]
    elif mutation == "missing_check":
        rules = ruleset["rules"]
        assert isinstance(rules, list)
        checks = rules[1]["parameters"]["required_status_checks"]
        rules[1]["parameters"]["required_status_checks"] = checks[:-1]
    elif mutation == "stale_head":
        pull["head"]["sha"] = "e" * 40
    else:
        pull["draft"] = False
    with pytest.raises(FactoryFailure) as captured:
        validate_live_governance(
            repository="nvkhoabk/ysim",
            pr_number=1,
            expected_base_ref="v3/main",
            expected_base_sha="5be8413d3c22d1345b3088424af40ca2eb9d1115",
            expected_head_ref="feature/v3-r1-g00-s00-secure-factory",
            expected_head_sha="d" * 40,
            run_id="123",
            fetch_json=lambda path: payloads[path],
        )
    assert captured.value.code == code


def test_github_readback_uses_bounded_json_response(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class Response:
        status = 200

        def read(self, limit: int) -> bytes:
            assert limit == 1024 * 1024 + 1
            return b'{"id":20583674}'

    class Connection:
        def __init__(self, host: str, timeout: int) -> None:
            assert host == "api.github.com"
            assert timeout == 15

        def request(self, method: str, path: str, headers: dict[str, str]) -> None:
            assert method == "GET"
            assert path.startswith("/repos/nvkhoabk/ysim/")
            assert "Authorization" not in headers

        def getresponse(self) -> Response:
            return Response()

        def close(self) -> None:
            pass

    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.setattr("ysf.secure_factory.policy.http.client.HTTPSConnection", Connection)
    assert _github_json("/repos/nvkhoabk/ysim/rulesets/20583674") == {"id": 20583674}


@pytest.mark.parametrize(("status", "payload"), [(503, b"{}"), (200, b"not-json")])
def test_github_readback_fails_closed_on_http_or_json(
    monkeypatch: pytest.MonkeyPatch, status: int, payload: bytes
) -> None:
    class Response:
        def read(self, limit: int) -> bytes:
            return payload

    Response.status = status

    class Connection:
        def __init__(self, host: str, timeout: int) -> None:
            pass

        def request(self, method: str, path: str, headers: dict[str, str]) -> None:
            pass

        def getresponse(self) -> Response:
            return Response()

        def close(self) -> None:
            pass

    monkeypatch.setattr("ysf.secure_factory.policy.http.client.HTTPSConnection", Connection)
    with pytest.raises(FactoryFailure) as captured:
        _github_json("/repos/nvkhoabk/ysim/rulesets/20583674")
    assert captured.value.code == "FAIL_GOVERNANCE_READBACK"
