from __future__ import annotations

import json
import shutil
from pathlib import Path
from subprocess import CompletedProcess
from typing import Any

import pytest

from ysf.secure_factory.candidate import (
    _parse_lock_components,
    build_candidate,
    normalize_generated_admin_email,
    sanitized_quality_output,
    verify_candidate,
    verify_declared_dependency_closure,
    write_reproducible_zip,
    write_sanitized_quality_output,
)
from ysf.secure_factory.evidence import build_manifest, sha256_file
from ysf.secure_factory.models import FactoryFailure
from ysf.secure_factory.policy import (
    APPROVED_CONTRACT_SHA256,
    CONTRACT_RELATIVE_PATH,
)

REPOSITORY = "nvkhoabk/ysim"
BRANCH = "feature/v3-r1-g00-s00-secure-factory"
COMMIT = "a" * 40
TREE = "b" * 40
CONTRACT = APPROVED_CONTRACT_SHA256
CHANGED_PATHS = ["AGENTS.md"]
PREFLIGHT_GATES = (
    "candidate_build_environment",
    "policy_self_protection",
    "source_allowlist",
    "immutable_corpus",
    "sensitive_data",
    "contract_digest",
)
QUALITY_GROUPS = {
    "test-and-coverage.json": ("pytest",),
    "lint-type-sast-dependency.json": ("ruff", "mypy", "bandit", "pip-audit"),
    "leak-scan.json": ("leak-scan",),
    "environment-identity.json": ("environment-identity",),
    "governance-readback.json": ("governance-readback",),
}


def _approved_contract() -> Path:
    return Path(__file__).resolve().parents[4] / CONTRACT_RELATIVE_PATH


def test_reproducible_zip_bytes_match(tmp_path: Path) -> None:
    files = {"ysf/data.txt": b"deterministic", "ysf/__init__.py": b""}
    first = tmp_path / "first.whl"
    second = tmp_path / "second.whl"
    write_reproducible_zip(first, files, source_date_epoch=1_700_000_000)
    write_reproducible_zip(second, files, source_date_epoch=1_700_000_000)
    assert first.read_bytes() == second.read_bytes()


def test_admin_email_normalization_is_role_preserving_and_idempotent(
    tmp_path: Path,
) -> None:
    non_reserved = "".join(("seed", "@", "synthetic.localdomain"))
    customer = "".join(("customer", "@", "example.com"))
    fulfillment = "".join(("fulfillment", "@", "example.com"))
    generated = tmp_path / "prompt.md"
    generated.write_text(
        "# 9. Demonstration Seed\n\n"
        "```yaml\n"
        "demo_user:\n"
        f"  email: {non_reserved}\n"
        "  role: PLATFORM_ADMIN\n"
        "customer_user:\n"
        f"  email: {customer}\n"
        "  role: customer\n"
        "fulfillment_user:\n"
        f"  email: {fulfillment}\n"
        "  role: fulfillment\n"
        "```\n",
        encoding="utf-8",
    )

    assert normalize_generated_admin_email(generated).passed
    normalized = generated.read_text(encoding="utf-8")
    assert "role: PLATFORM_ADMIN" in normalized
    assert "admin" + "@" + "example.com" in normalized
    assert customer in normalized
    assert fulfillment in normalized
    first = generated.read_bytes()
    assert normalize_generated_admin_email(generated).passed
    assert generated.read_bytes() == first


def test_admin_email_normalization_requires_explicit_role(tmp_path: Path) -> None:
    non_reserved = "".join(("seed", "@", "synthetic.localdomain"))
    generated = tmp_path / "prompt.md"
    source = (
        "# 9. Demonstration Seed\n\n"
        "```yaml\n"
        "demo_user:\n"
        f"  email: {non_reserved}\n"
        "```\n"
    )
    generated.write_text(source, encoding="utf-8")
    assert normalize_generated_admin_email(generated).passed
    assert generated.read_text(encoding="utf-8") == source


