"""Source-only configuration and access-control reference implementation."""

from ysf.configuration_access_control.controls import (
    AccessDecision,
    AccessGrant,
    AccessRequest,
    AuthenticationDecision,
    AuthenticationPolicy,
    ConfigurationRecord,
    ConfigurationRegistry,
    ConfigurationSchema,
    assert_pre_execution_access,
    authenticate,
    authorize,
    build_configuration_record,
    resolve_effective_configuration,
)
from ysf.configuration_access_control.validator import (
    validate_configuration_access_control,
)

__all__ = [
    "AccessDecision",
    "AccessGrant",
    "AccessRequest",
    "AuthenticationDecision",
    "AuthenticationPolicy",
    "ConfigurationRecord",
    "ConfigurationRegistry",
    "ConfigurationSchema",
    "assert_pre_execution_access",
    "authenticate",
    "authorize",
    "build_configuration_record",
    "resolve_effective_configuration",
    "validate_configuration_access_control",
]
