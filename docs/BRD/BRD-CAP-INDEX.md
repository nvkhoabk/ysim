---
document_code: "BRD-CAP-INDEX"
document_id: "BRD-CAP-INDEX"
title: "Enterprise Business Capability Registry"
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

# Enterprise Business Capability Registry

## BRD-CAP-INDEX

---

# 1. Purpose

Enterprise Business Capability Registry là tài liệu quản lý tập trung toàn bộ **Business Capability** của nền tảng YSim.

Business Capability phản ánh **những gì Platform có khả năng thực hiện**, không mô tả cách triển khai kỹ thuật.

Capability Registry là nền tảng để:

- Chuẩn hóa Capability trên toàn Platform.
- Tránh trùng lặp Capability.
- Quản lý phạm vi chức năng.
- Quản lý Feature Toggle.
- Quản lý Permission.
- Quản lý Licensing.
- Quản lý Marketplace Capability.
- Quản lý Roadmap.

Capability Registry là **Source of Truth** cho toàn bộ Platform Capability.

---

# 2. Objectives

Capability Registry được xây dựng nhằm các mục tiêu:

- Chuẩn hóa toàn bộ Business Capability.
- Chuẩn hóa Platform Capability.
- Chuẩn hóa Security Capability.
- Chuẩn hóa Integration Capability.
- Chuẩn hóa Operational Capability.
- Làm cơ sở cho BRD.
- Làm cơ sở cho DMS.
- Làm cơ sở cho SDD.
- Làm cơ sở cho API.
- Làm cơ sở cho Permission.
- Làm cơ sở cho Configuration.
- Làm cơ sở cho Feature Flag.

---

# 3. Scope

Capability Registry bao gồm toàn bộ Capability thuộc các Business Domain:

- Organization
- Customer
- Product
- Commercial
- Promotion
- Order
- Payment
- Inventory
- Fulfillment
- Settlement
- Customer Success
- Communication
- Analytics
- Configuration
- Integration
- Security
- Operations

Ngoài ra còn bao gồm:

- Cross Platform Capability
- Enterprise Capability
- Shared Capability
- Future Capability

---

# 4. Capability Classification

Capability được phân loại theo Type.

| Type | Description |
|------|-------------|
| Business | Năng lực nghiệp vụ |
| Platform | Năng lực nền tảng |
| Technical | Năng lực kỹ thuật |
| Integration | Năng lực tích hợp |
| Security | Năng lực bảo mật |
| Operational | Năng lực vận hành |
| Analytics | Năng lực phân tích |
| Shared | Năng lực dùng chung |

Mỗi Capability chỉ có một Type chính.

---

# 5. Capability Hierarchy

Capability được tổ chức theo mô hình phân cấp.

```text
Enterprise
      │
      ▼
Platform
      │
      ▼
Business Domain
      │
      ▼
Module
      │
      ▼
Feature
```

Ví dụ:

```text
Sales

↓

Order Management

↓

Checkout

↓

Guest Checkout
```

Hierarchy giúp:

- Phân rã chức năng
- Phân quyền
- Feature Toggle
- Capability Dependency

---

# 6. Capability Level

Capability được phân loại theo Level.

| Level | Description |
|-------|-------------|
| Enterprise | Áp dụng toàn Platform |
| Platform | Capability nền tảng |
| Domain | Capability của một Business Domain |
| Module | Capability của Module |
| Feature | Capability chi tiết |

Capability Level giúp xác định phạm vi ảnh hưởng khi thay đổi hoặc cấp quyền.

---

# 7. Capability Lifecycle

Capability có Lifecycle riêng.

```text
Planned

↓

Preview

↓

Beta

↓

General Availability

↓

Deprecated

↓

Retired
```

Lifecycle giúp quản lý Roadmap và Version của Platform.

---

# 8. Capability Availability

Không phải mọi Capability đều khả dụng cho mọi đối tượng.

Capability có thể được cấp cho:

- YSim Platform
- Organization
- Storefront
- Internal User
- Customer Portal
- Public API
- Partner API

Availability được quyết định bởi:

- Capability Policy
- License
- Commercial Agreement
- Permission
- Configuration

---

# 9. Capability Toggle

Capability hỗ trợ bật hoặc tắt.

Capability Toggle phục vụ:

- Feature Flag
- Kill Switch
- Progressive Rollout
- Pilot Deployment
- Beta Testing

Capability Toggle không thay đổi thiết kế nghiệp vụ.

Chỉ thay đổi khả năng sử dụng Capability.

---

# 10. Capability Identifier

Mỗi Capability được cấp một mã định danh duy nhất.

Quy ước:

```text
CAP-0001
CAP-0002
CAP-0003
...
```

Capability ID được sử dụng trong:

- BRD
- DMS
- SDD
- API
- Permission
- Feature Flag
- Marketplace
- Licensing
- Architecture Review

Capability ID không thay đổi trong suốt vòng đời của Capability.

---

# 11. Registry Principles

Capability Registry tuân thủ các nguyên tắc sau.

## CAP-P01 — Business First

Capability phản ánh năng lực nghiệp vụ hoặc nền tảng.

Không phản ánh thiết kế kỹ thuật.

---

## CAP-P02 — Single Source of Truth

Một Capability chỉ có một định nghĩa duy nhất.

Không tồn tại nhiều Capability có cùng ý nghĩa.

---

## CAP-P03 — Stable Identifier

Capability ID là bất biến.

Tên Capability có thể được cải tiến nhưng Capability ID không thay đổi.

---

## CAP-P04 — Configurable

Capability phải có khả năng được cấu hình khi phù hợp.

Không Hard-code nếu có thể cấu hình.

---

## CAP-P05 — Permission Aware

Capability có thể được cấp quyền.

Permission luôn tham chiếu Capability.

---

## CAP-P06 — Feature Toggle Ready

Capability có thể được bật hoặc tắt thông qua Feature Flag hoặc Configuration.

---

## CAP-P07 — Event Driven

Capability có thể Publish hoặc Subscribe Business Event.

---

## CAP-P08 — Enterprise Governance

Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance.

Mọi Capability mới phải trải qua:

- Architecture Review
- Approval
- Versioning
- Audit
- Traceability

---

# 12. Relationship to Other Documents

Capability Registry là tài liệu trung tâm của lớp Enterprise Capability.

Các tài liệu liên quan:

| Document | Relationship |
|----------|--------------|
| BRD Workshop | Định nghĩa Capability |
| BRD-BO-INDEX | Business Object sử dụng Capability |
| DMS | Domain Model |
| API Specification | API thực hiện Capability |
| SDD | Kiến trúc triển khai Capability |
| Permission Model | Quyền sử dụng Capability |
| Feature Flag | Điều khiển bật/tắt Capability |
| CIP | Triển khai Capability |

Capability Registry không thay thế các tài liệu trên.

Capability Registry đóng vai trò là **Enterprise Capability Dictionary** và là tài liệu tham chiếu thống nhất cho toàn bộ Platform.

------

# 13. Enterprise Capability Registry

## 13.1 Organization Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-0001 | Organization Management | Domain | Organization | Platform | Yes | Yes | Yes | WS-03 |
| CAP-0002 | Organization Hierarchy | Module | Organization Relationship | Platform | Yes | Yes | Yes | WS-03 |
| CAP-0003 | Organization Capability Management | Module | Organization Capability | Platform | Yes | Yes | Yes | WS-03 |
| CAP-0004 | User Management | Module | User | Organization | Yes | Yes | Yes | WS-03 |
| CAP-0005 | Role Management | Module | User Role Assignment | Organization | Yes | Yes | Yes | WS-03 |
| CAP-0006 | Storefront Management | Module | Storefront | Organization | Yes | Yes | Yes | WS-03 |
| CAP-0007 | Theme Management | Feature | Storefront Theme | Organization | Yes | Yes | Yes | WS-03 |
| CAP-0008 | Sales Management | Module | Sales Representative | Organization | Yes | Yes | Yes | WS-03 |
| CAP-0009 | Affiliate Management | Module | Affiliate | Organization | Yes | Yes | Yes | WS-03 |
| CAP-0010 | Collaborator Management | Module | Collaborator | Organization | Yes | Yes | Yes | WS-03 |

---

## 13.2 Customer Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-0101 | Customer Management | Domain | Customer | Platform | Yes | Yes | Yes | WS-03 |
| CAP-0102 | Guest Checkout | Feature | Customer Identity | Storefront | Yes | No | Yes | WS-07 |
| CAP-0103 | Identity Merge | Feature | Customer Identity | Platform | Yes | Yes | Yes | WS-03 |
| CAP-0104 | Customer Assignment | Module | Customer Assignment | Storefront | Yes | Yes | Yes | WS-09 |
| CAP-0105 | Customer Portal | Module | Customer Portal Account | Customer | Yes | Yes | Yes | WS-11 |
| CAP-0106 | Customer Preference | Module | Customer Preference | Customer | Yes | No | Yes | WS-11 |
| CAP-0107 | Customer Consent | Module | Customer Consent | Customer | Yes | No | Yes | WS-16 |
| CAP-0108 | Customer Subscription | Module | Customer Subscription | Customer | Yes | No | Yes | WS-12 |

---

## 13.3 Product Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-0201 | Product Management | Domain | Master Product | Platform | Yes | Yes | Yes | WS-04 |
| CAP-0202 | Supplier Product Mapping | Module | Supplier Product | Platform | Yes | Yes | Yes | WS-04 |
| CAP-0203 | Product Variant Management | Module | Product Variant | Platform | Yes | Yes | Yes | WS-04 |
| CAP-0204 | Product Category Management | Module | Product Category | Platform | Yes | Yes | Yes | WS-04 |
| CAP-0205 | Product Collection Management | Module | Product Collection | Platform | Yes | Yes | Yes | WS-04 |
| CAP-0206 | Product Attribute Management | Module | Product Attribute | Platform | Yes | Yes | Yes | WS-04 |
| CAP-0207 | Region Management | Module | Region | Platform | Yes | Yes | Yes | WS-04 |
| CAP-0208 | Carrier Management | Module | Carrier | Platform | Yes | Yes | Yes | WS-04 |

---

## 13.4 Commercial Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-0301 | Commercial Management | Domain | Commercial Agreement | Platform | Yes | Yes | Yes | WS-05 |
| CAP-0302 | Price Book Management | Module | Price Book | Organization | Yes | Yes | Yes | WS-05 |
| CAP-0303 | Pricing Engine | Module | Pricing Formula | Platform | Yes | Yes | Yes | WS-05 |
| CAP-0304 | Revenue Sharing | Module | Revenue Sharing Rule | Organization | Yes | Yes | Yes | WS-05 |
| CAP-0305 | Commercial Policy Management | Module | Commercial Policy | Platform | Yes | Yes | Yes | WS-05 |
| CAP-0306 | Payment Owner Management | Module | Payment Owner | Organization | Yes | Yes | Yes | WS-05 |

---

## 13.5 Promotion Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-0401 | Promotion Management | Domain | Promotion | Organization | Yes | Yes | Yes | WS-06 |
| CAP-0402 | Campaign Management | Module | Campaign | Organization | Yes | Yes | Yes | WS-06 |
| CAP-0403 | Coupon Management | Module | Coupon | Organization | Yes | Yes | Yes | WS-06 |
| CAP-0404 | Promotion Rule Management | Module | Promotion Rule | Organization | Yes | Yes | Yes | WS-06 |
| CAP-0405 | Promotion Funding | Module | Promotion Funding | Platform | Yes | Yes | Yes | WS-06 |
| CAP-0406 | Marketing Attribution | Module | Marketing Attribution | Organization | Yes | Yes | Yes | WS-06 |

---

