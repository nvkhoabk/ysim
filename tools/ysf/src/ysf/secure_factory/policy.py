"""Exact-allowlist, immutable-corpus, and path-safety policy."""

from __future__ import annotations

import hashlib
import http.client
import json
import os
import re
import subprocess
from collections.abc import Callable, Iterable, Mapping
from datetime import UTC, datetime, timedelta
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
_GOVERNANCE_ATTESTATION_MARKER = "<!-- ysim-s00-governance-attestation:v1 -->"
_GOVERNANCE_ATTESTATION_SCHEMA = "ysim.s00.governance-attestation.v1"
_GOVERNANCE_ATTESTATION_MAX_BYTES = 8192
_GOVERNANCE_ATTESTATION_MAX_AGE = timedelta(hours=24)
_GOVERNANCE_ATTESTOR_LOGIN = "nvkhoabk"
_GOVERNANCE_ATTESTOR_ID = 22950753
_EMPTY_ARRAY_SHA256 = (
    "sha256:4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"
)
_DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")


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


def _github_json(path: str) -> Any:
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
    if not isinstance(value, (dict, list)):
        raise FactoryFailure(
            "FAIL_GOVERNANCE_READBACK",
            "Authoritative GitHub governance metadata is invalid.",
        )
    return value


def _canonical_json(value: object) -> bytes:
    return json.dumps(
        value, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def _prefixed_digest(value: object) -> str:
    return "sha256:" + hashlib.sha256(_canonical_json(value)).hexdigest()


def _ruleset_components(
    ruleset: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
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
    return pull_rule, checks_rule, ref_condition


def observable_ruleset_evidence(ruleset: Mapping[str, Any]) -> dict[str, Any]:
    """Return only stable ruleset fields observable to the PR workflow."""

    pull_rule, checks_rule, ref_condition = _ruleset_components(ruleset)
    raw_checks = checks_rule.get("required_status_checks")
    checks = (
        sorted(
            str(item.get("context"))
            for item in raw_checks
            if isinstance(item, dict)
        )
        if isinstance(raw_checks, list)
        else []
    )
    return {
        "schema": "ysim.s00.observable-ruleset.v1",
        "ruleset_id": ruleset.get("id"),
        "target": ruleset.get("target"),
        "enforcement": ruleset.get("enforcement"),
        "updated_at": ruleset.get("updated_at"),
        "ref_include": ref_condition.get("include"),
        "ref_exclude": ref_condition.get("exclude"),
        "required_status_checks": checks,
        "strict_required_status_checks_policy": checks_rule.get(
            "strict_required_status_checks_policy"
        ),
        "required_approving_review_count": pull_rule.get(
            "required_approving_review_count"
        ),
        "dismiss_stale_reviews_on_push": pull_rule.get(
            "dismiss_stale_reviews_on_push"
        ),
        "require_code_owner_review": pull_rule.get("require_code_owner_review"),
        "required_review_thread_resolution": pull_rule.get(
            "required_review_thread_resolution"
        ),
    }


def full_ruleset_evidence(ruleset: Mapping[str, Any]) -> dict[str, Any]:
    """Normalize a privileged ruleset readback without retaining actor details."""

    bypass = ruleset.get("bypass_actors")
    if "bypass_actors" not in ruleset or not isinstance(bypass, list) or bypass:
        raise FactoryFailure(
            "FAIL_GOVERNANCE_FULL_READBACK",
            "Privileged ruleset readback does not prove an empty bypass actor set.",
        )
    return {
        "schema": "ysim.s00.full-ruleset.v1",
        "observable": observable_ruleset_evidence(ruleset),
        "bypass_actors": [],
    }


def build_governance_attestation_payload(
    *,
    ruleset: Mapping[str, Any],
    repository: str,
    pr_number: int,
    base_sha: str,
    head_sha: str,
    head_tree: str,
    retrieved_at: str,
) -> dict[str, Any]:
    """Build the deterministic payload from a fresh privileged readback."""

    observable = observable_ruleset_evidence(ruleset)
    full = full_ruleset_evidence(ruleset)
    payload: dict[str, Any] = {
        "schema": _GOVERNANCE_ATTESTATION_SCHEMA,
        "repository": repository,
        "pr_number": pr_number,
        "base_sha": base_sha,
        "head_sha": head_sha,
        "head_tree": head_tree,
        "ruleset_id": RULESET_ID,
        "ruleset_updated_at": ruleset.get("updated_at"),
        "observable_ruleset_sha256": _prefixed_digest(observable),
        "full_ruleset_sha256": _prefixed_digest(full),
        "bypass_actors_count": 0,
        "bypass_actors_sha256": _EMPTY_ARRAY_SHA256,
        "retrieved_at": retrieved_at,
    }
    payload["payload_sha256"] = _prefixed_digest(payload)
    return payload


def render_governance_attestation(payload: Mapping[str, Any]) -> str:
    """Render the only accepted top-level PR comment body."""

    return (
        f"{_GOVERNANCE_ATTESTATION_MARKER}\n```json\n"
        + _canonical_json(payload).decode("utf-8")
        + "\n```\n"
    )


class _AttestationInvalid(ValueError):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


def _invalid_attestation(reason: str) -> FactoryFailure:
    return FactoryFailure(
        f"FAIL_GOVERNANCE_ATTESTATION_INVALID:{reason}",
        "Human governance attestation is invalid; comment bytes are suppressed.",
    )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise _AttestationInvalid("DUPLICATE_JSON_KEY")
        value[key] = item
    return value


def _parse_attestation_body(body: object) -> dict[str, Any]:
    if not isinstance(body, str):
        raise _AttestationInvalid("COMMENT_BODY")
    if len(body.encode("utf-8")) > _GOVERNANCE_ATTESTATION_MAX_BYTES:
        raise _AttestationInvalid("COMMENT_OVERSIZED")
    prefix = f"{_GOVERNANCE_ATTESTATION_MARKER}\n```json\n"
    suffix = "\n```\n"
    if not body.startswith(prefix) or not body.endswith(suffix):
        raise _AttestationInvalid("COMMENT_ENVELOPE")
    encoded = body[len(prefix) : -len(suffix)]
    try:
        payload = json.loads(encoded, object_pairs_hook=_unique_object)
    except _AttestationInvalid:
        raise
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise _AttestationInvalid("COMMENT_JSON") from exc
    if not isinstance(payload, dict) or render_governance_attestation(payload) != body:
        raise _AttestationInvalid("COMMENT_CANONICAL")
    return payload


def _parse_utc(value: object, reason: str) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise _AttestationInvalid(reason)
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise _AttestationInvalid(reason) from exc
    if parsed.tzinfo is None:
        raise _AttestationInvalid(reason)
    return parsed.astimezone(UTC)


def _validate_attestation(
    *,
    comment: Mapping[str, Any],
    payload: Mapping[str, Any],
    observable: Mapping[str, Any],
    ruleset_updated_at: str,
    repository: str,
    pr_number: int,
    base_sha: str,
    head_sha: str,
    head_tree: str,
    head_committed_at: datetime,
    now: datetime,
) -> None:
    required_comment_fields = {
        "id",
        "body",
        "user",
        "author_association",
        "created_at",
        "updated_at",
        "issue_url",
        "html_url",
    }
    if not required_comment_fields.issubset(comment):
        raise _AttestationInvalid("COMMENT_FIELDS")
    user = comment.get("user")
    if not isinstance(comment.get("id"), int) or not isinstance(user, dict):
        raise _AttestationInvalid("COMMENT_FIELDS")
    if user.get("login") != _GOVERNANCE_ATTESTOR_LOGIN:
        raise _AttestationInvalid("AUTHOR_LOGIN")
    if user.get("id") != _GOVERNANCE_ATTESTOR_ID:
        raise _AttestationInvalid("AUTHOR_ID")
    if comment.get("author_association") != "OWNER":
        raise _AttestationInvalid("AUTHOR_ASSOCIATION")
    created_raw = comment.get("created_at")
    if created_raw != comment.get("updated_at"):
        raise _AttestationInvalid("COMMENT_EDITED")
    created_at = _parse_utc(created_raw, "COMMENT_TIMESTAMP")
    if comment.get("issue_url") != f"https://api.github.com/repos/{repository}/issues/{pr_number}":
        raise _AttestationInvalid("COMMENT_REPOSITORY_PR")
    html_prefix = f"https://github.com/{repository}/pull/{pr_number}#issuecomment-"
    if not isinstance(comment.get("html_url"), str) or not comment["html_url"].startswith(
        html_prefix
    ):
        raise _AttestationInvalid("COMMENT_REPOSITORY_PR")

    expected_keys = {
        "schema",
        "repository",
        "pr_number",
        "base_sha",
        "head_sha",
        "head_tree",
        "ruleset_id",
        "ruleset_updated_at",
        "observable_ruleset_sha256",
        "full_ruleset_sha256",
        "bypass_actors_count",
        "bypass_actors_sha256",
        "retrieved_at",
        "payload_sha256",
    }
    if set(payload) != expected_keys:
        raise _AttestationInvalid("PAYLOAD_FIELDS")
    exact = {
        "schema": _GOVERNANCE_ATTESTATION_SCHEMA,
        "repository": repository,
        "pr_number": pr_number,
        "base_sha": base_sha,
        "head_sha": head_sha,
        "head_tree": head_tree,
        "ruleset_id": RULESET_ID,
        "ruleset_updated_at": ruleset_updated_at,
    }
    if any(payload.get(key) != value for key, value in exact.items()):
        raise _AttestationInvalid("PAYLOAD_BINDING")
    if payload.get("bypass_actors_count") != 0:
        raise _AttestationInvalid("BYPASS_COUNT")
    if payload.get("bypass_actors_sha256") != _EMPTY_ARRAY_SHA256:
        raise _AttestationInvalid("BYPASS_DIGEST")
    observable_digest = _prefixed_digest(observable)
    if payload.get("observable_ruleset_sha256") != observable_digest:
        raise _AttestationInvalid("OBSERVABLE_DIGEST")
    full = {
        "schema": "ysim.s00.full-ruleset.v1",
        "observable": dict(observable),
        "bypass_actors": [],
    }
    if payload.get("full_ruleset_sha256") != _prefixed_digest(full):
        raise _AttestationInvalid("FULL_DIGEST")
    payload_digest = payload.get("payload_sha256")
    if not isinstance(payload_digest, str) or not _DIGEST.fullmatch(payload_digest):
        raise _AttestationInvalid("PAYLOAD_DIGEST")
    unsigned = dict(payload)
    del unsigned["payload_sha256"]
    if payload_digest != _prefixed_digest(unsigned):
        raise _AttestationInvalid("PAYLOAD_DIGEST")

    retrieved_at = _parse_utc(payload.get("retrieved_at"), "RETRIEVED_TIMESTAMP")
    if not (
        head_committed_at <= retrieved_at <= created_at <= now
        and created_at > head_committed_at
        and now - created_at <= _GOVERNANCE_ATTESTATION_MAX_AGE
        and now - retrieved_at <= _GOVERNANCE_ATTESTATION_MAX_AGE
    ):
        raise _AttestationInvalid("ATTESTATION_FRESHNESS")


def validate_live_governance(
    *,
    repository: str,
    pr_number: int,
    expected_base_ref: str,
    expected_base_sha: str,
    expected_head_ref: str,
    expected_head_sha: str,
    expected_head_tree: str,
    run_id: str,
    fetch_json: Callable[[str], Any] = _github_json,
    now: datetime | None = None,
) -> GateResult:
    """Validate live observable governance plus exact Human evidence if needed."""

    if (
        repository != "nvkhoabk/ysim"
        or not _REPOSITORY.fullmatch(repository)
        or pr_number <= 0
        or not run_id
        or not re.fullmatch(r"[0-9a-f]{40}", expected_base_sha)
        or not re.fullmatch(r"[0-9a-f]{40}", expected_head_sha)
        or not re.fullmatch(r"[0-9a-f]{40}", expected_head_tree)
    ):
        raise FactoryFailure(
            "FAIL_GOVERNANCE_EXPECTATION",
            "GitHub governance expectation is invalid.",
        )
    ruleset = fetch_json(f"/repos/{repository}/rulesets/{RULESET_ID}")
    pull = fetch_json(f"/repos/{repository}/pulls/{pr_number}")
    if not isinstance(ruleset, dict) or not isinstance(pull, dict):
        raise FactoryFailure(
            "FAIL_GOVERNANCE_READBACK",
            "Authoritative GitHub governance metadata is invalid.",
        )
    pull_rule, checks_rule, ref_condition = _ruleset_components(ruleset)
    raw_checks = checks_rule.get("required_status_checks")
    check_names = (
        [str(item.get("context")) for item in raw_checks if isinstance(item, dict)]
        if isinstance(raw_checks, list)
        else []
    )
    required = sorted(REQUIRED_STATUS_CHECKS)
    target_ref = f"refs/heads/{expected_base_ref}"
    include = ref_condition.get("include")
    exclude = ref_condition.get("exclude")
    required_approval_count = pull_rule.get("required_approving_review_count")
    ruleset_updated_at = ruleset.get("updated_at")
    ruleset_valid = (
        ruleset.get("id") == RULESET_ID
        and ruleset.get("target") == "branch"
        and ruleset.get("enforcement") == "active"
        and isinstance(ruleset_updated_at, str)
        and bool(ruleset_updated_at)
        and isinstance(include, list)
        and include == [target_ref]
        and exclude == []
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
    assert isinstance(ruleset_updated_at, str)

    bypass_value = ruleset.get("bypass_actors")
    if "bypass_actors" not in ruleset or bypass_value is None:
        bypass_state = "UNOBSERVABLE_UNDER_CALLER"
    elif not isinstance(bypass_value, list):
        raise FactoryFailure(
            "FAIL_GOVERNANCE_RULESET",
            "Authoritative bypass actor metadata has an invalid type.",
        )
    elif bypass_value:
        raise FactoryFailure(
            "FAIL_GOVERNANCE_BYPASS_ACTORS",
            "Authoritative ruleset has one or more bypass actors; details are suppressed.",
        )
    else:
        bypass_state = "OBSERVED_EMPTY"

    observable = observable_ruleset_evidence(ruleset)
    observable_digest = _prefixed_digest(observable)
    attestation_verified = False
    attestation_comment_id: int | None = None
    full_digest = _prefixed_digest(
        {
            "schema": "ysim.s00.full-ruleset.v1",
            "observable": observable,
            "bypass_actors": [],
        }
    )
    attestation_payload_digest: str | None = None
    if bypass_state == "UNOBSERVABLE_UNDER_CALLER":
        commit = fetch_json(f"/repos/{repository}/commits/{expected_head_sha}")
        comments = fetch_json(f"/repos/{repository}/issues/{pr_number}/comments?per_page=100")
        if not isinstance(commit, dict) or not isinstance(comments, list):
            raise _invalid_attestation("API_FIELDS")
        if len(comments) >= 100:
            raise _invalid_attestation("COMMENT_PAGE_LIMIT")
        commit_value = commit.get("commit")
        committer = commit_value.get("committer") if isinstance(commit_value, dict) else None
        if commit.get("sha") != expected_head_sha or not isinstance(committer, dict):
            raise _invalid_attestation("HEAD_COMMIT_FIELDS")
        try:
            head_committed_at = _parse_utc(
                committer.get("date"), "HEAD_COMMIT_TIMESTAMP"
            )
        except _AttestationInvalid as exc:
            raise _invalid_attestation(exc.reason) from exc

        invalid_reasons: list[str] = []
        valid: list[tuple[int, Mapping[str, Any]]] = []
        for comment in comments:
            if not isinstance(comment, dict):
                invalid_reasons.append("COMMENT_FIELDS")
                continue
            body = comment.get("body")
            if not isinstance(body, str) or _GOVERNANCE_ATTESTATION_MARKER not in body:
                continue
            try:
                payload = _parse_attestation_body(body)
                if payload.get("head_sha") != expected_head_sha:
                    continue
                _validate_attestation(
                    comment=comment,
                    payload=payload,
                    observable=observable,
                    ruleset_updated_at=ruleset_updated_at,
                    repository=repository,
                    pr_number=pr_number,
                    base_sha=expected_base_sha,
                    head_sha=expected_head_sha,
                    head_tree=expected_head_tree,
                    head_committed_at=head_committed_at,
                    now=(now or datetime.now(UTC)).astimezone(UTC),
                )
            except _AttestationInvalid as exc:
                invalid_reasons.append(exc.reason)
                continue
            comment_id = comment.get("id")
            assert isinstance(comment_id, int)
            valid.append((comment_id, payload))
        if invalid_reasons:
            raise _invalid_attestation(sorted(invalid_reasons)[0])
        if len(valid) > 1:
            raise _invalid_attestation("AMBIGUOUS_CURRENT_HEAD")
        if not valid:
            raise FactoryFailure(
                "FAIL_GOVERNANCE_ATTESTATION_REQUIRED",
                "A fresh exact-head Human governance attestation is required.",
            )
        attestation_comment_id, accepted_payload = valid[0]
        attestation_verified = True
        full_digest = str(accepted_payload["full_ruleset_sha256"])
        attestation_payload_digest = str(accepted_payload["payload_sha256"])

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
            "ruleset_updated_at": ruleset_updated_at,
            "observable_ruleset_sha256": observable_digest,
            "full_ruleset_sha256": full_digest,
            "bypass_actor_state": bypass_state,
            "bypass_actor_count": 0,
            "bypass_actors_sha256": _EMPTY_ARRAY_SHA256,
            "human_attestation_verified": attestation_verified,
            "attestation_comment_id": attestation_comment_id,
            "attestation_payload_sha256": attestation_payload_digest,
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
