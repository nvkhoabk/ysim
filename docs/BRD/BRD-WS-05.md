---
document_code: "BRD-WS-05"
document_id: "BRD-WS-05"
title: "Pricing, Commercial Policy & Revenue Model"
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

# BRD Workshop 05

# Pricing, Commercial Policy & Revenue Model

---

# 1. Workshop Objective

Workshop này xác định mô hình Pricing, Commercial Policy và Revenue Model của YSim.

Workshop bao gồm:

- Price Book
- Commercial Agreement
- Cost Model
- Multi-Currency
- Exchange Rate
- Commission
- Revenue Sharing
- Snapshot Pricing
- Price Reservation
- Commercial Consistency
- Price Change Set

Workshop này là Foundation cho:

- Promotion
- Coupon
- Checkout
- Payment
- Settlement
- Financial Event
- Reporting

---

# 2. Business Objects Introduced

| Business Object | Status |
|-----------------|--------|
| Price Book | NEW |
| Price Change Set | NEW |
| Commercial Agreement | NEW |
| Commercial Snapshot | NEW |
| Payment Session | NEW |
| Price Reservation | NEW |
| Revenue Sharing | NEW |
| Commission Snapshot | NEW |
| Exchange Rate Policy | NEW |
| Currency Policy | NEW |

---

# 3. Commercial Domain

YSim tách riêng Product Domain và Commercial Domain.

## Product Domain

- Product
- Catalog
- Supplier
- Inventory
- Fulfillment

## Commercial Domain

- Pricing
- Price Book
- Commercial Agreement
- Promotion
- Commission
- Revenue Sharing
- Settlement
- Credit
- Wallet

Product trả lời:

> Bán cái gì.

Commercial trả lời:

> Bán với điều kiện thương mại nào.

---

# 4. Pricing Ownership

Price không thuộc Product.

Price thuộc Catalog.

Product chỉ lưu các thông tin tham khảo:

- Supplier MSRP
- Supplier Unit Price
- Suggested Retail Price
- Reference Price

Giá bán thực tế được quản lý thông qua Price Book.

---

# 5. Reference Price

Khi tạo Master Product từ Supplier Product, hệ thống cần lưu:

- Supplier Unit Price
- Supplier MSRP
- Supplier Discount Price
- Supplier Discount Rate
- Supplier Tax
- Supplier Fee
- Suggested Retail Price

Reference Price chỉ phục vụ tham khảo.

Không phải Selling Price.

---

# 6. Cost Model

Cost được xác định theo Distribution Network.

Ví dụ:

```text
Supplier

↓

YSim

↓

ABC Travel

↓

Agency

↓

Customer
```

Master Cost của YSim là giá mua từ Supplier.

Cost của ABC Travel là giá YSim bán cho ABC Travel.

Cost của Agency là giá ABC Travel bán cho Agency.

Cost có thể bao gồm:

- Product Cost
- Tax
- Fee
- Procurement Cost

Cost phải hỗ trợ bóc tách phục vụ Settlement.

---

# 7. Price Book

YSim sử dụng Price Book.

Price Book xác định:

- Selling Price
- Currency
- Formula
- Effective Date
- Expiry Date

Một Organization có thể có nhiều Price Book.

Ví dụ:

- Retail
- Corporate
- VIP
- Promotion

---

# 8. Payment Owner

Chỉ Payment Owner mới được phép tạo hoặc chỉnh sửa Price Book.

Payment Owner là Organization nhận tiền từ Customer.

Trong phiên bản 2.0:

- Payment Owner được cố định theo Commercial Agreement.
- Không hỗ trợ thay đổi theo Campaign.
- Nếu thanh toán tiền mặt thì Payment Owner là Organization sở hữu Storefront.

---

# 9. Multi-Currency Price Book

Price Book hỗ trợ nhiều Currency.

Mỗi Price Book phải có:

- Base Currency

Ngoài Base Currency có thể khai báo:

- USD
- EUR
- VND
- JPY
- ...

Các Currency phụ có thể:

- nhập thủ công
- kế thừa Parent
- tính theo Exchange Rate
- Override

---

# 10. Currency Governance

Currency là một phần của Commercial Agreement.

Parent và Child phải thống nhất:

- Settlement Currency
- Exchange Rate Source
- Effective Date
- Exchange Policy

Exchange Rate có thể tham khảo từ:

- ECB
- Vietcombank
- Manual
- Internal Source

---

# 11. Margin Policy

Partner được phép thiết lập giá bán.

Nếu:

Selling Price < Cost

hoặc

Selling Price thấp hơn Parent Recommendation

thì hệ thống phải:

- Warning
- Reason Required
- Parent Notification
- Audit

Nếu giá giảm do:

- Coupon
- Promotion
- Campaign

thì không xem là vi phạm.

---

# 12. Price Change Set

Mọi thay đổi Price Book phải được thực hiện thông qua Price Change Set.

Price Change Set hỗ trợ:

- Bulk Edit
- Bulk Review
- Bulk Approve
- Bulk Publish
- Bulk Archive
- Rollback

UI ưu tiên dạng Table View.

Cho phép:

- Filter
- Multi Select
- Select by Region
- Select by Category
- Create From Parent Catalog

---

# 13. Commission

Commission tách khỏi Pricing.

Commission chỉ áp dụng cho các thực thể trực tiếp tham gia bán hàng.

Ví dụ:

- Sales Department
- Sales User
- Collaborator
- Agency

Commission được Snapshot ngay khi Item được bán.

Portal chỉ hiển thị:

Estimated Commission.

Settlement mới tạo:

Confirmed Commission.

Commission được tính sau khi trừ:

- Tax
- Fee

---

# 14. Revenue Sharing

Revenue Sharing độc lập với Commission.

Revenue Sharing mô tả việc phân chia doanh thu giữa các Organization.

Ví dụ:

Customer

↓

Payment Gateway Fee

↓

Tax

↓

Net Revenue

↓

Payment Owner

↓

Parent

↓

YSim

↓

Supplier

Commission không thuộc Revenue Sharing.

---

# 15. Commercial Agreement

Commercial Agreement là Business Object trung tâm của Commercial Domain.

Commercial Agreement quản lý:

- Payment Owner
- Currency
- Exchange Policy
- Price Policy
- Cost Policy
- Margin Policy
- Commission Policy
- Revenue Sharing Policy
- Settlement Cycle
- Credit Policy
- Payment Policy
- Support Policy

Commercial Agreement là Business Configuration.

---

# 16. Dynamic Pricing

Version 2.0 hỗ trợ Pricing Formula.

Ví dụ:

- Cost + 20%
- Parent Price + 5%
- Reference Price - 10%
- Fixed Price

Không triển khai AI Pricing.

---

# 17. Snapshot Pricing

Snapshot Pricing lưu toàn bộ Commercial Context.

Bao gồm:

- Product Version
- Product Item
- Price Book Version
- Commercial Agreement Version
- Selling Price
- Distribution Cost
- Currency
- Exchange Rate
- Tax
- Fee
- Promotion
- Coupon
- Commission Policy
- Revenue Sharing Policy
- Settlement Policy

Mỗi tầng Distribution chỉ xem được Cost của mình.

---

# 18. Price Reservation

Khi Customer bắt đầu thanh toán, hệ thống tạo Price Reservation.

Bao gồm:

- Product
- Price
- Currency
- Price Book Version
- Commercial Agreement Version
- Exchange Rate Version
- Reservation Time
- Expiry Time

Reservation mặc định:

10 phút.

---

# 19. Payment Session

Payment Session là Business Object độc lập.

Payment Session quản lý:

- Checkout
- Reservation
- Payment
- Retry
- Cancel
- Expiry
- Validation

Payment Session không đồng nhất với Order.

---

# 20. Commercial Consistency Principle

Trước khi Fulfillment, hệ thống bắt buộc thực hiện:

Pre-Fulfillment Commercial Validation.

Kiểm tra:

- Product Version
- Price Book Version
- Commercial Agreement
- Exchange Rate
- Supplier Cost
- Supplier Availability
- Reservation
- Payment

Nếu hợp lệ:

```text
Payment Success

↓

Commercial Validation

↓

Commercial Snapshot Lock

↓

Fulfillment

↓

Deliver QR
```

Nếu không hợp lệ:

```text
Commercial Change

↓

Pause Fulfillment

↓

Customer Decision
```

Customer có thể:

- Pay Difference
- Refund Difference
- Full Refund

---

# 21. Publish Guard

Trước khi Publish Price Change Set, hệ thống phải:

- kiểm tra Payment Session đang mở
- cảnh báo số lượng Payment Session bị ảnh hưởng
- cho phép Review
- cho phép Delay Publish
- cho phép Continue Publish

Ví dụ:

"12 Payment Sessions đang sử dụng Price Book này."

---

# 22. Business Decisions (Locked)

## BD-05-001

Price thuộc Catalog.

---

## BD-05-002

Product chỉ lưu Reference Price.

---

## BD-05-003

Cost được tính theo Distribution Network.

---

## BD-05-004

Chỉ Payment Owner được tạo Price Book.

---

## BD-05-005

Payment Owner cố định theo Commercial Agreement trong phiên bản 2.0.

---

## BD-05-006

Price Book hỗ trợ Multi Currency.

---

## BD-05-007

Currency thuộc Commercial Agreement.

---

## BD-05-008

Partner được phép bán dưới Cost nhưng phải có Warning và Audit.

---

## BD-05-009

Price Book thay đổi thông qua Price Change Set.

---

## BD-05-010

Commission độc lập với Pricing.

---

## BD-05-011

Revenue Sharing độc lập với Commission.

---

## BD-05-012

Dynamic Pricing chỉ hỗ trợ Pricing Formula.

---

## BD-05-013

Commercial Agreement là Business Object trung tâm.

---

## BD-05-014

Snapshot Pricing lưu toàn bộ Commercial Context.

---

## BD-05-015

Payment Session là Business Object độc lập.

---

## BD-05-016

Bắt buộc Pre-Fulfillment Commercial Validation.

---

## BD-05-017

Publish Price Change Set phải kiểm tra Payment Session đang mở.

---

# 23. Commercial Pricing Flow

```text
Supplier Cost
      │
      ▼
Master Catalog
      │
      ▼
Commercial Agreement
      │
      ▼
Price Book
      │
      ▼
Price Reservation
      │
      ▼
Payment Session
      │
      ▼
Commercial Validation
      │
      ▼
Commercial Snapshot
      │
      ▼
Fulfillment
      │
      ▼
Settlement
```

---

# 24. Traceability

Workshop này kế thừa:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04

---

