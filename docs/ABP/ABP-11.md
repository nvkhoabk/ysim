---
document_code: ABP-11
document_name: Platform Data Architecture
project: YSim v2.0
document_set: Architecture Baseline Pack
version: 1.0
status: FROZEN
language: en-US
---

# Platform Data Architecture

## ABP-11

---

# 1. Purpose

Platform Data Architecture định nghĩa kiến trúc quản lý dữ liệu của nền tảng YSim.

Tài liệu này chuẩn hóa:

- Data Ownership
- Data Classification
- Data Lifecycle
- Data Categories
- Data Consistency
- Data Governance
- Data Traceability
- Data Security
- Data Usage

Đây là nền tảng cho mọi thiết kế Domain Model, Database Design, Reporting và Analytics.

---

# 2. Data Principles

YSim áp dụng các nguyên tắc:

- Business Owns Data
- One Source of Truth
- Data by Contract
- Data Classification
- Immutable Evidence
- Data Lineage
- Policy Driven
- Privacy by Design
- Event Driven

Platform Data không phụ thuộc Database Technology.

---

# 3. Platform Data Categories

Platform chuẩn hóa các nhóm dữ liệu.

| Category | Description |
|----------|-------------|
| Runtime Data | Dữ liệu đang vận hành |
| Master Data | Dữ liệu lõi nghiệp vụ |
| Reference Data | Dữ liệu tham chiếu |
| Configuration Data | Dữ liệu cấu hình |
| Metadata | Mô tả cấu trúc và hành vi |
| Business Snapshot | Bằng chứng nghiệp vụ |
| Audit Data | Nhật ký thao tác |
| History Data | Lịch sử thay đổi |
| Reporting Data | Dữ liệu báo cáo |
| Analytics Data | Dữ liệu phân tích |
| Cache Data | Dữ liệu tạm thời |

Mỗi loại dữ liệu có Lifecycle và Policy riêng.

---

# 4. Data Ownership

Mỗi Business Data chỉ có một Domain Owner.

Ví dụ:

| Data | Owner |
|------|-------|
| Sales Order | Order Domain |
| Payment | Payment Domain |
| Inventory | Inventory Domain |
| Settlement | Financial Domain |
| Customer | Customer Domain |

Không có Shared Ownership.

---

# 5. One Source of Truth

Mỗi Business Concept chỉ có một Source of Truth.

Ví dụ:

| Business Concept | Source of Truth |
|------------------|-----------------|
| Customer | Customer Domain |
| Organization | Organization Domain |
| Product | Product Domain |
| Price | Commercial Domain |
| Payment | Payment Domain |

Projection, Cache hoặc Reporting Database không được trở thành Source of Truth.

---

# 6. Data Classification

Platform chuẩn hóa mức độ phân loại dữ liệu.

| Level | Description |
|--------|-------------|
| Public | Công khai |
| Internal | Nội bộ |
| Confidential | Bảo mật |
| Sensitive | Nhạy cảm |
| Restricted | Hạn chế đặc biệt |

Classification điều khiển:

- Permission
- Encryption
- Masking
- Retention
- Audit

---

# 7. Data Lifecycle

Mọi Data đều có Lifecycle.

```text
Created

↓

Validated

↓

Active

↓

Archived

↓

Expired

↓

Purged (if applicable)
```

Retention được điều khiển bởi Policy.

---

# 8. Data Consistency

Platform áp dụng hai mô hình:

| Model | Usage |
|--------|-------|
| Strong Consistency | Trong một Domain |
| Eventual Consistency | Giữa các Domain |

Không sử dụng Distributed Transaction để đạt Strong Consistency giữa nhiều Domain.

---

# 9. Data Persistence

Platform phân biệt:

- Runtime Database
- Snapshot Storage
- Audit Storage
- Reporting Storage
- Analytics Storage
- Cache

Mỗi loại có mục đích riêng.

Không sử dụng Runtime Database cho mọi nhu cầu.

---

# 10. Data Traceability

Mỗi Business Data phải truy vết được tới:

- Business Requirement
- Capability
- Business Object
- Policy
- Rule
- Event
- Snapshot
- Transaction
- API

Data phải luôn có Traceability.

---

# 11. Data Security

Platform áp dụng:

- Encryption
- Masking
- Permission
- Data Scope
- Field Level Protection
- Audit

Data Security được điều khiển bởi Security Policy.

---

# 12. Data Privacy

Platform hỗ trợ:

- Customer Consent
- GDPR
- Data Retention
- Data Minimization
- Right to Access
- Right to Erasure (theo chính sách áp dụng)

Privacy được tích hợp từ thiết kế.

---

# 13. Data Lineage

Platform quản lý Data Lineage.

Ví dụ:

```text
Sales Order
        │
        ▼
Payment
        │
        ▼
Inventory
        │
        ▼
Fulfillment
        │
        ▼
Settlement
        │
        ▼
Financial Ledger
```

Mỗi Business Artifact có khả năng truy ngược nguồn gốc dữ liệu.

---

# 14. Projection & Read Model

Reporting và Analytics sử dụng:

- Projection
- Read Model
- Snapshot
- Reporting View

Không truy vấn trực tiếp Runtime Database cho các báo cáo phức tạp.

---

# 15. Data Governance

Platform quản lý Data thông qua:

- Ownership
- Policy
- Classification
- Version
- Approval
- Audit
- Retention

Mọi thay đổi phải được truy vết.

---

# 16. Data Rules

DA-001 — Business Domain owns Business Data.

DA-002 — One Source of Truth.

DA-003 — Data must be classified.

DA-004 — Data follows Lifecycle.

DA-005 — Data must be traceable.

DA-006 — Runtime Data and Reporting Data are separated.

DA-007 — Snapshot is immutable.

DA-008 — Data Security follows Security Policy.

DA-009 — Projection is not Source of Truth.

DA-010 — Data Governance is mandatory.

---

# 17. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-1101 | Data Owner được xác định |
| ACC-1102 | Source of Truth rõ ràng |
| ACC-1103 | Data Classification được áp dụng |
| ACC-1104 | Runtime và Reporting Data được tách biệt |
| ACC-1105 | Snapshot không bị cập nhật |
| ACC-1106 | Projection không ghi ngược Runtime |
| ACC-1107 | Data Lifecycle được định nghĩa |
| ACC-1108 | Data được bảo vệ theo Security Policy |
| ACC-1109 | Data Traceability đầy đủ |
| ACC-1110 | Data Governance tuân thủ Policy |

Checklist này được sử dụng trong:

- Architecture Review
- Data Review
- AI Review
- CI/CD Validation
- Database Design Review

---

# 18. Relationship to Other Baselines

Platform Data Architecture liên kết với:

- ABP-04 Transaction Boundary
- ABP-05 Event Architecture
- ABP-06 Snapshot Architecture
- ABP-07 Configuration Architecture
- ABP-09 Security Architecture
- BRD-BO-INDEX
- BRD-SNAPSHOT-INDEX
- BRD-POLICY-INDEX

Platform Data Architecture là nền tảng cho DMS và DBD.

---

# 19. Document Status

**Status: FROZEN**

ABP-11 là tài liệu nền tảng quy định kiến trúc dữ liệu của nền tảng YSim.

Mọi Domain Model, Database Design, Reporting, Analytics và AI Implementation phải tuân thủ các nguyên tắc trong tài liệu này.

---