## 13.6 Order Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-0501 | Shopping Cart | Module | Shopping Cart | Storefront | Yes | No | Yes | WS-07 |
| CAP-0502 | Checkout | Module | Checkout Session | Storefront | Yes | No | Yes | WS-07 |
| CAP-0503 | Sales Order Management | Domain | Sales Order | Organization | Yes | Yes | Yes | WS-07 |
| CAP-0504 | Purchase Order Management | Domain | Purchase Order | Platform | Yes | Yes | Yes | WS-07 |
| CAP-0505 | Automatic Procurement | Feature | Purchase Order | Platform | Yes | Yes | Yes | WS-07 |
| CAP-0506 | Cart Recovery | Feature | Shopping Cart | Storefront | Yes | Yes | Yes | WS-07 |
| CAP-0507 | Order Snapshot | Feature | Sales Order | Platform | Automatic | No | Yes | WS-07 |

---

## 13.7 Payment Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-0601 | Payment Management | Domain | Payment | Organization | Yes | Yes | Yes | WS-08 |
| CAP-0602 | Payment Session | Module | Payment Session | Storefront | Automatic | No | Yes | WS-08 |
| CAP-0603 | Payment Retry | Feature | Payment Attempt | Platform | Yes | Yes | Yes | WS-08 |
| CAP-0604 | Refund Management | Module | Refund | Organization | Yes | Yes | Yes | WS-08 |
| CAP-0605 | Offline Payment | Module | Payment | Organization | Yes | Yes | Yes | WS-08 |
| CAP-0606 | Merchant Account Management | Module | Merchant Account | Organization | Yes | Yes | Yes | WS-08 |
| CAP-0607 | Payment Gateway Integration | Platform | Payment Gateway | Platform | Yes | Yes | Yes | WS-08 |

------

# 13.8 Inventory & Fulfillment Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-0701 | Inventory Management | Domain | Inventory | Platform | Yes | Yes | Yes | WS-09 |
| CAP-0702 | Inventory Reservation | Module | Inventory Reservation | Platform | Yes | Yes | Yes | WS-09 |
| CAP-0703 | Inventory Allocation | Module | Inventory Allocation | Platform | Yes | Yes | Yes | WS-09 |
| CAP-0704 | Allocation Engine | Module | Allocation Policy | Platform | Yes | Yes | Yes | WS-09 |
| CAP-0705 | Fulfillment Management | Domain | Fulfillment Session | Platform | Yes | Yes | Yes | WS-09 |
| CAP-0706 | Delivery Management | Module | Fulfillment Task | Platform | Yes | Yes | Yes | WS-09 |
| CAP-0707 | QR Distribution | Module | QR Distribution | Platform | Yes | Yes | Yes | WS-09 |
| CAP-0708 | Customer Assignment | Feature | Customer Assignment | Organization | Yes | Yes | Yes | WS-09 |
| CAP-0709 | Revoked Inventory Management | Module | Revoked Inventory | Platform | Yes | Yes | Yes | WS-09 |
| CAP-0710 | Delivery Retry | Feature | Fulfillment Task | Platform | Yes | Yes | Yes | WS-09 |

---

# 13.9 Financial & Settlement Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-0801 | Settlement Management | Domain | Settlement | Platform | Yes | Yes | Yes | WS-10 |
| CAP-0802 | Commission Management | Module | Commission Snapshot | Organization | Yes | Yes | Yes | WS-10 |
| CAP-0803 | Revenue Sharing | Module | Revenue Recipient | Organization | Yes | Yes | Yes | WS-10 |
| CAP-0804 | Financial Ledger | Module | Ledger Entry | Platform | Yes | Yes | Yes | WS-10 |
| CAP-0805 | Wallet Management | Module | Wallet | Organization | Yes | Yes | Yes | WS-10 |
| CAP-0806 | Financial Event Processing | Module | Financial Event | Platform | Automatic | No | Yes | WS-10 |
| CAP-0807 | Settlement Approval | Feature | Settlement | Organization | Yes | Yes | Yes | WS-10 |
| CAP-0808 | Financial Export | Feature | Settlement | Organization | Yes | Yes | Yes | WS-10 |

---

# 13.10 Customer Success Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-0901 | Customer Support | Domain | Ticket | Organization | Yes | Yes | Yes | WS-11 |
| CAP-0902 | Ticket Management | Module | Ticket | Organization | Yes | Yes | Yes | WS-11 |
| CAP-0903 | Knowledge Base | Module | Knowledge Base Article | Organization | Yes | Yes | Yes | WS-11 |
| CAP-0904 | FAQ Management | Module | FAQ | Organization | Yes | Yes | Yes | WS-11 |
| CAP-0905 | Troubleshooting Wizard | Module | Troubleshooting Guide | Organization | Yes | Yes | Yes | WS-11 |
| CAP-0906 | Customer Feedback | Module | Customer Feedback | Organization | Yes | Yes | Yes | WS-11 |
| CAP-0907 | Satisfaction Survey | Module | Satisfaction Survey | Organization | Yes | Yes | Yes | WS-11 |
| CAP-0908 | Support Queue Routing | Module | Support Queue | Platform | Yes | Yes | Yes | WS-11 |
| CAP-0909 | Organization Onboarding | Module | Organization Onboarding Checklist | Organization | Yes | Yes | Yes | WS-11 |
| CAP-0910 | Feature Request Management | Module | Feature Request | Platform | Yes | Yes | Yes | WS-11 |

---

# 13.11 Communication Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-1001 | Notification Management | Domain | Notification | Platform | Yes | Yes | Yes | WS-12 |
| CAP-1002 | Notification Routing | Module | Notification Event | Platform | Yes | Yes | Yes | WS-12 |
| CAP-1003 | Template Management | Module | Notification Template | Organization | Yes | Yes | Yes | WS-12 |
| CAP-1004 | Communication Policy | Module | Communication Policy | Platform | Yes | Yes | Yes | WS-12 |
| CAP-1005 | Contact Point Management | Module | Contact Point | Platform | Yes | Yes | Yes | WS-12 |
| CAP-1006 | Personal Inbox | Module | Personal Inbox Message | User | Automatic | No | Yes | WS-12 |
| CAP-1007 | Portal Announcement | Module | Portal Announcement | Organization | Yes | Yes | Yes | WS-12 |
| CAP-1008 | Multi-language Notification | Feature | Notification | Platform | Yes | No | Yes | WS-12 |
| CAP-1009 | Read Receipt | Feature | Communication Log | Platform | Yes | No | Yes | WS-12 |

---

# 13.12 Analytics & Reporting Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-1101 | Dashboard Management | Domain | Dashboard | Organization | Yes | Yes | Yes | WS-13 |
| CAP-1102 | Widget Management | Module | Dashboard Widget | Organization | Yes | Yes | Yes | WS-13 |
| CAP-1103 | Report Management | Domain | Report | Organization | Yes | Yes | Yes | WS-13 |
| CAP-1104 | Report Scheduling | Module | Report Schedule | Organization | Yes | Yes | Yes | WS-13 |
| CAP-1105 | Report Builder | Module | Report | Organization | Yes | Yes | Yes | WS-13 |
| CAP-1106 | KPI Management | Module | KPI Definition | Organization | Yes | Yes | Yes | WS-13 |
| CAP-1107 | Alert Management | Module | Alert Rule | Organization | Yes | Yes | Yes | WS-13 |
| CAP-1108 | Saved View | Module | Saved View | User | Yes | No | Yes | WS-13 |
| CAP-1109 | Widget Library | Module | Widget Library | Platform | Yes | Yes | Yes | WS-13 |

---

# 13.13 Platform Configuration Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-1201 | Configuration Management | Domain | Configuration | Platform | Yes | Yes | Yes | WS-14 |
| CAP-1202 | Reference Data Management | Module | Reference Data | Platform | Yes | Yes | Yes | WS-14 |
| CAP-1203 | Dictionary Management | Module | Dictionary | Platform | Yes | Yes | Yes | WS-14 |
| CAP-1204 | Business Rule Management | Module | Business Rule | Platform | Yes | Yes | Yes | WS-14 |
| CAP-1205 | Metadata Management | Module | Metadata | Platform | Yes | Yes | Yes | WS-14 |
| CAP-1206 | Configuration Package | Module | Configuration Package | Platform | Yes | Yes | Yes | WS-14 |
| CAP-1207 | Organization Template | Module | Organization Template | Platform | Yes | Yes | Yes | WS-14 |
| CAP-1208 | Runtime Configuration Reload | Feature | Configuration | Platform | Automatic | No | Yes | WS-14 |

---

# 13.14 Integration Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-1301 | Connector Management | Domain | Connector | Platform | Yes | Yes | Yes | WS-15 |
| CAP-1302 | Adapter Management | Module | Adapter | Platform | Yes | Yes | Yes | WS-15 |
| CAP-1303 | API Gateway | Platform | Connector | Platform | Yes | Yes | Yes | WS-15 |
| CAP-1304 | Business Event Platform | Platform | Business Event | Platform | Yes | Yes | Yes | WS-15 |
| CAP-1305 | Queue Management | Platform | Queue | Platform | Yes | Yes | Yes | WS-15 |
| CAP-1306 | Callback Management | Module | Callback | Platform | Yes | Yes | Yes | WS-15 |
| CAP-1307 | Canonical Data Management | Module | Canonical Data Model | Platform | Yes | Yes | Yes | WS-15 |
| CAP-1308 | Connector Routing | Module | Connector Routing Rule | Platform | Yes | Yes | Yes | WS-15 |
| CAP-1309 | Integration Monitoring | Module | Connector | Platform | Yes | Yes | Yes | WS-15 |
| CAP-1310 | Business Service Registry | Module | Business Service Registry | Platform | Yes | Yes | Yes | WS-15 |

---

# 13.15 Security Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-1401 | Authentication | Platform | Session | Platform | Yes | Yes | Yes | WS-16 |
| CAP-1402 | Authorization | Platform | Permission | Platform | Yes | Yes | Yes | WS-16 |
| CAP-1403 | RBAC & ABAC | Module | Permission | Platform | Yes | Yes | Yes | WS-16 |
| CAP-1404 | Customer Consent | Module | Customer Consent | Platform | Yes | Yes | Yes | WS-16 |
| CAP-1405 | Secret Management | Module | Secret | Platform | Yes | Yes | Yes | WS-16 |
| CAP-1406 | Risk Management | Module | Risk Rule | Platform | Yes | Yes | Yes | WS-16 |
| CAP-1407 | Data Protection | Module | Data Classification | Platform | Yes | Yes | Yes | WS-16 |
| CAP-1408 | Audit Logging | Platform | Audit Log | Platform | Automatic | No | Yes | WS-16 |

---

# 13.16 Platform Operations Domain

| CAP ID | Capability | Level | Main Business Object | Availability | Configurable | Permission | Event | Workshop |
|---------|------------|-------|----------------------|--------------|--------------|------------|-------|----------|
| CAP-1501 | Platform Operations | Domain | Operation Policy | Platform | Yes | Yes | Yes | WS-17 |
| CAP-1502 | Scheduler | Module | Scheduler Job | Platform | Yes | Yes | Yes | WS-17 |
| CAP-1503 | Worker Management | Module | Worker | Platform | Yes | Yes | Yes | WS-17 |
| CAP-1504 | Monitoring | Module | System Health | Platform | Yes | Yes | Yes | WS-17 |
| CAP-1505 | Alert Management | Module | Alert Rule | Platform | Yes | Yes | Yes | WS-17 |
| CAP-1506 | Maintenance Management | Module | Maintenance Window | Platform | Yes | Yes | Yes | WS-17 |
| CAP-1507 | Backup Management | Module | Backup Policy | Platform | Yes | Yes | Yes | WS-17 |
| CAP-1508 | Disaster Recovery | Module | Disaster Recovery Policy | Platform | Yes | Yes | Yes | WS-17 |
| CAP-1509 | Runbook Management | Module | Runbook | Platform | Yes | Yes | Yes | WS-17 |
| CAP-1510 | Feature Flag Management | Module | Feature Flag | Platform | Yes | Yes | Yes | WS-17 |
| CAP-1511 | Replay Platform | Module | Job Execution | Platform | Yes | Yes | Yes | WS-17 |
| CAP-1512 | Operational Dashboard | Module | System Health | Platform | Yes | Yes | Yes | WS-17 |

------

# 13.17 Cross Platform Capabilities

Các Capability dưới đây được sử dụng xuyên suốt nhiều Business Domain.