# 25. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Pricing Engine
- Promotion Engine
- Payment Engine
- Checkout
- Settlement
- Financial Event
- Reporting
- BI
- Commission Engine
- Revenue Sharing
- API
- DMS
- DBD

---

# 26. Workshop Status

**Status:** FROZEN

Workshop này là Foundation cho:

- Pricing
- Promotion
- Payment
- Checkout
- Settlement
- Revenue Sharing
- Financial Event

---

# 27. Next Workshop

**BRD-WS-06 – Promotion, Coupon & Campaign Model**

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-001 — Price thuộc Catalog

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
      "requirement_id": "BD-05-001",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "8123d9e5dbbd1cfab89a3cad7996feb05aa76a9c71c664f9be8ed328146f8662"
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
        "BD-05-001-AC001",
        "BD-05-001-AC002",
        "BD-05-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-001-O001",
      "obligation_text": "Price thuộc Catalog"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-001 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-001-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-001-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-001 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Price thuộc Catalog.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Pricing Ownership",
    "source_context_sha256": "a5f1645d6fcf36f6c0a42ab73af9ad8d6815b4c2574c62644d39a0f558a743b7",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "8123d9e5dbbd1cfab89a3cad7996feb05aa76a9c71c664f9be8ed328146f8662",
    "source_lines": "L772-L880",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-001"
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
  "stable_id": "BD-05-001",
  "title": "Price thuộc Catalog",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-002 — Product chỉ lưu Reference Price

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
      "requirement_id": "BD-05-002",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "fb43abaf0e975c7e60e623ce1ef09b192f93364d9b863af9b65e7642667e0ad6"
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
        "BD-05-002-AC001",
        "BD-05-002-AC002",
        "BD-05-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-002-O001",
      "obligation_text": "Product chỉ lưu Reference Price"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Product chỉ lưu Reference Price.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-002",
    "source_context_sha256": "ce048180e38c5c9de7a1a8d6d2ab9bb79c6cf1b62367987efdb45467e70d7873",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "fb43abaf0e975c7e60e623ce1ef09b192f93364d9b863af9b65e7642667e0ad6",
    "source_lines": "L882-L957",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-002"
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
  "stable_id": "BD-05-002",
  "title": "Product chỉ lưu Reference Price",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-003 — Cost được tính theo Distribution Network

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
      "requirement_id": "BD-05-003",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "99b2dcf3150c700a298a72c45d9d116bb590f8adf3824beb70a704df65caaa5a"
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
        "BD-05-003-AC001",
        "BD-05-003-AC002",
        "BD-05-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-003-O001",
      "obligation_text": "Cost được tính theo Distribution Network"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Cost được tính theo Distribution Network.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-003",
    "source_context_sha256": "662997e8782637a13e96c05d783ac8c20f55dba60216f09c7fa815c28f84ea62",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "99b2dcf3150c700a298a72c45d9d116bb590f8adf3824beb70a704df65caaa5a",
    "source_lines": "L959-L1034",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-003"
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
  "stable_id": "BD-05-003",
  "title": "Cost được tính theo Distribution Network",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-004 — Chỉ Payment Owner được tạo Price Book

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
      "requirement_id": "BD-05-004",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "cb411eb38056db61b0bc433046832ca35fbbadec03cee989789489c2fe1d5588"
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
        "BD-05-004-AC001",
        "BD-05-004-AC002",
        "BD-05-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-004-O001",
      "obligation_text": "Chỉ Payment Owner được tạo Price Book"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Chỉ Payment Owner được tạo Price Book.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-004",
    "source_context_sha256": "b8043adfffc2de9a2ae56cffa067005c718a65769636643a8d062d67e7dd59a9",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "cb411eb38056db61b0bc433046832ca35fbbadec03cee989789489c2fe1d5588",
    "source_lines": "L1036-L1144",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-004"
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
  "stable_id": "BD-05-004",
  "title": "Chỉ Payment Owner được tạo Price Book",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-005 — Payment Owner cố định theo Commercial Agreement trong phiên bản 2.0

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
      "requirement_id": "BD-05-005",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "44596678bd2f2f07792f2e5e2b2a3fa47eb60f7ed0b21e5212780eff37005dd7"
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
        "BD-05-005-AC001",
        "BD-05-005-AC002",
        "BD-05-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-005-O001",
      "obligation_text": "Payment Owner cố định theo Commercial Agreement trong phiên bản 2.0"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-005 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Payment Owner cố định theo Commercial Agreement trong phiên bản 2.0.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-005",
    "source_context_sha256": "ea35790d04640ccdb13a864bf58096a3e7800b497c0c1e7e9440b198196f7f43",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "44596678bd2f2f07792f2e5e2b2a3fa47eb60f7ed0b21e5212780eff37005dd7",
    "source_lines": "L1146-L1254",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-005"
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
  "stable_id": "BD-05-005",
  "title": "Payment Owner cố định theo Commercial Agreement trong phiên bản 2.0",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-006 — Price Book hỗ trợ Multi Currency

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
      "requirement_id": "BD-05-006",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "4e6030c19e0056ca7bce91b9a8bc93fd04aed5abfac45f0bcd96e9a5e22955c4"
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
        "BD-05-006-AC001",
        "BD-05-006-AC002",
        "BD-05-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-006-O001",
      "obligation_text": "Price Book hỗ trợ Multi Currency"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-006-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-006-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-006 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Price Book hỗ trợ Multi Currency.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-006",
    "source_context_sha256": "b448a2f7cd83c3571d2cc2412f4caf495369c03c86dd05b8369e1dd93cc5cf64",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "4e6030c19e0056ca7bce91b9a8bc93fd04aed5abfac45f0bcd96e9a5e22955c4",
    "source_lines": "L1256-L1364",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-006"
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
  "stable_id": "BD-05-006",
  "title": "Price Book hỗ trợ Multi Currency",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-007 — Currency thuộc Commercial Agreement

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
      "requirement_id": "BD-05-007",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "879db4ed64fc785219486c8aa02e5445314bf333dc5776f636789b26b99368d5"
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
        "BD-05-007-AC001",
        "BD-05-007-AC002",
        "BD-05-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-007-O001",
      "obligation_text": "Currency thuộc Commercial Agreement"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-007 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Currency thuộc Commercial Agreement.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-007",
    "source_context_sha256": "9fac07a6a8a035fc735a388f287765d7c10bc7619c840d80398e6248993e1bd0",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "879db4ed64fc785219486c8aa02e5445314bf333dc5776f636789b26b99368d5",
    "source_lines": "L1366-L1474",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-007"
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
  "stable_id": "BD-05-007",
  "title": "Currency thuộc Commercial Agreement",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-008 — Partner được phép bán dưới Cost nhưng phải có Warning và Audit

