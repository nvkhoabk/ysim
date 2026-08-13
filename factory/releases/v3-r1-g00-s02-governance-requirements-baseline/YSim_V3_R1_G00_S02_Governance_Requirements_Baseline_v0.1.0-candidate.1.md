# YSim V3 Release 1 — Governance Requirements Baseline

## V3-R1-G00-S02 — Candidate for Human Acceptance

| Field | Value |
| --- | --- |
| Document ID | `V3-R1-G00-S02-GOVERNANCE-REQUIREMENTS-BASELINE` |
| Candidate version | `0.1.0-candidate.1` |
| Candidate date | `2026-08-11` |
| Status | `CANDIDATE_FOR_HUMAN_ACCEPTANCE` |
| Requirement set | `V3-R1-GOV-001…V3-R1-GOV-012` |
| Decision count | `10 REFINE / 2 DEFER` |
| Human Acceptance | `NOT_RECORDED` |
| Repository effect | `NONE` |
| Production authorization | `NONE` |

## 1. Purpose and authority boundary

This candidate consolidates the twelve Governance decisions made for YSim V3 Release 1 into a testable requirements baseline. It defines what Release 1 must govern, what remains reference-only, and how later artifacts must prove conformance.

The YSim v2.0 documents cited below are historical inputs. Their `FROZEN` status does not transfer approval, maturity, scope, or acceptance into YSim V3 Release 1. This candidate becomes an accepted V3 R1 baseline only after an explicit Human Acceptance decision bound to this exact artifact version and its published SHA-256.

Acceptance of this candidate:

- accepts the requirement wording, scope, exclusions, ownership roles, and acceptance criteria in this document;
- does not assert that any registry, capability, experience, implementation, test, or production environment already conforms;
- does not authorize a commit, push, pull request, merge, tag, release, deployment, provider action, payment, email, scheduler, or other external effect;
- does not make `V3-R1-GOV-011` or `V3-R1-GOV-012` deliverables of Release 1.

## 2. Normative vocabulary

The keywords **MUST**, **MUST NOT**, **SHOULD**, and **MAY** are normative.

| Term | Meaning in this baseline |
| --- | --- |
| `IN_SCOPE_R1` | Approved for Release 1 and subject to the mandatory controls in this baseline. |
| `REFERENCE_ONLY` | Retained for context or compatibility; not a Release 1 implementation commitment. |
| `FUTURE` | Explicitly deferred beyond Release 1. |
| `NOT_APPLICABLE` | A model element or relationship is not needed for a specific case, with a recorded rationale. |
| `DEFINED` | Identity and business meaning are approved; implementation is not implied. |
| `IMPLEMENTED` | Implementation evidence exists and is traceable to the requirement. |
| `OPERATIONAL` | Approved environment evidence demonstrates operation; registry presence alone is insufficient. |
| Owner | Role accountable for the governed item and approval of its business meaning. |
| Steward | Role responsible for registry quality, validation, traceability, and controlled change. |

No maturity state may be inferred solely from a registry entry, a design document, source code, or an earlier release.

## 3. Governance ownership model

| Area | Accountable owner role | Steward/reviewer role |
| --- | --- | --- |
| Business Object Registry | Business Architecture Owner | Business Object Steward |
| Capability Registry | Product Governance Owner | Capability Steward |
| Business Meta Model | Enterprise Architecture Owner | Business Architecture Steward |
| Commerce Experience model | Commerce Product Owner | Commerce Architecture Steward |
| Blueprint and Store Template data boundary | Security & Privacy Owner | Commerce Architecture Steward |
| Deferred Business Factory rationale | Product Governance Owner | Enterprise Architecture Owner |
| Human Acceptance for this checkpoint | Authorized YSim V3 R1 human approver | Independent reviewer or designated governance reviewer |

These roles are baseline accountabilities. The controlled project artifact that operationalizes this baseline MUST bind each role to an identified person or approved group before an affected requirement advances to `IMPLEMENTED` or `OPERATIONAL`.

