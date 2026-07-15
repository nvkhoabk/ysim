---
document_code: "BRD-WS-09"
title: "Inventory, Allocation & Fulfillment Lifecycle"
product_baseline: "2.3"
document_revision: "2.3.0-draft.1"
lifecycle_status: "V2.3_DRAFT"
language: "vi-VN"
source_baseline: "v2.2"
generated_registry_role: "BRD_CANONICAL_SOURCE"
last_remediated_on: "2026-07-15"
---
## Thẩm quyền nguồn yêu cầu v2.3

Các khối `YSIM:REQUIREMENT` trong phụ lục chuẩn tắc là nguồn yêu cầu có thẩm quyền cho baseline 2.3. Nội dung legacy bên dưới được giữ làm ngữ cảnh; nếu có khác biệt, khối chuẩn tắc và các quyết định v2.3 đã phê duyệt được ưu tiên.

# BRD Workshop 09

# Inventory, Allocation & Fulfillment Lifecycle

---

# 1. Workshop Objective

Workshop này xác định toàn bộ Inventory Domain và Fulfillment Domain của YSim.

Bao gồm:

- Inventory
- Inventory Item
- Allocation
- Fulfillment
- Delivery
- Customer Assignment
- QR Security
- Customer Portal Access
- Fulfillment Notification

Workshop kết thúc khi Fulfillment hoàn thành.

Việc kích hoạt eSIM trên mạng di động (Activation) không thuộc phạm vi Workshop này.

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| Inventory | Master |
| InventoryType | Master |
| InventoryItem | Transaction |
| InventoryReservation | Transaction |
| AllocationRequest | Transaction |
| AllocationPolicy | Master |
| AllocationResult | Transaction |
| FulfillmentSession | Transaction |
| FulfillmentTask | Transaction |
| FulfillmentPackage | Transaction |
| DeliveryChannel | Master |
| DeliveryNotification | Transaction |
| FulfillmentSnapshot | Transaction |
| CustomerAssignment | Transaction |
| CustomerPortalAccess | Transaction |

---

# 3. Inventory Architecture

Inventory là Business Object quản lý kho.

Inventory **không phải** là trạng thái của Product Item.

Một Inventory có thể có nhiều loại.

Ví dụ:

- Ready Inventory
- Revoked Inventory
- Error Inventory
- Quarantine Inventory
- Imported Inventory

Kiến trúc Inventory được thiết kế mở để hỗ trợ nhiều mô hình nhập hàng trong các phiên bản tiếp theo.

---

# 4. Product Item Lifecycle

Inventory quản lý Product Item.

Product Item có vòng đời riêng.

```text
Ready

↓

Reserved

↓

Allocated

↓

Delivered

↓

Viewed

↓

Activated (Reference)

↓

Expired
```

Ngoài ra:

```text
Revoked
```

được sử dụng khi:

- Return
- Activation Failure
- Manual Recovery

Inventory và Product Item Lifecycle là hai khái niệm độc lập.

---

# 5. Inventory Ownership

Inventory luôn thuộc YSim.

Tuy nhiên Inventory View được phân quyền.

Organization chỉ nhìn thấy các Inventory Item mà Organization đang xử lý.

Ví dụ:

- Reserved
- Allocated
- Revoked
- Error

không hiển thị cho Organization khác.

---

# 6. Inventory Source

Inventory Item có thể phát sinh từ:

- Bulk Procurement
- Purchase Order
- Manual Import
- Auto Procurement

Ngay cả Auto Procurement trước Fulfillment cũng phải ghi nhận Product Item vào Inventory trước khi Allocation.

Điều này phục vụ:

- Audit
- Settlement
- Customer Support
- Traceability

---

# 7. Allocation Engine

Allocation được thực hiện theo từng Product.

Nếu SalesOrder có nhiều Product khác nhau:

Allocation được thực hiện độc lập cho từng Product.

Allocation Engine luôn ưu tiên:

1. Inventory có Cost thấp nhất.
2. Supplier Priority.
3. Supplier Cost.
4. Supplier Health.
5. Supplier Response Time.

Allocation chỉ áp dụng giữa các Supplier Mapping của cùng một Product.

---

# 8. Allocation Timing

Allocation được thực hiện Realtime.

Trigger:

```text
Payment Success

↓

Inventory Check

↓

Allocation
```

---

# 9. Fulfillment Session

FulfillmentSession là Transaction Object.

FulfillmentSession quản lý:

- SalesOrder
- Allocation
- Product Item
- Delivery
- Customer Assignment

---

# 10. Fulfillment Task

FulfillmentTask được tạo theo Delivery Channel.

Một FulfillmentTask tương ứng với:

- Một Email
- Một WhatsApp Message
- Một Telegram Message
- Một Zalo OA Message
- Một Portal Notification

Một Task có thể Delivery nhiều Product Item.

---

# 11. Fulfillment Package

FulfillmentPackage nhóm các Product Item theo Recipient.

Ví dụ:

```text
Customer A

↓

Thailand eSIM

Japan eSIM

↓

Email
Portal
WhatsApp
```

Một FulfillmentPackage có thể được gửi qua nhiều Delivery Channel.

Các Channel sử dụng Template riêng nhưng cùng một nội dung Fulfillment.

---

# 12. Delivery Channel

Version 2.0 hỗ trợ:

- Email
- Customer Portal
- Download QR
- WhatsApp
- Telegram
- Zalo OA

SMS chỉ sử dụng cho Notification Alert.

Không gửi QR Code qua SMS.

---

# 13. Customer Portal Access

Customer Portal là Capability độc lập.

Fulfillment chịu trách nhiệm:

- Tạo Customer Portal Access
- Tạo Access Account
- Gửi Access Information

Customer Portal hỗ trợ:

- View Order
- Download Purchased QR
- Customer Support
- Ticket
- Knowledge Base
- Product Catalog
- Reorder

---

# 14. Fulfillment Retry

Nếu Delivery thất bại:

Hệ thống Retry tối đa:

3 lần.

Nếu vẫn thất bại:

- Alternative Delivery Channel
- Customer cập nhật Delivery Channel
- Manual Support

Nếu Customer vẫn còn Payment Session hợp lệ trên Storefront:

