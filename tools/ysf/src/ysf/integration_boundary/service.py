"""Owned, deterministic and non-operational integration boundary for S04."""

from __future__ import annotations

import ast
import hashlib
import json
import re
from collections.abc import Iterable, Mapping
from dataclasses import asdict
from typing import Any, NoReturn

from ysf.integration_boundary.models import (
    AdapterProfile,
    CanonicalIntegrationRequest,
    CanonicalIntegrationResult,
    DiagnosticScalar,
    OperatorFailureProjection,
)
from ysf.secure_factory.models import FactoryFailure
from ysf.secure_factory.sensitive import scan_text

SUPPORTED_INTERACTION_MODES = frozenset({"REST", "WEBHOOK", "EVENT", "QUEUE", "BATCH"})
FAILURE_DISPOSITION = "DENIED_BEFORE_ADAPTER"
SUCCESS_DISPOSITION = "ACCEPTED_SYNTHETIC_NO_EFFECT"
FAILURE_STATE = "SYNTHETIC_FAILURE"
SUCCESS_STATE = "SYNTHETIC_ACCEPTED"
_IDENTIFIER = re.compile(r"^[A-Z][A-Z0-9_.:-]{2,127}$")
_CORRELATION = re.compile(r"^SYN-[A-Z0-9-]{6,64}$")
_IDEMPOTENCY = re.compile(r"^IDEM-[A-Z0-9-]{6,64}$")
_VERSION = re.compile(r"^v[1-9][0-9]*$")
_OWNER = re.compile(r"^[A-Za-z][A-Za-z0-9 ._-]{2,79}$")
_SAFE_CLASSIFICATION = re.compile(r"^[A-Z][A-Z0-9_]{2,63}$")
_FORBIDDEN_CONTEXT_KEYS = frozenset(
    {
        "authorization",
        "credential",
        "customer",
        "email",
        "mailbox",
        "payment_instrument",
        "secret",
        "token",
    }
)
_DIRECT_PROVIDER_MODULES = (
    "aiohttp",
    "boto3",
    "http.client",
    "httpx",
    "requests",
    "socket",
    "urllib",
    "ysf.execution.providers",
)
_BUSINESS_PRESENTATION_MARKERS = ("/business/", "/presentation/", "/ui/")


def _fail(code: str, message: str, **details: object) -> NoReturn:
    raise FactoryFailure(code, message, details=dict(details))


def _canonical_json(value: Any) -> bytes:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError):
        _fail("FAIL_INTEGRATION_SCHEMA", "Value cannot be encoded canonically.")


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value)).hexdigest()


def _safe_identifier(value: object, code: str, label: str) -> str:
    if not isinstance(value, str) or _IDENTIFIER.fullmatch(value) is None:
        _fail(code, f"{label} is malformed.")
    return value


def _safe_owner(value: object) -> str:
    if not isinstance(value, str) or _OWNER.fullmatch(value) is None:
        _fail("FAIL_INTEGRATION_OWNER", "Owner is malformed.")
    return value


def _safe_version(value: object) -> str:
    if not isinstance(value, str) or _VERSION.fullmatch(value) is None:
        _fail("FAIL_INTEGRATION_VERSION", "Contract version is malformed.")
    return value


def _safe_mode(value: object) -> str:
    if not isinstance(value, str) or value not in SUPPORTED_INTERACTION_MODES:
        _fail("FAIL_INTERACTION_MODE", "Interaction mode is undeclared.")
    return value


