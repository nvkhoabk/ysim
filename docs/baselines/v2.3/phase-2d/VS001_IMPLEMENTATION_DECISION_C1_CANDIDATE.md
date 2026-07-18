# VS001 Implementation Decision C1 Candidate

- Candidate: `V23-P2D-VS001-IMPLEMENTATION-DECISION-C1`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_APPROVAL`
- Governing commit: `4a0ff5700554023b30d9a6dba01d80d1dbc78867`
- Implementation authorized: `false`
- Runtime evidence: `NOT_EXECUTED`
- Implementation contract created: `false`
- Next gate: `HUMAN_PHASE_2D_VS001_IMPLEMENTATION_DECISION_REQUIRED`

Resolve observable-interface, data-lifecycle, security-boundary and future-compatibility choices before an implementation contract can authorize VS001 work.

## Authority objects

| Authority | Commit | Git path | Blob | SHA-256 | Role |
|---|---|---|---|---|---|
| `COMMISSIONING_C1_APPROVAL` | `c3429e79b2e80ac050b21dd9dc5844dd64029ce0` | `docs/baselines/v2.3/phase-2d/PRODUCT_IMPLEMENTATION_COMMISSIONING_C1_APPROVAL.md` | `4aa6eef4bceeaa6416a39186b72301fe4f1a9883` | `ae547142f29eb98950e86f99a1b61e301e082b8f8fe8ea9b6f6adba4025f5512` | Approved runtime, framework, database, migration and test-tool selections. |
| `COMMISSIONING_I1_R1_APPROVAL` | `f7f2aeca3c1643996f77dec1b0b5caae22363ddc` | `docs/baselines/v2.3/phase-2d/PRODUCT_IMPLEMENTATION_COMMISSIONING_I1_R1_APPROVAL.md` | `f2a856c92f91e14b631e3dfa8ce2f8ed09ee06d1` | `85ae4091af9fdcfb26c49bbbbf0623e9d85c62a69ce12e50235715368bfefc87` | Accepted technical foundation and reusable command/resource boundary. |
| `VS001_DECISION_C1_CANONICAL` | `f003eca82512887a616c4ee83ed4ab8da4432b8a` | `docs/baselines/v2.3/phase-2d/vs001-acceptance-decision-c1.json` | `d4786ec62ca6d4df9b667f7c835857c630ad3c89` | `b5f7ffb9eae4167749ffd5c7ba1038afe401d9e0366103f6223dbb8966695b3f` | Canonical rules for eligibility, public display, slug and uniform not-found behavior. |
| `VS001_DECISION_C1_APPROVAL` | `c818d734049fbf8997a5dce4e1e66e65d6a92f59` | `docs/baselines/v2.3/phase-2d/VS001_ACCEPTANCE_DECISION_C1_APPROVAL.md` | `7fd209449aee059da33324391b2e8e55aded7ee2` | `7907d2b523dbe24facabbf00bb4c9c34594dc55ebf2dfe77b3ea274f3f0afad5` | Detached effective selections for DEC-001, DEC-002 and DEC-003. |
| `VS001_ELABORATION_C2_R2_CANONICAL` | `5780bf5e89c66103980fd4cda7c2b294fdc23f20` | `docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r2.json` | `ab9535b8b54b9dcbff60761d24bf744b380a0b31` | `d80d6c5b00660eb9dc5a8d3835f9dd6baecca93e732def903f568b675af71ac7` | Signed 25-requirement acceptance population, 21 obligations, 32 criteria and 124 decision-derived clauses. |
| `VS001_ELABORATION_C2_R2_APPROVAL` | `4a0ff5700554023b30d9a6dba01d80d1dbc78867` | `docs/baselines/v2.3/phase-2d/VS001_ACCEPTANCE_ELABORATION_C2_R2_APPROVAL.md` | `1cdb2c8f7f915d97755676732fde1760e55f3df1` | `894892358e1bfaa8b22710b92abf7b962042e7a861fa12c12119a29531532987` | Detached acceptance-elaboration approval and current governing HEAD. |

## Accepted authority reconciliation

- Requirements: `25`
- Retained contracts: `9`
- Elaborated contracts: `16`
- Source obligations: `21`
- Acceptance criteria: `32`
- Decision clauses: `124`

## Technical decision audit

| ID | Topic | Class | Disposition | Decision |
|---|---|---|---|---|
| `TDA-001` | Node, pnpm, NestJS/Fastify, Next/React, PostgreSQL, Prisma, Vitest and Playwright versions | `A` | Reuse exact accepted commissioning selections without replacement. | — |
| `TDA-002` | API route paths and versioning | `C` | Public compatibility surface requires human selection. | `V23-P2D-VS001-IMPLEMENTATION-DEC-001` |
| `TDA-003` | Storefront request context, locale input and localization fallback | `C` | Affects Storefront isolation and observable localized content. | `V23-P2D-VS001-IMPLEMENTATION-DEC-002` |
| `TDA-004` | Pagination and deterministic ordering | `C` | Changes list contract and future compatibility. | `V23-P2D-VS001-IMPLEMENTATION-DEC-003` |
| `TDA-005` | Public list/detail response schemas | `C` | Wire representation is publicly observable. | `V23-P2D-VS001-IMPLEMENTATION-DEC-004` |
| `TDA-006` | Uniform 404 PRODUCT_NOT_FOUND error envelope | `C` | Status and code are fixed; envelope shape remains a public compatibility choice. | `V23-P2D-VS001-IMPLEMENTATION-DEC-004` |
| `TDA-007` | Media and primary-image representation | `C` | Public value shape and delivery indirection are observable. | `V23-P2D-VS001-IMPLEMENTATION-DEC-004` |
| `TDA-008` | Stable public slug storage and Storefront-scoped resolution | `C` | Controls identifier lifecycle and uniqueness. | `V23-P2D-VS001-IMPLEMENTATION-DEC-005` |
| `TDA-009` | Opaque canonical public Product identity | `C` | Public identity format and persistence affect privacy and compatibility. | `V23-P2D-VS001-IMPLEMENTATION-DEC-005` |
| `TDA-010` | Product, Product Version, Catalog, Storefront Catalog, Publication, Price and typed-reference persistence | `C` | Defines authoritative lifecycle and reference integrity. | `V23-P2D-VS001-IMPLEMENTATION-DEC-006` |
| `TDA-011` | PostgreSQL tables, indexes and constraints | `C` | Irreversible data-lifecycle and future-compatibility consequences require approval. | `V23-P2D-VS001-IMPLEMENTATION-DEC-006` |
| `TDA-012` | Migration, seed and controlled-fixture ownership | `C` | Distinguishes schema lifecycle from disposable test data. | `V23-P2D-VS001-IMPLEMENTATION-DEC-007` |
| `TDA-013` | List/detail evaluation snapshot consistency | `C` | Concurrent publication and price changes can alter observable equality. | `V23-P2D-VS001-IMPLEMENTATION-DEC-008` |
| `TDA-014` | Publication-window clock control | `C` | Boundary evaluation requires an approved clock and snapshot rule. | `V23-P2D-VS001-IMPLEMENTATION-DEC-008` |
| `TDA-015` | Runtime publication-validation evidence | `C` | PASS authority and freshness affect eligibility. | `V23-P2D-VS001-IMPLEMENTATION-DEC-008` |
| `TDA-016` | Price resolution and ISO currency validation | `C` | Resolver ambiguity and snapshot identity are public eligibility inputs. | `V23-P2D-VS001-IMPLEMENTATION-DEC-008` |
| `TDA-017` | Internal/public data separation | `C` | Security boundary must be explicit and auditable. | `V23-P2D-VS001-IMPLEMENTATION-DEC-009` |
| `TDA-018` | API, UI and data correlation identifiers | `C` | Public exposure versus internal-only correlation is observable and security-relevant. | `V23-P2D-VS001-IMPLEMENTATION-DEC-009` |
| `TDA-019` | Logging, audit reason codes and redaction | `C` | Must preserve internal diagnostics without public leakage. | `V23-P2D-VS001-IMPLEMENTATION-DEC-009` |
| `TDA-020` | Test isolation and Docker resource ownership | `A` | Reuse disposable project/volume ownership and success/failure cleanup from commissioning. | — |
| `TDA-021` | Controller, service, component and test-file names | `B` | Select locally after approval without changing semantic operations or public schemas. | — |
| `TDA-022` | Focused VS001 command script filenames | `B` | May be selected locally while preserving lifecycle, evidence and failure semantics. | — |
| `TDA-023` | Caching and materialized acceleration | `D` | Not required for VS001; no cache may become an unapproved authority. | — |
| `TDA-024` | Authentication, search, filter, recommendation, cart, checkout, inventory, procurement, promotion, tax and provider behavior | `D` | Excluded from VS001 and not selected by this pack. | — |
| `TDA-025` | Production deployment, CDN, observability vendor and YADF topology | `D` | Deferred beyond the VS001 implementation contract. | — |

## Human decisions

### V23-P2D-VS001-IMPLEMENTATION-DEC-001 — Public API Resource Paths and Versioning

- Classification: `C`
- Selected option: `None`
- Recommended option: `OPT-V1-STOREFRONT-RESOURCE-HIERARCHY`
- Question: Which stable public HTTP resource hierarchy and version boundary will expose LIST_PUBLIC_PRODUCTS and GET_PUBLIC_PRODUCT_BY_SLUG?
- Why human: Route hierarchy and versioning are externally observable and become a compatibility commitment.
- Source authorities: `COMMISSIONING_C1_APPROVAL`, `VS001_ELABORATION_C2_R2_CANONICAL`, `VS001_ELABORATION_C2_R2_APPROVAL`
- Impacted acceptance: `UXF-003`, `UXF-301`, `UXF-304`, `UXF-306`, `UXF-04-R011`, `UXF-05-R004`

#### OPT-V1-STOREFRONT-RESOURCE-HIERARCHY

- Summary: Versioned Storefront resource hierarchy with list and slug-detail beneath a public Storefront identifier.
- Contract: Use /api/v1/storefronts/{storefront_slug}/products and /api/v1/storefronts/{storefront_slug}/products/{public_slug}; web paths remain /catalog and /catalog/{public_slug} in the same Storefront context.
- Impact: Storefront isolation is explicit in the URI and API evolution has a visible v1 boundary.
- Rejection tradeoff: Longer URLs and future Storefront identifier changes require explicit compatibility handling.

#### OPT-V1-CATALOG-RESOURCE-WITH-STOREFRONT-HEADER

- Summary: Versioned catalog resources with Storefront supplied by a required public request header.
- Contract: Use /api/v1/catalog/products and /api/v1/catalog/products/{public_slug}; require X-Storefront-Slug and reject missing or ambiguous context without fallback.
- Impact: Short resource URLs but Storefront scope is less visible and browser/cache behavior depends on header variance.
- Rejection tradeoff: Higher risk of omitted-header leakage and more complex caching and evidence.

#### OPT-UNVERSIONED-STOREFRONT-RESOURCE

- Summary: Unversioned Storefront-scoped product resources.
- Contract: Use /storefronts/{storefront_slug}/products and slug detail without an explicit API version segment.
- Impact: Simpler initial surface with no declared version namespace.
- Rejection tradeoff: Future incompatible evolution lacks an agreed compatibility boundary.

Recommendation rationale: It makes Storefront isolation and compatibility versioning directly testable without inventing authentication.

Non-inferences:

- No authentication or organization administration.
- No search/filter endpoints.
- No route implementation is authorized by recommendation alone.

### V23-P2D-VS001-IMPLEMENTATION-DEC-002 — Storefront Context, Locale Input and Localization Fallback

- Classification: `C`
- Selected option: `None`
- Recommended option: `OPT-BCP47-REQUEST-THEN-STOREFRONT-DEFAULT`
- Question: How are requested Storefront and locale resolved, and what happens when localized mandatory content is unavailable?
- Why human: Context resolution controls isolation; fallback changes customer-visible content and mandatory-field eligibility.
- Source authorities: `VS001_DECISION_C1_CANONICAL`, `VS001_ELABORATION_C2_R2_CANONICAL`
- Impacted acceptance: `BD-04-001`, `BD-04-002`, `BD-05-001`, `UXF-301`, `UXF-304`, `UXF-306`

#### OPT-BCP47-REQUEST-THEN-STOREFRONT-DEFAULT

- Summary: Resolve a validated BCP 47 requested locale, then the configured Storefront default locale.
- Contract: Storefront comes only from the route/header mechanism selected by DEC-001; locale comes from Accept-Language. Exact supported locale wins, then Storefront default. If mandatory localized fields remain absent, exclude from list and use uniform not-found for detail; optional fields remain omitted.
- Impact: Deterministic fallback supports usable localized browsing while retaining mandatory-field guarantees.
- Rejection tradeoff: A fallback response may not use the caller's first requested locale and must expose the resolved content locale without internal state.

#### OPT-EXACT-BCP47-NO-FALLBACK

- Summary: Require an exact supported requested locale and never fall back.
- Contract: Unsupported or incomplete mandatory localized content excludes list entries and produces uniform not-found detail; optional fields are omitted.
- Impact: Strong locale predictability and no cross-locale substitution.
- Rejection tradeoff: Catalog availability can vary sharply by locale and empty states become more common.

#### OPT-STOREFRONT-DEFAULT-LOCALE-ONLY

- Summary: Ignore caller locale preference and always use the configured Storefront default locale.
- Contract: All list/detail content uses one Storefront locale; no request-level locale selection is exposed in VS001.
- Impact: Smallest contract and fixture matrix.
- Rejection tradeoff: Does not provide caller-driven localization despite localized source obligations.

Recommendation rationale: It preserves Storefront isolation, provides deterministic localization and fails closed when mandatory public content cannot be resolved.

Non-inferences:

- No localized slug.
- No machine translation.
- No inference of content from Product name.
- No cross-Storefront locale fallback.

### V23-P2D-VS001-IMPLEMENTATION-DEC-003 — List Pagination and Deterministic Ordering

- Classification: `C`
- Selected option: `None`
- Recommended option: `OPT-OPAQUE-CURSOR-SLUG-IDENTITY-ORDER`
- Question: What list-window and stable ordering contract prevents duplicates, omissions and nondeterministic evidence?
- Why human: Pagination and ordering are observable response semantics and affect future clients.
- Source authorities: `VS001_ELABORATION_C2_R2_CANONICAL`
- Impacted acceptance: `UXF-003`, `UXF-301`, `UXF-306`

#### OPT-OPAQUE-CURSOR-SLUG-IDENTITY-ORDER

- Summary: Opaque cursor pagination over deterministic public_slug then opaque canonical identity ordering.
- Contract: Default page size 20, maximum 100; cursor encodes no public internal IDs and represents the last public_slug plus opaque public identity in the evaluated Storefront snapshot.
- Impact: Stable traversal under a fixed snapshot and no offset drift.
- Rejection tradeoff: Cursor encoding and snapshot continuity add implementation and test complexity.

#### OPT-OFFSET-LIMIT-SLUG-IDENTITY-ORDER

- Summary: Offset/limit pagination with the same deterministic public ordering.
- Contract: Default limit 20, maximum 100; order by public_slug then opaque public identity; return total only if independently resolved in the same snapshot.
- Impact: Simple client navigation and test setup.
- Rejection tradeoff: Concurrent changes can shift offsets unless the implementation adds snapshot/version semantics.

#### OPT-UNPAGINATED-BOUNDED-VS001-LIST

- Summary: Return the complete eligible seeded Storefront catalog under an explicit maximum size.
- Contract: No pagination parameters; fail closed if eligible count exceeds 100; deterministic public_slug then opaque identity ordering remains mandatory.
- Impact: Smallest VS001 API and evidence surface.
- Rejection tradeoff: Creates an early hard size limit and requires a future public-contract change for growth.

Recommendation rationale: It provides deterministic evidence and better growth compatibility without exposing storage identity.

Non-inferences:

- No search or filter parameters.
- No recommendation ordering.
- No popularity or inventory ordering.

### V23-P2D-VS001-IMPLEMENTATION-DEC-004 — Public Wire Schema, Error Envelope and Media Representation

- Classification: `C`
- Selected option: `None`
- Recommended option: `OPT-EXPLICIT-DATA-META-DTO`
- Question: Which stable JSON projection and media representation carries the approved fields and uniform error without exposing internal state?
- Why human: Field names, envelopes and media indirection are public compatibility commitments.
- Source authorities: `VS001_DECISION_C1_CANONICAL`, `VS001_ELABORATION_C2_R2_CANONICAL`
- Impacted acceptance: `BD-05-001`, `UXF-301`, `UXF-304`, `UXF-306`, `UXF-05-R056`

#### OPT-EXPLICIT-DATA-META-DTO

- Summary: Explicit versioned DTOs inside data/meta envelopes with a minimal public error object.
- Contract: List returns {data:[PublicProductListItem],meta:{page}} and detail returns {data:PublicProductDetail}; primary_image is {url,alt}; uniform failure is {error:{code:'PRODUCT_NOT_FOUND',message:'Product not found'}} with HTTP 404 and no reason fields.
- Impact: Clear extension points and independently schema-validatable list/detail/error projections.
- Rejection tradeoff: Adds envelope nesting and commits exact public field names.

#### OPT-BARE-RESOURCE-DTO

- Summary: Bare array/object success payloads with a top-level public error object.
- Contract: List returns PublicProductListItem[]; detail returns PublicProductDetail; primary image remains a url/alt object; error is {code:'PRODUCT_NOT_FOUND',message:'Product not found'}.
- Impact: Minimal payload and client parsing.
- Rejection tradeoff: Future pagination and metadata additions require headers or a breaking envelope change.

#### OPT-JSONAPI-LIKE-RESOURCE-DOCUMENT

- Summary: Resource documents with type/id/attributes and errors collections.
- Contract: Represent public Product identity as resource id, approved fields as attributes, media as a public attribute object and uniform not-found as one errors entry carrying PRODUCT_NOT_FOUND.
- Impact: Standardized resource shape and extensibility.
- Rejection tradeoff: Higher ceremony and risk of accidentally exposing relationship or internal metadata not approved for VS001.

Recommendation rationale: It keeps the approved field boundary explicit while supporting pagination and schema evidence without supplier/internal relationships.

Non-inferences:

- No additional mandatory Product fields.
- No promotion, tax, inventory or cart properties.
- No internal reason in body or headers.
- No media storage provider selection.

### V23-P2D-VS001-IMPLEMENTATION-DEC-005 — Public Slug and Opaque Canonical Identity Persistence

- Classification: `C`
- Selected option: `None`
- Recommended option: `OPT-STOREFRONT-ENTRY-SLUG-UUIDV7-PUBLIC-ID`
- Question: How are Storefront-scoped stable slugs and opaque canonical public identities persisted without exposing storage or Supplier identifiers?
- Why human: Identifier lifecycle affects public compatibility, privacy and uniqueness constraints.
- Source authorities: `VS001_DECISION_C1_CANONICAL`, `VS001_ELABORATION_C2_R2_CANONICAL`
- Impacted acceptance: `BD-02-001`, `BD-04-001`, `UXF-301`, `UXF-304`, `UXF-04-R011`, `UXF-05-R004`

#### OPT-STOREFRONT-ENTRY-SLUG-UUIDV7-PUBLIC-ID

- Summary: Persist slug on the Storefront Catalog entry and a separate immutable UUIDv7 public Product identity.
- Contract: Enforce unique(storefront_id,public_slug), approved lowercase ASCII kebab grammar, immutable-after-publication slug in VS001 and unique UUIDv7 public_product_id unrelated to database sequence or Supplier reference.
- Impact: Direct Storefront lookup and sortable opaque public identity with explicit constraints.
- Rejection tradeoff: Slug history or future cross-Storefront canonical URLs require a later approved model.

#### OPT-SEPARATE-PUBLIC-IDENTIFIER-UUIDV4

- Summary: Use a dedicated public identifier table with Storefront-scoped slug and immutable UUIDv4 Product identity.
- Contract: Resolve slug through a typed identifier row linked to Storefront Catalog entry; disable alias/history rows in VS001; enforce uniqueness and grammar at database and application boundaries.
- Impact: Separates public identifier lifecycle from catalog projection and leaves controlled expansion space.
- Rejection tradeoff: Additional relation and resolver complexity for features explicitly excluded from VS001.

#### OPT-DERIVED-SLUG-ENCODED-INTERNAL-ID

- Summary: Derive slug from Product name and encode internal identity in the public identifier.
- Contract: Generate identifiers from display content plus reversible storage identity.
- Impact: Avoids a dedicated public identifier lifecycle.
- Rejection tradeoff: Conflicts with stable locale-neutral slug and no-internal-identity rules; retained only as an explicit rejectable alternative.

Recommendation rationale: It directly enforces Storefront uniqueness, stable slug and opaque canonical identity with the smallest approved VS001 model.

Non-inferences:

- No localized or historical slug.
- No alias or redirect.
- No direct lookup by database or Supplier ID.

### V23-P2D-VS001-IMPLEMENTATION-DEC-006 — VS001 Relational Persistence and Integrity Model

- Classification: `C`
- Selected option: `None`
- Recommended option: `OPT-HYBRID-RELATIONAL-CORE-JSONB-SPECIFICATION`
- Question: Which PostgreSQL representation preserves canonical Product authority, typed catalog projections, publication and price lifecycles?
- Why human: Table boundaries, reference ownership and constraints become durable data-lifecycle commitments.
- Source authorities: `COMMISSIONING_C1_APPROVAL`, `VS001_ELABORATION_C2_R2_CANONICAL`
- Impacted acceptance: `BD-02-001`, `BD-02-002`, `BD-04-001`, `BD-04-002`, `BD-04-003`, `BRD-WS-04-R001`, `BD-05-001`, `UXF-05-R018`

#### OPT-NORMALIZED-TYPED-RELATIONAL-MODEL

- Summary: Normalized typed tables for canonical Product, versions, catalog roles, entries, publication validation/window, localized public content, media and Storefront price.
- Contract: Use foreign keys and object-type-safe relations; unique current Product Version per Product, unique Storefront Catalog entry per Product/context, non-overlapping active publication rows where required, amount as exact decimal minor-unit-compatible value, ISO currency constraint, and no Supplier cost in public projection tables.
- Impact: Strong reference integrity and independently queryable evidence for every eligibility predicate.
- Rejection tradeoff: More migrations, joins and fixture setup than aggregate storage.

#### OPT-HYBRID-RELATIONAL-CORE-JSONB-SPECIFICATION

- Summary: Relational identity/lifecycle tables with source-defined public Product specification stored as validated JSONB.
- Contract: Keep Product, version, catalog, publication and price normalized; store conditional public specification in schema-versioned JSONB validated at write/publication boundaries.
- Impact: Retains lifecycle integrity while avoiding premature columns for conditional attributes.
- Rejection tradeoff: Database-level field constraints and query evidence for conditional attributes are weaker and require schema validators.

#### OPT-DENORMALIZED-PUBLIC-CATALOG-DOCUMENT

- Summary: Persist one denormalized Storefront public catalog document containing identity, publication, price and display data.
- Contract: Treat the document as a projection rebuilt from canonical entities; it may never become canonical Product authority.
- Impact: Simple read path and snapshot consistency.
- Rejection tradeoff: Greater stale-projection and dangling-reference risk, with harder independent evidence of typed ownership.

Recommendation rationale: It protects canonical lifecycle and typed references while avoiding unsupported mandatory columns for conditional Product specification fields.

Non-inferences:

- No Supplier procurement or inventory schema.
- No cart/order/payment tables.
- No Product Variant model.
- No rewrite of the accepted commissioning baseline migration.

### V23-P2D-VS001-IMPLEMENTATION-DEC-007 — Forward Migration, Seed and Controlled Fixture Ownership

- Classification: `C`
- Selected option: `None`
- Recommended option: `OPT-FORWARD-MIGRATION-SEPARATE-FIXTURE-LOADER`
- Question: How are durable schema migrations separated from deterministic disposable VS001 fixtures?
- Why human: Seed placement changes data lifecycle, cleanup safety and production compatibility.
- Source authorities: `COMMISSIONING_C1_APPROVAL`, `COMMISSIONING_I1_R1_APPROVAL`, `VS001_ELABORATION_C2_R2_CANONICAL`
- Impacted acceptance: `BD-02-001`, `BD-04-001`, `BD-05-001`, `UXF-04-R011`, `UXF-301`

#### OPT-FORWARD-MIGRATION-SEPARATE-FIXTURE-LOADER

- Summary: Add one or more forward-only schema migrations and a separate deterministic VS001 fixture loader/cleanup owner.
- Contract: Migrations contain schema only; fixtures use stable semantic fixture keys plus a run ownership token, run only in disposable local/test PostgreSQL, and cleanup deletes only owned rows/resources on success and failure.
- Impact: Clean lifecycle separation and safe reproducible evidence without production seed coupling.
- Rejection tradeoff: Requires dedicated fixture tooling and ownership validation.

#### OPT-MIGRATION-EMBEDS-REFERENCE-SEED

- Summary: Place deterministic VS001 Product/Catalog fixtures directly in forward migrations.
- Contract: Migration data becomes durable database history and is not removed by test cleanup.
- Impact: Migration verification immediately has browseable data.
- Rejection tradeoff: Conflates schema and test data, complicates production use and violates disposable fixture ownership.

#### OPT-RUNTIME-STARTUP-AUTO-SEED

- Summary: API startup creates missing VS001 schema data and fixtures.
- Contract: Startup performs idempotent data creation before serving requests.
- Impact: Low separate-tooling burden.
- Rejection tradeoff: Creates hidden runtime writes, weakens migration authority and risks persistent environment contamination.

Recommendation rationale: It reuses commissioning's forward-only migrations and disposable Docker ownership without turning fixtures into durable business seed data.

Non-inferences:

- No production business seed.
- No migration rewrite.
- No fixed container name or shared volume deletion.
- No runtime evidence is created in this decision pack.

### V23-P2D-VS001-IMPLEMENTATION-DEC-008 — Eligibility Evaluation Snapshot, Clock, Publication Validation and Price Resolution

- Classification: `C`
- Selected option: `None`
- Recommended option: `OPT-REQUEST-TIMESTAMP-REPEATABLE-READ-SNAPSHOT`
- Question: What request-scoped consistency model binds publication, reference, validation and price evidence for list/detail?
- Why human: Temporal and concurrent resolution choices can change observable eligibility and list/detail equality.
- Source authorities: `VS001_DECISION_C1_CANONICAL`, `VS001_ELABORATION_C2_R2_CANONICAL`
- Impacted acceptance: `BD-04-001`, `BD-04-003`, `BD-05-001`, `UXF-04-R011`, `UXF-301`, `UXF-304`, `UXF-306`

#### OPT-REQUEST-TIMESTAMP-REPEATABLE-READ-SNAPSHOT

- Summary: Capture one UTC evaluation instant and resolve all eligibility, publication, validation and price facts in one PostgreSQL repeatable-read snapshot.
- Contract: Inject the clock for controlled boundary tests; list cursor retains snapshot identity or fails closed when continuation cannot preserve it; detail resolves one coherent snapshot; publication validation PASS record and base price amount/currency must be current in that snapshot.
- Impact: Strong independent evidence and no mixed-version list/detail response within a request.
- Rejection tradeoff: Longer transactions or snapshot continuation mechanisms require careful limits.

#### OPT-REQUEST-TIMESTAMP-READ-COMMITTED-VERSION-CHECKS

- Summary: Capture one UTC instant but use read-committed queries with explicit entity/version stamps and retry on inconsistency.
- Contract: Every resolver receives the same evaluation instant; compare Product Version, publication-validation and price revision identifiers before serialization; retry once then fail closed.
- Impact: Short transactions with explicit optimistic consistency evidence.
- Rejection tradeoff: More resolver logic and retry behavior; failure semantics become observable under churn.

#### OPT-MATERIALIZED-ELIGIBLE-CATALOG-SNAPSHOT

- Summary: Read a prevalidated materialized Storefront catalog snapshot with immutable snapshot/version identity.
- Contract: Publication and price changes create a new snapshot; list/detail expose only one active validated snapshot and never fall back to raw unresolved state.
- Impact: Fast coherent reads and simple list/detail comparison.
- Rejection tradeoff: Introduces projection freshness, activation and rebuild lifecycle not otherwise required by VS001.

Recommendation rationale: It most directly proves the accepted publication-window, validation, reference and price predicates with a controlled clock and coherent evidence.

Non-inferences:

- No stock or reservation evaluation.
- No promotion or tax resolver.
- No cache authority.
- No claim that list and a later independent detail request share historical state unless the selected contract explicitly carries snapshot identity.

### V23-P2D-VS001-IMPLEMENTATION-DEC-009 — Public/Internal Separation, Correlation and Audit Redaction

- Classification: `C`
- Selected option: `None`
- Recommended option: `OPT-SERVER-CORRELATION-ID-ALLOWLISTED-AUDIT`
- Question: How will API/UI/data evidence correlate without exposing internal eligibility, Supplier, cost or storage details?
- Why human: Correlation exposure and logging policy define a security and privacy boundary.
- Source authorities: `VS001_DECISION_C1_CANONICAL`, `VS001_ELABORATION_C2_R2_CANONICAL`, `COMMISSIONING_I1_R1_APPROVAL`
- Impacted acceptance: `BD-02-002`, `BD-05-001`, `UXF-304`, `UXF-306`, `UXF-04-R011`, `UXF-05-R010`, `UXF-05-R018`, `UXF-05-R056`

#### OPT-SERVER-CORRELATION-ID-ALLOWLISTED-AUDIT

- Summary: Generate a server correlation UUID per request, expose only that opaque value, and use allowlisted structured internal audit fields.
- Contract: Return X-Correlation-Id on success and uniform failure; log correlation id, semantic operation, Storefront public identity and internal reason code only in protected evidence; redact Supplier identity/reference, cost, credentials, storage paths and raw request secrets; never vary public outcome by reason.
- Impact: Enables API/UI/data traceability and internal cause audit with an explicit public allowlist.
- Rejection tradeoff: Public correlation headers add a compatibility and abuse-monitoring surface.

#### OPT-INTERNAL-CORRELATION-ONLY

- Summary: Generate correlation identity internally but expose no correlation field or header publicly.
- Contract: Browser/API evidence correlates through test-harness capture and protected logs; public bodies and headers contain no correlation identity.
- Impact: Smallest public disclosure surface.
- Rejection tradeoff: Black-box support and API/UI/database evidence correlation are harder and depend on privileged test instrumentation.

#### OPT-VALIDATED-CLIENT-CORRELATION-ECHO

- Summary: Accept a constrained client correlation token and echo it after validation, otherwise generate a server value.
- Contract: Allow only bounded ASCII opaque tokens; never place the token into queries or unescaped logs; public response echoes only the validated token.
- Impact: Supports end-to-end caller tracing.
- Rejection tradeoff: Adds spoofing, log-injection and privacy risk plus more security tests.

Recommendation rationale: It makes required API/UI/data correlation independently observable while preserving uniform public not-found and strict redaction.

Non-inferences:

- No public internal reason code.
- No Supplier or cost logging authorization.
- No observability vendor selection.
- No production retention policy or deployment authorization.

## Implementation-contract blocker

- Code: `HUMAN_PHASE_2D_VS001_IMPLEMENTATION_DECISION_REQUIRED`
- Reason: Nine unresolved Type C choices affect public compatibility, data lifecycle, security boundaries or future compatibility.
- Required resolution: Human approval must select exactly one existing option for every decision in a detached approval layer; the candidate selected_option fields remain null.
- Smallest next step: Review the nine recommendations and approve or replace each with one listed option before authoring V23-P2D-VS001-IMPLEMENTATION-CONTRACT-C1.

## Reused technical foundation

- Node.js 24.18.0 and pnpm 11.13.1
- NestJS 11.1.28 with Fastify 5.10.0
- Next.js 16.2.10 with React 19.2.7
- PostgreSQL 18.4 and Prisma 7.8.0 forward-only migration harness
- Vitest 4.1.10 and Playwright 1.61.1
- Disposable Docker Compose project and volume ownership with cleanup after success and failure
- Existing commissioning lint, typecheck, test, build, smoke, migration and clean-checkout command interfaces

## Non-claims

- `NOT_VS001_IMPLEMENTATION_CONTRACT_APPROVAL`
- `NOT_VS001_IMPLEMENTATION_AUTHORIZATION`
- `NOT_RUNTIME_EVIDENCE`
- `NOT_APPLICATION_OR_PACKAGE_CODE`
- `NOT_DATABASE_SCHEMA_OR_MIGRATION`
- `NOT_API_OR_UI_IMPLEMENTATION`
- `NOT_COMMISSIONING_MODIFICATION`
- `NOT_BRD_UXF_MODIFICATION`
- `NOT_YADF_DEPLOYMENT_OR_PRODUCTION_WORK`

## Independent machine-readable projections

<!-- METADATA_JSON:V23-P2D-VS001-IMPLEMENTATION-DECISION-C1 -->
```json
{"approval":"PENDING_HUMAN_APPROVAL","candidate_id":"V23-P2D-VS001-IMPLEMENTATION-DECISION-C1","governing_commit":"4a0ff5700554023b30d9a6dba01d80d1dbc78867","implementation_authorized":false,"implementation_contract_created":false,"next_gate":"HUMAN_PHASE_2D_VS001_IMPLEMENTATION_DECISION_REQUIRED","runtime_evidence_status":"NOT_EXECUTED","status":"CANDIDATE"}
```

<!-- RECONCILIATION_JSON:ACCEPTED_AUTHORITY -->
```json
{"acceptance_criteria":32,"decision_clause_counts":{"V23-P2D-VS001-ACCEPTANCE-DEC-001":27,"V23-P2D-VS001-ACCEPTANCE-DEC-002":54,"V23-P2D-VS001-ACCEPTANCE-DEC-003":43},"decision_clauses":124,"effective_selections":{"V23-P2D-VS001-ACCEPTANCE-DEC-001":"OPT-PUBLISHED-STOREFRONT-ELIGIBLE","V23-P2D-VS001-ACCEPTANCE-DEC-002":"OPT-MINIMUM-COMMERCIAL-DISPLAY-WITH-PRICE","V23-P2D-VS001-ACCEPTANCE-DEC-003":"OPT-STABLE-SLUG-UNIFORM-NOT-FOUND"},"elaborated_contracts":16,"requirement_ids":["BRD-UPDATE-01-R001","BRD-WS-02-R002","BRD-WS-02-R003","BD-04-005","UXF-010","UXF-011","UXF-109","UXF-402","UXF-405","BD-02-001","BD-02-002","BD-04-001","BD-04-002","BD-04-003","BRD-WS-04-R001","BD-05-001","UXF-003","UXF-301","UXF-304","UXF-306","UXF-04-R011","UXF-05-R004","UXF-05-R010","UXF-05-R018","UXF-05-R056"],"requirements_total":25,"retained_contracts":9,"source_obligations":21,"verification_result":"RECONCILED_FROM_ACCEPTED_GIT_OBJECTS"}
```

<!-- AUDIT_JSON:TECHNICAL_DECISION_AUDIT -->
```json
[{"audit_id":"TDA-001","classification":"A","decision_id":null,"disposition":"Reuse exact accepted commissioning selections without replacement.","topic":"Node, pnpm, NestJS/Fastify, Next/React, PostgreSQL, Prisma, Vitest and Playwright versions"},{"audit_id":"TDA-002","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-001","disposition":"Public compatibility surface requires human selection.","topic":"API route paths and versioning"},{"audit_id":"TDA-003","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-002","disposition":"Affects Storefront isolation and observable localized content.","topic":"Storefront request context, locale input and localization fallback"},{"audit_id":"TDA-004","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-003","disposition":"Changes list contract and future compatibility.","topic":"Pagination and deterministic ordering"},{"audit_id":"TDA-005","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-004","disposition":"Wire representation is publicly observable.","topic":"Public list/detail response schemas"},{"audit_id":"TDA-006","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-004","disposition":"Status and code are fixed; envelope shape remains a public compatibility choice.","topic":"Uniform 404 PRODUCT_NOT_FOUND error envelope"},{"audit_id":"TDA-007","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-004","disposition":"Public value shape and delivery indirection are observable.","topic":"Media and primary-image representation"},{"audit_id":"TDA-008","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-005","disposition":"Controls identifier lifecycle and uniqueness.","topic":"Stable public slug storage and Storefront-scoped resolution"},{"audit_id":"TDA-009","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-005","disposition":"Public identity format and persistence affect privacy and compatibility.","topic":"Opaque canonical public Product identity"},{"audit_id":"TDA-010","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-006","disposition":"Defines authoritative lifecycle and reference integrity.","topic":"Product, Product Version, Catalog, Storefront Catalog, Publication, Price and typed-reference persistence"},{"audit_id":"TDA-011","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-006","disposition":"Irreversible data-lifecycle and future-compatibility consequences require approval.","topic":"PostgreSQL tables, indexes and constraints"},{"audit_id":"TDA-012","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-007","disposition":"Distinguishes schema lifecycle from disposable test data.","topic":"Migration, seed and controlled-fixture ownership"},{"audit_id":"TDA-013","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-008","disposition":"Concurrent publication and price changes can alter observable equality.","topic":"List/detail evaluation snapshot consistency"},{"audit_id":"TDA-014","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-008","disposition":"Boundary evaluation requires an approved clock and snapshot rule.","topic":"Publication-window clock control"},{"audit_id":"TDA-015","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-008","disposition":"PASS authority and freshness affect eligibility.","topic":"Runtime publication-validation evidence"},{"audit_id":"TDA-016","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-008","disposition":"Resolver ambiguity and snapshot identity are public eligibility inputs.","topic":"Price resolution and ISO currency validation"},{"audit_id":"TDA-017","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-009","disposition":"Security boundary must be explicit and auditable.","topic":"Internal/public data separation"},{"audit_id":"TDA-018","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-009","disposition":"Public exposure versus internal-only correlation is observable and security-relevant.","topic":"API, UI and data correlation identifiers"},{"audit_id":"TDA-019","classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-009","disposition":"Must preserve internal diagnostics without public leakage.","topic":"Logging, audit reason codes and redaction"},{"audit_id":"TDA-020","classification":"A","decision_id":null,"disposition":"Reuse disposable project/volume ownership and success/failure cleanup from commissioning.","topic":"Test isolation and Docker resource ownership"},{"audit_id":"TDA-021","classification":"B","decision_id":null,"disposition":"Select locally after approval without changing semantic operations or public schemas.","topic":"Controller, service, component and test-file names"},{"audit_id":"TDA-022","classification":"B","decision_id":null,"disposition":"May be selected locally while preserving lifecycle, evidence and failure semantics.","topic":"Focused VS001 command script filenames"},{"audit_id":"TDA-023","classification":"D","decision_id":null,"disposition":"Not required for VS001; no cache may become an unapproved authority.","topic":"Caching and materialized acceleration"},{"audit_id":"TDA-024","classification":"D","decision_id":null,"disposition":"Excluded from VS001 and not selected by this pack.","topic":"Authentication, search, filter, recommendation, cart, checkout, inventory, procurement, promotion, tax and provider behavior"},{"audit_id":"TDA-025","classification":"D","decision_id":null,"disposition":"Deferred beyond the VS001 implementation contract.","topic":"Production deployment, CDN, observability vendor and YADF topology"}]
```

<!-- DECISION_JSON:V23-P2D-VS001-IMPLEMENTATION-DEC-001 -->
```json
{"classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-001","impacted_acceptance":["UXF-003","UXF-301","UXF-304","UXF-306","UXF-04-R011","UXF-05-R004"],"non_inferences":["No authentication or organization administration.","No search/filter endpoints.","No route implementation is authorized by recommendation alone."],"options":[{"contract":"Use /api/v1/storefronts/{storefront_slug}/products and /api/v1/storefronts/{storefront_slug}/products/{public_slug}; web paths remain /catalog and /catalog/{public_slug} in the same Storefront context.","impact":"Storefront isolation is explicit in the URI and API evolution has a visible v1 boundary.","option_id":"OPT-V1-STOREFRONT-RESOURCE-HIERARCHY","rejection_tradeoff":"Longer URLs and future Storefront identifier changes require explicit compatibility handling.","summary":"Versioned Storefront resource hierarchy with list and slug-detail beneath a public Storefront identifier."},{"contract":"Use /api/v1/catalog/products and /api/v1/catalog/products/{public_slug}; require X-Storefront-Slug and reject missing or ambiguous context without fallback.","impact":"Short resource URLs but Storefront scope is less visible and browser/cache behavior depends on header variance.","option_id":"OPT-V1-CATALOG-RESOURCE-WITH-STOREFRONT-HEADER","rejection_tradeoff":"Higher risk of omitted-header leakage and more complex caching and evidence.","summary":"Versioned catalog resources with Storefront supplied by a required public request header."},{"contract":"Use /storefronts/{storefront_slug}/products and slug detail without an explicit API version segment.","impact":"Simpler initial surface with no declared version namespace.","option_id":"OPT-UNVERSIONED-STOREFRONT-RESOURCE","rejection_tradeoff":"Future incompatible evolution lacks an agreed compatibility boundary.","summary":"Unversioned Storefront-scoped product resources."}],"question":"Which stable public HTTP resource hierarchy and version boundary will expose LIST_PUBLIC_PRODUCTS and GET_PUBLIC_PRODUCT_BY_SLUG?","recommendation_rationale":"It makes Storefront isolation and compatibility versioning directly testable without inventing authentication.","recommended_option":"OPT-V1-STOREFRONT-RESOURCE-HIERARCHY","selected_option":null,"source_authorities":["COMMISSIONING_C1_APPROVAL","VS001_ELABORATION_C2_R2_CANONICAL","VS001_ELABORATION_C2_R2_APPROVAL"],"title":"Public API Resource Paths and Versioning","why_human":"Route hierarchy and versioning are externally observable and become a compatibility commitment."}
```

<!-- DECISION_JSON:V23-P2D-VS001-IMPLEMENTATION-DEC-002 -->
```json
{"classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-002","impacted_acceptance":["BD-04-001","BD-04-002","BD-05-001","UXF-301","UXF-304","UXF-306"],"non_inferences":["No localized slug.","No machine translation.","No inference of content from Product name.","No cross-Storefront locale fallback."],"options":[{"contract":"Storefront comes only from the route/header mechanism selected by DEC-001; locale comes from Accept-Language. Exact supported locale wins, then Storefront default. If mandatory localized fields remain absent, exclude from list and use uniform not-found for detail; optional fields remain omitted.","impact":"Deterministic fallback supports usable localized browsing while retaining mandatory-field guarantees.","option_id":"OPT-BCP47-REQUEST-THEN-STOREFRONT-DEFAULT","rejection_tradeoff":"A fallback response may not use the caller's first requested locale and must expose the resolved content locale without internal state.","summary":"Resolve a validated BCP 47 requested locale, then the configured Storefront default locale."},{"contract":"Unsupported or incomplete mandatory localized content excludes list entries and produces uniform not-found detail; optional fields are omitted.","impact":"Strong locale predictability and no cross-locale substitution.","option_id":"OPT-EXACT-BCP47-NO-FALLBACK","rejection_tradeoff":"Catalog availability can vary sharply by locale and empty states become more common.","summary":"Require an exact supported requested locale and never fall back."},{"contract":"All list/detail content uses one Storefront locale; no request-level locale selection is exposed in VS001.","impact":"Smallest contract and fixture matrix.","option_id":"OPT-STOREFRONT-DEFAULT-LOCALE-ONLY","rejection_tradeoff":"Does not provide caller-driven localization despite localized source obligations.","summary":"Ignore caller locale preference and always use the configured Storefront default locale."}],"question":"How are requested Storefront and locale resolved, and what happens when localized mandatory content is unavailable?","recommendation_rationale":"It preserves Storefront isolation, provides deterministic localization and fails closed when mandatory public content cannot be resolved.","recommended_option":"OPT-BCP47-REQUEST-THEN-STOREFRONT-DEFAULT","selected_option":null,"source_authorities":["VS001_DECISION_C1_CANONICAL","VS001_ELABORATION_C2_R2_CANONICAL"],"title":"Storefront Context, Locale Input and Localization Fallback","why_human":"Context resolution controls isolation; fallback changes customer-visible content and mandatory-field eligibility."}
```

<!-- DECISION_JSON:V23-P2D-VS001-IMPLEMENTATION-DEC-003 -->
```json
{"classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-003","impacted_acceptance":["UXF-003","UXF-301","UXF-306"],"non_inferences":["No search or filter parameters.","No recommendation ordering.","No popularity or inventory ordering."],"options":[{"contract":"Default page size 20, maximum 100; cursor encodes no public internal IDs and represents the last public_slug plus opaque public identity in the evaluated Storefront snapshot.","impact":"Stable traversal under a fixed snapshot and no offset drift.","option_id":"OPT-OPAQUE-CURSOR-SLUG-IDENTITY-ORDER","rejection_tradeoff":"Cursor encoding and snapshot continuity add implementation and test complexity.","summary":"Opaque cursor pagination over deterministic public_slug then opaque canonical identity ordering."},{"contract":"Default limit 20, maximum 100; order by public_slug then opaque public identity; return total only if independently resolved in the same snapshot.","impact":"Simple client navigation and test setup.","option_id":"OPT-OFFSET-LIMIT-SLUG-IDENTITY-ORDER","rejection_tradeoff":"Concurrent changes can shift offsets unless the implementation adds snapshot/version semantics.","summary":"Offset/limit pagination with the same deterministic public ordering."},{"contract":"No pagination parameters; fail closed if eligible count exceeds 100; deterministic public_slug then opaque identity ordering remains mandatory.","impact":"Smallest VS001 API and evidence surface.","option_id":"OPT-UNPAGINATED-BOUNDED-VS001-LIST","rejection_tradeoff":"Creates an early hard size limit and requires a future public-contract change for growth.","summary":"Return the complete eligible seeded Storefront catalog under an explicit maximum size."}],"question":"What list-window and stable ordering contract prevents duplicates, omissions and nondeterministic evidence?","recommendation_rationale":"It provides deterministic evidence and better growth compatibility without exposing storage identity.","recommended_option":"OPT-OPAQUE-CURSOR-SLUG-IDENTITY-ORDER","selected_option":null,"source_authorities":["VS001_ELABORATION_C2_R2_CANONICAL"],"title":"List Pagination and Deterministic Ordering","why_human":"Pagination and ordering are observable response semantics and affect future clients."}
```

<!-- DECISION_JSON:V23-P2D-VS001-IMPLEMENTATION-DEC-004 -->
```json
{"classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-004","impacted_acceptance":["BD-05-001","UXF-301","UXF-304","UXF-306","UXF-05-R056"],"non_inferences":["No additional mandatory Product fields.","No promotion, tax, inventory or cart properties.","No internal reason in body or headers.","No media storage provider selection."],"options":[{"contract":"List returns {data:[PublicProductListItem],meta:{page}} and detail returns {data:PublicProductDetail}; primary_image is {url,alt}; uniform failure is {error:{code:'PRODUCT_NOT_FOUND',message:'Product not found'}} with HTTP 404 and no reason fields.","impact":"Clear extension points and independently schema-validatable list/detail/error projections.","option_id":"OPT-EXPLICIT-DATA-META-DTO","rejection_tradeoff":"Adds envelope nesting and commits exact public field names.","summary":"Explicit versioned DTOs inside data/meta envelopes with a minimal public error object."},{"contract":"List returns PublicProductListItem[]; detail returns PublicProductDetail; primary image remains a url/alt object; error is {code:'PRODUCT_NOT_FOUND',message:'Product not found'}.","impact":"Minimal payload and client parsing.","option_id":"OPT-BARE-RESOURCE-DTO","rejection_tradeoff":"Future pagination and metadata additions require headers or a breaking envelope change.","summary":"Bare array/object success payloads with a top-level public error object."},{"contract":"Represent public Product identity as resource id, approved fields as attributes, media as a public attribute object and uniform not-found as one errors entry carrying PRODUCT_NOT_FOUND.","impact":"Standardized resource shape and extensibility.","option_id":"OPT-JSONAPI-LIKE-RESOURCE-DOCUMENT","rejection_tradeoff":"Higher ceremony and risk of accidentally exposing relationship or internal metadata not approved for VS001.","summary":"Resource documents with type/id/attributes and errors collections."}],"question":"Which stable JSON projection and media representation carries the approved fields and uniform error without exposing internal state?","recommendation_rationale":"It keeps the approved field boundary explicit while supporting pagination and schema evidence without supplier/internal relationships.","recommended_option":"OPT-EXPLICIT-DATA-META-DTO","selected_option":null,"source_authorities":["VS001_DECISION_C1_CANONICAL","VS001_ELABORATION_C2_R2_CANONICAL"],"title":"Public Wire Schema, Error Envelope and Media Representation","why_human":"Field names, envelopes and media indirection are public compatibility commitments."}
```

<!-- DECISION_JSON:V23-P2D-VS001-IMPLEMENTATION-DEC-005 -->
```json
{"classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-005","impacted_acceptance":["BD-02-001","BD-04-001","UXF-301","UXF-304","UXF-04-R011","UXF-05-R004"],"non_inferences":["No localized or historical slug.","No alias or redirect.","No direct lookup by database or Supplier ID."],"options":[{"contract":"Enforce unique(storefront_id,public_slug), approved lowercase ASCII kebab grammar, immutable-after-publication slug in VS001 and unique UUIDv7 public_product_id unrelated to database sequence or Supplier reference.","impact":"Direct Storefront lookup and sortable opaque public identity with explicit constraints.","option_id":"OPT-STOREFRONT-ENTRY-SLUG-UUIDV7-PUBLIC-ID","rejection_tradeoff":"Slug history or future cross-Storefront canonical URLs require a later approved model.","summary":"Persist slug on the Storefront Catalog entry and a separate immutable UUIDv7 public Product identity."},{"contract":"Resolve slug through a typed identifier row linked to Storefront Catalog entry; disable alias/history rows in VS001; enforce uniqueness and grammar at database and application boundaries.","impact":"Separates public identifier lifecycle from catalog projection and leaves controlled expansion space.","option_id":"OPT-SEPARATE-PUBLIC-IDENTIFIER-UUIDV4","rejection_tradeoff":"Additional relation and resolver complexity for features explicitly excluded from VS001.","summary":"Use a dedicated public identifier table with Storefront-scoped slug and immutable UUIDv4 Product identity."},{"contract":"Generate identifiers from display content plus reversible storage identity.","impact":"Avoids a dedicated public identifier lifecycle.","option_id":"OPT-DERIVED-SLUG-ENCODED-INTERNAL-ID","rejection_tradeoff":"Conflicts with stable locale-neutral slug and no-internal-identity rules; retained only as an explicit rejectable alternative.","summary":"Derive slug from Product name and encode internal identity in the public identifier."}],"question":"How are Storefront-scoped stable slugs and opaque canonical public identities persisted without exposing storage or Supplier identifiers?","recommendation_rationale":"It directly enforces Storefront uniqueness, stable slug and opaque canonical identity with the smallest approved VS001 model.","recommended_option":"OPT-STOREFRONT-ENTRY-SLUG-UUIDV7-PUBLIC-ID","selected_option":null,"source_authorities":["VS001_DECISION_C1_CANONICAL","VS001_ELABORATION_C2_R2_CANONICAL"],"title":"Public Slug and Opaque Canonical Identity Persistence","why_human":"Identifier lifecycle affects public compatibility, privacy and uniqueness constraints."}
```

<!-- DECISION_JSON:V23-P2D-VS001-IMPLEMENTATION-DEC-006 -->
```json
{"classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-006","impacted_acceptance":["BD-02-001","BD-02-002","BD-04-001","BD-04-002","BD-04-003","BRD-WS-04-R001","BD-05-001","UXF-05-R018"],"non_inferences":["No Supplier procurement or inventory schema.","No cart/order/payment tables.","No Product Variant model.","No rewrite of the accepted commissioning baseline migration."],"options":[{"contract":"Use foreign keys and object-type-safe relations; unique current Product Version per Product, unique Storefront Catalog entry per Product/context, non-overlapping active publication rows where required, amount as exact decimal minor-unit-compatible value, ISO currency constraint, and no Supplier cost in public projection tables.","impact":"Strong reference integrity and independently queryable evidence for every eligibility predicate.","option_id":"OPT-NORMALIZED-TYPED-RELATIONAL-MODEL","rejection_tradeoff":"More migrations, joins and fixture setup than aggregate storage.","summary":"Normalized typed tables for canonical Product, versions, catalog roles, entries, publication validation/window, localized public content, media and Storefront price."},{"contract":"Keep Product, version, catalog, publication and price normalized; store conditional public specification in schema-versioned JSONB validated at write/publication boundaries.","impact":"Retains lifecycle integrity while avoiding premature columns for conditional attributes.","option_id":"OPT-HYBRID-RELATIONAL-CORE-JSONB-SPECIFICATION","rejection_tradeoff":"Database-level field constraints and query evidence for conditional attributes are weaker and require schema validators.","summary":"Relational identity/lifecycle tables with source-defined public Product specification stored as validated JSONB."},{"contract":"Treat the document as a projection rebuilt from canonical entities; it may never become canonical Product authority.","impact":"Simple read path and snapshot consistency.","option_id":"OPT-DENORMALIZED-PUBLIC-CATALOG-DOCUMENT","rejection_tradeoff":"Greater stale-projection and dangling-reference risk, with harder independent evidence of typed ownership.","summary":"Persist one denormalized Storefront public catalog document containing identity, publication, price and display data."}],"question":"Which PostgreSQL representation preserves canonical Product authority, typed catalog projections, publication and price lifecycles?","recommendation_rationale":"It protects canonical lifecycle and typed references while avoiding unsupported mandatory columns for conditional Product specification fields.","recommended_option":"OPT-HYBRID-RELATIONAL-CORE-JSONB-SPECIFICATION","selected_option":null,"source_authorities":["COMMISSIONING_C1_APPROVAL","VS001_ELABORATION_C2_R2_CANONICAL"],"title":"VS001 Relational Persistence and Integrity Model","why_human":"Table boundaries, reference ownership and constraints become durable data-lifecycle commitments."}
```

<!-- DECISION_JSON:V23-P2D-VS001-IMPLEMENTATION-DEC-007 -->
```json
{"classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-007","impacted_acceptance":["BD-02-001","BD-04-001","BD-05-001","UXF-04-R011","UXF-301"],"non_inferences":["No production business seed.","No migration rewrite.","No fixed container name or shared volume deletion.","No runtime evidence is created in this decision pack."],"options":[{"contract":"Migrations contain schema only; fixtures use stable semantic fixture keys plus a run ownership token, run only in disposable local/test PostgreSQL, and cleanup deletes only owned rows/resources on success and failure.","impact":"Clean lifecycle separation and safe reproducible evidence without production seed coupling.","option_id":"OPT-FORWARD-MIGRATION-SEPARATE-FIXTURE-LOADER","rejection_tradeoff":"Requires dedicated fixture tooling and ownership validation.","summary":"Add one or more forward-only schema migrations and a separate deterministic VS001 fixture loader/cleanup owner."},{"contract":"Migration data becomes durable database history and is not removed by test cleanup.","impact":"Migration verification immediately has browseable data.","option_id":"OPT-MIGRATION-EMBEDS-REFERENCE-SEED","rejection_tradeoff":"Conflates schema and test data, complicates production use and violates disposable fixture ownership.","summary":"Place deterministic VS001 Product/Catalog fixtures directly in forward migrations."},{"contract":"Startup performs idempotent data creation before serving requests.","impact":"Low separate-tooling burden.","option_id":"OPT-RUNTIME-STARTUP-AUTO-SEED","rejection_tradeoff":"Creates hidden runtime writes, weakens migration authority and risks persistent environment contamination.","summary":"API startup creates missing VS001 schema data and fixtures."}],"question":"How are durable schema migrations separated from deterministic disposable VS001 fixtures?","recommendation_rationale":"It reuses commissioning's forward-only migrations and disposable Docker ownership without turning fixtures into durable business seed data.","recommended_option":"OPT-FORWARD-MIGRATION-SEPARATE-FIXTURE-LOADER","selected_option":null,"source_authorities":["COMMISSIONING_C1_APPROVAL","COMMISSIONING_I1_R1_APPROVAL","VS001_ELABORATION_C2_R2_CANONICAL"],"title":"Forward Migration, Seed and Controlled Fixture Ownership","why_human":"Seed placement changes data lifecycle, cleanup safety and production compatibility."}
```

<!-- DECISION_JSON:V23-P2D-VS001-IMPLEMENTATION-DEC-008 -->
```json
{"classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-008","impacted_acceptance":["BD-04-001","BD-04-003","BD-05-001","UXF-04-R011","UXF-301","UXF-304","UXF-306"],"non_inferences":["No stock or reservation evaluation.","No promotion or tax resolver.","No cache authority.","No claim that list and a later independent detail request share historical state unless the selected contract explicitly carries snapshot identity."],"options":[{"contract":"Inject the clock for controlled boundary tests; list cursor retains snapshot identity or fails closed when continuation cannot preserve it; detail resolves one coherent snapshot; publication validation PASS record and base price amount/currency must be current in that snapshot.","impact":"Strong independent evidence and no mixed-version list/detail response within a request.","option_id":"OPT-REQUEST-TIMESTAMP-REPEATABLE-READ-SNAPSHOT","rejection_tradeoff":"Longer transactions or snapshot continuation mechanisms require careful limits.","summary":"Capture one UTC evaluation instant and resolve all eligibility, publication, validation and price facts in one PostgreSQL repeatable-read snapshot."},{"contract":"Every resolver receives the same evaluation instant; compare Product Version, publication-validation and price revision identifiers before serialization; retry once then fail closed.","impact":"Short transactions with explicit optimistic consistency evidence.","option_id":"OPT-REQUEST-TIMESTAMP-READ-COMMITTED-VERSION-CHECKS","rejection_tradeoff":"More resolver logic and retry behavior; failure semantics become observable under churn.","summary":"Capture one UTC instant but use read-committed queries with explicit entity/version stamps and retry on inconsistency."},{"contract":"Publication and price changes create a new snapshot; list/detail expose only one active validated snapshot and never fall back to raw unresolved state.","impact":"Fast coherent reads and simple list/detail comparison.","option_id":"OPT-MATERIALIZED-ELIGIBLE-CATALOG-SNAPSHOT","rejection_tradeoff":"Introduces projection freshness, activation and rebuild lifecycle not otherwise required by VS001.","summary":"Read a prevalidated materialized Storefront catalog snapshot with immutable snapshot/version identity."}],"question":"What request-scoped consistency model binds publication, reference, validation and price evidence for list/detail?","recommendation_rationale":"It most directly proves the accepted publication-window, validation, reference and price predicates with a controlled clock and coherent evidence.","recommended_option":"OPT-REQUEST-TIMESTAMP-REPEATABLE-READ-SNAPSHOT","selected_option":null,"source_authorities":["VS001_DECISION_C1_CANONICAL","VS001_ELABORATION_C2_R2_CANONICAL"],"title":"Eligibility Evaluation Snapshot, Clock, Publication Validation and Price Resolution","why_human":"Temporal and concurrent resolution choices can change observable eligibility and list/detail equality."}
```

<!-- DECISION_JSON:V23-P2D-VS001-IMPLEMENTATION-DEC-009 -->
```json
{"classification":"C","decision_id":"V23-P2D-VS001-IMPLEMENTATION-DEC-009","impacted_acceptance":["BD-02-002","BD-05-001","UXF-304","UXF-306","UXF-04-R011","UXF-05-R010","UXF-05-R018","UXF-05-R056"],"non_inferences":["No public internal reason code.","No Supplier or cost logging authorization.","No observability vendor selection.","No production retention policy or deployment authorization."],"options":[{"contract":"Return X-Correlation-Id on success and uniform failure; log correlation id, semantic operation, Storefront public identity and internal reason code only in protected evidence; redact Supplier identity/reference, cost, credentials, storage paths and raw request secrets; never vary public outcome by reason.","impact":"Enables API/UI/data traceability and internal cause audit with an explicit public allowlist.","option_id":"OPT-SERVER-CORRELATION-ID-ALLOWLISTED-AUDIT","rejection_tradeoff":"Public correlation headers add a compatibility and abuse-monitoring surface.","summary":"Generate a server correlation UUID per request, expose only that opaque value, and use allowlisted structured internal audit fields."},{"contract":"Browser/API evidence correlates through test-harness capture and protected logs; public bodies and headers contain no correlation identity.","impact":"Smallest public disclosure surface.","option_id":"OPT-INTERNAL-CORRELATION-ONLY","rejection_tradeoff":"Black-box support and API/UI/database evidence correlation are harder and depend on privileged test instrumentation.","summary":"Generate correlation identity internally but expose no correlation field or header publicly."},{"contract":"Allow only bounded ASCII opaque tokens; never place the token into queries or unescaped logs; public response echoes only the validated token.","impact":"Supports end-to-end caller tracing.","option_id":"OPT-VALIDATED-CLIENT-CORRELATION-ECHO","rejection_tradeoff":"Adds spoofing, log-injection and privacy risk plus more security tests.","summary":"Accept a constrained client correlation token and echo it after validation, otherwise generate a server value."}],"question":"How will API/UI/data evidence correlate without exposing internal eligibility, Supplier, cost or storage details?","recommendation_rationale":"It makes required API/UI/data correlation independently observable while preserving uniform public not-found and strict redaction.","recommended_option":"OPT-SERVER-CORRELATION-ID-ALLOWLISTED-AUDIT","selected_option":null,"source_authorities":["VS001_DECISION_C1_CANONICAL","VS001_ELABORATION_C2_R2_CANONICAL","COMMISSIONING_I1_R1_APPROVAL"],"title":"Public/Internal Separation, Correlation and Audit Redaction","why_human":"Correlation exposure and logging policy define a security and privacy boundary."}
```

<!-- BLOCKER_JSON:IMPLEMENTATION_CONTRACT -->
```json
{"code":"HUMAN_PHASE_2D_VS001_IMPLEMENTATION_DECISION_REQUIRED","reason":"Nine unresolved Type C choices affect public compatibility, data lifecycle, security boundaries or future compatibility.","required_resolution":"Human approval must select exactly one existing option for every decision in a detached approval layer; the candidate selected_option fields remain null.","smallest_next_step":"Review the nine recommendations and approve or replace each with one listed option before authoring V23-P2D-VS001-IMPLEMENTATION-CONTRACT-C1."}
```

<!-- NON_CLAIMS_JSON:IMPLEMENTATION_DECISION_C1 -->
```json
["NOT_VS001_IMPLEMENTATION_CONTRACT_APPROVAL","NOT_VS001_IMPLEMENTATION_AUTHORIZATION","NOT_RUNTIME_EVIDENCE","NOT_APPLICATION_OR_PACKAGE_CODE","NOT_DATABASE_SCHEMA_OR_MIGRATION","NOT_API_OR_UI_IMPLEMENTATION","NOT_COMMISSIONING_MODIFICATION","NOT_BRD_UXF_MODIFICATION","NOT_YADF_DEPLOYMENT_OR_PRODUCTION_WORK"]
```