cho phép nhập lại Delivery Information.

---

# 15. Delivery Status

Delivery Status:

```text
Pending

↓

Processing

↓

Delivered

↓

Viewed

↓

Downloaded
```

Activation không thuộc Delivery Domain.

Viewed phản ánh Customer đã mở nội dung Fulfillment.

---

# 16. Activation

Activation thuộc Mobile Network Domain.

Version 2.0 không Poll Supplier API.

Activation Monitoring sẽ được triển khai ở phiên bản sau.

---

# 17. Revoked Inventory

Product Item Return không quay về Ready Inventory ngay.

Item chuyển sang:

Revoked Inventory.

Quy trình phục hồi:

```text
Revoked

↓

Export Revoked List

↓

Supplier / MNO Verification

↓

Unused Confirmation

↓

Ready Inventory
```

---

# 18. Allocation Failure

Nếu Allocation thất bại:

- Retry Supplier
- Retry Procurement
- Manual Queue
- Refund

Kiến trúc mở để hỗ trợ thêm Failure Strategy trong các phiên bản sau.

---

# 19. Fulfillment Notification

Fulfillment Notification có thể bao gồm:

- QR Code
- Activation Guide
- APN
- Hotline
- Promotion
- Customer Portal URL
- Customer Portal Access
- Marketing Content

Nội dung được sinh từ Notification Template.

Payment Notification và Fulfillment Notification là hai Workflow độc lập.

---

# 20. Fulfillment Snapshot

FulfillmentSnapshot được tạo sau Delivery thành công.

Snapshot lưu:

- Inventory Item
- Recipient
- Delivery Channel
- Allocation Result
- Delivery Time

---

# 21. Customer Assignment

CustomerAssignment có thể chỉnh sửa.

Quy tắc:

Nếu Fulfillment Package chỉ chứa:

1 Product Item

↓

Không cho phép đổi Recipient.

Nếu Fulfillment Package chứa nhiều Product Item:

↓

Cho phép Assignment lại.

Recipient cũ sẽ nhận Notification:

QR Code trước đây đã được chuyển sang Recipient khác.

---

# 22. QR Security

QR gốc chỉ được Download một lần trong Distribution Network.

Sau lần đầu:

- Portal hiển thị Watermark.
- Portal hiển thị Blur.

QR gốc được Archive.

Chỉ YSim Staff có quyền truy cập.

Customer Portal muốn xem lại QR gốc:

Bắt buộc:

- Two-Factor Authentication (OTP).

---

# 23. Fulfillment Completion

Fulfillment được coi là hoàn thành khi:

Delivery thành công.

Không chờ:

- Activation
- Usage

---

# 24. Delivery ≠ Activation Principle

Delivery và Activation là hai Capability độc lập.

```text
Payment

↓

Inventory

↓

Allocation

↓

Fulfillment

↓

Delivery

======================
YSim Responsibility
======================

↓

Activation

↓

Usage

↓

Renewal

↓

Topup

======================
MNO / Future Version
======================
```

---

# 25. Business Decisions (Locked)

## BD-09-001

Inventory và Product Item Lifecycle là hai Business Concept độc lập.

---

## BD-09-002

Inventory luôn thuộc YSim.

---

## BD-09-003

Allocation ưu tiên:

Inventory Cost → Supplier Priority → Supplier Cost → Supplier Health → Supplier Response Time.

---

## BD-09-004

Allocation được Trigger sau Payment Success.

---

## BD-09-005

FulfillmentSession là Business Object.

---

## BD-09-006

FulfillmentTask được tạo theo Delivery Channel.

---

## BD-09-007

FulfillmentPackage nhóm các Product Item theo Recipient.

---

## BD-09-008

Customer Portal là Capability độc lập.

---

## BD-09-009

Fulfillment Retry tối đa 3 lần.

---

## BD-09-010

SMS không truyền QR Code.

---

## BD-09-011

Revoked Inventory yêu cầu Manual Verification.

---

## BD-09-012

QR gốc chỉ Download một lần trên Distribution Network.

---

## BD-09-013

Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc.

---

## BD-09-014

Fulfillment hoàn thành khi Delivery thành công.

---

## BD-09-015

Delivery và Activation là hai Business Capability độc lập.

---

# 26. Enterprise Design Principles

## EP-09-001

Inventory chỉ quản lý Product Item.

---

## EP-09-002

Mọi Product Item phải đi qua Inventory trước khi Allocation.

---

## EP-09-003

Allocation Engine độc lập với Fulfillment Engine.

---

## EP-09-004

Fulfillment chỉ chịu trách nhiệm Delivery.

---

## EP-09-005

Customer Portal là điểm truy cập thống nhất sau bán hàng.

---

## EP-09-006

QR Code là Digital Asset có yêu cầu bảo mật cao.

---

## EP-09-007

Product Item là Digital Asset có Lifecycle và Traceability xuyên suốt hệ thống.

---

# 27. Fulfillment Lifecycle

```text
Payment Success
        │
        ▼
Inventory Check
        │
        ▼
Auto Procurement (nếu cần)
        │
        ▼
Inventory
        │
        ▼
Allocation
        │
        ▼
Fulfillment Session
        │
        ▼
Fulfillment Package
        │
        ▼
Delivery
        ├── Email
        ├── Customer Portal
        ├── WhatsApp
        ├── Telegram
        └── Zalo OA
        │
        ▼
Delivered
```

---

# 28. Traceability

Workshop này kế thừa:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04
- BRD-WS-05
- BRD-WS-06
- BRD-WS-07
- BRD-WS-08

---

# 29. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Settlement Engine
- Customer Support
- Customer Portal
- Notification Center
- Inventory Management
- Supplier Integration
- Reporting
- API
- DMS
- DBD

---

# 30. Workshop Status

**Status:** FROZEN

Workshop này là Foundation cho:

- Inventory Engine
- Allocation Engine
- Fulfillment Engine
- Customer Portal
- Notification Center
- Settlement Engine

---

# 31. Next Workshop

