from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path
from typing import Any

import yaml

from ysf.core.result import CommandResult

BASELINE_DIRECTORY = Path(
    "factory/config/local-infra"
)
COMPOSE_FILE = BASELINE_DIRECTORY / "compose.yaml"
ENV_EXAMPLE_FILE = BASELINE_DIRECTORY / ".env.example"

EXPECTED_SERVICES = {
    "postgres": {
        "volume": "ysim-postgres-data",
        "imageVariable": "YSIM_POSTGRES_IMAGE",
    },
    "redis": {
        "volume": "ysim-redis-data",
        "imageVariable": "YSIM_REDIS_IMAGE",
    },
    "minio": {
        "volume": "ysim-minio-data",
        "imageVariable": "YSIM_MINIO_IMAGE",
    },
    "mailpit": {
        "volume": "ysim-mailpit-data",
        "imageVariable": "YSIM_MAILPIT_IMAGE",
    },
}

REQUIRED_ENVIRONMENT_KEYS = {
    "YSIM_INFRA_PROJECT",
    "YSIM_POSTGRES_IMAGE",
    "YSIM_POSTGRES_HOST_PORT",
    "YSIM_POSTGRES_DB",
    "YSIM_POSTGRES_USER",
    "YSIM_POSTGRES_PASSWORD",
    "YSIM_REDIS_IMAGE",
    "YSIM_REDIS_HOST_PORT",
    "YSIM_MINIO_IMAGE",
    "YSIM_MINIO_API_HOST_PORT",
    "YSIM_MINIO_CONSOLE_HOST_PORT",
    "YSIM_MINIO_ROOT_USER",
    "YSIM_MINIO_ROOT_PASSWORD",
    "YSIM_MINIO_BUCKET",
    "YSIM_MAILPIT_IMAGE",
    "YSIM_MAILPIT_SMTP_HOST_PORT",
    "YSIM_MAILPIT_HTTP_HOST_PORT",
}


def _load_yaml(path: Path) -> dict[str, Any]:
    loaded = yaml.safe_load(
        path.read_text(encoding="utf-8")
    )

    if not isinstance(loaded, dict):
        msg = f"{path} must contain a YAML mapping."
        raise ValueError(msg)

    return loaded


def _parse_environment_keys(path: Path) -> set[str]:
    keys: set[str] = set()

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue

        key, separator, _value = stripped.partition("=")

        if separator:
            keys.add(key)

    return keys


def _has_named_volume_mount(
    service: dict[str, Any],
    expected_volume: str,
) -> bool:
    volumes = service.get("volumes", [])

    if not isinstance(volumes, list):
        return False

    return any(
        isinstance(volume, str)
        and volume.startswith(f"{expected_volume}:")
        for volume in volumes
    )


def _uses_environment_image(
    service: dict[str, Any],
    image_variable: str,
) -> bool:
    image = service.get("image")

    if not isinstance(image, str):
        return False

    return image.startswith(f"${{{image_variable}:-")


def _has_healthcheck(
    service: dict[str, Any],
) -> bool:
    healthcheck = service.get("healthcheck")

    if not isinstance(healthcheck, dict):
        return False

    test = healthcheck.get("test")

    return (
        isinstance(test, list)
        and len(test) >= 2
        and "interval" in healthcheck
        and "timeout" in healthcheck
        and "retries" in healthcheck
    )


