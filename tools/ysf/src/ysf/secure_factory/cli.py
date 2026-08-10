"""Command-line orchestration for the V3-R1 G00-S00 secure factory."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import uuid
from collections.abc import Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ysf.secure_factory.candidate import (
    build_candidate,
    verify_candidate,
    verify_declared_dependency_closure,
)
from ysf.secure_factory.environment import (
    load_expectation,
    observe_environment,
    validate_candidate_build_environment,
    validate_environment,
)
from ysf.secure_factory.evidence import EvidenceLedger
from ysf.secure_factory.models import FactoryFailure, GateResult
from ysf.secure_factory.policy import (
    APPROVED_CONTRACT_SHA256,
    CONTRACT_RELATIVE_PATH,
    QUARANTINED_FIXTURES,
    mutation_paths,
    validate_approval_and_ruleset,
    validate_changed_paths,
    validate_external_effect_policy,
    validate_relative_path,
    verify_approved_contract,
    verify_immutable_corpus,
    verify_policy_self_protection,
)
from ysf.secure_factory.sensitive import require_no_sensitive_values, scan_path

CONTRACT_SHA256 = APPROVED_CONTRACT_SHA256


def _repository_root() -> Path:
    process = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=False,
        capture_output=True,
        text=True,
    )
    if process.returncode != 0:
        raise FactoryFailure("FAIL_REPOSITORY_ROOT", "Not inside the YSim repository.")
    return Path(process.stdout.strip()).resolve(strict=True)


def _execution_id(mode: str) -> str:
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    return f"V3-R1-G00-S00-{mode.upper()}-{timestamp}-{uuid.uuid4().hex[:8].upper()}"


def _default_output_root() -> Path:
    return Path(tempfile.mkdtemp(prefix="ysim-v3-r1-s00-output."))


def _preflight(repository_root: Path, *, candidate_build: bool = False) -> list[GateResult]:
    context = repository_root / "docs/v3/r1/g00/s00"
    expected = load_expectation(context / "environment-identity.yaml")
    if candidate_build:
        identity_gate = validate_candidate_build_environment(expected, repository_root)
    else:
        identity_gate = validate_environment(expected, observe_environment(repository_root))
    results = [identity_gate]
    results.append(verify_policy_self_protection(context / "source-and-delivery-policy.md"))
    results.append(verify_approved_contract(repository_root))
    paths = mutation_paths(repository_root, base_ref="origin/v3/main")
    results.append(validate_changed_paths(repository_root, paths))
    results.append(verify_immutable_corpus(repository_root))
    scan_inputs = [
        repository_root / path
        for path in sorted(paths - QUARANTINED_FIXTURES)
        if (repository_root / path).is_file()
    ]
    results.append(require_no_sensitive_values(scan_inputs))
    return results


def _known_bad(repository_root: Path) -> list[GateResult]:
    fixture_root = repository_root / "tools/ysf/tests/fixtures/secure_factory/noncompliant"
    results: list[GateResult] = []
    path_record = json.loads((fixture_root / "path-escape.json").read_text(encoding="utf-8"))
    try:
        validate_relative_path(str(path_record["path"]))
    except FactoryFailure as exc:
        if exc.code != "FAIL_PATH_ESCAPE":
            raise
        results.append(GateResult("known_bad_path_escape", "PASS", "Path escape rejected."))
    else:
        raise FactoryFailure("FAIL_KNOWN_BAD_ACCEPTED", "Path-escape fixture was accepted.")
    for filename, gate, required_kinds in (
        ("synthetic-secret.txt", "known_bad_secret", {"SECRET_VALUE", "PII_EMAIL"}),
        (
            "synthetic-esim-payload.txt",
            "known_bad_esim",
            {"ICCID", "LPA", "QR_PAYLOAD"},
        ),
    ):
        kinds = {item.kind for item in scan_path(fixture_root / filename)}
        if not required_kinds.issubset(kinds):
            raise FactoryFailure(
                "FAIL_KNOWN_BAD_ACCEPTED",
                "Sensitive known-bad fixture did not trigger every required detector.",
                details={"fixture": filename, "observed_kinds": sorted(kinds)},
            )
        results.append(GateResult(gate, "PASS", "Sensitive fixture rejected safely."))
    tampered = json.loads((fixture_root / "tampered-manifest.json").read_text(encoding="utf-8"))
    if tampered.get("sha256") == "0" * 64:
        results.append(
            GateResult("known_bad_tampered_manifest", "PASS", "Tampered manifest rejected.")
        )
    else:
        raise FactoryFailure("FAIL_KNOWN_BAD_FIXTURE", "Tampered manifest fixture is invalid.")
    return results


def _commit_timestamp(repository_root: Path) -> int:
    process = subprocess.run(
        ["git", "show", "-s", "--format=%ct", "HEAD"],
        cwd=repository_root,
        check=False,
        capture_output=True,
        text=True,
    )
    if process.returncode != 0 or not process.stdout.strip().isdigit():
        raise FactoryFailure("FAIL_COMMIT_TIMESTAMP", "Candidate commit timestamp is unavailable.")
    return int(process.stdout.strip())


def _identity(repository_root: Path) -> tuple[str, str, str]:
    expectation = load_expectation(repository_root / "docs/v3/r1/g00/s00/environment-identity.yaml")
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repository_root,
        check=False,
        capture_output=True,
        text=True,
    )
    tree = subprocess.run(
        ["git", "rev-parse", "HEAD^{tree}"],
        cwd=repository_root,
        check=False,
        capture_output=True,
        text=True,
    )
    if commit.returncode != 0 or tree.returncode != 0:
        raise FactoryFailure(
            "FAIL_CANDIDATE_SOURCE_IDENTITY",
            "Candidate source commit or tree is unavailable.",
        )
    return expectation.repository, commit.stdout.strip(), tree.stdout.strip()


def _expected_rejection(name: str, code: str, operation: Any) -> GateResult:
    try:
        operation()
    except FactoryFailure as exc:
        if exc.code != code:
            raise FactoryFailure(
                "FAIL_RP_C_MATRIX_CODE",
                "RP-C negative scenario returned an unexpected failure code.",
                details={"scenario": name, "observed_code": exc.code},
            ) from exc
        return GateResult(name, "PASS", f"Expected rejection preserved: {code}.")
    raise FactoryFailure(
        "FAIL_RP_C_MATRIX_ACCEPTED",
        "RP-C negative scenario was accepted.",
        details={"scenario": name},
    )


def _rp_c_matrix(repository_root: Path) -> list[GateResult]:
    """Execute synthetic fail-closed security cases without external effects."""

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
    safe_effects = {
        "YSF_EXTERNAL_EFFECT_BUDGET": "DENY_ALL",
        "YSF_PROVIDERS": "OFF",
        "YSF_EMAIL_MODE": "NON_RELAYING",
    }
    results = _known_bad(repository_root)
    results.append(
        _expected_rejection(
            "stale_approval",
            "FAIL_APPROVAL_DIGEST",
            lambda: validate_approval_and_ruleset(
                approval_digest="0" * 64,
                reviewed_commit="a" * 40,
                current_commit="a" * 40,
                ruleset=ruleset,
            ),
        )
    )
    results.append(
        _expected_rejection(
            "stale_review",
            "FAIL_STALE_REVIEW",
            lambda: validate_approval_and_ruleset(
                approval_digest=CONTRACT_SHA256,
                reviewed_commit="a" * 40,
                current_commit="b" * 40,
                ruleset=ruleset,
            ),
        )
    )
    mismatched_ruleset = dict(ruleset)
    mismatched_ruleset["required_status_checks"] = ["S00 / policy"]
    results.append(
        _expected_rejection(
            "ruleset_mismatch",
            "FAIL_RULESET_MISMATCH",
            lambda: validate_approval_and_ruleset(
                approval_digest=CONTRACT_SHA256,
                reviewed_commit="a" * 40,
                current_commit="a" * 40,
                ruleset=mismatched_ruleset,
            ),
        )
    )
    for key, name in (
        ("YSF_PROVIDER_TARGET", "provider_target_present"),
        ("YSF_PROVIDER_SECRET", "secret_present"),
        ("YSF_OUTBOUND_BUSINESS_ACTION", "outbound_business_action"),
    ):
        controls = {**safe_effects, key: "SYNTHETIC_PRESENT"}
        results.append(
            _expected_rejection(
                name,
                "FAIL_EXTERNAL_EFFECT_POLICY",
                lambda controls=controls: validate_external_effect_policy(controls),
            )
        )
    lock_paths = (
        repository_root / "tools/ysf/requirements-s00-build.lock",
        repository_root / "tools/ysf/requirements-s00-dev.lock",
    )
    with tempfile.TemporaryDirectory(prefix="ysim-v3-r1-s00-rpc-matrix.") as temporary:
        declaration = Path(temporary) / "pyproject.toml"
        declaration.write_text(
            "[build-system]\nrequires=['setuptools==83.0.0']\n"
            "[project]\nname='synthetic'\nversion='0'\ndependencies=['absent-package==1.0']\n"
            "[project.optional-dependencies]\ndev=[]\n",
            encoding="utf-8",
        )
        results.append(
            _expected_rejection(
                "undeclared_dependency",
                "FAIL_DEPENDENCY_CLOSURE",
                lambda: verify_declared_dependency_closure(declaration, lock_paths),
            )
        )
    validate_external_effect_policy(safe_effects)
    results.append(
        GateResult(
            "rp_c_matrix_complete",
            "PASS",
            "All synthetic negative cases failed closed with no business external effect.",
            details={"scenario_count": len(results)},
        )
    )
    return results


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ysf-secure-factory")
    parser.add_argument(
        "mode",
        choices=(
            "preflight",
            "verify",
            "known-bad",
            "build-candidate",
            "verify-candidate",
            "rp-c-matrix",
        ),
    )
    parser.add_argument("candidate_path", nargs="?")
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--execution-id")
    parser.add_argument("--json", action="store_true")
    return parser


def _emit(payload: dict[str, Any], *, as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, sort_keys=True, ensure_ascii=True))
        return
    for key, value in payload.items():
        if isinstance(value, (str, int)):
            print(f"{key.upper()}={value}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)
    repository_root: Path | None = None
    ledger: EvidenceLedger | None = None
    try:
        repository_root = _repository_root()
        output_root = args.output_root or _default_output_root()
        execution_id = args.execution_id or _execution_id(args.mode)
        ledger = EvidenceLedger(output_root, repository_root, execution_id)
        ledger.append(
            {
                "execution_id": execution_id,
                "contract_sha256": CONTRACT_SHA256,
                "command_or_gate": args.mode,
                "mutation_class": "GENERATED_OUTPUT_OUTSIDE_GIT_CHECKOUT_ONLY",
                "result": "STARTED",
            }
        )
        gates: list[GateResult]
        if args.mode == "preflight" or args.mode == "verify":
            gates = _preflight(repository_root)
        elif args.mode == "known-bad":
            gates = _known_bad(repository_root)
        elif args.mode == "build-candidate":
            gates = _preflight(repository_root, candidate_build=True)
            quality_root_value = os.environ.get("YSF_S00_QUALITY_ROOT", "")
            if not quality_root_value:
                raise FactoryFailure(
                    "FAIL_CANDIDATE_REPORT_BUNDLE",
                    "Candidate quality report root was not supplied by CI.",
                )
            repository, commit, tree = _identity(repository_root)
            expectation = load_expectation(
                repository_root / "docs/v3/r1/g00/s00/environment-identity.yaml"
            )
            paths = mutation_paths(repository_root, base_ref="origin/v3/main")
            candidate_path = ledger.directory / "candidate"
            gates.append(
                build_candidate(
                    repository_root,
                    candidate_path,
                    repository=repository,
                    branch=expectation.branch,
                    commit=commit,
                    tree=tree,
                    contract_sha256=CONTRACT_SHA256,
                    source_date_epoch=_commit_timestamp(repository_root),
                    gate_report={
                        "changed_paths": sorted(paths),
                        "gates": [gate.to_dict() for gate in gates],
                    },
                    report_root=Path(quality_root_value),
                )
            )
        elif args.mode == "verify-candidate":
            if not args.candidate_path:
                parser.error("verify-candidate requires candidate_path")
            repository, commit, tree = _identity(repository_root)
            expectation = load_expectation(
                repository_root / "docs/v3/r1/g00/s00/environment-identity.yaml"
            )
            gates = [
                verify_candidate(
                    Path(args.candidate_path),
                    expected_repository=repository,
                    expected_branch=expectation.branch,
                    expected_commit=commit,
                    expected_tree=tree,
                    expected_contract_sha256=CONTRACT_SHA256,
                    expected_contract_path=repository_root / CONTRACT_RELATIVE_PATH,
                    expected_lock_paths=(
                        repository_root / "tools/ysf/requirements-s00-build.lock",
                        repository_root / "tools/ysf/requirements-s00-dev.lock",
                    ),
                    expected_changed_paths=mutation_paths(
                        repository_root, base_ref="origin/v3/main"
                    ),
                )
            ]
        else:
            gates = _rp_c_matrix(repository_root)
        payload = {
            "execution_id": execution_id,
            "result": "PASS",
            "mode": args.mode,
            "evidence_directory": str(ledger.directory),
            "gates": [gate.to_dict() for gate in gates],
            "next_allowed_action": "HUMAN_REVIEW",
        }
        ledger.write_json("result.json", payload)
        ledger.append(
            {
                "execution_id": execution_id,
                "command_or_gate": args.mode,
                "exit_code": 0,
                "result": "PASS",
                "next_allowed_action": "HUMAN_REVIEW",
            }
        )
        _emit(payload, as_json=args.json)
        return 0
    except FactoryFailure as exc:
        payload = {
            "result": "FAIL",
            "failure_code": exc.code,
            "message": exc.safe_message,
            "details": exc.details,
            "next_allowed_action": "STOP_AND_REVIEW",
        }
        if ledger is not None:
            ledger.append(
                {
                    "command_or_gate": args.mode,
                    "exit_code": 1,
                    "result": "FAIL",
                    "failure_code": exc.code,
                    "next_allowed_action": "STOP_AND_REVIEW",
                }
            )
            payload["evidence_directory"] = str(ledger.directory)
        _emit(payload, as_json=args.json)
        return 1


if __name__ == "__main__":
    sys.exit(main())
