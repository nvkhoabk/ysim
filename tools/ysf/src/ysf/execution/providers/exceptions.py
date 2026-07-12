from __future__ import annotations


class ProviderError(RuntimeError):
    """Base exception for execution providers."""


class ProviderNotFoundError(ProviderError):
    """Raised when a provider is not registered."""


class ProviderAlreadyRegisteredError(ProviderError):
    """Raised when registering the same provider twice."""


class ProviderValidationError(ProviderError):
    """Raised when a provider cannot execute."""