def _safe_diagnostics(
    value: object,
) -> tuple[tuple[str, DiagnosticScalar], ...]:
    if not isinstance(value, Mapping):
        _fail("FAIL_DIAGNOSTIC_CONTEXT", "Diagnostic context must be a mapping.")
    result: dict[str, DiagnosticScalar] = {}
    for key, item in value.items():
        if (
            not isinstance(key, str)
            or _IDENTIFIER.fullmatch(key) is None
            or key.casefold() in _FORBIDDEN_CONTEXT_KEYS
            or type(item) not in {str, int, bool, type(None)}
        ):
            _fail("FAIL_DIAGNOSTIC_CONTEXT", "Diagnostic context is not safely redacted.")
        if isinstance(item, str) and scan_text(item, location="synthetic-diagnostic"):
            _fail("FAIL_SENSITIVE_VALUE", "Sensitive diagnostic input was rejected.")
        result[key] = item
    if len(result) > 16:
        _fail("FAIL_DIAGNOSTIC_CONTEXT", "Diagnostic context exceeds the bounded schema.")
    encoded = _canonical_json(result).decode("utf-8")
    if scan_text(encoded, location="synthetic-diagnostic"):
        _fail("FAIL_SENSITIVE_VALUE", "Sensitive diagnostic input was rejected.")
    return tuple(sorted(result.items()))


_REQUEST_KEYS = frozenset(
    {
        "adapter_id",
        "capability_id",
        "contract_version",
        "correlation_id",
        "diagnostic_context",
        "idempotency_key",
        "interaction_mode",
        "owner",
        "retry_policy_ref",
        "scenario_id",
        "timeout_policy_ref",
    }
)


def build_canonical_request(values: Mapping[str, object]) -> CanonicalIntegrationRequest:
    """Build an exact-key, digest-bound synthetic integration request."""

    if set(values) != _REQUEST_KEYS:
        _fail(
            "FAIL_INTEGRATION_SCHEMA",
            "Request keys differ from the exact canonical schema.",
            missing=sorted(_REQUEST_KEYS - set(values)),
            extra=sorted(set(values) - _REQUEST_KEYS),
        )
    contract_version = _safe_version(values["contract_version"])
    capability_id = _safe_identifier(
        values["capability_id"], "FAIL_INTEGRATION_CAPABILITY", "Capability identity"
    )
    scenario_id = _safe_identifier(
        values["scenario_id"], "FAIL_INTEGRATION_SCENARIO", "Scenario identity"
    )
    adapter_id = _safe_identifier(
        values["adapter_id"], "FAIL_ADAPTER_IDENTITY", "Adapter identity"
    )
    owner = _safe_owner(values["owner"])
    interaction_mode = _safe_mode(values["interaction_mode"])
    correlation_id = values["correlation_id"]
    idempotency_key = values["idempotency_key"]
    if not isinstance(correlation_id, str) or _CORRELATION.fullmatch(correlation_id) is None:
        _fail("FAIL_CORRELATION_ID", "Correlation identifier is malformed.")
    if not isinstance(idempotency_key, str) or _IDEMPOTENCY.fullmatch(idempotency_key) is None:
        _fail("FAIL_IDEMPOTENCY_KEY", "Idempotency key is malformed.")
    timeout_policy_ref = _safe_identifier(
        values["timeout_policy_ref"], "FAIL_POLICY_REFERENCE", "Timeout policy reference"
    )
    retry_policy_ref = _safe_identifier(
        values["retry_policy_ref"], "FAIL_POLICY_REFERENCE", "Retry policy reference"
    )
    diagnostics = _safe_diagnostics(values["diagnostic_context"])
    binding = {
        **{key: values[key] for key in sorted(_REQUEST_KEYS - {"diagnostic_context"})},
        "diagnostic_context": dict(diagnostics),
    }
    return CanonicalIntegrationRequest(
        contract_version=contract_version,
        capability_id=capability_id,
        scenario_id=scenario_id,
        idempotency_key=idempotency_key,
        correlation_id=correlation_id,
        interaction_mode=interaction_mode,
        adapter_id=adapter_id,
        owner=owner,
        timeout_policy_ref=timeout_policy_ref,
        retry_policy_ref=retry_policy_ref,
        diagnostic_context=diagnostics,
        request_digest=_digest(binding),
    )


def _request_binding(request: CanonicalIntegrationRequest) -> dict[str, object]:
    return {
        "adapter_id": request.adapter_id,
        "capability_id": request.capability_id,
        "contract_version": request.contract_version,
        "correlation_id": request.correlation_id,
        "diagnostic_context": dict(request.diagnostic_context),
        "idempotency_key": request.idempotency_key,
        "interaction_mode": request.interaction_mode,
        "owner": request.owner,
        "retry_policy_ref": request.retry_policy_ref,
        "scenario_id": request.scenario_id,
        "timeout_policy_ref": request.timeout_policy_ref,
    }