## 4. Decision Matrix

| ID | Decision | Baseline result | Owner role | R1 disposition |
| --- | --- | --- | --- | --- |
| `V3-R1-GOV-001` | `REFINE` | Controlled Business Object Registry for approved R1 objects | Business Architecture Owner | Mandatory |
| `V3-R1-GOV-002` | `REFINE` | Registry is the canonical source for object identity and business meaning | Business Architecture Owner | Mandatory |
| `V3-R1-GOV-003` | `REFINE` | Coverage follows approved R1 objects and domains, not the historical full-platform list | Business Architecture Owner | Mandatory |
| `V3-R1-GOV-004` | `REFINE` | Controlled Capability Registry for approved R1 capabilities | Product Governance Owner | Mandatory |
| `V3-R1-GOV-005` | `REFINE` | Registry is the canonical cross-artifact source for R1 capability identity, scope, and evidenced maturity | Product Governance Owner | Mandatory |
| `V3-R1-GOV-006` | `REFINE` | Coverage follows domains with approved R1 capabilities | Product Governance Owner | Mandatory |
| `V3-R1-GOV-007` | `REFINE` | Version-controlled conceptual Business Meta Model for R1 | Enterprise Architecture Owner | Mandatory |
| `V3-R1-GOV-008` | `REFINE` | Typed one-to-many and many-to-many traceability relationships | Enterprise Architecture Owner | Mandatory |
| `V3-R1-GOV-009` | `REFINE` | Controlled model for approved R1 Commerce Experiences; no Store Factory | Commerce Product Owner | Mandatory where an R1 experience exists |
| `V3-R1-GOV-010` | `REFINE` | Blueprint and Store Template are reusable assets without organization-specific or operational data | Security & Privacy Owner | Mandatory where those assets exist |
| `V3-R1-GOV-011` | `DEFER` | Business Factory is `REFERENCE_ONLY/FUTURE` and not an R1 deliverable | Product Governance Owner | Excluded from implementation |
| `V3-R1-GOV-012` | `DEFER` | AI/developer Store creation benefit is rationale for a later release | Product Governance Owner | Excluded from implementation |

## 5. Normative requirements

### V3-R1-GOV-001 — R1 Business Object Registry

**Decision:** `REFINE`

Release 1 MUST maintain a controlled, versioned Business Object Registry for every Business Object approved as `IN_SCOPE_R1`. Each entry MUST include a stable identifier, canonical singular business name, business definition, one primary type, one owning domain, accountable owner, steward, scope status, maturity status, lifecycle or immutability treatment, and traceability to the approving requirement and supporting evidence. A Business Object MUST represent a business concept and MUST NOT be created solely as a database, API, DTO, source-code, or UI construct.

**Acceptance criteria**

1. Every `IN_SCOPE_R1` Business Object has all mandatory fields and exactly one primary type and owning domain.
2. Object identifiers are unique and stable; reusing or silently changing an identifier fails validation.
3. Canonical names are unique for a business meaning; known aliases are explicitly mapped and cannot act as competing canonical names.
4. Snapshot objects are marked immutable and cannot be represented as updateable lifecycle records.
5. Each entry traces to an approved R1 requirement; `IMPLEMENTED` and `OPERATIONAL` additionally trace to test and environment evidence.
6. Database tables, entities, DTOs, API payloads, and UI models do not become Business Objects merely by existing.

**Exclusions:** This requirement does not approve all objects listed in the historical registry and does not prescribe database or API schemas.

### V3-R1-GOV-002 — Canonical object identity and business meaning

**Decision:** `REFINE`

The R1 Business Object Registry MUST be the canonical cross-artifact source for Business Object identifier, canonical name, definition, owning domain, primary type, and approved scope. Every R1 requirement, domain model, data model, API, event, permission, configuration, UI, integration, and test that refers to a governed Business Object MUST use or map to the canonical registry identity. Technical artifacts MAY use implementation-specific names only when an explicit, versioned mapping preserves the business identity.

