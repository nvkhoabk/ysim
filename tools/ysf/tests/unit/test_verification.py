from pathlib import Path
from unittest.mock import patch

from ysf.core.result import CommandResult
from ysf.verification.service import (
    run_verification,
)


def test_verification_passes(
    tmp_path: Path,
) -> None:
    successful_process = {
        "name": "check",
        "status": "PASS",
        "exitCode": 0,
        "command": [],
        "workingDirectory": str(
            tmp_path
        ),
        "stdout": "",
        "stderr": "",
    }

    successful_result = CommandResult(
        command="test",
        status="PASS",
        message="Passed.",
    )

    with (
        patch(
            "ysf.verification.service."
            "run_doctor",
            return_value=successful_result,
        ),
        patch(
            "ysf.verification.service."
            "run_pipeline",
            return_value=successful_result,
        ),
        patch(
            "ysf.verification.service."
            "run_process",
            return_value=successful_process,
        ),
        patch(
            "ysf.verification.service."
            "validate_traceability_baseline",
            return_value={"requirement_count": 86},
        ),
    ):
        result = run_verification(
            tmp_path
        )

    assert result.successful
    assert (
        result.data["failedCheckCount"]
        == 0
    )
