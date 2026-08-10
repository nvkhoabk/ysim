from __future__ import annotations

import copy
import hashlib
import json
from datetime import UTC, datetime
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
    build_governance_attestation_payload,
    changed_paths,
    mutation_paths,
    observable_ruleset_evidence,
    parse_porcelain_z,
    render_governance_attestation,
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


_REPOSITORY_NAME = "nvkhoabk/ysim"
_BASE_SHA = "5be8413d3c22d1345b3088424af40ca2eb9d1115"
_HEAD_SHA = "d" * 40
_HEAD_TREE = "e" * 40
_RULESET_UPDATED_AT = "2026-08-08T16:22:16.442+07:00"
_HEAD_COMMITTED_AT = "2026-08-10T00:00:00Z"
_RETRIEVED_AT = "2026-08-10T00:01:00Z"
_COMMENT_CREATED_AT = "2026-08-10T00:02:00Z"
_NOW = datetime(2026, 8, 10, 1, 0, tzinfo=UTC)


def _governance_payloads() -> dict[str, Any]:
    repository = _REPOSITORY_NAME
    return {
        f"/repos/{repository}/rulesets/20583674": {
            "id": 20583674,
            "target": "branch",
            "enforcement": "active",
            "updated_at": _RULESET_UPDATED_AT,
            "bypass_actors": [],
            "conditions": {
                "ref_name": {
                    "include": ["refs/heads/v3/main"],
                    "exclude": [],
                }
            },
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
            "base": {
                "ref": "v3/main",
                "sha": _BASE_SHA,
                "repo": {"full_name": repository},
            },
            "head": {
                "ref": "feature/v3-r1-g00-s00-secure-factory",
                "sha": _HEAD_SHA,
                "repo": {"full_name": repository},
            },
        },
        f"/repos/{repository}/commits/{_HEAD_SHA}": {
            "sha": _HEAD_SHA,
            "commit": {"committer": {"date": _HEAD_COMMITTED_AT}},
        },
        f"/repos/{repository}/issues/1/comments?per_page=100": [],
    }


def _attestation_payload(ruleset: dict[str, Any]) -> dict[str, Any]:
    return build_governance_attestation_payload(
        ruleset=ruleset,
        repository=_REPOSITORY_NAME,
        pr_number=1,
        base_sha=_BASE_SHA,
        head_sha=_HEAD_SHA,
        head_tree=_HEAD_TREE,
        retrieved_at=_RETRIEVED_AT,
    )


def _attestation_comment(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": 123456,
        "body": render_governance_attestation(payload),
        "user": {"login": "nvkhoabk", "id": 22950753},
        "author_association": "OWNER",
        "created_at": _COMMENT_CREATED_AT,
        "updated_at": _COMMENT_CREATED_AT,
        "issue_url": "https://api.github.com/repos/nvkhoabk/ysim/issues/1",
        "html_url": "https://github.com/nvkhoabk/ysim/pull/1#issuecomment-123456",
    }


def _attested_payloads() -> tuple[dict[str, Any], dict[str, Any]]:
    payloads = _governance_payloads()
    ruleset_path = "/repos/nvkhoabk/ysim/rulesets/20583674"
    ruleset = payloads[ruleset_path]
    assert isinstance(ruleset, dict)
    payload = _attestation_payload(ruleset)
    del ruleset["bypass_actors"]
    payloads["/repos/nvkhoabk/ysim/issues/1/comments?per_page=100"] = [
        _attestation_comment(payload)
    ]
    return payloads, payload


def _validate(payloads: dict[str, Any]) -> Any:
    return validate_live_governance(
        repository=_REPOSITORY_NAME,
        pr_number=1,
        expected_base_ref="v3/main",
        expected_base_sha=_BASE_SHA,
        expected_head_ref="feature/v3-r1-g00-s00-secure-factory",
        expected_head_sha=_HEAD_SHA,
        expected_head_tree=_HEAD_TREE,
        run_id="123",
        fetch_json=lambda path: payloads[path],
        now=_NOW,
    )


