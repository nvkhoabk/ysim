---
document_code: "BRD-BO-INDEX"
title: "Business Object Registry"
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

# Business Object Registry

## BRD-BO-INDEX

---

# 1. Purpose

Business Object Registry là tài liệu quản lý tập trung toàn bộ **Business Object** của nền tảng YSim.

Tài liệu này đóng vai trò là **Enterprise Registry**, giúp chuẩn hóa:

- Business Vocabulary
- Business Object Naming
- Business Object Ownership
- Business Object Classification
- Business Object Relationship
- Business Object Traceability

Business Object Registry là **Source of Truth** cho toàn bộ hệ thống.

---

# 2. Objectives

Business Object Registry được xây dựng nhằm các mục tiêu sau:

- Chuẩn hóa toàn bộ Business Object trên Platform.
- Tránh trùng lặp hoặc định nghĩa nhiều tên cho cùng một Business Object.
- Làm cơ sở cho Domain Model (DMS).
- Làm cơ sở cho Database Design (DBD).
- Làm cơ sở cho API Specification.
- Làm cơ sở cho System Design Document (SDD).
- Làm cơ sở cho Codex Implementation Prompt (CIP).
- Làm cơ sở cho Enterprise Architecture Governance.

---

# 3. Scope

Business Object Registry bao gồm toàn bộ Business Object thuộc các Business Domain sau:

- Organization
- Customer
- Product
- Commercial
- Promotion
- Order
- Payment
- Procurement
- Inventory
- Fulfillment
- Settlement
- Customer Success
- Communication
- Reporting
- Analytics
- Configuration
- Integration
- Security
- Platform Operations

Ngoài ra còn bao gồm:

- Cross-Domain Objects
- Snapshot Objects
- Policy Objects
- Reference Objects
- Operational Objects

---

# 4. Classification

Business Object được phân loại theo các nhóm sau.

| Type | Description |
|------|-------------|
| Master | Dữ liệu nghiệp vụ chính, tồn tại lâu dài. |
| Reference | Dữ liệu tham chiếu dùng chung toàn hệ thống. |
| Transaction | Dữ liệu phát sinh từ giao dịch nghiệp vụ. |
| Snapshot | Dữ liệu bất biến được chụp tại một thời điểm. |
| Policy | Định nghĩa chính sách nghiệp vụ hoặc vận hành. |
| Configuration | Đối tượng cấu hình của Platform. |
| Integration | Đối tượng phục vụ tích hợp hệ thống. |
| Security | Đối tượng thuộc nền tảng bảo mật. |
| Operational | Đối tượng phục vụ vận hành Platform. |
| Analytics | Đối tượng phục vụ báo cáo và phân tích. |

Mỗi Business Object chỉ thuộc **một loại (Type) chính**, nhưng có thể tham gia nhiều Capability hoặc Workflow khác nhau.

---

# 5. Naming Convention

Business Object phải tuân thủ các quy tắc đặt tên sau:

## 5.1 Business-oriented Naming

Tên phải phản ánh đúng khái niệm nghiệp vụ.

Ví dụ:

- Customer
- Sales Order
- Payment
- Settlement
- Ticket

Không sử dụng tên mang tính kỹ thuật như:

- CustomerEntity
- PaymentDTO
- ProductTable
- OrderModel

---

## 5.2 Singular Form

Tên Business Object sử dụng danh từ số ít.

Ví dụ:

Đúng:

- Customer
- Product
- Payment
- Organization

Không sử dụng:

- Customers
- Products
- Payments

---

## 5.3 Stable Naming

Sau khi Business Object được công bố và sử dụng trong Platform, tên không được thay đổi nếu không có quyết định kiến trúc.

Nếu cần thay đổi phải:

- Review Impact
- Approval
- Versioning
- Traceability

---

## 5.4 Unique Naming

Một Business Object chỉ được tồn tại với một tên duy nhất trong toàn Platform.

Không được phép tồn tại các trường hợp:

- Customer / Client
- Store / Shop
- User Account / Account

cho cùng một khái niệm nghiệp vụ.

---

# 6. Business Object Identifier

Mỗi Business Object được cấp một mã định danh duy nhất.

Quy ước:

```
BO-0001
BO-0002
BO-0003
...
```

Business Object ID được sử dụng trong:

- BRD
- DMS
- DBD
- API
- SDD
- CIP
- Architecture Review

Business Object ID không thay đổi trong suốt vòng đời của Business Object.

---

# 7. Business Object Lifecycle

Không phải mọi Business Object đều có Lifecycle.

Những Business Object có Lifecycle thường tuân theo mô hình:

```text
Draft
    │
    ▼
Active
    │
    ▼
Suspended
    │
    ▼
Archived
```

Một số Business Object đặc biệt như Snapshot hoặc Audit Log là **Immutable Object**, không áp dụng Lifecycle.

Lifecycle cụ thể của từng Business Object được định nghĩa trong DMS.

---

# 8. Registry Principles

Business Object Registry tuân thủ các nguyên tắc sau.

## BO-P01 — Single Source of Truth

Một Business Object chỉ có một định nghĩa duy nhất trên toàn Platform.

---

## BO-P02 — Business First

Business Object phản ánh nghiệp vụ.

Không phản ánh cấu trúc Database hoặc Source Code.

---

## BO-P03 — Domain Ownership

Mỗi Business Object có đúng một Owner Domain.

Owner Domain chịu trách nhiệm quản lý vòng đời và nghiệp vụ của Business Object.

---

## BO-P04 — Cross-Reference

Mỗi Business Object phải có khả năng tham chiếu tới:

- Workshop
- DMS
- DBD
- API
- SDD

để đảm bảo Traceability.

---

## BO-P05 — Stable Identifier

Business Object ID là bất biến.

Tên có thể Version nhưng Business Object ID không thay đổi.

---

## BO-P06 — Platform Consistency

Mọi tài liệu của YSim phải sử dụng đúng Business Object được định nghĩa trong Business Object Registry.

Không được tạo Business Object mới ngoài Registry nếu chưa được Architecture Review.

---

## BO-P07 — Enterprise Governance

Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance.

Mọi thay đổi Business Object đều phải được:

- Review
- Approval
- Versioning
- Audit
- Traceability

---

# 9. Relationship to Other Documents

Business Object Registry là tài liệu trung tâm của toàn bộ bộ tài liệu BRD.

Các tài liệu liên quan bao gồm:

| Document | Relationship |
|----------|--------------|
| BRD Workshop | Nguồn gốc định nghĩa Business Object |
| DMS | Mô hình nghiệp vụ chi tiết |
| DBD | Thiết kế CSDL |
| API Specification | Định nghĩa giao diện tích hợp |
| SDD | Thiết kế kỹ thuật |
| CIP | Hướng dẫn triển khai bằng Codex |

Business Object Registry không thay thế các tài liệu trên mà đóng vai trò là **Enterprise Dictionary** và **Master Registry** cho toàn bộ Platform.

------

# 10. Business Object Registry

## 10.1 Organization Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-0001 | Organization | Master | Yes | No | Yes | WS-03 |
| BO-0002 | Organization Profile | Master | Yes | No | Yes | WS-03 |
| BO-0003 | Organization Relationship | Master | Yes | No | Yes | WS-03 |
| BO-0004 | Organization Capability | Master | Yes | No | Yes | WS-03 |
| BO-0005 | Organization Policy | Policy | Yes | No | Yes | WS-03 |
| BO-0006 | Department | Master | Yes | No | Yes | WS-03 |
| BO-0007 | Team | Master | Yes | No | Yes | WS-03 |
| BO-0008 | User | Master | Yes | No | Yes | WS-03 |
| BO-0009 | User Role Assignment | Transaction | Yes | No | Yes | WS-03 |
| BO-0010 | Storefront | Master | Yes | No | Yes | WS-03 |
| BO-0011 | Storefront Theme | Configuration | Yes | No | Yes | WS-03 |
| BO-0012 | Sales Channel | Master | Yes | No | Yes | WS-03 |
| BO-0013 | Sales Representative | Master | Yes | No | Yes | WS-03 |
| BO-0014 | Affiliate | Master | Yes | No | Yes | WS-03 |
| BO-0015 | Collaborator | Master | Yes | No | Yes | WS-03 |

---

## 10.2 Customer Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-0101 | Customer | Master | Yes | No | Yes | WS-03 |
| BO-0102 | Customer Identity | Master | Yes | No | Yes | WS-03 |
| BO-0103 | Customer Contact Point | Master | Yes | No | Yes | WS-12 |
| BO-0104 | Customer Assignment | Transaction | Yes | Yes | Yes | WS-09 |
| BO-0105 | Customer Portal Account | Master | Yes | No | Yes | WS-11 |
| BO-0106 | Customer Consent | Security | Yes | No | Yes | WS-16 |
| BO-0107 | Customer Preference | Master | Yes | No | Yes | WS-11 |
| BO-0108 | Customer Subscription | Master | Yes | No | Yes | WS-12 |

---

## 10.3 Product Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-0201 | Supplier Product | Master | Yes | No | Yes | WS-04 |
| BO-0202 | Master Product | Master | Yes | No | Yes | WS-04 |
| BO-0203 | Product Category | Reference | Yes | No | Yes | WS-04 |
| BO-0204 | Product Collection | Master | Yes | No | Yes | WS-04 |
| BO-0205 | Product Attribute | Reference | Yes | No | Yes | WS-04 |
| BO-0206 | Product Variant | Master | Yes | No | Yes | WS-04 |
| BO-0207 | Region | Reference | Yes | No | Yes | WS-04 |
| BO-0208 | Country | Reference | Yes | No | Yes | WS-04 |
| BO-0209 | Carrier | Reference | Yes | No | Yes | WS-04 |
| BO-0210 | Destination | Reference | Yes | No | Yes | WS-04 |

---

## 10.4 Commercial Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-0301 | Price Book | Master | Yes | No | Yes | WS-05 |
| BO-0302 | Price Book Version | Master | Yes | No | Yes | WS-05 |
| BO-0303 | Price Change Set | Transaction | Yes | No | Yes | WS-05 |
| BO-0304 | Price Item | Master | Yes | No | Yes | WS-05 |
| BO-0305 | Pricing Formula | Policy | Yes | No | Yes | WS-05 |
| BO-0306 | Commercial Agreement | Master | Yes | No | Yes | WS-05 |
| BO-0307 | Commercial Policy | Policy | Yes | No | Yes | WS-05 |
| BO-0308 | Revenue Sharing Rule | Policy | Yes | No | Yes | WS-05 |
| BO-0309 | Payment Owner | Master | Yes | No | Yes | WS-05 |

---

## 10.5 Promotion Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-0401 | Promotion | Master | Yes | No | Yes | WS-06 |
| BO-0402 | Coupon | Master | Yes | No | Yes | WS-06 |
| BO-0403 | Campaign | Master | Yes | No | Yes | WS-06 |
| BO-0404 | Promotion Rule | Policy | Yes | No | Yes | WS-06 |
| BO-0405 | Promotion Funding | Policy | Yes | No | Yes | WS-06 |
| BO-0406 | Marketing Attribution | Master | Yes | No | Yes | WS-06 |
| BO-0407 | Reference QR | Master | Yes | No | Yes | WS-06 |
| BO-0408 | Promotion QR | Master | Yes | No | Yes | WS-06 |

---

## 10.6 Order Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-0501 | Shopping Cart | Transaction | Yes | No | Yes | WS-07 |
| BO-0502 | Cart Item | Transaction | Yes | No | Yes | WS-07 |
| BO-0503 | Checkout Session | Transaction | Yes | Yes | Yes | WS-07 |
| BO-0504 | Customer Checkout Decision | Transaction | Yes | Yes | Yes | WS-07 |
| BO-0505 | Sales Order | Transaction | Yes | Yes | Yes | WS-07 |
| BO-0506 | Sales Order Item | Transaction | Yes | Yes | Yes | WS-07 |
| BO-0507 | Purchase Order | Transaction | Yes | No | Yes | WS-07 |
| BO-0508 | Purchase Order Item | Transaction | Yes | No | Yes | WS-07 |

