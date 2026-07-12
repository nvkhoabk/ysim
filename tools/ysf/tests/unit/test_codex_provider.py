import pytest

from ysf.execution.providers import (
    CodexProvider,
)


def test_provider_name() -> None:

    provider = CodexProvider()

    assert provider.name == "codex"


def test_provider_validate() -> None:

    provider = CodexProvider()

    provider.validate()


def test_provider_plan_not_implemented() -> None:

    provider = CodexProvider()

    with pytest.raises(
        NotImplementedError
    ):
        provider.plan(None)  # type: ignore[arg-type]


def test_provider_execute_not_implemented() -> None:

    provider = CodexProvider()

    with pytest.raises(
        NotImplementedError
    ):
        provider.execute(None)  # type: ignore[arg-type]
