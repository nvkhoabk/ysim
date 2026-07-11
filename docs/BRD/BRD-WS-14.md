---
document_code: BRD-WS-14
document_name: Platform Configuration, Reference Data & Business Rules
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-14
---

# BRD Workshop 14

# Platform Configuration, Reference Data & Business Rules

---

# 1. Workshop Objective

Workshop này xác định toàn bộ nền tảng Configuration của YSim.

Bao gồm:

- Configuration Management
- Reference Data Management
- Dictionary Management
- Lookup Management
- Business Rule Engine
- Feature Flag Management
- Parameter Management
- Metadata Management
- Configuration Versioning
- Configuration Approval
- Configuration Package
- Configuration Dependency
- Runtime Configuration

Workshop này không bao gồm:

- Workflow Engine
- Integration Platform
- Security Platform

(Các nội dung trên được triển khai trong các Workshop tiếp theo.)

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| Configuration | Master |
| Configuration Set | Master |
| Configuration Version | Master |
| Configuration Scope | Master |
| Configuration Package | Master |
| Reference Data | Master |
| Dictionary | Master |
| Lookup Value | Master |
| Business Rule | Master |
| Rule Condition | Master |
| Rule Action | Master |
| Feature Flag | Master |
| Parameter | Master |
| Metadata | Master |

---

# 3. Configuration Scope

Configuration là Business Object.

Configuration hỗ trợ đầy đủ các Scope:

- Global (YSim)
- Parent Organization
- Organization
- Department
- Storefront
- User

Configuration luôn được tính theo mô hình **Effective Configuration**.

Scope thấp hơn có thể kế thừa hoặc Override Configuration từ Scope phía trên.

---

# 4. Configuration Override

Configuration hỗ trợ mô hình kế thừa.

Mô hình áp dụng:

```text
YSim

↓

Parent Organization

↓

Organization

↓

Department

↓

Storefront

↓

User

↓

Effective Configuration
```

Nguyên tắc:

- Scope thấp hơn có thể Override các thuộc tính được phép.
- Các thuộc tính không được Override sẽ kế thừa.
- Effective Configuration luôn được tính tại Runtime.

---

# 5. Reference Data

Reference Data là Business Object.

Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform.

Ví dụ:

- Country
- Region
- Province
- City
- Airport
- Currency
- Exchange Rate Source
- Language
- Locale
- Timezone
- Measurement Unit
- Temperature Unit
- Product Category
- Promotion Type
- Ticket Category
- Notification Category
- KPI Type
- Dashboard Widget Type
- Payment Method
- Settlement Type
- Organization Type

Reference Data hỗ trợ:

- Multi-language Name
- Parent / Child Relationship
- Alias
- Effective Date
- Enable / Disable

Reference Data không được Hard-code.

---

# 6. Dictionary

Dictionary là Business Object.

Dictionary khác Reference Data.

Dictionary quản lý:

- Enum
- Status
- Caption
- Display Label
- Translation
- Tooltip
- Description

Dictionary được sử dụng thống nhất trên:

- Portal
- API
- Report
- Notification
- Dynamic Form

---

# 7. Lookup

Lookup là Business Object.

Lookup hỗ trợ:

- Hierarchy
- Parent / Child
- Auto Complete
- Search
- Filter
- Dynamic Selection

Lookup được sử dụng bởi:

- Dynamic Form
- Dynamic Search
- Dynamic Filter
- Import
- Export
- API

---

# 8. Business Rule Engine

Business Rule là Business Object.

Business Rule bao gồm:

- Rule Condition
- Rule Action
- Priority
- Sequence
- Stop Policy

Business Rule được sử dụng trong:

- Commercial
- Promotion
- Pricing
- Inventory
- Payment
- Notification
- Support
- Security

Business Rule không được Hard-code.

---

# 9. Rule Scope

Business Rule có thể áp dụng theo:

- Platform
- Parent Organization
- Organization
- Department
- Storefront
- Product
- Category
- Campaign
- Customer Group

Kiến trúc hỗ trợ mở rộng thêm Rule Scope.

---

# 10. Rule Execution Strategy

Business Rule hỗ trợ các thành phần:

