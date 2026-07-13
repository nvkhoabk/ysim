from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from ysf.core.result import CommandResult

BASELINE_FILE = Path(
    "factory/config/operational-api.yaml"
)

EXPECTED_ENDPOINTS = {
    "/health": {
        "method": "GET",
        "purpose": "liveness",
        "dependencies": [],
    },
    "/ready": {
        "method": "GET",
        "purpose": "readiness",
        "dependencies": [
            "postgres",
            "redis",
            "minio",
            "required-configuration",
        ],
    },
    "/version": {
        "method": "GET",
        "purpose": "version",
        "dependencies": [],
    },
    "/openapi.json": {
        "method": "GET",
        "purpose": "api-document",
        "dependencies": [],
    },
    "/docs": {
        "method": "GET",
        "purpose": "api-document-ui",
        "dependencies": [],
    },
}

SECRET_PATTERNS = {
    "password",
    "secret",
    "token",
    "credential",
    "privateKey",
    "accessKey",
}

PROHIBITED_OPENAPI_TERMS = {
    "supplier",
    "gigago",
    "onepay",
    "gpay",
}


def _load_yaml(path: Path) -> dict[str, Any]:
    loaded = yaml.safe_load(
        path.read_text(encoding="utf-8")
    )

    if not isinstance(loaded, dict):
        msg = f"{path} must contain a YAML mapping."
        raise ValueError(msg)

    return loaded


