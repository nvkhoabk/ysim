---
document_code: "BRD-WS-13"
document_id: "BRD-WS-13"
title: "Reporting, Analytics & Operational Intelligence"
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

# BRD Workshop 13

# Reporting, Analytics & Operational Intelligence

---

# 1. Workshop Objective

Workshop này xác định toàn bộ năng lực Reporting, Analytics và Operational Intelligence của nền tảng YSim.

Bao gồm:

- Dashboard
- Dashboard Widget
- Reporting
- KPI
- Metrics
- Operational Intelligence
- Business Intelligence
- Report Builder
- Report Schedule
- Data Export
- Saved View
- Alert Management

Workshop này không bao gồm:

- AI Analytics
- Machine Learning
- Predictive Analytics

(Các nội dung trên được giữ chỗ cho các phiên bản sau.)

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| Dashboard | Master |
| Dashboard Widget | Master |
| Report | Master |
| Report Template | Master |
| Report Schedule | Master |
| Report Execution | Transaction |
| KPI | Master |
| Metric | Master |
| Alert Rule | Master |
| Insight | Transaction |
| Saved View | Master |
| Export Job | Transaction |

---

# 3. Dashboard Model

Dashboard là Business Object.

Dashboard được hỗ trợ cho:

- Global Dashboard
- Organization Dashboard
- Department Dashboard
- User Dashboard
- Customer Dashboard

Customer Dashboard bao gồm:

- Order Statistics
- Trạng thái eSIM đang sử dụng (nếu có)
- Promotion theo khu vực
- Widget tìm kiếm nhanh eSIM
- Danh sách Order gần đây
- Notification
- Customer Portal Shortcut

Dashboard và Widget phải hỗ trợ Drill-down tới module hoặc Business Object tương ứng.

---

# 4. Dashboard Widget

Dashboard sử dụng Widget.

Widget là Platform Capability độc lập.

Dashboard hỗ trợ:

- Drag & Drop
- Resize
- Reorder
- Multiple Workspace
- Saved Dashboard Layout

Widget có thể tái sử dụng tại:

- Dashboard
- Workspace
- Admin Portal
- Organization Portal
- Customer Portal

Widget Library phải cho phép Organization lựa chọn từng Widget được hiển thị hoặc bị ẩn trên Dashboard, Workspace, Admin Portal, Organization Portal và Customer Portal khi surface đó áp dụng.

---

# 5. KPI

Version 2 hỗ trợ các nhóm KPI:

- Business KPI
- Operational KPI
- Financial KPI
- Customer KPI
- System KPI

Kiến trúc hỗ trợ mở rộng thêm các nhóm KPI mới.

KPI Definition được cấu hình.

Không Hard-code.

---

# 6. Report Model

Report là Business Object độc lập.

Bao gồm:

- System Report
- Business Report
- Financial Report
- Operational Report
- Customer Report
- KPI Report
- Analytics Report

System Report chỉ dành cho YSim Internal.

Business Report hỗ trợ mô hình kế thừa:

```text
YSim

↓

Parent Organization

↓

Organization Override
```

Organization có thể:

- Enable
- Disable
- Override
- Clone

Report Template theo Permission.

---

# 7. Saved View

Saved View là Business Object.

User có thể lưu:

- Filter
- Column
- Sort
- Group
- Dashboard Layout
- Search Condition

Saved View thuộc User.

Saved View có thể sử dụng lại trên Dashboard hoặc Report.

---

# 8. Report Schedule

Report hỗ trợ:

- Manual
- Schedule
- Event Trigger
- Auto Generate
- Auto Delivery

Ví dụ:

- Settlement Report
- Commission Report
- Financial Statement
- Debt Reminder

Recipient có thể là:

- User
- Organization
- Email
- Personal Inbox
- API Endpoint

---

# 9. Report Delivery

Report hỗ trợ:

- Download
- Email
- Portal
- Personal Inbox
- API

Report có thể tự động gửi tới Recipient theo Schedule hoặc Event Trigger.

---

# 10. Drill-down

Dashboard

↓

Widget

↓

Report

↓

Transaction

↓

Business Object

Tất cả Dashboard đều hỗ trợ Drill-down.

Drill-down phải tôn trọng Permission và Data Scope của User.

------

# 11. KPI Scope

KPI có thể áp dụng theo:

- Platform
- Organization
- Department
- User
- Storefront
- Campaign
- Product

Kiến trúc mở để bổ sung thêm các KPI Scope mới trong các phiên bản sau.

---

# 12. Metric

Metric là Business Object.

Metric là đơn vị đo lường cơ bản dùng để xây dựng KPI, Dashboard và Report.

Ví dụ:

- Revenue
- Gross Revenue
- Net Revenue
- Orders
- Sales Orders
- Purchase Orders
- Payments
- Refunds
- Conversion Rate
- Fulfillment Success Rate
- Supplier Health Score
- Settlement Accuracy
- Customer Satisfaction
- Ticket Resolution Time
- Inventory Turnover
- Average Order Value
- Customer Lifetime Value
- Customer Acquisition Cost

Metric có thể được sử dụng trong:

- Dashboard
- KPI
- Alert Rule
- Report
- Analytics
- Business Intelligence

---

# 13. Alert Rule

Alert Rule là Business Object.

Alert Rule được cấu hình theo điều kiện.

Ví dụ:

- Inventory thấp
- Supplier API lỗi
- Payment Failure
- Settlement Failure
- Promotion hết hạn
- Revenue giảm bất thường
- KPI vượt ngưỡng
- Ticket SLA quá hạn
- Wallet Balance thấp

Alert Rule có thể Trigger:

- Notification
- Workflow
- Business Action

Ví dụ:

- Block User
- Block Organization
- Block Transaction
- Escalation
- Auto Ticket
- Auto Notification
- Auto Report

Alert Rule hỗ trợ:

- Condition
- Threshold
- Schedule
- Recipient
- Escalation

Không Hard-code.

---

# 14. Operational Intelligence

Operational Dashboard có thể hoạt động theo:

- Real-time
- Near Real-time

Việc lựa chọn phụ thuộc:

- Loại Dashboard
- Độ quan trọng của dữ liệu
- Khối lượng tính toán
- Performance của hệ thống
- Công nghệ triển khai

Không bắt buộc toàn bộ Dashboard phải Real-time.

---

# 15. Export

Report và Dashboard hỗ trợ Export.

Version 2 hỗ trợ:

- Excel
- CSV
- PDF
- API
- Google Sheets

Kiến trúc mở để bổ sung thêm Export Target.

Export có thể:

- Manual
- Scheduled
- Event Trigger

---

# 16. Business Intelligence

Version 2 hỗ trợ:

- Dashboard
- Reporting
- Analytics
- Drill-down
- OLAP

Chưa triển khai:

- Machine Learning
- Predictive Analytics
- AI Insight

Các Capability trên được giữ chỗ cho các phiên bản sau.

---

# 17. Report Permission

Report Permission được xác định theo nhiều yếu tố.

Bao gồm:

- Organization
- Role
- Permission
- Data Scope
- Support Policy

Report có thể:

- Mask Data
- Hide Column
- Hide Metric
- Hide Widget

Permission được kế thừa theo Organization Hierarchy.

---

# 18. Multi Currency Reporting

Report mặc định sử dụng Currency chuẩn của Report.

Dashboard hiển thị theo:

- Localization
- Currency Preference
- Measurement Preference

Nếu Report sử dụng Currency khác thì phải hiển thị rõ:

- Currency
- Exchange Rate
- Conversion Rule
- Exchange Time

Dashboard luôn chuyển đổi đơn vị hiển thị theo cấu hình Localization của User.

---

# 19. Reporting Snapshot

Report luôn đọc dữ liệu từ Snapshot.

Không đọc trực tiếp dữ liệu Transaction đang thay đổi.

Điều này đảm bảo:

- Audit
- Traceability
- Financial Consistency
- Performance
- Historical Reporting

Snapshot được tạo bởi các Business Event tương ứng.

---

# 20. Analytics

Version 2 hỗ trợ:

- Sales Funnel
- Conversion Analytics
- Campaign Analytics
- Customer Journey
- Traffic Source
- Product Analytics
- Revenue Analytics
- Customer Behavior
- Fulfillment Analytics
- Financial Analytics
- Operational Analytics

Analytics phục vụ:

- Dashboard
- Report
- Operational Intelligence
- Business Intelligence

---

# 21. Customer Analytics

Customer Analytics được xây dựng theo Relationship Model.

Analytics được tổng hợp theo:

- Customer
- Customer Group
- Organization
- Relationship
- Storefront
- Campaign
- Product
- Country
- Region

Customer Analytics hỗ trợ:

- Purchase History
- Product Preference
- Customer Value
- Repeat Purchase
- Promotion Response
- Support History
- Customer Satisfaction
- Customer Lifecycle

Customer Analytics không được chia sẻ giữa các Organization.

Tuân thủ Relationship Policy và Data Permission.

---

# 22. Supplier Analytics

Supplier không có Dashboard riêng.

Supplier không sử dụng Portal của YSim.

Supplier Analytics chỉ dành cho YSim Internal.

Bao gồm:

- Supplier Revenue
- Supplier Cost
- Supplier Health
- Supplier Availability
- Supplier API Performance
- Procurement Volume
- Procurement Cost
- Procurement Success Rate
- Fulfillment Success Rate
- Supplier SLA

Supplier Analytics phục vụ:

- Procurement
- Allocation Engine
- Commercial
- Settlement
- Business Intelligence

---

# 23. Benchmark

Benchmark hỗ trợ so sánh KPI và Metric.

Organization chỉ được xem Benchmark của chính Organization đó.

Không được phép xem:

- Revenue của Organization khác
- KPI của Organization khác
- Customer của Organization khác

Benchmark được sử dụng để:

- Theo dõi xu hướng
- Đo lường hiệu quả
- Đánh giá tăng trưởng

Kiến trúc mở để hỗ trợ Industry Benchmark trong các phiên bản sau.

---

# 24. Report Builder

Version 2 hỗ trợ Custom Report Builder.

Report Builder hỗ trợ:

- Data Source
- Dataset
- Column Selection
- Filter
- Group
- Sort
- Formula
- Aggregate
- Visualization
- Export

Report Builder hỗ trợ lưu thành:

- Report Template
- Personal Report
- Organization Report

Permission được kiểm soát theo Report Permission.

---

# 25. Widget Library

Widget Library là Platform Capability.

Widget được quản lý độc lập.

Version 2 hỗ trợ các Widget chuẩn:

- KPI Widget
- Revenue Widget
- Order Widget
- Payment Widget
- Inventory Widget
- Fulfillment Widget
- Settlement Widget
- Supplier Widget
- Customer Widget
- Promotion Widget
- Campaign Widget
- Ticket Widget
- Notification Widget
- Dashboard Shortcut Widget

Widget có thể:

- Enable
- Disable
- Override Configuration
- Configure Parameter

Organization có thể lựa chọn Widget cần hiển thị.

---

# 26. Operational Insight

Insight là Business Object.

Insight được sinh ra từ:

- Rule Engine
- KPI Exception
- Threshold
- Analytics

Insight hỗ trợ:

- Business Recommendation
- Operational Recommendation
- Financial Recommendation
- Supplier Recommendation
- Customer Recommendation

Ví dụ:

- Supplier Health giảm
- Allocation Cost tăng
- Promotion hiệu quả thấp
- Fulfillment Failure tăng
- Ticket SLA vượt ngưỡng

Version 2 chưa sử dụng AI.

Kiến trúc giữ chỗ cho AI Insight ở phiên bản sau.

---

# 27. Report as Configuration

Report không được Hard-code.

Report được định nghĩa bởi:

- Data Source
- Dataset
- Column
- Formula
- Filter
- Permission
- Visualization
- Export
- Schedule

Report hỗ trợ:

Master Report Template

↓

Parent Organization

↓

Organization Override

Organization có thể:

- Enable
- Disable
- Override
- Clone

Report được quản lý như một Business Configuration.

---

# 28. Widget as Capability

Widget là Platform Capability.

Widget không thuộc Dashboard.

Một Widget có thể được sử dụng tại:

- Dashboard
- Workspace
- Admin Portal
- Organization Portal
- Customer Portal
- Landing Page (phiên bản sau)
- Mobile App (phiên bản sau)

Widget chỉ là thành phần hiển thị.

Business Logic thuộc Business Domain tương ứng.

Widget hỗ trợ:

- Reuse
- Configuration
- Permission
- Localization
- Theme
- Responsive Layout

Điều này giúp giảm trùng lặp giao diện và tăng khả năng tái sử dụng trên toàn bộ Platform.

------

# 29. Business Decisions (Locked)

## BD-13-001

Dashboard hỗ trợ nhiều cấp:

- Platform
- Organization
- Department
- User
- Customer

---

## BD-13-002

Dashboard Widget hỗ trợ:

- Drag & Drop
- Resize
- Reorder
- Multiple Workspace
- Saved Layout

---

## BD-13-003

KPI Definition được cấu hình.

Kiến trúc hỗ trợ mở rộng thêm các nhóm KPI và tiêu chuẩn đo lường.

---

## BD-13-004

Report là Business Object độc lập.

System Report chỉ dành cho YSim Internal.

Business Report hỗ trợ kế thừa:

YSim

↓

Parent Organization

↓

Organization Override

---

## BD-13-005

Saved View là Business Object.

Saved View thuộc User.

---

## BD-13-006

Report hỗ trợ:

- Manual
- Schedule
- Event Trigger
- Auto Generate
- Auto Delivery

---

## BD-13-007

Report hỗ trợ:

- Download
- Email
- Portal
- Personal Inbox
- API

---

## BD-13-008

Dashboard hỗ trợ Drill-down tới Business Object.

---

## BD-13-009

Metric là Business Object.

Metric là đơn vị đo lường chuẩn để xây dựng Dashboard, KPI và Report.

---

## BD-13-010

Alert Rule là Business Object.

Alert Rule có thể Trigger:

- Notification
- Workflow
- Business Action

Ví dụ:

- Block User
- Block Organization
- Block IP
- Block Transaction
- Escalation
- Auto Ticket

---

## BD-13-011

Operational Dashboard có thể:

- Real-time
- Near Real-time

Tùy theo yêu cầu nghiệp vụ và khả năng triển khai.

---

## BD-13-012

Version 2 hỗ trợ Business Intelligence theo mô hình OLAP.

Chưa triển khai:

- AI Analytics
- Machine Learning
- Predictive Analytics

---

## BD-13-013

Report Permission được xác định theo:

- Organization
- Role
- Permission
- Data Scope
- Support Policy

Có thể Mask dữ liệu theo Permission.

---

## BD-13-014

Dashboard hiển thị dữ liệu theo:

- Localization
- Currency Preference
- Measurement Preference

Report mặc định sử dụng Currency chuẩn của Report.

---

## BD-13-015

Report luôn đọc dữ liệu từ Snapshot.

Không đọc trực tiếp Transaction đang thay đổi.

---

## BD-13-016

Supplier Analytics chỉ dành cho YSim Internal.

Supplier không có Dashboard riêng.

---

## BD-13-017

Organization chỉ được Benchmark dữ liệu của chính Organization đó.

Không được phép xem dữ liệu của Organization khác.

---

## BD-13-018

Version 2 hỗ trợ Custom Report Builder.

Report được cấu hình thay vì Hard-code.

---

## BD-13-019

Widget Library là Platform Capability.

Widget được tái sử dụng trên:

- Dashboard
- Workspace
- Admin Portal
- Organization Portal
- Customer Portal

---

## BD-13-020

Insight là Business Object.

Insight được sinh từ Rule Engine và Analytics.

Version 2 chưa sử dụng AI.

---

# 30. Enterprise Design Principles

## EP-13-001

Dashboard là cửa ngõ truy cập nhanh tới Business Object.

Mọi Widget đều hỗ trợ Drill-down tới dữ liệu chi tiết theo Permission.

---

## EP-13-002

Reporting luôn sử dụng Snapshot.

Snapshot là nguồn dữ liệu chuẩn cho:

- Dashboard
- KPI
- Report
- Analytics
- Business Intelligence

---

## EP-13-003

Widget là Platform Capability.

Widget không thuộc Dashboard.

Một Widget có thể tái sử dụng trên nhiều Portal và Workspace.

---

## EP-13-004

Analytics phục vụ Decision Making.

Dashboard không chỉ hiển thị dữ liệu mà còn hỗ trợ phát hiện bất thường và đề xuất hành động.

---

## EP-13-005

Alert Rule được cấu hình hoàn toàn.

Alert có thể Trigger Notification, Workflow hoặc Business Action.

Không Hard-code.

---

## EP-13-006

Report, Dashboard và Widget đều được quản lý theo mô hình Configuration.

Organization có thể Enable, Disable hoặc Override theo Permission.

---

## EP-13-007

Localization được áp dụng xuyên suốt:

- Dashboard
- Report
- Widget
- Analytics

Bao gồm:

- Currency
- Language
- Measurement
- Temperature
- Date Time Format

---

## EP-13-008

Operational Intelligence và Business Intelligence phải phục vụ trực tiếp cho việc vận hành Platform và hỗ trợ ra quyết định.

---

# 31. Business Capabilities Covered

Workshop này bao gồm các Business Capability:

- Dashboard Management
- Workspace Management
- Widget Library
- Reporting
- Report Builder
- Report Scheduling
- Report Delivery
- KPI Management
- Metric Management
- Operational Intelligence
- Business Intelligence
- Analytics
- Drill-down
- Alert Management
- Saved View Management
- Export Management
- Insight Management

---

# 32. Traceability

Workshop này kế thừa các quyết định nghiệp vụ từ:

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

---

# 33. Impacts to Other Domains

Workshop này ảnh hưởng trực tiếp tới:

