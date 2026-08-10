"""Exact-allowlist, immutable-corpus, and path-safety policy."""

from __future__ import annotations

import hashlib
import http.client
import json
import os
import re
import subprocess
from collections.abc import Callable, Iterable, Mapping
from pathlib import Path, PurePosixPath
from typing import Any

from ysf.secure_factory.models import FactoryFailure, GateResult

EXACT_ALLOWLIST: tuple[str, ...] = (
    "AGENTS.md",
    ".github/CODEOWNERS",
    ".github/workflows/v3-r1-s00-secure-factory.yml",
    "docs/v3/r1/g00/s00/README.md",
    "docs/v3/r1/g00/s00/context-receipt.yaml",
    "docs/v3/r1/g00/s00/clarification-register.yaml",
    "docs/v3/r1/g00/s00/slice-contract.yaml",
    "docs/v3/r1/g00/s00/ExecPlan.md",
    "docs/v3/r1/g00/s00/source-and-delivery-policy.md",
    "docs/v3/r1/g00/s00/environment-identity.yaml",
    "docs/v3/r1/g00/s00/test-matrix.yaml",
    "docs/v3/r1/g00/s00/evidence-schema.yaml",
    "tools/ysf/pyproject.toml",
    "tools/ysf/requirements-s00-build.lock",
    "tools/ysf/requirements-s00-dev.lock",
    "tools/ysf/src/ysf/cli.py",
    "tools/ysf/src/ysf/secure_factory/__init__.py",
    "tools/ysf/src/ysf/secure_factory/models.py",
    "tools/ysf/src/ysf/secure_factory/cli.py",
    "tools/ysf/src/ysf/secure_factory/environment.py",
    "tools/ysf/src/ysf/secure_factory/policy.py",
    "tools/ysf/src/ysf/secure_factory/sensitive.py",
    "tools/ysf/src/ysf/secure_factory/evidence.py",
    "tools/ysf/src/ysf/secure_factory/candidate.py",
    "tools/ysf/tests/unit/test_secure_factory_environment.py",
    "tools/ysf/tests/unit/test_secure_factory_policy.py",
    "tools/ysf/tests/unit/test_secure_factory_sensitive.py",
    "tools/ysf/tests/unit/test_secure_factory_evidence.py",
    "tools/ysf/tests/unit/test_secure_factory_candidate.py",
    "tools/ysf/tests/integration/test_secure_factory_pipeline.py",
    "tools/ysf/tests/fixtures/secure_factory/compliant/README.txt",
    "tools/ysf/tests/fixtures/secure_factory/noncompliant/path-escape.json",
    "tools/ysf/tests/fixtures/secure_factory/noncompliant/synthetic-secret.txt",
    "tools/ysf/tests/fixtures/secure_factory/noncompliant/synthetic-esim-payload.txt",
    "tools/ysf/tests/fixtures/secure_factory/noncompliant/tampered-manifest.json",
    "scripts/v3-r1-s00.sh",
)

QUARANTINED_FIXTURES: frozenset[str] = frozenset(
    path for path in EXACT_ALLOWLIST if "/noncompliant/" in path
)

REQUIRED_STATUS_CHECKS: frozenset[str] = frozenset(
    {
        "S00 / policy",
        "S00 / test",
        "S00 / build-candidate",
        "S00 / verify-candidate",
    }
)
CONTRACT_RELATIVE_PATH = "docs/v3/r1/g00/s00/slice-contract.yaml"
APPROVED_CONTRACT_SHA256 = (
    "0c1c0e76c6ff55afd77c6c3aeaebae4a89bd2341870766c05d2ba8610a62b8dd"
)
RULESET_ID = 20583674
_GITHUB_API_HOST = "api.github.com"
_REPOSITORY = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def validate_relative_path(value: str) -> str:
    """Return a normalized repository path or fail closed."""

    if not value or "\x00" in value or "\\" in value:
        raise FactoryFailure("FAIL_PATH_FORMAT", "Repository path is not canonical.")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise FactoryFailure("FAIL_PATH_ESCAPE", "Repository path escapes its root.")
    normalized = path.as_posix()
    if normalized != value:
        raise FactoryFailure("FAIL_PATH_FORMAT", "Repository path is not canonical.")
    return normalized


