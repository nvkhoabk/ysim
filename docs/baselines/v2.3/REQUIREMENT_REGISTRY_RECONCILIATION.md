# BRD/UXF Requirement Registry Reconciliation — Phase 1C

Phase 1C applies the semantic membership rules to the complete Phase 1B finding set. BRD/UXF source content is unchanged, canonical IDs are not newly assigned, and retired temporary keys are never reused.

## Exact reconciliation result

- Baseline active requirements: **1309**
- Reconciled active requirements: **1185**
- False positives excluded: **137**
- False-positive candidates confirmed as requirements: **3**
- False negatives added: **3**
- False-negative candidates excluded: **7**
- Compound candidates split: **10** into **30** atomic requirements
- Composite parents retained: **2**
- Alias records retained: **9**
- Atomic implementation/acceptance requirements: **1174**
- Canonical IDs tombstoned/deprecated: **0**
- Temporary keys retired: **157**
- Unresolved human decisions: **0**
- Ready to freeze: **yes**

## Acceptance semantics

- Documented acceptance (`DIRECT + LINKED`): **0**
- Acceptance gap (`INFERRED_ONLY + MISSING`): **1174**
- Acceptance-unit distribution: `{"INFERRED_ONLY": 1174}`

## Scope-conflict treatment

The eight SD-03/UXD-11 promotions are active with `FRAMEWORK_DECISION` provenance, retain their legacy `source_scope_status`, and have `scope_conflict_resolved=true`. The resolved legacy conflict is no longer recorded as ambiguity.

## Composite parent decisions

- `BO-P06` remains the verbatim canonical composite parent; `ALL_CHILDREN` coverage maps to `TMP-BRD-BO-INDEX-048`, `TMP-BRD-BO-INDEX-049`.
- `BD-15-002` remains the verbatim canonical composite parent; `ALL_CHILDREN` coverage maps to `TMP-BRD-WS-15-026`, `EP-15-001`.

## Canonical and alias decisions

- `EP-06-004` remains a source-backed ID alias of canonical `BD-06-007`; it is not an implementation, acceptance, or scope-coverage unit.
- `EP-16-009` remains a source-backed ID alias of canonical `BD-16-026`; it is not an implementation, acceptance, or scope-coverage unit.
- `EP-16-008` remains a source-backed ID alias of canonical `BD-16-027`; it is not an implementation, acceptance, or scope-coverage unit.
- `EP-17-005` remains a source-backed ID alias of canonical `BD-17-011`; it is not an implementation, acceptance, or scope-coverage unit.
- `EP-17-009` remains a source-backed ID alias of canonical `BD-17-026`; it is not an implementation, acceptance, or scope-coverage unit.
- `CAP-EP-006` remains a source-backed ID alias of canonical `CAP-P07`; it is not an implementation, acceptance, or scope-coverage unit.
- `EP-06-005` remains a source-backed ID alias of canonical `BD-06-011`; it is not an implementation, acceptance, or scope-coverage unit.
- `SNP-EP-007` remains a source-backed ID alias of canonical `SNP-P07`; it is not an implementation, acceptance, or scope-coverage unit.

## Canonical and retired-temporary decisions

- `TMP-BRD-WS-07-002` is retired as `SUPERSEDED_BY` `BD-07-003`; its source evidence is retained as a supporting source of `BD-07-003`.
- `TMP-BRD-WS-08-001` is retired as `SUPERSEDED_BY` `BD-08-001`; its source evidence is retained as a supporting source of `BD-08-001`.
- `TMP-BRD-WS-08-009` is retired as `SUPERSEDED_BY` `BD-08-012`; its source evidence is retained as a supporting source of `BD-08-012`.
- `TMP-BRD-WS-09-002` is retired as `SUPERSEDED_BY` `BD-09-002`; its source evidence is retained as a supporting source of `BD-09-002`.
- `TMP-BRD-WS-10-005` is retired as `SUPERSEDED_BY` `BD-10-016`; its source evidence is retained as a supporting source of `BD-10-016`.
- `TMP-BRD-WS-10-006` is retired as `SUPERSEDED_BY` `BD-10-019`; its source evidence is retained as a supporting source of `BD-10-019`.
- `TMP-BRD-WS-12-001` is retired as `SUPERSEDED_BY` `BD-12-005`; its source evidence is retained as a supporting source of `BD-12-005`.
- `TMP-BRD-WS-15-002` is retired as `SUPERSEDED_BY` `EP-15-002`; its source evidence is retained as a supporting source of `EP-15-002`.
- `TMP-UXF-05-013` is retired as `SUPERSEDED_BY` `UXF-505`; its source evidence is retained as a supporting source of `UXF-505`.
- `TMP-BRD-WS-03-001` is retired as `SUPERSEDED_BY` `BD-03-006`; its source evidence is retained as a supporting source of `BD-03-006`.
- `OVL-EXACT-014`: `TMP-BRD-WS-15-001`, `TMP-BRD-WS-15-027` are retired as `SUPERSEDED_BY` `EP-15-001`; the full equivalence class is `EP-15-001`, `TMP-BRD-WS-15-001`, `TMP-BRD-WS-15-027`.

