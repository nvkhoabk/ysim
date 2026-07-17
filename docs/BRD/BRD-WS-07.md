---
document_code: "BRD-WS-07"
document_id: "BRD-WS-07"
title: "Sales Order, Purchase Order, Cart & Checkout Model"
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

# BRD Workshop 07

# Sales Order, Purchase Order, Cart & Checkout Model

---

# 1. Workshop Objective

Workshop này xác định toàn bộ Transaction Entry của nền tảng YSim.

Workshop bao gồm:

- Cart
- Checkout
- Checkout Session
- Sales Order
- Purchase Order
- Procurement Validation
- Procurement Capacity
- Inventory Reservation
- Allocation Preparation
- Customer Checkout Decision

Workshop này chỉ mô tả quá trình từ Customer lựa chọn sản phẩm đến khi Payment hoàn tất.

Payment Gateway, Fulfillment và Settlement sẽ được mô tả ở các Workshop tiếp theo.

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| Cart | Transaction |
| Cart Item | Transaction |
| Checkout Session | Transaction |
| Checkout Snapshot | Transaction |
| Sales Order | Transaction |
| Sales Order Item | Transaction |
| Purchase Order | Transaction |
| Purchase Order Item | Transaction |
| Procurement Validation | Transaction |
| Procurement Capacity | Transaction |
| Inventory Reservation | Transaction |
| Customer Checkout Decision | Transaction |
| Fulfillment Assignment | Transaction |

---

# 3. Transaction Domain Principle

Transaction Domain của YSim được chia thành các giai đoạn độc lập.

```text
Cart
    │
    ▼
Checkout
    │
    ▼
Payment
    │
    ▼
Fulfillment
    │
    ▼
Settlement
    │
    ▼
After Sales
```

Mỗi Workshop chỉ chịu trách nhiệm một giai đoạn.

---

# 4. Order Taxonomy

YSim định nghĩa hai loại Order độc lập.

## Sales Order (SO)

Sales Order phát sinh từ các kênh bán hàng.

SO là giao dịch giữa:

Organization

↓

Customer

Sales Order quản lý:

- Product
- Quantity
- Customer
- Commercial Snapshot
- Promotion Snapshot
- Payment
- Fulfillment

---

## Purchase Order (PO)

Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier.

PO là giao dịch giữa:

YSim

↓

Supplier

Purchase Order quản lý:

- Supplier Product
- Quantity
- Cost
- Supplier Agreement
- Supplier Wallet
- Credit
- Procurement

PO không sử dụng Payment Gateway bán lẻ.

Việc thanh toán tuân theo Supplier Agreement.

---

# 5. Procurement Validation

Checkout bắt buộc thực hiện Procurement Validation.

Quy trình:

```text
Inventory Available?

├── YES
│      │
│      ▼
│ Reserve Inventory
│
└── NO
       │
       ▼
Supplier Product Available?
       │
Supplier API Available?
       │
Supplier Payment Capacity?
       │
Purchase Order Feasible?
       │
       ▼
Checkout Allowed
```

Nếu Procurement Validation thất bại:

Checkout không được phép tạo Sales Order.

---

# 6. Procurement Capacity

Procurement Capacity xác định khả năng tạo Purchase Order.

Bao gồm:

- Supplier Availability
- Supplier Product Mapping
- Supplier API Availability
- Supplier Wallet Balance
- Supplier Credit Limit
- Supplier Agreement

Nếu Supplier yêu cầu thanh toán đặt cọc nhưng Wallet không đủ:

Purchase Order mặc định thất bại.

Checkout phải dừng trước Payment.

---

# 7. Cart

Cart thuộc Storefront.

Một Storefront chỉ có một Cart.

Một Cart không chứa:

- nhiều Storefront
- nhiều Organization

Cart có thời hạn mặc định:

24 giờ.

Guest Checkout được hỗ trợ.

Identity sẽ Merge sau nếu cần.

---

# 8. Checkout Session

Checkout Session là Transaction Object độc lập.

Checkout Session lưu:

- Cart
- Customer
- Currency
- Promotion
- Commercial Snapshot
- Price Reservation
- Inventory Reservation
- Procurement Validation

Checkout Snapshot được tạo khi Customer bắt đầu Checkout.

---

# 9. Sales Order Creation

Sales Order được tạo theo Model C.

```text
Cart

↓

Checkout

↓

Validation

↓

Sales Order

↓

Payment
```

Validation bao gồm:

- Product
- Catalog
- Price
- Promotion
- Inventory
- Procurement Capacity

---

# 10. Customer Information

Version 2.0 chỉ bắt buộc:

Primary Email.

Các thông tin khác đều Optional:

- Customer Name
- Phone Number
- Passport
- Billing Address
- Shipping Address

Primary Email luôn nhận:

- Payment Confirmation
- Invoice

Nếu không khai báo Recipient khác thì Primary Email cũng nhận toàn bộ QR Code.

---

# 11. Multi-Customer Order

Một Sales Order có thể phục vụ nhiều Customer.

Customer có thể khai báo:

- Recipient Email
- Recipient Phone
- Recipient Name

cho từng nhóm Item.

Ví dụ:

```text
Thailand 5GB/day ×2

↓

Recipient A
Recipient B
```

Nếu số Recipient ít hơn số lượng Item:

các Item còn lại gửi về Primary Email.

---

# 12. Fulfillment Assignment

Fulfillment Assignment thuộc Fulfillment Domain.

Customer có thể:

- khai báo Recipient ngay khi Checkout
- hoặc bổ sung sau Payment Success

Fulfillment Assignment quản lý:

- Recipient
- Product Item
- QR Recipient

---

# 13. Inventory Reservation

Nếu Inventory có đủ Item.

Khi Customer bắt đầu Payment:

Item phải được Reserve.

Reservation Time:

10 phút.

```text
Available

↓

Reserved

↓

Payment Success

↓

Allocated
```

Nếu Payment thất bại:

```text
Reserved

↓

Released

↓

Available
```

---

# 14. Purchase Order Trigger

Checkout không tạo Purchase Order.

Checkout chỉ xác nhận:

Purchase Order Feasible.

Sau Payment Success:

```text
Payment Success

↓

Revalidate Supplier

↓

Create Purchase Order

↓

Receive Product Item

↓

Inventory

↓

Allocation

↓

Fulfillment
```

Email Payment Success chỉ bao gồm:

- Payment Confirmation
- Invoice

Email Fulfillment được gửi riêng sau khi hoàn tất Allocation và Fulfillment.

---

# 15. Purchase Order Policy

Purchase Order tự động:

- chỉ mua đúng số lượng còn thiếu
- chỉ mua đúng Product cần thiết

Nếu Inventory đã có Item phù hợp:

Inventory sẽ được Reserve trước.

Supplier Policy có thể cấu hình:

- Minimum Purchase Quantity

Mặc định:

Không áp dụng.

Bulk Procurement được xử lý ngoài luồng Sales Order.

---

# 16. Purchase Order Relationship

Một Sales Order có thể phát sinh nhiều Purchase Order.

Purchase Order tự động luôn tham chiếu Sales Order.

Purchase Order nhập kho chủ động không tham chiếu Sales Order.

Một Product Item chỉ Allocation cho một Sales Order Item.

Nếu:

- Fulfillment thất bại
- Customer Return
- Activation thất bại

Item sẽ chuyển sang:

Revoked Inventory.

---

# 17. Purchase Order Failure

Sau Payment Success nếu Purchase Order thất bại:

Allocation Engine:

- thử Supplier khác
- Retry Procurement

Nếu vẫn thất bại:

- Pause Fulfillment
- Notify Customer
- Retry theo chính sách
- Full Refund nếu cần

Version 2.0 không hỗ trợ Customer tự chọn Product thay thế.

---

# 18. Order Status

Order Status chỉ quản lý Transaction thương mại.

```text
Draft

↓

Checkout

↓

Pending Payment

↓

Payment Success

↓

Payment Failed

↓

Cancelled
```

Các trạng thái:

- Fulfillment
- Assignment
- Delivery

được quản lý riêng trong Fulfillment Domain.

---

# 19. Customer Checkout Decision

Customer Checkout Decision là Business Object.

Bao gồm:

- Accept New Price
- Continue Checkout
- Cancel Checkout

Customer Decision được Snapshot cùng Checkout.

---

# 20. Order Ownership

Order luôn thuộc:

Payment Owner.

Order vẫn lưu Attribution:

- Organization
- Storefront
- Tracking
- Campaign
- Sales User
- Distribution Path

---

# 21. Order Number

Order Number được sinh theo Payment Owner.

Ví dụ:

```text
ABC-20260710-000123
```

Ngoài ra hệ thống sinh:

Global Order ID

để phục vụ:

- Traceability
- Parent Support
- Customer Support
- Correlation giữa SO, PO, Payment và Fulfillment

---

# 22. Order Modification

Sau Payment Success.

Không cho phép sửa:

- Product
- Quantity
- Currency
- Promotion
- Price

Chỉ cho phép thay đổi:

- Recipient
- Recipient Email
- Phone
- IM
- Fulfillment Assignment

Mọi thay đổi đều phải Audit.

---

# 23. Deferred Scope

Version sau sẽ bổ sung:

- Cart Recovery
- Product Replacement Suggestion
- Split Payment
- Multiple Payment
- Smart Procurement
- AI Procurement
- Bulk Procurement Recommendation

---

# 24. Business Decisions (Locked)

## BD-07-001

Transaction Domain được chia thành:

Cart → Checkout → Payment → Fulfillment → Settlement → After Sales.

---

## BD-07-002

YSim hỗ trợ hai loại Order:

Sales Order và Purchase Order.

---

## BD-07-003

Checkout bắt buộc thực hiện Procurement Validation.

---

## BD-07-004

Procurement Capacity là điều kiện bắt buộc trước Payment.

---

## BD-07-005

Sales Order được tạo theo Model C.

---

## BD-07-006

Cart thuộc Storefront.

---

## BD-07-007

Một Cart không chứa nhiều Storefront hoặc nhiều Organization.

---

## BD-07-008

Checkout Session là Transaction Object.

---

## BD-07-009

Primary Email là thông tin bắt buộc duy nhất.

---

## BD-07-010

Fulfillment Assignment thuộc Fulfillment Domain.

---

## BD-07-011

Inventory phải Reserve trong thời gian Price Reservation.

---

## BD-07-012

Purchase Order tự động chỉ được tạo sau Payment Success.

---

## BD-07-013

Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu.

---

## BD-07-014

Một Sales Order có thể phát sinh nhiều Purchase Order.

---

## BD-07-015

Một Product Item chỉ Allocation cho một Sales Order Item.

---

## BD-07-016

Purchase Order thất bại phải Retry hoặc Refund.

---

## BD-07-017

Order thuộc Payment Owner.

---

## BD-07-018

Order Number theo Payment Owner và có Global Order ID.

---

## BD-07-019

Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion.

---

# 25. Enterprise Design Principles

## EP-07-001

Sales Order và Purchase Order là hai Business Object độc lập.

---

## EP-07-002

Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement.

---

## EP-07-003

Inventory Reservation phải đồng bộ với Price Reservation.

---

## EP-07-004

Fulfillment Assignment là Capability của Fulfillment Domain.

---

## EP-07-005

Mọi Product Item phải truy vết được:

Purchase Order

↓

Inventory

↓

Allocation

↓

Sales Order

↓

Customer

---

## EP-07-006

Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot.

---

# 26. Traceability

Workshop này kế thừa:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04
- BRD-WS-05
- BRD-WS-06

---

# 27. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Payment Engine
- Procurement Engine
- Inventory Domain
- Allocation Engine
- Fulfillment Engine
- Settlement Engine
- Customer Portal
- Customer Support
- Reporting
- API
- DMS
- DBD

---

# 28. Workshop Status

**Status:** FROZEN

Workshop này là Foundation cho:

- Payment Engine
- Procurement Engine
- Allocation Engine
- Fulfillment Engine
- Settlement Engine

---

# 29. Next Workshop

