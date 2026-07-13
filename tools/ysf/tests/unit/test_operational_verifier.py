from pathlib import Path

from ysf.operational.verifier import (
    BASELINE_FILE,
    verify_operational_api,
)

OPENAPI_DOCUMENT = """
openapi: 3.1.0
info:
  title: YSim Platform Operational API
  version: 0.1.0
paths:
  /health:
    get:
      operationId: getHealth
      responses:
        "200":
          description: Process is alive.
  /ready:
    get:
      operationId: getReadiness
      responses:
        "200":
          description: Required dependencies are available.
  /version:
    get:
      operationId: getVersion
      responses:
        "200":
          description: Version metadata is available.
  /openapi.json:
    get:
      operationId: getOpenApiDocument
      responses:
        "200":
          description: OpenAPI document.
  /docs:
    get:
      operationId: getApiDocs
      responses:
        "200":
          description: API documentation UI.
"""


def write_operational_baseline(
    repository_root: Path,
    health_dependencies: str = "[]",
    openapi_document: str = OPENAPI_DOCUMENT,
) -> None:
    baseline_path = repository_root / BASELINE_FILE
    openapi_path = (
        repository_root
        / "knowledge/api/operational-endpoints.openapi.yaml"
    )

    baseline_path.parent.mkdir(parents=True)
    openapi_path.parent.mkdir(parents=True)

    baseline_path.write_text(
        f"""
schemaVersion: "1.0"
runtime:
  timeoutMs: 1000
  failureMode: degraded
endpoints:
  - path: /health
    method: GET
    purpose: liveness
    dependencies: {health_dependencies}
  - path: /ready
    method: GET
    purpose: readiness
    dependencies:
      - postgres
      - redis
      - minio
      - required-configuration
  - path: /version
    method: GET
    purpose: version
    dependencies: []
  - path: /openapi.json
    method: GET
    purpose: api-document
    dependencies: []
  - path: /docs
    method: GET
    purpose: api-document-ui
    dependencies: []
readinessDependencies:
  postgres:
    required: true
    timeoutMs: 1000
  redis:
    required: true
    timeoutMs: 1000
  minio:
    required: true
    timeoutMs: 1000
  required-configuration:
    required: true
    timeoutMs: 1000
redaction:
  denyFieldPatterns:
    - password
    - secret
    - token
    - credential
    - privateKey
    - accessKey
openapi:
  document: knowledge/api/operational-endpoints.openapi.yaml
""",
        encoding="utf-8",
    )
    openapi_path.write_text(
        openapi_document,
        encoding="utf-8",
    )


def test_verify_operational_api_passes_for_baseline(
    tmp_path: Path,
) -> None:
    write_operational_baseline(tmp_path)

    result = verify_operational_api(
        tmp_path
    )

    assert result.successful
    assert result.data["failedChecks"] == []


def test_verify_operational_api_rejects_health_dependency(
    tmp_path: Path,
) -> None:
    write_operational_baseline(
        tmp_path,
        health_dependencies="[redis]",
    )

    result = verify_operational_api(
        tmp_path
    )

    assert not result.successful
    assert (
        "/health-dependency-policy"
        in result.data["failedChecks"]
    )


def test_verify_operational_api_rejects_prohibited_openapi_terms(
    tmp_path: Path,
) -> None:
    write_operational_baseline(
        tmp_path,
        openapi_document=(
            OPENAPI_DOCUMENT
            + "\n# supplier details must not appear\n"
        ),
    )

    result = verify_operational_api(
        tmp_path
    )

    assert not result.successful
    assert (
        "openapi-no-prohibited-terms"
        in result.data["failedChecks"]
    )


def test_verify_operational_api_rejects_missing_operation(
    tmp_path: Path,
) -> None:
    invalid_openapi = OPENAPI_DOCUMENT.replace(
        (
            "  /ready:\n"
            "    get:\n"
            "      operationId: getReadiness\n"
            "      responses:\n"
            "        \"200\":\n"
            "          description: Required dependencies are available.\n"
        ),
        "  /ready: {}\n",
    )

    write_operational_baseline(
        tmp_path,
        openapi_document=invalid_openapi,
    )

    result = verify_operational_api(
        tmp_path
    )

    assert not result.successful
    assert (
        "openapi-/ready-operation"
        in result.data["failedChecks"]
    )