- Priority
- Sequence
- Stop Policy

Stop Policy hỗ trợ:

- Execute First Match
- Execute All
- Stop On Success
- Stop On Failure
- Continue

Execution Strategy được cấu hình.

Không Hard-code.

------

# 11. Rule Version

Business Rule được chỉnh sửa trực tiếp.

Mỗi lần thay đổi Rule sẽ tạo một phiên bản mới trong Configuration Version.

Business Rule luôn lưu:

- Current Version
- Modified By
- Modified Time
- Change Summary

Lịch sử thay đổi không được phép xóa.

---

# 12. Feature Flag

Feature Flag là Configuration Business Object.

Feature Flag được sử dụng để bật hoặc tắt các Capability của Platform.

Feature Flag hỗ trợ các Scope:

- Global
- Parent Organization
- Organization
- Storefront
- User

Feature Flag được sử dụng cho:

- Beta Feature
- Controlled Rollout
- Progressive Release
- Feature Toggle
- Emergency Disable

Feature Flag luôn được Runtime Reload.

Không yêu cầu Restart hệ thống.

---

# 13. Parameter

Parameter là Business Object.

Toàn bộ tham số hệ thống được quản lý thông qua Parameter.

Ví dụ:

- Reservation Timeout
- Retry Count
- Queue Size
- Tax Rate
- Default Currency
- Default Language
- OTP Expiration
- Session Timeout
- Payment Timeout
- Upload Size
- Password Policy
- Exchange Rate Refresh Interval

Parameter hỗ trợ Override theo Scope.

Parameter không được Hard-code.

---

# 14. Metadata

Metadata là Business Object.

Metadata mô tả đặc tính của dữ liệu.

Bao gồm:

- Field Name
- Data Type
- Required
- Default Value
- Validation Rule
- Searchable
- Sortable
- Filterable
- Exportable
- Importable
- Permission
- Localization
- Tooltip
- Description

Metadata phục vụ:

- Dynamic Form
- Dynamic API
- Report Builder
- Import
- Export
- Validation
- Search
- Dashboard

Metadata được sử dụng xuyên suốt toàn Platform.

---

# 15. Configuration Version

Configuration hỗ trợ Version.

Lifecycle:

```text
Draft

↓

Validate

↓

Approval

↓

Published

↓

Effective
```

Version cũ luôn được lưu lại.

Không ghi đè dữ liệu.

Configuration Version áp dụng cho:

- Configuration
- Business Rule
- Parameter
- Metadata
- Reference Data
- Dictionary

---

# 16. Configuration Approval

Configuration phải được Approval trước khi Publish.

Approval được thực hiện theo:

- Role
- Permission
- Organization Scope

Có thể hỗ trợ:

- Single Approval
- Multi-level Approval

Approval History được lưu Audit đầy đủ.

---

# 17. Effective Date

Configuration hỗ trợ:

- Effective From
- Effective To

Cho phép:

- Chuẩn bị Configuration trước
- Publish trước
- Tự động có hiệu lực đúng thời điểm

Configuration hết hiệu lực sẽ tự động chuyển sang Version kế tiếp nếu có.

---

# 18. Configuration Audit

Configuration Audit lưu đầy đủ:

- Who
- When
- Before Value
- After Value
- Reason
- Approval Information
- Version

Audit không được chỉnh sửa.

Audit luôn được lưu vĩnh viễn theo chính sách lưu trữ của Platform.

---

# 19. Configuration Import / Export

Configuration hỗ trợ Import và Export.

Định dạng hỗ trợ:

- JSON
- YAML
- Excel
- CSV

Import luôn thực hiện:

- Validation
- Dependency Check
- Conflict Check

trước khi Apply.

---

# 20. Configuration Package

Configuration Package là Business Object.

Một Package có thể bao gồm:

- Theme
- Dashboard
- Report
- Widget
- Storefront
- Notification
- Support Policy
- Price Book
- Business Rule
- Parameter
- Metadata
- Reference Data
- Dictionary

Configuration Package hỗ trợ:

- Export
- Import
- Install
- Upgrade
- Compare
- Merge
- Rollback