## Transitively resolved overlap groups

None.

## Corrected truncated extractions

- `OVL-EXACT-016` `CORRECTED_TRUNCATED_EXTRACTION` keeps `TMP-BRD-WS-12-003`, `TMP-BRD-WS-12-004` active and replaces shared-fragment evidence with full-context source ranges.

## Corrected channel-scoped restatements

- `OVL-EXACT-021` `CORRECTED_TRUNCATED_CHANNEL_CONTEXT` keeps `TMP-UXF-01-001`, `TMP-UXF-01-002`, `TMP-UXF-01-003` as distinct channel-scoped requirements with the same predicate.

## Deferred documentation findings

- `DOC-OVL-EXACT-004` (DEFERRED_TO_BRD_CORRECTION): Clarify 'Version 2.0' as the v2.3 baseline when the BRD is revised. Do not modify docs/BRD in Phase 1C. Partial Payment and Partial Refund are distinct capabilities. A decision to support Partial Refund does not activate Partial Payment.
- `DOC-OVL-EXACT-006` (DEFERRED_TO_BRD_CORRECTION): Correct 'Version 2.0' to the v2.3 baseline when the BRD is revised. Auto Payout remains out of scope for v2.3 under SD-02. Do not modify docs/BRD in Phase 1C.
- `DOC-OVL-EXACT-008` (DEFERRED_TO_BRD_CORRECTION): BRD v2.3 must replace 'cuối cùng' with explicit fallback semantics. Distinguish external delivery, durable inbox persistence, and user read state. Add retry policy, durable recovery/DLQ behavior, and source-backed acceptance criteria when the BRD is revised.
- `DOC-OVL-EXACT-009` (DEFERRED_TO_BRD_CORRECTION): The current Federation wording is insufficient for implementation and acceptance. Do not select a protocol or design a solution in Phase 1C. Federation actors and use cases.; Trust boundaries and tenant isolation.; Supported protocol/profile.; Claim/attribute mapping.; Account linking and conflict handling.; Provisioning/deprovisioning or related lifecycle behavior.; Authentication assurance, MFA, and risk interaction.; Audit, revocation, and failure behavior.; Acceptance criteria.
- `DOC-OVL-EXACT-010` (DEFERRED_TO_BRD_CORRECTION): The current Business Event wording is insufficient for implementation and acceptance. Do not design an event solution in Phase 1C. Mandatory security event taxonomy.; Trigger and producer ownership.; Event schema, versioning, and classification.; Tenant/Organization context.; Sensitive-data constraints.; Delivery guarantee, retry, and dead-letter handling.; Ordering, deduplication, and idempotency.; Consumer authorization.; Audit, retention, and observability.; Acceptance criteria.
- `DOC-OVL-EXACT-011` (DEFERRED_TO_BRD_CORRECTION): The independence between Operation Retry and Connector Retry must be specified when the BRD is revised. Do not design a retry policy in Phase 1C. Ownership and scope of each retry layer.; Independent counters and state.; Timeout, backoff, jitter, and retry budget.; Idempotency and duplicate prevention.; Conditions that escalate connector failure to operation failure.; Controls for nested retry amplification and retry storms.; Exhaustion, DLQ, and manual recovery.; Correlation, audit, and observability.; Acceptance criteria.
- `DOC-OVL-EXACT-012` (DEFERRED_TO_BRD_CORRECTION): The Operations Platform Business Event requirement must be specified when the BRD is revised. Do not design an event architecture in Phase 1C. Event taxonomy for operation lifecycle, retry, maintenance, runbook, and recovery.; Trigger and producer ownership.; Operation, correlation, and causation identifiers.; Organization, scope, and actor context.; Payload schema, versioning, and data classification.; Delivery guarantee, ordering, and idempotency.; Retry, DLQ, and replay.; Consumer authorization.; Audit, retention, and observability.; Acceptance criteria.
- `DOC-OVL-EXACT-013` (DEFERRED_TO_BRD_CORRECTION): Do not reclassify CAP-P07 or design an event model in Phase 1C. Consider reclassifying CAP-P07 from BUSINESS_REQUIREMENT to DESIGN_PRINCIPLE when the BRD is revised. Clarify event-role metadata, canonical event reference, ownership, and versioning.; Add validation for dangling or invalid event references.; Add acceptance criteria.
- `DOC-OVL-EXACT-015` (DEFERRED_TO_BRD_CORRECTION): The Gateway, Connector, and Adapter constraint must be clarified when the BRD is revised. Do not interpret or design an integration topology in Phase 1C. Scope inbound, outbound, synchronous, asynchronous, batch, and event interactions.; Clarify whether all three layers are always mandatory or depend on interaction type.; Clarify whether internal domain-to-domain communication is subject to the constraint.; Define approved exception and bypass policy.; Define enforcement, observability, and acceptance criteria.
- `DOC-OVL-EXACT-029` (DEFERRED_TO_UXF_CORRECTION): Replace 'never know suppliers' with explicit technical-decoupling semantics when UXF is revised. Do not reclassify UXF-505 or design an allocation solution in Phase 1C. Consider DESIGN_PRINCIPLE instead of UX_REQUIREMENT when UXF is revised. Distinguish supplier operational identity from provider/brand disclosure.; Add source-backed acceptance criteria.
- `DOC-OVL-PROB-001` (DEFERRED_TO_BRD_CORRECTION): The BRD/domain specification must clarify the Identity–User–Customer relationship. Do not create a detailed data model in Phase 1C. Cardinality between Identity, User, and Customer.; Organization ownership and scope.; Link/unlink behavior and lifecycle.; Account provisioning.; Merge and conflict rules.; Authorization and data-isolation implications.; Acceptance criteria.
- `DOC-OVL-PROB-002` (DEFERRED_TO_BRD_CORRECTION): The BRD must explicitly connect Promotion, Funding Owner, Organization ownership, and the associated financial lifecycle. Do not design a financial model in Phase 1C. Promotion.; Funding Owner.; Organization ownership.; Promotion budget reservation, consumption, and release.; Financial attribution.; Acceptance criteria.
- `DOC-OVL-PROB-003` (DEFERRED_TO_BRD_CORRECTION): The v2.3 BRD must replace the old term with Final Promotion Snapshot and specify the complete snapshot lifecycle. Change 'Promotion Snapshot' to 'Final Promotion Snapshot' in the old requirement.; Specify the Evaluation, Reservation, and Final lifecycle.; Link Promotion budget reserve, consume, and release behavior.; Define snapshot immutability, version, input, funding, currency, and timestamp.; Add transition and acceptance criteria.; Remove the interpretation that no snapshot may exist before Payment Success.
- `DOC-OVL-PROB-004` (DEFERRED_TO_BRD_CORRECTION): The Snapshot/Policy specification must define the joint Security Policy and Retention Policy contract. Do not design a policy engine or storage mechanism in Phase 1C. Policy precedence and conflict-resolution contract.; Jurisdiction and data-class mapping.; Legal hold.; Immutable snapshot behavior with deletion/anonymization.; Audit evidence.; Acceptance criteria.
- `DOC-OVL-PROB-006` (DEFERRED_TO_BRD_CORRECTION): Normalize both version labels to v2.3 when docs/BRD is revised. Phase 1C must not generalize this decision into a platform-wide Attachment policy. The Video exclusion applies only to Customer Support Ticket attachments and Notification attachments. If a shared Attachment capability is later established, its shared relationship must be designed in an architecture phase rather than this reconciliation.