---

## 10.7 Payment Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-0601 | Payment Session | Transaction | Yes | Yes | Yes | WS-08 |
| BO-0602 | Payment Attempt | Transaction | Yes | No | Yes | WS-08 |
| BO-0603 | Payment | Transaction | Yes | Yes | Yes | WS-08 |
| BO-0604 | Refund | Transaction | Yes | Yes | Yes | WS-08 |
| BO-0605 | Payment Callback | Integration | Yes | No | Yes | WS-08 |
| BO-0606 | Merchant Account | Master | Yes | No | Yes | WS-08 |
| BO-0607 | Payment Gateway | Integration | Yes | No | Yes | WS-08 |
| BO-0608 | Payment Method | Reference | Yes | No | Yes | WS-08 |

------

## 10.8 Inventory & Fulfillment Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-0701 | Inventory | Master | Yes | No | Yes | WS-09 |
| BO-0702 | Inventory Item | Master | Yes | No | Yes | WS-09 |
| BO-0703 | Inventory Reservation | Transaction | Yes | No | Yes | WS-09 |
| BO-0704 | Inventory Allocation | Transaction | Yes | Yes | Yes | WS-09 |
| BO-0705 | Allocation Policy | Policy | Yes | No | Yes | WS-09 |
| BO-0706 | Fulfillment Session | Transaction | Yes | Yes | Yes | WS-09 |
| BO-0707 | Fulfillment Task | Transaction | Yes | No | Yes | WS-09 |
| BO-0708 | Fulfillment Package | Transaction | Yes | No | Yes | WS-09 |
| BO-0709 | Delivery Channel | Reference | Yes | No | Yes | WS-09 |
| BO-0710 | QR Distribution | Transaction | Yes | No | Yes | WS-09 |
| BO-0711 | Revoked Inventory | Master | Yes | No | Yes | WS-09 |

---

## 10.9 Financial & Settlement Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-0801 | Financial Event | Transaction | No | Yes | Yes | WS-10 |
| BO-0802 | Settlement | Transaction | Yes | Yes | Yes | WS-10 |
| BO-0803 | Settlement Item | Transaction | Yes | Yes | Yes | WS-10 |
| BO-0804 | Settlement Snapshot | Snapshot | No | Yes | No | WS-10 |
| BO-0805 | Commission Snapshot | Snapshot | No | Yes | No | WS-10 |
| BO-0806 | Revenue Recipient | Master | Yes | No | Yes | WS-10 |
| BO-0807 | Financial Account | Master | Yes | No | Yes | WS-10 |
| BO-0808 | Wallet | Transaction | Yes | No | Yes | WS-10 |
| BO-0809 | Ledger Entry | Transaction | No | Yes | Yes | WS-10 |
| BO-0810 | Financial Snapshot | Snapshot | No | Yes | No | WS-10 |

---

## 10.10 Customer Success Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-0901 | Ticket | Transaction | Yes | No | Yes | WS-11 |
| BO-0902 | Ticket Category | Reference | Yes | No | Yes | WS-11 |
| BO-0903 | Support Queue | Master | Yes | No | Yes | WS-11 |
| BO-0904 | Support Policy | Policy | Yes | No | Yes | WS-11 |
| BO-0905 | Knowledge Base Article | Master | Yes | No | Yes | WS-11 |
| BO-0906 | FAQ | Master | Yes | No | Yes | WS-11 |
| BO-0907 | Troubleshooting Guide | Master | Yes | No | Yes | WS-11 |
| BO-0908 | Customer Feedback | Transaction | Yes | No | Yes | WS-11 |
| BO-0909 | Satisfaction Survey | Configuration | Yes | No | Yes | WS-11 |
| BO-0910 | Organization Onboarding Checklist | Configuration | Yes | No | Yes | WS-11 |
| BO-0911 | Feature Request | Transaction | Yes | No | Yes | WS-11 |
| BO-0912 | Supplier Case | Transaction | Yes | No | Yes | WS-11 |

---

## 10.11 Communication Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-1001 | Notification | Transaction | Yes | No | Yes | WS-12 |
| BO-1002 | Notification Event | Transaction | No | No | Yes | WS-12 |
| BO-1003 | Notification Template | Master | Yes | No | Yes | WS-12 |
| BO-1004 | Communication Policy | Policy | Yes | No | Yes | WS-12 |
| BO-1005 | Contact Point | Master | Yes | No | Yes | WS-12 |
| BO-1006 | Communication Log | Operational | No | No | No | WS-12 |
| BO-1007 | Portal Announcement | Transaction | Yes | No | Yes | WS-12 |
| BO-1008 | Personal Inbox Message | Transaction | Yes | No | Yes | WS-12 |
| BO-1009 | Notification Subscription | Master | Yes | No | Yes | WS-12 |

---

## 10.12 Analytics & Reporting Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-1101 | Dashboard | Configuration | Yes | No | Yes | WS-13 |
| BO-1102 | Dashboard Widget | Configuration | Yes | No | Yes | WS-13 |
| BO-1103 | Saved View | Configuration | Yes | No | Yes | WS-13 |
| BO-1104 | Report | Configuration | Yes | No | Yes | WS-13 |
| BO-1105 | Report Template | Master | Yes | No | Yes | WS-13 |
| BO-1106 | Report Schedule | Configuration | Yes | No | Yes | WS-13 |
| BO-1107 | Alert Rule | Configuration | Yes | No | Yes | WS-13 |
| BO-1108 | KPI Definition | Master | Yes | No | Yes | WS-13 |
| BO-1109 | Widget Library | Master | Yes | No | Yes | WS-13 |

---

## 10.13 Platform Configuration Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-1201 | Configuration | Configuration | Yes | No | Yes | WS-14 |
| BO-1202 | Configuration Package | Configuration | Yes | No | Yes | WS-14 |
| BO-1203 | Reference Data | Reference | Yes | No | Yes | WS-14 |
| BO-1204 | Dictionary | Reference | Yes | No | Yes | WS-14 |
| BO-1205 | Business Rule | Policy | Yes | No | Yes | WS-14 |
| BO-1206 | Metadata | Configuration | Yes | No | Yes | WS-14 |
| BO-1207 | Organization Template | Configuration | Yes | No | Yes | WS-14 |

---

## 10.14 Integration Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-1301 | Connector | Integration | Yes | No | Yes | WS-15 |
| BO-1302 | Adapter | Integration | Yes | No | Yes | WS-15 |
| BO-1303 | Business Event | Transaction | No | No | Yes | WS-15 |
| BO-1304 | Callback | Integration | Yes | No | Yes | WS-15 |
| BO-1305 | Queue | Operational | Yes | No | Yes | WS-15 |
| BO-1306 | Connector Policy | Policy | Yes | No | Yes | WS-15 |
| BO-1307 | Connector Routing Rule | Policy | Yes | No | Yes | WS-15 |
| BO-1308 | Canonical Data Model | Reference | Yes | No | Yes | WS-15 |
| BO-1309 | Canonical Event Model | Reference | Yes | No | Yes | WS-15 |
| BO-1310 | Business Service Registry | Master | Yes | No | Yes | WS-15 |

---

## 10.15 Security Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-1401 | Permission | Master | Yes | No | Yes | WS-16 |
| BO-1402 | Security Policy | Policy | Yes | No | Yes | WS-16 |
| BO-1403 | Session | Transaction | Yes | No | Yes | WS-16 |
| BO-1404 | Secret | Security | Yes | No | Yes | WS-16 |
| BO-1405 | Risk Rule | Policy | Yes | No | Yes | WS-16 |
| BO-1406 | Customer Consent | Security | Yes | No | Yes | WS-16 |
| BO-1407 | Data Classification | Reference | Yes | No | Yes | WS-16 |

---

## 10.16 Platform Operations Domain

| BO ID | Business Object | Type | Lifecycle | Snapshot | Publish Event | Workshop |
|--------|-----------------|------|-----------|-----------|---------------|----------|
| BO-1501 | Operation Policy | Policy | Yes | No | Yes | WS-17 |
| BO-1502 | Scheduler Job | Master | Yes | No | Yes | WS-17 |
| BO-1503 | Job Execution | Transaction | Yes | No | Yes | WS-17 |
| BO-1504 | Worker | Operational | Yes | No | Yes | WS-17 |
| BO-1505 | Alert Rule | Configuration | Yes | No | Yes | WS-17 |
| BO-1506 | Alert Event | Transaction | No | No | Yes | WS-17 |
| BO-1507 | Maintenance Window | Master | Yes | No | Yes | WS-17 |
| BO-1508 | Backup Policy | Policy | Yes | No | Yes | WS-17 |
| BO-1509 | Disaster Recovery Policy | Policy | Yes | No | Yes | WS-17 |
| BO-1510 | Capacity Policy | Policy | Yes | No | Yes | WS-17 |
| BO-1511 | Runbook | Master | Yes | No | Yes | WS-17 |
| BO-1512 | Feature Flag | Configuration | Yes | No | Yes | WS-17 |
| BO-1513 | System Health | Operational | No | No | Yes | WS-17 |

---

## 10.17 Cross-Domain Objects

Các Business Object sau được sử dụng xuyên suốt nhiều Business Domain:

| BO ID | Business Object | Type |
|--------|-----------------|------|
| BO-9001 | Audit Log | Operational |
| BO-9002 | Attachment | Master |
| BO-9003 | Localization Resource | Reference |
| BO-9004 | Currency | Reference |
| BO-9005 | Exchange Rate | Reference |
| BO-9006 | Language | Reference |
| BO-9007 | Time Zone | Reference |
| BO-9008 | Country | Reference |
| BO-9009 | Region | Reference |
| BO-9010 | Business Calendar | Reference |

---

## 10.18 Snapshot Objects

Snapshot Objects là các Business Object bất biến (Immutable), được tạo ra tại các thời điểm quan trọng của Business Workflow.

Các Snapshot hiện tại bao gồm:

| BO ID | Business Object |
|--------|-----------------|
| BO-9501 | Pricing Snapshot |
| BO-9502 | Commercial Snapshot |
| BO-9503 | Promotion Snapshot |
| BO-9504 | Order Snapshot |
| BO-9505 | Financial Snapshot |
| BO-9506 | Settlement Snapshot |
| BO-9507 | Commission Snapshot |

Snapshot chỉ được tạo mới, không chỉnh sửa.

---

## 10.19 Policy Objects

Các Policy Objects quản lý hành vi của Platform.

Bao gồm:

| BO ID | Business Object |
|--------|-----------------|
| BO-9801 | Commercial Policy |
| BO-9802 | Pricing Policy |
| BO-9803 | Allocation Policy |
| BO-9804 | Notification Policy |
| BO-9805 | Support Policy |
| BO-9806 | Security Policy |
| BO-9807 | Connector Policy |
| BO-9808 | Operation Policy |
| BO-9809 | Capacity Policy |

Policy được quản lý tập trung và có Versioning.

------

# 11. Business Object Dependency Matrix

Business Object không hoạt động độc lập mà có quan hệ phụ thuộc theo Business Workflow.

Ví dụ:

