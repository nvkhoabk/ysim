# VS-R1-001 — Slice Specification

## 1. Business outcome

Platform Administration can create and activate an agency organization, grant a principal an agency membership, and prove that the principal can resolve only its authorized organization context.

## 2. In scope

- YSim platform organization bootstrap.
- Agency organization lifecycle.
- Agency profile.
- Organization membership.
- Agency roles.
- Active organization-context resolution.
- Cross-agency denial.
- Append-only organization activity.
- PostgreSQL migration.
- Internal bootstrap API.
- Contract package.
- Unit and runtime tests.
- Clean candidate validation.

## 3. Out of scope

- Password authentication.
- OAuth or social login.
- MFA.
- Invitation email.
- Agency dashboard.
- Product entitlement.
- Agency Offer.
- Reference QR.
- Customer identity.
- Sub-agency.
- Production IAM gateway.

## 4. Bounded contexts

Primary:

- `ORG — Organization and Agency`

Supporting:

- `IAM — authenticated principal carrier contract`
- `AUD — future projection from append-only organization activity`

## 5. Security model

The slice exposes only internal bootstrap routes.

Administrative routes require:

- `YSIM_BOOTSTRAP_TOKEN` configured in the API process.
- `x-ysim-bootstrap-token` request header.
- `x-ysim-actor-id` UUID request header.

Organization-context resolution additionally requires:

- `x-ysim-identity-id`
- `x-ysim-organization-id`

The header-based identity carrier is temporary for this internal slice. It must not be exposed as a public trust boundary. A later IAM slice will replace the carrier without changing Organization ownership.

## 6. API routes

### Create agency

```text
POST /internal/r1/organizations/agencies
```

### Activate agency

```text
POST /internal/r1/organizations/:organizationId/activate
```

### Grant membership

```text
POST /internal/r1/organizations/:organizationId/memberships
```

### Resolve organization context

```text
GET /internal/r1/organizations/context
```

## 7. Data ownership

Owned by `ORG`:

- `organization_agency.organizations`
- `organization_agency.agency_profiles`
- `organization_agency.organization_memberships`
- `organization_agency.organization_activity`

The fixed YSim platform organization ID is:

```text
00000000-0000-4000-8000-000000000001
```

## 8. Organization states

- `DRAFT`
- `ACTIVE`
- `SUSPENDED`

New agencies begin in `DRAFT`.

Only an `ACTIVE` organization with an `ACTIVE` membership resolves as an authorized organization context.

## 9. Roles

- `PLATFORM_ADMIN`
- `OPERATIONS`
- `SUPPORT`
- `FINANCE_READ_ONLY`
- `AGENCY_ADMIN`
- `AGENCY_USER`

## 10. Idempotency and conflict behavior

- Organization code is unique.
- Agency code is unique.
- One active membership exists for an organization, identity and role tuple.
- Duplicate create or grant operations return a deterministic conflict.
- Activation of an already active agency returns the current organization without a second state transition.

## 11. Runtime proof

The runtime proof must:

1. Start a real PostgreSQL 18.4 container.
2. Apply committed migrations.
3. Build contracts and API.
4. Start the real API.
5. Create Agency A.
6. Grant a principal to Agency A.
7. Prove access is denied before activation.
8. Activate Agency A.
9. Prove Agency A context resolves.
10. Create Agency B.
11. Prove the Agency A principal cannot resolve Agency B.
12. Prove duplicate agency code is rejected.
13. Query persisted organization, membership and activity rows.
14. Stop the API.
15. Remove temporary Docker resources.

## 12. Acceptance

The slice is accepted only after:

- Automated validation passes.
- Runtime proof passes.
- Candidate inventory is exact.
- Clean-checkout evidence is produced.
- Human review records an acceptance result.
