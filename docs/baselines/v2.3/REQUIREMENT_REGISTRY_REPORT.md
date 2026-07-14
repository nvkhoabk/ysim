# Requirement Registry Report — BRD/UXF Phase 1C Reconciled

## Validation totals

| Metric | BRD | UXF | Total |
|---|---:|---:|---:|
| Files | 24 | 7 | 31 |
| Registry entries | 1020 | 165 | 1185 |
| With existing ID | 514 | 62 | 576 |
| Without ID / temporary key | 506 | 103 | 609 |
| Acceptance gap (`INFERRED_ONLY + MISSING`) | 1009 | 165 | 1174 |
| Scope `UNCLEAR` | 0 | 0 | 0 |

- Duplicate existing IDs: **0**
- Duplicate temporary keys: **0**
- Dangling requirement references: **0**
- Requirements with recorded ambiguity: **0**
- Requirements with overlap: **26**
- Unique overlap pairs: **13**
- Unique overlap groups: **13**
- Exact duplicate groups: **9**
- Probable semantic overlap groups: **4**

## Classification distributions

- Scope coverage across canonical atomic units (aliases/composite parents excluded): `{"DEFERRED": 15, "FUTURE": 74, "OUT_OF_SCOPE": 17, "V2.3_ACTIVE": 1068}`
- Lifecycle: `{"DRAFT": 165, "FROZEN": 1020}`
- Requirement type: `{"ACCESSIBILITY_REQUIREMENT": 8, "BUSINESS_DECISION": 177, "BUSINESS_REQUIREMENT": 367, "BUSINESS_RULE": 14, "DATA_REQUIREMENT": 149, "DESIGN_PRINCIPLE": 18, "INTEGRATION_REQUIREMENT": 54, "OPERATIONAL_REQUIREMENT": 77, "PERFORMANCE_REQUIREMENT": 4, "PRIVACY_REQUIREMENT": 9, "SCOPE_CONSTRAINT": 116, "SECURITY_REQUIREMENT": 60, "UX_REQUIREMENT": 132}`
- Acceptance metadata across registry entries (includes composite parents): `{"INFERRED_ONLY": 1185}`
- Scope basis: `{"BASELINE_INHERITANCE": 1054, "FRAMEWORK_DECISION": 8, "SOURCE_EXPLICIT": 123}`

## Ambiguities

None.

## Exact normalized duplicates/overlaps

- `CAP-P07` overlaps exact normalized statement with `CAP-EP-006`.
- `CAP-EP-006` overlaps exact normalized statement with `CAP-P07`.
- `SNP-P07` overlaps exact normalized statement with `SNP-EP-007`.
- `SNP-EP-007` overlaps exact normalized statement with `SNP-P07`.
- `TMP-BRD-WS-05-027` overlaps exact normalized statement with `BD-05-005`.
- `BD-05-005` overlaps exact normalized statement with `TMP-BRD-WS-05-027`.
- `BD-06-007` overlaps exact normalized statement with `EP-06-004`.
- `BD-06-011` overlaps exact normalized statement with `EP-06-005`.
- `BD-06-014` overlaps exact normalized statement with `EP-06-006`.
- `EP-06-004` overlaps exact normalized statement with `BD-06-007`.
- `EP-06-005` overlaps exact normalized statement with `BD-06-011`.
- `EP-06-006` overlaps exact normalized statement with `BD-06-014`.
- `TMP-BRD-WS-14-034` overlaps exact normalized statement with `TMP-BRD-WS-14-038`.
- `TMP-BRD-WS-14-038` overlaps exact normalized statement with `TMP-BRD-WS-14-034`.
- `BD-16-026` overlaps exact normalized statement with `EP-16-009`.
- `BD-16-027` overlaps exact normalized statement with `EP-16-008`.
- `EP-16-008` overlaps exact normalized statement with `BD-16-027`.
- `EP-16-009` overlaps exact normalized statement with `BD-16-026`.
- `BD-17-011` overlaps exact normalized statement with `EP-17-005`.
- `BD-17-026` overlaps exact normalized statement with `EP-17-009`.
- `EP-17-005` overlaps exact normalized statement with `BD-17-011`.
- `EP-17-009` overlaps exact normalized statement with `BD-17-026`.
- `UXF-005` overlaps exact normalized statement with `UXF-506`.
- `UXF-308` overlaps exact normalized statement with `UXF-509`.
- `UXF-506` overlaps exact normalized statement with `UXF-005`.
- `UXF-509` overlaps exact normalized statement with `UXF-308`.

## Reconciliation

- Baseline: **1309**
- Registry entries after reconciliation: **1185**
- Canonical atomic requirements: **1174**
- Composite parents: **2**
- Aliases: **9**
- Retired temporary keys: **157**
- Documented acceptance: **0**
- Acceptance gap: **1174**
- Ready to freeze: **yes**

## Registry interpretation

- `FROZEN` is retained as the source requirement lifecycle from the prior baseline; it is not represented as v2.3 approval.
- `DRAFT` is retained for UXF source requirements.
- `V2.3_ACTIVE` is the default for inherited requirements unless the source has an explicit future/deferred/out-of-scope signal or classification is uncertain.
- `acceptance_present` is true only for `DIRECT` or `LINKED`; testability alone remains `INFERRED_ONLY` and is counted in the acceptance gap.

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

## Semantic equivalence classes

- `OVL-EXACT-014` canonical `EP-15-001`; retired `TMP-BRD-WS-15-001`, `TMP-BRD-WS-15-027`; composite coverage {"BD-15-002": {"TMP-BRD-WS-15-027": "EP-15-001"}}.

## Transitively resolved overlap groups

None.

## Corrected truncated extractions

- `OVL-EXACT-016` `CORRECTED_TRUNCATED_EXTRACTION`: `TMP-BRD-WS-12-003`, `TMP-BRD-WS-12-004` remain active with full-context source excerpts; the shared trailing fragment is not treated as an exact semantic match.

## Channel-scoped restatements

- `OVL-EXACT-021` `CORRECTED_TRUNCATED_CHANNEL_CONTEXT`: `TMP-UXF-01-001`, `TMP-UXF-01-002`, `TMP-UXF-01-003` remain distinct because applicability scope is part of duplicate identity.
