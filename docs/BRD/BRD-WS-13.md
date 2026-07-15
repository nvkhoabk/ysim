---
document_code: "BRD-WS-13"
title: "Reporting, Analytics & Operational Intelligence"
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

Widget Library cho phép Organization lựa chọn Widget cần hiển thị hoặc ẩn.

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

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-001 — Dashboard hỗ trợ nhiều cấp: - Platform - Organization - Department - User - Customer

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-001-AC001",
      "given": "the applicable business context, actor, and input for Dashboard hỗ trợ nhiều cấp: - Platform - Organization - Department - User - Customer",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-001-AC002",
      "given": "the applicable business context, actor, and input for Dashboard hỗ trợ nhiều cấp: - Platform - Organization - Department - User - Customer",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-001-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-001-AC003",
      "given": "the applicable business context, actor, and input for Dashboard hỗ trợ nhiều cấp: - Platform - Organization - Department - User - Customer",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-001-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-001-AC004",
      "given": "the applicable business context, actor, and input for Dashboard hỗ trợ nhiều cấp: - Platform - Organization - Department - User - Customer",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-001-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-001-AC005",
      "given": "the applicable business context, actor, and input for Dashboard hỗ trợ nhiều cấp: - Platform - Organization - Department - User - Customer",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-001-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-13-001-AC006",
      "given": "an unsupported or invalid business input at the boundary governed by Dashboard hỗ trợ nhiều cấp: - Platform - Organization - Department - User - Customer",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-13-001-O001",
        "BD-13-001-O002",
        "BD-13-001-O003",
        "BD-13-001-O004",
        "BD-13-001-O005"
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
        "BD-13-001-AC001",
        "BD-13-001-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-001-O001",
      "obligation_text": "Dashboard hỗ trợ nhiều cấp: Platform."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-001-AC002",
        "BD-13-001-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-001-O002",
      "obligation_text": "Dashboard hỗ trợ nhiều cấp: Organization."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-001-AC003",
        "BD-13-001-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-001-O003",
      "obligation_text": "Dashboard hỗ trợ nhiều cấp: Department."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-001-AC004",
        "BD-13-001-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-001-O004",
      "obligation_text": "Dashboard hỗ trợ nhiều cấp: User."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-001-AC005",
        "BD-13-001-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-001-O005",
      "obligation_text": "Dashboard hỗ trợ nhiều cấp: Customer."
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
    "source_fingerprint": "f0c740a878ff515d5cfe0ef791e9c6704dec117176d20522459742553624dfb6",
    "source_lines": "L767-L776",
    "source_section": "29. Business Decisions (Locked) > BD-13-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-002-AC001",
      "given": "the applicable business context, actor, and input for Dashboard Widget hỗ trợ: - Drag & Drop - Resize - Reorder - Multiple Workspace - Saved Layout",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-002-AC002",
      "given": "the applicable business context, actor, and input for Dashboard Widget hỗ trợ: - Drag & Drop - Resize - Reorder - Multiple Workspace - Saved Layout",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-002-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-002-AC003",
      "given": "the applicable business context, actor, and input for Dashboard Widget hỗ trợ: - Drag & Drop - Resize - Reorder - Multiple Workspace - Saved Layout",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-002-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-002-AC004",
      "given": "the applicable business context, actor, and input for Dashboard Widget hỗ trợ: - Drag & Drop - Resize - Reorder - Multiple Workspace - Saved Layout",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-002-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-002-AC005",
      "given": "the applicable business context, actor, and input for Dashboard Widget hỗ trợ: - Drag & Drop - Resize - Reorder - Multiple Workspace - Saved Layout",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-002-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-13-002-AC006",
      "given": "an unsupported or invalid business input at the boundary governed by Dashboard Widget hỗ trợ: - Drag & Drop - Resize - Reorder - Multiple Workspace - Saved Layout",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-13-002-O001",
        "BD-13-002-O002",
        "BD-13-002-O003",
        "BD-13-002-O004",
        "BD-13-002-O005"
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
        "BD-13-002-AC001",
        "BD-13-002-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-002-O001",
      "obligation_text": "Dashboard Widget hỗ trợ: Drag & Drop."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-002-AC002",
        "BD-13-002-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-002-O002",
      "obligation_text": "Dashboard Widget hỗ trợ: Resize."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-002-AC003",
        "BD-13-002-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-002-O003",
      "obligation_text": "Dashboard Widget hỗ trợ: Reorder."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-002-AC004",
        "BD-13-002-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-002-O004",
      "obligation_text": "Dashboard Widget hỗ trợ: Multiple Workspace."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-002-AC005",
        "BD-13-002-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-002-O005",
      "obligation_text": "Dashboard Widget hỗ trợ: Saved Layout."
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
    "source_fingerprint": "4cadaf2bd8a61dbacd1b14590f6e7710b2106e9810de40321b99c0c58b150b47",
    "source_lines": "L779-L788",
    "source_section": "29. Business Decisions (Locked) > BD-13-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-003-AC001",
      "given": "the applicable business context, actor, and input for KPI Definition được cấu hình. Kiến trúc hỗ trợ mở rộng thêm các nhóm KPI và tiêu chuẩn đo lường",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-13-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-003-AC002",
      "given": "the applicable business context, actor, and input for KPI Definition được cấu hình. Kiến trúc hỗ trợ mở rộng thêm các nhóm KPI và tiêu chuẩn đo lường",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-003-O002"
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
        "BD-13-003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-003-O001",
      "obligation_text": "KPI Definition được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-003-O002",
      "obligation_text": "Kiến trúc hỗ trợ mở rộng thêm các nhóm KPI và tiêu chuẩn đo lường"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "KPI Definition được cấu hình. Kiến trúc hỗ trợ mở rộng thêm các nhóm KPI và tiêu chuẩn đo lường.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. KPI",
    "source_context_sha256": "85344345dc19bcf0ae9030dce66f928f0fb4827b426c021d0e9d60c273f65f67",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "118d78236b3b61bb4560bd320e5b3c71f048003f2e6864294adb2e34f2dd758e",
    "source_lines": "L791-L796",
    "source_section": "29. Business Decisions (Locked) > BD-13-003"
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
  "stable_id": "BD-13-003",
  "title": "KPI Definition được cấu hình. Kiến trúc hỗ trợ mở rộng thêm các nhóm KPI và tiêu chuẩn đo lường",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-004 — Report là Business Object độc lập. System Report chỉ dành cho YSim Internal. Business Report hỗ …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-004-AC001",
      "given": "a candidate Report là Business Object độc lập. System Report chỉ dành cho YSim Internal. Business Report hỗ … record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-004-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-004-AC002",
      "given": "a candidate Report là Business Object độc lập. System Report chỉ dành cho YSim Internal. Business Report hỗ … record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-004-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-004-AC003",
      "given": "a candidate Report là Business Object độc lập. System Report chỉ dành cho YSim Internal. Business Report hỗ … record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-004-O003"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-13-004-AC004",
      "given": "a Report là Business Object độc lập. System Report chỉ dành cho YSim Internal. Business Report hỗ … candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-13-004-O001",
        "BD-13-004-O002",
        "BD-13-004-O003"
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
        "BD-13-004-AC001",
        "BD-13-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-004-O001",
      "obligation_text": "Report là Business Object độc lập"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-004-AC002",
        "BD-13-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-004-O002",
      "obligation_text": "System Report chỉ dành cho YSim Internal"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-004-AC003",
        "BD-13-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-004-O003",
      "obligation_text": "Business Report hỗ trợ kế thừa: YSim ↓ Parent Organization ↓ Organization Override"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report là Business Object độc lập. System Report chỉ dành cho YSim Internal. Business Report hỗ trợ kế thừa: YSim ↓ Parent Organization ↓ Organization Override",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Report Model",
    "source_context_sha256": "6f73245c294739f9ff85868c2f0b56a1e0564d82247e21cc390fc671549063d1",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "417021a32b7b3387106e14462bcab42bbf2571d62a750b3e36ba8da1b9a614d4",
    "source_lines": "L799-L816",
    "source_section": "29. Business Decisions (Locked) > BD-13-004"
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
  "stable_id": "BD-13-004",
  "title": "Report là Business Object độc lập. System Report chỉ dành cho YSim Internal. Business Report hỗ …",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-005 — Saved View là Business Object. Saved View thuộc User

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-005-AC001",
      "given": "a candidate Saved View là Business Object. Saved View thuộc User record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-005-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-005-AC002",
      "given": "a candidate Saved View là Business Object. Saved View thuộc User record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-005-O002"
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
        "BD-13-005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-005-O001",
      "obligation_text": "Saved View là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-005-AC002"
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
    "source_fingerprint": "1f227c45159cfe3e3295ecbbd90724e5c52bc86d002b80c9e2fb9ea518549e52",
    "source_lines": "L819-L824",
    "source_section": "29. Business Decisions (Locked) > BD-13-005"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-006-AC001",
      "given": "the applicable business context, actor, and input for Report hỗ trợ: - Manual - Schedule - Event Trigger - Auto Generate - Auto Delivery",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-006-AC002",
      "given": "the applicable business context, actor, and input for Report hỗ trợ: - Manual - Schedule - Event Trigger - Auto Generate - Auto Delivery",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-006-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-006-AC003",
      "given": "the applicable business context, actor, and input for Report hỗ trợ: - Manual - Schedule - Event Trigger - Auto Generate - Auto Delivery",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-006-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-006-AC004",
      "given": "the applicable business context, actor, and input for Report hỗ trợ: - Manual - Schedule - Event Trigger - Auto Generate - Auto Delivery",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-006-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-006-AC005",
      "given": "the applicable business context, actor, and input for Report hỗ trợ: - Manual - Schedule - Event Trigger - Auto Generate - Auto Delivery",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-006-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-13-006-AC006",
      "given": "an unsupported or invalid business input at the boundary governed by Report hỗ trợ: - Manual - Schedule - Event Trigger - Auto Generate - Auto Delivery",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-13-006-O001",
        "BD-13-006-O002",
        "BD-13-006-O003",
        "BD-13-006-O004",
        "BD-13-006-O005"
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
        "BD-13-006-AC001",
        "BD-13-006-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-006-O001",
      "obligation_text": "Report hỗ trợ: Manual."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-006-AC002",
        "BD-13-006-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-006-O002",
      "obligation_text": "Report hỗ trợ: Schedule."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-006-AC003",
        "BD-13-006-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-006-O003",
      "obligation_text": "Report hỗ trợ: Event Trigger."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-006-AC004",
        "BD-13-006-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-006-O004",
      "obligation_text": "Report hỗ trợ: Auto Generate."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-006-AC005",
        "BD-13-006-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-006-O005",
      "obligation_text": "Report hỗ trợ: Auto Delivery."
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
    "source_fingerprint": "9c127741a3129a93e89249a5834c682e704abb1c2eba8ad8cffeb125b9e9032f",
    "source_lines": "L827-L836",
    "source_section": "29. Business Decisions (Locked) > BD-13-006"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-13-007-AC001",
      "given": "a contract interaction at the integration boundary defined by Report hỗ trợ: - Download - Email - Portal - Personal Inbox - API",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-13-007-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-13-007-AC002",
      "given": "a contract interaction at the integration boundary defined by Report hỗ trợ: - Download - Email - Portal - Personal Inbox - API",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-13-007-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-13-007-AC003",
      "given": "a contract interaction at the integration boundary defined by Report hỗ trợ: - Download - Email - Portal - Personal Inbox - API",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-13-007-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-13-007-AC004",
      "given": "a contract interaction at the integration boundary defined by Report hỗ trợ: - Download - Email - Portal - Personal Inbox - API",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-13-007-O004"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-13-007-AC005",
      "given": "a contract interaction at the integration boundary defined by Report hỗ trợ: - Download - Email - Portal - Personal Inbox - API",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-13-007-O005"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-13-007-AC006",
      "given": "an interaction that violates the contract or ownership boundary for Report hỗ trợ: - Download - Email - Portal - Personal Inbox - API",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-13-007-O001",
        "BD-13-007-O002",
        "BD-13-007-O003",
        "BD-13-007-O004",
        "BD-13-007-O005"
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
        "BD-13-007-AC001",
        "BD-13-007-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-007-O001",
      "obligation_text": "Report hỗ trợ: Download."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-007-AC002",
        "BD-13-007-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-007-O002",
      "obligation_text": "Report hỗ trợ: Email."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-007-AC003",
        "BD-13-007-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-007-O003",
      "obligation_text": "Report hỗ trợ: Portal."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-007-AC004",
        "BD-13-007-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-007-O004",
      "obligation_text": "Report hỗ trợ: Personal Inbox."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-007-AC005",
        "BD-13-007-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-007-O005",
      "obligation_text": "Report hỗ trợ: API."
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
    "source_fingerprint": "63ad7079a3989ffea26188463e08e8681df09a883e9a1a981c7e0148f7f2731b",
    "source_lines": "L839-L848",
    "source_section": "29. Business Decisions (Locked) > BD-13-007"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-008-AC001",
      "given": "a candidate Dashboard hỗ trợ Drill-down tới Business Object record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-008-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-13-008-AC002",
      "given": "a Dashboard hỗ trợ Drill-down tới Business Object candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-13-008-O001"
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
        "BD-13-008-AC001",
        "BD-13-008-AC002"
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
    "source_fingerprint": "510aa2823d919ea8b621844e3c6f535eac9cc3ed4f5bd1d5f637d86114ac1c9a",
    "source_lines": "L851-L854",
    "source_section": "29. Business Decisions (Locked) > BD-13-008"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-009-AC001",
      "given": "a candidate Metric là Business Object. Metric là đơn vị đo lường chuẩn để xây dựng Dashboard, KPI và Report record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-009-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-009-AC002",
      "given": "a candidate Metric là Business Object. Metric là đơn vị đo lường chuẩn để xây dựng Dashboard, KPI và Report record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-009-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-13-009-AC003",
      "given": "a Metric là Business Object. Metric là đơn vị đo lường chuẩn để xây dựng Dashboard, KPI và Report candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-13-009-O001",
        "BD-13-009-O002"
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
        "BD-13-009-AC001",
        "BD-13-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-009-O001",
      "obligation_text": "Metric là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-009-AC002",
        "BD-13-009-AC003"
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
    "source_fingerprint": "286e90210e1d0fb5d06bbf6dff2903aeaed6a1da607f6b3831fb26a6a9f1ef01",
    "source_lines": "L857-L862",
    "source_section": "29. Business Decisions (Locked) > BD-13-009"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-010-AC001",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-13-010-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-010-AC002",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-13-010-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-010-AC003",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-13-010-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-010-AC004",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-13-010-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-010-AC005",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-13-010-O005"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-010-AC006",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-13-010-O006"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-010-AC007",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-13-010-O007"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-010-AC008",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-13-010-O008"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-010-AC009",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-13-010-O009"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-13-010-AC010",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Alert Rule là Business Object. Alert Rule có thể Trigger: - Notification - Workflow - Business A…",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-13-010-O001",
        "BD-13-010-O002",
        "BD-13-010-O003",
        "BD-13-010-O004",
        "BD-13-010-O005",
        "BD-13-010-O006",
        "BD-13-010-O007",
        "BD-13-010-O008",
        "BD-13-010-O009"
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
        "BD-13-010-AC001",
        "BD-13-010-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O001",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Notification."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC002",
        "BD-13-010-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O002",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Workflow."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC003",
        "BD-13-010-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O003",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Business Action Ví dụ."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC004",
        "BD-13-010-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O004",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Block User."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC005",
        "BD-13-010-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O005",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Block Organization."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC006",
        "BD-13-010-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O006",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Block IP."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC007",
        "BD-13-010-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O007",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Block Transaction."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC008",
        "BD-13-010-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O008",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Escalation."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-010-AC009",
        "BD-13-010-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-010-O009",
      "obligation_text": "Alert Rule là Business Object. Alert Rule có thể Trigger: Auto Ticket."
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
    "source_fingerprint": "2952945f0dafe8d2cec2adfc8c72d56e646b7f00cbe2f2cb17d282f2e522cbdd",
    "source_lines": "L865-L883",
    "source_section": "29. Business Decisions (Locked) > BD-13-010"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-011-AC001",
      "given": "an operational task within the scope of Operational Dashboard có thể: - Real-time - Near Real-time Tùy theo yêu cầu nghiệp vụ và khả năn…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-13-011-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-011-AC002",
      "given": "an operational task within the scope of Operational Dashboard có thể: - Real-time - Near Real-time Tùy theo yêu cầu nghiệp vụ và khả năn…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-13-011-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-13-011-AC003",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Operational Dashboard có thể: - Real-time - Near Real-time Tùy theo yêu cầu nghiệp vụ và khả năn…",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-13-011-O001",
        "BD-13-011-O002"
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
        "BD-13-011-AC001",
        "BD-13-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-011-O001",
      "obligation_text": "Operational Dashboard có thể: Real-time."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-011-AC002",
        "BD-13-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-011-O002",
      "obligation_text": "Operational Dashboard có thể: Near Real-time Tùy theo yêu cầu nghiệp vụ và khả năng triển khai."
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
    "source_fingerprint": "85c815ad185d8737e6e70ce7484daa9473696b1a6abef9261b4656c21bf15065",
    "source_lines": "L886-L894",
    "source_section": "29. Business Decisions (Locked) > BD-13-011"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SCOPE_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-13-012-AC001",
      "given": "the v2.3 capability inventory and conformance evidence for Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: - AI Analytics - Mach…",
      "observable_evidence": "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
      "then": "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
      "verifies": [
        "BD-13-012-O001"
      ],
      "when": "the capability is inspected at the active baseline boundary"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SCOPE_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-13-012-AC002",
      "given": "the v2.3 capability inventory and conformance evidence for Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: - AI Analytics - Mach…",
      "observable_evidence": "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
      "then": "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
      "verifies": [
        "BD-13-012-O002"
      ],
      "when": "the capability is inspected at the active baseline boundary"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SCOPE_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-13-012-AC003",
      "given": "the v2.3 capability inventory and conformance evidence for Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: - AI Analytics - Mach…",
      "observable_evidence": "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
      "then": "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
      "verifies": [
        "BD-13-012-O003"
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
        "BD-13-012-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-012-O001",
      "obligation_text": "Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: AI Analytics."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-012-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-012-O002",
      "obligation_text": "Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: Machine Learning."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-012-O003",
      "obligation_text": "Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: Predictive Analytics."
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
    "source_fingerprint": "77818b3996eaa94784d5b165da98f5d5a07e275d41acad519b2b7d5de5cd752e",
    "source_lines": "L897-L906",
    "source_section": "29. Business Decisions (Locked) > BD-13-012"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-13-013-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support …",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-13-013-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-13-013-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support …",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-13-013-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-13-013-AC003",
      "given": "an identified principal, applicable assurance context, and policy inputs for Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support …",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-13-013-O003"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-13-013-AC004",
      "given": "an identified principal, applicable assurance context, and policy inputs for Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support …",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-13-013-O004"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-13-013-AC005",
      "given": "an identified principal, applicable assurance context, and policy inputs for Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support …",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-13-013-O005"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-13-013-AC006",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support …",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-13-013-O001",
        "BD-13-013-O002",
        "BD-13-013-O003",
        "BD-13-013-O004",
        "BD-13-013-O005"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-13-013-AC007",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support …",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-13-013-O001",
        "BD-13-013-O002",
        "BD-13-013-O003",
        "BD-13-013-O004",
        "BD-13-013-O005"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-13-013-AC008",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support …",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-13-013-O001",
        "BD-13-013-O002",
        "BD-13-013-O003",
        "BD-13-013-O004",
        "BD-13-013-O005"
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
        "BD-13-013-AC001",
        "BD-13-013-AC006",
        "BD-13-013-AC007",
        "BD-13-013-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-013-O001",
      "obligation_text": "Report Permission được xác định theo: Organization."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-013-AC002",
        "BD-13-013-AC006",
        "BD-13-013-AC007",
        "BD-13-013-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-013-O002",
      "obligation_text": "Report Permission được xác định theo: Role."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-013-AC003",
        "BD-13-013-AC006",
        "BD-13-013-AC007",
        "BD-13-013-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-013-O003",
      "obligation_text": "Report Permission được xác định theo: Permission."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-013-AC004",
        "BD-13-013-AC006",
        "BD-13-013-AC007",
        "BD-13-013-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-013-O004",
      "obligation_text": "Report Permission được xác định theo: Data Scope."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-013-AC005",
        "BD-13-013-AC006",
        "BD-13-013-AC007",
        "BD-13-013-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-013-O005",
      "obligation_text": "Report Permission được xác định theo: Support Policy Có thể Mask dữ liệu theo Permission."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-13-013-AC008"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-13-013 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-13-013 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-13-013-AC007"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-13-013-AC001",
        "BD-13-013-AC002",
        "BD-13-013-AC003",
        "BD-13-013-AC004",
        "BD-13-013-AC005"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-13-013 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support Policy Có thể Mask dữ liệu theo Permission.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-13-013",
    "source_context_sha256": "c2d9e76299e296e5c0f8f686f969d8b53c51bf163468c0eaf194a891f82dad3f",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "870fbac209e092746fa51e63bb215da9b9e9bde53432a004b8009c7300a5c1a4",
    "source_lines": "L909-L920",
    "source_section": "29. Business Decisions (Locked) > BD-13-013"
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
  "stable_id": "BD-13-013",
  "title": "Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support …",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-13-014 — Dashboard hiển thị dữ liệu theo: - Localization - Currency Preference - Measurement Preference R…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-014-AC001",
      "given": "the applicable business context, actor, and input for Dashboard hiển thị dữ liệu theo: - Localization - Currency Preference - Measurement Preference R…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-014-AC002",
      "given": "the applicable business context, actor, and input for Dashboard hiển thị dữ liệu theo: - Localization - Currency Preference - Measurement Preference R…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-014-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-014-AC003",
      "given": "the applicable business context, actor, and input for Dashboard hiển thị dữ liệu theo: - Localization - Currency Preference - Measurement Preference R…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-014-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-13-014-AC004",
      "given": "an unsupported or invalid business input at the boundary governed by Dashboard hiển thị dữ liệu theo: - Localization - Currency Preference - Measurement Preference R…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-13-014-O001",
        "BD-13-014-O002",
        "BD-13-014-O003"
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
        "BD-13-014-AC001",
        "BD-13-014-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-014-O001",
      "obligation_text": "Dashboard hiển thị dữ liệu theo: Localization."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-014-AC002",
        "BD-13-014-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-014-O002",
      "obligation_text": "Dashboard hiển thị dữ liệu theo: Currency Preference."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-014-AC003",
        "BD-13-014-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-014-O003",
      "obligation_text": "Dashboard hiển thị dữ liệu theo: Measurement Preference Report mặc định sử dụng Currency chuẩn của Report."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-13-014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-13-014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-13-014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-13-014 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-13-014-AC001",
        "BD-13-014-AC002",
        "BD-13-014-AC003"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-13-014 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "ca0704fdcac18f9a2a4c38d8499d53129dd9d4426496fb9c61240ee2e5753583",
    "source_lines": "L923-L932",
    "source_section": "29. Business Decisions (Locked) > BD-13-014"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-015-AC001",
      "given": "a candidate Report luôn đọc dữ liệu từ Snapshot. Không đọc trực tiếp Transaction đang thay đổi record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-015-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-015-AC002",
      "given": "a candidate Report luôn đọc dữ liệu từ Snapshot. Không đọc trực tiếp Transaction đang thay đổi record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-015-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-13-015-AC003",
      "given": "a Report luôn đọc dữ liệu từ Snapshot. Không đọc trực tiếp Transaction đang thay đổi candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-13-015-O001",
        "BD-13-015-O002"
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
        "BD-13-015-AC001",
        "BD-13-015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-015-O001",
      "obligation_text": "Report luôn đọc dữ liệu từ Snapshot"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-015-AC002",
        "BD-13-015-AC003"
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
    "source_fingerprint": "38c2711c90d5060fcedfad8afd307d11311470a21bdd25d760549b9bc6baa2cf",
    "source_lines": "L935-L940",
    "source_section": "29. Business Decisions (Locked) > BD-13-015"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-016-AC001",
      "given": "the applicable business context, actor, and input for Supplier Analytics chỉ dành cho YSim Internal. Supplier không có Dashboard riêng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-016-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-016-AC002",
      "given": "the applicable business context, actor, and input for Supplier Analytics chỉ dành cho YSim Internal. Supplier không có Dashboard riêng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-016-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-13-016-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Supplier Analytics chỉ dành cho YSim Internal. Supplier không có Dashboard riêng",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-13-016-O001",
        "BD-13-016-O002"
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
        "BD-13-016-AC001",
        "BD-13-016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-016-O001",
      "obligation_text": "Supplier Analytics chỉ dành cho YSim Internal"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-016-AC002",
        "BD-13-016-AC003"
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
    "source_fingerprint": "63f19b5ccb20986f24220a8cf38e1669c3ff96cb4557bcebef56905b033a3e0f",
    "source_lines": "L943-L948",
    "source_section": "29. Business Decisions (Locked) > BD-13-016"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-017-AC001",
      "given": "the applicable business context, actor, and input for Organization chỉ được Benchmark dữ liệu của chính Organization đó. Không được phép xem dữ liệu c…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-017-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-017-AC002",
      "given": "the applicable business context, actor, and input for Organization chỉ được Benchmark dữ liệu của chính Organization đó. Không được phép xem dữ liệu c…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BD-13-017-O002"
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
        "BD-13-017-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-017-O001",
      "obligation_text": "Organization chỉ được Benchmark dữ liệu của chính Organization đó"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-017-AC002"
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
    "source_fingerprint": "75925dbc5720ee7dd92d826d83506078584ae83051dd2574e2273261c640cc33",
    "source_lines": "L951-L956",
    "source_section": "29. Business Decisions (Locked) > BD-13-017"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-018-AC001",
      "given": "the applicable business context, actor, and input for Version 2 hỗ trợ Custom Report Builder. Report được cấu hình thay vì Hard-code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-018-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-018-AC002",
      "given": "the applicable business context, actor, and input for Version 2 hỗ trợ Custom Report Builder. Report được cấu hình thay vì Hard-code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-13-018-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-13-018-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Version 2 hỗ trợ Custom Report Builder. Report được cấu hình thay vì Hard-code",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-13-018-O001",
        "BD-13-018-O002"
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
        "BD-13-018-AC001",
        "BD-13-018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-018-O001",
      "obligation_text": "Version 2 hỗ trợ Custom Report Builder"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-018-AC002",
        "BD-13-018-AC003"
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
    "source_fingerprint": "0f8c318abfc379f6ac16bc7f1ea82ccffea9a64c869114bfd0d3d7ba8aeca522",
    "source_lines": "L959-L964",
    "source_section": "29. Business Decisions (Locked) > BD-13-018"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-019-AC001",
      "given": "the applicable business context, actor, and input for Widget Library là Platform Capability. Widget được tái sử dụng trên: - Dashboard - Workspace - A…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-019-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-019-AC002",
      "given": "the applicable business context, actor, and input for Widget Library là Platform Capability. Widget được tái sử dụng trên: - Dashboard - Workspace - A…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-019-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-019-AC003",
      "given": "the applicable business context, actor, and input for Widget Library là Platform Capability. Widget được tái sử dụng trên: - Dashboard - Workspace - A…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-019-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-019-AC004",
      "given": "the applicable business context, actor, and input for Widget Library là Platform Capability. Widget được tái sử dụng trên: - Dashboard - Workspace - A…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-019-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-13-019-AC005",
      "given": "the applicable business context, actor, and input for Widget Library là Platform Capability. Widget được tái sử dụng trên: - Dashboard - Workspace - A…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-13-019-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-13-019-AC006",
      "given": "an unsupported or invalid business input at the boundary governed by Widget Library là Platform Capability. Widget được tái sử dụng trên: - Dashboard - Workspace - A…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-13-019-O001",
        "BD-13-019-O002",
        "BD-13-019-O003",
        "BD-13-019-O004",
        "BD-13-019-O005"
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
        "BD-13-019-AC001",
        "BD-13-019-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-019-O001",
      "obligation_text": "Widget Library là Platform Capability. Widget được tái sử dụng trên: Dashboard."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-019-AC002",
        "BD-13-019-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-019-O002",
      "obligation_text": "Widget Library là Platform Capability. Widget được tái sử dụng trên: Workspace."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-019-AC003",
        "BD-13-019-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-019-O003",
      "obligation_text": "Widget Library là Platform Capability. Widget được tái sử dụng trên: Admin Portal."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-019-AC004",
        "BD-13-019-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-019-O004",
      "obligation_text": "Widget Library là Platform Capability. Widget được tái sử dụng trên: Organization Portal."
    },
    {
      "acceptance_criterion_references": [
        "BD-13-019-AC005",
        "BD-13-019-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-019-O005",
      "obligation_text": "Widget Library là Platform Capability. Widget được tái sử dụng trên: Customer Portal."
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
    "source_fingerprint": "305319079458944b01d7e31c5022405b3d617a0dea3ade2003b92bded290afba",
    "source_lines": "L967-L978",
    "source_section": "29. Business Decisions (Locked) > BD-13-019"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-020-AC001",
      "given": "a candidate Insight là Business Object. Insight được sinh từ Rule Engine và Analytics. Version 2 chưa sử dụn… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-020-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-020-AC002",
      "given": "a candidate Insight là Business Object. Insight được sinh từ Rule Engine và Analytics. Version 2 chưa sử dụn… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-020-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-13-020-AC003",
      "given": "a candidate Insight là Business Object. Insight được sinh từ Rule Engine và Analytics. Version 2 chưa sử dụn… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-13-020-O003"
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
        "BD-13-020-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-020-O001",
      "obligation_text": "Insight là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-020-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-020-O002",
      "obligation_text": "Insight được sinh từ Rule Engine và Analytics"
    },
    {
      "acceptance_criterion_references": [
        "BD-13-020-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-13-020-O003",
      "obligation_text": "Version 2 chưa sử dụng AI"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Insight là Business Object. Insight được sinh từ Rule Engine và Analytics. Version 2 chưa sử dụng AI.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-13-020",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. Operational Insight",
    "source_context_sha256": "e14305f76ca4b6c0410aa695e886b2cab72e8c679002d56f9a33141eb435ad63",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "8e0f9e6f8f3fe2a0086b261cffb1f37ca1b98d109b41c43f86bc2648ec579191",
    "source_lines": "L981-L988",
    "source_section": "29. Business Decisions (Locked) > BD-13-020"
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
  "stable_id": "BD-13-020",
  "title": "Insight là Business Object. Insight được sinh từ Rule Engine và Analytics. Version 2 chưa sử dụn…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R001 — (Các nội dung trên được giữ chỗ cho các phiên bản sau.)

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
    "source_lines": "L45",
    "source_section": "1. Workshop Objective"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R002-AC001",
      "given": "a candidate Dashboard và Widget phải hỗ trợ Drill-down tới module hoặc Business Object tương ứng record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-13-R002-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-13-R002-AC002",
      "given": "a Dashboard và Widget phải hỗ trợ Drill-down tới module hoặc Business Object tương ứng candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BRD-WS-13-R002-O001"
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
        "BRD-WS-13-R002-AC001",
        "BRD-WS-13-R002-AC002"
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
    "source_lines": "L90",
    "source_section": "3. Dashboard Model"
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
### BRD-WS-13-R003 — Widget Library cho phép Organization lựa chọn Widget cần hiển thị hoặc ẩn

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R003-AC001",
      "given": "the applicable business context, actor, and input for Widget Library cho phép Organization lựa chọn Widget cần hiển thị hoặc ẩn",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-13-R003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-13-R003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Widget Library cho phép Organization lựa chọn Widget cần hiển thị hoặc ẩn",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-13-R003-O001"
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
        "BRD-WS-13-R003-AC001",
        "BRD-WS-13-R003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R003-O001",
      "obligation_text": "Widget Library cho phép Organization lựa chọn Widget cần hiển thị hoặc ẩn"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Widget Library cho phép Organization lựa chọn Widget cần hiển thị hoặc ẩn.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-003",
    "previous_temporary_key": "TMP-BRD-WS-13-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Dashboard Widget",
    "source_context_sha256": "5ff050cde793f2ed33ece067c9283e4077eef7a36d130be15c3442c4584545de",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "4869eff46da71e315b600f95ba5e4486e6c65528df6296a77de417678a1611f4",
    "source_lines": "L116",
    "source_section": "4. Dashboard Widget"
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
  "title": "Widget Library cho phép Organization lựa chọn Widget cần hiển thị hoặc ẩn",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R004 — Drill-down phải tôn trọng Permission và Data Scope của User

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R004-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Drill-down phải tôn trọng Permission và Data Scope của User",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-13-R004-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-13-R004-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Drill-down phải tôn trọng Permission và Data Scope của User",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-13-R004-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-13-R004-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Drill-down phải tôn trọng Permission và Data Scope của User",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-13-R004-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-13-R004-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Drill-down phải tôn trọng Permission và Data Scope của User",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-13-R004-O001"
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
        "BRD-WS-13-R004-AC001",
        "BRD-WS-13-R004-AC002",
        "BRD-WS-13-R004-AC003",
        "BRD-WS-13-R004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R004-O001",
      "obligation_text": "Drill-down phải tôn trọng Permission và Data Scope của User"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-13-R004-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-13-R004-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-13-R004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L261",
    "source_section": "10. Drill-down"
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
    "source_lines": "L277",
    "source_section": "11. KPI Scope"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R006-AC001",
      "given": "the applicable business context, actor, and input for Không bắt buộc toàn bộ Dashboard phải Real-time",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-13-R006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-13-R006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Không bắt buộc toàn bộ Dashboard phải Real-time",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-13-R006-O001"
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
        "BRD-WS-13-R006-AC001",
        "BRD-WS-13-R006-AC002"
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
    "source_lines": "L380",
    "source_section": "14. Operational Intelligence"
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
    "source_lines": "L422",
    "source_section": "16. Business Intelligence"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R008-AC001",
      "given": "the applicable business context, actor, and input for Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Currency",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-13-R008-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-13-R008-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Currency",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-13-R008-O001"
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
        "BRD-WS-13-R008-AC001",
        "BRD-WS-13-R008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R008-O001",
      "obligation_text": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Currency"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R008 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R008 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-13-R008-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L459-L461",
    "source_section": "18. Multi Currency Reporting"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R009-AC001",
      "given": "the applicable business context, actor, and input for Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Rate",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-13-R009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-13-R009-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Rate",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-13-R009-O001"
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
        "BRD-WS-13-R009-AC001",
        "BRD-WS-13-R009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R009-O001",
      "obligation_text": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Rate"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R009 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R009 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R009 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R009 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-13-R009-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R009 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "2a2a7546ed524df2572da26a580046e0304e6dcc337c9e5b090603b9461d31ef",
    "source_lines": "L459-L462",
    "source_section": "18. Multi Currency Reporting"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R010-AC001",
      "given": "the applicable business context, actor, and input for Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Conversion Rule",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-13-R010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-13-R010-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Conversion Rule",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-13-R010-O001"
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
        "BRD-WS-13-R010-AC001",
        "BRD-WS-13-R010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R010-O001",
      "obligation_text": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Conversion Rule"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R010 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R010 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R010 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R010 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-13-R010-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R010 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "21b400ffa50d97d46e5f510e758dfa6f28a0fa7b4b09653d6bf2e7285e93cd33",
    "source_lines": "L459-L463",
    "source_section": "18. Multi Currency Reporting"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R011-AC001",
      "given": "the applicable business context, actor, and input for Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Time",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-13-R011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-13-R011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Time",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-13-R011-O001"
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
        "BRD-WS-13-R011-AC001",
        "BRD-WS-13-R011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R011-O001",
      "obligation_text": "Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Time"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R011 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R011 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R011 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R011 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-13-R011-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R011 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "133bf1b4d02b14bb2ff0664c874c8dbe7490e4ac2e73604d65a5b2c06d9e81b6",
    "source_lines": "L459-L464",
    "source_section": "18. Multi Currency Reporting"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R012-AC001",
      "given": "the applicable business context, actor, and input for Dashboard luôn chuyển đổi đơn vị hiển thị theo cấu hình Localization của User",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-13-R012-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-13-R012-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Dashboard luôn chuyển đổi đơn vị hiển thị theo cấu hình Localization của User",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-13-R012-O001"
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
        "BRD-WS-13-R012-AC001",
        "BRD-WS-13-R012-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R012-O001",
      "obligation_text": "Dashboard luôn chuyển đổi đơn vị hiển thị theo cấu hình Localization của User"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R012 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R012 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R012 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R012 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-13-R012-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R012 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L466",
    "source_section": "18. Multi Currency Reporting"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R013-AC001",
      "given": "a candidate Report luôn đọc dữ liệu từ Snapshot record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-13-R013-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-13-R013-AC002",
      "given": "a Report luôn đọc dữ liệu từ Snapshot candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BRD-WS-13-R013-O001"
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
        "BRD-WS-13-R013-AC001",
        "BRD-WS-13-R013-AC002"
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
    "source_lines": "L472",
    "source_section": "19. Reporting Snapshot"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R014-AC001",
      "given": "the applicable business context, actor, and input for Customer Analytics không được chia sẻ giữa các Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-13-R014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-13-R014-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Customer Analytics không được chia sẻ giữa các Organization",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-13-R014-O001"
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
        "BRD-WS-13-R014-AC001",
        "BRD-WS-13-R014-AC002"
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
    "source_lines": "L540",
    "source_section": "21. Customer Analytics"
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
### BRD-WS-13-R015 — Tuân thủ Relationship Policy và Data Permission

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R015-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Tuân thủ Relationship Policy và Data Permission",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-13-R015-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-13-R015-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Tuân thủ Relationship Policy và Data Permission",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-13-R015-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-13-R015-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Tuân thủ Relationship Policy và Data Permission",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-13-R015-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-13-R015-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Tuân thủ Relationship Policy và Data Permission",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-13-R015-O001"
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
        "BRD-WS-13-R015-AC001",
        "BRD-WS-13-R015-AC002",
        "BRD-WS-13-R015-AC003",
        "BRD-WS-13-R015-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-13-R015-O001",
      "obligation_text": "Tuân thủ Relationship Policy và Data Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-13-R015-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R015 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R015 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-13-R015-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-13-R015-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-13-R015 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Tuân thủ Relationship Policy và Data Permission.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-13-015",
    "previous_temporary_key": "TMP-BRD-WS-13-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Customer Analytics",
    "source_context_sha256": "6be481274936098d942a55f4ee80908074b96fd2eb0306aef4b48993dff1edf1",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "0b55aa2fcb4e14db8ca3dfbf2f6ef84be565c50726b8e7eefda7d8002633231c",
    "source_lines": "L542",
    "source_section": "21. Customer Analytics"
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
  "title": "Tuân thủ Relationship Policy và Data Permission",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-13-R016 — Organization chỉ được xem Benchmark của chính Organization đó

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R016-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Organization chỉ được xem Benchmark của chính Organization đó",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the actor can retrieve only customer identities attributed to that actor; a customer attributed to another actor is absent and access to it is denied",
      "verifies": [
        "BRD-WS-13-R016-O001"
      ],
      "when": "the protected decision or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-13-R016-AC001"
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
    "source_lines": "L581",
    "source_section": "23. Benchmark"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R017-AC001",
      "given": "the applicable business context, actor, and input for Không được phép xem: - Revenue của Organization khác",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-13-R017-O001"
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
        "BRD-WS-13-R017-AC001"
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
    "source_lines": "L583-L585",
    "source_section": "23. Benchmark"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R018-AC001",
      "given": "the applicable business context, actor, and input for Không được phép xem: - KPI của Organization khác",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-13-R018-O001"
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
        "BRD-WS-13-R018-AC001"
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
    "source_fingerprint": "076d8072a1e09879228fa01095b1507a4b303bdfab837d6d1f9de6d9c91207d6",
    "source_lines": "L583-L586",
    "source_section": "23. Benchmark"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R019-AC001",
      "given": "the applicable business context, actor, and input for Không được phép xem: - Customer của Organization khác",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-13-R019-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-13-R019-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Không được phép xem: - Customer của Organization khác",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-13-R019-O001"
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
        "BRD-WS-13-R019-AC001",
        "BRD-WS-13-R019-AC002"
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
    "source_fingerprint": "53ff91d8b8015716aafcd972f4b34ddc4d0d0488457ffcbff85b910e348351d6",
    "source_lines": "L583-L587",
    "source_section": "23. Benchmark"
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
    "source_lines": "L595",
    "source_section": "23. Benchmark"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R021-AC001",
      "given": "the applicable business context, actor, and input for Organization có thể lựa chọn Widget cần hiển thị",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-13-R021-O001"
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
        "BRD-WS-13-R021-AC001"
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
    "source_lines": "L656",
    "source_section": "25. Widget Library"
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
    "source_lines": "L689",
    "source_section": "26. Operational Insight"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-13-R023-AC001",
      "given": "the applicable business context, actor, and input for Report không được Hard-code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-13-R023-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-13-R023-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Report không được Hard-code",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-13-R023-O001"
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
        "BRD-WS-13-R023-AC001",
        "BRD-WS-13-R023-AC002"
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
    "source_lines": "L695",
    "source_section": "27. Report as Configuration"
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
    "source_lines": "L745",
    "source_section": "28. Widget as Capability"
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
    "source_lines": "L746",
    "source_section": "28. Widget as Capability"
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
### EP-13-001 — Dashboard là cửa ngõ truy cập nhanh tới Business Object. Mọi Widget đều hỗ trợ Drill-down tới dữ…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-13-001-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Dashboard là cửa ngõ truy cập nhanh tới Business Object. Mọi Widget đều hỗ trợ Drill-down tới dữ…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "EP-13-001-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-13-001-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Dashboard là cửa ngõ truy cập nhanh tới Business Object. Mọi Widget đều hỗ trợ Drill-down tới dữ…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "EP-13-001-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "EP-13-001-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Dashboard là cửa ngõ truy cập nhanh tới Business Object. Mọi Widget đều hỗ trợ Drill-down tới dữ…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "EP-13-001-O001",
        "EP-13-001-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-13-001-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Dashboard là cửa ngõ truy cập nhanh tới Business Object. Mọi Widget đều hỗ trợ Drill-down tới dữ…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-13-001-O001",
        "EP-13-001-O002"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "EP-13-001-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Dashboard là cửa ngõ truy cập nhanh tới Business Object. Mọi Widget đều hỗ trợ Drill-down tới dữ…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "EP-13-001-O001",
        "EP-13-001-O002"
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
        "EP-13-001-AC001",
        "EP-13-001-AC003",
        "EP-13-001-AC004",
        "EP-13-001-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-001-O001",
      "obligation_text": "Dashboard là cửa ngõ truy cập nhanh tới Business Object"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-001-AC002",
        "EP-13-001-AC003",
        "EP-13-001-AC004",
        "EP-13-001-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-001-O002",
      "obligation_text": "Mọi Widget đều hỗ trợ Drill-down tới dữ liệu chi tiết theo Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "EP-13-001-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-13-001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-13-001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-13-001-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-13-001-AC001",
        "EP-13-001-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-13-001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "b3b6e454a9bdaaa3fd08554efa6f9cfa5ec03065c077d49c7792ac6ff8c35e39",
    "source_lines": "L993-L998",
    "source_section": "30. Enterprise Design Principles > EP-13-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "EP-13-002-AC001",
      "given": "a candidate Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: - Dashboard - KPI - Report… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "EP-13-002-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "EP-13-002-AC002",
      "given": "a candidate Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: - Dashboard - KPI - Report… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "EP-13-002-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "EP-13-002-AC003",
      "given": "a candidate Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: - Dashboard - KPI - Report… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "EP-13-002-O003"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "EP-13-002-AC004",
      "given": "a candidate Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: - Dashboard - KPI - Report… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "EP-13-002-O004"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "EP-13-002-AC005",
      "given": "a candidate Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: - Dashboard - KPI - Report… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "EP-13-002-O005"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-13-002-AC006",
      "given": "a Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: - Dashboard - KPI - Report… candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "EP-13-002-O001",
        "EP-13-002-O002",
        "EP-13-002-O003",
        "EP-13-002-O004",
        "EP-13-002-O005"
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
        "EP-13-002-AC001",
        "EP-13-002-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-002-O001",
      "obligation_text": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: Dashboard."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-002-AC002",
        "EP-13-002-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-002-O002",
      "obligation_text": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: KPI."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-002-AC003",
        "EP-13-002-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-002-O003",
      "obligation_text": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: Report."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-002-AC004",
        "EP-13-002-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-002-O004",
      "obligation_text": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: Analytics."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-002-AC005",
        "EP-13-002-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-002-O005",
      "obligation_text": "Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: Business Intelligence."
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
    "source_fingerprint": "9aed280038c1ff7c79ddbc2eef70dc67f62a1a3965451815233929a02d4d338c",
    "source_lines": "L1001-L1012",
    "source_section": "30. Enterprise Design Principles > EP-13-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-003-AC001",
      "given": "the applicable business context, actor, and input for Widget là Platform Capability. Widget không thuộc Dashboard. Một Widget có thể tái sử dụng trên …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-003-AC002",
      "given": "the applicable business context, actor, and input for Widget là Platform Capability. Widget không thuộc Dashboard. Một Widget có thể tái sử dụng trên …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-003-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-003-AC003",
      "given": "the applicable business context, actor, and input for Widget là Platform Capability. Widget không thuộc Dashboard. Một Widget có thể tái sử dụng trên …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-003-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-13-003-AC004",
      "given": "an unsupported or invalid business input at the boundary governed by Widget là Platform Capability. Widget không thuộc Dashboard. Một Widget có thể tái sử dụng trên …",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-13-003-O001",
        "EP-13-003-O002",
        "EP-13-003-O003"
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
        "EP-13-003-AC001",
        "EP-13-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-003-O001",
      "obligation_text": "Widget là Platform Capability"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-003-AC002",
        "EP-13-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-003-O002",
      "obligation_text": "Widget không thuộc Dashboard"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-003-AC003",
        "EP-13-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-003-O003",
      "obligation_text": "Một Widget có thể tái sử dụng trên nhiều Portal và Workspace"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Widget là Platform Capability. Widget không thuộc Dashboard. Một Widget có thể tái sử dụng trên nhiều Portal và Workspace.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-13-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Widget as Capability",
    "source_context_sha256": "a591bfbca16337e050d804aa0bd2410901039358ecea3e5469d76181e94f0d55",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "898bca38828038686159637e2e1dde51d7cbd734603c359adf285b3e435b2af6",
    "source_lines": "L1015-L1022",
    "source_section": "30. Enterprise Design Principles > EP-13-003"
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
  "stable_id": "EP-13-003",
  "title": "Widget là Platform Capability. Widget không thuộc Dashboard. Một Widget có thể tái sử dụng trên …",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-13-004 — Analytics phục vụ Decision Making. Dashboard không chỉ hiển thị dữ liệu mà còn hỗ trợ phát hiện …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-004-AC001",
      "given": "the applicable business context, actor, and input for Analytics phục vụ Decision Making. Dashboard không chỉ hiển thị dữ liệu mà còn hỗ trợ phát hiện …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-004-AC002",
      "given": "the applicable business context, actor, and input for Analytics phục vụ Decision Making. Dashboard không chỉ hiển thị dữ liệu mà còn hỗ trợ phát hiện …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-004-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-13-004-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Analytics phục vụ Decision Making. Dashboard không chỉ hiển thị dữ liệu mà còn hỗ trợ phát hiện …",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-13-004-O001",
        "EP-13-004-O002"
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
        "EP-13-004-AC001",
        "EP-13-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-004-O001",
      "obligation_text": "Analytics phục vụ Decision Making"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-004-AC002",
        "EP-13-004-AC003"
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
    "source_fingerprint": "d35b75443b0ad24c278351a344d704b2922201f01f682107f09b671a2b812547",
    "source_lines": "L1025-L1030",
    "source_section": "30. Enterprise Design Principles > EP-13-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-005-AC001",
      "given": "an operational task within the scope of Alert Rule được cấu hình hoàn toàn. Alert có thể Trigger Notification, Workflow hoặc Business Ac…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-13-005-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-005-AC002",
      "given": "an operational task within the scope of Alert Rule được cấu hình hoàn toàn. Alert có thể Trigger Notification, Workflow hoặc Business Ac…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-13-005-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-005-AC003",
      "given": "an operational task within the scope of Alert Rule được cấu hình hoàn toàn. Alert có thể Trigger Notification, Workflow hoặc Business Ac…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-13-005-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EP-13-005-AC004",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Alert Rule được cấu hình hoàn toàn. Alert có thể Trigger Notification, Workflow hoặc Business Ac…",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EP-13-005-O001",
        "EP-13-005-O002",
        "EP-13-005-O003"
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
        "EP-13-005-AC001",
        "EP-13-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-005-O001",
      "obligation_text": "Alert Rule được cấu hình hoàn toàn"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-005-AC002",
        "EP-13-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-005-O002",
      "obligation_text": "Alert có thể Trigger Notification, Workflow hoặc Business Action"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-005-AC003",
        "EP-13-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-005-O003",
      "obligation_text": "Không Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Alert Rule được cấu hình hoàn toàn. Alert có thể Trigger Notification, Workflow hoặc Business Action. Không Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-13-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-13-005",
    "source_context_sha256": "c92e19faf0c58044dca1cd2ba8269e199979dc09796aa3d56233483760a975f7",
    "source_document": "docs/BRD/BRD-WS-13.md",
    "source_fingerprint": "32ffcf9ae5fda813de01570868d63abc822b16411b591bda57a9e7557400bc96",
    "source_lines": "L1033-L1040",
    "source_section": "30. Enterprise Design Principles > EP-13-005"
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
  "stable_id": "EP-13-005",
  "title": "Alert Rule được cấu hình hoàn toàn. Alert có thể Trigger Notification, Workflow hoặc Business Ac…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-13-006 — Report, Dashboard và Widget đều được quản lý theo mô hình Configuration. Organization có thể Ena…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-13-006-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Report, Dashboard và Widget đều được quản lý theo mô hình Configuration. Organization có thể Ena…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "EP-13-006-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-13-006-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Report, Dashboard và Widget đều được quản lý theo mô hình Configuration. Organization có thể Ena…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "EP-13-006-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "EP-13-006-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Report, Dashboard và Widget đều được quản lý theo mô hình Configuration. Organization có thể Ena…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "EP-13-006-O001",
        "EP-13-006-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-13-006-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Report, Dashboard và Widget đều được quản lý theo mô hình Configuration. Organization có thể Ena…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-13-006-O001",
        "EP-13-006-O002"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "EP-13-006-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Report, Dashboard và Widget đều được quản lý theo mô hình Configuration. Organization có thể Ena…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "EP-13-006-O001",
        "EP-13-006-O002"
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
        "EP-13-006-AC001",
        "EP-13-006-AC003",
        "EP-13-006-AC004",
        "EP-13-006-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-006-O001",
      "obligation_text": "Report, Dashboard và Widget đều được quản lý theo mô hình Configuration"
    },
    {
      "acceptance_criterion_references": [
        "EP-13-006-AC002",
        "EP-13-006-AC003",
        "EP-13-006-AC004",
        "EP-13-006-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-006-O002",
      "obligation_text": "Organization có thể Enable, Disable hoặc Override theo Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "EP-13-006-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-13-006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-13-006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-13-006-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-13-006-AC001",
        "EP-13-006-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-13-006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "e8c291231c0b19a4e38a949acebb02f939b02bf439109d5ebf44b6deca9b16e1",
    "source_lines": "L1043-L1048",
    "source_section": "30. Enterprise Design Principles > EP-13-006"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-007-AC001",
      "given": "the applicable business context, actor, and input for Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-007-AC002",
      "given": "the applicable business context, actor, and input for Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-007-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-007-AC003",
      "given": "the applicable business context, actor, and input for Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-007-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-007-AC004",
      "given": "the applicable business context, actor, and input for Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-007-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-007-AC005",
      "given": "the applicable business context, actor, and input for Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-007-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-007-AC006",
      "given": "the applicable business context, actor, and input for Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-007-O006"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-007-AC007",
      "given": "the applicable business context, actor, and input for Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-007-O007"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-007-AC008",
      "given": "the applicable business context, actor, and input for Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-007-O008"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-007-AC009",
      "given": "the applicable business context, actor, and input for Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-13-007-O009"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-13-007-AC010",
      "given": "an unsupported or invalid business input at the boundary governed by Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Curre…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-13-007-O001",
        "EP-13-007-O002",
        "EP-13-007-O003",
        "EP-13-007-O004",
        "EP-13-007-O005",
        "EP-13-007-O006",
        "EP-13-007-O007",
        "EP-13-007-O008",
        "EP-13-007-O009"
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
        "EP-13-007-AC001",
        "EP-13-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O001",
      "obligation_text": "Localization được áp dụng xuyên suốt: Dashboard."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC002",
        "EP-13-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O002",
      "obligation_text": "Localization được áp dụng xuyên suốt: Report."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC003",
        "EP-13-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O003",
      "obligation_text": "Localization được áp dụng xuyên suốt: Widget."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC004",
        "EP-13-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O004",
      "obligation_text": "Localization được áp dụng xuyên suốt: Analytics Bao gồm."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC005",
        "EP-13-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O005",
      "obligation_text": "Localization được áp dụng xuyên suốt: Currency."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC006",
        "EP-13-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O006",
      "obligation_text": "Localization được áp dụng xuyên suốt: Language."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC007",
        "EP-13-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O007",
      "obligation_text": "Localization được áp dụng xuyên suốt: Measurement."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC008",
        "EP-13-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O008",
      "obligation_text": "Localization được áp dụng xuyên suốt: Temperature."
    },
    {
      "acceptance_criterion_references": [
        "EP-13-007-AC009",
        "EP-13-007-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-13-007-O009",
      "obligation_text": "Localization được áp dụng xuyên suốt: Date Time Format."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-13-007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-13-007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-13-007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-13-007 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
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
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-13-007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "331b878c5a4412e2b8cb91aaebe298040ca35c8a6cb47982f594a53dc174fdb2",
    "source_lines": "L1051-L1067",
    "source_section": "30. Enterprise Design Principles > EP-13-007"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-13-008-AC001",
      "given": "an operational task within the scope of Operational Intelligence và Business Intelligence phải phục vụ trực tiếp cho việc vận hành Platf…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-13-008-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EP-13-008-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Operational Intelligence và Business Intelligence phải phục vụ trực tiếp cho việc vận hành Platf…",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EP-13-008-O001"
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
        "EP-13-008-AC001",
        "EP-13-008-AC002"
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
    "source_fingerprint": "e16a6efb0b6d8942e85e89e801886137aaf0a0c396a8a7fa0644c427584fc619",
    "source_lines": "L1070-L1073",
    "source_section": "30. Enterprise Design Principles > EP-13-008"
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
