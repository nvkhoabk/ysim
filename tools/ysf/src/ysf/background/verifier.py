from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from ysf.core.result import CommandResult

BASELINE_FILE = Path(
    "factory/config/background-runtime.yaml"
)

REQUIRED_TOP_LEVEL_KEYS = {
    "queueNaming",
    "bullmq",
    "defaults",
    "workerLifecycle",
    "scheduler",
    "failedJobHandling",
    "observability",
    "testQueues",
    "productionJobs",
}


def _load_yaml(
    path: Path,
) -> dict[str, Any]:
    loaded = yaml.safe_load(
        path.read_text(encoding="utf-8")
    )

    if not isinstance(loaded, dict):
        msg = f"{path} must contain a YAML mapping."
        raise ValueError(msg)

    return loaded


def verify_background_runtime(
    repository_root: Path,
) -> CommandResult:
    path = repository_root / BASELINE_FILE
    checks: list[dict[str, Any]] = [{
        "name": "background-config-exists",
        "status": "PASS" if path.is_file() else "FAIL",
        "path": str(BASELINE_FILE),
    }]

    if path.is_file():
        config = _load_yaml(path)
        missing_keys = sorted(
            REQUIRED_TOP_LEVEL_KEYS - set(config)
        )

        checks.append({
            "name": "required-sections",
            "status": (
                "PASS"
                if not missing_keys
                else "FAIL"
            ),
            "missing": missing_keys,
        })

        checks.extend(
            _policy_checks(config)
        )

    failed_checks = [
        check["name"]
        for check in checks
        if check["status"] != "PASS"
    ]
    status = "PASS" if not failed_checks else "FAIL"

    return CommandResult(
        command="background-runtime",
        status=status,
        message=(
            "Background runtime baseline is valid."
            if status == "PASS"
            else "Background runtime baseline is invalid."
        ),
        data={
            "configFile": str(BASELINE_FILE),
            "checkCount": len(checks),
            "failedCheckCount": len(failed_checks),
            "failedChecks": failed_checks,
            "checks": checks,
        },
    )


def _policy_checks(
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    production_jobs = config.get("productionJobs")
    defaults = config.get("defaults", {})
    bullmq = config.get("bullmq", {})
    observability = config.get("observability", {})
    failed = config.get("failedJobHandling", {})
    test_queues = config.get("testQueues", [])

    return [
        {
            "name": "no-production-business-jobs",
            "status": (
                "PASS"
                if production_jobs == []
                else "FAIL"
            ),
        },
        {
            "name": "redis-connection-reference",
            "status": (
                "PASS"
                if (
                    isinstance(bullmq, dict)
                    and bullmq.get("connection")
                    == "redis"
                )
                else "FAIL"
            ),
        },
        {
            "name": "retry-backoff-defaults",
            "status": (
                "PASS"
                if (
                    isinstance(defaults, dict)
                    and defaults.get("attempts", 0) >= 2
                    and isinstance(
                        defaults.get("backoff"),
                        dict,
                    )
                    and defaults["backoff"].get(
                        "strategy"
                    )
                    in {"fixed", "exponential"}
                )
                else "FAIL"
            ),
        },
        {
            "name": "failed-job-retention",
            "status": (
                "PASS"
                if (
                    isinstance(failed, dict)
                    and failed.get("retain") is True
                    and failed.get("alertSeverity")
                    in {"warning", "error", "critical"}
                )
                else "FAIL"
            ),
        },
        {
            "name": "observability-seams",
            "status": (
                "PASS"
                if (
                    isinstance(observability, dict)
                    and observability.get("logs") is True
                    and observability.get("metrics") is True
                    and observability.get("traces") is True
                )
                else "FAIL"
            ),
        },
        {
            "name": "test-only-queues",
            "status": (
                "PASS"
                if (
                    isinstance(test_queues, list)
                    and test_queues
                    and all(
                        isinstance(queue, dict)
                        and queue.get("production")
                        is False
                        for queue in test_queues
                    )
                )
                else "FAIL"
            ),
        },
    ]
