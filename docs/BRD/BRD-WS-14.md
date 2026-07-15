---
document_code: "BRD-WS-14"
title: "Platform Configuration, Reference Data & Business Rules"
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

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-001 — Configuration hỗ trợ đầy đủ các Scope: - Global - Parent Organization - Organization - Departmen…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-001-AC001",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ đầy đủ các Scope: - Global - Parent Organization - Organization - Departmen…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-001-AC002",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ đầy đủ các Scope: - Global - Parent Organization - Organization - Departmen…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-001-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-001-AC003",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ đầy đủ các Scope: - Global - Parent Organization - Organization - Departmen…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-001-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-001-AC004",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ đầy đủ các Scope: - Global - Parent Organization - Organization - Departmen…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-001-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-001-AC005",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ đầy đủ các Scope: - Global - Parent Organization - Organization - Departmen…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-001-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-001-AC006",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ đầy đủ các Scope: - Global - Parent Organization - Organization - Departmen…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-001-O006"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-14-001-AC007",
      "given": "an unsupported or invalid business input at the boundary governed by Configuration hỗ trợ đầy đủ các Scope: - Global - Parent Organization - Organization - Departmen…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-14-001-O001",
        "BD-14-001-O002",
        "BD-14-001-O003",
        "BD-14-001-O004",
        "BD-14-001-O005",
        "BD-14-001-O006"
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
        "BD-14-001-AC001",
        "BD-14-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O001",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: Global."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-001-AC002",
        "BD-14-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O002",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: Parent Organization."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-001-AC003",
        "BD-14-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O003",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: Organization."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-001-AC004",
        "BD-14-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O004",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: Department."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-001-AC005",
        "BD-14-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O005",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: Storefront."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-001-AC006",
        "BD-14-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O006",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: User."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration hỗ trợ đầy đủ các Scope: - Global - Parent Organization - Organization - Department - Storefront - User",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Configuration Scope",
    "source_context_sha256": "3c00a3b8e83af1a79299293f4bed5adb860fb385ab6d3bd6f8ecd5a047619f05",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "77f1ee1c9538fa8554cc464d70320a665a5177711fcfa166784c17527c728b84",
    "source_lines": "L859-L869",
    "source_section": "31. Business Decisions (Locked) > BD-14-001"
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
  "stable_id": "BD-14-001",
  "title": "Configuration hỗ trợ đầy đủ các Scope: - Global - Parent Organization - Organization - Departmen…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-002 — Configuration hỗ trợ Override theo mô hình Layer. Effective Configuration được tính tại Runtime

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-002-AC001",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ Override theo mô hình Layer. Effective Configuration được tính tại Runtime",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-002-AC002",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ Override theo mô hình Layer. Effective Configuration được tính tại Runtime",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-002-O002"
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
        "BD-14-002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-002-O001",
      "obligation_text": "Configuration hỗ trợ Override theo mô hình Layer"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-002-O002",
      "obligation_text": "Effective Configuration được tính tại Runtime"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration hỗ trợ Override theo mô hình Layer. Effective Configuration được tính tại Runtime.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-002",
    "source_context_sha256": "bc10a73b52d2392c60d4d70571a8030c42301d3854603ad973604e8308c0c8ea",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "0d146e30a60b4851d685d92724af3d3a93ab02ec748e3000cd6dedcf4a440d3d",
    "source_lines": "L872-L877",
    "source_section": "31. Business Decisions (Locked) > BD-14-002"
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
  "stable_id": "BD-14-002",
  "title": "Configuration hỗ trợ Override theo mô hình Layer. Effective Configuration được tính tại Runtime",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-003 — Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-003-AC001",
      "given": "a candidate Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-003-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-003-AC002",
      "given": "a candidate Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-003-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-003-AC003",
      "given": "a candidate Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-003-O003"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-003-AC004",
      "given": "a candidate Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-003-O004"
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
        "BD-14-003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-003-O001",
      "obligation_text": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform. Reference Data hỗ trợ: Multi-language."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-003-O002",
      "obligation_text": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform. Reference Data hỗ trợ: Parent / Child."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-003-O003",
      "obligation_text": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform. Reference Data hỗ trợ: Alias."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-003-O004",
      "obligation_text": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform. Reference Data hỗ trợ: Effective Date."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform. Reference Data hỗ trợ: - Multi-language - Parent / Child - Alias - Effective Date",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Data",
    "source_context_sha256": "8159a2e679167d6d72d40b009066fd1f2181eed5a5122ec29675371dcf1ef8de",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "f8ffedfcc14d6f86a45d6e94ad06106862bb94329e2f1b2610f39629b776884a",
    "source_lines": "L880-L892",
    "source_section": "31. Business Decisions (Locked) > BD-14-003"
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
  "stable_id": "BD-14-003",
  "title": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-004 — Dictionary là Business Object độc lập. Dictionary không thay thế Reference Data. Dictionary quản…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-004-AC001",
      "given": "a candidate Dictionary là Business Object độc lập. Dictionary không thay thế Reference Data. Dictionary quản… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-004-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-004-AC002",
      "given": "a candidate Dictionary là Business Object độc lập. Dictionary không thay thế Reference Data. Dictionary quản… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-004-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-004-AC003",
      "given": "a candidate Dictionary là Business Object độc lập. Dictionary không thay thế Reference Data. Dictionary quản… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-004-O003"
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
        "BD-14-004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-004-O001",
      "obligation_text": "Dictionary là Business Object độc lập"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-004-O002",
      "obligation_text": "Dictionary không thay thế Reference Data"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-004-O003",
      "obligation_text": "Dictionary quản lý Label, Enum, Caption và Translation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dictionary là Business Object độc lập. Dictionary không thay thế Reference Data. Dictionary quản lý Label, Enum, Caption và Translation.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-010"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-004",
    "source_context_sha256": "6acc8c8e8f8c79c34e8e3d5a62ad5e90891a24c77aa4a41c451f45395691f8c5",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "e7ac4df687cd599afce951a9c4ae9abf8959a71d66fa2a9ef0c911658dff822a",
    "source_lines": "L895-L902",
    "source_section": "31. Business Decisions (Locked) > BD-14-004"
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
  "stable_id": "BD-14-004",
  "title": "Dictionary là Business Object độc lập. Dictionary không thay thế Reference Data. Dictionary quản…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-005 — Lookup là Business Object. Lookup hỗ trợ Dynamic Form, Search và API

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-14-005-AC001",
      "given": "a contract interaction at the integration boundary defined by Lookup là Business Object. Lookup hỗ trợ Dynamic Form, Search và API",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-14-005-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-14-005-AC002",
      "given": "a contract interaction at the integration boundary defined by Lookup là Business Object. Lookup hỗ trợ Dynamic Form, Search và API",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-14-005-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-14-005-AC003",
      "given": "an interaction that violates the contract or ownership boundary for Lookup là Business Object. Lookup hỗ trợ Dynamic Form, Search và API",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-14-005-O001",
        "BD-14-005-O002"
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
        "BD-14-005-AC001",
        "BD-14-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-005-O001",
      "obligation_text": "Lookup là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-005-AC002",
        "BD-14-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-005-O002",
      "obligation_text": "Lookup hỗ trợ Dynamic Form, Search và API"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Lookup là Business Object. Lookup hỗ trợ Dynamic Form, Search và API.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Lookup",
    "source_context_sha256": "8804366f4a545b0fb9bbb50d4eaa779da1bf068f6ea2f59a6482952396f5cd97",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "63d532bb558fe392405de1eee5c917cf25b105f246d50e31a69846f86b90eb16",
    "source_lines": "L905-L910",
    "source_section": "31. Business Decisions (Locked) > BD-14-005"
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
  "stable_id": "BD-14-005",
  "title": "Lookup là Business Object. Lookup hỗ trợ Dynamic Form, Search và API",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-006 — Business Rule là Business Object. Business Rule được cấu hình. Không Hard-code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-006-AC001",
      "given": "a candidate Business Rule là Business Object. Business Rule được cấu hình. Không Hard-code record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-006-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-006-AC002",
      "given": "a candidate Business Rule là Business Object. Business Rule được cấu hình. Không Hard-code record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-006-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-006-AC003",
      "given": "a candidate Business Rule là Business Object. Business Rule được cấu hình. Không Hard-code record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-006-O003"
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
        "BD-14-006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-006-O001",
      "obligation_text": "Business Rule là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-006-O002",
      "obligation_text": "Business Rule được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-006-O003",
      "obligation_text": "Không Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule là Business Object. Business Rule được cấu hình. Không Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Business Rule Engine",
    "source_context_sha256": "86d3ad94506a400c239a818b3540c68c8fa7011a8692d42b51ff06ebc3155e51",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "229a3404ed449712b41ef2f142542eb356567db3a11a775a488094cfa5dd0c18",
    "source_lines": "L913-L920",
    "source_section": "31. Business Decisions (Locked) > BD-14-006"
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
  "stable_id": "BD-14-006",
  "title": "Business Rule là Business Object. Business Rule được cấu hình. Không Hard-code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-007 — Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-007-AC001",
      "given": "the applicable business context, actor, and input for Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-007-AC002",
      "given": "the applicable business context, actor, and input for Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-007-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-007-AC003",
      "given": "the applicable business context, actor, and input for Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-007-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-007-AC004",
      "given": "the applicable business context, actor, and input for Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-007-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-007-AC005",
      "given": "the applicable business context, actor, and input for Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-007-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-007-AC006",
      "given": "the applicable business context, actor, and input for Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-007-O006"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-007-AC007",
      "given": "the applicable business context, actor, and input for Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-007-O007"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-007-AC008",
      "given": "the applicable business context, actor, and input for Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-007-O008"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-14-007-AC009",
      "given": "an unsupported or invalid business input at the boundary governed by Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-14-007-O001",
        "BD-14-007-O002",
        "BD-14-007-O003",
        "BD-14-007-O004",
        "BD-14-007-O005",
        "BD-14-007-O006",
        "BD-14-007-O007",
        "BD-14-007-O008"
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
        "BD-14-007-AC001",
        "BD-14-007-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O001",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Platform."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC002",
        "BD-14-007-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O002",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Organization."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC003",
        "BD-14-007-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O003",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Department."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC004",
        "BD-14-007-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O004",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Storefront."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC005",
        "BD-14-007-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O005",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Product."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC006",
        "BD-14-007-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O006",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Campaign."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC007",
        "BD-14-007-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O007",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Category."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC008",
        "BD-14-007-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O008",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Customer Group."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Department - Storefront - Product - Campaign - Category - Customer Group",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-007",
    "source_context_sha256": "662132496ffd7daed1f4ee62ead372d25a28fd8be7af04aecdfb915c18c513e3",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "d8b54e9a12f232d34e00e97b39e4a04cce03eedb4c1aa771b776ae1a5110200e",
    "source_lines": "L923-L937",
    "source_section": "31. Business Decisions (Locked) > BD-14-007"
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
  "stable_id": "BD-14-007",
  "title": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-008 — Business Rule hỗ trợ: - Priority - Sequence - Stop Policy Stop Policy được cấu hình

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-008-AC001",
      "given": "the applicable business context, actor, and input for Business Rule hỗ trợ: - Priority - Sequence - Stop Policy Stop Policy được cấu hình",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-008-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-008-AC002",
      "given": "the applicable business context, actor, and input for Business Rule hỗ trợ: - Priority - Sequence - Stop Policy Stop Policy được cấu hình",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-008-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-008-AC003",
      "given": "the applicable business context, actor, and input for Business Rule hỗ trợ: - Priority - Sequence - Stop Policy Stop Policy được cấu hình",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-008-O003"
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
        "BD-14-008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-008-O001",
      "obligation_text": "Business Rule hỗ trợ: Priority."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-008-O002",
      "obligation_text": "Business Rule hỗ trợ: Sequence."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-008-O003",
      "obligation_text": "Business Rule hỗ trợ: Stop Policy Stop Policy được cấu hình."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule hỗ trợ: - Priority - Sequence - Stop Policy Stop Policy được cấu hình.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-008",
    "source_context_sha256": "c33e5331273aa6b1e9c6ebedcb0ed552e775fdaa9d47922b35962d1646a2a60d",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "d98549cce9b6afa8593c082040fadb8d58c5b273a01bd1ebd304ad336d2ce1bb",
    "source_lines": "L940-L949",
    "source_section": "31. Business Decisions (Locked) > BD-14-008"
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
  "stable_id": "BD-14-008",
  "title": "Business Rule hỗ trợ: - Priority - Sequence - Stop Policy Stop Policy được cấu hình",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-009 — Business Rule chỉnh sửa trực tiếp. Lịch sử thay đổi được lưu thông qua Configuration Version và …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-009-AC001",
      "given": "an operational task within the scope of Business Rule chỉnh sửa trực tiếp. Lịch sử thay đổi được lưu thông qua Configuration Version và …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-14-009-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-009-AC002",
      "given": "an operational task within the scope of Business Rule chỉnh sửa trực tiếp. Lịch sử thay đổi được lưu thông qua Configuration Version và …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-14-009-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-14-009-AC003",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Business Rule chỉnh sửa trực tiếp. Lịch sử thay đổi được lưu thông qua Configuration Version và …",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-14-009-O001",
        "BD-14-009-O002"
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
        "BD-14-009-AC001",
        "BD-14-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-009-O001",
      "obligation_text": "Business Rule chỉnh sửa trực tiếp"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-009-AC002",
        "BD-14-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-009-O002",
      "obligation_text": "Lịch sử thay đổi được lưu thông qua Configuration Version và Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-14-009 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-14-009 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-14-009 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-14-009 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-14-009-AC001",
        "BD-14-009-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-14-009 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule chỉnh sửa trực tiếp. Lịch sử thay đổi được lưu thông qua Configuration Version và Audit.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-009",
    "source_context_sha256": "789bfafdb51cab59b8dee4fa52e7620990a8dbccf6e2071e0299d5856b138ec7",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "35f92c275bb092a7ccafb79e457fd2dc59b64b175a3af46b376b57d3a29a46dc",
    "source_lines": "L952-L957",
    "source_section": "31. Business Decisions (Locked) > BD-14-009"
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
  "stable_id": "BD-14-009",
  "title": "Business Rule chỉnh sửa trực tiếp. Lịch sử thay đổi được lưu thông qua Configuration Version và …",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-010 — Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organizat…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-010-AC001",
      "given": "a candidate Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organizat… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-010-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-010-AC002",
      "given": "a candidate Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organizat… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-010-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-010-AC003",
      "given": "a candidate Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organizat… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-010-O003"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-010-AC004",
      "given": "a candidate Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organizat… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-010-O004"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-14-010-AC005",
      "given": "a candidate Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organizat… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-14-010-O005"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-14-010-AC006",
      "given": "a Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organizat… candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-14-010-O001",
        "BD-14-010-O002",
        "BD-14-010-O003",
        "BD-14-010-O004",
        "BD-14-010-O005"
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
        "BD-14-010-AC001",
        "BD-14-010-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-010-O001",
      "obligation_text": "Feature Flag là Business Object. Feature Flag hỗ trợ: Global."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-010-AC002",
        "BD-14-010-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-010-O002",
      "obligation_text": "Feature Flag là Business Object. Feature Flag hỗ trợ: Parent Organization."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-010-AC003",
        "BD-14-010-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-010-O003",
      "obligation_text": "Feature Flag là Business Object. Feature Flag hỗ trợ: Organization."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-010-AC004",
        "BD-14-010-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-010-O004",
      "obligation_text": "Feature Flag là Business Object. Feature Flag hỗ trợ: Storefront."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-010-AC005",
        "BD-14-010-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-010-O005",
      "obligation_text": "Feature Flag là Business Object. Feature Flag hỗ trợ: User."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organization - Storefront - User",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-010",
    "source_context_sha256": "36a85a92279eb52803fdc59156a6e359a91c89f4dce29f08327f34b94c7d92ef",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "0523a5bee5c4241730ee1947df4ef2cf9eb75b2b328edd8366e62629616c27a5",
    "source_lines": "L960-L971",
    "source_section": "31. Business Decisions (Locked) > BD-14-010"
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
  "stable_id": "BD-14-010",
  "title": "Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organizat…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-011 — Toàn bộ tham số hệ thống được quản lý bằng Parameter. Parameter hỗ trợ Override theo Scope

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-011-AC001",
      "given": "the applicable business context, actor, and input for Toàn bộ tham số hệ thống được quản lý bằng Parameter. Parameter hỗ trợ Override theo Scope",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-011-AC002",
      "given": "the applicable business context, actor, and input for Toàn bộ tham số hệ thống được quản lý bằng Parameter. Parameter hỗ trợ Override theo Scope",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "an override is accepted only for a policy marked override-eligible, with an explicit reason and the required approval; otherwise the inherited or system policy remains effective",
      "verifies": [
        "BD-14-011-O002"
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
        "BD-14-011-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-011-O001",
      "obligation_text": "Toàn bộ tham số hệ thống được quản lý bằng Parameter"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-011-O002",
      "obligation_text": "Parameter hỗ trợ Override theo Scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ tham số hệ thống được quản lý bằng Parameter. Parameter hỗ trợ Override theo Scope.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-011",
    "source_context_sha256": "550167cc87b869e7936afdb28c96141b362aab4e5f3cc49bb70ba9fa7694a294",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "2a5866f3e92fe5d19f431dab5aab38d844a55515396188f6fa0a484ba2622dec",
    "source_lines": "L974-L979",
    "source_section": "31. Business Decisions (Locked) > BD-14-011"
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
  "stable_id": "BD-14-011",
  "title": "Toàn bộ tham số hệ thống được quản lý bằng Parameter. Parameter hỗ trợ Override theo Scope",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-012 — Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Impor…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-14-012-AC001",
      "given": "a contract interaction at the integration boundary defined by Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Impor…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-14-012-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-14-012-AC002",
      "given": "a contract interaction at the integration boundary defined by Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Impor…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-14-012-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-14-012-AC003",
      "given": "a contract interaction at the integration boundary defined by Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Impor…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-14-012-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-14-012-AC004",
      "given": "a contract interaction at the integration boundary defined by Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Impor…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-14-012-O004"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-14-012-AC005",
      "given": "a contract interaction at the integration boundary defined by Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Impor…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-14-012-O005"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-14-012-AC006",
      "given": "a contract interaction at the integration boundary defined by Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Impor…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-14-012-O006"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-14-012-AC007",
      "given": "a contract interaction at the integration boundary defined by Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Impor…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-14-012-O007"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-14-012-AC008",
      "given": "an interaction that violates the contract or ownership boundary for Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Impor…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-14-012-O001",
        "BD-14-012-O002",
        "BD-14-012-O003",
        "BD-14-012-O004",
        "BD-14-012-O005",
        "BD-14-012-O006",
        "BD-14-012-O007"
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
        "BD-14-012-AC001",
        "BD-14-012-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O001",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Dynamic Form."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC002",
        "BD-14-012-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O002",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Dynamic API."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC003",
        "BD-14-012-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O003",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Validation."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC004",
        "BD-14-012-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O004",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Import."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC005",
        "BD-14-012-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O005",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Export."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC006",
        "BD-14-012-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O006",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Report Builder."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC007",
        "BD-14-012-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O007",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Dashboard."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Import - Export - Report Builder - Dashboard",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "14. Metadata",
    "source_context_sha256": "5e71733be65b602ceed11ed75d259d10efb1f70342928aafa57143942ec38334",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "0973c98b92f817034cf75f3e6835984ddd8796bf8c15e47f2ad34fb0e22e6328",
    "source_lines": "L982-L995",
    "source_section": "31. Business Decisions (Locked) > BD-14-012"
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
  "stable_id": "BD-14-012",
  "title": "Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Impor…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-013 — Configuration hỗ trợ Version. Lifecycle: Draft ↓ Validate ↓ Approval ↓ Published ↓ Effective

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-013-AC001",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ Version. Lifecycle: Draft ↓ Validate ↓ Approval ↓ Published ↓ Effective",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-013-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-013-AC002",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ Version. Lifecycle: Draft ↓ Validate ↓ Approval ↓ Published ↓ Effective",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BD-14-013-O002"
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
        "BD-14-013-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-013-O001",
      "obligation_text": "Configuration hỗ trợ Version"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-013-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-013-O002",
      "obligation_text": "Lifecycle: Draft ↓ Validate ↓ Approval ↓ Published ↓ Effective"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration hỗ trợ Version. Lifecycle: Draft ↓ Validate ↓ Approval ↓ Published ↓ Effective",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Configuration Version",
    "source_context_sha256": "9208e204d9cb610736822c64809a0e8ced379623045721629805a45957b7c6aa",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "a2326baa7c9a17910595380dd7309a083c1940abba0cb497d71fa5f3b4c53822",
    "source_lines": "L998-L1021",
    "source_section": "31. Business Decisions (Locked) > BD-14-013"
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
  "stable_id": "BD-14-013",
  "title": "Configuration hỗ trợ Version. Lifecycle: Draft ↓ Validate ↓ Approval ↓ Published ↓ Effective",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-014 — Configuration bắt buộc Approval trước Publish. Approval theo Role và Permission

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-014-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration bắt buộc Approval trước Publish. Approval theo Role và Permission",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-014-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-014-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration bắt buộc Approval trước Publish. Approval theo Role và Permission",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-014-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-14-014-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Configuration bắt buộc Approval trước Publish. Approval theo Role và Permission",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-14-014-O001",
        "BD-14-014-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-14-014-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Configuration bắt buộc Approval trước Publish. Approval theo Role và Permission",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-14-014-O001",
        "BD-14-014-O002"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-14-014-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Configuration bắt buộc Approval trước Publish. Approval theo Role và Permission",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-14-014-O001",
        "BD-14-014-O002"
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
        "BD-14-014-AC001",
        "BD-14-014-AC003",
        "BD-14-014-AC004",
        "BD-14-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-014-O001",
      "obligation_text": "Configuration bắt buộc Approval trước Publish"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-014-AC002",
        "BD-14-014-AC003",
        "BD-14-014-AC004",
        "BD-14-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-014-O002",
      "obligation_text": "Approval theo Role và Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-14-014-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-14-014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-14-014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-14-014-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-14-014-AC001",
        "BD-14-014-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-14-014 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration bắt buộc Approval trước Publish. Approval theo Role và Permission.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-014",
    "source_context_sha256": "6ad86f4ee0c202da397039faf58ada876473c44bd24fbff6aa11b8b2f6c33099",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "9011a32f3fc115fb5197ac61eab7152448090e995e495da1c60db01856e8520c",
    "source_lines": "L1024-L1029",
    "source_section": "31. Business Decisions (Locked) > BD-14-014"
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
  "stable_id": "BD-14-014",
  "title": "Configuration bắt buộc Approval trước Publish. Approval theo Role và Permission",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-015 — Configuration hỗ trợ: - Effective From - Effective To

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-015-AC001",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ: - Effective From - Effective To",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-015-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-015-AC002",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ: - Effective From - Effective To",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-015-O002"
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
        "BD-14-015-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-015-O001",
      "obligation_text": "Configuration hỗ trợ: Effective From."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-015-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-015-O002",
      "obligation_text": "Configuration hỗ trợ: Effective To."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration hỗ trợ: - Effective From - Effective To",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Effective Date",
    "source_context_sha256": "0bc95a06ad66f1a7207489557a3f2e1417f67b9873ad312e346a36807fa8c018",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "bb61031e2b821c2c869a16dbf4bd3c2c58266291e8881d2d6c09c2ba5497541c",
    "source_lines": "L1032-L1038",
    "source_section": "31. Business Decisions (Locked) > BD-14-015"
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
  "stable_id": "BD-14-015",
  "title": "Configuration hỗ trợ: - Effective From - Effective To",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-016 — Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-016-AC001",
      "given": "an operational task within the scope of Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-14-016-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-016-AC002",
      "given": "an operational task within the scope of Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-14-016-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-016-AC003",
      "given": "an operational task within the scope of Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-14-016-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-016-AC004",
      "given": "an operational task within the scope of Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-14-016-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-016-AC005",
      "given": "an operational task within the scope of Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-14-016-O005"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-016-AC006",
      "given": "an operational task within the scope of Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-14-016-O006"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-14-016-AC007",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-14-016-O001",
        "BD-14-016-O002",
        "BD-14-016-O003",
        "BD-14-016-O004",
        "BD-14-016-O005",
        "BD-14-016-O006"
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
        "BD-14-016-AC001",
        "BD-14-016-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O001",
      "obligation_text": "Configuration Audit lưu đầy đủ: Who."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-016-AC002",
        "BD-14-016-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O002",
      "obligation_text": "Configuration Audit lưu đầy đủ: When."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-016-AC003",
        "BD-14-016-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O003",
      "obligation_text": "Configuration Audit lưu đầy đủ: Before."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-016-AC004",
        "BD-14-016-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O004",
      "obligation_text": "Configuration Audit lưu đầy đủ: After."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-016-AC005",
        "BD-14-016-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O005",
      "obligation_text": "Configuration Audit lưu đầy đủ: Reason."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-016-AC006",
        "BD-14-016-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O006",
      "obligation_text": "Configuration Audit lưu đầy đủ: Version."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-14-016 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-14-016 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-14-016 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-14-016 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-14-016-AC001",
        "BD-14-016-AC002",
        "BD-14-016-AC003",
        "BD-14-016-AC004",
        "BD-14-016-AC005",
        "BD-14-016-AC006"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-14-016 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-016",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Configuration Audit",
    "source_context_sha256": "499b94c479357d38c562a4af9165c2e4ab7dfd9e08e42abf02e3063255d8b275",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "4018ba43f9de31c594da1230a23a9bc57947d66a926f698714e9cce5b2249b9d",
    "source_lines": "L1041-L1051",
    "source_section": "31. Business Decisions (Locked) > BD-14-016"
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
  "stable_id": "BD-14-016",
  "title": "Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-017 — Configuration hỗ trợ: - JSON - YAML - Excel - CSV Import luôn Validate trước Apply

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-017-AC001",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ: - JSON - YAML - Excel - CSV Import luôn Validate trước Apply",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-017-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-017-AC002",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ: - JSON - YAML - Excel - CSV Import luôn Validate trước Apply",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-017-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-017-AC003",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ: - JSON - YAML - Excel - CSV Import luôn Validate trước Apply",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-017-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-017-AC004",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ: - JSON - YAML - Excel - CSV Import luôn Validate trước Apply",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-017-O004"
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
        "BD-14-017-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-017-O001",
      "obligation_text": "Configuration hỗ trợ: JSON."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-017-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-017-O002",
      "obligation_text": "Configuration hỗ trợ: YAML."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-017-O003",
      "obligation_text": "Configuration hỗ trợ: Excel."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-017-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-017-O004",
      "obligation_text": "Configuration hỗ trợ: CSV Import luôn Validate trước Apply."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration hỗ trợ: - JSON - YAML - Excel - CSV Import luôn Validate trước Apply.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-017",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Effective Date",
    "source_context_sha256": "0bc95a06ad66f1a7207489557a3f2e1417f67b9873ad312e346a36807fa8c018",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "a1b58f97e9329769db2ad68ad5e3f12e9806b44d949a816a885a334973ee3242",
    "source_lines": "L1054-L1064",
    "source_section": "31. Business Decisions (Locked) > BD-14-017"
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
  "stable_id": "BD-14-017",
  "title": "Configuration hỗ trợ: - JSON - YAML - Excel - CSV Import luôn Validate trước Apply",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-018 — Configuration Package hỗ trợ: - Export - Import - Install - Upgrade - Compare - Merge - Rollback

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-018-AC001",
      "given": "the applicable business context, actor, and input for Configuration Package hỗ trợ: - Export - Import - Install - Upgrade - Compare - Merge - Rollback",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-018-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-018-AC002",
      "given": "the applicable business context, actor, and input for Configuration Package hỗ trợ: - Export - Import - Install - Upgrade - Compare - Merge - Rollback",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-018-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-018-AC003",
      "given": "the applicable business context, actor, and input for Configuration Package hỗ trợ: - Export - Import - Install - Upgrade - Compare - Merge - Rollback",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-018-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-018-AC004",
      "given": "the applicable business context, actor, and input for Configuration Package hỗ trợ: - Export - Import - Install - Upgrade - Compare - Merge - Rollback",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-018-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-018-AC005",
      "given": "the applicable business context, actor, and input for Configuration Package hỗ trợ: - Export - Import - Install - Upgrade - Compare - Merge - Rollback",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-018-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-018-AC006",
      "given": "the applicable business context, actor, and input for Configuration Package hỗ trợ: - Export - Import - Install - Upgrade - Compare - Merge - Rollback",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-018-O006"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-018-AC007",
      "given": "the applicable business context, actor, and input for Configuration Package hỗ trợ: - Export - Import - Install - Upgrade - Compare - Merge - Rollback",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-018-O007"
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
        "BD-14-018-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O001",
      "obligation_text": "Configuration Package hỗ trợ: Export."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O002",
      "obligation_text": "Configuration Package hỗ trợ: Import."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O003",
      "obligation_text": "Configuration Package hỗ trợ: Install."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O004",
      "obligation_text": "Configuration Package hỗ trợ: Upgrade."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O005",
      "obligation_text": "Configuration Package hỗ trợ: Compare."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O006",
      "obligation_text": "Configuration Package hỗ trợ: Merge."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O007",
      "obligation_text": "Configuration Package hỗ trợ: Rollback."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration Package hỗ trợ: - Export - Import - Install - Upgrade - Compare - Merge - Rollback",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-018",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Configuration Package",
    "source_context_sha256": "366debe484b4a182ab427a756968011defb86b59a2f877cf67ad1447d48f37e1",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "88542407ec6fa63f75d3ac3d7b9154b5cd2bb023966a4c4b0e369ba66b01c1c0",
    "source_lines": "L1067-L1078",
    "source_section": "31. Business Decisions (Locked) > BD-14-018"
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
  "stable_id": "BD-14-018",
  "title": "Configuration Package hỗ trợ: - Export - Import - Install - Upgrade - Compare - Merge - Rollback",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-019 — Configuration hỗ trợ: - Validation - Dependency - Rollback

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-019-AC001",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ: - Validation - Dependency - Rollback",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-019-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-019-AC002",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ: - Validation - Dependency - Rollback",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-019-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-019-AC003",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ: - Validation - Dependency - Rollback",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-019-O003"
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
        "BD-14-019-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-019-O001",
      "obligation_text": "Configuration hỗ trợ: Validation."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-019-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-019-O002",
      "obligation_text": "Configuration hỗ trợ: Dependency."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-019-O003",
      "obligation_text": "Configuration hỗ trợ: Rollback."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration hỗ trợ: - Validation - Dependency - Rollback",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-019",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Effective Date",
    "source_context_sha256": "0bc95a06ad66f1a7207489557a3f2e1417f67b9873ad312e346a36807fa8c018",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "92069fea02de10dab83e8c3488e312b7cf7101c846f23ddbebe852a24fb0b926",
    "source_lines": "L1081-L1088",
    "source_section": "31. Business Decisions (Locked) > BD-14-019"
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
  "stable_id": "BD-14-019",
  "title": "Configuration hỗ trợ: - Validation - Dependency - Rollback",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-020 — Configuration hỗ trợ nhiều Environment. - Development - UAT - Production

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-020-AC001",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ nhiều Environment. - Development - UAT - Production",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-020-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-14-020-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Configuration hỗ trợ nhiều Environment. - Development - UAT - Production",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-14-020-O001"
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
        "BD-14-020-AC001",
        "BD-14-020-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-020-O001",
      "obligation_text": "Configuration hỗ trợ nhiều Environment. - Development - UAT - Production"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration hỗ trợ nhiều Environment. - Development - UAT - Production",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-020",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "24. Environment Configuration",
    "source_context_sha256": "db58ed47df5e56088e7b7097ba8bb8ed2d0b9ed9806b707ff18e1cb0b4720347",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "e2583f5cfbc23689894c9d9311957858ce9e378ec04db458701970f967d0dc26",
    "source_lines": "L1091-L1098",
    "source_section": "31. Business Decisions (Locked) > BD-14-020"
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
  "stable_id": "BD-14-020",
  "title": "Configuration hỗ trợ nhiều Environment. - Development - UAT - Production",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-021 — Configuration hỗ trợ Runtime Reload. Không yêu cầu Restart đối với đa số Configuration

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-021-AC001",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ Runtime Reload. Không yêu cầu Restart đối với đa số Configuration",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-021-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-021-AC002",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ Runtime Reload. Không yêu cầu Restart đối với đa số Configuration",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-021-O002"
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
        "BD-14-021-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-021-O001",
      "obligation_text": "Configuration hỗ trợ Runtime Reload"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-021-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-021-O002",
      "obligation_text": "Không yêu cầu Restart đối với đa số Configuration"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration hỗ trợ Runtime Reload. Không yêu cầu Restart đối với đa số Configuration.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-021",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Runtime Reload",
    "source_context_sha256": "0a583e1a14b32ca7c248623089f83877941ca3111239950796bab794f3655578",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "7997f79ff46882738c22208429baffbcd6aa180ef40d1f80b599c96e6dcc05e8",
    "source_lines": "L1101-L1106",
    "source_section": "31. Business Decisions (Locked) > BD-14-021"
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
  "stable_id": "BD-14-021",
  "title": "Configuration hỗ trợ Runtime Reload. Không yêu cầu Restart đối với đa số Configuration",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-022 — Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-022-AC001",
      "given": "the applicable business context, actor, and input for Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-022-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-022-AC002",
      "given": "the applicable business context, actor, and input for Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-022-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-022-AC003",
      "given": "the applicable business context, actor, and input for Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-022-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-022-AC004",
      "given": "the applicable business context, actor, and input for Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-022-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-022-AC005",
      "given": "the applicable business context, actor, and input for Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-022-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-022-AC006",
      "given": "the applicable business context, actor, and input for Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-022-O006"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-022-AC007",
      "given": "the applicable business context, actor, and input for Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-022-O007"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-022-AC008",
      "given": "the applicable business context, actor, and input for Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-022-O008"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-022-AC009",
      "given": "the applicable business context, actor, and input for Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-022-O009"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-022-AC010",
      "given": "the applicable business context, actor, and input for Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-14-022-O010"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-022-AC011",
      "given": "the applicable business context, actor, and input for Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-022-O011"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-14-022-AC012",
      "given": "an unsupported or invalid business input at the boundary governed by Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-14-022-O001",
        "BD-14-022-O002",
        "BD-14-022-O003",
        "BD-14-022-O004",
        "BD-14-022-O005",
        "BD-14-022-O006",
        "BD-14-022-O007",
        "BD-14-022-O008",
        "BD-14-022-O009",
        "BD-14-022-O010",
        "BD-14-022-O011"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-14-022-AC013",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-14-022-O001",
        "BD-14-022-O002",
        "BD-14-022-O003",
        "BD-14-022-O004",
        "BD-14-022-O005",
        "BD-14-022-O006",
        "BD-14-022-O007",
        "BD-14-022-O008",
        "BD-14-022-O009",
        "BD-14-022-O010",
        "BD-14-022-O011"
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
        "BD-14-022-AC001",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O001",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Role."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC002",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O002",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Dashboard."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC003",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O003",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Storefront."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC004",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O004",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Theme."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC005",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O005",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Report."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC006",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O006",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Notification."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC007",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O007",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: KB."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC008",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O008",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: FAQ."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC009",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O009",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Survey."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC010",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O010",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Support Policy."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC011",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O011",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Configuration."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-14-022-AC013"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-14-022 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-14-022 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-14-022 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-14-022-AC001",
        "BD-14-022-AC002",
        "BD-14-022-AC003",
        "BD-14-022-AC004",
        "BD-14-022-AC005",
        "BD-14-022-AC006",
        "BD-14-022-AC007",
        "BD-14-022-AC008",
        "BD-14-022-AC009",
        "BD-14-022-AC010",
        "BD-14-022-AC011"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-14-022 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION",
      "exception_id": "P2-CRIT-EXC-002",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dashboard - Storefront - Theme - Report - Notification - KB - FAQ - Survey - Support Policy - Configuration",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-022",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-022",
    "source_context_sha256": "003421397d82fa8e14cd916391ef83590dc9be506c5ce15d5a2f583bd9648235",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "e16f1a5f039a5d630aba44af44edd5d16672b97cc1a05a505dc9bdd77fc4d75f",
    "source_lines": "L1109-L1126",
    "source_section": "31. Business Decisions (Locked) > BD-14-022"
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
  "stable_id": "BD-14-022",
  "title": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dash…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-023 — Configuration áp dụng theo mô hình Layering. Effective Configuration luôn được tính theo Scope

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-023-AC001",
      "given": "the applicable business context, actor, and input for Configuration áp dụng theo mô hình Layering. Effective Configuration luôn được tính theo Scope",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-023-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-023-AC002",
      "given": "the applicable business context, actor, and input for Configuration áp dụng theo mô hình Layering. Effective Configuration luôn được tính theo Scope",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-023-O002"
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
        "BD-14-023-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-023-O001",
      "obligation_text": "Configuration áp dụng theo mô hình Layering"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-023-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-023-O002",
      "obligation_text": "Effective Configuration luôn được tính theo Scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration áp dụng theo mô hình Layering. Effective Configuration luôn được tính theo Scope.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-023",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-023",
    "source_context_sha256": "3d8d746e8ecae7c4abbd9baf9a0a029af03d433c40f0b2bbcd8071c119196200",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "98c863c62315887f2ed50477cc1a94004d073e70adcdd313ab318aab61aeb1d4",
    "source_lines": "L1129-L1134",
    "source_section": "31. Business Decisions (Locked) > BD-14-023"
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
  "stable_id": "BD-14-023",
  "title": "Configuration áp dụng theo mô hình Layering. Effective Configuration luôn được tính theo Scope",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-024 — Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-024-AC001",
      "given": "the applicable business context, actor, and input for Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-024-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-024-AC002",
      "given": "the applicable business context, actor, and input for Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-024-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-024-AC003",
      "given": "the applicable business context, actor, and input for Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-024-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-024-AC004",
      "given": "the applicable business context, actor, and input for Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-024-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-024-AC005",
      "given": "the applicable business context, actor, and input for Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-024-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-024-AC006",
      "given": "the applicable business context, actor, and input for Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-024-O006"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-024-AC007",
      "given": "the applicable business context, actor, and input for Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-024-O007"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-024-AC008",
      "given": "the applicable business context, actor, and input for Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-024-O008"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-024-AC009",
      "given": "the applicable business context, actor, and input for Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-024-O009"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-024-AC010",
      "given": "the applicable business context, actor, and input for Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-024-O010"
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
        "BD-14-024-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O001",
      "obligation_text": "Configuration Capability Matrix xác định: Read."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O002",
      "obligation_text": "Configuration Capability Matrix xác định: Create."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O003",
      "obligation_text": "Configuration Capability Matrix xác định: Edit."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O004",
      "obligation_text": "Configuration Capability Matrix xác định: Delete."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O005",
      "obligation_text": "Configuration Capability Matrix xác định: Override."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O006",
      "obligation_text": "Configuration Capability Matrix xác định: Clone."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O007",
      "obligation_text": "Configuration Capability Matrix xác định: Import."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O008",
      "obligation_text": "Configuration Capability Matrix xác định: Export."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O009",
      "obligation_text": "Configuration Capability Matrix xác định: Approval Required."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O010",
      "obligation_text": "Configuration Capability Matrix xác định: Runtime Reload."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Required - Runtime Reload",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "P2-DEC-005",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-024",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-024",
    "source_context_sha256": "9034c78036b50341510cbd9e086cc75ba9f1386f22a3da1bf9e0e0a9ad692146",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "0c9bdafb145b3c8fd5197d5589b3a6e44dba7746b50d07b80b277988a5b0fcf3",
    "source_lines": "L1137-L1151",
    "source_section": "31. Business Decisions (Locked) > BD-14-024"
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
  "stable_id": "BD-14-024",
  "title": "Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - I…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-025 — Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC003",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O003"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC004",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O004"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC005",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O005"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC006",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O006"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC007",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O007"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC008",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O008"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC009",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O009"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC010",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O010"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC011",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O011"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC012",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O012"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC013",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O013"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC014",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O014"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-14-025-AC015",
      "given": "an identified principal, applicable assurance context, and policy inputs for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-14-025-O015"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-14-025-AC016",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-14-025-O001",
        "BD-14-025-O002",
        "BD-14-025-O003",
        "BD-14-025-O004",
        "BD-14-025-O005",
        "BD-14-025-O006",
        "BD-14-025-O007",
        "BD-14-025-O008",
        "BD-14-025-O009",
        "BD-14-025-O010",
        "BD-14-025-O011",
        "BD-14-025-O012",
        "BD-14-025-O013",
        "BD-14-025-O014",
        "BD-14-025-O015"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-14-025-AC017",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-14-025-O001",
        "BD-14-025-O002",
        "BD-14-025-O003",
        "BD-14-025-O004",
        "BD-14-025-O005",
        "BD-14-025-O006",
        "BD-14-025-O007",
        "BD-14-025-O008",
        "BD-14-025-O009",
        "BD-14-025-O010",
        "BD-14-025-O011",
        "BD-14-025-O012",
        "BD-14-025-O013",
        "BD-14-025-O014",
        "BD-14-025-O015"
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
        "BD-14-025-AC001",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O001",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: System."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC002",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O002",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Organization."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC003",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O003",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Storefront."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC004",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O004",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Commercial."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC005",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O005",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Financial."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC006",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O006",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Notification."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC007",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O007",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Customer."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC008",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O008",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Support."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC009",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O009",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Security."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC010",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O010",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Integration."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC011",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O011",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Workflow."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC012",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O012",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Localization."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC013",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O013",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Reporting."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC014",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O014",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Monitoring."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC015",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O015",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Scheduler."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-14-025 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-14-025 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-14-025 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-14-025-AC017"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-14-025-AC001",
        "BD-14-025-AC002",
        "BD-14-025-AC003",
        "BD-14-025-AC004",
        "BD-14-025-AC005",
        "BD-14-025-AC006",
        "BD-14-025-AC007",
        "BD-14-025-AC008",
        "BD-14-025-AC009",
        "BD-14-025-AC010",
        "BD-14-025-AC011",
        "BD-14-025-AC012",
        "BD-14-025-AC013",
        "BD-14-025-AC014",
        "BD-14-025-AC015"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-14-025 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefront - Commercial - Financial - Notification - Customer - Support - Security - Integration - Workflow - Localization - Reporting - Monitoring - Scheduler",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-025",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-025",
    "source_context_sha256": "7cd9d38c5e6769991d01145dc144e18024b11dfe076e78817787bd1be482262f",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "aec37224683c1f556fdf700bd3239c893ad8a6b61447764e6c7726a79b919409",
    "source_lines": "L1154-L1175",
    "source_section": "31. Business Decisions (Locked) > BD-14-025"
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
  "stable_id": "BD-14-025",
  "title": "Configuration được phân nhóm theo Category. Category mặc định: - System - Organization - Storefr…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-026 — Configuration Dependency Graph hỗ trợ: - Dependency Analysis - Impact Analysis - Upgrade Plannin…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-026-AC001",
      "given": "the applicable business context, actor, and input for Configuration Dependency Graph hỗ trợ: - Dependency Analysis - Impact Analysis - Upgrade Plannin…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-026-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-026-AC002",
      "given": "the applicable business context, actor, and input for Configuration Dependency Graph hỗ trợ: - Dependency Analysis - Impact Analysis - Upgrade Plannin…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-026-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-026-AC003",
      "given": "the applicable business context, actor, and input for Configuration Dependency Graph hỗ trợ: - Dependency Analysis - Impact Analysis - Upgrade Plannin…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-026-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-026-AC004",
      "given": "the applicable business context, actor, and input for Configuration Dependency Graph hỗ trợ: - Dependency Analysis - Impact Analysis - Upgrade Plannin…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-026-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-14-026-AC005",
      "given": "the applicable business context, actor, and input for Configuration Dependency Graph hỗ trợ: - Dependency Analysis - Impact Analysis - Upgrade Plannin…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-14-026-O005"
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
        "BD-14-026-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-026-O001",
      "obligation_text": "Configuration Dependency Graph hỗ trợ: Dependency Analysis."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-026-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-026-O002",
      "obligation_text": "Configuration Dependency Graph hỗ trợ: Impact Analysis."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-026-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-026-O003",
      "obligation_text": "Configuration Dependency Graph hỗ trợ: Upgrade Planning."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-026-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-026-O004",
      "obligation_text": "Configuration Dependency Graph hỗ trợ: Publish Validation."
    },
    {
      "acceptance_criterion_references": [
        "BD-14-026-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-026-O005",
      "obligation_text": "Configuration Dependency Graph hỗ trợ: Rollback."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration Dependency Graph hỗ trợ: - Dependency Analysis - Impact Analysis - Upgrade Planning - Publish Validation - Rollback",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-026",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-026",
    "source_context_sha256": "f74bca7a641eda69ca72d2c1db49dc764423a08ec9aee6a2075d96c3e4d707f8",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "9f2cb8cbac110b27695a918a74f52f85545f6cb23712837b59ebaf8b3d4c909d",
    "source_lines": "L1178-L1187",
    "source_section": "31. Business Decisions (Locked) > BD-14-026"
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
  "stable_id": "BD-14-026",
  "title": "Configuration Dependency Graph hỗ trợ: - Dependency Analysis - Impact Analysis - Upgrade Plannin…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R001 — Configuration luôn được tính theo mô hình **Effective Configuration**

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R001-AC001",
      "given": "the applicable business context, actor, and input for Configuration luôn được tính theo mô hình **Effective Configuration**",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R001-O001"
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
        "BRD-WS-14-R001-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R001-O001",
      "obligation_text": "Configuration luôn được tính theo mô hình **Effective Configuration**"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration luôn được tính theo mô hình **Effective Configuration**.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-001",
    "previous_temporary_key": "TMP-BRD-WS-14-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Configuration Scope",
    "source_context_sha256": "3c00a3b8e83af1a79299293f4bed5adb860fb385ab6d3bd6f8ecd5a047619f05",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "8aa6645dd4d3c742667bceacb98f68b2b7162a446e8a4856f3014f3ddcf4e2b9",
    "source_lines": "L84",
    "source_section": "3. Configuration Scope"
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
  "stable_id": "BRD-WS-14-R001",
  "title": "Configuration luôn được tính theo mô hình **Effective Configuration**",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R003 — Reference Data không được Hard-code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R003-AC001",
      "given": "the applicable business context, actor, and input for Reference Data không được Hard-code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R003-O001"
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
        "BRD-WS-14-R003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R003-O001",
      "obligation_text": "Reference Data không được Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference Data không được Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-003",
    "previous_temporary_key": "TMP-BRD-WS-14-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Data",
    "source_context_sha256": "8159a2e679167d6d72d40b009066fd1f2181eed5a5122ec29675371dcf1ef8de",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "49b81ff9c12144b91925f782a4abfb9deb91d18565f755d85e1f8c4ee681b169",
    "source_lines": "L170",
    "source_section": "5. Reference Data"
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
  "stable_id": "BRD-WS-14-R003",
  "title": "Reference Data không được Hard-code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R004 — Business Rule không được Hard-code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R004-AC001",
      "given": "the applicable business context, actor, and input for Business Rule không được Hard-code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R004-O001"
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
        "BRD-WS-14-R004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R004-O001",
      "obligation_text": "Business Rule không được Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule không được Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-004",
    "previous_temporary_key": "TMP-BRD-WS-14-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Business Rule Engine",
    "source_context_sha256": "86d3ad94506a400c239a818b3540c68c8fa7011a8692d42b51ff06ebc3155e51",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "90e5cb967f6f2ec9469be9f2a4d8ab1348db614d108d8d4e635ca0e65c3db3ed",
    "source_lines": "L247",
    "source_section": "8. Business Rule Engine"
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
  "stable_id": "BRD-WS-14-R004",
  "title": "Business Rule không được Hard-code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R005 — Business Rule luôn lưu: - Current Version

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R005-AC001",
      "given": "the applicable business context, actor, and input for Business Rule luôn lưu: - Current Version",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R005-O001"
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
        "BRD-WS-14-R005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R005-O001",
      "obligation_text": "Business Rule luôn lưu: - Current Version"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule luôn lưu: - Current Version",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-005",
    "previous_temporary_key": "TMP-BRD-WS-14-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Rule Version",
    "source_context_sha256": "ab1b1ad48bf5cdab8738f643014270672ff5f3a35d0fe875698ff5521c5cd742",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "80b3165c8920f2cbf590bf42254c396f19cc62fe4d8fa2e1e53dbf57acf52fb7",
    "source_lines": "L297-L299",
    "source_section": "11. Rule Version"
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
  "stable_id": "BRD-WS-14-R005",
  "title": "Business Rule luôn lưu: - Current Version",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R006 — Business Rule luôn lưu: - Modified By

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R006-AC001",
      "given": "the applicable business context, actor, and input for Business Rule luôn lưu: - Modified By",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R006-O001"
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
        "BRD-WS-14-R006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R006-O001",
      "obligation_text": "Business Rule luôn lưu: - Modified By"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule luôn lưu: - Modified By",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-006",
    "previous_temporary_key": "TMP-BRD-WS-14-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Rule Version",
    "source_context_sha256": "ab1b1ad48bf5cdab8738f643014270672ff5f3a35d0fe875698ff5521c5cd742",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "3ee1599defc9361644dc77c1b700a40e94d8c4447f1161ffff6f9e86820d2989",
    "source_lines": "L297-L300",
    "source_section": "11. Rule Version"
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
  "stable_id": "BRD-WS-14-R006",
  "title": "Business Rule luôn lưu: - Modified By",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R007 — Business Rule luôn lưu: - Modified Time

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R007-AC001",
      "given": "the applicable business context, actor, and input for Business Rule luôn lưu: - Modified Time",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R007-O001"
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
        "BRD-WS-14-R007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R007-O001",
      "obligation_text": "Business Rule luôn lưu: - Modified Time"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule luôn lưu: - Modified Time",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-007",
    "previous_temporary_key": "TMP-BRD-WS-14-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Rule Version",
    "source_context_sha256": "ab1b1ad48bf5cdab8738f643014270672ff5f3a35d0fe875698ff5521c5cd742",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "c3f26a8f634423f21f9b89aaaae62ad8431244ac6b3f9bd76af46f9abb036246",
    "source_lines": "L297-L301",
    "source_section": "11. Rule Version"
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
  "stable_id": "BRD-WS-14-R007",
  "title": "Business Rule luôn lưu: - Modified Time",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R008 — Business Rule luôn lưu: - Change Summary

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R008-AC001",
      "given": "the applicable business context, actor, and input for Business Rule luôn lưu: - Change Summary",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R008-O001"
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
        "BRD-WS-14-R008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R008-O001",
      "obligation_text": "Business Rule luôn lưu: - Change Summary"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule luôn lưu: - Change Summary",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-008",
    "previous_temporary_key": "TMP-BRD-WS-14-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Rule Version",
    "source_context_sha256": "ab1b1ad48bf5cdab8738f643014270672ff5f3a35d0fe875698ff5521c5cd742",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "299a93daef3859d45c3cc8120e0219e5ba74d8a352fff1dddce8cf3b9cf540da",
    "source_lines": "L297-L302",
    "source_section": "11. Rule Version"
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
  "stable_id": "BRD-WS-14-R008",
  "title": "Business Rule luôn lưu: - Change Summary",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R009 — Lịch sử thay đổi không được phép xóa

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R009-AC001",
      "given": "the applicable business context, actor, and input for Lịch sử thay đổi không được phép xóa",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-14-R009-O001"
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
        "BRD-WS-14-R009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R009-O001",
      "obligation_text": "Lịch sử thay đổi không được phép xóa"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Lịch sử thay đổi không được phép xóa.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-009",
    "previous_temporary_key": "TMP-BRD-WS-14-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Rule Version",
    "source_context_sha256": "ab1b1ad48bf5cdab8738f643014270672ff5f3a35d0fe875698ff5521c5cd742",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "a6209cfee7468cae1bb99a4d2be50e791bb98ccdcad2226c3c90249412ba6295",
    "source_lines": "L304",
    "source_section": "11. Rule Version"
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
  "stable_id": "BRD-WS-14-R009",
  "title": "Lịch sử thay đổi không được phép xóa",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R010 — Feature Flag luôn được Runtime Reload

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R010-AC001",
      "given": "the applicable business context, actor, and input for Feature Flag luôn được Runtime Reload",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R010-O001"
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
        "BRD-WS-14-R010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R010-O001",
      "obligation_text": "Feature Flag luôn được Runtime Reload"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Feature Flag luôn được Runtime Reload.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-010",
    "previous_temporary_key": "TMP-BRD-WS-14-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Feature Flag",
    "source_context_sha256": "204d9be3f380c835b46acde0e0d1a208bbeb7d1bdae6185234f488636af7499b",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "8fbe32b693b61843cd8e52fe90068741253502d14ec8982b2404373847584bd9",
    "source_lines": "L330",
    "source_section": "12. Feature Flag"
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
  "stable_id": "BRD-WS-14-R010",
  "title": "Feature Flag luôn được Runtime Reload",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R011 — Parameter không được Hard-code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R011-AC001",
      "given": "the applicable business context, actor, and input for Parameter không được Hard-code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R011-O001"
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
        "BRD-WS-14-R011-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R011-O001",
      "obligation_text": "Parameter không được Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Parameter không được Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-011",
    "previous_temporary_key": "TMP-BRD-WS-14-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Parameter",
    "source_context_sha256": "60de64cbad1b9e489d51a5cf556eb83f143111fdf49a711bcf60edcf82db3d94",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "40dc5ad6ace9ca40c52597b260c4470d50f2b796bced0d30e69100104d989996",
    "source_lines": "L359",
    "source_section": "13. Parameter"
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
  "stable_id": "BRD-WS-14-R011",
  "title": "Parameter không được Hard-code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R012 — Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC003",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O003"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC004",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O004"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC005",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O005"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC006",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O006"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC007",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O007"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC008",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O008"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC009",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O009"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC010",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O010"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC011",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O011"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC012",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O012"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC013",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O013"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R012-AC014",
      "given": "an identified principal, applicable assurance context, and policy inputs for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-14-R012-O014"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-14-R012-AC015",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-14-R012-O001",
        "BRD-WS-14-R012-O002",
        "BRD-WS-14-R012-O003",
        "BRD-WS-14-R012-O004",
        "BRD-WS-14-R012-O005",
        "BRD-WS-14-R012-O006",
        "BRD-WS-14-R012-O007",
        "BRD-WS-14-R012-O008",
        "BRD-WS-14-R012-O009",
        "BRD-WS-14-R012-O010",
        "BRD-WS-14-R012-O011",
        "BRD-WS-14-R012-O012",
        "BRD-WS-14-R012-O013",
        "BRD-WS-14-R012-O014"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-14-R012-AC016",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-14-R012-O001",
        "BRD-WS-14-R012-O002",
        "BRD-WS-14-R012-O003",
        "BRD-WS-14-R012-O004",
        "BRD-WS-14-R012-O005",
        "BRD-WS-14-R012-O006",
        "BRD-WS-14-R012-O007",
        "BRD-WS-14-R012-O008",
        "BRD-WS-14-R012-O009",
        "BRD-WS-14-R012-O010",
        "BRD-WS-14-R012-O011",
        "BRD-WS-14-R012-O012",
        "BRD-WS-14-R012-O013",
        "BRD-WS-14-R012-O014"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-14-R012-AC017",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-14-R012-O001",
        "BRD-WS-14-R012-O002",
        "BRD-WS-14-R012-O003",
        "BRD-WS-14-R012-O004",
        "BRD-WS-14-R012-O005",
        "BRD-WS-14-R012-O006",
        "BRD-WS-14-R012-O007",
        "BRD-WS-14-R012-O008",
        "BRD-WS-14-R012-O009",
        "BRD-WS-14-R012-O010",
        "BRD-WS-14-R012-O011",
        "BRD-WS-14-R012-O012",
        "BRD-WS-14-R012-O013",
        "BRD-WS-14-R012-O014"
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
        "BRD-WS-14-R012-AC001",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O001",
      "obligation_text": "Bao gồm: Field Name."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC002",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O002",
      "obligation_text": "Bao gồm: Data Type."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC003",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O003",
      "obligation_text": "Bao gồm: Required."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC004",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O004",
      "obligation_text": "Bao gồm: Default Value."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC005",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O005",
      "obligation_text": "Bao gồm: Validation Rule."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC006",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O006",
      "obligation_text": "Bao gồm: Searchable."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC007",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O007",
      "obligation_text": "Bao gồm: Sortable."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC008",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O008",
      "obligation_text": "Bao gồm: Filterable."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC009",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O009",
      "obligation_text": "Bao gồm: Exportable."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC010",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O010",
      "obligation_text": "Bao gồm: Importable."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC011",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O011",
      "obligation_text": "Bao gồm: Permission."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC012",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O012",
      "obligation_text": "Bao gồm: Localization."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC013",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O013",
      "obligation_text": "Bao gồm: Tooltip."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R012-AC014",
        "BRD-WS-14-R012-AC015",
        "BRD-WS-14-R012-AC016",
        "BRD-WS-14-R012-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O014",
      "obligation_text": "Bao gồm: Description."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-14-R012-AC017"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R012 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R012 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-14-R012-AC016"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-14-R012-AC001",
        "BRD-WS-14-R012-AC002",
        "BRD-WS-14-R012-AC003",
        "BRD-WS-14-R012-AC004",
        "BRD-WS-14-R012-AC005",
        "BRD-WS-14-R012-AC006",
        "BRD-WS-14-R012-AC007",
        "BRD-WS-14-R012-AC008",
        "BRD-WS-14-R012-AC009",
        "BRD-WS-14-R012-AC010",
        "BRD-WS-14-R012-AC011",
        "BRD-WS-14-R012-AC012",
        "BRD-WS-14-R012-AC013",
        "BRD-WS-14-R012-AC014"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R012 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - Sortable - Filterable - Exportable - Importable - Permission - Localization - Tooltip - Description",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-012",
    "previous_temporary_key": "TMP-BRD-WS-14-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "1. Workshop Objective",
    "source_context_sha256": "4874f7decb0ca7427cd9840d305561e668d5b5e66020de3c80501b800cb88c47",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "5ab75ac869cbf9e45f90f5dab00610aaa6e07c625f2f72a78159885dca9f486e",
    "source_lines": "L369-L384",
    "source_section": "14. Metadata"
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
  "stable_id": "BRD-WS-14-R012",
  "title": "Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - So…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R013 — Version cũ luôn được lưu lại

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R013-AC001",
      "given": "the applicable business context, actor, and input for Version cũ luôn được lưu lại",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R013-O001"
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
        "BRD-WS-14-R013-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R013-O001",
      "obligation_text": "Version cũ luôn được lưu lại"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Version cũ luôn được lưu lại.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-013",
    "previous_temporary_key": "TMP-BRD-WS-14-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Configuration Version",
    "source_context_sha256": "9208e204d9cb610736822c64809a0e8ced379623045721629805a45957b7c6aa",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "288b245850188ca6d4a926ffb1fd897e1cb765f3cc259150b14c3dd1f0031ca9",
    "source_lines": "L427",
    "source_section": "15. Configuration Version"
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
  "stable_id": "BRD-WS-14-R013",
  "title": "Version cũ luôn được lưu lại",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R014 — Configuration phải được Approval trước khi Publish

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R014-AC001",
      "given": "the applicable business context, actor, and input for Configuration phải được Approval trước khi Publish",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R014-O001"
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
        "BRD-WS-14-R014-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R014-O001",
      "obligation_text": "Configuration phải được Approval trước khi Publish"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration phải được Approval trước khi Publish.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-014",
    "previous_temporary_key": "TMP-BRD-WS-14-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Configuration Approval",
    "source_context_sha256": "3bb25c09716b706f3f5b52c9bce5867fd8afef316dcf02b0b78e9cb603a21fca",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "125bf18516e0d78b8ddb3b0e0ffcee0dae95f3872b3ba9a8de4a30e62f90ba43",
    "source_lines": "L444",
    "source_section": "16. Configuration Approval"
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
  "stable_id": "BRD-WS-14-R014",
  "title": "Configuration phải được Approval trước khi Publish",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R015 — Audit không được chỉnh sửa

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R015-AC001",
      "given": "an operational task within the scope of Audit không được chỉnh sửa",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-14-R015-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-14-R015-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Audit không được chỉnh sửa",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-14-R015-O001"
      ],
      "when": "operational verification is performed"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-14-R015-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Audit không được chỉnh sửa",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-14-R015-O001"
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
        "BRD-WS-14-R015-AC001",
        "BRD-WS-14-R015-AC002",
        "BRD-WS-14-R015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R015-O001",
      "obligation_text": "Audit không được chỉnh sửa"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R015 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R015 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R015 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-14-R015-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-14-R015-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R015 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Audit không được chỉnh sửa.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-015",
    "previous_temporary_key": "TMP-BRD-WS-14-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Configuration Audit",
    "source_context_sha256": "499b94c479357d38c562a4af9165c2e4ab7dfd9e08e42abf02e3063255d8b275",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "0524c178daee01147c8b0e4c6eb12a0a656aef82c0fb2abe7ad931e173909b5b",
    "source_lines": "L490",
    "source_section": "18. Configuration Audit"
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
  "stable_id": "BRD-WS-14-R015",
  "title": "Audit không được chỉnh sửa",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R016 — Audit luôn được lưu vĩnh viễn theo chính sách lưu trữ của Platform

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R016-AC001",
      "given": "an operational task within the scope of Audit luôn được lưu vĩnh viễn theo chính sách lưu trữ của Platform",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-14-R016-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-14-R016-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Audit luôn được lưu vĩnh viễn theo chính sách lưu trữ của Platform",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-14-R016-O001"
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
        "BRD-WS-14-R016-AC001",
        "BRD-WS-14-R016-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R016-O001",
      "obligation_text": "Audit luôn được lưu vĩnh viễn theo chính sách lưu trữ của Platform"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R016 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R016 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R016 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R016 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-14-R016-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R016 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Audit luôn được lưu vĩnh viễn theo chính sách lưu trữ của Platform.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-016",
    "previous_temporary_key": "TMP-BRD-WS-14-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Configuration Audit",
    "source_context_sha256": "499b94c479357d38c562a4af9165c2e4ab7dfd9e08e42abf02e3063255d8b275",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "b3ee3224cf7da6525e86cec8bce75ea2f112c752034dc30a4c172bf7b902b02b",
    "source_lines": "L492",
    "source_section": "18. Configuration Audit"
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
  "stable_id": "BRD-WS-14-R016",
  "title": "Audit luôn được lưu vĩnh viễn theo chính sách lưu trữ của Platform",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R017 — Import luôn thực hiện: - Validation

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R017-AC001",
      "given": "the applicable business context, actor, and input for Import luôn thực hiện: - Validation",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R017-O001"
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
        "BRD-WS-14-R017-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R017-O001",
      "obligation_text": "Import luôn thực hiện: - Validation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Import luôn thực hiện: - Validation",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-017",
    "previous_temporary_key": "TMP-BRD-WS-14-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Configuration Import / Export",
    "source_context_sha256": "7b198993b105ff0f945dc8b61fa12277636725c7ef9fe6e56615a7605c97cf86",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "48a37fce4c451b429099515722cfd5b3a91e809622f3d7d8d586e22a01809603",
    "source_lines": "L507-L509",
    "source_section": "19. Configuration Import / Export"
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
  "stable_id": "BRD-WS-14-R017",
  "title": "Import luôn thực hiện: - Validation",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R018 — Import luôn thực hiện: - Dependency Check

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R018-AC001",
      "given": "the applicable business context, actor, and input for Import luôn thực hiện: - Dependency Check",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R018-O001"
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
        "BRD-WS-14-R018-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R018-O001",
      "obligation_text": "Import luôn thực hiện: - Dependency Check"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Import luôn thực hiện: - Dependency Check",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-018",
    "previous_temporary_key": "TMP-BRD-WS-14-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Configuration Import / Export",
    "source_context_sha256": "7b198993b105ff0f945dc8b61fa12277636725c7ef9fe6e56615a7605c97cf86",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "fb8710f4166f7518b722cbabac8a4a55f2d123226b46f579a1c08a40e6ccb1d5",
    "source_lines": "L507-L510",
    "source_section": "19. Configuration Import / Export"
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
  "stable_id": "BRD-WS-14-R018",
  "title": "Import luôn thực hiện: - Dependency Check",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R019 — Import luôn thực hiện: - Conflict Check

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R019-AC001",
      "given": "the applicable business context, actor, and input for Import luôn thực hiện: - Conflict Check",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R019-O001"
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
        "BRD-WS-14-R019-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R019-O001",
      "obligation_text": "Import luôn thực hiện: - Conflict Check"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Import luôn thực hiện: - Conflict Check",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-019",
    "previous_temporary_key": "TMP-BRD-WS-14-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Configuration Import / Export",
    "source_context_sha256": "7b198993b105ff0f945dc8b61fa12277636725c7ef9fe6e56615a7605c97cf86",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "17d207dbaba675f368f5684576a26769da9fa47e7e90920ba1ce5b3de86ffaa3",
    "source_lines": "L507-L511",
    "source_section": "19. Configuration Import / Export"
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
  "stable_id": "BRD-WS-14-R019",
  "title": "Import luôn thực hiện: - Conflict Check",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R020 — Configuration phải được Validate trước khi Save và trước khi Publish

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R020-AC001",
      "given": "the applicable business context, actor, and input for Configuration phải được Validate trước khi Save và trước khi Publish",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R020-O001"
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
        "BRD-WS-14-R020-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R020-O001",
      "obligation_text": "Configuration phải được Validate trước khi Save và trước khi Publish"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration phải được Validate trước khi Save và trước khi Publish.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-020",
    "previous_temporary_key": "TMP-BRD-WS-14-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Configuration Validation",
    "source_context_sha256": "7e296e84b5fa0a380313d73d69f85e94ab0ba42b1712e059ae67d697bdd7083b",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "f26bbcfa2124f01092953373cb7b45fa97001e9bf83db2d7762352f8e6fa6f51",
    "source_lines": "L553",
    "source_section": "21. Configuration Validation"
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
  "stable_id": "BRD-WS-14-R020",
  "title": "Configuration phải được Validate trước khi Save và trước khi Publish",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R021 — Configuration không hợp lệ không được phép Publish

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R021-AC001",
      "given": "the applicable business context, actor, and input for Configuration không hợp lệ không được phép Publish",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R021-O001"
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
        "BRD-WS-14-R021-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R021-O001",
      "obligation_text": "Configuration không hợp lệ không được phép Publish"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration không hợp lệ không được phép Publish.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-021",
    "previous_temporary_key": "TMP-BRD-WS-14-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Configuration Validation",
    "source_context_sha256": "7e296e84b5fa0a380313d73d69f85e94ab0ba42b1712e059ae67d697bdd7083b",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "1493ddac14ea07c37a234488d9b01d25888cf82079e7cd7080d8a1724e0090bf",
    "source_lines": "L570",
    "source_section": "21. Configuration Validation"
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
  "stable_id": "BRD-WS-14-R021",
  "title": "Configuration không hợp lệ không được phép Publish",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R022 — Rollback không được làm mất: - Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R022-AC001",
      "given": "an operational task within the scope of Rollback không được làm mất: - Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-14-R022-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-14-R022-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Rollback không được làm mất: - Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-14-R022-O001"
      ],
      "when": "operational verification is performed"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-14-R022-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Rollback không được làm mất: - Audit",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-14-R022-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "RECOVERY",
      "controlled_contract": "EXPLICIT_RECOVERY_CONTRACT_V1",
      "criterion_id": "BRD-WS-14-R022-AC004",
      "given": "a failed or interrupted case for which Rollback không được làm mất: - Audit explicitly defines recovery, restore, rollback, or fallback behavior",
      "observable_evidence": "pre-failure state, recovery action, resulting state, outcome, and recovery evidence named by the obligation",
      "then": "the resulting state and outcome follow the requirement-specific recovery obligation and expose whether recovery completed or failed",
      "verifies": [
        "BRD-WS-14-R022-O001"
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
        "BRD-WS-14-R022-AC001",
        "BRD-WS-14-R022-AC002",
        "BRD-WS-14-R022-AC003",
        "BRD-WS-14-R022-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R022-O001",
      "obligation_text": "Rollback không được làm mất: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R022 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R022 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-14-R022 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-14-R022-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-14-R022-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [
        "BRD-WS-14-R022-AC004"
      ],
      "status": "APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Rollback không được làm mất: - Audit",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-022",
    "previous_temporary_key": "TMP-BRD-WS-14-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Configuration Rollback",
    "source_context_sha256": "9c7682701e01006a7c022c53b6cfdc365351db2e6f2aabe4c649e85538d65df9",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "b0db4e81ec219cb517f7c9eb3c45f0c65862f663d01ce155b603f666c8e24721",
    "source_lines": "L589-L591",
    "source_section": "22. Configuration Rollback"
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
  "stable_id": "BRD-WS-14-R022",
  "title": "Rollback không được làm mất: - Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R023 — Rollback không được làm mất: - Version History

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R023-AC001",
      "given": "the applicable business context, actor, and input for Rollback không được làm mất: - Version History",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-14-R023-O001"
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
        "BRD-WS-14-R023-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R023-O001",
      "obligation_text": "Rollback không được làm mất: - Version History"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Rollback không được làm mất: - Version History",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-023",
    "previous_temporary_key": "TMP-BRD-WS-14-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Configuration Rollback",
    "source_context_sha256": "9c7682701e01006a7c022c53b6cfdc365351db2e6f2aabe4c649e85538d65df9",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "95d63de08217c62b335c1da8882895b2b73da56b0c8224238fc5c5f992453bb7",
    "source_lines": "L589-L592",
    "source_section": "22. Configuration Rollback"
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
  "stable_id": "BRD-WS-14-R023",
  "title": "Rollback không được làm mất: - Version History",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R024 — Rollback không được làm mất: - Approval History

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R024-AC001",
      "given": "the applicable business context, actor, and input for Rollback không được làm mất: - Approval History",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-14-R024-O001"
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
        "BRD-WS-14-R024-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R024-O001",
      "obligation_text": "Rollback không được làm mất: - Approval History"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Rollback không được làm mất: - Approval History",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-024",
    "previous_temporary_key": "TMP-BRD-WS-14-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Configuration Rollback",
    "source_context_sha256": "9c7682701e01006a7c022c53b6cfdc365351db2e6f2aabe4c649e85538d65df9",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "7b16577682a8890665aa753344b2981ced95deb4b396f3b19faf79177631dbb9",
    "source_lines": "L589-L593",
    "source_section": "22. Configuration Rollback"
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
  "stable_id": "BRD-WS-14-R024",
  "title": "Rollback không được làm mất: - Approval History",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R025 — Rollback luôn tạo một Version mới

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R025-AC001",
      "given": "the applicable business context, actor, and input for Rollback luôn tạo một Version mới",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R025-O001"
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
        "BRD-WS-14-R025-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R025-O001",
      "obligation_text": "Rollback luôn tạo một Version mới"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Rollback luôn tạo một Version mới.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-025",
    "previous_temporary_key": "TMP-BRD-WS-14-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Configuration Rollback",
    "source_context_sha256": "9c7682701e01006a7c022c53b6cfdc365351db2e6f2aabe4c649e85538d65df9",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "55d489bc18404f4017ab8ccc5eb3aa9f82976f5831919ae0a22f62925b7a8e84",
    "source_lines": "L595",
    "source_section": "22. Configuration Rollback"
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
  "stable_id": "BRD-WS-14-R025",
  "title": "Rollback luôn tạo một Version mới",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R026 — Một số Configuration đặc biệt có thể yêu cầu Restart và phải được cảnh báo trước khi Publish

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R026-AC001",
      "given": "the applicable business context, actor, and input for Một số Configuration đặc biệt có thể yêu cầu Restart và phải được cảnh báo trước khi Publish",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R026-O001"
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
        "BRD-WS-14-R026-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R026-O001",
      "obligation_text": "Một số Configuration đặc biệt có thể yêu cầu Restart và phải được cảnh báo trước khi Publish"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một số Configuration đặc biệt có thể yêu cầu Restart và phải được cảnh báo trước khi Publish.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-026",
    "previous_temporary_key": "TMP-BRD-WS-14-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Runtime Reload",
    "source_context_sha256": "0a583e1a14b32ca7c248623089f83877941ca3111239950796bab794f3655578",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "26be61dae2a993e528a201f0e6e7c80982ba0e7eb7acc4bf8985a21175483ce2",
    "source_lines": "L664",
    "source_section": "25. Runtime Reload"
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
  "stable_id": "BRD-WS-14-R026",
  "title": "Một số Configuration đặc biệt có thể yêu cầu Restart và phải được cảnh báo trước khi Publish",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R028 — Không phải mọi Configuration đều được phép Override

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R028-AC001",
      "given": "the applicable business context, actor, and input for Không phải mọi Configuration đều được phép Override",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R028-O001"
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
        "BRD-WS-14-R028-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R028-O001",
      "obligation_text": "Không phải mọi Configuration đều được phép Override"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không phải mọi Configuration đều được phép Override.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-028",
    "previous_temporary_key": "TMP-BRD-WS-14-028",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Configuration Capability Matrix",
    "source_context_sha256": "4bc030377a312b1ed32caa33297f3cd1a7bfe2c327bd8ce60a7f10ea752baeab",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "7a5dd8629eaa6ae44e16a830d4952a841071d88d5f4fb7f7d22a7216a7eab3d3",
    "source_lines": "L751",
    "source_section": "28. Configuration Capability Matrix"
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
  "stable_id": "BRD-WS-14-R028",
  "title": "Không phải mọi Configuration đều được phép Override",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R029 — Mỗi Configuration phải định nghĩa Capability Matrix

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R029-AC001",
      "given": "the applicable business context, actor, and input for Mỗi Configuration phải định nghĩa Capability Matrix",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R029-O001"
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
        "BRD-WS-14-R029-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R029-O001",
      "obligation_text": "Mỗi Configuration phải định nghĩa Capability Matrix"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Configuration phải định nghĩa Capability Matrix.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-029",
    "previous_temporary_key": "TMP-BRD-WS-14-029",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Configuration Capability Matrix",
    "source_context_sha256": "4bc030377a312b1ed32caa33297f3cd1a7bfe2c327bd8ce60a7f10ea752baeab",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
    "source_lines": "L753",
    "source_section": "28. Configuration Capability Matrix"
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
  "stable_id": "BRD-WS-14-R029",
  "title": "Mỗi Configuration phải định nghĩa Capability Matrix",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R030 — Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R030-AC001",
      "given": "the applicable business context, actor, and input for Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R030-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R030-AC002",
      "given": "the applicable business context, actor, and input for Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R030-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R030-AC003",
      "given": "the applicable business context, actor, and input for Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R030-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R030-AC004",
      "given": "the applicable business context, actor, and input for Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R030-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R030-AC005",
      "given": "the applicable business context, actor, and input for Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "an override is accepted only for a policy marked override-eligible, with an explicit reason and the required approval; otherwise the inherited or system policy remains effective",
      "verifies": [
        "BRD-WS-14-R030-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R030-AC006",
      "given": "the applicable business context, actor, and input for Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R030-O006"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R030-AC007",
      "given": "the applicable business context, actor, and input for Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R030-O007"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R030-AC008",
      "given": "the applicable business context, actor, and input for Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R030-O008"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R030-AC009",
      "given": "the applicable business context, actor, and input for Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-WS-14-R030-O009"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R030-AC010",
      "given": "the applicable business context, actor, and input for Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R030-O010"
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
        "BRD-WS-14-R030-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R030-O001",
      "obligation_text": "Bao gồm: Read."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R030-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R030-O002",
      "obligation_text": "Bao gồm: Create."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R030-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R030-O003",
      "obligation_text": "Bao gồm: Edit."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R030-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R030-O004",
      "obligation_text": "Bao gồm: Delete."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R030-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R030-O005",
      "obligation_text": "Bao gồm: Override."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R030-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R030-O006",
      "obligation_text": "Bao gồm: Clone."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R030-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R030-O007",
      "obligation_text": "Bao gồm: Import."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R030-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R030-O008",
      "obligation_text": "Bao gồm: Export."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R030-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R030-O009",
      "obligation_text": "Bao gồm: Approval Required."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R030-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R030-O010",
      "obligation_text": "Bao gồm: Runtime Reload Supported."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Required - Runtime Reload Supported",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-030",
    "previous_temporary_key": "TMP-BRD-WS-14-030",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "1. Workshop Objective",
    "source_context_sha256": "4874f7decb0ca7427cd9840d305561e668d5b5e66020de3c80501b800cb88c47",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "ce1d0a5b4062200dd152903c1c3dc033dfb45004c6db516f5a3f3fd8aa749962",
    "source_lines": "L755-L766",
    "source_section": "28. Configuration Capability Matrix"
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
  "stable_id": "BRD-WS-14-R030",
  "title": "Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Require…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R031 — Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Cap…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R031-AC001",
      "given": "the applicable business context, actor, and input for Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Cap…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R031-O001"
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
        "BRD-WS-14-R031-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R031-O001",
      "obligation_text": "Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Capability bị ảnh hưởng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Capability bị ảnh hưởng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-031",
    "previous_temporary_key": "TMP-BRD-WS-14-031",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Configuration Dependency Graph",
    "source_context_sha256": "409a86828940697f85ca0e45a62a08462d6afeaf394e836409fc84414fc34939",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
    "source_lines": "L851",
    "source_section": "30. Configuration Dependency Graph"
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
  "stable_id": "BRD-WS-14-R031",
  "title": "Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Cap…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R032 — Nguyên tắc: - Scope thấp hơn có thể Override các thuộc tính được phép

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R032-AC001",
      "given": "the applicable business context, actor, and input for Nguyên tắc: - Scope thấp hơn có thể Override các thuộc tính được phép",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "an override is accepted only for a policy marked override-eligible, with an explicit reason and the required approval; otherwise the inherited or system policy remains effective",
      "verifies": [
        "BRD-WS-14-R032-O001"
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
        "BRD-WS-14-R032-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R032-O001",
      "obligation_text": "Nguyên tắc: - Scope thấp hơn có thể Override các thuộc tính được phép"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Scope thấp hơn có thể Override các thuộc tính được phép.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-14-002"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-032",
    "previous_temporary_key": "TMP-BRD-WS-14-032",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Configuration Override",
    "source_context_sha256": "c4aa6cef84f314f32a6461f1d31eb59ce9d7fdd0be06efe0a27a4af0f2517f58",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "c4a9b55681ed6480a6394301f236db348e1e1109d9c462ccdb489c8530f05d2a",
    "source_lines": "L124-L128",
    "source_section": "4. Configuration Override"
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
  "stable_id": "BRD-WS-14-R032",
  "title": "Nguyên tắc: - Scope thấp hơn có thể Override các thuộc tính được phép",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R033 — Nguyên tắc: - Các thuộc tính không được Override sẽ kế thừa

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R033-AC001",
      "given": "the applicable business context, actor, and input for Nguyên tắc: - Các thuộc tính không được Override sẽ kế thừa",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-14-R033-O001"
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
        "BRD-WS-14-R033-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R033-O001",
      "obligation_text": "Nguyên tắc: - Các thuộc tính không được Override sẽ kế thừa"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Các thuộc tính không được Override sẽ kế thừa.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-14-002"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-033",
    "previous_temporary_key": "TMP-BRD-WS-14-033",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Configuration Override",
    "source_context_sha256": "c4aa6cef84f314f32a6461f1d31eb59ce9d7fdd0be06efe0a27a4af0f2517f58",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "c4a9b55681ed6480a6394301f236db348e1e1109d9c462ccdb489c8530f05d2a",
    "source_lines": "L124-L128",
    "source_section": "4. Configuration Override"
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
  "stable_id": "BRD-WS-14-R033",
  "title": "Nguyên tắc: - Các thuộc tính không được Override sẽ kế thừa",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R034 — Nguyên tắc: - Effective Configuration luôn được tính tại Runtime

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R034-AC001",
      "given": "the applicable business context, actor, and input for Nguyên tắc: - Effective Configuration luôn được tính tại Runtime",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R034-O001"
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
        "BRD-WS-14-R034-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R034-O001",
      "obligation_text": "Nguyên tắc: - Effective Configuration luôn được tính tại Runtime"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Effective Configuration luôn được tính tại Runtime.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-14-002"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-034",
    "previous_temporary_key": "TMP-BRD-WS-14-034",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Configuration Override",
    "source_context_sha256": "c4aa6cef84f314f32a6461f1d31eb59ce9d7fdd0be06efe0a27a4af0f2517f58",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "c4a9b55681ed6480a6394301f236db348e1e1109d9c462ccdb489c8530f05d2a",
    "source_lines": "L124-L128",
    "source_section": "4. Configuration Override"
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
  "stable_id": "BRD-WS-14-R034",
  "title": "Nguyên tắc: - Effective Configuration luôn được tính tại Runtime",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R035 — Nguyên tắc: - Scope thấp hơn có độ ưu tiên cao hơn

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R035-AC001",
      "given": "the applicable business context, actor, and input for Nguyên tắc: - Scope thấp hơn có độ ưu tiên cao hơn",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R035-O001"
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
        "BRD-WS-14-R035-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R035-O001",
      "obligation_text": "Nguyên tắc: - Scope thấp hơn có độ ưu tiên cao hơn"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Scope thấp hơn có độ ưu tiên cao hơn.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-14-027"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-035",
    "previous_temporary_key": "TMP-BRD-WS-14-035",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Configuration Override",
    "source_context_sha256": "c4aa6cef84f314f32a6461f1d31eb59ce9d7fdd0be06efe0a27a4af0f2517f58",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "f5aadcd1995482c32c6b52890cd579f14ba9808275b101019420e61725c06b8e",
    "source_lines": "L738-L743",
    "source_section": "27. Configuration Layering"
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
  "stable_id": "BRD-WS-14-R035",
  "title": "Nguyên tắc: - Scope thấp hơn có độ ưu tiên cao hơn",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R036 — Nguyên tắc: - Chỉ các thuộc tính được phép mới được Override

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R036-AC001",
      "given": "the applicable business context, actor, and input for Nguyên tắc: - Chỉ các thuộc tính được phép mới được Override",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "an override is accepted only for a policy marked override-eligible, with an explicit reason and the required approval; otherwise the inherited or system policy remains effective",
      "verifies": [
        "BRD-WS-14-R036-O001"
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
        "BRD-WS-14-R036-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R036-O001",
      "obligation_text": "Nguyên tắc: - Chỉ các thuộc tính được phép mới được Override"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Chỉ các thuộc tính được phép mới được Override.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-14-027"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-036",
    "previous_temporary_key": "TMP-BRD-WS-14-036",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Configuration Override",
    "source_context_sha256": "c4aa6cef84f314f32a6461f1d31eb59ce9d7fdd0be06efe0a27a4af0f2517f58",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "f5aadcd1995482c32c6b52890cd579f14ba9808275b101019420e61725c06b8e",
    "source_lines": "L738-L743",
    "source_section": "27. Configuration Layering"
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
  "stable_id": "BRD-WS-14-R036",
  "title": "Nguyên tắc: - Chỉ các thuộc tính được phép mới được Override",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R037 — Nguyên tắc: - Các thuộc tính khác kế thừa từ Scope phía trên

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R037-AC001",
      "given": "the applicable business context, actor, and input for Nguyên tắc: - Các thuộc tính khác kế thừa từ Scope phía trên",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-14-R037-O001"
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
        "BRD-WS-14-R037-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R037-O001",
      "obligation_text": "Nguyên tắc: - Các thuộc tính khác kế thừa từ Scope phía trên"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Các thuộc tính khác kế thừa từ Scope phía trên.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-14-027"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-037",
    "previous_temporary_key": "TMP-BRD-WS-14-037",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Configuration Override",
    "source_context_sha256": "c4aa6cef84f314f32a6461f1d31eb59ce9d7fdd0be06efe0a27a4af0f2517f58",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "f5aadcd1995482c32c6b52890cd579f14ba9808275b101019420e61725c06b8e",
    "source_lines": "L738-L743",
    "source_section": "27. Configuration Layering"
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
  "stable_id": "BRD-WS-14-R037",
  "title": "Nguyên tắc: - Các thuộc tính khác kế thừa từ Scope phía trên",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R038 — Nguyên tắc: - Effective Configuration luôn được tính tại Runtime

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-14-R038-AC001",
      "given": "the applicable business context, actor, and input for Nguyên tắc: - Effective Configuration luôn được tính tại Runtime",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-14-R038-O001"
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
        "BRD-WS-14-R038-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R038-O001",
      "obligation_text": "Nguyên tắc: - Effective Configuration luôn được tính tại Runtime"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Effective Configuration luôn được tính tại Runtime.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-14-027"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-038",
    "previous_temporary_key": "TMP-BRD-WS-14-038",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Configuration Override",
    "source_context_sha256": "c4aa6cef84f314f32a6461f1d31eb59ce9d7fdd0be06efe0a27a4af0f2517f58",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "f5aadcd1995482c32c6b52890cd579f14ba9808275b101019420e61725c06b8e",
    "source_lines": "L738-L743",
    "source_section": "27. Configuration Layering"
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
  "stable_id": "BRD-WS-14-R038",
  "title": "Nguyên tắc: - Effective Configuration luôn được tính tại Runtime",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-14-001 — Configuration over Customization là nguyên tắc cốt lõi của Platform

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-14-001-AC001",
      "given": "the applicable business context, actor, and input for Configuration over Customization là nguyên tắc cốt lõi của Platform",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "EP-14-001-O001"
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
        "EP-14-001-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-001-O001",
      "obligation_text": "Configuration over Customization là nguyên tắc cốt lõi của Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration over Customization là nguyên tắc cốt lõi của Platform.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-14-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-14-001",
    "source_context_sha256": "71264bbe17a4472d1f8941315c0920743edffe083fc86a9d9e3670528188a0b2",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "bf53662059e42ec625ec0c55e07a23e755c9fdba453572be1ecf9d472358556f",
    "source_lines": "L1192-L1195",
    "source_section": "32. Enterprise Design Principles > EP-14-001"
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
  "stable_id": "EP-14-001",
  "title": "Configuration over Customization là nguyên tắc cốt lõi của Platform",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-14-002 — Toàn bộ Business Domain ưu tiên Configuration trước khi Hard-code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-14-002-AC001",
      "given": "the applicable business context, actor, and input for Toàn bộ Business Domain ưu tiên Configuration trước khi Hard-code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "EP-14-002-O001"
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
        "EP-14-002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-002-O001",
      "obligation_text": "Toàn bộ Business Domain ưu tiên Configuration trước khi Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ Business Domain ưu tiên Configuration trước khi Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-14-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-14-002",
    "source_context_sha256": "532b4f3a2ad46ca69571a2d4c324e7b9bde29b0ecda0742ab7069223f7a16f04",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "1b3a70ccf95d9fe4319615a1a8be7f2e4c29ce82fa320c61effab8af7cf7f020",
    "source_lines": "L1198-L1201",
    "source_section": "32. Enterprise Design Principles > EP-14-002"
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
  "stable_id": "EP-14-002",
  "title": "Toàn bộ Business Domain ưu tiên Configuration trước khi Hard-code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-14-003 — Reference Data là nguồn dữ liệu chuẩn của toàn Platform

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-14-003-AC001",
      "given": "the applicable business context, actor, and input for Reference Data là nguồn dữ liệu chuẩn của toàn Platform",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-14-003-O001"
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
        "EP-14-003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-003-O001",
      "obligation_text": "Reference Data là nguồn dữ liệu chuẩn của toàn Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference Data là nguồn dữ liệu chuẩn của toàn Platform.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-14-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-14-003",
    "source_context_sha256": "950d6651c412cd8ad9bf97619c4dbfc9a22ce3dbd8978f9975328a66a4d43df7",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "f16ecbb41a33b722f96e9cbbb4c73b433e31fdee28ccb6e1c3a47f053f608a1a",
    "source_lines": "L1204-L1207",
    "source_section": "32. Enterprise Design Principles > EP-14-003"
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
  "stable_id": "EP-14-003",
  "title": "Reference Data là nguồn dữ liệu chuẩn của toàn Platform",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-14-004 — Business Rule được cấu hình, không Hard-code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-14-004-AC001",
      "given": "the applicable business context, actor, and input for Business Rule được cấu hình, không Hard-code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "EP-14-004-O001"
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
        "EP-14-004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-004-O001",
      "obligation_text": "Business Rule được cấu hình, không Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule được cấu hình, không Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-14-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-14-004",
    "source_context_sha256": "f9a975b112927556f7c8b1cb6522d90bf82e631f1b3c04ee19a50f14fc2003e2",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
    "source_lines": "L1210-L1213",
    "source_section": "32. Enterprise Design Principles > EP-14-004"
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
  "stable_id": "EP-14-004",
  "title": "Business Rule được cấu hình, không Hard-code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-14-005 — Metadata điều khiển Dynamic Form, Dynamic API, Validation và Reporting

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-14-005-AC001",
      "given": "a contract interaction at the integration boundary defined by Metadata điều khiển Dynamic Form, Dynamic API, Validation và Reporting",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-14-005-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-14-005-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Metadata điều khiển Dynamic Form, Dynamic API, Validation và Reporting",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "EP-14-005-O001"
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
        "EP-14-005-AC001",
        "EP-14-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-005-O001",
      "obligation_text": "Metadata điều khiển Dynamic Form, Dynamic API, Validation và Reporting"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Metadata điều khiển Dynamic Form, Dynamic API, Validation và Reporting.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-14-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-14-005",
    "source_context_sha256": "f70c83817bae8fa69660d949f043206a4cfb01ab46107ffcd7e1e3755f19e0d7",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "238f7ccd8e114f0f1763ed73b97b0a2a2b8dcee5b502b275e535e2181200ba3a",
    "source_lines": "L1216-L1219",
    "source_section": "32. Enterprise Design Principles > EP-14-005"
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
  "stable_id": "EP-14-005",
  "title": "Metadata điều khiển Dynamic Form, Dynamic API, Validation và Reporting",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-14-006 — Configuration luôn có: - Version - Approval - Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-14-006-AC001",
      "given": "an operational task within the scope of Configuration luôn có: - Version - Approval - Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-14-006-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-14-006-AC002",
      "given": "an operational task within the scope of Configuration luôn có: - Version - Approval - Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-14-006-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-14-006-AC003",
      "given": "an operational task within the scope of Configuration luôn có: - Version - Approval - Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-14-006-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EP-14-006-AC004",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Configuration luôn có: - Version - Approval - Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EP-14-006-O001",
        "EP-14-006-O002",
        "EP-14-006-O003"
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
        "EP-14-006-AC001",
        "EP-14-006-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-006-O001",
      "obligation_text": "Configuration luôn có: Version."
    },
    {
      "acceptance_criterion_references": [
        "EP-14-006-AC002",
        "EP-14-006-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-006-O002",
      "obligation_text": "Configuration luôn có: Approval."
    },
    {
      "acceptance_criterion_references": [
        "EP-14-006-AC003",
        "EP-14-006-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-006-O003",
      "obligation_text": "Configuration luôn có: Audit."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-14-006 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-14-006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-14-006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-14-006 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-14-006-AC001",
        "EP-14-006-AC002",
        "EP-14-006-AC003"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-14-006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration luôn có: - Version - Approval - Audit",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-14-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-14-006",
    "source_context_sha256": "fbbd21343b6884ab343a196da2102c3f46fc5e38501d4695518ca0b9ae017335",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "fa17edf2ed0b2f88f9d99cbc2a41d16b517de1e65d865da63a4b6935c987d12b",
    "source_lines": "L1222-L1229",
    "source_section": "32. Enterprise Design Principles > EP-14-006"
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
  "stable_id": "EP-14-006",
  "title": "Configuration luôn có: - Version - Approval - Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-14-007 — Configuration hỗ trợ Runtime Reload

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-14-007-AC001",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ Runtime Reload",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "EP-14-007-O001"
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
        "EP-14-007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-007-O001",
      "obligation_text": "Configuration hỗ trợ Runtime Reload"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration hỗ trợ Runtime Reload.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-14-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Runtime Reload",
    "source_context_sha256": "0a583e1a14b32ca7c248623089f83877941ca3111239950796bab794f3655578",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "f7ab0500deac182f6a78ae71e864bf00890cb1adb1673548087ce5408bf06483",
    "source_lines": "L1232-L1235",
    "source_section": "32. Enterprise Design Principles > EP-14-007"
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
  "stable_id": "EP-14-007",
  "title": "Configuration hỗ trợ Runtime Reload",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-14-008 — Configuration hỗ trợ Layering và Effective Configuration

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-14-008-AC001",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ Layering và Effective Configuration",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "EP-14-008-O001"
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
        "EP-14-008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-008-O001",
      "obligation_text": "Configuration hỗ trợ Layering và Effective Configuration"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration hỗ trợ Layering và Effective Configuration.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-14-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-14-008",
    "source_context_sha256": "75f9d38a26429981d02eb41a3772dbd7662cf0b101989e7742285d6b5cc42c09",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "dafde97a0177f3560f226f404810e07d47ceb680a1e502a2b5340231836cc161",
    "source_lines": "L1238-L1241",
    "source_section": "32. Enterprise Design Principles > EP-14-008"
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
  "stable_id": "EP-14-008",
  "title": "Configuration hỗ trợ Layering và Effective Configuration",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-14-009 — Configuration hỗ trợ Package để triển khai và nâng cấp Platform

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-14-009-AC001",
      "given": "the applicable business context, actor, and input for Configuration hỗ trợ Package để triển khai và nâng cấp Platform",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "EP-14-009-O001"
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
        "EP-14-009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-009-O001",
      "obligation_text": "Configuration hỗ trợ Package để triển khai và nâng cấp Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Configuration hỗ trợ Package để triển khai và nâng cấp Platform.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-14-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-14-009",
    "source_context_sha256": "1c1d8041dc00f22a8cdc8fa1629c24cf0e297c7ff88925e4ef91da16d149ca7b",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "c10fae674900ee3bb32b58276873419d420a0a8489ffe6c2dc9985dfd7d55206",
    "source_lines": "L1244-L1247",
    "source_section": "32. Enterprise Design Principles > EP-14-009"
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
  "stable_id": "EP-14-009",
  "title": "Configuration hỗ trợ Package để triển khai và nâng cấp Platform",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-14-010 — Organization được khởi tạo bằng Template nhằm giảm thời gian Onboarding

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-14-010-AC001",
      "given": "the applicable business context, actor, and input for Organization được khởi tạo bằng Template nhằm giảm thời gian Onboarding",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-14-010-O001"
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
        "EP-14-010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-010-O001",
      "obligation_text": "Organization được khởi tạo bằng Template nhằm giảm thời gian Onboarding"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization được khởi tạo bằng Template nhằm giảm thời gian Onboarding.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-14-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-14-010",
    "source_context_sha256": "607589477828a948f15017dd4efe83a9594e10758d0d31946aa64727eda14cb8",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "d817ef271baf12ebd3afbe4df10a619cf8294dee8aed45fcc78231fa26af4ef7",
    "source_lines": "L1250-L1253",
    "source_section": "32. Enterprise Design Principles > EP-14-010"
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
  "stable_id": "EP-14-010",
  "title": "Organization được khởi tạo bằng Template nhằm giảm thời gian Onboarding",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