| CAP ID | Capability | Level | Main Business Object | Availability | Workshop |
|---------|------------|-------|----------------------|--------------|----------|
| CAP-9001 | Enterprise Search | Platform | Search Index | Platform | Future |
| CAP-9002 | Workflow Engine | Platform | Workflow Definition | Platform | Future |
| CAP-9003 | Approval Engine | Platform | Approval Workflow | Platform | Future |
| CAP-9004 | Notification Engine | Platform | Notification | Platform | WS-12 |
| CAP-9005 | Event Bus | Platform | Business Event | Platform | WS-15 |
| CAP-9006 | Audit Platform | Platform | Audit Log | Platform | WS-16 |
| CAP-9007 | Localization Platform | Platform | Localization Resource | Platform | WS-12 |
| CAP-9008 | Feature Flag Platform | Platform | Feature Flag | Platform | WS-17 |
| CAP-9009 | Scheduler Platform | Platform | Scheduler Job | Platform | WS-17 |
| CAP-9010 | Analytics Platform | Platform | Dashboard | Platform | WS-13 |

---

# 13.18 Future Capability Roadmap

Các Capability dự kiến triển khai trong các phiên bản tiếp theo.

| Capability | Planned Version |
|------------|-----------------|
| AI Customer Support | vNext |
| AI Knowledge Assistant | vNext |
| AI Translation Improvement | vNext |
| Loyalty Program | vNext |
| Loyalty Wallet | vNext |
| Reward Point | vNext |
| Subscription Billing | vNext |
| Device Management | vNext |
| eSIM Activation Polling | vNext |
| WebRTC Call Center | vNext |
| Marketplace Platform | Future |
| Recommendation Engine | Future |
| Dynamic Pricing Engine | Future |
| Fraud Detection Platform | Future |

Các Capability trên chưa thuộc phạm vi Version hiện tại nhưng kiến trúc đã được thiết kế mở để hỗ trợ mở rộng.

---

# 14. Capability Dependency Matrix

Capability trên Platform có quan hệ phụ thuộc lẫn nhau.

Ví dụ:

```text
Organization Management
            │
            ▼
Storefront Management
            │
            ▼
Shopping Cart
            │
            ▼
Checkout
            │
            ▼
Payment
            │
            ▼
Inventory Allocation
            │
            ▼
Fulfillment
            │
            ▼
Notification
            │
            ▼
Settlement
            │
            ▼
Analytics
```

Một số Capability nền tảng được nhiều Domain sử dụng:

```text
Configuration
        │
        ├──── Security
        ├──── Notification
        ├──── Integration
        ├──── Analytics
        ├──── Operations
        └──── Customer Portal
```

Dependency Matrix được sử dụng cho:

- Impact Analysis
- Capability Planning
- Architecture Review
- Roadmap Planning

---

# 15. Capability Relationship Principles

## CAP-R01 — Business First

Capability phản ánh năng lực nghiệp vụ.

Không phản ánh thiết kế kỹ thuật.

---

## CAP-R02 — Business Object Driven

Mỗi Capability phải có ít nhất một Business Object chính.

---

## CAP-R03 — Event Driven

Capability ưu tiên Publish hoặc Subscribe Business Event.

---

## CAP-R04 — Configurable

Capability phải ưu tiên Configuration thay vì Hard-code.

---

## CAP-R05 — Permission Controlled

Capability được kiểm soát bởi Permission Model.

---

## CAP-R06 — Feature Toggle Ready

Capability có khả năng bật/tắt thông qua Feature Flag.

---

## CAP-R07 — Organization Aware

Capability có thể được:

- kế thừa từ Parent Organization
- Override bởi Organization
- giới hạn theo Commercial Agreement
- giới hạn theo Capability Policy

---

# 16. Capability Mapping

Capability Registry có mối liên hệ với các Registry khác.

| Registry | Relationship |
|----------|--------------|
| Business Object Registry | Capability sử dụng Business Object |
| Business Event Registry | Capability Publish / Subscribe Event |
| Policy Registry | Capability chịu điều khiển bởi Policy |
| Snapshot Registry | Capability tạo Snapshot |
| Permission Model | Capability được cấp quyền |
| Feature Flag | Capability được bật/tắt |
| Configuration Registry | Capability được cấu hình |

---

# 17. Capability Traceability

Mỗi Capability nên có khả năng Trace tới:

- Business Requirement
- Business Rule
- Business Object
- Business Event
- API
- UI Module
- Configuration
- Permission
- Feature Flag
- Test Case

Ví dụ:

| Capability | Traceability |
|------------|--------------|
| Checkout | BRD → BO → Event → API → UI → Test |
| Payment | BRD → BO → Event → Gateway → Test |
| Fulfillment | BRD → BO → Notification → Test |
| Settlement | BRD → BO → Ledger → Report |

---

# 18. Capability Statistics

## 18.1 Statistics by Domain

| Domain | Estimated Capability |
|---------|---------------------:|
| Organization | 10 |
| Customer | 8 |
| Product | 8 |
| Commercial | 6 |
| Promotion | 6 |
| Order | 7 |
| Payment | 7 |
| Inventory & Fulfillment | 10 |
| Settlement | 8 |
| Customer Success | 10 |
| Communication | 9 |
| Analytics | 9 |
| Configuration | 8 |
| Integration | 10 |
| Security | 8 |
| Operations | 12 |
| Cross Platform | 10 |

---

## 18.2 Statistics by Type

| Type | Estimated Capability |
|------|---------------------:|
| Business | 70+ |
| Platform | 25+ |
| Technical | 8+ |
| Integration | 12+ |
| Security | 10+ |
| Operational | 15+ |
| Analytics | 10+ |
| Shared | 10+ |

---

## 18.3 Total

Tổng số Capability hiện tại:

**Khoảng 220 Capability**

Số lượng này có thể tăng theo từng phiên bản.

---

# 19. Enterprise Capability Principles

## CAP-EP-001

Capability phản ánh năng lực của Platform.

---

## CAP-EP-002

Capability độc lập với UI.

---

## CAP-EP-003

Capability độc lập với Database.

---

## CAP-EP-004

Capability độc lập với Source Code.

---

## CAP-EP-005

Capability được cấu hình thay vì Hard-code khi phù hợp.

---

## CAP-EP-006

Capability có thể Publish hoặc Subscribe Business Event.

---

## CAP-EP-007

Capability hỗ trợ Multi-tenant.

---

## CAP-EP-008

Capability hỗ trợ White-label.

---

## CAP-EP-009

Capability hỗ trợ mở rộng theo Version.

---

## CAP-EP-010

Capability Registry là Enterprise Capability Dictionary của YSim.

---

# 20. Document Status

Status:

**FROZEN**

Enterprise Business Capability Registry là tài liệu nền tảng quản lý toàn bộ Capability của nền tảng YSim.

Mọi Capability mới hoặc thay đổi Capability hiện có phải được:

- Architecture Review
- Approval
- Versioning
- Audit
- Traceability

trước khi được sử dụng trong Platform.

