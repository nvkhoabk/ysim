# VS-R1-002 — Slice Specification

## 1. Business outcome

An authenticated agency principal can open a role-aware Agency Portal shell only for an organization in which the principal has an active agency membership.

## 2. In scope

- Signed server-side agency session.
- Organization-context verification through the Platform API.
- Agency Admin and Agency User roles.
- Responsive Agency Portal shell.
- Organization name, code, market and role presentation.
- Role-aware navigation.
- Unauthenticated state.
- Access-denied state.
- Draft-organization state.
- Suspended-organization state.
- Empty dashboard state.
- Vietnamese and English shell copy.
- Browser runtime proof with real API, PostgreSQL and Next.js.
- Candidate and clean-checkout validation.

## 3. Out of scope

- Password login.
- OAuth.
- MFA.
- Invitation workflow.
- Session issuance endpoint.
- Public reverse-proxy authentication.
- Revenue data.
- Order listing.
- Commission data.
- Reference QR management.
- Team management workflow.
- Logout workflow.
- Lao localization.
- Production IAM.

## 4. Temporary session adapter

The slice uses an HMAC-signed cookie named:

```text
ysim_agency_session
```

Payload:

```text
identityId
organizationId
locale
expiresAt
```

The cookie is verified only on the Next.js server.

The browser never receives:

- `YSIM_BOOTSTRAP_TOKEN`
- `YSIM_PORTAL_SESSION_SECRET`
- Provider credentials

The session adapter is transitional. A future IAM slice replaces session issuance without changing Organization ownership or Portal context resolution.

## 5. Platform API behavior

New internal endpoint:

```text
GET /internal/r1/organizations/portal-context
```

Rules:

- Missing agency membership returns access denied.
- Non-agency role returns access denied.
- Draft organization returns HTTP 423 with structured organization status.
- Suspended organization returns HTTP 423 with structured organization status.
- Active organization with active Agency role returns organization and membership context.

Supporting lifecycle endpoint:

```text
POST /internal/r1/organizations/:organizationId/suspend
```

It is internal bootstrap functionality and records organization activity.

## 6. Portal states

- `unauthenticated`
- `denied`
- `organization-inactive`
- `suspended`
- `unavailable`
- `ready`

Each state is exposed through a stable `data-portal-state` attribute for browser acceptance.

## 7. Role-aware navigation

Agency User:

- Dashboard.
- Orders.
- Reference QR.

Agency Admin:

- Dashboard.
- Orders.
- Reference QR.
- Team.

These routes beyond `/agency` are navigation placeholders in this slice. Their business screens are not implemented.

## 8. Localization

The signed session selects:

- `vi`
- `en`

Lao localization is introduced in the R1.1 localization slice.

## 9. Runtime proof

The runtime proof must:

1. Start real PostgreSQL.
2. Apply committed migrations.
3. Start the real NestJS API.
4. Start the real Next.js production server.
5. Launch Chromium through Playwright.
6. Prove no cookie produces unauthenticated state.
7. Create Agency A and grant Agency Admin membership.
8. Prove Draft Agency A produces inactive state.
9. Activate Agency A.
10. Prove the ready shell and administrator navigation.
11. Create and activate Agency B.
12. Prove Agency A identity cannot open Agency B.
13. Suspend Agency A.
14. Prove suspended state.
15. Verify persisted suspension activity.
16. Stop browser, servers and Docker resources.

## 10. Security constraints

- Session secret contains at least 32 characters.
- Cookie signature uses HMAC-SHA256.
- Signature comparison is timing-safe.
- Expired or modified tokens are rejected.
- Organization ID from the cookie is re-authorized by API.
- Bootstrap token is server-only.
- Platform API calls are not cached.
- Cross-agency denial does not expose business data.
- Portal states contain no sensitive customer or eSIM data.

## 11. Acceptance

The slice is accepted only after:

- Existing VS-R1-001 tests remain green.
- New session and navigation tests pass.
- Browser runtime proof passes.
- Chromium is available in clean checkout.
- Candidate inventory is exact.
- Clean-checkout evidence is produced.
- Human acceptance is recorded.
