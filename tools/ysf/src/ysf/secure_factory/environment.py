"""Exact repository and runtime identity checks."""

from __future__ import annotations

import os
import platform
import subprocess
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path

import yaml

from ysf.secure_factory.models import (
    EnvironmentExpectation,
    EnvironmentObservation,
    FactoryFailure,
    GateResult,
)


def _run_text(command: Sequence[str], *, cwd: Path) -> str:
    process = subprocess.run(
        list(command),
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
    )
    if process.returncode != 0:
        raise FactoryFailure(
            "FAIL_ENVIRONMENT_COMMAND",
            f"Identity command failed: {command[0]}",
            details={"command": list(command), "exit_code": process.returncode},
        )
    return process.stdout.strip()


def _read_os_release(path: Path = Path("/etc/os-release")) -> dict[str, str]:
    values: dict[str, str] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise FactoryFailure(
            "FAIL_OS_IDENTITY_UNAVAILABLE",
            "Operating-system identity is unavailable.",
        ) from exc
    for line in lines:
        if "=" not in line or line.startswith("#"):
            continue
        key, value = line.split("=", 1)
        values[key] = value.strip().strip('"')
    return values


def load_expectation(path: Path) -> EnvironmentExpectation:
    """Load the frozen environment record without accepting loose defaults."""

    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        protected = raw["protected_source"]
        implementation = raw["implementation"]
        return EnvironmentExpectation(
            repository=str(raw["repository"]),
            checkout=Path(str(implementation["checkout"])),
            branch=str(implementation["branch"]),
            head_commit=str(protected["commit"]),
            head_tree=str(protected["tree"]),
            wsl_distribution=str(implementation["wsl_distribution"]),
            os_id=str(implementation["os_id"]),
            os_version_id=str(implementation["os_version_id"]),
            architecture=str(implementation["architecture"]),
            python_version=str(implementation["python_version"]),
            upstream=str(implementation["upstream"]),
        )
    except (OSError, KeyError, TypeError, yaml.YAMLError) as exc:
        raise FactoryFailure(
            "FAIL_ENVIRONMENT_CONTRACT_INVALID",
            "Frozen environment identity is missing or invalid.",
        ) from exc


def observe_environment(
    repository_root: Path,
    *,
    environ: Mapping[str, str] | None = None,
) -> EnvironmentObservation:
    """Capture identity using only local, read-only operations."""

    root = repository_root.resolve(strict=True)
    env = os.environ if environ is None else environ
    remote = _run_text(["git", "remote", "get-url", "origin"], cwd=root)
    repository = normalize_repository_identity(remote)
    upstream_process = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    upstream = upstream_process.stdout.strip() if upstream_process.returncode == 0 else "NONE"
    os_release = _read_os_release()
    return EnvironmentObservation(
        repository=repository,
        checkout=root,
        branch=_run_text(["git", "branch", "--show-current"], cwd=root),
        head_commit=_run_text(["git", "merge-base", "HEAD", "origin/v3/main"], cwd=root),
        head_tree=_run_text(["git", "rev-parse", "origin/v3/main^{tree}"], cwd=root),
        wsl_distribution=env.get("WSL_DISTRO_NAME", ""),
        os_id=os_release.get("ID", ""),
        os_version_id=os_release.get("VERSION_ID", ""),
        architecture=platform.machine(),
        python_version=".".join(str(item) for item in sys.version_info[:3]),
        upstream=upstream,
    )


def normalize_repository_identity(remote: str) -> str:
    """Normalize approved HTTPS and SSH GitHub repository identities."""

    value = remote.strip()
    ssh_user_host = "git" + "@github.com:"
    ssh_alias = "git" + "@github-ysim:"
    ssh_url = "ssh://git" + "@github.com/"
    prefixes = (
        "https://github.com/",
        ssh_user_host,
        ssh_alias,
        ssh_url,
    )
    matched = False
    for prefix in prefixes:
        if value.startswith(prefix):
            value = value[len(prefix) :]
            matched = True
            break
    if not matched:
        raise FactoryFailure(
            "FAIL_REPOSITORY_IDENTITY",
            "Repository remote identity is not an approved GitHub form.",
        )
    value = value.removesuffix(".git")
    if value.count("/") != 1 or any(part in {"", ".", ".."} for part in value.split("/")):
        raise FactoryFailure(
            "FAIL_REPOSITORY_IDENTITY",
            "Repository remote identity is not an approved GitHub form.",
        )
    return value


