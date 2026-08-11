from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any

from ysf.core.doctor import run_doctor
from ysf.core.result import CommandResult
from ysf.pipeline.service import run_pipeline
from ysf.secure_factory.models import FactoryFailure
from ysf.traceability.validator import validate_traceability_baseline


def run_process(
    name: str,
    command: list[str],
    working_directory: Path,
) -> dict[str, Any]:
    process = subprocess.run(
        command,
        cwd=working_directory,
        capture_output=True,
        text=True,
        check=False,
    )

    stdout = process.stdout.strip()
    stderr = process.stderr.strip()

    return {
        "name": name,
        "status": (
            "PASS"
            if process.returncode == 0
            else "FAIL"
        ),
        "exitCode": process.returncode,
        "command": command,
        "workingDirectory": str(
            working_directory
        ),
        "stdout": stdout,
        "stderr": stderr,
    }


def run_verification(
    repository_root: Path,
) -> CommandResult:
    ysf_root = (
        repository_root
        / "tools"
        / "ysf"
    )

    checks: list[dict[str, Any]] = []

    try:
        traceability = validate_traceability_baseline(repository_root)
        checks.append(
            {
                "name": "traceability",
                "status": "PASS",
                "exitCode": 0,
                "data": traceability,
            }
        )
    except FactoryFailure as exc:
        checks.append(
            {
                "name": "traceability",
                "status": "FAIL",
                "exitCode": 3,
                "data": {"code": exc.code, "details": exc.details},
            }
        )

    doctor_result = run_doctor(
        repository_root
    )

    checks.append({
        "name": "doctor",
        "status": doctor_result.status,
        "exitCode": (
            0
            if doctor_result.successful
            else 1
        ),
        "data": doctor_result.data,
    })

    checks.append(
        run_process(
            name="ruff",
            command=[
                sys.executable,
                "-m",
                "ruff",
                "check",
                "src",
                "tests",
            ],
            working_directory=ysf_root,
        )
    )

    checks.append(
        run_process(
            name="mypy",
            command=[
                sys.executable,
                "-m",
                "mypy",
                "src",
            ],
            working_directory=ysf_root,
        )
    )

    checks.append(
        run_process(
            name="pytest",
            command=[
                sys.executable,
                "-m",
                "pytest",
                "-q",
            ],
            working_directory=ysf_root,
        )
    )

    pipeline_result = run_pipeline(
        repository_root=repository_root,
        fail_fast=True,
    )

    checks.append({
        "name": "pipeline",
        "status": pipeline_result.status,
        "exitCode": (
            0
            if pipeline_result.successful
            else 1
        ),
        "data": pipeline_result.data,
    })

    checks.append(
        run_process(
            name="git-diff-check",
            command=[
                "git",
                "diff",
                "--check",
            ],
            working_directory=repository_root,
        )
    )

    failed_checks = [
        check["name"]
        for check in checks
        if check["status"] != "PASS"
    ]

    status = (
        "PASS"
        if not failed_checks
        else "FAIL"
    )

    return CommandResult(
        command="verify",
        status=status,
        message=(
            "YSF verification completed successfully."
            if status == "PASS"
            else "YSF verification failed."
        ),
        data={
            "checkCount": len(checks),
            "failedCheckCount": len(
                failed_checks
            ),
            "failedChecks": failed_checks,
            "checks": checks,
        },
    )