```json
{
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "Composite parent coverage is satisfied only through ALL_CHILDREN; the parent is not an implementation, acceptance, scope-coverage, or criticality unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Partner được phép bán dưới Cost nhưng phải có Warning và Audit.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-008",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-008",
    "source_context_sha256": "4b3964499096f5967517741b362afda424073f5f230ff5e6589d0d12d5674b96",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "0aad42ecc3ed189e7ce0681ff075353800702d67cc7f689e6b111ce6a1035f8b",
    "source_fingerprint_before_c3": "ba1aada17c6d5bde5e1445117d11085ec7539d3d43084b192c963d020273636b",
    "source_lines": "L1476-L1535",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-008"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-05-R030",
      "BRD-WS-05-R031"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-05-008",
  "title": "Partner được phép bán dưới Cost nhưng phải có Warning và Audit",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-009 — Price Book thay đổi thông qua Price Change Set

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "A rejected or future Price Change Set leaves the current Price Book unchanged"
    ],
    "concrete_bindings": [
      {
        "action": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BD-05-009.ACTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.ACTION.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BD-05-009-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
            "source_lines": "L617-L620",
            "source_section": "22. Business Decisions (Locked) > BD-05-009"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.BD-05-009.BD-05-009.ACTION",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        },
        "approval_policy": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BD-05-009.APPROVAL_POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.APPROVAL_POLICY.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BD-05-009-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
            "source_lines": "L617-L620",
            "source_section": "22. Business Decisions (Locked) > BD-05-009"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BD-05-009.BD-05-009.APPROVAL_POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "approval_reference": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BD-05-009.APPROVAL_REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.APPROVAL_REFERENCE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BD-05-009-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
            "source_lines": "L617-L620",
            "source_section": "22. Business Decisions (Locked) > BD-05-009"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "APPROVAL_ID",
            "resolver_id": "RESOLVE.BD-05-009.BD-05-009.APPROVAL_REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "APPROVAL_ID"
        }
      },
      {
        "from_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-05-009.FROM_STATE"
            ],
            "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BD-05-009.FROM_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BD-05-009-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
            "source_lines": "L617-L620",
            "source_section": "22. Business Decisions (Locked) > BD-05-009"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BD-05-009.BD-05-009.FROM_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "state_machine": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BD-05-009.STATE_MACHINE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BD-05-009-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
            "source_lines": "L617-L620",
            "source_section": "22. Business Decisions (Locked) > BD-05-009"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_MACHINE_ID",
            "resolver_id": "RESOLVE.BD-05-009.BD-05-009.STATE_MACHINE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_MACHINE_ID"
        },
        "to_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BD-05-009.TO_STATE"
            ],
            "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BD-05-009.TO_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BD-05-009-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
            "source_lines": "L617-L620",
            "source_section": "22. Business Decisions (Locked) > BD-05-009"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BD-05-009.BD-05-009.TO_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "trigger": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BD-05-009.TRIGGER",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BD-05-009-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
            "source_lines": "L617-L620",
            "source_section": "22. Business Decisions (Locked) > BD-05-009"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.BD-05-009.BD-05-009.TRIGGER",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BD-05-009",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "The Price Book is modified directly without a Price Change Set"
    ],
    "operator_composition": [
      "APPROVAL_REQUIRED",
      "STATE_TRANSITION_ALLOWED"
    ],
    "positive_oracle": [
      "The Price Book changes only through the Price Change Set"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2C-OBT-C1-BD-05-009-OPT-1"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
      "source_lines": "L617-L620",
      "source_section": "22. Business Decisions (Locked) > BD-05-009"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
          "source_type": "APPROVED_DECISION",
          "version": "2026-07-16"
        },
        "identifier": "BD-05-009.BD-05-009.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BD-05-009.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2C-OBT-C1-BD-05-009-OPT-1"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-05.md",
          "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
          "source_lines": "L617-L620",
          "source_section": "22. Business Decisions (Locked) > BD-05-009"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BD-05-009.BD-05-009.BD-05-009.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BD-05-009.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PRICE_BOOK_ID",
        "FIELD.CHANGE_SET_ID",
        "FIELD.APPROVAL_STATE",
        "FIELD.BEFORE_VERSION",
        "FIELD.AFTER_VERSION",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "BD-05-009.EVIDENCE.PRODUCER",
      "required_collection_origin": "BD-05-009.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PRICE_BOOK_ID",
        "FIELD.CHANGE_SET_ID",
        "FIELD.APPROVAL_STATE",
        "FIELD.BEFORE_VERSION",
        "FIELD.AFTER_VERSION",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "BD-05-009.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BD-05-009.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BD-05-009.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BD-05-009-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": {
        "meaning": "Price Change Set uses a governed lifecycle and Shared Approval Engine approval before becoming effective.",
        "non_inferences": [
          "No fixed approver role is inferred.",
          "No approval SLA is inferred."
        ],
        "option_id": "P2C-OBT-C1-BD-05-009-OPT-1"
      },
      "assertions": [
        {
          "assertion_id": "BD-05-009.O1.1.APPROVAL_REQUIRED",
          "evaluator_consumed_bindings": [
            "action",
            "approval_policy",
            "approval_reference"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BD-05-009-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-05.md",
              "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
              "source_lines": "L617-L620",
              "source_section": "22. Business Decisions (Locked) > BD-05-009"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-05-009.BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BD-05-009-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-05.md",
              "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
              "source_lines": "L617-L620",
              "source_section": "22. Business Decisions (Locked) > BD-05-009"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ACTION_ID",
              "resolver_id": "RESOLVE.BD-05-009.BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ACTION_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "action": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BD-05-009.ACTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.ACTION.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BD-05-009-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                  "source_lines": "L617-L620",
                  "source_section": "22. Business Decisions (Locked) > BD-05-009"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BD-05-009.BD-05-009.ACTION",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              },
              "approval_policy": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BD-05-009.APPROVAL_POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.APPROVAL_POLICY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BD-05-009-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                  "source_lines": "L617-L620",
                  "source_section": "22. Business Decisions (Locked) > BD-05-009"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BD-05-009.BD-05-009.APPROVAL_POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "approval_reference": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BD-05-009.APPROVAL_REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.APPROVAL_REFERENCE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BD-05-009-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                  "source_lines": "L617-L620",
                  "source_section": "22. Business Decisions (Locked) > BD-05-009"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "APPROVAL_ID",
                  "resolver_id": "RESOLVE.BD-05-009.BD-05-009.APPROVAL_REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "APPROVAL_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BD-05-009-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                  "source_lines": "L617-L620",
                  "source_section": "22. Business Decisions (Locked) > BD-05-009"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BD-05-009.BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BD-05-009-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                  "source_lines": "L617-L620",
                  "source_section": "22. Business Decisions (Locked) > BD-05-009"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "OBSERVE.BD-05-009.BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BD-05-009-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                "source_lines": "L617-L620",
                "source_section": "22. Business Decisions (Locked) > BD-05-009"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-05-009.BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "APPROVAL_REQUIRED"
          },
          "obligation_id": "BD-05-009-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BD-05-009-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-05.md",
              "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
              "source_lines": "L617-L620",
              "source_section": "22. Business Decisions (Locked) > BD-05-009"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ACTION_ID",
              "resolver_id": "OBSERVE.BD-05-009.BD-05-009.BD-05-009.O1.1.APPROVAL_REQUIRED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ACTION_ID"
          },
          "operator_id": "APPROVAL_REQUIRED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "action": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BD-05-009.ACTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.ACTION.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BD-05-009-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                "source_lines": "L617-L620",
                "source_section": "22. Business Decisions (Locked) > BD-05-009"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.BD-05-009.BD-05-009.ACTION",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            },
            "approval_policy": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BD-05-009.APPROVAL_POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.APPROVAL_POLICY.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BD-05-009-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                "source_lines": "L617-L620",
                "source_section": "22. Business Decisions (Locked) > BD-05-009"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BD-05-009.BD-05-009.APPROVAL_POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "approval_reference": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BD-05-009.APPROVAL_REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-05-009.O1.1.APPROVAL_REQUIRED.APPROVAL_REFERENCE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BD-05-009-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                "source_lines": "L617-L620",
                "source_section": "22. Business Decisions (Locked) > BD-05-009"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "APPROVAL_ID",
                "resolver_id": "RESOLVE.BD-05-009.BD-05-009.APPROVAL_REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "APPROVAL_ID"
            }
          }
        },
        {
          "assertion_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED",
          "evaluator_consumed_bindings": [
            "from_state",
            "state_machine",
            "to_state",
            "trigger"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BD-05-009-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-05.md",
              "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
              "source_lines": "L617-L620",
              "source_section": "22. Business Decisions (Locked) > BD-05-009"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-05-009.BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BD-05-009-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-05.md",
              "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
              "source_lines": "L617-L620",
              "source_section": "22. Business Decisions (Locked) > BD-05-009"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "RESOLVE.BD-05-009.BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
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
                    "BD-05-009.FROM_STATE"
                  ],
                  "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BD-05-009.FROM_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BD-05-009-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                  "source_lines": "L617-L620",
                  "source_section": "22. Business Decisions (Locked) > BD-05-009"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BD-05-009.BD-05-009.FROM_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "state_machine": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BD-05-009.STATE_MACHINE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BD-05-009-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                  "source_lines": "L617-L620",
                  "source_section": "22. Business Decisions (Locked) > BD-05-009"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_MACHINE_ID",
                  "resolver_id": "RESOLVE.BD-05-009.BD-05-009.STATE_MACHINE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_MACHINE_ID"
              },
              "to_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-05-009.TO_STATE"
                  ],
                  "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BD-05-009.TO_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BD-05-009-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                  "source_lines": "L617-L620",
                  "source_section": "22. Business Decisions (Locked) > BD-05-009"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BD-05-009.BD-05-009.TO_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "trigger": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BD-05-009.TRIGGER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BD-05-009-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                  "source_lines": "L617-L620",
                  "source_section": "22. Business Decisions (Locked) > BD-05-009"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BD-05-009.BD-05-009.TRIGGER",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BD-05-009-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                  "source_lines": "L617-L620",
                  "source_section": "22. Business Decisions (Locked) > BD-05-009"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BD-05-009.BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-BD-05-009-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                  "source_lines": "L617-L620",
                  "source_section": "22. Business Decisions (Locked) > BD-05-009"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "OBSERVE.BD-05-009.BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BD-05-009-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                "source_lines": "L617-L620",
                "source_section": "22. Business Decisions (Locked) > BD-05-009"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-05-009.BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "STATE_TRANSITION_ALLOWED"
          },
          "obligation_id": "BD-05-009-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-BD-05-009-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-05.md",
              "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
              "source_lines": "L617-L620",
              "source_section": "22. Business Decisions (Locked) > BD-05-009"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "OBSERVE.BD-05-009.BD-05-009.BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
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
                  "BD-05-009.FROM_STATE"
                ],
                "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BD-05-009.FROM_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BD-05-009-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                "source_lines": "L617-L620",
                "source_section": "22. Business Decisions (Locked) > BD-05-009"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BD-05-009.BD-05-009.FROM_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "state_machine": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BD-05-009.STATE_MACHINE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BD-05-009-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                "source_lines": "L617-L620",
                "source_section": "22. Business Decisions (Locked) > BD-05-009"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_MACHINE_ID",
                "resolver_id": "RESOLVE.BD-05-009.BD-05-009.STATE_MACHINE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_MACHINE_ID"
            },
            "to_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-05-009.TO_STATE"
                ],
                "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BD-05-009.TO_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BD-05-009-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                "source_lines": "L617-L620",
                "source_section": "22. Business Decisions (Locked) > BD-05-009"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BD-05-009.BD-05-009.TO_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "trigger": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "BD-05-009.TRIGGER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-BD-05-009-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
                "source_lines": "L617-L620",
                "source_section": "22. Business Decisions (Locked) > BD-05-009"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.BD-05-009.BD-05-009.TRIGGER",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "A rejected or future Price Change Set leaves the current Price Book unchanged"
      ],
      "contract_ast_sha256": "c9b1cd714a89bf1a90cd0c7bde41df7c24233136212f2690cf52d2a7649e7aca",
      "contract_id": "P2C.C4.CONTRACT.BD-05-009",
      "criticality": "CRITICAL",
      "disposition": "SOURCE_CLARIFICATION_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-BD-05-009-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "BD-05-009.BD-05-009.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-05-009.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-BD-05-009-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
            "source_lines": "L617-L620",
            "source_section": "22. Business Decisions (Locked) > BD-05-009"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BD-05-009.BD-05-009.BD-05-009.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BD-05-009.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PRICE_BOOK_ID",
          "FIELD.CHANGE_SET_ID",
          "FIELD.APPROVAL_STATE",
          "FIELD.BEFORE_VERSION",
          "FIELD.AFTER_VERSION",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "BD-05-009.EVIDENCE.PRODUCER",
        "required_collection_origin": "BD-05-009.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PRICE_BOOK_ID",
          "FIELD.CHANGE_SET_ID",
          "FIELD.APPROVAL_STATE",
          "FIELD.BEFORE_VERSION",
          "FIELD.AFTER_VERSION",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "BD-05-009.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BD-05-009.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BD-05-009.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-F1274B85877AC98E372C",
        "P2C-C4-FX-8BBA79413E721B7279F1",
        "P2C-C4-FX-BFDE6C8955D638255B03"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "The Price Book is modified directly without a Price Change Set"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-05-009-O001",
          "obligation_text": "Price Book thay đổi thông qua Price Change Set"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BD-05-009.O1.1.APPROVAL_REQUIRED",
            "BD-05-009.O1.2.STATE_TRANSITION_ALLOWED"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-05-009-O001"
        }
      ],
      "operator_composition": [
        "APPROVAL_REQUIRED",
        "STATE_TRANSITION_ALLOWED"
      ],
      "positive_oracles": [
        "The Price Book changes only through the Price Change Set"
      ],
      "preconditions": [
        "A versioned Price Change Set exists and is authorized"
      ],
      "prohibitions": [
        "The Price Book is modified directly without a Price Change Set"
      ],
      "requirement_id": "BD-05-009",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2C-OBT-C1-BD-05-009-OPT-1"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-05.md",
        "source_fingerprint": "9578531bcc5212dde93063f773cf51dae285025e9522b244f4d3523a28f62f77",
        "source_lines": "L617-L620",
        "source_section": "22. Business Decisions (Locked) > BD-05-009"
      },
      "source_statement": "Price Book thay đổi thông qua Price Change Set.",
      "surrounding_source_context": "## BD-05-009\n\nPrice Book thay đổi thông qua Price Change Set.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BD-05-009",
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
        "BD-05-009-AC001",
        "BD-05-009-AC002",
        "BD-05-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-009-O001",
      "obligation_text": "Price Book thay đổi thông qua Price Change Set"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-009 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-009 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-009 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-009-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-009-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-009 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Price Book thay đổi thông qua Price Change Set.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-009",
    "source_context_sha256": "b01c03b5a9262b211bfeb6d1d4cdeaffb83ffa25b0639b5d41783eb5217020ec",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "7c1a7ae8d164397e482c4b11da033f90dc1e46e0971f45684a0c5100c324d587",
    "source_lines": "L1537-L3141",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-009"
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
  "stable_id": "BD-05-009",
  "title": "Price Book thay đổi thông qua Price Change Set",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-010 — Commission độc lập với Pricing

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
      "requirement_id": "BD-05-010",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "b6f59c8fe9df25c053c5ec2bcca7df9987408bcfeef3fc84d6542a88c0e328b2"
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
        "BD-05-010-AC001",
        "BD-05-010-AC002",
        "BD-05-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-010-O001",
      "obligation_text": "Commission độc lập với Pricing"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-010-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-010 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-010 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-010-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-010-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-010 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commission độc lập với Pricing.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-010",
    "source_context_sha256": "6c05d6e025a043b0e18b21cb730fbbae375e7bcbc1ed1d4be9c2aee95cac8303",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "b6f59c8fe9df25c053c5ec2bcca7df9987408bcfeef3fc84d6542a88c0e328b2",
    "source_lines": "L3143-L3253",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-010"
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
  "stable_id": "BD-05-010",
  "title": "Commission độc lập với Pricing",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-011 — Revenue Sharing độc lập với Commission

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
      "requirement_id": "BD-05-011",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "08f0518ead0884984924f5ae45d026f25a790dc926edcf1839197a77c10ab4c1"
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
        "BD-05-011-AC001",
        "BD-05-011-AC002",
        "BD-05-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-011-O001",
      "obligation_text": "Revenue Sharing độc lập với Commission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-011-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-011 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-011 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-011-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-011-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-011 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Revenue Sharing độc lập với Commission.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "14. Revenue Sharing",
    "source_context_sha256": "47c9a4b2d7766d67ce70c60765a72e1b0aff4fa73bb0f637ab9587ad68b66766",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "08f0518ead0884984924f5ae45d026f25a790dc926edcf1839197a77c10ab4c1",
    "source_lines": "L3255-L3365",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-011"
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
  "stable_id": "BD-05-011",
  "title": "Revenue Sharing độc lập với Commission",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-012 — Dynamic Pricing chỉ hỗ trợ Pricing Formula

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
      "requirement_id": "BD-05-012",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "60dc88b0b29371a7a06367d40e94cea66684d31ee3972b336bdc2cac04dfa67f"
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
        "BD-05-012-AC001",
        "BD-05-012-AC002",
        "BD-05-012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-012-O001",
      "obligation_text": "Dynamic Pricing chỉ hỗ trợ Pricing Formula"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-012 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-012-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-012-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-012 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dynamic Pricing chỉ hỗ trợ Pricing Formula.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-012",
    "source_context_sha256": "4670de0d953dbbfdab3048145c57b967066e381a05c834fa4d9c816174346cc1",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "60dc88b0b29371a7a06367d40e94cea66684d31ee3972b336bdc2cac04dfa67f",
    "source_lines": "L3367-L3475",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-012"
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
  "stable_id": "BD-05-012",
  "title": "Dynamic Pricing chỉ hỗ trợ Pricing Formula",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-013 — Commercial Agreement là Business Object trung tâm

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
      "requirement_id": "BD-05-013",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "15d5769d27c07da1a2c4a4d9fc1839f855d0d2424b2f2f6301fef848f26bc741"
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
        "BD-05-013-AC001",
        "BD-05-013-AC002",
        "BD-05-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-013-O001",
      "obligation_text": "Commercial Agreement là Business Object trung tâm"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Commercial Agreement là Business Object trung tâm.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-013",
    "source_context_sha256": "5e0cdccfec7205512a25b02778f35888cb64eff03a4164aad6c7c8041feb7d66",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "15d5769d27c07da1a2c4a4d9fc1839f855d0d2424b2f2f6301fef848f26bc741",
    "source_lines": "L3477-L3552",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-013"
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
  "stable_id": "BD-05-013",
  "title": "Commercial Agreement là Business Object trung tâm",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-014 — Snapshot Pricing lưu toàn bộ Commercial Context

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
      "requirement_id": "BD-05-014",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "6bf1e56772adb3473b69b219f274b03982f77acdd4f6b78a8e428cc581dbb11d"
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
        "BD-05-014-AC001",
        "BD-05-014-AC002",
        "BD-05-014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-014-O001",
      "obligation_text": "Snapshot Pricing lưu toàn bộ Commercial Context"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-014 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot Pricing lưu toàn bộ Commercial Context.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Snapshot Pricing",
    "source_context_sha256": "adfa47595cbdfb5bc86f2c7db5d13dfee5ce553c9473c10fc82b8746fb3426be",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "6bf1e56772adb3473b69b219f274b03982f77acdd4f6b78a8e428cc581dbb11d",
    "source_lines": "L3554-L3662",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-014"
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
  "stable_id": "BD-05-014",
  "title": "Snapshot Pricing lưu toàn bộ Commercial Context",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-015 — Payment Session là Business Object độc lập

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
      "requirement_id": "BD-05-015",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "50febd948f76ef02c618d7ca248791d63957d85420106021987b90f6d5fa4d85"
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
        "BD-05-015-AC001",
        "BD-05-015-AC002",
        "BD-05-015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-015-O001",
      "obligation_text": "Payment Session là Business Object độc lập"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-015-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-015 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-015 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-015-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-015-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-015 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Payment Session là Business Object độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Payment Session",
    "source_context_sha256": "0ce9d67cf13ded6f664d20aba6c6fd2f910f5b3481529ce8f544e065d5a424c9",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "50febd948f76ef02c618d7ca248791d63957d85420106021987b90f6d5fa4d85",
    "source_lines": "L3664-L3774",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-015"
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
  "stable_id": "BD-05-015",
  "title": "Payment Session là Business Object độc lập",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-016 — Bắt buộc Pre-Fulfillment Commercial Validation

```json
{
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "BD-05-016 aliases the canonical comprehensive Pre-Fulfillment Commercial Validation contract.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Bắt buộc Pre-Fulfillment Commercial Validation.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-016",
    "phase_2c_c3_actions": [
      "C3_APPROVED_PREFULFILLMENT_ALIAS"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-016",
    "source_context_sha256": "c812aa9e53231026a0365bd85e4150329cd927a381d93a933e148a6afab714cc",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "219f415da869fa40ea7bf2ac4bd5ce5a36aa4701e9e4fd26b1c4d2b93d2900b1",
    "source_fingerprint_before_c3": "71e275433e30a42859ec4546ddd984ee9448e2c92b40bcde228d9cc6423509e5",
    "source_lines": "L3776-L3832",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-016"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "BRD-WS-05-R021",
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-05-016",
  "title": "Bắt buộc Pre-Fulfillment Commercial Validation",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-05-017 — Publish Price Change Set phải kiểm tra Payment Session đang mở

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
      "requirement_id": "BD-05-017",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "fa8f9c2101eea079ba0d2fd2c337b605f2b1fd6972a8cf05714c4fe367aa2e8f"
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
        "BD-05-017-AC001",
        "BD-05-017-AC002",
        "BD-05-017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-05-017-O001",
      "obligation_text": "Publish Price Change Set phải kiểm tra Payment Session đang mở"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-017 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-017 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-017 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-017-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-05-017-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-05-017 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Publish Price Change Set phải kiểm tra Payment Session đang mở.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-05-017",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-017",
    "source_context_sha256": "3585047f2df433f7c36fac55ddac6140e858e384098f4537893f005c900678c8",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "fa8f9c2101eea079ba0d2fd2c337b605f2b1fd6972a8cf05714c4fe367aa2e8f",
    "source_lines": "L3834-L3942",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-05-017"
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
  "stable_id": "BD-05-017",
  "title": "Publish Price Change Set phải kiểm tra Payment Session đang mở",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R001 — Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Unit Price

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
      "requirement_id": "BRD-WS-05-R001",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "e58fe14821f19f3470e16b57bf7d57dc91d6d249e1a6761f8a1899d7a2f3a66b"
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
        "BRD-WS-05-R001-AC001",
        "BRD-WS-05-R001-AC002",
        "BRD-WS-05-R001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R001-O001",
      "obligation_text": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Unit Price"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R001 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R001-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R001-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R001 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Unit Price",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-001",
    "previous_temporary_key": "TMP-BRD-WS-05-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Price",
    "source_context_sha256": "0304fac7de637db6d21b1da0a904420d96ba8e00b20fa2f595a640da02b85132",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "e58fe14821f19f3470e16b57bf7d57dc91d6d249e1a6761f8a1899d7a2f3a66b",
    "source_lines": "L3944-L4056",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R001"
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
  "stable_id": "BRD-WS-05-R001",
  "title": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Unit Price",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R002 — Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier MSRP

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
      "requirement_id": "BRD-WS-05-R002",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "7090a2091b07976ad09531a63d43ba7c5f796e524ba7a911680ffc379ba20c9d"
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
        "BRD-WS-05-R002-AC001",
        "BRD-WS-05-R002-AC002",
        "BRD-WS-05-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R002-O001",
      "obligation_text": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier MSRP"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R002 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R002 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier MSRP",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-002",
    "previous_temporary_key": "TMP-BRD-WS-05-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Price",
    "source_context_sha256": "0304fac7de637db6d21b1da0a904420d96ba8e00b20fa2f595a640da02b85132",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "7090a2091b07976ad09531a63d43ba7c5f796e524ba7a911680ffc379ba20c9d",
    "source_lines": "L4058-L4170",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R002"
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
  "stable_id": "BRD-WS-05-R002",
  "title": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier MSRP",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R003 — Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Discount Price

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
      "requirement_id": "BRD-WS-05-R003",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "a712b6ac9311b9a76cee6738f0cf7b93d4f17b0277ab2f5eea0e1b483475cd9c"
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
        "BRD-WS-05-R003-AC001",
        "BRD-WS-05-R003-AC002",
        "BRD-WS-05-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R003-O001",
      "obligation_text": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Discount Price"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R003 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Discount Price",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-003",
    "previous_temporary_key": "TMP-BRD-WS-05-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Price",
    "source_context_sha256": "0304fac7de637db6d21b1da0a904420d96ba8e00b20fa2f595a640da02b85132",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "a712b6ac9311b9a76cee6738f0cf7b93d4f17b0277ab2f5eea0e1b483475cd9c",
    "source_lines": "L4172-L4284",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R003"
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
  "stable_id": "BRD-WS-05-R003",
  "title": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Discount Price",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R004 — Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Discount Rate

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
      "requirement_id": "BRD-WS-05-R004",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "ddd0f8b6f25eee840a34c6319bc92dea5c8c5eceb9b28d240a9e66c7d72bf788"
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
        "BRD-WS-05-R004-AC001",
        "BRD-WS-05-R004-AC002",
        "BRD-WS-05-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R004-O001",
      "obligation_text": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Discount Rate"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Discount Rate",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-004",
    "previous_temporary_key": "TMP-BRD-WS-05-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Price",
    "source_context_sha256": "0304fac7de637db6d21b1da0a904420d96ba8e00b20fa2f595a640da02b85132",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "ddd0f8b6f25eee840a34c6319bc92dea5c8c5eceb9b28d240a9e66c7d72bf788",
    "source_lines": "L4286-L4398",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R004"
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
  "stable_id": "BRD-WS-05-R004",
  "title": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Discount Rate",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R005 — Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Tax

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
      "requirement_id": "BRD-WS-05-R005",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "f9ca2676c404db9a9ab2480f3b850cabb91584f02138a0927b6b44373ab9c1b7"
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
        "BRD-WS-05-R005-AC001",
        "BRD-WS-05-R005-AC002",
        "BRD-WS-05-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R005-O001",
      "obligation_text": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Tax"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R005 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Tax",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-005",
    "previous_temporary_key": "TMP-BRD-WS-05-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Price",
    "source_context_sha256": "0304fac7de637db6d21b1da0a904420d96ba8e00b20fa2f595a640da02b85132",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "f9ca2676c404db9a9ab2480f3b850cabb91584f02138a0927b6b44373ab9c1b7",
    "source_lines": "L4400-L4512",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R005"
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
  "stable_id": "BRD-WS-05-R005",
  "title": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Tax",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R006 — Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Fee

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
      "requirement_id": "BRD-WS-05-R006",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "d49b4633205ee761d6ec46c73cae1136a95b8a727ba31e09ceab23d6349631d0"
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
        "BRD-WS-05-R006-AC001",
        "BRD-WS-05-R006-AC002",
        "BRD-WS-05-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R006-O001",
      "obligation_text": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Fee"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R006-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R006-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R006 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Fee",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-006",
    "previous_temporary_key": "TMP-BRD-WS-05-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Price",
    "source_context_sha256": "0304fac7de637db6d21b1da0a904420d96ba8e00b20fa2f595a640da02b85132",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "d49b4633205ee761d6ec46c73cae1136a95b8a727ba31e09ceab23d6349631d0",
    "source_lines": "L4514-L4626",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R006"
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
  "stable_id": "BRD-WS-05-R006",
  "title": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Fee",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R007 — Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Suggested Retail Price

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
      "requirement_id": "BRD-WS-05-R007",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "61ee1cdea5adc6fbb574f73097270d42ba4d30d0c6edc506b45755ff8bf58ea0"
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
        "BRD-WS-05-R007-AC001",
        "BRD-WS-05-R007-AC002",
        "BRD-WS-05-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R007-O001",
      "obligation_text": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Suggested Retail Price"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R007 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Suggested Retail Price",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-007",
    "previous_temporary_key": "TMP-BRD-WS-05-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Price",
    "source_context_sha256": "0304fac7de637db6d21b1da0a904420d96ba8e00b20fa2f595a640da02b85132",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "61ee1cdea5adc6fbb574f73097270d42ba4d30d0c6edc506b45755ff8bf58ea0",
    "source_lines": "L4628-L4740",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R007"
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
  "stable_id": "BRD-WS-05-R007",
  "title": "Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Suggested Retail Price",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R008 — Không phải Selling Price

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
      "requirement_id": "BRD-WS-05-R008",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "cc40946787e9e29f276c52ae809cb3d066e910d95cf5ee86a844c3db20d16670"
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
        "BRD-WS-05-R008-AC001",
        "BRD-WS-05-R008-AC002",
        "BRD-WS-05-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R008-O001",
      "obligation_text": "Không phải Selling Price"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R008 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R008-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R008-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R008 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không phải Selling Price.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-008",
    "previous_temporary_key": "TMP-BRD-WS-05-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Price",
    "source_context_sha256": "0304fac7de637db6d21b1da0a904420d96ba8e00b20fa2f595a640da02b85132",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "cc40946787e9e29f276c52ae809cb3d066e910d95cf5ee86a844c3db20d16670",
    "source_lines": "L4742-L4850",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R008"
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
  "stable_id": "BRD-WS-05-R008",
  "title": "Không phải Selling Price",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R009 — Cost phải hỗ trợ bóc tách phục vụ Settlement

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
      "requirement_id": "BRD-WS-05-R009",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "8cd461996ada7eac60ec273555e0cb06096c41a039faed0b4e068d41a9282fd0"
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
        "BRD-WS-05-R009-AC001",
        "BRD-WS-05-R009-AC002",
        "BRD-WS-05-R009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R009-O001",
      "obligation_text": "Cost phải hỗ trợ bóc tách phục vụ Settlement"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Cost phải hỗ trợ bóc tách phục vụ Settlement.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-009",
    "previous_temporary_key": "TMP-BRD-WS-05-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Cost Model",
    "source_context_sha256": "89b70d1db5ab31ac82e86e22ad16a6bbf7a991d93dd97a52a35cc633f78406a4",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "8cd461996ada7eac60ec273555e0cb06096c41a039faed0b4e068d41a9282fd0",
    "source_lines": "L4852-L4927",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R009"
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
  "stable_id": "BRD-WS-05-R009",
  "title": "Cost phải hỗ trợ bóc tách phục vụ Settlement",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R011 — Mỗi Price Book phải có: - Base Currency

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
      "requirement_id": "BRD-WS-05-R011",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "92596598003787401ba8725a2670a27cee4c94efd5640b31a8d7065c46c37ae6"
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
        "BRD-WS-05-R011-AC001",
        "BRD-WS-05-R011-AC002",
        "BRD-WS-05-R011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R011-O001",
      "obligation_text": "Mỗi Price Book phải có: - Base Currency"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R011 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R011 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R011 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R011-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R011-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R011 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Price Book phải có: - Base Currency",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-011",
    "previous_temporary_key": "TMP-BRD-WS-05-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Multi-Currency Price Book",
    "source_context_sha256": "8a69310a96d502ebfd6bef77b280feb018f5c6c5ef1cc05351a507855e3dd5f1",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "92596598003787401ba8725a2670a27cee4c94efd5640b31a8d7065c46c37ae6",
    "source_lines": "L4929-L5037",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R011"
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
  "stable_id": "BRD-WS-05-R011",
  "title": "Mỗi Price Book phải có: - Base Currency",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R012 — Parent và Child phải thống nhất: - Settlement Currency

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
      "requirement_id": "BRD-WS-05-R012",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "5bc0abc3d3e7b4c7ee8ca2fdd973f86b2a40f06d8689c28d0ef8b0b5d4269b8a"
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
        "BRD-WS-05-R012-AC001",
        "BRD-WS-05-R012-AC002",
        "BRD-WS-05-R012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R012-O001",
      "obligation_text": "Parent và Child phải thống nhất: - Settlement Currency"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R012 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R012-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R012-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R012 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Parent và Child phải thống nhất: - Settlement Currency",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-012",
    "previous_temporary_key": "TMP-BRD-WS-05-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Currency Governance",
    "source_context_sha256": "fb98cbeb4e8b8ea83f216887a46f4032a51e081ab9d7b34118d355f4b359ae86",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "5bc0abc3d3e7b4c7ee8ca2fdd973f86b2a40f06d8689c28d0ef8b0b5d4269b8a",
    "source_lines": "L5039-L5147",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R012"
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
  "stable_id": "BRD-WS-05-R012",
  "title": "Parent và Child phải thống nhất: - Settlement Currency",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R013 — Parent và Child phải thống nhất: - Exchange Rate Source

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
      "requirement_id": "BRD-WS-05-R013",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "96a9aa952baeba5ac979ccd9c976a50eec6e9687f4bc458b2f4fd34cda5a7db9"
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
        "BRD-WS-05-R013-AC001",
        "BRD-WS-05-R013-AC002",
        "BRD-WS-05-R013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R013-O001",
      "obligation_text": "Parent và Child phải thống nhất: - Exchange Rate Source"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R013 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R013 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R013 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R013-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R013-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R013 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Parent và Child phải thống nhất: - Exchange Rate Source",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-013",
    "previous_temporary_key": "TMP-BRD-WS-05-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Currency Governance",
    "source_context_sha256": "fb98cbeb4e8b8ea83f216887a46f4032a51e081ab9d7b34118d355f4b359ae86",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "96a9aa952baeba5ac979ccd9c976a50eec6e9687f4bc458b2f4fd34cda5a7db9",
    "source_lines": "L5149-L5257",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R013"
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
  "stable_id": "BRD-WS-05-R013",
  "title": "Parent và Child phải thống nhất: - Exchange Rate Source",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R014 — Parent và Child phải thống nhất: - Effective Date

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Independent records without a parent-child relationship are not subject to this pair constraint"
    ],
    "concrete_bindings": [
      {
        "expected_outcome": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-05-R014.POLICY.OUTCOME.CONFORMING"
            ],
            "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
            "source_type": "SOURCE_LITERAL",
            "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
          },
          "identifier": "BRD-WS-05-R014.POLICY.OUTCOME.CONFORMING",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
            "source_lines": "L245-L249",
            "source_section": "10. Currency Governance"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_OUTCOME",
            "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY.OUTCOME.CONFORMING",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_OUTCOME"
        },
        "policy": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
            "source_type": "SOURCE_LITERAL",
            "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
          },
          "identifier": "BRD-WS-05-R014.POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
            "source_lines": "L245-L249",
            "source_section": "10. Currency Governance"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "policy_inputs": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
            "source_type": "SOURCE_LITERAL",
            "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
          },
          "identifier": "BRD-WS-05-R014.POLICY_INPUTS",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
            "source_lines": "L245-L249",
            "source_section": "10. Currency Governance"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY_INPUTS",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "policy_version": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
            "source_type": "SOURCE_LITERAL",
            "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
          },
          "identifier": "BRD-WS-05-R014.POLICY_VERSION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
            "source_lines": "L245-L249",
            "source_section": "10. Currency Governance"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_VERSION",
            "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY_VERSION",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_VERSION"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-05-R014",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Their Effective Dates conflict"
    ],
    "operator_composition": [
      "POLICY_OUTCOME_EQUALS"
    ],
    "positive_oracle": [
      "Parent and Child Effective Date values are consistent under the promotion policy"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
      "source_lines": "L245-L249",
      "source_section": "10. Currency Governance"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
          "source_type": "SOURCE_LITERAL",
          "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
        },
        "identifier": "BRD-WS-05-R014.BRD-WS-05-R014.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-05-R014.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-05.md",
          "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
          "source_lines": "L245-L249",
          "source_section": "10. Currency Governance"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-05-R014.BRD-WS-05-R014.BRD-WS-05-R014.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-05-R014.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PARENT_ID",
        "FIELD.CHILD_ID",
        "FIELD.PARENT_EFFECTIVE_DATE",
        "FIELD.CHILD_EFFECTIVE_DATE",
        "FIELD.CONSISTENCY_RESULT"
      ],
      "producer": "BRD-WS-05-R014.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-05-R014.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PARENT_ID",
        "FIELD.CHILD_ID",
        "FIELD.PARENT_EFFECTIVE_DATE",
        "FIELD.CHILD_EFFECTIVE_DATE",
        "FIELD.CONSISTENCY_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-05-R014.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-05-R014.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-05-R014.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-05-R014-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS",
          "evaluator_consumed_bindings": [
            "expected_outcome",
            "policy",
            "policy_inputs",
            "policy_version"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
              "source_type": "SOURCE_LITERAL",
              "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
            },
            "identifier": "BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-05.md",
              "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
              "source_lines": "L245-L249",
              "source_section": "10. Currency Governance"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-05-R014.BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
              "source_type": "SOURCE_LITERAL",
              "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
            },
            "identifier": "BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-05.md",
              "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
              "source_lines": "L245-L249",
              "source_section": "10. Currency Governance"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
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
                    "BRD-WS-05-R014.POLICY.OUTCOME.CONFORMING"
                  ],
                  "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
                },
                "identifier": "BRD-WS-05-R014.POLICY.OUTCOME.CONFORMING",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
                  "source_lines": "L245-L249",
                  "source_section": "10. Currency Governance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY.OUTCOME.CONFORMING",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "policy": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
                },
                "identifier": "BRD-WS-05-R014.POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
                  "source_lines": "L245-L249",
                  "source_section": "10. Currency Governance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "policy_inputs": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
                },
                "identifier": "BRD-WS-05-R014.POLICY_INPUTS",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
                  "source_lines": "L245-L249",
                  "source_section": "10. Currency Governance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY_INPUTS",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "policy_version": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
                },
                "identifier": "BRD-WS-05-R014.POLICY_VERSION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
                  "source_lines": "L245-L249",
                  "source_section": "10. Currency Governance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_VERSION",
                  "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY_VERSION",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_VERSION"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
                },
                "identifier": "BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
                  "source_lines": "L245-L249",
                  "source_section": "10. Currency Governance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
                },
                "identifier": "BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-05.md",
                  "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
                  "source_lines": "L245-L249",
                  "source_section": "10. Currency Governance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "OBSERVE.BRD-WS-05-R014.BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
                "source_type": "SOURCE_LITERAL",
                "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
              },
              "identifier": "BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
                "source_lines": "L245-L249",
                "source_section": "10. Currency Governance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-05-R014.BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "POLICY_OUTCOME_EQUALS"
          },
          "obligation_id": "BRD-WS-05-R014-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
              "source_type": "SOURCE_LITERAL",
              "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
            },
            "identifier": "BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-05.md",
              "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
              "source_lines": "L245-L249",
              "source_section": "10. Currency Governance"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "OBSERVE.BRD-WS-05-R014.BRD-WS-05-R014.BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
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
                  "BRD-WS-05-R014.POLICY.OUTCOME.CONFORMING"
                ],
                "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
                "source_type": "SOURCE_LITERAL",
                "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
              },
              "identifier": "BRD-WS-05-R014.POLICY.OUTCOME.CONFORMING",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
                "source_lines": "L245-L249",
                "source_section": "10. Currency Governance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_OUTCOME",
                "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY.OUTCOME.CONFORMING",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_OUTCOME"
            },
            "policy": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
                "source_type": "SOURCE_LITERAL",
                "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
              },
              "identifier": "BRD-WS-05-R014.POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
                "source_lines": "L245-L249",
                "source_section": "10. Currency Governance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "policy_inputs": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
                "source_type": "SOURCE_LITERAL",
                "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
              },
              "identifier": "BRD-WS-05-R014.POLICY_INPUTS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
                "source_lines": "L245-L249",
                "source_section": "10. Currency Governance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY_INPUTS",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "policy_version": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
                "source_type": "SOURCE_LITERAL",
                "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
              },
              "identifier": "BRD-WS-05-R014.POLICY_VERSION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-05.md",
                "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
                "source_lines": "L245-L249",
                "source_section": "10. Currency Governance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.BRD-WS-05-R014.BRD-WS-05-R014.POLICY_VERSION",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          }
        }
      ],
      "boundary_cases": [
        "Independent records without a parent-child relationship are not subject to this pair constraint"
      ],
      "contract_ast_sha256": "360975b96c2c11e887876ed407f5130d1d08e8bba2491016dc961160f614ce66",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-05-R014",
      "criticality": "CRITICAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-05.md#10. Currency Governance",
            "source_type": "SOURCE_LITERAL",
            "version": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004"
          },
          "identifier": "BRD-WS-05-R014.BRD-WS-05-R014.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-05-R014.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-05.md",
            "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
            "source_lines": "L245-L249",
            "source_section": "10. Currency Governance"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-05-R014.BRD-WS-05-R014.BRD-WS-05-R014.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-05-R014.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PARENT_ID",
          "FIELD.CHILD_ID",
          "FIELD.PARENT_EFFECTIVE_DATE",
          "FIELD.CHILD_EFFECTIVE_DATE",
          "FIELD.CONSISTENCY_RESULT"
        ],
        "producer": "BRD-WS-05-R014.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-05-R014.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PARENT_ID",
          "FIELD.CHILD_ID",
          "FIELD.PARENT_EFFECTIVE_DATE",
          "FIELD.CHILD_EFFECTIVE_DATE",
          "FIELD.CONSISTENCY_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-05-R014.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-05-R014.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-05-R014.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-5E6094A8BE2D6613BA3B",
        "P2C-C4-FX-AEA86889A04ABF7DAB84",
        "P2C-C4-FX-2711EB4A75B39F4A06B5"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Their Effective Dates conflict"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-05-R014-O001",
          "obligation_text": "Parent và Child phải thống nhất: - Effective Date"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-05-R014.O1.1.POLICY_OUTCOME_EQUALS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-05-R014-O001"
        }
      ],
      "operator_composition": [
        "POLICY_OUTCOME_EQUALS"
      ],
      "positive_oracles": [
        "Parent and Child Effective Date values are consistent under the promotion policy"
      ],
      "preconditions": [
        "Both records have Effective Date values"
      ],
      "prohibitions": [
        "Their Effective Dates conflict"
      ],
      "requirement_id": "BRD-WS-05-R014",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-05.md",
        "source_fingerprint": "7e9019a3d0f8bf30f5bf7b6b4f868d6a5c0397a293bd027f65347ede9171f004",
        "source_lines": "L245-L249",
        "source_section": "10. Currency Governance"
      },
      "source_statement": "Parent và Child phải thống nhất: - Effective Date",
      "surrounding_source_context": "### BRD-WS-05-R014 — Parent và Child phải thống nhất: - Effective Date"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-05-R014",
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
        "BRD-WS-05-R014-AC001",
        "BRD-WS-05-R014-AC002",
        "BRD-WS-05-R014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R014-O001",
      "obligation_text": "Parent và Child phải thống nhất: - Effective Date"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R014 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Parent và Child phải thống nhất: - Effective Date",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-014",
    "previous_temporary_key": "TMP-BRD-WS-05-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Currency Governance",
    "source_context_sha256": "fb98cbeb4e8b8ea83f216887a46f4032a51e081ab9d7b34118d355f4b359ae86",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "45e9abf57c3311cbb59d5e5d64c019c37a0d9b6da28e6981ac2791d0ef374f1d",
    "source_lines": "L5259-L6233",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R014"
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
  "stable_id": "BRD-WS-05-R014",
  "title": "Parent và Child phải thống nhất: - Effective Date",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R015 — Parent và Child phải thống nhất: - Exchange Policy

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
      "requirement_id": "BRD-WS-05-R015",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "2475a7989b6da9f26693af596a7ceb913b7d75dafb5c47c299117bc75705d3b6"
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
        "BRD-WS-05-R015-AC001",
        "BRD-WS-05-R015-AC002",
        "BRD-WS-05-R015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R015-O001",
      "obligation_text": "Parent và Child phải thống nhất: - Exchange Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R015 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R015 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R015 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R015-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R015-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R015 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Parent và Child phải thống nhất: - Exchange Policy",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-015",
    "previous_temporary_key": "TMP-BRD-WS-05-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Currency Governance",
    "source_context_sha256": "fb98cbeb4e8b8ea83f216887a46f4032a51e081ab9d7b34118d355f4b359ae86",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "2475a7989b6da9f26693af596a7ceb913b7d75dafb5c47c299117bc75705d3b6",
    "source_lines": "L6235-L6343",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R015"
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
  "stable_id": "BRD-WS-05-R015",
  "title": "Parent và Child phải thống nhất: - Exchange Policy",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R016 — Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải cảnh báo

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-05-R016",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "ceac73c75ad29b4ae15bd21475efc58796e0fbeae39704d6bc9c3e2536423084"
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
        "BRD-WS-05-R016-AC001",
        "BRD-WS-05-R016-AC002",
        "BRD-WS-05-R016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R016-O001",
      "obligation_text": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải cảnh báo"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R016 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R016 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R016 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R016-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R016-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R016 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải cảnh báo.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-05.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "11. Margin Policy"
    },
    "deterministic_transformation": "RESTORE_MARGIN_POLICY_CONDITION",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-016",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-05-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Margin Policy",
    "source_context_sha256": "71b093d07d83758c10d9b0a16f53c7c6b13c3690ddf663dfd053e259bafb8679",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "ceac73c75ad29b4ae15bd21475efc58796e0fbeae39704d6bc9c3e2536423084",
    "source_fingerprint_before_c3": "ea03b79ea7f4837e8ba68d048a8387a5f9baf7a1fac5a432e785d58a7902733b",
    "source_lines": "L6345-L6474",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-05.md",
      "lines": "L273-L275",
      "section": "11. Margin Policy"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R016"
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
  "stable_id": "BRD-WS-05-R016",
  "title": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải cảnh báo",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R017 — Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải yêu cầu lý do

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-05-R017",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "12d0b7beba88996cba25dcccffc3eaef97ccc9fa1a4f9b267a17c48a381dee77"
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
        "BRD-WS-05-R017-AC001",
        "BRD-WS-05-R017-AC002",
        "BRD-WS-05-R017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R017-O001",
      "obligation_text": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải yêu cầu lý do"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R017 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R017 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R017 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R017-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R017-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R017 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải yêu cầu lý do.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-05.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "11. Margin Policy"
    },
    "deterministic_transformation": "RESTORE_MARGIN_POLICY_CONDITION",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-017",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-05-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Margin Policy",
    "source_context_sha256": "71b093d07d83758c10d9b0a16f53c7c6b13c3690ddf663dfd053e259bafb8679",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "12d0b7beba88996cba25dcccffc3eaef97ccc9fa1a4f9b267a17c48a381dee77",
    "source_fingerprint_before_c3": "688136067d78dbc2da9233ff30504965380ebdb93272ea65f8e3105f9739dccb",
    "source_lines": "L6476-L6605",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-05.md",
      "lines": "L273-L276",
      "section": "11. Margin Policy"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R017"
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
  "stable_id": "BRD-WS-05-R017",
  "title": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải yêu cầu lý do",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R018 — Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải thông báo Parent Organ…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-05-R018",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "b9a009e799415e894929faff47234005d66f6dc8fbf2403e04577d054f426dee"
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
        "BRD-WS-05-R018-AC001",
        "BRD-WS-05-R018-AC002",
        "BRD-WS-05-R018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R018-O001",
      "obligation_text": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải thông báo Parent Organization"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R018 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R018 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R018 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R018-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R018-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R018 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải thông báo Parent Organization.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-05.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "11. Margin Policy"
    },
    "deterministic_transformation": "RESTORE_MARGIN_POLICY_CONDITION",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-018",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-05-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Margin Policy",
    "source_context_sha256": "71b093d07d83758c10d9b0a16f53c7c6b13c3690ddf663dfd053e259bafb8679",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "b9a009e799415e894929faff47234005d66f6dc8fbf2403e04577d054f426dee",
    "source_fingerprint_before_c3": "c8fe2db062627c02f868945fec9d6911f19b8e513e62af54f74ad7e438dbecfd",
    "source_lines": "L6607-L6736",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-05.md",
      "lines": "L273-L277",
      "section": "11. Margin Policy"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R018"
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
  "stable_id": "BRD-WS-05-R018",
  "title": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải thông báo Parent Organ…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R019 — Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải ghi audit

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-05-R019",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "86d5ad78449eb8d71adefc5efe231bb0ca22ad0f5cfc4bb417ed9da9417bc362"
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
        "BRD-WS-05-R019-AC001",
        "BRD-WS-05-R019-AC002",
        "BRD-WS-05-R019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R019-O001",
      "obligation_text": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải ghi audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R019 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R019 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R019 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R019-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R019-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R019 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải ghi audit.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-05.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "11. Margin Policy"
    },
    "deterministic_transformation": "RESTORE_MARGIN_POLICY_CONDITION",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-019",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-05-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Margin Policy",
    "source_context_sha256": "71b093d07d83758c10d9b0a16f53c7c6b13c3690ddf663dfd053e259bafb8679",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "86d5ad78449eb8d71adefc5efe231bb0ca22ad0f5cfc4bb417ed9da9417bc362",
    "source_fingerprint_before_c3": "5812c4bf36e15390c9a94a2dcf40caace03dfdda8f6c6255b789492f911d728a",
    "source_lines": "L6738-L6867",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-05.md",
      "lines": "L273-L278",
      "section": "11. Margin Policy"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R019"
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
  "stable_id": "BRD-WS-05-R019",
  "title": "Khi Selling Price thấp hơn Cost hoặc Parent Recommendation, Platform phải ghi audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R020 — Mọi thay đổi Price Book phải được thực hiện thông qua Price Change Set

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
      "requirement_id": "BRD-WS-05-R020",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "fddf36acbf5795d3ef041673fe77ac3445242fa85980eaa3020ad39c406f4c66"
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
        "BRD-WS-05-R020-AC001",
        "BRD-WS-05-R020-AC002",
        "BRD-WS-05-R020-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R020-O001",
      "obligation_text": "Mọi thay đổi Price Book phải được thực hiện thông qua Price Change Set"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R020 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R020 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R020 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R020-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R020-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R020 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thay đổi Price Book phải được thực hiện thông qua Price Change Set.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-020",
    "previous_temporary_key": "TMP-BRD-WS-05-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Price Change Set",
    "source_context_sha256": "bdbf1e3348c64cf7d68bbf0c8e0d6a5e46ceed5e54ee5fda60c5c53dcd1223df",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "fddf36acbf5795d3ef041673fe77ac3445242fa85980eaa3020ad39c406f4c66",
    "source_lines": "L6869-L6977",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R020"
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
  "stable_id": "BRD-WS-05-R020",
  "title": "Mọi thay đổi Price Book phải được thực hiện thông qua Price Change Set",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R021 — Trước payment initiation, Platform phải chứng minh toàn bộ order có commercial eligibility gồm p…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-05-R021",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "e1eca663e62adedb995c53f53ec855b2025f9d8392b440284dc849c6128f4e31"
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
        "BRD-WS-05-R021-AC001",
        "BRD-WS-05-R021-AC008",
        "BRD-WS-05-R021-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R021-O001",
      "obligation_text": "Pricing validity must be confirmed before payment initiation"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-05-R021-AC002",
        "BRD-WS-05-R021-AC008",
        "BRD-WS-05-R021-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R021-O002",
      "obligation_text": "Minimum-margin and cost policy must be satisfied before payment initiation"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-05-R021-AC003",
        "BRD-WS-05-R021-AC008",
        "BRD-WS-05-R021-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R021-O003",
      "obligation_text": "Supplier commercial terms and required approvals must be satisfied"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-05-R021-AC004",
        "BRD-WS-05-R021-AC008",
        "BRD-WS-05-R021-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R021-O004",
      "obligation_text": "Allocatable stock uses the reservation path"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-05-R021-AC005",
        "BRD-WS-05-R021-AC008",
        "BRD-WS-05-R021-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R021-O005",
      "obligation_text": "When procurement is required, procurement feasibility must be confirmed before payment initiation"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-05-R021-AC006",
        "BRD-WS-05-R021-AC008",
        "BRD-WS-05-R021-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R021-O006",
      "obligation_text": "The entire order must be fulfillable under the v2.3 no-partial policy"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-05-R021-AC007",
        "BRD-WS-05-R021-AC008",
        "BRD-WS-05-R021-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R021-O007",
      "obligation_text": "Commercial or procurement validation failure blocks payment initiation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R021 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R021 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R021 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R021-AC008"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R021-AC001",
        "BRD-WS-05-R021-AC002",
        "BRD-WS-05-R021-AC003",
        "BRD-WS-05-R021-AC004",
        "BRD-WS-05-R021-AC005",
        "BRD-WS-05-R021-AC006",
        "BRD-WS-05-R021-AC007"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R021 does not define a recovery obligation."
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-019",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trước payment initiation, Platform phải chứng minh toàn bộ order có commercial eligibility gồm pricing validity, minimum-margin/cost policy, supplier commercial terms, required approvals, inventory availability hoặc procurement feasibility, và khả năng fulfill toàn bộ order theo no-partial policy v2.3; khi có allocatable stock phải dùng reservation path, khi cần procurement phải xác nhận procurement feasibility, và mọi commercial/procurement validation failure phải block payment initiation.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-021",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": "TMP-BRD-WS-05-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Commercial Consistency Principle",
    "source_context_sha256": "0559996de13bf4b1e203f2a3702ccad5afab8cbd895d6bccf8f1fa8374c70cab",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "e1eca663e62adedb995c53f53ec855b2025f9d8392b440284dc849c6128f4e31",
    "source_fingerprint_before_c3": "be65e84eaeb1c705861c317ce204c84c0394dfce6a0c5cad9c59e6f62b4909a1",
    "source_lines": "L6979-L7175",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R021"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-07-003",
      "BRD-WS-07-R003"
    ],
    "derived_requirements": []
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-05-R021",
  "title": "Trước payment initiation, Platform phải chứng minh toàn bộ order có commercial eligibility gồm p…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R022 — Trước khi Publish Price Change Set, hệ thống phải: - kiểm tra Payment Session đang mở

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
      "requirement_id": "BRD-WS-05-R022",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "c773f56aa80d2ab1e028e1df3ecced4fb97bb6b11bc8f1750bd3420f07014af4"
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
        "BRD-WS-05-R022-AC001",
        "BRD-WS-05-R022-AC002",
        "BRD-WS-05-R022-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R022-O001",
      "obligation_text": "Trước khi Publish Price Change Set, hệ thống phải: - kiểm tra Payment Session đang mở"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R022 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R022 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R022 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R022-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R022-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R022 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trước khi Publish Price Change Set, hệ thống phải: - kiểm tra Payment Session đang mở",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-022",
    "previous_temporary_key": "TMP-BRD-WS-05-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Publish Guard",
    "source_context_sha256": "e9b0a37bce20c29b4ac791f85c27d4023d93ba51a77d83fb3d0c7dfa3b1b5bfe",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "c773f56aa80d2ab1e028e1df3ecced4fb97bb6b11bc8f1750bd3420f07014af4",
    "source_lines": "L7177-L7285",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R022"
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
  "stable_id": "BRD-WS-05-R022",
  "title": "Trước khi Publish Price Change Set, hệ thống phải: - kiểm tra Payment Session đang mở",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R023 — Trước khi Publish Price Change Set, hệ thống phải: - cảnh báo số lượng Payment Session bị ảnh hư…

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
      "requirement_id": "BRD-WS-05-R023",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "30d05782f91f9ad8d687d71aac275affb6dfd4a337512b6b3a824880b467ee4d"
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
        "BRD-WS-05-R023-AC001",
        "BRD-WS-05-R023-AC002",
        "BRD-WS-05-R023-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R023-O001",
      "obligation_text": "Trước khi Publish Price Change Set, hệ thống phải: - cảnh báo số lượng Payment Session bị ảnh hưởng"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R023 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R023 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R023 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R023-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R023-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R023 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trước khi Publish Price Change Set, hệ thống phải: - cảnh báo số lượng Payment Session bị ảnh hưởng",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-023",
    "previous_temporary_key": "TMP-BRD-WS-05-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Publish Guard",
    "source_context_sha256": "e9b0a37bce20c29b4ac791f85c27d4023d93ba51a77d83fb3d0c7dfa3b1b5bfe",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "30d05782f91f9ad8d687d71aac275affb6dfd4a337512b6b3a824880b467ee4d",
    "source_lines": "L7287-L7395",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R023"
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
  "stable_id": "BRD-WS-05-R023",
  "title": "Trước khi Publish Price Change Set, hệ thống phải: - cảnh báo số lượng Payment Session bị ảnh hư…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R024 — Trước khi Publish Price Change Set, hệ thống phải: - cho phép Review

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
      "requirement_id": "BRD-WS-05-R024",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "4adaed4b24314fda1f95e6b62b138c4e6a68f8a4e6a8c75d64dc352616918c8b"
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
        "BRD-WS-05-R024-AC001",
        "BRD-WS-05-R024-AC002",
        "BRD-WS-05-R024-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R024-O001",
      "obligation_text": "Trước khi Publish Price Change Set, hệ thống phải: - cho phép Review"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R024 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R024 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R024 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R024-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R024-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R024 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trước khi Publish Price Change Set, hệ thống phải: - cho phép Review",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-024",
    "previous_temporary_key": "TMP-BRD-WS-05-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Publish Guard",
    "source_context_sha256": "e9b0a37bce20c29b4ac791f85c27d4023d93ba51a77d83fb3d0c7dfa3b1b5bfe",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "4adaed4b24314fda1f95e6b62b138c4e6a68f8a4e6a8c75d64dc352616918c8b",
    "source_lines": "L7397-L7505",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R024"
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
  "stable_id": "BRD-WS-05-R024",
  "title": "Trước khi Publish Price Change Set, hệ thống phải: - cho phép Review",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R025 — Trước khi Publish Price Change Set, hệ thống phải: - cho phép Delay Publish

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
      "requirement_id": "BRD-WS-05-R025",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "2135572b14f94c18c167db960ba3ea157d8d8bd90112c67e8fc5652c22df0fad"
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
        "BRD-WS-05-R025-AC001",
        "BRD-WS-05-R025-AC002",
        "BRD-WS-05-R025-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R025-O001",
      "obligation_text": "Trước khi Publish Price Change Set, hệ thống phải: - cho phép Delay Publish"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R025 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R025 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R025 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R025-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R025-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R025 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trước khi Publish Price Change Set, hệ thống phải: - cho phép Delay Publish",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-025",
    "previous_temporary_key": "TMP-BRD-WS-05-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Publish Guard",
    "source_context_sha256": "e9b0a37bce20c29b4ac791f85c27d4023d93ba51a77d83fb3d0c7dfa3b1b5bfe",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "2135572b14f94c18c167db960ba3ea157d8d8bd90112c67e8fc5652c22df0fad",
    "source_lines": "L7507-L7615",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R025"
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
  "stable_id": "BRD-WS-05-R025",
  "title": "Trước khi Publish Price Change Set, hệ thống phải: - cho phép Delay Publish",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R026 — Trước khi Publish Price Change Set, hệ thống phải: - cho phép Continue Publish

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
      "requirement_id": "BRD-WS-05-R026",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "4255dd8b26e3516de5c83e95fbf082798ab7fe8e86f11ef918bf8cb26da16331"
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
        "BRD-WS-05-R026-AC001",
        "BRD-WS-05-R026-AC002",
        "BRD-WS-05-R026-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R026-O001",
      "obligation_text": "Trước khi Publish Price Change Set, hệ thống phải: - cho phép Continue Publish"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R026 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R026 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R026 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R026-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R026-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R026 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trước khi Publish Price Change Set, hệ thống phải: - cho phép Continue Publish",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-026",
    "previous_temporary_key": "TMP-BRD-WS-05-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Publish Guard",
    "source_context_sha256": "e9b0a37bce20c29b4ac791f85c27d4023d93ba51a77d83fb3d0c7dfa3b1b5bfe",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "4255dd8b26e3516de5c83e95fbf082798ab7fe8e86f11ef918bf8cb26da16331",
    "source_lines": "L7617-L7725",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R026"
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
  "stable_id": "BRD-WS-05-R026",
  "title": "Trước khi Publish Price Change Set, hệ thống phải: - cho phép Continue Publish",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R027 — Trong phiên bản 2.0: - Payment Owner được cố định theo Commercial Agreement

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
      "requirement_id": "BRD-WS-05-R027",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "4c91956ab7eff33f4a4c64ca3afeb74d90e86b95ced68245dc25e2e4072c21eb"
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
        "BRD-WS-05-R027-AC001",
        "BRD-WS-05-R027-AC002",
        "BRD-WS-05-R027-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R027-O001",
      "obligation_text": "Trong phiên bản 2.0: - Payment Owner được cố định theo Commercial Agreement"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R027 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R027 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R027 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R027-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R027-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R027 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trong phiên bản 2.0: - Payment Owner được cố định theo Commercial Agreement.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-05-010"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-027",
    "previous_temporary_key": "TMP-BRD-WS-05-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Payment Owner",
    "source_context_sha256": "6891915c218e97921f6c9f4987411dddf442cf91e9f1d20634e00ee6f087d595",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "4c91956ab7eff33f4a4c64ca3afeb74d90e86b95ced68245dc25e2e4072c21eb",
    "source_lines": "L7727-L7838",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R027"
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
  "stable_id": "BRD-WS-05-R027",
  "title": "Trong phiên bản 2.0: - Payment Owner được cố định theo Commercial Agreement",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R028 — Trong phiên bản 2.0: - Không hỗ trợ thay đổi theo Campaign

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-05-R028",
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
  "normative_statement": "Trong phiên bản 2.0: - Không hỗ trợ thay đổi theo Campaign.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-05-010"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-028",
    "previous_temporary_key": "TMP-BRD-WS-05-028",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Payment Owner",
    "source_context_sha256": "6891915c218e97921f6c9f4987411dddf442cf91e9f1d20634e00ee6f087d595",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "e9fcd51e18e837281959c85f3b6982476150a2096105b9bb84a50c6dc683ade3",
    "source_lines": "L7840-L7901",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R028"
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
  "stable_id": "BRD-WS-05-R028",
  "title": "Trong phiên bản 2.0: - Không hỗ trợ thay đổi theo Campaign",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R029 — Trong phiên bản 2.0: - Nếu thanh toán tiền mặt thì Payment Owner là Organization sở hữu Storefro…

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
      "requirement_id": "BRD-WS-05-R029",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "bb0f4af07133b132264a42ecbb407f9a482ac4949fab6c3089d8410041ca2926"
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
        "BRD-WS-05-R029-AC001",
        "BRD-WS-05-R029-AC002",
        "BRD-WS-05-R029-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R029-O001",
      "obligation_text": "Trong phiên bản 2.0: - Nếu thanh toán tiền mặt thì Payment Owner là Organization sở hữu Storefront"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R029 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R029 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R029 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R029-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R029-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R029 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Trong phiên bản 2.0: - Nếu thanh toán tiền mặt thì Payment Owner là Organization sở hữu Storefront.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-05-010"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-05-029",
    "previous_temporary_key": "TMP-BRD-WS-05-029",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Payment Owner",
    "source_context_sha256": "6891915c218e97921f6c9f4987411dddf442cf91e9f1d20634e00ee6f087d595",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "bb0f4af07133b132264a42ecbb407f9a482ac4949fab6c3089d8410041ca2926",
    "source_lines": "L7903-L8014",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R029"
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
  "stable_id": "BRD-WS-05-R029",
  "title": "Trong phiên bản 2.0: - Nếu thanh toán tiền mặt thì Payment Owner là Organization sở hữu Storefro…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R030 — Partner bán dưới Cost phải nhận Warning

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-05-R030",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "01a629cd3972844f9551bc70c149d4d3d7e657409a680c5f36c6844c66282e09"
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
        "BRD-WS-05-R030-AC001",
        "BRD-WS-05-R030-AC002",
        "BRD-WS-05-R030-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R030-O001",
      "obligation_text": "Partner bán dưới Cost phải nhận Warning"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R030 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R030 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R030 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R030-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R030-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R030 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Partner bán dưới Cost phải nhận Warning.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-05-008",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-05-R030",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-008",
    "source_context_sha256": "4b3964499096f5967517741b362afda424073f5f230ff5e6589d0d12d5674b96",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "01a629cd3972844f9551bc70c149d4d3d7e657409a680c5f36c6844c66282e09",
    "source_fingerprint_before_c3": "01a629cd3972844f9551bc70c149d4d3d7e657409a680c5f36c6844c66282e09",
    "source_lines": "L8016-L8141",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R030"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-05-008"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-05-008"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-05-R030",
  "title": "Partner bán dưới Cost phải nhận Warning",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-05-R031 — Partner bán dưới Cost phải tạo Audit evidence

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-05-R031",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "source_fingerprint": "7d527e8ea9d243a06d8309eb0e75e0a47b8d0ec0fbe73727267175a93b5e0a95"
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
        "BRD-WS-05-R031-AC001",
        "BRD-WS-05-R031-AC002",
        "BRD-WS-05-R031-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-05-R031-O001",
      "obligation_text": "Partner bán dưới Cost phải tạo Audit evidence"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R031 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R031 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R031 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R031-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-05-R031-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-05-R031 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Partner bán dưới Cost phải tạo Audit evidence.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-05-008",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-05-R031",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-05-008",
    "source_context_sha256": "4b3964499096f5967517741b362afda424073f5f230ff5e6589d0d12d5674b96",
    "source_document": "docs/BRD/BRD-WS-05.md",
    "source_fingerprint": "7d527e8ea9d243a06d8309eb0e75e0a47b8d0ec0fbe73727267175a93b5e0a95",
    "source_fingerprint_before_c3": "7d527e8ea9d243a06d8309eb0e75e0a47b8d0ec0fbe73727267175a93b5e0a95",
    "source_lines": "L8143-L8268",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-05-R031"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-05-008"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-05-008"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-05-R031",
  "title": "Partner bán dưới Cost phải tạo Audit evidence",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
