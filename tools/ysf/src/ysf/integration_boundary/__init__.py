"""Public source-only integration boundary for V3-R1 G00-S04."""

from ysf.integration_boundary.models import (
    AdapterProfile,
    CanonicalIntegrationRequest,
    CanonicalIntegrationResult,
    DiagnosticScalar,
    OperatorFailureProjection,
)
from ysf.integration_boundary.service import (
    FAILURE_DISPOSITION,
    FAILURE_STATE,
    SUCCESS_DISPOSITION,
    SUCCESS_STATE,
    SUPPORTED_INTERACTION_MODES,
    IntegrationGateway,
    assert_owned_integration_dependencies,
    build_adapter_profile,
    build_canonical_request,
    build_operator_failure_projection,
)
from ysf.integration_boundary.validator import validate_integration_boundary

__all__ = [
    "AdapterProfile",
    "CanonicalIntegrationRequest",
    "CanonicalIntegrationResult",
    "DiagnosticScalar",
    "FAILURE_DISPOSITION",
    "FAILURE_STATE",
    "IntegrationGateway",
    "OperatorFailureProjection",
    "SUCCESS_DISPOSITION",
    "SUCCESS_STATE",
    "SUPPORTED_INTERACTION_MODES",
    "assert_owned_integration_dependencies",
    "build_adapter_profile",
    "build_canonical_request",
    "build_operator_failure_projection",
    "validate_integration_boundary",
]