def _endpoint_index(
    config: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    endpoints = config.get("endpoints", [])

    if not isinstance(endpoints, list):
        return {}

    return {
        endpoint["path"]: endpoint
        for endpoint in endpoints
        if isinstance(endpoint, dict)
        and isinstance(endpoint.get("path"), str)
    }


def _openapi_paths(
    document: dict[str, Any],
) -> dict[str, Any]:
    paths = document.get("paths", {})

    if not isinstance(paths, dict):
        return {}

    return paths


def verify_operational_api(
    repository_root: Path,
) -> CommandResult:
    baseline_path = repository_root / BASELINE_FILE
    checks: list[dict[str, Any]] = [{
        "name": "operational-config-exists",
        "status": (
            "PASS"
            if baseline_path.is_file()
            else "FAIL"
        ),
        "path": str(BASELINE_FILE),
    }]

    if baseline_path.is_file():
        config = _load_yaml(baseline_path)
        checks.extend(
            _baseline_checks(
                repository_root,
                config,
            )
        )

    failed_checks = [
        check["name"]
        for check in checks
        if check["status"] != "PASS"
    ]
    status = "PASS" if not failed_checks else "FAIL"

    return CommandResult(
        command="operational-api",
        status=status,
        message=(
            "Operational API baseline is valid."
            if status == "PASS"
            else "Operational API baseline is invalid."
        ),
        data={
            "configFile": str(BASELINE_FILE),
            "checkCount": len(checks),
            "failedCheckCount": len(failed_checks),
            "failedChecks": failed_checks,
            "checks": checks,
        },
    )


def _baseline_checks(
    repository_root: Path,
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    endpoints = _endpoint_index(config)

    missing_paths = sorted(
        set(EXPECTED_ENDPOINTS) - set(endpoints)
    )
    extra_paths = sorted(
        set(endpoints) - set(EXPECTED_ENDPOINTS)
    )

    checks.append({
        "name": "foundation-endpoint-set",
        "status": (
            "PASS"
            if not missing_paths and not extra_paths
            else "FAIL"
        ),
        "missing": missing_paths,
        "extra": extra_paths,
    })

    checks.extend(
        _endpoint_policy_checks(endpoints)
    )
    checks.extend(
        _readiness_policy_checks(config)
    )
    checks.extend(
        _redaction_checks(config)
    )
    checks.extend(
        _openapi_checks(
            repository_root,
            config,
        )
    )

    return checks


def _endpoint_policy_checks(
    endpoints: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    for path, expected in EXPECTED_ENDPOINTS.items():
        endpoint = endpoints.get(path, {})
        dependencies = endpoint.get("dependencies")

        checks.append({
            "name": f"{path}-method-purpose",
            "status": (
                "PASS"
                if (
                    endpoint.get("method")
                    == expected["method"]
                    and endpoint.get("purpose")
                    == expected["purpose"]
                )
                else "FAIL"
            ),
        })

        checks.append({
            "name": f"{path}-dependency-policy",
            "status": (
                "PASS"
                if dependencies
                == expected["dependencies"]
                else "FAIL"
            ),
        })

    return checks


def _readiness_policy_checks(
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    dependencies = config.get(
        "readinessDependencies",
        {},
    )
    runtime = config.get("runtime", {})

    all_required = (
        isinstance(dependencies, dict)
        and set(dependencies)
        == set(EXPECTED_ENDPOINTS["/ready"]["dependencies"])
        and all(
            isinstance(value, dict)
            and value.get("required") is True
            and isinstance(value.get("timeoutMs"), int)
            and value["timeoutMs"] <= 1000
            for value in dependencies.values()
        )
    )

    return [
        {
            "name": "readiness-required-dependencies",
            "status": (
                "PASS"
                if all_required
                else "FAIL"
            ),
        },
        {
            "name": "bounded-runtime-timeout",
            "status": (
                "PASS"
                if (
                    isinstance(runtime, dict)
                    and isinstance(
                        runtime.get("timeoutMs"),
                        int,
                    )
                    and runtime["timeoutMs"] <= 1000
                    and runtime.get("failureMode")
                    == "degraded"
                )
                else "FAIL"
            ),
        },
    ]


def _redaction_checks(
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    redaction = config.get("redaction", {})
    patterns = (
        redaction.get("denyFieldPatterns", [])
        if isinstance(redaction, dict)
        else []
    )

    return [{
        "name": "secret-redaction-policy",
        "status": (
            "PASS"
            if (
                isinstance(patterns, list)
                and SECRET_PATTERNS.issubset(
                    set(patterns)
                )
            )
            else "FAIL"
        ),
    }]


def _openapi_checks(
    repository_root: Path,
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    openapi = config.get("openapi", {})
    document_value = (
        openapi.get("document")
        if isinstance(openapi, dict)
        else None
    )
    document_path = (
        Path(document_value)
        if isinstance(document_value, str)
        else Path()
    )
    full_path = repository_root / document_path

    checks: list[dict[str, Any]] = [{
        "name": "openapi-document-exists",
        "status": (
            "PASS"
            if document_value
            and full_path.is_file()
            else "FAIL"
        ),
        "path": str(document_path),
    }]

    if not document_value or not full_path.is_file():
        return checks

    document = _load_yaml(full_path)
    paths = _openapi_paths(document)
    content = full_path.read_text(encoding="utf-8").lower()

    checks.append({
        "name": "openapi-version",
        "status": (
            "PASS"
            if str(document.get("openapi", "")).startswith("3.")
            else "FAIL"
        ),
    })

    checks.append({
        "name": "openapi-path-set",
        "status": (
            "PASS"
            if set(paths) == set(EXPECTED_ENDPOINTS)
            else "FAIL"
        ),
        "paths": sorted(paths),
    })

    checks.extend(
        _openapi_operation_checks(paths)
    )

    checks.append({
        "name": "openapi-no-prohibited-terms",
        "status": (
            "PASS"
            if not any(
                term in content
                for term in PROHIBITED_OPENAPI_TERMS
            )
            else "FAIL"
        ),
    })

    return checks


def _openapi_operation_checks(
    paths: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    for path, expected in EXPECTED_ENDPOINTS.items():
        path_item = paths.get(path, {})
        method = str(expected["method"]).lower()
        operation = (
            path_item.get(method)
            if isinstance(path_item, dict)
            else None
        )
        responses = (
            operation.get("responses")
            if isinstance(operation, dict)
            else None
        )

        checks.append({
            "name": f"openapi-{path}-operation",
            "status": (
                "PASS"
                if isinstance(operation, dict)
                else "FAIL"
            ),
        })
        checks.append({
            "name": f"openapi-{path}-responses",
            "status": (
                "PASS"
                if (
                    isinstance(responses, dict)
                    and len(responses) > 0
                )
                else "FAIL"
            ),
        })

    return checks