- Product Intelligence
- Commercial
- Order
- Payment
- Inventory
- Fulfillment
- Financial
- Settlement
- Customer Success
- Communication
- Platform Configuration
- Security
- Audit
- Monitoring

Các Domain trên có thể Publish Business Event để Dashboard, KPI, Analytics và Reporting sử dụng.

---

# 34. Workshop Status

Status:

**FROZEN**

Toàn bộ quyết định của Workshop này được xem là Architecture Baseline cho:

- Dashboard
- Reporting
- Analytics
- Business Intelligence
- KPI
- Operational Intelligence

---

# 35. Next Workshop

**BRD-WS-14**

**Platform Configuration, Reference Data & Business Rules**

Workshop tiếp theo sẽ xác định toàn bộ Platform Foundation phục vụ khả năng cấu hình và mở rộng của YSim, bao gồm:

- Configuration Management
- Reference Data Management
- Lookup Management
- Dictionary Management
- Business Rule Engine
- Feature Flag
- Parameter Management
- Workflow Configuration
- Capability Configuration
- System Settings
- Organization Settings
- Platform Metadata

Đây sẽ là nền tảng để toàn bộ các Business Domain của YSim hoạt động theo mô hình **Configuration over Customization**, giảm Hard-code và tăng khả năng mở rộng của nền tảng.

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-001 — Dashboard hỗ trợ nhiều cấp: - Platform - Organization - Department - User - Customer

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
      "requirement_id": "BD-13-001",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "6d40e59b92bf70320c43311c78b77a71e307b1caca785b85369b55c3a774acc1"
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
        "BD-13-001-AC001",
        "BD-13-001-AC006",
        "BD-13-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-001-O001",
      "obligation_text": "Dashboard hỗ trợ nhiều cấp: Platform"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-001-AC002",
        "BD-13-001-AC006",
        "BD-13-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-001-O002",
      "obligation_text": "Dashboard hỗ trợ nhiều cấp: Organization"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-001-AC003",
        "BD-13-001-AC006",
        "BD-13-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-001-O003",
      "obligation_text": "Dashboard hỗ trợ nhiều cấp: Department"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-001-AC004",
        "BD-13-001-AC006",
        "BD-13-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-001-O004",
      "obligation_text": "Dashboard hỗ trợ nhiều cấp: User"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-001-AC005",
        "BD-13-001-AC006",
        "BD-13-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-001-O005",
      "obligation_text": "Dashboard hỗ trợ nhiều cấp: Customer"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dashboard hỗ trợ nhiều cấp: - Platform - Organization - Department - User - Customer",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-001",
    "source_context_sha256": "a31d204f2d8ff66ae54a5c13db31d3593f9b4a77a387752f4122de45373c3e3e",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "6d40e59b92bf70320c43311c78b77a71e307b1caca785b85369b55c3a774acc1",
    "source_lines": "L1197-L1316",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-001"
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
  "stable_id": "BD-13-001",
  "title": "Dashboard hỗ trợ nhiều cấp: - Platform - Organization - Department - User - Customer",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-002 — Dashboard Widget hỗ trợ: - Drag & Drop - Resize - Reorder - Multiple Workspace - Saved Layout

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
      "requirement_id": "BD-13-002",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "6c224d55b6047fc46b7ff528aaa31525a355b165aa8d73b865ffb4b3377426b3"
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
        "BD-13-002-AC001",
        "BD-13-002-AC006",
        "BD-13-002-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-002-O001",
      "obligation_text": "Dashboard Widget hỗ trợ: Drag & Drop"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-002-AC002",
        "BD-13-002-AC006",
        "BD-13-002-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-002-O002",
      "obligation_text": "Dashboard Widget hỗ trợ: Resize"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-002-AC003",
        "BD-13-002-AC006",
        "BD-13-002-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-002-O003",
      "obligation_text": "Dashboard Widget hỗ trợ: Reorder"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-002-AC004",
        "BD-13-002-AC006",
        "BD-13-002-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-002-O004",
      "obligation_text": "Dashboard Widget hỗ trợ: Multiple Workspace"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-002-AC005",
        "BD-13-002-AC006",
        "BD-13-002-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-002-O005",
      "obligation_text": "Dashboard Widget hỗ trợ: Saved Layout"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dashboard Widget hỗ trợ: - Drag & Drop - Resize - Reorder - Multiple Workspace - Saved Layout",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-002",
    "source_context_sha256": "52bf780149c083bf2f603f5f32e4bd7917c80e51c7a1ec26bd067ad31a6a20ad",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "6c224d55b6047fc46b7ff528aaa31525a355b165aa8d73b865ffb4b3377426b3",
    "source_lines": "L1318-L1433",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-002"
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
  "stable_id": "BD-13-002",
  "title": "Dashboard Widget hỗ trợ: - Drag & Drop - Resize - Reorder - Multiple Workspace - Saved Layout",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-003 — KPI Definition được cấu hình. Kiến trúc hỗ trợ mở rộng thêm các nhóm KPI và tiêu chuẩn đo lường

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
  "normative_statement": "KPI Definition được cấu hình. Kiến trúc hỗ trợ mở rộng thêm các nhóm KPI và tiêu chuẩn đo lường.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-003",
    "phase_2c_c3_actions": [
      "C3_APPROVED_DECISION_COMPOSITE_SPLIT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. KPI",
    "source_context_sha256": "85344345dc19bcf0ae9030dce66f928f0fb4827b426c021d0e9d60c273f65f67",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "d2aba07c112f191c32bab386549c0e3f6575f5509c208c4c97962f4a1cd472cb",
    "source_fingerprint_before_c3": "118d78236b3b61bb4560bd320e5b3c71f048003f2e6864294adb2e34f2dd758e",
    "source_lines": "L1435-L1495",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-003"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-13-R043",
      "BRD-WS-13-R044",
      "BRD-WS-13-R045"
    ]
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-13-003",
  "title": "KPI Definition được cấu hình. Kiến trúc hỗ trợ mở rộng thêm các nhóm KPI và tiêu chuẩn đo lường",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-004 — Report là Business Object độc lập. System Report chỉ dành cho YSim Internal. Business Report hỗ …

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
  "normative_statement": "Report là Business Object độc lập. System Report chỉ dành cho YSim Internal. Business Report hỗ trợ kế thừa: YSim ↓ Parent Organization ↓ Organization Override",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-004",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Report Model",
    "source_context_sha256": "6f73245c294739f9ff85868c2f0b56a1e0564d82247e21cc390fc671549063d1",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "9790f500148d72bc50ad1ef266291e4b120a141f0fd49b68fa0f7f8af2ba2f6b",
    "source_fingerprint_before_c3": "417021a32b7b3387106e14462bcab42bbf2571d62a750b3e36ba8da1b9a614d4",
    "source_lines": "L1497-L1557",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-004"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-13-R026",
      "BRD-WS-13-R027",
      "BRD-WS-13-R028"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-13-004",
  "title": "Report là Business Object độc lập. System Report chỉ dành cho YSim Internal. Business Report hỗ …",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-005 — Saved View là Business Object. Saved View thuộc User

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
      "requirement_id": "BD-13-005",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "f20a4f04f8dc385d884006efbd56cf20a40650e60081c36f572328c4bcaf9d5b"
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
        "BD-13-005-AC001",
        "BD-13-005-AC003",
        "BD-13-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-005-O001",
      "obligation_text": "Saved View là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-005-AC002",
        "BD-13-005-AC003",
        "BD-13-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-005-O002",
      "obligation_text": "Saved View thuộc User"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Saved View là Business Object. Saved View thuộc User.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Saved View",
    "source_context_sha256": "6bafe0ecf9d78ed34ca431bbcfbbb18b456f40cf921d9630b456fd52d17c587c",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "f20a4f04f8dc385d884006efbd56cf20a40650e60081c36f572328c4bcaf9d5b",
    "source_lines": "L1559-L1648",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-005"
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
  "stable_id": "BD-13-005",
  "title": "Saved View là Business Object. Saved View thuộc User",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-006 — Report hỗ trợ: - Manual - Schedule - Event Trigger - Auto Generate - Auto Delivery

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
      "requirement_id": "BD-13-006",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "746d2d38740a8dba20b5560e9f68680529668f4a49abe131ddd9856a6494425b"
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
        "BD-13-006-AC001",
        "BD-13-006-AC006",
        "BD-13-006-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-006-O001",
      "obligation_text": "Report hỗ trợ: Manual"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-006-AC002",
        "BD-13-006-AC006",
        "BD-13-006-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-006-O002",
      "obligation_text": "Report hỗ trợ: Schedule"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-006-AC003",
        "BD-13-006-AC006",
        "BD-13-006-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-006-O003",
      "obligation_text": "Report hỗ trợ: Event Trigger"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-006-AC004",
        "BD-13-006-AC006",
        "BD-13-006-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-006-O004",
      "obligation_text": "Report hỗ trợ: Auto Generate"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-006-AC005",
        "BD-13-006-AC006",
        "BD-13-006-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-006-O005",
      "obligation_text": "Report hỗ trợ: Auto Delivery"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report hỗ trợ: - Manual - Schedule - Event Trigger - Auto Generate - Auto Delivery",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Report Schedule",
    "source_context_sha256": "ef4878e20a5bf00fbc2c93ee63aee6329f251c0aff3fec22eb16af80ee055de1",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "746d2d38740a8dba20b5560e9f68680529668f4a49abe131ddd9856a6494425b",
    "source_lines": "L1650-L1765",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-006"
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
  "stable_id": "BD-13-006",
  "title": "Report hỗ trợ: - Manual - Schedule - Event Trigger - Auto Generate - Auto Delivery",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-007 — Report hỗ trợ: - Download - Email - Portal - Personal Inbox - API

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
      "requirement_id": "BD-13-007",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "014f8080271b72044f5abb9f170cd2b46bdc58e5a5e8b25253ad146d1b4c78dd"
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
        "BD-13-007-AC001",
        "BD-13-007-AC006",
        "BD-13-007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-007-O001",
      "obligation_text": "Report hỗ trợ: Download"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-007-AC002",
        "BD-13-007-AC006",
        "BD-13-007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-007-O002",
      "obligation_text": "Report hỗ trợ: Email"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-007-AC003",
        "BD-13-007-AC006",
        "BD-13-007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-007-O003",
      "obligation_text": "Report hỗ trợ: Portal"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-007-AC004",
        "BD-13-007-AC006",
        "BD-13-007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-007-O004",
      "obligation_text": "Report hỗ trợ: Personal Inbox"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-007-AC005",
        "BD-13-007-AC006",
        "BD-13-007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-007-O005",
      "obligation_text": "Report hỗ trợ: API"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report hỗ trợ: - Download - Email - Portal - Personal Inbox - API",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Report Schedule",
    "source_context_sha256": "ef4878e20a5bf00fbc2c93ee63aee6329f251c0aff3fec22eb16af80ee055de1",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "014f8080271b72044f5abb9f170cd2b46bdc58e5a5e8b25253ad146d1b4c78dd",
    "source_lines": "L1767-L1882",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-007"
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
  "stable_id": "BD-13-007",
  "title": "Report hỗ trợ: - Download - Email - Portal - Personal Inbox - API",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-008 — Dashboard hỗ trợ Drill-down tới Business Object

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
      "requirement_id": "BD-13-008",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "afce28673e1503ef11a59c39b2df9108159760ca55b598ace0d903425d2bd436"
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
        "BD-13-008-AC001",
        "BD-13-008-AC002",
        "BD-13-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-008-O001",
      "obligation_text": "Dashboard hỗ trợ Drill-down tới Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dashboard hỗ trợ Drill-down tới Business Object.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-008",
    "source_context_sha256": "5ccda981949ec7d80ee71d57a5a8bab8c9fdafdccf201640a774c046b6ce2e4f",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "afce28673e1503ef11a59c39b2df9108159760ca55b598ace0d903425d2bd436",
    "source_lines": "L1884-L1959",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-008"
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
  "stable_id": "BD-13-008",
  "title": "Dashboard hỗ trợ Drill-down tới Business Object",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-009 — Metric là Business Object. Metric là đơn vị đo lường chuẩn để xây dựng Dashboard, KPI và Report

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
      "requirement_id": "BD-13-009",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "77b088f753072550cb008682fc8347ba128234c304823637a4baab20961510b5"
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
        "BD-13-009-AC001",
        "BD-13-009-AC003",
        "BD-13-009-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-009-O001",
      "obligation_text": "Metric là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-009-AC002",
        "BD-13-009-AC003",
        "BD-13-009-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-009-O002",
      "obligation_text": "Metric là đơn vị đo lường chuẩn để xây dựng Dashboard, KPI và Report"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Metric là Business Object. Metric là đơn vị đo lường chuẩn để xây dựng Dashboard, KPI và Report.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Metric",
    "source_context_sha256": "2fbb375914d47a181ea7c864bddff0a18c1017527da1e489db6104c69de070cd",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "77b088f753072550cb008682fc8347ba128234c304823637a4baab20961510b5",
    "source_lines": "L1961-L2046",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-009"
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
  "stable_id": "BD-13-009",
  "title": "Metric là Business Object. Metric là đơn vị đo lường chuẩn để xây dựng Dashboard, KPI và Report",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-010 — Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…

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
      "requirement_id": "BD-13-010",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "451f60e7a8c096189d54d453c071285e28a6414094fd6f4e5358f3c81f74f2cd"
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
        "BD-13-010-AC001",
        "BD-13-010-AC010",
        "BD-13-010-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O001",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Notification"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC002",
        "BD-13-010-AC010",
        "BD-13-010-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O002",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Workflow"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC003",
        "BD-13-010-AC010",
        "BD-13-010-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O003",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Business Action Ví dụ"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC004",
        "BD-13-010-AC010",
        "BD-13-010-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O004",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Block User"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC005",
        "BD-13-010-AC010",
        "BD-13-010-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O005",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Block Organization"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC006",
        "BD-13-010-AC010",
        "BD-13-010-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O006",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Block IP"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC007",
        "BD-13-010-AC010",
        "BD-13-010-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O007",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Block Transaction"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC008",
        "BD-13-010-AC010",
        "BD-13-010-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O008",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Escalation"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC009",
        "BD-13-010-AC010",
        "BD-13-010-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O009",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Auto Ticket"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business Action Ví dụ: - Block User - Block Organization - Block IP - Block Transaction - Escalation - Auto Ticket",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Alert Rule",
    "source_context_sha256": "25d39dcaa70499da4371c1f7288f3899a3506528d3f4a875f711e63970e85c71",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "451f60e7a8c096189d54d453c071285e28a6414094fd6f4e5358f3c81f74f2cd",
    "source_lines": "L2048-L2207",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-010"
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
  "stable_id": "BD-13-010",
  "title": "Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-011 — Operational Dashboard có thể: - Real-time - Near Real-time Tùy theo yêu cầu nghiệp vụ và khả năn…

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
      "requirement_id": "BD-13-011",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "5404b40759428d6cfa32d22937ca0549545fa54826f4163554bfc456fde13e1e"
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
        "BD-13-011-AC001",
        "BD-13-011-AC003",
        "BD-13-011-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-011-O001",
      "obligation_text": "Operational Dashboard có thể: Real-time"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-011-AC002",
        "BD-13-011-AC003",
        "BD-13-011-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-011-O002",
      "obligation_text": "Operational Dashboard có thể: Near Real-time Tùy theo yêu cầu nghiệp vụ và khả năng triển khai"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operational Dashboard có thể: - Real-time - Near Real-time Tùy theo yêu cầu nghiệp vụ và khả năng triển khai.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-011",
    "source_context_sha256": "c398847263e024a0efaa86c690a040d643922e9f21df7294f8c2c449af41924f",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "5404b40759428d6cfa32d22937ca0549545fa54826f4163554bfc456fde13e1e",
    "source_lines": "L2209-L2294",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-011"
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
  "stable_id": "BD-13-011",
  "title": "Operational Dashboard có thể: - Real-time - Near Real-time Tùy theo yêu cầu nghiệp vụ và khả năn…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-012 — Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: - AI Analytics - Mach…

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
      "requirement_id": "BD-13-012",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "2314dd86bf3748c821ce79b031d7d1a3c3149b6fe7e370b5212ee2f6b0729a3d"
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
        "BD-13-012-AC001",
        "BD-13-012-AC004",
        "BD-13-012-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-012-O001",
      "obligation_text": "Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: AI Analytics"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-012-AC002",
        "BD-13-012-AC004",
        "BD-13-012-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-012-O002",
      "obligation_text": "Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: Machine Learning"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-012-AC003",
        "BD-13-012-AC004",
        "BD-13-012-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-012-O003",
      "obligation_text": "Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: Predictive Analytics"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: - AI Analytics - Machine Learning - Predictive Analytics",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-012",
    "source_context_sha256": "097406231ae0b7a8c981c00dba166579fdff8e83c32e81ae5cc98bfa5b2ff4b1",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "2314dd86bf3748c821ce79b031d7d1a3c3149b6fe7e370b5212ee2f6b0729a3d",
    "source_lines": "L2296-L2391",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-012"
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
  "stable_id": "BD-13-012",
  "title": "Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: - AI Analytics - Mach…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-013 — Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support …

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
  "normative_statement": "Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support Policy Có thể Mask dữ liệu theo Permission.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-013",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-013",
    "source_context_sha256": "c2d9e76299e296e5c0f8f686f969d8b53c51bf163468c0eaf194a891f82dad3f",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "a941b33800e8f1734ba43db66c434bd72e42d1d802700984d1fa46009204beea",
    "source_fingerprint_before_c3": "870fbac209e092746fa51e63bb215da9b9e9bde53432a004b8009c7300a5c1a4",
    "source_lines": "L2393-L2455",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-013"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-13-R029",
      "BRD-WS-13-R030",
      "BRD-WS-13-R031",
      "BRD-WS-13-R032",
      "BRD-WS-13-R033"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-13-013",
  "title": "Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support …",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-014 — Dashboard hiển thị dữ liệu theo: - Localization - Currency Preference - Measurement Preference R…

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
      "requirement_id": "BD-13-014",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "49ca608971ebe5882407b24d4e3579b59052c0dbb91df303bf216429c4b7363d"
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
        "BD-13-014-AC001",
        "BD-13-014-AC004",
        "BD-13-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-014-O001",
      "obligation_text": "Dashboard hiển thị dữ liệu theo: Localization"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-014-AC002",
        "BD-13-014-AC004",
        "BD-13-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-014-O002",
      "obligation_text": "Dashboard hiển thị dữ liệu theo: Currency Preference"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-014-AC003",
        "BD-13-014-AC004",
        "BD-13-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-014-O003",
      "obligation_text": "Dashboard hiển thị dữ liệu theo: Measurement Preference Report mặc định sử dụng Currency chuẩn của Report"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-13-014-AC005"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-13-014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-13-014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-13-014-AC004"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-13-014-AC001",
        "BD-13-014-AC002",
        "BD-13-014-AC003"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-13-014 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dashboard hiển thị dữ liệu theo: - Localization - Currency Preference - Measurement Preference Report mặc định sử dụng Currency chuẩn của Report.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-014",
    "source_context_sha256": "9508f494a2f6139643fe1e264c9d9bcf642ee1c1cd7b779a3c81d20991ed4f45",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "49ca608971ebe5882407b24d4e3579b59052c0dbb91df303bf216429c4b7363d",
    "source_lines": "L2457-L2589",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-014"
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
  "stable_id": "BD-13-014",
  "title": "Dashboard hiển thị dữ liệu theo: - Localization - Currency Preference - Measurement Preference R…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-015 — Report luôn đọc dữ liệu từ Snapshot. Không đọc trực tiếp Transaction đang thay đổi

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "A newly created Snapshot may replace the prior source for a subsequent report; an executing report stays on its selected Snapshot"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-13-015.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                "source_type": "SOURCE_LITERAL",
                "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
              },
              "identifier": "BD-13-015.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BD-13-015.BD-13-015.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
            "source_lines": "L935-L940",
            "source_section": "29. Business Decisions (Locked) > BD-13-015"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BD-13-015.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                "source_type": "SOURCE_LITERAL",
                "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
              },
              "identifier": "BD-13-015.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BD-13-015.BD-13-015.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
            "source_lines": "L935-L940",
            "source_section": "29. Business Decisions (Locked) > BD-13-015"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
            "source_type": "SOURCE_LITERAL",
            "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
          },
          "identifier": "BD-13-015.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
            "source_lines": "L935-L940",
            "source_section": "29. Business Decisions (Locked) > BD-13-015"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BD-13-015.BD-13-015.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
            "source_type": "SOURCE_LITERAL",
            "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
          },
          "identifier": "BD-13-015.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
            "source_lines": "L935-L940",
            "source_section": "29. Business Decisions (Locked) > BD-13-015"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BD-13-015.BD-13-015.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
            "source_type": "SOURCE_LITERAL",
            "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
          },
          "identifier": "BD-13-015.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
            "source_lines": "L935-L940",
            "source_section": "29. Business Decisions (Locked) > BD-13-015"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BD-13-015.BD-13-015.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
            "source_type": "SOURCE_LITERAL",
            "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
          },
          "identifier": "BD-13-015.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
            "source_lines": "L935-L940",
            "source_section": "29. Business Decisions (Locked) > BD-13-015"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BD-13-015.BD-13-015.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
            "source_type": "SOURCE_LITERAL",
            "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
          },
          "identifier": "BD-13-015.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
            "source_lines": "L935-L940",
            "source_section": "29. Business Decisions (Locked) > BD-13-015"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.BD-13-015.BD-13-015.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      },
      {
        "actual_set": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
            "source_type": "SOURCE_LITERAL",
            "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
          },
          "identifier": "RESOLVED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BD-13-015.RESOLVED.COLLECTION",
          "origin": {
            "origin_id": "YSIM.BD-13-015.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
            "source_lines": "L935-L940",
            "source_section": "29. Business Decisions (Locked) > BD-13-015"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "OBSERVE.BD-13-015.RESOLVED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
        },
        "prohibited_members": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
            "source_type": "SOURCE_LITERAL",
            "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
          },
          "identifier": "GOVERNED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BD-13-015.GOVERNED.COLLECTION",
          "origin": {
            "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.PROHIBITED_MEMBERS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
            "source_lines": "L935-L940",
            "source_section": "29. Business Decisions (Locked) > BD-13-015"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "RESOLVE.BD-13-015.GOVERNED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BD-13-015",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "The Report reads mutable Transaction state directly"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID",
      "SET_EXCLUDES"
    ],
    "positive_oracle": [
      "The Report reads the Snapshot and never reads a changing Transaction directly"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
      "source_lines": "L935-L940",
      "source_section": "29. Business Decisions (Locked) > BD-13-015"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
          "source_type": "SOURCE_LITERAL",
          "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
        },
        "identifier": "BD-13-015.BD-13-015.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BD-13-015.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-13.md",
          "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
          "source_lines": "L935-L940",
          "source_section": "29. Business Decisions (Locked) > BD-13-015"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BD-13-015.BD-13-015.BD-13-015.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BD-13-015.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.REPORT_ID",
        "FIELD.SNAPSHOT_ID",
        "FIELD.TRANSACTION_ID",
        "FIELD.DATA_SOURCE_TYPE",
        "FIELD.SNAPSHOT_VERSION",
        "FIELD.READ_AUDIT"
      ],
      "producer": "BD-13-015.EVIDENCE.PRODUCER",
      "required_collection_origin": "BD-13-015.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.REPORT_ID",
        "FIELD.SNAPSHOT_ID",
        "FIELD.TRANSACTION_ID",
        "FIELD.DATA_SOURCE_TYPE",
        "FIELD.SNAPSHOT_VERSION",
        "FIELD.READ_AUDIT"
      ],
      "required_values_or_hashes": [
        "BD-13-015.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BD-13-015.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BD-13-015.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BD-13-015-O001",
      "BD-13-015-O002"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID",
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
              "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
              "source_type": "SOURCE_LITERAL",
              "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
            },
            "identifier": "BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
              "source_lines": "L935-L940",
              "source_section": "29. Business Decisions (Locked) > BD-13-015"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-13-015.BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
              "source_type": "SOURCE_LITERAL",
              "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
            },
            "identifier": "BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
              "source_lines": "L935-L940",
              "source_section": "29. Business Decisions (Locked) > BD-13-015"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BD-13-015.BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                        "BD-13-015.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                      "source_type": "SOURCE_LITERAL",
                      "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                    },
                    "identifier": "BD-13-015.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-13.md",
                      "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                      "source_lines": "L935-L940",
                      "source_section": "29. Business Decisions (Locked) > BD-13-015"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BD-13-015.BD-13-015.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BD-13-015.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                      "source_type": "SOURCE_LITERAL",
                      "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                    },
                    "identifier": "BD-13-015.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-13.md",
                      "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                      "source_lines": "L935-L940",
                      "source_section": "29. Business Decisions (Locked) > BD-13-015"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BD-13-015.BD-13-015.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                  "source_type": "SOURCE_LITERAL",
                  "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                },
                "identifier": "BD-13-015.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BD-13-015.BD-13-015.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                  "source_type": "SOURCE_LITERAL",
                  "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                },
                "identifier": "BD-13-015.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BD-13-015.BD-13-015.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                  "source_type": "SOURCE_LITERAL",
                  "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                },
                "identifier": "BD-13-015.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BD-13-015.BD-13-015.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                  "source_type": "SOURCE_LITERAL",
                  "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                },
                "identifier": "BD-13-015.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BD-13-015.BD-13-015.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                  "source_type": "SOURCE_LITERAL",
                  "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                },
                "identifier": "BD-13-015.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.BD-13-015.BD-13-015.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                  "source_type": "SOURCE_LITERAL",
                  "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                },
                "identifier": "BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BD-13-015.BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                  "source_type": "SOURCE_LITERAL",
                  "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                },
                "identifier": "BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BD-13-015.BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                "source_type": "SOURCE_LITERAL",
                "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
              },
              "identifier": "BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-13-015.BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "BD-13-015-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
              "source_type": "SOURCE_LITERAL",
              "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
            },
            "identifier": "BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
              "source_lines": "L935-L940",
              "source_section": "29. Business Decisions (Locked) > BD-13-015"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BD-13-015.BD-13-015.BD-13-015.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                      "BD-13-015.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                    "source_type": "SOURCE_LITERAL",
                    "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                  },
                  "identifier": "BD-13-015.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-13.md",
                    "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                    "source_lines": "L935-L940",
                    "source_section": "29. Business Decisions (Locked) > BD-13-015"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BD-13-015.BD-13-015.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BD-13-015.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                    "source_type": "SOURCE_LITERAL",
                    "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                  },
                  "identifier": "BD-13-015.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-13.md",
                    "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                    "source_lines": "L935-L940",
                    "source_section": "29. Business Decisions (Locked) > BD-13-015"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BD-13-015.BD-13-015.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                "source_type": "SOURCE_LITERAL",
                "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
              },
              "identifier": "BD-13-015.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BD-13-015.BD-13-015.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                "source_type": "SOURCE_LITERAL",
                "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
              },
              "identifier": "BD-13-015.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BD-13-015.BD-13-015.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                "source_type": "SOURCE_LITERAL",
                "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
              },
              "identifier": "BD-13-015.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BD-13-015.BD-13-015.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                "source_type": "SOURCE_LITERAL",
                "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
              },
              "identifier": "BD-13-015.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BD-13-015.BD-13-015.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                "source_type": "SOURCE_LITERAL",
                "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
              },
              "identifier": "BD-13-015.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-015.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.BD-13-015.BD-13-015.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        },
        {
          "assertion_id": "BD-13-015.O2.1.SET_EXCLUDES",
          "evaluator_consumed_bindings": [
            "actual_set",
            "prohibited_members"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
              "source_type": "SOURCE_LITERAL",
              "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
            },
            "identifier": "BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
              "source_lines": "L935-L940",
              "source_section": "29. Business Decisions (Locked) > BD-13-015"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-13-015.BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                  "source_type": "SOURCE_LITERAL",
                  "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                },
                "identifier": "BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.AUTHORITY.ORIGIN.MEMBER.1",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BD-13-015.BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
              "source_lines": "L935-L940",
              "source_section": "29. Business Decisions (Locked) > BD-13-015"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                  "source_type": "SOURCE_LITERAL",
                  "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                },
                "identifier": "RESOLVED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BD-13-015.RESOLVED.COLLECTION",
                "origin": {
                  "origin_id": "YSIM.BD-13-015.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "OBSERVE.BD-13-015.RESOLVED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
              },
              "prohibited_members": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                  "source_type": "SOURCE_LITERAL",
                  "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                },
                "identifier": "GOVERNED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BD-13-015.GOVERNED.COLLECTION",
                "origin": {
                  "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.PROHIBITED_MEMBERS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "RESOLVE.BD-13-015.GOVERNED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
              }
            },
            "comparison": {
              "expected": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                      "source_type": "SOURCE_LITERAL",
                      "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                    },
                    "identifier": "BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.AUTHORITY.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-13.md",
                      "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                      "source_lines": "L935-L940",
                      "source_section": "29. Business Decisions (Locked) > BD-13-015"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BD-13-015.BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                      "source_type": "SOURCE_LITERAL",
                      "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                    },
                    "identifier": "BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.OBSERVED.ORIGIN.MEMBER.1",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-13.md",
                      "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                      "source_lines": "L935-L940",
                      "source_section": "29. Business Decisions (Locked) > BD-13-015"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "OBSERVE.BD-13-015.BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                "source_type": "SOURCE_LITERAL",
                "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
              },
              "identifier": "BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-13-015.BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SET_EXCLUDES"
          },
          "obligation_id": "BD-13-015-O002",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                  "source_type": "SOURCE_LITERAL",
                  "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
                },
                "identifier": "BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.OBSERVED.ORIGIN.MEMBER.1",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                  "source_lines": "L935-L940",
                  "source_section": "29. Business Decisions (Locked) > BD-13-015"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BD-13-015.BD-13-015.BD-13-015.O2.1.SET_EXCLUDES.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
              "source_lines": "L935-L940",
              "source_section": "29. Business Decisions (Locked) > BD-13-015"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "operator_id": "SET_EXCLUDES",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_set": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                "source_type": "SOURCE_LITERAL",
                "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
              },
              "identifier": "RESOLVED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BD-13-015.RESOLVED.COLLECTION",
              "origin": {
                "origin_id": "YSIM.BD-13-015.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "OBSERVE.BD-13-015.RESOLVED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
            },
            "prohibited_members": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
                "source_type": "SOURCE_LITERAL",
                "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
              },
              "identifier": "GOVERNED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BD-13-015.GOVERNED.COLLECTION",
              "origin": {
                "origin_id": "BD-13-015.O2.1.SET_EXCLUDES.PROHIBITED_MEMBERS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
                "source_lines": "L935-L940",
                "source_section": "29. Business Decisions (Locked) > BD-13-015"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "RESOLVE.BD-13-015.GOVERNED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
            }
          }
        }
      ],
      "boundary_cases": [
        "A newly created Snapshot may replace the prior source for a subsequent report; an executing report stays on its selected Snapshot"
      ],
      "contract_ast_sha256": "aca001832d8271d6597e014ed03ad62bdd0eea61b23fdffb9e94ab081bea7f66",
      "contract_id": "P2C.C4.CONTRACT.BD-13-015",
      "criticality": "HIGH",
      "disposition": "COMPOUND_AST_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-015",
            "source_type": "SOURCE_LITERAL",
            "version": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf"
          },
          "identifier": "BD-13-015.BD-13-015.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-015.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
            "source_lines": "L935-L940",
            "source_section": "29. Business Decisions (Locked) > BD-13-015"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BD-13-015.BD-13-015.BD-13-015.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BD-13-015.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.REPORT_ID",
          "FIELD.SNAPSHOT_ID",
          "FIELD.TRANSACTION_ID",
          "FIELD.DATA_SOURCE_TYPE",
          "FIELD.SNAPSHOT_VERSION",
          "FIELD.READ_AUDIT"
        ],
        "producer": "BD-13-015.EVIDENCE.PRODUCER",
        "required_collection_origin": "BD-13-015.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.REPORT_ID",
          "FIELD.SNAPSHOT_ID",
          "FIELD.TRANSACTION_ID",
          "FIELD.DATA_SOURCE_TYPE",
          "FIELD.SNAPSHOT_VERSION",
          "FIELD.READ_AUDIT"
        ],
        "required_values_or_hashes": [
          "BD-13-015.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BD-13-015.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BD-13-015.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-R2-FX-51F21E789AF0A272EDF4",
        "P2C-C4-R2-FX-EA1245150EADDCBF2F19",
        "P2C-C4-R2-FX-758A8D261DFC155B7F44"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "The Report reads mutable Transaction state directly"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-13-015-O001",
          "obligation_text": "Report luôn đọc dữ liệu từ Snapshot"
        },
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-13-015-O002",
          "obligation_text": "Không đọc trực tiếp Transaction đang thay đổi"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BD-13-015.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-13-015-O001"
        },
        {
          "assertion_ids": [
            "BD-13-015.O2.1.SET_EXCLUDES"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-13-015-O002"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID",
        "SET_EXCLUDES"
      ],
      "positive_oracles": [
        "The Report reads the Snapshot and never reads a changing Transaction directly"
      ],
      "preconditions": [
        "The applicable immutable Snapshot exists"
      ],
      "prohibitions": [
        "The Report reads mutable Transaction state directly"
      ],
      "requirement_id": "BD-13-015",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-13.md",
        "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
        "source_lines": "L935-L940",
        "source_section": "29. Business Decisions (Locked) > BD-13-015"
      },
      "source_statement": "Report luôn đọc dữ liệu từ Snapshot. Không đọc trực tiếp Transaction đang thay đổi.",
      "surrounding_source_context": "## BD-13-015\n\nReport luôn đọc dữ liệu từ Snapshot.\n\nKhông đọc trực tiếp Transaction đang thay đổi.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BD-13-015",
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
        "BD-13-015-AC001",
        "BD-13-015-AC003",
        "BD-13-015-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-015-O001",
      "obligation_text": "Report luôn đọc dữ liệu từ Snapshot"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-015-AC002",
        "BD-13-015-AC003",
        "BD-13-015-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-015-O002",
      "obligation_text": "Không đọc trực tiếp Transaction đang thay đổi"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report luôn đọc dữ liệu từ Snapshot. Không đọc trực tiếp Transaction đang thay đổi.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Reporting Snapshot",
    "source_context_sha256": "249ed3d5f4ce9a4f8ec5ebc8323ba8cf46130e41018e4f119b561e8f889c3bd7",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "30bcd1716bfbe0dd44cfb07c69b5c7b17394a2450bb5bad9a463201ae0e853f4",
    "source_lines": "L2591-L4479",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-015"
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
  "stable_id": "BD-13-015",
  "title": "Report luôn đọc dữ liệu từ Snapshot. Không đọc trực tiếp Transaction đang thay đổi",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-016 — Supplier Analytics chỉ dành cho YSim Internal. Supplier không có Dashboard riêng

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Internal authorized access is allowed; supplier self-service remains unavailable"
    ],
    "concrete_bindings": [
      {
        "action": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
            "source_type": "SOURCE_LITERAL",
            "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
          },
          "identifier": "BD-13-016.ACTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.ACTION.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-007"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
            "source_lines": "L943-L948",
            "source_section": "29. Business Decisions (Locked) > BD-13-016"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTION",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        },
        "actor": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
            "source_type": "SOURCE_LITERAL",
            "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
          },
          "identifier": "BD-13-016.ACTOR",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.ACTOR.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-007"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
            "source_lines": "L943-L948",
            "source_section": "29. Business Decisions (Locked) > BD-13-016"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "PRINCIPAL_ID",
            "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTOR",
            "version": "1.0.0"
          },
          "semantic_type": "PRINCIPAL_ID"
        },
        "effective_policy": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
            "source_type": "SOURCE_LITERAL",
            "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
          },
          "identifier": "BD-13-016.EFFECTIVE_POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.EFFECTIVE_POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-007"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
            "source_lines": "L943-L948",
            "source_section": "29. Business Decisions (Locked) > BD-13-016"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BD-13-016.BD-13-016.EFFECTIVE_POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "resource": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
            "source_type": "SOURCE_LITERAL",
            "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
          },
          "identifier": "BD-13-016.RESOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.RESOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-007"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
            "source_lines": "L943-L948",
            "source_section": "29. Business Decisions (Locked) > BD-13-016"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "RESOURCE_ID",
            "resolver_id": "RESOLVE.BD-13-016.BD-13-016.RESOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "RESOURCE_ID"
        }
      },
      {
        "action": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
            "source_type": "SOURCE_LITERAL",
            "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
          },
          "identifier": "BD-13-016.ACTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.ACTION.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-007"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
            "source_lines": "L943-L948",
            "source_section": "29. Business Decisions (Locked) > BD-13-016"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTION",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        },
        "actor": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
            "source_type": "SOURCE_LITERAL",
            "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
          },
          "identifier": "BD-13-016.ACTOR",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.ACTOR.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-007"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
            "source_lines": "L943-L948",
            "source_section": "29. Business Decisions (Locked) > BD-13-016"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "PRINCIPAL_ID",
            "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTOR",
            "version": "1.0.0"
          },
          "semantic_type": "PRINCIPAL_ID"
        },
        "effective_policy": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
            "source_type": "SOURCE_LITERAL",
            "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
          },
          "identifier": "BD-13-016.EFFECTIVE_POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.EFFECTIVE_POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-007"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
            "source_lines": "L943-L948",
            "source_section": "29. Business Decisions (Locked) > BD-13-016"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BD-13-016.BD-13-016.EFFECTIVE_POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "resource": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
            "source_type": "SOURCE_LITERAL",
            "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
          },
          "identifier": "BD-13-016.RESOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.RESOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-007"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
            "source_lines": "L943-L948",
            "source_section": "29. Business Decisions (Locked) > BD-13-016"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "RESOURCE_ID",
            "resolver_id": "RESOLVE.BD-13-016.BD-13-016.RESOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "RESOURCE_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BD-13-016",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "A Supplier or other external principal receives Supplier Analytics or a supplier dashboard"
    ],
    "operator_composition": [
      "ACTOR_AUTHORIZED",
      "ACTOR_DENIED"
    ],
    "positive_oracle": [
      "Only YSim Internal users can access Supplier Analytics"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-007"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
      "source_lines": "L943-L948",
      "source_section": "29. Business Decisions (Locked) > BD-13-016"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
          "source_type": "SOURCE_LITERAL",
          "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
        },
        "identifier": "BD-13-016.BD-13-016.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BD-13-016.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-007"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-13.md",
          "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
          "source_lines": "L943-L948",
          "source_section": "29. Business Decisions (Locked) > BD-13-016"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BD-13-016.BD-13-016.BD-13-016.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BD-13-016.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PRINCIPAL_ID",
        "FIELD.PRINCIPAL_TYPE",
        "FIELD.ROLE",
        "FIELD.AUTHORIZATION_RESULT",
        "FIELD.DASHBOARD_STATE",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "BD-13-016.EVIDENCE.PRODUCER",
      "required_collection_origin": "BD-13-016.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PRINCIPAL_ID",
        "FIELD.PRINCIPAL_TYPE",
        "FIELD.ROLE",
        "FIELD.AUTHORIZATION_RESULT",
        "FIELD.DASHBOARD_STATE",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "BD-13-016.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BD-13-016.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BD-13-016.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BD-13-016-O001",
      "BD-13-016-O002"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED",
          "evaluator_consumed_bindings": [
            "action",
            "actor",
            "effective_policy",
            "resource"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
              "source_type": "SOURCE_LITERAL",
              "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
            },
            "identifier": "BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-007"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
              "source_lines": "L943-L948",
              "source_section": "29. Business Decisions (Locked) > BD-13-016"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-13-016.BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
              "source_type": "SOURCE_LITERAL",
              "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
            },
            "identifier": "BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-007"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
              "source_lines": "L943-L948",
              "source_section": "29. Business Decisions (Locked) > BD-13-016"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "PRINCIPAL_ID",
              "resolver_id": "RESOLVE.BD-13-016.BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "PRINCIPAL_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "action": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.ACTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.ACTION.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTION",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              },
              "actor": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.ACTOR",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.ACTOR.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "PRINCIPAL_ID",
                  "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTOR",
                  "version": "1.0.0"
                },
                "semantic_type": "PRINCIPAL_ID"
              },
              "effective_policy": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.EFFECTIVE_POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.EFFECTIVE_POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BD-13-016.BD-13-016.EFFECTIVE_POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "resource": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.RESOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.RESOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "RESOURCE_ID",
                  "resolver_id": "RESOLVE.BD-13-016.BD-13-016.RESOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "RESOURCE_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "PRINCIPAL_ID",
                  "resolver_id": "RESOLVE.BD-13-016.BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "PRINCIPAL_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "PRINCIPAL_ID",
                  "resolver_id": "OBSERVE.BD-13-016.BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "PRINCIPAL_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                "source_type": "SOURCE_LITERAL",
                "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
              },
              "identifier": "BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-007"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                "source_lines": "L943-L948",
                "source_section": "29. Business Decisions (Locked) > BD-13-016"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-13-016.BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "ACTOR_AUTHORIZED"
          },
          "obligation_id": "BD-13-016-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
              "source_type": "SOURCE_LITERAL",
              "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
            },
            "identifier": "BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-007"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
              "source_lines": "L943-L948",
              "source_section": "29. Business Decisions (Locked) > BD-13-016"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "PRINCIPAL_ID",
              "resolver_id": "OBSERVE.BD-13-016.BD-13-016.BD-13-016.O1.1.ACTOR_AUTHORIZED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "PRINCIPAL_ID"
          },
          "operator_id": "ACTOR_AUTHORIZED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "action": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                "source_type": "SOURCE_LITERAL",
                "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
              },
              "identifier": "BD-13-016.ACTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.ACTION.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-007"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                "source_lines": "L943-L948",
                "source_section": "29. Business Decisions (Locked) > BD-13-016"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTION",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            },
            "actor": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                "source_type": "SOURCE_LITERAL",
                "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
              },
              "identifier": "BD-13-016.ACTOR",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.ACTOR.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-007"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                "source_lines": "L943-L948",
                "source_section": "29. Business Decisions (Locked) > BD-13-016"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "PRINCIPAL_ID",
                "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTOR",
                "version": "1.0.0"
              },
              "semantic_type": "PRINCIPAL_ID"
            },
            "effective_policy": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                "source_type": "SOURCE_LITERAL",
                "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
              },
              "identifier": "BD-13-016.EFFECTIVE_POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.EFFECTIVE_POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-007"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                "source_lines": "L943-L948",
                "source_section": "29. Business Decisions (Locked) > BD-13-016"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BD-13-016.BD-13-016.EFFECTIVE_POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "resource": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                "source_type": "SOURCE_LITERAL",
                "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
              },
              "identifier": "BD-13-016.RESOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-016.O1.1.ACTOR_AUTHORIZED.RESOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-007"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                "source_lines": "L943-L948",
                "source_section": "29. Business Decisions (Locked) > BD-13-016"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "RESOURCE_ID",
                "resolver_id": "RESOLVE.BD-13-016.BD-13-016.RESOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "RESOURCE_ID"
            }
          }
        },
        {
          "assertion_id": "BD-13-016.O2.1.ACTOR_DENIED",
          "evaluator_consumed_bindings": [
            "action",
            "actor",
            "effective_policy",
            "resource"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
              "source_type": "SOURCE_LITERAL",
              "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
            },
            "identifier": "BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-007"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
              "source_lines": "L943-L948",
              "source_section": "29. Business Decisions (Locked) > BD-13-016"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BD-13-016.BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
              "source_type": "SOURCE_LITERAL",
              "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
            },
            "identifier": "BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-007"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
              "source_lines": "L943-L948",
              "source_section": "29. Business Decisions (Locked) > BD-13-016"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "PRINCIPAL_ID",
              "resolver_id": "RESOLVE.BD-13-016.BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "PRINCIPAL_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "action": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.ACTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.ACTION.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTION",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              },
              "actor": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.ACTOR",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.ACTOR.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "PRINCIPAL_ID",
                  "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTOR",
                  "version": "1.0.0"
                },
                "semantic_type": "PRINCIPAL_ID"
              },
              "effective_policy": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.EFFECTIVE_POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.EFFECTIVE_POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BD-13-016.BD-13-016.EFFECTIVE_POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "resource": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.RESOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.RESOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "RESOURCE_ID",
                  "resolver_id": "RESOLVE.BD-13-016.BD-13-016.RESOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "RESOURCE_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "PRINCIPAL_ID",
                  "resolver_id": "RESOLVE.BD-13-016.BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "PRINCIPAL_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                  "source_type": "SOURCE_LITERAL",
                  "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
                },
                "identifier": "BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-007"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                  "source_lines": "L943-L948",
                  "source_section": "29. Business Decisions (Locked) > BD-13-016"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "PRINCIPAL_ID",
                  "resolver_id": "OBSERVE.BD-13-016.BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "PRINCIPAL_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                "source_type": "SOURCE_LITERAL",
                "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
              },
              "identifier": "BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-007"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                "source_lines": "L943-L948",
                "source_section": "29. Business Decisions (Locked) > BD-13-016"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BD-13-016.BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "ACTOR_DENIED"
          },
          "obligation_id": "BD-13-016-O002",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
              "source_type": "SOURCE_LITERAL",
              "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
            },
            "identifier": "BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-007"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
              "source_lines": "L943-L948",
              "source_section": "29. Business Decisions (Locked) > BD-13-016"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "PRINCIPAL_ID",
              "resolver_id": "OBSERVE.BD-13-016.BD-13-016.BD-13-016.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "PRINCIPAL_ID"
          },
          "operator_id": "ACTOR_DENIED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "action": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                "source_type": "SOURCE_LITERAL",
                "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
              },
              "identifier": "BD-13-016.ACTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.ACTION.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-007"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                "source_lines": "L943-L948",
                "source_section": "29. Business Decisions (Locked) > BD-13-016"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTION",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            },
            "actor": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                "source_type": "SOURCE_LITERAL",
                "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
              },
              "identifier": "BD-13-016.ACTOR",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.ACTOR.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-007"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                "source_lines": "L943-L948",
                "source_section": "29. Business Decisions (Locked) > BD-13-016"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "PRINCIPAL_ID",
                "resolver_id": "RESOLVE.BD-13-016.BD-13-016.ACTOR",
                "version": "1.0.0"
              },
              "semantic_type": "PRINCIPAL_ID"
            },
            "effective_policy": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                "source_type": "SOURCE_LITERAL",
                "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
              },
              "identifier": "BD-13-016.EFFECTIVE_POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.EFFECTIVE_POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-007"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                "source_lines": "L943-L948",
                "source_section": "29. Business Decisions (Locked) > BD-13-016"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BD-13-016.BD-13-016.EFFECTIVE_POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "resource": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
                "source_type": "SOURCE_LITERAL",
                "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
              },
              "identifier": "BD-13-016.RESOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BD-13-016.O2.1.ACTOR_DENIED.RESOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-007"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
                "source_lines": "L943-L948",
                "source_section": "29. Business Decisions (Locked) > BD-13-016"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "RESOURCE_ID",
                "resolver_id": "RESOLVE.BD-13-016.BD-13-016.RESOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "RESOURCE_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "Internal authorized access is allowed; supplier self-service remains unavailable"
      ],
      "contract_ast_sha256": "8608f412f131b02091b8767da476ab6c1736e3f7d2c81b0466bab5555cc52d20",
      "contract_id": "P2C.C4.CONTRACT.BD-13-016",
      "criticality": "HIGH",
      "disposition": "COMPOUND_AST_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#29. Business Decisions (Locked) > BD-13-016",
            "source_type": "SOURCE_LITERAL",
            "version": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f"
          },
          "identifier": "BD-13-016.BD-13-016.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BD-13-016.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-007"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
            "source_lines": "L943-L948",
            "source_section": "29. Business Decisions (Locked) > BD-13-016"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BD-13-016.BD-13-016.BD-13-016.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BD-13-016.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PRINCIPAL_ID",
          "FIELD.PRINCIPAL_TYPE",
          "FIELD.ROLE",
          "FIELD.AUTHORIZATION_RESULT",
          "FIELD.DASHBOARD_STATE",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "BD-13-016.EVIDENCE.PRODUCER",
        "required_collection_origin": "BD-13-016.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PRINCIPAL_ID",
          "FIELD.PRINCIPAL_TYPE",
          "FIELD.ROLE",
          "FIELD.AUTHORIZATION_RESULT",
          "FIELD.DASHBOARD_STATE",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "BD-13-016.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BD-13-016.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BD-13-016.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-5EF8573E695C84FC9CC5",
        "P2C-C4-FX-4AB518A653038516F0B0",
        "P2C-C4-FX-878B37A562A122A02A39"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "A Supplier or other external principal receives Supplier Analytics or a supplier dashboard"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-13-016-O001",
          "obligation_text": "Supplier Analytics chỉ dành cho YSim Internal"
        },
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BD-13-016-O002",
          "obligation_text": "Supplier không có Dashboard riêng"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BD-13-016.O1.1.ACTOR_AUTHORIZED"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-13-016-O001"
        },
        {
          "assertion_ids": [
            "BD-13-016.O2.1.ACTOR_DENIED"
          ],
          "coverage_count": 1,
          "obligation_id": "BD-13-016-O002"
        }
      ],
      "operator_composition": [
        "ACTOR_AUTHORIZED",
        "ACTOR_DENIED"
      ],
      "positive_oracles": [
        "Only YSim Internal users can access Supplier Analytics"
      ],
      "preconditions": [
        "The principal identity and role are resolved"
      ],
      "prohibitions": [
        "A Supplier or other external principal receives Supplier Analytics or a supplier dashboard"
      ],
      "requirement_id": "BD-13-016",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-007"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-13.md",
        "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
        "source_lines": "L943-L948",
        "source_section": "29. Business Decisions (Locked) > BD-13-016"
      },
      "source_statement": "Supplier Analytics chỉ dành cho YSim Internal. Supplier không có Dashboard riêng.",
      "surrounding_source_context": "## BD-13-016\n\nSupplier Analytics chỉ dành cho YSim Internal.\n\nSupplier không có Dashboard riêng.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BD-13-016",
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
        "BD-13-016-AC001",
        "BD-13-016-AC003",
        "BD-13-016-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-016-O001",
      "obligation_text": "Supplier Analytics chỉ dành cho YSim Internal"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-016-AC002",
        "BD-13-016-AC003",
        "BD-13-016-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-016-O002",
      "obligation_text": "Supplier không có Dashboard riêng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier Analytics chỉ dành cho YSim Internal. Supplier không có Dashboard riêng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-016",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Supplier Analytics",
    "source_context_sha256": "62d4026978ad73121ea2b210155e4124b83cd0d93407ce4a43e4543085d46d0a",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "57d3e3b479a88829047af674b1c7d04145fffc5cab50dff1ad3e93b62b81dde6",
    "source_lines": "L4481-L6148",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-016"
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
  "stable_id": "BD-13-016",
  "title": "Supplier Analytics chỉ dành cho YSim Internal. Supplier không có Dashboard riêng",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-017 — Organization chỉ được Benchmark dữ liệu của chính Organization đó. Không được phép xem dữ liệu c…

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
      "requirement_id": "BD-13-017",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "22e037ebe01e5033a38e590b5f74954d7701945eba67b76bfe062fc2e4fddcec"
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
        "BD-13-017-AC001",
        "BD-13-017-AC003",
        "BD-13-017-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-017-O001",
      "obligation_text": "Organization chỉ được Benchmark dữ liệu của chính Organization đó"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-017-AC002",
        "BD-13-017-AC003",
        "BD-13-017-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-017-O002",
      "obligation_text": "Không được phép xem dữ liệu của Organization khác"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization chỉ được Benchmark dữ liệu của chính Organization đó. Không được phép xem dữ liệu của Organization khác.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-017",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-017",
    "source_context_sha256": "5e3c84b14eb737ead14e51cf50455173a7b46ad0715d63b0e2edf71c49296eb8",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "22e037ebe01e5033a38e590b5f74954d7701945eba67b76bfe062fc2e4fddcec",
    "source_lines": "L6150-L6235",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-017"
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
  "stable_id": "BD-13-017",
  "title": "Organization chỉ được Benchmark dữ liệu của chính Organization đó. Không được phép xem dữ liệu c…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-018 — Version 2 hỗ trợ Custom Report Builder. Report được cấu hình thay vì Hard-code

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
      "requirement_id": "BD-13-018",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "0fece934eec1d84fdcddecc5ee3207cecad1163d441a9470d8afa4ed0d22bda9"
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
        "BD-13-018-AC001",
        "BD-13-018-AC003",
        "BD-13-018-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-018-O001",
      "obligation_text": "Version 2 hỗ trợ Custom Report Builder"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-018-AC002",
        "BD-13-018-AC003",
        "BD-13-018-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-018-O002",
      "obligation_text": "Report được cấu hình thay vì Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Version 2 hỗ trợ Custom Report Builder. Report được cấu hình thay vì Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-018",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "24. Report Builder",
    "source_context_sha256": "af8f07d7e274c4cd098fcece8d51e97d431c4c1ff4c40c7bc36a9521765bf37f",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "0fece934eec1d84fdcddecc5ee3207cecad1163d441a9470d8afa4ed0d22bda9",
    "source_lines": "L6237-L6322",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-018"
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
  "stable_id": "BD-13-018",
  "title": "Version 2 hỗ trợ Custom Report Builder. Report được cấu hình thay vì Hard-code",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-019 — Widget Library là Platform Capability. Widget được tái sử dụng trên: - Dashboard - Workspace - A…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005",
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-13-019",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "876eab5bdefdfae336ab9437744be4d6fcfa3da9284c471cde5deeaff1d2326c"
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
        "BD-13-019-AC001",
        "BD-13-019-AC006",
        "BD-13-019-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-019-O001",
      "obligation_text": "Widget Library là Platform Capability. Widget được tái sử dụng trên: Dashboard"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-019-AC002",
        "BD-13-019-AC006",
        "BD-13-019-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-019-O002",
      "obligation_text": "Widget Library là Platform Capability. Widget được tái sử dụng trên: Workspace"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-019-AC003",
        "BD-13-019-AC006",
        "BD-13-019-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-019-O003",
      "obligation_text": "Widget Library là Platform Capability. Widget được tái sử dụng trên: Admin Portal"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-019-AC004",
        "BD-13-019-AC006",
        "BD-13-019-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-019-O004",
      "obligation_text": "Widget Library là Platform Capability. Widget được tái sử dụng trên: Organization Portal"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-019-AC005",
        "BD-13-019-AC006",
        "BD-13-019-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-019-O005",
      "obligation_text": "Widget Library là Platform Capability. Widget được tái sử dụng trên: Customer Portal"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Widget Library là Platform Capability. Widget được tái sử dụng trên: - Dashboard - Workspace - Admin Portal - Organization Portal - Customer Portal",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-019",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Widget Library",
    "source_context_sha256": "23adaa9026073a8156aa394e9d4951b65efd1f0759ace24911947babf5d3ecd8",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "876eab5bdefdfae336ab9437744be4d6fcfa3da9284c471cde5deeaff1d2326c",
    "source_lines": "L6324-L6445",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-019"
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
  "stable_id": "BD-13-019",
  "title": "Widget Library là Platform Capability. Widget được tái sử dụng trên: - Dashboard - Workspace - A…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-020 — Insight là Business Object. Insight được sinh từ Rule Engine và Analytics. Version 2 chưa sử dụn…

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
  "normative_statement": "Insight là Business Object. Insight được sinh từ Rule Engine và Analytics. Version 2 chưa sử dụng AI.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-020",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. Operational Insight",
    "source_context_sha256": "e14305f76ca4b6c0410aa695e886b2cab72e8c679002d56f9a33141eb435ad63",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "bb8f64901e3f13dd394f952dc62b2205ebc86e65aff9d0d99779f0ef25d5288b",
    "source_fingerprint_before_c3": "8e0f9e6f8f3fe2a0086b261cffb1f37ca1b98d109b41c43f86bc2648ec579191",
    "source_lines": "L6447-L6507",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-13-020"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-13-R034",
      "BRD-WS-13-R035",
      "BRD-WS-13-R036"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-13-020",
  "title": "Insight là Business Object. Insight được sinh từ Rule Engine và Analytics. Version 2 chưa sử dụn…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R001 — (Các nội dung trên được giữ chỗ cho các phiên bản sau.)

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-13-R001",
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
  "normative_statement": "(Các nội dung trên được giữ chỗ cho các phiên bản sau.)",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-001",
    "previous_temporary_key": "TMP-BRD-WS-13-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "1. Workshop Objective",
    "source_context_sha256": "ff5d2d6c9ccaa7d8015dd4d1ce9e1f600f7eefa607740cb684b128be3c5d9344",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "342495c719a53e556ce271956cdc09b86d32b124db94d46100a7ce92f1fb0a1b",
    "source_lines": "L6509-L6567",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R001"
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
  "stable_id": "BRD-WS-13-R001",
  "title": "(Các nội dung trên được giữ chỗ cho các phiên bản sau.)",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R002 — Dashboard và Widget phải hỗ trợ Drill-down tới module hoặc Business Object tương ứng

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
      "requirement_id": "BRD-WS-13-R002",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "c17bf6295dddaf1dc833cc10658a7c3fe397fdc8ff1c8d8a1cebf8cb9898d7e9"
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
        "BRD-WS-13-R002-AC001",
        "BRD-WS-13-R002-AC002",
        "BRD-WS-13-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R002-O001",
      "obligation_text": "Dashboard và Widget phải hỗ trợ Drill-down tới module hoặc Business Object tương ứng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dashboard và Widget phải hỗ trợ Drill-down tới module hoặc Business Object tương ứng.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-002",
    "previous_temporary_key": "TMP-BRD-WS-13-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Dashboard Model",
    "source_context_sha256": "5e5d4e68d2e4787a078aa6aa6579cb37881422ec7dc9e499450bc6786b4c1d82",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "c17bf6295dddaf1dc833cc10658a7c3fe397fdc8ff1c8d8a1cebf8cb9898d7e9",
    "source_lines": "L6569-L6644",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R002"
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
  "stable_id": "BRD-WS-13-R002",
  "title": "Dashboard và Widget phải hỗ trợ Drill-down tới module hoặc Business Object tương ứng",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R003 — Widget Library phải cho phép Organization lựa chọn từng Widget được hiển thị hoặc bị ẩn trên Dashboard, Workspace, Ad…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2C-SC-C1-DEC-011/OPT-CLARIFY"
      ],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-011",
        "option_id": "OPT-CLARIFY"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-13-R003",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "1d4f02ed721297883d61ea683b475ba3159f9cb5c7c55c899ca7cb7b858b6b8b"
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
        "BRD-WS-13-R003-AC001",
        "BRD-WS-13-R003-AC002",
        "BRD-WS-13-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R003-O001",
      "obligation_text": "Widget Library phải cho phép Organization lựa chọn từng Widget được hiển thị hoặc bị ẩn trên Dashboard, Workspace, Admin Portal, Organization Portal và Customer Portal khi surface đó áp dụng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Widget Library phải cho phép Organization lựa chọn từng Widget được hiển thị hoặc bị ẩn trên Dashboard, Workspace, Admin Portal, Organization Portal và Customer Portal khi surface đó áp dụng.",
  "provenance": {
    "approved_decisions": [
      "P2C-SC-C1-DEC-011/OPT-CLARIFY"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-003",
    "previous_temporary_key": "TMP-BRD-WS-13-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Dashboard Widget",
    "source_context_sha256": "5ff050cde793f2ed33ece067c9283e4077eef7a36d130be15c3442c4584545de",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "1d4f02ed721297883d61ea683b475ba3159f9cb5c7c55c899ca7cb7b858b6b8b",
    "source_lines": "L6646-L6729",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R003"
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
  "stable_id": "BRD-WS-13-R003",
  "title": "Widget Library phải cho phép Organization lựa chọn từng Widget được hiển thị hoặc bị ẩn trên Dashboard, Workspace, Ad…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R004 — Drill-down phải tôn trọng Permission và Data Scope của User

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
      "requirement_id": "BRD-WS-13-R004",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "7b0061b52ecf933978543035339f40da23f67d12e9395985301719502dd6cbd4"
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
        "BRD-WS-13-R004-AC001",
        "BRD-WS-13-R004-AC002",
        "BRD-WS-13-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R004-O001",
      "obligation_text": "Drill-down phải tôn trọng Permission và Data Scope của User"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R004-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Drill-down phải tôn trọng Permission và Data Scope của User.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-004",
    "previous_temporary_key": "TMP-BRD-WS-13-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Drill-down",
    "source_context_sha256": "3880c11de55966be70dcb1d21e8a2a23d0847c538a4a026b3d56c5699efc4af4",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "7b0061b52ecf933978543035339f40da23f67d12e9395985301719502dd6cbd4",
    "source_lines": "L6731-L6845",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R004"
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
  "stable_id": "BRD-WS-13-R004",
  "title": "Drill-down phải tôn trọng Permission và Data Scope của User",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R005 — Kiến trúc mở để bổ sung thêm các KPI Scope mới trong các phiên bản sau

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-13-R005",
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
  "normative_statement": "Kiến trúc mở để bổ sung thêm các KPI Scope mới trong các phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-005",
    "previous_temporary_key": "TMP-BRD-WS-13-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. KPI Scope",
    "source_context_sha256": "f0f3819edd030b33bb1f88fd37e6a576e3faa2b243f7e3f38cb8a3e213d2716f",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "d088994229fcc25454331ed295bae26c305a2002a8412c188bbdb77be94f2977",
    "source_lines": "L6847-L6905",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R005"
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
  "stable_id": "BRD-WS-13-R005",
  "title": "Kiến trúc mở để bổ sung thêm các KPI Scope mới trong các phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R006 — Không bắt buộc toàn bộ Dashboard phải Real-time

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
      "requirement_id": "BRD-WS-13-R006",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "0ed8d00f0b0c376c465904c18df8d98a7340f966f2d2a48d7c893c76a4556bec"
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
        "BRD-WS-13-R006-AC001",
        "BRD-WS-13-R006-AC002",
        "BRD-WS-13-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R006-O001",
      "obligation_text": "Không bắt buộc toàn bộ Dashboard phải Real-time"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không bắt buộc toàn bộ Dashboard phải Real-time.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-006",
    "previous_temporary_key": "TMP-BRD-WS-13-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "14. Operational Intelligence",
    "source_context_sha256": "a5fbcedf5d23962d735091d5bd6b3b82cc7706167ef0fb5fbcad9c3adbc86883",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "0ed8d00f0b0c376c465904c18df8d98a7340f966f2d2a48d7c893c76a4556bec",
    "source_lines": "L6907-L6982",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R006"
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
  "stable_id": "BRD-WS-13-R006",
  "title": "Không bắt buộc toàn bộ Dashboard phải Real-time",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R007 — Các Capability trên được giữ chỗ cho các phiên bản sau

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-13-R007",
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
  "normative_statement": "Các Capability trên được giữ chỗ cho các phiên bản sau.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-007",
    "previous_temporary_key": "TMP-BRD-WS-13-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Business Intelligence",
    "source_context_sha256": "ca41807cf2074889e3c9c93950ff4a0277dc156495b8695b81d84a3ecef9c6e7",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "f7ca03d50ab7bf8dc7616efc08eed0f8655ae9f87656f22c47abf682f168c460",
    "source_lines": "L6984-L7044",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R007"
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
  "stable_id": "BRD-WS-13-R007",
  "title": "Các Capability trên được giữ chỗ cho các phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R008 — Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Currency

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
      "requirement_id": "BRD-WS-13-R008",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "e7fd13e28ea2896611e82927131ffbdf6980495cbd5cedbb0edb2496692fae11"
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
        "BRD-WS-13-R008-AC001",
        "BRD-WS-13-R008-AC002",
        "BRD-WS-13-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R008-O001",
      "obligation_text": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Currency"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R008 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R008-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R008-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R008 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Currency",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-008",
    "previous_temporary_key": "TMP-BRD-WS-13-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Multi Currency Reporting",
    "source_context_sha256": "03f5d16f5e49b899306ec9d117a0cb37bae6dcbc690304c5ff7b8bc0922a2c87",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "e7fd13e28ea2896611e82927131ffbdf6980495cbd5cedbb0edb2496692fae11",
    "source_lines": "L7046-L7154",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R008"
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
  "stable_id": "BRD-WS-13-R008",
  "title": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Currency",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R009 — Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Rate

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
      "requirement_id": "BRD-WS-13-R009",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "2ab09d5b5180f836d9c436f82cdec81c848265a63ef29a2d5408d23e338c26d4"
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
        "BRD-WS-13-R009-AC001",
        "BRD-WS-13-R009-AC002",
        "BRD-WS-13-R009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R009-O001",
      "obligation_text": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Rate"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R009 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R009 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R009 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R009-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R009-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R009 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Rate",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-009",
    "previous_temporary_key": "TMP-BRD-WS-13-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Multi Currency Reporting",
    "source_context_sha256": "03f5d16f5e49b899306ec9d117a0cb37bae6dcbc690304c5ff7b8bc0922a2c87",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "2ab09d5b5180f836d9c436f82cdec81c848265a63ef29a2d5408d23e338c26d4",
    "source_lines": "L7156-L7264",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R009"
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
  "stable_id": "BRD-WS-13-R009",
  "title": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Rate",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R010 — Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Conversion Rule

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
      "requirement_id": "BRD-WS-13-R010",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "9a5e11d3f38159654db2c4619ca990acb24d513d3337a8291300d5ee25cdec38"
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
        "BRD-WS-13-R010-AC001",
        "BRD-WS-13-R010-AC002",
        "BRD-WS-13-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R010-O001",
      "obligation_text": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Conversion Rule"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R010 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R010 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R010 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R010-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R010-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R010 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Conversion Rule",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-010",
    "previous_temporary_key": "TMP-BRD-WS-13-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Multi Currency Reporting",
    "source_context_sha256": "03f5d16f5e49b899306ec9d117a0cb37bae6dcbc690304c5ff7b8bc0922a2c87",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "9a5e11d3f38159654db2c4619ca990acb24d513d3337a8291300d5ee25cdec38",
    "source_lines": "L7266-L7374",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R010"
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
  "stable_id": "BRD-WS-13-R010",
  "title": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Conversion Rule",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R011 — Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Time

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
      "requirement_id": "BRD-WS-13-R011",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "479d6b375bc499849dfe181c90cc55455a75f1ac063d5fb291423f8dce1cc4ab"
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
        "BRD-WS-13-R011-AC001",
        "BRD-WS-13-R011-AC002",
        "BRD-WS-13-R011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R011-O001",
      "obligation_text": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Time"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R011 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R011 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R011 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R011-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R011-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R011 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Time",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-011",
    "previous_temporary_key": "TMP-BRD-WS-13-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Multi Currency Reporting",
    "source_context_sha256": "03f5d16f5e49b899306ec9d117a0cb37bae6dcbc690304c5ff7b8bc0922a2c87",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "479d6b375bc499849dfe181c90cc55455a75f1ac063d5fb291423f8dce1cc4ab",
    "source_lines": "L7376-L7484",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R011"
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
  "stable_id": "BRD-WS-13-R011",
  "title": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Time",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R012 — Dashboard luôn chuyển đổi đơn vị hiển thị theo cấu hình Localization của User

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
      "requirement_id": "BRD-WS-13-R012",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "1d5e557d0acde0579e57b65b47a9a65602585e8980a55dd5df05d0d52f56f108"
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
        "BRD-WS-13-R012-AC001",
        "BRD-WS-13-R012-AC002",
        "BRD-WS-13-R012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R012-O001",
      "obligation_text": "Dashboard luôn chuyển đổi đơn vị hiển thị theo cấu hình Localization của User"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R012 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R012-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R012-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R012 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dashboard luôn chuyển đổi đơn vị hiển thị theo cấu hình Localization của User.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-012",
    "previous_temporary_key": "TMP-BRD-WS-13-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Multi Currency Reporting",
    "source_context_sha256": "03f5d16f5e49b899306ec9d117a0cb37bae6dcbc690304c5ff7b8bc0922a2c87",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "1d5e557d0acde0579e57b65b47a9a65602585e8980a55dd5df05d0d52f56f108",
    "source_lines": "L7486-L7598",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R012"
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
  "stable_id": "BRD-WS-13-R012",
  "title": "Dashboard luôn chuyển đổi đơn vị hiển thị theo cấu hình Localization của User",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R013 — Report luôn đọc dữ liệu từ Snapshot

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Changing runtime data after Snapshot creation does not alter the report based on that Snapshot"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-13-R013.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                "source_type": "SOURCE_LITERAL",
                "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
              },
              "identifier": "BRD-WS-13-R013.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                "source_lines": "L472",
                "source_section": "19. Reporting Snapshot"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
            "source_lines": "L472",
            "source_section": "19. Reporting Snapshot"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-13-R013.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                "source_type": "SOURCE_LITERAL",
                "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
              },
              "identifier": "BRD-WS-13-R013.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                "source_lines": "L472",
                "source_section": "19. Reporting Snapshot"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
            "source_lines": "L472",
            "source_section": "19. Reporting Snapshot"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
            "source_type": "SOURCE_LITERAL",
            "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
          },
          "identifier": "BRD-WS-13-R013.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
            "source_lines": "L472",
            "source_section": "19. Reporting Snapshot"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
            "source_type": "SOURCE_LITERAL",
            "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
          },
          "identifier": "BRD-WS-13-R013.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
            "source_lines": "L472",
            "source_section": "19. Reporting Snapshot"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
            "source_type": "SOURCE_LITERAL",
            "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
          },
          "identifier": "BRD-WS-13-R013.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
            "source_lines": "L472",
            "source_section": "19. Reporting Snapshot"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
            "source_type": "SOURCE_LITERAL",
            "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
          },
          "identifier": "BRD-WS-13-R013.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
            "source_lines": "L472",
            "source_section": "19. Reporting Snapshot"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
            "source_type": "SOURCE_LITERAL",
            "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
          },
          "identifier": "BRD-WS-13-R013.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
            "source_lines": "L472",
            "source_section": "19. Reporting Snapshot"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-13-R013",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "The Report reads mutable transaction state directly"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "The Report reads from Snapshot"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
      "source_lines": "L472",
      "source_section": "19. Reporting Snapshot"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
          "source_type": "SOURCE_LITERAL",
          "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
        },
        "identifier": "BRD-WS-13-R013.BRD-WS-13-R013.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-13-R013.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-13.md",
          "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
          "source_lines": "L472",
          "source_section": "19. Reporting Snapshot"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-13-R013.BRD-WS-13-R013.BRD-WS-13-R013.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-13-R013.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.REPORT_ID",
        "FIELD.SNAPSHOT_ID",
        "FIELD.DATA_SOURCE_TYPE",
        "FIELD.RUNTIME_READ_COUNT",
        "FIELD.REPORT_RESULT"
      ],
      "producer": "BRD-WS-13-R013.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-13-R013.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.REPORT_ID",
        "FIELD.SNAPSHOT_ID",
        "FIELD.DATA_SOURCE_TYPE",
        "FIELD.RUNTIME_READ_COUNT",
        "FIELD.REPORT_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-13-R013.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-13-R013.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-13-R013.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-13-R013-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID",
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
              "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
              "source_type": "SOURCE_LITERAL",
              "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
            },
            "identifier": "BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
              "source_lines": "L472",
              "source_section": "19. Reporting Snapshot"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-13-R013.BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
              "source_type": "SOURCE_LITERAL",
              "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
            },
            "identifier": "BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
              "source_lines": "L472",
              "source_section": "19. Reporting Snapshot"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                        "BRD-WS-13-R013.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                      "source_type": "SOURCE_LITERAL",
                      "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
                    },
                    "identifier": "BRD-WS-13-R013.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-13.md",
                      "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                      "source_lines": "L472",
                      "source_section": "19. Reporting Snapshot"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                  "source_lines": "L472",
                  "source_section": "19. Reporting Snapshot"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-13-R013.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                      "source_type": "SOURCE_LITERAL",
                      "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
                    },
                    "identifier": "BRD-WS-13-R013.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-13.md",
                      "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                      "source_lines": "L472",
                      "source_section": "19. Reporting Snapshot"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                  "source_lines": "L472",
                  "source_section": "19. Reporting Snapshot"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                  "source_type": "SOURCE_LITERAL",
                  "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
                },
                "identifier": "BRD-WS-13-R013.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                  "source_lines": "L472",
                  "source_section": "19. Reporting Snapshot"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                  "source_type": "SOURCE_LITERAL",
                  "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
                },
                "identifier": "BRD-WS-13-R013.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                  "source_lines": "L472",
                  "source_section": "19. Reporting Snapshot"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                  "source_type": "SOURCE_LITERAL",
                  "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
                },
                "identifier": "BRD-WS-13-R013.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                  "source_lines": "L472",
                  "source_section": "19. Reporting Snapshot"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                  "source_type": "SOURCE_LITERAL",
                  "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
                },
                "identifier": "BRD-WS-13-R013.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                  "source_lines": "L472",
                  "source_section": "19. Reporting Snapshot"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                  "source_type": "SOURCE_LITERAL",
                  "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
                },
                "identifier": "BRD-WS-13-R013.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                  "source_lines": "L472",
                  "source_section": "19. Reporting Snapshot"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                  "source_type": "SOURCE_LITERAL",
                  "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
                },
                "identifier": "BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                  "source_lines": "L472",
                  "source_section": "19. Reporting Snapshot"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                  "source_type": "SOURCE_LITERAL",
                  "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
                },
                "identifier": "BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-13.md",
                  "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                  "source_lines": "L472",
                  "source_section": "19. Reporting Snapshot"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-13-R013.BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                "source_type": "SOURCE_LITERAL",
                "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
              },
              "identifier": "BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                "source_lines": "L472",
                "source_section": "19. Reporting Snapshot"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-13-R013.BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "BRD-WS-13-R013-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
              "source_type": "SOURCE_LITERAL",
              "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
            },
            "identifier": "BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-13.md",
              "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
              "source_lines": "L472",
              "source_section": "19. Reporting Snapshot"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BRD-WS-13-R013.BRD-WS-13-R013.BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                      "BRD-WS-13-R013.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                    "source_type": "SOURCE_LITERAL",
                    "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
                  },
                  "identifier": "BRD-WS-13-R013.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-13.md",
                    "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                    "source_lines": "L472",
                    "source_section": "19. Reporting Snapshot"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                "source_lines": "L472",
                "source_section": "19. Reporting Snapshot"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-WS-13-R013.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                    "source_type": "SOURCE_LITERAL",
                    "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
                  },
                  "identifier": "BRD-WS-13-R013.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-13.md",
                    "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                    "source_lines": "L472",
                    "source_section": "19. Reporting Snapshot"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                "source_lines": "L472",
                "source_section": "19. Reporting Snapshot"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                "source_type": "SOURCE_LITERAL",
                "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
              },
              "identifier": "BRD-WS-13-R013.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                "source_lines": "L472",
                "source_section": "19. Reporting Snapshot"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                "source_type": "SOURCE_LITERAL",
                "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
              },
              "identifier": "BRD-WS-13-R013.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                "source_lines": "L472",
                "source_section": "19. Reporting Snapshot"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                "source_type": "SOURCE_LITERAL",
                "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
              },
              "identifier": "BRD-WS-13-R013.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                "source_lines": "L472",
                "source_section": "19. Reporting Snapshot"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                "source_type": "SOURCE_LITERAL",
                "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
              },
              "identifier": "BRD-WS-13-R013.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                "source_lines": "L472",
                "source_section": "19. Reporting Snapshot"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
                "source_type": "SOURCE_LITERAL",
                "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
              },
              "identifier": "BRD-WS-13-R013.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-13.md",
                "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
                "source_lines": "L472",
                "source_section": "19. Reporting Snapshot"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.BRD-WS-13-R013.BRD-WS-13-R013.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "Changing runtime data after Snapshot creation does not alter the report based on that Snapshot"
      ],
      "contract_ast_sha256": "1fac7d5e909a8d53f6160a2ec74913fddc04203476e4f3c4f0140a14e5d58f82",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-13-R013",
      "criticality": "HIGH",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-13.md#19. Reporting Snapshot",
            "source_type": "SOURCE_LITERAL",
            "version": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2"
          },
          "identifier": "BRD-WS-13-R013.BRD-WS-13-R013.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-13-R013.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-13.md",
            "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
            "source_lines": "L472",
            "source_section": "19. Reporting Snapshot"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-13-R013.BRD-WS-13-R013.BRD-WS-13-R013.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-13-R013.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.REPORT_ID",
          "FIELD.SNAPSHOT_ID",
          "FIELD.DATA_SOURCE_TYPE",
          "FIELD.RUNTIME_READ_COUNT",
          "FIELD.REPORT_RESULT"
        ],
        "producer": "BRD-WS-13-R013.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-13-R013.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.REPORT_ID",
          "FIELD.SNAPSHOT_ID",
          "FIELD.DATA_SOURCE_TYPE",
          "FIELD.RUNTIME_READ_COUNT",
          "FIELD.REPORT_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-13-R013.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-13-R013.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-13-R013.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-0A6516AD338CF2DF0919",
        "P2C-C4-FX-D4AB10D135A9A865E806",
        "P2C-C4-FX-CD429EE6642FB462AC5A"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "The Report reads mutable transaction state directly"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-13-R013-O001",
          "obligation_text": "Report luôn đọc dữ liệu từ Snapshot"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-13-R013.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-13-R013-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "The Report reads from Snapshot"
      ],
      "preconditions": [
        "An applicable Snapshot exists"
      ],
      "prohibitions": [
        "The Report reads mutable transaction state directly"
      ],
      "requirement_id": "BRD-WS-13-R013",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-13.md",
        "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
        "source_lines": "L472",
        "source_section": "19. Reporting Snapshot"
      },
      "source_statement": "Report luôn đọc dữ liệu từ Snapshot.",
      "surrounding_source_context": "### BRD-WS-13-R013 — Report luôn đọc dữ liệu từ Snapshot"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-13-R013",
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
        "BRD-WS-13-R013-AC001",
        "BRD-WS-13-R013-AC002",
        "BRD-WS-13-R013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R013-O001",
      "obligation_text": "Report luôn đọc dữ liệu từ Snapshot"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report luôn đọc dữ liệu từ Snapshot.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-013",
    "previous_temporary_key": "TMP-BRD-WS-13-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Reporting Snapshot",
    "source_context_sha256": "249ed3d5f4ce9a4f8ec5ebc8323ba8cf46130e41018e4f119b561e8f889c3bd7",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "fe7cddff01e4f4997f722c6665cfa3394ac657017a983dd48f14d70e02b782d2",
    "source_lines": "L7600-L8949",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R013"
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
  "stable_id": "BRD-WS-13-R013",
  "title": "Report luôn đọc dữ liệu từ Snapshot",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R014 — Customer Analytics không được chia sẻ giữa các Organization

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
      "requirement_id": "BRD-WS-13-R014",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "fd1f40de80e12a7c978f5bae58bf1eff3a2470b38de66ef930b49f0d0eefe9cc"
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
        "BRD-WS-13-R014-AC001",
        "BRD-WS-13-R014-AC002",
        "BRD-WS-13-R014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R014-O001",
      "obligation_text": "Customer Analytics không được chia sẻ giữa các Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Analytics không được chia sẻ giữa các Organization.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-014",
    "previous_temporary_key": "TMP-BRD-WS-13-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Customer Analytics",
    "source_context_sha256": "6be481274936098d942a55f4ee80908074b96fd2eb0306aef4b48993dff1edf1",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "fd1f40de80e12a7c978f5bae58bf1eff3a2470b38de66ef930b49f0d0eefe9cc",
    "source_lines": "L8951-L9030",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R014"
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
  "stable_id": "BRD-WS-13-R014",
  "title": "Customer Analytics không được chia sẻ giữa các Organization",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R015 — Customer Analytics phải tuân thủ Relationship Policy và Data Permission

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
      "requirement_id": "BRD-WS-13-R015",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "76d8aed90ccee7528b495d7c941f2b634c98d05e40334032ab6bbf199cf5739b"
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
        "BRD-WS-13-R015-AC001",
        "BRD-WS-13-R015-AC002",
        "BRD-WS-13-R015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R015-O001",
      "obligation_text": "Customer Analytics phải tuân thủ Relationship Policy và Data Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R015-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R015 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R015 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R015-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R015-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R015 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Analytics phải tuân thủ Relationship Policy và Data Permission.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-13.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "21. Customer Analytics"
    },
    "deterministic_transformation": "RESTORE_CUSTOMER_ANALYTICS_SUBJECT",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-015",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-13-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Customer Analytics",
    "source_context_sha256": "6be481274936098d942a55f4ee80908074b96fd2eb0306aef4b48993dff1edf1",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "76d8aed90ccee7528b495d7c941f2b634c98d05e40334032ab6bbf199cf5739b",
    "source_fingerprint_before_c3": "0b55aa2fcb4e14db8ca3dfbf2f6ef84be565c50726b8e7eefda7d8002633231c",
    "source_lines": "L9032-L9163",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-13.md",
      "lines": "L542",
      "section": "21. Customer Analytics"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R015"
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
  "stable_id": "BRD-WS-13-R015",
  "title": "Customer Analytics phải tuân thủ Relationship Policy và Data Permission",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R016 — Organization chỉ được xem Benchmark của chính Organization đó

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
      "requirement_id": "BRD-WS-13-R016",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "325b94a4c18e49d5cf8bd64150f5eb0ae7ff573b93dc8450f326286eae241f24"
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
        "BRD-WS-13-R016-AC001",
        "BRD-WS-13-R016-AC002",
        "BRD-WS-13-R016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R016-O001",
      "obligation_text": "Organization chỉ được xem Benchmark của chính Organization đó"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization chỉ được xem Benchmark của chính Organization đó.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-016",
    "previous_temporary_key": "TMP-BRD-WS-13-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Benchmark",
    "source_context_sha256": "da9055aa97d2ab0a13f035864f584f339cacfb32c37be032bec80313de59935d",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "325b94a4c18e49d5cf8bd64150f5eb0ae7ff573b93dc8450f326286eae241f24",
    "source_lines": "L9165-L9240",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R016"
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
  "stable_id": "BRD-WS-13-R016",
  "title": "Organization chỉ được xem Benchmark của chính Organization đó",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R017 — Không được phép xem: - Revenue của Organization khác

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
      "requirement_id": "BRD-WS-13-R017",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "bd8d39b845e89346e437a6d90b3c0862c6c645f3b0491d4721a24d63b0aa7a07"
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
        "BRD-WS-13-R017-AC001",
        "BRD-WS-13-R017-AC002",
        "BRD-WS-13-R017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R017-O001",
      "obligation_text": "Không được phép xem: - Revenue của Organization khác"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không được phép xem: - Revenue của Organization khác",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-017",
    "previous_temporary_key": "TMP-BRD-WS-13-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Benchmark",
    "source_context_sha256": "da9055aa97d2ab0a13f035864f584f339cacfb32c37be032bec80313de59935d",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "bd8d39b845e89346e437a6d90b3c0862c6c645f3b0491d4721a24d63b0aa7a07",
    "source_lines": "L9242-L9317",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R017"
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
  "stable_id": "BRD-WS-13-R017",
  "title": "Không được phép xem: - Revenue của Organization khác",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R018 — Không được phép xem: - KPI của Organization khác

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
      "requirement_id": "BRD-WS-13-R018",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "64672b71d70a837b25ec5649ee0d98719ac8a7c79af7ee58ac5ffd654133f02d"
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
        "BRD-WS-13-R018-AC001",
        "BRD-WS-13-R018-AC002",
        "BRD-WS-13-R018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R018-O001",
      "obligation_text": "Không được phép xem: - KPI của Organization khác"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không được phép xem: - KPI của Organization khác",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-018",
    "previous_temporary_key": "TMP-BRD-WS-13-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Benchmark",
    "source_context_sha256": "da9055aa97d2ab0a13f035864f584f339cacfb32c37be032bec80313de59935d",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "64672b71d70a837b25ec5649ee0d98719ac8a7c79af7ee58ac5ffd654133f02d",
    "source_lines": "L9319-L9394",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R018"
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
  "stable_id": "BRD-WS-13-R018",
  "title": "Không được phép xem: - KPI của Organization khác",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R019 — Không được phép xem: - Customer của Organization khác

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
      "requirement_id": "BRD-WS-13-R019",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "db82984a7476912a66873bcc3de9381250ad30c57712895bd98a820d96912b13"
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
        "BRD-WS-13-R019-AC001",
        "BRD-WS-13-R019-AC002",
        "BRD-WS-13-R019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R019-O001",
      "obligation_text": "Không được phép xem: - Customer của Organization khác"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không được phép xem: - Customer của Organization khác",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-019",
    "previous_temporary_key": "TMP-BRD-WS-13-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Benchmark",
    "source_context_sha256": "da9055aa97d2ab0a13f035864f584f339cacfb32c37be032bec80313de59935d",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "db82984a7476912a66873bcc3de9381250ad30c57712895bd98a820d96912b13",
    "source_lines": "L9396-L9475",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R019"
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
  "stable_id": "BRD-WS-13-R019",
  "title": "Không được phép xem: - Customer của Organization khác",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R020 — Kiến trúc mở để hỗ trợ Industry Benchmark trong các phiên bản sau

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-13-R020",
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
  "normative_statement": "Kiến trúc mở để hỗ trợ Industry Benchmark trong các phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-020",
    "previous_temporary_key": "TMP-BRD-WS-13-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Benchmark",
    "source_context_sha256": "da9055aa97d2ab0a13f035864f584f339cacfb32c37be032bec80313de59935d",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "4d9634751d1e9ca35a4643b6518302740e2484f670a0dc81545b5dd042353991",
    "source_lines": "L9477-L9535",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R020"
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
  "stable_id": "BRD-WS-13-R020",
  "title": "Kiến trúc mở để hỗ trợ Industry Benchmark trong các phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R021 — Organization có thể lựa chọn Widget cần hiển thị

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-012",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-13-R021",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "10309aafa1d3b838ff518946bceecbd79e3a6c28a4a3053719e9eabae92cb4f0"
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
        "BRD-WS-13-R021-AC001",
        "BRD-WS-13-R021-AC002",
        "BRD-WS-13-R021-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R021-O001",
      "obligation_text": "Organization có thể lựa chọn Widget cần hiển thị"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization có thể lựa chọn Widget cần hiển thị.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-021",
    "previous_temporary_key": "TMP-BRD-WS-13-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Widget Library",
    "source_context_sha256": "23adaa9026073a8156aa394e9d4951b65efd1f0759ace24911947babf5d3ecd8",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "10309aafa1d3b838ff518946bceecbd79e3a6c28a4a3053719e9eabae92cb4f0",
    "source_lines": "L9537-L9616",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R021"
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
  "stable_id": "BRD-WS-13-R021",
  "title": "Organization có thể lựa chọn Widget cần hiển thị",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R022 — Kiến trúc giữ chỗ cho AI Insight ở phiên bản sau

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-13-R022",
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
  "normative_statement": "Kiến trúc giữ chỗ cho AI Insight ở phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-022",
    "previous_temporary_key": "TMP-BRD-WS-13-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. Operational Insight",
    "source_context_sha256": "e14305f76ca4b6c0410aa695e886b2cab72e8c679002d56f9a33141eb435ad63",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "d15fc5e9461cfb271d6921b0fdf45b6b109e4f444fefb717e20be1f6d6eccd62",
    "source_lines": "L9618-L9676",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R022"
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
  "stable_id": "BRD-WS-13-R022",
  "title": "Kiến trúc giữ chỗ cho AI Insight ở phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R023 — Report không được Hard-code

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
      "requirement_id": "BRD-WS-13-R023",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "d136a60a74970b21b04fe6850928023aeb6599d022dbb716781e22bbb5c858e2"
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
        "BRD-WS-13-R023-AC001",
        "BRD-WS-13-R023-AC002",
        "BRD-WS-13-R023-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R023-O001",
      "obligation_text": "Report không được Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report không được Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-023",
    "previous_temporary_key": "TMP-BRD-WS-13-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Report as Configuration",
    "source_context_sha256": "777a30261a8a3c369fdd2cee0b010b7d2dcf160636dfd44498377da04014702e",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "d136a60a74970b21b04fe6850928023aeb6599d022dbb716781e22bbb5c858e2",
    "source_lines": "L9678-L9753",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R023"
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
  "stable_id": "BRD-WS-13-R023",
  "title": "Report không được Hard-code",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R024 —  Landing Page (phiên bản sau)

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-13-R024",
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
  "normative_statement": "- Landing Page (phiên bản sau)",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-024",
    "previous_temporary_key": "TMP-BRD-WS-13-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Widget as Capability",
    "source_context_sha256": "a591bfbca16337e050d804aa0bd2410901039358ecea3e5469d76181e94f0d55",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "d87fb0e7a878f58e697e80d5361b9244eba0346d1e1b219c6a51ef1899b6e1fc",
    "source_lines": "L9755-L9813",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R024"
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
  "stable_id": "BRD-WS-13-R024",
  "title": " Landing Page (phiên bản sau)",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R025 —  Mobile App (phiên bản sau)

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-13-R025",
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
  "normative_statement": "- Mobile App (phiên bản sau)",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-025",
    "previous_temporary_key": "TMP-BRD-WS-13-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Widget as Capability",
    "source_context_sha256": "a591bfbca16337e050d804aa0bd2410901039358ecea3e5469d76181e94f0d55",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "b394f52950410f92fa31c04c5deace716f421b77c133bde408ae75fe4076c4d0",
    "source_lines": "L9815-L9873",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R025"
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
  "stable_id": "BRD-WS-13-R025",
  "title": " Mobile App (phiên bản sau)",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R026 — Report là Business Object độc lập

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
      "requirement_id": "BRD-WS-13-R026",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "a1268661dba004b6b553bda5d6a580ad68d1a83a6032e121dac9ebb0895d03da"
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
        "BRD-WS-13-R026-AC001",
        "BRD-WS-13-R026-AC002",
        "BRD-WS-13-R026-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R026-O001",
      "obligation_text": "Report là Business Object độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report là Business Object độc lập.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-004",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R026",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Report Model",
    "source_context_sha256": "6f73245c294739f9ff85868c2f0b56a1e0564d82247e21cc390fc671549063d1",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "a1268661dba004b6b553bda5d6a580ad68d1a83a6032e121dac9ebb0895d03da",
    "source_fingerprint_before_c3": "a1268661dba004b6b553bda5d6a580ad68d1a83a6032e121dac9ebb0895d03da",
    "source_lines": "L9875-L9967",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R026"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-004"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-004"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R026",
  "title": "Report là Business Object độc lập",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R027 — System Report chỉ dành cho YSim Internal

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
      "requirement_id": "BRD-WS-13-R027",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "2ca22cc724994c2e7be9ecda78b3ec59ceaf3e62e57f26f6e44ef3ca328485c1"
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
        "BRD-WS-13-R027-AC001",
        "BRD-WS-13-R027-AC002",
        "BRD-WS-13-R027-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R027-O001",
      "obligation_text": "System Report chỉ dành cho YSim Internal"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "System Report chỉ dành cho YSim Internal.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-004",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R027",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Report Model",
    "source_context_sha256": "6f73245c294739f9ff85868c2f0b56a1e0564d82247e21cc390fc671549063d1",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "2ca22cc724994c2e7be9ecda78b3ec59ceaf3e62e57f26f6e44ef3ca328485c1",
    "source_fingerprint_before_c3": "2ca22cc724994c2e7be9ecda78b3ec59ceaf3e62e57f26f6e44ef3ca328485c1",
    "source_lines": "L9969-L10061",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R027"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-004"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-004"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R027",
  "title": "System Report chỉ dành cho YSim Internal",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R028 — Business Report hỗ trợ kế thừa: YSim ↓ Parent Organization ↓ Organization Override

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
      "requirement_id": "BRD-WS-13-R028",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "febe6fadb5f15fdaa856eb9b60bdd4eee7557b68c9291a8f47f6f48762b5dba3"
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
        "BRD-WS-13-R028-AC001",
        "BRD-WS-13-R028-AC002",
        "BRD-WS-13-R028-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R028-O001",
      "obligation_text": "Business Report hỗ trợ kế thừa: YSim ↓ Parent Organization ↓ Organization Override"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Report hỗ trợ kế thừa: YSim ↓ Parent Organization ↓ Organization Override.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-004",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R028",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Report Model",
    "source_context_sha256": "6f73245c294739f9ff85868c2f0b56a1e0564d82247e21cc390fc671549063d1",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "febe6fadb5f15fdaa856eb9b60bdd4eee7557b68c9291a8f47f6f48762b5dba3",
    "source_fingerprint_before_c3": "febe6fadb5f15fdaa856eb9b60bdd4eee7557b68c9291a8f47f6f48762b5dba3",
    "source_lines": "L10063-L10155",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R028"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-004"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-004"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R028",
  "title": "Business Report hỗ trợ kế thừa: YSim ↓ Parent Organization ↓ Organization Override",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R029 — Report Permission được xác định theo: Organization

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
      "requirement_id": "BRD-WS-13-R029",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "1340362fd1eb0c085fcc0eba37f3261041f4b5d1c2e288e93adf80f647a65a84"
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
        "BRD-WS-13-R029-AC001",
        "BRD-WS-13-R029-AC002",
        "BRD-WS-13-R029-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R029-O001",
      "obligation_text": "Report Permission được xác định theo: Organization"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R029-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R029 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R029 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R029-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R029-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R029 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report Permission được xác định theo: Organization.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-013",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R029",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-013",
    "source_context_sha256": "c2d9e76299e296e5c0f8f686f969d8b53c51bf163468c0eaf194a891f82dad3f",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "1340362fd1eb0c085fcc0eba37f3261041f4b5d1c2e288e93adf80f647a65a84",
    "source_fingerprint_before_c3": "1340362fd1eb0c085fcc0eba37f3261041f4b5d1c2e288e93adf80f647a65a84",
    "source_lines": "L10157-L10284",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R029"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-013"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-013"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R029",
  "title": "Report Permission được xác định theo: Organization",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R030 — Report Permission được xác định theo: Role

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
      "requirement_id": "BRD-WS-13-R030",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "df7246408b2fb68ca5d54e82022f9828627d404b18a17539dda3ea2e6457da5f"
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
        "BRD-WS-13-R030-AC001",
        "BRD-WS-13-R030-AC002",
        "BRD-WS-13-R030-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R030-O001",
      "obligation_text": "Report Permission được xác định theo: Role"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R030-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R030 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R030 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R030-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R030-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R030 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report Permission được xác định theo: Role.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-013",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R030",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-013",
    "source_context_sha256": "c2d9e76299e296e5c0f8f686f969d8b53c51bf163468c0eaf194a891f82dad3f",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "df7246408b2fb68ca5d54e82022f9828627d404b18a17539dda3ea2e6457da5f",
    "source_fingerprint_before_c3": "df7246408b2fb68ca5d54e82022f9828627d404b18a17539dda3ea2e6457da5f",
    "source_lines": "L10286-L10413",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R030"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-013"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-013"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R030",
  "title": "Report Permission được xác định theo: Role",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R031 — Report Permission được xác định theo: Permission

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
      "requirement_id": "BRD-WS-13-R031",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "0cda030a1a6e93b0fac963761db783632a741a0890ec328644c5c7d21c866d7f"
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
        "BRD-WS-13-R031-AC001",
        "BRD-WS-13-R031-AC002",
        "BRD-WS-13-R031-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R031-O001",
      "obligation_text": "Report Permission được xác định theo: Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R031-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R031 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R031 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R031-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R031-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R031 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report Permission được xác định theo: Permission.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-013",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R031",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-013",
    "source_context_sha256": "c2d9e76299e296e5c0f8f686f969d8b53c51bf163468c0eaf194a891f82dad3f",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "0cda030a1a6e93b0fac963761db783632a741a0890ec328644c5c7d21c866d7f",
    "source_fingerprint_before_c3": "0cda030a1a6e93b0fac963761db783632a741a0890ec328644c5c7d21c866d7f",
    "source_lines": "L10415-L10542",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R031"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-013"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-013"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R031",
  "title": "Report Permission được xác định theo: Permission",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R032 — Report Permission được xác định theo: Data Scope

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
      "requirement_id": "BRD-WS-13-R032",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "0a912fdccdce2b7e642e4fafa984d56714927b8d184f92c1ba109149e762358d"
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
        "BRD-WS-13-R032-AC001",
        "BRD-WS-13-R032-AC002",
        "BRD-WS-13-R032-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R032-O001",
      "obligation_text": "Report Permission được xác định theo: Data Scope"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R032-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R032 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R032 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R032-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R032-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R032 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report Permission được xác định theo: Data Scope.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-013",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R032",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-013",
    "source_context_sha256": "c2d9e76299e296e5c0f8f686f969d8b53c51bf163468c0eaf194a891f82dad3f",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "0a912fdccdce2b7e642e4fafa984d56714927b8d184f92c1ba109149e762358d",
    "source_fingerprint_before_c3": "0a912fdccdce2b7e642e4fafa984d56714927b8d184f92c1ba109149e762358d",
    "source_lines": "L10544-L10671",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R032"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-013"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-013"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R032",
  "title": "Report Permission được xác định theo: Data Scope",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R033 — Report Permission được xác định theo: Support Policy Có thể Mask dữ liệu theo Permission

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
      "requirement_id": "BRD-WS-13-R033",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "c3eb2aa37b3c62a5043b466a00d982c6c665c25d0d81294d8f110ad07fe6f757"
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
        "BRD-WS-13-R033-AC001",
        "BRD-WS-13-R033-AC002",
        "BRD-WS-13-R033-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R033-O001",
      "obligation_text": "Report Permission được xác định theo: Support Policy Có thể Mask dữ liệu theo Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R033-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R033 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R033 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R033-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-13-R033-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-13-R033 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report Permission được xác định theo: Support Policy Có thể Mask dữ liệu theo Permission.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-013",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R033",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-013",
    "source_context_sha256": "c2d9e76299e296e5c0f8f686f969d8b53c51bf163468c0eaf194a891f82dad3f",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "c3eb2aa37b3c62a5043b466a00d982c6c665c25d0d81294d8f110ad07fe6f757",
    "source_fingerprint_before_c3": "c3eb2aa37b3c62a5043b466a00d982c6c665c25d0d81294d8f110ad07fe6f757",
    "source_lines": "L10673-L10800",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R033"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-013"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-013"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R033",
  "title": "Report Permission được xác định theo: Support Policy Có thể Mask dữ liệu theo Permission",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R034 — Insight là Business Object

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
      "requirement_id": "BRD-WS-13-R034",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "0ca817ca6dd600dc294c8fa5d0181cef1d9da77675eb267a714f22fb5a2d25ad"
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
        "BRD-WS-13-R034-AC001",
        "BRD-WS-13-R034-AC002",
        "BRD-WS-13-R034-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R034-O001",
      "obligation_text": "Insight là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Insight là Business Object.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-020",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R034",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. Operational Insight",
    "source_context_sha256": "e14305f76ca4b6c0410aa695e886b2cab72e8c679002d56f9a33141eb435ad63",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "0ca817ca6dd600dc294c8fa5d0181cef1d9da77675eb267a714f22fb5a2d25ad",
    "source_fingerprint_before_c3": "0ca817ca6dd600dc294c8fa5d0181cef1d9da77675eb267a714f22fb5a2d25ad",
    "source_lines": "L10802-L10894",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R034"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-020"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-020"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R034",
  "title": "Insight là Business Object",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R035 — Insight được sinh từ Rule Engine và Analytics

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
      "requirement_id": "BRD-WS-13-R035",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "b1f89198235137a11335eac3baa67a4c156100c2890f7092cf7f0748dce1b145"
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
        "BRD-WS-13-R035-AC001",
        "BRD-WS-13-R035-AC002",
        "BRD-WS-13-R035-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R035-O001",
      "obligation_text": "Insight được sinh từ Rule Engine và Analytics"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Insight được sinh từ Rule Engine và Analytics.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-020",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R035",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. Operational Insight",
    "source_context_sha256": "e14305f76ca4b6c0410aa695e886b2cab72e8c679002d56f9a33141eb435ad63",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "b1f89198235137a11335eac3baa67a4c156100c2890f7092cf7f0748dce1b145",
    "source_fingerprint_before_c3": "b1f89198235137a11335eac3baa67a4c156100c2890f7092cf7f0748dce1b145",
    "source_lines": "L10896-L10988",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R035"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-020"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-020"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R035",
  "title": "Insight được sinh từ Rule Engine và Analytics",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R036 — Version 2 chưa sử dụng AI

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-13-R036",
    "scope_status": "FUTURE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "This record is not an active canonical atomic v2.3 acceptance unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version 2 chưa sử dụng AI.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-020",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R036",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. Operational Insight",
    "source_context_sha256": "e14305f76ca4b6c0410aa695e886b2cab72e8c679002d56f9a33141eb435ad63",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "97102a3fa24e5a2dffc9133882b60178e3b05cbd9bf5b8050c2d3e16c3c78a95",
    "source_fingerprint_before_c3": "97102a3fa24e5a2dffc9133882b60178e3b05cbd9bf5b8050c2d3e16c3c78a95",
    "source_lines": "L10990-L11063",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R036"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-020"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-020"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "FUTURE",
  "stable_id": "BRD-WS-13-R036",
  "title": "Version 2 chưa sử dụng AI",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R037 — Widget là Platform Capability

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
      "requirement_id": "BRD-WS-13-R037",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "738f60244c9e40816b03abd8c755a0a5591e10d00dd04cafd62c9c2900198740"
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
        "BRD-WS-13-R037-AC001",
        "BRD-WS-13-R037-AC002",
        "BRD-WS-13-R037-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R037-O001",
      "obligation_text": "Widget là Platform Capability"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Widget là Platform Capability.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-005",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-13-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R037",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Widget as Capability",
    "source_context_sha256": "a591bfbca16337e050d804aa0bd2410901039358ecea3e5469d76181e94f0d55",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "738f60244c9e40816b03abd8c755a0a5591e10d00dd04cafd62c9c2900198740",
    "source_fingerprint_before_c3": "738f60244c9e40816b03abd8c755a0a5591e10d00dd04cafd62c9c2900198740",
    "source_lines": "L11065-L11159",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R037"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-13-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-13-003"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R037",
  "title": "Widget là Platform Capability",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R038 — Widget không thuộc Dashboard

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
      "requirement_id": "BRD-WS-13-R038",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "8249d5c211aba641abedd71a44579cf0af02f36880140c639837c3429a13f60a"
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
        "BRD-WS-13-R038-AC001",
        "BRD-WS-13-R038-AC002",
        "BRD-WS-13-R038-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R038-O001",
      "obligation_text": "Widget không thuộc Dashboard"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Widget không thuộc Dashboard.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-005",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-13-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R038",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Widget as Capability",
    "source_context_sha256": "a591bfbca16337e050d804aa0bd2410901039358ecea3e5469d76181e94f0d55",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "8249d5c211aba641abedd71a44579cf0af02f36880140c639837c3429a13f60a",
    "source_fingerprint_before_c3": "8249d5c211aba641abedd71a44579cf0af02f36880140c639837c3429a13f60a",
    "source_lines": "L11161-L11255",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R038"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-13-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-13-003"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R038",
  "title": "Widget không thuộc Dashboard",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R039 — Một Widget có thể tái sử dụng trên nhiều Portal và Workspace

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
      "requirement_id": "BRD-WS-13-R039",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "bbe80660850d031cb0f863bde14618368fe6ef398aae1f9fa134e4124478e95e"
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
        "BRD-WS-13-R039-AC001",
        "BRD-WS-13-R039-AC002",
        "BRD-WS-13-R039-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R039-O001",
      "obligation_text": "Một Widget có thể tái sử dụng trên nhiều Portal và Workspace"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Widget có thể tái sử dụng trên nhiều Portal và Workspace.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-005",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-13-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R039",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Widget as Capability",
    "source_context_sha256": "a591bfbca16337e050d804aa0bd2410901039358ecea3e5469d76181e94f0d55",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "bbe80660850d031cb0f863bde14618368fe6ef398aae1f9fa134e4124478e95e",
    "source_fingerprint_before_c3": "bbe80660850d031cb0f863bde14618368fe6ef398aae1f9fa134e4124478e95e",
    "source_lines": "L11257-L11351",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R039"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-13-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-13-003"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R039",
  "title": "Một Widget có thể tái sử dụng trên nhiều Portal và Workspace",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R040 — Alert Rule được cấu hình hoàn toàn

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
      "requirement_id": "BRD-WS-13-R040",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "ee6697476ab74dcdaa241ea3cbac958be3bff9d6dd22ac41ecef43b25173eeab"
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
        "BRD-WS-13-R040-AC001",
        "BRD-WS-13-R040-AC002",
        "BRD-WS-13-R040-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R040-O001",
      "obligation_text": "Alert Rule được cấu hình hoàn toàn"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Alert Rule được cấu hình hoàn toàn.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-13-005",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R040",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-13-005",
    "source_context_sha256": "c92e19faf0c58044dca1cd2ba8269e199979dc09796aa3d56233483760a975f7",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "ee6697476ab74dcdaa241ea3cbac958be3bff9d6dd22ac41ecef43b25173eeab",
    "source_fingerprint_before_c3": "ee6697476ab74dcdaa241ea3cbac958be3bff9d6dd22ac41ecef43b25173eeab",
    "source_lines": "L11353-L11445",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R040"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-13-005"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-13-005"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R040",
  "title": "Alert Rule được cấu hình hoàn toàn",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R041 — Alert có thể Trigger Notification, Workflow hoặc Business Action

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
      "requirement_id": "BRD-WS-13-R041",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "0b6f7a48637c40b378ecaf9a764c29d1b4a74b38421da91d2909850636495783"
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
        "BRD-WS-13-R041-AC001",
        "BRD-WS-13-R041-AC002",
        "BRD-WS-13-R041-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R041-O001",
      "obligation_text": "Alert có thể Trigger Notification, Workflow hoặc Business Action"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Alert có thể Trigger Notification, Workflow hoặc Business Action.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-13-005",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R041",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-13-005",
    "source_context_sha256": "c92e19faf0c58044dca1cd2ba8269e199979dc09796aa3d56233483760a975f7",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "0b6f7a48637c40b378ecaf9a764c29d1b4a74b38421da91d2909850636495783",
    "source_fingerprint_before_c3": "0b6f7a48637c40b378ecaf9a764c29d1b4a74b38421da91d2909850636495783",
    "source_lines": "L11447-L11539",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R041"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-13-005"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-13-005"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R041",
  "title": "Alert có thể Trigger Notification, Workflow hoặc Business Action",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R042 — Không Hard-code

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
      "requirement_id": "BRD-WS-13-R042",
      "source_document": "docs/BRD/BRD-WS-13.md",
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
        "BRD-WS-13-R042-AC001",
        "BRD-WS-13-R042-AC002",
        "BRD-WS-13-R042-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R042-O001",
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
    "derived_from_parent": "EP-13-005",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R042",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-13-005",
    "source_context_sha256": "c92e19faf0c58044dca1cd2ba8269e199979dc09796aa3d56233483760a975f7",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "4a4f9fc70196c62582583bd1f5a465fcfd49191969988f4db3f00452e0acf501",
    "source_fingerprint_before_c3": "4a4f9fc70196c62582583bd1f5a465fcfd49191969988f4db3f00452e0acf501",
    "source_lines": "L11541-L11633",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R042"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-13-005"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-13-005"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R042",
  "title": "Không Hard-code",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R043 — Các KPI group và measurement standard bắt buộc của v2.3 phải được định nghĩa và versioning

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
      "requirement_id": "BRD-WS-13-R043",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "93d15dd352746ed3559e418c2d72dfe6ef8c31b335ad73fa60277761b50ca2c3"
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
        "BRD-WS-13-R043-AC001",
        "BRD-WS-13-R043-AC002",
        "BRD-WS-13-R043-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R043-O001",
      "obligation_text": "Các KPI group và measurement standard bắt buộc của v2.3 phải được định nghĩa và versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Các KPI group và measurement standard bắt buộc của v2.3 phải được định nghĩa và versioning.",
  "provenance": {
    "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R043",
    "phase_2c_c3_actions": [
      "C3_APPROVED_DECISION_ATOMIC_SPLIT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. KPI",
    "source_context_sha256": "85344345dc19bcf0ae9030dce66f928f0fb4827b426c021d0e9d60c273f65f67",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "93d15dd352746ed3559e418c2d72dfe6ef8c31b335ad73fa60277761b50ca2c3",
    "source_fingerprint_before_c3": "93d15dd352746ed3559e418c2d72dfe6ef8c31b335ad73fa60277761b50ca2c3",
    "source_lines": "L11635-L11727",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R043"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-003"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R043",
  "title": "Các KPI group và measurement standard bắt buộc của v2.3 phải được định nghĩa và versioning",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R044 — KPI Definition phải được cấu hình bằng governed configuration

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
      "requirement_id": "BRD-WS-13-R044",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "fa8f9a9f8587877816790460ebc17d7100e6be4f31c1faa977a4dfe4339af3c9"
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
        "BRD-WS-13-R044-AC001",
        "BRD-WS-13-R044-AC002",
        "BRD-WS-13-R044-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R044-O001",
      "obligation_text": "KPI Definition phải được cấu hình bằng governed configuration"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "KPI Definition phải được cấu hình bằng governed configuration.",
  "provenance": {
    "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R044",
    "phase_2c_c3_actions": [
      "C3_APPROVED_DECISION_ATOMIC_SPLIT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. KPI",
    "source_context_sha256": "85344345dc19bcf0ae9030dce66f928f0fb4827b426c021d0e9d60c273f65f67",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "fa8f9a9f8587877816790460ebc17d7100e6be4f31c1faa977a4dfe4339af3c9",
    "source_fingerprint_before_c3": "fa8f9a9f8587877816790460ebc17d7100e6be4f31c1faa977a4dfe4339af3c9",
    "source_lines": "L11729-L11821",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R044"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-003"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R044",
  "title": "KPI Definition phải được cấu hình bằng governed configuration",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R045 — KPI group và measurement standard mới phải có thể được bổ sung bằng governed configuration mà kh…

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
      "requirement_id": "BRD-WS-13-R045",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "1b461e475bde1ca9738cdd5493efe31b4f9dde50d8dfda3ae72a7512edadf435"
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
        "BRD-WS-13-R045-AC001",
        "BRD-WS-13-R045-AC002",
        "BRD-WS-13-R045-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R045-O001",
      "obligation_text": "KPI group và measurement standard mới phải có thể được bổ sung bằng governed configuration mà không thay đổi Analytics business logic"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "KPI group và measurement standard mới phải có thể được bổ sung bằng governed configuration mà không thay đổi Analytics business logic.",
  "provenance": {
    "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-13-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-13-R045",
    "phase_2c_c3_actions": [
      "C3_APPROVED_DECISION_ATOMIC_SPLIT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. KPI",
    "source_context_sha256": "85344345dc19bcf0ae9030dce66f928f0fb4827b426c021d0e9d60c273f65f67",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "1b461e475bde1ca9738cdd5493efe31b4f9dde50d8dfda3ae72a7512edadf435",
    "source_fingerprint_before_c3": "1b461e475bde1ca9738cdd5493efe31b4f9dde50d8dfda3ae72a7512edadf435",
    "source_lines": "L11823-L11915",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-13-R045"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-13-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-13-003"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-13-R045",
  "title": "KPI group và measurement standard mới phải có thể được bổ sung bằng governed configuration mà kh…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-13-001 — Dashboard là cửa ngõ truy cập nhanh tới Business Object. Mọi Widget đều hỗ trợ Drill-down tới dữ…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-018",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-13-001",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "783ab7629b74b392defcf6b905478ed89ecdcd3b115816a7230379397dfafe74"
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
        "EP-13-001-AC001",
        "EP-13-001-AC003",
        "EP-13-001-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-001-O001",
      "obligation_text": "Dashboard là cửa ngõ truy cập nhanh tới Business Object"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-001-AC002",
        "EP-13-001-AC003",
        "EP-13-001-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-001-O002",
      "obligation_text": "Mọi Widget đều hỗ trợ Drill-down tới dữ liệu chi tiết theo Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-13-001-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-13-001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-13-001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-13-001-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-13-001-AC001",
        "EP-13-001-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-13-001 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dashboard là cửa ngõ truy cập nhanh tới Business Object. Mọi Widget đều hỗ trợ Drill-down tới dữ liệu chi tiết theo Permission.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-13-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-13-001",
    "source_context_sha256": "917901f75b0d4cef16761ef242878ffe9a3b57d32f94d5ce054fb8d4def936f4",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "783ab7629b74b392defcf6b905478ed89ecdcd3b115816a7230379397dfafe74",
    "source_lines": "L11917-L12042",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-13-001"
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
  "stable_id": "EP-13-001",
  "title": "Dashboard là cửa ngõ truy cập nhanh tới Business Object. Mọi Widget đều hỗ trợ Drill-down tới dữ…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-13-002 — Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: - Dashboard - KPI - Report…

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
      "requirement_id": "EP-13-002",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "4544e01022f56293e69353d4e1e5c5d0a9a160ca7d38c01b1444571f5f8ab940"
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
        "EP-13-002-AC001",
        "EP-13-002-AC006",
        "EP-13-002-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-002-O001",
      "obligation_text": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: Dashboard"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-002-AC002",
        "EP-13-002-AC006",
        "EP-13-002-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-002-O002",
      "obligation_text": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: KPI"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-002-AC003",
        "EP-13-002-AC006",
        "EP-13-002-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-002-O003",
      "obligation_text": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: Report"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-002-AC004",
        "EP-13-002-AC006",
        "EP-13-002-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-002-O004",
      "obligation_text": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: Analytics"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-002-AC005",
        "EP-13-002-AC006",
        "EP-13-002-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-002-O005",
      "obligation_text": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: Business Intelligence"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: - Dashboard - KPI - Report - Analytics - Business Intelligence",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-13-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-13-002",
    "source_context_sha256": "9ad1998ae645df778f9b07ff31aa36f17ff5cd4d4efde24e56a0224506ce4bd2",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "4544e01022f56293e69353d4e1e5c5d0a9a160ca7d38c01b1444571f5f8ab940",
    "source_lines": "L12044-L12159",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-13-002"
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
  "stable_id": "EP-13-002",
  "title": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: - Dashboard - KPI - Report…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-13-003 — Widget là Platform Capability. Widget không thuộc Dashboard. Một Widget có thể tái sử dụng trên …

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
  "normative_statement": "Widget là Platform Capability. Widget không thuộc Dashboard. Một Widget có thể tái sử dụng trên nhiều Portal và Workspace.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-13-003",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Widget as Capability",
    "source_context_sha256": "a591bfbca16337e050d804aa0bd2410901039358ecea3e5469d76181e94f0d55",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "5c730781e252cdd159434411efb89b3a7236498f67efa1f25a00e63ce900d3b3",
    "source_fingerprint_before_c3": "898bca38828038686159637e2e1dde51d7cbd734603c359adf285b3e435b2af6",
    "source_lines": "L12161-L12222",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-13-003"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-13-R037",
      "BRD-WS-13-R038",
      "BRD-WS-13-R039"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-13-003",
  "title": "Widget là Platform Capability. Widget không thuộc Dashboard. Một Widget có thể tái sử dụng trên …",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-13-004 — Analytics phục vụ Decision Making. Dashboard không chỉ hiển thị dữ liệu mà còn hỗ trợ phát hiện …

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
      "requirement_id": "EP-13-004",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "e911c30a353ef0e667b774eabf0bd2f3cebf579a9937d862fb00301311cae8fb"
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
        "EP-13-004-AC001",
        "EP-13-004-AC003",
        "EP-13-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-004-O001",
      "obligation_text": "Analytics phục vụ Decision Making"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-004-AC002",
        "EP-13-004-AC003",
        "EP-13-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-004-O002",
      "obligation_text": "Dashboard không chỉ hiển thị dữ liệu mà còn hỗ trợ phát hiện bất thường và đề xuất hành động"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Analytics phục vụ Decision Making. Dashboard không chỉ hiển thị dữ liệu mà còn hỗ trợ phát hiện bất thường và đề xuất hành động.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-13-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-13-004",
    "source_context_sha256": "1c9ce7719e1592a560f755b8ec75f57248d3e5a5a3828083d05a3faab48e9e86",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "e911c30a353ef0e667b774eabf0bd2f3cebf579a9937d862fb00301311cae8fb",
    "source_lines": "L12224-L12309",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-13-004"
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
  "stable_id": "EP-13-004",
  "title": "Analytics phục vụ Decision Making. Dashboard không chỉ hiển thị dữ liệu mà còn hỗ trợ phát hiện …",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-13-005 — Alert Rule được cấu hình hoàn toàn. Alert có thể Trigger Notification, Workflow hoặc Business Ac…

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
  "normative_statement": "Alert Rule được cấu hình hoàn toàn. Alert có thể Trigger Notification, Workflow hoặc Business Action. Không Hard-code.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-13-005",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-13-005",
    "source_context_sha256": "c92e19faf0c58044dca1cd2ba8269e199979dc09796aa3d56233483760a975f7",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "d5ec251dc81c3dc02270d14bb4732b277b8d874a49947c5a9082046a371e8557",
    "source_fingerprint_before_c3": "32ffcf9ae5fda813de01570868d63abc822b16411b591bda57a9e7557400bc96",
    "source_lines": "L12311-L12371",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-13-005"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-13-R040",
      "BRD-WS-13-R041",
      "BRD-WS-13-R042"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-13-005",
  "title": "Alert Rule được cấu hình hoàn toàn. Alert có thể Trigger Notification, Workflow hoặc Business Ac…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-13-006 — Report, Dashboard và Widget đều được quản lý theo mô hình Configuration. Organization có thể Ena…

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
      "requirement_id": "EP-13-006",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "cc28521d49d6dcf7cc69a462f6ab14523dcbf062f0d15b644c6a028dabb20113"
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
        "EP-13-006-AC001",
        "EP-13-006-AC003",
        "EP-13-006-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-006-O001",
      "obligation_text": "Report, Dashboard và Widget đều được quản lý theo mô hình Configuration"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-006-AC002",
        "EP-13-006-AC003",
        "EP-13-006-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-006-O002",
      "obligation_text": "Organization có thể Enable, Disable hoặc Override theo Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-13-006-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-13-006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-13-006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-13-006-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-13-006-AC001",
        "EP-13-006-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-13-006 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report, Dashboard và Widget đều được quản lý theo mô hình Configuration. Organization có thể Enable, Disable hoặc Override theo Permission.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-13-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-13-006",
    "source_context_sha256": "caad1b33d73f9c84a1f0c64e331cfbf5d36efd5741e7add78138bd13ecc6c4b8",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "cc28521d49d6dcf7cc69a462f6ab14523dcbf062f0d15b644c6a028dabb20113",
    "source_lines": "L12373-L12494",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-13-006"
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
  "stable_id": "EP-13-006",
  "title": "Report, Dashboard và Widget đều được quản lý theo mô hình Configuration. Organization có thể Ena…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-13-007 — Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…

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
      "requirement_id": "EP-13-007",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "353ba3a4b2c97f8be83db81f341b96d27f4871d7d11b71c3bddd28e2b1057a2c"
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
        "EP-13-007-AC001",
        "EP-13-007-AC010",
        "EP-13-007-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O001",
      "obligation_text": "Localization được áp dụng xuyên suốt: Dashboard"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC002",
        "EP-13-007-AC010",
        "EP-13-007-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O002",
      "obligation_text": "Localization được áp dụng xuyên suốt: Report"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC003",
        "EP-13-007-AC010",
        "EP-13-007-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O003",
      "obligation_text": "Localization được áp dụng xuyên suốt: Widget"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC004",
        "EP-13-007-AC010",
        "EP-13-007-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O004",
      "obligation_text": "Localization được áp dụng xuyên suốt: Analytics Bao gồm"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC005",
        "EP-13-007-AC010",
        "EP-13-007-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O005",
      "obligation_text": "Localization được áp dụng xuyên suốt: Currency"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC006",
        "EP-13-007-AC010",
        "EP-13-007-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O006",
      "obligation_text": "Localization được áp dụng xuyên suốt: Language"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC007",
        "EP-13-007-AC010",
        "EP-13-007-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O007",
      "obligation_text": "Localization được áp dụng xuyên suốt: Measurement"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC008",
        "EP-13-007-AC010",
        "EP-13-007-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O008",
      "obligation_text": "Localization được áp dụng xuyên suốt: Temperature"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC009",
        "EP-13-007-AC010",
        "EP-13-007-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O009",
      "obligation_text": "Localization được áp dụng xuyên suốt: Date Time Format"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-13-007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-13-007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-13-007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-13-007-AC010"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-13-007-AC001",
        "EP-13-007-AC002",
        "EP-13-007-AC003",
        "EP-13-007-AC004",
        "EP-13-007-AC005",
        "EP-13-007-AC006",
        "EP-13-007-AC007",
        "EP-13-007-AC008",
        "EP-13-007-AC009"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-13-007 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Currency - Language - Measurement - Temperature - Date Time Format",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-13-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-13-007",
    "source_context_sha256": "e1498a121728d1860b5b07b638762503375a00a890c91f29f1d2d3985a091dd9",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "353ba3a4b2c97f8be83db81f341b96d27f4871d7d11b71c3bddd28e2b1057a2c",
    "source_lines": "L12496-L12692",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-13-007"
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
  "stable_id": "EP-13-007",
  "title": "Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-13-008 — Operational Intelligence và Business Intelligence phải phục vụ trực tiếp cho việc vận hành Platf…

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
      "requirement_id": "EP-13-008",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "source_fingerprint": "2c41ad815bb4b249eb2231ac170b904a54b6cdf126aaa8996dc2e43eeabaa780"
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
        "EP-13-008-AC001",
        "EP-13-008-AC002",
        "EP-13-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-008-O001",
      "obligation_text": "Operational Intelligence và Business Intelligence phải phục vụ trực tiếp cho việc vận hành Platform và hỗ trợ ra quyết định"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operational Intelligence và Business Intelligence phải phục vụ trực tiếp cho việc vận hành Platform và hỗ trợ ra quyết định.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-13-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-13-008",
    "source_context_sha256": "a30bcfec9fc89506b5a5a40b7129b0ad9c39f683eef45847eb03d65305f17746",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "2c41ad815bb4b249eb2231ac170b904a54b6cdf126aaa8996dc2e43eeabaa780",
    "source_lines": "L12694-L12769",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-13-008"
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
  "stable_id": "EP-13-008",
  "title": "Operational Intelligence và Business Intelligence phải phục vụ trực tiếp cho việc vận hành Platf…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