@pytest.mark.parametrize(
    "ambiguous",
    [
        "  role: admin\n  role: admin\n",
        "  role: customer\n  role: admin\n",
        "  email: " + "duplicate" + "@" + "example.com\n  role: admin\n",
    ],
)
def test_admin_email_normalization_rejects_ambiguous_mapping(
    tmp_path: Path, ambiguous: str
) -> None:
    non_reserved = "".join(("seed", "@", "synthetic.localdomain"))
    generated = tmp_path / "prompt.md"
    source = (
        "# Demonstration Seed\n\n```yaml\n"
        f"demo_user:\n  email: {non_reserved}\n{ambiguous}```\n"
    )
    generated.write_text(source, encoding="utf-8")
    assert normalize_generated_admin_email(generated).passed
    assert generated.read_text(encoding="utf-8") == source


def test_sanitized_quality_outputs_are_derived_from_actual_results() -> None:
    pytest_output = (
        b"Required test coverage of 90% reached. Total coverage: 91.25%\n"
        b"132 passed in 1.00s\n"
    )
    summary = sanitized_quality_output("pytest", 0, pytest_output)
    assert summary["metrics"] == {
        "passed": 132,
        "failed": 0,
        "skipped": 0,
        "coverage_percent": 91.25,
    }
    bandit = sanitized_quality_output(
        "bandit", 0, b'{"results":[],"metrics":{"_totals":{"loc":100,"nosec":0}}}'
    )
    assert bandit["metrics"] == {
        "issue_count": 0,
        "lines_of_code": 100,
        "files_skipped": 0,
    }
    audit = sanitized_quality_output(
        "pip-audit",
        0,
        b"sanitized warning with {invalid payload\n{\"dependencies\":[]}\n",
    )
    assert audit["metrics"]["vulnerability_count"] == 0

    ruff = sanitized_quality_output("ruff", 0, b"All checks passed!\n")
    assert ruff["metrics"]["issue_count"] == 0
    failed_ruff = sanitized_quality_output("ruff", 1, b"sanitized failure\n")
    assert failed_ruff["result"] == "FAIL"
    assert failed_ruff["metrics"]["issue_count"] == 1
    mypy = sanitized_quality_output(
        "mypy", 0, b"Success: no issues found in 67 source files\n"
    )
    assert mypy["metrics"]["source_file_count"] == 67
    environment = sanitized_quality_output(
        "environment-identity",
        0,
        b'{"email_mode":"NON_RELAYING","external_effect_budget":"DENY_ALL","providers":"OFF"}',
    )
    assert environment["metrics"]["providers"] == "OFF"
    leak = sanitized_quality_output(
        "leak-scan",
        0,
        b'{"gate":"sensitive_data","result":"PASS","details":{"scanned_file_count":3,"profile":"V3-R1-S00-PROHIBITED-V3"}}',
    )
    assert leak["metrics"]["finding_count"] == 0
    governance = sanitized_quality_output(
        "governance-readback",
        0,
        json.dumps(
            {
                "gate": "governance_readback",
                "result": "PASS",
                "details": _quality_metrics("governance-readback"),
            }
        ).encode(),
    )
    assert governance["metrics"]["ruleset_id"] == 20583674


def test_sanitized_quality_output_bytes_are_persisted_and_scannable(
    tmp_path: Path,
) -> None:
    raw = tmp_path / "ruff.log"
    raw.write_bytes(b"All checks passed!\n")
    output = tmp_path / "quality-outputs/ruff.json"
    write_sanitized_quality_output("ruff", 0, raw, output)
    value = json.loads(output.read_text(encoding="utf-8"))
    assert value["gate"] == "ruff"
    assert value["metrics"]["issue_count"] == 0