def parse_porcelain_z(data: bytes) -> set[str]:
    """Parse Git porcelain v1 -z, retaining both sides of rename records."""

    records = data.split(b"\x00")
    paths: set[str] = set()
    index = 0
    while index < len(records):
        record = records[index]
        index += 1
        if not record:
            continue
        if len(record) < 4 or record[2:3] != b" ":
            raise FactoryFailure("FAIL_GIT_STATUS_FORMAT", "Git status record is invalid.")
        status = record[:2].decode("ascii", errors="strict")
        path = record[3:].decode("utf-8", errors="strict")
        paths.add(validate_relative_path(path))
        if "R" in status or "C" in status:
            if index >= len(records) or not records[index]:
                raise FactoryFailure("FAIL_GIT_STATUS_FORMAT", "Rename status is incomplete.")
            other = records[index].decode("utf-8", errors="strict")
            index += 1
            paths.add(validate_relative_path(other))
    return paths


def changed_paths(repository_root: Path) -> set[str]:
    process = subprocess.run(
        ["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        cwd=repository_root,
        check=False,
        capture_output=True,
    )
    if process.returncode != 0:
        raise FactoryFailure(
            "FAIL_GIT_STATUS",
            "Unable to determine the repository mutation set.",
            details={"exit_code": process.returncode},
        )
    return parse_porcelain_z(process.stdout)


def mutation_paths(repository_root: Path, *, base_ref: str = "v3/main") -> set[str]:
    """Return committed branch diff plus unstaged/staged/untracked mutations."""

    process = subprocess.run(
        ["git", "diff", "--name-only", "-z", f"{base_ref}...HEAD"],
        cwd=repository_root,
        check=False,
        capture_output=True,
    )
    if process.returncode != 0:
        raise FactoryFailure("FAIL_GIT_DIFF", "Unable to determine branch mutation set.")
    committed = {
        validate_relative_path(item.decode("utf-8", errors="strict"))
        for item in process.stdout.split(b"\x00")
        if item
    }
    return committed.union(changed_paths(repository_root))


def _assert_no_symlink(repository_root: Path, relative_path: str) -> None:
    current = repository_root
    for part in PurePosixPath(relative_path).parts:
        current = current / part
        if current.is_symlink():
            raise FactoryFailure(
                "FAIL_SYMLINK_PATH",
                "Changed repository path contains a symbolic link.",
                details={"path": relative_path},
            )
        if not current.exists():
            break


def validate_changed_paths(
    repository_root: Path,
    paths: Iterable[str],
    *,
    expected: Iterable[str] | None = None,
) -> GateResult:
    """Apply exact allowlist/default-deny and optional exact-stage scope."""

    normalized = {validate_relative_path(path) for path in paths}
    unexpected = sorted(normalized.difference(EXACT_ALLOWLIST))
    if unexpected:
        raise FactoryFailure(
            "FAIL_UNAPPROVED_PATH",
            "Repository contains a changed path outside the exact S00 allowlist.",
            details={"paths": unexpected},
        )
    for path in sorted(normalized):
        _assert_no_symlink(repository_root, path)
    if expected is not None:
        expected_set = {validate_relative_path(path) for path in expected}
        if normalized != expected_set:
            raise FactoryFailure(
                "FAIL_STAGE_MUTATION_SET",
                "Repository mutation set does not match the authorized stage.",
                details={
                    "missing": sorted(expected_set - normalized),
                    "extra": sorted(normalized - expected_set),
                },
            )
    return GateResult(
        gate="source_allowlist",
        result="PASS",
        message="Exact changed-path policy verified.",
        details={"changed_path_count": len(normalized)},
    )


def verify_immutable_corpus(repository_root: Path) -> GateResult:
    """Verify BRD/UXF bytes against HEAD and reject untracked corpus files."""

    process = subprocess.run(
        [
            "git",
            "status",
            "--porcelain=v1",
            "-z",
            "--untracked-files=all",
            "--",
            "docs/BRD",
            "docs/UXF",
        ],
        cwd=repository_root,
        check=False,
        capture_output=True,
    )
    if process.returncode != 0:
        raise FactoryFailure("FAIL_CORPUS_CHECK", "Immutable corpus check failed.")
    mutations = parse_porcelain_z(process.stdout)
    if mutations:
        raise FactoryFailure(
            "FAIL_IMMUTABLE_CORPUS",
            "BRD or UXF corpus bytes differ from the approved seed tree.",
            details={"paths": sorted(mutations)},
        )
    files = subprocess.run(
        ["git", "ls-files", "-z", "--", "docs/BRD", "docs/UXF"],
        cwd=repository_root,
        check=False,
        capture_output=True,
    )
    if files.returncode != 0:
        raise FactoryFailure("FAIL_CORPUS_CHECK", "Immutable corpus inventory failed.")
    count = len([item for item in files.stdout.split(b"\x00") if item])
    if count != 31:
        raise FactoryFailure(
            "FAIL_IMMUTABLE_CORPUS_COUNT",
            "Immutable corpus file count does not match the approved inventory.",
            details={"observed_count": count},
        )
    return GateResult(
        gate="immutable_corpus",
        result="PASS",
        message="All 24 BRD and seven UXF files remain immutable.",
        details={"file_count": count},
    )


def read_policy_allowlist(policy_path: Path) -> tuple[str, ...]:
    """Read the only text block following the Exact allowlist heading."""

    lines = policy_path.read_text(encoding="utf-8").splitlines()
    try:
        heading = lines.index("## Exact allowlist")
        start = lines.index("```text", heading) + 1
        end = lines.index("```", start)
    except ValueError as exc:
        raise FactoryFailure(
            "FAIL_POLICY_SELF_CHECK",
            "Source policy does not contain one readable exact allowlist.",
        ) from exc
    return tuple(line for line in lines[start:end] if line)


def verify_policy_self_protection(policy_path: Path) -> GateResult:
    recorded = read_policy_allowlist(policy_path)
    if recorded != EXACT_ALLOWLIST or len(set(recorded)) != len(recorded):
        raise FactoryFailure(
            "FAIL_POLICY_SELF_CHECK",
            "Executable allowlist differs from the frozen source policy.",
        )
    return GateResult(
        gate="policy_self_protection",
        result="PASS",
        message="Executable and frozen allowlists match exactly.",
        details={"allowlist_path_count": len(recorded)},
    )


def require_regular_files(repository_root: Path, paths: Iterable[str]) -> None:
    """Reject missing, non-regular, or multiply linked source inputs."""

    for relative_path in paths:
        normalized = validate_relative_path(relative_path)
        path = repository_root / normalized
        try:
            stat = path.lstat()
        except OSError as exc:
            raise FactoryFailure(
                "FAIL_SOURCE_FILE",
                "Required source input is missing.",
                details={"path": normalized},
            ) from exc
        if not path.is_file() or path.is_symlink() or stat.st_nlink != 1:
            raise FactoryFailure(
                "FAIL_SOURCE_FILE",
                "Required source input is not a single regular file.",
                details={"path": normalized},
            )


def contract_digest(path: Path) -> str:
    """Hash the exact approved Contract bytes or fail closed."""

    try:
        stat = path.lstat()
        if not path.is_file() or path.is_symlink() or stat.st_nlink != 1:
            raise OSError
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as exc:
        raise FactoryFailure(
            "FAIL_CONTRACT_SOURCE",
            "Approved Contract bytes are missing, unreadable or unsafe.",
            details={"contract_path": CONTRACT_RELATIVE_PATH},
        ) from exc


def verify_approved_contract(repository_root: Path) -> GateResult:
    """Bind actual Contract bytes to the exact Human-approved digest."""

    actual = contract_digest(repository_root / CONTRACT_RELATIVE_PATH)
    if actual != APPROVED_CONTRACT_SHA256:
        raise FactoryFailure(
            "FAIL_CONTRACT_DIGEST",
            "Actual Contract bytes do not match the Human-approved digest.",
            details={
                "contract_path": CONTRACT_RELATIVE_PATH,
                "actual_sha256": actual,
                "approved_sha256": APPROVED_CONTRACT_SHA256,
                "digest_match": False,
            },
        )
    return GateResult(
        gate="contract_digest",
        result="PASS",
        message="Actual Contract bytes match the Human-approved digest.",
        details={
            "contract_path": CONTRACT_RELATIVE_PATH,
            "actual_sha256": actual,
            "approved_sha256": APPROVED_CONTRACT_SHA256,
            "digest_match": True,
        },
    )


def _github_json(path: str) -> dict[str, Any]:
    connection = http.client.HTTPSConnection(_GITHUB_API_HOST, timeout=15)
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ysim-s00-governance-readback",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        connection.request("GET", path, headers=headers)
        response = connection.getresponse()
        payload = response.read(1024 * 1024 + 1)
    except (OSError, http.client.HTTPException) as exc:
        raise FactoryFailure(
            "FAIL_GOVERNANCE_READBACK",
            "Authoritative GitHub governance metadata is unavailable.",
        ) from exc
    finally:
        connection.close()
    if response.status != 200 or len(payload) > 1024 * 1024:
        raise FactoryFailure(
            "FAIL_GOVERNANCE_READBACK",
            "Authoritative GitHub governance metadata is unavailable.",
            details={"http_status": response.status},
        )
    try:
        value = json.loads(payload)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise FactoryFailure(
            "FAIL_GOVERNANCE_READBACK",
            "Authoritative GitHub governance metadata is invalid.",
        ) from exc
    if not isinstance(value, dict):
        raise FactoryFailure(
            "FAIL_GOVERNANCE_READBACK",
            "Authoritative GitHub governance metadata is invalid.",
        )
    return value


def validate_live_governance(
    *,
    repository: str,
    pr_number: int,
    expected_base_ref: str,
    expected_base_sha: str,
    expected_head_ref: str,
    expected_head_sha: str,
    run_id: str,
    fetch_json: Callable[[str], dict[str, Any]] = _github_json,
) -> GateResult:
    """Read and validate the authoritative public GitHub ruleset and PR state."""

    if (
        repository != "nvkhoabk/ysim"
        or not _REPOSITORY.fullmatch(repository)
        or pr_number <= 0
        or not run_id
        or not re.fullmatch(r"[0-9a-f]{40}", expected_base_sha)
        or not re.fullmatch(r"[0-9a-f]{40}", expected_head_sha)
    ):
        raise FactoryFailure(
            "FAIL_GOVERNANCE_EXPECTATION",
            "GitHub governance expectation is invalid.",
        )
    ruleset = fetch_json(f"/repos/{repository}/rulesets/{RULESET_ID}")
    pull = fetch_json(f"/repos/{repository}/pulls/{pr_number}")
    rules = ruleset.get("rules")
    conditions = ruleset.get("conditions")
    if not isinstance(rules, list) or not isinstance(conditions, dict):
        raise FactoryFailure(
            "FAIL_GOVERNANCE_RULESET",
            "Authoritative GitHub ruleset metadata is incomplete.",
        )
    by_type = {
        str(item.get("type")): item.get("parameters", {})
        for item in rules
        if isinstance(item, dict)
    }
    pull_rule = by_type.get("pull_request")
    checks_rule = by_type.get("required_status_checks")
    ref_condition = conditions.get("ref_name")
    if not all(isinstance(item, dict) for item in (pull_rule, checks_rule, ref_condition)):
        raise FactoryFailure(
            "FAIL_GOVERNANCE_RULESET",
            "Authoritative GitHub ruleset controls are incomplete.",
        )
    assert isinstance(pull_rule, dict)
    assert isinstance(checks_rule, dict)
    assert isinstance(ref_condition, dict)
    raw_checks = checks_rule.get("required_status_checks")
    check_names = (
        [str(item.get("context")) for item in raw_checks if isinstance(item, dict)]
        if isinstance(raw_checks, list)
        else []
    )
    required = sorted(REQUIRED_STATUS_CHECKS)
    target_ref = f"refs/heads/{expected_base_ref}"
    include = ref_condition.get("include")
    required_approval_count = pull_rule.get("required_approving_review_count")
    ruleset_valid = (
        ruleset.get("id") == RULESET_ID
        and ruleset.get("target") == "branch"
        and ruleset.get("enforcement") == "active"
        and ruleset.get("bypass_actors") == []
        and isinstance(include, list)
        and include == [target_ref]
        and sorted(check_names) == required
        and len(check_names) == len(required)
        and checks_rule.get("strict_required_status_checks_policy") is True
        and isinstance(required_approval_count, int)
        and required_approval_count >= 1
        and pull_rule.get("dismiss_stale_reviews_on_push") is True
        and pull_rule.get("require_code_owner_review") is True
        and pull_rule.get("required_review_thread_resolution") is True
    )
    base = pull.get("base")
    head = pull.get("head")
    pr_valid = (
        pull.get("number") == pr_number
        and pull.get("state") == "open"
        and pull.get("draft") is True
        and pull.get("merged") is False
        and isinstance(base, dict)
        and isinstance(head, dict)
        and base.get("ref") == expected_base_ref
        and base.get("sha") == expected_base_sha
        and head.get("ref") == expected_head_ref
        and head.get("sha") == expected_head_sha
        and isinstance(base.get("repo"), dict)
        and isinstance(head.get("repo"), dict)
        and base["repo"].get("full_name") == repository
        and head["repo"].get("full_name") == repository
    )
    if not ruleset_valid or not pr_valid:
        raise FactoryFailure(
            "FAIL_GOVERNANCE_MISMATCH",
            "Authoritative GitHub ruleset or pull-request identity is stale or mismatched.",
            details={"ruleset_match": ruleset_valid, "pull_request_match": pr_valid},
        )
    return GateResult(
        gate="governance_readback",
        result="PASS",
        message="Authoritative GitHub ruleset and draft PR identity verified read-only.",
        details={
            "api_host": _GITHUB_API_HOST,
            "repository": repository,
            "ruleset_id": RULESET_ID,
            "enforcement": "active",
            "target_ref": target_ref,
            "required_status_checks": required,
            "required_approving_review_count": required_approval_count,
            "dismiss_stale_reviews_on_push": True,
            "require_code_owner_review": True,
            "required_review_thread_resolution": True,
            "bypass_actor_count": 0,
            "pr_number": pr_number,
            "pr_state": "open",
            "pr_draft": True,
            "pr_merged": False,
            "base_ref": expected_base_ref,
            "base_sha": expected_base_sha,
            "head_ref": expected_head_ref,
            "head_sha": expected_head_sha,
            "retrieval_context": {"github_actions_run_id": run_id},
            "github_approving_review_claimed": False,
        },
    )


def validate_approval_and_ruleset(
    *,
    approval_digest: str,
    reviewed_commit: str,
    current_commit: str,
    ruleset: Mapping[str, object],
) -> GateResult:
    """Fail closed on stale approval/review or non-exact source protection."""

    if approval_digest != APPROVED_CONTRACT_SHA256:
        raise FactoryFailure("FAIL_APPROVAL_DIGEST", "Contract approval digest is stale.")
    if reviewed_commit != current_commit:
        raise FactoryFailure("FAIL_STALE_REVIEW", "Source review does not cover current commit.")
    required_checks = ruleset.get("required_status_checks")
    if (
        ruleset.get("enforcement") != "active"
        or ruleset.get("target") != "refs/heads/v3/main"
        or ruleset.get("bypass_actors") != []
        or not isinstance(required_checks, list)
        or set(required_checks) != REQUIRED_STATUS_CHECKS
        or len(required_checks) != len(REQUIRED_STATUS_CHECKS)
    ):
        raise FactoryFailure("FAIL_RULESET_MISMATCH", "Protected source ruleset is not exact.")
    return GateResult(
        gate="approval_and_ruleset",
        result="PASS",
        message="Approval, review freshness and exact ruleset verified.",
    )


def validate_external_effect_policy(environ: Mapping[str, str]) -> GateResult:
    """Reject provider targets, credential presence and outbound business actions."""

    exact = {
        "YSF_EXTERNAL_EFFECT_BUDGET": "DENY_ALL",
        "YSF_PROVIDERS": "OFF",
        "YSF_EMAIL_MODE": "NON_RELAYING",
    }
    mismatches = sorted(name for name, value in exact.items() if environ.get(name) != value)
    prohibited_presence = sorted(
        name
        for name in (
            "YSF_PROVIDER_TARGET",
            "YSF_PROVIDER_SECRET",
            "YSF_OUTBOUND_BUSINESS_ACTION",
        )
        if environ.get(name)
    )
    if mismatches or prohibited_presence:
        raise FactoryFailure(
            "FAIL_EXTERNAL_EFFECT_POLICY",
            "External-effect policy rejected a provider, secret or outbound action.",
            details={"mismatched_controls": mismatches, "prohibited_presence": prohibited_presence},
        )
    return GateResult(
        gate="external_effect_policy",
        result="PASS",
        message="No provider target, secret or outbound business action is enabled.",
    )
