from ysf.core.result import CommandResult


def test_successful_result() -> None:
    result = CommandResult(
        command="doctor",
        status="PASS",
        message="Ready",
    )

    assert result.successful is True
    assert result.to_dict()["status"] == "PASS"


def test_failed_result() -> None:
    result = CommandResult(
        command="doctor",
        status="FAIL",
        message="Not ready",
    )

    assert result.successful is False
