---
document_code: "BRD-WS-09"
document_id: "BRD-WS-09"
title: "Inventory, Allocation & Fulfillment Lifecycle"
version: "2.3.0-draft.3"
document_revision: "2.3.0-draft.3"
status: "V2.3_DRAFT"
lifecycle_status: "V2.3_DRAFT"
language: "vi-VN"
baseline: "2.3"
product_baseline: "2.3"
source_lineage: "v2.2 + approved Phase 1/2A/2B + accepted Acceptance Model C1 + accepted Mapping C3"
source_baseline: "v2.2"
last_reviewed_date: "2026-07-15"
last_remediated_on: "2026-07-17"
applicable_scope: "V2.3_ACTIVE_AND_RETAINED_SCOPE_RECORDS"
generated_registry_role: "BRD_CANONICAL_SOURCE"
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

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-09-001 — Inventory và Product Item Lifecycle là hai Business Concept độc lập

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-001",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "41eb88ef03ad2a9cf81d68fcd1e571b5e8975f4def1354c8d74014e6d52c93ba"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-001-AC001",
        "BD-09-001-AC002",
        "BD-09-001-AC003"
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
    "source_fingerprint": "41eb88ef03ad2a9cf81d68fcd1e571b5e8975f4def1354c8d74014e6d52c93ba",
    "source_lines": "L799-L874",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-002",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "fcdeaed2948a88dc98b3150195deccee47d75b333edad259918d1f40af83a89e"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-002-AC001",
        "BD-09-002-AC002",
        "BD-09-002-AC003"
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
    "source_fingerprint": "fcdeaed2948a88dc98b3150195deccee47d75b333edad259918d1f40af83a89e",
    "source_lines": "L876-L951",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-003",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "1b6cf6bd7bdde5e4ee9a7a0c3e42b9f85b751a5d485e4f6c47628e3a00532a3b"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-003-AC001",
        "BD-09-003-AC002",
        "BD-09-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-003-O001",
      "obligation_text": "Allocation ưu tiên: Inventory Cost → Supplier Priority → Supplier Cost → Supplier Health → Supplier Response Time"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-003 does not define a recovery obligation."
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
    "source_fingerprint": "1b6cf6bd7bdde5e4ee9a7a0c3e42b9f85b751a5d485e4f6c47628e3a00532a3b",
    "source_lines": "L953-L1065",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-004",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "bdd781aeb551d78baea8b6312fa9b76994461579811ef99a9f6dd683beac5106"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-004-AC001",
        "BD-09-004-AC002",
        "BD-09-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-004-O001",
      "obligation_text": "Allocation được Trigger sau Payment Success"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-004 does not define a recovery obligation."
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
    "source_fingerprint": "bdd781aeb551d78baea8b6312fa9b76994461579811ef99a9f6dd683beac5106",
    "source_lines": "L1067-L1179",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-005",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "0621a7f4d68cfa6365fc9e0bdcec6b1a82c49dc52acd807ee1f8074cf8339606"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-005-AC001",
        "BD-09-005-AC002",
        "BD-09-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-005-O001",
      "obligation_text": "FulfillmentSession là Business Object"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-005 does not define a recovery obligation."
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
    "source_fingerprint": "0621a7f4d68cfa6365fc9e0bdcec6b1a82c49dc52acd807ee1f8074cf8339606",
    "source_lines": "L1181-L1289",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-006",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "5a02fb83a8791d03bbe2127c92624233ab0a67db342c1c3851b493b4ce7bebc3"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-006-AC001",
        "BD-09-006-AC002",
        "BD-09-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-006-O001",
      "obligation_text": "FulfillmentTask được tạo theo Delivery Channel"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-006-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-006-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-006 does not define a recovery obligation."
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
    "source_fingerprint": "5a02fb83a8791d03bbe2127c92624233ab0a67db342c1c3851b493b4ce7bebc3",
    "source_lines": "L1291-L1399",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-007",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "f05468bea857bf8efe3a7a54b67b1e7472afc6cfa648d585098b19016b52d760"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-007-AC001",
        "BD-09-007-AC002",
        "BD-09-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-007-O001",
      "obligation_text": "FulfillmentPackage nhóm các Product Item theo Recipient"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-007 does not define a recovery obligation."
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
    "source_fingerprint": "f05468bea857bf8efe3a7a54b67b1e7472afc6cfa648d585098b19016b52d760",
    "source_lines": "L1401-L1509",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005",
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-008",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "3b87829f2019d8cc8db0531ffdbacfa8af64a4b66c9219a959cb1c2ecdcd9e6e"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-008-AC001",
        "BD-09-008-AC002",
        "BD-09-008-AC003"
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
    "source_fingerprint": "3b87829f2019d8cc8db0531ffdbacfa8af64a4b66c9219a959cb1c2ecdcd9e6e",
    "source_lines": "L1511-L1592",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-009",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "b83c08b5148445a2beadc93a412c31e304cb1e38db9599b02c8386493c0f0d21"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-009 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-009 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-009 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-009-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-009-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-009 does not define a recovery obligation."
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
    "source_fingerprint": "b83c08b5148445a2beadc93a412c31e304cb1e38db9599b02c8386493c0f0d21",
    "source_lines": "L1594-L1706",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-010",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "331f9089501fdc2aec2096e75d2ddb58d32ef0f8d6b4e41de31f7e55be547fc6"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-010-AC001",
        "BD-09-010-AC002",
        "BD-09-010-AC003"
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
    "source_fingerprint": "331f9089501fdc2aec2096e75d2ddb58d32ef0f8d6b4e41de31f7e55be547fc6",
    "source_lines": "L1708-L1783",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-011",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "e286efc3d4b75ed939cffe905e46e5a84781ce9e675bd51beae8113246111316"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-011-AC001",
        "BD-09-011-AC002",
        "BD-09-011-AC003"
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
    "source_fingerprint": "e286efc3d4b75ed939cffe905e46e5a84781ce9e675bd51beae8113246111316",
    "source_lines": "L1785-L1860",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-011"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-012",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "ba1bb3a20d7e50f5e94a5d7b44b7157f2c71288838a0d94aafe32c4756be34e4"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-012-AC001",
        "BD-09-012-AC002",
        "BD-09-012-AC003"
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
    "source_fingerprint": "ba1bb3a20d7e50f5e94a5d7b44b7157f2c71288838a0d94aafe32c4756be34e4",
    "source_lines": "L1862-L1937",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-012"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-013",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "12873fa9590c2badbe5548da48583c89e32b7b1fb769aafef0cd15b10d64725f"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-013 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-013 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-013 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-013-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-013-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-013 does not define a recovery obligation."
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
    "source_fingerprint": "12873fa9590c2badbe5548da48583c89e32b7b1fb769aafef0cd15b10d64725f",
    "source_lines": "L1939-L2051",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-013"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-003",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-014",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "678e42233846db006f0283c8f9b6857ce193d5b922a222a9bafc013388c156eb"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-014-AC001",
        "BD-09-014-AC002",
        "BD-09-014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-09-014-O001",
      "obligation_text": "Fulfillment hoàn thành khi Delivery thành công"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-09-014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-09-014 does not define a recovery obligation."
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
    "source_fingerprint": "678e42233846db006f0283c8f9b6857ce193d5b922a222a9bafc013388c156eb",
    "source_lines": "L2053-L2165",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-014"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-09-015",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "32ca1212884a39f553b1ba788a088b97416534058a0856c6ce621f2a6b36da28"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-09-015-AC001",
        "BD-09-015-AC002",
        "BD-09-015-AC003"
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
    "source_fingerprint": "32ca1212884a39f553b1ba788a088b97416534058a0856c6ce621f2a6b36da28",
    "source_lines": "L2167-L2246",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-09-015"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-09-R001",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "27d278cb5aeb73ba267f097dfd68bb5d83d89bcc3f9c3268a64f46acbab985c2"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R001-AC001",
        "BRD-WS-09-R001-AC002",
        "BRD-WS-09-R001-AC003"
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
    "source_lines": "L2248-L2323",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-09-R003",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "285afd918ba7656588e088eae16b2cd3268ba1f9357992f2407a787e10b34147"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R003-AC001",
        "BRD-WS-09-R003-AC002",
        "BRD-WS-09-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R003-O001",
      "obligation_text": "Ngay cả Auto Procurement trước Fulfillment cũng phải ghi nhận Product Item vào Inventory trước khi Allocation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R003 does not define a recovery obligation."
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
    "source_lines": "L2325-L2437",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-09-R004",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "289ca962ac0e64dffd7ad956c687a59dcbbc3aad8092dd0a5d45a497e059af4a"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R004-AC001",
        "BRD-WS-09-R004-AC003",
        "BRD-WS-09-R004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R004-O001",
      "obligation_text": "Allocation Engine luôn ưu tiên: 1"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R004-AC002",
        "BRD-WS-09-R004-AC003",
        "BRD-WS-09-R004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R004-O002",
      "obligation_text": "Inventory có Cost thấp nhất"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R004-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R004-AC001",
        "BRD-WS-09-R004-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R004 does not define a recovery obligation."
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
    "source_lines": "L2439-L2562",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-09-R005",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "3f5e00d5acd2e0d0e7ab3ef6d88e4d707ff6370168fd741acb7407a4dd10496a"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R005-AC001",
        "BRD-WS-09-R005-AC003",
        "BRD-WS-09-R005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R005-O001",
      "obligation_text": "Allocation Engine luôn ưu tiên: 2"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R005-AC002",
        "BRD-WS-09-R005-AC003",
        "BRD-WS-09-R005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R005-O002",
      "obligation_text": "Supplier Priority"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R005-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R005-AC001",
        "BRD-WS-09-R005-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R005 does not define a recovery obligation."
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
    "source_fingerprint": "3f5e00d5acd2e0d0e7ab3ef6d88e4d707ff6370168fd741acb7407a4dd10496a",
    "source_lines": "L2564-L2687",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-09-R006",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "18837bb8e82825318bc1441022cf1ad758f3fcfaf6e995b9e806375df1cbe3e6"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R006-AC001",
        "BRD-WS-09-R006-AC003",
        "BRD-WS-09-R006-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R006-O001",
      "obligation_text": "Allocation Engine luôn ưu tiên: 3"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R006-AC002",
        "BRD-WS-09-R006-AC003",
        "BRD-WS-09-R006-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R006-O002",
      "obligation_text": "Supplier Cost"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R006-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R006-AC001",
        "BRD-WS-09-R006-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R006 does not define a recovery obligation."
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
    "source_fingerprint": "18837bb8e82825318bc1441022cf1ad758f3fcfaf6e995b9e806375df1cbe3e6",
    "source_lines": "L2689-L2812",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-09-R007",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "73c65e93195ceb55ce797db3cceec11f7c38a84a5108f682ee36a0c23574c764"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R007-AC001",
        "BRD-WS-09-R007-AC003",
        "BRD-WS-09-R007-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R007-O001",
      "obligation_text": "Allocation Engine luôn ưu tiên: 4"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R007-AC002",
        "BRD-WS-09-R007-AC003",
        "BRD-WS-09-R007-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R007-O002",
      "obligation_text": "Supplier Health"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R007-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R007-AC001",
        "BRD-WS-09-R007-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R007 does not define a recovery obligation."
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
    "source_fingerprint": "73c65e93195ceb55ce797db3cceec11f7c38a84a5108f682ee36a0c23574c764",
    "source_lines": "L2814-L2937",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-09-R008",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "4a8bdefa1b4f951a74acd89ad00a9e6cb062497bbef6c809ab429b938282497b"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R008-AC001",
        "BRD-WS-09-R008-AC003",
        "BRD-WS-09-R008-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R008-O001",
      "obligation_text": "Allocation Engine luôn ưu tiên: 5"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R008-AC002",
        "BRD-WS-09-R008-AC003",
        "BRD-WS-09-R008-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R008-O002",
      "obligation_text": "Supplier Response Time"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R008 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R008-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R008-AC001",
        "BRD-WS-09-R008-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R008 does not define a recovery obligation."
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
    "source_fingerprint": "4a8bdefa1b4f951a74acd89ad00a9e6cb062497bbef6c809ab429b938282497b",
    "source_lines": "L2939-L3062",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-09-R009",
    "scope_status": "FUTURE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_lines": "L3064-L3122",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-09-R010",
    "scope_status": "FUTURE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_lines": "L3124-L3182",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-09-R011",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "e13743cfd9a5f191f02af0929b7c40f0448da4eaca5227b421ea2dc5f34f945a"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R011-AC001",
        "BRD-WS-09-R011-AC002",
        "BRD-WS-09-R011-AC003"
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
    "source_lines": "L3184-L3259",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R011"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-09-R012",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "9fd6477a03ce946bfa9c4aa84e582d5b7d95cdfad8f607e04df2c2ef010e7c49"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R012-AC001",
        "BRD-WS-09-R012-AC002",
        "BRD-WS-09-R012-AC003"
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
    "source_lines": "L3261-L3336",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R012"
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
### BRD-WS-09-R013 — Khi Customer Portal yêu cầu truy cập lại QR gốc, xác thực hai yếu tố bằng OTP là bắt buộc

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-09-R013",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "28a3de5c6d155e4dc4d9cb523cd75b9953532f43fe1b8a1de3c1a526124887a0"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R013-AC001",
        "BRD-WS-09-R013-AC002",
        "BRD-WS-09-R013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R013-O001",
      "obligation_text": "Khi Customer Portal yêu cầu truy cập lại QR gốc, xác thực hai yếu tố bằng OTP là bắt buộc"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi Customer Portal yêu cầu truy cập lại QR gốc, xác thực hai yếu tố bằng OTP là bắt buộc.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-09.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "22. QR Security"
    },
    "deterministic_transformation": "EXPAND_QR_REACCESS_CONDITION_AND_OUTCOME",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-09-013",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-09-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. QR Security",
    "source_context_sha256": "c878a1b4cb0732b168fc4cc60804862e228160113ed7ff4169983ebdef722cf0",
    "source_document": "docs/BRD/BRD-WS-09.md",
    "source_fingerprint": "28a3de5c6d155e4dc4d9cb523cd75b9953532f43fe1b8a1de3c1a526124887a0",
    "source_fingerprint_before_c3": "ec717c98ed85f9658795a7b8119f1e239a8a6f915198c73aad8e48fe3e16a0b4",
    "source_lines": "L3338-L3436",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-09.md",
      "lines": "L487-L489",
      "section": "22. QR Security"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R013"
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
  "title": "Khi Customer Portal yêu cầu truy cập lại QR gốc, xác thực hai yếu tố bằng OTP là bắt buộc",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-09-R014 — Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP)

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-09-R014",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "73881032b519d93c38e2c9b158bf77716c88c17216adaf7a099b0b6956d9cc1d"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-09-R014-AC001",
        "BRD-WS-09-R014-AC002",
        "BRD-WS-09-R014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-09-R014-O001",
      "obligation_text": "Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP)"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-09-R014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-09-R014 does not define a recovery obligation."
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
    "source_lines": "L3438-L3553",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-09-R014"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-09-001",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "1f4e419785353c6ab758b47decaf0d96c7f81e15e65b65bb46a402419432159c"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-001-AC001",
        "EP-09-001-AC002",
        "EP-09-001-AC003"
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
    "source_fingerprint": "1f4e419785353c6ab758b47decaf0d96c7f81e15e65b65bb46a402419432159c",
    "source_lines": "L3555-L3630",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-09-001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-09-002",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "a8d37be0ae6c626d9a812b975a041609cb0dccb2a5b298fc233a66f5fcb06f00"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-002-AC001",
        "EP-09-002-AC002",
        "EP-09-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-09-002-O001",
      "obligation_text": "Mọi Product Item phải đi qua Inventory trước khi Allocation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-09-002 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-09-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-09-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-09-002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-09-002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-09-002 does not define a recovery obligation."
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
    "source_fingerprint": "a8d37be0ae6c626d9a812b975a041609cb0dccb2a5b298fc233a66f5fcb06f00",
    "source_lines": "L3632-L3744",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-09-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-09-003",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "a5decb906f8311a22c866f90e219809c782697925298d0a2c87bf909385d8e40"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-09-003-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-09-003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-09-003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-09-003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-09-003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-09-003 does not define a recovery obligation."
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
    "source_fingerprint": "a5decb906f8311a22c866f90e219809c782697925298d0a2c87bf909385d8e40",
    "source_lines": "L3746-L3860",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-09-003"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "Fulfillment may consume their outcomes but does not own those domains"
    ],
    "concrete_bindings": [
      {
        "expected_outcome": {
          "authoritative_source": {
            "allowed_identifiers": [
              "EP-09-004.POLICY.OUTCOME.CONFORMING"
            ],
            "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
            "source_type": "SOURCE_LITERAL",
            "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
          },
          "identifier": "EP-09-004.POLICY.OUTCOME.CONFORMING",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-09.md",
            "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
            "source_lines": "L672-L675",
            "source_section": "26. Enterprise Design Principles > EP-09-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_OUTCOME",
            "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY.OUTCOME.CONFORMING",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_OUTCOME"
        },
        "policy": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
            "source_type": "SOURCE_LITERAL",
            "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
          },
          "identifier": "EP-09-004.POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-09.md",
            "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
            "source_lines": "L672-L675",
            "source_section": "26. Enterprise Design Principles > EP-09-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "policy_inputs": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
            "source_type": "SOURCE_LITERAL",
            "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
          },
          "identifier": "EP-09-004.POLICY_INPUTS",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-09.md",
            "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
            "source_lines": "L672-L675",
            "source_section": "26. Enterprise Design Principles > EP-09-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY_INPUTS",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "policy_version": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
            "source_type": "SOURCE_LITERAL",
            "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
          },
          "identifier": "EP-09-004.POLICY_VERSION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-09.md",
            "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
            "source_lines": "L672-L675",
            "source_section": "26. Enterprise Design Principles > EP-09-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_VERSION",
            "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY_VERSION",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_VERSION"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.EP-09-004",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Fulfillment changes pricing, payment or procurement decisions"
    ],
    "operator_composition": [
      "POLICY_OUTCOME_EQUALS"
    ],
    "positive_oracle": [
      "Fulfillment owns Delivery responsibility only"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
      "source_lines": "L672-L675",
      "source_section": "26. Enterprise Design Principles > EP-09-004"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
          "source_type": "SOURCE_LITERAL",
          "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
        },
        "identifier": "EP-09-004.EP-09-004.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "EP-09-004.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-09.md",
          "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
          "source_lines": "L672-L675",
          "source_section": "26. Enterprise Design Principles > EP-09-004"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.EP-09-004.EP-09-004.EP-09-004.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "EP-09-004.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.FULFILLMENT_ID",
        "FIELD.DELIVERY_ID",
        "FIELD.RESPONSIBILITY_MAP",
        "FIELD.PRICING_CHANGES",
        "FIELD.PAYMENT_CHANGES",
        "FIELD.PROCUREMENT_CHANGES"
      ],
      "producer": "EP-09-004.EVIDENCE.PRODUCER",
      "required_collection_origin": "EP-09-004.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.FULFILLMENT_ID",
        "FIELD.DELIVERY_ID",
        "FIELD.RESPONSIBILITY_MAP",
        "FIELD.PRICING_CHANGES",
        "FIELD.PAYMENT_CHANGES",
        "FIELD.PROCUREMENT_CHANGES"
      ],
      "required_values_or_hashes": [
        "EP-09-004.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "EP-09-004.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "EP-09-004.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "EP-09-004-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS",
          "evaluator_consumed_bindings": [
            "expected_outcome",
            "policy",
            "policy_inputs",
            "policy_version"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
              "source_type": "SOURCE_LITERAL",
              "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
            },
            "identifier": "EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-09.md",
              "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
              "source_lines": "L672-L675",
              "source_section": "26. Enterprise Design Principles > EP-09-004"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.EP-09-004.EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
              "source_type": "SOURCE_LITERAL",
              "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
            },
            "identifier": "EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-09.md",
              "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
              "source_lines": "L672-L675",
              "source_section": "26. Enterprise Design Principles > EP-09-004"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "RESOLVE.EP-09-004.EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_OUTCOME"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "expected_outcome": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-09-004.POLICY.OUTCOME.CONFORMING"
                  ],
                  "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
                },
                "identifier": "EP-09-004.POLICY.OUTCOME.CONFORMING",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-09.md",
                  "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
                  "source_lines": "L672-L675",
                  "source_section": "26. Enterprise Design Principles > EP-09-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY.OUTCOME.CONFORMING",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "policy": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
                },
                "identifier": "EP-09-004.POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-09.md",
                  "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
                  "source_lines": "L672-L675",
                  "source_section": "26. Enterprise Design Principles > EP-09-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "policy_inputs": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
                },
                "identifier": "EP-09-004.POLICY_INPUTS",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-09.md",
                  "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
                  "source_lines": "L672-L675",
                  "source_section": "26. Enterprise Design Principles > EP-09-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY_INPUTS",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "policy_version": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
                },
                "identifier": "EP-09-004.POLICY_VERSION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-09.md",
                  "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
                  "source_lines": "L672-L675",
                  "source_section": "26. Enterprise Design Principles > EP-09-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_VERSION",
                  "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY_VERSION",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_VERSION"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
                },
                "identifier": "EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-09.md",
                  "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
                  "source_lines": "L672-L675",
                  "source_section": "26. Enterprise Design Principles > EP-09-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.EP-09-004.EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
                },
                "identifier": "EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-09.md",
                  "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
                  "source_lines": "L672-L675",
                  "source_section": "26. Enterprise Design Principles > EP-09-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "OBSERVE.EP-09-004.EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
                "source_type": "SOURCE_LITERAL",
                "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
              },
              "identifier": "EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-09.md",
                "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
                "source_lines": "L672-L675",
                "source_section": "26. Enterprise Design Principles > EP-09-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.EP-09-004.EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "POLICY_OUTCOME_EQUALS"
          },
          "obligation_id": "EP-09-004-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
              "source_type": "SOURCE_LITERAL",
              "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
            },
            "identifier": "EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-09.md",
              "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
              "source_lines": "L672-L675",
              "source_section": "26. Enterprise Design Principles > EP-09-004"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "OBSERVE.EP-09-004.EP-09-004.EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_OUTCOME"
          },
          "operator_id": "POLICY_OUTCOME_EQUALS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "expected_outcome": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "EP-09-004.POLICY.OUTCOME.CONFORMING"
                ],
                "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
                "source_type": "SOURCE_LITERAL",
                "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
              },
              "identifier": "EP-09-004.POLICY.OUTCOME.CONFORMING",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-09.md",
                "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
                "source_lines": "L672-L675",
                "source_section": "26. Enterprise Design Principles > EP-09-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_OUTCOME",
                "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY.OUTCOME.CONFORMING",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_OUTCOME"
            },
            "policy": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
                "source_type": "SOURCE_LITERAL",
                "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
              },
              "identifier": "EP-09-004.POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-09.md",
                "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
                "source_lines": "L672-L675",
                "source_section": "26. Enterprise Design Principles > EP-09-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "policy_inputs": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
                "source_type": "SOURCE_LITERAL",
                "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
              },
              "identifier": "EP-09-004.POLICY_INPUTS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-09.md",
                "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
                "source_lines": "L672-L675",
                "source_section": "26. Enterprise Design Principles > EP-09-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY_INPUTS",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "policy_version": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
                "source_type": "SOURCE_LITERAL",
                "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
              },
              "identifier": "EP-09-004.POLICY_VERSION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-09.md",
                "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
                "source_lines": "L672-L675",
                "source_section": "26. Enterprise Design Principles > EP-09-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.EP-09-004.EP-09-004.POLICY_VERSION",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          }
        }
      ],
      "boundary_cases": [
        "Fulfillment may consume their outcomes but does not own those domains"
      ],
      "contract_ast_sha256": "eef29f9bb7436fbea461145303e205cc5432424d12089563eb93e279459e84d8",
      "contract_id": "P2C.C4.CONTRACT.EP-09-004",
      "criticality": "CRITICAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-09.md#26. Enterprise Design Principles > EP-09-004",
            "source_type": "SOURCE_LITERAL",
            "version": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910"
          },
          "identifier": "EP-09-004.EP-09-004.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-09-004.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-09.md",
            "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
            "source_lines": "L672-L675",
            "source_section": "26. Enterprise Design Principles > EP-09-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.EP-09-004.EP-09-004.EP-09-004.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "EP-09-004.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.FULFILLMENT_ID",
          "FIELD.DELIVERY_ID",
          "FIELD.RESPONSIBILITY_MAP",
          "FIELD.PRICING_CHANGES",
          "FIELD.PAYMENT_CHANGES",
          "FIELD.PROCUREMENT_CHANGES"
        ],
        "producer": "EP-09-004.EVIDENCE.PRODUCER",
        "required_collection_origin": "EP-09-004.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.FULFILLMENT_ID",
          "FIELD.DELIVERY_ID",
          "FIELD.RESPONSIBILITY_MAP",
          "FIELD.PRICING_CHANGES",
          "FIELD.PAYMENT_CHANGES",
          "FIELD.PROCUREMENT_CHANGES"
        ],
        "required_values_or_hashes": [
          "EP-09-004.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "EP-09-004.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "EP-09-004.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-B7AD4B5C5E9FF9E98F07",
        "P2C-C4-FX-2B8E24BB702AC22F093D",
        "P2C-C4-FX-0E898AB3E18E2A98F700"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Fulfillment changes pricing, payment or procurement decisions"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "EP-09-004-O001",
          "obligation_text": "Fulfillment chỉ chịu trách nhiệm Delivery"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "EP-09-004.O1.1.POLICY_OUTCOME_EQUALS"
          ],
          "coverage_count": 1,
          "obligation_id": "EP-09-004-O001"
        }
      ],
      "operator_composition": [
        "POLICY_OUTCOME_EQUALS"
      ],
      "positive_oracles": [
        "Fulfillment owns Delivery responsibility only"
      ],
      "preconditions": [
        "An Order requiring Delivery exists"
      ],
      "prohibitions": [
        "Fulfillment changes pricing, payment or procurement decisions"
      ],
      "requirement_id": "EP-09-004",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-09.md",
        "source_fingerprint": "157fb2cafe8eac357069087e65c1bb8fe92f3b7cbaa22985a10b9d91a12bc910",
        "source_lines": "L672-L675",
        "source_section": "26. Enterprise Design Principles > EP-09-004"
      },
      "source_statement": "Fulfillment chỉ chịu trách nhiệm Delivery.",
      "surrounding_source_context": "## EP-09-004\n\nFulfillment chỉ chịu trách nhiệm Delivery.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.EP-09-004",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "SEMANTIC_ACCEPTANCE_RENDERER_C2",
    "runtime_status": "RUNTIME_ADAPTER_PENDING"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "ACCEPTANCE_READY",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-004-AC001",
        "EP-09-004-AC002",
        "EP-09-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-09-004-O001",
      "obligation_text": "Fulfillment chỉ chịu trách nhiệm Delivery"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-09-004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-09-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-09-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-09-004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-09-004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-09-004 does not define a recovery obligation."
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
    "source_fingerprint": "5fb3404511f46f85a8b548d82a7e54dec421d79e2d0582087ec721cf27c7d44c",
    "source_lines": "L3862-L4840",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-09-004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-09-005",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "76223666708ca2da8a3302e9439e5b3e1998a2e5d5c67732be11997b93dc6765"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-005-AC001",
        "EP-09-005-AC002",
        "EP-09-005-AC003"
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
    "source_fingerprint": "76223666708ca2da8a3302e9439e5b3e1998a2e5d5c67732be11997b93dc6765",
    "source_lines": "L4842-L4921",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-09-005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-09-006",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "a373e4b12b3a17ee2220030378dd93476cc1a1fa64868d6ca685e35e9806d0fd"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-006-AC001",
        "EP-09-006-AC002",
        "EP-09-006-AC003"
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
    "source_fingerprint": "a373e4b12b3a17ee2220030378dd93476cc1a1fa64868d6ca685e35e9806d0fd",
    "source_lines": "L4923-L4998",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-09-006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-09-007",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "source_fingerprint": "b4f268222cd2f025c2578c8087d37d3454c40f140e695802736a7e91e576ff6f"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-09-007-AC001",
        "EP-09-007-AC002",
        "EP-09-007-AC003"
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
    "source_fingerprint": "b4f268222cd2f025c2578c8087d37d3454c40f140e695802736a7e91e576ff6f",
    "source_lines": "L5000-L5075",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-09-007"
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