def _validate_request_integrity(request: CanonicalIntegrationRequest) -> None:
    if _digest(_request_binding(request)) != request.request_digest:
        _fail("FAIL_REQUEST_INTEGRITY", "Request digest binding is incorrect.")
    _safe_diagnostics(dict(request.diagnostic_context))


def build_adapter_profile(
    *,
    adapter_id: str,
    capability_id: str,
    enabled: bool,
    interaction_modes: Iterable[str],
    contract_versions: Iterable[str],
    scenario_ids: Iterable[str],
    owner: str,
    timeout_policy_ref: str,
    retry_policy_ref: str,
) -> AdapterProfile:
    """Create one immutable adapter policy; schema presence never enables it."""

    safe_adapter = _safe_identifier(adapter_id, "FAIL_ADAPTER_IDENTITY", "Adapter identity")
    safe_capability = _safe_identifier(
        capability_id, "FAIL_INTEGRATION_CAPABILITY", "Capability identity"
    )
    if type(enabled) is not bool:
        _fail("FAIL_ADAPTER_POLICY", "Adapter enabled state must be boolean.")
    modes = tuple(sorted(set(interaction_modes)))
    versions = tuple(sorted(set(contract_versions)))
    scenarios = tuple(sorted(set(scenario_ids)))
    if any(mode not in SUPPORTED_INTERACTION_MODES for mode in modes):
        _fail("FAIL_INTERACTION_MODE", "Adapter policy contains an undeclared mode.")
    if any(_VERSION.fullmatch(version) is None for version in versions):
        _fail("FAIL_INTEGRATION_VERSION", "Adapter policy has a malformed contract version.")
    if any(_IDENTIFIER.fullmatch(scenario) is None for scenario in scenarios):
        _fail("FAIL_INTEGRATION_SCENARIO", "Adapter policy has a malformed scenario.")
    safe_owner = _safe_owner(owner)
    timeout = _safe_identifier(
        timeout_policy_ref, "FAIL_POLICY_REFERENCE", "Timeout policy reference"
    )
    retry = _safe_identifier(retry_policy_ref, "FAIL_POLICY_REFERENCE", "Retry policy reference")
    if enabled and (not modes or not versions or not scenarios):
        _fail("FAIL_ADAPTER_POLICY", "Enabled adapter policy is not fully bound.")
    binding = {
        "adapter_id": safe_adapter,
        "capability_id": safe_capability,
        "contract_versions": versions,
        "enabled": enabled,
        "interaction_modes": modes,
        "owner": safe_owner,
        "retry_policy_ref": retry,
        "scenario_ids": scenarios,
        "timeout_policy_ref": timeout,
    }
    return AdapterProfile(
        adapter_id=safe_adapter,
        capability_id=safe_capability,
        enabled=enabled,
        interaction_modes=modes,
        contract_versions=versions,
        scenario_ids=scenarios,
        owner=safe_owner,
        timeout_policy_ref=timeout,
        retry_policy_ref=retry,
        profile_digest=_digest(binding),
    )


def _profile_binding(profile: AdapterProfile) -> dict[str, object]:
    value = asdict(profile)
    value.pop("profile_digest")
    return value


