# Product Implementation Commissioning C1

- Candidate: `V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-C1`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_APPROVAL`
- Governing decision: `V23-P2D-FIRST-SLICE-DECISION-001`
- Next gate: `HUMAN_PHASE_2D_PRODUCT_IMPLEMENTATION_COMMISSIONING_C1_APPROVAL`

## Purpose

This contract commissions only the product implementation workspace and process shells required before VS001. It creates no application code, product schema, business API, product UI, business seed, runtime adapter, provider integration, or deployment.

## Authoritative technology boundary

The approved documents establish a Node runtime category, pnpm workspace/package management, monorepo organization, deployable application shells under `apps/`, business/shared packages under `packages/`, centralized additive migrations under `database/`, automated testing, Docker availability where required, and clean-checkout validation.

They do not establish exact Node or pnpm versions, an API framework, UI framework, database engine, migration library, test libraries, or local database orchestration. Those choices remain explicit human decisions in the approval pack. Commissioning implementation cannot begin until every required technology decision is selected.

## Stable validation interface

Regardless of the selected implementation technologies, the commissioned root workspace must expose:

- `corepack pnpm install --frozen-lockfile`
- `corepack pnpm lint`
- `corepack pnpm typecheck`
- `corepack pnpm test`
- `corepack pnpm build`
- `corepack pnpm smoke:api`
- `corepack pnpm smoke:web`
- `corepack pnpm db:migrate:verify`
- `corepack pnpm bootstrap:clean-checkout`

## Acceptance boundary

Commissioning completes only when the approved path inventory is present, exact dependency versions are locked, all validation commands pass, API and UI processes expose non-business smoke surfaces, an ephemeral migration verification passes, evidence is captured, a clean checkout reproduces the result, Git is clean, and the independent no-business-logic gate reports zero findings.

## Correction and recovery

After approval, commissioning implementation has at most two correction passes. Recovery uses a normal Git revert of the commissioning implementation commit plus disposal of ephemeral local containers, databases, caches, and generated logs. Released migrations are never rewritten, destructive reset is not part of the procedure, and no production data or secret is involved.

## Non-claims

- No commissioning implementation is included.
- No VS001 acceptance elaboration or business implementation is included.
- No BRD/UXF source is changed.
- No runtime adapter, provider integration, YADF production work, deployment, or production authorization is included.