---

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R001 —  Future Capability

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R001",
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
  "normative_statement": "- Future Capability",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-001",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Scope",
    "source_context_sha256": "9f62803020731dac65c52a9a79fb950abf304dc612a946abf06d6fd27d117e10",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "2a0425a67d37d9d304a1e540c1a857eaf2af6b01c3800767a9a2ca49898a5f99",
    "source_lines": "L963-L1023",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R001"
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
  "stable_id": "BRD-CAP-INDEX-R001",
  "title": " Future Capability",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R002 — Không phải mọi Capability đều khả dụng cho mọi đối tượng

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
      "requirement_id": "BRD-CAP-INDEX-R002",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "c5f750dae413d6dc3c22777ebda6723db51805257f345fcc38d62adb7f57fc10"
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
        "BRD-CAP-INDEX-R002-AC001",
        "BRD-CAP-INDEX-R002-AC002",
        "BRD-CAP-INDEX-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R002-O001",
      "obligation_text": "Không phải mọi Capability đều khả dụng cho mọi đối tượng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không phải mọi Capability đều khả dụng cho mọi đối tượng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-002",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Capability Availability",
    "source_context_sha256": "497c1f8f3bada17bce3e707cded295bc794c641ec3aedd0354c80eb156e715d2",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "c5f750dae413d6dc3c22777ebda6723db51805257f345fcc38d62adb7f57fc10",
    "source_lines": "L1025-L1107",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R002"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-CAP-INDEX-R004"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R002",
  "title": "Không phải mọi Capability đều khả dụng cho mọi đối tượng",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R003 — Mỗi Capability được cấp một mã định danh duy nhất

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
      "requirement_id": "BRD-CAP-INDEX-R003",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "f2cde12ec2a2f83abb8b89ac4a8531af65838f5f90ea7a15ee9ed5ab24430fb3"
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
        "BRD-CAP-INDEX-R003-AC001",
        "BRD-CAP-INDEX-R003-AC002",
        "BRD-CAP-INDEX-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R003-O001",
      "obligation_text": "Mỗi Capability được cấp một mã định danh duy nhất"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Capability được cấp một mã định danh duy nhất.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-003",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Capability Identifier",
    "source_context_sha256": "7b4bb18b28a04779b5f4f5e0dbabeb8464342d61664b566328eed6a94efc1e87",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "f2cde12ec2a2f83abb8b89ac4a8531af65838f5f90ea7a15ee9ed5ab24430fb3",
    "source_lines": "L1109-L1191",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R003"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-CAP-INDEX-R004"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R003",
  "title": "Mỗi Capability được cấp một mã định danh duy nhất",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R004 — Capability Registry tuân thủ các nguyên tắc sau

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
  "normative_statement": "Capability Registry tuân thủ các nguyên tắc sau.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-004",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Registry Principles",
    "source_context_sha256": "8cc5c2e64651797bcc871a28877ede5204d2ccf7a34543a1760a30bbc3444294",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "637111fb992fcef4a72f019a72061d027e5f871df94673681ad252e9f7c0f62f",
    "source_fingerprint_before_c3": "637111fb992fcef4a72f019a72061d027e5f871df94673681ad252e9f7c0f62f",
    "source_lines": "L1193-L1258",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R004"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-CAP-INDEX-R002",
      "BRD-CAP-INDEX-R003",
      "BRD-CAP-INDEX-R024",
      "BRD-CAP-INDEX-R025",
      "BRD-CAP-INDEX-R026",
      "BRD-CAP-INDEX-R027",
      "BRD-CAP-INDEX-R028"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R004",
  "title": "Capability Registry tuân thủ các nguyên tắc sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R005 — | CAP ID | Capability | Level | Main Business Object | Availability | Workshop | | CAP-9001 | En…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R005",
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
  "normative_statement": "| CAP ID | Capability | Level | Main Business Object | Availability | Workshop | | CAP-9001 | Enterprise Search | Platform | Search Index | Platform | Future |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-010"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-005",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.17 Cross Platform Capabilities",
    "source_context_sha256": "0891ca89a0d69d778fae30177c82a932fc6508289c8b09bab6d3c846aa062071",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "7fc9d0aac8722228a747ea2c170ec7d33c5f0d40d1a59f2cc6fbd370fbd150af",
    "source_lines": "L1260-L1321",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R005"
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
  "stable_id": "BRD-CAP-INDEX-R005",
  "title": "| CAP ID | Capability | Level | Main Business Object | Availability | Workshop | | CAP-9001 | En…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R006 — | CAP ID | Capability | Level | Main Business Object | Availability | Workshop | | CAP-9002 | Wo…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R006",
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
  "normative_statement": "| CAP ID | Capability | Level | Main Business Object | Availability | Workshop | | CAP-9002 | Workflow Engine | Platform | Workflow Definition | Platform | Future |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-010"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-006",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.17 Cross Platform Capabilities",
    "source_context_sha256": "0891ca89a0d69d778fae30177c82a932fc6508289c8b09bab6d3c846aa062071",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "edab623caaf788986a3b41ea30f651a45e285e1344eea24fadcfa50a009fd4ee",
    "source_lines": "L1323-L1384",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R006"
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
  "stable_id": "BRD-CAP-INDEX-R006",
  "title": "| CAP ID | Capability | Level | Main Business Object | Availability | Workshop | | CAP-9002 | Wo…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R007 — Shared Approval Engine

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
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-003",
      "selected_disposition": "APPROVED_SCOPE_PROMOTION_REMEDIATION"
    }
  ],
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nền tảng phải cung cấp Shared Approval Engine dùng chung cho ngoại lệ biên lợi nhuận, hoàn tiền, cấu hình, thông tin xác thực, ghi đè rủi ro và các nghiệp vụ BRD quy định; engine phải hỗ trợ policy, phân giải người duyệt, phân tách nhiệm vụ, hết hạn, escalation, delegation, evidence và immutable audit, đồng thời không được diễn giải thành general-purpose BPM workflow engine.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "P2-DEC-005",
      "P2-DEC-010",
      "SD-03",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-007",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-007",
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.17 Cross Platform Capabilities",
    "source_context_sha256": "0891ca89a0d69d778fae30177c82a932fc6508289c8b09bab6d3c846aa062071",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "cea70aaf3de7030c0356aa4c27d74461559e3ff1e2872ac59d49f89341872de8",
    "source_fingerprint_before_c3": "906e4dc6c37245c232bdb378483b08e6091f230e370e05810029517652b9f23e",
    "source_lines": "L1386-L1461",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R007"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-CAP-INDEX-R030",
      "BRD-CAP-INDEX-R031"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R007",
  "title": "Shared Approval Engine",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R009 — | Capability | Planned Version | | AI Customer Support | vNext |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R009",
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
  "normative_statement": "| Capability | Planned Version | | AI Customer Support | vNext |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-009",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "e0f13a705ff26889ecf8bb213fd985dc5bf9af52a606ce023d65b6f47f57b3b9",
    "source_lines": "L1463-L1524",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R009"
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
  "stable_id": "BRD-CAP-INDEX-R009",
  "title": "| Capability | Planned Version | | AI Customer Support | vNext |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R010 — | Capability | Planned Version | | AI Knowledge Assistant | vNext |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R010",
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
  "normative_statement": "| Capability | Planned Version | | AI Knowledge Assistant | vNext |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-010",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "74dcf9cf6f6ff80826103a0bb6056bf2c6e499b419dfd76837212109d5791364",
    "source_lines": "L1526-L1586",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R010"
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
  "stable_id": "BRD-CAP-INDEX-R010",
  "title": "| Capability | Planned Version | | AI Knowledge Assistant | vNext |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R011 — | Capability | Planned Version | | AI Translation Improvement | vNext |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R011",
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
  "normative_statement": "| Capability | Planned Version | | AI Translation Improvement | vNext |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-010"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-011",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "7f9bb6a197a691369152f2423b65e437e4b6b12f0690032600d9c72b42571d02",
    "source_lines": "L1588-L1649",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R011"
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
  "stable_id": "BRD-CAP-INDEX-R011",
  "title": "| Capability | Planned Version | | AI Translation Improvement | vNext |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R012 — | Capability | Planned Version | | Loyalty Program | vNext |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R012",
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
  "normative_statement": "| Capability | Planned Version | | Loyalty Program | vNext |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-012",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "c75744846d8edda05b606c01fb5fc4be11e48724eea9d9a15b8e804e953a3586",
    "source_lines": "L1651-L1711",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R012"
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
  "stable_id": "BRD-CAP-INDEX-R012",
  "title": "| Capability | Planned Version | | Loyalty Program | vNext |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R013 — | Capability | Planned Version | | Loyalty Wallet | vNext |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R013",
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
  "normative_statement": "| Capability | Planned Version | | Loyalty Wallet | vNext |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-013",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "76572583626859b830b87161ef24c622b4c573bf73f007e6d2cca06a8089e1e1",
    "source_lines": "L1713-L1773",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R013"
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
  "stable_id": "BRD-CAP-INDEX-R013",
  "title": "| Capability | Planned Version | | Loyalty Wallet | vNext |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R014 — | Capability | Planned Version | | Reward Point | vNext |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R014",
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
  "normative_statement": "| Capability | Planned Version | | Reward Point | vNext |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-014",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "6893edbea136a79f7fd551d2ca79bced70d1f75e8fe701e968f914718ba3c461",
    "source_lines": "L1775-L1835",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R014"
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
  "stable_id": "BRD-CAP-INDEX-R014",
  "title": "| Capability | Planned Version | | Reward Point | vNext |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R015 — | Capability | Planned Version | | Subscription Billing | vNext |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R015",
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
  "normative_statement": "| Capability | Planned Version | | Subscription Billing | vNext |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-015",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "0d9242d8b6b433505e1ff23c8d55a95898ccd526473f425f64b850e15ecfab16",
    "source_lines": "L1837-L1897",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R015"
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
  "stable_id": "BRD-CAP-INDEX-R015",
  "title": "| Capability | Planned Version | | Subscription Billing | vNext |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R016 — | Capability | Planned Version | | Device Management | vNext |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R016",
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
  "normative_statement": "| Capability | Planned Version | | Device Management | vNext |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-016",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "0239fd3f4921ae23bc541a08efdc456c81be3876d4f7c61598cdcc767b07ac07",
    "source_lines": "L1899-L1959",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R016"
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
  "stable_id": "BRD-CAP-INDEX-R016",
  "title": "| Capability | Planned Version | | Device Management | vNext |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R017 — | Capability | Planned Version | | eSIM Activation Polling | vNext |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R017",
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
  "normative_statement": "| Capability | Planned Version | | eSIM Activation Polling | vNext |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-017",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "a9a7d374aa6e0d863ccc176e8e3da4b9b581e0971307785ba8ff4e36bbd1116e",
    "source_lines": "L1961-L2021",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R017"
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
  "stable_id": "BRD-CAP-INDEX-R017",
  "title": "| Capability | Planned Version | | eSIM Activation Polling | vNext |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R018 — | Capability | Planned Version | | WebRTC Call Center | vNext |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R018",
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
  "normative_statement": "| Capability | Planned Version | | WebRTC Call Center | vNext |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-018",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "dcdd265a78974a8966bf5d5b1f7a46916fded8ccf6b77827561e3e4488241399",
    "source_lines": "L2023-L2083",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R018"
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
  "stable_id": "BRD-CAP-INDEX-R018",
  "title": "| Capability | Planned Version | | WebRTC Call Center | vNext |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R019 — | Capability | Planned Version | | Marketplace Platform | Future |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R019",
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
  "normative_statement": "| Capability | Planned Version | | Marketplace Platform | Future |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-019",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "551186b55bb67987aef0a930d7e9da0deb44638f4afb6331865cf1b4ba4ccf36",
    "source_lines": "L2085-L2145",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R019"
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
  "stable_id": "BRD-CAP-INDEX-R019",
  "title": "| Capability | Planned Version | | Marketplace Platform | Future |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R020 — | Capability | Planned Version | | Recommendation Engine | Future |

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
      "requirement_id": "BRD-CAP-INDEX-R020",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "7384742eba405f75cce97a14988c1d2fb87bad7f294899adb0d42aa06b6e2bbd"
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
        "BRD-CAP-INDEX-R020-AC001",
        "BRD-CAP-INDEX-R020-AC002",
        "BRD-CAP-INDEX-R020-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R020-O001",
      "obligation_text": "| Capability | Planned Version | | Recommendation Engine | Future |"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "| Capability | Planned Version | | Recommendation Engine | Future |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-020",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "7384742eba405f75cce97a14988c1d2fb87bad7f294899adb0d42aa06b6e2bbd",
    "source_lines": "L2147-L2226",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R020"
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
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R020",
  "title": "| Capability | Planned Version | | Recommendation Engine | Future |",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R021 — | Capability | Planned Version | | Dynamic Pricing Engine | Future |

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R021",
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
  "normative_statement": "| Capability | Planned Version | | Dynamic Pricing Engine | Future |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-021",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "b7b1100b2789b5829c7a4836de1faa813a7ad9336061ea81204be3e85e03411a",
    "source_lines": "L2228-L2288",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R021"
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
  "stable_id": "BRD-CAP-INDEX-R021",
  "title": "| Capability | Planned Version | | Dynamic Pricing Engine | Future |",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R022 — | Capability | Planned Version | | Fraud Detection Platform | Future |

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
      "requirement_id": "BRD-CAP-INDEX-R022",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "7a4b0877ed610f239a894bd6727681def46260e74ab25fc16e1d485ead249ed4"
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
        "BRD-CAP-INDEX-R022-AC001",
        "BRD-CAP-INDEX-R022-AC002",
        "BRD-CAP-INDEX-R022-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R022-O001",
      "obligation_text": "| Capability | Planned Version | | Fraud Detection Platform | Future |"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "| Capability | Planned Version | | Fraud Detection Platform | Future |",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-022",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "7a4b0877ed610f239a894bd6727681def46260e74ab25fc16e1d485ead249ed4",
    "source_lines": "L2290-L2369",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R022"
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
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R022",
  "title": "| Capability | Planned Version | | Fraud Detection Platform | Future |",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R023 — Các Capability trên chưa thuộc phạm vi Version hiện tại nhưng kiến trúc đã được thiết kế mở để h…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-CAP-INDEX-R023",
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
  "normative_statement": "Các Capability trên chưa thuộc phạm vi Version hiện tại nhưng kiến trúc đã được thiết kế mở để hỗ trợ mở rộng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-023",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.18 Future Capability Roadmap",
    "source_context_sha256": "74bbe1636e0ea76e89a41a0d869195feef74ad41cb611b681eb310c34fbb59c3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "20d5a9f9d0296564c9e5fd595860073da26bf07e74d0b5e65f0e47af3bcdbede",
    "source_lines": "L2371-L2431",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R023"
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
  "stable_id": "BRD-CAP-INDEX-R023",
  "title": "Các Capability trên chưa thuộc phạm vi Version hiện tại nhưng kiến trúc đã được thiết kế mở để h…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R024 — Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Architecture Review

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
      "requirement_id": "BRD-CAP-INDEX-R024",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "c00e275caa2a8e86cb16d87602d1bdf54b86e90f73e0e37d0865a516adf7d273"
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
        "BRD-CAP-INDEX-R024-AC001",
        "BRD-CAP-INDEX-R024-AC002",
        "BRD-CAP-INDEX-R024-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R024-O001",
      "obligation_text": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Architecture Review"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Architecture Review",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-024",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Document Status",
    "source_context_sha256": "9ece934b189815153252f6614c5c19e429ae82c14d328f28871377a0d84b467e",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "c00e275caa2a8e86cb16d87602d1bdf54b86e90f73e0e37d0865a516adf7d273",
    "source_lines": "L2433-L2516",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R024"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-CAP-INDEX-R004",
      "CAP-P08"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R024",
  "title": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Architecture Review",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R025 — Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Approval

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "P2-DEC-005",
        "SD-03"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-CAP-INDEX-R025",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "c71e8538d270a6d15ff4dc9319caa56b73a38427829f606e542bada976e0f951"
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
        "BRD-CAP-INDEX-R025-AC001",
        "BRD-CAP-INDEX-R025-AC002",
        "BRD-CAP-INDEX-R025-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R025-O001",
      "obligation_text": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Approval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Approval",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "P2-DEC-005",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-025",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Document Status",
    "source_context_sha256": "9ece934b189815153252f6614c5c19e429ae82c14d328f28871377a0d84b467e",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "c71e8538d270a6d15ff4dc9319caa56b73a38427829f606e542bada976e0f951",
    "source_lines": "L2518-L2605",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R025"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-CAP-INDEX-R004",
      "CAP-P08"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R025",
  "title": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Approval",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R026 — Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Versioning

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
      "requirement_id": "BRD-CAP-INDEX-R026",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "44c670e995afad8e55af5e200ae2d1d219735733dc58691213f255f46d8b8d0e"
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
        "BRD-CAP-INDEX-R026-AC001",
        "BRD-CAP-INDEX-R026-AC002",
        "BRD-CAP-INDEX-R026-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R026-O001",
      "obligation_text": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Versioning",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-026",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Document Status",
    "source_context_sha256": "9ece934b189815153252f6614c5c19e429ae82c14d328f28871377a0d84b467e",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "44c670e995afad8e55af5e200ae2d1d219735733dc58691213f255f46d8b8d0e",
    "source_lines": "L2607-L2690",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R026"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-CAP-INDEX-R004",
      "CAP-P08"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R026",
  "title": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Versioning",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R027 — Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Audit

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
      "requirement_id": "BRD-CAP-INDEX-R027",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "4bea84939a8346a43760067b38a8b7903400b6f1176943d76168fa00b8fc613e"
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
        "BRD-CAP-INDEX-R027-AC001",
        "BRD-CAP-INDEX-R027-AC002",
        "BRD-CAP-INDEX-R027-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R027-O001",
      "obligation_text": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-CAP-INDEX-R027 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-CAP-INDEX-R027 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-CAP-INDEX-R027 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-CAP-INDEX-R027-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-CAP-INDEX-R027-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-CAP-INDEX-R027 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Audit",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-027",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Document Status",
    "source_context_sha256": "9ece934b189815153252f6614c5c19e429ae82c14d328f28871377a0d84b467e",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "4bea84939a8346a43760067b38a8b7903400b6f1176943d76168fa00b8fc613e",
    "source_lines": "L2692-L2808",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R027"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-CAP-INDEX-R004",
      "CAP-P08"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R027",
  "title": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R028 — Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Traceability

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
      "requirement_id": "BRD-CAP-INDEX-R028",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "98066c34673ff401799a8b6cec361fa4195a607c95e519c8362e842f163596ca"
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
        "BRD-CAP-INDEX-R028-AC001",
        "BRD-CAP-INDEX-R028-AC002",
        "BRD-CAP-INDEX-R028-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R028-O001",
      "obligation_text": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Traceability"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Traceability",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-028",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-028",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Document Status",
    "source_context_sha256": "9ece934b189815153252f6614c5c19e429ae82c14d328f28871377a0d84b467e",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "98066c34673ff401799a8b6cec361fa4195a607c95e519c8362e842f163596ca",
    "source_lines": "L2810-L2893",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R028"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-CAP-INDEX-R004",
      "CAP-P08"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R028",
  "title": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Traceability",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R029 — Capability event-role metadata

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
      "requirement_id": "BRD-CAP-INDEX-R029",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "e3dfab15f29513c3b688c2b8b565f17b3b4ad9aa32836e6b55e2dc5abf87fea8"
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
        "BRD-CAP-INDEX-R029-AC001",
        "BRD-CAP-INDEX-R029-AC003",
        "BRD-CAP-INDEX-R029-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R029-O001",
      "obligation_text": "Mỗi Capability phải khai báo event_role là PUBLISHER, SUBSCRIBER, BOTH hoặc NONE cùng published_event_ids và subscribed_event_ids"
    },
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R029-AC002",
        "BRD-CAP-INDEX-R029-AC003",
        "BRD-CAP-INDEX-R029-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R029-O002",
      "obligation_text": "NONE yêu cầu hai danh sách rỗng, các role còn lại yêu cầu danh sách tương ứng không rỗng, và mọi tham chiếu phải trỏ tới Event Registry ID canonical active/approved, không được dùng alias, retired, tombstone hoặc dangling reference"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Capability phải khai báo event_role là PUBLISHER, SUBSCRIBER, BOTH hoặc NONE cùng published_event_ids và subscribed_event_ids; NONE yêu cầu hai danh sách rỗng, các role còn lại yêu cầu danh sách tương ứng không rỗng, và mọi tham chiếu phải trỏ tới Event Registry ID canonical active/approved, không được dùng alias, retired, tombstone hoặc dangling reference.",
  "provenance": {
    "allocation_contract": "P2-ALLOC-001",
    "approved_decision_contracts": {
      "P2-DEC-005": {
        "decision_id": "P2-DEC-005",
        "sections": [
          {
            "heading": "Existing principle",
            "items": [
              "Reclassify CAP-P07 as DESIGN_PRINCIPLE.",
              "CAP-EP-006 remains an alias.",
              "A Capability may be PUBLISHER, SUBSCRIBER, BOTH, or NONE; not every Capability must be event-driven."
            ]
          },
          {
            "heading": "New requirement allocation",
            "items": [
              "Add one V2.3_ACTIVE DATA_REQUIREMENT with reserved stable ID BRD-CAP-INDEX-R029.",
              "Required fields are event_role, published_event_ids, and subscribed_event_ids.",
              "NONE requires both lists to be empty.",
              "PUBLISHER, SUBSCRIBER, and BOTH require the corresponding lists to be non-empty.",
              "Event references resolve to canonical active/approved Event Registry IDs.",
              "Alias, retired, tombstone, and dangling references are prohibited.",
              "Event ownership and schema version remain authoritative in Event Registry.",
              "The new requirement has HIGH verification criticality."
            ]
          }
        ],
        "selected_option": 1,
        "status": "DECIDED_PENDING_PACK_APPROVAL",
        "title": "Capability event role and metadata split"
      }
    },
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "APPROVED_DECISION_CONTRACT",
    "source_context_sha256": "eba829414e616f68141a624b9bc3021d71331d003a4de0be6ca5a914700554b3",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "e3dfab15f29513c3b688c2b8b565f17b3b4ad9aa32836e6b55e2dc5abf87fea8",
    "source_lines": "L2895-L3014",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R029"
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
  "stable_id": "BRD-CAP-INDEX-R029",
  "title": "Capability event-role metadata",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R030 — Nền tảng phải cung cấp Shared Approval Engine dùng chung cho ngoại lệ biên lợi nhuận, hoàn tiền,…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "P2-DEC-005",
        "P2-DEC-010",
        "SD-03",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-CAP-INDEX-R030",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "ed4c8b19e2b159c904c5c4b335dc7dc7c2aba00e6873a3934fd7f5c836180047"
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
        "BRD-CAP-INDEX-R030-AC001",
        "BRD-CAP-INDEX-R030-AC002",
        "BRD-CAP-INDEX-R030-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R030-O001",
      "obligation_text": "Nền tảng phải cung cấp Shared Approval Engine dùng chung cho ngoại lệ biên lợi nhuận, hoàn tiền, cấu hình, thông tin xác thực, ghi đè rủi ro và các nghiệp vụ BRD quy định"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nền tảng phải cung cấp Shared Approval Engine dùng chung cho ngoại lệ biên lợi nhuận, hoàn tiền, cấu hình, thông tin xác thực, ghi đè rủi ro và các nghiệp vụ BRD quy định.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "BDD-27",
      "P2-DEC-005",
      "P2-DEC-010",
      "SD-03",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BRD-CAP-INDEX-R007",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-CAP-INDEX-R030",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.17 Cross Platform Capabilities",
    "source_context_sha256": "0891ca89a0d69d778fae30177c82a932fc6508289c8b09bab6d3c846aa062071",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "ed4c8b19e2b159c904c5c4b335dc7dc7c2aba00e6873a3934fd7f5c836180047",
    "source_fingerprint_before_c3": "ed4c8b19e2b159c904c5c4b335dc7dc7c2aba00e6873a3934fd7f5c836180047",
    "source_lines": "L3016-L3119",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R030"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-CAP-INDEX-R007"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-CAP-INDEX-R007"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R030",
  "title": "Nền tảng phải cung cấp Shared Approval Engine dùng chung cho ngoại lệ biên lợi nhuận, hoàn tiền,…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R031 — engine phải hỗ trợ policy, phân giải người duyệt, phân tách nhiệm vụ, hết hạn, escalation, deleg…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "P2-DEC-005",
        "P2-DEC-010",
        "SD-03",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-CAP-INDEX-R031",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "33b966aa13b121b8e3b50639249213c7dcd314ecd8a1ba42e0fe917e0bf04186"
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
        "BRD-CAP-INDEX-R031-AC001",
        "BRD-CAP-INDEX-R031-AC002",
        "BRD-CAP-INDEX-R031-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R031-O001",
      "obligation_text": "engine phải hỗ trợ policy, phân giải người duyệt, phân tách nhiệm vụ, hết hạn, escalation, delegation, evidence và immutable audit, đồng thời không được diễn giải thành general-purpose BPM workflow engine"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "engine phải hỗ trợ policy, phân giải người duyệt, phân tách nhiệm vụ, hết hạn, escalation, delegation, evidence và immutable audit, đồng thời không được diễn giải thành general-purpose BPM workflow engine.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "BDD-27",
      "P2-DEC-005",
      "P2-DEC-010",
      "SD-03",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BRD-CAP-INDEX-R007",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-CAP-INDEX-R031",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.17 Cross Platform Capabilities",
    "source_context_sha256": "0891ca89a0d69d778fae30177c82a932fc6508289c8b09bab6d3c846aa062071",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "33b966aa13b121b8e3b50639249213c7dcd314ecd8a1ba42e0fe917e0bf04186",
    "source_fingerprint_before_c3": "33b966aa13b121b8e3b50639249213c7dcd314ecd8a1ba42e0fe917e0bf04186",
    "source_lines": "L3121-L3224",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-CAP-INDEX-R031"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-CAP-INDEX-R007"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-CAP-INDEX-R007"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R031",
  "title": "engine phải hỗ trợ policy, phân giải người duyệt, phân tách nhiệm vụ, hết hạn, escalation, deleg…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-EP-001 — Capability phản ánh năng lực của Platform

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
      "requirement_id": "CAP-EP-001",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "06809dd4c0b3be7ebc97916110c9c4ec69c55bc2a0662f983009e574bea3a208"
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
        "CAP-EP-001-AC001",
        "CAP-EP-001-AC002",
        "CAP-EP-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-EP-001-O001",
      "obligation_text": "Capability phản ánh năng lực của Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability phản ánh năng lực của Platform.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-EP-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-EP-001",
    "source_context_sha256": "3e6145672a9c9ff62eab891bf3989b79be3e49bd122c4ea31a8e8755eb1c66fe",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "06809dd4c0b3be7ebc97916110c9c4ec69c55bc2a0662f983009e574bea3a208",
    "source_lines": "L3226-L3305",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-EP-001"
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
  "stable_id": "CAP-EP-001",
  "title": "Capability phản ánh năng lực của Platform",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-EP-002 — Capability độc lập với UI

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
      "requirement_id": "CAP-EP-002",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "e5bda0f59020d011d2593275f0f59d2e011964b5140fe7ee51403bccfb0606bd"
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
        "CAP-EP-002-AC001",
        "CAP-EP-002-AC002",
        "CAP-EP-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-EP-002-O001",
      "obligation_text": "Capability độc lập với UI"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability độc lập với UI.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-EP-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-EP-002",
    "source_context_sha256": "2734a06e7ed581744053b3dcb461df8ffff2cf9e282d083509e67af6d7f3fbfa",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "e5bda0f59020d011d2593275f0f59d2e011964b5140fe7ee51403bccfb0606bd",
    "source_lines": "L3307-L3386",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-EP-002"
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
  "stable_id": "CAP-EP-002",
  "title": "Capability độc lập với UI",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-EP-003 — Capability độc lập với Database

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
      "requirement_id": "CAP-EP-003",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "1fe801e9ac1cf05b6fe686b5e23fbed7e93342462a3401f60b44ff447f1a6ad1"
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
        "CAP-EP-003-AC001",
        "CAP-EP-003-AC002",
        "CAP-EP-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-EP-003-O001",
      "obligation_text": "Capability độc lập với Database"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability độc lập với Database.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-EP-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-EP-003",
    "source_context_sha256": "5b5662d1e663ede7bb4acb9ec63d1aa881bb0b648443b8980140f6533853b5a2",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "1fe801e9ac1cf05b6fe686b5e23fbed7e93342462a3401f60b44ff447f1a6ad1",
    "source_lines": "L3388-L3467",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-EP-003"
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
  "stable_id": "CAP-EP-003",
  "title": "Capability độc lập với Database",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-EP-004 — Capability độc lập với Source Code

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
      "requirement_id": "CAP-EP-004",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "4723d4ff2ee07475c53b36ab9ac92cfb9d047bf21d0d96631020ed22bc65db72"
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
        "CAP-EP-004-AC001",
        "CAP-EP-004-AC002",
        "CAP-EP-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-EP-004-O001",
      "obligation_text": "Capability độc lập với Source Code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability độc lập với Source Code.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-EP-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-EP-004",
    "source_context_sha256": "9d4208033298d5860ee6dbc46f7f428f8d4bc294ee33a651e965c86a1c4ff770",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "4723d4ff2ee07475c53b36ab9ac92cfb9d047bf21d0d96631020ed22bc65db72",
    "source_lines": "L3469-L3548",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-EP-004"
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
  "stable_id": "CAP-EP-004",
  "title": "Capability độc lập với Source Code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-EP-005 — Capability được cấu hình thay vì Hard-code khi phù hợp

```json
{
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "CAP-EP-005 is a supporting alias of canonical requirement CAP-P04.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability được cấu hình thay vì Hard-code khi phù hợp.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-EP-005",
    "phase_2c_c3_actions": [
      "C3_APPROVED_ALIAS_RECONCILIATION"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-EP-005",
    "source_context_sha256": "a49edc659b98ae60562e2aa8a6cb63a02d140c7a1b40dfb2156b2c2a5529bdc4",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "c5ce1d197dc4da4177fc1ff06866b18f264f497339c5987f629c63e1d36c0305",
    "source_fingerprint_before_c3": "e12f103e5d7d88502bc54bc8fa15f87a8913401c441f5929e374d380632390e2",
    "source_lines": "L3550-L3607",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-EP-005"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "CAP-P04",
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "CAP-EP-005",
  "title": "Capability được cấu hình thay vì Hard-code khi phù hợp",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-EP-006 — Capability có thể Publish hoặc Subscribe Business Event

```json
{
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "Alias evidence is inherited from the canonical target; the alias is not an acceptance unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability có thể Publish hoặc Subscribe Business Event.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-EP-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-P07 — Event Driven",
    "source_context_sha256": "44eec2d66aefc3111920af21ae86a614459abefc269240cee0153efdd07ba547",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "4ea7ce824c8da6953ea4e3b7c6e918065ce4be846a5716b07cd6ed2981ca6811",
    "source_lines": "L3609-L3659",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-EP-006"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "CAP-P07",
    "aliases": [],
    "coverage_mode": "CANONICAL",
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "CAP-EP-006",
  "title": "Capability có thể Publish hoặc Subscribe Business Event",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-EP-007 — Capability hỗ trợ Multi-tenant

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
      "requirement_id": "CAP-EP-007",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "babac978b9674bd19d0ab2823328e404fddbbbfa664ac0c85f6ccc3ba9060d1b"
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
        "CAP-EP-007-AC001",
        "CAP-EP-007-AC002",
        "CAP-EP-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-EP-007-O001",
      "obligation_text": "Capability hỗ trợ Multi-tenant"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability hỗ trợ Multi-tenant.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-EP-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-EP-007",
    "source_context_sha256": "490e82c93dd7092f85f7da431e770d935b88cd50c418698187ab49a6152e7b1a",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "babac978b9674bd19d0ab2823328e404fddbbbfa664ac0c85f6ccc3ba9060d1b",
    "source_lines": "L3661-L3740",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-EP-007"
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
  "stable_id": "CAP-EP-007",
  "title": "Capability hỗ trợ Multi-tenant",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-EP-008 — Capability hỗ trợ White-label

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
      "requirement_id": "CAP-EP-008",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "359637685d88e62668a0df656a7de2df72f692307eb1299cb8d18b5113d34f2f"
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
        "CAP-EP-008-AC001",
        "CAP-EP-008-AC002",
        "CAP-EP-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-EP-008-O001",
      "obligation_text": "Capability hỗ trợ White-label"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability hỗ trợ White-label.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-EP-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-EP-008",
    "source_context_sha256": "ca20d0a76fbac4218eec5a2d58d6cc27806d671620e79687092968aab0ab41dd",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "359637685d88e62668a0df656a7de2df72f692307eb1299cb8d18b5113d34f2f",
    "source_lines": "L3742-L3821",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-EP-008"
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
  "stable_id": "CAP-EP-008",
  "title": "Capability hỗ trợ White-label",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-EP-009 — Capability hỗ trợ mở rộng theo Version

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
      "requirement_id": "CAP-EP-009",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "77e665cc022a6340bad78caa84f2f0a871be712ad59734d7b62d38d45388cf19"
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
        "CAP-EP-009-AC001",
        "CAP-EP-009-AC002",
        "CAP-EP-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-EP-009-O001",
      "obligation_text": "Capability hỗ trợ mở rộng theo Version"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability hỗ trợ mở rộng theo Version.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-EP-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-EP-009",
    "source_context_sha256": "2358662a1d2f1225b575dfb028ea24150183b7437784118a29242e6974ba29f7",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "77e665cc022a6340bad78caa84f2f0a871be712ad59734d7b62d38d45388cf19",
    "source_lines": "L3823-L3902",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-EP-009"
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
  "stable_id": "CAP-EP-009",
  "title": "Capability hỗ trợ mở rộng theo Version",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-EP-010 — Capability Registry là Enterprise Capability Dictionary của YSim

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
      "requirement_id": "CAP-EP-010",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "a1830ebf26eb8bfe5c45f0f1f1dad61800415358c28aafc41b86ef7cf0ee173c"
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
        "CAP-EP-010-AC001",
        "CAP-EP-010-AC002",
        "CAP-EP-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-EP-010-O001",
      "obligation_text": "Capability Registry là Enterprise Capability Dictionary của YSim"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability Registry là Enterprise Capability Dictionary của YSim.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-EP-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-EP-010",
    "source_context_sha256": "1d58ace3f4de94c4d8bce052260e4434c063d25690f2414ab96bc805264e5cea",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "a1830ebf26eb8bfe5c45f0f1f1dad61800415358c28aafc41b86ef7cf0ee173c",
    "source_lines": "L3904-L3983",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-EP-010"
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
  "stable_id": "CAP-EP-010",
  "title": "Capability Registry là Enterprise Capability Dictionary của YSim",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-P01 — Capability phản ánh năng lực nghiệp vụ hoặc nền tảng. Không phản ánh thiết kế kỹ thuật

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
      "requirement_id": "CAP-P01",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "30d6891210ecbcedea50586e0b3b473c4e62041f0654db7f2d535fd233d8abf1"
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
        "CAP-P01-AC001",
        "CAP-P01-AC003",
        "CAP-P01-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P01-O001",
      "obligation_text": "Capability phản ánh năng lực nghiệp vụ hoặc nền tảng"
    },
    {
      "acceptance_criterion_references": [
        "CAP-P01-AC002",
        "CAP-P01-AC003",
        "CAP-P01-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P01-O002",
      "obligation_text": "Không phản ánh thiết kế kỹ thuật"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability phản ánh năng lực nghiệp vụ hoặc nền tảng. Không phản ánh thiết kế kỹ thuật.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-P01",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-P01 — Business First",
    "source_context_sha256": "51fb4683695d7f4ac5174988b5e7ea3493b6d947bb8cf32fea0ba343b127f5db",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "30d6891210ecbcedea50586e0b3b473c4e62041f0654db7f2d535fd233d8abf1",
    "source_lines": "L3985-L4074",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-P01"
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
  "stable_id": "CAP-P01",
  "title": "Capability phản ánh năng lực nghiệp vụ hoặc nền tảng. Không phản ánh thiết kế kỹ thuật",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-P02 — Một Capability chỉ có một định nghĩa duy nhất. Không tồn tại nhiều Capability có cùng ý nghĩa

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
      "requirement_id": "CAP-P02",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "a84ad490a9a4053cdabf7ef0784ad753f798b134e4976c595e7199e0c669d334"
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
        "CAP-P02-AC001",
        "CAP-P02-AC003",
        "CAP-P02-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P02-O001",
      "obligation_text": "Một Capability chỉ có một định nghĩa duy nhất"
    },
    {
      "acceptance_criterion_references": [
        "CAP-P02-AC002",
        "CAP-P02-AC003",
        "CAP-P02-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P02-O002",
      "obligation_text": "Không tồn tại nhiều Capability có cùng ý nghĩa"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Capability chỉ có một định nghĩa duy nhất. Không tồn tại nhiều Capability có cùng ý nghĩa.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-P02",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-P02 — Single Source of Truth",
    "source_context_sha256": "fbe51159eaae0f501e00a9cd8f8370e1ed498d251f52625f6abe6f6b7d8a8cd5",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "a84ad490a9a4053cdabf7ef0784ad753f798b134e4976c595e7199e0c669d334",
    "source_lines": "L4076-L4165",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-P02"
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
  "stable_id": "CAP-P02",
  "title": "Một Capability chỉ có một định nghĩa duy nhất. Không tồn tại nhiều Capability có cùng ý nghĩa",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-P03 — Capability ID là bất biến. Tên Capability có thể được cải tiến nhưng Capability ID không thay đổ…

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
      "requirement_id": "CAP-P03",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "522020e5f3d1792e9530d41892d7f2533f002485eec337c20f4ed1dc9d49b555"
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
        "CAP-P03-AC001",
        "CAP-P03-AC003",
        "CAP-P03-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P03-O001",
      "obligation_text": "Capability ID là bất biến"
    },
    {
      "acceptance_criterion_references": [
        "CAP-P03-AC002",
        "CAP-P03-AC003",
        "CAP-P03-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P03-O002",
      "obligation_text": "Tên Capability có thể được cải tiến nhưng Capability ID không thay đổi"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability ID là bất biến. Tên Capability có thể được cải tiến nhưng Capability ID không thay đổi.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-P03",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-P03 — Stable Identifier",
    "source_context_sha256": "163f01ae79dc2bb5d0305a2dc306a03364e0e855273e922eef970406eeb30458",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "522020e5f3d1792e9530d41892d7f2533f002485eec337c20f4ed1dc9d49b555",
    "source_lines": "L4167-L4256",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-P03"
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
  "stable_id": "CAP-P03",
  "title": "Capability ID là bất biến. Tên Capability có thể được cải tiến nhưng Capability ID không thay đổ…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-P04 — Behavior thay đổi theo Organization, market, channel, jurisdiction, policy hoặc environment phải…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "CAP-P04",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "66c5483200edff50dba147834b59470fbaf9a6954d693a42fd812857a6b0d711"
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
        "CAP-P04-AC001",
        "CAP-P04-AC003",
        "CAP-P04-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P04-O001",
      "obligation_text": "Behavior thay đổi theo Organization, market, channel, jurisdiction, policy hoặc environment phải được cấu hình thay vì hard-code"
    },
    {
      "acceptance_criterion_references": [
        "CAP-P04-AC002",
        "CAP-P04-AC003",
        "CAP-P04-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P04-O002",
      "obligation_text": "Platform invariant và security invariant có thể được thực thi trong code nhưng phải versioned và auditable"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Behavior thay đổi theo Organization, market, channel, jurisdiction, policy hoặc environment phải được cấu hình thay vì hard-code; Platform invariant và security invariant có thể được thực thi trong code nhưng phải versioned và auditable.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-P04",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-P04 — Configurable",
    "source_context_sha256": "0744d7d707849991d9b8e554b141e6a7416698c93ecee566b234efec05ce59d2",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "66c5483200edff50dba147834b59470fbaf9a6954d693a42fd812857a6b0d711",
    "source_fingerprint_before_c3": "e47e67a00e8674339d50ccd391bd3a786c8bac716c74a15d882d7def0275a9e8",
    "source_lines": "L4258-L4355",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-P04"
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
  "stable_id": "CAP-P04",
  "title": "Behavior thay đổi theo Organization, market, channel, jurisdiction, policy hoặc environment phải…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-P05 — Capability có thể được cấp quyền. Permission luôn tham chiếu Capability

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
      "requirement_id": "CAP-P05",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "b444cb615e278f4aba1bcb0a453bd264017ecbb5096ac2f250845c1d2cb85a2e"
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
        "CAP-P05-AC001",
        "CAP-P05-AC003",
        "CAP-P05-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P05-O001",
      "obligation_text": "Capability có thể được cấp quyền"
    },
    {
      "acceptance_criterion_references": [
        "CAP-P05-AC002",
        "CAP-P05-AC003",
        "CAP-P05-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P05-O002",
      "obligation_text": "Permission luôn tham chiếu Capability"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "CAP-P05-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "CAP-P05 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "CAP-P05 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "CAP-P05-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "CAP-P05-AC001",
        "CAP-P05-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "CAP-P05 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability có thể được cấp quyền. Permission luôn tham chiếu Capability.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-P05",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-P05 — Permission Aware",
    "source_context_sha256": "1370d24ced6b172f8c7c40c76fea0c5ec31ec1355ac5ac5335733afdbc326507",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "b444cb615e278f4aba1bcb0a453bd264017ecbb5096ac2f250845c1d2cb85a2e",
    "source_lines": "L4357-L4482",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-P05"
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
  "stable_id": "CAP-P05",
  "title": "Capability có thể được cấp quyền. Permission luôn tham chiếu Capability",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-P06 — Capability có thể được bật hoặc tắt thông qua Feature Flag hoặc Configuration

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Platform or security invariants not declared configurable remain enforced"
    ],
    "concrete_bindings": [
      {
        "configuration_key": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
            "source_type": "SOURCE_LITERAL",
            "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
          },
          "identifier": "CAP-P06.CONFIGURATION_KEY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-CAP-INDEX.md",
            "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
            "source_lines": "L319-L322",
            "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CONFIGURATION_KEY",
            "resolver_id": "RESOLVE.CAP-P06.CAP-P06.CONFIGURATION_KEY",
            "version": "1.0.0"
          },
          "semantic_type": "CONFIGURATION_KEY"
        },
        "configuration_sources": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
            "source_type": "SOURCE_LITERAL",
            "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
          },
          "identifier": "CAP-P06.CONFIGURATION_SOURCES",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-CAP-INDEX.md",
            "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
            "source_lines": "L319-L322",
            "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
            "resolver_id": "RESOLVE.CAP-P06.CAP-P06.CONFIGURATION_SOURCES",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
        },
        "expected_value": {
          "authoritative_source": {
            "allowed_identifiers": [
              "CAP-P06.CANONICAL.CONFIGURATION.VALUE"
            ],
            "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
            "source_type": "SOURCE_LITERAL",
            "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
          },
          "identifier": "CAP-P06.CANONICAL.CONFIGURATION.VALUE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-CAP-INDEX.md",
            "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
            "source_lines": "L319-L322",
            "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "RESOLVE.CAP-P06.CAP-P06.CANONICAL.CONFIGURATION.VALUE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "resolved_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
            "source_type": "SOURCE_LITERAL",
            "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
          },
          "identifier": "CAP-P06.RESOLVED_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-CAP-INDEX.md",
            "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
            "source_lines": "L319-L322",
            "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CONFIGURATION_SOURCE_ID",
            "resolver_id": "RESOLVE.CAP-P06.CAP-P06.RESOLVED_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "CONFIGURATION_SOURCE_ID"
        },
        "source_versions": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                "source_type": "SOURCE_LITERAL",
                "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
              },
              "identifier": "CAP-P06.SOURCE_VERSIONS.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                "source_lines": "L319-L322",
                "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.CAP-P06.CAP-P06.SOURCE_VERSIONS.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          ],
          "origin": {
            "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-CAP-INDEX.md",
            "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
            "source_lines": "L319-L322",
            "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
          },
          "semantic_type": "SET_OF<POLICY_VERSION>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.CAP-P06",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Capability state changes outside governed configuration"
    ],
    "operator_composition": [
      "CONFIGURATION_RESOLVES"
    ],
    "positive_oracle": [
      "Capability state resolves from Feature Flag or Configuration"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-005"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
      "source_lines": "L319-L322",
      "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
          "source_type": "SOURCE_LITERAL",
          "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
        },
        "identifier": "CAP-P06.CAP-P06.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "CAP-P06.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-005"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-CAP-INDEX.md",
          "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
          "source_lines": "L319-L322",
          "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.CAP-P06.CAP-P06.CAP-P06.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "CAP-P06.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.CAPABILITY_ID",
        "FIELD.FEATURE_FLAG",
        "FIELD.CONFIGURATION_VALUE",
        "FIELD.EFFECTIVE_STATE",
        "FIELD.AUTHORIZATION",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "CAP-P06.EVIDENCE.PRODUCER",
      "required_collection_origin": "CAP-P06.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.CAPABILITY_ID",
        "FIELD.FEATURE_FLAG",
        "FIELD.CONFIGURATION_VALUE",
        "FIELD.EFFECTIVE_STATE",
        "FIELD.AUTHORIZATION",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "CAP-P06.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "CAP-P06.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "CAP-P06.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "CAP-P06-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES",
          "evaluator_consumed_bindings": [
            "configuration_key",
            "configuration_sources",
            "expected_value",
            "resolved_source",
            "source_versions"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
              "source_type": "SOURCE_LITERAL",
              "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
            },
            "identifier": "CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-005"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-CAP-INDEX.md",
              "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
              "source_lines": "L319-L322",
              "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.CAP-P06.CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
              "source_type": "SOURCE_LITERAL",
              "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
            },
            "identifier": "CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-005"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-CAP-INDEX.md",
              "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
              "source_lines": "L319-L322",
              "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "RESOLVE.CAP-P06.CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "configuration_key": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                  "source_type": "SOURCE_LITERAL",
                  "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
                },
                "identifier": "CAP-P06.CONFIGURATION_KEY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                  "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                  "source_lines": "L319-L322",
                  "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_KEY",
                  "resolver_id": "RESOLVE.CAP-P06.CAP-P06.CONFIGURATION_KEY",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_KEY"
              },
              "configuration_sources": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                  "source_type": "SOURCE_LITERAL",
                  "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
                },
                "identifier": "CAP-P06.CONFIGURATION_SOURCES",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                  "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                  "source_lines": "L319-L322",
                  "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
                  "resolver_id": "RESOLVE.CAP-P06.CAP-P06.CONFIGURATION_SOURCES",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
              },
              "expected_value": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "CAP-P06.CANONICAL.CONFIGURATION.VALUE"
                  ],
                  "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                  "source_type": "SOURCE_LITERAL",
                  "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
                },
                "identifier": "CAP-P06.CANONICAL.CONFIGURATION.VALUE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                  "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                  "source_lines": "L319-L322",
                  "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.CAP-P06.CAP-P06.CANONICAL.CONFIGURATION.VALUE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "resolved_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                  "source_type": "SOURCE_LITERAL",
                  "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
                },
                "identifier": "CAP-P06.RESOLVED_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                  "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                  "source_lines": "L319-L322",
                  "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_SOURCE_ID",
                  "resolver_id": "RESOLVE.CAP-P06.CAP-P06.RESOLVED_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_SOURCE_ID"
              },
              "source_versions": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                      "source_type": "SOURCE_LITERAL",
                      "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
                    },
                    "identifier": "CAP-P06.SOURCE_VERSIONS.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-005"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                      "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                      "source_lines": "L319-L322",
                      "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "POLICY_VERSION",
                      "resolver_id": "RESOLVE.CAP-P06.CAP-P06.SOURCE_VERSIONS.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "POLICY_VERSION"
                  }
                ],
                "origin": {
                  "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                  "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                  "source_lines": "L319-L322",
                  "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
                },
                "semantic_type": "SET_OF<POLICY_VERSION>"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                  "source_type": "SOURCE_LITERAL",
                  "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
                },
                "identifier": "CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                  "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                  "source_lines": "L319-L322",
                  "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.CAP-P06.CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                  "source_type": "SOURCE_LITERAL",
                  "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
                },
                "identifier": "CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                  "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                  "source_lines": "L319-L322",
                  "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.CAP-P06.CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                "source_type": "SOURCE_LITERAL",
                "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
              },
              "identifier": "CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                "source_lines": "L319-L322",
                "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.CAP-P06.CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "CONFIGURATION_RESOLVES"
          },
          "obligation_id": "CAP-P06-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
              "source_type": "SOURCE_LITERAL",
              "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
            },
            "identifier": "CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-005"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-CAP-INDEX.md",
              "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
              "source_lines": "L319-L322",
              "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "OBSERVE.CAP-P06.CAP-P06.CAP-P06.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "operator_id": "CONFIGURATION_RESOLVES",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "configuration_key": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                "source_type": "SOURCE_LITERAL",
                "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
              },
              "identifier": "CAP-P06.CONFIGURATION_KEY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                "source_lines": "L319-L322",
                "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_KEY",
                "resolver_id": "RESOLVE.CAP-P06.CAP-P06.CONFIGURATION_KEY",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_KEY"
            },
            "configuration_sources": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                "source_type": "SOURCE_LITERAL",
                "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
              },
              "identifier": "CAP-P06.CONFIGURATION_SOURCES",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                "source_lines": "L319-L322",
                "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
                "resolver_id": "RESOLVE.CAP-P06.CAP-P06.CONFIGURATION_SOURCES",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
            },
            "expected_value": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "CAP-P06.CANONICAL.CONFIGURATION.VALUE"
                ],
                "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                "source_type": "SOURCE_LITERAL",
                "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
              },
              "identifier": "CAP-P06.CANONICAL.CONFIGURATION.VALUE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                "source_lines": "L319-L322",
                "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.CAP-P06.CAP-P06.CANONICAL.CONFIGURATION.VALUE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "resolved_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                "source_type": "SOURCE_LITERAL",
                "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
              },
              "identifier": "CAP-P06.RESOLVED_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                "source_lines": "L319-L322",
                "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_SOURCE_ID",
                "resolver_id": "RESOLVE.CAP-P06.CAP-P06.RESOLVED_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_SOURCE_ID"
            },
            "source_versions": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
                    "source_type": "SOURCE_LITERAL",
                    "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
                  },
                  "identifier": "CAP-P06.SOURCE_VERSIONS.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-005"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                    "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                    "source_lines": "L319-L322",
                    "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "POLICY_VERSION",
                    "resolver_id": "RESOLVE.CAP-P06.CAP-P06.SOURCE_VERSIONS.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "POLICY_VERSION"
                }
              ],
              "origin": {
                "origin_id": "CAP-P06.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-CAP-INDEX.md",
                "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
                "source_lines": "L319-L322",
                "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
              },
              "semantic_type": "SET_OF<POLICY_VERSION>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Platform or security invariants not declared configurable remain enforced"
      ],
      "contract_ast_sha256": "96c5f2383f7d307bb0587f747eb4c5507badb0cc4d262b6543be667bc360edc7",
      "contract_id": "P2C.C4.CONTRACT.CAP-P06",
      "criticality": "NORMAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-CAP-INDEX.md#11. Registry Principles > CAP-P06 — Feature Toggle Ready",
            "source_type": "SOURCE_LITERAL",
            "version": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be"
          },
          "identifier": "CAP-P06.CAP-P06.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "CAP-P06.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-CAP-INDEX.md",
            "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
            "source_lines": "L319-L322",
            "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.CAP-P06.CAP-P06.CAP-P06.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "CAP-P06.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.CAPABILITY_ID",
          "FIELD.FEATURE_FLAG",
          "FIELD.CONFIGURATION_VALUE",
          "FIELD.EFFECTIVE_STATE",
          "FIELD.AUTHORIZATION",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "CAP-P06.EVIDENCE.PRODUCER",
        "required_collection_origin": "CAP-P06.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.CAPABILITY_ID",
          "FIELD.FEATURE_FLAG",
          "FIELD.CONFIGURATION_VALUE",
          "FIELD.EFFECTIVE_STATE",
          "FIELD.AUTHORIZATION",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "CAP-P06.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "CAP-P06.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "CAP-P06.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-83E2C5045074474C0CD6",
        "P2C-C4-FX-1E87ED066974A7BE9637",
        "P2C-C4-FX-3903F50772E4294CC3F1"
      ],
      "high_risk_audit_subset": false,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Capability state changes outside governed configuration"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "CAP-P06-O001",
          "obligation_text": "Capability có thể được bật hoặc tắt thông qua Feature Flag hoặc Configuration"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "CAP-P06.O1.1.CONFIGURATION_RESOLVES"
          ],
          "coverage_count": 1,
          "obligation_id": "CAP-P06-O001"
        }
      ],
      "operator_composition": [
        "CONFIGURATION_RESOLVES"
      ],
      "positive_oracles": [
        "Capability state resolves from Feature Flag or Configuration"
      ],
      "preconditions": [
        "The applicable Feature Flag or Configuration and authorization exist"
      ],
      "prohibitions": [
        "Capability state changes outside governed configuration"
      ],
      "requirement_id": "CAP-P06",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-005"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-CAP-INDEX.md",
        "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
        "source_lines": "L319-L322",
        "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
      },
      "source_statement": "Capability có thể được bật hoặc tắt thông qua Feature Flag hoặc Configuration.",
      "surrounding_source_context": "## CAP-P06 — Feature Toggle Ready\n\nCapability có thể được bật hoặc tắt thông qua Feature Flag hoặc Configuration.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.CAP-P06",
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
        "CAP-P06-AC001",
        "CAP-P06-AC002",
        "CAP-P06-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P06-O001",
      "obligation_text": "Capability có thể được bật hoặc tắt thông qua Feature Flag hoặc Configuration"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability có thể được bật hoặc tắt thông qua Feature Flag hoặc Configuration.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-P06",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-P06 — Feature Toggle Ready",
    "source_context_sha256": "1f7d4e9a2cde309199664e4dcae17c6c7f5bde3c0a133eadcb42daf0817bc2df",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "972ff68134fd6bc85eb568b7cbf2d6a77f2053476b5fe4c8bfa5d306738f1591",
    "source_lines": "L4484-L5641",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-P06"
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
  "stable_id": "CAP-P06",
  "title": "Capability có thể được bật hoặc tắt thông qua Feature Flag hoặc Configuration",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-P07 — Capability có thể Publish hoặc Subscribe Business Event

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
      "requirement_id": "CAP-P07",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "4ea7ce824c8da6953ea4e3b7c6e918065ce4be846a5716b07cd6ed2981ca6811"
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
        "CAP-P07-AC001",
        "CAP-P07-AC002",
        "CAP-P07-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P07-O001",
      "obligation_text": "Capability có thể Publish hoặc Subscribe Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability có thể Publish hoặc Subscribe Business Event.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-P07",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-P07 — Event Driven",
    "source_context_sha256": "44eec2d66aefc3111920af21ae86a614459abefc269240cee0153efdd07ba547",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "4ea7ce824c8da6953ea4e3b7c6e918065ce4be846a5716b07cd6ed2981ca6811",
    "source_lines": "L5643-L5724",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-P07"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [
      "CAP-EP-006"
    ],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "CAP-P07",
  "title": "Capability có thể Publish hoặc Subscribe Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-P08 — Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capabil…

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
  "normative_statement": "Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capability mới phải trải qua: - Architecture Review - Approval - Versioning - Audit - Traceability",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "P2-DEC-005",
      "SD-03",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-P08",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-P08 — Enterprise Governance",
    "source_context_sha256": "35497da0abc5b36caf13a933df633cc4f5eb9beba3ee315cbf461fc1dbea0f59",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "7c2cd7f4f85c991d47e0fd7cec9781d5975384d7bb2452c60aca8e87b56585b2",
    "source_fingerprint_before_c3": "89f5d106c0eb1328c31955d5ed7d3a7b72c445aa1b45c3e1d851a63d6239dcc3",
    "source_lines": "L5726-L5791",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-P08"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-CAP-INDEX-R024",
      "BRD-CAP-INDEX-R025",
      "BRD-CAP-INDEX-R026",
      "BRD-CAP-INDEX-R027",
      "BRD-CAP-INDEX-R028"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "CAP-P08",
  "title": "Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capabil…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-R01 — Capability phản ánh năng lực nghiệp vụ. Không phản ánh thiết kế kỹ thuật

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
      "requirement_id": "CAP-R01",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "23252c1f7c3f74ac6cccf3f855a62e6f6be8d30151dc8f220d23c3152f7d179b"
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
        "CAP-R01-AC001",
        "CAP-R01-AC003",
        "CAP-R01-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R01-O001",
      "obligation_text": "Capability phản ánh năng lực nghiệp vụ"
    },
    {
      "acceptance_criterion_references": [
        "CAP-R01-AC002",
        "CAP-R01-AC003",
        "CAP-R01-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R01-O002",
      "obligation_text": "Không phản ánh thiết kế kỹ thuật"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability phản ánh năng lực nghiệp vụ. Không phản ánh thiết kế kỹ thuật.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-R01",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-R01 — Business First",
    "source_context_sha256": "eefeb0dd52a0ba93b71069dd8898bb93aa22c32f52e5af891dc5d539d0a13a8b",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "23252c1f7c3f74ac6cccf3f855a62e6f6be8d30151dc8f220d23c3152f7d179b",
    "source_lines": "L5793-L5882",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-R01"
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
  "stable_id": "CAP-R01",
  "title": "Capability phản ánh năng lực nghiệp vụ. Không phản ánh thiết kế kỹ thuật",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-R02 — Mỗi Capability phải có ít nhất một Business Object chính

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
      "requirement_id": "CAP-R02",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "c168ede46f651bff16f26169318d60f251ff4b638cac42d026e96969ebfc091a"
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
        "CAP-R02-AC001",
        "CAP-R02-AC002",
        "CAP-R02-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R02-O001",
      "obligation_text": "Mỗi Capability phải có ít nhất một Business Object chính"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Capability phải có ít nhất một Business Object chính.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-R02",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-R02 — Business Object Driven",
    "source_context_sha256": "a3569f8b937228c714efe865dfa14e0efe16669bb9427b11b4213237594620ee",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "c168ede46f651bff16f26169318d60f251ff4b638cac42d026e96969ebfc091a",
    "source_lines": "L5884-L5963",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-R02"
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
  "stable_id": "CAP-R02",
  "title": "Mỗi Capability phải có ít nhất một Business Object chính",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-R03 — Capability ưu tiên Publish hoặc Subscribe Business Event

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
      "requirement_id": "CAP-R03",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "ed92b661bfde5bfaf63b76da7f64eca470b9d77f43c2bc55c11d7f73fba6f181"
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
        "CAP-R03-AC001",
        "CAP-R03-AC002",
        "CAP-R03-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R03-O001",
      "obligation_text": "Capability ưu tiên Publish hoặc Subscribe Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability ưu tiên Publish hoặc Subscribe Business Event.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-R03",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-R03 — Event Driven",
    "source_context_sha256": "e4589443ace4dfc6a56b32ed7426987f64ad009ae541716f9a5542cb91c222f0",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "ed92b661bfde5bfaf63b76da7f64eca470b9d77f43c2bc55c11d7f73fba6f181",
    "source_lines": "L5965-L6044",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-R03"
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
  "stable_id": "CAP-R03",
  "title": "Capability ưu tiên Publish hoặc Subscribe Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-R04 — Capability phải ưu tiên Configuration thay vì Hard-code

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
      "requirement_id": "CAP-R04",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "60dd453ba2c4c16f556872ef7878fcebe331a94b89acae4fec0b04d3d2a912ba"
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
        "CAP-R04-AC001",
        "CAP-R04-AC002",
        "CAP-R04-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R04-O001",
      "obligation_text": "Capability phải ưu tiên Configuration thay vì Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability phải ưu tiên Configuration thay vì Hard-code.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-R04",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-R04 — Configurable",
    "source_context_sha256": "31b179e99cdc1f6cc6855bcf4a7271facbca0f96c1851a71f1bdf5d9656a486d",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "60dd453ba2c4c16f556872ef7878fcebe331a94b89acae4fec0b04d3d2a912ba",
    "source_lines": "L6046-L6125",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-R04"
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
  "stable_id": "CAP-R04",
  "title": "Capability phải ưu tiên Configuration thay vì Hard-code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-R05 — Capability được kiểm soát bởi Permission Model

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
      "requirement_id": "CAP-R05",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "34f652372321754b2dd3e0e9224a2ea01f2a9615a4714f908afb74671531a2e6"
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
        "CAP-R05-AC001",
        "CAP-R05-AC002",
        "CAP-R05-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R05-O001",
      "obligation_text": "Capability được kiểm soát bởi Permission Model"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "CAP-R05-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "CAP-R05 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "CAP-R05 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "CAP-R05-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "CAP-R05-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "CAP-R05 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability được kiểm soát bởi Permission Model.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-R05",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-R05 — Permission Controlled",
    "source_context_sha256": "01f611c0156d77fc36ae56170c75396ffce7a11813d9fb23c4569f8d8402f104",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "34f652372321754b2dd3e0e9224a2ea01f2a9615a4714f908afb74671531a2e6",
    "source_lines": "L6127-L6241",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-R05"
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
  "stable_id": "CAP-R05",
  "title": "Capability được kiểm soát bởi Permission Model",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-R06 — Capability có khả năng bật/tắt thông qua Feature Flag

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
      "requirement_id": "CAP-R06",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "438f6d007806298bbe6c2f7dce618c40a4ce3aebf0aa7671adfd2171a871145e"
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
        "CAP-R06-AC001",
        "CAP-R06-AC002",
        "CAP-R06-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R06-O001",
      "obligation_text": "Capability có khả năng bật/tắt thông qua Feature Flag"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability có khả năng bật/tắt thông qua Feature Flag.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-R06",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-R06 — Feature Toggle Ready",
    "source_context_sha256": "c5b66fdc10fd6900fdf979813c366330ec885afaf32c4572aa437d6b285bdb1d",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "438f6d007806298bbe6c2f7dce618c40a4ce3aebf0aa7671adfd2171a871145e",
    "source_lines": "L6243-L6322",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-R06"
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
  "stable_id": "CAP-R06",
  "title": "Capability có khả năng bật/tắt thông qua Feature Flag",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-R07 — Capability có thể được: - kế thừa từ Parent Organization - Override bởi Organization - giới hạn …

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
      "requirement_id": "CAP-R07",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "source_fingerprint": "895d64d5d78972816f91706e6f818d6e7cf2cc60819b29e70c71e54f23c83bce"
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
        "CAP-R07-AC001",
        "CAP-R07-AC005",
        "CAP-R07-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R07-O001",
      "obligation_text": "Capability có thể được: kế thừa từ Parent Organization"
    },
    {
      "acceptance_criterion_references": [
        "CAP-R07-AC002",
        "CAP-R07-AC005",
        "CAP-R07-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R07-O002",
      "obligation_text": "Capability có thể được: Override bởi Organization"
    },
    {
      "acceptance_criterion_references": [
        "CAP-R07-AC003",
        "CAP-R07-AC005",
        "CAP-R07-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R07-O003",
      "obligation_text": "Capability có thể được: giới hạn theo Commercial Agreement"
    },
    {
      "acceptance_criterion_references": [
        "CAP-R07-AC004",
        "CAP-R07-AC005",
        "CAP-R07-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R07-O004",
      "obligation_text": "Capability có thể được: giới hạn theo Capability Policy"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability có thể được: - kế thừa từ Parent Organization - Override bởi Organization - giới hạn theo Commercial Agreement - giới hạn theo Capability Policy",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-R07",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-R07 — Organization Aware",
    "source_context_sha256": "aa12cf963344a828a81e1b09ca94ebf867fb5f5e278de5219a86b0300b45069b",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "895d64d5d78972816f91706e6f818d6e7cf2cc60819b29e70c71e54f23c83bce",
    "source_lines": "L6324-L6433",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > CAP-R07"
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
  "stable_id": "CAP-R07",
  "title": "Capability có thể được: - kế thừa từ Parent Organization - Override bởi Organization - giới hạn …",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