**Acceptance criteria**

1. Automated validation detects references to an unknown, retired, or out-of-scope object.
2. Competing canonical definitions or uncontrolled synonyms fail validation.
3. Technical aliases have an explicit mapping to exactly one governed object.
4. A change to identifier, canonical meaning, owner, domain, or primary type requires a versioned decision and impact record.
5. Runtime schemas remain authoritative for technical structure; the registry remains authoritative for business identity and meaning.
6. Registry status never substitutes for implementation, test, deployment, or operational evidence.

**Exclusions:** The registry is not a database schema, API schema, event payload schema, or runtime configuration store.

### V3-R1-GOV-003 — R1 object coverage by approved scope

**Decision:** `REFINE`

The R1 Business Object Registry MUST cover every Business Object owned or referenced by an approved R1 requirement or process. Coverage is derived from approved R1 scope, not from the historical list of platform domains. Cross-domain objects MUST identify one owning domain or steward and all consuming domains. Every retained historical object MUST be classified as `IN_SCOPE_R1`, `REFERENCE_ONLY`, or `FUTURE`.

**Acceptance criteria**

1. Every object referenced by an approved R1 artifact exists in the registry.
2. Every registered `IN_SCOPE_R1` object has an owner, owning domain, and primary type.
3. Cross-domain use records one governing owner/steward and the consuming domains.
4. Unreferenced historical objects are not counted as R1 scope or implementation.
5. `REFERENCE_ONLY` and `FUTURE` objects cannot satisfy R1 coverage or maturity gates.
6. A domain is included in mandatory R1 coverage only when it owns or consumes an approved R1 object.

**Exclusions:** Release 1 is not required to implement every historical domain, object, snapshot, policy object, or future-evolution item.

### V3-R1-GOV-004 — R1 Capability Registry

**Decision:** `REFINE`

Release 1 MUST maintain a controlled, versioned Capability Registry for every capability approved as `IN_SCOPE_R1`. Each entry MUST include a stable identifier, canonical name, business or platform outcome, one primary type, owning domain, accountable owner, steward, scope status, maturity status, availability context, dependencies, and traceability to requirements and evidence. Capability descriptions MUST state what the platform can achieve and MUST NOT merely restate a service, endpoint, database, UI component, or implementation technique.

**Acceptance criteria**

1. Every `IN_SCOPE_R1` capability has all mandatory fields, exactly one primary type, and one owning domain or designated steward.
2. Identifiers are unique and stable; duplicate meanings or uncontrolled canonical names fail validation.
3. Business/platform outcomes are distinguishable from implementation mechanisms.
4. Dependencies and cross-domain consumers are recorded where applicable.
5. Maturity is one of the controlled states and is supported by the evidence required for that state.
6. Registry presence alone cannot yield `IMPLEMENTED` or `OPERATIONAL`.

**Exclusions:** Licensing, marketplace capability, white-label expansion, and future roadmap items are not automatically in R1 scope.

### V3-R1-GOV-005 — Canonical capability references and evidenced maturity

**Decision:** `REFINE`

Every R1 requirement, process, API, permission model, configuration, feature flag, architecture artifact, and test that refers to a Business or Platform Capability MUST use or map to the canonical identifier and name from the Capability Registry. Adding a capability or changing its identity, outcome, scope, owner, type, dependency, or maturity MUST be versioned and traceable to an approved decision and evidence. Permission and feature-flag artifacts MAY reference a capability, but their runtime behavior remains governed by their specialized technical contracts.

**Acceptance criteria**

