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

from ysf.secure_factory.candidate import build_candidate, verify_candidate
from ysf.secure_factory.environment import (
    load_expectation,
    observe_environment,
    validate_candidate_build_environment,
    validate_environment,
)
from ysf.secure_factory.evidence import EvidenceLedger
from ysf.secure_factory.models import FactoryFailure, GateResult
from ysf.secure_factory.policy import (
    QUARANTINED_FIXTURES,
    mutation_paths,
    validate_changed_paths,
    validate_relative_path,
    verify_immutable_corpus,
    verify_policy_self_protection,
)
from ysf.secure_factory.sensitive import require_no_sensitive_values, scan_path

CONTRACT_SHA256 = "337519fcf7d08104ba0e53cbf33dcc4b4a75ec32aac18601cb097c778aa0ae35"


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
    paths = mutation_paths(repository_root)
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
            candidate_path = ledger.directory / "candidate"
            gates.append(
                build_candidate(
                    repository_root,
                    candidate_path,
                    repository=repository,
                    commit=commit,
                    tree=tree,
                    contract_sha256=CONTRACT_SHA256,
                    source_date_epoch=_commit_timestamp(repository_root),
                    gate_report={"gates": [gate.to_dict() for gate in gates]},
                    report_root=Path(quality_root_value),
                )
            )
        else:
            if not args.candidate_path:
                parser.error("verify-candidate requires candidate_path")
            gates = [verify_candidate(Path(args.candidate_path))]
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
