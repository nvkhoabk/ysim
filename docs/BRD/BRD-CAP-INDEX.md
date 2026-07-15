---
document_code: "BRD-CAP-INDEX"
title: "Enterprise Business Capability Registry"
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

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R001 —  Future Capability

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
    "source_lines": "L86",
    "source_section": "3. Scope"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R002-AC001",
      "given": "the applicable business context, actor, and input for Không phải mọi Capability đều khả dụng cho mọi đối tượng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-CAP-INDEX-R002-O001"
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
        "BRD-CAP-INDEX-R002-AC001"
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
    "source_lines": "L206",
    "source_section": "8. Capability Availability"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R003-AC001",
      "given": "the applicable business context, actor, and input for Mỗi Capability được cấp một mã định danh duy nhất",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-CAP-INDEX-R003-O001"
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
        "BRD-CAP-INDEX-R003-AC001"
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
    "source_lines": "L248",
    "source_section": "10. Capability Identifier"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R004-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Capability Registry tuân thủ các nguyên tắc sau",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-CAP-INDEX-R004-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R004-O001",
      "obligation_text": "Capability Registry tuân thủ các nguyên tắc sau"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability Registry tuân thủ các nguyên tắc sau.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-004",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Registry Principles",
    "source_context_sha256": "8cc5c2e64651797bcc871a28877ede5204d2ccf7a34543a1760a30bbc3444294",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "637111fb992fcef4a72f019a72061d027e5f871df94673681ad252e9f7c0f62f",
    "source_lines": "L277",
    "source_section": "11. Registry Principles"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-CAP-INDEX-R004",
  "title": "Capability Registry tuân thủ các nguyên tắc sau",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R005 — | CAP ID | Capability | Level | Main Business Object | Availability | Workshop | | CAP-9001 | En…

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
    "source_fingerprint": "1f14676a199859466da58922e0f2373362eb36b27222ad141199f64cbec14f34",
    "source_lines": "L624",
    "source_section": "13.17 Cross Platform Capabilities"
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
    "source_fingerprint": "76cd430ea66a9718d44677b02703b9acea27f7f5b753f003e7bd52c859cfac75",
    "source_lines": "L625",
    "source_section": "13.17 Cross Platform Capabilities"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R007-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Shared Approval Engine",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-CAP-INDEX-R007-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R007-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Shared Approval Engine",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the prohibited security decision path produces no effective permission or protected-state change, and conformance evidence identifies the attempted bypass",
      "verifies": [
        "BRD-CAP-INDEX-R007-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-CAP-INDEX-R007-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Shared Approval Engine",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-CAP-INDEX-R007-O001",
        "BRD-CAP-INDEX-R007-O002"
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
        "BRD-CAP-INDEX-R007-AC001",
        "BRD-CAP-INDEX-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R007-O001",
      "obligation_text": "Nền tảng phải cung cấp Shared Approval Engine dùng chung cho ngoại lệ biên lợi nhuận, hoàn tiền, cấu hình, thông tin xác thực, ghi đè rủi ro và các nghiệp vụ BRD quy định"
    },
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R007-AC002",
        "BRD-CAP-INDEX-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R007-O002",
      "obligation_text": "engine phải hỗ trợ policy, phân giải người duyệt, phân tách nhiệm vụ, hết hạn, escalation, delegation, evidence và immutable audit, đồng thời không được diễn giải thành general-purpose BPM workflow engine"
    }
  ],
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
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nền tảng phải cung cấp Shared Approval Engine dùng chung cho ngoại lệ biên lợi nhuận, hoàn tiền, cấu hình, thông tin xác thực, ghi đè rủi ro và các nghiệp vụ BRD quy định; engine phải hỗ trợ policy, phân giải người duyệt, phân tách nhiệm vụ, hết hạn, escalation, delegation, evidence và immutable audit, đồng thời không được diễn giải thành general-purpose BPM workflow engine.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "P2-DEC-005",
      "P2-DEC-010",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-CAP-INDEX-007",
    "previous_temporary_key": "TMP-BRD-CAP-INDEX-007",
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.17 Cross Platform Capabilities",
    "source_context_sha256": "0891ca89a0d69d778fae30177c82a932fc6508289c8b09bab6d3c846aa062071",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "906e4dc6c37245c232bdb378483b08e6091f230e370e05810029517652b9f23e",
    "source_lines": "L626",
    "source_section": "13.17 Cross Platform Capabilities"
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
  "stable_id": "BRD-CAP-INDEX-R007",
  "title": "Shared Approval Engine",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-CAP-INDEX-R009 — | Capability | Planned Version | | AI Customer Support | vNext |

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
    "source_fingerprint": "631832afe63d2bb34156326d1405f9af8b3ef8d47ba2203ea445dcea5dd4c34f",
    "source_lines": "L643",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_fingerprint": "d65432338cbc6374926de12ece12c308cf5f8c0b23b745f81357fec7560b0cb3",
    "source_lines": "L644",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_fingerprint": "b197937549196f24cba79676cbbb595a220ccd102c3f282870540674c79f345b",
    "source_lines": "L645",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_fingerprint": "75678ece2a8f04a354f2b9a064363ae0cc1b906284bff348e2a71b8229013d6b",
    "source_lines": "L646",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_fingerprint": "958c6a52881cf19c05bfbd387ce4a3fe3673d3d0256039b8b069645a86d7931e",
    "source_lines": "L647",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_fingerprint": "a11278adea1652f36502f5b60fcd948b8e5eff93c15ee629c6901093f63dfa62",
    "source_lines": "L648",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_fingerprint": "a056cb14ef0db972ac059edc4d6116d50db786dcf12ae5234b293a640744a358",
    "source_lines": "L649",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_fingerprint": "899b2fa7c5cb1fd1b0d8c6a9f2e0434c8140d284b4782224acf386f830aa107b",
    "source_lines": "L650",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_fingerprint": "6c2aa30ed9ce8fe00c01a19a9d985c0ebe4174e459790f50b69b57ecc1602279",
    "source_lines": "L651",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_fingerprint": "aeee5e5977785fbe5ea359da9214d953086aebf39913df2a0d548e8a15d7a1ce",
    "source_lines": "L652",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_fingerprint": "e67e378ced90818c81543e908a798dd46a411413432b5d407c9d688f013ca857",
    "source_lines": "L653",
    "source_section": "13.18 Future Capability Roadmap"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SCOPE_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R020-AC001",
      "given": "the v2.3 capability inventory and conformance evidence for | Capability | Planned Version | | Recommendation Engine | Future |",
      "observable_evidence": "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
      "then": "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
      "verifies": [
        "BRD-CAP-INDEX-R020-O001"
      ],
      "when": "the capability is inspected at the active baseline boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R020-AC001"
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
    "source_fingerprint": "120ce66a06a6bfc55ec92f6c9f64b19839cea2c877d70cbddb348e35e4f93615",
    "source_lines": "L654",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_fingerprint": "5267c7b388bcaf8fc2670d82278c87b387f1da1406a7e646b8eb83a1444aaf10",
    "source_lines": "L655",
    "source_section": "13.18 Future Capability Roadmap"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SCOPE_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R022-AC001",
      "given": "the v2.3 capability inventory and conformance evidence for | Capability | Planned Version | | Fraud Detection Platform | Future |",
      "observable_evidence": "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
      "then": "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
      "verifies": [
        "BRD-CAP-INDEX-R022-O001"
      ],
      "when": "the capability is inspected at the active baseline boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R022-AC001"
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
    "source_fingerprint": "1df8a9c4122e768074a5892234b22a983178a0de8e16e2f1949e35e379d0f48b",
    "source_lines": "L656",
    "source_section": "13.18 Future Capability Roadmap"
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
    "source_lines": "L658",
    "source_section": "13.18 Future Capability Roadmap"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R024-AC001",
      "given": "the applicable business context, actor, and input for Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Architecture Review",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-CAP-INDEX-R024-O001"
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
        "BRD-CAP-INDEX-R024-AC001"
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
    "source_lines": "L935-L937",
    "source_section": "20. Document Status"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R025-AC001",
      "given": "the applicable business context, actor, and input for Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Approval",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-CAP-INDEX-R025-O001"
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
        "BRD-CAP-INDEX-R025-AC001"
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
    "source_fingerprint": "7fac2abf1a40ac727e4766c8d3793fb2300ff941cc1193c16f6a2a7b8c438bb5",
    "source_lines": "L935-L938",
    "source_section": "20. Document Status"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R026-AC001",
      "given": "the applicable business context, actor, and input for Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Versioning",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-CAP-INDEX-R026-O001"
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
        "BRD-CAP-INDEX-R026-AC001"
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
    "source_fingerprint": "e0ae02c66d1e3eac7403539c513a03492ff7a8c876cb6c208b42d389ce3be0c1",
    "source_lines": "L935-L939",
    "source_section": "20. Document Status"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R027-AC001",
      "given": "an operational task within the scope of Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-CAP-INDEX-R027-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-CAP-INDEX-R027-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-CAP-INDEX-R027-O001"
      ],
      "when": "operational verification is performed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R027-AC001",
        "BRD-CAP-INDEX-R027-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R027-O001",
      "obligation_text": "Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-CAP-INDEX-R027 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-CAP-INDEX-R027 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-CAP-INDEX-R027 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-CAP-INDEX-R027 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-CAP-INDEX-R027-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-CAP-INDEX-R027 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "4784389292cc7dc00dfb6526409b317a5b355f13ab6864ae7e7ab429a2d8c9ac",
    "source_lines": "L935-L940",
    "source_section": "20. Document Status"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R028-AC001",
      "given": "the applicable business context, actor, and input for Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Traceability",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-CAP-INDEX-R028-O001"
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
        "BRD-CAP-INDEX-R028-AC001"
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
    "source_fingerprint": "d3b25203a743c72f87b6019cdf53714b71d7cc8dc8829dde92c8ad26d688e046",
    "source_lines": "L935-L941",
    "source_section": "20. Document Status"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "CAPABILITY_EVENT_ROLE_ENUM_V1",
      "criterion_id": "BRD-CAP-INDEX-R029-AC001",
      "given": "a Capability metadata candidate",
      "observable_evidence": "submitted value and enum-validation result",
      "then": "only PUBLISHER, SUBSCRIBER, BOTH, or NONE is accepted",
      "verifies": [
        "BRD-CAP-INDEX-R029-O001"
      ],
      "when": "event_role is validated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "CAPABILITY_EVENT_ROLE_LIST_MATRIX_V1",
      "criterion_id": "BRD-CAP-INDEX-R029-AC002",
      "given": "Capability metadata for each supported event role",
      "observable_evidence": "event_role, both submitted lists, and field-level validation results",
      "then": "NONE accepts only two empty lists; PUBLISHER, SUBSCRIBER, and BOTH accept only the corresponding required non-empty lists",
      "verifies": [
        "BRD-CAP-INDEX-R029-O002",
        "BRD-CAP-INDEX-R029-O003",
        "BRD-CAP-INDEX-R029-O004",
        "BRD-CAP-INDEX-R029-O005"
      ],
      "when": "role/list consistency is validated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "CAPABILITY_EVENT_ROLE_LIST_MATRIX_V1",
      "criterion_id": "BRD-CAP-INDEX-R029-AC003",
      "given": "NONE with at least one non-empty event list",
      "observable_evidence": "rejection reason, submitted lists, and absence of persisted inconsistent state",
      "then": "the record is rejected and neither inconsistent list is persisted",
      "verifies": [
        "BRD-CAP-INDEX-R029-O002"
      ],
      "when": "the metadata is submitted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "CAPABILITY_EVENT_ROLE_LIST_MATRIX_V1",
      "criterion_id": "BRD-CAP-INDEX-R029-AC004",
      "given": "PUBLISHER, SUBSCRIBER, or BOTH with a missing corresponding list",
      "observable_evidence": "role, submitted lists, missing-list reason, and rejected persistence outcome",
      "then": "the record is rejected with the missing required list identified",
      "verifies": [
        "BRD-CAP-INDEX-R029-O003",
        "BRD-CAP-INDEX-R029-O004",
        "BRD-CAP-INDEX-R029-O005"
      ],
      "when": "the metadata is submitted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "CANONICAL_EVENT_REFERENCE_VALIDATION_V1",
      "criterion_id": "BRD-CAP-INDEX-R029-AC005",
      "given": "an event list containing an alias, retired, tombstone, unknown, or dangling Event ID",
      "observable_evidence": "submitted IDs, canonical-resolution result, reference status, and rejection outcome",
      "then": "the metadata is rejected and every non-canonical reference is identified",
      "verifies": [
        "BRD-CAP-INDEX-R029-O006"
      ],
      "when": "canonical references are resolved"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R029-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R029-O001",
      "obligation_text": "event_role accepts only PUBLISHER, SUBSCRIBER, BOTH, or NONE."
    },
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R029-AC002",
        "BRD-CAP-INDEX-R029-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R029-O002",
      "obligation_text": "NONE requires published_event_ids and subscribed_event_ids to both be empty."
    },
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R029-AC002",
        "BRD-CAP-INDEX-R029-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R029-O003",
      "obligation_text": "PUBLISHER requires published_event_ids to be non-empty."
    },
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R029-AC002",
        "BRD-CAP-INDEX-R029-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R029-O004",
      "obligation_text": "SUBSCRIBER requires subscribed_event_ids to be non-empty."
    },
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R029-AC002",
        "BRD-CAP-INDEX-R029-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R029-O005",
      "obligation_text": "BOTH requires published_event_ids and subscribed_event_ids to both be non-empty."
    },
    {
      "acceptance_criterion_references": [
        "BRD-CAP-INDEX-R029-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-CAP-INDEX-R029-O006",
      "obligation_text": "Every event reference resolves to a canonical active or approved Event Registry ID and rejects alias, retired, tombstone, or dangling IDs."
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
    "source_document": "docs/BRD/BRD-CAP-INDEX.md"
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
### CAP-EP-001 — Capability phản ánh năng lực của Platform

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-EP-001-AC001",
      "given": "the applicable business context, actor, and input for Capability phản ánh năng lực của Platform",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-EP-001-O001"
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
        "CAP-EP-001-AC001"
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
    "source_fingerprint": "5fccf565ad26fb9edcaccbd890dec7122910cd8fc6d9dbad7f73c782339beefb",
    "source_lines": "L867-L870",
    "source_section": "19. Enterprise Capability Principles > CAP-EP-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-EP-002-AC001",
      "given": "the applicable business context, actor, and input for Capability độc lập với UI",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "CAP-EP-002-O001"
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
        "CAP-EP-002-AC001"
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
    "source_fingerprint": "63c609e86bc2cd1fc6097bf11a18956a8ebbff9b7d3d278be71d25e1dc717f18",
    "source_lines": "L873-L876",
    "source_section": "19. Enterprise Capability Principles > CAP-EP-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-EP-003-AC001",
      "given": "the applicable business context, actor, and input for Capability độc lập với Database",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "CAP-EP-003-O001"
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
        "CAP-EP-003-AC001"
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
    "source_fingerprint": "f8adccf6af417c9dfdf78f6764ed4b468d492055ecdca8954da04f2e26dde5e0",
    "source_lines": "L879-L882",
    "source_section": "19. Enterprise Capability Principles > CAP-EP-003"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-EP-004-AC001",
      "given": "the applicable business context, actor, and input for Capability độc lập với Source Code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "CAP-EP-004-O001"
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
        "CAP-EP-004-AC001"
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
    "source_fingerprint": "94eb5225cc850d56ab53ed0a21fed879af29c9c1138261a76c05f88f967b2a2c",
    "source_lines": "L885-L888",
    "source_section": "19. Enterprise Capability Principles > CAP-EP-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-EP-005-AC001",
      "given": "the applicable business context, actor, and input for Capability được cấu hình thay vì Hard-code khi phù hợp",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "CAP-EP-005-O001"
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
        "CAP-EP-005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-EP-005-O001",
      "obligation_text": "Capability được cấu hình thay vì Hard-code khi phù hợp"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability được cấu hình thay vì Hard-code khi phù hợp.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-EP-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-EP-005",
    "source_context_sha256": "a49edc659b98ae60562e2aa8a6cb63a02d140c7a1b40dfb2156b2c2a5529bdc4",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "e12f103e5d7d88502bc54bc8fa15f87a8913401c441f5929e374d380632390e2",
    "source_lines": "L891-L894",
    "source_section": "19. Enterprise Capability Principles > CAP-EP-005"
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
  "stable_id": "CAP-EP-005",
  "title": "Capability được cấu hình thay vì Hard-code khi phù hợp",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-EP-006 — Capability có thể Publish hoặc Subscribe Business Event

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Alias evidence is inherited from the canonical target; the alias is not an acceptance unit.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
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
    "source_fingerprint": "2f3585de3f3c8852d3268e42940a7c59481d4c8b3a9e9fd11bf2d6ceebb04ad7",
    "source_lines": "L897-L900",
    "source_section": "19. Enterprise Capability Principles > CAP-EP-006"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-EP-007-AC001",
      "given": "the applicable business context, actor, and input for Capability hỗ trợ Multi-tenant",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-EP-007-O001"
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
        "CAP-EP-007-AC001"
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
    "source_fingerprint": "a2e58eeeab0bcf038c74ffe0aab0c060adfff197b4a8007bd7bc326187e4f6ef",
    "source_lines": "L903-L906",
    "source_section": "19. Enterprise Capability Principles > CAP-EP-007"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-EP-008-AC001",
      "given": "the applicable business context, actor, and input for Capability hỗ trợ White-label",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-EP-008-O001"
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
        "CAP-EP-008-AC001"
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
    "source_fingerprint": "aa54d38f72567432854ac7ac57a5c94913f92c2aae177e0e45f456499a04cd43",
    "source_lines": "L909-L912",
    "source_section": "19. Enterprise Capability Principles > CAP-EP-008"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-EP-009-AC001",
      "given": "the applicable business context, actor, and input for Capability hỗ trợ mở rộng theo Version",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-EP-009-O001"
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
        "CAP-EP-009-AC001"
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
    "source_fingerprint": "b093231f7874deec20b8e130173991c6fa1474c218231466fb7c39df114af31a",
    "source_lines": "L915-L918",
    "source_section": "19. Enterprise Capability Principles > CAP-EP-009"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-EP-010-AC001",
      "given": "the applicable business context, actor, and input for Capability Registry là Enterprise Capability Dictionary của YSim",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-EP-010-O001"
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
        "CAP-EP-010-AC001"
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
    "source_fingerprint": "7ef3cd4a1006463eb052476b4e6e5c142fd75f6e849a3b627dab06e907268074",
    "source_lines": "L921-L924",
    "source_section": "19. Enterprise Capability Principles > CAP-EP-010"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P01-AC001",
      "given": "the applicable business context, actor, and input for Capability phản ánh năng lực nghiệp vụ hoặc nền tảng. Không phản ánh thiết kế kỹ thuật",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-P01-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P01-AC002",
      "given": "the applicable business context, actor, and input for Capability phản ánh năng lực nghiệp vụ hoặc nền tảng. Không phản ánh thiết kế kỹ thuật",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-P01-O002"
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
        "CAP-P01-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P01-O001",
      "obligation_text": "Capability phản ánh năng lực nghiệp vụ hoặc nền tảng"
    },
    {
      "acceptance_criterion_references": [
        "CAP-P01-AC002"
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
    "source_fingerprint": "c23994f0db41ef0fc5b265f13ef81fbb4be947451574c2a30b22f4690e552dc4",
    "source_lines": "L279-L284",
    "source_section": "11. Registry Principles > CAP-P01 — Business First"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P02-AC001",
      "given": "the applicable business context, actor, and input for Một Capability chỉ có một định nghĩa duy nhất. Không tồn tại nhiều Capability có cùng ý nghĩa",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-P02-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P02-AC002",
      "given": "the applicable business context, actor, and input for Một Capability chỉ có một định nghĩa duy nhất. Không tồn tại nhiều Capability có cùng ý nghĩa",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-P02-O002"
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
        "CAP-P02-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P02-O001",
      "obligation_text": "Một Capability chỉ có một định nghĩa duy nhất"
    },
    {
      "acceptance_criterion_references": [
        "CAP-P02-AC002"
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
    "source_fingerprint": "832a3456804d318ee055820044c38476b4fa7c1562bc8beb87e437d1cc7e453a",
    "source_lines": "L287-L292",
    "source_section": "11. Registry Principles > CAP-P02 — Single Source of Truth"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P03-AC001",
      "given": "the applicable business context, actor, and input for Capability ID là bất biến. Tên Capability có thể được cải tiến nhưng Capability ID không thay đổ…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-P03-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P03-AC002",
      "given": "the applicable business context, actor, and input for Capability ID là bất biến. Tên Capability có thể được cải tiến nhưng Capability ID không thay đổ…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-P03-O002"
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
        "CAP-P03-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P03-O001",
      "obligation_text": "Capability ID là bất biến"
    },
    {
      "acceptance_criterion_references": [
        "CAP-P03-AC002"
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
    "source_fingerprint": "7955f806e402cf89d9ee0995dc2738d7cb64134abe1ff7947bac8bde5e426127",
    "source_lines": "L295-L300",
    "source_section": "11. Registry Principles > CAP-P03 — Stable Identifier"
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
### CAP-P04 — Capability phải có khả năng được cấu hình khi phù hợp. Không Hard-code nếu có thể cấu hình

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P04-AC001",
      "given": "the applicable business context, actor, and input for Capability phải có khả năng được cấu hình khi phù hợp. Không Hard-code nếu có thể cấu hình",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "CAP-P04-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P04-AC002",
      "given": "the applicable business context, actor, and input for Capability phải có khả năng được cấu hình khi phù hợp. Không Hard-code nếu có thể cấu hình",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "CAP-P04-O002"
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
        "CAP-P04-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P04-O001",
      "obligation_text": "Capability phải có khả năng được cấu hình khi phù hợp"
    },
    {
      "acceptance_criterion_references": [
        "CAP-P04-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P04-O002",
      "obligation_text": "Không Hard-code nếu có thể cấu hình"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability phải có khả năng được cấu hình khi phù hợp. Không Hard-code nếu có thể cấu hình.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-P04",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-P04 — Configurable",
    "source_context_sha256": "0744d7d707849991d9b8e554b141e6a7416698c93ecee566b234efec05ce59d2",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "e47e67a00e8674339d50ccd391bd3a786c8bac716c74a15d882d7def0275a9e8",
    "source_lines": "L303-L308",
    "source_section": "11. Registry Principles > CAP-P04 — Configurable"
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
  "title": "Capability phải có khả năng được cấu hình khi phù hợp. Không Hard-code nếu có thể cấu hình",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-P05 — Capability có thể được cấp quyền. Permission luôn tham chiếu Capability

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "CAP-P05-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Capability có thể được cấp quyền. Permission luôn tham chiếu Capability",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "CAP-P05-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "CAP-P05-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Capability có thể được cấp quyền. Permission luôn tham chiếu Capability",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "CAP-P05-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "CAP-P05-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Capability có thể được cấp quyền. Permission luôn tham chiếu Capability",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "CAP-P05-O001",
        "CAP-P05-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "CAP-P05-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Capability có thể được cấp quyền. Permission luôn tham chiếu Capability",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "CAP-P05-O001",
        "CAP-P05-O002"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "CAP-P05-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Capability có thể được cấp quyền. Permission luôn tham chiếu Capability",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "CAP-P05-O001",
        "CAP-P05-O002"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "CAP-P05-AC001",
        "CAP-P05-AC003",
        "CAP-P05-AC004",
        "CAP-P05-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P05-O001",
      "obligation_text": "Capability có thể được cấp quyền"
    },
    {
      "acceptance_criterion_references": [
        "CAP-P05-AC002",
        "CAP-P05-AC003",
        "CAP-P05-AC004",
        "CAP-P05-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P05-O002",
      "obligation_text": "Permission luôn tham chiếu Capability"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "CAP-P05-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "CAP-P05 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "CAP-P05 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "CAP-P05-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "CAP-P05-AC001",
        "CAP-P05-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "CAP-P05 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "f807de4efd10162add2ab6bdcaae8db41c744b894675e38669a3681bd361793f",
    "source_lines": "L311-L316",
    "source_section": "11. Registry Principles > CAP-P05 — Permission Aware"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P06-AC001",
      "given": "the applicable business context, actor, and input for Capability có thể được bật hoặc tắt thông qua Feature Flag hoặc Configuration",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "CAP-P06-O001"
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
        "CAP-P06-AC001"
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
    "source_fingerprint": "94968e40b2b6c8fadb2219c42becf236b5b31de4097bbfb70dd168eff61220be",
    "source_lines": "L319-L322",
    "source_section": "11. Registry Principles > CAP-P06 — Feature Toggle Ready"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P07-AC001",
      "given": "the applicable business context, actor, and input for Capability có thể Publish hoặc Subscribe Business Event",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-P07-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "CAP-P07-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Capability có thể Publish hoặc Subscribe Business Event",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "CAP-P07-O001"
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
        "CAP-P07-AC001",
        "CAP-P07-AC002"
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
    "source_fingerprint": "d26f3c19eb047b584e02ff4b67bff7fec074e1f83255aebfb57ef04a72c2da4a",
    "source_lines": "L325-L328",
    "source_section": "11. Registry Principles > CAP-P07 — Event Driven"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P08-AC001",
      "given": "an operational task within the scope of Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capabil…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "CAP-P08-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P08-AC002",
      "given": "an operational task within the scope of Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capabil…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "CAP-P08-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P08-AC003",
      "given": "an operational task within the scope of Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capabil…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "CAP-P08-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P08-AC004",
      "given": "an operational task within the scope of Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capabil…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "CAP-P08-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-P08-AC005",
      "given": "an operational task within the scope of Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capabil…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "CAP-P08-O005"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "CAP-P08-AC006",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capabil…",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "CAP-P08-O001",
        "CAP-P08-O002",
        "CAP-P08-O003",
        "CAP-P08-O004",
        "CAP-P08-O005"
      ],
      "when": "operational verification is performed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "CAP-P08-AC001",
        "CAP-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P08-O001",
      "obligation_text": "Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capability mới phải trải qua: Architecture Review."
    },
    {
      "acceptance_criterion_references": [
        "CAP-P08-AC002",
        "CAP-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P08-O002",
      "obligation_text": "Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capability mới phải trải qua: Approval."
    },
    {
      "acceptance_criterion_references": [
        "CAP-P08-AC003",
        "CAP-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P08-O003",
      "obligation_text": "Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capability mới phải trải qua: Versioning."
    },
    {
      "acceptance_criterion_references": [
        "CAP-P08-AC004",
        "CAP-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P08-O004",
      "obligation_text": "Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capability mới phải trải qua: Audit."
    },
    {
      "acceptance_criterion_references": [
        "CAP-P08-AC005",
        "CAP-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-P08-O005",
      "obligation_text": "Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capability mới phải trải qua: Traceability."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "CAP-P08 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "CAP-P08 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "CAP-P08 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "CAP-P08 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "CAP-P08-AC001",
        "CAP-P08-AC002",
        "CAP-P08-AC003",
        "CAP-P08-AC004",
        "CAP-P08-AC005"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "CAP-P08 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capability mới phải trải qua: - Architecture Review - Approval - Versioning - Audit - Traceability",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "P2-DEC-005",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "CAP-P08",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "CAP-P08 — Enterprise Governance",
    "source_context_sha256": "35497da0abc5b36caf13a933df633cc4f5eb9beba3ee315cbf461fc1dbea0f59",
    "source_document": "docs/BRD/BRD-CAP-INDEX.md",
    "source_fingerprint": "89f5d106c0eb1328c31955d5ed7d3a7b72c445aa1b45c3e1d851a63d6239dcc3",
    "source_lines": "L331-L342",
    "source_section": "11. Registry Principles > CAP-P08 — Enterprise Governance"
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
  "stable_id": "CAP-P08",
  "title": "Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capabil…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### CAP-R01 — Capability phản ánh năng lực nghiệp vụ. Không phản ánh thiết kế kỹ thuật

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-R01-AC001",
      "given": "the applicable business context, actor, and input for Capability phản ánh năng lực nghiệp vụ. Không phản ánh thiết kế kỹ thuật",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-R01-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-R01-AC002",
      "given": "the applicable business context, actor, and input for Capability phản ánh năng lực nghiệp vụ. Không phản ánh thiết kế kỹ thuật",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-R01-O002"
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
        "CAP-R01-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R01-O001",
      "obligation_text": "Capability phản ánh năng lực nghiệp vụ"
    },
    {
      "acceptance_criterion_references": [
        "CAP-R01-AC002"
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
    "source_fingerprint": "6f310b30607234455e78d03deb9a17b87e0c919dfd7b3abb84671e655475c207",
    "source_lines": "L723-L728",
    "source_section": "15. Capability Relationship Principles > CAP-R01 — Business First"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "CAP-R02-AC001",
      "given": "a candidate Mỗi Capability phải có ít nhất một Business Object chính record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "CAP-R02-O001"
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
        "CAP-R02-AC001"
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
    "source_fingerprint": "eaf759447e6ad69d0a572d5d3a73be66e3f6c5aad5807a15a3f04659b9d870b6",
    "source_lines": "L731-L734",
    "source_section": "15. Capability Relationship Principles > CAP-R02 — Business Object Driven"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-R03-AC001",
      "given": "the applicable business context, actor, and input for Capability ưu tiên Publish hoặc Subscribe Business Event",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-R03-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "CAP-R03-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Capability ưu tiên Publish hoặc Subscribe Business Event",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "CAP-R03-O001"
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
        "CAP-R03-AC001",
        "CAP-R03-AC002"
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
    "source_fingerprint": "0c7d9c85ca095abb08fc4c43660bdbbaa6f35c3d472c174987dbaee5d1854a78",
    "source_lines": "L737-L740",
    "source_section": "15. Capability Relationship Principles > CAP-R03 — Event Driven"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-R04-AC001",
      "given": "the applicable business context, actor, and input for Capability phải ưu tiên Configuration thay vì Hard-code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "CAP-R04-O001"
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
        "CAP-R04-AC001"
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
    "source_fingerprint": "0eb5f611dde434daa87fc935c6ed5dcbe857dc82908922c48711097d36c0e970",
    "source_lines": "L743-L746",
    "source_section": "15. Capability Relationship Principles > CAP-R04 — Configurable"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "CAP-R05-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Capability được kiểm soát bởi Permission Model",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "CAP-R05-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "CAP-R05-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Capability được kiểm soát bởi Permission Model",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "CAP-R05-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "CAP-R05-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Capability được kiểm soát bởi Permission Model",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "CAP-R05-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "CAP-R05-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Capability được kiểm soát bởi Permission Model",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "CAP-R05-O001"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "CAP-R05-AC001",
        "CAP-R05-AC002",
        "CAP-R05-AC003",
        "CAP-R05-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R05-O001",
      "obligation_text": "Capability được kiểm soát bởi Permission Model"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "CAP-R05-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "CAP-R05 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "CAP-R05 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "CAP-R05-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "CAP-R05-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "CAP-R05 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "f78b9fa93b445776c7dd9f04cb5d110c8e908c9e3b7aa344a19bd99efc3561f9",
    "source_lines": "L749-L752",
    "source_section": "15. Capability Relationship Principles > CAP-R05 — Permission Controlled"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-R06-AC001",
      "given": "the applicable business context, actor, and input for Capability có khả năng bật/tắt thông qua Feature Flag",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-R06-O001"
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
        "CAP-R06-AC001"
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
    "source_fingerprint": "f13cd5446a5ba9bb63be694270fca659cc0e2a6cd9d91e0c375cd3cfe7132709",
    "source_lines": "L755-L758",
    "source_section": "15. Capability Relationship Principles > CAP-R06 — Feature Toggle Ready"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-R07-AC001",
      "given": "the applicable business context, actor, and input for Capability có thể được: - kế thừa từ Parent Organization - Override bởi Organization - giới hạn …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-R07-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-R07-AC002",
      "given": "the applicable business context, actor, and input for Capability có thể được: - kế thừa từ Parent Organization - Override bởi Organization - giới hạn …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "an override is accepted only for a policy marked override-eligible, with an explicit reason and the required approval; otherwise the inherited or system policy remains effective",
      "verifies": [
        "CAP-R07-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-R07-AC003",
      "given": "the applicable business context, actor, and input for Capability có thể được: - kế thừa từ Parent Organization - Override bởi Organization - giới hạn …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-R07-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "CAP-R07-AC004",
      "given": "the applicable business context, actor, and input for Capability có thể được: - kế thừa từ Parent Organization - Override bởi Organization - giới hạn …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "CAP-R07-O004"
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
        "CAP-R07-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R07-O001",
      "obligation_text": "Capability có thể được: kế thừa từ Parent Organization."
    },
    {
      "acceptance_criterion_references": [
        "CAP-R07-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R07-O002",
      "obligation_text": "Capability có thể được: Override bởi Organization."
    },
    {
      "acceptance_criterion_references": [
        "CAP-R07-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R07-O003",
      "obligation_text": "Capability có thể được: giới hạn theo Commercial Agreement."
    },
    {
      "acceptance_criterion_references": [
        "CAP-R07-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "CAP-R07-O004",
      "obligation_text": "Capability có thể được: giới hạn theo Capability Policy."
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
    "source_fingerprint": "73fc35ee091988f84ef62a2e13f1db754a05f09d83fad618c7bba59194ce187e",
    "source_lines": "L761-L769",
    "source_section": "15. Capability Relationship Principles > CAP-R07 — Organization Aware"
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