Package có thể được sử dụng để triển khai nhanh cho Organization mới hoặc nâng cấp Configuration giữa các Environment.

------

# 21. Configuration Validation

Configuration phải được Validate trước khi Save và trước khi Publish.

Validation bao gồm:

- Duplicate Configuration
- Missing Reference
- Missing Required Parameter
- Circular Dependency
- Invalid Scope
- Invalid Permission
- Invalid Environment
- Business Rule Conflict
- Invalid Effective Date
- Invalid Version Dependency

Validation được thực hiện tự động.

Configuration không hợp lệ không được phép Publish.

Validation Result được lưu lại để phục vụ Audit.

---

# 22. Configuration Rollback

Configuration hỗ trợ Rollback theo Version.

Rollback có thể thực hiện đối với:

- Configuration
- Parameter
- Business Rule
- Metadata
- Reference Data
- Dictionary

Rollback không được làm mất:

- Audit
- Version History
- Approval History

Rollback luôn tạo một Version mới.

Không ghi đè Version cũ.

---

# 23. Configuration Dependency

Configuration hỗ trợ quản lý Dependency.

Một Configuration có thể phụ thuộc vào:

- Parameter
- Business Rule
- Reference Data
- Dictionary
- Metadata
- Feature Flag
- Configuration khác

Dependency được kiểm tra:

- Khi Save
- Khi Publish
- Khi Import
- Khi Upgrade

Dependency được sử dụng để phân tích ảnh hưởng trước khi Configuration có hiệu lực.

---

# 24. Environment Configuration

Configuration hỗ trợ nhiều Environment.

Bao gồm:

- Development
- UAT
- Production

Configuration có thể:

- Publish riêng cho từng Environment
- Đồng bộ giữa các Environment
- So sánh khác biệt giữa các Environment

Environment Configuration phục vụ quá trình triển khai và kiểm thử.

---

# 25. Runtime Reload

Configuration hỗ trợ Runtime Reload.

Sau khi Configuration được Publish:

- Runtime tự động tải lại Configuration.
- Không yêu cầu Restart Application trong hầu hết các trường hợp.

Runtime Reload áp dụng cho:

- Parameter
- Business Rule
- Reference Data
- Dictionary
- Feature Flag
- Metadata

Một số Configuration đặc biệt có thể yêu cầu Restart và phải được cảnh báo trước khi Publish.

---

# 26. Organization Template

Organization Template là Business Capability.

Khi tạo Organization mới, người quản trị có thể lựa chọn Template.

Ví dụ:

- Travel Agency
- OTA
- Affiliate
- Distributor
- Enterprise
- Internal Department

Sau khi chọn Template, hệ thống tự động khởi tạo:

- Organization Structure
- Default Roles
- Permission
- Dashboard
- Storefront
- Theme
- Report
- Widget
- Knowledge Base
- FAQ
- Notification
- Support Policy
- Survey
- Configuration
- Price Book
- Business Rule

Organization có thể Active ngay cả khi chưa hoàn thành toàn bộ Checklist Onboarding.

---

# 27. Configuration Layering

Configuration áp dụng theo mô hình Layer.

```text
YSim Global

↓

Parent Organization

↓

Organization

↓

Department

↓

Storefront

↓

User

↓

Effective Configuration
```

Nguyên tắc:

- Scope thấp hơn có độ ưu tiên cao hơn.
- Chỉ các thuộc tính được phép mới được Override.
- Các thuộc tính khác kế thừa từ Scope phía trên.
- Effective Configuration luôn được tính tại Runtime.

Configuration Layering áp dụng thống nhất trên toàn Platform.

---

# 28. Configuration Capability Matrix

Không phải mọi Configuration đều được phép Override.

Mỗi Configuration phải định nghĩa Capability Matrix.

Bao gồm:

- Read
- Create
- Edit
- Delete
- Override
- Clone
- Import
- Export
- Approval Required
- Runtime Reload Supported

Capability Matrix được xác định theo:

- Configuration Type
- Scope
- Role
- Permission

Điều này giúp đảm bảo Architecture Baseline không bị phá vỡ.

---

# 29. Configuration Category

Configuration được phân nhóm để thuận tiện cho việc quản trị.

