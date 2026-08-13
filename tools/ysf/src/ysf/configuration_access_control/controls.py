"""Deterministic, non-operational configuration and access controls for S03."""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import datetime
from typing import NoReturn, TypeAlias

from ysf.secure_factory.models import FactoryFailure
from ysf.secure_factory.sensitive import scan_text

Scalar: TypeAlias = str | int | bool | None

SCOPES = ("GLOBAL", "ORGANIZATION", "DEPARTMENT", "STOREFRONT", "USER")
SCOPE_RANK = {scope: rank for rank, scope in enumerate(SCOPES)}
AUTHENTICATION_METHODS = frozenset({"SERVICE_ASSERTION", "SYNTHETIC_OTP", "SYNTHETIC_PASSWORD"})
_IDENTIFIER = re.compile(r"^[A-Z0-9][A-Z0-9_.:-]{2,127}$")
_OWNER = re.compile(r"^[A-Za-z][A-Za-z0-9 ._-]{2,79}$")
_CORRELATION = re.compile(r"^SYN-[A-Z0-9-]{6,64}$")
_REDACT_KEYS = frozenset({"authorization", "credential", "email", "private_key", "secret", "token"})


def _fail(code: str, message: str, **details: object) -> NoReturn:
    raise FactoryFailure(code, message, details=dict(details))