@pytest.mark.parametrize(
    ("gate", "raw", "code"),
    [
        ("unsupported", b"safe", "FAIL_QUALITY_OUTPUT_GATE"),
        ("ruff", b"unexpected", "FAIL_QUALITY_OUTPUT_FORMAT"),
        ("mypy", b"unexpected", "FAIL_QUALITY_OUTPUT_FORMAT"),
        ("pytest", b"1 passed\nTotal coverage: 80%", "FAIL_QUALITY_OUTPUT_RESULT"),
        ("bandit", b"{}", "FAIL_QUALITY_OUTPUT_FORMAT"),
        ("pip-audit", b"{}", "FAIL_QUALITY_OUTPUT_FORMAT"),
        ("leak-scan", b"{}", "FAIL_QUALITY_OUTPUT_FORMAT"),
        ("governance-readback", b"{}", "FAIL_QUALITY_OUTPUT_FORMAT"),
    ],
)
def test_sanitized_quality_output_fails_closed(
    gate: str, raw: bytes, code: str
) -> None:
    with pytest.raises(FactoryFailure) as captured:
        sanitized_quality_output(gate, 0, raw)
    assert captured.value.code == code


def _locks(root: Path, *, version: str = "1.2.3") -> tuple[Path, Path]:
    lock_root = root / "locks"
    lock_root.mkdir(parents=True)
    paths = (
        lock_root / "requirements-s00-build.lock",
        lock_root / "requirements-s00-dev.lock",
    )
    for path in paths:
        path.write_text(
            f"example-package=={version} --hash=sha256:" + "c" * 64 + "\n",
            encoding="utf-8",
        )
    return paths


def _input_digests(locks: tuple[Path, Path]) -> dict[str, str]:
    return {
        "contract_path": CONTRACT_RELATIVE_PATH,
        "contract_actual_sha256": CONTRACT,
        "contract_approved_sha256": CONTRACT,
        "contract_digest_match": "true",
        "head_tree": TREE,
        **{path.name: sha256_file(path) for path in locks},
    }


def _quality_metrics(gate: str) -> dict[str, Any]:
    if gate in {"ruff", "mypy", "bandit"}:
        return {"issue_count": 0, **({"source_file_count": 1} if gate == "mypy" else {})}
    if gate == "pip-audit":
        return {"dependency_count": 1, "vulnerability_count": 0}
    if gate == "pytest":
        return {
            "passed": 1,
            "failed": 0,
            "skipped": 0,
            "coverage_percent": 100.0,
        }
    if gate == "leak-scan":
        return {
            "finding_count": 0,
            "scanned_file_count": 1,
            "profile": "V3-R1-S00-PROHIBITED-V3",
        }
    if gate == "environment-identity":
        return {
            "external_effect_budget": "DENY_ALL",
            "providers": "OFF",
            "email_mode": "NON_RELAYING",
        }
    return {
        "api_host": "api.github.com",
        "repository": REPOSITORY,
        "ruleset_id": 20583674,
        "enforcement": "active",
        "target_ref": "refs/heads/v3/main",
        "required_status_checks": [
            "S00 / build-candidate",
            "S00 / policy",
            "S00 / test",
            "S00 / verify-candidate",
        ],
        "required_approving_review_count": 1,
        "dismiss_stale_reviews_on_push": True,
        "require_code_owner_review": True,
        "required_review_thread_resolution": True,
        "bypass_actor_count": 0,
        "pr_number": 1,
        "pr_state": "open",
        "pr_draft": True,
        "pr_merged": False,
        "base_ref": "v3/main",
        "base_sha": "5be8413d3c22d1345b3088424af40ca2eb9d1115",
        "head_ref": BRANCH,
        "head_sha": COMMIT,
        "retrieval_context": {"github_actions_run_id": "123"},
        "github_approving_review_claimed": False,
    }