1. Unknown or out-of-scope capability references fail validation.
2. Duplicate identifiers, competing canonical names, and duplicate meanings fail validation.
3. Identity, outcome, scope, ownership, type, dependency, and maturity changes have a version and impact record.
4. `DEFINED` requires an approved definition; `IMPLEMENTED` requires requirement and test evidence; `OPERATIONAL` requires approved environment evidence.
5. Permission and feature-flag references resolve to a governed capability without making the registry a runtime policy engine.
6. Licensing, marketplace, and non-R1 capabilities do not become R1 commitments by appearing in a historical registry.

**Exclusions:** The Capability Registry does not replace permission, feature-flag, configuration, API, deployment, or operational artifacts.

### V3-R1-GOV-006 — R1 capability coverage by approved domain scope

**Decision:** `REFINE`

The R1 Capability Registry MUST cover every capability owned or referenced by an approved R1 requirement, business process, permission model, configuration, or feature flag. Domain coverage is determined by approved R1 capabilities, including required supporting Security, Integration, and Operations capabilities. A shared or cross-domain capability MUST have one primary steward and identify consuming domains. Every retained historical capability MUST be classified as `IN_SCOPE_R1`, `REFERENCE_ONLY`, or `FUTURE`.

**Acceptance criteria**

1. Every approved R1 capability reference resolves to a registry entry.
2. Every `IN_SCOPE_R1` capability has an owner, owning domain or steward, and primary type.
3. Shared and cross-domain capabilities have one primary steward and recorded consumers.
4. `REFERENCE_ONLY` and `FUTURE` capabilities cannot satisfy implementation or operational gates.
5. A domain is counted in R1 coverage only when it owns or consumes an approved R1 capability.
6. Supporting Security, Integration, and Operations capabilities required by R1 flows are not omitted because they are non-customer-facing.

**Exclusions:** The historical full-platform domain and future-capability lists do not define R1 implementation scope.

### V3-R1-GOV-007 — Controlled conceptual Business Meta Model

**Decision:** `REFINE`

Release 1 MUST maintain a controlled, versioned conceptual Business Meta Model that defines the governed R1 component types and valid relationship types among them. At minimum it MUST address Business Requirement, Capability, Business Object, Business Policy, Business Rule, Business Event, Business Snapshot, and the Commerce components retained by `V3-R1-GOV-009`. Each component type and relationship type MUST have a definition, owner or steward, reference rule, and applicability rule.

**Acceptance criteria**

1. Every component type used by an R1 artifact is defined by the meta-model or explicitly governed by a linked specialized model.
2. Each relationship type specifies source, target, semantics, and cardinality.
3. Unknown component or relationship types fail validation.
4. Each component reference resolves to its governed registry or approved source.
5. Meta-model changes are versioned, owned, reviewed, and traceable to a decision.
6. Component presence never implies `IMPLEMENTED` or `OPERATIONAL`.

**Exclusions:** The meta-model is not a database schema, API schema, runtime workflow engine, or service implementation, and it does not require modeling the entire future platform.

### V3-R1-GOV-008 — Typed, non-linear business traceability

**Decision:** `REFINE`

The R1 Business Meta Model MUST represent Business Requirement, Capability, Business Object, Business Policy, Business Rule, Business Event, and Business Snapshot relationships as typed traceability edges supporting one-to-many and many-to-many cardinalities. Each edge MUST identify its source, target, type, meaning, and cardinality. The historical seven-element sequence is explanatory only and MUST NOT be treated as a mandatory runtime or documentation pipeline.

**Acceptance criteria**

1. An edge with a missing source or target fails validation.
2. A relationship type not permitted by the meta-model fails validation.
3. One-to-many and many-to-many relationships are representable without duplicating governed components.
4. Every approved business requirement traces to at least one relevant capability.
5. Object, policy, rule, event, or snapshot relationships are mandatory only when applicable; `NOT_APPLICABLE` requires a recorded rationale.
6. Design-time traceability cannot be used as evidence of runtime execution order.

**Exclusions:** Not every requirement must have all seven component types, and synthetic records MUST NOT be created merely to complete the historical chain.