## Human semantic clarifications

- `BD-12-005` (`OVL-EXACT-008`) semantic clarification:
  - Khi tất cả delivery channel bên ngoài được áp dụng đều thất bại hoặc không thể hoàn tất, hệ thống phải fallback về Personal Inbox.
  - Personal Inbox là kênh nội bộ, không phụ thuộc nền tảng communication bên ngoài.
  - Personal Inbox delivery thành công khi notification đã được persist bền vững và có thể truy xuất trong inbox của đúng recipient.
  - Delivery success không đồng nghĩa recipient đã đọc notification.
  - Nếu internal persistence tạm thời thất bại, hệ thống phải retry theo policy và đưa vào durable recovery/DLQ khi cần; không được đánh dấu success giả hoặc bỏ mất notification.
  - Acceptance intent:
    1. External channels được áp dụng đều fail hoặc không thể hoàn tất.
    2. Personal Inbox fallback được tạo.
    3. Notification được persist bền vững và có thể truy xuất cho đúng recipient.
    4. Trạng thái phân biệt DELIVERED_TO_INBOX và READ.
    5. Persistence failure không tạo false success, không làm mất notification và được retry/recover qua durable recovery hoặc DLQ khi cần.
  - Acceptance metadata remains `INFERRED_ONLY` until source-backed acceptance criteria are added.