def _result(
    request: CanonicalIntegrationRequest,
    *,
    state: str,
    disposition: str,
    classification: str,
    reconciliation_eligible: bool,
    alert_eligible: bool,
    manual_action: str,
) -> CanonicalIntegrationResult:
    diagnostics = _safe_diagnostics(dict(request.diagnostic_context))
    binding = {
        "adapter_id": request.adapter_id,
        "adapter_invocation_count": 0,
        "alert_eligible": alert_eligible,
        "capability_id": request.capability_id,
        "contract_version": request.contract_version,
        "correlation_id": request.correlation_id,
        "current_state": state,
        "diagnostic_context": dict(diagnostics),
        "disposition": disposition,
        "exception_classification": classification,
        "interaction_mode": request.interaction_mode,
        "network_call_count": 0,
        "owner": request.owner,
        "reconciliation_eligible": reconciliation_eligible,
        "request_digest": request.request_digest,
        "safe_manual_action": manual_action,
        "scenario_id": request.scenario_id,
    }
    return CanonicalIntegrationResult(
        contract_version=request.contract_version,
        request_digest=request.request_digest,
        capability_id=request.capability_id,
        scenario_id=request.scenario_id,
        correlation_id=request.correlation_id,
        interaction_mode=request.interaction_mode,
        adapter_id=request.adapter_id,
        owner=request.owner,
        current_state=state,
        disposition=disposition,
        exception_classification=classification,
        reconciliation_eligible=reconciliation_eligible,
        alert_eligible=alert_eligible,
        safe_manual_action=manual_action,
        diagnostic_context=diagnostics,
        adapter_invocation_count=0,
        network_call_count=0,
        result_digest=_digest(binding),
    )


class IntegrationGateway:
    """Owned in-memory policy boundary with no transport implementation."""

    def __init__(
        self,
        *,
        allowed_adapter_ids: Iterable[str],
        profiles: Iterable[AdapterProfile] = (),
    ) -> None:
        allowlist = frozenset(allowed_adapter_ids)
        if any(_IDENTIFIER.fullmatch(item) is None for item in allowlist):
            _fail("FAIL_ADAPTER_ALLOWLIST", "Adapter allowlist is malformed.")
        self._allowlist = allowlist
        self._profiles: dict[str, AdapterProfile] = {}
        self._seen_idempotency: dict[str, str] = {}
        for profile in profiles:
            self.register(profile)

    @property
    def adapter_invocation_count(self) -> int:
        return 0

    @property
    def network_call_count(self) -> int:
        return 0

    @property
    def profiles(self) -> tuple[AdapterProfile, ...]:
        return tuple(self._profiles[key] for key in sorted(self._profiles))

    def register(self, profile: AdapterProfile) -> None:
        if profile.adapter_id not in self._allowlist:
            _fail("FAIL_ADAPTER_ALLOWLIST", "Adapter is not allowlisted.")
        if _digest(_profile_binding(profile)) != profile.profile_digest:
            _fail("FAIL_ADAPTER_INTEGRITY", "Adapter profile digest is incorrect.")
        existing = self._profiles.get(profile.adapter_id)
        if existing is not None and existing != profile:
            _fail("FAIL_ADAPTER_AMBIGUITY", "Adapter identity maps to different policies.")
        self._profiles.setdefault(profile.adapter_id, profile)

    def submit(self, request: CanonicalIntegrationRequest) -> CanonicalIntegrationResult:
        """Apply all policy gates and return without invoking a provider or network."""

        _validate_request_integrity(request)
        previous = self._seen_idempotency.get(request.idempotency_key)
        if previous is not None and previous != request.request_digest:
            return _result(
                request,
                state=FAILURE_STATE,
                disposition=FAILURE_DISPOSITION,
                classification="IDEMPOTENCY_REPLAY_MISMATCH",
                reconciliation_eligible=True,
                alert_eligible=True,
                manual_action="REVIEW_SYNTHETIC_REQUEST_BINDING",
            )
        if request.adapter_id not in self._allowlist:
            classification = "ADAPTER_NOT_ALLOWLISTED"
        else:
            profile = self._profiles.get(request.adapter_id)
            if profile is None:
                classification = "ADAPTER_ABSENT"
            elif not profile.enabled:
                classification = "ADAPTER_DISABLED"
            elif _digest(_profile_binding(profile)) != profile.profile_digest:
                classification = "ADAPTER_PROFILE_INTEGRITY_FAILURE"
            elif request.capability_id != profile.capability_id:
                classification = "CAPABILITY_POLICY_MISMATCH"
            elif request.interaction_mode not in profile.interaction_modes:
                classification = "INTERACTION_MODE_DISABLED"
            elif request.contract_version not in profile.contract_versions:
                classification = "CONTRACT_VERSION_DISABLED"
            elif request.scenario_id not in profile.scenario_ids:
                classification = "SCENARIO_DISABLED"
            elif request.owner != profile.owner:
                classification = "OWNER_POLICY_MISMATCH"
            elif request.timeout_policy_ref != profile.timeout_policy_ref:
                classification = "TIMEOUT_POLICY_MISMATCH"
            elif request.retry_policy_ref != profile.retry_policy_ref:
                classification = "RETRY_POLICY_MISMATCH"
            else:
                self._seen_idempotency.setdefault(request.idempotency_key, request.request_digest)
                return _result(
                    request,
                    state=SUCCESS_STATE,
                    disposition=SUCCESS_DISPOSITION,
                    classification="NONE",
                    reconciliation_eligible=False,
                    alert_eligible=False,
                    manual_action="NONE",
                )
        self._seen_idempotency.setdefault(request.idempotency_key, request.request_digest)
        return _result(
            request,
            state=FAILURE_STATE,
            disposition=FAILURE_DISPOSITION,
            classification=classification,
            reconciliation_eligible=True,
            alert_eligible=True,
            manual_action="REVIEW_SYNTHETIC_POLICY",
        )