def validate_candidate_build_environment(
    expected: EnvironmentExpectation,
    repository_root: Path,
    *,
    environ: Mapping[str, str] | None = None,
) -> GateResult:
    """Validate the isolated GitHub Actions candidate-build identity."""

    env = os.environ if environ is None else environ
    root = repository_root.resolve(strict=True)
    observed = {
        "ci": env.get("CI", "").lower(),
        "github_actions": env.get("GITHUB_ACTIONS", "").lower(),
        "repository": env.get("GITHUB_REPOSITORY", ""),
        "sha": env.get("GITHUB_SHA", ""),
        "python_major_minor": ".".join(str(item) for item in sys.version_info[:2]),
        "base_commit": _run_text(["git", "merge-base", "HEAD", "origin/v3/main"], cwd=root),
        "base_tree": _run_text(["git", "rev-parse", "origin/v3/main^{tree}"], cwd=root),
        "head_commit": _run_text(["git", "rev-parse", "HEAD"], cwd=root),
    }
    wanted = {
        "ci": "true",
        "github_actions": "true",
        "repository": expected.repository,
        "sha": observed["head_commit"],
        "python_major_minor": "3.11",
        "base_commit": expected.head_commit,
        "base_tree": expected.head_tree,
    }
    mismatches = sorted(name for name, value in wanted.items() if observed.get(name) != value)
    if mismatches:
        raise FactoryFailure(
            "FAIL_CANDIDATE_BUILD_ENVIRONMENT",
            "Candidate-build environment does not match the approved CI identity.",
            details={"mismatched_axes": mismatches},
        )
    return GateResult(
        gate="candidate_build_environment",
        result="PASS",
        message="Isolated GitHub Actions candidate-build identity verified.",
        details={"verified_axes": sorted(wanted)},
    )


def validate_environment(
    expected: EnvironmentExpectation,
    observed: EnvironmentObservation,
) -> GateResult:
    """Require every identity axis to match the approved record."""

    axes: tuple[tuple[str, object, object], ...] = (
        ("repository", expected.repository, observed.repository),
        ("checkout", expected.checkout.resolve(), observed.checkout.resolve()),
        ("branch", expected.branch, observed.branch),
        ("head_commit", expected.head_commit, observed.head_commit),
        ("head_tree", expected.head_tree, observed.head_tree),
        ("wsl_distribution", expected.wsl_distribution, observed.wsl_distribution),
        ("os_id", expected.os_id, observed.os_id),
        ("os_version_id", expected.os_version_id, observed.os_version_id),
        ("architecture", expected.architecture, observed.architecture),
        ("python_version", expected.python_version, observed.python_version),
        ("upstream", expected.upstream, observed.upstream),
    )
    mismatches = [name for name, wanted, actual in axes if wanted != actual]
    if mismatches:
        raise FactoryFailure(
            "FAIL_ENVIRONMENT_IDENTITY",
            "Environment identity does not match the approved S00 record.",
            details={"mismatched_axes": sorted(mismatches)},
        )
    return GateResult(
        gate="environment_identity",
        result="PASS",
        message="Exact implementation identity verified.",
        details={"verified_axes": [name for name, _, _ in axes]},
    )


def require_output_outside_checkout(repository_root: Path, output_root: Path) -> Path:
    """Reject generated output inside or through a symlink into the checkout."""

    repository = repository_root.resolve(strict=True)
    output = output_root.resolve(strict=False)
    try:
        output.relative_to(repository)
    except ValueError:
        return output
    raise FactoryFailure(
        "FAIL_OUTPUT_INSIDE_CHECKOUT",
        "Generated output must remain outside the Git checkout.",
    )