- `CAP-P07` (`OVL-EXACT-013`) semantic clarification:
  - CAP-P07 mô tả khả năng của Capability Model, không bắt buộc mọi capability phải event-driven.
  - Mỗi capability có thể khai báo vai trò PUBLISHER, SUBSCRIBER, BOTH hoặc NONE.
  - Khi khai báo event role, capability phải tham chiếu canonical Business Event definition và versioned event contract tương ứng.
  - Không tự tạo event relationship nếu registry không khai báo.
- `UXF-505` (`OVL-EXACT-029`) semantic clarification:
  - Storefront không được lựa chọn supplier.
  - Storefront không được gửi supplier-selection instruction hoặc tham gia routing.
  - Storefront không gọi trực tiếp supplier connector/API.
  - Procurement, allocation và supplier routing nằm sau application/domain contract tương ứng.
  - Supplier/provider/network brand có thể được hiển thị read-only nếu catalog, product disclosure, legal hoặc market policy yêu cầu.
  - Dữ liệu supplier được hiển thị không được dùng để điều khiển allocation/routing.
  - Internal supplier identifiers, cost, priority, health và connector details không được lộ ra Storefront nếu không có explicit disclosure contract.
  - Acceptance intent:
    1. Storefront request không chứa supplier-selection instruction.
    2. Storefront không gọi supplier connector.
    3. Allocation là capability quyết định supplier.
    4. Provider/brand disclosure, nếu có, chỉ là read-only presentation.
    5. Internal supplier routing, cost, và health metadata không bị lộ.
  - Acceptance metadata remains `INFERRED_ONLY` until source-backed acceptance criteria are added.
- `BD-03-006` (`OVL-PROB-001`) semantic clarification:
  - Identity là canonical authentication identity.
  - User là actor/membership trong Organization context.
  - Customer là commercial/customer relationship concept.
  - User và Customer có thể liên kết nhưng không phải cùng entity.
  - Không dùng chung lifecycle hoặc mặc định đồng nhất record.
  - Global Customer Identity/Profile phải tách khỏi Organization Customer Relationship theo quyết định v2.3.
  - Một Identity có thể liên kết nhiều User records theo Organization.
- `BD-06-011` (`OVL-PROB-002`) semantic clarification:
  - Mỗi Promotion có đúng một Funding Owner.
  - Funding Owner là Organization tạo Promotion theo source hiện tại.
  - V2.3 không hỗ trợ nhiều Funding Owner hoặc co-funded Promotion.
  - Không suy diễn khả năng chuyển Funding Owner.
  - Nếu tương lai hỗ trợ reassignment, phải có lifecycle, approval, effective date, financial reconciliation và audit.
  - Promotion budget reservation/consumption phải hạch toán về Funding Owner này.
- `BD-06-014` (`OVL-PROB-003`) semantic clarification:
  - Source statement lịch sử được bảo toàn.
  - Effective v2.3 meaning: Final Promotion Snapshot is created only after Payment Success.
  - Từ 'chỉ' của EP-06-006 chỉ giới hạn Final Promotion Snapshot.
  - Requirement này không cấm Evaluation Snapshot hoặc Reservation Snapshot trước Payment Success.
- `SNP-P07` (`OVL-PROB-004`) semantic clarification:
  - Mọi Snapshot đồng thời chịu Security Policy và Retention Policy.
  - Security Policy quản lý authorization, classification, encryption, masking và access audit.
  - Retention Policy quản lý retention duration, archival, legal hold và deletion/anonymization.
  - Policy resolution xét data class, jurisdiction, Organization và platform minimum.
  - Khi policy xung đột hoặc thiếu cấu hình bắt buộc, xử lý fail-closed và chuyển governance/approval; không tự chọn policy thắng.
  - Snapshot immutability không loại bỏ nghĩa vụ retention/deletion.
  - Cơ chế tombstone, crypto-erasure hoặc compliant archival phải được đặc tả ở phase tài liệu phù hợp.

## Unresolved human decisions

None.

The complete one-record-per-finding evidence, dispositions, split mappings, retired keys, and tombstones are in `requirements/registry-reconciliation.json`.
