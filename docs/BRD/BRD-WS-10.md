---
document_code: "BRD-WS-10"
document_id: "BRD-WS-10"
title: "Settlement, Revenue Sharing & Financial Lifecycle"
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

# BRD Workshop 10

# Settlement, Revenue Sharing & Financial Lifecycle

---

# 1. Workshop Objective

Workshop này xác định toàn bộ Financial Domain của YSim.

Bao gồm:

- Settlement
- Revenue Sharing
- Commission
- Financial Event
- Financial Snapshot
- Financial Account
- Wallet
- Event Ledger
- Reconciliation
- Financial Export

Workshop này không mô tả:

- ERP
- General Ledger
- Thuế kế toán
- Auto Payout

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| SettlementBatch | Transaction |
| SettlementItem | Transaction |
| SettlementSnapshot | Transaction |
| FinancialEvent | Transaction |
| FinancialSnapshot | Transaction |
| EventLedger | Transaction |
| RevenueSharing | Transaction |
| RevenueRecipient | Master |
| CommissionSnapshot | Transaction |
| FinancialAccount | Master |
| Wallet | Master |
| ReconciliationCase | Transaction |
| ReconciliationEvidence | Transaction |
| ReconciliationDecision | Transaction |
| ManualAdjustment | Transaction |
| FinancialExport | Transaction |

---

# 3. Financial Domain Architecture

Financial Domain được tổ chức theo các lớp sau:

```text
Commercial Snapshot
        │
        ▼
Payment Snapshot
        │
        ▼
Fulfillment Snapshot
        │
        ▼
Financial Snapshot
        │
        ▼
Settlement
        │
        ▼
Reconciliation
        │
        ▼
Revenue Sharing
        │
        ▼
Commission
        │
        ▼
Event Ledger
        │
        ▼
Financial Export
```

Financial Domain chỉ đọc dữ liệu từ các Snapshot.

Không sửa dữ liệu giao dịch gốc.

---

# 4. Settlement

Settlement được thực hiện giữa các thực thể trong Distribution Network.

Ví dụ:

```text
Supplier

↑

YSim

↑

ABC Travel

↑

Agency

↑

Collaborator
```

Settlement không thực hiện giữa Customer và Merchant.

Thanh toán Customer đã hoàn thành tại Payment Domain.

---

# 5. Settlement Cycle

Settlement hỗ trợ:

- Realtime
- Daily
- Weekly
- Monthly
- Custom Date Range

Khoảng thời gian Settlement tùy chỉnh không vượt quá:

**03 tháng**

Chu kỳ Settlement được quy định trong Commercial Agreement.

---

# 6. Financial Event

Mọi Transaction đều phát sinh FinancialEvent.

Ví dụ:

- Payment Success
- Refund
- Purchase Order
- Settlement
- Commission
- Manual Adjustment

FinancialEvent là nguồn dữ liệu chuẩn của Financial Domain.

---

# 7. Settlement Scope

Version 2.0 thực hiện Settlement theo:

**SalesOrder**

Settlement theo SalesOrderItem sẽ được xem xét ở các phiên bản sau.

Settlement vẫn lưu các thông tin:

- Payment Difference
- Over Payment
- Under Payment
- Invoice Difference

để phục vụ Reconciliation.

---

# 8. Commission Snapshot

CommissionSnapshot phát sinh:

Ngay sau Payment Success.

Trạng thái mặc định:

```text
Pending
```

Sau khi Settlement được xác nhận:

```text
Confirmed
```

---

# 9. Revenue Sharing

Revenue Sharing được tính theo:

**Bottom-Up Distribution**

Ví dụ:

```text
Sales

↑

Collaborator

↑

Agency

↑

ABC Travel

↑

YSim
```

Financial Visibility được giới hạn theo Distribution Hierarchy.

- Child không nhìn thấy Revenue Sharing của Parent.
- Parent không nhìn thấy Revenue Sharing của Grand Child.
- YSim có quyền xem toàn bộ.

---

# 10. Revenue Recipient

RevenueRecipient là Business Object.

RevenueRecipient có thể là:

- Organization
- Department
- Collaborator
- Sales
- Affiliate *(Reserved)*

RevenueRecipient là chủ sở hữu của:

- Commission
- Revenue Sharing
- Settlement Result

---

# 11. Settlement Snapshot

SettlementSnapshot lưu:

- Commercial Snapshot
- Payment Snapshot
- Fulfillment Snapshot
- Multi-level Cost
- Multi-level Price
- Tax
- Fee
- Exchange Rate
- Revenue Sharing
- Commission
- FinancialEvent Reference

Settlement luôn dựa trên Snapshot.

---

# 12. Event Ledger

YSim sử dụng:

**Event Ledger**

Event Ledger không phải hệ thống kế toán.

Ledger chỉ ghi nhận:

- FinancialEvent

---

# 13. Financial Account

FinancialAccount là Business Object.

FinancialAccount hỗ trợ:

- Wallet
- Accounts Receivable
- Accounts Payable
- Commission Payable
- Promotion Funding
- Settlement Balance

FinancialAccount phục vụ Business Settlement.

Không thay thế ERP.

---

# 14. Wallet

Wallet thuộc:

- Organization
- Collaborator

Collaborator Wallet hoạt động tương tự Organization Wallet.

Quyền sử dụng Wallet được xác định trong Commercial Agreement.

---

# 15. Supplier Settlement

Supplier Settlement thuộc cùng Financial Domain.

Settlement Engine quản lý:

- Distribution Settlement
- Supplier Settlement

trên cùng một nền tảng.

---

# 16. Multi Currency Settlement

Settlement giữa Parent và Child sử dụng:

**Settlement Currency**

Settlement Currency được quy định trong Commercial Agreement.

Settlement Currency không thay đổi trong suốt kỳ Settlement.

---

# 17. Exchange Difference

Financial Domain hỗ trợ:

- FX Gain
- FX Loss

Việc tính toán dựa trên:

FX Configuration Policy của Organization.

Nguồn tỷ giá có thể:

- ECB
- Vietcombank
- hoặc nguồn khác theo Agreement.

---

# 18. Refund Settlement

Refund phát sinh:

Rollback.

Rollback bao gồm:

- Settlement
- Revenue Sharing
- Commission

Rollback luôn sinh FinancialEvent mới.

Không sửa dữ liệu gốc.

---

# 19. Chargeback

Chargeback không triển khai trong Version 2.0.

Được giữ chỗ trong kiến trúc Financial Domain.

---

# 20. Payout

Version 2.0:

Không hỗ trợ Auto Payout.

Settlement chỉ xác nhận nghĩa vụ thanh toán.

Việc chuyển tiền thực tế được thực hiện thủ công.

---

# 21. Settlement Approval

SettlementBatch yêu cầu Approval.

Approval dựa trên:

Role Permission.

Toàn bộ Approval được Audit.

---

# 22. Financial Export

Financial Export hỗ trợ:

