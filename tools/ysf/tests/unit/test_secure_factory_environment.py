from __future__ import annotations

from dataclasses import replace
from pathlib import Path
from subprocess import CompletedProcess

import pytest

from ysf.secure_factory.environment import (
    _read_os_release,
    _run_text,
    load_expectation,
    normalize_repository_identity,
    observe_environment,
    require_output_outside_checkout,
    validate_candidate_build_environment,
    validate_environment,
)
from ysf.secure_factory.models import (
    EnvironmentExpectation,
    EnvironmentObservation,
    FactoryFailure,
)


def expectation(root: Path) -> EnvironmentExpectation:
    return EnvironmentExpectation(
        repository="nvkhoabk/ysim",
        checkout=root,
        branch="feature/v3-r1-g00-s00-secure-factory",
        head_commit="a" * 40,
        head_tree="b" * 40,
        wsl_distribution="YSim-Debian12",
        os_id="debian",
        os_version_id="12",
        architecture="aarch64",
        python_version="3.11.2",
    )


def observation(root: Path) -> EnvironmentObservation:
    expected = expectation(root)
    return EnvironmentObservation(**expected.__dict__)


def test_exact_environment_passes(tmp_path: Path) -> None:
    result = validate_environment(expectation(tmp_path), observation(tmp_path))
    assert result.passed
    assert len(result.details["verified_axes"]) == 11


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("repository", "other/repo"),
        ("checkout", Path("/tmp/wrong")),
        ("branch", "wrong"),
        ("head_commit", "c" * 40),
        ("head_tree", "d" * 40),
        ("wsl_distribution", "wrong"),
        ("os_id", "wrong"),
        ("os_version_id", "13"),
        ("architecture", "x86_64"),
        ("python_version", "3.12.0"),
        ("upstream", "origin/feature"),
    ],
)
def test_every_identity_mismatch_fails(tmp_path: Path, field: str, value: object) -> None:
    observed = replace(observation(tmp_path), **{field: value})
    with pytest.raises(FactoryFailure, match="Environment identity") as captured:
        validate_environment(expectation(tmp_path), observed)
    assert captured.value.details == {"mismatched_axes": [field]}


@pytest.mark.parametrize(
    "remote",
    [
        "https://github.com/nvkhoabk/ysim.git",
        "git" + "@github.com:nvkhoabk/ysim.git",
        "git" + "@github-ysim:nvkhoabk/ysim.git",
        "ssh://git" + "@github.com/nvkhoabk/ysim.git",
    ],
)
def test_repository_identity_forms(remote: str) -> None:
    assert normalize_repository_identity(remote) == "nvkhoabk/ysim"


def test_output_must_be_outside_checkout(tmp_path: Path) -> None:
    checkout = tmp_path / "repo"
    checkout.mkdir()
    outside = tmp_path / "output"
    assert require_output_outside_checkout(checkout, outside) == outside.resolve()
    with pytest.raises(FactoryFailure, match="outside"):
        require_output_outside_checkout(checkout, checkout / "generated")


def test_load_expectation_and_observe_environment(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    identity = tmp_path / "environment.yaml"
    identity.write_text(
        "repository: nvkhoabk/ysim\n"
        "protected_source:\n"
        "  commit: " + "a" * 40 + "\n"
        "  tree: " + "b" * 40 + "\n"
        "implementation:\n"
        f"  checkout: {tmp_path}\n"
        "  branch: feature/v3-r1-g00-s00-secure-factory\n"
        "  wsl_distribution: YSim-Debian12\n"
        "  os_id: debian\n"
        "  os_version_id: '12'\n"
        "  architecture: aarch64\n"
        "  python_version: 3.11.2\n"
        "  upstream: NONE\n",
        encoding="utf-8",
    )
    assert load_expectation(identity).repository == "nvkhoabk/ysim"

    values = {
        ("git", "remote", "get-url", "origin"): (
            "git" + "@github-ysim:nvkhoabk/ysim.git"
        ),
        ("git", "branch", "--show-current"): "feature/v3-r1-g00-s00-secure-factory",
        ("git", "merge-base", "HEAD", "origin/v3/main"): "a" * 40,
        ("git", "rev-parse", "origin/v3/main^{tree}"): "b" * 40,
    }
    monkeypatch.setattr(
        "ysf.secure_factory.environment._run_text",
        lambda command, cwd: values[tuple(command)],
    )
    monkeypatch.setattr(
        "ysf.secure_factory.environment.subprocess.run",
        lambda *args, **kwargs: CompletedProcess(args, 1, "", ""),
    )
    monkeypatch.setattr(
        "ysf.secure_factory.environment._read_os_release",
        lambda: {"ID": "debian", "VERSION_ID": "12"},
    )
    monkeypatch.setattr("ysf.secure_factory.environment.platform.machine", lambda: "aarch64")
    observed = observe_environment(tmp_path, environ={"WSL_DISTRO_NAME": "YSim-Debian12"})
    assert observed.repository == "nvkhoabk/ysim"
    assert observed.upstream == "NONE"


def test_environment_contract_and_identity_command_fail_closed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    invalid = tmp_path / "invalid.yaml"
    invalid.write_text("repository: nvkhoabk/ysim\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        load_expectation(invalid)
    assert captured.value.code == "FAIL_ENVIRONMENT_CONTRACT_INVALID"

    monkeypatch.setattr(
        "ysf.secure_factory.environment.subprocess.run",
        lambda *args, **kwargs: CompletedProcess(args, 4, "", ""),
    )
    with pytest.raises(FactoryFailure) as captured:
        _run_text(["git", "status"], cwd=tmp_path)
    assert captured.value.code == "FAIL_ENVIRONMENT_COMMAND"


def test_os_release_and_repository_forms_fail_closed(tmp_path: Path) -> None:
    os_release = tmp_path / "os-release"
    os_release.write_text('ID=debian\nVERSION_ID="12"\n# ignored\n', encoding="utf-8")
    assert _read_os_release(os_release) == {"ID": "debian", "VERSION_ID": "12"}
    with pytest.raises(FactoryFailure) as captured:
        _read_os_release(tmp_path / "missing")
    assert captured.value.code == "FAIL_OS_IDENTITY_UNAVAILABLE"
    for remote in ("https://example.test/owner/repo", "owner/../repo", "owner"):
        with pytest.raises(FactoryFailure):
            normalize_repository_identity(remote)


def test_candidate_build_environment_positive_and_negative(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    expected = expectation(tmp_path)
    values = {
        ("git", "merge-base", "HEAD", "origin/v3/main"): "a" * 40,
        ("git", "rev-parse", "origin/v3/main^{tree}"): "b" * 40,
        ("git", "rev-parse", "HEAD"): "c" * 40,
    }
    monkeypatch.setattr(
        "ysf.secure_factory.environment._run_text",
        lambda command, cwd: values[tuple(command)],
    )
    monkeypatch.setattr("ysf.secure_factory.environment.sys.version_info", (3, 11, 2))
    env = {
        "CI": "true",
        "GITHUB_ACTIONS": "true",
        "GITHUB_REPOSITORY": "nvkhoabk/ysim",
        "GITHUB_SHA": "c" * 40,
    }
    assert validate_candidate_build_environment(expected, tmp_path, environ=env).passed
    env["GITHUB_REPOSITORY"] = "other/repo"
    with pytest.raises(FactoryFailure) as captured:
        validate_candidate_build_environment(expected, tmp_path, environ=env)
    assert captured.value.code == "FAIL_CANDIDATE_BUILD_ENVIRONMENT"