def _canonical_values(values: Mapping[str, Scalar]) -> bytes:
    return json.dumps(
        dict(values),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def _parse_utc(value: str) -> datetime:
    if not value.endswith("Z"):
        _fail("FAIL_CONFIG_INTERVAL", "Effective interval must use UTC Z form.")
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        _fail("FAIL_CONFIG_INTERVAL", "Effective interval is malformed.")
    return parsed


def _require_safe_text(value: str, code: str) -> None:
    if scan_text(value, location="synthetic-input"):
        _fail(code, "Sensitive input was rejected before state mutation.")


@dataclass(frozen=True)
class ConfigurationSchema:
    """Exact schema and override boundary for one configuration family."""

    version: str
    fields: tuple[tuple[str, str], ...]
    required_fields: frozenset[str]
    overridable_fields: frozenset[str]

    @classmethod
    def create(
        cls,
        *,
        version: str,
        fields: Mapping[str, str],
        required_fields: Iterable[str],
        overridable_fields: Iterable[str],
    ) -> ConfigurationSchema:
        if _IDENTIFIER.fullmatch(version) is None:
            _fail("FAIL_CONFIG_SCHEMA", "Schema version is malformed.")
        ordered = tuple(sorted(fields.items()))
        allowed_types = {"boolean", "integer", "null", "string"}
        if not ordered or any(
            _IDENTIFIER.fullmatch(name) is None or kind not in allowed_types
            for name, kind in ordered
        ):
            _fail("FAIL_CONFIG_SCHEMA", "Schema fields are malformed.")
        names = {name for name, _ in ordered}
        required = frozenset(required_fields)
        overridable = frozenset(overridable_fields)
        if not required <= names or not overridable <= names:
            _fail("FAIL_CONFIG_SCHEMA", "Schema field sets exceed declared fields.")
        return cls(version, ordered, required, overridable)

    @property
    def field_types(self) -> dict[str, str]:
        return dict(self.fields)


@dataclass(frozen=True)
class ConfigurationRecord:
    """Immutable configuration identity/version and canonical value binding."""

    identity: str
    version: int
    schema_version: str
    scope: str
    owner: str
    effective_from: str
    effective_until: str
    parent_identity: str | None
    values: tuple[tuple[str, Scalar], ...]
    audit_metadata: tuple[tuple[str, str], ...]
    value_digest: str

    @property
    def value_map(self) -> dict[str, Scalar]:
        return dict(self.values)

    def is_effective(self, at: str) -> bool:
        point = _parse_utc(at)
        return _parse_utc(self.effective_from) <= point < _parse_utc(self.effective_until)


def build_configuration_record(
    *,
    identity: str,
    version: int,
    schema: ConfigurationSchema,
    scope: str,
    owner: str,
    effective_from: str,
    effective_until: str,
    values: Mapping[str, Scalar],
    audit_metadata: Mapping[str, str],
    parent_identity: str | None = None,
) -> ConfigurationRecord:
    """Validate completely and then return immutable canonical state."""

    if _IDENTIFIER.fullmatch(identity) is None or type(version) is not int or version < 1:
        _fail("FAIL_CONFIG_IDENTITY", "Configuration identity/version is invalid.")
    if scope not in SCOPE_RANK or _OWNER.fullmatch(owner) is None:
        _fail("FAIL_CONFIG_SCOPE_OWNER", "Configuration scope/owner is invalid.")
    start = _parse_utc(effective_from)
    end = _parse_utc(effective_until)
    if start >= end:
        _fail("FAIL_CONFIG_INTERVAL", "Effective interval must be non-empty.")
    if parent_identity is not None and _IDENTIFIER.fullmatch(parent_identity) is None:
        _fail("FAIL_CONFIG_PARENT", "Parent identity is malformed.")
    declared = schema.field_types
    if not schema.required_fields <= set(values) or not set(values) <= set(declared):
        _fail("FAIL_CONFIG_SCHEMA", "Configuration keys differ from the schema.")
    python_types: dict[str, type[object]] = {
        "boolean": bool,
        "integer": int,
        "null": type(None),
        "string": str,
    }
    for key, value in values.items():
        expected = python_types[declared[key]]
        if type(value) is not expected:
            _fail("FAIL_CONFIG_SCHEMA", "Configuration value type is incorrect.", key=key)
    encoded = _canonical_values(values)
    _require_safe_text(encoded.decode("utf-8"), "FAIL_CONFIG_SENSITIVE")
    if not audit_metadata or any(
        _IDENTIFIER.fullmatch(key) is None or not isinstance(value, str) or not value
        for key, value in audit_metadata.items()
    ):
        _fail("FAIL_CONFIG_AUDIT", "Audit metadata is incomplete or malformed.")
    _require_safe_text(json.dumps(dict(audit_metadata), sort_keys=True), "FAIL_CONFIG_SENSITIVE")
    return ConfigurationRecord(
        identity=identity,
        version=version,
        schema_version=schema.version,
        scope=scope,
        owner=owner,
        effective_from=effective_from,
        effective_until=effective_until,
        parent_identity=parent_identity,
        values=tuple(sorted(values.items())),
        audit_metadata=tuple(sorted(audit_metadata.items())),
        value_digest=hashlib.sha256(encoded).hexdigest(),
    )


class ConfigurationRegistry:
    """In-memory source reference that rejects ambiguous immutable versions."""

    def __init__(self) -> None:
        self._records: dict[tuple[str, int], ConfigurationRecord] = {}

    def add(self, record: ConfigurationRecord) -> None:
        key = (record.identity, record.version)
        existing = self._records.get(key)
        if existing is not None and existing != record:
            _fail(
                "FAIL_CONFIG_AMBIGUITY",
                "The same configuration identity/version binds different bytes.",
            )
        self._records.setdefault(key, record)

    def remove(self, identity: str, version: int) -> ConfigurationRecord:
        try:
            return self._records.pop((identity, version))
        except KeyError:
            _fail("FAIL_CONFIG_MISSING", "Configuration record does not exist.")

    @property
    def records(self) -> tuple[ConfigurationRecord, ...]:
        return tuple(sorted(self._records.values(), key=lambda item: (item.identity, item.version)))


@dataclass(frozen=True)
class EffectiveConfiguration:
    values: tuple[tuple[str, Scalar], ...]
    source_records: tuple[tuple[str, str], ...]
    resolution_digest: str


def resolve_effective_configuration(
    records: Iterable[ConfigurationRecord],
    schema: ConfigurationSchema,
    *,
    at: str,
) -> EffectiveConfiguration:
    """Resolve one explicit chain from the highest active scope, fail closed."""

    active = tuple(record for record in records if record.is_effective(at))
    if not active:
        _fail("FAIL_CONFIG_MISSING", "No effective configuration exists.")
    by_identity: dict[str, ConfigurationRecord] = {}
    for record in active:
        if record.schema_version != schema.version:
            _fail("FAIL_CONFIG_SCHEMA", "Configuration schema versions differ.")
        previous = by_identity.get(record.identity)
        if previous is not None:
            _fail("FAIL_CONFIG_AMBIGUITY", "Multiple active versions are ambiguous.")
        by_identity[record.identity] = record
    for record in active:
        path: set[str] = set()
        current_record = record
        while current_record.parent_identity is not None:
            if current_record.identity in path:
                _fail("FAIL_CONFIG_CYCLE", "Configuration inheritance contains a cycle.")
            path.add(current_record.identity)
            parent = by_identity.get(current_record.parent_identity)
            if parent is None:
                _fail("FAIL_CONFIG_PARENT", "Configuration parent is missing.")
            current_record = parent
    for record in active:
        if record.parent_identity is None:
            continue
        parent = by_identity[record.parent_identity]
        if SCOPE_RANK[parent.scope] >= SCOPE_RANK[record.scope]:
            _fail("FAIL_CONFIG_SCOPE", "Configuration scope precedence is invalid.")
    highest = max(SCOPE_RANK[record.scope] for record in active)
    leaves = [record for record in active if SCOPE_RANK[record.scope] == highest]
    if len(leaves) != 1:
        _fail("FAIL_CONFIG_AMBIGUITY", "Effective configuration has multiple leaves.")
    chain: list[ConfigurationRecord] = []
    seen: set[str] = set()
    current = leaves[0]
    while True:
        if current.identity in seen:
            _fail("FAIL_CONFIG_CYCLE", "Configuration inheritance contains a cycle.")
        seen.add(current.identity)
        chain.append(current)
        if current.parent_identity is None:
            break
        parent = by_identity.get(current.parent_identity)
        if parent is None:
            _fail("FAIL_CONFIG_PARENT", "Configuration parent is missing.")
        current = parent
    merged: dict[str, Scalar] = {}
    sources: dict[str, str] = {}
    for record in reversed(chain):
        for key, value in record.values:
            if key in merged and merged[key] != value and key not in schema.overridable_fields:
                _fail("FAIL_CONFIG_OVERRIDE", "Configuration override is unauthorized.")
            if key in merged and merged[key] == value:
                continue
            merged[key] = value
            sources[key] = f"{record.identity}:{record.version}"
    canonical_values: dict[str, Scalar] = dict(sorted(merged.items()))
    digest = hashlib.sha256(_canonical_values(canonical_values)).hexdigest()
    return EffectiveConfiguration(
        values=tuple(sorted(merged.items())),
        source_records=tuple(sorted(sources.items())),
        resolution_digest=digest,
    )


@dataclass(frozen=True)
class AuthenticationPolicy:
    actor_methods: tuple[tuple[str, tuple[str, ...]], ...]

    @classmethod
    def create(cls, actor_methods: Mapping[str, Iterable[str]]) -> AuthenticationPolicy:
        normalized: list[tuple[str, tuple[str, ...]]] = []
        if not actor_methods:
            _fail("FAIL_AUTH_POLICY", "Authentication policy is empty.")
        for actor, methods in actor_methods.items():
            selected = tuple(sorted(set(methods)))
            if (
                _IDENTIFIER.fullmatch(actor) is None
                or not selected
                or not set(selected) <= AUTHENTICATION_METHODS
            ):
                _fail("FAIL_AUTH_POLICY", "Authentication policy is malformed.")
            normalized.append((actor, selected))
        return cls(tuple(sorted(normalized)))

    def methods_for(self, actor_class: str) -> tuple[str, ...]:
        return dict(self.actor_methods).get(actor_class, ())


@dataclass(frozen=True)
class AuthenticationDecision:
    result: str
    actor_class: str
    method: str
    evidence: str


def authenticate(
    policy: AuthenticationPolicy,
    *,
    actor_class: str,
    method: str,
    synthetic_proof: str,
) -> AuthenticationDecision:
    if _IDENTIFIER.fullmatch(actor_class) is None or method not in AUTHENTICATION_METHODS:
        _fail("FAIL_AUTHENTICATION_METHOD", "Authentication input is malformed.")
    if method not in policy.methods_for(actor_class):
        _fail("FAIL_AUTHENTICATION_METHOD", "Authentication method is not allowlisted.")
    if synthetic_proof not in {"SYNTHETIC_REJECTED", "SYNTHETIC_VERIFIED"}:
        _fail("FAIL_AUTHENTICATION_PROOF", "Only synthetic proof status is accepted.")
    result = "PASS" if synthetic_proof == "SYNTHETIC_VERIFIED" else "FAIL"
    evidence = hashlib.sha256(f"{actor_class}|{method}|{result}".encode()).hexdigest()
    return AuthenticationDecision(result, actor_class, method, evidence)


@dataclass(frozen=True)
class AccessGrant:
    actor_class: str
    action: str
    resource: str
    data_scope: str


@dataclass(frozen=True)
class AccessRequest:
    subject: str
    actor_class: str
    action: str
    resource: str
    data_scope: str
    correlation_id: str


@dataclass(frozen=True)
class AccessDecision:
    result: str
    subject_digest: str
    action: str
    resource: str
    data_scope: str
    audit_record: tuple[tuple[str, str], ...]


def _validate_access_text(value: str) -> None:
    if _IDENTIFIER.fullmatch(value) is None:
        _fail("FAIL_AUTHORIZATION_INPUT", "Access-control input is malformed.")
    _require_safe_text(value, "FAIL_AUTHORIZATION_SENSITIVE")


def authorize(
    authentication: AuthenticationDecision,
    request: AccessRequest,
    grants: Iterable[AccessGrant],
) -> AccessDecision:
    for value in (
        request.subject,
        request.actor_class,
        request.action,
        request.resource,
        request.data_scope,
    ):
        _validate_access_text(value)
    if _CORRELATION.fullmatch(request.correlation_id) is None:
        _fail("FAIL_AUTHORIZATION_INPUT", "Audit correlation identifier is malformed.")
    if authentication.result != "PASS" or authentication.actor_class != request.actor_class:
        result = "DENY"
    else:
        expected = AccessGrant(
            request.actor_class, request.action, request.resource, request.data_scope
        )
        result = "ALLOW" if expected in set(grants) else "DENY"
    subject_digest = hashlib.sha256(request.subject.encode("utf-8")).hexdigest()
    correlation_digest = hashlib.sha256(request.correlation_id.encode("utf-8")).hexdigest()
    audit = {
        "action": request.action,
        "correlation_digest": correlation_digest,
        "data_scope": request.data_scope,
        "resource": request.resource,
        "result": result,
        "subject_digest": subject_digest,
    }
    return AccessDecision(
        result=result,
        subject_digest=subject_digest,
        action=request.action,
        resource=request.resource,
        data_scope=request.data_scope,
        audit_record=tuple(sorted(audit.items())),
    )


def redact_for_output(fields: Mapping[str, str]) -> tuple[tuple[str, str], ...]:
    redacted: dict[str, str] = {}
    for key, value in fields.items():
        if key.casefold() in _REDACT_KEYS or scan_text(value, location="output"):
            redacted[key] = "<REDACTED>"
        else:
            redacted[key] = value
    return tuple(sorted(redacted.items()))


@dataclass(frozen=True)
class PreExecutionAccess:
    result: str
    provider_invoked: bool
    delivery_performed: bool
    decision_digest: str


def assert_pre_execution_access(
    authentication: AuthenticationDecision,
    authorization: AccessDecision,
) -> PreExecutionAccess:
    """Require decisions before the boundary; never invoke a provider/delivery."""

    if authentication.result != "PASS":
        _fail("FAIL_PRE_EXECUTION_AUTHENTICATION", "Authentication did not pass.")
    if authorization.result != "ALLOW":
        _fail("FAIL_PRE_EXECUTION_AUTHORIZATION", "Authorization did not allow access.")
    digest = hashlib.sha256(
        json.dumps(dict(authorization.audit_record), sort_keys=True).encode("utf-8")
    ).hexdigest()
    return PreExecutionAccess(
        result="PASS",
        provider_invoked=False,
        delivery_performed=False,
        decision_digest=digest,
    )
