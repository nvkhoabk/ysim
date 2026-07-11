---
document_code: BRD-WS-13
document_name: Reporting, Analytics & Operational Intelligence
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-13
---

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