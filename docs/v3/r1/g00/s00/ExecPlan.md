---
document_code: V3-R1-G00-S00-EXECPLAN
document_name: V3-R1 G00 S00 Active ExecPlan
project: YSim v3
document_set: V3-R1-G00-S00
version: 0.2.0
status: APPROVED
language: en
---
# V3-R1-G00-S00 Active ExecPlan

**Operational record:** `V3-R1-G00-S00-EXECPLAN-ACTIVE-001`  
**Approved source ExecPlan:** `V3-R1-G00-S00-EXECPLAN-002`, SHA-256
`fd92dcf8d7dd3ca7970f47774d09f1104d91de6f82ed7677c4e9026fe7f6d58d`  
**Contract SHA-256:**
`0c1c0e76c6ff55afd77c6c3aeaebae4a89bd2341870766c05d2ba8610a62b8dd`
**Status:** `ACTIVE_UNDER_HUMAN_CONTRACT_APPROVAL`

This file records progress without changing the byte-exact approved Contract.
Every failed or completed execution keeps a distinct immutable execution ID.

## Purpose

S00 builds a fail-closed repository source and candidate-delivery factory. Its
observable proof is one compliant source tree producing one reproducible,
checksummed, provenance-bound `ysf` wheel, while a deliberately noncompliant
synthetic fixture is rejected and its safe failure evidence is preserved.

The candidate retains exactly one authorized wheel. Reproducibility is proven
by a second independent build in disposable storage; its bytes are compared to
the retained wheel and then destroyed. A mismatch fails
`FAIL_WHEEL_REPRODUCIBILITY` and no candidate is authorized.

## Locked invariants

- The base is the protected `v3/main` source line at commit
  `5be8413d3c22d1345b3088424af40ca2eb9d1115` and tree
  `4631630f4d57872e08f6b523ab8adf0a94453673`; it inherits no legacy maturity.
- Only the 36 exact Contract paths may change.
- The 24 BRD and seven UXF files are immutable.
- Requirements remain `PROPOSED`; S01 owns exact source-anchor review.
- External-effect budget is `DENY_ALL`.
- Generated candidate/evidence output stays outside the Git checkout.
- Merge, default-branch change, tag/release, application deployment and
  production activation require later Human authority.

## Execution stages

| Stage | State | Evidence / next gate |
|---|---|---|
| RP-A Contract | `COMPLETED` | `HUMAN_CONTRACT_APPROVED` |
| Ruleset bootstrap B1-R1 | `COMPLETED` | `PASS_RULESET_APPLIED_AND_READ_BACK` |
| Source line B2-R1 | `COMPLETED` | `PASS_V3_MAIN_CREATED_AND_READ_BACK` |
| Isolated checkout B3-R1 | `COMPLETED` | `PASS_ISOLATED_V3_CHECKOUT_AND_IMPLEMENTATION_BRANCH_CREATED` |
| Context freeze B4-R1 | `IN_PROGRESS` | Review exact ten-path diff and corpus evidence |
| Dependency/toolchain lock | `BLOCKED_BY_B4_REVIEW` | Separate bounded execution |
| Factory controls and tests | `BLOCKED_BY_DEPENDENCY_LOCK` | Exact secure-factory allowlist only |
| CI/source integration | `PENDING` | Four named ruleset checks |
| RP-B behavior evidence | `PENDING` | Human decision against exact evidence |
| RP-C security/review | `PENDING` | Human source/security decision |
| Build-once candidate | `PENDING` | One immutable wheel/evidence identity |
| RP-D clean-room verify | `PENDING` | Non-rebuilding, non-installing verification |
| Closure | `PENDING` | Separate Human closure decision |

## Required repository entrypoint

Later implementation must expose only these bounded modes:

```text
bash scripts/v3-r1-s00.sh preflight
bash scripts/v3-r1-s00.sh verify
bash scripts/v3-r1-s00.sh known-bad
bash scripts/v3-r1-s00.sh build-candidate
bash scripts/v3-r1-s00.sh verify-candidate <candidate-path>
```

Context Freeze B4-R1 does not implement or execute these commands.