def _quality_record(
    gate: str, locks: tuple[Path, Path], output: Path
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "execution_id": f"GHA-100-1-{gate.upper().replace('-', '_')}",
        "timestamp_utc": "2026-08-08T15:00:00Z",
        "mutation_class": "READ_ONLY_QUALITY_GATE",
        "repository": REPOSITORY,
        "branch": BRANCH,
        "head_commit": COMMIT,
        "head_tree": TREE,
        "contract_sha256": CONTRACT,
        "contract_path": CONTRACT_RELATIVE_PATH,
        "contract_actual_sha256": CONTRACT,
        "contract_approved_sha256": CONTRACT,
        "contract_digest_match": True,
        "environment_identity": {
            "architecture": "x86_64",
            "email_mode": "NON_RELAYING",
            "external_effect_budget": "DENY_ALL",
            "providers": "OFF",
            "python_version": "3.11.2",
            "runner_os": "Linux",
        },
        "changed_paths": CHANGED_PATHS,
        "input_digests": _input_digests(locks),
        "command_or_gate": gate,
        "exit_code": 0,
        "result": "PASS",
        "next_allowed_action": "BUILD_ONCE_CANDIDATE",
        "output_sha256": "d" * 64,
        "output_path": f"reports/quality-outputs/{gate}.json",
        "output_size": output.stat().st_size,
    }
    record["output_sha256"] = sha256_file(output)
    if gate == "pytest":
        record["branch_coverage_threshold_percent"] = 90
    return record