Các nhóm mặc định:

- System
- Organization
- Storefront
- Commercial
- Financial
- Notification
- Customer
- Support
- Security
- Integration
- Workflow
- Localization
- Reporting
- Monitoring
- Scheduler

Kiến trúc hỗ trợ bổ sung Category mới.

Category phục vụ:

- Portal Navigation
- Search
- Permission
- Report
- Audit

---

# 30. Configuration Dependency Graph

Configuration hỗ trợ Dependency Graph.

Dependency Graph được sử dụng để:

- Impact Analysis
- Upgrade Planning
- Validation
- Rollback
- Publish Checking

Ví dụ:

```text
Currency

↓

Exchange Rate

↓

Price Book

↓

Commercial Policy

↓

Settlement

↓

Financial Report
```

Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Capability bị ảnh hưởng.

Dependency Graph là nền tảng cho việc quản lý Configuration của toàn bộ Platform.

------

# 31. Business Decisions (Locked)

## BD-14-001

Configuration hỗ trợ đầy đủ các Scope:

- Global
- Parent Organization
- Organization
- Department
- Storefront
- User

---

## BD-14-002

Configuration hỗ trợ Override theo mô hình Layer.

Effective Configuration được tính tại Runtime.

---

## BD-14-003

Reference Data là Business Object.

Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform.

Reference Data hỗ trợ:

- Multi-language
- Parent / Child
- Alias
- Effective Date

---

## BD-14-004

Dictionary là Business Object độc lập.

Dictionary không thay thế Reference Data.

Dictionary quản lý Label, Enum, Caption và Translation.

---

## BD-14-005

Lookup là Business Object.

Lookup hỗ trợ Dynamic Form, Search và API.

---

## BD-14-006

Business Rule là Business Object.

Business Rule được cấu hình.

Không Hard-code.

---

## BD-14-007

Business Rule hỗ trợ nhiều Scope.

Rule có thể áp dụng theo:

- Platform
- Organization
- Department
- Storefront
- Product
- Campaign
- Category
- Customer Group

---

## BD-14-008

Business Rule hỗ trợ:

- Priority
- Sequence
- Stop Policy

Stop Policy được cấu hình.

---

## BD-14-009

Business Rule chỉnh sửa trực tiếp.

Lịch sử thay đổi được lưu thông qua Configuration Version và Audit.

---

## BD-14-010

Feature Flag là Business Object.

Feature Flag hỗ trợ:

- Global
- Parent Organization
- Organization
- Storefront
- User

---

## BD-14-011

Toàn bộ tham số hệ thống được quản lý bằng Parameter.

Parameter hỗ trợ Override theo Scope.

---

## BD-14-012

Metadata là Business Object.

Metadata phục vụ:

- Dynamic Form
- Dynamic API
- Validation
- Import
- Export
- Report Builder
- Dashboard

---

## BD-14-013

Configuration hỗ trợ Version.

Lifecycle:

Draft

↓

Validate

↓

Approval

↓

Published

↓

Effective

---

## BD-14-014

Configuration bắt buộc Approval trước Publish.

Approval theo Role và Permission.

---

## BD-14-015

Configuration hỗ trợ:

- Effective From
- Effective To

---

## BD-14-016

Configuration Audit lưu đầy đủ:

- Who
- When
- Before
- After
- Reason
- Version

---

## BD-14-017

Configuration hỗ trợ:

- JSON
- YAML
- Excel
- CSV

Import luôn Validate trước Apply.

---

## BD-14-018

Configuration Package hỗ trợ:

- Export
- Import
- Install
- Upgrade
- Compare
- Merge
- Rollback

---

## BD-14-019

Configuration hỗ trợ:

- Validation
- Dependency
- Rollback

---

## BD-14-020

Configuration hỗ trợ nhiều Environment.

- Development
- UAT
- Production

---

## BD-14-021

Configuration hỗ trợ Runtime Reload.

Không yêu cầu Restart đối với đa số Configuration.

---

## BD-14-022

Organization Template hỗ trợ Bootstrap toàn bộ Organization.

Template tự động tạo:

