---
document_code: "BRD-WS-10"
title: "Settlement, Revenue Sharing & Financial Lifecycle"
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

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-10-001 — Settlement thực hiện theo SalesOrder

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-001-AC001",
      "given": "the applicable business context, actor, and input for Settlement thực hiện theo SalesOrder",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-10-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Settlement thực hiện theo SalesOrder",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-10-001-O001"
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
        "BD-10-001-AC001",
        "BD-10-001-AC002"
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
    "source_fingerprint": "c75e77d3da8df3db779e985438aebad0ab9d67cf210ab6484622a2304cec9abd",
    "source_lines": "L645-L648",
    "source_section": "30. Business Decisions (Locked) > BD-10-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-002-AC001",
      "given": "the applicable business context, actor, and input for Settlement hỗ trợ chu kỳ cố định hoặc khoảng thời gian tùy chỉnh (≤ 03 tháng)",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-002-O001"
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
        "BD-10-002-AC001"
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
    "source_fingerprint": "e2a4d5545d7bcd548c5fbed08d063004704b3d8cb2f68b30c69d81627cf9384a",
    "source_lines": "L651-L654",
    "source_section": "30. Business Decisions (Locked) > BD-10-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-003-AC001",
      "given": "the applicable business context, actor, and input for Mọi Transaction đều sinh FinancialEvent",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-10-003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Mọi Transaction đều sinh FinancialEvent",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-10-003-O001"
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
        "BD-10-003-AC001",
        "BD-10-003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-003-O001",
      "obligation_text": "Mọi Transaction đều sinh FinancialEvent"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-10-003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-10-003 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-10-003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "e250a795ac70e0361be91e83b8b4041d147d8967db6e0049d1c91ad456d0c702",
    "source_lines": "L657-L660",
    "source_section": "30. Business Decisions (Locked) > BD-10-003"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-10-004-AC001",
      "given": "a candidate CommissionSnapshot phát sinh sau Payment Success và ở trạng thái Pending cho đến khi Settlement … record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-10-004-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-10-004-AC002",
      "given": "a CommissionSnapshot phát sinh sau Payment Success và ở trạng thái Pending cho đến khi Settlement … candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-10-004-O001"
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
        "BD-10-004-AC001",
        "BD-10-004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-004-O001",
      "obligation_text": "CommissionSnapshot phát sinh sau Payment Success và ở trạng thái Pending cho đến khi Settlement xác nhận"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-10-004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-10-004 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-10-004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "6a50fb8fe3668c2638571610a7740b0d6cb316e793d7653efc95ecb40a0fd1bf",
    "source_lines": "L663-L666",
    "source_section": "30. Business Decisions (Locked) > BD-10-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-005-AC001",
      "given": "the applicable business context, actor, and input for Revenue Sharing tính theo Bottom-Up Distribution",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-005-O001"
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
        "BD-10-005-AC001"
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
    "source_fingerprint": "80f684f2a46d220ffb8c4d310d0ffba0e9b7a34f7d946087683b034d8c6b1a78",
    "source_lines": "L669-L672",
    "source_section": "30. Business Decisions (Locked) > BD-10-005"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-10-006-AC001",
      "given": "a candidate RevenueRecipient là Business Object record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-10-006-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-10-006-AC001"
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
    "source_fingerprint": "fa8416806d499d87161e71ff8cf5536e8865a0dc272e9c7cd3e897b787904135",
    "source_lines": "L675-L678",
    "source_section": "30. Business Decisions (Locked) > BD-10-006"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-10-007-AC001",
      "given": "a candidate SettlementSnapshot lưu đầy đủ Multi-level Cost và Multi-level Price record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-10-007-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-10-007-AC001"
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
    "source_fingerprint": "5548054fa4c6319bf47dc8db85fbca2dae74867178f333e490e226fe558677a1",
    "source_lines": "L681-L684",
    "source_section": "30. Business Decisions (Locked) > BD-10-007"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-008-AC001",
      "given": "the applicable business context, actor, and input for YSim sử dụng Event Ledger",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-008-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-10-008-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by YSim sử dụng Event Ledger",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-10-008-O001"
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
        "BD-10-008-AC001",
        "BD-10-008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-008-O001",
      "obligation_text": "YSim sử dụng Event Ledger"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-10-008 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-10-008 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-008-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-10-008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "83e65c1ed783297eb1a188df179b319203b9b9ef281a72879ce664d596fdffd2",
    "source_lines": "L687-L690",
    "source_section": "30. Business Decisions (Locked) > BD-10-008"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-10-009-AC001",
      "given": "a candidate FinancialAccount là Business Object độc lập record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-10-009-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-10-009-AC002",
      "given": "a FinancialAccount là Business Object độc lập candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-10-009-O001"
      ],
      "when": "the candidate is validated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-10-009-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by FinancialAccount là Business Object độc lập",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-10-009-O001"
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
      "criterion_references": [],
      "rationale": "BD-10-009 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-009 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-009 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-10-009-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-009-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-10-009 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "39168c7505b700169dfe828784eb4431a2824a2904f0c3084c05c9736c7f018e",
    "source_lines": "L693-L696",
    "source_section": "30. Business Decisions (Locked) > BD-10-009"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-010-AC001",
      "given": "the applicable business context, actor, and input for Wallet hỗ trợ Organization và Collaborator",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-010-O001"
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
        "BD-10-010-AC001"
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
    "source_fingerprint": "71cea7a3cf90fe5d24af59b305e764f041c4c826b8e53ff1c15a3b73e6b761a1",
    "source_lines": "L699-L702",
    "source_section": "30. Business Decisions (Locked) > BD-10-010"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-011-AC001",
      "given": "the applicable business context, actor, and input for Supplier Settlement thuộc Financial Domain",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-10-011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Supplier Settlement thuộc Financial Domain",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-10-011-O001"
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
        "BD-10-011-AC001",
        "BD-10-011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-011-O001",
      "obligation_text": "Supplier Settlement thuộc Financial Domain"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-10-011 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-011 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-011 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-10-011 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-011-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-10-011 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "70bf02e119a38229db461aef71a8e478b86b92189998493c28b92096b3501149",
    "source_lines": "L705-L708",
    "source_section": "30. Business Decisions (Locked) > BD-10-011"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-012-AC001",
      "given": "the applicable business context, actor, and input for Settlement sử dụng Settlement Currency theo Commercial Agreement",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-012-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-10-012-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Settlement sử dụng Settlement Currency theo Commercial Agreement",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-10-012-O001"
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
        "BD-10-012-AC001",
        "BD-10-012-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-012-O001",
      "obligation_text": "Settlement sử dụng Settlement Currency theo Commercial Agreement"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-10-012 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-012 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-012 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-10-012 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-012-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-10-012 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "398ae82c321b590bab3f8e5bb0e7ba8472b307f28bd14601e53ae2ff30a143fa",
    "source_lines": "L711-L714",
    "source_section": "30. Business Decisions (Locked) > BD-10-012"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-013-AC001",
      "given": "the applicable business context, actor, and input for Financial Domain hỗ trợ FX Gain/Loss",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-013-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-10-013-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Financial Domain hỗ trợ FX Gain/Loss",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-10-013-O001"
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
        "BD-10-013-AC001",
        "BD-10-013-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-013-O001",
      "obligation_text": "Financial Domain hỗ trợ FX Gain/Loss"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-10-013 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-013 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-013 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-10-013 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-013-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-10-013 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "9e57fb2978a07e5f6a53bd189bc0daa19cad5cf9ea7b22db2ecb18eb2cb744b2",
    "source_lines": "L717-L720",
    "source_section": "30. Business Decisions (Locked) > BD-10-013"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-014-AC001",
      "given": "the applicable business context, actor, and input for Refund thực hiện Rollback Settlement",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-10-014-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Refund thực hiện Rollback Settlement",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-10-014-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "RECOVERY",
      "controlled_contract": "EXPLICIT_RECOVERY_CONTRACT_V1",
      "criterion_id": "BD-10-014-AC003",
      "given": "a failed or interrupted case for which Refund thực hiện Rollback Settlement explicitly defines recovery, restore, rollback, or fallback behavior",
      "observable_evidence": "pre-failure state, recovery action, resulting state, outcome, and recovery evidence named by the obligation",
      "then": "the resulting state and outcome follow the requirement-specific recovery obligation and expose whether recovery completed or failed",
      "verifies": [
        "BD-10-014-O001"
      ],
      "when": "the declared recovery path is invoked"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
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
      "criterion_references": [],
      "rationale": "BD-10-014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-10-014 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-014-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [
        "BD-10-014-AC003"
      ],
      "status": "APPLICABLE"
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
    "source_fingerprint": "9826de69db809dceec60e3ae8b568eb9b972f2939a5dbe269a9bb0f83a1549b4",
    "source_lines": "L723-L726",
    "source_section": "30. Business Decisions (Locked) > BD-10-014"
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
    "source_fingerprint": "60df769f0c3d9f4b31ec5316612c16031af495a44ec6e1f2a8c8807268ef9a42",
    "source_lines": "L729-L732",
    "source_section": "30. Business Decisions (Locked) > BD-10-015"
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
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
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
    "source_fingerprint": "5f5ab4824902b692486742f5e1f536ac378443252785b2786c6cd98f2b2546ec",
    "source_lines": "L735-L738",
    "source_section": "30. Business Decisions (Locked) > BD-10-016"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-017-AC001",
      "given": "the applicable business context, actor, and input for SettlementBatch yêu cầu Approval",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BD-10-017-O001"
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
        "BD-10-017-AC001"
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
    "source_fingerprint": "191b1fb1a1cd18b324fc15d8f09cda209762503ed9a6ebe385902db5cc770b61",
    "source_lines": "L741-L744",
    "source_section": "30. Business Decisions (Locked) > BD-10-017"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-10-018-AC001",
      "given": "a contract interaction at the integration boundary defined by FinancialExport hỗ trợ Excel, CSV và REST API",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-10-018-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-10-018-AC002",
      "given": "an interaction that violates the contract or ownership boundary for FinancialExport hỗ trợ Excel, CSV và REST API",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-10-018-O001"
      ],
      "when": "the interaction reaches the integration boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-10-018-AC001",
        "BD-10-018-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-018-O001",
      "obligation_text": "FinancialExport hỗ trợ Excel, CSV và REST API"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-10-018 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-018 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-018 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-10-018 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-018-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-10-018 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "7dcc0bf7b23112eb7b34b90e616e403198840bd83b1d10681ff8006bbe806f78",
    "source_lines": "L747-L750",
    "source_section": "30. Business Decisions (Locked) > BD-10-018"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-10-019-AC001",
      "given": "a candidate FinancialSnapshot là đầu vào duy nhất của Settlement record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-10-019-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-10-019-AC002",
      "given": "a FinancialSnapshot là đầu vào duy nhất của Settlement candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-10-019-O001"
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
        "BD-10-019-AC001",
        "BD-10-019-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-019-O001",
      "obligation_text": "FinancialSnapshot là đầu vào duy nhất của Settlement"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-10-019 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-019 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-019 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-10-019 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-019-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-10-019 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "8bce1713451bff6983f45794c3cceebad85720cda6556925d6a955d3bbb17c94",
    "source_lines": "L753-L756",
    "source_section": "30. Business Decisions (Locked) > BD-10-019"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-020-AC001",
      "given": "the applicable business context, actor, and input for Settlement hỗ trợ Reconciliation",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-020-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-10-020-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Settlement hỗ trợ Reconciliation",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-10-020-O001"
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
        "BD-10-020-AC001",
        "BD-10-020-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-10-020-O001",
      "obligation_text": "Settlement hỗ trợ Reconciliation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-10-020 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-020 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-020 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-10-020 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-020-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-10-020 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "c4ff1d02348355c58d0f5f3ff29633ae36edb50f6eec2e429e9ad42c70602629",
    "source_lines": "L759-L762",
    "source_section": "30. Business Decisions (Locked) > BD-10-020"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-021-AC001",
      "given": "an operational task within the scope of ManualAdjustment yêu cầu Approval và Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-10-021-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-10-021-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for ManualAdjustment yêu cầu Approval và Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-10-021-O001"
      ],
      "when": "operational verification is performed"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-10-021-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by ManualAdjustment yêu cầu Approval và Audit",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-10-021-O001"
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
      "criterion_references": [],
      "rationale": "BD-10-021 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-10-021 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-10-021 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-10-021-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-10-021-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-10-021 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "0c9e5474fdd1807651673c0ab8b16581413d31c167d70e53a0456b9daea66fae",
    "source_lines": "L765-L768",
    "source_section": "30. Business Decisions (Locked) > BD-10-021"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-022-AC001",
      "given": "the applicable business context, actor, and input for Settlement không sửa dữ liệu giao dịch gốc",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-10-022-O001"
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
        "BD-10-022-AC001"
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
    "source_fingerprint": "6b43d5655323da243b9003da2412ee5fb48ffca4b4d5345c9167f46987772fc2",
    "source_lines": "L771-L774",
    "source_section": "30. Business Decisions (Locked) > BD-10-022"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-10-023-AC001",
      "given": "the applicable business context, actor, and input for Money Flow và Product Flow là hai Business Flow độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-10-023-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-10-023-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Money Flow và Product Flow là hai Business Flow độc lập",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-10-023-O001"
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
        "BD-10-023-AC001",
        "BD-10-023-AC002"
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
    "source_fingerprint": "b956002dab1af5979816d99c757d81c030c98cf2759a15e546921852fd7e0a9c",
    "source_lines": "L777-L780",
    "source_section": "30. Business Decisions (Locked) > BD-10-023"
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
    "source_lines": "L183",
    "source_section": "7. Settlement Scope"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-10-R002-AC001",
      "given": "a candidate Settlement luôn dựa trên Snapshot record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-10-R002-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-10-R002-AC001"
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
    "source_lines": "L288",
    "source_section": "11. Settlement Snapshot"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-10-R003-AC001",
      "given": "the applicable business context, actor, and input for Event Ledger không phải hệ thống kế toán",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-10-R003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-10-R003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Event Ledger không phải hệ thống kế toán",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-10-R003-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-10-R003-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Event Ledger không phải hệ thống kế toán",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-10-R003-O001"
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
      "criterion_references": [],
      "rationale": "BRD-WS-10-R003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-10-R003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-10-R003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-10-R003-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-10-R003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-10-R003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L298",
    "source_section": "12. Event Ledger"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-10-R004-AC001",
      "given": "the applicable business context, actor, and input for Rollback luôn sinh FinancialEvent mới",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-10-R004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-10-R004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Rollback luôn sinh FinancialEvent mới",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-10-R004-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "RECOVERY",
      "controlled_contract": "EXPLICIT_RECOVERY_CONTRACT_V1",
      "criterion_id": "BRD-WS-10-R004-AC003",
      "given": "a failed or interrupted case for which Rollback luôn sinh FinancialEvent mới explicitly defines recovery, restore, rollback, or fallback behavior",
      "observable_evidence": "pre-failure state, recovery action, resulting state, outcome, and recovery evidence named by the obligation",
      "then": "the resulting state and outcome follow the requirement-specific recovery obligation and expose whether recovery completed or failed",
      "verifies": [
        "BRD-WS-10-R004-O001"
      ],
      "when": "the declared recovery path is invoked"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
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
      "criterion_references": [],
      "rationale": "BRD-WS-10-R004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-10-R004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-10-R004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-10-R004 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-10-R004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [
        "BRD-WS-10-R004-AC003"
      ],
      "status": "APPLICABLE"
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
    "source_lines": "L394",
    "source_section": "18. Refund Settlement"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-10-R007-AC001",
      "given": "the applicable business context, actor, and input for ManualAdjustment luôn sinh: FinancialEvent",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-10-R007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-10-R007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by ManualAdjustment luôn sinh: FinancialEvent",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-10-R007-O001"
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
        "BRD-WS-10-R007-AC001",
        "BRD-WS-10-R007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-10-R007-O001",
      "obligation_text": "ManualAdjustment luôn sinh: FinancialEvent"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-10-R007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-10-R007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-10-R007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-10-R007 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-10-R007-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-10-R007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L562-L564",
    "source_section": "27. Manual Adjustment"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "EP-10-001-AC001",
      "given": "a candidate Financial Domain chỉ đọc Snapshot, không sửa Transaction record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "EP-10-001-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-10-001-AC002",
      "given": "a Financial Domain chỉ đọc Snapshot, không sửa Transaction candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "EP-10-001-O001"
      ],
      "when": "the candidate is validated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-10-001-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Financial Domain chỉ đọc Snapshot, không sửa Transaction",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-10-001-O001"
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
      "criterion_references": [],
      "rationale": "EP-10-001 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-10-001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-10-001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-10-001-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-10-001-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-10-001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "8c58cdb30e5780f7c8a05c5dcdf89ac5c9b8937348e2ba37c60008fc582059c1",
    "source_lines": "L785-L788",
    "source_section": "31. Enterprise Design Principles > EP-10-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-10-002-AC001",
      "given": "the applicable business context, actor, and input for Mọi điều chỉnh tài chính đều được biểu diễn bằng FinancialEvent mới",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-10-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-10-002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Mọi điều chỉnh tài chính đều được biểu diễn bằng FinancialEvent mới",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-10-002-O001"
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
        "EP-10-002-AC001",
        "EP-10-002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-10-002-O001",
      "obligation_text": "Mọi điều chỉnh tài chính đều được biểu diễn bằng FinancialEvent mới"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-10-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-10-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-10-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-10-002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-10-002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-10-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "e25ee4aee100a5e428f7c8bec1ddb2d310579ee861f1c5beafd7128dbbbd6ba3",
    "source_lines": "L791-L794",
    "source_section": "31. Enterprise Design Principles > EP-10-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-10-003-AC001",
      "given": "the applicable business context, actor, and input for Financial Visibility tuân thủ Distribution Hierarchy",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-10-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-10-003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Financial Visibility tuân thủ Distribution Hierarchy",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-10-003-O001"
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
        "EP-10-003-AC001",
        "EP-10-003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-10-003-O001",
      "obligation_text": "Financial Visibility tuân thủ Distribution Hierarchy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-10-003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-10-003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-10-003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-10-003 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-10-003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-10-003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "0111c71d770c98646893b142e8e9b85c4c50380d40d5b345335bae2530eb631f",
    "source_lines": "L797-L800",
    "source_section": "31. Enterprise Design Principles > EP-10-003"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-10-004-AC001",
      "given": "the applicable business context, actor, and input for Settlement và Reconciliation là hai Capability độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "EP-10-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-10-004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Settlement và Reconciliation là hai Capability độc lập",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-10-004-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-10-004-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Settlement và Reconciliation là hai Capability độc lập",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-10-004-O001"
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
      "criterion_references": [],
      "rationale": "EP-10-004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-10-004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-10-004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-10-004-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-10-004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-10-004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "772e598c5f08b9c024ab96a66e3630865d7463ffb3b5a6d2c5f3a960c5ae1ade",
    "source_lines": "L803-L806",
    "source_section": "31. Enterprise Design Principles > EP-10-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-10-005-AC001",
      "given": "the applicable business context, actor, and input for Event Ledger là nguồn dữ liệu chuẩn cho Reporting và Financial Export",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-10-005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-10-005-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Event Ledger là nguồn dữ liệu chuẩn cho Reporting và Financial Export",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-10-005-O001"
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
        "EP-10-005-AC001",
        "EP-10-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-10-005-O001",
      "obligation_text": "Event Ledger là nguồn dữ liệu chuẩn cho Reporting và Financial Export"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-10-005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-10-005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-10-005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-10-005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-10-005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-10-005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "d57bcb680849e8536bbcd2f6bbd63f36dcb9e9c3ecf7ed19f5c5d2b2a1cde6b3",
    "source_lines": "L809-L812",
    "source_section": "31. Enterprise Design Principles > EP-10-005"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-10-006-AC001",
      "given": "the applicable business context, actor, and input for Money Flow độc lập với Product Flow",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "EP-10-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-10-006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Money Flow độc lập với Product Flow",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-10-006-O001"
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
        "EP-10-006-AC001",
        "EP-10-006-AC002"
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
    "source_fingerprint": "dd34b5c3c377f650d0899c6ca9cd0b8743d1b648383840994e743acf352aaeb0",
    "source_lines": "L815-L818",
    "source_section": "31. Enterprise Design Principles > EP-10-006"
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