def build_operator_failure_projection(
    result: CanonicalIntegrationResult,
) -> OperatorFailureProjection:
    """Expose only bounded redacted evidence and no executable action."""

    if result.current_state != FAILURE_STATE or result.disposition != FAILURE_DISPOSITION:
        _fail("FAIL_OPERATOR_SCOPE", "Operator projection accepts synthetic failures only.")
    if (
        result.adapter_invocation_count != 0
        or result.network_call_count != 0
        or _SAFE_CLASSIFICATION.fullmatch(result.exception_classification) is None
    ):
        _fail("FAIL_OPERATOR_INTEGRITY", "Failure result exceeds the operator boundary.")
    diagnostics = _safe_diagnostics(dict(result.diagnostic_context))
    binding = {
        "adapter_id": result.adapter_id,
        "alert_eligible": result.alert_eligible,
        "capability_id": result.capability_id,
        "correlation_id": result.correlation_id,
        "current_state": result.current_state,
        "diagnostic_context": dict(diagnostics),
        "exception_classification": result.exception_classification,
        "reconciliation_eligible": result.reconciliation_eligible,
        "safe_manual_action": result.safe_manual_action,
        "source_result_digest": result.result_digest,
    }
    return OperatorFailureProjection(
        correlation_id=result.correlation_id,
        current_state=result.current_state,
        adapter_id=result.adapter_id,
        capability_id=result.capability_id,
        exception_classification=result.exception_classification,
        reconciliation_eligible=result.reconciliation_eligible,
        alert_eligible=result.alert_eligible,
        safe_manual_action=result.safe_manual_action,
        diagnostic_context=diagnostics,
        source_result_digest=result.result_digest,
        projection_digest=_digest(binding),
    )


def assert_owned_integration_dependencies(sources: Mapping[str, str]) -> None:
    """Reject direct transport/provider imports in business, presentation, or UI source."""

    for path, source in sorted(sources.items()):
        portable_path = path.replace(chr(92), "/")
        normalized = f"/{portable_path.lstrip('/')}"
        if not normalized.endswith(".py") or not any(
            marker in normalized for marker in _BUSINESS_PRESENTATION_MARKERS
        ):
            continue
        try:
            tree = ast.parse(source)
        except (SyntaxError, ValueError):
            _fail("FAIL_DEPENDENCY_SOURCE", "Dependency source cannot be parsed.", path=path)
        modules: list[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                modules.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module is not None:
                modules.append(node.module)
        if any(
            module == denied or module.startswith(f"{denied}.")
            for module in modules
            for denied in _DIRECT_PROVIDER_MODULES
        ):
            _fail(
                "FAIL_DIRECT_PROVIDER_DEPENDENCY",
                "Business or presentation source imports a provider or transport directly.",
                path=path,
            )