### V3-R1-GOV-009 — Minimum R1 Commerce Experience model

**Decision:** `REFINE`

Release 1 MUST maintain a controlled, versioned definition for each approved R1 Commerce Experience. Each experience MUST identify a stable ID, canonical name, owner, audience, applicable Business Model, configuration or Blueprint, Store/Organization context where applicable, Publishing Target, lifecycle state, dependencies, and traceability to requirement and evidence. Only Commerce Meta Model layers actually used by an R1 experience are mandatory; an unused layer MUST be marked `NOT_APPLICABLE` with rationale.

**Acceptance criteria**

1. Every R1 Commerce Experience has identity, owner, audience, lifecycle, and Publishing Target.
2. The experience traces to an approved R1 requirement and its applicable configuration or Blueprint.
3. A Store Instance, when used, binds to the correct Organization and exact Blueprint/Template version.
4. `PUBLISHABLE` or `OPERATIONAL` status requires test and approved environment evidence.
5. `NOT_APPLICABLE` layers include a rationale and do not create synthetic artifacts.
6. Declaring a Publishing Target does not grant deployment or production-activation authority.

**Exclusions:** Runtime Business Factory, mass Store generation, AI Store generation, white-label marketplace, and automatic publishing pipelines are outside this requirement.

### V3-R1-GOV-010 — Reusable Blueprint and Store Template data boundary

**Decision:** `REFINE`

An R1 Business Blueprint or Store Template MUST be an identified, versioned, reusable asset. It MAY contain shared structure, rules, safe defaults, and references to approved configuration, but MUST NOT contain organization-specific operational data, personal data, customer records, orders, payments, fulfillment records, production credentials, secrets, tokens, certificates, passwords, or runtime state. Organization-specific data and configuration MUST be kept in the applicable Store Instance or specialized controlled store.

**Acceptance criteria**

1. Each Blueprint and Store Template has an ID, version, owner, scope, and change history.
2. Automated validation scans the asset and referenced packaged content for prohibited operational, personal, transactional, credential, and secret material.
3. Applying an asset to another Organization does not copy data from an existing Organization.
4. Organization-specific values are externalized to the appropriate Store Instance or specialized configuration store.
5. Sample data is synthetic, clearly labeled, and cannot be selected as production data.
6. Publishing Target definitions do not contain deployment credentials or secrets.

**Exclusions:** Safe shared defaults are allowed; this requirement does not require a Store Factory and does not make Blueprint or Template a runtime state store.

### V3-R1-GOV-011 — Business Factory deferred beyond R1

**Decision:** `DEFER`

Business Factory Pattern MUST be classified as `REFERENCE_ONLY/FUTURE` for Release 1 and MUST NOT be claimed as an R1 deliverable, implemented capability, or operational capability. Release 1 MAY manually create and govern the Commerce Experiences, Blueprints, Store Templates, and Store Instances allowed by `V3-R1-GOV-009` and `V3-R1-GOV-010`; manual reuse is not evidence of a Business Factory.

**Acceptance criteria**

1. No R1 scope, implementation plan, maturity report, or acceptance report claims a runtime Factory or Store generator as delivered.
2. No R1 acceptance gate requires Factory UI, Store-generation API, mass provisioning, or automated publishing.
3. Manual use of a Blueprint or Store Template is not counted as Factory implementation evidence.
4. Any later proposal requires a new requirement, owner, security and tenant-isolation boundary, test plan, evidence, and Human Acceptance.
5. R1 Commerce Experience governance remains valid without a Business Factory.
6. The deferred status cannot be advanced by this baseline's acceptance.

**Exclusions:** All Business Factory implementation and operational claims are outside Release 1.

### V3-R1-GOV-012 — AI/developer Store-creation rationale deferred

**Decision:** `DEFER`