def _replace_comment_payload(
    payloads: dict[str, Any], payload: dict[str, Any]
) -> dict[str, Any]:
    unsigned = dict(payload)
    unsigned.pop("payload_sha256", None)
    payload["payload_sha256"] = "sha256:" + hashlib.sha256(
        json.dumps(unsigned, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    comments = payloads["/repos/nvkhoabk/ysim/issues/1/comments?per_page=100"]
    assert isinstance(comments, list)
    comment = comments[0]
    assert isinstance(comment, dict)
    comment["body"] = render_governance_attestation(payload)
    return comment


def test_live_governance_observed_empty_bypass_passes_directly() -> None:
    gate = _validate(_governance_payloads())
    assert gate.passed
    assert gate.details["bypass_actor_state"] == "OBSERVED_EMPTY"
    assert gate.details["human_attestation_verified"] is False


@pytest.mark.parametrize(
    "mutation",
    ["disabled", "missing_check", "stale_head", "not_draft", "missing_updated_at"],
)
def test_live_governance_observable_controls_still_fail_closed(
    mutation: str,
) -> None:
    payloads = _governance_payloads()
    ruleset = payloads["/repos/nvkhoabk/ysim/rulesets/20583674"]
    pull = payloads["/repos/nvkhoabk/ysim/pulls/1"]
    assert isinstance(ruleset, dict) and isinstance(pull, dict)
    if mutation == "disabled":
        ruleset["enforcement"] = "disabled"
    elif mutation == "missing_check":
        rules = ruleset["rules"]
        assert isinstance(rules, list)
        checks = rules[1]["parameters"]["required_status_checks"]
        rules[1]["parameters"]["required_status_checks"] = checks[:-1]
    elif mutation == "stale_head":
        pull["head"]["sha"] = "a" * 40
    elif mutation == "not_draft":
        pull["draft"] = False
    else:
        del ruleset["updated_at"]
    with pytest.raises(FactoryFailure) as captured:
        _validate(payloads)
    assert captured.value.code == "FAIL_GOVERNANCE_MISMATCH"


def test_live_governance_nonempty_bypass_fails_even_with_attestation() -> None:
    payloads, _ = _attested_payloads()
    ruleset = payloads["/repos/nvkhoabk/ysim/rulesets/20583674"]
    assert isinstance(ruleset, dict)
    ruleset["bypass_actors"] = [{"synthetic_actor_type": "NONEMPTY"}]
    with pytest.raises(FactoryFailure) as captured:
        _validate(payloads)
    assert captured.value.code == "FAIL_GOVERNANCE_BYPASS_ACTORS"

    ruleset["bypass_actors"] = "synthetic-invalid-type"
    with pytest.raises(FactoryFailure) as captured:
        _validate(payloads)
    assert captured.value.code == "FAIL_GOVERNANCE_RULESET"


def test_unobservable_bypass_requires_exact_human_attestation() -> None:
    payloads = _governance_payloads()
    ruleset = payloads["/repos/nvkhoabk/ysim/rulesets/20583674"]
    assert isinstance(ruleset, dict)
    del ruleset["bypass_actors"]
    with pytest.raises(FactoryFailure) as captured:
        _validate(payloads)
    assert captured.value.code == "FAIL_GOVERNANCE_ATTESTATION_REQUIRED"

    ruleset["bypass_actors"] = None
    with pytest.raises(FactoryFailure) as captured:
        _validate(payloads)
    assert captured.value.code == "FAIL_GOVERNANCE_ATTESTATION_REQUIRED"

    payloads, payload = _attested_payloads()
    gate = _validate(payloads)
    assert gate.passed
    assert gate.details["bypass_actor_state"] == "UNOBSERVABLE_UNDER_CALLER"
    assert gate.details["human_attestation_verified"] is True
    retained = json.dumps(gate.details, sort_keys=True)
    assert "Authorization" not in retained
    assert "synthetic_actor_type" not in retained
    assert gate.details["attestation_payload_sha256"] == payload["payload_sha256"]


@pytest.mark.parametrize(
    ("mutation", "reason"),
    [
        ("author_login", "AUTHOR_LOGIN"),
        ("author_id", "AUTHOR_ID"),
        ("association", "AUTHOR_ASSOCIATION"),
        ("comment_issue", "COMMENT_REPOSITORY_PR"),
        ("comment_html", "COMMENT_REPOSITORY_PR"),
        ("edited", "COMMENT_EDITED"),
        ("expired", "ATTESTATION_FRESHNESS"),
        ("before_head", "ATTESTATION_FRESHNESS"),
        ("repository", "PAYLOAD_BINDING"),
        ("pr", "PAYLOAD_BINDING"),
        ("base", "PAYLOAD_BINDING"),
        ("tree", "PAYLOAD_BINDING"),
        ("ruleset_id", "PAYLOAD_BINDING"),
        ("ruleset_updated", "PAYLOAD_BINDING"),
        ("observable_digest", "OBSERVABLE_DIGEST"),
        ("full_digest", "FULL_DIGEST"),
        ("bypass_digest", "BYPASS_DIGEST"),
        ("payload_digest", "PAYLOAD_DIGEST"),
        ("bypass_count", "BYPASS_COUNT"),
        ("retrieved_timestamp", "RETRIEVED_TIMESTAMP"),
        ("payload_fields", "PAYLOAD_FIELDS"),
    ],
)
def test_attestation_identity_freshness_and_digest_fail_closed(
    mutation: str, reason: str
) -> None:
    payloads, payload = _attested_payloads()
    comments = payloads["/repos/nvkhoabk/ysim/issues/1/comments?per_page=100"]
    assert isinstance(comments, list) and isinstance(comments[0], dict)
    comment = comments[0]
    if mutation == "author_login":
        comment["user"]["login"] = "synthetic-untrusted"
    elif mutation == "author_id":
        comment["user"]["id"] = 1
    elif mutation == "association":
        comment["author_association"] = "CONTRIBUTOR"
    elif mutation == "comment_issue":
        comment["issue_url"] = "https://api.github.com/repos/synthetic/repo/issues/1"
    elif mutation == "comment_html":
        comment["html_url"] = "https://github.com/synthetic/repo/pull/1#issuecomment-1"
    elif mutation == "edited":
        comment["updated_at"] = "2026-08-10T00:03:00Z"
    elif mutation == "expired":
        comment["created_at"] = "2026-08-08T00:02:00Z"
        comment["updated_at"] = comment["created_at"]
    elif mutation == "before_head":
        comment["created_at"] = "2026-08-09T23:59:00Z"
        comment["updated_at"] = comment["created_at"]
    else:
        if mutation == "payload_fields":
            payload["secondary"] = "synthetic"
            _replace_comment_payload(payloads, payload)
        else:
            key, value = {
            "repository": ("repository", "synthetic/repository"),
            "pr": ("pr_number", 2),
            "base": ("base_sha", "a" * 40),
            "tree": ("head_tree", "a" * 40),
            "ruleset_id": ("ruleset_id", 1),
            "ruleset_updated": ("ruleset_updated_at", "2026-01-01T00:00:00Z"),
            "observable_digest": ("observable_ruleset_sha256", "sha256:" + "a" * 64),
            "full_digest": ("full_ruleset_sha256", "sha256:" + "a" * 64),
            "bypass_digest": ("bypass_actors_sha256", "sha256:" + "a" * 64),
            "payload_digest": ("payload_sha256", "sha256:" + "a" * 64),
            "bypass_count": ("bypass_actors_count", 1),
            "retrieved_timestamp": ("retrieved_at", "invalid"),
            }[mutation]
            payload[key] = value
            if mutation != "payload_digest":
                _replace_comment_payload(payloads, payload)
            else:
                comment["body"] = render_governance_attestation(payload)
    with pytest.raises(FactoryFailure) as captured:
        _validate(payloads)
    assert captured.value.code == f"FAIL_GOVERNANCE_ATTESTATION_INVALID:{reason}"


@pytest.mark.parametrize(
    ("mutation", "reason"),
    [
        ("duplicate", "DUPLICATE_JSON_KEY"),
        ("malformed_json", "COMMENT_JSON"),
        ("malformed_marker", "COMMENT_ENVELOPE"),
        ("noncanonical", "COMMENT_CANONICAL"),
        ("trailing", "COMMENT_ENVELOPE"),
        ("missing_fields", "COMMENT_FIELDS"),
        ("oversized", "COMMENT_OVERSIZED"),
    ],
)
def test_attestation_comment_parser_fails_closed(mutation: str, reason: str) -> None:
    payloads, payload = _attested_payloads()
    comments = payloads["/repos/nvkhoabk/ysim/issues/1/comments?per_page=100"]
    assert isinstance(comments, list) and isinstance(comments[0], dict)
    comment = comments[0]
    if mutation == "duplicate":
        body = render_governance_attestation(payload)
        comment["body"] = body.replace('{"base_sha"', '{"schema":"duplicate","base_sha"')
    elif mutation == "malformed_json":
        comment["body"] = (
            "<!-- ysim-s00-governance-attestation:v1 -->\n```json\n{invalid\n```\n"
        )
    elif mutation == "malformed_marker":
        comment["body"] = str(comment["body"]).replace(
            "<!-- ysim-s00-governance-attestation:v1 -->\n",
            "<!-- ysim-s00-governance-attestation:v1 --> \n",
        )
    elif mutation == "noncanonical":
        comment["body"] = str(comment["body"]).replace(
            '{"base_sha"', '{\n"base_sha"'
        )
    elif mutation == "trailing":
        comment["body"] = str(comment["body"]) + "{}"
    elif mutation == "missing_fields":
        del comment["author_association"]
    else:
        comment["body"] = (
            "<!-- ysim-s00-governance-attestation:v1 -->\n```json\n"
            + " " * 8192
            + "\n```\n"
        )
    with pytest.raises(FactoryFailure) as captured:
        _validate(payloads)
    assert captured.value.code == f"FAIL_GOVERNANCE_ATTESTATION_INVALID:{reason}"


def test_attestation_ambiguity_old_head_and_untrusted_text() -> None:
    payloads, payload = _attested_payloads()
    comments = payloads["/repos/nvkhoabk/ysim/issues/1/comments?per_page=100"]
    assert isinstance(comments, list) and isinstance(comments[0], dict)
    duplicate = copy.deepcopy(comments[0])
    duplicate["id"] = 123457
    duplicate["html_url"] = (
        "https://github.com/nvkhoabk/ysim/pull/1#issuecomment-123457"
    )
    comments.append(duplicate)
    with pytest.raises(FactoryFailure) as captured:
        _validate(payloads)
    assert captured.value.code.endswith(":AMBIGUOUS_CURRENT_HEAD")

    old_payloads, old_payload = _attested_payloads()
    old_payload["head_sha"] = "a" * 40
    _replace_comment_payload(old_payloads, old_payload)
    with pytest.raises(FactoryFailure) as captured:
        _validate(old_payloads)
    assert captured.value.code == "FAIL_GOVERNANCE_ATTESTATION_REQUIRED"

    untrusted = _governance_payloads()
    ruleset = untrusted["/repos/nvkhoabk/ysim/rulesets/20583674"]
    assert isinstance(ruleset, dict)
    del ruleset["bypass_actors"]
    untrusted["/repos/nvkhoabk/ysim/issues/1/comments?per_page=100"] = [
        {"body": "$(synthetic-command)"}
    ]
    with pytest.raises(FactoryFailure) as captured:
        _validate(untrusted)
    assert captured.value.code == "FAIL_GOVERNANCE_ATTESTATION_REQUIRED"


@pytest.mark.parametrize(
    ("mutation", "reason"),
    [
        ("comments_response", "API_FIELDS"),
        ("comment_page_limit", "COMMENT_PAGE_LIMIT"),
        ("head_fields", "HEAD_COMMIT_FIELDS"),
    ],
)
def test_attestation_api_metadata_fails_closed(mutation: str, reason: str) -> None:
    payloads, _ = _attested_payloads()
    if mutation == "comments_response":
        payloads["/repos/nvkhoabk/ysim/issues/1/comments?per_page=100"] = {}
    elif mutation == "comment_page_limit":
        comments = payloads["/repos/nvkhoabk/ysim/issues/1/comments?per_page=100"]
        assert isinstance(comments, list)
        payloads["/repos/nvkhoabk/ysim/issues/1/comments?per_page=100"] = (
            comments * 100
        )
    else:
        payloads[f"/repos/{_REPOSITORY_NAME}/commits/{_HEAD_SHA}"] = {"sha": _HEAD_SHA}
    with pytest.raises(FactoryFailure) as captured:
        _validate(payloads)
    assert captured.value.code == f"FAIL_GOVERNANCE_ATTESTATION_INVALID:{reason}"


def test_observable_ruleset_digest_is_stable_and_excludes_hidden_field() -> None:
    payloads = _governance_payloads()
    ruleset = payloads["/repos/nvkhoabk/ysim/rulesets/20583674"]
    assert isinstance(ruleset, dict)
    before = observable_ruleset_evidence(ruleset)
    del ruleset["bypass_actors"]
    assert observable_ruleset_evidence(ruleset) == before


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