**BRD-WS-08 – Payment, Payment Gateway & Payment Lifecycle**

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-001 — Transaction Domain được chia thành: Cart → Checkout → Payment → Fulfillment → Settlement → After…

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
      "requirement_id": "BD-07-001",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "66ded58274b87b6dbcda83a881ebbe1199ff6dd9fdba65c69b85b523ee0ba8e2"
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
        "BD-07-001-AC001",
        "BD-07-001-AC002",
        "BD-07-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-001-O001",
      "obligation_text": "Transaction Domain được chia thành: Cart → Checkout → Payment → Fulfillment → Settlement → After Sales"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-001 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-001-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-001-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-001 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Transaction Domain được chia thành: Cart → Checkout → Payment → Fulfillment → Settlement → After Sales.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-001",
    "source_context_sha256": "f55c126003d54a46c1908072a1ebd8456945bcea7a3397190657e3625817e435",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "66ded58274b87b6dbcda83a881ebbe1199ff6dd9fdba65c69b85b523ee0ba8e2",
    "source_lines": "L873-L981",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-001"
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
  "stable_id": "BD-07-001",
  "title": "Transaction Domain được chia thành: Cart → Checkout → Payment → Fulfillment → Settlement → After…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-002 — YSim hỗ trợ hai loại Order: Sales Order và Purchase Order

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
      "requirement_id": "BD-07-002",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "ea1a73913f575ddb18b5ecae5ef3ee7495b4e26880bc7893de8643cdee7202d3"
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
        "BD-07-002-AC001",
        "BD-07-002-AC002",
        "BD-07-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-002-O001",
      "obligation_text": "YSim hỗ trợ hai loại Order: Sales Order và Purchase Order"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "YSim hỗ trợ hai loại Order: Sales Order và Purchase Order.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-002",
    "source_context_sha256": "f57aa293dc490be17c8e6d709ee8978e1dcbe167d3c8a88587268ae5c8fd9e73",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "ea1a73913f575ddb18b5ecae5ef3ee7495b4e26880bc7893de8643cdee7202d3",
    "source_lines": "L983-L1058",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-002"
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
  "stable_id": "BD-07-002",
  "title": "YSim hỗ trợ hai loại Order: Sales Order và Purchase Order",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-003 — Checkout bắt buộc thực hiện Procurement Validation

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
      "requirement_id": "BD-07-003",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "dc609219ad83379b52299679772fd5c100a6fed884eb04d4d9dd910f5a16d8bf"
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
        "BD-07-003-AC001",
        "BD-07-003-AC002",
        "BD-07-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-003-O001",
      "obligation_text": "Checkout bắt buộc thực hiện Procurement Validation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-003 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Checkout bắt buộc thực hiện Procurement Validation.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Procurement Validation",
    "source_context_sha256": "09c4c12b18c53c171fc8599edfe49f3d037b8d9d3d2ed38dd6fa1aea530c77d4",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "dc609219ad83379b52299679772fd5c100a6fed884eb04d4d9dd910f5a16d8bf",
    "source_lines": "L1060-L1168",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-003"
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
  "stable_id": "BD-07-003",
  "title": "Checkout bắt buộc thực hiện Procurement Validation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-004 — Procurement Capacity là điều kiện bắt buộc trước Payment

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
      "requirement_id": "BD-07-004",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "3a4b3876fe8b6886f5e59b26b89bc6634aaa774d134cd145320ea72d59e1b330"
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
        "BD-07-004-AC001",
        "BD-07-004-AC002",
        "BD-07-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-004-O001",
      "obligation_text": "Procurement Capacity là điều kiện bắt buộc trước Payment"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Procurement Capacity là điều kiện bắt buộc trước Payment.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-004",
    "source_context_sha256": "42031d70708f17ac2f3044a3956da0f5cb43373d4d08a5806411eb6ca1d8f32c",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "3a4b3876fe8b6886f5e59b26b89bc6634aaa774d134cd145320ea72d59e1b330",
    "source_lines": "L1170-L1278",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-004"
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
  "stable_id": "BD-07-004",
  "title": "Procurement Capacity là điều kiện bắt buộc trước Payment",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-005 — Sales Order được tạo theo Model C

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
      "requirement_id": "BD-07-005",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "c21ee8b269768b7f5c3136cbd27de33ee0c53add93e0717f03bd36194bb5ca5c"
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
        "BD-07-005-AC001",
        "BD-07-005-AC002",
        "BD-07-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-005-O001",
      "obligation_text": "Sales Order được tạo theo Model C"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sales Order được tạo theo Model C.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Sales Order Creation",
    "source_context_sha256": "624524de6957658198a8cceb53f2481b15e4ecf33adebe8bd487aa6a8fef894a",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "c21ee8b269768b7f5c3136cbd27de33ee0c53add93e0717f03bd36194bb5ca5c",
    "source_lines": "L1280-L1355",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-005"
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
  "stable_id": "BD-07-005",
  "title": "Sales Order được tạo theo Model C",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-006 — Cart thuộc Storefront

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
      "requirement_id": "BD-07-006",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "50f93242011435757555916f7c825f5273a8cbee5566c6d4ab55e50723555bfe"
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
        "BD-07-006-AC001",
        "BD-07-006-AC002",
        "BD-07-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-006-O001",
      "obligation_text": "Cart thuộc Storefront"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Cart thuộc Storefront.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Cart",
    "source_context_sha256": "2a151fb191691fafb4e40db77d2d6f250971c287d9e8919cf434118d7c4a60f4",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "50f93242011435757555916f7c825f5273a8cbee5566c6d4ab55e50723555bfe",
    "source_lines": "L1357-L1432",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-006"
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
  "stable_id": "BD-07-006",
  "title": "Cart thuộc Storefront",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-007 — Một Cart không chứa nhiều Storefront hoặc nhiều Organization

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "An empty Cart acquires scope from its first item; later items must match it"
    ],
    "concrete_bindings": [
      {
        "actor_tenant": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
            "source_type": "SOURCE_LITERAL",
            "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
          },
          "identifier": "BD-07-007.ACTOR_TENANT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.ACTOR_TENANT.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
            "source_lines": "L674-L677",
            "source_section": "24. Business Decisions (Locked) > BD-07-007"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "TENANT_ID",
            "resolver_id": "RESOLVE.BD-07-007.BD-07-007.ACTOR_TENANT",
            "version": "1.0.0"
          },
          "semantic_type": "TENANT_ID"
        },
        "permission_context": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
            "source_type": "SOURCE_LITERAL",
            "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
          },
          "identifier": "BD-07-007.PERMISSION_CONTEXT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.PERMISSION_CONTEXT.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
            "source_lines": "L674-L677",
            "source_section": "24. Business Decisions (Locked) > BD-07-007"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BD-07-007.BD-07-007.PERMISSION_CONTEXT",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "resource_tenant": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
            "source_type": "SOURCE_LITERAL",
            "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
          },
          "identifier": "BD-07-007.RESOURCE_TENANT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.RESOURCE_TENANT.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
            "source_lines": "L674-L677",
            "source_section": "24. Business Decisions (Locked) > BD-07-007"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "TENANT_ID",
            "resolver_id": "RESOLVE.BD-07-007.BD-07-007.RESOURCE_TENANT",
            "version": "1.0.0"
          },
          "semantic_type": "TENANT_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BD-07-007",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "An item from another Storefront or Organization is added to the Cart"
    ],
    "operator_composition": [
      "TENANT_ISOLATED"
    ],
    "positive_oracle": [
      "Every Cart contains items from exactly one Storefront and one Organization"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
      "source_lines": "L674-L677",
      "source_section": "24. Business Decisions (Locked) > BD-07-007"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
          "source_type": "SOURCE_LITERAL",
          "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
        },
        "identifier": "BD-07-007.BD-07-007.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BD-07-007.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-07.md",
          "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
          "source_lines": "L674-L677",
          "source_section": "24. Business Decisions (Locked) > BD-07-007"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BD-07-007.BD-07-007.BD-07-007.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BD-07-007.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.CART_ID",
        "FIELD.CART_STOREFRONT_ID",
        "FIELD.CART_ORGANIZATION_ID",
        "FIELD.ITEM_STOREFRONT_ID",
        "FIELD.ITEM_ORGANIZATION_ID",
        "FIELD.ADD_RESULT"
      ],
      "producer": "BD-07-007.EVIDENCE.PRODUCER",
      "required_collection_origin": "BD-07-007.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.CART_ID",
        "FIELD.CART_STOREFRONT_ID",
        "FIELD.CART_ORGANIZATION_ID",
        "FIELD.ITEM_STOREFRONT_ID",
        "FIELD.ITEM_ORGANIZATION_ID",
        "FIELD.ADD_RESULT"
      ],
      "required_values_or_hashes": [
        "BD-07-007.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BD-07-007.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BD-07-007.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BD-07-007-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BD-07-007.O1.1.TENANT_ISOLATED",
          "evaluator_consumed_bindings": [
            "actor_tenant",
            "permission_context",
            "resource_tenant"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
              "source_type": "SOURCE_LITERAL",
              "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
            },
            "identifier": "BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
              "source_lines": "L674-L677",
              "source_section": "24. Business Decisions (Locked) > BD-07-007"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-07-007.BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
              "source_type": "SOURCE_LITERAL",
              "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
            },
            "identifier": "BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
              "source_lines": "L674-L677",
              "source_section": "24. Business Decisions (Locked) > BD-07-007"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "TENANT_ID",
              "resolver_id": "RESOLVE.BD-07-007.BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "TENANT_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actor_tenant": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
                  "source_type": "SOURCE_LITERAL",
                  "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
                },
                "identifier": "BD-07-007.ACTOR_TENANT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.ACTOR_TENANT.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
                  "source_lines": "L674-L677",
                  "source_section": "24. Business Decisions (Locked) > BD-07-007"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "TENANT_ID",
                  "resolver_id": "RESOLVE.BD-07-007.BD-07-007.ACTOR_TENANT",
                  "version": "1.0.0"
                },
                "semantic_type": "TENANT_ID"
              },
              "permission_context": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
                  "source_type": "SOURCE_LITERAL",
                  "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
                },
                "identifier": "BD-07-007.PERMISSION_CONTEXT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.PERMISSION_CONTEXT.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
                  "source_lines": "L674-L677",
                  "source_section": "24. Business Decisions (Locked) > BD-07-007"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BD-07-007.BD-07-007.PERMISSION_CONTEXT",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "resource_tenant": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
                  "source_type": "SOURCE_LITERAL",
                  "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
                },
                "identifier": "BD-07-007.RESOURCE_TENANT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.RESOURCE_TENANT.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
                  "source_lines": "L674-L677",
                  "source_section": "24. Business Decisions (Locked) > BD-07-007"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "TENANT_ID",
                  "resolver_id": "RESOLVE.BD-07-007.BD-07-007.RESOURCE_TENANT",
                  "version": "1.0.0"
                },
                "semantic_type": "TENANT_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
                  "source_type": "SOURCE_LITERAL",
                  "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
                },
                "identifier": "BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
                  "source_lines": "L674-L677",
                  "source_section": "24. Business Decisions (Locked) > BD-07-007"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "TENANT_ID",
                  "resolver_id": "RESOLVE.BD-07-007.BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "TENANT_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
                  "source_type": "SOURCE_LITERAL",
                  "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
                },
                "identifier": "BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
                  "source_lines": "L674-L677",
                  "source_section": "24. Business Decisions (Locked) > BD-07-007"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "TENANT_ID",
                  "resolver_id": "OBSERVE.BD-07-007.BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "TENANT_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
                "source_type": "SOURCE_LITERAL",
                "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
              },
              "identifier": "BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
                "source_lines": "L674-L677",
                "source_section": "24. Business Decisions (Locked) > BD-07-007"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-07-007.BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "TENANT_ISOLATED"
          },
          "obligation_id": "BD-07-007-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
              "source_type": "SOURCE_LITERAL",
              "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
            },
            "identifier": "BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
              "source_lines": "L674-L677",
              "source_section": "24. Business Decisions (Locked) > BD-07-007"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "TENANT_ID",
              "resolver_id": "OBSERVE.BD-07-007.BD-07-007.BD-07-007.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "TENANT_ID"
          },
          "operator_id": "TENANT_ISOLATED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actor_tenant": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
                "source_type": "SOURCE_LITERAL",
                "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
              },
              "identifier": "BD-07-007.ACTOR_TENANT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.ACTOR_TENANT.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
                "source_lines": "L674-L677",
                "source_section": "24. Business Decisions (Locked) > BD-07-007"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "TENANT_ID",
                "resolver_id": "RESOLVE.BD-07-007.BD-07-007.ACTOR_TENANT",
                "version": "1.0.0"
              },
              "semantic_type": "TENANT_ID"
            },
            "permission_context": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
                "source_type": "SOURCE_LITERAL",
                "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
              },
              "identifier": "BD-07-007.PERMISSION_CONTEXT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.PERMISSION_CONTEXT.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
                "source_lines": "L674-L677",
                "source_section": "24. Business Decisions (Locked) > BD-07-007"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BD-07-007.BD-07-007.PERMISSION_CONTEXT",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "resource_tenant": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
                "source_type": "SOURCE_LITERAL",
                "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
              },
              "identifier": "BD-07-007.RESOURCE_TENANT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-07-007.O1.1.TENANT_ISOLATED.RESOURCE_TENANT.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
                "source_lines": "L674-L677",
                "source_section": "24. Business Decisions (Locked) > BD-07-007"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "TENANT_ID",
                "resolver_id": "RESOLVE.BD-07-007.BD-07-007.RESOURCE_TENANT",
                "version": "1.0.0"
              },
              "semantic_type": "TENANT_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "An empty Cart acquires scope from its first item; later items must match it"
      ],
      "contract_ast_sha256": "abb321d7c7d8a71a683950fe1ebaf3d80630de4fb995c5149f95fec7e775220f",
      "contract_id": "P2C.C4.CONTRACT.BD-07-007",
      "criticality": "HIGH",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#24. Business Decisions (Locked) > BD-07-007",
            "source_type": "SOURCE_LITERAL",
            "version": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b"
          },
          "identifier": "BD-07-007.BD-07-007.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-07-007.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
            "source_lines": "L674-L677",
            "source_section": "24. Business Decisions (Locked) > BD-07-007"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BD-07-007.BD-07-007.BD-07-007.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BD-07-007.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.CART_ID",
          "FIELD.CART_STOREFRONT_ID",
          "FIELD.CART_ORGANIZATION_ID",
          "FIELD.ITEM_STOREFRONT_ID",
          "FIELD.ITEM_ORGANIZATION_ID",
          "FIELD.ADD_RESULT"
        ],
        "producer": "BD-07-007.EVIDENCE.PRODUCER",
        "required_collection_origin": "BD-07-007.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.CART_ID",
          "FIELD.CART_STOREFRONT_ID",
          "FIELD.CART_ORGANIZATION_ID",
          "FIELD.ITEM_STOREFRONT_ID",
          "FIELD.ITEM_ORGANIZATION_ID",
          "FIELD.ADD_RESULT"
        ],
        "required_values_or_hashes": [
          "BD-07-007.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BD-07-007.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BD-07-007.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-93F45BDB432E139AFBAC",
        "P2C-C4-FX-86011B09FB2530F0B7D5",
        "P2C-C4-FX-944B2EBB0705126827BC"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "An item from another Storefront or Organization is added to the Cart"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-07-007-O001",
          "obligation_text": "Một Cart không chứa nhiều Storefront hoặc nhiều Organization"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BD-07-007.O1.1.TENANT_ISOLATED"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-07-007-O001"
        }
      ],
      "operator_composition": [
        "TENANT_ISOLATED"
      ],
      "positive_oracles": [
        "Every Cart contains items from exactly one Storefront and one Organization"
      ],
      "preconditions": [
        "The Cart has either no existing scope or an established Storefront and Organization scope"
      ],
      "prohibitions": [
        "An item from another Storefront or Organization is added to the Cart"
      ],
      "requirement_id": "BD-07-007",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-07.md",
        "source_fingerprint": "8d40324803774a9fa5453d41b96cc7e7f8e053a110ec39e46ff530209bad489b",
        "source_lines": "L674-L677",
        "source_section": "24. Business Decisions (Locked) > BD-07-007"
      },
      "source_statement": "Một Cart không chứa nhiều Storefront hoặc nhiều Organization.",
      "surrounding_source_context": "## BD-07-007\n\nMột Cart không chứa nhiều Storefront hoặc nhiều Organization.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BD-07-007",
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
        "BD-07-007-AC001",
        "BD-07-007-AC002",
        "BD-07-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-007-O001",
      "obligation_text": "Một Cart không chứa nhiều Storefront hoặc nhiều Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Cart không chứa nhiều Storefront hoặc nhiều Organization.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-007",
    "source_context_sha256": "641b50baca17f20a8ba90584976733d544da7163dd06423ead58544fbbd55886",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "0110d6937c9da8a0e44a9be08ac99e7b7808fd1129c061b139c64884f66d4ed8",
    "source_lines": "L1434-L2255",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-007"
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
  "stable_id": "BD-07-007",
  "title": "Một Cart không chứa nhiều Storefront hoặc nhiều Organization",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-008 — Checkout Session là Transaction Object

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
      "requirement_id": "BD-07-008",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "3a051e4cca2dd911be4b9ae9e683d78d3da1b25d3927d4c2ec3091e9ae354ccd"
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
        "BD-07-008-AC001",
        "BD-07-008-AC002",
        "BD-07-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-008-O001",
      "obligation_text": "Checkout Session là Transaction Object"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-008 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-008-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-008-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-008 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Checkout Session là Transaction Object.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-008",
    "source_context_sha256": "9073362e8b562486591e323893b814c9ba69f0f5a9d9bf3cd6b7cf6175daab40",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "3a051e4cca2dd911be4b9ae9e683d78d3da1b25d3927d4c2ec3091e9ae354ccd",
    "source_lines": "L2257-L2365",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-008"
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
  "stable_id": "BD-07-008",
  "title": "Checkout Session là Transaction Object",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-009 — Primary Email là thông tin bắt buộc duy nhất

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
      "requirement_id": "BD-07-009",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "39da3678e95a3e275d20f601d75c1a9e9c3c132ef16e9a74162f46cce33278ab"
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
        "BD-07-009-AC001",
        "BD-07-009-AC002",
        "BD-07-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-009-O001",
      "obligation_text": "Primary Email là thông tin bắt buộc duy nhất"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Primary Email là thông tin bắt buộc duy nhất.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-009",
    "source_context_sha256": "6a3390d9c17001b62049679973aaa8dc641d3eb93cf24771854c34a18fa9c760",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "39da3678e95a3e275d20f601d75c1a9e9c3c132ef16e9a74162f46cce33278ab",
    "source_lines": "L2367-L2442",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-009"
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
  "stable_id": "BD-07-009",
  "title": "Primary Email là thông tin bắt buộc duy nhất",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-010 — Fulfillment Assignment thuộc Fulfillment Domain

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
      "requirement_id": "BD-07-010",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "820559f41d0b969c150f757992ad156a7c4d15601a828de3790d1f8290074f82"
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
        "BD-07-010-AC001",
        "BD-07-010-AC002",
        "BD-07-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-010-O001",
      "obligation_text": "Fulfillment Assignment thuộc Fulfillment Domain"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-010 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-010 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-010 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-010-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-010-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-010 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Fulfillment Assignment thuộc Fulfillment Domain.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Fulfillment Assignment",
    "source_context_sha256": "b6744f15982bd28e9762c6bf762966254e5010984bb08088f1173cbe88b80053",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "820559f41d0b969c150f757992ad156a7c4d15601a828de3790d1f8290074f82",
    "source_lines": "L2444-L2552",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-010"
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
  "stable_id": "BD-07-010",
  "title": "Fulfillment Assignment thuộc Fulfillment Domain",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-011 — Inventory phải Reserve trong thời gian Price Reservation

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
      "requirement_id": "BD-07-011",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "5866c67964e94f593db7fcece08128a85a952bd407553f0f816f39b4cdd6eeff"
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
        "BD-07-011-AC001",
        "BD-07-011-AC002",
        "BD-07-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-011-O001",
      "obligation_text": "Inventory phải Reserve trong thời gian Price Reservation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-011 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-011 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-011 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-011-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-011-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-011 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Inventory phải Reserve trong thời gian Price Reservation.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-011",
    "source_context_sha256": "e8b3dfc40f5b4f3c5c08ff1287f36d0a5fa531bc48f29478c4e000b68c69b524",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "5866c67964e94f593db7fcece08128a85a952bd407553f0f816f39b4cdd6eeff",
    "source_lines": "L2554-L2662",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-011"
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
  "stable_id": "BD-07-011",
  "title": "Inventory phải Reserve trong thời gian Price Reservation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-012 — Purchase Order tự động chỉ được tạo sau Payment Success

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
      "requirement_id": "BD-07-012",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "25aa8b7b86a734679adc25a9ec6fb293769750750bdec1d168cf9882a0d86da6"
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
        "BD-07-012-AC001",
        "BD-07-012-AC002",
        "BD-07-012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-012-O001",
      "obligation_text": "Purchase Order tự động chỉ được tạo sau Payment Success"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-012 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-012-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-012-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-012 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order tự động chỉ được tạo sau Payment Success.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-012",
    "source_context_sha256": "186d8cfc286f0ca9174a147e67f07e845c03df1cc4a910a0974f71fb622075e5",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "25aa8b7b86a734679adc25a9ec6fb293769750750bdec1d168cf9882a0d86da6",
    "source_lines": "L2664-L2772",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-012"
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
  "stable_id": "BD-07-012",
  "title": "Purchase Order tự động chỉ được tạo sau Payment Success",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-013 — Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu

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
      "requirement_id": "BD-07-013",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "0b531f36ebc122686092a2870a4aa2e3bed3d1d942540254ac6d9d7d8aa82800"
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
        "BD-07-013-AC001",
        "BD-07-013-AC002",
        "BD-07-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-013-O001",
      "obligation_text": "Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-013",
    "source_context_sha256": "6f2e785196aa5d64ddc0de5a684d47ca3b1515cee843311238a53c8ff8c7adcc",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "0b531f36ebc122686092a2870a4aa2e3bed3d1d942540254ac6d9d7d8aa82800",
    "source_lines": "L2774-L2849",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-013"
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
  "stable_id": "BD-07-013",
  "title": "Purchase Order chỉ mua đúng số lượng và chủng loại còn thiếu",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-014 — Một Sales Order có thể phát sinh nhiều Purchase Order

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-002",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-07-014",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "88393717ead21e6bd1a8a42895d633f63ead2783a7b00837905b8b49cd5853f5"
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
        "BD-07-014-AC001",
        "BD-07-014-AC002",
        "BD-07-014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-014-O001",
      "obligation_text": "Một Sales Order có thể phát sinh nhiều Purchase Order"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Sales Order có thể phát sinh nhiều Purchase Order.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Purchase Order Relationship",
    "source_context_sha256": "377ba4c9e2d7228a57bd381962536a997d53127ff0180913ea416eff141893e5",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "88393717ead21e6bd1a8a42895d633f63ead2783a7b00837905b8b49cd5853f5",
    "source_lines": "L2851-L2930",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-014"
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
  "stable_id": "BD-07-014",
  "title": "Một Sales Order có thể phát sinh nhiều Purchase Order",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-015 — Một Product Item chỉ Allocation cho một Sales Order Item

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
      "requirement_id": "BD-07-015",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "352413019e91e7a31269f795bb96b237746bba42764117b9fac878ecb8ea064b"
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
        "BD-07-015-AC001",
        "BD-07-015-AC002",
        "BD-07-015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-015-O001",
      "obligation_text": "Một Product Item chỉ Allocation cho một Sales Order Item"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-015 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-015 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-015 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-015-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-015-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-015 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Product Item chỉ Allocation cho một Sales Order Item.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Purchase Order Relationship",
    "source_context_sha256": "377ba4c9e2d7228a57bd381962536a997d53127ff0180913ea416eff141893e5",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "352413019e91e7a31269f795bb96b237746bba42764117b9fac878ecb8ea064b",
    "source_lines": "L2932-L3044",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-015"
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
  "stable_id": "BD-07-015",
  "title": "Một Product Item chỉ Allocation cho một Sales Order Item",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-016 — Purchase Order thất bại phải Retry hoặc Refund

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
      "requirement_id": "BD-07-016",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "b7767d7f21efc7c7ca860e1d748a62f2a68122c9249baeae81d51284edab9757"
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
        "BD-07-016-AC001",
        "BD-07-016-AC002",
        "BD-07-016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-016-O001",
      "obligation_text": "Purchase Order thất bại phải Retry hoặc Refund"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-016 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-016 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-016 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-016-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-016-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-016 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order thất bại phải Retry hoặc Refund.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-016",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-016",
    "source_context_sha256": "9b6445cc64f07e51e624c5ae68dd08a37cf04bc15311452afbebe06d369de504",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "b7767d7f21efc7c7ca860e1d748a62f2a68122c9249baeae81d51284edab9757",
    "source_lines": "L3046-L3158",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-016"
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
  "stable_id": "BD-07-016",
  "title": "Purchase Order thất bại phải Retry hoặc Refund",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-017 — Order thuộc Payment Owner

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
      "requirement_id": "BD-07-017",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "be6a310e00ee40e1198e906981b354b149a032e2b94e29256e2c4d76dd254bc2"
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
        "BD-07-017-AC001",
        "BD-07-017-AC002",
        "BD-07-017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-017-O001",
      "obligation_text": "Order thuộc Payment Owner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-017 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-017 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-017 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-017-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-017-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-017 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Order thuộc Payment Owner.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-017",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-017",
    "source_context_sha256": "2963e59c01909323da4f306a54f027b70c0f8a7d949a0ef91af6697375134422",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "be6a310e00ee40e1198e906981b354b149a032e2b94e29256e2c4d76dd254bc2",
    "source_lines": "L3160-L3268",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-017"
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
  "stable_id": "BD-07-017",
  "title": "Order thuộc Payment Owner",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-018 — Order Number theo Payment Owner và có Global Order ID

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
      "requirement_id": "BD-07-018",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "b9e8bac5e3d5a115b9d74a9304c4a4b37a6e45d8ba704d7435d1e1a990d46a24"
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
        "BD-07-018-AC001",
        "BD-07-018-AC002",
        "BD-07-018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-018-O001",
      "obligation_text": "Order Number theo Payment Owner và có Global Order ID"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-018 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-018 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-018 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-018-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-018-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-018 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Order Number theo Payment Owner và có Global Order ID.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-018",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-018",
    "source_context_sha256": "f7a1d74628316c68b965e40e20ab56945b52d32b76608251bb5348c282ed47d2",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "b9e8bac5e3d5a115b9d74a9304c4a4b37a6e45d8ba704d7435d1e1a990d46a24",
    "source_lines": "L3270-L3378",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-018"
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
  "stable_id": "BD-07-018",
  "title": "Order Number theo Payment Owner và có Global Order ID",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-07-019 — Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion

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
      "requirement_id": "BD-07-019",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "38b121bac5221972f2ab22567e8120d4a488561ea574e0fe2f4a7af494c06171"
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
        "BD-07-019-AC001",
        "BD-07-019-AC002",
        "BD-07-019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-07-019-O001",
      "obligation_text": "Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-019 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-019 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-019 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-019-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-07-019-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-07-019 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-07-019",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-07-019",
    "source_context_sha256": "79fc47e444f6e6689180d34eb1db9c51a3cb3fccf574d75dbc8284bd86c806c5",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "38b121bac5221972f2ab22567e8120d4a488561ea574e0fe2f4a7af494c06171",
    "source_lines": "L3380-L3488",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-07-019"
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
  "stable_id": "BD-07-019",
  "title": "Sau Payment Success không được sửa Product, Quantity, Price hoặc Promotion",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R001 — Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier

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
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-009",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-07-R001",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "4ae91cbfa4c2c8ebb02387696a7ef83a2cd450667aa188ce91acb9a8d04465bd"
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
        "BRD-WS-07-R001-AC001",
        "BRD-WS-07-R001-AC002",
        "BRD-WS-07-R001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R001-O001",
      "obligation_text": "Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R001 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R001-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R001-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R001 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-001",
    "previous_temporary_key": "TMP-BRD-WS-07-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "Purchase Order (PO)",
    "source_context_sha256": "8ba73bf3d27037bd42689497e98ff67a2b9470c09a4a610cb51ef2aeeaefe7fc",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "4ae91cbfa4c2c8ebb02387696a7ef83a2cd450667aa188ce91acb9a8d04465bd",
    "source_lines": "L3490-L3606",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R001"
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
  "stable_id": "BRD-WS-07-R001",
  "title": "Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R003 — Nếu Procurement Validation thất bại: Checkout không được phép tạo Sales Order

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
      "requirement_id": "BRD-WS-07-R003",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "ebe4171ef9805a1be78ae846d995d6fd9973155be793be9b8ece74183a8490a6"
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
        "BRD-WS-07-R003-AC001",
        "BRD-WS-07-R003-AC002",
        "BRD-WS-07-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R003-O001",
      "obligation_text": "Nếu Procurement Validation thất bại: Checkout không được phép tạo Sales Order"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R003 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu Procurement Validation thất bại: Checkout không được phép tạo Sales Order.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-003",
    "previous_temporary_key": "TMP-BRD-WS-07-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Procurement Validation",
    "source_context_sha256": "09c4c12b18c53c171fc8599edfe49f3d037b8d9d3d2ed38dd6fa1aea530c77d4",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "ebe4171ef9805a1be78ae846d995d6fd9973155be793be9b8ece74183a8490a6",
    "source_lines": "L3608-L3716",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R003"
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
  "stable_id": "BRD-WS-07-R003",
  "title": "Nếu Procurement Validation thất bại: Checkout không được phép tạo Sales Order",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R004 — Checkout phải dừng trước Payment

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
      "requirement_id": "BRD-WS-07-R004",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "815f09d2cfcb8171193d305d65651ad4ac51cf1d9f1f06b6babc7d2063146195"
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
        "BRD-WS-07-R004-AC001",
        "BRD-WS-07-R004-AC002",
        "BRD-WS-07-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R004-O001",
      "obligation_text": "Checkout phải dừng trước Payment"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Checkout phải dừng trước Payment.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-004",
    "previous_temporary_key": "TMP-BRD-WS-07-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Procurement Capacity",
    "source_context_sha256": "3d367e8860d74f1845736db291a02eb92c963f21a84005208567253d9048adca",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "815f09d2cfcb8171193d305d65651ad4ac51cf1d9f1f06b6babc7d2063146195",
    "source_lines": "L3718-L3826",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R004"
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
  "stable_id": "BRD-WS-07-R004",
  "title": "Checkout phải dừng trước Payment",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R005 — Identity sẽ Merge sau nếu cần

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Potential matches may remain unmerged; approved merge produces traceable canonical linkage"
    ],
    "concrete_bindings": [
      {
        "action": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.ACTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.ACTION.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.ACTION",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        },
        "approval_policy": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.APPROVAL_POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.APPROVAL_POLICY.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.APPROVAL_POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "approval_reference": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.APPROVAL_REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.APPROVAL_REFERENCE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "APPROVAL_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.APPROVAL_REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "APPROVAL_ID"
        }
      },
      {
        "from_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-07-R005.FROM_STATE"
            ],
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.FROM_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.FROM_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "state_machine": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.STATE_MACHINE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_MACHINE_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.STATE_MACHINE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_MACHINE_ID"
        },
        "to_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-07-R005.TO_STATE"
            ],
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.TO_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.TO_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "trigger": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.TRIGGER",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.TRIGGER",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        }
      },
      {
        "after_hash": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.AFTER_HASH",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.AFTER_HASH.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "HASH",
            "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.AFTER_HASH",
            "version": "1.0.0"
          },
          "semantic_type": "HASH"
        },
        "audit_record": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.AUDIT_RECORD",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.AUDIT_RECORD.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.AUDIT_RECORD",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "before_hash": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.BEFORE_HASH",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.BEFORE_HASH.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "HASH",
            "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.BEFORE_HASH",
            "version": "1.0.0"
          },
          "semantic_type": "HASH"
        },
        "immutability_boundary": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.IMMUTABILITY_BOUNDARY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.IMMUTABILITY_BOUNDARY.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.IMMUTABILITY_BOUNDARY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "protected_fields": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.CANDIDATE_IDENTITY_IDS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.1",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.CANDIDATE_IDENTITY_IDS",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.MATCH_EVIDENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.2",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MATCH_EVIDENCE",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.MERGE_POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.3",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.AUTHORIZATION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.4",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUTHORIZATION",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.MERGE_RESULT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.5",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_RESULT",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.AUDIT_RECORD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.6",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUDIT_RECORD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "semantic_type": "SET_OF<FIELD_ID>"
        },
        "required_fields": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.CANDIDATE_IDENTITY_IDS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.CANDIDATE_IDENTITY_IDS",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.MATCH_EVIDENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MATCH_EVIDENCE",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.MERGE_POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.AUTHORIZATION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUTHORIZATION",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.MERGE_RESULT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.5",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_RESULT",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.AUDIT_RECORD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.6",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUDIT_RECORD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "semantic_type": "SET_OF<FIELD_ID>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R005",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Records are automatically merged without need, policy or authorization"
    ],
    "operator_composition": [
      "APPROVAL_REQUIRED",
      "STATE_TRANSITION_ALLOWED",
      "AUDIT_IMMUTABLE"
    ],
    "positive_oracle": [
      "Identity records remain separate until a governed merge is executed"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
        "P2-DEC-008"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
      "source_lines": "L219",
      "source_section": "7. Cart"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
          "source_type": "APPROVED_DECISION",
          "version": "2026-07-16"
        },
        "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-07-R005.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "P2-DEC-008"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-07.md",
          "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
          "source_lines": "L219",
          "source_section": "7. Cart"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-07-R005.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.CANDIDATE_IDENTITY_IDS",
        "FIELD.MATCH_EVIDENCE",
        "FIELD.MERGE_POLICY",
        "FIELD.AUTHORIZATION",
        "FIELD.MERGE_RESULT",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "BRD-WS-07-R005.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-07-R005.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.CANDIDATE_IDENTITY_IDS",
        "FIELD.MATCH_EVIDENCE",
        "FIELD.MERGE_POLICY",
        "FIELD.AUTHORIZATION",
        "FIELD.MERGE_RESULT",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "BRD-WS-07-R005.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-07-R005.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-07-R005.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-07-R005-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": {
        "meaning": "Identity Merge uses an authorized Merge Proposal lifecycle with retained lineage and immutable audit evidence.",
        "non_inferences": [
          "No automatic merge threshold is inferred.",
          "No legal ownership, tenant scope or permission transfer is inferred."
        ],
        "option_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1"
      },
      "assertions": [
        {
          "assertion_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED",
          "evaluator_consumed_bindings": [
            "action",
            "approval_policy",
            "approval_reference"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
              "source_lines": "L219",
              "source_section": "7. Cart"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
              "source_lines": "L219",
              "source_section": "7. Cart"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ACTION_ID",
              "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ACTION_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "action": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.ACTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.ACTION.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.ACTION",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              },
              "approval_policy": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.APPROVAL_POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.APPROVAL_POLICY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.APPROVAL_POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "approval_reference": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.APPROVAL_REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.APPROVAL_REFERENCE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "APPROVAL_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.APPROVAL_REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "APPROVAL_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "APPROVAL_REQUIRED"
          },
          "obligation_id": "BRD-WS-07-R005-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
              "source_lines": "L219",
              "source_section": "7. Cart"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ACTION_ID",
              "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ACTION_ID"
          },
          "operator_id": "APPROVAL_REQUIRED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "action": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.ACTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.ACTION.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.ACTION",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            },
            "approval_policy": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.APPROVAL_POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.APPROVAL_POLICY.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.APPROVAL_POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "approval_reference": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.APPROVAL_REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED.APPROVAL_REFERENCE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "APPROVAL_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.APPROVAL_REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "APPROVAL_ID"
            }
          }
        },
        {
          "assertion_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED",
          "evaluator_consumed_bindings": [
            "from_state",
            "state_machine",
            "to_state",
            "trigger"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
              "source_lines": "L219",
              "source_section": "7. Cart"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
              "source_lines": "L219",
              "source_section": "7. Cart"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "from_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R005.FROM_STATE"
                  ],
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.FROM_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.FROM_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "state_machine": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.STATE_MACHINE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_MACHINE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.STATE_MACHINE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_MACHINE_ID"
              },
              "to_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R005.TO_STATE"
                  ],
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.TO_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.TO_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "trigger": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.TRIGGER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.TRIGGER",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "STATE_TRANSITION_ALLOWED"
          },
          "obligation_id": "BRD-WS-07-R005-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
              "source_lines": "L219",
              "source_section": "7. Cart"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "operator_id": "STATE_TRANSITION_ALLOWED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "from_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-07-R005.FROM_STATE"
                ],
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.FROM_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.FROM_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "state_machine": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.STATE_MACHINE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_MACHINE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.STATE_MACHINE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_MACHINE_ID"
            },
            "to_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-07-R005.TO_STATE"
                ],
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.TO_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.TO_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "trigger": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.TRIGGER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.TRIGGER",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            }
          }
        },
        {
          "assertion_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE",
          "evaluator_consumed_bindings": [
            "after_hash",
            "audit_record",
            "before_hash",
            "immutability_boundary",
            "protected_fields",
            "required_fields"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
              "source_lines": "L219",
              "source_section": "7. Cart"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
              "source_lines": "L219",
              "source_section": "7. Cart"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "after_hash": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.AFTER_HASH",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.AFTER_HASH.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "HASH",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.AFTER_HASH",
                  "version": "1.0.0"
                },
                "semantic_type": "HASH"
              },
              "audit_record": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.AUDIT_RECORD",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.AUDIT_RECORD.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.AUDIT_RECORD",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "before_hash": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.BEFORE_HASH",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.BEFORE_HASH.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "HASH",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.BEFORE_HASH",
                  "version": "1.0.0"
                },
                "semantic_type": "HASH"
              },
              "immutability_boundary": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.IMMUTABILITY_BOUNDARY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.IMMUTABILITY_BOUNDARY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.IMMUTABILITY_BOUNDARY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "protected_fields": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.CANDIDATE_IDENTITY_IDS",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.CANDIDATE_IDENTITY_IDS",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.MATCH_EVIDENCE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.2",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MATCH_EVIDENCE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.MERGE_POLICY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.3",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_POLICY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.AUTHORIZATION",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.4",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUTHORIZATION",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.MERGE_RESULT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.5",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_RESULT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.AUDIT_RECORD",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.6",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUDIT_RECORD",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "semantic_type": "SET_OF<FIELD_ID>"
              },
              "required_fields": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.CANDIDATE_IDENTITY_IDS",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.CANDIDATE_IDENTITY_IDS",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.MATCH_EVIDENCE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MATCH_EVIDENCE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.MERGE_POLICY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_POLICY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.AUTHORIZATION",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUTHORIZATION",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.MERGE_RESULT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.5",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_RESULT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.AUDIT_RECORD",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.6",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                      "source_lines": "L219",
                      "source_section": "7. Cart"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUDIT_RECORD",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "semantic_type": "SET_OF<FIELD_ID>"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                  "source_lines": "L219",
                  "source_section": "7. Cart"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "AUDIT_IMMUTABLE"
          },
          "obligation_id": "BRD-WS-07-R005-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
              "source_lines": "L219",
              "source_section": "7. Cart"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "operator_id": "AUDIT_IMMUTABLE",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "after_hash": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.AFTER_HASH",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.AFTER_HASH.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "HASH",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.AFTER_HASH",
                "version": "1.0.0"
              },
              "semantic_type": "HASH"
            },
            "audit_record": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.AUDIT_RECORD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.AUDIT_RECORD.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.AUDIT_RECORD",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "before_hash": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.BEFORE_HASH",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.BEFORE_HASH.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "HASH",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.BEFORE_HASH",
                "version": "1.0.0"
              },
              "semantic_type": "HASH"
            },
            "immutability_boundary": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BRD-WS-07-R005.IMMUTABILITY_BOUNDARY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.IMMUTABILITY_BOUNDARY.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R005.BRD-WS-07-R005.IMMUTABILITY_BOUNDARY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "protected_fields": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.CANDIDATE_IDENTITY_IDS",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.1",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.CANDIDATE_IDENTITY_IDS",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.MATCH_EVIDENCE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.2",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MATCH_EVIDENCE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.MERGE_POLICY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.3",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_POLICY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.AUTHORIZATION",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.4",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUTHORIZATION",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.MERGE_RESULT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.5",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_RESULT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.AUDIT_RECORD",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.6",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUDIT_RECORD",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "semantic_type": "SET_OF<FIELD_ID>"
            },
            "required_fields": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.CANDIDATE_IDENTITY_IDS",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.CANDIDATE_IDENTITY_IDS",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.MATCH_EVIDENCE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MATCH_EVIDENCE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.MERGE_POLICY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_POLICY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.AUTHORIZATION",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUTHORIZATION",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.MERGE_RESULT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.5",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.MERGE_RESULT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.AUDIT_RECORD",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.6",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                    "source_lines": "L219",
                    "source_section": "7. Cart"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R005.FIELD.AUDIT_RECORD",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
                "source_lines": "L219",
                "source_section": "7. Cart"
              },
              "semantic_type": "SET_OF<FIELD_ID>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Potential matches may remain unmerged; approved merge produces traceable canonical linkage"
      ],
      "contract_ast_sha256": "d90be98fef30ff7f258a0cd63952f98ff4cecfc3ee1ceb147264cca98354eb83",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R005",
      "criticality": "CRITICAL",
      "disposition": "SOURCE_CLARIFICATION_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BRD-WS-07-R005.BRD-WS-07-R005.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R005.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
            "source_lines": "L219",
            "source_section": "7. Cart"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-07-R005.BRD-WS-07-R005.BRD-WS-07-R005.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-07-R005.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.CANDIDATE_IDENTITY_IDS",
          "FIELD.MATCH_EVIDENCE",
          "FIELD.MERGE_POLICY",
          "FIELD.AUTHORIZATION",
          "FIELD.MERGE_RESULT",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "BRD-WS-07-R005.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-07-R005.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.CANDIDATE_IDENTITY_IDS",
          "FIELD.MATCH_EVIDENCE",
          "FIELD.MERGE_POLICY",
          "FIELD.AUTHORIZATION",
          "FIELD.MERGE_RESULT",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "BRD-WS-07-R005.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-07-R005.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-07-R005.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-BF3056D5774650E2C68D",
        "P2C-C4-FX-5E00915A7C8C5562098E",
        "P2C-C4-FX-65BADD57B34EEBBFF5F2"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Records are automatically merged without need, policy or authorization"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-07-R005-O001",
          "obligation_text": "Identity sẽ Merge sau nếu cần"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-07-R005.O1.1.APPROVAL_REQUIRED",
            "BRD-WS-07-R005.O1.2.STATE_TRANSITION_ALLOWED",
            "BRD-WS-07-R005.O1.3.AUDIT_IMMUTABLE"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-07-R005-O001"
        }
      ],
      "operator_composition": [
        "APPROVAL_REQUIRED",
        "STATE_TRANSITION_ALLOWED",
        "AUDIT_IMMUTABLE"
      ],
      "positive_oracles": [
        "Identity records remain separate until a governed merge is executed"
      ],
      "preconditions": [
        "Candidate identities, policy and authorization are resolved"
      ],
      "prohibitions": [
        "Records are automatically merged without need, policy or authorization"
      ],
      "requirement_id": "BRD-WS-07-R005",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
          "P2-DEC-008"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-07.md",
        "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
        "source_lines": "L219",
        "source_section": "7. Cart"
      },
      "source_statement": "Identity sẽ Merge sau nếu cần.",
      "surrounding_source_context": "### BRD-WS-07-R005 — Identity sẽ Merge sau nếu cần"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R005",
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
        "BRD-WS-07-R005-AC001",
        "BRD-WS-07-R005-AC002",
        "BRD-WS-07-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R005-O001",
      "obligation_text": "Identity sẽ Merge sau nếu cần"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R005-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R005 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Identity sẽ Merge sau nếu cần.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-005",
    "previous_temporary_key": "TMP-BRD-WS-07-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Cart",
    "source_context_sha256": "2a151fb191691fafb4e40db77d2d6f250971c287d9e8919cf434118d7c4a60f4",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "e5921e33a6361130038654e19ea59705f98095d8c6a6f4e633cdd2ed534ece80",
    "source_lines": "L3828-L7620",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R005"
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
  "stable_id": "BRD-WS-07-R005",
  "title": "Identity sẽ Merge sau nếu cần",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R006 — Version 2.0 chỉ bắt buộc: Primary Email

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Additional contact fields are optional unless another requirement makes them mandatory"
    ],
    "concrete_bindings": [
      {
        "actual_set": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
            "source_type": "SOURCE_LITERAL",
            "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
          },
          "identifier": "RESOLVED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-WS-07-R006.RESOLVED.COLLECTION",
          "origin": {
            "origin_id": "YSIM.BRD-WS-07-R006.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
            "source_lines": "L279-L281",
            "source_section": "10. Customer Information"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "OBSERVE.BRD-WS-07-R006.RESOLVED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
        },
        "required_members": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
            "source_type": "SOURCE_LITERAL",
            "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
          },
          "identifier": "GOVERNED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-WS-07-R006.GOVERNED.COLLECTION",
          "origin": {
            "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
            "source_lines": "L279-L281",
            "source_section": "10. Customer Information"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "RESOLVE.BRD-WS-07-R006.GOVERNED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R006",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "The record is activated without Primary Email"
    ],
    "operator_composition": [
      "SET_CONTAINS"
    ],
    "positive_oracle": [
      "Primary Email is present as the required identity contact"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
      "source_lines": "L279-L281",
      "source_section": "10. Customer Information"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
          "source_type": "SOURCE_LITERAL",
          "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
        },
        "identifier": "BRD-WS-07-R006.BRD-WS-07-R006.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-07-R006.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-07.md",
          "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
          "source_lines": "L279-L281",
          "source_section": "10. Customer Information"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-07-R006.BRD-WS-07-R006.BRD-WS-07-R006.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-07-R006.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.CUSTOMER_IDENTITY_ID",
        "FIELD.PRIMARY_EMAIL",
        "FIELD.VALIDATION_RESULT",
        "FIELD.ACTIVATION_STATE"
      ],
      "producer": "BRD-WS-07-R006.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-07-R006.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.CUSTOMER_IDENTITY_ID",
        "FIELD.PRIMARY_EMAIL",
        "FIELD.VALIDATION_RESULT",
        "FIELD.ACTIVATION_STATE"
      ],
      "required_values_or_hashes": [
        "BRD-WS-07-R006.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-07-R006.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-07-R006.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-07-R006-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS",
          "evaluator_consumed_bindings": [
            "actual_set",
            "required_members"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
              "source_type": "SOURCE_LITERAL",
              "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
            },
            "identifier": "BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
              "source_lines": "L279-L281",
              "source_section": "10. Customer Information"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R006.BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
                },
                "identifier": "BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
                  "source_lines": "L279-L281",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BRD-WS-07-R006.BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
              "source_lines": "L279-L281",
              "source_section": "10. Customer Information"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
                },
                "identifier": "RESOLVED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-WS-07-R006.RESOLVED.COLLECTION",
                "origin": {
                  "origin_id": "YSIM.BRD-WS-07-R006.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
                  "source_lines": "L279-L281",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "OBSERVE.BRD-WS-07-R006.RESOLVED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
              },
              "required_members": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
                },
                "identifier": "GOVERNED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-WS-07-R006.GOVERNED.COLLECTION",
                "origin": {
                  "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
                  "source_lines": "L279-L281",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "RESOLVE.BRD-WS-07-R006.GOVERNED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
              }
            },
            "comparison": {
              "expected": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                      "source_type": "SOURCE_LITERAL",
                      "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
                    },
                    "identifier": "BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
                      "source_lines": "L279-L281",
                      "source_section": "10. Customer Information"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BRD-WS-07-R006.BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
                  "source_lines": "L279-L281",
                  "source_section": "10. Customer Information"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                      "source_type": "SOURCE_LITERAL",
                      "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
                    },
                    "identifier": "BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
                      "source_lines": "L279-L281",
                      "source_section": "10. Customer Information"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "OBSERVE.BRD-WS-07-R006.BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
                  "source_lines": "L279-L281",
                  "source_section": "10. Customer Information"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
              },
              "identifier": "BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
                "source_lines": "L279-L281",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R006.BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SET_CONTAINS"
          },
          "obligation_id": "BRD-WS-07-R006-O001",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
                },
                "identifier": "BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
                  "source_lines": "L279-L281",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BRD-WS-07-R006.BRD-WS-07-R006.BRD-WS-07-R006.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
              "source_lines": "L279-L281",
              "source_section": "10. Customer Information"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "operator_id": "SET_CONTAINS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_set": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
              },
              "identifier": "RESOLVED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-WS-07-R006.RESOLVED.COLLECTION",
              "origin": {
                "origin_id": "YSIM.BRD-WS-07-R006.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
                "source_lines": "L279-L281",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "OBSERVE.BRD-WS-07-R006.RESOLVED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
            },
            "required_members": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
              },
              "identifier": "GOVERNED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-WS-07-R006.GOVERNED.COLLECTION",
              "origin": {
                "origin_id": "BRD-WS-07-R006.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
                "source_lines": "L279-L281",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "RESOLVE.BRD-WS-07-R006.GOVERNED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Additional contact fields are optional unless another requirement makes them mandatory"
      ],
      "contract_ast_sha256": "a3d85a486b8be606ea84d220af44b8cf820f746ffc4039587582cefff5b979de",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R006",
      "criticality": "HIGH",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
            "source_type": "SOURCE_LITERAL",
            "version": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1"
          },
          "identifier": "BRD-WS-07-R006.BRD-WS-07-R006.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R006.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
            "source_lines": "L279-L281",
            "source_section": "10. Customer Information"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-07-R006.BRD-WS-07-R006.BRD-WS-07-R006.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-07-R006.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.CUSTOMER_IDENTITY_ID",
          "FIELD.PRIMARY_EMAIL",
          "FIELD.VALIDATION_RESULT",
          "FIELD.ACTIVATION_STATE"
        ],
        "producer": "BRD-WS-07-R006.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-07-R006.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.CUSTOMER_IDENTITY_ID",
          "FIELD.PRIMARY_EMAIL",
          "FIELD.VALIDATION_RESULT",
          "FIELD.ACTIVATION_STATE"
        ],
        "required_values_or_hashes": [
          "BRD-WS-07-R006.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-07-R006.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-07-R006.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-R2-FX-795638C1B4A041F54A7D",
        "P2C-C4-R2-FX-4B2144D285B62939CCE1",
        "P2C-C4-R2-FX-C41D060B2C0F50666E30"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "The record is activated without Primary Email"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-07-R006-O001",
          "obligation_text": "Version 2.0 chỉ bắt buộc: Primary Email"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-07-R006.O1.1.SET_CONTAINS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-07-R006-O001"
        }
      ],
      "operator_composition": [
        "SET_CONTAINS"
      ],
      "positive_oracles": [
        "Primary Email is present as the required identity contact"
      ],
      "preconditions": [
        "The record is in v2.3 active scope"
      ],
      "prohibitions": [
        "The record is activated without Primary Email"
      ],
      "requirement_id": "BRD-WS-07-R006",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-07.md",
        "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
        "source_lines": "L279-L281",
        "source_section": "10. Customer Information"
      },
      "source_statement": "Version 2.0 chỉ bắt buộc: Primary Email.",
      "surrounding_source_context": "### BRD-WS-07-R006 — Version 2.0 chỉ bắt buộc: Primary Email"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R006",
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
        "BRD-WS-07-R006-AC001",
        "BRD-WS-07-R006-AC002",
        "BRD-WS-07-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R006-O001",
      "obligation_text": "Version 2.0 chỉ bắt buộc: Primary Email"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Version 2.0 chỉ bắt buộc: Primary Email.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-006",
    "previous_temporary_key": "TMP-BRD-WS-07-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Customer Information",
    "source_context_sha256": "4e9815b138059f521584e985c83bbb92efb08decc438b45224a4ce2d37d75d23",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "04aecae66a9dee037eac79a2bcd12a00ae885cc7a0bc7847358a4cb5f18640f1",
    "source_lines": "L7622-L8412",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R006"
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
  "stable_id": "BRD-WS-07-R006",
  "title": "Version 2.0 chỉ bắt buộc: Primary Email",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R007 — Primary Email luôn nhận: - Payment Confirmation

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Other approved recipients may also receive confirmation; Primary Email remains required"
    ],
    "concrete_bindings": [
      {
        "allowed_terminal_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "PAYMENT.CONFIRMATION.DELIVERED"
                ],
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "PAYMENT.CONFIRMATION.DELIVERED",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.ALLOWED_TERMINAL_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R007.PAYMENT.CONFIRMATION.DELIVERED",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.ALLOWED_TERMINAL_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
            "source_lines": "L291-L293",
            "source_section": "10. Customer Information"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "delivery_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
            "source_type": "SOURCE_LITERAL",
            "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
          },
          "identifier": "BRD-WS-07-R007.DELIVERY_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.DELIVERY_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
            "source_lines": "L291-L293",
            "source_section": "10. Customer Information"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "DELIVERY_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.DELIVERY_ID",
            "version": "1.0.0"
          },
          "semantic_type": "DELIVERY_ID"
        },
        "observed_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-07-R007.OBSERVED.STATE"
            ],
            "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
            "source_type": "SOURCE_LITERAL",
            "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
          },
          "identifier": "BRD-WS-07-R007.OBSERVED.STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.OBSERVED_STATE.ORIGIN",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
            "source_lines": "L291-L293",
            "source_section": "10. Customer Information"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.OBSERVED.STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        }
      },
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-07-R007.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "BRD-WS-07-R007.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
            "source_lines": "L291-L293",
            "source_section": "10. Customer Information"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-07-R007.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "BRD-WS-07-R007.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
            "source_lines": "L291-L293",
            "source_section": "10. Customer Information"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
            "source_type": "SOURCE_LITERAL",
            "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
          },
          "identifier": "BRD-WS-07-R007.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
            "source_lines": "L291-L293",
            "source_section": "10. Customer Information"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
            "source_type": "SOURCE_LITERAL",
            "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
          },
          "identifier": "BRD-WS-07-R007.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
            "source_lines": "L291-L293",
            "source_section": "10. Customer Information"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
            "source_type": "SOURCE_LITERAL",
            "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
          },
          "identifier": "BRD-WS-07-R007.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
            "source_lines": "L291-L293",
            "source_section": "10. Customer Information"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
            "source_type": "SOURCE_LITERAL",
            "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
          },
          "identifier": "BRD-WS-07-R007.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
            "source_lines": "L291-L293",
            "source_section": "10. Customer Information"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
            "source_type": "SOURCE_LITERAL",
            "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
          },
          "identifier": "BRD-WS-07-R007.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
            "source_lines": "L291-L293",
            "source_section": "10. Customer Information"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R007",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Primary Email is omitted from required recipients"
    ],
    "operator_composition": [
      "DELIVERY_TERMINAL_STATE",
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "Payment Confirmation is delivered to Primary Email"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
      "source_lines": "L291-L293",
      "source_section": "10. Customer Information"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
          "source_type": "SOURCE_LITERAL",
          "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
        },
        "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-07-R007.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-07.md",
          "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
          "source_lines": "L291-L293",
          "source_section": "10. Customer Information"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-07-R007.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PAYMENT_ID",
        "FIELD.PRIMARY_EMAIL",
        "FIELD.RECIPIENT_LIST",
        "FIELD.DELIVERY_STATE",
        "FIELD.CORRELATION_ID"
      ],
      "producer": "BRD-WS-07-R007.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-07-R007.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PAYMENT_ID",
        "FIELD.PRIMARY_EMAIL",
        "FIELD.RECIPIENT_LIST",
        "FIELD.DELIVERY_STATE",
        "FIELD.CORRELATION_ID"
      ],
      "required_values_or_hashes": [
        "BRD-WS-07-R007.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-07-R007.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-07-R007.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-07-R007-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE",
          "evaluator_consumed_bindings": [
            "allowed_terminal_states",
            "delivery_id",
            "observed_state"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
              "source_type": "SOURCE_LITERAL",
              "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
            },
            "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
              "source_lines": "L291-L293",
              "source_section": "10. Customer Information"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
              "source_type": "SOURCE_LITERAL",
              "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
            },
            "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
              "source_lines": "L291-L293",
              "source_section": "10. Customer Information"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "allowed_terminal_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "PAYMENT.CONFIRMATION.DELIVERED"
                      ],
                      "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                      "source_type": "SOURCE_LITERAL",
                      "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                    },
                    "identifier": "PAYMENT.CONFIRMATION.DELIVERED",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.ALLOWED_TERMINAL_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                      "source_lines": "L291-L293",
                      "source_section": "10. Customer Information"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R007.PAYMENT.CONFIRMATION.DELIVERED",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.ALLOWED_TERMINAL_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "delivery_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                },
                "identifier": "BRD-WS-07-R007.DELIVERY_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.DELIVERY_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "DELIVERY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.DELIVERY_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "DELIVERY_ID"
              },
              "observed_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R007.OBSERVED.STATE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                },
                "identifier": "BRD-WS-07-R007.OBSERVED.STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.OBSERVED_STATE.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.OBSERVED.STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                },
                "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                },
                "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "DELIVERY_TERMINAL_STATE"
          },
          "obligation_id": "BRD-WS-07-R007-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
              "source_type": "SOURCE_LITERAL",
              "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
            },
            "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
              "source_lines": "L291-L293",
              "source_section": "10. Customer Information"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "operator_id": "DELIVERY_TERMINAL_STATE",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "allowed_terminal_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "PAYMENT.CONFIRMATION.DELIVERED"
                    ],
                    "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                    "source_type": "SOURCE_LITERAL",
                    "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                  },
                  "identifier": "PAYMENT.CONFIRMATION.DELIVERED",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.ALLOWED_TERMINAL_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                    "source_lines": "L291-L293",
                    "source_section": "10. Customer Information"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R007.PAYMENT.CONFIRMATION.DELIVERED",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.ALLOWED_TERMINAL_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "delivery_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "BRD-WS-07-R007.DELIVERY_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.DELIVERY_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "DELIVERY_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.DELIVERY_ID",
                "version": "1.0.0"
              },
              "semantic_type": "DELIVERY_ID"
            },
            "observed_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-07-R007.OBSERVED.STATE"
                ],
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "BRD-WS-07-R007.OBSERVED.STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE.OBSERVED_STATE.ORIGIN",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.OBSERVED.STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          }
        },
        {
          "assertion_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID",
          "evaluator_consumed_bindings": [
            "allowed_lifecycle_states",
            "allowed_states",
            "reference",
            "registry",
            "registry_source",
            "target_id",
            "target_type"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
              "source_type": "SOURCE_LITERAL",
              "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
            },
            "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
              "source_lines": "L291-L293",
              "source_section": "10. Customer Information"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
              "source_type": "SOURCE_LITERAL",
              "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
            },
            "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
              "source_lines": "L291-L293",
              "source_section": "10. Customer Information"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "allowed_lifecycle_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-07-R007.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                      "source_type": "SOURCE_LITERAL",
                      "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                    },
                    "identifier": "BRD-WS-07-R007.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                      "source_lines": "L291-L293",
                      "source_section": "10. Customer Information"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-07-R007.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                      "source_type": "SOURCE_LITERAL",
                      "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                    },
                    "identifier": "BRD-WS-07-R007.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                      "source_lines": "L291-L293",
                      "source_section": "10. Customer Information"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                },
                "identifier": "BRD-WS-07-R007.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                },
                "identifier": "BRD-WS-07-R007.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                },
                "identifier": "BRD-WS-07-R007.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                },
                "identifier": "BRD-WS-07-R007.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                },
                "identifier": "BRD-WS-07-R007.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                },
                "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                },
                "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                  "source_lines": "L291-L293",
                  "source_section": "10. Customer Information"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "BRD-WS-07-R007-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
              "source_type": "SOURCE_LITERAL",
              "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
            },
            "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
              "source_lines": "L291-L293",
              "source_section": "10. Customer Information"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "operator_id": "REFERENCE_TARGET_VALID",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "allowed_lifecycle_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-WS-07-R007.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                    "source_type": "SOURCE_LITERAL",
                    "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                  },
                  "identifier": "BRD-WS-07-R007.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                    "source_lines": "L291-L293",
                    "source_section": "10. Customer Information"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-WS-07-R007.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                    "source_type": "SOURCE_LITERAL",
                    "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
                  },
                  "identifier": "BRD-WS-07-R007.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                    "source_lines": "L291-L293",
                    "source_section": "10. Customer Information"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "BRD-WS-07-R007.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "BRD-WS-07-R007.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "BRD-WS-07-R007.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "BRD-WS-07-R007.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
                "source_type": "SOURCE_LITERAL",
                "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
              },
              "identifier": "BRD-WS-07-R007.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
                "source_lines": "L291-L293",
                "source_section": "10. Customer Information"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.BRD-WS-07-R007.BRD-WS-07-R007.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "Other approved recipients may also receive confirmation; Primary Email remains required"
      ],
      "contract_ast_sha256": "4f4146a359645966aaa793489a6a080a62d8a6ec59a21b8b8b2d3f3de868508e",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R007",
      "criticality": "CRITICAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#10. Customer Information",
            "source_type": "SOURCE_LITERAL",
            "version": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7"
          },
          "identifier": "BRD-WS-07-R007.BRD-WS-07-R007.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R007.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
            "source_lines": "L291-L293",
            "source_section": "10. Customer Information"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-07-R007.BRD-WS-07-R007.BRD-WS-07-R007.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-07-R007.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PAYMENT_ID",
          "FIELD.PRIMARY_EMAIL",
          "FIELD.RECIPIENT_LIST",
          "FIELD.DELIVERY_STATE",
          "FIELD.CORRELATION_ID"
        ],
        "producer": "BRD-WS-07-R007.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-07-R007.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PAYMENT_ID",
          "FIELD.PRIMARY_EMAIL",
          "FIELD.RECIPIENT_LIST",
          "FIELD.DELIVERY_STATE",
          "FIELD.CORRELATION_ID"
        ],
        "required_values_or_hashes": [
          "BRD-WS-07-R007.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-07-R007.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-07-R007.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-7D8A3E52C123BB445701",
        "P2C-C4-FX-3DEFE67994C3E29631D9",
        "P2C-C4-FX-003EEB4F5235B45F94CA"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Primary Email is omitted from required recipients"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-07-R007-O001",
          "obligation_text": "Primary Email luôn nhận: - Payment Confirmation"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-07-R007.O1.1.DELIVERY_TERMINAL_STATE",
            "BRD-WS-07-R007.O1.2.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-07-R007-O001"
        }
      ],
      "operator_composition": [
        "DELIVERY_TERMINAL_STATE",
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "Payment Confirmation is delivered to Primary Email"
      ],
      "preconditions": [
        "Payment Owner Primary Email is resolved and permitted"
      ],
      "prohibitions": [
        "Primary Email is omitted from required recipients"
      ],
      "requirement_id": "BRD-WS-07-R007",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-07.md",
        "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
        "source_lines": "L291-L293",
        "source_section": "10. Customer Information"
      },
      "source_statement": "Primary Email luôn nhận: - Payment Confirmation",
      "surrounding_source_context": "### BRD-WS-07-R007 — Primary Email luôn nhận: - Payment Confirmation"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R007",
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
        "BRD-WS-07-R007-AC001",
        "BRD-WS-07-R007-AC002",
        "BRD-WS-07-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R007-O001",
      "obligation_text": "Primary Email luôn nhận: - Payment Confirmation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R007 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Primary Email luôn nhận: - Payment Confirmation",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-007",
    "previous_temporary_key": "TMP-BRD-WS-07-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Customer Information",
    "source_context_sha256": "4e9815b138059f521584e985c83bbb92efb08decc438b45224a4ce2d37d75d23",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "1edf2dfff3534e50e6cf573f40e603648f5eca47bef52f9d4b02d784d89ab7d7",
    "source_lines": "L8414-L10413",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R007"
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
  "stable_id": "BRD-WS-07-R007",
  "title": "Primary Email luôn nhận: - Payment Confirmation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R008 — Primary Email luôn nhận: - Invoice

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
      "requirement_id": "BRD-WS-07-R008",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "d67104a14dabdb9718d01415502637dbe99361c8dc0d02f25369d46eab0a84bd"
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
        "BRD-WS-07-R008-AC001",
        "BRD-WS-07-R008-AC002",
        "BRD-WS-07-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R008-O001",
      "obligation_text": "Primary Email luôn nhận: - Invoice"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Primary Email luôn nhận: - Invoice",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-008",
    "previous_temporary_key": "TMP-BRD-WS-07-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Customer Information",
    "source_context_sha256": "4e9815b138059f521584e985c83bbb92efb08decc438b45224a4ce2d37d75d23",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "d67104a14dabdb9718d01415502637dbe99361c8dc0d02f25369d46eab0a84bd",
    "source_lines": "L10415-L10490",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R008"
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
  "stable_id": "BRD-WS-07-R008",
  "title": "Primary Email luôn nhận: - Invoice",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R009 — Khi Customer bắt đầu Payment: Item phải được Reserve

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "When procurement is required, the separately approved commercial gate applies before payment"
    ],
    "concrete_bindings": [
      {
        "from_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-07-R009.FROM_STATE"
            ],
            "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
            "source_type": "SOURCE_LITERAL",
            "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
          },
          "identifier": "BRD-WS-07-R009.FROM_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
            "source_lines": "L350-L352",
            "source_section": "13. Inventory Reservation"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.FROM_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "state_machine": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
            "source_type": "SOURCE_LITERAL",
            "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
          },
          "identifier": "BRD-WS-07-R009.STATE_MACHINE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
            "source_lines": "L350-L352",
            "source_section": "13. Inventory Reservation"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_MACHINE_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.STATE_MACHINE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_MACHINE_ID"
        },
        "to_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-07-R009.TO_STATE"
            ],
            "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
            "source_type": "SOURCE_LITERAL",
            "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
          },
          "identifier": "BRD-WS-07-R009.TO_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
            "source_lines": "L350-L352",
            "source_section": "13. Inventory Reservation"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.TO_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "trigger": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
            "source_type": "SOURCE_LITERAL",
            "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
          },
          "identifier": "BRD-WS-07-R009.TRIGGER",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
            "source_lines": "L350-L352",
            "source_section": "13. Inventory Reservation"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.TRIGGER",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        }
      },
      {
        "blocked_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-07-R009.BLOCKED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                "source_type": "SOURCE_LITERAL",
                "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
              },
              "identifier": "BRD-WS-07-R009.BLOCKED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.BLOCKED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                "source_lines": "L350-L352",
                "source_section": "13. Inventory Reservation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.BLOCKED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.BLOCKED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
            "source_lines": "L350-L352",
            "source_section": "13. Inventory Reservation"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "failed_checks": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-07-R009.FAILED_CHECKS.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                "source_type": "SOURCE_LITERAL",
                "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
              },
              "identifier": "BRD-WS-07-R009.FAILED_CHECKS.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.FAILED_CHECKS.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                "source_lines": "L350-L352",
                "source_section": "13. Inventory Reservation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_OUTCOME",
                "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.FAILED_CHECKS.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_OUTCOME"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.FAILED_CHECKS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
            "source_lines": "L350-L352",
            "source_section": "13. Inventory Reservation"
          },
          "semantic_type": "SET_OF<CANONICAL_OUTCOME>"
        },
        "order_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
            "source_type": "SOURCE_LITERAL",
            "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
          },
          "identifier": "BRD-WS-07-R009.ORDER_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.ORDER_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
            "source_lines": "L350-L352",
            "source_section": "13. Inventory Reservation"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ORDER_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.ORDER_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ORDER_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R009",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Payment starts while an applicable Item is not Reserved"
    ],
    "operator_composition": [
      "STATE_TRANSITION_ALLOWED",
      "PAYMENT_INITIATION_BLOCKED"
    ],
    "positive_oracle": [
      "Each applicable Item is Reserved before Payment initiation proceeds"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-008"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
      "source_lines": "L350-L352",
      "source_section": "13. Inventory Reservation"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
          "source_type": "SOURCE_LITERAL",
          "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
        },
        "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-07-R009.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-008"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-07.md",
          "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
          "source_lines": "L350-L352",
          "source_section": "13. Inventory Reservation"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-07-R009.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.ORDER_ID",
        "FIELD.ITEM_IDS",
        "FIELD.RESERVATION_IDS",
        "FIELD.RESERVATION_STATE",
        "FIELD.PAYMENT_STATE",
        "FIELD.TIMESTAMPS"
      ],
      "producer": "BRD-WS-07-R009.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-07-R009.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.ORDER_ID",
        "FIELD.ITEM_IDS",
        "FIELD.RESERVATION_IDS",
        "FIELD.RESERVATION_STATE",
        "FIELD.PAYMENT_STATE",
        "FIELD.TIMESTAMPS"
      ],
      "required_values_or_hashes": [
        "BRD-WS-07-R009.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-07-R009.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-07-R009.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-07-R009-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED",
          "evaluator_consumed_bindings": [
            "from_state",
            "state_machine",
            "to_state",
            "trigger"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
              "source_type": "SOURCE_LITERAL",
              "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
            },
            "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
              "source_lines": "L350-L352",
              "source_section": "13. Inventory Reservation"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
              "source_type": "SOURCE_LITERAL",
              "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
            },
            "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
              "source_lines": "L350-L352",
              "source_section": "13. Inventory Reservation"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "from_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R009.FROM_STATE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                },
                "identifier": "BRD-WS-07-R009.FROM_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                  "source_lines": "L350-L352",
                  "source_section": "13. Inventory Reservation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.FROM_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "state_machine": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                },
                "identifier": "BRD-WS-07-R009.STATE_MACHINE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                  "source_lines": "L350-L352",
                  "source_section": "13. Inventory Reservation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_MACHINE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.STATE_MACHINE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_MACHINE_ID"
              },
              "to_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R009.TO_STATE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                },
                "identifier": "BRD-WS-07-R009.TO_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                  "source_lines": "L350-L352",
                  "source_section": "13. Inventory Reservation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.TO_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "trigger": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                },
                "identifier": "BRD-WS-07-R009.TRIGGER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                  "source_lines": "L350-L352",
                  "source_section": "13. Inventory Reservation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.TRIGGER",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                },
                "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                  "source_lines": "L350-L352",
                  "source_section": "13. Inventory Reservation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                },
                "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                  "source_lines": "L350-L352",
                  "source_section": "13. Inventory Reservation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                "source_type": "SOURCE_LITERAL",
                "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
              },
              "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                "source_lines": "L350-L352",
                "source_section": "13. Inventory Reservation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "STATE_TRANSITION_ALLOWED"
          },
          "obligation_id": "BRD-WS-07-R009-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
              "source_type": "SOURCE_LITERAL",
              "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
            },
            "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
              "source_lines": "L350-L352",
              "source_section": "13. Inventory Reservation"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "OBSERVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "operator_id": "STATE_TRANSITION_ALLOWED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "from_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-07-R009.FROM_STATE"
                ],
                "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                "source_type": "SOURCE_LITERAL",
                "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
              },
              "identifier": "BRD-WS-07-R009.FROM_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                "source_lines": "L350-L352",
                "source_section": "13. Inventory Reservation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.FROM_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "state_machine": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                "source_type": "SOURCE_LITERAL",
                "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
              },
              "identifier": "BRD-WS-07-R009.STATE_MACHINE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                "source_lines": "L350-L352",
                "source_section": "13. Inventory Reservation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_MACHINE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.STATE_MACHINE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_MACHINE_ID"
            },
            "to_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-07-R009.TO_STATE"
                ],
                "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                "source_type": "SOURCE_LITERAL",
                "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
              },
              "identifier": "BRD-WS-07-R009.TO_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                "source_lines": "L350-L352",
                "source_section": "13. Inventory Reservation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.TO_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "trigger": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                "source_type": "SOURCE_LITERAL",
                "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
              },
              "identifier": "BRD-WS-07-R009.TRIGGER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                "source_lines": "L350-L352",
                "source_section": "13. Inventory Reservation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.TRIGGER",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            }
          }
        },
        {
          "assertion_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED",
          "evaluator_consumed_bindings": [
            "blocked_states",
            "failed_checks",
            "order_id"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
              "source_type": "SOURCE_LITERAL",
              "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
            },
            "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
              "source_lines": "L350-L352",
              "source_section": "13. Inventory Reservation"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
              "source_type": "SOURCE_LITERAL",
              "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
            },
            "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
              "source_lines": "L350-L352",
              "source_section": "13. Inventory Reservation"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ORDER_ID",
              "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ORDER_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "blocked_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-07-R009.BLOCKED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                      "source_type": "SOURCE_LITERAL",
                      "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                    },
                    "identifier": "BRD-WS-07-R009.BLOCKED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.BLOCKED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                      "source_lines": "L350-L352",
                      "source_section": "13. Inventory Reservation"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.BLOCKED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.BLOCKED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                  "source_lines": "L350-L352",
                  "source_section": "13. Inventory Reservation"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "failed_checks": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-07-R009.FAILED_CHECKS.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                      "source_type": "SOURCE_LITERAL",
                      "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                    },
                    "identifier": "BRD-WS-07-R009.FAILED_CHECKS.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.FAILED_CHECKS.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                      "source_lines": "L350-L352",
                      "source_section": "13. Inventory Reservation"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_OUTCOME",
                      "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.FAILED_CHECKS.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_OUTCOME"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.FAILED_CHECKS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                  "source_lines": "L350-L352",
                  "source_section": "13. Inventory Reservation"
                },
                "semantic_type": "SET_OF<CANONICAL_OUTCOME>"
              },
              "order_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                },
                "identifier": "BRD-WS-07-R009.ORDER_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.ORDER_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                  "source_lines": "L350-L352",
                  "source_section": "13. Inventory Reservation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ORDER_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.ORDER_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ORDER_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                },
                "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                  "source_lines": "L350-L352",
                  "source_section": "13. Inventory Reservation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ORDER_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ORDER_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                },
                "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                  "source_lines": "L350-L352",
                  "source_section": "13. Inventory Reservation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ORDER_ID",
                  "resolver_id": "OBSERVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ORDER_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                "source_type": "SOURCE_LITERAL",
                "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
              },
              "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                "source_lines": "L350-L352",
                "source_section": "13. Inventory Reservation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "PAYMENT_INITIATION_BLOCKED"
          },
          "obligation_id": "BRD-WS-07-R009-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
              "source_type": "SOURCE_LITERAL",
              "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
            },
            "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
              "source_lines": "L350-L352",
              "source_section": "13. Inventory Reservation"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ORDER_ID",
              "resolver_id": "OBSERVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ORDER_ID"
          },
          "operator_id": "PAYMENT_INITIATION_BLOCKED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "blocked_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-WS-07-R009.BLOCKED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                    "source_type": "SOURCE_LITERAL",
                    "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                  },
                  "identifier": "BRD-WS-07-R009.BLOCKED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.BLOCKED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                    "source_lines": "L350-L352",
                    "source_section": "13. Inventory Reservation"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.BLOCKED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.BLOCKED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                "source_lines": "L350-L352",
                "source_section": "13. Inventory Reservation"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "failed_checks": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-WS-07-R009.FAILED_CHECKS.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                    "source_type": "SOURCE_LITERAL",
                    "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
                  },
                  "identifier": "BRD-WS-07-R009.FAILED_CHECKS.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.FAILED_CHECKS.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                    "source_lines": "L350-L352",
                    "source_section": "13. Inventory Reservation"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CANONICAL_OUTCOME",
                    "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.FAILED_CHECKS.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CANONICAL_OUTCOME"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.FAILED_CHECKS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                "source_lines": "L350-L352",
                "source_section": "13. Inventory Reservation"
              },
              "semantic_type": "SET_OF<CANONICAL_OUTCOME>"
            },
            "order_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
                "source_type": "SOURCE_LITERAL",
                "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
              },
              "identifier": "BRD-WS-07-R009.ORDER_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED.ORDER_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
                "source_lines": "L350-L352",
                "source_section": "13. Inventory Reservation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ORDER_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R009.BRD-WS-07-R009.ORDER_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ORDER_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "When procurement is required, the separately approved commercial gate applies before payment"
      ],
      "contract_ast_sha256": "b38c23889c4b7e1b7029148949e344aca1d04508ce2522a8be466e7b8cb428fe",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R009",
      "criticality": "CRITICAL",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#13. Inventory Reservation",
            "source_type": "SOURCE_LITERAL",
            "version": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3"
          },
          "identifier": "BRD-WS-07-R009.BRD-WS-07-R009.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R009.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
            "source_lines": "L350-L352",
            "source_section": "13. Inventory Reservation"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-07-R009.BRD-WS-07-R009.BRD-WS-07-R009.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-07-R009.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.ORDER_ID",
          "FIELD.ITEM_IDS",
          "FIELD.RESERVATION_IDS",
          "FIELD.RESERVATION_STATE",
          "FIELD.PAYMENT_STATE",
          "FIELD.TIMESTAMPS"
        ],
        "producer": "BRD-WS-07-R009.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-07-R009.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.ORDER_ID",
          "FIELD.ITEM_IDS",
          "FIELD.RESERVATION_IDS",
          "FIELD.RESERVATION_STATE",
          "FIELD.PAYMENT_STATE",
          "FIELD.TIMESTAMPS"
        ],
        "required_values_or_hashes": [
          "BRD-WS-07-R009.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-07-R009.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-07-R009.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-0C7CAF5E4E920F4F54B3",
        "P2C-C4-FX-F007A892AF5BD22616E0",
        "P2C-C4-FX-C18DAB06A72ED16F149A"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Payment starts while an applicable Item is not Reserved"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-07-R009-O001",
          "obligation_text": "Khi Customer bắt đầu Payment: Item phải được Reserve"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-07-R009.O1.1.STATE_TRANSITION_ALLOWED",
            "BRD-WS-07-R009.O1.2.PAYMENT_INITIATION_BLOCKED"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-07-R009-O001"
        }
      ],
      "operator_composition": [
        "STATE_TRANSITION_ALLOWED",
        "PAYMENT_INITIATION_BLOCKED"
      ],
      "positive_oracles": [
        "Each applicable Item is Reserved before Payment initiation proceeds"
      ],
      "preconditions": [
        "The order items and allocatable inventory are identified"
      ],
      "prohibitions": [
        "Payment starts while an applicable Item is not Reserved"
      ],
      "requirement_id": "BRD-WS-07-R009",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-008"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-07.md",
        "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
        "source_lines": "L350-L352",
        "source_section": "13. Inventory Reservation"
      },
      "source_statement": "Khi Customer bắt đầu Payment: Item phải được Reserve.",
      "surrounding_source_context": "### BRD-WS-07-R009 — Khi Customer bắt đầu Payment: Item phải được Reserve"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R009",
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
        "BRD-WS-07-R009-AC001",
        "BRD-WS-07-R009-AC002",
        "BRD-WS-07-R009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R009-O001",
      "obligation_text": "Khi Customer bắt đầu Payment: Item phải được Reserve"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R009 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R009 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R009 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R009-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R009-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R009 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi Customer bắt đầu Payment: Item phải được Reserve.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-009",
    "previous_temporary_key": "TMP-BRD-WS-07-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Inventory Reservation",
    "source_context_sha256": "bbb1bb9024c71508d6f6ac64841cde2691f20ddb7eac32d7202f0f280def7483",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "0d076404a4e1631b602ba9ad50155a0b2eadb97873a8862a96028a4786db3ae3",
    "source_lines": "L10492-L12223",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R009"
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
  "stable_id": "BRD-WS-07-R009",
  "title": "Khi Customer bắt đầu Payment: Item phải được Reserve",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R010 — Purchase Order tự động: - chỉ mua đúng số lượng còn thiếu - chỉ mua đúng Product cần thiết

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "No shortage creates no automatic Purchase Order; a shortage creates only its required coverage"
    ],
    "concrete_bindings": [
      {
        "capacity": {
          "origin": {
            "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.CAPACITY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
            "source_lines": "L439-L442",
            "source_section": "15. Purchase Order Policy"
          },
          "semantic_type": "DECIMAL",
          "value": 1
        },
        "coverage_policy": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
            "source_type": "SOURCE_LITERAL",
            "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
          },
          "identifier": "BRD-WS-07-R010.COVERAGE_POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.COVERAGE_POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
            "source_lines": "L439-L442",
            "source_section": "15. Purchase Order Policy"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.COVERAGE_POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "order_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
            "source_type": "SOURCE_LITERAL",
            "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
          },
          "identifier": "BRD-WS-07-R010.ORDER_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.ORDER_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
            "source_lines": "L439-L442",
            "source_section": "15. Purchase Order Policy"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ORDER_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.ORDER_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ORDER_ID"
        },
        "supplier_terms": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
            "source_type": "SOURCE_LITERAL",
            "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
          },
          "identifier": "BRD-WS-07-R010.SUPPLIER_TERMS",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.SUPPLIER_TERMS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
            "source_lines": "L439-L442",
            "source_section": "15. Purchase Order Policy"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.SUPPLIER_TERMS",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        }
      },
      {
        "expected_outcome": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-07-R010.POLICY.OUTCOME.CONFORMING"
            ],
            "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
            "source_type": "SOURCE_LITERAL",
            "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
          },
          "identifier": "BRD-WS-07-R010.POLICY.OUTCOME.CONFORMING",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
            "source_lines": "L439-L442",
            "source_section": "15. Purchase Order Policy"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_OUTCOME",
            "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY.OUTCOME.CONFORMING",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_OUTCOME"
        },
        "policy": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
            "source_type": "SOURCE_LITERAL",
            "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
          },
          "identifier": "BRD-WS-07-R010.POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
            "source_lines": "L439-L442",
            "source_section": "15. Purchase Order Policy"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "policy_inputs": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
            "source_type": "SOURCE_LITERAL",
            "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
          },
          "identifier": "BRD-WS-07-R010.POLICY_INPUTS",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
            "source_lines": "L439-L442",
            "source_section": "15. Purchase Order Policy"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY_INPUTS",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "policy_version": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
            "source_type": "SOURCE_LITERAL",
            "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
          },
          "identifier": "BRD-WS-07-R010.POLICY_VERSION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
            "source_lines": "L439-L442",
            "source_section": "15. Purchase Order Policy"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_VERSION",
            "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY_VERSION",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_VERSION"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R010",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "It buys excess quantity or a different Product"
    ],
    "operator_composition": [
      "PROCUREMENT_FEASIBLE",
      "POLICY_OUTCOME_EQUALS"
    ],
    "positive_oracle": [
      "Purchase Order buys exactly the missing quantity of exactly the required Product"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
      "source_lines": "L439-L442",
      "source_section": "15. Purchase Order Policy"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
          "source_type": "SOURCE_LITERAL",
          "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
        },
        "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-07-R010.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-07.md",
          "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
          "source_lines": "L439-L442",
          "source_section": "15. Purchase Order Policy"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-07-R010.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.ORDER_ID",
        "FIELD.PRODUCT_ID",
        "FIELD.MISSING_QUANTITY",
        "FIELD.PURCHASE_ORDER_PRODUCT",
        "FIELD.PURCHASE_ORDER_QUANTITY",
        "FIELD.CALCULATION_RESULT"
      ],
      "producer": "BRD-WS-07-R010.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-07-R010.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.ORDER_ID",
        "FIELD.PRODUCT_ID",
        "FIELD.MISSING_QUANTITY",
        "FIELD.PURCHASE_ORDER_PRODUCT",
        "FIELD.PURCHASE_ORDER_QUANTITY",
        "FIELD.CALCULATION_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-07-R010.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-07-R010.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-07-R010.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-07-R010-O001",
      "BRD-WS-07-R010-O002"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE",
          "evaluator_consumed_bindings": [
            "capacity",
            "coverage_policy",
            "order_id",
            "supplier_terms"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
              "source_type": "SOURCE_LITERAL",
              "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
            },
            "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
              "source_lines": "L439-L442",
              "source_section": "15. Purchase Order Policy"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
              "source_type": "SOURCE_LITERAL",
              "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
            },
            "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
              "source_lines": "L439-L442",
              "source_section": "15. Purchase Order Policy"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ORDER_ID",
              "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ORDER_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "capacity": {
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.CAPACITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "semantic_type": "DECIMAL",
                "value": 1
              },
              "coverage_policy": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                  "source_type": "SOURCE_LITERAL",
                  "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
                },
                "identifier": "BRD-WS-07-R010.COVERAGE_POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.COVERAGE_POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.COVERAGE_POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "order_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                  "source_type": "SOURCE_LITERAL",
                  "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
                },
                "identifier": "BRD-WS-07-R010.ORDER_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.ORDER_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ORDER_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.ORDER_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ORDER_ID"
              },
              "supplier_terms": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                  "source_type": "SOURCE_LITERAL",
                  "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
                },
                "identifier": "BRD-WS-07-R010.SUPPLIER_TERMS",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.SUPPLIER_TERMS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.SUPPLIER_TERMS",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                  "source_type": "SOURCE_LITERAL",
                  "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
                },
                "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ORDER_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ORDER_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                  "source_type": "SOURCE_LITERAL",
                  "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
                },
                "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ORDER_ID",
                  "resolver_id": "OBSERVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ORDER_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                "source_type": "SOURCE_LITERAL",
                "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
              },
              "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                "source_lines": "L439-L442",
                "source_section": "15. Purchase Order Policy"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "PROCUREMENT_FEASIBLE"
          },
          "obligation_id": "BRD-WS-07-R010-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
              "source_type": "SOURCE_LITERAL",
              "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
            },
            "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
              "source_lines": "L439-L442",
              "source_section": "15. Purchase Order Policy"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ORDER_ID",
              "resolver_id": "OBSERVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ORDER_ID"
          },
          "operator_id": "PROCUREMENT_FEASIBLE",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "capacity": {
              "origin": {
                "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.CAPACITY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                "source_lines": "L439-L442",
                "source_section": "15. Purchase Order Policy"
              },
              "semantic_type": "DECIMAL",
              "value": 1
            },
            "coverage_policy": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                "source_type": "SOURCE_LITERAL",
                "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
              },
              "identifier": "BRD-WS-07-R010.COVERAGE_POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.COVERAGE_POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                "source_lines": "L439-L442",
                "source_section": "15. Purchase Order Policy"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.COVERAGE_POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "order_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                "source_type": "SOURCE_LITERAL",
                "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
              },
              "identifier": "BRD-WS-07-R010.ORDER_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.ORDER_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                "source_lines": "L439-L442",
                "source_section": "15. Purchase Order Policy"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ORDER_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.ORDER_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ORDER_ID"
            },
            "supplier_terms": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                "source_type": "SOURCE_LITERAL",
                "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
              },
              "identifier": "BRD-WS-07-R010.SUPPLIER_TERMS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE.SUPPLIER_TERMS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                "source_lines": "L439-L442",
                "source_section": "15. Purchase Order Policy"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.SUPPLIER_TERMS",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            }
          }
        },
        {
          "assertion_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS",
          "evaluator_consumed_bindings": [
            "expected_outcome",
            "policy",
            "policy_inputs",
            "policy_version"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
              "source_type": "SOURCE_LITERAL",
              "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
            },
            "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
              "source_lines": "L439-L442",
              "source_section": "15. Purchase Order Policy"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
              "source_type": "SOURCE_LITERAL",
              "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
            },
            "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
              "source_lines": "L439-L442",
              "source_section": "15. Purchase Order Policy"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
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
                    "BRD-WS-07-R010.POLICY.OUTCOME.CONFORMING"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                  "source_type": "SOURCE_LITERAL",
                  "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
                },
                "identifier": "BRD-WS-07-R010.POLICY.OUTCOME.CONFORMING",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY.OUTCOME.CONFORMING",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "policy": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                  "source_type": "SOURCE_LITERAL",
                  "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
                },
                "identifier": "BRD-WS-07-R010.POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "policy_inputs": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                  "source_type": "SOURCE_LITERAL",
                  "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
                },
                "identifier": "BRD-WS-07-R010.POLICY_INPUTS",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY_INPUTS",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "policy_version": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                  "source_type": "SOURCE_LITERAL",
                  "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
                },
                "identifier": "BRD-WS-07-R010.POLICY_VERSION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_VERSION",
                  "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY_VERSION",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_VERSION"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                  "source_type": "SOURCE_LITERAL",
                  "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
                },
                "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                  "source_type": "SOURCE_LITERAL",
                  "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
                },
                "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                  "source_lines": "L439-L442",
                  "source_section": "15. Purchase Order Policy"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "OBSERVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                "source_type": "SOURCE_LITERAL",
                "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
              },
              "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                "source_lines": "L439-L442",
                "source_section": "15. Purchase Order Policy"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "POLICY_OUTCOME_EQUALS"
          },
          "obligation_id": "BRD-WS-07-R010-O002",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
              "source_type": "SOURCE_LITERAL",
              "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
            },
            "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
              "source_lines": "L439-L442",
              "source_section": "15. Purchase Order Policy"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "OBSERVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
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
                  "BRD-WS-07-R010.POLICY.OUTCOME.CONFORMING"
                ],
                "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                "source_type": "SOURCE_LITERAL",
                "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
              },
              "identifier": "BRD-WS-07-R010.POLICY.OUTCOME.CONFORMING",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                "source_lines": "L439-L442",
                "source_section": "15. Purchase Order Policy"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_OUTCOME",
                "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY.OUTCOME.CONFORMING",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_OUTCOME"
            },
            "policy": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                "source_type": "SOURCE_LITERAL",
                "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
              },
              "identifier": "BRD-WS-07-R010.POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                "source_lines": "L439-L442",
                "source_section": "15. Purchase Order Policy"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "policy_inputs": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                "source_type": "SOURCE_LITERAL",
                "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
              },
              "identifier": "BRD-WS-07-R010.POLICY_INPUTS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                "source_lines": "L439-L442",
                "source_section": "15. Purchase Order Policy"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY_INPUTS",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "policy_version": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
                "source_type": "SOURCE_LITERAL",
                "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
              },
              "identifier": "BRD-WS-07-R010.POLICY_VERSION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
                "source_lines": "L439-L442",
                "source_section": "15. Purchase Order Policy"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.BRD-WS-07-R010.BRD-WS-07-R010.POLICY_VERSION",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          }
        }
      ],
      "boundary_cases": [
        "No shortage creates no automatic Purchase Order; a shortage creates only its required coverage"
      ],
      "contract_ast_sha256": "619b323c459fdc40387948384b905d44d470f15167c27c5306667e3c391d7956",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R010",
      "criticality": "HIGH",
      "disposition": "COMPOUND_AST_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#15. Purchase Order Policy",
            "source_type": "SOURCE_LITERAL",
            "version": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608"
          },
          "identifier": "BRD-WS-07-R010.BRD-WS-07-R010.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R010.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
            "source_lines": "L439-L442",
            "source_section": "15. Purchase Order Policy"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-07-R010.BRD-WS-07-R010.BRD-WS-07-R010.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-07-R010.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.ORDER_ID",
          "FIELD.PRODUCT_ID",
          "FIELD.MISSING_QUANTITY",
          "FIELD.PURCHASE_ORDER_PRODUCT",
          "FIELD.PURCHASE_ORDER_QUANTITY",
          "FIELD.CALCULATION_RESULT"
        ],
        "producer": "BRD-WS-07-R010.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-07-R010.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.ORDER_ID",
          "FIELD.PRODUCT_ID",
          "FIELD.MISSING_QUANTITY",
          "FIELD.PURCHASE_ORDER_PRODUCT",
          "FIELD.PURCHASE_ORDER_QUANTITY",
          "FIELD.CALCULATION_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-07-R010.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-07-R010.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-07-R010.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-ED2B5DDD5594F0A41542",
        "P2C-C4-FX-DFBEC9100A5B19190033",
        "P2C-C4-FX-F765422DC37B7103B088"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "It buys excess quantity or a different Product"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-07-R010-O001",
          "obligation_text": "Purchase Order tự động: chỉ mua đúng số lượng còn thiếu"
        },
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-07-R010-O002",
          "obligation_text": "Purchase Order tự động: chỉ mua đúng Product cần thiết"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-07-R010.O1.1.PROCUREMENT_FEASIBLE"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-07-R010-O001"
        },
        {
          "assertion_ids": [
            "BRD-WS-07-R010.O2.1.POLICY_OUTCOME_EQUALS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-07-R010-O002"
        }
      ],
      "operator_composition": [
        "PROCUREMENT_FEASIBLE",
        "POLICY_OUTCOME_EQUALS"
      ],
      "positive_oracles": [
        "Purchase Order buys exactly the missing quantity of exactly the required Product"
      ],
      "preconditions": [
        "Missing quantity and required Product are calculated"
      ],
      "prohibitions": [
        "It buys excess quantity or a different Product"
      ],
      "requirement_id": "BRD-WS-07-R010",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-07.md",
        "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
        "source_lines": "L439-L442",
        "source_section": "15. Purchase Order Policy"
      },
      "source_statement": "Purchase Order tự động: - chỉ mua đúng số lượng còn thiếu - chỉ mua đúng Product cần thiết",
      "surrounding_source_context": "### BRD-WS-07-R010 — Purchase Order tự động: - chỉ mua đúng số lượng còn thiếu - chỉ mua đúng Product cần thiết"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R010",
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
        "BRD-WS-07-R010-AC001",
        "BRD-WS-07-R010-AC003",
        "BRD-WS-07-R010-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R010-O001",
      "obligation_text": "Purchase Order tự động: chỉ mua đúng số lượng còn thiếu"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-07-R010-AC002",
        "BRD-WS-07-R010-AC003",
        "BRD-WS-07-R010-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R010-O002",
      "obligation_text": "Purchase Order tự động: chỉ mua đúng Product cần thiết"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order tự động: - chỉ mua đúng số lượng còn thiếu - chỉ mua đúng Product cần thiết",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-010",
    "previous_temporary_key": "TMP-BRD-WS-07-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Purchase Order Policy",
    "source_context_sha256": "673e9ed2ed14ab642327d405c52df29ffef681ab912c9264a65ff4e2ac90d7dc",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "37f6c5d3c2173c41ab8c2ff13e4ae639542273aa15c687b24bc1d1bd09541608",
    "source_lines": "L12225-L13777",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R010"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_RULE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-07-R010",
  "title": "Purchase Order tự động: - chỉ mua đúng số lượng còn thiếu - chỉ mua đúng Product cần thiết",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R011 — Purchase Order tự động luôn tham chiếu Sales Order

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
      "requirement_id": "BRD-WS-07-R011",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "3d7ba11d8feee75d0a0c0c15aaaf636e619717c2ca75c1cf8644c9edbc15dbbb"
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
        "BRD-WS-07-R011-AC001",
        "BRD-WS-07-R011-AC002",
        "BRD-WS-07-R011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R011-O001",
      "obligation_text": "Purchase Order tự động luôn tham chiếu Sales Order"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Purchase Order tự động luôn tham chiếu Sales Order.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-011",
    "previous_temporary_key": "TMP-BRD-WS-07-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Purchase Order Relationship",
    "source_context_sha256": "377ba4c9e2d7228a57bd381962536a997d53127ff0180913ea416eff141893e5",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "3d7ba11d8feee75d0a0c0c15aaaf636e619717c2ca75c1cf8644c9edbc15dbbb",
    "source_lines": "L13779-L13854",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R011"
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
  "stable_id": "BRD-WS-07-R011",
  "title": "Purchase Order tự động luôn tham chiếu Sales Order",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R012 — Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nế…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-07-R012",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "ef3281d3aaae09e4ee5fcdfdd8de1633076e64e4a5c0e308159b542884c07e50"
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
        "BRD-WS-07-R012-AC001",
        "BRD-WS-07-R012-AC005",
        "BRD-WS-07-R012-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R012-O001",
      "obligation_text": "Nếu vẫn thất bại: Pause Fulfillment"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-07-R012-AC002",
        "BRD-WS-07-R012-AC005",
        "BRD-WS-07-R012-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R012-O002",
      "obligation_text": "Nếu vẫn thất bại: Notify Customer"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-07-R012-AC003",
        "BRD-WS-07-R012-AC005",
        "BRD-WS-07-R012-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R012-O003",
      "obligation_text": "Nếu vẫn thất bại: Retry theo chính sách"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-07-R012-AC004",
        "BRD-WS-07-R012-AC005",
        "BRD-WS-07-R012-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R012-O004",
      "obligation_text": "Nếu vẫn thất bại: Full Refund nếu cần"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R012 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R012-AC005"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R012-AC001",
        "BRD-WS-07-R012-AC002",
        "BRD-WS-07-R012-AC003",
        "BRD-WS-07-R012-AC004"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R012 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nếu cần",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-012",
    "previous_temporary_key": "TMP-BRD-WS-07-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Purchase Order Failure",
    "source_context_sha256": "722aeb6ff740623273c009b5eae31efeb0c9ca82e39bab1a0cb8cbec80ed1554",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "ef3281d3aaae09e4ee5fcdfdd8de1633076e64e4a5c0e308159b542884c07e50",
    "source_lines": "L13856-L14003",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R012"
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
  "stable_id": "BRD-WS-07-R012",
  "title": "Nếu vẫn thất bại: - Pause Fulfillment - Notify Customer - Retry theo chính sách - Full Refund nế…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R013 — Version 2.0 không hỗ trợ Customer tự chọn Product thay thế

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-07-R013",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version 2.0 không hỗ trợ Customer tự chọn Product thay thế.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-013",
    "previous_temporary_key": "TMP-BRD-WS-07-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Purchase Order Failure",
    "source_context_sha256": "722aeb6ff740623273c009b5eae31efeb0c9ca82e39bab1a0cb8cbec80ed1554",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "6e5dc4e1d71f94740f0368cb0c96eeff53a3729e966ed220d5fc043134cafa41",
    "source_lines": "L14005-L14065",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R013"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-07-R013",
  "title": "Version 2.0 không hỗ trợ Customer tự chọn Product thay thế",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R014 — Order luôn thuộc: Payment Owner

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Display or service actors do not become Order owner"
    ],
    "concrete_bindings": [
      {
        "actual_owner": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
            "source_type": "SOURCE_LITERAL",
            "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
          },
          "identifier": "BRD-WS-07-R014.OBSERVED.OWNER.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.ACTUAL_OWNER.ORIGIN",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
            "source_lines": "L556-L558",
            "source_section": "20. Order Ownership"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "OBSERVE.BRD-WS-07-R014.BRD-WS-07-R014.OBSERVED.OWNER.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "entity": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
            "source_type": "SOURCE_LITERAL",
            "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
          },
          "identifier": "BRD-WS-07-R014.ENTITY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.ENTITY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
            "source_lines": "L556-L558",
            "source_section": "20. Order Ownership"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R014.BRD-WS-07-R014.ENTITY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "expected_owner": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
            "source_type": "SOURCE_LITERAL",
            "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
          },
          "identifier": "BRD-WS-07-R014.CANONICAL.OWNER.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.EXPECTED_OWNER.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
            "source_lines": "L556-L558",
            "source_section": "20. Order Ownership"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R014.BRD-WS-07-R014.CANONICAL.OWNER.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "ownership_semantics": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-07-R014.OWNERSHIP_SEMANTICS"
            ],
            "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
            "source_type": "SOURCE_LITERAL",
            "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
          },
          "identifier": "BRD-WS-07-R014.OWNERSHIP_SEMANTICS",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.OWNERSHIP_SEMANTICS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
            "source_lines": "L556-L558",
            "source_section": "20. Order Ownership"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "RESOLVE.BRD-WS-07-R014.BRD-WS-07-R014.OWNERSHIP_SEMANTICS",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R014",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Order is assigned to a different owner"
    ],
    "operator_composition": [
      "OWNER_EQUALS"
    ],
    "positive_oracle": [
      "Order owner equals Payment Owner"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
      "source_lines": "L556-L558",
      "source_section": "20. Order Ownership"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
          "source_type": "SOURCE_LITERAL",
          "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
        },
        "identifier": "BRD-WS-07-R014.BRD-WS-07-R014.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-07-R014.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-07.md",
          "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
          "source_lines": "L556-L558",
          "source_section": "20. Order Ownership"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-07-R014.BRD-WS-07-R014.BRD-WS-07-R014.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-07-R014.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.ORDER_ID",
        "FIELD.PAYMENT_OWNER_ID",
        "FIELD.ORDER_OWNER_ID",
        "FIELD.OWNERSHIP_AUDIT"
      ],
      "producer": "BRD-WS-07-R014.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-07-R014.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.ORDER_ID",
        "FIELD.PAYMENT_OWNER_ID",
        "FIELD.ORDER_OWNER_ID",
        "FIELD.OWNERSHIP_AUDIT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-07-R014.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-07-R014.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-07-R014.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-07-R014-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS",
          "evaluator_consumed_bindings": [
            "actual_owner",
            "entity",
            "expected_owner",
            "ownership_semantics"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
              "source_type": "SOURCE_LITERAL",
              "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
            },
            "identifier": "BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
              "source_lines": "L556-L558",
              "source_section": "20. Order Ownership"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R014.BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
              "source_type": "SOURCE_LITERAL",
              "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
            },
            "identifier": "BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
              "source_lines": "L556-L558",
              "source_section": "20. Order Ownership"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BRD-WS-07-R014.BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_owner": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
                  "source_type": "SOURCE_LITERAL",
                  "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
                },
                "identifier": "BRD-WS-07-R014.OBSERVED.OWNER.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.ACTUAL_OWNER.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
                  "source_lines": "L556-L558",
                  "source_section": "20. Order Ownership"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-07-R014.BRD-WS-07-R014.OBSERVED.OWNER.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "entity": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
                  "source_type": "SOURCE_LITERAL",
                  "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
                },
                "identifier": "BRD-WS-07-R014.ENTITY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.ENTITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
                  "source_lines": "L556-L558",
                  "source_section": "20. Order Ownership"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R014.BRD-WS-07-R014.ENTITY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "expected_owner": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
                  "source_type": "SOURCE_LITERAL",
                  "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
                },
                "identifier": "BRD-WS-07-R014.CANONICAL.OWNER.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.EXPECTED_OWNER.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
                  "source_lines": "L556-L558",
                  "source_section": "20. Order Ownership"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R014.BRD-WS-07-R014.CANONICAL.OWNER.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "ownership_semantics": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-07-R014.OWNERSHIP_SEMANTICS"
                  ],
                  "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
                  "source_type": "SOURCE_LITERAL",
                  "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
                },
                "identifier": "BRD-WS-07-R014.OWNERSHIP_SEMANTICS",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.OWNERSHIP_SEMANTICS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
                  "source_lines": "L556-L558",
                  "source_section": "20. Order Ownership"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BRD-WS-07-R014.BRD-WS-07-R014.OWNERSHIP_SEMANTICS",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
                  "source_type": "SOURCE_LITERAL",
                  "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
                },
                "identifier": "BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
                  "source_lines": "L556-L558",
                  "source_section": "20. Order Ownership"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R014.BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
                  "source_type": "SOURCE_LITERAL",
                  "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
                },
                "identifier": "BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
                  "source_lines": "L556-L558",
                  "source_section": "20. Order Ownership"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-07-R014.BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
                "source_type": "SOURCE_LITERAL",
                "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
              },
              "identifier": "BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
                "source_lines": "L556-L558",
                "source_section": "20. Order Ownership"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R014.BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "OWNER_EQUALS"
          },
          "obligation_id": "BRD-WS-07-R014-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
              "source_type": "SOURCE_LITERAL",
              "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
            },
            "identifier": "BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
              "source_lines": "L556-L558",
              "source_section": "20. Order Ownership"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BRD-WS-07-R014.BRD-WS-07-R014.BRD-WS-07-R014.O1.1.OWNER_EQUALS.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "operator_id": "OWNER_EQUALS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_owner": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
                "source_type": "SOURCE_LITERAL",
                "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
              },
              "identifier": "BRD-WS-07-R014.OBSERVED.OWNER.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.ACTUAL_OWNER.ORIGIN",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
                "source_lines": "L556-L558",
                "source_section": "20. Order Ownership"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "OBSERVE.BRD-WS-07-R014.BRD-WS-07-R014.OBSERVED.OWNER.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "entity": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
                "source_type": "SOURCE_LITERAL",
                "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
              },
              "identifier": "BRD-WS-07-R014.ENTITY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.ENTITY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
                "source_lines": "L556-L558",
                "source_section": "20. Order Ownership"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R014.BRD-WS-07-R014.ENTITY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "expected_owner": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
                "source_type": "SOURCE_LITERAL",
                "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
              },
              "identifier": "BRD-WS-07-R014.CANONICAL.OWNER.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.EXPECTED_OWNER.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
                "source_lines": "L556-L558",
                "source_section": "20. Order Ownership"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R014.BRD-WS-07-R014.CANONICAL.OWNER.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "ownership_semantics": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-07-R014.OWNERSHIP_SEMANTICS"
                ],
                "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
                "source_type": "SOURCE_LITERAL",
                "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
              },
              "identifier": "BRD-WS-07-R014.OWNERSHIP_SEMANTICS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R014.O1.1.OWNER_EQUALS.OWNERSHIP_SEMANTICS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
                "source_lines": "L556-L558",
                "source_section": "20. Order Ownership"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BRD-WS-07-R014.BRD-WS-07-R014.OWNERSHIP_SEMANTICS",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            }
          }
        }
      ],
      "boundary_cases": [
        "Display or service actors do not become Order owner"
      ],
      "contract_ast_sha256": "eddc92ce92b49c80c1ce49466a333d191029bbd6bcb72b6ae638dacda479b4d8",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R014",
      "criticality": "CRITICAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#20. Order Ownership",
            "source_type": "SOURCE_LITERAL",
            "version": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5"
          },
          "identifier": "BRD-WS-07-R014.BRD-WS-07-R014.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R014.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
            "source_lines": "L556-L558",
            "source_section": "20. Order Ownership"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-07-R014.BRD-WS-07-R014.BRD-WS-07-R014.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-07-R014.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.ORDER_ID",
          "FIELD.PAYMENT_OWNER_ID",
          "FIELD.ORDER_OWNER_ID",
          "FIELD.OWNERSHIP_AUDIT"
        ],
        "producer": "BRD-WS-07-R014.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-07-R014.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.ORDER_ID",
          "FIELD.PAYMENT_OWNER_ID",
          "FIELD.ORDER_OWNER_ID",
          "FIELD.OWNERSHIP_AUDIT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-07-R014.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-07-R014.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-07-R014.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-736F885C6B8AFAC7179D",
        "P2C-C4-FX-CDB49272F3EBB78B9B35",
        "P2C-C4-FX-D6F5B9B238E6A232B9F1"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Order is assigned to a different owner"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-07-R014-O001",
          "obligation_text": "Order luôn thuộc: Payment Owner"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-07-R014.O1.1.OWNER_EQUALS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-07-R014-O001"
        }
      ],
      "operator_composition": [
        "OWNER_EQUALS"
      ],
      "positive_oracles": [
        "Order owner equals Payment Owner"
      ],
      "preconditions": [
        "The Payment Owner identity is known"
      ],
      "prohibitions": [
        "Order is assigned to a different owner"
      ],
      "requirement_id": "BRD-WS-07-R014",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-07.md",
        "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
        "source_lines": "L556-L558",
        "source_section": "20. Order Ownership"
      },
      "source_statement": "Order luôn thuộc: Payment Owner.",
      "surrounding_source_context": "### BRD-WS-07-R014 — Order luôn thuộc: Payment Owner"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R014",
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
        "BRD-WS-07-R014-AC001",
        "BRD-WS-07-R014-AC002",
        "BRD-WS-07-R014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R014-O001",
      "obligation_text": "Order luôn thuộc: Payment Owner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R014 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Order luôn thuộc: Payment Owner.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-014",
    "previous_temporary_key": "TMP-BRD-WS-07-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Order Ownership",
    "source_context_sha256": "939e7e3f383f58df388dcd34c57f3cf691c5f84fd26da559d9ff391106fee0f1",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "66f66e9f60de592f62d2156dc144fe2aa635f01f32093874a105f4674f89b3e5",
    "source_lines": "L14067-L15025",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R014"
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
  "stable_id": "BRD-WS-07-R014",
  "title": "Order luôn thuộc: Payment Owner",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R015 — Không cho phép sửa: - Product

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Quantity or other separately permitted fields are outside this specific prohibition"
    ],
    "concrete_bindings": [
      {
        "after_hash": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
            "source_type": "SOURCE_LITERAL",
            "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
          },
          "identifier": "BRD-WS-07-R015.AFTER_HASH",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.AFTER_HASH.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
            "source_lines": "L598-L600",
            "source_section": "22. Order Modification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "HASH",
            "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.AFTER_HASH",
            "version": "1.0.0"
          },
          "semantic_type": "HASH"
        },
        "audit_record": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
            "source_type": "SOURCE_LITERAL",
            "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
          },
          "identifier": "BRD-WS-07-R015.AUDIT_RECORD",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.AUDIT_RECORD.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
            "source_lines": "L598-L600",
            "source_section": "22. Order Modification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.AUDIT_RECORD",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "before_hash": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
            "source_type": "SOURCE_LITERAL",
            "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
          },
          "identifier": "BRD-WS-07-R015.BEFORE_HASH",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.BEFORE_HASH.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
            "source_lines": "L598-L600",
            "source_section": "22. Order Modification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "HASH",
            "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.BEFORE_HASH",
            "version": "1.0.0"
          },
          "semantic_type": "HASH"
        },
        "immutability_boundary": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
            "source_type": "SOURCE_LITERAL",
            "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
          },
          "identifier": "BRD-WS-07-R015.IMMUTABILITY_BOUNDARY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.IMMUTABILITY_BOUNDARY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
            "source_lines": "L598-L600",
            "source_section": "22. Order Modification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.IMMUTABILITY_BOUNDARY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "protected_fields": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "FIELD.ORDER_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.ORDER_ID",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "FIELD.PRODUCT_ID_BEFORE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.2",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_BEFORE",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "FIELD.PRODUCT_ID_AFTER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.3",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_AFTER",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "FIELD.MODIFICATION_RESULT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.4",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.MODIFICATION_RESULT",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "FIELD.AUDIT_RECORD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.5",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.AUDIT_RECORD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
            "source_lines": "L598-L600",
            "source_section": "22. Order Modification"
          },
          "semantic_type": "SET_OF<FIELD_ID>"
        },
        "required_fields": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "FIELD.ORDER_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.ORDER_ID",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "FIELD.PRODUCT_ID_BEFORE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_BEFORE",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "FIELD.PRODUCT_ID_AFTER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_AFTER",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "FIELD.MODIFICATION_RESULT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.MODIFICATION_RESULT",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "FIELD.AUDIT_RECORD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.5",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.AUDIT_RECORD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
            "source_lines": "L598-L600",
            "source_section": "22. Order Modification"
          },
          "semantic_type": "SET_OF<FIELD_ID>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R015",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "The Product reference is modified in place"
    ],
    "operator_composition": [
      "AUDIT_IMMUTABLE"
    ],
    "positive_oracle": [
      "The Product reference remains unchanged"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
      "source_lines": "L598-L600",
      "source_section": "22. Order Modification"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
          "source_type": "SOURCE_LITERAL",
          "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
        },
        "identifier": "BRD-WS-07-R015.BRD-WS-07-R015.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-07-R015.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-07.md",
          "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
          "source_lines": "L598-L600",
          "source_section": "22. Order Modification"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-07-R015.BRD-WS-07-R015.BRD-WS-07-R015.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-07-R015.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.ORDER_ID",
        "FIELD.PRODUCT_ID_BEFORE",
        "FIELD.PRODUCT_ID_AFTER",
        "FIELD.MODIFICATION_RESULT",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "BRD-WS-07-R015.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-07-R015.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.ORDER_ID",
        "FIELD.PRODUCT_ID_BEFORE",
        "FIELD.PRODUCT_ID_AFTER",
        "FIELD.MODIFICATION_RESULT",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "BRD-WS-07-R015.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-07-R015.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-07-R015.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-07-R015-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE",
          "evaluator_consumed_bindings": [
            "after_hash",
            "audit_record",
            "before_hash",
            "immutability_boundary",
            "protected_fields",
            "required_fields"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
              "source_type": "SOURCE_LITERAL",
              "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
            },
            "identifier": "BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
              "source_lines": "L598-L600",
              "source_section": "22. Order Modification"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R015.BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
              "source_type": "SOURCE_LITERAL",
              "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
            },
            "identifier": "BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
              "source_lines": "L598-L600",
              "source_section": "22. Order Modification"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "after_hash": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                },
                "identifier": "BRD-WS-07-R015.AFTER_HASH",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.AFTER_HASH.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                  "source_lines": "L598-L600",
                  "source_section": "22. Order Modification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "HASH",
                  "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.AFTER_HASH",
                  "version": "1.0.0"
                },
                "semantic_type": "HASH"
              },
              "audit_record": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                },
                "identifier": "BRD-WS-07-R015.AUDIT_RECORD",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.AUDIT_RECORD.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                  "source_lines": "L598-L600",
                  "source_section": "22. Order Modification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.AUDIT_RECORD",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "before_hash": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                },
                "identifier": "BRD-WS-07-R015.BEFORE_HASH",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.BEFORE_HASH.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                  "source_lines": "L598-L600",
                  "source_section": "22. Order Modification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "HASH",
                  "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.BEFORE_HASH",
                  "version": "1.0.0"
                },
                "semantic_type": "HASH"
              },
              "immutability_boundary": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                },
                "identifier": "BRD-WS-07-R015.IMMUTABILITY_BOUNDARY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.IMMUTABILITY_BOUNDARY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                  "source_lines": "L598-L600",
                  "source_section": "22. Order Modification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.IMMUTABILITY_BOUNDARY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "protected_fields": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                    },
                    "identifier": "FIELD.ORDER_ID",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                      "source_lines": "L598-L600",
                      "source_section": "22. Order Modification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.ORDER_ID",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                    },
                    "identifier": "FIELD.PRODUCT_ID_BEFORE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.2",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                      "source_lines": "L598-L600",
                      "source_section": "22. Order Modification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_BEFORE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                    },
                    "identifier": "FIELD.PRODUCT_ID_AFTER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.3",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                      "source_lines": "L598-L600",
                      "source_section": "22. Order Modification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_AFTER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                    },
                    "identifier": "FIELD.MODIFICATION_RESULT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.4",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                      "source_lines": "L598-L600",
                      "source_section": "22. Order Modification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.MODIFICATION_RESULT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                    },
                    "identifier": "FIELD.AUDIT_RECORD",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.5",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                      "source_lines": "L598-L600",
                      "source_section": "22. Order Modification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.AUDIT_RECORD",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                  "source_lines": "L598-L600",
                  "source_section": "22. Order Modification"
                },
                "semantic_type": "SET_OF<FIELD_ID>"
              },
              "required_fields": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                    },
                    "identifier": "FIELD.ORDER_ID",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                      "source_lines": "L598-L600",
                      "source_section": "22. Order Modification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.ORDER_ID",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                    },
                    "identifier": "FIELD.PRODUCT_ID_BEFORE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                      "source_lines": "L598-L600",
                      "source_section": "22. Order Modification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_BEFORE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                    },
                    "identifier": "FIELD.PRODUCT_ID_AFTER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                      "source_lines": "L598-L600",
                      "source_section": "22. Order Modification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_AFTER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                    },
                    "identifier": "FIELD.MODIFICATION_RESULT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                      "source_lines": "L598-L600",
                      "source_section": "22. Order Modification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.MODIFICATION_RESULT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                      "source_type": "SOURCE_LITERAL",
                      "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                    },
                    "identifier": "FIELD.AUDIT_RECORD",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.5",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-07.md",
                      "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                      "source_lines": "L598-L600",
                      "source_section": "22. Order Modification"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.AUDIT_RECORD",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                  "source_lines": "L598-L600",
                  "source_section": "22. Order Modification"
                },
                "semantic_type": "SET_OF<FIELD_ID>"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                },
                "identifier": "BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                  "source_lines": "L598-L600",
                  "source_section": "22. Order Modification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                  "source_type": "SOURCE_LITERAL",
                  "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                },
                "identifier": "BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-07.md",
                  "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                  "source_lines": "L598-L600",
                  "source_section": "22. Order Modification"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "OBSERVE.BRD-WS-07-R015.BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-07-R015.BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "AUDIT_IMMUTABLE"
          },
          "obligation_id": "BRD-WS-07-R015-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
              "source_type": "SOURCE_LITERAL",
              "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
            },
            "identifier": "BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-07.md",
              "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
              "source_lines": "L598-L600",
              "source_section": "22. Order Modification"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-07-R015.BRD-WS-07-R015.BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "operator_id": "AUDIT_IMMUTABLE",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "after_hash": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "BRD-WS-07-R015.AFTER_HASH",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.AFTER_HASH.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "HASH",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.AFTER_HASH",
                "version": "1.0.0"
              },
              "semantic_type": "HASH"
            },
            "audit_record": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "BRD-WS-07-R015.AUDIT_RECORD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.AUDIT_RECORD.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.AUDIT_RECORD",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "before_hash": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "BRD-WS-07-R015.BEFORE_HASH",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.BEFORE_HASH.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "HASH",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.BEFORE_HASH",
                "version": "1.0.0"
              },
              "semantic_type": "HASH"
            },
            "immutability_boundary": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                "source_type": "SOURCE_LITERAL",
                "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
              },
              "identifier": "BRD-WS-07-R015.IMMUTABILITY_BOUNDARY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.IMMUTABILITY_BOUNDARY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BRD-WS-07-R015.BRD-WS-07-R015.IMMUTABILITY_BOUNDARY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "protected_fields": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                  },
                  "identifier": "FIELD.ORDER_ID",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                    "source_lines": "L598-L600",
                    "source_section": "22. Order Modification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.ORDER_ID",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                  },
                  "identifier": "FIELD.PRODUCT_ID_BEFORE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.2",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                    "source_lines": "L598-L600",
                    "source_section": "22. Order Modification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_BEFORE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                  },
                  "identifier": "FIELD.PRODUCT_ID_AFTER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.3",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                    "source_lines": "L598-L600",
                    "source_section": "22. Order Modification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_AFTER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                  },
                  "identifier": "FIELD.MODIFICATION_RESULT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.4",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                    "source_lines": "L598-L600",
                    "source_section": "22. Order Modification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.MODIFICATION_RESULT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                  },
                  "identifier": "FIELD.AUDIT_RECORD",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.5",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                    "source_lines": "L598-L600",
                    "source_section": "22. Order Modification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.AUDIT_RECORD",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "semantic_type": "SET_OF<FIELD_ID>"
            },
            "required_fields": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                  },
                  "identifier": "FIELD.ORDER_ID",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                    "source_lines": "L598-L600",
                    "source_section": "22. Order Modification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.ORDER_ID",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                  },
                  "identifier": "FIELD.PRODUCT_ID_BEFORE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                    "source_lines": "L598-L600",
                    "source_section": "22. Order Modification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_BEFORE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                  },
                  "identifier": "FIELD.PRODUCT_ID_AFTER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                    "source_lines": "L598-L600",
                    "source_section": "22. Order Modification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.PRODUCT_ID_AFTER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                  },
                  "identifier": "FIELD.MODIFICATION_RESULT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                    "source_lines": "L598-L600",
                    "source_section": "22. Order Modification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.MODIFICATION_RESULT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
                    "source_type": "SOURCE_LITERAL",
                    "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
                  },
                  "identifier": "FIELD.AUDIT_RECORD",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.5",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-07.md",
                    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                    "source_lines": "L598-L600",
                    "source_section": "22. Order Modification"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-WS-07-R015.FIELD.AUDIT_RECORD",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-07.md",
                "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
                "source_lines": "L598-L600",
                "source_section": "22. Order Modification"
              },
              "semantic_type": "SET_OF<FIELD_ID>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Quantity or other separately permitted fields are outside this specific prohibition"
      ],
      "contract_ast_sha256": "3b6d543bfc319fc8512c6619c61c5cad49452f6961215b5293dc10d38e70d5e7",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R015",
      "criticality": "HIGH",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-07.md#22. Order Modification",
            "source_type": "SOURCE_LITERAL",
            "version": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5"
          },
          "identifier": "BRD-WS-07-R015.BRD-WS-07-R015.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-07-R015.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-07.md",
            "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
            "source_lines": "L598-L600",
            "source_section": "22. Order Modification"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-07-R015.BRD-WS-07-R015.BRD-WS-07-R015.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-07-R015.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.ORDER_ID",
          "FIELD.PRODUCT_ID_BEFORE",
          "FIELD.PRODUCT_ID_AFTER",
          "FIELD.MODIFICATION_RESULT",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "BRD-WS-07-R015.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-07-R015.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.ORDER_ID",
          "FIELD.PRODUCT_ID_BEFORE",
          "FIELD.PRODUCT_ID_AFTER",
          "FIELD.MODIFICATION_RESULT",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "BRD-WS-07-R015.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-07-R015.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-07-R015.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-2B59EA732D4FC23D9076",
        "P2C-C4-FX-E4A31B3383B6A101B385",
        "P2C-C4-FX-AE4A749C046D71483BB3"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "The Product reference is modified in place"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-07-R015-O001",
          "obligation_text": "Không cho phép sửa: - Product"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-07-R015.O1.1.AUDIT_IMMUTABLE"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-07-R015-O001"
        }
      ],
      "operator_composition": [
        "AUDIT_IMMUTABLE"
      ],
      "positive_oracles": [
        "The Product reference remains unchanged"
      ],
      "preconditions": [
        "The Order and current Product reference exist"
      ],
      "prohibitions": [
        "The Product reference is modified in place"
      ],
      "requirement_id": "BRD-WS-07-R015",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-07.md",
        "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
        "source_lines": "L598-L600",
        "source_section": "22. Order Modification"
      },
      "source_statement": "Không cho phép sửa: - Product",
      "surrounding_source_context": "### BRD-WS-07-R015 — Không cho phép sửa: - Product"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-07-R015",
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
        "BRD-WS-07-R015-AC001",
        "BRD-WS-07-R015-AC002",
        "BRD-WS-07-R015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R015-O001",
      "obligation_text": "Không cho phép sửa: - Product"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cho phép sửa: - Product",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-015",
    "previous_temporary_key": "TMP-BRD-WS-07-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "33ea05b4955d1761e637512672f1a6917fe74b07e042e6fb9c97d00c0d9d06c5",
    "source_lines": "L15027-L17071",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R015"
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
  "stable_id": "BRD-WS-07-R015",
  "title": "Không cho phép sửa: - Product",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R016 — Không cho phép sửa: - Quantity

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
      "requirement_id": "BRD-WS-07-R016",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "8f1d6b0d78b173a570926aa9a712baf3dce467ea86c24dd2e96972596baa16df"
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
        "BRD-WS-07-R016-AC001",
        "BRD-WS-07-R016-AC002",
        "BRD-WS-07-R016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R016-O001",
      "obligation_text": "Không cho phép sửa: - Quantity"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cho phép sửa: - Quantity",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-016",
    "previous_temporary_key": "TMP-BRD-WS-07-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "8f1d6b0d78b173a570926aa9a712baf3dce467ea86c24dd2e96972596baa16df",
    "source_lines": "L17073-L17148",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R016"
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
  "stable_id": "BRD-WS-07-R016",
  "title": "Không cho phép sửa: - Quantity",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R017 — Không cho phép sửa: - Currency

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
      "requirement_id": "BRD-WS-07-R017",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "4d91dc538129691177083e22367287148c84e996b4786291bc265248c48e76a2"
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
        "BRD-WS-07-R017-AC001",
        "BRD-WS-07-R017-AC002",
        "BRD-WS-07-R017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R017-O001",
      "obligation_text": "Không cho phép sửa: - Currency"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R017 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R017 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R017 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R017-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R017-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R017 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cho phép sửa: - Currency",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-017",
    "previous_temporary_key": "TMP-BRD-WS-07-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "4d91dc538129691177083e22367287148c84e996b4786291bc265248c48e76a2",
    "source_lines": "L17150-L17258",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R017"
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
  "stable_id": "BRD-WS-07-R017",
  "title": "Không cho phép sửa: - Currency",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R018 — Không cho phép sửa: - Promotion

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
      "requirement_id": "BRD-WS-07-R018",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "02ab776ccf9c1be8db47a94cc9b328cc4bed865c14fd981592385d11f17b3d87"
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
        "BRD-WS-07-R018-AC001",
        "BRD-WS-07-R018-AC002",
        "BRD-WS-07-R018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R018-O001",
      "obligation_text": "Không cho phép sửa: - Promotion"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cho phép sửa: - Promotion",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-018",
    "previous_temporary_key": "TMP-BRD-WS-07-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "02ab776ccf9c1be8db47a94cc9b328cc4bed865c14fd981592385d11f17b3d87",
    "source_lines": "L17260-L17335",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R018"
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
  "stable_id": "BRD-WS-07-R018",
  "title": "Không cho phép sửa: - Promotion",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R019 — Không cho phép sửa: - Price

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
      "requirement_id": "BRD-WS-07-R019",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "df48a1c8dcbd04fdadd8b20c1f860cfb069f23fb68169d1ea3323e9d0deeab3e"
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
        "BRD-WS-07-R019-AC001",
        "BRD-WS-07-R019-AC002",
        "BRD-WS-07-R019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R019-O001",
      "obligation_text": "Không cho phép sửa: - Price"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R019 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R019 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R019 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R019-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R019-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R019 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cho phép sửa: - Price",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-019",
    "previous_temporary_key": "TMP-BRD-WS-07-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "df48a1c8dcbd04fdadd8b20c1f860cfb069f23fb68169d1ea3323e9d0deeab3e",
    "source_lines": "L17337-L17445",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R019"
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
  "stable_id": "BRD-WS-07-R019",
  "title": "Không cho phép sửa: - Price",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R020 — Mọi thay đổi đều phải Audit

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
      "requirement_id": "BRD-WS-07-R020",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "cd9db4c12934e25d077f0a1b9f1a7fcb3f5f3273ae2e35dd86549a876ba70fb1"
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
        "BRD-WS-07-R020-AC001",
        "BRD-WS-07-R020-AC002",
        "BRD-WS-07-R020-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-07-R020-O001",
      "obligation_text": "Mọi thay đổi đều phải Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R020 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R020 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R020 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R020-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-07-R020-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-07-R020 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thay đổi đều phải Audit.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-020",
    "previous_temporary_key": "TMP-BRD-WS-07-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Order Modification",
    "source_context_sha256": "49b3e8f656c364bf08dada0a7ea8b50193274b34c461fcbd60a522cd7aca444b",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "cd9db4c12934e25d077f0a1b9f1a7fcb3f5f3273ae2e35dd86549a876ba70fb1",
    "source_lines": "L17447-L17555",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R020"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-07-R020",
  "title": "Mọi thay đổi đều phải Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R021 — Version sau sẽ bổ sung: - Cart Recovery

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-07-R021",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Cart Recovery",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-021",
    "previous_temporary_key": "TMP-BRD-WS-07-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "eb33243acc6025873e06f817782746ba0f0c757e0210acedca0492057d5fe63e",
    "source_lines": "L17557-L17615",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R021"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R021",
  "title": "Version sau sẽ bổ sung: - Cart Recovery",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R022 — Version sau sẽ bổ sung: - Product Replacement Suggestion

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-07-R022",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Product Replacement Suggestion",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-022",
    "previous_temporary_key": "TMP-BRD-WS-07-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "52cdec10d15c74ea63d97325dd38bf25f02b47c38f10c2f867ac4cd6b69d053d",
    "source_lines": "L17617-L17675",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R022"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R022",
  "title": "Version sau sẽ bổ sung: - Product Replacement Suggestion",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R023 — Version sau sẽ bổ sung: - Split Payment

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-07-R023",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Split Payment",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-023",
    "previous_temporary_key": "TMP-BRD-WS-07-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "9656f26b2e05d6a6bd6c61e25b7c10e51a237d042ae05a24265ed3f09825a791",
    "source_lines": "L17677-L17735",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R023"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R023",
  "title": "Version sau sẽ bổ sung: - Split Payment",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R024 — Version sau sẽ bổ sung: - Multiple Payment

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-07-R024",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Multiple Payment",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-024",
    "previous_temporary_key": "TMP-BRD-WS-07-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "2b8170e032b5f2f10cabf09a3b6a053d696e07153d56fdb2769ede9659e32461",
    "source_lines": "L17737-L17795",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R024"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R024",
  "title": "Version sau sẽ bổ sung: - Multiple Payment",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R025 — Version sau sẽ bổ sung: - Smart Procurement

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-07-R025",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Smart Procurement",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-025",
    "previous_temporary_key": "TMP-BRD-WS-07-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "1c59f317bcf055e2ae233e2bdb47a166a99aa5d1f087259dd28d8855c1fddc6d",
    "source_lines": "L17797-L17855",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R025"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R025",
  "title": "Version sau sẽ bổ sung: - Smart Procurement",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R026 — Version sau sẽ bổ sung: - AI Procurement

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-07-R026",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - AI Procurement",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-026",
    "previous_temporary_key": "TMP-BRD-WS-07-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "e767cc5f84e98217900b94ca5cd756f6f89a19237891e44bfad088ce7b1c746f",
    "source_lines": "L17857-L17915",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R026"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R026",
  "title": "Version sau sẽ bổ sung: - AI Procurement",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-07-R027 — Version sau sẽ bổ sung: - Bulk Procurement Recommendation

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-07-R027",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version sau sẽ bổ sung: - Bulk Procurement Recommendation",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-07-027",
    "previous_temporary_key": "TMP-BRD-WS-07-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Deferred Scope",
    "source_context_sha256": "aa9fcaee6ff8a1abbb7bd53f9886bce79efae987261ac2ed3415c1e995d79cee",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "581fafe2166fdf5dc24d879c7e40364d11e86c2a37ace2e8f80c93e5d7d40821",
    "source_lines": "L17917-L17975",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-07-R027"
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
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-07-R027",
  "title": "Version sau sẽ bổ sung: - Bulk Procurement Recommendation",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-001 — Sales Order và Purchase Order là hai Business Object độc lập

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
      "requirement_id": "EP-07-001",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "a757f7faa5b59aeea1e518c3dc45113316dea092028d2141e215f3d0fb7f6717"
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
        "EP-07-001-AC001",
        "EP-07-001-AC002",
        "EP-07-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-001-O001",
      "obligation_text": "Sales Order và Purchase Order là hai Business Object độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sales Order và Purchase Order là hai Business Object độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-001",
    "source_context_sha256": "7a16be798c8f208cd58624aa19131a2c51820c4594aaf9a4cbd3b90281928592",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "a757f7faa5b59aeea1e518c3dc45113316dea092028d2141e215f3d0fb7f6717",
    "source_lines": "L17977-L18052",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-07-001"
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
  "stable_id": "EP-07-001",
  "title": "Sales Order và Purchase Order là hai Business Object độc lập",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-002 — Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement

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
      "requirement_id": "EP-07-002",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "8c7cbcbe7c9d581c8707c05331bfff591c0816b0a4f4c9ed9a7b913316bf6586"
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
        "EP-07-002-AC001",
        "EP-07-002-AC002",
        "EP-07-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-002-O001",
      "obligation_text": "Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-002 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-07-002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-07-002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-002 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-002",
    "source_context_sha256": "1569316653d8164e447873ad46bedd4b537e902397ef338cdc4165785959f9ac",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "8c7cbcbe7c9d581c8707c05331bfff591c0816b0a4f4c9ed9a7b913316bf6586",
    "source_lines": "L18054-L18162",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-07-002"
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
  "stable_id": "EP-07-002",
  "title": "Checkout chỉ xác nhận khả năng Procurement, không thực hiện Procurement",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-003 — Inventory Reservation phải đồng bộ với Price Reservation

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
      "requirement_id": "EP-07-003",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "4c14ddf1a9bc74cce91573fa86847a3cf489a25cc976ccb4e3c7b610cc3f1b11"
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
        "EP-07-003-AC001",
        "EP-07-003-AC002",
        "EP-07-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-003-O001",
      "obligation_text": "Inventory Reservation phải đồng bộ với Price Reservation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-07-003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-07-003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-003 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Inventory Reservation phải đồng bộ với Price Reservation.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-003",
    "source_context_sha256": "a35edd96208b2e158a41db196e6abef502ea3f6344cc4e34daf7979aa26bc0ad",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "4c14ddf1a9bc74cce91573fa86847a3cf489a25cc976ccb4e3c7b610cc3f1b11",
    "source_lines": "L18164-L18272",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-07-003"
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
  "stable_id": "EP-07-003",
  "title": "Inventory Reservation phải đồng bộ với Price Reservation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-004 — Fulfillment Assignment là Capability của Fulfillment Domain

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
      "requirement_id": "EP-07-004",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "340b223c31df400742422c6bf61d39b5582b131c917146b982c2af1689e0c428"
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
        "EP-07-004-AC001",
        "EP-07-004-AC002",
        "EP-07-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-004-O001",
      "obligation_text": "Fulfillment Assignment là Capability của Fulfillment Domain"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-07-004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-07-004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Fulfillment Assignment là Capability của Fulfillment Domain.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-004",
    "source_context_sha256": "76956279943f9abd9e06fc1248ff1613371340d76ab58e023e1861d9520f1995",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "340b223c31df400742422c6bf61d39b5582b131c917146b982c2af1689e0c428",
    "source_lines": "L18274-L18386",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-07-004"
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
  "stable_id": "EP-07-004",
  "title": "Fulfillment Assignment là Capability của Fulfillment Domain",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-005 — Mọi Product Item phải truy vết được: Purchase Order ↓ Inventory ↓ Allocation ↓ Sales Order ↓ Cus…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007",
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-07-005",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "9f045a04dcb7c17a39cf088af65f329518eea3e17ac2370f4e5d867367b3581f"
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
        "EP-07-005-AC001",
        "EP-07-005-AC002",
        "EP-07-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-005-O001",
      "obligation_text": "Mọi Product Item phải truy vết được: Purchase Order ↓ Inventory ↓ Allocation ↓ Sales Order ↓ Customer"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-07-005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-07-005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-07-005 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Product Item phải truy vết được: Purchase Order ↓ Inventory ↓ Allocation ↓ Sales Order ↓ Customer",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007",
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-005",
    "source_context_sha256": "dd0222a62fc1d8a4c95c720cc15fb7ccccc4a657bef21b7171e0018d65bffc55",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "9f045a04dcb7c17a39cf088af65f329518eea3e17ac2370f4e5d867367b3581f",
    "source_lines": "L18388-L18502",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-07-005"
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
  "stable_id": "EP-07-005",
  "title": "Mọi Product Item phải truy vết được: Purchase Order ↓ Inventory ↓ Allocation ↓ Sales Order ↓ Cus…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-07-006 — Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot

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
      "requirement_id": "EP-07-006",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "source_fingerprint": "259637d87e826dd20ea2de1d6cef23d6547fe67c6c6db14a6959c7a55e206684"
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
        "EP-07-006-AC001",
        "EP-07-006-AC002",
        "EP-07-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-07-006-O001",
      "obligation_text": "Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-07-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-07-006",
    "source_context_sha256": "6544ba81f342311f094fa231c838c86d40cc4782c405ad435ad9189adcce58c3",
    "source_document": "docs/BRD/BRD-WS-07.md",
    "source_fingerprint": "259637d87e826dd20ea2de1d6cef23d6547fe67c6c6db14a6959c7a55e206684",
    "source_lines": "L18504-L18579",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-07-006"
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
  "stable_id": "EP-07-006",
  "title": "Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