- Role
- Dashboard
- Storefront
- Theme
- Report
- Notification
- KB
- FAQ
- Survey
- Support Policy
- Configuration

---

## BD-14-023

Configuration áp dụng theo mô hình Layering.

Effective Configuration luôn được tính theo Scope.

---

## BD-14-024

Configuration Capability Matrix xác định:

- Read
- Create
- Edit
- Delete
- Override
- Clone
- Import
- Export
- Approval Required
- Runtime Reload

---

## BD-14-025

Configuration được phân nhóm theo Category.

Category mặc định:

- System
- Organization
- Storefront
- Commercial
- Financial
- Notification
- Customer
- Support
- Security
- Integration
- Workflow
- Localization
- Reporting
- Monitoring
- Scheduler

---

## BD-14-026

Configuration Dependency Graph hỗ trợ:

- Dependency Analysis
- Impact Analysis
- Upgrade Planning
- Publish Validation
- Rollback

---

# 32. Enterprise Design Principles

## EP-14-001

Configuration over Customization là nguyên tắc cốt lõi của Platform.

---

## EP-14-002

Toàn bộ Business Domain ưu tiên Configuration trước khi Hard-code.

---

## EP-14-003

Reference Data là nguồn dữ liệu chuẩn của toàn Platform.

---

## EP-14-004

Business Rule được cấu hình, không Hard-code.

---

## EP-14-005

Metadata điều khiển Dynamic Form, Dynamic API, Validation và Reporting.

---

## EP-14-006

Configuration luôn có:

- Version
- Approval
- Audit

---

## EP-14-007

Configuration hỗ trợ Runtime Reload.

---

## EP-14-008

Configuration hỗ trợ Layering và Effective Configuration.

---

## EP-14-009

Configuration hỗ trợ Package để triển khai và nâng cấp Platform.

---

## EP-14-010

Organization được khởi tạo bằng Template nhằm giảm thời gian Onboarding.

---

# 33. Business Capabilities Covered

Workshop này bao gồm các Business Capability:

- Configuration Management
- Configuration Version Management
- Configuration Approval
- Configuration Audit
- Configuration Package
- Reference Data Management
- Dictionary Management
- Lookup Management
- Business Rule Engine
- Feature Flag Management
- Parameter Management
- Metadata Management
- Runtime Configuration
- Environment Configuration
- Organization Template Management
- Configuration Dependency Management

---

# 34. Traceability

Workshop này kế thừa toàn bộ các quyết định từ:

- BRD-WS-01 Business Vision
- BRD-WS-02 Product
- BRD-WS-03 Organization
- BRD-WS-04 Catalog
- BRD-WS-05 Commercial
- BRD-WS-06 Promotion
- BRD-WS-07 Order
- BRD-WS-08 Payment
- BRD-WS-09 Inventory & Fulfillment
- BRD-WS-10 Financial & Settlement
- BRD-WS-11 Customer Success
- BRD-WS-12 Communication Platform
- BRD-WS-13 Reporting, Analytics & Operational Intelligence

WS-14 là Platform Foundation phục vụ toàn bộ Business Domain của YSim.

---

# 35. Impacts to Other Domains

Workshop này ảnh hưởng trực tiếp tới:

- Product
- Commercial
- Promotion
- Order
- Payment
- Inventory
- Fulfillment
- Financial
- Settlement
- Customer Success
- Communication
- Reporting
- Analytics
- Integration
- Security
- Monitoring

Toàn bộ các Domain đều sử dụng chung Platform Configuration.

---

# 36. Workshop Status

Status:

**FROZEN**

Workshop này hoàn thiện toàn bộ Configuration Foundation của nền tảng YSim.

---

# 37. Next Workshop

**BRD-WS-15**

**Integration Platform, API Gateway & Event Bus**

Workshop tiếp theo sẽ xác định:

- Integration Platform
- API Gateway
- Event Bus
- Event Contract
- Webhook
- Connector
- Adapter
- Integration Monitoring
- Retry & Dead Letter Queue
- Event-driven Architecture

Đây sẽ là nền tảng tích hợp toàn bộ Supplier, Payment Gateway và các hệ thống bên ngoài của YSim.

---