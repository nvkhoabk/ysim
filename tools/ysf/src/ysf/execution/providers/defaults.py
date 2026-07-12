from __future__ import annotations

from ysf.execution.providers.codex import CodexProvider
from ysf.execution.providers.registry import ProviderRegistry


def create_default_provider_registry() -> ProviderRegistry:
    registry = ProviderRegistry()
    registry.register(CodexProvider())

    return registry