The expected benefit of helping AI or development teams create Stores from standardized Blueprints MUST be retained only as rationale for a future Business Factory requirement. Release 1 MUST NOT implement or accept an AI Store generator, specialized Store-creation assistant, or automated Store-generation pipeline under this requirement.

**Acceptance criteria**

1. The statement is labeled `REFERENCE_ONLY/FUTURE`, not `IN_SCOPE_R1`.
2. No R1 gate measures Store-generation speed, AI automation, or Factory throughput.
3. Manual Blueprint/Template reuse is not accepted as evidence for this deferred capability.
4. No AI agent receives implicit permission to provision, publish, or activate a Store.
5. A later release must define users, inputs, outputs, permissions, tenant isolation, failure handling, tests, evidence, and Human Acceptance.
6. Deferral does not weaken the data-separation controls in `V3-R1-GOV-010`.

**Exclusions:** This requirement contains no R1 product or implementation deliverable.

## 6. Cross-requirement validation gates

The accepted baseline MUST later be supported by deterministic validation at the controlled execution point. At minimum, the validation design MUST cover:

| Gate | Required result |
| --- | --- |
| `GOV-GATE-01-COMPLETENESS` | All mandatory fields exist for every `IN_SCOPE_R1` object, capability, relationship, and experience. |
| `GOV-GATE-02-IDENTITY` | IDs are unique and stable; canonical names and meanings are not duplicated. |
| `GOV-GATE-03-REFERENCE-INTEGRITY` | All cross-artifact references resolve to existing, scope-valid governed items. |
| `GOV-GATE-04-SCOPE` | `IN_SCOPE_R1`, `REFERENCE_ONLY`, `FUTURE`, and `NOT_APPLICABLE` are distinguished and enforced. |
| `GOV-GATE-05-MATURITY-EVIDENCE` | `IMPLEMENTED` and `OPERATIONAL` states are rejected without the required evidence. |
| `GOV-GATE-06-OWNERSHIP` | Each governed item and controlled change has an accountable owner/steward. |
| `GOV-GATE-07-CHANGE-CONTROL` | Identity, meaning, scope, ownership, type, relationship, and maturity changes are versioned and impact-assessed. |
| `GOV-GATE-08-DATA-BOUNDARY` | Blueprint/Template packages contain no prohibited organization, personal, transaction, credential, secret, or runtime data. |
| `GOV-GATE-09-DEFERRED-BOUNDARY` | Business Factory and AI Store generation cannot be reported as R1 deliverables or maturity evidence. |
| `GOV-GATE-10-AUTHORIZATION` | Registry or Publishing Target presence cannot authorize merge, deploy, production activation, provider action, or other external effect. |

The test implementation, execution environment, and evidence artifacts for these gates are subsequent deliverables. Acceptance of this requirements baseline accepts the required outcomes, not an unimplemented test suite.

## 7. Traceability to historical source inputs

All source inputs were read at immutable repository commit `3afc37eb366769603f7a898c53432c444f50726a` in `nvkhoabk/ysim`.

| Requirements | Source path and immutable blob | Source sections | Refinement applied |
| --- | --- | --- | --- |
| `GOV-001…003` | `docs/BRD/BRD-BO-INDEX.md`; blob `864f11dda3748417cda6a5a4c44509d5f888b4e8` | Purpose, Objectives, Scope, Classification, Identifier, Registry Principles | Limited to approved R1 objects/domains; separated business identity from technical schemas; maturity requires evidence. |
| `GOV-004…006` | `docs/BRD/BRD-CAP-INDEX.md`; blob `f0f60cb5a24a0971ccdacade911ca6a163641a0f` | Purpose, Objectives, Scope, Classification, Lifecycle, Identifier, Registry Principles | Limited to approved R1 capabilities/domains; runtime permission/config/flag contracts remain specialized; maturity requires evidence. |
| `GOV-007…008` | `docs/BRD/BRD-META-MODEL.md`; blob `574b716098b0269afa59c37e447ad11e8f9132ea` | Purpose, Business Meta Model, Component Responsibilities, Traceability | Replaced the historical linear chain with a typed conceptual graph; no mandatory runtime sequence. |
| `GOV-009…010` | same meta-model blob | Commerce Meta Model, Commerce Meta Components | Retained minimum R1 experience governance and reusable-asset data boundary; no Store Factory. |
| `GOV-011…012` | same meta-model blob | Business Factory | Deferred Factory implementation and AI/developer benefit rationale beyond R1. |