**BRD-WS-10 – Settlement, Revenue Sharing & Financial Lifecycle**

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-001 — Inventory và Product Item Lifecycle là hai Business Concept độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-001-AC001",
      "given": "the applicable business context, actor, and input for Inventory và Product Item Lifecycle là hai Business Concept độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-09-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-09-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Inventory và Product Item Lifecycle là hai Business Concept độc lập",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-09-001-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-001-AC001",
        "BD-09-001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-001-O001",
      "obligation_text": "Inventory và Product Item Lifecycle là hai Business Concept độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Inventory và Product Item Lifecycle là hai Business Concept độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-09-001",
    "source_context_sha256": "f2aa6a096a70b662b7d90fbf87059fbc235dcb9ca249d9653a5c40730367e76b",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "3a2abb6927ab74007a75f69b22c2852094b08d9abb1f7f08ee7ad15ed1541d71",
    "source_lines": "L560-L563",
    "source_section": "25. Business Decisions (Locked) > BD-09-001"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-001",
  "title": "Inventory và Product Item Lifecycle là hai Business Concept độc lập",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-002 — Inventory luôn thuộc YSim

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-002-AC001",
      "given": "the applicable business context, actor, and input for Inventory luôn thuộc YSim",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-09-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-002-O001",
      "obligation_text": "Inventory luôn thuộc YSim"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Inventory luôn thuộc YSim.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Inventory Ownership",
    "source_context_sha256": "478910be23e3503aff0646bd9468884dbf3bf53c87b5ba06549ff059ab0c765b",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "030ee6b4d3071756dae1c1f355397d943ec10291caf7e3a686c25ecbb3234407",
    "source_lines": "L566-L569",
    "source_section": "25. Business Decisions (Locked) > BD-09-002"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-002",
  "title": "Inventory luôn thuộc YSim",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-003 — Allocation ưu tiên: Inventory Cost → Supplier Priority → Supplier Cost → Supplier Health → Suppl…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BD-09-003-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Allocation ưu tiên: Inventory Cost → Supplier Priority → Supplier Cost → Supplier Health → Suppl…",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BD-09-003-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BD-09-003-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under Allocation ưu tiên: Inventory Cost → Supplier Priority → Supplier Cost → Supplier Health → Suppl…",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BD-09-003-O001"
      ],
      "when": "design conformance is reviewed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-003-AC001",
        "BD-09-003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-003-O001",
      "obligation_text": "Allocation ưu tiên: Inventory Cost → Supplier Priority → Supplier Cost → Supplier Health → Supplier Response Time"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-09-003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-09-003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-09-003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-09-003 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-09-003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-09-003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Allocation ưu tiên: Inventory Cost → Supplier Priority → Supplier Cost → Supplier Health → Supplier Response Time.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-09-003",
    "source_context_sha256": "b58e3ee1e500105c54c3cf2308a7f0bab509e36af25e13f997538bae25aa5b74",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "ba7ed48cef26660b4c53366af44e1f5b14e4406472e57bc9a6e679a6376defa4",
    "source_lines": "L572-L577",
    "source_section": "25. Business Decisions (Locked) > BD-09-003"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PERFORMANCE_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-003",
  "title": "Allocation ưu tiên: Inventory Cost → Supplier Priority → Supplier Cost → Supplier Health → Suppl…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-004 — Allocation được Trigger sau Payment Success

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-004-AC001",
      "given": "the applicable business context, actor, and input for Allocation được Trigger sau Payment Success",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-09-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-09-004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Allocation được Trigger sau Payment Success",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-09-004-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-004-AC001",
        "BD-09-004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-004-O001",
      "obligation_text": "Allocation được Trigger sau Payment Success"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-09-004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-09-004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-09-004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-09-004 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-09-004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-09-004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Allocation được Trigger sau Payment Success.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-09-004",
    "source_context_sha256": "a58a5247737178ffaa34ef9bf81f93f59209e8b6fc083b3ac3a1ab7d1145e04f",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "1d871affa2de1f9193d7fe783fe7050f26be25df3cb70e45d8bd6a9cace792c6",
    "source_lines": "L580-L583",
    "source_section": "25. Business Decisions (Locked) > BD-09-004"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-004",
  "title": "Allocation được Trigger sau Payment Success",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-005 — FulfillmentSession là Business Object

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-09-005-AC001",
      "given": "a candidate FulfillmentSession là Business Object record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-09-005-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-09-005-AC002",
      "given": "a FulfillmentSession là Business Object candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-09-005-O001"
      ],
      "when": "the candidate is validated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-005-AC001",
        "BD-09-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-005-O001",
      "obligation_text": "FulfillmentSession là Business Object"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-09-005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-09-005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-09-005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-09-005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-09-005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-09-005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "FulfillmentSession là Business Object.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-09-005",
    "source_context_sha256": "34074930bd4ba6c22c14f501684a31f3c491720c8b70d727dc7903573156f885",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "67111391c4b118254dd188682c9e4298a5d67428e7301f596f426bc6e7820115",
    "source_lines": "L586-L589",
    "source_section": "25. Business Decisions (Locked) > BD-09-005"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-005",
  "title": "FulfillmentSession là Business Object",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-006 — FulfillmentTask được tạo theo Delivery Channel

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-006-AC001",
      "given": "the applicable business context, actor, and input for FulfillmentTask được tạo theo Delivery Channel",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-09-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-09-006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by FulfillmentTask được tạo theo Delivery Channel",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-09-006-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-006-AC001",
        "BD-09-006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-006-O001",
      "obligation_text": "FulfillmentTask được tạo theo Delivery Channel"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-09-006 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-09-006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-09-006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-09-006 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-09-006-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-09-006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "FulfillmentTask được tạo theo Delivery Channel.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Fulfillment Task",
    "source_context_sha256": "3912527b548b78757732f43c3d51656463bc4a8d888a7493d55b93e1d34b3b4c",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "0da9ff96d17f5a507213aa11f3f51d3f4ffc210bfad00bb648e977797dd2f40f",
    "source_lines": "L592-L595",
    "source_section": "25. Business Decisions (Locked) > BD-09-006"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-006",
  "title": "FulfillmentTask được tạo theo Delivery Channel",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-007 — FulfillmentPackage nhóm các Product Item theo Recipient

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-007-AC001",
      "given": "the applicable business context, actor, and input for FulfillmentPackage nhóm các Product Item theo Recipient",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-09-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-09-007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by FulfillmentPackage nhóm các Product Item theo Recipient",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-09-007-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-007-AC001",
        "BD-09-007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-007-O001",
      "obligation_text": "FulfillmentPackage nhóm các Product Item theo Recipient"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-09-007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-09-007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-09-007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-09-007 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-09-007-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-09-007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "FulfillmentPackage nhóm các Product Item theo Recipient.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Fulfillment Package",
    "source_context_sha256": "f0bf65eec68e39d5833b6ceddea03ff576b044c397328718f0b5ab535173e95f",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "a3fae279f6018d782a76f946d3d2580363a0f0b5068718d3db94ca5c846425a8",
    "source_lines": "L598-L601",
    "source_section": "25. Business Decisions (Locked) > BD-09-007"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-007",
  "title": "FulfillmentPackage nhóm các Product Item theo Recipient",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-008 — Customer Portal là Capability độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-008-AC001",
      "given": "the applicable business context, actor, and input for Customer Portal là Capability độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-09-008-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-09-008-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Customer Portal là Capability độc lập",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-09-008-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-008-AC001",
        "BD-09-008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-008-O001",
      "obligation_text": "Customer Portal là Capability độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Portal là Capability độc lập.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Customer Portal Access",
    "source_context_sha256": "de68fca9deaaaba0e5a89c3b86320baf7598a4e35e71e0bbe0be567c272d2cc8",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "b5894fa1e756c1e3bdb3880073cd560c92594d1f1f1fae73b8360a29735f47ed",
    "source_lines": "L604-L607",
    "source_section": "25. Business Decisions (Locked) > BD-09-008"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-008",
  "title": "Customer Portal là Capability độc lập",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-009 — Fulfillment Retry tối đa 3 lần

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-009-AC001",
      "given": "the applicable business context, actor, and input for Fulfillment Retry tối đa 3 lần",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-09-009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-09-009-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Fulfillment Retry tối đa 3 lần",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-09-009-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "IDEMPOTENCY",
      "controlled_contract": "EXPLICIT_IDEMPOTENCY_CONTRACT_V1",
      "criterion_id": "BD-09-009-AC003",
      "given": "a repeated request, retry, replay, or duplicate explicitly governed by Fulfillment Retry tối đa 3 lần",
      "observable_evidence": "original and repeated action identities, both outcomes, side-effect count, and resulting business state",
      "then": "the repeated action produces the requirement-specific stable result without an additional prohibited side effect",
      "verifies": [
        "BD-09-009-O001"
      ],
      "when": "the same governed action is presented again under the declared identity or deduplication boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-009-AC001",
        "BD-09-009-AC002",
        "BD-09-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-009-O001",
      "obligation_text": "Fulfillment Retry tối đa 3 lần"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-09-009 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-09-009 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [
        "BD-09-009-AC003"
      ],
      "status": "APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-09-009 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-09-009-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-09-009 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Fulfillment Retry tối đa 3 lần.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-09-009",
    "source_context_sha256": "35117a854b9715b6cada13bdfaf02008edd431ab8d04277e345f176dbcfcd88a",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "568891fe81b33d818b1e1cf72fe4f8c415c735ba850fa7d7649b3324f611ee50",
    "source_lines": "L610-L613",
    "source_section": "25. Business Decisions (Locked) > BD-09-009"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-009",
  "title": "Fulfillment Retry tối đa 3 lần",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-010 — SMS không truyền QR Code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-010-AC001",
      "given": "the applicable business context, actor, and input for SMS không truyền QR Code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-09-010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-010-O001",
      "obligation_text": "SMS không truyền QR Code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "SMS không truyền QR Code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-09-010",
    "source_context_sha256": "92f51e46f5a4d750c94863c69abd24eaac78b170460a5e67f58af04b9b6448dc",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "83119d8c3f95331c77b7b23dc8cc841545a97a59e62c72d65c3b134b34329cdd",
    "source_lines": "L616-L619",
    "source_section": "25. Business Decisions (Locked) > BD-09-010"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-010",
  "title": "SMS không truyền QR Code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-011 — Revoked Inventory yêu cầu Manual Verification

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-011-AC001",
      "given": "the applicable business context, actor, and input for Revoked Inventory yêu cầu Manual Verification",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-09-011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-011-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-011-O001",
      "obligation_text": "Revoked Inventory yêu cầu Manual Verification"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Revoked Inventory yêu cầu Manual Verification.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-09-011",
    "source_context_sha256": "4c08babf6391b2f44a1e280c87e25e8b3a3b9b71ba09eee317d626135d18a566",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "17a558b0eb4e484bb90a39ec1902179400dba1667b13484088fe77cc03da1899",
    "source_lines": "L622-L625",
    "source_section": "25. Business Decisions (Locked) > BD-09-011"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-011",
  "title": "Revoked Inventory yêu cầu Manual Verification",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-012 — QR gốc chỉ Download một lần trên Distribution Network

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-012-AC001",
      "given": "the applicable business context, actor, and input for QR gốc chỉ Download một lần trên Distribution Network",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-09-012-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-012-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-012-O001",
      "obligation_text": "QR gốc chỉ Download một lần trên Distribution Network"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "QR gốc chỉ Download một lần trên Distribution Network.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-09-012",
    "source_context_sha256": "eec94582a5780e358cab31e8c0384218a731f9da8b79a01a51f040b1c89e53a3",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "afccf80019824e73230f1a08c1cd637c587e2ac7269f91a41da06d1b193a0a14",
    "source_lines": "L628-L631",
    "source_section": "25. Business Decisions (Locked) > BD-09-012"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-012",
  "title": "QR gốc chỉ Download một lần trên Distribution Network",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-013 — Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-09-013-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-09-013-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-09-013-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-09-013-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-09-013-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-09-013-O001"
      ],
      "when": "the violating input or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-013-AC001",
        "BD-09-013-AC002",
        "BD-09-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-013-O001",
      "obligation_text": "Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-09-013 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-09-013 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-09-013 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-09-013-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-09-013-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-09-013 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-09-013",
    "source_context_sha256": "b37729906f527a89ebdebc4ace7c6d1f02fbb6df3e798f4870cda44881fc4d6c",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "b88ed36543e3a232f796e31c81c5d3ccda95a665ef117bee2876448a9723e468",
    "source_lines": "L634-L637",
    "source_section": "25. Business Decisions (Locked) > BD-09-013"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-013",
  "title": "Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-014 — Fulfillment hoàn thành khi Delivery thành công

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-014-AC001",
      "given": "the applicable business context, actor, and input for Fulfillment hoàn thành khi Delivery thành công",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-09-014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-09-014-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Fulfillment hoàn thành khi Delivery thành công",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-09-014-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-014-AC001",
        "BD-09-014-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-014-O001",
      "obligation_text": "Fulfillment hoàn thành khi Delivery thành công"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-09-014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-09-014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-09-014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-09-014 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-09-014-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-09-014 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Fulfillment hoàn thành khi Delivery thành công.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-09-014",
    "source_context_sha256": "082199309b457c38ce744ec2598a43319128d7081643a2c72a9ece18a666b7c3",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "9453b41071784ab2fdcc5bee633d3211482194cb8bdd3497a3f98e1c2eb522d3",
    "source_lines": "L640-L643",
    "source_section": "25. Business Decisions (Locked) > BD-09-014"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-014",
  "title": "Fulfillment hoàn thành khi Delivery thành công",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-015 — Delivery và Activation là hai Business Capability độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-09-015-AC001",
      "given": "the applicable business context, actor, and input for Delivery và Activation là hai Business Capability độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-09-015-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-015-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-015-O001",
      "obligation_text": "Delivery và Activation là hai Business Capability độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Delivery và Activation là hai Business Capability độc lập.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-09-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-09-015",
    "source_context_sha256": "0f0568ed2098b3ade7a758c02eda4faa5bdc5ea86a75985500ead22841d9625e",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "244271cfd53c99210d11dc1e1a0e756c86f5e3fabf5d52dbb6de3bbcdc2d77ea",
    "source_lines": "L646-L649",
    "source_section": "25. Business Decisions (Locked) > BD-09-015"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-09-015",
  "title": "Delivery và Activation là hai Business Capability độc lập",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R001 — Inventory **không phải** là trạng thái của Product Item

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R001-AC001",
      "given": "the applicable business context, actor, and input for Inventory **không phải** là trạng thái của Product Item",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the resulting business state equals the declared destination for a valid transition and records the prior state, triggering input, and transition reason",
      "verifies": [
        "BRD-WS-09-R001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-09-R001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Inventory **không phải** là trạng thái của Product Item",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-09-R001-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R001-AC001",
        "BRD-WS-09-R001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R001-O001",
      "obligation_text": "Inventory **không phải** là trạng thái của Product Item"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Inventory **không phải** là trạng thái của Product Item.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-001",
    "previous_temporary_key": "TMP-BRD-WS-09-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Inventory Architecture",
    "source_context_sha256": "ccc5f4f0d2c6b5889ff3fe1280acb629e3ca3dc9b8f9c128d96e6efef6f38dad",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "27d278cb5aeb73ba267f097dfd68bb5d83d89bcc3f9c3268a64f46acbab985c2",
    "source_lines": "L68",
    "source_section": "3. Inventory Architecture"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-09-R001",
  "title": "Inventory **không phải** là trạng thái của Product Item",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R003 — Ngay cả Auto Procurement trước Fulfillment cũng phải ghi nhận Product Item vào Inventory trước k…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R003-AC001",
      "given": "the applicable business context, actor, and input for Ngay cả Auto Procurement trước Fulfillment cũng phải ghi nhận Product Item vào Inventory trước k…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-09-R003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Ngay cả Auto Procurement trước Fulfillment cũng phải ghi nhận Product Item vào Inventory trước k…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-09-R003-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R003-AC001",
        "BRD-WS-09-R003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R003-O001",
      "obligation_text": "Ngay cả Auto Procurement trước Fulfillment cũng phải ghi nhận Product Item vào Inventory trước khi Allocation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R003 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-09-R003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Ngay cả Auto Procurement trước Fulfillment cũng phải ghi nhận Product Item vào Inventory trước khi Allocation.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-003",
    "previous_temporary_key": "TMP-BRD-WS-09-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Inventory Source",
    "source_context_sha256": "0ee6e8aacb76fa8ee97a09b8d0ea1846477ee2d6e2d40e5c01c4fbb5b4816d6a",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "285afd918ba7656588e088eae16b2cd3268ba1f9357992f2407a787e10b34147",
    "source_lines": "L162",
    "source_section": "6. Inventory Source"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-09-R003",
  "title": "Ngay cả Auto Procurement trước Fulfillment cũng phải ghi nhận Product Item vào Inventory trước k…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R004 — Allocation Engine luôn ưu tiên: 1. Inventory có Cost thấp nhất

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R004-AC001",
      "given": "the applicable business context, actor, and input for Allocation Engine luôn ưu tiên: 1. Inventory có Cost thấp nhất",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R004-AC002",
      "given": "the applicable business context, actor, and input for Allocation Engine luôn ưu tiên: 1. Inventory có Cost thấp nhất",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R004-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-09-R004-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Allocation Engine luôn ưu tiên: 1. Inventory có Cost thấp nhất",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-09-R004-O001",
        "BRD-WS-09-R004-O002"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R004-AC001",
        "BRD-WS-09-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R004-O001",
      "obligation_text": "Allocation Engine luôn ưu tiên: 1"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R004-AC002",
        "BRD-WS-09-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R004-O002",
      "obligation_text": "Inventory có Cost thấp nhất"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R004 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-09-R004-AC001",
        "BRD-WS-09-R004-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Allocation Engine luôn ưu tiên: 1. Inventory có Cost thấp nhất.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-004",
    "previous_temporary_key": "TMP-BRD-WS-09-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Allocation Engine",
    "source_context_sha256": "0bec6e04df4205f5744f35f9d6e15a0ce2764cd739fe19ba1d1d1aeff7ad728e",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "289ca962ac0e64dffd7ad956c687a59dcbbc3aad8092dd0a5d45a497e059af4a",
    "source_lines": "L181-L183",
    "source_section": "7. Allocation Engine"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-09-R004",
  "title": "Allocation Engine luôn ưu tiên: 1. Inventory có Cost thấp nhất",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R005 — Allocation Engine luôn ưu tiên: 2. Supplier Priority

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R005-AC001",
      "given": "the applicable business context, actor, and input for Allocation Engine luôn ưu tiên: 2. Supplier Priority",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R005-AC002",
      "given": "the applicable business context, actor, and input for Allocation Engine luôn ưu tiên: 2. Supplier Priority",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R005-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-09-R005-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Allocation Engine luôn ưu tiên: 2. Supplier Priority",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-09-R005-O001",
        "BRD-WS-09-R005-O002"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R005-AC001",
        "BRD-WS-09-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R005-O001",
      "obligation_text": "Allocation Engine luôn ưu tiên: 2"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R005-AC002",
        "BRD-WS-09-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R005-O002",
      "obligation_text": "Supplier Priority"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-09-R005-AC001",
        "BRD-WS-09-R005-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Allocation Engine luôn ưu tiên: 2. Supplier Priority.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-005",
    "previous_temporary_key": "TMP-BRD-WS-09-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Allocation Engine",
    "source_context_sha256": "0bec6e04df4205f5744f35f9d6e15a0ce2764cd739fe19ba1d1d1aeff7ad728e",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "b777d73aab9e9d31f8fe2cb9d74c144bd4e2f236a59ea4411c5b57b2f6eb1b48",
    "source_lines": "L181-L184",
    "source_section": "7. Allocation Engine"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-09-R005",
  "title": "Allocation Engine luôn ưu tiên: 2. Supplier Priority",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R006 — Allocation Engine luôn ưu tiên: 3. Supplier Cost

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R006-AC001",
      "given": "the applicable business context, actor, and input for Allocation Engine luôn ưu tiên: 3. Supplier Cost",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R006-AC002",
      "given": "the applicable business context, actor, and input for Allocation Engine luôn ưu tiên: 3. Supplier Cost",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R006-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-09-R006-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Allocation Engine luôn ưu tiên: 3. Supplier Cost",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-09-R006-O001",
        "BRD-WS-09-R006-O002"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R006-AC001",
        "BRD-WS-09-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R006-O001",
      "obligation_text": "Allocation Engine luôn ưu tiên: 3"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R006-AC002",
        "BRD-WS-09-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R006-O002",
      "obligation_text": "Supplier Cost"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R006 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R006 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-09-R006-AC001",
        "BRD-WS-09-R006-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Allocation Engine luôn ưu tiên: 3. Supplier Cost.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-006",
    "previous_temporary_key": "TMP-BRD-WS-09-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Allocation Engine",
    "source_context_sha256": "0bec6e04df4205f5744f35f9d6e15a0ce2764cd739fe19ba1d1d1aeff7ad728e",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "118e56293d795404e78415f37bd856ded826b3a334b2fcfaa1432f9360b95d60",
    "source_lines": "L181-L185",
    "source_section": "7. Allocation Engine"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-09-R006",
  "title": "Allocation Engine luôn ưu tiên: 3. Supplier Cost",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R007 — Allocation Engine luôn ưu tiên: 4. Supplier Health

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R007-AC001",
      "given": "the applicable business context, actor, and input for Allocation Engine luôn ưu tiên: 4. Supplier Health",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R007-AC002",
      "given": "the applicable business context, actor, and input for Allocation Engine luôn ưu tiên: 4. Supplier Health",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R007-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-09-R007-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Allocation Engine luôn ưu tiên: 4. Supplier Health",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-09-R007-O001",
        "BRD-WS-09-R007-O002"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R007-AC001",
        "BRD-WS-09-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R007-O001",
      "obligation_text": "Allocation Engine luôn ưu tiên: 4"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R007-AC002",
        "BRD-WS-09-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R007-O002",
      "obligation_text": "Supplier Health"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R007 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-09-R007-AC001",
        "BRD-WS-09-R007-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Allocation Engine luôn ưu tiên: 4. Supplier Health.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-007",
    "previous_temporary_key": "TMP-BRD-WS-09-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Allocation Engine",
    "source_context_sha256": "0bec6e04df4205f5744f35f9d6e15a0ce2764cd739fe19ba1d1d1aeff7ad728e",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "f4849455e29c0cd84ca81cbde07d02248884f88d74a68059971ca6636e4b0de5",
    "source_lines": "L181-L186",
    "source_section": "7. Allocation Engine"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-09-R007",
  "title": "Allocation Engine luôn ưu tiên: 4. Supplier Health",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R008 — Allocation Engine luôn ưu tiên: 5. Supplier Response Time

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R008-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Allocation Engine luôn ưu tiên: 5. Supplier Response Time",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-WS-09-R008-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R008-AC002",
      "given": "a v2.3 capability, configuration, or design change governed by Allocation Engine luôn ưu tiên: 5. Supplier Response Time",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-WS-09-R008-O002"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BRD-WS-09-R008-AC003",
      "given": "a proposed change with missing traceability or a boundary violation under Allocation Engine luôn ưu tiên: 5. Supplier Response Time",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BRD-WS-09-R008-O001",
        "BRD-WS-09-R008-O002"
      ],
      "when": "design conformance is reviewed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R008-AC001",
        "BRD-WS-09-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R008-O001",
      "obligation_text": "Allocation Engine luôn ưu tiên: 5"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R008-AC002",
        "BRD-WS-09-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R008-O002",
      "obligation_text": "Supplier Response Time"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R008 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R008 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-09-R008-AC001",
        "BRD-WS-09-R008-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Allocation Engine luôn ưu tiên: 5. Supplier Response Time.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-008",
    "previous_temporary_key": "TMP-BRD-WS-09-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Allocation Engine",
    "source_context_sha256": "0bec6e04df4205f5744f35f9d6e15a0ce2764cd739fe19ba1d1d1aeff7ad728e",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "8f2dbc5af01fac8a3693c143345fcf390e50944f6a29a1f61829ded0536da2b5",
    "source_lines": "L181-L187",
    "source_section": "7. Allocation Engine"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PERFORMANCE_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-09-R008",
  "title": "Allocation Engine luôn ưu tiên: 5. Supplier Response Time",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R009 — Activation Monitoring sẽ được triển khai ở phiên bản sau

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Activation Monitoring sẽ được triển khai ở phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-009",
    "previous_temporary_key": "TMP-BRD-WS-09-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Activation",
    "source_context_sha256": "ef8deb41b23b228594b262057ff135cdbaf9739d4922b5b14f3f4d00b88a7925",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "7c6fcf0965c34dca24e4684592170206a34ca99647c171dcefd151aa5a97ef52",
    "source_lines": "L366",
    "source_section": "16. Activation"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "FUTURE",
  "stable_id": "BRD-WS-09-R009",
  "title": "Activation Monitoring sẽ được triển khai ở phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R010 — Kiến trúc mở để hỗ trợ thêm Failure Strategy trong các phiên bản sau

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Kiến trúc mở để hỗ trợ thêm Failure Strategy trong các phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-010",
    "previous_temporary_key": "TMP-BRD-WS-09-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Allocation Failure",
    "source_context_sha256": "b128afce29b79ddac3e77673263ff8e7ca5a4ea1905910a92f538452f362d261",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "146814458179069f70d17465d732f435609d33c0c809923d9246270f29a637b2",
    "source_lines": "L411",
    "source_section": "18. Allocation Failure"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "FUTURE",
  "stable_id": "BRD-WS-09-R010",
  "title": "Kiến trúc mở để hỗ trợ thêm Failure Strategy trong các phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R011 — Không cho phép đổi Recipient

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R011-AC001",
      "given": "the applicable business context, actor, and input for Không cho phép đổi Recipient",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-09-R011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Không cho phép đổi Recipient",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-09-R011-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R011-AC001",
        "BRD-WS-09-R011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R011-O001",
      "obligation_text": "Không cho phép đổi Recipient"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cho phép đổi Recipient.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-011",
    "previous_temporary_key": "TMP-BRD-WS-09-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Customer Assignment",
    "source_context_sha256": "0530ad65b9a0d65a87e887f9ec4fcf07ba17510b06d26c9c3d75e2fe90333d42",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "e13743cfd9a5f191f02af0929b7c40f0448da4eaca5227b421ea2dc5f34f945a",
    "source_lines": "L460",
    "source_section": "21. Customer Assignment"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-09-R011",
  "title": "Không cho phép đổi Recipient",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R012 — QR gốc chỉ được Download một lần trong Distribution Network

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R012-AC001",
      "given": "the applicable business context, actor, and input for QR gốc chỉ được Download một lần trong Distribution Network",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R012-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R012-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R012-O001",
      "obligation_text": "QR gốc chỉ được Download một lần trong Distribution Network"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "QR gốc chỉ được Download một lần trong Distribution Network.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-012",
    "previous_temporary_key": "TMP-BRD-WS-09-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. QR Security",
    "source_context_sha256": "c878a1b4cb0732b168fc4cc60804862e228160113ed7ff4169983ebdef722cf0",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "9fd6477a03ce946bfa9c4aa84e582d5b7d95cdfad8f607e04df2c2ef010e7c49",
    "source_lines": "L476",
    "source_section": "22. QR Security"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-09-R012",
  "title": "QR gốc chỉ được Download một lần trong Distribution Network",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R013 — Customer Portal muốn xem lại QR gốc: Bắt buộc

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R013-AC001",
      "given": "the applicable business context, actor, and input for Customer Portal muốn xem lại QR gốc: Bắt buộc",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-09-R013-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-09-R013-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Customer Portal muốn xem lại QR gốc: Bắt buộc",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-09-R013-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R013-AC001",
        "BRD-WS-09-R013-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R013-O001",
      "obligation_text": "Customer Portal muốn xem lại QR gốc: Bắt buộc"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Portal muốn xem lại QR gốc: Bắt buộc:",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-013",
    "previous_temporary_key": "TMP-BRD-WS-09-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. QR Security",
    "source_context_sha256": "c878a1b4cb0732b168fc4cc60804862e228160113ed7ff4169983ebdef722cf0",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "ec717c98ed85f9658795a7b8119f1e239a8a6f915198c73aad8e48fe3e16a0b4",
    "source_lines": "L487-L489",
    "source_section": "22. QR Security"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-09-R013",
  "title": "Customer Portal muốn xem lại QR gốc: Bắt buộc",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R014 — Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP)

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-09-R014-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP)",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-09-R014-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-09-R014-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP)",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-09-R014-O001"
      ],
      "when": "the protected decision or action is attempted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R014-AC001",
        "BRD-WS-09-R014-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R014-O001",
      "obligation_text": "Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP)"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R014 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-09-R014-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-09-R014 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP).",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "historical_derived_from": [
      "docs/BRD/BRD-WS-09.md:L491"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-014",
    "previous_temporary_key": "TMP-BRD-WS-09-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. QR Security",
    "source_context_sha256": "c878a1b4cb0732b168fc4cc60804862e228160113ed7ff4169983ebdef722cf0",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "73881032b519d93c38e2c9b158bf77716c88c17216adaf7a099b0b6956d9cc1d",
    "source_lines": "L487-L491",
    "source_section": "22. QR Security"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-09-R014",
  "title": "Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP)",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-09-001 — Inventory chỉ quản lý Product Item

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-09-001-AC001",
      "given": "the applicable business context, actor, and input for Inventory chỉ quản lý Product Item",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-09-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-09-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Inventory chỉ quản lý Product Item",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-09-001-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-001-AC001",
        "EP-09-001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-09-001-O001",
      "obligation_text": "Inventory chỉ quản lý Product Item"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Inventory chỉ quản lý Product Item.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-09-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-09-001",
    "source_context_sha256": "5cb82035e9368a1d52011ebcdea544e04c349834935d9eabb075fc5860d21659",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "5fb9651655db26d8367bca865e3d4d4a298897c602ff34cfb0a5f8b90117102b",
    "source_lines": "L654-L657",
    "source_section": "26. Enterprise Design Principles > EP-09-001"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-09-001",
  "title": "Inventory chỉ quản lý Product Item",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-09-002 — Mọi Product Item phải đi qua Inventory trước khi Allocation

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-09-002-AC001",
      "given": "the applicable business context, actor, and input for Mọi Product Item phải đi qua Inventory trước khi Allocation",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-09-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-09-002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Mọi Product Item phải đi qua Inventory trước khi Allocation",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-09-002-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-002-AC001",
        "EP-09-002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-09-002-O001",
      "obligation_text": "Mọi Product Item phải đi qua Inventory trước khi Allocation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-09-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-09-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-09-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-09-002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-09-002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-09-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Product Item phải đi qua Inventory trước khi Allocation.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-09-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-09-002",
    "source_context_sha256": "49950ebd19f692c86bec203e7eae40b6f2aae92e988aaddb54ee94666fca9951",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "00495e3a4c1ab22f0c039478def9b1090d27c450cded89ba9046da0ab45e3b40",
    "source_lines": "L660-L663",
    "source_section": "26. Enterprise Design Principles > EP-09-002"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-09-002",
  "title": "Mọi Product Item phải đi qua Inventory trước khi Allocation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-09-003 — Allocation Engine độc lập với Fulfillment Engine

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-09-003-AC001",
      "given": "the applicable business context, actor, and input for Allocation Engine độc lập với Fulfillment Engine",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "EP-09-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-09-003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Allocation Engine độc lập với Fulfillment Engine",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-09-003-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-09-003-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Allocation Engine độc lập với Fulfillment Engine",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-09-003-O001"
      ],
      "when": "the violating input or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-003-AC001",
        "EP-09-003-AC002",
        "EP-09-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-09-003-O001",
      "obligation_text": "Allocation Engine độc lập với Fulfillment Engine"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-09-003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-09-003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-09-003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-09-003-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-09-003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-09-003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Allocation Engine độc lập với Fulfillment Engine.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-09-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-09-003",
    "source_context_sha256": "b2e1eaba4697f01a718b76550ed5623bca9bfedf2b12edb8f0ca60f6b5a4364f",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "f7b79e8339c4d231389f2254b1f1bb51bb5886720d7ac3231c31ddaa1ea856a6",
    "source_lines": "L666-L669",
    "source_section": "26. Enterprise Design Principles > EP-09-003"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-09-003",
  "title": "Allocation Engine độc lập với Fulfillment Engine",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-09-004 — Fulfillment chỉ chịu trách nhiệm Delivery

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-09-004-AC001",
      "given": "the applicable business context, actor, and input for Fulfillment chỉ chịu trách nhiệm Delivery",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-09-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-09-004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Fulfillment chỉ chịu trách nhiệm Delivery",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-09-004-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-004-AC001",
        "EP-09-004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-09-004-O001",
      "obligation_text": "Fulfillment chỉ chịu trách nhiệm Delivery"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-09-004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-09-004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-09-004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-09-004 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-09-004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-09-004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Fulfillment chỉ chịu trách nhiệm Delivery.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-09-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-09-004",
    "source_context_sha256": "6c8cffcd37d5d5d3f1d18b45014e5fe5b2ece1e6cc79749c69f4dc69ec221a54",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
    "source_lines": "L672-L675",
    "source_section": "26. Enterprise Design Principles > EP-09-004"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-09-004",
  "title": "Fulfillment chỉ chịu trách nhiệm Delivery",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-09-005 — Customer Portal là điểm truy cập thống nhất sau bán hàng

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-09-005-AC001",
      "given": "the applicable business context, actor, and input for Customer Portal là điểm truy cập thống nhất sau bán hàng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-09-005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-09-005-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Customer Portal là điểm truy cập thống nhất sau bán hàng",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-09-005-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-005-AC001",
        "EP-09-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-09-005-O001",
      "obligation_text": "Customer Portal là điểm truy cập thống nhất sau bán hàng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Portal là điểm truy cập thống nhất sau bán hàng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-09-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-09-005",
    "source_context_sha256": "2051e954d6b249b1c0c84eb79eba54796044453657618c072b87f699644b6511",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "468c328877abb51c9f47164cab10757565444205708dea4fc6142a66ed870b60",
    "source_lines": "L678-L681",
    "source_section": "26. Enterprise Design Principles > EP-09-005"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-09-005",
  "title": "Customer Portal là điểm truy cập thống nhất sau bán hàng",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-09-006 — QR Code là Digital Asset có yêu cầu bảo mật cao

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-09-006-AC001",
      "given": "the applicable business context, actor, and input for QR Code là Digital Asset có yêu cầu bảo mật cao",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-09-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-09-006-O001",
      "obligation_text": "QR Code là Digital Asset có yêu cầu bảo mật cao"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "QR Code là Digital Asset có yêu cầu bảo mật cao.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-09-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-09-006",
    "source_context_sha256": "fe6e2e1fd3fb9d64f88ca018ba668a3bde83e0f7770639ae992ac175939b7ad3",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "79ab5335a64d221d2e58c41d53ebfed330c968e71db7fae246b36e3dc3cbb233",
    "source_lines": "L684-L687",
    "source_section": "26. Enterprise Design Principles > EP-09-006"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-09-006",
  "title": "QR Code là Digital Asset có yêu cầu bảo mật cao",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-09-007 — Product Item là Digital Asset có Lifecycle và Traceability xuyên suốt hệ thống

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-09-007-AC001",
      "given": "the applicable business context, actor, and input for Product Item là Digital Asset có Lifecycle và Traceability xuyên suốt hệ thống",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-09-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-09-007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Product Item là Digital Asset có Lifecycle và Traceability xuyên suốt hệ thống",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-09-007-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-007-AC001",
        "EP-09-007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-09-007-O001",
      "obligation_text": "Product Item là Digital Asset có Lifecycle và Traceability xuyên suốt hệ thống"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Product Item là Digital Asset có Lifecycle và Traceability xuyên suốt hệ thống.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-09-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-09-007",
    "source_context_sha256": "6bb34b5bdce6b1e0ca0c2cc0214d8015a3a9c6daec2e84a29644f81934ed536c",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "2ce11fbc71784a61228aa06047d014b45156cd5457d4943320177bc7fde1b7a9",
    "source_lines": "L690-L693",
    "source_section": "26. Enterprise Design Principles > EP-09-007"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-09-007",
  "title": "Product Item là Digital Asset có Lifecycle và Traceability xuyên suốt hệ thống",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