```text
Organization
        │
        ▼
Storefront
        │
        ▼
Customer
        │
        ▼
Shopping Cart
        │
        ▼
Checkout Session
        │
        ▼
Sales Order
        │
        ▼
Payment
        │
        ▼
Commercial Snapshot
        │
        ▼
Inventory Allocation
        │
        ▼
Purchase Order
        │
        ▼
Inventory Item
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

Business Object Dependency được sử dụng để:

- Impact Analysis
- Architecture Review
- Dependency Validation
- Business Workflow Design

---

# 12. Business Object Relationship Principles

Business Object tuân thủ các nguyên tắc quan hệ sau.

## BO-R01 — Ownership

Mỗi Business Object chỉ có một Owner Domain.

---

## BO-R02 — Reference

Business Object chỉ được tham chiếu thông qua Business Identity.

Không tham chiếu trực tiếp Database Key.

---

## BO-R03 — Immutable Snapshot

Snapshot không được cập nhật.

Snapshot chỉ được tạo mới.

---

## BO-R04 — Event Driven

Business Object Publish Business Event.

Business Object khác Subscribe Business Event.

Không gọi trực tiếp khi không cần thiết.

---

## BO-R05 — Loose Coupling

Business Object giữa các Domain phải giảm phụ thuộc trực tiếp.

Ưu tiên:

- Business Event
- Canonical Model
- Business Service

---

## BO-R06 — Configuration First

Business Object sử dụng Configuration và Policy.

Không Hard-code hành vi nghiệp vụ.

---

# 13. Reference Mapping

Business Object Registry là điểm tham chiếu của toàn bộ tài liệu kiến trúc.

| Document | Purpose |
|----------|---------|
| BRD Workshop | Định nghĩa nghiệp vụ |
| DMS | Domain Model |
| DBD | Database Design |
| API | API Specification |
| SDD | Technical Architecture |
| SATP | Solution Architecture |
| CIP | Implementation Guidance |

Business Object Registry là tài liệu trung tâm kết nối toàn bộ các tài liệu trên.

---

# 14. Business Object Traceability

Mỗi Business Object nên có khả năng Trace tới:

- Business Requirement
- Business Rule
- Business Capability
- Business Event
- Database Entity
- API Contract
- UI Module
- Integration Interface
- Test Case

Ví dụ:

| Business Object | Traceability |
|-----------------|--------------|
| Sales Order | BRD → DMS → DBD → API → UI → Test |
| Payment | BRD → DMS → DBD → API → Gateway → Test |
| Fulfillment Session | BRD → DMS → DBD → Notification → Test |

---

# 15. Business Object Governance

Business Object chỉ được tạo mới khi:

- Có Business Requirement.
- Có Owner Domain.
- Có Business Definition.
- Có Architecture Review.
- Có Approval.

Business Object không được tạo ra chỉ để phục vụ kỹ thuật.

---

# 16. Business Object Statistics

## 16.1 Statistics by Domain

| Domain | Estimated Objects |
|---------|------------------:|
| Organization | 15 |
| Customer | 8 |
| Product | 10 |
| Commercial | 9 |
| Promotion | 8 |
| Order | 8 |
| Payment | 8 |
| Inventory & Fulfillment | 11 |
| Financial & Settlement | 10 |
| Customer Success | 12 |
| Communication | 9 |
| Analytics | 9 |
| Configuration | 7 |
| Integration | 10 |
| Security | 7 |
| Operations | 13 |
| Cross Domain | 10 |

---

## 16.2 Statistics by Type

| Type | Estimated Objects |
|------|------------------:|
| Master | 70+ |
| Transaction | 40+ |
| Configuration | 18+ |
| Policy | 15+ |
| Snapshot | 7+ |
| Integration | 10+ |
| Security | 7+ |
| Operational | 10+ |
| Reference | 18+ |

---

## 16.3 Total

Tổng số Business Object hiện tại:

**Khoảng 220 Business Objects**

Con số này có thể thay đổi trong các phiên bản tiếp theo.

---

# 17. Enterprise Design Principles

## BO-EP-001

Business Object là trung tâm của Enterprise Model.

---

## BO-EP-002

Business Object độc lập với Database.

---

## BO-EP-003

Business Object độc lập với Source Code.

---

## BO-EP-004

Business Object độc lập với UI.

---

## BO-EP-005

Business Object độc lập với Integration Technology.

---

## BO-EP-006

Business Object được sở hữu bởi đúng một Business Domain.

---

## BO-EP-007

Business Object có thể Publish Business Event.

---

## BO-EP-008

Business Object sử dụng Canonical Vocabulary trên toàn Platform.

---

## BO-EP-009

Business Object được quản lý tập trung trong Business Object Registry.

---

## BO-EP-010

Business Object Registry là Enterprise Dictionary của nền tảng YSim.

---

# 18. Future Evolution

Business Object Registry được thiết kế để mở rộng.

Các Business Object dự kiến bổ sung trong các phiên bản sau:

- Loyalty Program
- Loyalty Wallet
- Membership
- Reward Point
- Campaign Attribution
- AI Assistant
- AI Conversation
- Recommendation Engine
- Dynamic Pricing Engine
- Fraud Detection
- Partner Marketplace
- Marketplace Product
- Subscription Billing
- Device Management
- eSIM Activation Status
- Roaming Usage
- Usage Analytics

Business Object ID hiện có sẽ được giữ nguyên.

Business Object mới sẽ được bổ sung theo Version.

---

# 19. Traceability

Business Object Registry được xây dựng dựa trên các Workshop:

- WS-01
- WS-02
- WS-03
- WS-04
- WS-05
- WS-06
- WS-07
- WS-08
- WS-09
- WS-10
- WS-11
- WS-12
- WS-13
- WS-14
- WS-15
- WS-16
- WS-17

Đồng thời là tài liệu tham chiếu chính cho:

- Domain Model Specification (DMS)
- Database Design (DBD)
- API Specification
- System Design Document (SDD)
- Codex Implementation Prompt (CIP)

---

# 20. Document Status

Status:

**FROZEN**

Business Object Registry là tài liệu nền tảng (Foundation Registry) của toàn bộ hệ thống YSim.

Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được:

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
### BO-EP-001 — Business Object là trung tâm của Enterprise Model

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-EP-001-AC001",
      "given": "a candidate Business Object là trung tâm của Enterprise Model record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-EP-001-O001"
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
        "BO-EP-001-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-EP-001-O001",
      "obligation_text": "Business Object là trung tâm của Enterprise Model"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object là trung tâm của Enterprise Model.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-EP-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-EP-001",
    "source_context_sha256": "0e314e546f98395eee16c706d4478b28bd9892202339ddcbdd696c2ecd2d1764",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "4d2d1d1d8ca2ea7044d5e6c5718b3a57d75511da243a349b093223e37b5d3c01",
    "source_lines": "L876-L879",
    "source_section": "17. Enterprise Design Principles > BO-EP-001"
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
  "stable_id": "BO-EP-001",
  "title": "Business Object là trung tâm của Enterprise Model",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-EP-002 — Business Object độc lập với Database

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-EP-002-AC001",
      "given": "a candidate Business Object độc lập với Database record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-EP-002-O001"
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
        "BO-EP-002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-EP-002-O001",
      "obligation_text": "Business Object độc lập với Database"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object độc lập với Database.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-EP-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-EP-002",
    "source_context_sha256": "0a677354937c6066c74abd657fc3cf7a2a2210f48a4ae4247cc46592e2c49a60",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "add7debef814a4c313b2cacb0b1e76902ca7bf4860aac06217a628b698880e25",
    "source_lines": "L882-L885",
    "source_section": "17. Enterprise Design Principles > BO-EP-002"
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
  "stable_id": "BO-EP-002",
  "title": "Business Object độc lập với Database",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-EP-003 — Business Object độc lập với Source Code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-EP-003-AC001",
      "given": "a candidate Business Object độc lập với Source Code record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-EP-003-O001"
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
        "BO-EP-003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-EP-003-O001",
      "obligation_text": "Business Object độc lập với Source Code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object độc lập với Source Code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-EP-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-EP-003",
    "source_context_sha256": "de866e52c65a08d418de487351e86fee0c512231be2f37be097354a2323b8e44",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "a64ebb3dfa9a7fcfcc016b0f2c395c4d13b11fda679bb871a5433e1c098986cf",
    "source_lines": "L888-L891",
    "source_section": "17. Enterprise Design Principles > BO-EP-003"
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
  "stable_id": "BO-EP-003",
  "title": "Business Object độc lập với Source Code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-EP-004 — Business Object độc lập với UI

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-EP-004-AC001",
      "given": "a candidate Business Object độc lập với UI record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-EP-004-O001"
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
        "BO-EP-004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-EP-004-O001",
      "obligation_text": "Business Object độc lập với UI"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object độc lập với UI.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-EP-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-EP-004",
    "source_context_sha256": "30b90d0e5345f0964936377aea5bd4dedb32e671350cddedde307ef2a0758076",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "d68619db23d0f6a22a2b9d8c4d6b9408ec5a99a427e6b81ced8e19a3544b4e6e",
    "source_lines": "L894-L897",
    "source_section": "17. Enterprise Design Principles > BO-EP-004"
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
  "stable_id": "BO-EP-004",
  "title": "Business Object độc lập với UI",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-EP-005 — Business Object độc lập với Integration Technology

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BO-EP-005-AC001",
      "given": "a contract interaction at the integration boundary defined by Business Object độc lập với Integration Technology",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "each boundary object keeps a distinct identity, owner, reference, and lifecycle; changing one does not implicitly mutate the other",
      "verifies": [
        "BO-EP-005-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BO-EP-005-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Business Object độc lập với Integration Technology",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BO-EP-005-O001"
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
        "BO-EP-005-AC001",
        "BO-EP-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-EP-005-O001",
      "obligation_text": "Business Object độc lập với Integration Technology"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object độc lập với Integration Technology.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-EP-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-EP-005",
    "source_context_sha256": "97d06d0d623ad3fc440664ea4c61937de811e64111230b1c93134d5f416d8a2d",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "0c6bb774aa2889f332d40226bbf47db18deff65a858d50c99c7c8f31e2ee64a3",
    "source_lines": "L900-L903",
    "source_section": "17. Enterprise Design Principles > BO-EP-005"
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
  "stable_id": "BO-EP-005",
  "title": "Business Object độc lập với Integration Technology",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-EP-006 — Business Object được sở hữu bởi đúng một Business Domain

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-EP-006-AC001",
      "given": "a candidate Business Object được sở hữu bởi đúng một Business Domain record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-EP-006-O001"
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
        "BO-EP-006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-EP-006-O001",
      "obligation_text": "Business Object được sở hữu bởi đúng một Business Domain"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object được sở hữu bởi đúng một Business Domain.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-EP-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-EP-006",
    "source_context_sha256": "54dc1c289bebd352e936928c2c7f4388d6e6a26b77d724f16c7fbe12068e2dd8",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "c04c736b8088ab2837d37479de786f0ef088509ce5b7a3d7a57a2b5ccdf9cdad",
    "source_lines": "L906-L909",
    "source_section": "17. Enterprise Design Principles > BO-EP-006"
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
  "stable_id": "BO-EP-006",
  "title": "Business Object được sở hữu bởi đúng một Business Domain",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-EP-007 — Business Object có thể Publish Business Event

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-EP-007-AC001",
      "given": "a candidate Business Object có thể Publish Business Event record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-EP-007-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BO-EP-007-AC002",
      "given": "a Business Object có thể Publish Business Event candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BO-EP-007-O001"
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
        "BO-EP-007-AC001",
        "BO-EP-007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-EP-007-O001",
      "obligation_text": "Business Object có thể Publish Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object có thể Publish Business Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-EP-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-EP-007",
    "source_context_sha256": "7ecc65dcbb18b09af290f7ef3795f8311f86ffc2b8ccbabb1e2bee5f82bfa1b4",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "778c3a0c20c5cdd5ab0db4980ad05308ef2e4eaec34ebab2710e75873bde5676",
    "source_lines": "L912-L915",
    "source_section": "17. Enterprise Design Principles > BO-EP-007"
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
  "stable_id": "BO-EP-007",
  "title": "Business Object có thể Publish Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-EP-008 — Business Object sử dụng Canonical Vocabulary trên toàn Platform

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-EP-008-AC001",
      "given": "a candidate Business Object sử dụng Canonical Vocabulary trên toàn Platform record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-EP-008-O001"
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
        "BO-EP-008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-EP-008-O001",
      "obligation_text": "Business Object sử dụng Canonical Vocabulary trên toàn Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object sử dụng Canonical Vocabulary trên toàn Platform.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-EP-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-EP-008",
    "source_context_sha256": "afab05cf606bd7bc29fc9f153a019b329717d68bc5696d4e669defe204779139",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "ef0ef3da9599ccd0fd5a4d8962ed49bde04e0243172ff29c0d4c0e4e8a8c1a3a",
    "source_lines": "L918-L921",
    "source_section": "17. Enterprise Design Principles > BO-EP-008"
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
  "stable_id": "BO-EP-008",
  "title": "Business Object sử dụng Canonical Vocabulary trên toàn Platform",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-EP-009 — Business Object được quản lý tập trung trong Business Object Registry

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-EP-009-AC001",
      "given": "a candidate Business Object được quản lý tập trung trong Business Object Registry record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-EP-009-O001"
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
        "BO-EP-009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-EP-009-O001",
      "obligation_text": "Business Object được quản lý tập trung trong Business Object Registry"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object được quản lý tập trung trong Business Object Registry.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-EP-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-EP-009",
    "source_context_sha256": "fb3bd67777408fc8bc775421132bc53822ceee8ec2063bf2f2f6852a1a70dd84",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "01fc02c5085009ce3c1566013937b474ffdfcd0080acbfee4bdebabe39204b60",
    "source_lines": "L924-L927",
    "source_section": "17. Enterprise Design Principles > BO-EP-009"
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
  "stable_id": "BO-EP-009",
  "title": "Business Object được quản lý tập trung trong Business Object Registry",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-EP-010 — Business Object Registry là Enterprise Dictionary của nền tảng YSim

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-EP-010-AC001",
      "given": "a candidate Business Object Registry là Enterprise Dictionary của nền tảng YSim record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-EP-010-O001"
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
        "BO-EP-010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-EP-010-O001",
      "obligation_text": "Business Object Registry là Enterprise Dictionary của nền tảng YSim"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object Registry là Enterprise Dictionary của nền tảng YSim.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-EP-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-EP-010",
    "source_context_sha256": "5b7cd298fa4cc7b77426983dc1d723b11bd792a0bb214b8f51e695af44103597",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "ed3736324633b75f94d1a2af6cc0ce05917b4b8da695e9b7b1896f578ffd1ae4",
    "source_lines": "L930-L933",
    "source_section": "17. Enterprise Design Principles > BO-EP-010"
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
  "stable_id": "BO-EP-010",
  "title": "Business Object Registry là Enterprise Dictionary của nền tảng YSim",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-P01 — Một Business Object chỉ có một định nghĩa duy nhất trên toàn Platform

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-P01-AC001",
      "given": "a candidate Một Business Object chỉ có một định nghĩa duy nhất trên toàn Platform record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-P01-O001"
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
        "BO-P01-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P01-O001",
      "obligation_text": "Một Business Object chỉ có một định nghĩa duy nhất trên toàn Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Business Object chỉ có một định nghĩa duy nhất trên toàn Platform.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-P01",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-P01 — Single Source of Truth",
    "source_context_sha256": "843f0f9053129815badb6feaa0952e704871b3444e11894085ed66fdb4c86536",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "388aa820051c890b5b6790727c130d645fca730e9eef212e2d77d4d202546edf",
    "source_lines": "L235-L238",
    "source_section": "8. Registry Principles > BO-P01 — Single Source of Truth"
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
  "stable_id": "BO-P01",
  "title": "Một Business Object chỉ có một định nghĩa duy nhất trên toàn Platform",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-P02 — Business Object phản ánh nghiệp vụ. Không phản ánh cấu trúc Database hoặc Source Code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-P02-AC001",
      "given": "a candidate Business Object phản ánh nghiệp vụ. Không phản ánh cấu trúc Database hoặc Source Code record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-P02-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-P02-AC002",
      "given": "a candidate Business Object phản ánh nghiệp vụ. Không phản ánh cấu trúc Database hoặc Source Code record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-P02-O002"
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
        "BO-P02-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P02-O001",
      "obligation_text": "Business Object phản ánh nghiệp vụ"
    },
    {
      "acceptance_criterion_references": [
        "BO-P02-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P02-O002",
      "obligation_text": "Không phản ánh cấu trúc Database hoặc Source Code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object phản ánh nghiệp vụ. Không phản ánh cấu trúc Database hoặc Source Code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-P02",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-P02 — Business First",
    "source_context_sha256": "33e1794f3678c5e34621c96c4ad2e73233c03f3d52c05607a261cbdfdde04358",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "fcf83a758154ec4d43acb69b2ada8f0f5429ccdf27c40fa9b639f4f82ada5202",
    "source_lines": "L241-L246",
    "source_section": "8. Registry Principles > BO-P02 — Business First"
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
  "stable_id": "BO-P02",
  "title": "Business Object phản ánh nghiệp vụ. Không phản ánh cấu trúc Database hoặc Source Code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-P03 — Mỗi Business Object có đúng một Owner Domain. Owner Domain chịu trách nhiệm quản lý vòng đời và …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-P03-AC001",
      "given": "a candidate Mỗi Business Object có đúng một Owner Domain. Owner Domain chịu trách nhiệm quản lý vòng đời và … record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-P03-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-P03-AC002",
      "given": "a candidate Mỗi Business Object có đúng một Owner Domain. Owner Domain chịu trách nhiệm quản lý vòng đời và … record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-P03-O002"
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
        "BO-P03-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P03-O001",
      "obligation_text": "Mỗi Business Object có đúng một Owner Domain"
    },
    {
      "acceptance_criterion_references": [
        "BO-P03-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P03-O002",
      "obligation_text": "Owner Domain chịu trách nhiệm quản lý vòng đời và nghiệp vụ của Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Business Object có đúng một Owner Domain. Owner Domain chịu trách nhiệm quản lý vòng đời và nghiệp vụ của Business Object.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-P03",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-P03 — Domain Ownership",
    "source_context_sha256": "1a607662feb93ed808d935151689f08a5300d32347b5102d0a87968f1ca09562",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "a96f9670ad124d3cba23dbf177958b6011c2db73df04130578c718e63249bded",
    "source_lines": "L249-L254",
    "source_section": "8. Registry Principles > BO-P03 — Domain Ownership"
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
  "stable_id": "BO-P03",
  "title": "Mỗi Business Object có đúng một Owner Domain. Owner Domain chịu trách nhiệm quản lý vòng đời và …",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-P04 — Mỗi Business Object phải có khả năng tham chiếu tới: - Workshop - DMS - DBD - API - SDD để đảm b…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BO-P04-AC001",
      "given": "a contract interaction at the integration boundary defined by Mỗi Business Object phải có khả năng tham chiếu tới: - Workshop - DMS - DBD - API - SDD để đảm b…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BO-P04-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BO-P04-AC002",
      "given": "a contract interaction at the integration boundary defined by Mỗi Business Object phải có khả năng tham chiếu tới: - Workshop - DMS - DBD - API - SDD để đảm b…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BO-P04-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BO-P04-AC003",
      "given": "a contract interaction at the integration boundary defined by Mỗi Business Object phải có khả năng tham chiếu tới: - Workshop - DMS - DBD - API - SDD để đảm b…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BO-P04-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BO-P04-AC004",
      "given": "a contract interaction at the integration boundary defined by Mỗi Business Object phải có khả năng tham chiếu tới: - Workshop - DMS - DBD - API - SDD để đảm b…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BO-P04-O004"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BO-P04-AC005",
      "given": "a contract interaction at the integration boundary defined by Mỗi Business Object phải có khả năng tham chiếu tới: - Workshop - DMS - DBD - API - SDD để đảm b…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BO-P04-O005"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BO-P04-AC006",
      "given": "an interaction that violates the contract or ownership boundary for Mỗi Business Object phải có khả năng tham chiếu tới: - Workshop - DMS - DBD - API - SDD để đảm b…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BO-P04-O001",
        "BO-P04-O002",
        "BO-P04-O003",
        "BO-P04-O004",
        "BO-P04-O005"
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
        "BO-P04-AC001",
        "BO-P04-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P04-O001",
      "obligation_text": "Mỗi Business Object phải có khả năng tham chiếu tới: Workshop."
    },
    {
      "acceptance_criterion_references": [
        "BO-P04-AC002",
        "BO-P04-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P04-O002",
      "obligation_text": "Mỗi Business Object phải có khả năng tham chiếu tới: DMS."
    },
    {
      "acceptance_criterion_references": [
        "BO-P04-AC003",
        "BO-P04-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P04-O003",
      "obligation_text": "Mỗi Business Object phải có khả năng tham chiếu tới: DBD."
    },
    {
      "acceptance_criterion_references": [
        "BO-P04-AC004",
        "BO-P04-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P04-O004",
      "obligation_text": "Mỗi Business Object phải có khả năng tham chiếu tới: API."
    },
    {
      "acceptance_criterion_references": [
        "BO-P04-AC005",
        "BO-P04-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P04-O005",
      "obligation_text": "Mỗi Business Object phải có khả năng tham chiếu tới: SDD để đảm bảo Traceability."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Business Object phải có khả năng tham chiếu tới: - Workshop - DMS - DBD - API - SDD để đảm bảo Traceability.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-P04",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-P04 — Cross-Reference",
    "source_context_sha256": "2b6347dced73cb1287e824f92fa4c8129101365a381e59de3f6825842dbb4906",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "5aaa1576e70fc028db6046fdc35a4fe4d9419eab11a28124fe22ec5d6a795f2c",
    "source_lines": "L257-L268",
    "source_section": "8. Registry Principles > BO-P04 — Cross-Reference"
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
  "stable_id": "BO-P04",
  "title": "Mỗi Business Object phải có khả năng tham chiếu tới: - Workshop - DMS - DBD - API - SDD để đảm b…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-P05 — Business Object ID là bất biến. Tên có thể Version nhưng Business Object ID không thay đổi

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-P05-AC001",
      "given": "a candidate Business Object ID là bất biến. Tên có thể Version nhưng Business Object ID không thay đổi record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-P05-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-P05-AC002",
      "given": "a candidate Business Object ID là bất biến. Tên có thể Version nhưng Business Object ID không thay đổi record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-P05-O002"
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
        "BO-P05-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P05-O001",
      "obligation_text": "Business Object ID là bất biến"
    },
    {
      "acceptance_criterion_references": [
        "BO-P05-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P05-O002",
      "obligation_text": "Tên có thể Version nhưng Business Object ID không thay đổi"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object ID là bất biến. Tên có thể Version nhưng Business Object ID không thay đổi.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-P05",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-P05 — Stable Identifier",
    "source_context_sha256": "5a5cf1b7665b7c21a94f03d3e3dd88c7b87eeac4465b27666ab5915cdd35b68c",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "f78c3a3811508cbfc09d62054c120654dcf831862dac17c6d2538b032091db51",
    "source_lines": "L271-L276",
    "source_section": "8. Registry Principles > BO-P05 — Stable Identifier"
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
  "stable_id": "BO-P05",
  "title": "Business Object ID là bất biến. Tên có thể Version nhưng Business Object ID không thay đổi",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-P06 — Mọi tài liệu của YSim phải sử dụng đúng Business Object được định nghĩa trong Business Object Re…

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Composite parent coverage is satisfied only through ALL_CHILDREN; the parent is not an acceptance unit.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi tài liệu của YSim phải sử dụng đúng Business Object được định nghĩa trong Business Object Registry. Không được tạo Business Object mới ngoài Registry nếu chưa được Architecture Review.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-P06",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-P06 — Platform Consistency",
    "source_context_sha256": "d9020504172b8b99c630c1d44b7429f9481bdb95371466306f8ad7e5928efd70",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "82e126f63111a544dcf2e0d8819554e625f61d10e929ddf33cf5879a2547c7c9",
    "source_lines": "L279-L284",
    "source_section": "8. Registry Principles > BO-P06 — Platform Consistency"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-BO-INDEX-R048",
      "BRD-BO-INDEX-R049"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BO-P06",
  "title": "Mọi tài liệu của YSim phải sử dụng đúng Business Object được định nghĩa trong Business Object Re…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-P07 — Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi th…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BO-P07-AC001",
      "given": "an operational task within the scope of Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi th…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BO-P07-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BO-P07-AC002",
      "given": "an operational task within the scope of Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi th…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BO-P07-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BO-P07-AC003",
      "given": "an operational task within the scope of Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi th…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BO-P07-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BO-P07-AC004",
      "given": "an operational task within the scope of Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi th…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BO-P07-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BO-P07-AC005",
      "given": "an operational task within the scope of Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi th…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BO-P07-O005"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BO-P07-AC006",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi th…",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BO-P07-O001",
        "BO-P07-O002",
        "BO-P07-O003",
        "BO-P07-O004",
        "BO-P07-O005"
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
        "BO-P07-AC001",
        "BO-P07-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P07-O001",
      "obligation_text": "Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi thay đổi Business Object đều phải được: Review."
    },
    {
      "acceptance_criterion_references": [
        "BO-P07-AC002",
        "BO-P07-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P07-O002",
      "obligation_text": "Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi thay đổi Business Object đều phải được: Approval."
    },
    {
      "acceptance_criterion_references": [
        "BO-P07-AC003",
        "BO-P07-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P07-O003",
      "obligation_text": "Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi thay đổi Business Object đều phải được: Versioning."
    },
    {
      "acceptance_criterion_references": [
        "BO-P07-AC004",
        "BO-P07-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P07-O004",
      "obligation_text": "Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi thay đổi Business Object đều phải được: Audit."
    },
    {
      "acceptance_criterion_references": [
        "BO-P07-AC005",
        "BO-P07-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-P07-O005",
      "obligation_text": "Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi thay đổi Business Object đều phải được: Traceability."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BO-P07 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BO-P07 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BO-P07 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BO-P07 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BO-P07-AC001",
        "BO-P07-AC002",
        "BO-P07-AC003",
        "BO-P07-AC004",
        "BO-P07-AC005"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BO-P07 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi thay đổi Business Object đều phải được: - Review - Approval - Versioning - Audit - Traceability",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-P07",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-P07 — Enterprise Governance",
    "source_context_sha256": "f005724cd25296b5b79b0481f59aa74b41b460616c8eff23191681cee08b6139",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "3b85f93bdf5484cd033c7205f0e26dacad3be7faac01d2ec6202cd6974d00554",
    "source_lines": "L287-L298",
    "source_section": "8. Registry Principles > BO-P07 — Enterprise Governance"
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
  "stable_id": "BO-P07",
  "title": "Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi th…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-R01 — Mỗi Business Object chỉ có một Owner Domain

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R01-AC001",
      "given": "a candidate Mỗi Business Object chỉ có một Owner Domain record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R01-O001"
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
        "BO-R01-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R01-O001",
      "obligation_text": "Mỗi Business Object chỉ có một Owner Domain"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Business Object chỉ có một Owner Domain.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-R01",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-R01 — Ownership",
    "source_context_sha256": "426230a303a30683a7d34eb0ee30444cc57dfb4c774ffac171203ebcde5ffc87",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "25690802699ea4bfaf677f56ffdf84dfd9644baa4cb8746a947b1868fdd9e03d",
    "source_lines": "L714-L717",
    "source_section": "12. Business Object Relationship Principles > BO-R01 — Ownership"
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
  "stable_id": "BO-R01",
  "title": "Mỗi Business Object chỉ có một Owner Domain",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-R02 — Business Object chỉ được tham chiếu thông qua Business Identity. Không tham chiếu trực tiếp Data…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R02-AC001",
      "given": "a candidate Business Object chỉ được tham chiếu thông qua Business Identity. Không tham chiếu trực tiếp Data… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R02-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R02-AC002",
      "given": "a candidate Business Object chỉ được tham chiếu thông qua Business Identity. Không tham chiếu trực tiếp Data… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R02-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BO-R02-AC003",
      "given": "a Business Object chỉ được tham chiếu thông qua Business Identity. Không tham chiếu trực tiếp Data… candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BO-R02-O001",
        "BO-R02-O002"
      ],
      "when": "the candidate is validated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BO-R02-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Business Object chỉ được tham chiếu thông qua Business Identity. Không tham chiếu trực tiếp Data…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BO-R02-O001",
        "BO-R02-O002"
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
        "BO-R02-AC001",
        "BO-R02-AC003",
        "BO-R02-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R02-O001",
      "obligation_text": "Business Object chỉ được tham chiếu thông qua Business Identity"
    },
    {
      "acceptance_criterion_references": [
        "BO-R02-AC002",
        "BO-R02-AC003",
        "BO-R02-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R02-O002",
      "obligation_text": "Không tham chiếu trực tiếp Database Key"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BO-R02 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BO-R02 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BO-R02 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BO-R02-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BO-R02-AC001",
        "BO-R02-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BO-R02 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object chỉ được tham chiếu thông qua Business Identity. Không tham chiếu trực tiếp Database Key.",
  "provenance": {
    "approved_decision_contracts": {
      "P2-DEC-008": {
        "decision_id": "P2-DEC-008",
        "sections": [
          {
            "heading": "Cardinality",
            "items": [
              "Identity is a global authentication principal with multiple verified methods.",
              "User is a workforce membership in exactly one Organization.",
              "Each User has exactly one Identity.",
              "There is at most one active User per Identity + Organization.",
              "Multiple roles belong to one User.",
              "Customer is a commercial relationship in exactly one selling Organization.",
              "Customer may temporarily exist without Identity.",
              "Customer links to at most one Identity.",
              "There is at most one active Customer per Identity + Organization.",
              "There is no YSim-wide Customer Portal aggregation."
            ]
          },
          {
            "heading": "Lifecycle and access",
            "items": [
              "User and Customer lifecycles are independent.",
              "A User role does not grant Customer access and Customer status does not grant workforce access.",
              "Disabling/deleting one relationship does not delete the others.",
              "Federation JIT creates User only.",
              "Guest checkout always has email.",
              "Payment-success account provisioning is idempotent.",
              "An existing verified Identity is reused; otherwise a pending-verification Identity is created and a magic link/OTP is sent.",
              "Portal access begins only after identifier control is proven.",
              "Email text matching is not ownership proof.",
              "Linking requires verified control or an audited case-scoped admin action.",
              "A conflict blocks automatic linking and goes to manual resolution.",
              "Destructive Customer merge is outside v2.3.",
              "Manual resolution may select a canonical relationship and correct links but must not silently re-parent financial/order history.",
              "Portal session is bound to Organization/Customer context and fails closed."
            ]
          }
        ],
        "selected_option": 1,
        "status": "DECIDED_PENDING_PACK_APPROVAL",
        "title": "Identity, User, and Customer cardinality and lifecycle"
      }
    },
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-R02",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-R02 — Reference",
    "source_context_sha256": "01c9d8f3c0824244b92d80ea220db8755da2d9ddc77244aed152faeceb2a7d34",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "28f646c666f8788420ffec093a42f8a2dc6ed225332f72a234ebaa710ebc44e5",
    "source_lines": "L720-L725",
    "source_section": "12. Business Object Relationship Principles > BO-R02 — Reference"
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
  "stable_id": "BO-R02",
  "title": "Business Object chỉ được tham chiếu thông qua Business Identity. Không tham chiếu trực tiếp Data…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-R03 — Snapshot không được cập nhật. Snapshot chỉ được tạo mới

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R03-AC001",
      "given": "a candidate Snapshot không được cập nhật. Snapshot chỉ được tạo mới record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns REJECTED when the prohibited value or relationship is present, and no rejected state is persisted",
      "verifies": [
        "BO-R03-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R03-AC002",
      "given": "a candidate Snapshot không được cập nhật. Snapshot chỉ được tạo mới record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R03-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BO-R03-AC003",
      "given": "a Snapshot không được cập nhật. Snapshot chỉ được tạo mới candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BO-R03-O001",
        "BO-R03-O002"
      ],
      "when": "the candidate is validated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BO-R03-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Snapshot không được cập nhật. Snapshot chỉ được tạo mới",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BO-R03-O001",
        "BO-R03-O002"
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
        "BO-R03-AC001",
        "BO-R03-AC003",
        "BO-R03-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R03-O001",
      "obligation_text": "Snapshot không được cập nhật"
    },
    {
      "acceptance_criterion_references": [
        "BO-R03-AC002",
        "BO-R03-AC003",
        "BO-R03-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R03-O002",
      "obligation_text": "Snapshot chỉ được tạo mới"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BO-R03 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BO-R03 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BO-R03 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BO-R03-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BO-R03-AC001",
        "BO-R03-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BO-R03 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot không được cập nhật. Snapshot chỉ được tạo mới.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-R03",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-R03 — Immutable Snapshot",
    "source_context_sha256": "2287d079eba30fd0a9d848aeedfddf77644352fcf0664e4de9d8fdfd84203e20",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "5895a28947fb01c08377fdb5cc7442df0e070eafc8a5ce4c52a51c93243d3333",
    "source_lines": "L728-L733",
    "source_section": "12. Business Object Relationship Principles > BO-R03 — Immutable Snapshot"
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
  "stable_id": "BO-R03",
  "title": "Snapshot không được cập nhật. Snapshot chỉ được tạo mới",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-R04 — Business Object Publish Business Event. Business Object khác Subscribe Business Event. Không gọi…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R04-AC001",
      "given": "a candidate Business Object Publish Business Event. Business Object khác Subscribe Business Event. Không gọi… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R04-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R04-AC002",
      "given": "a candidate Business Object Publish Business Event. Business Object khác Subscribe Business Event. Không gọi… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R04-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R04-AC003",
      "given": "a candidate Business Object Publish Business Event. Business Object khác Subscribe Business Event. Không gọi… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R04-O003"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BO-R04-AC004",
      "given": "a Business Object Publish Business Event. Business Object khác Subscribe Business Event. Không gọi… candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BO-R04-O001",
        "BO-R04-O002",
        "BO-R04-O003"
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
        "BO-R04-AC001",
        "BO-R04-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R04-O001",
      "obligation_text": "Business Object Publish Business Event"
    },
    {
      "acceptance_criterion_references": [
        "BO-R04-AC002",
        "BO-R04-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R04-O002",
      "obligation_text": "Business Object khác Subscribe Business Event"
    },
    {
      "acceptance_criterion_references": [
        "BO-R04-AC003",
        "BO-R04-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R04-O003",
      "obligation_text": "Không gọi trực tiếp khi không cần thiết"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object Publish Business Event. Business Object khác Subscribe Business Event. Không gọi trực tiếp khi không cần thiết.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-R04",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-R04 — Event Driven",
    "source_context_sha256": "7d3d05fe0e933b489a514f6d58d6aa3069b03cc132c2efc955c6104417ffb40d",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "361b3d94cdc7ac914f107a149120cea3a72f437a51c1ccafb81e9352dd9a5012",
    "source_lines": "L736-L743",
    "source_section": "12. Business Object Relationship Principles > BO-R04 — Event Driven"
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
  "stable_id": "BO-R04",
  "title": "Business Object Publish Business Event. Business Object khác Subscribe Business Event. Không gọi…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-R05 — Business Object giữa các Domain phải giảm phụ thuộc trực tiếp. Ưu tiên: - Business Event - Canon…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R05-AC001",
      "given": "a candidate Business Object giữa các Domain phải giảm phụ thuộc trực tiếp. Ưu tiên: - Business Event - Canon… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R05-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R05-AC002",
      "given": "a candidate Business Object giữa các Domain phải giảm phụ thuộc trực tiếp. Ưu tiên: - Business Event - Canon… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R05-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R05-AC003",
      "given": "a candidate Business Object giữa các Domain phải giảm phụ thuộc trực tiếp. Ưu tiên: - Business Event - Canon… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R05-O003"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BO-R05-AC004",
      "given": "a Business Object giữa các Domain phải giảm phụ thuộc trực tiếp. Ưu tiên: - Business Event - Canon… candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BO-R05-O001",
        "BO-R05-O002",
        "BO-R05-O003"
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
        "BO-R05-AC001",
        "BO-R05-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R05-O001",
      "obligation_text": "Business Object giữa các Domain phải giảm phụ thuộc trực tiếp. Ưu tiên: Business Event."
    },
    {
      "acceptance_criterion_references": [
        "BO-R05-AC002",
        "BO-R05-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R05-O002",
      "obligation_text": "Business Object giữa các Domain phải giảm phụ thuộc trực tiếp. Ưu tiên: Canonical Model."
    },
    {
      "acceptance_criterion_references": [
        "BO-R05-AC003",
        "BO-R05-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R05-O003",
      "obligation_text": "Business Object giữa các Domain phải giảm phụ thuộc trực tiếp. Ưu tiên: Business Service."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object giữa các Domain phải giảm phụ thuộc trực tiếp. Ưu tiên: - Business Event - Canonical Model - Business Service",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-R05",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-R05 — Loose Coupling",
    "source_context_sha256": "09d1a96500f02d972888b70e1b028ff5bb383ffddb5c6e94b3a4d1847cd77de0",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "3f9cc8761029944f530397ebf2bf0dc481112401fa4899bfcdfef473177fa0c0",
    "source_lines": "L746-L755",
    "source_section": "12. Business Object Relationship Principles > BO-R05 — Loose Coupling"
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
  "stable_id": "BO-R05",
  "title": "Business Object giữa các Domain phải giảm phụ thuộc trực tiếp. Ưu tiên: - Business Event - Canon…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BO-R06 — Business Object sử dụng Configuration và Policy. Không Hard-code hành vi nghiệp vụ

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R06-AC001",
      "given": "a candidate Business Object sử dụng Configuration và Policy. Không Hard-code hành vi nghiệp vụ record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R06-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BO-R06-AC002",
      "given": "a candidate Business Object sử dụng Configuration và Policy. Không Hard-code hành vi nghiệp vụ record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BO-R06-O002"
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
        "BO-R06-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R06-O001",
      "obligation_text": "Business Object sử dụng Configuration và Policy"
    },
    {
      "acceptance_criterion_references": [
        "BO-R06-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BO-R06-O002",
      "obligation_text": "Không Hard-code hành vi nghiệp vụ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object sử dụng Configuration và Policy. Không Hard-code hành vi nghiệp vụ.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BO-R06",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-R06 — Configuration First",
    "source_context_sha256": "ae6103787b44190d665e4b941fa744c32af8c4291dd179a4598148566f302376",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "eb59825b754db930d67cc1ca7e6e9835768faf8a50bddc404420f0aba847e3ee",
    "source_lines": "L758-L763",
    "source_section": "12. Business Object Relationship Principles > BO-R06 — Configuration First"
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
  "stable_id": "BO-R06",
  "title": "Business Object sử dụng Configuration và Policy. Không Hard-code hành vi nghiệp vụ",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R001 — Business Object phải tuân thủ các quy tắc đặt tên sau

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R001-AC001",
      "given": "a candidate Business Object phải tuân thủ các quy tắc đặt tên sau record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R001-O001"
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
        "BRD-BO-INDEX-R001-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R001-O001",
      "obligation_text": "Business Object phải tuân thủ các quy tắc đặt tên sau"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object phải tuân thủ các quy tắc đặt tên sau:",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-001",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Naming Convention",
    "source_context_sha256": "f5c333b59336b4dba7854ba53b5c97db6498eb10bc96ef31075b54a9fb020dff",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "ad0d60e40b9ae4a1134a91a427204f004d92a3048dad26f509c7f6608cfb0dea",
    "source_lines": "L108",
    "source_section": "5. Naming Convention"
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
  "stable_id": "BRD-BO-INDEX-R001",
  "title": "Business Object phải tuân thủ các quy tắc đặt tên sau",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R002 — Tên phải phản ánh đúng khái niệm nghiệp vụ

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R002-AC001",
      "given": "the applicable business context, actor, and input for Tên phải phản ánh đúng khái niệm nghiệp vụ",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-BO-INDEX-R002-O001"
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
        "BRD-BO-INDEX-R002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R002-O001",
      "obligation_text": "Tên phải phản ánh đúng khái niệm nghiệp vụ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Tên phải phản ánh đúng khái niệm nghiệp vụ.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-002",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5.1 Business-oriented Naming",
    "source_context_sha256": "5c7fed44d1ac88f6ddb62947ca5ece42eec0bc7a819a130f12566b7e59a1e64d",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "4f24bf3f0837237d268a40d9e76f6dbc16c21fb0a0da0cff726bf506ce731de9",
    "source_lines": "L112",
    "source_section": "5. Naming Convention > 5.1 Business-oriented Naming"
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
  "stable_id": "BRD-BO-INDEX-R002",
  "title": "Tên phải phản ánh đúng khái niệm nghiệp vụ",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R003 — Sau khi Business Object được công bố và sử dụng trong Platform, tên không được thay đổi nếu khôn…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R003-AC001",
      "given": "a candidate Sau khi Business Object được công bố và sử dụng trong Platform, tên không được thay đổi nếu khôn… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns REJECTED when the prohibited value or relationship is present, and no rejected state is persisted",
      "verifies": [
        "BRD-BO-INDEX-R003-O001"
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
        "BRD-BO-INDEX-R003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R003-O001",
      "obligation_text": "Sau khi Business Object được công bố và sử dụng trong Platform, tên không được thay đổi nếu không có quyết định kiến trúc"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sau khi Business Object được công bố và sử dụng trong Platform, tên không được thay đổi nếu không có quyết định kiến trúc.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-003",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5.3 Stable Naming",
    "source_context_sha256": "570536880580bfd45cc22b9d52ebd81a1dd6dab6ee49bbf70cff07e8f25843ac",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "aa9053409011a0b3aace769492d5fabbec942766a48d9e62d2da3c5c65533d73",
    "source_lines": "L154",
    "source_section": "5. Naming Convention > 5.3 Stable Naming"
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
  "stable_id": "BRD-BO-INDEX-R003",
  "title": "Sau khi Business Object được công bố và sử dụng trong Platform, tên không được thay đổi nếu khôn…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R004 — Nếu cần thay đổi phải: - Review Impact

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R004-AC001",
      "given": "the applicable business context, actor, and input for Nếu cần thay đổi phải: - Review Impact",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-BO-INDEX-R004-O001"
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
        "BRD-BO-INDEX-R004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R004-O001",
      "obligation_text": "Nếu cần thay đổi phải: - Review Impact"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu cần thay đổi phải: - Review Impact",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-004",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5.3 Stable Naming",
    "source_context_sha256": "570536880580bfd45cc22b9d52ebd81a1dd6dab6ee49bbf70cff07e8f25843ac",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "58d928f4945770c655fc5f7c1d38c6383dadfb8c187a954892a5d9aa54ca5db8",
    "source_lines": "L156-L158",
    "source_section": "5. Naming Convention > 5.3 Stable Naming"
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
  "stable_id": "BRD-BO-INDEX-R004",
  "title": "Nếu cần thay đổi phải: - Review Impact",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R005 — Nếu cần thay đổi phải: - Approval

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R005-AC001",
      "given": "the applicable business context, actor, and input for Nếu cần thay đổi phải: - Approval",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-BO-INDEX-R005-O001"
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
        "BRD-BO-INDEX-R005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R005-O001",
      "obligation_text": "Nếu cần thay đổi phải: - Approval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu cần thay đổi phải: - Approval",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-005",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5.3 Stable Naming",
    "source_context_sha256": "570536880580bfd45cc22b9d52ebd81a1dd6dab6ee49bbf70cff07e8f25843ac",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "22b78ee3b5f3166013c26a0ce06b27d70efb9bf304064321c476a90179cb1801",
    "source_lines": "L156-L159",
    "source_section": "5. Naming Convention > 5.3 Stable Naming"
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
  "stable_id": "BRD-BO-INDEX-R005",
  "title": "Nếu cần thay đổi phải: - Approval",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R006 — Nếu cần thay đổi phải: - Versioning

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R006-AC001",
      "given": "the applicable business context, actor, and input for Nếu cần thay đổi phải: - Versioning",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-BO-INDEX-R006-O001"
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
        "BRD-BO-INDEX-R006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R006-O001",
      "obligation_text": "Nếu cần thay đổi phải: - Versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu cần thay đổi phải: - Versioning",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-006",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5.3 Stable Naming",
    "source_context_sha256": "570536880580bfd45cc22b9d52ebd81a1dd6dab6ee49bbf70cff07e8f25843ac",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "ef0ee7cee6a28d1b0655596cc097936fb42ef9403dd90cb0a5678e037fef464f",
    "source_lines": "L156-L160",
    "source_section": "5. Naming Convention > 5.3 Stable Naming"
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
  "stable_id": "BRD-BO-INDEX-R006",
  "title": "Nếu cần thay đổi phải: - Versioning",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R007 — Nếu cần thay đổi phải: - Traceability

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R007-AC001",
      "given": "the applicable business context, actor, and input for Nếu cần thay đổi phải: - Traceability",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-BO-INDEX-R007-O001"
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
        "BRD-BO-INDEX-R007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R007-O001",
      "obligation_text": "Nếu cần thay đổi phải: - Traceability"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu cần thay đổi phải: - Traceability",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-007",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5.3 Stable Naming",
    "source_context_sha256": "570536880580bfd45cc22b9d52ebd81a1dd6dab6ee49bbf70cff07e8f25843ac",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "a3521aaaa0347aca28a9231b19efc3ae7d109b0a847c24bcbd1f387bd723b6cf",
    "source_lines": "L156-L161",
    "source_section": "5. Naming Convention > 5.3 Stable Naming"
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
  "stable_id": "BRD-BO-INDEX-R007",
  "title": "Nếu cần thay đổi phải: - Traceability",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R008 — Một Business Object chỉ được tồn tại với một tên duy nhất trong toàn Platform

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R008-AC001",
      "given": "a candidate Một Business Object chỉ được tồn tại với một tên duy nhất trong toàn Platform record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R008-O001"
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
        "BRD-BO-INDEX-R008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R008-O001",
      "obligation_text": "Một Business Object chỉ được tồn tại với một tên duy nhất trong toàn Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Business Object chỉ được tồn tại với một tên duy nhất trong toàn Platform.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-008",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5.4 Unique Naming",
    "source_context_sha256": "393979cf38b2bbbd076edc7f1a22d54a48a128ccc22c49b7a9e5c1ff214ab253",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "d370f933fe973f6878e5958f89e44382dfcf845ca1b2b43afeef28a62908b0e2",
    "source_lines": "L167",
    "source_section": "5. Naming Convention > 5.4 Unique Naming"
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
  "stable_id": "BRD-BO-INDEX-R008",
  "title": "Một Business Object chỉ được tồn tại với một tên duy nhất trong toàn Platform",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R009 — Không được phép tồn tại các trường hợp: - Customer / Client

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R009-AC001",
      "given": "the applicable business context, actor, and input for Không được phép tồn tại các trường hợp: - Customer / Client",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-BO-INDEX-R009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-BO-INDEX-R009-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Không được phép tồn tại các trường hợp: - Customer / Client",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-BO-INDEX-R009-O001"
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
        "BRD-BO-INDEX-R009-AC001",
        "BRD-BO-INDEX-R009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R009-O001",
      "obligation_text": "Không được phép tồn tại các trường hợp: - Customer / Client"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không được phép tồn tại các trường hợp: - Customer / Client",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-009",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5.4 Unique Naming",
    "source_context_sha256": "393979cf38b2bbbd076edc7f1a22d54a48a128ccc22c49b7a9e5c1ff214ab253",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "a35b37323aa776584efc20aadf655138c3acf1c6c0fff29a6974f386f69f6803",
    "source_lines": "L169-L171",
    "source_section": "5. Naming Convention > 5.4 Unique Naming"
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
  "stable_id": "BRD-BO-INDEX-R009",
  "title": "Không được phép tồn tại các trường hợp: - Customer / Client",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R010 — Không được phép tồn tại các trường hợp: - Store / Shop

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R010-AC001",
      "given": "the applicable business context, actor, and input for Không được phép tồn tại các trường hợp: - Store / Shop",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-BO-INDEX-R010-O001"
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
        "BRD-BO-INDEX-R010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R010-O001",
      "obligation_text": "Không được phép tồn tại các trường hợp: - Store / Shop"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không được phép tồn tại các trường hợp: - Store / Shop",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-010",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5.4 Unique Naming",
    "source_context_sha256": "393979cf38b2bbbd076edc7f1a22d54a48a128ccc22c49b7a9e5c1ff214ab253",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "f186180fab5ed19db650721c39065b4a4d108c141614bf469104d486ae61f6b3",
    "source_lines": "L169-L172",
    "source_section": "5. Naming Convention > 5.4 Unique Naming"
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
  "stable_id": "BRD-BO-INDEX-R010",
  "title": "Không được phép tồn tại các trường hợp: - Store / Shop",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R011 — Không được phép tồn tại các trường hợp: - User Account / Account

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R011-AC001",
      "given": "the applicable business context, actor, and input for Không được phép tồn tại các trường hợp: - User Account / Account",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-BO-INDEX-R011-O001"
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
        "BRD-BO-INDEX-R011-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R011-O001",
      "obligation_text": "Không được phép tồn tại các trường hợp: - User Account / Account"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không được phép tồn tại các trường hợp: - User Account / Account",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-011",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5.4 Unique Naming",
    "source_context_sha256": "393979cf38b2bbbd076edc7f1a22d54a48a128ccc22c49b7a9e5c1ff214ab253",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "da52794de0138ba7b008b73c00bfba161cd84d2ab5c78eba9cfd03767c7501d0",
    "source_lines": "L169-L173",
    "source_section": "5. Naming Convention > 5.4 Unique Naming"
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
  "stable_id": "BRD-BO-INDEX-R011",
  "title": "Không được phép tồn tại các trường hợp: - User Account / Account",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R012 — Mỗi Business Object được cấp một mã định danh duy nhất

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R012-AC001",
      "given": "a candidate Mỗi Business Object được cấp một mã định danh duy nhất record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R012-O001"
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
        "BRD-BO-INDEX-R012-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R012-O001",
      "obligation_text": "Mỗi Business Object được cấp một mã định danh duy nhất"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Business Object được cấp một mã định danh duy nhất.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-012",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Business Object Identifier",
    "source_context_sha256": "ba9d89719117b2ca6e7fcc94056d4aa1ed4fd6ba51031befeb8b0f9e4ce14aea",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "7f7af52c61d0d11288f9e8b43c84305f693c080efaa180f33f7af60d267a1363",
    "source_lines": "L181",
    "source_section": "6. Business Object Identifier"
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
  "stable_id": "BRD-BO-INDEX-R012",
  "title": "Mỗi Business Object được cấp một mã định danh duy nhất",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R013 — Không phải mọi Business Object đều có Lifecycle

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R013-AC001",
      "given": "a candidate Không phải mọi Business Object đều có Lifecycle record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns REJECTED when the prohibited value or relationship is present, and no rejected state is persisted",
      "verifies": [
        "BRD-BO-INDEX-R013-O001"
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
        "BRD-BO-INDEX-R013-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R013-O001",
      "obligation_text": "Không phải mọi Business Object đều có Lifecycle"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không phải mọi Business Object đều có Lifecycle.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-013",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Business Object Lifecycle",
    "source_context_sha256": "529e7279bff653a316c34184f25e9f66b71fa6673003e1f3b5ac470667dd45d8",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "1fc63ad421f5e5c794166f9eff9fd24dfd307416ab60de860da7e40e7f02f4f7",
    "source_lines": "L208",
    "source_section": "7. Business Object Lifecycle"
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
  "stable_id": "BRD-BO-INDEX-R013",
  "title": "Không phải mọi Business Object đều có Lifecycle",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R014 — Business Object Registry tuân thủ các nguyên tắc sau

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R014-AC001",
      "given": "a candidate Business Object Registry tuân thủ các nguyên tắc sau record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R014-O001"
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
        "BRD-BO-INDEX-R014-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R014-O001",
      "obligation_text": "Business Object Registry tuân thủ các nguyên tắc sau"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object Registry tuân thủ các nguyên tắc sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-014",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Registry Principles",
    "source_context_sha256": "0da9e49c9d92fe3bc9a7eea7f22e1187c1cb3869fb7ab65e6ce238db3462850f",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "b7b3ffa55ec8dc0ae850587ed7e8e8695010edba352915473b9028d7b795b977",
    "source_lines": "L233",
    "source_section": "8. Registry Principles"
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
  "stable_id": "BRD-BO-INDEX-R014",
  "title": "Business Object Registry tuân thủ các nguyên tắc sau",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R015 — Snapshot chỉ được tạo mới, không chỉnh sửa

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R015-AC001",
      "given": "a candidate Snapshot chỉ được tạo mới, không chỉnh sửa record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R015-O001"
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
        "BRD-BO-INDEX-R015-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R015-O001",
      "obligation_text": "Snapshot chỉ được tạo mới, không chỉnh sửa"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot chỉ được tạo mới, không chỉnh sửa.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-015",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10.18 Snapshot Objects",
    "source_context_sha256": "2df43736c3197c85de052e87ccde0fa63f386c72a76842826b09c2b4d734ea11",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "d06b60fe2a2912da1c8a903852e3c22ccb02000fc11c510988acb660f1e7e297",
    "source_lines": "L623",
    "source_section": "10. Business Object Registry > 10.18 Snapshot Objects"
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
  "stable_id": "BRD-BO-INDEX-R015",
  "title": "Snapshot chỉ được tạo mới, không chỉnh sửa",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R016 — Business Object tuân thủ các nguyên tắc quan hệ sau

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R016-AC001",
      "given": "a candidate Business Object tuân thủ các nguyên tắc quan hệ sau record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R016-O001"
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
        "BRD-BO-INDEX-R016-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R016-O001",
      "obligation_text": "Business Object tuân thủ các nguyên tắc quan hệ sau"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object tuân thủ các nguyên tắc quan hệ sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-016",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Business Object Relationship Principles",
    "source_context_sha256": "6d0b98a4623bd6bf9a78502b8dc3854c7d0728e2f1178c3b2fb0d9ce73c35ac6",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "dc2477e5da3a33de2e82ae1417432bbf23fb8efd04cc581837b738c480e7ef7d",
    "source_lines": "L712",
    "source_section": "12. Business Object Relationship Principles"
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
  "stable_id": "BRD-BO-INDEX-R016",
  "title": "Business Object tuân thủ các nguyên tắc quan hệ sau",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R017 — Business Object chỉ được tạo mới khi: - Có Business Requirement

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R017-AC001",
      "given": "a candidate Business Object chỉ được tạo mới khi: - Có Business Requirement record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R017-O001"
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
        "BRD-BO-INDEX-R017-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R017-O001",
      "obligation_text": "Business Object chỉ được tạo mới khi: - Có Business Requirement"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object chỉ được tạo mới khi: - Có Business Requirement.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-017",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Business Object Governance",
    "source_context_sha256": "5c33d6d8e0eb6cee7918195e421cbdc51e3cc74abc0773b9960ee86ab5040e35",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "c25ce0ad108825289be601697d76d9dd536694288b6c6393fdd303f46e106c91",
    "source_lines": "L810-L812",
    "source_section": "15. Business Object Governance"
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
  "stable_id": "BRD-BO-INDEX-R017",
  "title": "Business Object chỉ được tạo mới khi: - Có Business Requirement",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R018 — Business Object chỉ được tạo mới khi: - Có Owner Domain

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R018-AC001",
      "given": "a candidate Business Object chỉ được tạo mới khi: - Có Owner Domain record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R018-O001"
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
        "BRD-BO-INDEX-R018-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R018-O001",
      "obligation_text": "Business Object chỉ được tạo mới khi: - Có Owner Domain"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object chỉ được tạo mới khi: - Có Owner Domain.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-018",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Business Object Governance",
    "source_context_sha256": "5c33d6d8e0eb6cee7918195e421cbdc51e3cc74abc0773b9960ee86ab5040e35",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "8a551881ff96078389142cf9e3904a322ff1906b17f38a5d1213c82c5d6bfeae",
    "source_lines": "L810-L813",
    "source_section": "15. Business Object Governance"
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
  "stable_id": "BRD-BO-INDEX-R018",
  "title": "Business Object chỉ được tạo mới khi: - Có Owner Domain",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R019 — Business Object chỉ được tạo mới khi: - Có Business Definition

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R019-AC001",
      "given": "a candidate Business Object chỉ được tạo mới khi: - Có Business Definition record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R019-O001"
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
        "BRD-BO-INDEX-R019-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R019-O001",
      "obligation_text": "Business Object chỉ được tạo mới khi: - Có Business Definition"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object chỉ được tạo mới khi: - Có Business Definition.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-019",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Business Object Governance",
    "source_context_sha256": "5c33d6d8e0eb6cee7918195e421cbdc51e3cc74abc0773b9960ee86ab5040e35",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "d45794af9f89d7f7273a99e37653c92c200b3880c30a4f23975382347a6fba9e",
    "source_lines": "L810-L814",
    "source_section": "15. Business Object Governance"
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
  "stable_id": "BRD-BO-INDEX-R019",
  "title": "Business Object chỉ được tạo mới khi: - Có Business Definition",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R020 — Business Object chỉ được tạo mới khi: - Có Architecture Review

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R020-AC001",
      "given": "a candidate Business Object chỉ được tạo mới khi: - Có Architecture Review record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R020-O001"
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
        "BRD-BO-INDEX-R020-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R020-O001",
      "obligation_text": "Business Object chỉ được tạo mới khi: - Có Architecture Review"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object chỉ được tạo mới khi: - Có Architecture Review.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-020",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Business Object Governance",
    "source_context_sha256": "5c33d6d8e0eb6cee7918195e421cbdc51e3cc74abc0773b9960ee86ab5040e35",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "b0173fa308f90a51577959fa1436f1182485afb838296e70a5c0f8372bbcf37e",
    "source_lines": "L810-L815",
    "source_section": "15. Business Object Governance"
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
  "stable_id": "BRD-BO-INDEX-R020",
  "title": "Business Object chỉ được tạo mới khi: - Có Architecture Review",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R021 — Business Object chỉ được tạo mới khi: - Có Approval

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R021-AC001",
      "given": "the applicable business context, actor, and input for Business Object chỉ được tạo mới khi: - Có Approval",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-BO-INDEX-R021-O001"
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
        "BRD-BO-INDEX-R021-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R021-O001",
      "obligation_text": "Business Object chỉ được tạo mới khi: - Có Approval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object chỉ được tạo mới khi: - Có Approval.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-021",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Business Object Governance",
    "source_context_sha256": "5c33d6d8e0eb6cee7918195e421cbdc51e3cc74abc0773b9960ee86ab5040e35",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "ea89d9eff088323af959cc920ea717084b508df1983b8f0a1c0d5d0df210ae52",
    "source_lines": "L810-L816",
    "source_section": "15. Business Object Governance"
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
  "stable_id": "BRD-BO-INDEX-R021",
  "title": "Business Object chỉ được tạo mới khi: - Có Approval",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R022 — Business Object không được tạo ra chỉ để phục vụ kỹ thuật

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R022-AC001",
      "given": "a candidate Business Object không được tạo ra chỉ để phục vụ kỹ thuật record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns REJECTED when the prohibited value or relationship is present, and no rejected state is persisted",
      "verifies": [
        "BRD-BO-INDEX-R022-O001"
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
        "BRD-BO-INDEX-R022-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R022-O001",
      "obligation_text": "Business Object không được tạo ra chỉ để phục vụ kỹ thuật"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Object không được tạo ra chỉ để phục vụ kỹ thuật.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-022",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Business Object Governance",
    "source_context_sha256": "5c33d6d8e0eb6cee7918195e421cbdc51e3cc74abc0773b9960ee86ab5040e35",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "a46c3279a2d575bf725e15c528e156efa8eced32ea09a3eb94268ed6d5b9dd0b",
    "source_lines": "L818",
    "source_section": "15. Business Object Governance"
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
  "stable_id": "BRD-BO-INDEX-R022",
  "title": "Business Object không được tạo ra chỉ để phục vụ kỹ thuật",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R024 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Loyalty Program

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Loyalty Program",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-024",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "3da84c0017cb6275e1c09e7a18763f3591d532646fd903e997f4369334e47c99",
    "source_lines": "L940-L942",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R024",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Loyalty Program",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R025 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Loyalty Wallet

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Loyalty Wallet",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-025",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "1d95eb706164eb6f451c1867cc0308d7e61fab5914cbcbef6f880055a702c62a",
    "source_lines": "L940-L943",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R025",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Loyalty Wallet",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R026 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Membership

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Membership",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-026",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "2aed1bedad85a8fb5c90da3fac7d5480015fadfa935949b814a28b1527507320",
    "source_lines": "L940-L944",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R026",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Membership",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R027 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Reward Point

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Reward Point",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-027",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "a8407a5f9d991c1ed1d2bb6c15e7f4c47a6ea18a3c0eacbe834b3d028a08c793",
    "source_lines": "L940-L945",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R027",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Reward Point",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R028 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Campaign Attribution

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Campaign Attribution",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-028",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-028",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "50d62cad74cc0a4226e3517a6ce81a7f727245eaeb7220464592688566bb8989",
    "source_lines": "L940-L946",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R028",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Campaign Attribution",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R029 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - AI Assistant

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - AI Assistant",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-029",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-029",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "f6afa6732e1d15650e909aaa0a10bd2579724563d79d88cd30ed5c32f7038fb8",
    "source_lines": "L940-L947",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R029",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - AI Assistant",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R030 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - AI Conversation

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - AI Conversation",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-030",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-030",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "fa823b03a38e1a20ec4c0be34bbbc9c5ec32a26b38abe12e1a085c57d9b21e2d",
    "source_lines": "L940-L948",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R030",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - AI Conversation",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R031 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Recommendation Engine

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SCOPE_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R031-AC001",
      "given": "the v2.3 capability inventory and conformance evidence for Các Business Object dự kiến bổ sung trong các phiên bản sau: - Recommendation Engine",
      "observable_evidence": "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
      "then": "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
      "verifies": [
        "BRD-BO-INDEX-R031-O001"
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
        "BRD-BO-INDEX-R031-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R031-O001",
      "obligation_text": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Recommendation Engine"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Recommendation Engine",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-031",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-031",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "0b854be96b398ee8e264341386489f2bd2de11c797e82822ceb1719213271c30",
    "source_lines": "L940-L949",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R031",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Recommendation Engine",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R032 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Dynamic Pricing Engine

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Dynamic Pricing Engine",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-032",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-032",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "c7d63af04648a2f037d7bfa4fff6773aa79afc5f5ca50fcb4b225da1116a250e",
    "source_lines": "L940-L950",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R032",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Dynamic Pricing Engine",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R033 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Fraud Detection

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SCOPE_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R033-AC001",
      "given": "the v2.3 capability inventory and conformance evidence for Các Business Object dự kiến bổ sung trong các phiên bản sau: - Fraud Detection",
      "observable_evidence": "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
      "then": "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
      "verifies": [
        "BRD-BO-INDEX-R033-O001"
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
        "BRD-BO-INDEX-R033-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R033-O001",
      "obligation_text": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Fraud Detection"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Fraud Detection",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-033",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-033",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "3455ff9650638b0c9045276f097be522ff79581c0ddcb6c530a5e8ed6aa4100c",
    "source_lines": "L940-L951",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R033",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Fraud Detection",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R034 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Partner Marketplace

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Partner Marketplace",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-034",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-034",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "e12d5b44ab407c7d728cccd2997bd0fc99da9111fda6194292a1198424da357b",
    "source_lines": "L940-L952",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R034",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Partner Marketplace",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R035 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Marketplace Product

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Marketplace Product",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-035",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-035",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "824de64db5bcdef53a670df319ca54ae9fad1ea452a8b9b6c584303e18722319",
    "source_lines": "L940-L953",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R035",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Marketplace Product",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R036 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Subscription Billing

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Subscription Billing",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-036",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-036",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "8b28165d5d67f9e7b06b3d09d1dec62847b49c9a6aa646acd0b8e6a9cbdc3049",
    "source_lines": "L940-L954",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R036",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Subscription Billing",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R037 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Device Management

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Device Management",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-037",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-037",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "d3f4a0d93db163afa74585b64c83eaabd20f43f746afb14529a696033c9032b9",
    "source_lines": "L940-L955",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R037",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Device Management",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R038 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - eSIM Activation Status

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - eSIM Activation Status",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-038",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-038",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "8282a2b1a04c697d40347b76d57fccd4202e2988dad3a1a9f60b42157bc6008a",
    "source_lines": "L940-L956",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R038",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - eSIM Activation Status",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R039 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Roaming Usage

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Roaming Usage",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-039",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-039",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "e0f4b4da04e73247819df2ecdb687dfff62b87a11c51569b0ef75144560dccd5",
    "source_lines": "L940-L957",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R039",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Roaming Usage",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R040 — Các Business Object dự kiến bổ sung trong các phiên bản sau: - Usage Analytics

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
  "normative_statement": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Usage Analytics",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-040",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-040",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "7d09c195c3415caf25f2b03a862ad8e4d67b69733b18b81267e1a8d21dbe1cfe",
    "source_lines": "L940-L958",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R040",
  "title": "Các Business Object dự kiến bổ sung trong các phiên bản sau: - Usage Analytics",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R041 — Business Object ID hiện có sẽ được giữ nguyên

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
  "normative_statement": "Business Object ID hiện có sẽ được giữ nguyên.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-041",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-041",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "e24c08ac73e468966534e33affbfd8698d0349aaeee20bbfcadd14cc2285a6e2",
    "source_lines": "L960",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R041",
  "title": "Business Object ID hiện có sẽ được giữ nguyên",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R042 — Business Object mới sẽ được bổ sung theo Version

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
  "normative_statement": "Business Object mới sẽ được bổ sung theo Version.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-042",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-042",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Future Evolution",
    "source_context_sha256": "8806fede352be867b8df79cd4d5a6069ca1a2e89ee6b130f38868a25e4209ba7",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "c999ccf8901149fccfd03c1c2b41b442a3974beaf532676cdff8b5ae4a68cea4",
    "source_lines": "L962",
    "source_section": "18. Future Evolution"
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
  "stable_id": "BRD-BO-INDEX-R042",
  "title": "Business Object mới sẽ được bổ sung theo Version",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R043 — Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Architecture Review

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R043-AC001",
      "given": "a candidate Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Architecture Review record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R043-O001"
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
        "BRD-BO-INDEX-R043-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R043-O001",
      "obligation_text": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Architecture Review"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Architecture Review",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-043",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-043",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Document Status",
    "source_context_sha256": "d1788813fa7d5918a0b20d414290559a731d0594567e18b1b80cb1155f871998",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "3af0bc9fbb9502e901ea4525da79ff0c1d2555c7e64bd9ad8c3e69b567829be6",
    "source_lines": "L1006-L1008",
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
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-BO-INDEX-R043",
  "title": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Architecture Review",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R044 — Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Approval

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R044-AC001",
      "given": "the applicable business context, actor, and input for Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Approval",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-BO-INDEX-R044-O001"
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
        "BRD-BO-INDEX-R044-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R044-O001",
      "obligation_text": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Approval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Approval",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-044",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-044",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Document Status",
    "source_context_sha256": "d1788813fa7d5918a0b20d414290559a731d0594567e18b1b80cb1155f871998",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "616498dc3372115434e775a79b14317c7eb704969340e4c3822736112d0c8534",
    "source_lines": "L1006-L1009",
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
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-BO-INDEX-R044",
  "title": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Approval",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R045 — Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Versioning

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R045-AC001",
      "given": "a candidate Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Versioning record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R045-O001"
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
        "BRD-BO-INDEX-R045-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R045-O001",
      "obligation_text": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Versioning",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-045",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-045",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Document Status",
    "source_context_sha256": "d1788813fa7d5918a0b20d414290559a731d0594567e18b1b80cb1155f871998",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "92843f14c5c8cefff7a6502f56ad97e4f53c30360a0f07b5f59bc688dbc91e06",
    "source_lines": "L1006-L1010",
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
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-BO-INDEX-R045",
  "title": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Versioning",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R046 — Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R046-AC001",
      "given": "an operational task within the scope of Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-BO-INDEX-R046-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-BO-INDEX-R046-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-BO-INDEX-R046-O001"
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
        "BRD-BO-INDEX-R046-AC001",
        "BRD-BO-INDEX-R046-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R046-O001",
      "obligation_text": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-BO-INDEX-R046 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-BO-INDEX-R046 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-BO-INDEX-R046 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-BO-INDEX-R046 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-BO-INDEX-R046-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-BO-INDEX-R046 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Audit",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-046",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-046",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Document Status",
    "source_context_sha256": "d1788813fa7d5918a0b20d414290559a731d0594567e18b1b80cb1155f871998",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "c64dfe00c880b01bca70d898606315e5490e1f51bacec1acee4fd863bfbe4eae",
    "source_lines": "L1006-L1011",
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
  "stable_id": "BRD-BO-INDEX-R046",
  "title": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R047 — Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Traceability

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R047-AC001",
      "given": "a candidate Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Traceability record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R047-O001"
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
        "BRD-BO-INDEX-R047-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R047-O001",
      "obligation_text": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Traceability"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Traceability",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-047",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-047",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Document Status",
    "source_context_sha256": "d1788813fa7d5918a0b20d414290559a731d0594567e18b1b80cb1155f871998",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "d0cb75c4b42a5907db02bae2d56d4f72fbf576a776f0a6da1800e7df9d0f775a",
    "source_lines": "L1006-L1012",
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
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-BO-INDEX-R047",
  "title": "Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Traceability",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R048 — Mọi tài liệu YSim phải sử dụng đúng Business Object được định nghĩa trong Business Object Regist…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R048-AC001",
      "given": "a candidate Mọi tài liệu YSim phải sử dụng đúng Business Object được định nghĩa trong Business Object Regist… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-BO-INDEX-R048-O001"
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
        "BRD-BO-INDEX-R048-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R048-O001",
      "obligation_text": "Mọi tài liệu YSim phải sử dụng đúng Business Object được định nghĩa trong Business Object Registry"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi tài liệu YSim phải sử dụng đúng Business Object được định nghĩa trong Business Object Registry.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-048",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-048",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "cfdb402d1ef9c88e82c6a97c3e98f8d8963461cdd6b2d232b0df6dc08bf26afa",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "82e126f63111a544dcf2e0d8819554e625f61d10e929ddf33cf5879a2547c7c9",
    "source_lines": "L279-L284",
    "source_section": "8. Registry Principles > BO-P06 — Platform Consistency"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BO-P06"
    ],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-BO-INDEX-R048",
  "title": "Mọi tài liệu YSim phải sử dụng đúng Business Object được định nghĩa trong Business Object Regist…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-BO-INDEX-R049 — Không được tạo Business Object mới ngoài Registry nếu chưa được Architecture Review

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-BO-INDEX-R049-AC001",
      "given": "an operational task within the scope of Không được tạo Business Object mới ngoài Registry nếu chưa được Architecture Review",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-BO-INDEX-R049-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-BO-INDEX-R049-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Không được tạo Business Object mới ngoài Registry nếu chưa được Architecture Review",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-BO-INDEX-R049-O001"
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
        "BRD-BO-INDEX-R049-AC001",
        "BRD-BO-INDEX-R049-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-BO-INDEX-R049-O001",
      "obligation_text": "Không được tạo Business Object mới ngoài Registry nếu chưa được Architecture Review"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không được tạo Business Object mới ngoài Registry nếu chưa được Architecture Review.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-BO-INDEX-049",
    "previous_temporary_key": "TMP-BRD-BO-INDEX-049",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BO-P06 — Platform Consistency",
    "source_context_sha256": "d9020504172b8b99c630c1d44b7429f9481bdb95371466306f8ad7e5928efd70",
    "source_document": "docs/BRD/BRD-BO-INDEX.md",
    "source_fingerprint": "82e126f63111a544dcf2e0d8819554e625f61d10e929ddf33cf5879a2547c7c9",
    "source_lines": "L279-L284",
    "source_section": "8. Registry Principles > BO-P06 — Platform Consistency"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BO-P06"
    ],
    "derived_requirements": []
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-BO-INDEX-R049",
  "title": "Không được tạo Business Object mới ngoài Registry nếu chưa được Architecture Review",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
