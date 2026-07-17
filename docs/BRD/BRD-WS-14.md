---
document_code: "BRD-WS-14"
document_id: "BRD-WS-14"
title: "Platform Configuration, Reference Data & Business Rules"
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

Lịch sử Configuration Version phải append-only; version bị supersede vẫn phải truy cập được và không được ghi đè. Không suy diễn thời hạn lưu trữ hữu hạn; mọi quy tắc archive hoặc xóa trong tương lai phải được quản trị riêng.

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

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-001 — Configuration hỗ trợ đầy đủ các Scope: - Global - Parent Organization - Organization - Departmen…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-001",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "388614f027b707ad8159f911b59d72089d466605f1f5575c6622b48a948c95de"
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
        "BD-14-001-AC001",
        "BD-14-001-AC007",
        "BD-14-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O001",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: Global"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-001-AC002",
        "BD-14-001-AC007",
        "BD-14-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O002",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: Parent Organization"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-001-AC003",
        "BD-14-001-AC007",
        "BD-14-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O003",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: Organization"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-001-AC004",
        "BD-14-001-AC007",
        "BD-14-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O004",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: Department"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-001-AC005",
        "BD-14-001-AC007",
        "BD-14-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O005",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: Storefront"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-001-AC006",
        "BD-14-001-AC007",
        "BD-14-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-001-O006",
      "obligation_text": "Configuration hỗ trợ đầy đủ các Scope: User"
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
    "source_fingerprint": "388614f027b707ad8159f911b59d72089d466605f1f5575c6622b48a948c95de",
    "source_lines": "L1372-L1501",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-002",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "73aef207980a939ae35ae95bd63021fe0f19cf0d1e5f238b9617bfdb01fd26fb"
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
        "BD-14-002-AC001",
        "BD-14-002-AC003",
        "BD-14-002-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-002-O001",
      "obligation_text": "Configuration hỗ trợ Override theo mô hình Layer"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-002-AC002",
        "BD-14-002-AC003",
        "BD-14-002-AC004"
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
    "source_fingerprint": "73aef207980a939ae35ae95bd63021fe0f19cf0d1e5f238b9617bfdb01fd26fb",
    "source_lines": "L1503-L1588",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-002"
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
  "normative_statement": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform. Reference Data hỗ trợ: - Multi-language - Parent / Child - Alias - Effective Date",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-003",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Data",
    "source_context_sha256": "8159a2e679167d6d72d40b009066fd1f2181eed5a5122ec29675371dcf1ef8de",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "b6f3bc3e667620cf59532d90d586f72f7bcafa79e9dc8af0349b9470de907bc6",
    "source_fingerprint_before_c3": "f8ffedfcc14d6f86a45d6e94ad06106862bb94329e2f1b2610f39629b776884a",
    "source_lines": "L1590-L1651",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-003"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-14-R039",
      "BRD-WS-14-R040",
      "BRD-WS-14-R041",
      "BRD-WS-14-R042"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-14-003",
  "title": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-004 — Dictionary là Business Object độc lập. Dictionary không thay thế Reference Data. Dictionary quản…

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
  "normative_statement": "Dictionary là Business Object độc lập. Dictionary không thay thế Reference Data. Dictionary quản lý Label, Enum, Caption và Translation.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-004",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-004",
    "source_context_sha256": "6acc8c8e8f8c79c34e8e3d5a62ad5e90891a24c77aa4a41c451f45395691f8c5",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "27a2e07b1e7e4a09e0672ecb8a66c0546a101eb53734215b213d8cdb18436f3a",
    "source_fingerprint_before_c3": "e7ac4df687cd599afce951a9c4ae9abf8959a71d66fa2a9ef0c911658dff822a",
    "source_lines": "L1653-L1714",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-004"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-14-R043",
      "BRD-WS-14-R044",
      "BRD-WS-14-R045"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-14-004",
  "title": "Dictionary là Business Object độc lập. Dictionary không thay thế Reference Data. Dictionary quản…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-005 — Lookup là Business Object. Lookup hỗ trợ Dynamic Form, Search và API

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
      "requirement_id": "BD-14-005",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "0da08b5d97e5ece4f68138c9bb151379218d87ebfe0895afc643c9111dbeac98"
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
        "BD-14-005-AC001",
        "BD-14-005-AC003",
        "BD-14-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-005-O001",
      "obligation_text": "Lookup là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-005-AC002",
        "BD-14-005-AC003",
        "BD-14-005-AC004"
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
    "source_fingerprint": "0da08b5d97e5ece4f68138c9bb151379218d87ebfe0895afc643c9111dbeac98",
    "source_lines": "L1716-L1801",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-005"
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
  "normative_statement": "Business Rule là Business Object. Business Rule được cấu hình. Không Hard-code.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-006",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Business Rule Engine",
    "source_context_sha256": "86d3ad94506a400c239a818b3540c68c8fa7011a8692d42b51ff06ebc3155e51",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "ee4b1bac38f19cbbbe8ddcde6800c6b10127f2249c1fee1892677b4abe7ce3e9",
    "source_fingerprint_before_c3": "229a3404ed449712b41ef2f142542eb356567db3a11a775a488094cfa5dd0c18",
    "source_lines": "L1803-L1863",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-006"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-14-R046",
      "BRD-WS-14-R047",
      "BRD-WS-14-R048"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-14-006",
  "title": "Business Rule là Business Object. Business Rule được cấu hình. Không Hard-code",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-007 — Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Departme…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-007",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "f78db455c6f301f749b714cb88b47b2abc7c5de9316c8fcecaa31e592c78dff4"
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
        "BD-14-007-AC001",
        "BD-14-007-AC009",
        "BD-14-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O001",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Platform"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC002",
        "BD-14-007-AC009",
        "BD-14-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O002",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Organization"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC003",
        "BD-14-007-AC009",
        "BD-14-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O003",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Department"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC004",
        "BD-14-007-AC009",
        "BD-14-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O004",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Storefront"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC005",
        "BD-14-007-AC009",
        "BD-14-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O005",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Product"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC006",
        "BD-14-007-AC009",
        "BD-14-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O006",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Campaign"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC007",
        "BD-14-007-AC009",
        "BD-14-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O007",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Category"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-007-AC008",
        "BD-14-007-AC009",
        "BD-14-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-007-O008",
      "obligation_text": "Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: Customer Group"
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
    "source_fingerprint": "f78db455c6f301f749b714cb88b47b2abc7c5de9316c8fcecaa31e592c78dff4",
    "source_lines": "L1865-L2014",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-008",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "688b3601bd80920e6f4d17724ca491f12594b2c2535743a39f123276b8fb1b9c"
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
        "BD-14-008-AC001",
        "BD-14-008-AC004",
        "BD-14-008-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-008-O001",
      "obligation_text": "Business Rule hỗ trợ: Priority"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-008-AC002",
        "BD-14-008-AC004",
        "BD-14-008-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-008-O002",
      "obligation_text": "Business Rule hỗ trợ: Sequence"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-008-AC003",
        "BD-14-008-AC004",
        "BD-14-008-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-008-O003",
      "obligation_text": "Business Rule hỗ trợ: Stop Policy Stop Policy được cấu hình"
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
    "source_fingerprint": "688b3601bd80920e6f4d17724ca491f12594b2c2535743a39f123276b8fb1b9c",
    "source_lines": "L2016-L2111",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-009",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "8ccf1f0b506032d8f2c677a4547d8b78a6ee2b77481634963d41e5ed39e32069"
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
        "BD-14-009-AC001",
        "BD-14-009-AC003",
        "BD-14-009-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-009-O001",
      "obligation_text": "Business Rule chỉnh sửa trực tiếp"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-009-AC002",
        "BD-14-009-AC003",
        "BD-14-009-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-009-O002",
      "obligation_text": "Lịch sử thay đổi được lưu thông qua Configuration Version và Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-009 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-009 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-009 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-14-009-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-14-009-AC001",
        "BD-14-009-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-009 does not define a recovery obligation."
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
    "source_fingerprint": "8ccf1f0b506032d8f2c677a4547d8b78a6ee2b77481634963d41e5ed39e32069",
    "source_lines": "L2113-L2232",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-009"
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
  "normative_statement": "Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organization - Storefront - User",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-14-010",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-010",
    "source_context_sha256": "36a85a92279eb52803fdc59156a6e359a91c89f4dce29f08327f34b94c7d92ef",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "1df0db0074bab2773fac20d6be477c4fa9d9bf8d0e822a2069c2012625aa8f88",
    "source_fingerprint_before_c3": "0523a5bee5c4241730ee1947df4ef2cf9eb75b2b328edd8366e62629616c27a5",
    "source_lines": "L2234-L2297",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-010"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-14-R049",
      "BRD-WS-14-R050",
      "BRD-WS-14-R051",
      "BRD-WS-14-R052",
      "BRD-WS-14-R053"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-14-010",
  "title": "Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organizat…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-14-011 — Toàn bộ tham số hệ thống được quản lý bằng Parameter. Parameter hỗ trợ Override theo Scope

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
      "requirement_id": "BD-14-011",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "f1c4eb9e639ce7cf88ace701938675ce86b9cd93526d3b7d81bef472d3c8bb9b"
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
        "BD-14-011-AC001",
        "BD-14-011-AC003",
        "BD-14-011-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-011-O001",
      "obligation_text": "Toàn bộ tham số hệ thống được quản lý bằng Parameter"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-011-AC002",
        "BD-14-011-AC003",
        "BD-14-011-AC004"
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
    "source_fingerprint": "f1c4eb9e639ce7cf88ace701938675ce86b9cd93526d3b7d81bef472d3c8bb9b",
    "source_lines": "L2299-L2384",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-011"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-012",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "d16f6c98d175f1b5c3c0fe1347ef821662a1ce86646a8baba7086bb1549ede60"
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
        "BD-14-012-AC001",
        "BD-14-012-AC008",
        "BD-14-012-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O001",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Dynamic Form"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC002",
        "BD-14-012-AC008",
        "BD-14-012-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O002",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Dynamic API"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC003",
        "BD-14-012-AC008",
        "BD-14-012-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O003",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Validation"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC004",
        "BD-14-012-AC008",
        "BD-14-012-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O004",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Import"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC005",
        "BD-14-012-AC008",
        "BD-14-012-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O005",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Export"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC006",
        "BD-14-012-AC008",
        "BD-14-012-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O006",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Report Builder"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-012-AC007",
        "BD-14-012-AC008",
        "BD-14-012-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-012-O007",
      "obligation_text": "Metadata là Business Object. Metadata phục vụ: Dashboard"
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
    "source_fingerprint": "d16f6c98d175f1b5c3c0fe1347ef821662a1ce86646a8baba7086bb1549ede60",
    "source_lines": "L2386-L2521",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-012"
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
      "requirement_id": "BD-14-013",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "17b40064ee25397f30c87a33eae94de31ad823ead9b4061976ed582d9429d7e5"
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
        "BD-14-013-AC001",
        "BD-14-013-AC003",
        "BD-14-013-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-013-O001",
      "obligation_text": "Configuration hỗ trợ Version"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-013-AC002",
        "BD-14-013-AC003",
        "BD-14-013-AC004"
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
    "source_fingerprint": "17b40064ee25397f30c87a33eae94de31ad823ead9b4061976ed582d9429d7e5",
    "source_lines": "L2523-L2614",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-013"
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
      "requirement_id": "BD-14-014",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "5de217d3b465526bb1da6df0ab14f39178ef587e301e00ea8865ccc57c558039"
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
        "BD-14-014-AC001",
        "BD-14-014-AC003",
        "BD-14-014-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-014-O001",
      "obligation_text": "Configuration bắt buộc Approval trước Publish"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-014-AC002",
        "BD-14-014-AC003",
        "BD-14-014-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-014-O002",
      "obligation_text": "Approval theo Role và Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-14-014-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-14-014-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-14-014-AC001",
        "BD-14-014-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-014 does not define a recovery obligation."
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
    "source_fingerprint": "5de217d3b465526bb1da6df0ab14f39178ef587e301e00ea8865ccc57c558039",
    "source_lines": "L2616-L2743",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-014"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-015",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "68d8f76f763e9788d3c4983943a4963aa2f355095d6c47a7e72713fda19ab47d"
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
        "BD-14-015-AC001",
        "BD-14-015-AC003",
        "BD-14-015-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-015-O001",
      "obligation_text": "Configuration hỗ trợ: Effective From"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-015-AC002",
        "BD-14-015-AC003",
        "BD-14-015-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-015-O002",
      "obligation_text": "Configuration hỗ trợ: Effective To"
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
    "source_fingerprint": "68d8f76f763e9788d3c4983943a4963aa2f355095d6c47a7e72713fda19ab47d",
    "source_lines": "L2745-L2830",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-015"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-016",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "e1bdc55c4764814ed4b5c47c9c0d79cdd69d76e542c7cbbce452ec5630031a99"
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
        "BD-14-016-AC001",
        "BD-14-016-AC007",
        "BD-14-016-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O001",
      "obligation_text": "Configuration Audit lưu đầy đủ: Who"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-016-AC002",
        "BD-14-016-AC007",
        "BD-14-016-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O002",
      "obligation_text": "Configuration Audit lưu đầy đủ: When"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-016-AC003",
        "BD-14-016-AC007",
        "BD-14-016-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O003",
      "obligation_text": "Configuration Audit lưu đầy đủ: Before"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-016-AC004",
        "BD-14-016-AC007",
        "BD-14-016-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O004",
      "obligation_text": "Configuration Audit lưu đầy đủ: After"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-016-AC005",
        "BD-14-016-AC007",
        "BD-14-016-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O005",
      "obligation_text": "Configuration Audit lưu đầy đủ: Reason"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-016-AC006",
        "BD-14-016-AC007",
        "BD-14-016-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-016-O006",
      "obligation_text": "Configuration Audit lưu đầy đủ: Version"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-016 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-016 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-016 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-14-016-AC007"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-14-016-AC001",
        "BD-14-016-AC002",
        "BD-14-016-AC003",
        "BD-14-016-AC004",
        "BD-14-016-AC005",
        "BD-14-016-AC006"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-016 does not define a recovery obligation."
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
    "source_fingerprint": "e1bdc55c4764814ed4b5c47c9c0d79cdd69d76e542c7cbbce452ec5630031a99",
    "source_lines": "L2832-L2995",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-016"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-017",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "ba8a33dd9f4594f7af3b9b4dbac8a5ced84a8f8a24fe7f92d911a8691cb5f746"
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
        "BD-14-017-AC001",
        "BD-14-017-AC005",
        "BD-14-017-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-017-O001",
      "obligation_text": "Configuration hỗ trợ: JSON"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-017-AC002",
        "BD-14-017-AC005",
        "BD-14-017-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-017-O002",
      "obligation_text": "Configuration hỗ trợ: YAML"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-017-AC003",
        "BD-14-017-AC005",
        "BD-14-017-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-017-O003",
      "obligation_text": "Configuration hỗ trợ: Excel"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-017-AC004",
        "BD-14-017-AC005",
        "BD-14-017-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-017-O004",
      "obligation_text": "Configuration hỗ trợ: CSV Import luôn Validate trước Apply"
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
    "source_fingerprint": "ba8a33dd9f4594f7af3b9b4dbac8a5ced84a8f8a24fe7f92d911a8691cb5f746",
    "source_lines": "L2997-L3102",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-017"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-018",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "0e678534006f9b100c0ac8e91acbce21dc6f6addd1c46f15d2e584e84bd65327"
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
        "BD-14-018-AC001",
        "BD-14-018-AC008",
        "BD-14-018-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O001",
      "obligation_text": "Configuration Package hỗ trợ: Export"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC002",
        "BD-14-018-AC008",
        "BD-14-018-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O002",
      "obligation_text": "Configuration Package hỗ trợ: Import"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC003",
        "BD-14-018-AC008",
        "BD-14-018-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O003",
      "obligation_text": "Configuration Package hỗ trợ: Install"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC004",
        "BD-14-018-AC008",
        "BD-14-018-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O004",
      "obligation_text": "Configuration Package hỗ trợ: Upgrade"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC005",
        "BD-14-018-AC008",
        "BD-14-018-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O005",
      "obligation_text": "Configuration Package hỗ trợ: Compare"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC006",
        "BD-14-018-AC008",
        "BD-14-018-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O006",
      "obligation_text": "Configuration Package hỗ trợ: Merge"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-018-AC007",
        "BD-14-018-AC008",
        "BD-14-018-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-018-O007",
      "obligation_text": "Configuration Package hỗ trợ: Rollback"
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
    "source_fingerprint": "0e678534006f9b100c0ac8e91acbce21dc6f6addd1c46f15d2e584e84bd65327",
    "source_lines": "L3104-L3239",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-018"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-019",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "9ee58c66d5a5285ff74fb57bcb152671f87959b898b1b2c5259411aac0f6b95d"
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
        "BD-14-019-AC001",
        "BD-14-019-AC004",
        "BD-14-019-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-019-O001",
      "obligation_text": "Configuration hỗ trợ: Validation"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-019-AC002",
        "BD-14-019-AC004",
        "BD-14-019-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-019-O002",
      "obligation_text": "Configuration hỗ trợ: Dependency"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-019-AC003",
        "BD-14-019-AC004",
        "BD-14-019-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-019-O003",
      "obligation_text": "Configuration hỗ trợ: Rollback"
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
    "source_fingerprint": "9ee58c66d5a5285ff74fb57bcb152671f87959b898b1b2c5259411aac0f6b95d",
    "source_lines": "L3241-L3336",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-019"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-020",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "634e88ef291a8b229013f53e81b7a4b3a1e56691dabeee7777905f8d53b3ac19"
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
        "BD-14-020-AC001",
        "BD-14-020-AC002",
        "BD-14-020-AC003"
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
    "source_fingerprint": "634e88ef291a8b229013f53e81b7a4b3a1e56691dabeee7777905f8d53b3ac19",
    "source_lines": "L3338-L3413",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-020"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-021",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "9b4c2a3c22e3925b78a8471711b089d187e36e760ee9e19803fd4404bb3b0091"
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
        "BD-14-021-AC001",
        "BD-14-021-AC003",
        "BD-14-021-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-021-O001",
      "obligation_text": "Configuration hỗ trợ Runtime Reload"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-021-AC002",
        "BD-14-021-AC003",
        "BD-14-021-AC004"
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
    "source_fingerprint": "9b4c2a3c22e3925b78a8471711b089d187e36e760ee9e19803fd4404bb3b0091",
    "source_lines": "L3415-L3500",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-021"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-022",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "e150e5d2910f370b8a99d220c3ed644846eded3f930e3bbd6db9d3bf23ad749e"
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
        "BD-14-022-AC001",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O001",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Role"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC002",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O002",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Dashboard"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC003",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O003",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Storefront"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC004",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O004",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Theme"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC005",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O005",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Report"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC006",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O006",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Notification"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC007",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O007",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: KB"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC008",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O008",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: FAQ"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC009",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O009",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Survey"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC010",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O010",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Support Policy"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-022-AC011",
        "BD-14-022-AC012",
        "BD-14-022-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-022-O011",
      "obligation_text": "Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: Configuration"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-022 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-022 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-022 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-14-022-AC012"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
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
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-022 does not define a recovery obligation."
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
    "source_fingerprint": "e150e5d2910f370b8a99d220c3ed644846eded3f930e3bbd6db9d3bf23ad749e",
    "source_lines": "L3502-L3729",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-022"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-023",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "94bb50c14f2829e6b959eebda21f4270b1001282aa663a98a529d455e32318c5"
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
        "BD-14-023-AC001",
        "BD-14-023-AC003",
        "BD-14-023-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-023-O001",
      "obligation_text": "Configuration áp dụng theo mô hình Layering"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-023-AC002",
        "BD-14-023-AC003",
        "BD-14-023-AC004"
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
    "source_fingerprint": "94bb50c14f2829e6b959eebda21f4270b1001282aa663a98a529d455e32318c5",
    "source_lines": "L3731-L3816",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-023"
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
      "requirement_id": "BD-14-024",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "dba9613502ec41a9a184c32d59e5158401c7d9566672b24d89e596f7a08e5fa2"
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
        "BD-14-024-AC001",
        "BD-14-024-AC011",
        "BD-14-024-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O001",
      "obligation_text": "Configuration Capability Matrix xác định: Read"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC002",
        "BD-14-024-AC011",
        "BD-14-024-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O002",
      "obligation_text": "Configuration Capability Matrix xác định: Create"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC003",
        "BD-14-024-AC011",
        "BD-14-024-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O003",
      "obligation_text": "Configuration Capability Matrix xác định: Edit"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC004",
        "BD-14-024-AC011",
        "BD-14-024-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O004",
      "obligation_text": "Configuration Capability Matrix xác định: Delete"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC005",
        "BD-14-024-AC011",
        "BD-14-024-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O005",
      "obligation_text": "Configuration Capability Matrix xác định: Override"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC006",
        "BD-14-024-AC011",
        "BD-14-024-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O006",
      "obligation_text": "Configuration Capability Matrix xác định: Clone"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC007",
        "BD-14-024-AC011",
        "BD-14-024-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O007",
      "obligation_text": "Configuration Capability Matrix xác định: Import"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC008",
        "BD-14-024-AC011",
        "BD-14-024-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O008",
      "obligation_text": "Configuration Capability Matrix xác định: Export"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC009",
        "BD-14-024-AC011",
        "BD-14-024-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O009",
      "obligation_text": "Configuration Capability Matrix xác định: Approval Required"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-024-AC010",
        "BD-14-024-AC011",
        "BD-14-024-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-024-O010",
      "obligation_text": "Configuration Capability Matrix xác định: Runtime Reload"
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
    "source_fingerprint": "dba9613502ec41a9a184c32d59e5158401c7d9566672b24d89e596f7a08e5fa2",
    "source_lines": "L3818-L3991",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-024"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-025",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "155015aba5029a115836941db9e615e3b5d03a7ac0b1235a989d8f9430a971c1"
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
        "BD-14-025-AC001",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O001",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: System"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC002",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O002",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Organization"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC003",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O003",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Storefront"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC004",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O004",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Commercial"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC005",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O005",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Financial"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC006",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O006",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Notification"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC007",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O007",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Customer"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC008",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O008",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Support"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC009",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O009",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Security"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC010",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O010",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Integration"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC011",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O011",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Workflow"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC012",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O012",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Localization"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC013",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O013",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Reporting"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC014",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O014",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Monitoring"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-025-AC015",
        "BD-14-025-AC016",
        "BD-14-025-AC017"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-025-O015",
      "obligation_text": "Configuration được phân nhóm theo Category. Category mặc định: Scheduler"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-14-025-AC017"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-025 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-025 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-14-025-AC016"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
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
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-14-025 does not define a recovery obligation."
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
    "source_fingerprint": "155015aba5029a115836941db9e615e3b5d03a7ac0b1235a989d8f9430a971c1",
    "source_lines": "L3993-L4261",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-025"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-14-026",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "2063acdec5faf281c6f7c3e5b050d3103772008330c8d4644931fbd5a8141c00"
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
        "BD-14-026-AC001",
        "BD-14-026-AC006",
        "BD-14-026-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-026-O001",
      "obligation_text": "Configuration Dependency Graph hỗ trợ: Dependency Analysis"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-026-AC002",
        "BD-14-026-AC006",
        "BD-14-026-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-026-O002",
      "obligation_text": "Configuration Dependency Graph hỗ trợ: Impact Analysis"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-026-AC003",
        "BD-14-026-AC006",
        "BD-14-026-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-026-O003",
      "obligation_text": "Configuration Dependency Graph hỗ trợ: Upgrade Planning"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-026-AC004",
        "BD-14-026-AC006",
        "BD-14-026-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-026-O004",
      "obligation_text": "Configuration Dependency Graph hỗ trợ: Publish Validation"
    },
    {
      "acceptance_criterion_references": [
        "BD-14-026-AC005",
        "BD-14-026-AC006",
        "BD-14-026-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-14-026-O005",
      "obligation_text": "Configuration Dependency Graph hỗ trợ: Rollback"
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
    "source_fingerprint": "2063acdec5faf281c6f7c3e5b050d3103772008330c8d4644931fbd5a8141c00",
    "source_lines": "L4263-L4378",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-14-026"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R001",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "8aa6645dd4d3c742667bceacb98f68b2b7162a446e8a4856f3014f3ddcf4e2b9"
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
        "BRD-WS-14-R001-AC001",
        "BRD-WS-14-R001-AC002",
        "BRD-WS-14-R001-AC003"
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
    "source_lines": "L4380-L4455",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R003",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "49b81ff9c12144b91925f782a4abfb9deb91d18565f755d85e1f8c4ee681b169"
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
        "BRD-WS-14-R003-AC001",
        "BRD-WS-14-R003-AC002",
        "BRD-WS-14-R003-AC003"
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
    "source_lines": "L4457-L4532",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R004",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "90e5cb967f6f2ec9469be9f2a4d8ab1348db614d108d8d4e635ca0e65c3db3ed"
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
        "BRD-WS-14-R004-AC001",
        "BRD-WS-14-R004-AC002",
        "BRD-WS-14-R004-AC003"
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
    "source_lines": "L4534-L4609",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R005",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "80b3165c8920f2cbf590bf42254c396f19cc62fe4d8fa2e1e53dbf57acf52fb7"
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
        "BRD-WS-14-R005-AC001",
        "BRD-WS-14-R005-AC002",
        "BRD-WS-14-R005-AC003"
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
    "source_lines": "L4611-L4686",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R006",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "e832489b49118aa3e879fdaaec5c10f19d37ed032eda8ed36ab79ccffa487bfc"
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
        "BRD-WS-14-R006-AC001",
        "BRD-WS-14-R006-AC002",
        "BRD-WS-14-R006-AC003"
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
    "source_fingerprint": "e832489b49118aa3e879fdaaec5c10f19d37ed032eda8ed36ab79ccffa487bfc",
    "source_lines": "L4688-L4763",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R007",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "daa0faf9352dec8598528915bbd362a56e90c52d31c35a5971fdd9865cbe4966"
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
        "BRD-WS-14-R007-AC001",
        "BRD-WS-14-R007-AC002",
        "BRD-WS-14-R007-AC003"
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
    "source_fingerprint": "daa0faf9352dec8598528915bbd362a56e90c52d31c35a5971fdd9865cbe4966",
    "source_lines": "L4765-L4840",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R008",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "5b4470a765784db56dcc41016c9ec8dfe673e0cc9758cdb5491233d7478a5886"
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
        "BRD-WS-14-R008-AC001",
        "BRD-WS-14-R008-AC002",
        "BRD-WS-14-R008-AC003"
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
    "source_fingerprint": "5b4470a765784db56dcc41016c9ec8dfe673e0cc9758cdb5491233d7478a5886",
    "source_lines": "L4842-L4917",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R009",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "a6209cfee7468cae1bb99a4d2be50e791bb98ccdcad2226c3c90249412ba6295"
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
        "BRD-WS-14-R009-AC001",
        "BRD-WS-14-R009-AC002",
        "BRD-WS-14-R009-AC003"
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
    "source_lines": "L4919-L4994",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R010",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "8fbe32b693b61843cd8e52fe90068741253502d14ec8982b2404373847584bd9"
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
        "BRD-WS-14-R010-AC001",
        "BRD-WS-14-R010-AC002",
        "BRD-WS-14-R010-AC003"
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
    "source_lines": "L4996-L5071",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R011",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "40dc5ad6ace9ca40c52597b260c4470d50f2b796bced0d30e69100104d989996"
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
        "BRD-WS-14-R011-AC001",
        "BRD-WS-14-R011-AC002",
        "BRD-WS-14-R011-AC003"
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
    "source_lines": "L5073-L5148",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R011"
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
### BRD-WS-14-R012 — Metadata phải chứa Field Name, Data Type, Required, Default Value, Validation Rule, Searchable, …

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R012",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "6221394b74678449ae7a3297f6bcadc55ea483a5d8005ebb94ac2b54fa8dbe6d"
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
        "BRD-WS-14-R012-AC001",
        "BRD-WS-14-R012-AC002",
        "BRD-WS-14-R012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R012-O001",
      "obligation_text": "Metadata phải chứa Field Name, Data Type, Required, Default Value, Validation Rule, Searchable, Sortable, Filterable, Exportable, Importable, Permission, Localization, Tooltip và Description"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-14-R012-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-14-R012-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-14-R012-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R012 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Metadata phải chứa Field Name, Data Type, Required, Default Value, Validation Rule, Searchable, Sortable, Filterable, Exportable, Importable, Permission, Localization, Tooltip và Description.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-14.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "14. Metadata"
    },
    "deterministic_transformation": "RESTORE_METADATA_SUBJECT",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-012",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-14-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "1. Workshop Objective",
    "source_context_sha256": "4874f7decb0ca7427cd9840d305561e668d5b5e66020de3c80501b800cb88c47",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "6221394b74678449ae7a3297f6bcadc55ea483a5d8005ebb94ac2b54fa8dbe6d",
    "source_fingerprint_before_c3": "5ab75ac869cbf9e45f90f5dab00610aaa6e07c625f2f72a78159885dca9f486e",
    "source_lines": "L5150-L5281",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-14.md",
      "lines": "L369-L384",
      "section": "14. Metadata"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R012"
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
  "title": "Metadata phải chứa Field Name, Data Type, Required, Default Value, Validation Rule, Searchable, …",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R013 — Lịch sử Configuration Version phải append-only; version bị supersede vẫn phải truy cập được và không được ghi đè. Khô…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2C-SC-C1-DEC-013/OPT-A"
      ],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-013",
        "option_id": "OPT-A"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R013",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "9963553267ed5e63d686ca78b40547f916c328ab22f0d6f3b089886d5c943a65"
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
        "BRD-WS-14-R013-AC001",
        "BRD-WS-14-R013-AC002",
        "BRD-WS-14-R013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R013-O001",
      "obligation_text": "Lịch sử Configuration Version phải append-only; version bị supersede vẫn phải truy cập được và không được ghi đè. Không suy diễn thời hạn lưu trữ hữu hạn; mọi quy tắc archive hoặc xóa trong tương lai phải được quản trị riêng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Lịch sử Configuration Version phải append-only; version bị supersede vẫn phải truy cập được và không được ghi đè. Không suy diễn thời hạn lưu trữ hữu hạn; mọi quy tắc archive hoặc xóa trong tương lai phải được quản trị riêng.",
  "provenance": {
    "approved_decisions": [
      "P2C-SC-C1-DEC-013/OPT-A"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-013",
    "previous_temporary_key": "TMP-BRD-WS-14-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Configuration Version",
    "source_context_sha256": "9208e204d9cb610736822c64809a0e8ced379623045721629805a45957b7c6aa",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "9963553267ed5e63d686ca78b40547f916c328ab22f0d6f3b089886d5c943a65",
    "source_lines": "L5283-L5366",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R013"
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
  "title": "Lịch sử Configuration Version phải append-only; version bị supersede vẫn phải truy cập được và không được ghi đè. Khô…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R014 — Configuration phải được Approval trước khi Publish

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
      "requirement_id": "BRD-WS-14-R014",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "125bf18516e0d78b8ddb3b0e0ffcee0dae95f3872b3ba9a8de4a30e62f90ba43"
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
        "BRD-WS-14-R014-AC001",
        "BRD-WS-14-R014-AC002",
        "BRD-WS-14-R014-AC003"
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
    "source_lines": "L5368-L5449",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R014"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R015",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "0524c178daee01147c8b0e4c6eb12a0a656aef82c0fb2abe7ad931e173909b5b"
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R015 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R015 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R015 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-14-R015-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-14-R015-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R015 does not define a recovery obligation."
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
    "source_lines": "L5451-L5559",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R015"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R016",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "b3ee3224cf7da6525e86cec8bce75ea2f112c752034dc30a4c172bf7b902b02b"
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
        "BRD-WS-14-R016-AC001",
        "BRD-WS-14-R016-AC002",
        "BRD-WS-14-R016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R016-O001",
      "obligation_text": "Audit luôn được lưu vĩnh viễn theo chính sách lưu trữ của Platform"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R016 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R016 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R016 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-14-R016-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-14-R016-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R016 does not define a recovery obligation."
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
    "source_lines": "L5561-L5669",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R016"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R017",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "48a37fce4c451b429099515722cfd5b3a91e809622f3d7d8d586e22a01809603"
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
        "BRD-WS-14-R017-AC001",
        "BRD-WS-14-R017-AC002",
        "BRD-WS-14-R017-AC003"
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
    "source_lines": "L5671-L5746",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R017"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R018",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "ecafee3537bb7e96347ffbe5356ab225e48e4eb9156f0976a53e1806a7dd1c1d"
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
        "BRD-WS-14-R018-AC001",
        "BRD-WS-14-R018-AC002",
        "BRD-WS-14-R018-AC003"
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
    "source_fingerprint": "ecafee3537bb7e96347ffbe5356ab225e48e4eb9156f0976a53e1806a7dd1c1d",
    "source_lines": "L5748-L5823",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R018"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R019",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "2961ef8ff592f7676248e0234d949538994db0e6572359472c1183ce292a2ea6"
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
        "BRD-WS-14-R019-AC001",
        "BRD-WS-14-R019-AC002",
        "BRD-WS-14-R019-AC003"
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
    "source_fingerprint": "2961ef8ff592f7676248e0234d949538994db0e6572359472c1183ce292a2ea6",
    "source_lines": "L5825-L5900",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R019"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R020",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "f26bbcfa2124f01092953373cb7b45fa97001e9bf83db2d7762352f8e6fa6f51"
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
        "BRD-WS-14-R020-AC001",
        "BRD-WS-14-R020-AC002",
        "BRD-WS-14-R020-AC003"
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
    "source_lines": "L5902-L5977",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R020"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R021",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "1493ddac14ea07c37a234488d9b01d25888cf82079e7cd7080d8a1724e0090bf"
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
        "BRD-WS-14-R021-AC001",
        "BRD-WS-14-R021-AC002",
        "BRD-WS-14-R021-AC003"
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
    "source_lines": "L5979-L6054",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R021"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R022",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "b0db4e81ec219cb517f7c9eb3c45f0c65862f663d01ce155b603f666c8e24721"
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
        "BRD-WS-14-R022-AC001",
        "BRD-WS-14-R022-AC002",
        "BRD-WS-14-R022-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R022-O001",
      "obligation_text": "Rollback không được làm mất: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R022 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R022 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R022 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-14-R022-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-14-R022-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-14-R022 does not define a recovery obligation."
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
    "source_lines": "L6056-L6164",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R022"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R023",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "d16de75730bc81e65464b72bfecba6deeb26fd98af793152fc80e78cdd7894a4"
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
        "BRD-WS-14-R023-AC001",
        "BRD-WS-14-R023-AC002",
        "BRD-WS-14-R023-AC003"
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
    "source_fingerprint": "d16de75730bc81e65464b72bfecba6deeb26fd98af793152fc80e78cdd7894a4",
    "source_lines": "L6166-L6241",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R023"
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
      "requirement_id": "BRD-WS-14-R024",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "150c85fbaa623d6c60085cb3dc67fb8e837cfd87b02e807e28a4c0e9114e2da2"
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
        "BRD-WS-14-R024-AC001",
        "BRD-WS-14-R024-AC002",
        "BRD-WS-14-R024-AC003"
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
    "source_fingerprint": "150c85fbaa623d6c60085cb3dc67fb8e837cfd87b02e807e28a4c0e9114e2da2",
    "source_lines": "L6243-L6324",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R024"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-014",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R025",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "55d489bc18404f4017ab8ccc5eb3aa9f82976f5831919ae0a22f62925b7a8e84"
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
        "BRD-WS-14-R025-AC001",
        "BRD-WS-14-R025-AC002",
        "BRD-WS-14-R025-AC003"
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
    "source_lines": "L6326-L6405",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R025"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R026",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "26be61dae2a993e528a201f0e6e7c80982ba0e7eb7acc4bf8985a21175483ce2"
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
        "BRD-WS-14-R026-AC001",
        "BRD-WS-14-R026-AC002",
        "BRD-WS-14-R026-AC003"
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
    "source_lines": "L6407-L6482",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R026"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R028",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "7a5dd8629eaa6ae44e16a830d4952a841071d88d5f4fb7f7d22a7216a7eab3d3"
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
        "BRD-WS-14-R028-AC001",
        "BRD-WS-14-R028-AC002",
        "BRD-WS-14-R028-AC003"
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
    "source_lines": "L6484-L6559",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R028"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "A matrix may contain denied capabilities but must exist"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-14-R029.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                "source_type": "SOURCE_LITERAL",
                "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
              },
              "identifier": "BRD-WS-14-R029.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                "source_lines": "L753",
                "source_section": "28. Configuration Capability Matrix"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
            "source_lines": "L753",
            "source_section": "28. Configuration Capability Matrix"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-14-R029.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                "source_type": "SOURCE_LITERAL",
                "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
              },
              "identifier": "BRD-WS-14-R029.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                "source_lines": "L753",
                "source_section": "28. Configuration Capability Matrix"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
            "source_lines": "L753",
            "source_section": "28. Configuration Capability Matrix"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
            "source_type": "SOURCE_LITERAL",
            "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
          },
          "identifier": "BRD-WS-14-R029.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
            "source_lines": "L753",
            "source_section": "28. Configuration Capability Matrix"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
            "source_type": "SOURCE_LITERAL",
            "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
          },
          "identifier": "BRD-WS-14-R029.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
            "source_lines": "L753",
            "source_section": "28. Configuration Capability Matrix"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
            "source_type": "SOURCE_LITERAL",
            "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
          },
          "identifier": "BRD-WS-14-R029.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
            "source_lines": "L753",
            "source_section": "28. Configuration Capability Matrix"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
            "source_type": "SOURCE_LITERAL",
            "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
          },
          "identifier": "BRD-WS-14-R029.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
            "source_lines": "L753",
            "source_section": "28. Configuration Capability Matrix"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
            "source_type": "SOURCE_LITERAL",
            "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
          },
          "identifier": "BRD-WS-14-R029.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
            "source_lines": "L753",
            "source_section": "28. Configuration Capability Matrix"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-14-R029",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "The Configuration has no Capability Matrix"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "The Configuration defines a Capability Matrix"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-005"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
      "source_lines": "L753",
      "source_section": "28. Configuration Capability Matrix"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
          "source_type": "SOURCE_LITERAL",
          "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
        },
        "identifier": "BRD-WS-14-R029.BRD-WS-14-R029.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-14-R029.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-005"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-14.md",
          "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
          "source_lines": "L753",
          "source_section": "28. Configuration Capability Matrix"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-14-R029.BRD-WS-14-R029.BRD-WS-14-R029.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-14-R029.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.CONFIGURATION_ID",
        "FIELD.CAPABILITY_MATRIX_ID",
        "FIELD.MATRIX_VERSION",
        "FIELD.VALIDATION_RESULT"
      ],
      "producer": "BRD-WS-14-R029.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-14-R029.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.CONFIGURATION_ID",
        "FIELD.CAPABILITY_MATRIX_ID",
        "FIELD.MATRIX_VERSION",
        "FIELD.VALIDATION_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-14-R029.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-14-R029.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-14-R029.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-14-R029-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID",
          "evaluator_consumed_bindings": [
            "allowed_lifecycle_states",
            "allowed_states",
            "reference",
            "registry",
            "registry_source",
            "target_id",
            "target_type"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
              "source_type": "SOURCE_LITERAL",
              "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
            },
            "identifier": "BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-005"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-14.md",
              "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
              "source_lines": "L753",
              "source_section": "28. Configuration Capability Matrix"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-14-R029.BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
              "source_type": "SOURCE_LITERAL",
              "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
            },
            "identifier": "BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-005"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-14.md",
              "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
              "source_lines": "L753",
              "source_section": "28. Configuration Capability Matrix"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "allowed_lifecycle_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-14-R029.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                      "source_type": "SOURCE_LITERAL",
                      "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
                    },
                    "identifier": "BRD-WS-14-R029.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-005"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-14.md",
                      "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                      "source_lines": "L753",
                      "source_section": "28. Configuration Capability Matrix"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                  "source_lines": "L753",
                  "source_section": "28. Configuration Capability Matrix"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-14-R029.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                      "source_type": "SOURCE_LITERAL",
                      "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
                    },
                    "identifier": "BRD-WS-14-R029.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-005"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-14.md",
                      "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                      "source_lines": "L753",
                      "source_section": "28. Configuration Capability Matrix"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                  "source_lines": "L753",
                  "source_section": "28. Configuration Capability Matrix"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                  "source_type": "SOURCE_LITERAL",
                  "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
                },
                "identifier": "BRD-WS-14-R029.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                  "source_lines": "L753",
                  "source_section": "28. Configuration Capability Matrix"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                  "source_type": "SOURCE_LITERAL",
                  "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
                },
                "identifier": "BRD-WS-14-R029.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                  "source_lines": "L753",
                  "source_section": "28. Configuration Capability Matrix"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                  "source_type": "SOURCE_LITERAL",
                  "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
                },
                "identifier": "BRD-WS-14-R029.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                  "source_lines": "L753",
                  "source_section": "28. Configuration Capability Matrix"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                  "source_type": "SOURCE_LITERAL",
                  "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
                },
                "identifier": "BRD-WS-14-R029.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                  "source_lines": "L753",
                  "source_section": "28. Configuration Capability Matrix"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                  "source_type": "SOURCE_LITERAL",
                  "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
                },
                "identifier": "BRD-WS-14-R029.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                  "source_lines": "L753",
                  "source_section": "28. Configuration Capability Matrix"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                  "source_type": "SOURCE_LITERAL",
                  "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
                },
                "identifier": "BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                  "source_lines": "L753",
                  "source_section": "28. Configuration Capability Matrix"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                  "source_type": "SOURCE_LITERAL",
                  "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
                },
                "identifier": "BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                  "source_lines": "L753",
                  "source_section": "28. Configuration Capability Matrix"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-14-R029.BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                "source_type": "SOURCE_LITERAL",
                "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
              },
              "identifier": "BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                "source_lines": "L753",
                "source_section": "28. Configuration Capability Matrix"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-14-R029.BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "BRD-WS-14-R029-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
              "source_type": "SOURCE_LITERAL",
              "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
            },
            "identifier": "BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-005"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-14.md",
              "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
              "source_lines": "L753",
              "source_section": "28. Configuration Capability Matrix"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BRD-WS-14-R029.BRD-WS-14-R029.BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "operator_id": "REFERENCE_TARGET_VALID",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "allowed_lifecycle_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-WS-14-R029.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                    "source_type": "SOURCE_LITERAL",
                    "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
                  },
                  "identifier": "BRD-WS-14-R029.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-005"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-14.md",
                    "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                    "source_lines": "L753",
                    "source_section": "28. Configuration Capability Matrix"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                "source_lines": "L753",
                "source_section": "28. Configuration Capability Matrix"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-WS-14-R029.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                    "source_type": "SOURCE_LITERAL",
                    "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
                  },
                  "identifier": "BRD-WS-14-R029.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-005"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-14.md",
                    "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                    "source_lines": "L753",
                    "source_section": "28. Configuration Capability Matrix"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                "source_lines": "L753",
                "source_section": "28. Configuration Capability Matrix"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                "source_type": "SOURCE_LITERAL",
                "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
              },
              "identifier": "BRD-WS-14-R029.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                "source_lines": "L753",
                "source_section": "28. Configuration Capability Matrix"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                "source_type": "SOURCE_LITERAL",
                "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
              },
              "identifier": "BRD-WS-14-R029.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                "source_lines": "L753",
                "source_section": "28. Configuration Capability Matrix"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                "source_type": "SOURCE_LITERAL",
                "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
              },
              "identifier": "BRD-WS-14-R029.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                "source_lines": "L753",
                "source_section": "28. Configuration Capability Matrix"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                "source_type": "SOURCE_LITERAL",
                "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
              },
              "identifier": "BRD-WS-14-R029.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                "source_lines": "L753",
                "source_section": "28. Configuration Capability Matrix"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
                "source_type": "SOURCE_LITERAL",
                "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
              },
              "identifier": "BRD-WS-14-R029.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
                "source_lines": "L753",
                "source_section": "28. Configuration Capability Matrix"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.BRD-WS-14-R029.BRD-WS-14-R029.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "A matrix may contain denied capabilities but must exist"
      ],
      "contract_ast_sha256": "5a00a0af8c1e9daf6cf6c7edc7b69be58749fa9ab943cd5124e37b3e2677f7b5",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-14-R029",
      "criticality": "NORMAL",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-14.md#28. Configuration Capability Matrix",
            "source_type": "SOURCE_LITERAL",
            "version": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a"
          },
          "identifier": "BRD-WS-14-R029.BRD-WS-14-R029.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-14-R029.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
            "source_lines": "L753",
            "source_section": "28. Configuration Capability Matrix"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-14-R029.BRD-WS-14-R029.BRD-WS-14-R029.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-14-R029.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.CONFIGURATION_ID",
          "FIELD.CAPABILITY_MATRIX_ID",
          "FIELD.MATRIX_VERSION",
          "FIELD.VALIDATION_RESULT"
        ],
        "producer": "BRD-WS-14-R029.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-14-R029.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.CONFIGURATION_ID",
          "FIELD.CAPABILITY_MATRIX_ID",
          "FIELD.MATRIX_VERSION",
          "FIELD.VALIDATION_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-14-R029.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-14-R029.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-14-R029.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-B50D65DE9FAE2227D764",
        "P2C-C4-FX-0CBD84EBFFB99F29CE54",
        "P2C-C4-FX-7CDEB9DA46BA23F98382"
      ],
      "high_risk_audit_subset": false,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "The Configuration has no Capability Matrix"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-14-R029-O001",
          "obligation_text": "Mỗi Configuration phải định nghĩa Capability Matrix"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-14-R029.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-14-R029-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "The Configuration defines a Capability Matrix"
      ],
      "preconditions": [
        "The Configuration identity exists"
      ],
      "prohibitions": [
        "The Configuration has no Capability Matrix"
      ],
      "requirement_id": "BRD-WS-14-R029",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-005"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-14.md",
        "source_fingerprint": "f1b22cd7a660f01303808eb7c600ef8cd4f926f5a4690740b6d4e376de05311a",
        "source_lines": "L753",
        "source_section": "28. Configuration Capability Matrix"
      },
      "source_statement": "Mỗi Configuration phải định nghĩa Capability Matrix.",
      "surrounding_source_context": "### BRD-WS-14-R029 — Mỗi Configuration phải định nghĩa Capability Matrix"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-14-R029",
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
        "BRD-WS-14-R029-AC001",
        "BRD-WS-14-R029-AC002",
        "BRD-WS-14-R029-AC003"
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
    "source_lines": "L6561-L7982",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R029"
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
### BRD-WS-14-R030 — Mỗi Configuration Capability Matrix phải định nghĩa Read, Create, Edit, Delete, Override, Clone,…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R030",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "bac1ab2d8504b9328047fb1a60501fb058cd7834a4e129803904c1b6d5a947b1"
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
        "BRD-WS-14-R030-AC001",
        "BRD-WS-14-R030-AC002",
        "BRD-WS-14-R030-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R030-O001",
      "obligation_text": "Mỗi Configuration Capability Matrix phải định nghĩa Read, Create, Edit, Delete, Override, Clone, Import, Export, Approval Required và Runtime Reload Supported"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Configuration Capability Matrix phải định nghĩa Read, Create, Edit, Delete, Override, Clone, Import, Export, Approval Required và Runtime Reload Supported.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-14.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "28. Configuration Capability Matrix"
    },
    "deterministic_transformation": "RESTORE_CONFIGURATION_MATRIX_SUBJECT",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-14-030",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-14-030",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "1. Workshop Objective",
    "source_context_sha256": "4874f7decb0ca7427cd9840d305561e668d5b5e66020de3c80501b800cb88c47",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "bac1ab2d8504b9328047fb1a60501fb058cd7834a4e129803904c1b6d5a947b1",
    "source_fingerprint_before_c3": "ce1d0a5b4062200dd152903c1c3dc033dfb45004c6db516f5a3f3fd8aa749962",
    "source_lines": "L7984-L8084",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-14.md",
      "lines": "L755-L766",
      "section": "28. Configuration Capability Matrix"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R030"
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
  "title": "Mỗi Configuration Capability Matrix phải định nghĩa Read, Create, Edit, Delete, Override, Clone,…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R031 — Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Cap…

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Unaffected dependencies remain outside the set"
    ],
    "concrete_bindings": [
      {
        "actual_set": {
          "allowed_target_types": [
            "CONFIGURATION_KEY",
            "CAPABILITY_ID"
          ],
          "authoritative_source": {
            "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
            "source_type": "EVIDENCE_OBJECT",
            "version_source": "FIELD.IMPACT_VERSION"
          },
          "identifier": "REPORTED_AFFECTED_NODE_REFERENCES",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.NODE_REFERENCE",
          "origin": {
            "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "accepted_type_model_disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
            "source_lines": "L815-L855",
            "source_section": "30. Configuration Dependency Graph"
          },
          "resolved_members": [
            {
              "authoritative_source": {
                "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                "source_type": "VERSIONED_CONFIGURATION",
                "version": "FIELD.IMPACT_VERSION"
              },
              "identifier": "AFFECTED_CONFIGURATION_FIXTURE_001",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
              "origin": {
                "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT.CONFIGURATION_KEY",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                "source_lines": "L851",
                "source_section": "30. Configuration Dependency Graph"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [
                  "EVIDENCE_OBJECT_REF"
                ],
                "output_type": "REFERENCE_ID",
                "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                "version": "1.0.0-amendment.a1"
              },
              "semantic_type": "REFERENCE_ID",
              "target_type": "CONFIGURATION_KEY"
            },
            {
              "authoritative_source": {
                "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                "source_type": "VERSIONED_CONFIGURATION",
                "version": "FIELD.IMPACT_VERSION"
              },
              "identifier": "AFFECTED_CAPABILITY_FIXTURE_001",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
              "origin": {
                "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT.CAPABILITY_ID",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                "source_lines": "L851",
                "source_section": "30. Configuration Dependency Graph"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [
                  "EVIDENCE_OBJECT_REF"
                ],
                "output_type": "REFERENCE_ID",
                "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                "version": "1.0.0-amendment.a1"
              },
              "semantic_type": "REFERENCE_ID",
              "target_type": "CAPABILITY_ID"
            }
          ],
          "resolver_contract": {
            "deterministic": true,
            "input_types": [
              "EVIDENCE_OBJECT_REF"
            ],
            "output_type": "SET_OF<REFERENCE_ID>",
            "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
            "version": "1.0.0-amendment.a1"
          },
          "semantic_type": "RUNTIME_SET_REF<REFERENCE_ID>"
        },
        "expected_set": {
          "allowed_target_types": [
            "CONFIGURATION_KEY",
            "CAPABILITY_ID"
          ],
          "authoritative_source": {
            "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
            "source_type": "VERSIONED_CONFIGURATION",
            "version_source": "FIELD.IMPACT_VERSION"
          },
          "identifier": "AFFECTED_NODE_REFERENCES",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
          "origin": {
            "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION",
            "origin_type": "VERSIONED_CONFIGURATION"
          },
          "provenance": {
            "accepted_type_model_disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
            "source_lines": "L815-L855",
            "source_section": "30. Configuration Dependency Graph"
          },
          "resolved_members": [
            {
              "authoritative_source": {
                "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                "source_type": "VERSIONED_CONFIGURATION",
                "version": "FIELD.IMPACT_VERSION"
              },
              "identifier": "AFFECTED_CONFIGURATION_FIXTURE_001",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
              "origin": {
                "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION.CONFIGURATION_KEY",
                "origin_type": "VERSIONED_CONFIGURATION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                "source_lines": "L851",
                "source_section": "30. Configuration Dependency Graph"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [
                  "HASH"
                ],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                "version": "1.0.0-amendment.a1"
              },
              "semantic_type": "REFERENCE_ID",
              "target_type": "CONFIGURATION_KEY"
            },
            {
              "authoritative_source": {
                "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                "source_type": "VERSIONED_CONFIGURATION",
                "version": "FIELD.IMPACT_VERSION"
              },
              "identifier": "AFFECTED_CAPABILITY_FIXTURE_001",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
              "origin": {
                "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION.CAPABILITY_ID",
                "origin_type": "VERSIONED_CONFIGURATION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                "source_lines": "L851",
                "source_section": "30. Configuration Dependency Graph"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [
                  "HASH"
                ],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                "version": "1.0.0-amendment.a1"
              },
              "semantic_type": "REFERENCE_ID",
              "target_type": "CAPABILITY_ID"
            }
          ],
          "resolver_contract": {
            "deterministic": true,
            "input_types": [
              "CONFIGURATION_KEY",
              "HASH"
            ],
            "output_type": "SET_OF<REFERENCE_ID>",
            "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
            "version": "1.0.0-amendment.a1"
          },
          "semantic_type": "CANONICAL_SET_REF<REFERENCE_ID>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-14-R031",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "An affected dependency is omitted from the impact set"
    ],
    "operator_composition": [
      "SET_EQUALS"
    ],
    "positive_oracle": [
      "All affected Configurations and Business Capabilities are identified"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-005"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
      "source_lines": "L851",
      "source_section": "30. Configuration Dependency Graph"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-14.md#30. Configuration Dependency Graph",
          "source_type": "SOURCE_LITERAL",
          "version": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98"
        },
        "identifier": "BRD-WS-14-R031.BRD-WS-14-R031.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-14-R031.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-005"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-14.md",
          "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
          "source_lines": "L851",
          "source_section": "30. Configuration Dependency Graph"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-14-R031.BRD-WS-14-R031.BRD-WS-14-R031.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-14-R031.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.CHANGED_CONFIGURATION_ID",
        "FIELD.DEPENDENCY_GRAPH",
        "FIELD.AFFECTED_CONFIGURATION_IDS",
        "FIELD.AFFECTED_CAPABILITY_IDS",
        "FIELD.IMPACT_VERSION"
      ],
      "producer": "BRD-WS-14-R031.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-14-R031.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.CHANGED_CONFIGURATION_ID",
        "FIELD.DEPENDENCY_GRAPH",
        "FIELD.AFFECTED_CONFIGURATION_IDS",
        "FIELD.AFFECTED_CAPABILITY_IDS",
        "FIELD.IMPACT_VERSION"
      ],
      "required_values_or_hashes": [
        "BRD-WS-14-R031.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-14-R031.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-14-R031.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-14-R031-O001"
    ],
    "typed_contract_ast": {
      "accepted_infrastructure_amendment": "V23-P2C-SEMANTIC-INFRASTRUCTURE-AMENDMENT-A1",
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-14-R031.O1.1.SET_EQUALS",
          "evaluator_consumed_bindings": [
            "actual_set",
            "expected_set"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-14.md#30. Configuration Dependency Graph",
              "source_type": "SOURCE_LITERAL",
              "version": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98"
            },
            "identifier": "BRD-WS-14-R031.BRD-WS-14-R031.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-14-R031.O1.1.SET_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-005"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-14.md",
              "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
              "source_lines": "L851",
              "source_section": "30. Configuration Dependency Graph"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-14-R031.BRD-WS-14-R031.BRD-WS-14-R031.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                  "source_type": "VERSIONED_CONFIGURATION",
                  "version": "FIELD.IMPACT_VERSION"
                },
                "identifier": "AFFECTED_CONFIGURATION_FIXTURE_001",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                "origin": {
                  "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION.CONFIGURATION_KEY",
                  "origin_type": "VERSIONED_CONFIGURATION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                  "source_lines": "L851",
                  "source_section": "30. Configuration Dependency Graph"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [
                    "HASH"
                  ],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                  "version": "1.0.0-amendment.a1"
                },
                "semantic_type": "REFERENCE_ID",
                "target_type": "CONFIGURATION_KEY"
              },
              {
                "authoritative_source": {
                  "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                  "source_type": "VERSIONED_CONFIGURATION",
                  "version": "FIELD.IMPACT_VERSION"
                },
                "identifier": "AFFECTED_CAPABILITY_FIXTURE_001",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                "origin": {
                  "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION.CAPABILITY_ID",
                  "origin_type": "VERSIONED_CONFIGURATION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                  "source_lines": "L851",
                  "source_section": "30. Configuration Dependency Graph"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [
                    "HASH"
                  ],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                  "version": "1.0.0-amendment.a1"
                },
                "semantic_type": "REFERENCE_ID",
                "target_type": "CAPABILITY_ID"
              }
            ],
            "origin": {
              "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION",
              "origin_type": "VERSIONED_CONFIGURATION"
            },
            "provenance": {
              "accepted_type_model_disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-14.md",
              "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
              "source_lines": "L815-L855",
              "source_section": "30. Configuration Dependency Graph"
            },
            "semantic_type": "SET_OF<REFERENCE_ID>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "allowed_target_types": [
                  "CONFIGURATION_KEY",
                  "CAPABILITY_ID"
                ],
                "authoritative_source": {
                  "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                  "source_type": "EVIDENCE_OBJECT",
                  "version_source": "FIELD.IMPACT_VERSION"
                },
                "identifier": "REPORTED_AFFECTED_NODE_REFERENCES",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.NODE_REFERENCE",
                "origin": {
                  "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "accepted_type_model_disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                  "source_lines": "L815-L855",
                  "source_section": "30. Configuration Dependency Graph"
                },
                "resolved_members": [
                  {
                    "authoritative_source": {
                      "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                      "source_type": "VERSIONED_CONFIGURATION",
                      "version": "FIELD.IMPACT_VERSION"
                    },
                    "identifier": "AFFECTED_CONFIGURATION_FIXTURE_001",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                    "origin": {
                      "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT.CONFIGURATION_KEY",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-005"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-14.md",
                      "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                      "source_lines": "L851",
                      "source_section": "30. Configuration Dependency Graph"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [
                        "EVIDENCE_OBJECT_REF"
                      ],
                      "output_type": "REFERENCE_ID",
                      "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                      "version": "1.0.0-amendment.a1"
                    },
                    "semantic_type": "REFERENCE_ID",
                    "target_type": "CONFIGURATION_KEY"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                      "source_type": "VERSIONED_CONFIGURATION",
                      "version": "FIELD.IMPACT_VERSION"
                    },
                    "identifier": "AFFECTED_CAPABILITY_FIXTURE_001",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                    "origin": {
                      "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT.CAPABILITY_ID",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-005"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-14.md",
                      "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                      "source_lines": "L851",
                      "source_section": "30. Configuration Dependency Graph"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [
                        "EVIDENCE_OBJECT_REF"
                      ],
                      "output_type": "REFERENCE_ID",
                      "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                      "version": "1.0.0-amendment.a1"
                    },
                    "semantic_type": "REFERENCE_ID",
                    "target_type": "CAPABILITY_ID"
                  }
                ],
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [
                    "EVIDENCE_OBJECT_REF"
                  ],
                  "output_type": "SET_OF<REFERENCE_ID>",
                  "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                  "version": "1.0.0-amendment.a1"
                },
                "semantic_type": "RUNTIME_SET_REF<REFERENCE_ID>"
              },
              "expected_set": {
                "allowed_target_types": [
                  "CONFIGURATION_KEY",
                  "CAPABILITY_ID"
                ],
                "authoritative_source": {
                  "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                  "source_type": "VERSIONED_CONFIGURATION",
                  "version_source": "FIELD.IMPACT_VERSION"
                },
                "identifier": "AFFECTED_NODE_REFERENCES",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                "origin": {
                  "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION",
                  "origin_type": "VERSIONED_CONFIGURATION"
                },
                "provenance": {
                  "accepted_type_model_disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                  "source_lines": "L815-L855",
                  "source_section": "30. Configuration Dependency Graph"
                },
                "resolved_members": [
                  {
                    "authoritative_source": {
                      "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                      "source_type": "VERSIONED_CONFIGURATION",
                      "version": "FIELD.IMPACT_VERSION"
                    },
                    "identifier": "AFFECTED_CONFIGURATION_FIXTURE_001",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                    "origin": {
                      "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION.CONFIGURATION_KEY",
                      "origin_type": "VERSIONED_CONFIGURATION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-005"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-14.md",
                      "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                      "source_lines": "L851",
                      "source_section": "30. Configuration Dependency Graph"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [
                        "HASH"
                      ],
                      "output_type": "REFERENCE_ID",
                      "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                      "version": "1.0.0-amendment.a1"
                    },
                    "semantic_type": "REFERENCE_ID",
                    "target_type": "CONFIGURATION_KEY"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                      "source_type": "VERSIONED_CONFIGURATION",
                      "version": "FIELD.IMPACT_VERSION"
                    },
                    "identifier": "AFFECTED_CAPABILITY_FIXTURE_001",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                    "origin": {
                      "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION.CAPABILITY_ID",
                      "origin_type": "VERSIONED_CONFIGURATION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-005"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-14.md",
                      "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                      "source_lines": "L851",
                      "source_section": "30. Configuration Dependency Graph"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [
                        "HASH"
                      ],
                      "output_type": "REFERENCE_ID",
                      "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                      "version": "1.0.0-amendment.a1"
                    },
                    "semantic_type": "REFERENCE_ID",
                    "target_type": "CAPABILITY_ID"
                  }
                ],
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [
                    "CONFIGURATION_KEY",
                    "HASH"
                  ],
                  "output_type": "SET_OF<REFERENCE_ID>",
                  "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                  "version": "1.0.0-amendment.a1"
                },
                "semantic_type": "CANONICAL_SET_REF<REFERENCE_ID>"
              }
            },
            "comparison": {
              "expected": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                      "source_type": "VERSIONED_CONFIGURATION",
                      "version": "FIELD.IMPACT_VERSION"
                    },
                    "identifier": "AFFECTED_CONFIGURATION_FIXTURE_001",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                    "origin": {
                      "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION.CONFIGURATION_KEY",
                      "origin_type": "VERSIONED_CONFIGURATION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-005"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-14.md",
                      "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                      "source_lines": "L851",
                      "source_section": "30. Configuration Dependency Graph"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [
                        "HASH"
                      ],
                      "output_type": "REFERENCE_ID",
                      "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                      "version": "1.0.0-amendment.a1"
                    },
                    "semantic_type": "REFERENCE_ID",
                    "target_type": "CONFIGURATION_KEY"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                      "source_type": "VERSIONED_CONFIGURATION",
                      "version": "FIELD.IMPACT_VERSION"
                    },
                    "identifier": "AFFECTED_CAPABILITY_FIXTURE_001",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                    "origin": {
                      "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION.CAPABILITY_ID",
                      "origin_type": "VERSIONED_CONFIGURATION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-005"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-14.md",
                      "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                      "source_lines": "L851",
                      "source_section": "30. Configuration Dependency Graph"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [
                        "HASH"
                      ],
                      "output_type": "REFERENCE_ID",
                      "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                      "version": "1.0.0-amendment.a1"
                    },
                    "semantic_type": "REFERENCE_ID",
                    "target_type": "CAPABILITY_ID"
                  }
                ],
                "origin": {
                  "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION",
                  "origin_type": "VERSIONED_CONFIGURATION"
                },
                "provenance": {
                  "accepted_type_model_disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                  "source_lines": "L815-L855",
                  "source_section": "30. Configuration Dependency Graph"
                },
                "semantic_type": "SET_OF<REFERENCE_ID>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                      "source_type": "VERSIONED_CONFIGURATION",
                      "version": "FIELD.IMPACT_VERSION"
                    },
                    "identifier": "AFFECTED_CONFIGURATION_FIXTURE_001",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                    "origin": {
                      "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT.CONFIGURATION_KEY",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-005"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-14.md",
                      "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                      "source_lines": "L851",
                      "source_section": "30. Configuration Dependency Graph"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [
                        "EVIDENCE_OBJECT_REF"
                      ],
                      "output_type": "REFERENCE_ID",
                      "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                      "version": "1.0.0-amendment.a1"
                    },
                    "semantic_type": "REFERENCE_ID",
                    "target_type": "CONFIGURATION_KEY"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                      "source_type": "VERSIONED_CONFIGURATION",
                      "version": "FIELD.IMPACT_VERSION"
                    },
                    "identifier": "AFFECTED_CAPABILITY_FIXTURE_001",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                    "origin": {
                      "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT.CAPABILITY_ID",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-005"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-14.md",
                      "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                      "source_lines": "L851",
                      "source_section": "30. Configuration Dependency Graph"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [
                        "EVIDENCE_OBJECT_REF"
                      ],
                      "output_type": "REFERENCE_ID",
                      "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                      "version": "1.0.0-amendment.a1"
                    },
                    "semantic_type": "REFERENCE_ID",
                    "target_type": "CAPABILITY_ID"
                  }
                ],
                "origin": {
                  "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "accepted_type_model_disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                  "source_lines": "L815-L855",
                  "source_section": "30. Configuration Dependency Graph"
                },
                "semantic_type": "SET_OF<REFERENCE_ID>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#30. Configuration Dependency Graph",
                "source_type": "SOURCE_LITERAL",
                "version": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98"
              },
              "identifier": "BRD-WS-14-R031.BRD-WS-14-R031.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-14-R031.O1.1.SET_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-005"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                "source_lines": "L851",
                "source_section": "30. Configuration Dependency Graph"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-14-R031.BRD-WS-14-R031.BRD-WS-14-R031.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "generic_set_type_parameter": "REFERENCE_ID",
            "operator_id": "SET_EQUALS",
            "required_evidence_fields": [
              "FIELD.CHANGED_CONFIGURATION_ID",
              "FIELD.DEPENDENCY_GRAPH",
              "FIELD.AFFECTED_CONFIGURATION_IDS",
              "FIELD.AFFECTED_CAPABILITY_IDS",
              "FIELD.IMPACT_VERSION"
            ]
          },
          "obligation_id": "BRD-WS-14-R031-O001",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                  "source_type": "VERSIONED_CONFIGURATION",
                  "version": "FIELD.IMPACT_VERSION"
                },
                "identifier": "AFFECTED_CONFIGURATION_FIXTURE_001",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                "origin": {
                  "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT.CONFIGURATION_KEY",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                  "source_lines": "L851",
                  "source_section": "30. Configuration Dependency Graph"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [
                    "EVIDENCE_OBJECT_REF"
                  ],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                  "version": "1.0.0-amendment.a1"
                },
                "semantic_type": "REFERENCE_ID",
                "target_type": "CONFIGURATION_KEY"
              },
              {
                "authoritative_source": {
                  "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                  "source_type": "VERSIONED_CONFIGURATION",
                  "version": "FIELD.IMPACT_VERSION"
                },
                "identifier": "AFFECTED_CAPABILITY_FIXTURE_001",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                "origin": {
                  "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT.CAPABILITY_ID",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-005"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                  "source_lines": "L851",
                  "source_section": "30. Configuration Dependency Graph"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [
                    "EVIDENCE_OBJECT_REF"
                  ],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                  "version": "1.0.0-amendment.a1"
                },
                "semantic_type": "REFERENCE_ID",
                "target_type": "CAPABILITY_ID"
              }
            ],
            "origin": {
              "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "accepted_type_model_disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-14.md",
              "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
              "source_lines": "L815-L855",
              "source_section": "30. Configuration Dependency Graph"
            },
            "semantic_type": "SET_OF<REFERENCE_ID>"
          },
          "operator_id": "SET_EQUALS",
          "operator_version": "1.1.0-amendment.a1",
          "typed_bindings": {
            "actual_set": {
              "allowed_target_types": [
                "CONFIGURATION_KEY",
                "CAPABILITY_ID"
              ],
              "authoritative_source": {
                "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                "source_type": "EVIDENCE_OBJECT",
                "version_source": "FIELD.IMPACT_VERSION"
              },
              "identifier": "REPORTED_AFFECTED_NODE_REFERENCES",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.NODE_REFERENCE",
              "origin": {
                "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "accepted_type_model_disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                "source_lines": "L815-L855",
                "source_section": "30. Configuration Dependency Graph"
              },
              "resolved_members": [
                {
                  "authoritative_source": {
                    "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                    "source_type": "VERSIONED_CONFIGURATION",
                    "version": "FIELD.IMPACT_VERSION"
                  },
                  "identifier": "AFFECTED_CONFIGURATION_FIXTURE_001",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                  "origin": {
                    "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT.CONFIGURATION_KEY",
                    "origin_type": "RUNTIME_OBSERVED"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-005"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-14.md",
                    "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                    "source_lines": "L851",
                    "source_section": "30. Configuration Dependency Graph"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [
                      "EVIDENCE_OBJECT_REF"
                    ],
                    "output_type": "REFERENCE_ID",
                    "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                    "version": "1.0.0-amendment.a1"
                  },
                  "semantic_type": "REFERENCE_ID",
                  "target_type": "CONFIGURATION_KEY"
                },
                {
                  "authoritative_source": {
                    "source_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.RESULT",
                    "source_type": "VERSIONED_CONFIGURATION",
                    "version": "FIELD.IMPACT_VERSION"
                  },
                  "identifier": "AFFECTED_CAPABILITY_FIXTURE_001",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                  "origin": {
                    "origin_id": "YSIM.CONFIGURATION_IMPACT_ANALYSIS.EXECUTION_RESULT.CAPABILITY_ID",
                    "origin_type": "RUNTIME_OBSERVED"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-005"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-14.md",
                    "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                    "source_lines": "L851",
                    "source_section": "30. Configuration Dependency Graph"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [
                      "EVIDENCE_OBJECT_REF"
                    ],
                    "output_type": "REFERENCE_ID",
                    "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                    "version": "1.0.0-amendment.a1"
                  },
                  "semantic_type": "REFERENCE_ID",
                  "target_type": "CAPABILITY_ID"
                }
              ],
              "resolver_contract": {
                "deterministic": true,
                "input_types": [
                  "EVIDENCE_OBJECT_REF"
                ],
                "output_type": "SET_OF<REFERENCE_ID>",
                "resolver_id": "OBSERVE.CONFIGURATION_IMPACT_ANALYSIS.REPORTED_AFFECTED_NODE_REFERENCES",
                "version": "1.0.0-amendment.a1"
              },
              "semantic_type": "RUNTIME_SET_REF<REFERENCE_ID>"
            },
            "expected_set": {
              "allowed_target_types": [
                "CONFIGURATION_KEY",
                "CAPABILITY_ID"
              ],
              "authoritative_source": {
                "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                "source_type": "VERSIONED_CONFIGURATION",
                "version_source": "FIELD.IMPACT_VERSION"
              },
              "identifier": "AFFECTED_NODE_REFERENCES",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
              "origin": {
                "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION",
                "origin_type": "VERSIONED_CONFIGURATION"
              },
              "provenance": {
                "accepted_type_model_disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                "source_lines": "L815-L855",
                "source_section": "30. Configuration Dependency Graph"
              },
              "resolved_members": [
                {
                  "authoritative_source": {
                    "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                    "source_type": "VERSIONED_CONFIGURATION",
                    "version": "FIELD.IMPACT_VERSION"
                  },
                  "identifier": "AFFECTED_CONFIGURATION_FIXTURE_001",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                  "origin": {
                    "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION.CONFIGURATION_KEY",
                    "origin_type": "VERSIONED_CONFIGURATION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-005"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-14.md",
                    "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                    "source_lines": "L851",
                    "source_section": "30. Configuration Dependency Graph"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [
                      "HASH"
                    ],
                    "output_type": "REFERENCE_ID",
                    "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                    "version": "1.0.0-amendment.a1"
                  },
                  "semantic_type": "REFERENCE_ID",
                  "target_type": "CONFIGURATION_KEY"
                },
                {
                  "authoritative_source": {
                    "source_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH",
                    "source_type": "VERSIONED_CONFIGURATION",
                    "version": "FIELD.IMPACT_VERSION"
                  },
                  "identifier": "AFFECTED_CAPABILITY_FIXTURE_001",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.NODE_REFERENCE",
                  "origin": {
                    "origin_id": "YSIM.CONFIGURATION_DEPENDENCY_GRAPH.VERSIONED_RESOLUTION.CAPABILITY_ID",
                    "origin_type": "VERSIONED_CONFIGURATION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-005"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-14.md",
                    "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
                    "source_lines": "L851",
                    "source_section": "30. Configuration Dependency Graph"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [
                      "HASH"
                    ],
                    "output_type": "REFERENCE_ID",
                    "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                    "version": "1.0.0-amendment.a1"
                  },
                  "semantic_type": "REFERENCE_ID",
                  "target_type": "CAPABILITY_ID"
                }
              ],
              "resolver_contract": {
                "deterministic": true,
                "input_types": [
                  "CONFIGURATION_KEY",
                  "HASH"
                ],
                "output_type": "SET_OF<REFERENCE_ID>",
                "resolver_id": "RESOLVE.CONFIGURATION_DEPENDENCY_GRAPH.AFFECTED_NODE_REFERENCES",
                "version": "1.0.0-amendment.a1"
              },
              "semantic_type": "CANONICAL_SET_REF<REFERENCE_ID>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Unaffected dependencies remain outside the set"
      ],
      "contract_ast_sha256": "2342aedfc016ba65695f620b701102b870e7b9f8eae0b29be1d13946a115a0bf",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-14-R031",
      "criticality": "NORMAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-14.md#30. Configuration Dependency Graph",
            "source_type": "SOURCE_LITERAL",
            "version": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98"
          },
          "identifier": "BRD-WS-14-R031.BRD-WS-14-R031.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-14-R031.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-005"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
            "source_lines": "L851",
            "source_section": "30. Configuration Dependency Graph"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-14-R031.BRD-WS-14-R031.BRD-WS-14-R031.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-14-R031.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.CHANGED_CONFIGURATION_ID",
          "FIELD.DEPENDENCY_GRAPH",
          "FIELD.AFFECTED_CONFIGURATION_IDS",
          "FIELD.AFFECTED_CAPABILITY_IDS",
          "FIELD.IMPACT_VERSION"
        ],
        "producer": "BRD-WS-14-R031.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-14-R031.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.CHANGED_CONFIGURATION_ID",
          "FIELD.DEPENDENCY_GRAPH",
          "FIELD.AFFECTED_CONFIGURATION_IDS",
          "FIELD.AFFECTED_CAPABILITY_IDS",
          "FIELD.IMPACT_VERSION"
        ],
        "required_values_or_hashes": [
          "BRD-WS-14-R031.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-14-R031.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-14-R031.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-R2-FX-F31F69A86FD58BE30F44",
        "P2C-C4-R2-FX-056A22B09B2EC5B5ADCC",
        "P2C-C4-R2-FX-8207E9E5875F5EF60BA1"
      ],
      "high_risk_audit_subset": false,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "An affected dependency is omitted from the impact set"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-14-R031-O001",
          "obligation_text": "Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Capability bị ảnh hưởng"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-14-R031.O1.1.SET_EQUALS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-14-R031-O001"
        }
      ],
      "operator_composition": [
        "SET_EQUALS"
      ],
      "positive_oracles": [
        "All affected Configurations and Business Capabilities are identified"
      ],
      "preconditions": [
        "The changed Configuration identity and dependency graph are available"
      ],
      "prohibitions": [
        "An affected dependency is omitted from the impact set"
      ],
      "requirement_id": "BRD-WS-14-R031",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_clarification_required": false,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-005"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-14.md",
        "source_fingerprint": "39191fa401eda0ef60c152a07a59a1213f121b35e097bd1520ab1997b7054d98",
        "source_lines": "L851",
        "source_section": "30. Configuration Dependency Graph"
      },
      "source_statement": "Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Capability bị ảnh hưởng.",
      "surrounding_source_context": "### BRD-WS-14-R031 — Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Cap…"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-14-R031",
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
        "BRD-WS-14-R031-AC001",
        "BRD-WS-14-R031-AC002",
        "BRD-WS-14-R031-AC003"
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
    "source_lines": "L8086-L9587",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R031"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R032",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "75597e69bf9a32aa03b7f66fe1aa7701304d37c32028fcc6e973c6431c606746"
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
        "BRD-WS-14-R032-AC001",
        "BRD-WS-14-R032-AC002",
        "BRD-WS-14-R032-AC003"
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
    "source_fingerprint": "75597e69bf9a32aa03b7f66fe1aa7701304d37c32028fcc6e973c6431c606746",
    "source_lines": "L9589-L9667",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R032"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R033",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "d8062897cb2931de6cb44491cd2210788bf304d3de1cfe1522ab26c07497abca"
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
        "BRD-WS-14-R033-AC001",
        "BRD-WS-14-R033-AC002",
        "BRD-WS-14-R033-AC003"
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
    "source_fingerprint": "d8062897cb2931de6cb44491cd2210788bf304d3de1cfe1522ab26c07497abca",
    "source_lines": "L9669-L9747",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R033"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R034",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "bf37e3e38d94cd4b4e937d0b5819d66b0905154719ec8b32189fe60c2617b8b7"
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
        "BRD-WS-14-R034-AC001",
        "BRD-WS-14-R034-AC002",
        "BRD-WS-14-R034-AC003"
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
    "source_fingerprint": "bf37e3e38d94cd4b4e937d0b5819d66b0905154719ec8b32189fe60c2617b8b7",
    "source_lines": "L9749-L9827",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R034"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R035",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "47c9132380c7f97d98464fbfba49984d3e4d8f1d6e8f870e65e36135891d9e5f"
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
        "BRD-WS-14-R035-AC001",
        "BRD-WS-14-R035-AC002",
        "BRD-WS-14-R035-AC003"
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
    "source_fingerprint": "47c9132380c7f97d98464fbfba49984d3e4d8f1d6e8f870e65e36135891d9e5f",
    "source_lines": "L9829-L9907",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R035"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R036",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "0ed672b66f2d3df7c02401758dbc99b5178d7deb11ad39b52c7265c4c98017c2"
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
        "BRD-WS-14-R036-AC001",
        "BRD-WS-14-R036-AC002",
        "BRD-WS-14-R036-AC003"
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
    "source_fingerprint": "0ed672b66f2d3df7c02401758dbc99b5178d7deb11ad39b52c7265c4c98017c2",
    "source_lines": "L9909-L9987",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R036"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R037",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "6c3a62bc5f14dab76972012aa84b39a485c8420eace48d6e92087dd18706b35e"
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
        "BRD-WS-14-R037-AC001",
        "BRD-WS-14-R037-AC002",
        "BRD-WS-14-R037-AC003"
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
    "source_fingerprint": "6c3a62bc5f14dab76972012aa84b39a485c8420eace48d6e92087dd18706b35e",
    "source_lines": "L9989-L10067",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R037"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R038",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "bf37e3e38d94cd4b4e937d0b5819d66b0905154719ec8b32189fe60c2617b8b7"
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
        "BRD-WS-14-R038-AC001",
        "BRD-WS-14-R038-AC002",
        "BRD-WS-14-R038-AC003"
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
    "source_fingerprint": "bf37e3e38d94cd4b4e937d0b5819d66b0905154719ec8b32189fe60c2617b8b7",
    "source_lines": "L10069-L10147",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R038"
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
### BRD-WS-14-R039 — Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R039",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "7ba5c852ac6c3626653d582e04d8e08f12aa230759aba6dfbdca564a125e873a"
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
        "BRD-WS-14-R039-AC001",
        "BRD-WS-14-R039-AC004",
        "BRD-WS-14-R039-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R039-O001",
      "obligation_text": "Reference Data là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R039-AC002",
        "BRD-WS-14-R039-AC004",
        "BRD-WS-14-R039-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R039-O002",
      "obligation_text": "Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R039-AC003",
        "BRD-WS-14-R039-AC004",
        "BRD-WS-14-R039-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R039-O003",
      "obligation_text": "Reference Data hỗ trợ: Multi-language"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform. Reference Data hỗ trợ: Multi-language.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R039",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Data",
    "source_context_sha256": "8159a2e679167d6d72d40b009066fd1f2181eed5a5122ec29675371dcf1ef8de",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "7ba5c852ac6c3626653d582e04d8e08f12aa230759aba6dfbdca564a125e873a",
    "source_fingerprint_before_c3": "7ba5c852ac6c3626653d582e04d8e08f12aa230759aba6dfbdca564a125e873a",
    "source_lines": "L10149-L10261",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R039"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-003"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R039",
  "title": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R040 — Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R040",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "9e65ca84ebb8e5365c8e79dbcd63854be818cf1af562d693a9173cd0911a9c60"
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
        "BRD-WS-14-R040-AC001",
        "BRD-WS-14-R040-AC004",
        "BRD-WS-14-R040-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R040-O001",
      "obligation_text": "Reference Data là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R040-AC002",
        "BRD-WS-14-R040-AC004",
        "BRD-WS-14-R040-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R040-O002",
      "obligation_text": "Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R040-AC003",
        "BRD-WS-14-R040-AC004",
        "BRD-WS-14-R040-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R040-O003",
      "obligation_text": "Reference Data hỗ trợ: Parent / Child"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform. Reference Data hỗ trợ: Parent / Child.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R040",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Data",
    "source_context_sha256": "8159a2e679167d6d72d40b009066fd1f2181eed5a5122ec29675371dcf1ef8de",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "9e65ca84ebb8e5365c8e79dbcd63854be818cf1af562d693a9173cd0911a9c60",
    "source_fingerprint_before_c3": "9e65ca84ebb8e5365c8e79dbcd63854be818cf1af562d693a9173cd0911a9c60",
    "source_lines": "L10263-L10375",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R040"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-003"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R040",
  "title": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R041 — Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R041",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "a2a7ff1d3fce44cbe903085a6bc2772dc87950deb4c615d819ab6604fe70c41f"
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
        "BRD-WS-14-R041-AC001",
        "BRD-WS-14-R041-AC004",
        "BRD-WS-14-R041-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R041-O001",
      "obligation_text": "Reference Data là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R041-AC002",
        "BRD-WS-14-R041-AC004",
        "BRD-WS-14-R041-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R041-O002",
      "obligation_text": "Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R041-AC003",
        "BRD-WS-14-R041-AC004",
        "BRD-WS-14-R041-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R041-O003",
      "obligation_text": "Reference Data hỗ trợ: Alias"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform. Reference Data hỗ trợ: Alias.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R041",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Data",
    "source_context_sha256": "8159a2e679167d6d72d40b009066fd1f2181eed5a5122ec29675371dcf1ef8de",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "a2a7ff1d3fce44cbe903085a6bc2772dc87950deb4c615d819ab6604fe70c41f",
    "source_fingerprint_before_c3": "a2a7ff1d3fce44cbe903085a6bc2772dc87950deb4c615d819ab6604fe70c41f",
    "source_lines": "L10377-L10489",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R041"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-003"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R041",
  "title": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R042 — Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R042",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "6ca9c3cd20eea54f471630c632b84b7bf38b5ea8e8c4c4e3fca333a052d13ce6"
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
        "BRD-WS-14-R042-AC001",
        "BRD-WS-14-R042-AC004",
        "BRD-WS-14-R042-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R042-O001",
      "obligation_text": "Reference Data là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R042-AC002",
        "BRD-WS-14-R042-AC004",
        "BRD-WS-14-R042-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R042-O002",
      "obligation_text": "Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R042-AC003",
        "BRD-WS-14-R042-AC004",
        "BRD-WS-14-R042-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R042-O003",
      "obligation_text": "Reference Data hỗ trợ: Effective Date"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform. Reference Data hỗ trợ: Effective Date.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R042",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Reference Data",
    "source_context_sha256": "8159a2e679167d6d72d40b009066fd1f2181eed5a5122ec29675371dcf1ef8de",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "6ca9c3cd20eea54f471630c632b84b7bf38b5ea8e8c4c4e3fca333a052d13ce6",
    "source_fingerprint_before_c3": "6ca9c3cd20eea54f471630c632b84b7bf38b5ea8e8c4c4e3fca333a052d13ce6",
    "source_lines": "L10491-L10603",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R042"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-003"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R042",
  "title": "Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platfor…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R043 — Dictionary là Business Object độc lập

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-010",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R043",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "011b201a80db022d1bdabf75f1e203b6c847a4d43355ebd7c9910255c8f913f3"
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
        "BRD-WS-14-R043-AC001",
        "BRD-WS-14-R043-AC002",
        "BRD-WS-14-R043-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R043-O001",
      "obligation_text": "Dictionary là Business Object độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dictionary là Business Object độc lập.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-004",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R043",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-004",
    "source_context_sha256": "6acc8c8e8f8c79c34e8e3d5a62ad5e90891a24c77aa4a41c451f45395691f8c5",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "011b201a80db022d1bdabf75f1e203b6c847a4d43355ebd7c9910255c8f913f3",
    "source_fingerprint_before_c3": "011b201a80db022d1bdabf75f1e203b6c847a4d43355ebd7c9910255c8f913f3",
    "source_lines": "L10605-L10699",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R043"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-004"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-004"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R043",
  "title": "Dictionary là Business Object độc lập",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R044 — Dictionary không thay thế Reference Data

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-010",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R044",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "26fbd71a284bdfc877fe6d329589472015a962e871342053c6f16179542a3f27"
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
        "BRD-WS-14-R044-AC001",
        "BRD-WS-14-R044-AC002",
        "BRD-WS-14-R044-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R044-O001",
      "obligation_text": "Dictionary không thay thế Reference Data"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dictionary không thay thế Reference Data.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-004",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R044",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-004",
    "source_context_sha256": "6acc8c8e8f8c79c34e8e3d5a62ad5e90891a24c77aa4a41c451f45395691f8c5",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "26fbd71a284bdfc877fe6d329589472015a962e871342053c6f16179542a3f27",
    "source_fingerprint_before_c3": "26fbd71a284bdfc877fe6d329589472015a962e871342053c6f16179542a3f27",
    "source_lines": "L10701-L10795",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R044"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-004"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-004"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R044",
  "title": "Dictionary không thay thế Reference Data",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R045 — Dictionary quản lý Label, Enum, Caption và Translation

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-010",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R045",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "3ec9fb0b643a7a99b7942dad5f328e31a683633caba6e266981c0d1683d269bf"
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
        "BRD-WS-14-R045-AC001",
        "BRD-WS-14-R045-AC002",
        "BRD-WS-14-R045-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R045-O001",
      "obligation_text": "Dictionary quản lý Label, Enum, Caption và Translation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dictionary quản lý Label, Enum, Caption và Translation.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-004",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R045",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-004",
    "source_context_sha256": "6acc8c8e8f8c79c34e8e3d5a62ad5e90891a24c77aa4a41c451f45395691f8c5",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "3ec9fb0b643a7a99b7942dad5f328e31a683633caba6e266981c0d1683d269bf",
    "source_fingerprint_before_c3": "3ec9fb0b643a7a99b7942dad5f328e31a683633caba6e266981c0d1683d269bf",
    "source_lines": "L10797-L10891",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R045"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-004"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-004"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R045",
  "title": "Dictionary quản lý Label, Enum, Caption và Translation",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R046 — Business Rule là Business Object

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R046",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "df85881ad88cb5cd1b6ab1992e5020055a29a18d6672cc9905836b5b22965a55"
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
        "BRD-WS-14-R046-AC001",
        "BRD-WS-14-R046-AC002",
        "BRD-WS-14-R046-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R046-O001",
      "obligation_text": "Business Rule là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule là Business Object.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R046",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Business Rule Engine",
    "source_context_sha256": "86d3ad94506a400c239a818b3540c68c8fa7011a8692d42b51ff06ebc3155e51",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "df85881ad88cb5cd1b6ab1992e5020055a29a18d6672cc9905836b5b22965a55",
    "source_fingerprint_before_c3": "df85881ad88cb5cd1b6ab1992e5020055a29a18d6672cc9905836b5b22965a55",
    "source_lines": "L10893-L10985",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R046"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-006"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R046",
  "title": "Business Rule là Business Object",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R047 — Business Rule được cấu hình

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R047",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "412db3e92227a2fd8ab24061541cc4372e6738a58b1276129342fe149932d798"
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
        "BRD-WS-14-R047-AC001",
        "BRD-WS-14-R047-AC002",
        "BRD-WS-14-R047-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R047-O001",
      "obligation_text": "Business Rule được cấu hình"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Rule được cấu hình.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R047",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Business Rule Engine",
    "source_context_sha256": "86d3ad94506a400c239a818b3540c68c8fa7011a8692d42b51ff06ebc3155e51",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "412db3e92227a2fd8ab24061541cc4372e6738a58b1276129342fe149932d798",
    "source_fingerprint_before_c3": "412db3e92227a2fd8ab24061541cc4372e6738a58b1276129342fe149932d798",
    "source_lines": "L10987-L11079",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R047"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-006"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R047",
  "title": "Business Rule được cấu hình",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R048 — Không Hard-code

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R048",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "4a4f9fc70196c62582583bd1f5a465fcfd49191969988f4db3f00452e0acf501"
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
        "BRD-WS-14-R048-AC001",
        "BRD-WS-14-R048-AC002",
        "BRD-WS-14-R048-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R048-O001",
      "obligation_text": "Không Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không Hard-code.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R048",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Business Rule Engine",
    "source_context_sha256": "86d3ad94506a400c239a818b3540c68c8fa7011a8692d42b51ff06ebc3155e51",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "4a4f9fc70196c62582583bd1f5a465fcfd49191969988f4db3f00452e0acf501",
    "source_fingerprint_before_c3": "4a4f9fc70196c62582583bd1f5a465fcfd49191969988f4db3f00452e0acf501",
    "source_lines": "L11081-L11173",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R048"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-006"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R048",
  "title": "Không Hard-code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R049 — Feature Flag là Business Object. Feature Flag hỗ trợ: Global

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R049",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "45cc04401944ca621287aff04bbc735893c21de4c6bd3f179cbb2bed4df7c7a9"
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
        "BRD-WS-14-R049-AC001",
        "BRD-WS-14-R049-AC003",
        "BRD-WS-14-R049-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R049-O001",
      "obligation_text": "Feature Flag là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R049-AC002",
        "BRD-WS-14-R049-AC003",
        "BRD-WS-14-R049-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R049-O002",
      "obligation_text": "Feature Flag hỗ trợ: Global"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Feature Flag là Business Object. Feature Flag hỗ trợ: Global.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R049",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-010",
    "source_context_sha256": "36a85a92279eb52803fdc59156a6e359a91c89f4dce29f08327f34b94c7d92ef",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "45cc04401944ca621287aff04bbc735893c21de4c6bd3f179cbb2bed4df7c7a9",
    "source_fingerprint_before_c3": "45cc04401944ca621287aff04bbc735893c21de4c6bd3f179cbb2bed4df7c7a9",
    "source_lines": "L11175-L11279",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R049"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-010"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R049",
  "title": "Feature Flag là Business Object. Feature Flag hỗ trợ: Global",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R050 — Feature Flag là Business Object. Feature Flag hỗ trợ: Parent Organization

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R050",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "5a2a32a36743de0c9c8467231d42d3b1b990acb3f5c59416b1e73bed4974f2ad"
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
        "BRD-WS-14-R050-AC001",
        "BRD-WS-14-R050-AC003",
        "BRD-WS-14-R050-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R050-O001",
      "obligation_text": "Feature Flag là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R050-AC002",
        "BRD-WS-14-R050-AC003",
        "BRD-WS-14-R050-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R050-O002",
      "obligation_text": "Feature Flag hỗ trợ: Parent Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Feature Flag là Business Object. Feature Flag hỗ trợ: Parent Organization.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R050",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-010",
    "source_context_sha256": "36a85a92279eb52803fdc59156a6e359a91c89f4dce29f08327f34b94c7d92ef",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "5a2a32a36743de0c9c8467231d42d3b1b990acb3f5c59416b1e73bed4974f2ad",
    "source_fingerprint_before_c3": "5a2a32a36743de0c9c8467231d42d3b1b990acb3f5c59416b1e73bed4974f2ad",
    "source_lines": "L11281-L11385",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R050"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-010"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R050",
  "title": "Feature Flag là Business Object. Feature Flag hỗ trợ: Parent Organization",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R051 — Feature Flag là Business Object. Feature Flag hỗ trợ: Organization

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R051",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "45e219287a2efd3d4aa4237a215bc84200715c66ef0d2f570d270f9e1a5e773d"
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
        "BRD-WS-14-R051-AC001",
        "BRD-WS-14-R051-AC003",
        "BRD-WS-14-R051-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R051-O001",
      "obligation_text": "Feature Flag là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R051-AC002",
        "BRD-WS-14-R051-AC003",
        "BRD-WS-14-R051-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R051-O002",
      "obligation_text": "Feature Flag hỗ trợ: Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Feature Flag là Business Object. Feature Flag hỗ trợ: Organization.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R051",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-010",
    "source_context_sha256": "36a85a92279eb52803fdc59156a6e359a91c89f4dce29f08327f34b94c7d92ef",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "45e219287a2efd3d4aa4237a215bc84200715c66ef0d2f570d270f9e1a5e773d",
    "source_fingerprint_before_c3": "45e219287a2efd3d4aa4237a215bc84200715c66ef0d2f570d270f9e1a5e773d",
    "source_lines": "L11387-L11491",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R051"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-010"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R051",
  "title": "Feature Flag là Business Object. Feature Flag hỗ trợ: Organization",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R052 — Feature Flag là Business Object. Feature Flag hỗ trợ: Storefront

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R052",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "9eb46ac44be51302e591c9b8fb818ccf64c447173aa10d3cf175852111a5a655"
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
        "BRD-WS-14-R052-AC001",
        "BRD-WS-14-R052-AC003",
        "BRD-WS-14-R052-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R052-O001",
      "obligation_text": "Feature Flag là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R052-AC002",
        "BRD-WS-14-R052-AC003",
        "BRD-WS-14-R052-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R052-O002",
      "obligation_text": "Feature Flag hỗ trợ: Storefront"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Feature Flag là Business Object. Feature Flag hỗ trợ: Storefront.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R052",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-010",
    "source_context_sha256": "36a85a92279eb52803fdc59156a6e359a91c89f4dce29f08327f34b94c7d92ef",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "9eb46ac44be51302e591c9b8fb818ccf64c447173aa10d3cf175852111a5a655",
    "source_fingerprint_before_c3": "9eb46ac44be51302e591c9b8fb818ccf64c447173aa10d3cf175852111a5a655",
    "source_lines": "L11493-L11597",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R052"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-010"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R052",
  "title": "Feature Flag là Business Object. Feature Flag hỗ trợ: Storefront",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-14-R053 — Feature Flag là Business Object. Feature Flag hỗ trợ: User

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-14-R053",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "e3854c7422ce4faf1c670a4f3cc2c96b6b7f1a08e20da0df6445cea13f5337bc"
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
        "BRD-WS-14-R053-AC001",
        "BRD-WS-14-R053-AC003",
        "BRD-WS-14-R053-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R053-O001",
      "obligation_text": "Feature Flag là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-14-R053-AC002",
        "BRD-WS-14-R053-AC003",
        "BRD-WS-14-R053-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-14-R053-O002",
      "obligation_text": "Feature Flag hỗ trợ: User"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Feature Flag là Business Object. Feature Flag hỗ trợ: User.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-14-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-14-R053",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-14-010",
    "source_context_sha256": "36a85a92279eb52803fdc59156a6e359a91c89f4dce29f08327f34b94c7d92ef",
    "source_document": "docs/BRD/BRD-WS-14.md",
    "source_fingerprint": "e3854c7422ce4faf1c670a4f3cc2c96b6b7f1a08e20da0df6445cea13f5337bc",
    "source_fingerprint_before_c3": "e3854c7422ce4faf1c670a4f3cc2c96b6b7f1a08e20da0df6445cea13f5337bc",
    "source_lines": "L11599-L11703",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-14-R053"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-14-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-14-010"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-14-R053",
  "title": "Feature Flag là Business Object. Feature Flag hỗ trợ: User",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-14-001 — Configuration over Customization là nguyên tắc cốt lõi của Platform

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
      "requirement_id": "EP-14-001",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "a074517e25f52051d82e769d6c1c4f8deea1e378ee6da4679922862931dd43e1"
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
        "EP-14-001-AC001",
        "EP-14-001-AC002",
        "EP-14-001-AC003"
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
    "source_fingerprint": "a074517e25f52051d82e769d6c1c4f8deea1e378ee6da4679922862931dd43e1",
    "source_lines": "L11705-L11780",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-14-001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-14-002",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "a3a9094f0b7f421af818a134bb5a59af23a7b5d5d6f13a1a3f575efc07ccbf19"
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
        "EP-14-002-AC001",
        "EP-14-002-AC002",
        "EP-14-002-AC003"
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
    "source_fingerprint": "a3a9094f0b7f421af818a134bb5a59af23a7b5d5d6f13a1a3f575efc07ccbf19",
    "source_lines": "L11782-L11857",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-14-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-14-003",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "7d8746c417d5e7650062ed84778a453588b7fa755111e7392b07fb157511941e"
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
        "EP-14-003-AC001",
        "EP-14-003-AC002",
        "EP-14-003-AC003"
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
    "source_fingerprint": "7d8746c417d5e7650062ed84778a453588b7fa755111e7392b07fb157511941e",
    "source_lines": "L11859-L11934",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-14-003"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "Platform invariants may be code-enforced when versioned and auditable; variable business rules remain configured"
    ],
    "concrete_bindings": [
      {
        "configuration_key": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
            "source_type": "SOURCE_LITERAL",
            "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
          },
          "identifier": "EP-14-004.CONFIGURATION_KEY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
            "source_lines": "L1210-L1213",
            "source_section": "32. Enterprise Design Principles > EP-14-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CONFIGURATION_KEY",
            "resolver_id": "RESOLVE.EP-14-004.EP-14-004.CONFIGURATION_KEY",
            "version": "1.0.0"
          },
          "semantic_type": "CONFIGURATION_KEY"
        },
        "configuration_sources": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
            "source_type": "SOURCE_LITERAL",
            "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
          },
          "identifier": "EP-14-004.CONFIGURATION_SOURCES",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
            "source_lines": "L1210-L1213",
            "source_section": "32. Enterprise Design Principles > EP-14-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
            "resolver_id": "RESOLVE.EP-14-004.EP-14-004.CONFIGURATION_SOURCES",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
        },
        "expected_value": {
          "authoritative_source": {
            "allowed_identifiers": [
              "EP-14-004.CANONICAL.CONFIGURATION.VALUE"
            ],
            "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
            "source_type": "SOURCE_LITERAL",
            "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
          },
          "identifier": "EP-14-004.CANONICAL.CONFIGURATION.VALUE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
            "source_lines": "L1210-L1213",
            "source_section": "32. Enterprise Design Principles > EP-14-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "RESOLVE.EP-14-004.EP-14-004.CANONICAL.CONFIGURATION.VALUE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "resolved_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
            "source_type": "SOURCE_LITERAL",
            "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
          },
          "identifier": "EP-14-004.RESOLVED_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
            "source_lines": "L1210-L1213",
            "source_section": "32. Enterprise Design Principles > EP-14-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CONFIGURATION_SOURCE_ID",
            "resolver_id": "RESOLVE.EP-14-004.EP-14-004.RESOLVED_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "CONFIGURATION_SOURCE_ID"
        },
        "source_versions": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                "source_type": "SOURCE_LITERAL",
                "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
              },
              "identifier": "EP-14-004.SOURCE_VERSIONS.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                "source_lines": "L1210-L1213",
                "source_section": "32. Enterprise Design Principles > EP-14-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.EP-14-004.EP-14-004.SOURCE_VERSIONS.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          ],
          "origin": {
            "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
            "source_lines": "L1210-L1213",
            "source_section": "32. Enterprise Design Principles > EP-14-004"
          },
          "semantic_type": "SET_OF<POLICY_VERSION>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.EP-14-004",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Rule behavior is hard-coded or changed outside governed configuration"
    ],
    "operator_composition": [
      "CONFIGURATION_RESOLVES"
    ],
    "positive_oracle": [
      "Business Rule changes through configuration"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
      "source_lines": "L1210-L1213",
      "source_section": "32. Enterprise Design Principles > EP-14-004"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
          "source_type": "SOURCE_LITERAL",
          "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
        },
        "identifier": "EP-14-004.EP-14-004.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "EP-14-004.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-14.md",
          "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
          "source_lines": "L1210-L1213",
          "source_section": "32. Enterprise Design Principles > EP-14-004"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.EP-14-004.EP-14-004.EP-14-004.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "EP-14-004.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.RULE_ID",
        "FIELD.CONFIGURATION_VERSION",
        "FIELD.EFFECTIVE_RULE",
        "FIELD.CODE_DIFF",
        "FIELD.AUTHORIZATION",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "EP-14-004.EVIDENCE.PRODUCER",
      "required_collection_origin": "EP-14-004.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.RULE_ID",
        "FIELD.CONFIGURATION_VERSION",
        "FIELD.EFFECTIVE_RULE",
        "FIELD.CODE_DIFF",
        "FIELD.AUTHORIZATION",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "EP-14-004.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "EP-14-004.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "EP-14-004.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "EP-14-004-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES",
          "evaluator_consumed_bindings": [
            "configuration_key",
            "configuration_sources",
            "expected_value",
            "resolved_source",
            "source_versions"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
              "source_type": "SOURCE_LITERAL",
              "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
            },
            "identifier": "EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-14.md",
              "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
              "source_lines": "L1210-L1213",
              "source_section": "32. Enterprise Design Principles > EP-14-004"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.EP-14-004.EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
              "source_type": "SOURCE_LITERAL",
              "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
            },
            "identifier": "EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-14.md",
              "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
              "source_lines": "L1210-L1213",
              "source_section": "32. Enterprise Design Principles > EP-14-004"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "RESOLVE.EP-14-004.EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "configuration_key": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
                },
                "identifier": "EP-14-004.CONFIGURATION_KEY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                  "source_lines": "L1210-L1213",
                  "source_section": "32. Enterprise Design Principles > EP-14-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_KEY",
                  "resolver_id": "RESOLVE.EP-14-004.EP-14-004.CONFIGURATION_KEY",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_KEY"
              },
              "configuration_sources": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
                },
                "identifier": "EP-14-004.CONFIGURATION_SOURCES",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                  "source_lines": "L1210-L1213",
                  "source_section": "32. Enterprise Design Principles > EP-14-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
                  "resolver_id": "RESOLVE.EP-14-004.EP-14-004.CONFIGURATION_SOURCES",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
              },
              "expected_value": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-14-004.CANONICAL.CONFIGURATION.VALUE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
                },
                "identifier": "EP-14-004.CANONICAL.CONFIGURATION.VALUE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                  "source_lines": "L1210-L1213",
                  "source_section": "32. Enterprise Design Principles > EP-14-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.EP-14-004.EP-14-004.CANONICAL.CONFIGURATION.VALUE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "resolved_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
                },
                "identifier": "EP-14-004.RESOLVED_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                  "source_lines": "L1210-L1213",
                  "source_section": "32. Enterprise Design Principles > EP-14-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_SOURCE_ID",
                  "resolver_id": "RESOLVE.EP-14-004.EP-14-004.RESOLVED_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_SOURCE_ID"
              },
              "source_versions": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                      "source_type": "SOURCE_LITERAL",
                      "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
                    },
                    "identifier": "EP-14-004.SOURCE_VERSIONS.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-14.md",
                      "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                      "source_lines": "L1210-L1213",
                      "source_section": "32. Enterprise Design Principles > EP-14-004"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "POLICY_VERSION",
                      "resolver_id": "RESOLVE.EP-14-004.EP-14-004.SOURCE_VERSIONS.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "POLICY_VERSION"
                  }
                ],
                "origin": {
                  "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                  "source_lines": "L1210-L1213",
                  "source_section": "32. Enterprise Design Principles > EP-14-004"
                },
                "semantic_type": "SET_OF<POLICY_VERSION>"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
                },
                "identifier": "EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                  "source_lines": "L1210-L1213",
                  "source_section": "32. Enterprise Design Principles > EP-14-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.EP-14-004.EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
                },
                "identifier": "EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-14.md",
                  "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                  "source_lines": "L1210-L1213",
                  "source_section": "32. Enterprise Design Principles > EP-14-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.EP-14-004.EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                "source_type": "SOURCE_LITERAL",
                "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
              },
              "identifier": "EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                "source_lines": "L1210-L1213",
                "source_section": "32. Enterprise Design Principles > EP-14-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.EP-14-004.EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "CONFIGURATION_RESOLVES"
          },
          "obligation_id": "EP-14-004-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
              "source_type": "SOURCE_LITERAL",
              "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
            },
            "identifier": "EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-14.md",
              "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
              "source_lines": "L1210-L1213",
              "source_section": "32. Enterprise Design Principles > EP-14-004"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "OBSERVE.EP-14-004.EP-14-004.EP-14-004.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "operator_id": "CONFIGURATION_RESOLVES",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "configuration_key": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                "source_type": "SOURCE_LITERAL",
                "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
              },
              "identifier": "EP-14-004.CONFIGURATION_KEY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                "source_lines": "L1210-L1213",
                "source_section": "32. Enterprise Design Principles > EP-14-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_KEY",
                "resolver_id": "RESOLVE.EP-14-004.EP-14-004.CONFIGURATION_KEY",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_KEY"
            },
            "configuration_sources": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                "source_type": "SOURCE_LITERAL",
                "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
              },
              "identifier": "EP-14-004.CONFIGURATION_SOURCES",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                "source_lines": "L1210-L1213",
                "source_section": "32. Enterprise Design Principles > EP-14-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
                "resolver_id": "RESOLVE.EP-14-004.EP-14-004.CONFIGURATION_SOURCES",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
            },
            "expected_value": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "EP-14-004.CANONICAL.CONFIGURATION.VALUE"
                ],
                "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                "source_type": "SOURCE_LITERAL",
                "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
              },
              "identifier": "EP-14-004.CANONICAL.CONFIGURATION.VALUE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                "source_lines": "L1210-L1213",
                "source_section": "32. Enterprise Design Principles > EP-14-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.EP-14-004.EP-14-004.CANONICAL.CONFIGURATION.VALUE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "resolved_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                "source_type": "SOURCE_LITERAL",
                "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
              },
              "identifier": "EP-14-004.RESOLVED_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                "source_lines": "L1210-L1213",
                "source_section": "32. Enterprise Design Principles > EP-14-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_SOURCE_ID",
                "resolver_id": "RESOLVE.EP-14-004.EP-14-004.RESOLVED_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_SOURCE_ID"
            },
            "source_versions": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
                    "source_type": "SOURCE_LITERAL",
                    "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
                  },
                  "identifier": "EP-14-004.SOURCE_VERSIONS.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-14.md",
                    "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                    "source_lines": "L1210-L1213",
                    "source_section": "32. Enterprise Design Principles > EP-14-004"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "POLICY_VERSION",
                    "resolver_id": "RESOLVE.EP-14-004.EP-14-004.SOURCE_VERSIONS.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "POLICY_VERSION"
                }
              ],
              "origin": {
                "origin_id": "EP-14-004.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-14.md",
                "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
                "source_lines": "L1210-L1213",
                "source_section": "32. Enterprise Design Principles > EP-14-004"
              },
              "semantic_type": "SET_OF<POLICY_VERSION>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Platform invariants may be code-enforced when versioned and auditable; variable business rules remain configured"
      ],
      "contract_ast_sha256": "06205de4c30cf1553600085d6fd83569e7d876910b834dc4e6b6271eacb63263",
      "contract_id": "P2C.C4.CONTRACT.EP-14-004",
      "criticality": "NORMAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-14.md#32. Enterprise Design Principles > EP-14-004",
            "source_type": "SOURCE_LITERAL",
            "version": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e"
          },
          "identifier": "EP-14-004.EP-14-004.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-14-004.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-14.md",
            "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
            "source_lines": "L1210-L1213",
            "source_section": "32. Enterprise Design Principles > EP-14-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.EP-14-004.EP-14-004.EP-14-004.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "EP-14-004.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.RULE_ID",
          "FIELD.CONFIGURATION_VERSION",
          "FIELD.EFFECTIVE_RULE",
          "FIELD.CODE_DIFF",
          "FIELD.AUTHORIZATION",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "EP-14-004.EVIDENCE.PRODUCER",
        "required_collection_origin": "EP-14-004.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.RULE_ID",
          "FIELD.CONFIGURATION_VERSION",
          "FIELD.EFFECTIVE_RULE",
          "FIELD.CODE_DIFF",
          "FIELD.AUTHORIZATION",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "EP-14-004.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "EP-14-004.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "EP-14-004.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-E7A57ECACE77AB6F03E4",
        "P2C-C4-FX-CFACF72D65D484420234",
        "P2C-C4-FX-AD109E968B6542704D59"
      ],
      "high_risk_audit_subset": false,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Rule behavior is hard-coded or changed outside governed configuration"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "EP-14-004-O001",
          "obligation_text": "Business Rule được cấu hình, không Hard-code"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "EP-14-004.O1.1.CONFIGURATION_RESOLVES"
          ],
          "coverage_count": 1,
          "obligation_id": "EP-14-004-O001"
        }
      ],
      "operator_composition": [
        "CONFIGURATION_RESOLVES"
      ],
      "positive_oracles": [
        "Business Rule changes through configuration"
      ],
      "preconditions": [
        "A versioned governed configuration and authorization exist"
      ],
      "prohibitions": [
        "Rule behavior is hard-coded or changed outside governed configuration"
      ],
      "requirement_id": "EP-14-004",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-14.md",
        "source_fingerprint": "09521da9ba8dc61dd18095b4df1e36a3b8b19f9c6cff69564fd079acc99e731e",
        "source_lines": "L1210-L1213",
        "source_section": "32. Enterprise Design Principles > EP-14-004"
      },
      "source_statement": "Business Rule được cấu hình, không Hard-code.",
      "surrounding_source_context": "## EP-14-004\n\nBusiness Rule được cấu hình, không Hard-code.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.EP-14-004",
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
        "EP-14-004-AC001",
        "EP-14-004-AC002",
        "EP-14-004-AC003"
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
    "source_fingerprint": "a9b30d9ac7f426110b72c53957d4c623a7fa7bfa1ac3155e74125b19d3972549",
    "source_lines": "L11936-L13035",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-14-004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-14-005",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "aac49b5abf2fea4592022507f6b77a7fa7cd81d7077105079f5c841f0921bb13"
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
        "EP-14-005-AC001",
        "EP-14-005-AC002",
        "EP-14-005-AC003"
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
    "source_fingerprint": "aac49b5abf2fea4592022507f6b77a7fa7cd81d7077105079f5c841f0921bb13",
    "source_lines": "L13037-L13112",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-14-005"
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
      "requirement_id": "EP-14-006",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "2e1798224de7a5e150e43d3450aad90eca4aacb95470705c5e04851a4bc67cfc"
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
        "EP-14-006-AC001",
        "EP-14-006-AC004",
        "EP-14-006-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-006-O001",
      "obligation_text": "Configuration luôn có: Version"
    },
    {
      "acceptance_criterion_references": [
        "EP-14-006-AC002",
        "EP-14-006-AC004",
        "EP-14-006-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-006-O002",
      "obligation_text": "Configuration luôn có: Approval"
    },
    {
      "acceptance_criterion_references": [
        "EP-14-006-AC003",
        "EP-14-006-AC004",
        "EP-14-006-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-14-006-O003",
      "obligation_text": "Configuration luôn có: Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-14-006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-14-006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-14-006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-14-006-AC004"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-14-006-AC001",
        "EP-14-006-AC002",
        "EP-14-006-AC003"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-14-006 does not define a recovery obligation."
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
    "source_fingerprint": "2e1798224de7a5e150e43d3450aad90eca4aacb95470705c5e04851a4bc67cfc",
    "source_lines": "L13114-L13250",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-14-006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-14-007",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "31247a968b823b8c1a95aac6e09bc8012f67d64978a382e2c86dbdd2ac6e3c2b"
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
        "EP-14-007-AC001",
        "EP-14-007-AC002",
        "EP-14-007-AC003"
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
    "source_fingerprint": "31247a968b823b8c1a95aac6e09bc8012f67d64978a382e2c86dbdd2ac6e3c2b",
    "source_lines": "L13252-L13327",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-14-007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-14-008",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "029bd0444e7fe6562ccda66ea94868dd3a8b7e9ab65328c7543e3d1200e6c5fc"
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
        "EP-14-008-AC001",
        "EP-14-008-AC002",
        "EP-14-008-AC003"
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
    "source_fingerprint": "029bd0444e7fe6562ccda66ea94868dd3a8b7e9ab65328c7543e3d1200e6c5fc",
    "source_lines": "L13329-L13404",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-14-008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-14-009",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "ef70426b0a42de229e42ac83450239cd7fec5f34a1259163f3ee6c36736f3124"
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
        "EP-14-009-AC001",
        "EP-14-009-AC002",
        "EP-14-009-AC003"
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
    "source_fingerprint": "ef70426b0a42de229e42ac83450239cd7fec5f34a1259163f3ee6c36736f3124",
    "source_lines": "L13406-L13481",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-14-009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-019",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-14-010",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "source_fingerprint": "4e581c469de766b7f63f64fd7b988b36728aaf6ebaae097a22881e29677dba24"
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
        "EP-14-010-AC001",
        "EP-14-010-AC002",
        "EP-14-010-AC003"
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
    "source_fingerprint": "4e581c469de766b7f63f64fd7b988b36728aaf6ebaae097a22881e29677dba24",
    "source_lines": "L13483-L13562",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-14-010"
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
