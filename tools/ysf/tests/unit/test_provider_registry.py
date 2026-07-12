import pytest

from ysf.execution.providers import (
    CodexProvider,
    ProviderRegistry,
)
from ysf.execution.providers.exceptions import (
    ProviderAlreadyRegisteredError,
    ProviderNotFoundError,
)


def test_registry_register() -> None:

    registry = ProviderRegistry()

    registry.register(
        CodexProvider()
    )

    assert registry.exists("codex")

    assert (
        registry.get("codex").name
        == "codex"
    )


def test_registry_list() -> None:

    registry = ProviderRegistry()

    registry.register(
        CodexProvider()
    )

    assert registry.list() == [
        "codex"
    ]


def test_duplicate_provider() -> None:

    registry = ProviderRegistry()

    registry.register(
        CodexProvider()
    )

    with pytest.raises(
        ProviderAlreadyRegisteredError
    ):
        registry.register(
            CodexProvider()
        )

def test_unknown_provider() -> None:

    registry = ProviderRegistry()

    with pytest.raises(
        ProviderNotFoundError
    ):
        registry.get("claude")
