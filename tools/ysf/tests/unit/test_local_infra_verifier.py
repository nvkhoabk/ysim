from pathlib import Path

from ysf.local_infra.verifier import (
    BASELINE_DIRECTORY,
    ENV_EXAMPLE_FILE,
    verify_local_infra,
)


def write_baseline(
    repository_root: Path,
) -> None:
    baseline = (
        repository_root
        / BASELINE_DIRECTORY
    )
    baseline.mkdir(parents=True)

    (baseline / "compose.yaml").write_text(
        """
services:
  postgres:
    image: ${YSIM_POSTGRES_IMAGE:-postgres:16.4-alpine}
    volumes:
      - ysim-postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: [CMD-SHELL, pg_isready]
      interval: 10s
      timeout: 5s
      retries: 10
  redis:
    image: ${YSIM_REDIS_IMAGE:-redis:7.4-alpine}
    volumes:
      - ysim-redis-data:/data
    healthcheck:
      test: [CMD, redis-cli, ping]
      interval: 10s
      timeout: 5s
      retries: 10
  minio:
    image: ${YSIM_MINIO_IMAGE:-minio/minio:RELEASE.2024-07-16T23-46-41Z}
    volumes:
      - ysim-minio-data:/data
    healthcheck:
      test: [CMD-SHELL, curl -fsS http://localhost:9000/minio/health/live]
      interval: 10s
      timeout: 5s
      retries: 10
  mailpit:
    image: ${YSIM_MAILPIT_IMAGE:-axllent/mailpit:v1.20.5}
    volumes:
      - ysim-mailpit-data:/data
    healthcheck:
      test: [CMD-SHELL, wget -q --spider http://localhost:8025/livez]
      interval: 10s
      timeout: 5s
      retries: 10
volumes:
  ysim-postgres-data:
  ysim-redis-data:
  ysim-minio-data:
  ysim-mailpit-data:
""",
        encoding="utf-8",
    )

    (repository_root / ENV_EXAMPLE_FILE).write_text(
        """
YSIM_INFRA_PROJECT=ysim-local-foundation
YSIM_POSTGRES_IMAGE=postgres:16.4-alpine
YSIM_POSTGRES_HOST_PORT=5432
YSIM_POSTGRES_DB=ysim
YSIM_POSTGRES_USER=ysim
YSIM_POSTGRES_PASSWORD=ysim_local_password
YSIM_REDIS_IMAGE=redis:7.4-alpine
YSIM_REDIS_HOST_PORT=6379
YSIM_MINIO_IMAGE=minio/minio:RELEASE.2024-07-16T23-46-41Z
YSIM_MINIO_API_HOST_PORT=9000
YSIM_MINIO_CONSOLE_HOST_PORT=9001
YSIM_MINIO_ROOT_USER=ysim_minio
YSIM_MINIO_ROOT_PASSWORD=ysim_minio_password
YSIM_MINIO_BUCKET=ysim-local
YSIM_MAILPIT_IMAGE=axllent/mailpit:v1.20.5
YSIM_MAILPIT_SMTP_HOST_PORT=1025
YSIM_MAILPIT_HTTP_HOST_PORT=8025
""",
        encoding="utf-8",
    )


def test_verify_local_infra_passes_for_complete_baseline(
    tmp_path: Path,
) -> None:
    write_baseline(tmp_path)

    result = verify_local_infra(
        tmp_path
    )

    assert result.successful
    assert result.data["failedChecks"] == []


def test_verify_local_infra_fails_when_env_key_missing(
    tmp_path: Path,
) -> None:
    write_baseline(tmp_path)

    env_file = tmp_path / ENV_EXAMPLE_FILE
    env_file.write_text(
        env_file.read_text(encoding="utf-8").replace(
            "YSIM_MAILPIT_HTTP_HOST_PORT=8025\n",
            "",
        ),
        encoding="utf-8",
    )

    result = verify_local_infra(
        tmp_path
    )

    assert not result.successful
    assert (
        "environment-conventions"
        in result.data["failedChecks"]
    )