## 8. Completeness and consistency audit

### 8.1 Findings

No unresolved internal contradiction was found in the candidate requirement set.

### 8.2 Audit results

| Check | Result | Evidence in candidate |
| --- | --- | --- |
| All twelve decisions represented | `PASS` | Decision Matrix and twelve normative sections |
| Decision fidelity | `PASS` | `GOV-001…010 = REFINE`; `GOV-011…012 = DEFER` |
| Business Object requirements separated by concern | `PASS` | Registry content (`001`), canonical use (`002`), coverage (`003`) |
| Capability requirements separated by concern | `PASS` | Registry content (`004`), canonical use/maturity (`005`), coverage (`006`) |
| Meta-model requirements non-linear and conceptual | `PASS` | Typed model (`007`) and typed graph rules (`008`) |
| Commerce scope consistent with Factory deferral | `PASS` | Minimum experience model (`009`), data boundary (`010`), deferrals (`011…012`) |
| Historical V2 status not inherited | `PASS` | Authority boundary and source traceability |
| Scope classifications explicit | `PASS` | Normative vocabulary and scope criteria |
| Maturity claims evidence-bound | `PASS` | Vocabulary, `GOV-004…005`, and `GOV-GATE-05` |
| Owner/steward accountability present | `PASS` | Ownership model and requirement owner roles |
| Acceptance criteria individually testable | `PASS` | Six criteria for every requirement plus ten cross-requirement gates |
| Human Acceptance not pre-claimed | `PASS` | Status is `CANDIDATE_FOR_HUMAN_ACCEPTANCE`; Human Acceptance is `NOT_RECORDED` |
| External effects remain unauthorized | `PASS` | Authority boundary and `GOV-GATE-10` |

### 8.3 Resolved source conflicts

1. Historical documents describe the entire platform; this baseline limits mandatory coverage to approved R1 objects, capabilities, domains, and experiences.
2. Historical registries call themselves platform-wide sources of truth; this baseline limits authority to business identity and meaning and preserves specialized runtime contracts.
3. The historical meta-model shows linear chains; this baseline uses typed, non-linear traceability and does not infer runtime order.
4. The historical Commerce Meta Model proposes Business Factory; this baseline retains minimum R1 experience governance and explicitly defers Factory and AI Store-generation capability.

## 9. Human Acceptance decision protocol

The authorized human approver MUST choose exactly one outcome for the exact candidate version and SHA-256 published with it:

- `ACCEPT`: the twelve requirements, their scope, exclusions, ownership roles, acceptance criteria, validation outcomes, and deferrals are accepted as the `V3-R1-G00-S02` Governance Requirements Baseline.
- `CHANGES_REQUESTED`: the candidate remains unaccepted; the response MUST identify the requirement IDs or sections to revise.

An `ACCEPT` decision does not authorize repository or production effects. A later repository checkpoint MUST separately bind any committed baseline to its exact commit and artifact identity.

## 10. Candidate state

```yaml
checkpoint: V3-R1-G00-S02
document_id: V3-R1-G00-S02-GOVERNANCE-REQUIREMENTS-BASELINE
version: 0.1.0-candidate.1
status: CANDIDATE_FOR_HUMAN_ACCEPTANCE
requirements_total: 12
refine_total: 10
defer_total: 2
human_acceptance: NOT_RECORDED
repository_mutation: NONE
external_effects_authorized: false
production_authorized: false
```