def _write_quality_inputs(root: Path, locks: tuple[Path, Path]) -> list[dict[str, Any]]:
    root.mkdir(parents=True, exist_ok=True)
    output_root = root / "quality-outputs"
    output_root.mkdir()
    records: list[dict[str, Any]] = []
    for name, gates in QUALITY_GROUPS.items():
        group = []
        for gate in gates:
            output = output_root / f"{gate}.json"
            output.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "gate": gate,
                        "tool": gate,
                        "exit_code": 0,
                        "result": "PASS",
                        "metrics": _quality_metrics(gate),
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
                + "\n",
                encoding="utf-8",
            )
            group.append(_quality_record(gate, locks, output))
        records.extend(group)
        (root / name).write_text(
            json.dumps(
                {"schema_version": 1, "result": "PASS", "records": group},
                sort_keys=True,
                separators=(",", ":"),
            )
            + "\n",
            encoding="utf-8",
        )
    (root / "execution-ledger.jsonl").write_text(
        "".join(json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n" for item in records),
        encoding="utf-8",
    )
    return records


def _rehash_candidate(candidate: Path) -> None:
    paths = sorted(
        path.relative_to(candidate).as_posix()
        for path in candidate.rglob("*")
        if path.is_file() and path.name not in {"artifact-manifest.json", "SHA256SUMS"}
    )
    manifest = [item.to_dict() for item in build_manifest(candidate, paths)]
    (candidate / "artifact-manifest.json").write_text(
        json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    checksum_paths = sorted(paths + ["artifact-manifest.json"])
    (candidate / "SHA256SUMS").write_text(
        "".join(f"{sha256_file(candidate / path)}  {path}\n" for path in checksum_paths),
        encoding="ascii",
    )


def _synthetic_candidate(root: Path) -> Path:
    locks = _locks(root)
    candidate = root / "candidate"
    artifacts = candidate / "artifacts"
    reports = candidate / "reports"
    artifacts.mkdir(parents=True)
    reports.mkdir()
    wheel = artifacts / "ysf-0.1.0-py3-none-any.whl"
    write_reproducible_zip(
        wheel,
        {"ysf/__init__.py": b""},
        source_date_epoch=1_700_000_000,
    )
    quality_root = root / "quality"
    quality_records = _write_quality_inputs(quality_root, locks)
    for name in ("test-and-coverage.json", "lint-type-sast-dependency.json", "leak-scan.json"):
        shutil.copyfile(quality_root / name, reports / name)
    shutil.copyfile(quality_root / "governance-readback.json", reports / "governance-readback.json")
    shutil.copytree(quality_root / "quality-outputs", reports / "quality-outputs")
    shutil.copyfile(
        quality_root / "environment-identity.json", candidate / "environment-identity.json"
    )
    shutil.copyfile(quality_root / "execution-ledger.jsonl", candidate / "execution-ledger.jsonl")
    contract_target = candidate / "contract/slice-contract.yaml"
    contract_target.parent.mkdir()
    shutil.copyfile(_approved_contract(), contract_target)
    (reports / "gates.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "repository": REPOSITORY,
                "branch": BRANCH,
                "head_commit": COMMIT,
                "head_tree": TREE,
                "contract_sha256": CONTRACT,
                "contract_binding": {
                    "path": CONTRACT_RELATIVE_PATH,
                    "actual_sha256": CONTRACT,
                    "approved_sha256": CONTRACT,
                    "digest_match": True,
                },
                "changed_paths": CHANGED_PATHS,
                "gates": [
                    {"gate": gate, "result": "PASS", "message": "safe"} for gate in PREFLIGHT_GATES
                ],
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n",
        encoding="utf-8",
    )
    lock_digests = {path.name: sha256_file(path) for path in locks}
    components = _parse_lock_components(locks)
    (candidate / "sbom.cdx.json").write_text(
        json.dumps(
            {
                "bomFormat": "CycloneDX",
                "specVersion": "1.6",
                "version": 1,
                "metadata": {
                    "component": {"type": "application", "name": "ysf", "version": "0.1.0"},
                    "properties": [
                        {"name": "ysim:contract:sha256", "value": CONTRACT},
                        {"name": "ysim:contract:path", "value": CONTRACT_RELATIVE_PATH},
                        {"name": "ysim:contract:actual-sha256", "value": CONTRACT},
                        {"name": "ysim:contract:approved-sha256", "value": CONTRACT},
                        {"name": "ysim:contract:digest-match", "value": "true"},
                        {"name": "ysim:source:branch", "value": BRANCH},
                        {"name": "ysim:source:commit", "value": COMMIT},
                        {"name": "ysim:source:tree", "value": TREE},
                        *[
                            {"name": f"ysim:lock:{name}:sha256", "value": digest}
                            for name, digest in sorted(lock_digests.items())
                        ],
                    ],
                },
                "components": components,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n",
        encoding="utf-8",
    )
    wheel_digest = sha256_file(wheel)
    (candidate / "provenance.json").write_text(
        json.dumps(
            {
                "_type": "https://in-toto.io/Statement/v1",
                "subject": [
                    {"name": f"artifacts/{wheel.name}", "digest": {"sha256": wheel_digest}}
                ],
                "predicateType": "https://slsa.dev/provenance/v1",
                "predicate": {
                    "buildDefinition": {
                        "buildType": "https://ysim.vn/build-types/v3-r1-s00/ysf-wheel/v1",
                        "externalParameters": {
                            "branch": BRANCH,
                            "contract_sha256": CONTRACT,
                            "contract_binding": {
                                "path": CONTRACT_RELATIVE_PATH,
                                "actual_sha256": CONTRACT,
                                "approved_sha256": CONTRACT,
                                "digest_match": True,
                            },
                            "lock_digests": lock_digests,
                        },
                        "resolvedDependencies": [
                            {
                                "uri": f"git+https://github.com/{REPOSITORY}@{COMMIT}",
                                "digest": {"gitTree": TREE},
                            }
                        ],
                    },
                    "runDetails": {
                        "builder": {"id": "https://github.com/actions/runner"},
                        "metadata": {
                            "invocationId": f"{COMMIT}:{TREE}",
                            "startedOnEpoch": 1_700_000_000,
                            "finishedOnEpoch": 1_700_000_000,
                            "reproducibility": {
                                "independentBuildCount": 2,
                                "wheelSha256": wheel_digest,
                            },
                        },
                    },
                },
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n",
        encoding="utf-8",
    )
    assert len(quality_records) == 8
    _rehash_candidate(candidate)
    return candidate


def _verify(candidate: Path, **overrides: Any) -> Any:
    values = {
        "expected_repository": REPOSITORY,
        "expected_branch": BRANCH,
        "expected_commit": COMMIT,
        "expected_tree": TREE,
        "expected_contract_sha256": CONTRACT,
        "expected_contract_path": _approved_contract(),
        "expected_lock_paths": (
            candidate.parent / "locks/requirements-s00-build.lock",
            candidate.parent / "locks/requirements-s00-dev.lock",
        ),
        "expected_changed_paths": CHANGED_PATHS,
    }
    values.update(overrides)
    return verify_candidate(candidate, **values)


def test_candidate_verification_is_non_rebuilding_and_tamper_evident(tmp_path: Path) -> None:
    candidate = _synthetic_candidate(tmp_path)
    assert _verify(candidate).passed
    (candidate / "reports/gates.json").write_text('{"result":"FAIL"}\n', encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_MANIFEST_TAMPER"


def test_semantic_substitution_is_rejected_even_after_rehash(tmp_path: Path) -> None:
    candidate = _synthetic_candidate(tmp_path / "sbom")
    sbom = json.loads((candidate / "sbom.cdx.json").read_text(encoding="utf-8"))
    sbom["components"] = []
    (candidate / "sbom.cdx.json").write_text(json.dumps(sbom) + "\n", encoding="utf-8")
    _rehash_candidate(candidate)
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_SBOM_SEMANTICS"

    candidate = _synthetic_candidate(tmp_path / "provenance")
    provenance = json.loads((candidate / "provenance.json").read_text(encoding="utf-8"))
    provenance["predicate"]["runDetails"]["builder"]["id"] = "synthetic-substitute"
    (candidate / "provenance.json").write_text(json.dumps(provenance) + "\n", encoding="utf-8")
    _rehash_candidate(candidate)
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_PROVENANCE_SEMANTICS"


def test_contract_and_retained_quality_bytes_are_recomputed(tmp_path: Path) -> None:
    candidate = _synthetic_candidate(tmp_path / "contract")
    retained_contract = candidate / "contract/slice-contract.yaml"
    retained_contract.write_bytes(retained_contract.read_bytes() + b"\n")
    _rehash_candidate(candidate)
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_CONTRACT_DIGEST"

    candidate = _synthetic_candidate(tmp_path / "quality-digest")
    output = candidate / "reports/quality-outputs/ruff.json"
    value = json.loads(output.read_text(encoding="utf-8"))
    value["metrics"]["issue_count"] = 1
    output.write_text(json.dumps(value) + "\n", encoding="utf-8")
    _rehash_candidate(candidate)
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_QUALITY_OUTPUT_TAMPER"

    report = candidate / "reports/lint-type-sast-dependency.json"
    report_value = json.loads(report.read_text(encoding="utf-8"))
    ruff_record = next(
        item for item in report_value["records"] if item["command_or_gate"] == "ruff"
    )
    ruff_record["output_sha256"] = sha256_file(output)
    ruff_record["output_size"] = output.stat().st_size
    report.write_text(json.dumps(report_value) + "\n", encoding="utf-8")
    ledger = candidate / "execution-ledger.jsonl"
    records = [json.loads(line) for line in ledger.read_text(encoding="utf-8").splitlines()]
    ledger_record = next(item for item in records if item["command_or_gate"] == "ruff")
    ledger_record.update(
        {
            "output_sha256": ruff_record["output_sha256"],
            "output_size": ruff_record["output_size"],
        }
    )
    ledger.write_text(
        "".join(json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n" for item in records),
        encoding="utf-8",
    )
    _rehash_candidate(candidate)
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_QUALITY_OUTPUT_RESULT"


def test_evidence_missing_skipped_duplicate_and_wrong_identity_fail(tmp_path: Path) -> None:
    candidate = _synthetic_candidate(tmp_path / "missing")
    report_path = candidate / "reports/lint-type-sast-dependency.json"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    report["records"] = report["records"][:-1]
    report_path.write_text(json.dumps(report) + "\n", encoding="utf-8")
    _rehash_candidate(candidate)
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_EVIDENCE_GATE_SET"

    candidate = _synthetic_candidate(tmp_path / "identity")
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate, expected_commit="c" * 40)
    assert captured.value.code == "FAIL_GATE_REPORT_IDENTITY"


def test_build_candidate_refuses_second_build(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    repository.mkdir()
    contract = repository / CONTRACT_RELATIVE_PATH
    contract.parent.mkdir(parents=True)
    shutil.copyfile(_approved_contract(), contract)
    candidate = tmp_path / "candidate"
    candidate.mkdir()
    with pytest.raises(FactoryFailure) as captured:
        build_candidate(
            repository,
            candidate,
            repository=REPOSITORY,
            branch=BRANCH,
            commit=COMMIT,
            tree=TREE,
            contract_sha256=CONTRACT,
            source_date_epoch=1_700_000_000,
            gate_report={"changed_paths": CHANGED_PATHS, "gates": []},
            report_root=tmp_path,
        )
    assert captured.value.code == "FAIL_SECOND_BUILD"


def test_lock_components_and_dependency_closure_fail_closed(tmp_path: Path) -> None:
    first = tmp_path / "first.lock"
    second = tmp_path / "second.lock"
    first.write_text("Zulu_Pkg==2.0 --hash=sha256:" + "a" * 64 + "\n", encoding="utf-8")
    second.write_text("alpha==1.0 --hash=sha256:" + "b" * 64 + "\n", encoding="utf-8")
    assert [item["name"] for item in _parse_lock_components([first, second])] == [
        "alpha",
        "zulu-pkg",
    ]
    second.write_text("zulu-pkg==3.0 --hash=sha256:" + "c" * 64 + "\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        _parse_lock_components([first, second])
    assert captured.value.code == "FAIL_LOCK_CONFLICT"
    second.write_text("# no package\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        _parse_lock_components([second])
    assert captured.value.code == "FAIL_LOCK_EMPTY"

    declaration = tmp_path / "pyproject.toml"
    declaration.write_text(
        "[build-system]\nrequires=['alpha==1.0']\n"
        "[project]\nname='test'\nversion='0'\ndependencies=['missing==1.0']\n"
        "[project.optional-dependencies]\ndev=[]\n",
        encoding="utf-8",
    )
    second.write_text("alpha==1.0 --hash=sha256:" + "b" * 64 + "\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        verify_declared_dependency_closure(declaration, [second])
    assert captured.value.code == "FAIL_DEPENDENCY_CLOSURE"


def _build_repository(root: Path) -> tuple[Path, tuple[Path, Path], Path]:
    repository = root / "repo"
    tool = repository / "tools/ysf"
    tool.mkdir(parents=True)
    locks = (
        tool / "requirements-s00-build.lock",
        tool / "requirements-s00-dev.lock",
    )
    for path in locks:
        path.write_text(
            "example-package==1.2.3 --hash=sha256:" + "a" * 64 + "\n",
            encoding="utf-8",
        )
    (tool / "pyproject.toml").write_text(
        "[build-system]\nrequires=['example-package==1.2.3']\n"
        "[project]\nname='ysf'\nversion='0.1.0'\ndependencies=['example-package==1.2.3']\n"
        "[project.optional-dependencies]\ndev=['example-package==1.2.3']\n",
        encoding="utf-8",
    )
    contract = repository / CONTRACT_RELATIVE_PATH
    contract.parent.mkdir(parents=True)
    shutil.copyfile(_approved_contract(), contract)
    report_root = root / "reports"
    _write_quality_inputs(report_root, locks)
    return repository, locks, report_root


def test_build_candidate_proves_actual_wheel_reproducibility_and_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repository, locks, report_root = _build_repository(tmp_path)
    observed_build_sources: list[Path] = []

    def successful_run(command: list[str], **_: object) -> CompletedProcess[str]:
        output = Path(command[command.index("--outdir") + 1])
        build_source = Path(command[-1])
        assert build_source.is_dir()
        assert repository not in build_source.parents
        observed_build_sources.append(build_source)
        write_reproducible_zip(
            output / "ysf-0.1.0-py3-none-any.whl",
            {"ysf/__init__.py": b""},
            source_date_epoch=1_700_000_000,
        )
        return CompletedProcess(command, 0, "", "")

    monkeypatch.setattr("ysf.secure_factory.candidate.subprocess.run", successful_run)
    candidate = tmp_path / "candidate"
    result = build_candidate(
        repository,
        candidate,
        repository=REPOSITORY,
        branch=BRANCH,
        commit=COMMIT,
        tree=TREE,
        contract_sha256=CONTRACT,
        source_date_epoch=1_700_000_000,
        gate_report={
            "changed_paths": CHANGED_PATHS,
            "gates": [
                {"gate": gate, "result": "PASS", "message": "safe"} for gate in PREFLIGHT_GATES
            ],
        },
        report_root=report_root,
    )
    assert result.passed
    assert len(observed_build_sources) == 2
    assert all(not path.exists() for path in observed_build_sources)
    assert verify_candidate(
        candidate,
        expected_repository=REPOSITORY,
        expected_branch=BRANCH,
        expected_commit=COMMIT,
        expected_tree=TREE,
        expected_contract_sha256=CONTRACT,
        expected_contract_path=repository / CONTRACT_RELATIVE_PATH,
        expected_lock_paths=locks,
        expected_changed_paths=CHANGED_PATHS,
    ).passed
    assert not (repository / "tools/ysf/build").exists()

    monkeypatch.setattr(
        "ysf.secure_factory.candidate.subprocess.run",
        lambda *args, **kwargs: CompletedProcess(args, 7, "", ""),
    )
    with pytest.raises(FactoryFailure) as captured:
        build_candidate(
            repository,
            tmp_path / "failed-candidate",
            repository=REPOSITORY,
            branch=BRANCH,
            commit=COMMIT,
            tree=TREE,
            contract_sha256=CONTRACT,
            source_date_epoch=1_700_000_000,
            gate_report={"changed_paths": CHANGED_PATHS, "gates": []},
            report_root=report_root,
        )
    assert captured.value.code == "FAIL_CANDIDATE_BUILD"


def test_candidate_rejects_file_set_path_and_format_failures(tmp_path: Path) -> None:
    with pytest.raises(FactoryFailure) as captured:
        _verify(tmp_path / "missing")
    assert captured.value.code == "FAIL_CANDIDATE_PATH"

    candidate = _synthetic_candidate(tmp_path / "link-source")
    link = tmp_path / "candidate-link"
    link.symlink_to(candidate, target_is_directory=True)
    with pytest.raises(FactoryFailure) as captured:
        _verify(
            link, expected_lock_paths=(candidate.parent / "locks/a", candidate.parent / "locks/b")
        )
    assert captured.value.code == "FAIL_CANDIDATE_PATH"

    candidate = _synthetic_candidate(tmp_path / "missing-required")
    (candidate / "sbom.cdx.json").unlink()
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_CANDIDATE_INCOMPLETE"

    candidate = _synthetic_candidate(tmp_path / "two-wheels")
    wheel = next((candidate / "artifacts").glob("*.whl"))
    shutil.copyfile(wheel, candidate / "artifacts/other.whl")
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_WHEEL_COUNT"

    candidate = _synthetic_candidate(tmp_path / "member-link")
    (candidate / "link").symlink_to(candidate / "reports/gates.json")
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_CANDIDATE_SYMLINK"

    candidate = _synthetic_candidate(tmp_path / "bad-manifest")
    (candidate / "artifact-manifest.json").write_text("{}\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_MANIFEST_FORMAT"

    candidate = _synthetic_candidate(tmp_path / "bad-checksum")
    (candidate / "SHA256SUMS").write_text("invalid\n", encoding="ascii")
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_CHECKSUM_FORMAT"

    candidate = _synthetic_candidate(tmp_path / "extra-file")
    (candidate / "unexpected.txt").write_text("safe", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_MANIFEST_FILE_SET"

    candidate = _synthetic_candidate(tmp_path / "checksum-set")
    lines = (candidate / "SHA256SUMS").read_text(encoding="ascii").splitlines()
    (candidate / "SHA256SUMS").write_text("\n".join(lines[1:]) + "\n", encoding="ascii")
    with pytest.raises(FactoryFailure) as captured:
        _verify(candidate)
    assert captured.value.code == "FAIL_CHECKSUM_FILE_SET"
