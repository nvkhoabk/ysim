---
document_code: BRD-WS-10
document_name: Settlement, Revenue Sharing & Financial Lifecycle
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-10
---

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