def _static_checks(
    repository_root: Path,
) -> list[dict[str, Any]]:
    compose_path = repository_root / COMPOSE_FILE
    env_example_path = repository_root / ENV_EXAMPLE_FILE
    checks: list[dict[str, Any]] = []

    checks.append({
        "name": "compose-file-exists",
        "status": "PASS" if compose_path.is_file() else "FAIL",
        "path": str(COMPOSE_FILE),
    })

    checks.append({
        "name": "env-example-exists",
        "status": "PASS" if env_example_path.is_file() else "FAIL",
        "path": str(ENV_EXAMPLE_FILE),
    })

    if not compose_path.is_file() or not env_example_path.is_file():
        return checks

    compose = _load_yaml(compose_path)
    services = compose.get("services", {})
    volumes = compose.get("volumes", {})

    checks.append({
        "name": "services-mapping",
        "status": "PASS" if isinstance(services, dict) else "FAIL",
    })

    checks.append({
        "name": "volumes-mapping",
        "status": "PASS" if isinstance(volumes, dict) else "FAIL",
    })

    if not isinstance(services, dict) or not isinstance(volumes, dict):
        return checks

    for service_name, expectation in EXPECTED_SERVICES.items():
        service = services.get(service_name)
        service_mapping = (
            service
            if isinstance(service, dict)
            else {}
        )

        checks.append({
            "name": f"{service_name}-service-defined",
            "status": "PASS" if service_mapping else "FAIL",
        })

        checks.append({
            "name": f"{service_name}-image-convention",
            "status": (
                "PASS"
                if _uses_environment_image(
                    service_mapping,
                    expectation["imageVariable"],
                )
                else "FAIL"
            ),
        })

        checks.append({
            "name": f"{service_name}-healthcheck",
            "status": (
                "PASS"
                if _has_healthcheck(service_mapping)
                else "FAIL"
            ),
        })

        volume_name = expectation["volume"]

        checks.append({
            "name": f"{service_name}-named-volume",
            "status": (
                "PASS"
                if volume_name in volumes
                and _has_named_volume_mount(
                    service_mapping,
                    volume_name,
                )
                else "FAIL"
            ),
        })

    env_keys = _parse_environment_keys(env_example_path)
    missing_env_keys = sorted(
        REQUIRED_ENVIRONMENT_KEYS - env_keys
    )

    checks.append({
        "name": "environment-conventions",
        "status": (
            "PASS"
            if not missing_env_keys
            else "FAIL"
        ),
        "missing": missing_env_keys,
    })

    image_tags = [
        service.get("image")
        for service in services.values()
        if isinstance(service, dict)
    ]
    mutable_image_tags = [
        image
        for image in image_tags
        if isinstance(image, str)
        and re.search(r":(?:latest)?\}", image)
    ]

    checks.append({
        "name": "no-latest-images",
        "status": (
            "PASS"
            if not mutable_image_tags
            else "FAIL"
        ),
        "mutableImages": mutable_image_tags,
    })

    return checks


def _compose_config_check(
    repository_root: Path,
    env_file: Path,
) -> dict[str, Any]:
    compose_path = repository_root / COMPOSE_FILE
    command = [
        "docker",
        "compose",
        "--env-file",
        str(env_file),
        "-f",
        str(compose_path),
        "config",
        "--quiet",
    ]
    environment = {
        **os.environ,
        "COMPOSE_PROJECT_NAME": "ysim-local-foundation-verify",
    }

    process = subprocess.run(
        command,
        cwd=repository_root,
        capture_output=True,
        text=True,
        check=False,
        env=environment,
    )

    return {
        "name": "docker-compose-config",
        "status": "PASS" if process.returncode == 0 else "FAIL",
        "exitCode": process.returncode,
        "command": command,
        "stdout": process.stdout.strip(),
        "stderr": process.stderr.strip(),
    }


def verify_local_infra(
    repository_root: Path,
    runtime: bool = False,
) -> CommandResult:
    checks = _static_checks(repository_root)

    if runtime:
        env_file = repository_root / ENV_EXAMPLE_FILE
        checks.append(
            _compose_config_check(
                repository_root,
                env_file,
            )
        )

    failed_checks = [
        check["name"]
        for check in checks
        if check["status"] != "PASS"
    ]
    status = "PASS" if not failed_checks else "FAIL"

    return CommandResult(
        command="local-infra",
        status=status,
        message=(
            "Local infrastructure baseline is valid."
            if status == "PASS"
            else "Local infrastructure baseline is invalid."
        ),
        data={
            "composeFile": str(COMPOSE_FILE),
            "environmentExample": str(ENV_EXAMPLE_FILE),
            "runtime": runtime,
            "checkCount": len(checks),
            "failedCheckCount": len(failed_checks),
            "failedChecks": failed_checks,
            "checks": checks,
        },
    )
