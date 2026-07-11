---
document_code: BRD-CAP-INDEX
document_name: Enterprise Business Capability Registry
project: YSim v2.0
document_set: BRD
version: 1.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
---

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