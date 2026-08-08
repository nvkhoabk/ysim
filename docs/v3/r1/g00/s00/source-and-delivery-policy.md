---
document_code: V3-R1-G00-S00-SOURCE-DELIVERY-POLICY
document_name: S00 Source and Delivery Policy
project: YSim v3
document_set: V3-R1-G00-S00
version: 0.2.0
status: FROZEN
language: en
---
# S00 Source and Delivery Policy

Contract: `V3-R1-G00-S00-CONTRACT-001 v0.2.0`  
Contract SHA-256:
`337519fcf7d08104ba0e53cbf33dcc4b4a75ec32aac18601cb097c778aa0ae35`

## Exact allowlist

Only these 36 repository paths may change during S00:

```text
AGENTS.md
.github/CODEOWNERS
.github/workflows/v3-r1-s00-secure-factory.yml
docs/v3/r1/g00/s00/README.md
docs/v3/r1/g00/s00/context-receipt.yaml
docs/v3/r1/g00/s00/clarification-register.yaml
docs/v3/r1/g00/s00/slice-contract.yaml
docs/v3/r1/g00/s00/ExecPlan.md
docs/v3/r1/g00/s00/source-and-delivery-policy.md
docs/v3/r1/g00/s00/environment-identity.yaml
docs/v3/r1/g00/s00/test-matrix.yaml
docs/v3/r1/g00/s00/evidence-schema.yaml
tools/ysf/pyproject.toml
tools/ysf/requirements-s00-build.lock
tools/ysf/requirements-s00-dev.lock
tools/ysf/src/ysf/cli.py
tools/ysf/src/ysf/secure_factory/__init__.py
tools/ysf/src/ysf/secure_factory/models.py
tools/ysf/src/ysf/secure_factory/cli.py
tools/ysf/src/ysf/secure_factory/environment.py
tools/ysf/src/ysf/secure_factory/policy.py
tools/ysf/src/ysf/secure_factory/sensitive.py
tools/ysf/src/ysf/secure_factory/evidence.py
tools/ysf/src/ysf/secure_factory/candidate.py
tools/ysf/tests/unit/test_secure_factory_environment.py
tools/ysf/tests/unit/test_secure_factory_policy.py
tools/ysf/tests/unit/test_secure_factory_sensitive.py
tools/ysf/tests/unit/test_secure_factory_evidence.py
tools/ysf/tests/unit/test_secure_factory_candidate.py
tools/ysf/tests/integration/test_secure_factory_pipeline.py
tools/ysf/tests/fixtures/secure_factory/compliant/README.txt
tools/ysf/tests/fixtures/secure_factory/noncompliant/path-escape.json
tools/ysf/tests/fixtures/secure_factory/noncompliant/synthetic-secret.txt
tools/ysf/tests/fixtures/secure_factory/noncompliant/synthetic-esim-payload.txt
tools/ysf/tests/fixtures/secure_factory/noncompliant/tampered-manifest.json
scripts/v3-r1-s00.sh
```

Every other path is default-deny. Any unexpected changed path produces
`FAIL_UNAPPROVED_PATH`.

## Protected data and paths

The following remain immutable: all paths outside the allowlist; `docs/BRD/**`;
`docs/UXF/**`; `factory/releases/**`; `factory/executions/**`;
`factory/evidence/**`; `knowledge/**`; business application/runtime paths;
secrets; environment data; deployment controls; and production configuration.

No real secret, PII, ICCID, LPA or QR payload may enter source, artifact or
evidence. Only clearly synthetic quarantined negative fixtures are permitted at
their exact allowlisted paths.

## Source control and delivery

Ruleset `20583674` protects `refs/heads/v3/main`, has no bypass actor, blocks
deletion and force push, requires one Human code-owner approval, dismissal of
stale approvals, conversation resolution, and these exact checks:

- `S00 / policy`
- `S00 / test`
- `S00 / build-candidate`
- `S00 / verify-candidate`

Candidate build occurs once in an isolated CI job from an exact commit/tree and
hash-locked dependencies. RP-D consumes those exact candidate bytes in a
separate clean-room job and must not rebuild, install or deploy them.
