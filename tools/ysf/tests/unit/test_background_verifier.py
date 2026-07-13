from pathlib import Path

from ysf.background.verifier import (
    BASELINE_FILE,
    verify_background_runtime,
)


def write_background_config(
    repository_root: Path,
    production_jobs: str = "[]",
) -> None:
    path = repository_root / BASELINE_FILE
    path.parent.mkdir(parents=True)
    path.write_text(
        f"""
queueNaming:
  pattern: ysim:{{environment}}:{{capability}}:{{purpose}}
bullmq:
  connection: redis
defaults:
  attempts: 3
  timeoutMs: 30000
  concurrency: 1
  backoff:
    strategy: exponential
    delayMs: 1000
workerLifecycle:
  start: explicit
  shutdown: graceful
scheduler:
  delayed: true
  recurring: true
failedJobHandling:
  retain: true
  alertSeverity: error
observability:
  logs: true
  metrics: true
  traces: true
testQueues:
  - name: ysim:local:platform:test-lifecycle
    production: false
productionJobs: {production_jobs}
""",
        encoding="utf-8",
    )


def test_verify_background_runtime_passes_for_baseline(
    tmp_path: Path,
) -> None:
    write_background_config(tmp_path)

    result = verify_background_runtime(
        tmp_path
    )

    assert result.successful
    assert result.data["failedChecks"] == []


def test_verify_background_runtime_rejects_production_jobs(
    tmp_path: Path,
) -> None:
    write_background_config(
        tmp_path,
        production_jobs="[order-job]",
    )

    result = verify_background_runtime(
        tmp_path
    )

    assert not result.successful
    assert (
        "no-production-business-jobs"
        in result.data["failedChecks"]
    )