- Excel
- CSV
- REST API

ERP sẽ Import dữ liệu từ Financial Export.

---

# 23. Financial Snapshot

FinancialSnapshot tổng hợp:

- Commercial Snapshot
- Payment Snapshot
- Fulfillment Snapshot

FinancialSnapshot là đầu vào duy nhất của Settlement.

---

# 24. Settlement Status

SettlementBatch hỗ trợ các trạng thái:

```text
Draft

↓

Calculated

↓

Pending Approval

↓

Approved

↓

Denied

↓

Exported

↓

Paid

↓

Closed
```

Denied yêu cầu:

- Reason
- Recalculation

---

# 25. Reconciliation

Settlement hỗ trợ Reconciliation.

Quy trình:

```text
Calculate

↓

Compare

↓

Difference

↓

Review

↓

Approve

↓

Close
```

---

# 26. Settlement Difference

Settlement Difference được phân loại:

- Missing Payment
- Missing Order
- Amount Difference
- FX Difference
- Manual Adjustment
- Gateway Difference
- Supplier Difference

Mỗi Difference đều sinh:

ReconciliationCase.

---

# 27. Manual Adjustment

Financial Domain hỗ trợ:

ManualAdjustment.

ManualAdjustment yêu cầu:

- Approval
- Audit

ManualAdjustment không sửa dữ liệu giao dịch gốc.

ManualAdjustment luôn sinh:

FinancialEvent.

---

# 28. Enterprise Financial Principle

Settlement không sửa dữ liệu gốc.

Settlement chỉ đọc:

- Commercial Snapshot
- Payment Snapshot
- Fulfillment Snapshot
- Financial Snapshot

Nếu phát hiện sai lệch:

Không sửa:

- SalesOrder
- Payment
- Snapshot

Hệ thống tạo:

- ReconciliationCase
- ManualAdjustment
- FinancialEvent

---

# 29. Money Flow ≠ Product Flow

Money Flow độc lập với Product Flow.

## Product Flow

```text
Supplier

↓

Inventory

↓

Allocation

↓

Customer
```

## Money Flow

```text
Customer

↓

Payment Owner

↓

Parent

↓

YSim

↓

Supplier
```

Hai Flow được quản lý độc lập.

---

# 30. Business Decisions (Locked)

## BD-10-001

Settlement thực hiện theo SalesOrder.

---

## BD-10-002

Settlement hỗ trợ chu kỳ cố định hoặc khoảng thời gian tùy chỉnh (≤ 03 tháng).

---

## BD-10-003

Mọi Transaction đều sinh FinancialEvent.

---

## BD-10-004

CommissionSnapshot phát sinh sau Payment Success và ở trạng thái Pending cho đến khi Settlement xác nhận.

---

## BD-10-005

Revenue Sharing tính theo Bottom-Up Distribution.

---

## BD-10-006

RevenueRecipient là Business Object.

---

## BD-10-007

SettlementSnapshot lưu đầy đủ Multi-level Cost và Multi-level Price.

---

## BD-10-008

YSim sử dụng Event Ledger.

---

## BD-10-009

FinancialAccount là Business Object độc lập.

---

## BD-10-010

Wallet hỗ trợ Organization và Collaborator.

---

## BD-10-011

Supplier Settlement thuộc Financial Domain.

---

## BD-10-012

Settlement sử dụng Settlement Currency theo Commercial Agreement.

---

## BD-10-013

Financial Domain hỗ trợ FX Gain/Loss.

---

## BD-10-014

Refund thực hiện Rollback Settlement.

---

## BD-10-015

Chargeback được giữ chỗ cho phiên bản sau.

---

## BD-10-016

Version 2.0 không hỗ trợ Auto Payout.

---

## BD-10-017

SettlementBatch yêu cầu Approval.

---

## BD-10-018

FinancialExport hỗ trợ Excel, CSV và REST API.

---

## BD-10-019

FinancialSnapshot là đầu vào duy nhất của Settlement.

---

## BD-10-020

Settlement hỗ trợ Reconciliation.

---

## BD-10-021

ManualAdjustment yêu cầu Approval và Audit.

---

## BD-10-022

Settlement không sửa dữ liệu giao dịch gốc.

---

## BD-10-023

Money Flow và Product Flow là hai Business Flow độc lập.

---

# 31. Enterprise Design Principles

## EP-10-001

Financial Domain chỉ đọc Snapshot, không sửa Transaction.

---

## EP-10-002

Mọi điều chỉnh tài chính đều được biểu diễn bằng FinancialEvent mới.

---

## EP-10-003

Financial Visibility tuân thủ Distribution Hierarchy.

---

## EP-10-004

Settlement và Reconciliation là hai Capability độc lập.

---

## EP-10-005

Event Ledger là nguồn dữ liệu chuẩn cho Reporting và Financial Export.

---

## EP-10-006

Money Flow độc lập với Product Flow.

---

# 32. Financial Lifecycle

```text
Commercial Snapshot
        │
        ▼
Payment Snapshot
        │
        ▼
Fulfillment Snapshot
        │
        ▼
Financial Snapshot
        │
        ▼
Settlement
        │
        ▼
Reconciliation
        │
        ▼
Revenue Sharing
        │
        ▼
Commission
        │
        ▼
Event Ledger
        │
        ▼
Financial Export
```

---

# 33. Traceability

Workshop này kế thừa:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04
- BRD-WS-05
- BRD-WS-06
- BRD-WS-07
- BRD-WS-08
- BRD-WS-09

---

# 34. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Reporting & BI
- Financial Dashboard
- Settlement Engine
- Customer Support
- ERP Integration
- Accounting Export
- Audit & Compliance
- API
- DMS
- DBD

---

# 35. Workshop Status

**Status:** FROZEN

Workshop này hoàn thiện toàn bộ Financial Domain và Transaction Domain của YSim.

---

# 36. Next Workshop

