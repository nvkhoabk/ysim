from __future__ import annotations

from ysf.execution.providers.base import (
    ExecutionProvider,
)
from ysf.execution.providers.exceptions import (
    ProviderAlreadyRegisteredError,
    ProviderNotFoundError,
)


class ProviderRegistry:

    def __init__(self) -> None:

        self._providers: dict[
            str,
            ExecutionProvider,
        ] = {}

    def register(
        self,
        provider: ExecutionProvider,
    ) -> None:

        name = provider.name.lower()

        if name in self._providers:
            raise ProviderAlreadyRegisteredError(
                f"Provider already exists: {name}"
            )

        self._providers[name] = provider

    def get(
        self,
        name: str,
    ) -> ExecutionProvider:

        key = name.lower()

        if key not in self._providers:
            raise ProviderNotFoundError(
                f"Unknown provider: {name}"
            )

        return self._providers[key]

    def exists(
        self,
        name: str,
    ) -> bool:

        return (
            name.lower()
            in self._providers
        )

    def list(
        self,
    ) -> list[str]:

        return sorted(
            self._providers.keys()
        )