**BRD-WS-11 – Customer Service, Ticketing & Customer Lifecycle**

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-001 — Settlement thực hiện theo SalesOrder

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
      "requirement_id": "BD-10-001",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "b275245ae67c26db295d9b01975e06b291bed5fcb3ca65ad3534e9dbc8452ed2"
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
        "BD-10-001-AC001",
        "BD-10-001-AC002",
        "BD-10-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-001-O001",
      "obligation_text": "Settlement thực hiện theo SalesOrder"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Settlement thực hiện theo SalesOrder.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-001",
    "source_context_sha256": "bf5240f1f93af4239a9dff51fbc3ed1ace07b3e0ad7f4ca7313dea5791bb0f83",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "b275245ae67c26db295d9b01975e06b291bed5fcb3ca65ad3534e9dbc8452ed2",
    "source_lines": "L916-L991",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-001"
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
  "stable_id": "BD-10-001",
  "title": "Settlement thực hiện theo SalesOrder",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-002 — Settlement hỗ trợ chu kỳ cố định hoặc khoảng thời gian tùy chỉnh (≤ 03 tháng)

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
      "requirement_id": "BD-10-002",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "1c5df516ab75554ede45ac8921f524e246c0c56e70966cab4cd89d723f540b6d"
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
        "BD-10-002-AC001",
        "BD-10-002-AC002",
        "BD-10-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-002-O001",
      "obligation_text": "Settlement hỗ trợ chu kỳ cố định hoặc khoảng thời gian tùy chỉnh (≤ 03 tháng)"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Settlement hỗ trợ chu kỳ cố định hoặc khoảng thời gian tùy chỉnh (≤ 03 tháng).",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-002",
    "source_context_sha256": "cfdaafaea8409e5c2374e905a8d9840f4334af95c26c1f629e12a614a350409c",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "1c5df516ab75554ede45ac8921f524e246c0c56e70966cab4cd89d723f540b6d",
    "source_lines": "L993-L1068",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-002"
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
  "stable_id": "BD-10-002",
  "title": "Settlement hỗ trợ chu kỳ cố định hoặc khoảng thời gian tùy chỉnh (≤ 03 tháng)",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-003 — Mọi Transaction đều sinh FinancialEvent

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
      "requirement_id": "BD-10-003",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "603fbd624389ea7f5a43974b048da63d8dee41723dab55ddee4714996bfac728"
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
        "BD-10-003-AC001",
        "BD-10-003-AC002",
        "BD-10-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-003-O001",
      "obligation_text": "Mọi Transaction đều sinh FinancialEvent"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-003 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Transaction đều sinh FinancialEvent.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-003",
    "source_context_sha256": "b7864c7b3c808821df0dbc7a803ae0710303adff1f350e86de6098cf4a3e22d6",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "603fbd624389ea7f5a43974b048da63d8dee41723dab55ddee4714996bfac728",
    "source_lines": "L1070-L1178",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-003"
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
  "stable_id": "BD-10-003",
  "title": "Mọi Transaction đều sinh FinancialEvent",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-004 — CommissionSnapshot phát sinh sau Payment Success và ở trạng thái Pending cho đến khi Settlement …

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
      "requirement_id": "BD-10-004",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "8b62605a0bb1c5a4f5527bd01a57a85870f4fe3deae095eb6b58d420a8f37dc7"
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
        "BD-10-004-AC001",
        "BD-10-004-AC002",
        "BD-10-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-004-O001",
      "obligation_text": "CommissionSnapshot phát sinh sau Payment Success và ở trạng thái Pending cho đến khi Settlement xác nhận"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "CommissionSnapshot phát sinh sau Payment Success và ở trạng thái Pending cho đến khi Settlement xác nhận.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-004",
    "source_context_sha256": "b7361db884afdadd4c7d3be5a412ef088110c47e47fb36c5baab3430baea7406",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "8b62605a0bb1c5a4f5527bd01a57a85870f4fe3deae095eb6b58d420a8f37dc7",
    "source_lines": "L1180-L1288",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-004"
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
  "stable_id": "BD-10-004",
  "title": "CommissionSnapshot phát sinh sau Payment Success và ở trạng thái Pending cho đến khi Settlement …",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-005 — Revenue Sharing tính theo Bottom-Up Distribution

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
      "requirement_id": "BD-10-005",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "bc88fbda37ad197d405acdb988385fb9549f9d4659a53f0801649b4363d90cc3"
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
        "BD-10-005-AC001",
        "BD-10-005-AC002",
        "BD-10-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-005-O001",
      "obligation_text": "Revenue Sharing tính theo Bottom-Up Distribution"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Revenue Sharing tính theo Bottom-Up Distribution.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-005",
    "source_context_sha256": "5e10d231595619f0a9a47c7327428f4056155b9e0aa19055b1e841f171aa53d3",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "bc88fbda37ad197d405acdb988385fb9549f9d4659a53f0801649b4363d90cc3",
    "source_lines": "L1290-L1365",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-005"
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
  "stable_id": "BD-10-005",
  "title": "Revenue Sharing tính theo Bottom-Up Distribution",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-006 — RevenueRecipient là Business Object

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
      "requirement_id": "BD-10-006",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "c6b4c84e2a9324828b178d1218ee2481184a44f250f1b82504bc6e4075f96fe7"
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
        "BD-10-006-AC001",
        "BD-10-006-AC002",
        "BD-10-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-006-O001",
      "obligation_text": "RevenueRecipient là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "RevenueRecipient là Business Object.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Revenue Recipient",
    "source_context_sha256": "a647554ddef26139d541a9028a61ec94ed32dd9e1d94807e33b5883345e690b3",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "c6b4c84e2a9324828b178d1218ee2481184a44f250f1b82504bc6e4075f96fe7",
    "source_lines": "L1367-L1442",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-006"
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
  "stable_id": "BD-10-006",
  "title": "RevenueRecipient là Business Object",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-007 — SettlementSnapshot lưu đầy đủ Multi-level Cost và Multi-level Price

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
      "requirement_id": "BD-10-007",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "99426e022c800a44e2f786845622f9e16816e18edcc3cc5770301cacec92c971"
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
        "BD-10-007-AC001",
        "BD-10-007-AC002",
        "BD-10-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-007-O001",
      "obligation_text": "SettlementSnapshot lưu đầy đủ Multi-level Cost và Multi-level Price"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "SettlementSnapshot lưu đầy đủ Multi-level Cost và Multi-level Price.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-007",
    "source_context_sha256": "67f0a8ffbe93a307b1405be02b6f45edaadd6abda63b7db4d72116ff2f4dc2f5",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "99426e022c800a44e2f786845622f9e16816e18edcc3cc5770301cacec92c971",
    "source_lines": "L1444-L1519",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-007"
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
  "stable_id": "BD-10-007",
  "title": "SettlementSnapshot lưu đầy đủ Multi-level Cost và Multi-level Price",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-008 — YSim sử dụng Event Ledger

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
      "requirement_id": "BD-10-008",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "be9313171ebe4bc987ed4287fe6e453342f5fcdbe5e914daae40b18f7b4f4b35"
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
        "BD-10-008-AC001",
        "BD-10-008-AC002",
        "BD-10-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-008-O001",
      "obligation_text": "YSim sử dụng Event Ledger"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-008 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-008-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-008-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-008 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "YSim sử dụng Event Ledger.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-008",
    "source_context_sha256": "46c9d6904c55d8c1ddd1555939e4c36957f0b86ea8257092c2102954948c6032",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "be9313171ebe4bc987ed4287fe6e453342f5fcdbe5e914daae40b18f7b4f4b35",
    "source_lines": "L1521-L1629",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-008"
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
  "stable_id": "BD-10-008",
  "title": "YSim sử dụng Event Ledger",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-009 — FinancialAccount là Business Object độc lập

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
      "requirement_id": "BD-10-009",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "d616cfc74ed3ce4f84f702777e332ef6896558a8c62b877567adbc5d43e3131a"
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
        "BD-10-009-AC001",
        "BD-10-009-AC002",
        "BD-10-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-009-O001",
      "obligation_text": "FinancialAccount là Business Object độc lập"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-009-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-009 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-009 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-009-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-009-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-009 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "FinancialAccount là Business Object độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-009",
    "source_context_sha256": "d0371218f6394f4f56ff369edf8e9bc1b195fa2239489ceca084a63d5ef26b6c",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "d616cfc74ed3ce4f84f702777e332ef6896558a8c62b877567adbc5d43e3131a",
    "source_lines": "L1631-L1741",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-009"
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
  "stable_id": "BD-10-009",
  "title": "FinancialAccount là Business Object độc lập",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-010 — Wallet hỗ trợ Organization và Collaborator

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
      "requirement_id": "BD-10-010",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "fbcfb468aaaf83b373af9686942929ca28293983acd06cdf0e3ecf63c1b0e200"
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
        "BD-10-010-AC001",
        "BD-10-010-AC002",
        "BD-10-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-010-O001",
      "obligation_text": "Wallet hỗ trợ Organization và Collaborator"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Wallet hỗ trợ Organization và Collaborator.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-010",
    "source_context_sha256": "2adb885eb01fcb9a7452c89f505bec884665c7e1da3fbcb402d85613d2c05c5d",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "fbcfb468aaaf83b373af9686942929ca28293983acd06cdf0e3ecf63c1b0e200",
    "source_lines": "L1743-L1818",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-010"
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
  "stable_id": "BD-10-010",
  "title": "Wallet hỗ trợ Organization và Collaborator",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-011 — Supplier Settlement thuộc Financial Domain

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
      "requirement_id": "BD-10-011",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "3a0bc08d4f73ba3e021e860682001fd3b7fb39039258401f0330cb7d67f2ef1d"
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
        "BD-10-011-AC001",
        "BD-10-011-AC002",
        "BD-10-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-011-O001",
      "obligation_text": "Supplier Settlement thuộc Financial Domain"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-011 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-011 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-011 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-011-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-011-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-011 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier Settlement thuộc Financial Domain.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-011",
    "source_context_sha256": "a4a861591038a37a84b198e8f9327399181fcccc75c560ed4633b9653cf63cfa",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "3a0bc08d4f73ba3e021e860682001fd3b7fb39039258401f0330cb7d67f2ef1d",
    "source_lines": "L1820-L1932",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-011"
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
  "stable_id": "BD-10-011",
  "title": "Supplier Settlement thuộc Financial Domain",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-012 — Settlement sử dụng Settlement Currency theo Commercial Agreement

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
      "requirement_id": "BD-10-012",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "f3304e1eaf639a40e97c47297d19fe62e3d7a2ae921abbf374bf829f6e2e3726"
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
        "BD-10-012-AC001",
        "BD-10-012-AC002",
        "BD-10-012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-012-O001",
      "obligation_text": "Settlement sử dụng Settlement Currency theo Commercial Agreement"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-012 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-012-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-012-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-012 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Settlement sử dụng Settlement Currency theo Commercial Agreement.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-012",
    "source_context_sha256": "f9aec2084f3e1d8496e852b24c816bbcba0b6f942d89a7ae218b237c7d69d74f",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "f3304e1eaf639a40e97c47297d19fe62e3d7a2ae921abbf374bf829f6e2e3726",
    "source_lines": "L1934-L2042",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-012"
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
  "stable_id": "BD-10-012",
  "title": "Settlement sử dụng Settlement Currency theo Commercial Agreement",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-013 — Financial Domain hỗ trợ FX Gain/Loss

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
      "requirement_id": "BD-10-013",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "489635ea098e27cee9b865773a6026ec8cee7cdffee848adb1e506c02a149e60"
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
        "BD-10-013-AC001",
        "BD-10-013-AC002",
        "BD-10-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-013-O001",
      "obligation_text": "Financial Domain hỗ trợ FX Gain/Loss"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-013 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-013 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-013 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-013-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-013-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-013 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Financial Domain hỗ trợ FX Gain/Loss.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-013",
    "source_context_sha256": "af3550398f77b7fd607d95b76ea07114814de610e8831691bad1aa9433635e09",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "489635ea098e27cee9b865773a6026ec8cee7cdffee848adb1e506c02a149e60",
    "source_lines": "L2044-L2152",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-013"
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
  "stable_id": "BD-10-013",
  "title": "Financial Domain hỗ trợ FX Gain/Loss",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-014 — Refund thực hiện Rollback Settlement

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
      "requirement_id": "BD-10-014",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "216fd1020ccb89c614ed83da3d839145c2ff4f282d1333991ea5531f80267364"
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
        "BD-10-014-AC001",
        "BD-10-014-AC002",
        "BD-10-014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-014-O001",
      "obligation_text": "Refund thực hiện Rollback Settlement"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-014 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Refund thực hiện Rollback Settlement.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-014",
    "source_context_sha256": "e11e07f50b9a3531201fb6335b928ecb7faf79551eda6b05a9304ce3b7bf6e47",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "216fd1020ccb89c614ed83da3d839145c2ff4f282d1333991ea5531f80267364",
    "source_lines": "L2154-L2262",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-014"
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
  "stable_id": "BD-10-014",
  "title": "Refund thực hiện Rollback Settlement",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-015 — Chargeback được giữ chỗ cho phiên bản sau

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BD-10-015",
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
  "normative_statement": "Chargeback được giữ chỗ cho phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-015",
    "source_context_sha256": "bd3876ba9fa8dd2c96d03f50d5e39eabdd3935bae37d1ded3190161e598d97a8",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "96b9a434cfddb4850c1543a1d8e3a6093f54311c08e373b5f40a26f2c2289ff9",
    "source_lines": "L2264-L2322",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-015"
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
  "stable_id": "BD-10-015",
  "title": "Chargeback được giữ chỗ cho phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-016 — Version 2.0 không hỗ trợ Auto Payout

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BD-10-016",
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
  "normative_statement": "Version 2.0 không hỗ trợ Auto Payout.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-016",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-016",
    "source_context_sha256": "4ba793eb532f0843ddd29fb7785a4e883af4252e65476948a5a49cf2bd0f16ad",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "b50ce0de4074940b025d3513cb96c6dcd131136f7600277179c8db663dbcba38",
    "source_lines": "L2324-L2382",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-016"
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
  "stable_id": "BD-10-016",
  "title": "Version 2.0 không hỗ trợ Auto Payout",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-017 — SettlementBatch yêu cầu Approval

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-10-017",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "3be2374982d5f641c7048b15e96e849dfbf649f90a87a8b6cd0f52aa741663bd"
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
        "BD-10-017-AC001",
        "BD-10-017-AC002",
        "BD-10-017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-017-O001",
      "obligation_text": "SettlementBatch yêu cầu Approval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "SettlementBatch yêu cầu Approval.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-017",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Settlement Approval",
    "source_context_sha256": "83d3943518089db79e9913e22ff86b00c1a492e92b8120aad25d57349036e552",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "3be2374982d5f641c7048b15e96e849dfbf649f90a87a8b6cd0f52aa741663bd",
    "source_lines": "L2384-L2465",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-017"
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
  "stable_id": "BD-10-017",
  "title": "SettlementBatch yêu cầu Approval",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-018 — FinancialExport hỗ trợ Excel, CSV và REST API

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
      "requirement_id": "BD-10-018",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "2373855eb7a044369965a3c155e8b5f18c2ccfb2f5c5ad653a72b00ff038bbc2"
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
        "BD-10-018-AC001",
        "BD-10-018-AC002",
        "BD-10-018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-018-O001",
      "obligation_text": "FinancialExport hỗ trợ Excel, CSV và REST API"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-018 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-018 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-018 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-018-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-018-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-018 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "FinancialExport hỗ trợ Excel, CSV và REST API.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-018",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-018",
    "source_context_sha256": "bb8412a67c18942cd9b532002e45f3a218d2d6224ad93308c02dffdeeab6b1ea",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "2373855eb7a044369965a3c155e8b5f18c2ccfb2f5c5ad653a72b00ff038bbc2",
    "source_lines": "L2467-L2575",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-018"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-10-018",
  "title": "FinancialExport hỗ trợ Excel, CSV và REST API",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-019 — FinancialSnapshot là đầu vào duy nhất của Settlement

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
      "requirement_id": "BD-10-019",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "dcdaf60f66b36b0b9383fa684e007b4ade3fceb519c5f2a201336bfa4ec19eb8"
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
        "BD-10-019-AC001",
        "BD-10-019-AC002",
        "BD-10-019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-019-O001",
      "obligation_text": "FinancialSnapshot là đầu vào duy nhất của Settlement"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-019 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-019 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-019 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-019-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-019-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-019 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "FinancialSnapshot là đầu vào duy nhất của Settlement.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-019",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Financial Snapshot",
    "source_context_sha256": "80cb7d1475ebdb006ffe0cc149f46dff7c5df5b845d3dc1a052a96164d32db19",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "dcdaf60f66b36b0b9383fa684e007b4ade3fceb519c5f2a201336bfa4ec19eb8",
    "source_lines": "L2577-L2685",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-019"
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
  "stable_id": "BD-10-019",
  "title": "FinancialSnapshot là đầu vào duy nhất của Settlement",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-020 — Settlement hỗ trợ Reconciliation

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
      "requirement_id": "BD-10-020",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "7a32134cc79b95a1a9096068054806c77feacddfe5dfdfce588433892e0cc1ef"
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
        "BD-10-020-AC001",
        "BD-10-020-AC002",
        "BD-10-020-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-020-O001",
      "obligation_text": "Settlement hỗ trợ Reconciliation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-020 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-020 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-020 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-020-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-020-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-020 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Settlement hỗ trợ Reconciliation.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-020",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Reconciliation",
    "source_context_sha256": "5bf80d817853e0472ec23887c08ed2ba3299707592328e87d23799d0a92b5493",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "7a32134cc79b95a1a9096068054806c77feacddfe5dfdfce588433892e0cc1ef",
    "source_lines": "L2687-L2795",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-020"
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
  "stable_id": "BD-10-020",
  "title": "Settlement hỗ trợ Reconciliation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-021 — ManualAdjustment yêu cầu Approval và Audit

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-10-021",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "00dde5514e5f386950a4881c3e0b2b8da09ee659afb38696197daa549b9bde87"
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
        "BD-10-021-AC001",
        "BD-10-021-AC002",
        "BD-10-021-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-021-O001",
      "obligation_text": "ManualAdjustment yêu cầu Approval và Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-021 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-021 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-021 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-021-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-10-021-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-10-021 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "ManualAdjustment yêu cầu Approval và Audit.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-021",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-021",
    "source_context_sha256": "d6777ecfdb26c6eb50098c6f16bafcb5e3748a557c25c0883adba3fc567d8eb1",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "00dde5514e5f386950a4881c3e0b2b8da09ee659afb38696197daa549b9bde87",
    "source_lines": "L2797-L2911",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-021"
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
  "stable_id": "BD-10-021",
  "title": "ManualAdjustment yêu cầu Approval và Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-022 — Settlement không sửa dữ liệu giao dịch gốc

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
      "requirement_id": "BD-10-022",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "52810a4e31f0e4f333961f20c7cd1d0fea3705ca2af88c6072fadf5a0f167ca7"
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
        "BD-10-022-AC001",
        "BD-10-022-AC002",
        "BD-10-022-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-022-O001",
      "obligation_text": "Settlement không sửa dữ liệu giao dịch gốc"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Settlement không sửa dữ liệu giao dịch gốc.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-022",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-022",
    "source_context_sha256": "9b04a1b0c84f6d4d7d35578e17ba08ce8c8264b9e11a4c321812e29790552719",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "52810a4e31f0e4f333961f20c7cd1d0fea3705ca2af88c6072fadf5a0f167ca7",
    "source_lines": "L2913-L2988",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-022"
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
  "stable_id": "BD-10-022",
  "title": "Settlement không sửa dữ liệu giao dịch gốc",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-023 — Money Flow và Product Flow là hai Business Flow độc lập

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
      "requirement_id": "BD-10-023",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "eabc3fca0826ad89fc6699edcefad0ab0d5779a899a232ab9c35274045fc6e3d"
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
        "BD-10-023-AC001",
        "BD-10-023-AC002",
        "BD-10-023-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-023-O001",
      "obligation_text": "Money Flow và Product Flow là hai Business Flow độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Money Flow và Product Flow là hai Business Flow độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-10-023",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-10-023",
    "source_context_sha256": "03e13923e7dcee54c74b8608b2aa92e3db5d70558facae2176361b797e5ef94d",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "eabc3fca0826ad89fc6699edcefad0ab0d5779a899a232ab9c35274045fc6e3d",
    "source_lines": "L2990-L3065",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-10-023"
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
  "stable_id": "BD-10-023",
  "title": "Money Flow và Product Flow là hai Business Flow độc lập",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-10-R001 — Settlement theo SalesOrderItem sẽ được xem xét ở các phiên bản sau

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-10-R001",
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
  "normative_statement": "Settlement theo SalesOrderItem sẽ được xem xét ở các phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-10-001",
    "previous_temporary_key": "TMP-BRD-WS-10-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Settlement Scope",
    "source_context_sha256": "6e4e2bd143074d6c0afb1136b401fd6e1ace10f08c8580c2cb46b5d05f4b8c5e",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "dd837da59e89fc5e879bc2668cc95f0cda744a84109e71aefad140192708eba4",
    "source_lines": "L3067-L3125",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-10-R001"
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
  "stable_id": "BRD-WS-10-R001",
  "title": "Settlement theo SalesOrderItem sẽ được xem xét ở các phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-10-R002 — Settlement luôn dựa trên Snapshot

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
      "requirement_id": "BRD-WS-10-R002",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "08a4b0a624725a5fe402cdaf46f4359476ec0df95807436aa9c6195ba26dac41"
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
        "BRD-WS-10-R002-AC001",
        "BRD-WS-10-R002-AC002",
        "BRD-WS-10-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-10-R002-O001",
      "obligation_text": "Settlement luôn dựa trên Snapshot"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Settlement luôn dựa trên Snapshot.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-10-002",
    "previous_temporary_key": "TMP-BRD-WS-10-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Settlement Snapshot",
    "source_context_sha256": "6589a361810793b161cfdabd4e380005e158f57bf57c5f320a789d87806440b5",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "08a4b0a624725a5fe402cdaf46f4359476ec0df95807436aa9c6195ba26dac41",
    "source_lines": "L3127-L3202",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-10-R002"
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
  "stable_id": "BRD-WS-10-R002",
  "title": "Settlement luôn dựa trên Snapshot",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-10-R003 — Event Ledger không phải hệ thống kế toán

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
      "requirement_id": "BRD-WS-10-R003",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "6fb2593b7502a26d026518f874c4a5fe4dde80ce16f1e76b603347d744ae6e1c"
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
        "BRD-WS-10-R003-AC001",
        "BRD-WS-10-R003-AC002",
        "BRD-WS-10-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-10-R003-O001",
      "obligation_text": "Event Ledger không phải hệ thống kế toán"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-10-R003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-10-R003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R003 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Event Ledger không phải hệ thống kế toán.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-10-003",
    "previous_temporary_key": "TMP-BRD-WS-10-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Event Ledger",
    "source_context_sha256": "7f58ed52440d636766659dd85d045674132eb94c0363aa3037d326592dc2777a",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "6fb2593b7502a26d026518f874c4a5fe4dde80ce16f1e76b603347d744ae6e1c",
    "source_lines": "L3204-L3312",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-10-R003"
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
  "stable_id": "BRD-WS-10-R003",
  "title": "Event Ledger không phải hệ thống kế toán",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-10-R004 — Rollback luôn sinh FinancialEvent mới

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
      "requirement_id": "BRD-WS-10-R004",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "708cb6cf150654ad0e1992328ec9fbfe140d6486f7a9e977904a95458233911d"
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
        "BRD-WS-10-R004-AC001",
        "BRD-WS-10-R004-AC002",
        "BRD-WS-10-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-10-R004-O001",
      "obligation_text": "Rollback luôn sinh FinancialEvent mới"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-10-R004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-10-R004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Rollback luôn sinh FinancialEvent mới.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-10-004",
    "previous_temporary_key": "TMP-BRD-WS-10-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Refund Settlement",
    "source_context_sha256": "f2373cac4723cf8c780219f06e6223a3863a5f3db3e431fc3dfdac12426ccb95",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "708cb6cf150654ad0e1992328ec9fbfe140d6486f7a9e977904a95458233911d",
    "source_lines": "L3314-L3422",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-10-R004"
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
  "stable_id": "BRD-WS-10-R004",
  "title": "Rollback luôn sinh FinancialEvent mới",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-10-R007 — ManualAdjustment luôn sinh: FinancialEvent

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Rejected adjustment emits no committed-adjustment FinancialEvent"
    ],
    "concrete_bindings": [
      {
        "correlation_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
            "source_type": "SOURCE_LITERAL",
            "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
          },
          "identifier": "BRD-WS-10-R007.CORRELATION_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.CORRELATION_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-10.md",
            "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
            "source_lines": "L562-L564",
            "source_section": "27. Manual Adjustment"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CORRELATION_ID",
            "resolver_id": "RESOLVE.BRD-WS-10-R007.BRD-WS-10-R007.CORRELATION_ID",
            "version": "1.0.0"
          },
          "semantic_type": "CORRELATION_ID"
        },
        "event_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
            "source_type": "SOURCE_LITERAL",
            "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
          },
          "identifier": "BRD-WS-10-R007.EVENT_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.EVENT_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-10.md",
            "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
            "source_lines": "L562-L564",
            "source_section": "27. Manual Adjustment"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVENT_TYPE_ID",
            "resolver_id": "RESOLVE.BRD-WS-10-R007.BRD-WS-10-R007.EVENT_ID",
            "version": "1.0.0"
          },
          "semantic_type": "EVENT_TYPE_ID"
        },
        "trigger": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
            "source_type": "SOURCE_LITERAL",
            "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
          },
          "identifier": "BRD-WS-10-R007.TRIGGER",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.TRIGGER.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-10.md",
            "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
            "source_lines": "L562-L564",
            "source_section": "27. Manual Adjustment"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.BRD-WS-10-R007.BRD-WS-10-R007.TRIGGER",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-10-R007",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "The FinancialEvent is suppressed or duplicated"
    ],
    "operator_composition": [
      "EVENT_EMITTED"
    ],
    "positive_oracle": [
      "Exactly one FinancialEvent is emitted for the ManualAdjustment"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
      "source_lines": "L562-L564",
      "source_section": "27. Manual Adjustment"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
          "source_type": "SOURCE_LITERAL",
          "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
        },
        "identifier": "BRD-WS-10-R007.BRD-WS-10-R007.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-10-R007.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-10.md",
          "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
          "source_lines": "L562-L564",
          "source_section": "27. Manual Adjustment"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-10-R007.BRD-WS-10-R007.BRD-WS-10-R007.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-10-R007.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.MANUAL_ADJUSTMENT_ID",
        "FIELD.FINANCIAL_EVENT_ID",
        "FIELD.EVENT_COUNT",
        "FIELD.CORRELATION_ID",
        "FIELD.COMMIT_TIME",
        "FIELD.EVENT_TIME"
      ],
      "producer": "BRD-WS-10-R007.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-10-R007.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.MANUAL_ADJUSTMENT_ID",
        "FIELD.FINANCIAL_EVENT_ID",
        "FIELD.EVENT_COUNT",
        "FIELD.CORRELATION_ID",
        "FIELD.COMMIT_TIME",
        "FIELD.EVENT_TIME"
      ],
      "required_values_or_hashes": [
        "BRD-WS-10-R007.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-10-R007.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-10-R007.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-10-R007-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED",
          "evaluator_consumed_bindings": [
            "correlation_id",
            "event_id",
            "trigger"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
              "source_type": "SOURCE_LITERAL",
              "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
            },
            "identifier": "BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-10.md",
              "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
              "source_lines": "L562-L564",
              "source_section": "27. Manual Adjustment"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-10-R007.BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
              "source_type": "SOURCE_LITERAL",
              "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
            },
            "identifier": "BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-10.md",
              "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
              "source_lines": "L562-L564",
              "source_section": "27. Manual Adjustment"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVENT_TYPE_ID",
              "resolver_id": "RESOLVE.BRD-WS-10-R007.BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "EVENT_TYPE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "correlation_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
                },
                "identifier": "BRD-WS-10-R007.CORRELATION_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.CORRELATION_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-10.md",
                  "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
                  "source_lines": "L562-L564",
                  "source_section": "27. Manual Adjustment"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CORRELATION_ID",
                  "resolver_id": "RESOLVE.BRD-WS-10-R007.BRD-WS-10-R007.CORRELATION_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "CORRELATION_ID"
              },
              "event_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
                },
                "identifier": "BRD-WS-10-R007.EVENT_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.EVENT_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-10.md",
                  "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
                  "source_lines": "L562-L564",
                  "source_section": "27. Manual Adjustment"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVENT_TYPE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-10-R007.BRD-WS-10-R007.EVENT_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "EVENT_TYPE_ID"
              },
              "trigger": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
                },
                "identifier": "BRD-WS-10-R007.TRIGGER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.TRIGGER.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-10.md",
                  "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
                  "source_lines": "L562-L564",
                  "source_section": "27. Manual Adjustment"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BRD-WS-10-R007.BRD-WS-10-R007.TRIGGER",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
                },
                "identifier": "BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-10.md",
                  "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
                  "source_lines": "L562-L564",
                  "source_section": "27. Manual Adjustment"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVENT_TYPE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-10-R007.BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "EVENT_TYPE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
                  "source_type": "SOURCE_LITERAL",
                  "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
                },
                "identifier": "BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-10.md",
                  "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
                  "source_lines": "L562-L564",
                  "source_section": "27. Manual Adjustment"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVENT_TYPE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-10-R007.BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "EVENT_TYPE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
                "source_type": "SOURCE_LITERAL",
                "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
              },
              "identifier": "BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-10.md",
                "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
                "source_lines": "L562-L564",
                "source_section": "27. Manual Adjustment"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-10-R007.BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "EVENT_EMITTED"
          },
          "obligation_id": "BRD-WS-10-R007-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
              "source_type": "SOURCE_LITERAL",
              "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
            },
            "identifier": "BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-10.md",
              "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
              "source_lines": "L562-L564",
              "source_section": "27. Manual Adjustment"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVENT_TYPE_ID",
              "resolver_id": "OBSERVE.BRD-WS-10-R007.BRD-WS-10-R007.BRD-WS-10-R007.O1.1.EVENT_EMITTED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "EVENT_TYPE_ID"
          },
          "operator_id": "EVENT_EMITTED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "correlation_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
                "source_type": "SOURCE_LITERAL",
                "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
              },
              "identifier": "BRD-WS-10-R007.CORRELATION_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.CORRELATION_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-10.md",
                "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
                "source_lines": "L562-L564",
                "source_section": "27. Manual Adjustment"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CORRELATION_ID",
                "resolver_id": "RESOLVE.BRD-WS-10-R007.BRD-WS-10-R007.CORRELATION_ID",
                "version": "1.0.0"
              },
              "semantic_type": "CORRELATION_ID"
            },
            "event_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
                "source_type": "SOURCE_LITERAL",
                "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
              },
              "identifier": "BRD-WS-10-R007.EVENT_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.EVENT_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-10.md",
                "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
                "source_lines": "L562-L564",
                "source_section": "27. Manual Adjustment"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVENT_TYPE_ID",
                "resolver_id": "RESOLVE.BRD-WS-10-R007.BRD-WS-10-R007.EVENT_ID",
                "version": "1.0.0"
              },
              "semantic_type": "EVENT_TYPE_ID"
            },
            "trigger": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
                "source_type": "SOURCE_LITERAL",
                "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
              },
              "identifier": "BRD-WS-10-R007.TRIGGER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-10-R007.O1.1.EVENT_EMITTED.TRIGGER.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-10.md",
                "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
                "source_lines": "L562-L564",
                "source_section": "27. Manual Adjustment"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.BRD-WS-10-R007.BRD-WS-10-R007.TRIGGER",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "Rejected adjustment emits no committed-adjustment FinancialEvent"
      ],
      "contract_ast_sha256": "01323968d40d1e3a9d2406aa63325abe2fac888310b3d542a50ad0f437015b3b",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-10-R007",
      "criticality": "CRITICAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-10.md#27. Manual Adjustment",
            "source_type": "SOURCE_LITERAL",
            "version": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed"
          },
          "identifier": "BRD-WS-10-R007.BRD-WS-10-R007.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-10-R007.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-10.md",
            "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
            "source_lines": "L562-L564",
            "source_section": "27. Manual Adjustment"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-10-R007.BRD-WS-10-R007.BRD-WS-10-R007.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-10-R007.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.MANUAL_ADJUSTMENT_ID",
          "FIELD.FINANCIAL_EVENT_ID",
          "FIELD.EVENT_COUNT",
          "FIELD.CORRELATION_ID",
          "FIELD.COMMIT_TIME",
          "FIELD.EVENT_TIME"
        ],
        "producer": "BRD-WS-10-R007.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-10-R007.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.MANUAL_ADJUSTMENT_ID",
          "FIELD.FINANCIAL_EVENT_ID",
          "FIELD.EVENT_COUNT",
          "FIELD.CORRELATION_ID",
          "FIELD.COMMIT_TIME",
          "FIELD.EVENT_TIME"
        ],
        "required_values_or_hashes": [
          "BRD-WS-10-R007.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-10-R007.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-10-R007.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-1F662F0EB1D9FB63ADE9",
        "P2C-C4-FX-C505E4288B8AD85BDD6B",
        "P2C-C4-FX-FA2BB234AE4C982DEB18"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "The FinancialEvent is suppressed or duplicated"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-10-R007-O001",
          "obligation_text": "ManualAdjustment luôn sinh: FinancialEvent"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-10-R007.O1.1.EVENT_EMITTED"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-10-R007-O001"
        }
      ],
      "operator_composition": [
        "EVENT_EMITTED"
      ],
      "positive_oracles": [
        "Exactly one FinancialEvent is emitted for the ManualAdjustment"
      ],
      "preconditions": [
        "The adjustment identity and correlation context exist"
      ],
      "prohibitions": [
        "The FinancialEvent is suppressed or duplicated"
      ],
      "requirement_id": "BRD-WS-10-R007",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-10.md",
        "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
        "source_lines": "L562-L564",
        "source_section": "27. Manual Adjustment"
      },
      "source_statement": "ManualAdjustment luôn sinh: FinancialEvent.",
      "surrounding_source_context": "### BRD-WS-10-R007 — ManualAdjustment luôn sinh: FinancialEvent"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-10-R007",
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
        "BRD-WS-10-R007-AC001",
        "BRD-WS-10-R007-AC002",
        "BRD-WS-10-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-10-R007-O001",
      "obligation_text": "ManualAdjustment luôn sinh: FinancialEvent"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-10-R007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-10-R007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-10-R007 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "ManualAdjustment luôn sinh: FinancialEvent.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-10-007",
    "previous_temporary_key": "TMP-BRD-WS-10-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Manual Adjustment",
    "source_context_sha256": "964fb40e3cb66358a9f58f87a28142b3134181c02086fe7281f908c2be5fb65f",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "1fe18692979f3eb5dee187e2fa0b8edfcc2bc18e6cae16028ecf919a3b665fed",
    "source_lines": "L3424-L4278",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-10-R007"
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
  "stable_id": "BRD-WS-10-R007",
  "title": "ManualAdjustment luôn sinh: FinancialEvent",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-10-001 — Financial Domain chỉ đọc Snapshot, không sửa Transaction

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
      "requirement_id": "EP-10-001",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "067a060ea32799962d39cacdbd792fa297019e5f840e35cf6f6613412fe35a9e"
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
        "EP-10-001-AC001",
        "EP-10-001-AC002",
        "EP-10-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-10-001-O001",
      "obligation_text": "Financial Domain chỉ đọc Snapshot, không sửa Transaction"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-001 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-10-001-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-10-001-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-001 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Financial Domain chỉ đọc Snapshot, không sửa Transaction.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-10-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-10-001",
    "source_context_sha256": "30634a2697075a8f1ca3d6b5b656e2ebb6ad25231d8e242219c9c90f84a8b515",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "067a060ea32799962d39cacdbd792fa297019e5f840e35cf6f6613412fe35a9e",
    "source_lines": "L4280-L4388",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-10-001"
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
  "stable_id": "EP-10-001",
  "title": "Financial Domain chỉ đọc Snapshot, không sửa Transaction",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-10-002 — Mọi điều chỉnh tài chính đều được biểu diễn bằng FinancialEvent mới

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
      "requirement_id": "EP-10-002",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "1ed9bab70ef6a92ba502b10eb1b43bffceef89da09675590057f7ea3f51b0c35"
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
        "EP-10-002-AC001",
        "EP-10-002-AC002",
        "EP-10-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-10-002-O001",
      "obligation_text": "Mọi điều chỉnh tài chính đều được biểu diễn bằng FinancialEvent mới"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-002 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-10-002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-10-002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-002 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi điều chỉnh tài chính đều được biểu diễn bằng FinancialEvent mới.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-10-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-10-002",
    "source_context_sha256": "f9ca36def95b0f3779394e0dea331e10d4ffa899319582dfe204e06424a1c825",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "1ed9bab70ef6a92ba502b10eb1b43bffceef89da09675590057f7ea3f51b0c35",
    "source_lines": "L4390-L4498",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-10-002"
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
  "stable_id": "EP-10-002",
  "title": "Mọi điều chỉnh tài chính đều được biểu diễn bằng FinancialEvent mới",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-10-003 — Financial Visibility tuân thủ Distribution Hierarchy

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
      "requirement_id": "EP-10-003",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "6f1827493478a23721174a01f6c4913fe4d3a6ad7cd4cf4a5d0fc1b000f567fd"
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
        "EP-10-003-AC001",
        "EP-10-003-AC002",
        "EP-10-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-10-003-O001",
      "obligation_text": "Financial Visibility tuân thủ Distribution Hierarchy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-10-003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-10-003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-003 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Financial Visibility tuân thủ Distribution Hierarchy.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-10-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-10-003",
    "source_context_sha256": "f0b74be6baaf961b16a04db7332e48ad45bf5a4d80c22e9ada5ed03c71735347",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "6f1827493478a23721174a01f6c4913fe4d3a6ad7cd4cf4a5d0fc1b000f567fd",
    "source_lines": "L4500-L4608",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-10-003"
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
  "stable_id": "EP-10-003",
  "title": "Financial Visibility tuân thủ Distribution Hierarchy",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-10-004 — Settlement và Reconciliation là hai Capability độc lập

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
      "requirement_id": "EP-10-004",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "9e22d2f7d6aa40ef1e16cefb4e6b7fcb6a43871b7e8389ead13aa9ad3be458be"
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
        "EP-10-004-AC001",
        "EP-10-004-AC002",
        "EP-10-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-10-004-O001",
      "obligation_text": "Settlement và Reconciliation là hai Capability độc lập"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-10-004-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-10-004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-10-004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Settlement và Reconciliation là hai Capability độc lập.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-10-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-10-004",
    "source_context_sha256": "9ea68cc6fc060eb5bb15418cc2ae0e37afe35d629e51b6a8cdd0664454df00d7",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "9e22d2f7d6aa40ef1e16cefb4e6b7fcb6a43871b7e8389ead13aa9ad3be458be",
    "source_lines": "L4610-L4724",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-10-004"
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
  "stable_id": "EP-10-004",
  "title": "Settlement và Reconciliation là hai Capability độc lập",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-10-005 — Event Ledger là nguồn dữ liệu chuẩn cho Reporting và Financial Export

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
      "requirement_id": "EP-10-005",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "342564e39575fa542acf1bd2da6d65db304d2a1563011b71b5feabd66b78f37b"
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
        "EP-10-005-AC001",
        "EP-10-005-AC002",
        "EP-10-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-10-005-O001",
      "obligation_text": "Event Ledger là nguồn dữ liệu chuẩn cho Reporting và Financial Export"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-10-005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-10-005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-10-005 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Event Ledger là nguồn dữ liệu chuẩn cho Reporting và Financial Export.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-10-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-10-005",
    "source_context_sha256": "797d46369459ea89d131a6565d0a326b98cfab101322cb35189ab535cf2175f1",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "342564e39575fa542acf1bd2da6d65db304d2a1563011b71b5feabd66b78f37b",
    "source_lines": "L4726-L4834",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-10-005"
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
  "stable_id": "EP-10-005",
  "title": "Event Ledger là nguồn dữ liệu chuẩn cho Reporting và Financial Export",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-10-006 — Money Flow độc lập với Product Flow

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
      "requirement_id": "EP-10-006",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "source_fingerprint": "e8ad3c81f3c3df889d10853f6ba8cb110e6316d4971c8e1c2096ee6dcc43bbfc"
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
        "EP-10-006-AC001",
        "EP-10-006-AC002",
        "EP-10-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-10-006-O001",
      "obligation_text": "Money Flow độc lập với Product Flow"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Money Flow độc lập với Product Flow.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-10-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "29. Money Flow ≠ Product Flow",
    "source_context_sha256": "0574cced1eedbfc1e397d1c8087c357fcd097692c5e216087802f442853b4bf3",
    "source_document": "docs/BRD/BRD-WS-10.md",
    "source_fingerprint": "e8ad3c81f3c3df889d10853f6ba8cb110e6316d4971c8e1c2096ee6dcc43bbfc",
    "source_lines": "L4836-L4911",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-10-006"
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
  "stable_id": "EP-10-006",
  "title": "Money Flow độc lập với Product Flow",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
