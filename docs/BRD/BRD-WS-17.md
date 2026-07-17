---
document_code: "BRD-WS-17"
document_id: "BRD-WS-17"
title: "Platform Operations, Monitoring, Scheduler & Background Processing"
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

# BRD Workshop 17

# Platform Operations, Monitoring, Scheduler & Background Processing

---

# 1. Workshop Objective

Workshop này xác định toàn bộ năng lực vận hành (Operations Capability) của nền tảng YSim.

Bao gồm:

- Platform Operations Center
- Monitoring
- Metrics
- Alerting
- Health Check
- Scheduler
- Background Jobs
- Worker Management
- Queue Management
- Distributed Processing
- Maintenance
- Backup
- Disaster Recovery
- Capacity Management
- Operational Dashboard
- Feature Flag
- Kill Switch
- Runbook
- Replay Platform
- SLO / SLA Monitoring

Workshop này không bao gồm:

- Infrastructure Provisioning
- CI/CD Pipeline
- Kubernetes Deployment
- Cloud Infrastructure Implementation

(Các nội dung trên sẽ được mô tả trong SDD và Platform Operations Manual.)

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| Operation Policy | Master |
| Scheduler Job | Master |
| Job Execution | Transaction |
| Worker | Master |
| Queue Monitor | Transaction |
| System Health | Transaction |
| Alert Rule | Master |
| Alert Event | Transaction |
| Maintenance Window | Master |
| Backup Policy | Master |
| Disaster Recovery Policy | Master |
| Capacity Policy | Master |
| Runbook | Master |
| Feature Flag | Master |

---

# 3. Platform Operations Center

Platform có một Platform Operations Center thống nhất.

Operations Center là trung tâm điều hành của toàn bộ hệ thống.

Operations Center quản lý:

- Monitoring
- Queue
- Scheduler
- Worker
- Connector
- Payment
- Background Job
- Alert
- Health
- Maintenance
- Backup
- Replay
- Capacity

Operations Center cung cấp giao diện tập trung cho Operator theo dõi và xử lý toàn bộ hoạt động của Platform.

---

# 4. Monitoring

Monitoring bao phủ toàn bộ Platform.

Bao gồm:

- Business Monitoring
- API Monitoring
- Queue Monitoring
- Worker Monitoring
- Scheduler Monitoring
- Connector Monitoring
- Payment Monitoring
- Notification Monitoring
- Infrastructure Monitoring
- Database Monitoring
- Cache Monitoring
- Storage Monitoring
- Network Monitoring

Monitoring được chuẩn hóa và có khả năng mở rộng.

Mọi thành phần của Platform đều có khả năng phát sinh Metrics và Health Status.

---

# 5. Health Check

Health Check hỗ trợ nhiều cấp.

Bao gồm:

- Platform
- Service
- Module
- Connector
- Queue
- Worker
- Scheduler
- Database
- Cache
- Storage
- External Dependency

Health Status bao gồm:

- Healthy
- Warning
- Critical
- Maintenance
- Offline

Health Status được cập nhật theo thời gian thực hoặc Near Real-time tùy từng thành phần.

---

# 6. Metrics

Metrics được chuẩn hóa trên toàn Platform.

Ví dụ:

- Request Count
- Transactions Per Second (TPS)
- Average Response Time
- Error Rate
- Success Rate
- Queue Length
- Retry Count
- Dead Letter Queue Count
- Active Worker
- CPU Usage
- Memory Usage
- Disk Usage
- Network Throughput

Metrics được sử dụng cho:

- Dashboard
- Alert
- Capacity Planning
- SLA Monitoring
- SLO Monitoring

---

# 7. Alert Rule

Alert Rule là Business Object.

Alert Rule quản lý:

- Alert Condition
- Threshold
- Priority
- Escalation Policy
- Notification Policy
- Target Audience

Alert Rule được cấu hình.

Không Hard-code.

Alert Rule có thể được kích hoạt bởi:

- Metrics
- Health Status
- Business Event
- Scheduler
- Queue
- Worker
- External Dependency

---

# 8. Alert Channel

Alert được gửi theo Notification Preference của từng User.

Các kênh hỗ trợ:

- Email
- SMS
- Push Notification
- Microsoft Teams
- Slack
- Telegram
- Personal Inbox

Personal Inbox là kênh bắt buộc.

Mọi Alert đều được lưu trong Personal Inbox để đảm bảo không mất thông tin.

Notification Channel được quyết định theo Notification Matrix và Notification Policy.

---

# 9. Scheduler

Scheduler là Business Object.

Scheduler chịu trách nhiệm lập lịch thực thi các Background Job.

Scheduler hỗ trợ:

- Cron Expression
- Fixed Interval
- Manual Trigger
- Business Event Trigger

Scheduler được cấu hình.

Không Hard-code.

Scheduler có thể được Enable hoặc Disable theo Operation Policy.

---

# 10. Scheduler Trigger

Scheduler hỗ trợ nhiều cơ chế Trigger.

Bao gồm:

- Cron Trigger
- Fixed Interval Trigger
- Manual Trigger
- Business Event Trigger

Ví dụ:

PaymentSucceeded

↓

Delay 30 Minutes

↓

Check eSIM Activation

Scheduler cũng có thể Publish Business Event sau khi hoàn thành Job.

Scheduler Trigger được cấu hình và có thể thay đổi mà không cần sửa mã nguồn.

---

# 11. Job Execution

Job Execution là Business Object.

Job Execution ghi nhận:

- Scheduler Job
- Worker
- Trigger Source
- Start Time
- End Time
- Execution Duration
- Retry Count
- Execution Result
- Execution Log
- Status

Job Execution là cơ sở cho:

- Monitoring
- Audit
- Replay
- Retry
- Capacity Planning

---

# 12. Worker

Worker là Business Object.

Worker chịu trách nhiệm xử lý Background Job.

Một Job có thể được xử lý bởi nhiều Worker.

Worker được quản lý độc lập.

Thông tin Worker bao gồm:

- Worker Name
- Worker Type
- Version
- Status
- Capacity
- Current Load

Worker được Monitoring theo thời gian thực.

------

# 13. Queue Monitoring

Queue Monitoring là thành phần giám sát toàn bộ Message Queue trên Platform.

Queue Monitoring theo dõi:

- Pending
- Processing
- Completed
- Retry
- Failed
- Dead Letter Queue (DLQ)
- Delayed
- Scheduled

Đối với mỗi Queue, hệ thống theo dõi:

- Queue Length
- Processing Speed
- Consumer Count
- Average Processing Time
- Retry Rate
- Failure Rate

Queue Monitoring hỗ trợ Dashboard và Alert theo thời gian thực hoặc Near Real-time.

---

# 14. Operation Retry

Operation Retry là cơ chế Retry ở cấp Platform Operation.

Operation Retry độc lập với Connector Retry.

Operation Retry hỗ trợ:

- Retry Job
- Retry Queue Message
- Retry Notification
- Retry Fulfillment
- Retry Procurement
- Retry Settlement
- Retry Synchronization

Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp.

Mọi thao tác Retry đều được ghi nhận trong Audit Log.

---

# 15. Maintenance Window

Maintenance Window là Business Object.

Maintenance Window được sử dụng để lập lịch bảo trì hệ thống.

Maintenance có thể áp dụng theo:

- Platform
- Organization
- Storefront
- Module
- Connector
- Service
- API
- Queue
- Scheduler Job

Maintenance Window bao gồm:

- Start Time
- End Time
- Scope
- Description
- Maintenance Type
- Notification Policy
- Approval Status

Maintenance Window được quản lý tập trung.

---

# 16. Backup Policy

Backup Policy là Business Object.

Backup Policy hỗ trợ:

- Manual Backup
- Scheduled Backup
- Full Backup
- Incremental Backup
- Differential Backup (mở rộng)

Backup Policy quản lý:

- Backup Schedule
- Backup Retention
- Backup Destination
- Encryption
- Verification Policy

Backup Policy được cấu hình.

Không Hard-code.

---

# 17. Disaster Recovery

Platform hỗ trợ Disaster Recovery.

Bao gồm:

- Manual Recovery
- Semi-Automatic Recovery
- Automatic Recovery

Phiên bản hiện tại ưu tiên:

- Manual Recovery

Kiến trúc hỗ trợ mở rộng Automatic Recovery trong tương lai.

Disaster Recovery Policy bao gồm:

- Recovery Procedure
- Recovery Priority
- Recovery Target
- Notification
- Approval

---

# 18. Capacity Policy

Capacity Policy là Business Object.

Capacity Policy quản lý:

- Worker Capacity
- Queue Capacity
- Storage Threshold
- CPU Threshold
- Memory Threshold
- Network Threshold
- Concurrent Job Limit

Capacity Policy phục vụ:

- Capacity Planning
- Alert
- Auto Scaling (Future Version)

Capacity Policy được cấu hình theo từng Environment.

---

# 19. Operational Dashboard

Platform có Dashboard dành riêng cho Operator.

Operational Dashboard hiển thị:

- Platform Health
- Queue Status
- Worker Status
- Scheduler Status
- Connector Status
- Alert Summary
- Running Jobs
- Failed Jobs
- Retry Queue
- Backup Status
- Maintenance Schedule
- Capacity Usage
- SLO/SLA Status

Mỗi Widget trên Dashboard cho phép truy cập nhanh đến chức năng quản trị tương ứng.

Dashboard hỗ trợ tùy biến theo từng Operator.

---

# 20. Operation Permission

Operator sử dụng Permission riêng.

Operation Permission được quản lý bởi Security Platform.

Permission có thể áp dụng cho:

- Queue
- Scheduler
- Worker
- Replay
- Retry
- Backup
- Restore
- Maintenance
- Alert
- Feature Flag

Mọi thao tác đều:

- Kiểm tra Permission
- Ghi Audit
- Tuân thủ Security Policy

---

# 21. Maintenance Notification

Maintenance phải gửi Notification trước khi bắt đầu.

Notification được gửi theo Notification Policy.

Các nhóm nhận Notification có thể bao gồm:

- Platform Operator
- Organization Administrator
- Storefront Administrator
- Internal User
- Customer (nếu ảnh hưởng dịch vụ)

Maintenance Notification hỗ trợ:

- Thông báo trước
- Thông báo bắt đầu
- Thông báo kết thúc
- Thông báo kéo dài thời gian bảo trì (nếu có)

Mọi Maintenance Notification đều được lưu trong Personal Inbox.

---

# 22. Scheduler Priority

Scheduler hỗ trợ Priority.

Bao gồm:

- Critical
- High
- Normal
- Low

Business Critical Job luôn được ưu tiên.

Ví dụ:

- Payment Processing
- Procurement
- Fulfillment
- Settlement

được ưu tiên cao hơn:

- Marketing Campaign
- Report Generation
- Analytics Refresh

Priority được Scheduler Engine sử dụng để tối ưu việc phân bổ Worker và Queue.

------

# 23. Auto Scaling

Kiến trúc Platform hỗ trợ Auto Scaling.

Version hiện tại chưa triển khai tự động mở rộng tài nguyên.

Tuy nhiên, kiến trúc được thiết kế sẵn để hỗ trợ:

- Worker Auto Scaling
- Queue Consumer Auto Scaling
- Scheduler Scaling
- API Service Scaling
- Connector Scaling

Auto Scaling có thể được kích hoạt dựa trên:

- CPU Usage
- Memory Usage
- Queue Length
- Active Request
- Concurrent Job
- Throughput
- Capacity Policy

---

# 24. Operational Audit

Mọi hoạt động vận hành đều phát sinh Audit.

Ví dụ:

- Retry Job
- Replay Event
- Replay Queue
- Pause Queue
- Resume Queue
- Drain Queue
- Restart Worker
- Cancel Job
- Backup
- Restore
- Maintenance
- Feature Flag Change
- Kill Switch Change

Operational Audit tuân thủ Security Policy.

Audit không được phép chỉnh sửa.

---

# 25. Operation Policy

Operation Policy là Business Object.

Operation Policy quản lý:

- Scheduler Policy
- Queue Policy
- Retry Policy
- Timeout Policy
- Worker Policy
- Capacity Policy
- Maintenance Policy
- Replay Policy
- Alert Policy

Operation Policy được Versioning.

Hỗ trợ:

- Effective Date
- Approval
- Audit
- Rollback

Operation Policy không được Hard-code.

---

# 26. Business Scheduler

Scheduler không chỉ hỗ trợ Cron.

Scheduler còn hỗ trợ Business Event Trigger.

Ví dụ:

PaymentSucceeded

↓

Delay 30 Minutes

↓

Check eSIM Activation

Hoặc:

FulfillmentCompleted

↓

Delay 7 Days

↓

Send Customer Satisfaction Survey

Business Scheduler giúp tự động hóa quy trình nghiệp vụ mà không cần lập trình bổ sung.

---

# 27. Organization Operations

Operations Capability không thuộc Organization.

Operations chỉ thuộc Platform.

Organization không có quyền:

- Restart Worker
- Pause Queue
- Replay Event
- Retry Queue
- Backup
- Restore
- Maintenance Platform

Organization chỉ được xem các thông tin Monitoring được Platform chia sẻ theo Permission.

---

# 28. Maintenance Level

Maintenance hỗ trợ nhiều cấp.

Bao gồm:

- Global
- Organization
- Storefront
- Module
- Connector
- Service
- API
- Queue
- Scheduler Job

Maintenance Level được lựa chọn khi tạo Maintenance Window.

Việc bảo trì ở phạm vi nhỏ không ảnh hưởng tới các thành phần khác ngoài phạm vi được chỉ định.

---

# 29. Operation Business Events

Operations Platform Publish Business Event.

Ví dụ:

- JobStarted
- JobCompleted
- JobFailed
- QueuePaused
- QueueResumed
- QueueOverflowDetected
- WorkerStarted
- WorkerStopped
- BackupStarted
- BackupCompleted
- RestoreCompleted
- MaintenanceStarted
- MaintenanceCompleted
- AlertRaised
- AlertResolved

Các Business Event này có thể được:

- Monitoring Platform Subscribe
- Notification Platform Subscribe
- Reporting Platform Subscribe
- Analytics Platform Subscribe

---

# 30. Enterprise Operations Principle

Platform áp dụng nguyên lý:

**Mọi tác vụ vận hành phải có khả năng:**

- Observable
- Auditable
- Configurable
- Recoverable
- Automatable

Operator không thao tác trực tiếp trên hạ tầng nếu Platform đã cung cấp chức năng tương ứng.

Đây là nguyên lý cốt lõi của Enterprise Operations Foundation.

---

# 31. Runbook

Runbook là Business Object.

Runbook mô tả quy trình xử lý chuẩn đối với từng sự cố hoặc tình huống vận hành.

Ví dụ:

- Payment Gateway Down
- Supplier Connector Timeout
- Queue Overflow
- Email Service Failure
- Worker Crash
- Database Slow Query
- Cache Failure

Runbook bao gồm:

- Description
- Preconditions
- Handling Steps
- Verification Steps
- Escalation Procedure
- Related Alert Rules
- Related Business Events

Alert có thể liên kết trực tiếp với Runbook.

---

# 32. Feature Flag & Kill Switch

Platform hỗ trợ:

- Feature Flag
- Kill Switch

Feature Flag cho phép:

- Bật/Tắt tính năng
- Triển khai từng phần
- A/B Testing (Future)

Kill Switch cho phép dừng ngay lập tức:

- Auto Procurement
- Fulfillment
- Promotion Engine
- Notification Channel
- Connector
- Payment Gateway

Không cần Deploy lại hệ thống.

Mọi thay đổi đều được Audit.

---

# 33. Operational Command Center

Operations Center hỗ trợ các tác vụ quản trị.

Bao gồm:

- Retry Job
- Replay Event
- Replay Queue
- Pause Queue
- Resume Queue
- Drain Queue
- Restart Worker
- Cancel Job
- Force Scheduler Trigger
- Trigger Health Check
- Trigger Backup
- Trigger Restore

Mọi thao tác yêu cầu:

- Permission
- Audit
- Runbook (nếu có)

---

# 34. Replay Platform

Platform hỗ trợ Replay.

Replay bao gồm:

- Replay Business Event
- Replay Queue Message
- Replay Notification
- Replay Fulfillment
- Replay Procurement
- Replay Settlement

Replay giúp xử lý các trường hợp lỗi mà không cần viết Script hoặc thao tác trực tiếp trên Database.

Replay chỉ được thực hiện bởi Operator có Permission phù hợp.

---

# 35. Chaos Readiness

Kiến trúc hỗ trợ Chaos Readiness.

Version hiện tại chưa triển khai.

Kiến trúc cho phép mô phỏng:

- Connector Down
- Queue Delay
- Payment Timeout
- Email Failure
- Worker Crash
- Database Unavailable
- Cache Failure

Chaos Readiness phục vụ kiểm thử khả năng chịu lỗi và phục hồi của Platform.

---

# 36. SLO / SLA Monitoring

Platform hỗ trợ theo dõi:

- Service Level Objective (SLO)
- Service Level Agreement (SLA)

Ví dụ:

- Payment Callback < 30 giây
- Fulfillment < 2 phút
- Notification Email < 1 phút
- API Availability ≥ 99.9%
- Scheduler Success Rate ≥ 99.5%

SLO/SLA được sử dụng cho:

- Dashboard
- Alert
- Capacity Planning
- Operational Review
- Service Improvement

Vi phạm SLO hoặc SLA có thể kích hoạt Alert Rule hoặc Escalation Policy.

------

# 37. Business Decisions (Locked)

## BD-17-001

Platform có một Platform Operations Center thống nhất.

Operations Center là trung tâm điều hành toàn bộ nền tảng.

---

## BD-17-002

Monitoring bao phủ toàn Platform.

Bao gồm:

- Business
- API
- Queue
- Worker
- Scheduler
- Connector
- Payment
- Notification
- Database
- Cache
- Infrastructure

---

## BD-17-003

Health Check hỗ trợ đầy đủ các thành phần của Platform.

Health Status được chuẩn hóa.

---

## BD-17-004

Metrics được chuẩn hóa.

Metrics là nguồn dữ liệu cho:

- Dashboard
- Alert
- Capacity Planning
- SLO
- SLA

---

## BD-17-005

Alert Rule là Business Object.

Alert Rule được cấu hình.

Không Hard-code.

---

## BD-17-006

Alert được gửi theo Notification Preference.

Personal Inbox luôn là kênh nhận mặc định.

---

## BD-17-007

Scheduler là Business Object.

Scheduler hỗ trợ:

- Cron
- Fixed Interval
- Manual Trigger
- Business Event Trigger

---

## BD-17-008

Job Execution là Business Object.

Mọi Job đều sinh Job Execution.

---

## BD-17-009

Worker là Business Object.

Một Job có thể được xử lý bởi nhiều Worker.

---

## BD-17-010

Queue Monitoring hỗ trợ nhiều trạng thái.

Bao gồm:

- Pending
- Processing
- Completed
- Retry
- Failed
- DLQ

---

## BD-17-011

Operation Retry độc lập Connector Retry.

---

## BD-17-012

Maintenance Window là Business Object.

Maintenance hỗ trợ nhiều cấp.

---

## BD-17-013

Backup Policy là Business Object.

---

## BD-17-014

Platform hỗ trợ Disaster Recovery.

Kiến trúc hỗ trợ:

- Manual
- Semi Automatic
- Automatic

---

## BD-17-015

Capacity Policy là Business Object.

Kiến trúc hỗ trợ Auto Scaling trong tương lai.

---

## BD-17-016

Platform có Operational Dashboard dành riêng cho Operator.

---

## BD-17-017

Operator sử dụng Permission riêng.

Mọi thao tác đều được Security Platform kiểm soát.

---

## BD-17-018

Maintenance phải gửi Notification trước khi thực hiện.

---

## BD-17-019

Scheduler hỗ trợ Priority.

Business Critical Job luôn được ưu tiên.

---

## BD-17-020

Kiến trúc hỗ trợ Auto Scaling.

Version hiện tại chưa triển khai.

---

## BD-17-021

Operational Audit ghi nhận toàn bộ thao tác vận hành.

---

## BD-17-022

Operation Policy là Business Object.

Operation Policy được Versioning.

---

## BD-17-023

Scheduler hỗ trợ Business Event Trigger.

---

## BD-17-024

Organization không có Operations Capability.

Operations chỉ thuộc Platform.

---

## BD-17-025

Maintenance hỗ trợ nhiều Scope.

---

## BD-17-026

Operations Platform Publish Business Event.

---

## BD-17-027

Runbook là Business Object.

---

## BD-17-028

Platform hỗ trợ Feature Flag và Kill Switch.

---

## BD-17-029

Platform hỗ trợ Operational Command Center.

---

## BD-17-030

Platform hỗ trợ Replay.

---

## BD-17-031

Kiến trúc hỗ trợ Chaos Readiness.

Version hiện tại chưa triển khai.

---

## BD-17-032

Platform hỗ trợ SLO và SLA Monitoring.

---

# 38. Enterprise Design Principles

## EP-17-001

Platform Operations được quản lý tập trung thông qua Platform Operations Center.

---

## EP-17-002

Monitoring phải bao phủ toàn Platform.

---

## EP-17-003

Scheduler, Queue, Worker, Alert và Runbook đều là Business Object.

---

## EP-17-004

Operation Policy được cấu hình.

Không Hard-code.

---

## EP-17-005

Operation Retry độc lập Connector Retry.

---

## EP-17-006

Platform hỗ trợ Replay và Recoverable Operation.

---

## EP-17-007

Platform hỗ trợ Feature Flag và Kill Switch.

Không cần Deploy để bật hoặc tắt chức năng.

---

## EP-17-008

Mọi thao tác Operations đều phải:

- Kiểm tra Permission
- Ghi Audit
- Tuân thủ Runbook (nếu có)

---

## EP-17-009

Operations Platform Publish Business Event.

---

## EP-17-010

Mọi tác vụ vận hành của Platform phải bảo đảm:

- Observable
- Auditable
- Configurable
- Recoverable
- Automatable

Operator không thao tác trực tiếp trên hạ tầng nếu Platform đã hỗ trợ chức năng tương ứng.

---

# 39. Published Business Events

Ví dụ:

- JobStarted
- JobCompleted
- JobFailed
- QueuePaused
- QueueResumed
- QueueOverflowDetected
- WorkerStarted
- WorkerStopped
- BackupStarted
- BackupCompleted
- RestoreCompleted
- MaintenanceStarted
- MaintenanceCompleted
- AlertRaised
- AlertResolved
- ReplayCompleted
- FeatureFlagChanged
- KillSwitchActivated

---

# 40. Consumed Business Events

Ví dụ:

- PaymentSucceeded
- ConnectorFailed
- HealthStatusChanged
- ConfigurationPublished
- SchedulerTriggered
- SecurityAlertRaised
- OrganizationCreated
- DeploymentCompleted

---

# 41. Business Capabilities Covered

Workshop này bao gồm các Business Capability:

- Platform Operations Center
- Monitoring
- Health Check
- Metrics
- Alert Management
- Scheduler
- Background Processing
- Worker Management
- Queue Management
- Retry Management
- Replay Management
- Maintenance Management
- Backup Management
- Disaster Recovery
- Capacity Management
- Feature Flag
- Kill Switch
- Runbook Management
- Operational Dashboard
- SLO Monitoring
- SLA Monitoring

---

# 42. Traceability

Workshop này kế thừa toàn bộ các quyết định từ:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04
- BRD-WS-05
- BRD-WS-06
- BRD-WS-07
- BRD-WS-08
- BRD-WS-09
- BRD-WS-10
- BRD-WS-11
- BRD-WS-12
- BRD-WS-13
- BRD-WS-14
- BRD-WS-15
- BRD-WS-16

WS-17 hoàn thiện Enterprise Operations Foundation cho toàn bộ nền tảng YSim.

---

# 43. Workshop Status

Status:

**FROZEN**

Workshop này xác định toàn bộ Enterprise Operations Foundation của YSim.

---

# 44. Platform Foundation Summary

Nhóm Platform Foundation của YSim bao gồm:

- WS-14 — Configuration Foundation
- WS-15 — Integration Foundation
- WS-16 — Security Foundation
- WS-17 — Operations Foundation

Bốn Workshop này tạo thành **Platform Foundation Layer**, là nền tảng chung cho:

- Business Domain
- Technical Architecture
- API
- Database
- Integration
- Security
- Operations
- DevOps
- Platform Governance

---

# 45. Next Step

Sau khi hoàn thành WS-17, nhóm **Platform Foundation Workshops** được xem là hoàn tất.

Bước tiếp theo là xây dựng tài liệu:

**Enterprise Platform Architecture Overview (EPAO)**

EPAO sẽ tổng hợp và chuẩn hóa toàn bộ kiến trúc nền tảng của YSim từ các Workshop:

- WS-14 — Configuration Foundation
- WS-15 — Integration Foundation
- WS-16 — Security Foundation
- WS-17 — Operations Foundation

EPAO đóng vai trò là tài liệu kiến trúc nền tảng (Platform Architecture Blueprint), làm cơ sở cho:

- System Design Document (SDD)
- Database Design (DBD)
- API Specification
- Codex Implementation Prompt (CIP)
- Platform Operations Manual
- Technical Training
- Enterprise Architecture Governance

---

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-001 — Platform có một Platform Operations Center thống nhất. Operations Center là trung tâm điều hành …

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
      "requirement_id": "BD-17-001",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "9ade89830ed7bb45429a1e98f369119b566f9a8b0e040b7df5c0ee5c4a70259b"
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
        "BD-17-001-AC001",
        "BD-17-001-AC003",
        "BD-17-001-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-001-O001",
      "obligation_text": "Platform có một Platform Operations Center thống nhất"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-001-AC002",
        "BD-17-001-AC003",
        "BD-17-001-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-001-O002",
      "obligation_text": "Operations Center là trung tâm điều hành toàn bộ nền tảng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform có một Platform Operations Center thống nhất. Operations Center là trung tâm điều hành toàn bộ nền tảng.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Platform Operations Center",
    "source_context_sha256": "6f313bff0676a2a75ceb119b5d9e08390c018ce16405f0ee72f081b150946add",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "9ade89830ed7bb45429a1e98f369119b566f9a8b0e040b7df5c0ee5c4a70259b",
    "source_lines": "L1479-L1564",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-001"
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
  "stable_id": "BD-17-001",
  "title": "Platform có một Platform Operations Center thống nhất. Operations Center là trung tâm điều hành …",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-002 — Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-17-002",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "dd428ee138959684bce7044f71e753a6f748b4e86ed818f15406924274bfcece"
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
        "BD-17-002-AC001",
        "BD-17-002-AC012",
        "BD-17-002-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O001",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Business"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC002",
        "BD-17-002-AC012",
        "BD-17-002-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O002",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: API"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC003",
        "BD-17-002-AC012",
        "BD-17-002-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O003",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Queue"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC004",
        "BD-17-002-AC012",
        "BD-17-002-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O004",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Worker"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC005",
        "BD-17-002-AC012",
        "BD-17-002-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O005",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Scheduler"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC006",
        "BD-17-002-AC012",
        "BD-17-002-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O006",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Connector"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC007",
        "BD-17-002-AC012",
        "BD-17-002-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O007",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Payment"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC008",
        "BD-17-002-AC012",
        "BD-17-002-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O008",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Notification"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC009",
        "BD-17-002-AC012",
        "BD-17-002-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O009",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Database"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC010",
        "BD-17-002-AC012",
        "BD-17-002-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O010",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Cache"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC011",
        "BD-17-002-AC012",
        "BD-17-002-AC013"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O011",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Infrastructure"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-002 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-17-002-AC012"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-17-002-AC001",
        "BD-17-002-AC002",
        "BD-17-002-AC003",
        "BD-17-002-AC004",
        "BD-17-002-AC005",
        "BD-17-002-AC006",
        "BD-17-002-AC007",
        "BD-17-002-AC008",
        "BD-17-002-AC009",
        "BD-17-002-AC010",
        "BD-17-002-AC011"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-002 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Connector - Payment - Notification - Database - Cache - Infrastructure",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-002",
    "source_context_sha256": "6a6836d4eaf27e9a6920f740020dc0e76da2bfa538f48221b42752d9a86dd45d",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "dd428ee138959684bce7044f71e753a6f748b4e86ed818f15406924274bfcece",
    "source_lines": "L1566-L1788",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-002"
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
  "stable_id": "BD-17-002",
  "title": "Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-003 — Health Check hỗ trợ đầy đủ các thành phần của Platform. Health Status được chuẩn hóa

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
      "requirement_id": "BD-17-003",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "6e1da3ed522235b8b1d2ff3d98823d4abc99bdbcfee2d4ec65c4b088182e4abc"
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
        "BD-17-003-AC001",
        "BD-17-003-AC003",
        "BD-17-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-003-O001",
      "obligation_text": "Health Check hỗ trợ đầy đủ các thành phần của Platform"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-003-AC002",
        "BD-17-003-AC003",
        "BD-17-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-003-O002",
      "obligation_text": "Health Status được chuẩn hóa"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Health Check hỗ trợ đầy đủ các thành phần của Platform. Health Status được chuẩn hóa.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-003",
    "source_context_sha256": "cc7aba8681bfaf48783f96ec033e7be98250f0c97d3ee952ab867e4647c12f4c",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "6e1da3ed522235b8b1d2ff3d98823d4abc99bdbcfee2d4ec65c4b088182e4abc",
    "source_lines": "L1790-L1875",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-003"
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
  "stable_id": "BD-17-003",
  "title": "Health Check hỗ trợ đầy đủ các thành phần của Platform. Health Status được chuẩn hóa",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-004 — Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: - Dashboard - Alert - Capacity Planning - …

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-010"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-17-004",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "eb0a43bacec1cb60b4498d050886f4d83747050c5bd4b4171476b902c017376a"
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
        "BD-17-004-AC001",
        "BD-17-004-AC006",
        "BD-17-004-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-004-O001",
      "obligation_text": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: Dashboard"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-004-AC002",
        "BD-17-004-AC006",
        "BD-17-004-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-004-O002",
      "obligation_text": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: Alert"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-004-AC003",
        "BD-17-004-AC006",
        "BD-17-004-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-004-O003",
      "obligation_text": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: Capacity Planning"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-004-AC004",
        "BD-17-004-AC006",
        "BD-17-004-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-004-O004",
      "obligation_text": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: SLO"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-004-AC005",
        "BD-17-004-AC006",
        "BD-17-004-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-004-O005",
      "obligation_text": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: SLA"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: - Dashboard - Alert - Capacity Planning - SLO - SLA",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-010"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-004",
    "source_context_sha256": "8665c4437b590e1611f3ed6ab0ff3e7c972f7da6f1d33ead96d35fbbb43b7284",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "eb0a43bacec1cb60b4498d050886f4d83747050c5bd4b4171476b902c017376a",
    "source_lines": "L1877-L1996",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-004"
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
  "stable_id": "BD-17-004",
  "title": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: - Dashboard - Alert - Capacity Planning - …",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-005 — Alert Rule là Business Object. Alert Rule được cấu hình. Không Hard-code

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
  "normative_statement": "Alert Rule là Business Object. Alert Rule được cấu hình. Không Hard-code.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-005",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Alert Rule",
    "source_context_sha256": "20268973697bfc64bdd4536c7deca7ea62de0777e79a4ef2903bd3f315dcad18",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "0351806295bddbe1be0f5303d8c5b3052077f5cc7e09f72ff3a41bbcca0578dc",
    "source_fingerprint_before_c3": "d7d2758777eb46a2c6e43cfba30bdcfe3d106c345ac8a6d1fa325b2610e98c87",
    "source_lines": "L1998-L2058",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-005"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-17-R032",
      "BRD-WS-17-R033",
      "BRD-WS-17-R034"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-17-005",
  "title": "Alert Rule là Business Object. Alert Rule được cấu hình. Không Hard-code",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-006 — Alert được gửi theo Notification Preference. Personal Inbox luôn là kênh nhận mặc định

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
  "normative_statement": "Alert được gửi theo Notification Preference. Personal Inbox luôn là kênh nhận mặc định.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-006",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-006",
    "source_context_sha256": "da00372cb2b839eb3d3445a3cb7fb61416558a5cc85f95e72c2bf933f422f32b",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "81c188ab89c8da5d5cec6fd15e138d69c23fa10c559fbe445bcbc997e5d72ceb",
    "source_fingerprint_before_c3": "667c30202eebbbf2c1922910c1f6b9da85f46983123ed38501eb73dec81196c7",
    "source_lines": "L2060-L2119",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-006"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-17-R035",
      "BRD-WS-17-R036"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-17-006",
  "title": "Alert được gửi theo Notification Preference. Personal Inbox luôn là kênh nhận mặc định",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-007 — Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Busin…

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
  "normative_statement": "Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Business Event Trigger",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-007",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Scheduler",
    "source_context_sha256": "867847cfa5f35a218d9ca4c09054fad6f3806ef2db0bd26361426efbaad00983",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "ef940dda20d74c0c7752f25358f9ebfe041820f877c32b3438a45a2d5b31ea86",
    "source_fingerprint_before_c3": "11ffc66ac3a680ed0c555ce7ca04285c49e6868880290ea13a6f46af400d5cd3",
    "source_lines": "L2121-L2182",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-007"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-17-R037",
      "BRD-WS-17-R038",
      "BRD-WS-17-R039",
      "BRD-WS-17-R040"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-17-007",
  "title": "Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Busin…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-008 — Job Execution là Business Object. Mọi Job đều sinh Job Execution

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
      "requirement_id": "BD-17-008",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "139d655a19d91e6a93b310f226c8c1845dfeadfd65d72735739105381e5a13c0"
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
        "BD-17-008-AC001",
        "BD-17-008-AC003",
        "BD-17-008-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-008-O001",
      "obligation_text": "Job Execution là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-008-AC002",
        "BD-17-008-AC003",
        "BD-17-008-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-008-O002",
      "obligation_text": "Mọi Job đều sinh Job Execution"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Job Execution là Business Object. Mọi Job đều sinh Job Execution.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Job Execution",
    "source_context_sha256": "3aa3cbed38956908b99936821c2069982c56bb29365731aac2a5c41680a3f107",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "139d655a19d91e6a93b310f226c8c1845dfeadfd65d72735739105381e5a13c0",
    "source_lines": "L2184-L2269",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-008"
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
  "stable_id": "BD-17-008",
  "title": "Job Execution là Business Object. Mọi Job đều sinh Job Execution",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-009 — Worker là Business Object. Một Job có thể được xử lý bởi nhiều Worker

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
      "requirement_id": "BD-17-009",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "18fd72a3e36383b4db254f76c07aa060e768e8dfc9b13032f587ec5cd2b2884b"
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
        "BD-17-009-AC001",
        "BD-17-009-AC003",
        "BD-17-009-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-009-O001",
      "obligation_text": "Worker là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-009-AC002",
        "BD-17-009-AC003",
        "BD-17-009-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-009-O002",
      "obligation_text": "Một Job có thể được xử lý bởi nhiều Worker"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Worker là Business Object. Một Job có thể được xử lý bởi nhiều Worker.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Worker",
    "source_context_sha256": "880d22bb4db3afdca137719395ef76a347207d0830bd82043c053c81ad2bf8cd",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "18fd72a3e36383b4db254f76c07aa060e768e8dfc9b13032f587ec5cd2b2884b",
    "source_lines": "L2271-L2356",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-009"
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
  "stable_id": "BD-17-009",
  "title": "Worker là Business Object. Một Job có thể được xử lý bởi nhiều Worker",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-010 — Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: - Pending - Processing - Completed - Retry - …

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-17-010",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "0b42b390c5f77c401b956a2b01ea0304bfb5392397de4fa97927e1b70492e19d"
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
        "BD-17-010-AC001",
        "BD-17-010-AC007",
        "BD-17-010-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O001",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: Pending"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-010-AC002",
        "BD-17-010-AC007",
        "BD-17-010-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O002",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: Processing"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-010-AC003",
        "BD-17-010-AC007",
        "BD-17-010-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O003",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: Completed"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-010-AC004",
        "BD-17-010-AC007",
        "BD-17-010-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O004",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: Retry"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-010-AC005",
        "BD-17-010-AC007",
        "BD-17-010-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O005",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: Failed"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-010-AC006",
        "BD-17-010-AC007",
        "BD-17-010-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O006",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: DLQ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: - Pending - Processing - Completed - Retry - Failed - DLQ",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-010",
    "source_context_sha256": "300c92ef518b31c11f79f3ec9892d6e349c92da139617c8514226c1732e50182",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "0b42b390c5f77c401b956a2b01ea0304bfb5392397de4fa97927e1b70492e19d",
    "source_lines": "L2358-L2487",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-010"
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
  "stable_id": "BD-17-010",
  "title": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: - Pending - Processing - Completed - Retry - …",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-011 — Operation Retry độc lập Connector Retry

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-17-011",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "2182c0fb868876035b46a98a806d187921bb0de85494a038eca637e05bb86701"
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
        "BD-17-011-AC001",
        "BD-17-011-AC002",
        "BD-17-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-011-O001",
      "obligation_text": "Operation Retry độc lập Connector Retry"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operation Retry độc lập Connector Retry.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-011",
    "source_context_sha256": "2aebb9cc529851f28c32018d00f73946f21a29a8a0cf36843bbafce05b2b2f8a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "2182c0fb868876035b46a98a806d187921bb0de85494a038eca637e05bb86701",
    "source_lines": "L2489-L2572",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-011"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [
      "EP-17-005"
    ],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-17-011",
  "title": "Operation Retry độc lập Connector Retry",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-012 — Maintenance Window là Business Object. Maintenance hỗ trợ nhiều cấp

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-004"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-17-012",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "95c8a4d1ede1d9c6a0ddf17f000513b255b7644ba7ab22ddf32727bd7e232d04"
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
        "BD-17-012-AC001",
        "BD-17-012-AC003",
        "BD-17-012-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-012-O001",
      "obligation_text": "Maintenance Window là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-012-AC002",
        "BD-17-012-AC003",
        "BD-17-012-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-012-O002",
      "obligation_text": "Maintenance hỗ trợ nhiều cấp"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Maintenance Window là Business Object. Maintenance hỗ trợ nhiều cấp.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-004"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Maintenance Window",
    "source_context_sha256": "7a1f5d1e44bec1cf2eab35e66698d5dce984973fa8f5122f9c9a3ce7bc328540",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "95c8a4d1ede1d9c6a0ddf17f000513b255b7644ba7ab22ddf32727bd7e232d04",
    "source_lines": "L2574-L2663",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-012"
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
  "stable_id": "BD-17-012",
  "title": "Maintenance Window là Business Object. Maintenance hỗ trợ nhiều cấp",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-013 — Backup Policy là Business Object

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
      "requirement_id": "BD-17-013",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "ba35acd2b5cef6100721b0707dcdce5bb881ab37b6c95b9354e422bf04428dd4"
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
        "BD-17-013-AC001",
        "BD-17-013-AC002",
        "BD-17-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-013-O001",
      "obligation_text": "Backup Policy là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Backup Policy là Business Object.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Backup Policy",
    "source_context_sha256": "9d90a4ec4c3934844154e16311f5fdb4d455b8f4ef513fd16d3ceeff8b8797f9",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "ba35acd2b5cef6100721b0707dcdce5bb881ab37b6c95b9354e422bf04428dd4",
    "source_lines": "L2665-L2740",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-013"
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
  "stable_id": "BD-17-013",
  "title": "Backup Policy là Business Object",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-014 — Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: - Manual - Semi Automatic - Automatic

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
      "requirement_id": "BD-17-014",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "8069966a4baad2d65a7615a735319b361e49d8038c02d17e3a5d3f4418bcb93a"
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
        "BD-17-014-AC001",
        "BD-17-014-AC004",
        "BD-17-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-014-O001",
      "obligation_text": "Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: Manual"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-014-AC002",
        "BD-17-014-AC004",
        "BD-17-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-014-O002",
      "obligation_text": "Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: Semi Automatic"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-014-AC003",
        "BD-17-014-AC004",
        "BD-17-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-014-O003",
      "obligation_text": "Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: Automatic"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-17-014-AC004"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-17-014-AC001",
        "BD-17-014-AC002",
        "BD-17-014-AC003"
      ]
    },
    "RECOVERY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-17-014-AC005"
      ],
      "rationale": null
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: - Manual - Semi Automatic - Automatic",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Disaster Recovery",
    "source_context_sha256": "6d609055052f25e77fe8d7fedfb4d2b91c0ac5f8ede21a504a9f77d851a579d3",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "8069966a4baad2d65a7615a735319b361e49d8038c02d17e3a5d3f4418bcb93a",
    "source_lines": "L2742-L2874",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-014"
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
  "stable_id": "BD-17-014",
  "title": "Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: - Manual - Semi Automatic - Automatic",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-015 — Capacity Policy là Business Object. Kiến trúc hỗ trợ Auto Scaling trong tương lai

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
      "requirement_id": "BD-17-015",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "393f3362575152d056af55474705ed3fabf370a0f6b7f9694216313ede253da8"
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
        "BD-17-015-AC001",
        "BD-17-015-AC003",
        "BD-17-015-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-015-O001",
      "obligation_text": "Capacity Policy là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-015-AC002",
        "BD-17-015-AC003",
        "BD-17-015-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-015-O002",
      "obligation_text": "Kiến trúc hỗ trợ Auto Scaling trong tương lai"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capacity Policy là Business Object. Kiến trúc hỗ trợ Auto Scaling trong tương lai.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Capacity Policy",
    "source_context_sha256": "35b46362ca2e055de876727569c50112df05ff0fe3cbeaf3ca4fc668418aefaa",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "393f3362575152d056af55474705ed3fabf370a0f6b7f9694216313ede253da8",
    "source_lines": "L2876-L2961",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-015"
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
  "stable_id": "BD-17-015",
  "title": "Capacity Policy là Business Object. Kiến trúc hỗ trợ Auto Scaling trong tương lai",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-016 — Platform có Operational Dashboard dành riêng cho Operator

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-005",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-17-016",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "6ac1ce9e5c28386ad19da131b8d6da87eb34c025be958b6b981ba026aacb7e9b"
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
        "BD-17-016-AC001",
        "BD-17-016-AC002",
        "BD-17-016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-016-O001",
      "obligation_text": "Platform có Operational Dashboard dành riêng cho Operator"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform có Operational Dashboard dành riêng cho Operator.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-016",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-016",
    "source_context_sha256": "82d6cb771db89481d4e8731831abec1fbc8c2661d3489995ede0fada4ac3f04e",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "6ac1ce9e5c28386ad19da131b8d6da87eb34c025be958b6b981ba026aacb7e9b",
    "source_lines": "L2963-L3042",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-016"
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
  "stable_id": "BD-17-016",
  "title": "Platform có Operational Dashboard dành riêng cho Operator",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-017 — Operator sử dụng Permission riêng. Mọi thao tác đều được Security Platform kiểm soát

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
      "requirement_id": "BD-17-017",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "30d383c39c3351e46e9662675407bd4d13b8f9501a7f5d14f52b90f05f624cff"
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
        "BD-17-017-AC001",
        "BD-17-017-AC003",
        "BD-17-017-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-017-O001",
      "obligation_text": "Operator sử dụng Permission riêng"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-017-AC002",
        "BD-17-017-AC003",
        "BD-17-017-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-017-O002",
      "obligation_text": "Mọi thao tác đều được Security Platform kiểm soát"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-17-017-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-017 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-017 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-17-017-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-17-017-AC001",
        "BD-17-017-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-017 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operator sử dụng Permission riêng. Mọi thao tác đều được Security Platform kiểm soát.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-017",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Operation Permission",
    "source_context_sha256": "6d40656f50a9ead910dd75e3bc79e99ac8f3f397474048d45d6a87a735d3271d",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "30d383c39c3351e46e9662675407bd4d13b8f9501a7f5d14f52b90f05f624cff",
    "source_lines": "L3044-L3165",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-017"
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
  "stable_id": "BD-17-017",
  "title": "Operator sử dụng Permission riêng. Mọi thao tác đều được Security Platform kiểm soát",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-018 — Maintenance phải gửi Notification trước khi thực hiện

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-004"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-17-018",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "0e4e9db1814bedf6dab0ae680daf75328f4ecbc0f3497797f7a60a76993331bb"
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
        "BD-17-018-AC001",
        "BD-17-018-AC002",
        "BD-17-018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-018-O001",
      "obligation_text": "Maintenance phải gửi Notification trước khi thực hiện"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Maintenance phải gửi Notification trước khi thực hiện.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-004"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-018",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-018",
    "source_context_sha256": "c3a5eda4f2bf660e5fa1c35cd855b49015e53e74a4d145fd94b5d40fa6acd924",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "0e4e9db1814bedf6dab0ae680daf75328f4ecbc0f3497797f7a60a76993331bb",
    "source_lines": "L3167-L3246",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-018"
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
  "stable_id": "BD-17-018",
  "title": "Maintenance phải gửi Notification trước khi thực hiện",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-019 — Scheduler hỗ trợ Priority. Business Critical Job luôn được ưu tiên

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
      "requirement_id": "BD-17-019",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "65a0a392e23b87840f76c1c0f3b41e6884f70840c80da72ccb95c9d089e514b9"
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
        "BD-17-019-AC001",
        "BD-17-019-AC003",
        "BD-17-019-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-019-O001",
      "obligation_text": "Scheduler hỗ trợ Priority"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-019-AC002",
        "BD-17-019-AC003",
        "BD-17-019-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-019-O002",
      "obligation_text": "Business Critical Job luôn được ưu tiên"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Scheduler hỗ trợ Priority. Business Critical Job luôn được ưu tiên.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-019",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Scheduler Priority",
    "source_context_sha256": "ee849292348f3551510bfd40a7a6460b6f49278dea438ab576df64843cb65a03",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "65a0a392e23b87840f76c1c0f3b41e6884f70840c80da72ccb95c9d089e514b9",
    "source_lines": "L3248-L3333",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-019"
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
  "stable_id": "BD-17-019",
  "title": "Scheduler hỗ trợ Priority. Business Critical Job luôn được ưu tiên",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-020 — Kiến trúc hỗ trợ Auto Scaling. Version hiện tại chưa triển khai

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
      "requirement_id": "BD-17-020",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "73437e33183cf1e523da41d3b6c2a26a915bcf3ad7693d9b9f355e32218cb029"
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
        "BD-17-020-AC001",
        "BD-17-020-AC003",
        "BD-17-020-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-020-O001",
      "obligation_text": "Kiến trúc hỗ trợ Auto Scaling"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-020-AC002",
        "BD-17-020-AC003",
        "BD-17-020-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-020-O002",
      "obligation_text": "Version hiện tại chưa triển khai"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Kiến trúc hỗ trợ Auto Scaling. Version hiện tại chưa triển khai.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-020",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-020",
    "source_context_sha256": "2391c6384af6aab5ec39c690363542f386694968c28f1841191b25e4eccd90b5",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "73437e33183cf1e523da41d3b6c2a26a915bcf3ad7693d9b9f355e32218cb029",
    "source_lines": "L3335-L3420",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-020"
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
  "stable_id": "BD-17-020",
  "title": "Kiến trúc hỗ trợ Auto Scaling. Version hiện tại chưa triển khai",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-021 — Operational Audit ghi nhận toàn bộ thao tác vận hành

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
      "requirement_id": "BD-17-021",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "1ec9921967a9781ee18eba2d824890c4f7e75c47656cf3fa2f2861684f5a2d3d"
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
        "BD-17-021-AC001",
        "BD-17-021-AC002",
        "BD-17-021-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-021-O001",
      "obligation_text": "Operational Audit ghi nhận toàn bộ thao tác vận hành"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-021 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-021 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-021 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-17-021-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-17-021-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-17-021 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operational Audit ghi nhận toàn bộ thao tác vận hành.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-021",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-021",
    "source_context_sha256": "a78fd5b3ee3fa05b89efc1e2f95dd6d9f198f5ec0f6adf808c550d90c63a342a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "1ec9921967a9781ee18eba2d824890c4f7e75c47656cf3fa2f2861684f5a2d3d",
    "source_lines": "L3422-L3530",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-021"
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
  "stable_id": "BD-17-021",
  "title": "Operational Audit ghi nhận toàn bộ thao tác vận hành",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-022 — Operation Policy là Business Object. Operation Policy được Versioning

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
      "requirement_id": "BD-17-022",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "e378d49ffef94577d5c810933eec19b98e4fe3aef2a05fcea2385f531f6d9565"
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
        "BD-17-022-AC001",
        "BD-17-022-AC003",
        "BD-17-022-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-022-O001",
      "obligation_text": "Operation Policy là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-022-AC002",
        "BD-17-022-AC003",
        "BD-17-022-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-022-O002",
      "obligation_text": "Operation Policy được Versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operation Policy là Business Object. Operation Policy được Versioning.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-022",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Operation Policy",
    "source_context_sha256": "60c1917802a618eff2f187c3e98750eecbc31c464cb1885596ecb0b29b871998",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "e378d49ffef94577d5c810933eec19b98e4fe3aef2a05fcea2385f531f6d9565",
    "source_lines": "L3532-L3617",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-022"
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
  "stable_id": "BD-17-022",
  "title": "Operation Policy là Business Object. Operation Policy được Versioning",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-023 — Scheduler hỗ trợ Business Event Trigger

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
      "requirement_id": "BD-17-023",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "37c90eb0b19c87167abb887ae59148cdbf99a1ed5ffdd5a2bf67cfac764fb328"
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
        "BD-17-023-AC001",
        "BD-17-023-AC002",
        "BD-17-023-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-023-O001",
      "obligation_text": "Scheduler hỗ trợ Business Event Trigger"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Scheduler hỗ trợ Business Event Trigger.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-023",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-023",
    "source_context_sha256": "e9b4f43845ddedbd5a1fda9dd7a30a60d586e518ca5ea0f2b85cf31301a4e327",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "37c90eb0b19c87167abb887ae59148cdbf99a1ed5ffdd5a2bf67cfac764fb328",
    "source_lines": "L3619-L3694",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-023"
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
  "stable_id": "BD-17-023",
  "title": "Scheduler hỗ trợ Business Event Trigger",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-024 — Organization không có Operations Capability. Operations chỉ thuộc Platform

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
      "requirement_id": "BD-17-024",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "25c70ae43f472acdce61236f41124eaf1f5b5757db13c1d80c72d68f958c3984"
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
        "BD-17-024-AC001",
        "BD-17-024-AC003",
        "BD-17-024-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-024-O001",
      "obligation_text": "Organization không có Operations Capability"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-024-AC002",
        "BD-17-024-AC003",
        "BD-17-024-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-024-O002",
      "obligation_text": "Operations chỉ thuộc Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization không có Operations Capability. Operations chỉ thuộc Platform.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-024",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-024",
    "source_context_sha256": "cfcb2e10d1891c18b84fc1ecaebcfcbf4d60e4dfe8e3d3de3099436ba61ad234",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "25c70ae43f472acdce61236f41124eaf1f5b5757db13c1d80c72d68f958c3984",
    "source_lines": "L3696-L3785",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-024"
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
  "stable_id": "BD-17-024",
  "title": "Organization không có Operations Capability. Operations chỉ thuộc Platform",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-025 — Maintenance hỗ trợ nhiều Scope

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-004"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-17-025",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "85c8ef2707c18439269868739e9f474a532ab2a827925c09b6a46317e3cc83e2"
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
        "BD-17-025-AC001",
        "BD-17-025-AC002",
        "BD-17-025-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-025-O001",
      "obligation_text": "Maintenance hỗ trợ nhiều Scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Maintenance hỗ trợ nhiều Scope.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-004"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-025",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-025",
    "source_context_sha256": "1a80e711ceb369a386e5893c702c18e882fced427e927a2f47e75012fe52dea9",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "85c8ef2707c18439269868739e9f474a532ab2a827925c09b6a46317e3cc83e2",
    "source_lines": "L3787-L3866",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-025"
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
  "stable_id": "BD-17-025",
  "title": "Maintenance hỗ trợ nhiều Scope",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-026 — Operations Platform Publish Business Event

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
      "requirement_id": "BD-17-026",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "2d6ab7828fff5926a1ff83d7a6f945bb080760411b88cf84663dd41e02544bbc"
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
        "BD-17-026-AC001",
        "BD-17-026-AC002",
        "BD-17-026-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-026-O001",
      "obligation_text": "Operations Platform Publish Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operations Platform Publish Business Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-026",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "29. Operation Business Events",
    "source_context_sha256": "ab56286c8a4ab9a35eda380fb856a41d2c3038d4f5c35c93c36835f9e4844bc8",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "2d6ab7828fff5926a1ff83d7a6f945bb080760411b88cf84663dd41e02544bbc",
    "source_lines": "L3868-L3945",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-026"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [
      "EP-17-009"
    ],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-17-026",
  "title": "Operations Platform Publish Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-027 — Runbook là Business Object

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-004"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-17-027",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "61fcc8024ddec9ff5e5751a0fc9077a108d945dda508355ce35b352ad166be90"
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
        "BD-17-027-AC001",
        "BD-17-027-AC002",
        "BD-17-027-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-027-O001",
      "obligation_text": "Runbook là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Runbook là Business Object.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-004"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-027",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "31. Runbook",
    "source_context_sha256": "0a53caf54c8ce30adb45c717be6663db1967f1b85d15de5829ae1e1ecec451b4",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "61fcc8024ddec9ff5e5751a0fc9077a108d945dda508355ce35b352ad166be90",
    "source_lines": "L3947-L4026",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-027"
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
  "stable_id": "BD-17-027",
  "title": "Runbook là Business Object",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-028 — Platform hỗ trợ Feature Flag và Kill Switch

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
      "requirement_id": "BD-17-028",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "7b92ca6093a9e3d16cdd4d7e18ca707ddec774e91ee4e438ae7c8f007fb2d8c0"
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
        "BD-17-028-AC001",
        "BD-17-028-AC002",
        "BD-17-028-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-028-O001",
      "obligation_text": "Platform hỗ trợ Feature Flag và Kill Switch"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Feature Flag và Kill Switch.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-028",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-028",
    "source_context_sha256": "0f20242bcc1e11401db1c54c141059ce5ca4305fc42048118296482ad058af16",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "7b92ca6093a9e3d16cdd4d7e18ca707ddec774e91ee4e438ae7c8f007fb2d8c0",
    "source_lines": "L4028-L4103",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-028"
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
  "stable_id": "BD-17-028",
  "title": "Platform hỗ trợ Feature Flag và Kill Switch",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-029 — Platform hỗ trợ Operational Command Center

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
      "requirement_id": "BD-17-029",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "67da15addfab30702dfae17d1c83473ed5676da6e741501ffcfb39c718917936"
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
        "BD-17-029-AC001",
        "BD-17-029-AC002",
        "BD-17-029-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-029-O001",
      "obligation_text": "Platform hỗ trợ Operational Command Center"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Operational Command Center.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-029",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-029",
    "source_context_sha256": "f4617410542f0c347907810bcb430dd265f1915a53166fadf57584f343c29b86",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "67da15addfab30702dfae17d1c83473ed5676da6e741501ffcfb39c718917936",
    "source_lines": "L4105-L4180",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-029"
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
  "stable_id": "BD-17-029",
  "title": "Platform hỗ trợ Operational Command Center",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-030 — Platform hỗ trợ Replay

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
      "requirement_id": "BD-17-030",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "153d41eda48201d3bb1b9dd5a1446390ca3d4b18144ca128c4023779e60bc972"
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
        "BD-17-030-AC001",
        "BD-17-030-AC002",
        "BD-17-030-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-030-O001",
      "obligation_text": "Platform hỗ trợ Replay"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Replay.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-030",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "34. Replay Platform",
    "source_context_sha256": "e3b46ff8ab39ade87f8ba8a9f09000c1364d0d744774b2b40fb23ec7c966c147",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "153d41eda48201d3bb1b9dd5a1446390ca3d4b18144ca128c4023779e60bc972",
    "source_lines": "L4182-L4257",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-030"
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
  "stable_id": "BD-17-030",
  "title": "Platform hỗ trợ Replay",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-031 — Kiến trúc hỗ trợ Chaos Readiness. Version hiện tại chưa triển khai

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
      "requirement_id": "BD-17-031",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "168e09b2fcd95316298b4cacf5f0a4e6cbda4de538705c5304f0e05133eb9c6e"
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
        "BD-17-031-AC001",
        "BD-17-031-AC003",
        "BD-17-031-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-031-O001",
      "obligation_text": "Kiến trúc hỗ trợ Chaos Readiness"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-031-AC002",
        "BD-17-031-AC003",
        "BD-17-031-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-031-O002",
      "obligation_text": "Version hiện tại chưa triển khai"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Kiến trúc hỗ trợ Chaos Readiness. Version hiện tại chưa triển khai.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-031",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "35. Chaos Readiness",
    "source_context_sha256": "7ad31828e1954900121ef58910f0778d0e86628804d20e1962c93b86018944b1",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "168e09b2fcd95316298b4cacf5f0a4e6cbda4de538705c5304f0e05133eb9c6e",
    "source_lines": "L4259-L4344",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-031"
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
  "stable_id": "BD-17-031",
  "title": "Kiến trúc hỗ trợ Chaos Readiness. Version hiện tại chưa triển khai",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-032 — Platform hỗ trợ SLO và SLA Monitoring

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-010"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-17-032",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "27470bb20635847a073a4d70a675fe4ec6ef76a8585d6c0ea6f2f8cc34d506f3"
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
        "BD-17-032-AC001",
        "BD-17-032-AC002",
        "BD-17-032-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-032-O001",
      "obligation_text": "Platform hỗ trợ SLO và SLA Monitoring"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ SLO và SLA Monitoring.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-010"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-032",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-032",
    "source_context_sha256": "515996d9e450b86b38587407b7a1995b5bfcdd71ebbdf22b0ff6c8283130b555",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "27470bb20635847a073a4d70a675fe4ec6ef76a8585d6c0ea6f2f8cc34d506f3",
    "source_lines": "L4346-L4425",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-17-032"
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
  "stable_id": "BD-17-032",
  "title": "Platform hỗ trợ SLO và SLA Monitoring",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R001 — Personal Inbox là kênh bắt buộc

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
      "requirement_id": "BRD-WS-17-R001",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "3e9a9f0fad04d7aff926749d1d7cff1cb15b05d5d636e680cd14d98c1f16ce20"
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
        "BRD-WS-17-R001-AC001",
        "BRD-WS-17-R001-AC002",
        "BRD-WS-17-R001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R001-O001",
      "obligation_text": "Personal Inbox là kênh bắt buộc"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Personal Inbox là kênh bắt buộc.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-001",
    "previous_temporary_key": "TMP-BRD-WS-17-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Alert Channel",
    "source_context_sha256": "1162d9cd178e0c92904ae963d450169cc9bf63b27e6653c1c585698b3357407f",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "3e9a9f0fad04d7aff926749d1d7cff1cb15b05d5d636e680cd14d98c1f16ce20",
    "source_lines": "L4427-L4502",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R001"
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
  "stable_id": "BRD-WS-17-R001",
  "title": "Personal Inbox là kênh bắt buộc",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R002 — Scheduler Trigger được cấu hình và có thể thay đổi mà không cần sửa mã nguồn

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Platform invariant changes remain governed separately; operational scheduling remains configurable"
    ],
    "concrete_bindings": [
      {
        "configuration_key": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
            "source_type": "SOURCE_LITERAL",
            "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
          },
          "identifier": "BRD-WS-17-R002.CONFIGURATION_KEY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-17.md",
            "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
            "source_lines": "L288",
            "source_section": "10. Scheduler Trigger"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CONFIGURATION_KEY",
            "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.CONFIGURATION_KEY",
            "version": "1.0.0"
          },
          "semantic_type": "CONFIGURATION_KEY"
        },
        "configuration_sources": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
            "source_type": "SOURCE_LITERAL",
            "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
          },
          "identifier": "BRD-WS-17-R002.CONFIGURATION_SOURCES",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-17.md",
            "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
            "source_lines": "L288",
            "source_section": "10. Scheduler Trigger"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
            "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.CONFIGURATION_SOURCES",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
        },
        "expected_value": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-17-R002.CANONICAL.CONFIGURATION.VALUE"
            ],
            "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
            "source_type": "SOURCE_LITERAL",
            "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
          },
          "identifier": "BRD-WS-17-R002.CANONICAL.CONFIGURATION.VALUE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-17.md",
            "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
            "source_lines": "L288",
            "source_section": "10. Scheduler Trigger"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.CANONICAL.CONFIGURATION.VALUE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "resolved_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
            "source_type": "SOURCE_LITERAL",
            "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
          },
          "identifier": "BRD-WS-17-R002.RESOLVED_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-17.md",
            "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
            "source_lines": "L288",
            "source_section": "10. Scheduler Trigger"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CONFIGURATION_SOURCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.RESOLVED_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "CONFIGURATION_SOURCE_ID"
        },
        "source_versions": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                "source_type": "SOURCE_LITERAL",
                "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
              },
              "identifier": "BRD-WS-17-R002.SOURCE_VERSIONS.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                "source_lines": "L288",
                "source_section": "10. Scheduler Trigger"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.SOURCE_VERSIONS.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-17.md",
            "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
            "source_lines": "L288",
            "source_section": "10. Scheduler Trigger"
          },
          "semantic_type": "SET_OF<POLICY_VERSION>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-17-R002",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Changing trigger behavior requires source-code modification or bypasses configuration"
    ],
    "operator_composition": [
      "CONFIGURATION_RESOLVES"
    ],
    "positive_oracle": [
      "Trigger behavior changes through configuration without source-code modification"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
      "source_lines": "L288",
      "source_section": "10. Scheduler Trigger"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
          "source_type": "SOURCE_LITERAL",
          "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
        },
        "identifier": "BRD-WS-17-R002.BRD-WS-17-R002.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-17-R002.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-17.md",
          "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
          "source_lines": "L288",
          "source_section": "10. Scheduler Trigger"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-17-R002.BRD-WS-17-R002.BRD-WS-17-R002.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-17-R002.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.TRIGGER_ID",
        "FIELD.CONFIGURATION_BEFORE",
        "FIELD.CONFIGURATION_AFTER",
        "FIELD.CODE_DIFF",
        "FIELD.AUTHORIZATION",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "BRD-WS-17-R002.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-17-R002.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.TRIGGER_ID",
        "FIELD.CONFIGURATION_BEFORE",
        "FIELD.CONFIGURATION_AFTER",
        "FIELD.CODE_DIFF",
        "FIELD.AUTHORIZATION",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "BRD-WS-17-R002.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-17-R002.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-17-R002.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-17-R002-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES",
          "evaluator_consumed_bindings": [
            "configuration_key",
            "configuration_sources",
            "expected_value",
            "resolved_source",
            "source_versions"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
              "source_type": "SOURCE_LITERAL",
              "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
            },
            "identifier": "BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-17.md",
              "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
              "source_lines": "L288",
              "source_section": "10. Scheduler Trigger"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-17-R002.BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
              "source_type": "SOURCE_LITERAL",
              "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
            },
            "identifier": "BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-17.md",
              "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
              "source_lines": "L288",
              "source_section": "10. Scheduler Trigger"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "configuration_key": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
                },
                "identifier": "BRD-WS-17-R002.CONFIGURATION_KEY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                  "source_lines": "L288",
                  "source_section": "10. Scheduler Trigger"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_KEY",
                  "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.CONFIGURATION_KEY",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_KEY"
              },
              "configuration_sources": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
                },
                "identifier": "BRD-WS-17-R002.CONFIGURATION_SOURCES",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                  "source_lines": "L288",
                  "source_section": "10. Scheduler Trigger"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
                  "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.CONFIGURATION_SOURCES",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
              },
              "expected_value": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-17-R002.CANONICAL.CONFIGURATION.VALUE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
                },
                "identifier": "BRD-WS-17-R002.CANONICAL.CONFIGURATION.VALUE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                  "source_lines": "L288",
                  "source_section": "10. Scheduler Trigger"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.CANONICAL.CONFIGURATION.VALUE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "resolved_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
                },
                "identifier": "BRD-WS-17-R002.RESOLVED_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                  "source_lines": "L288",
                  "source_section": "10. Scheduler Trigger"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_SOURCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.RESOLVED_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_SOURCE_ID"
              },
              "source_versions": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                      "source_type": "SOURCE_LITERAL",
                      "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
                    },
                    "identifier": "BRD-WS-17-R002.SOURCE_VERSIONS.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-17.md",
                      "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                      "source_lines": "L288",
                      "source_section": "10. Scheduler Trigger"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "POLICY_VERSION",
                      "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.SOURCE_VERSIONS.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "POLICY_VERSION"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                  "source_lines": "L288",
                  "source_section": "10. Scheduler Trigger"
                },
                "semantic_type": "SET_OF<POLICY_VERSION>"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
                },
                "identifier": "BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                  "source_lines": "L288",
                  "source_section": "10. Scheduler Trigger"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                  "source_type": "SOURCE_LITERAL",
                  "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
                },
                "identifier": "BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                  "source_lines": "L288",
                  "source_section": "10. Scheduler Trigger"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BRD-WS-17-R002.BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                "source_type": "SOURCE_LITERAL",
                "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
              },
              "identifier": "BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                "source_lines": "L288",
                "source_section": "10. Scheduler Trigger"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-17-R002.BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "CONFIGURATION_RESOLVES"
          },
          "obligation_id": "BRD-WS-17-R002-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
              "source_type": "SOURCE_LITERAL",
              "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
            },
            "identifier": "BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-17.md",
              "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
              "source_lines": "L288",
              "source_section": "10. Scheduler Trigger"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "OBSERVE.BRD-WS-17-R002.BRD-WS-17-R002.BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "operator_id": "CONFIGURATION_RESOLVES",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "configuration_key": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                "source_type": "SOURCE_LITERAL",
                "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
              },
              "identifier": "BRD-WS-17-R002.CONFIGURATION_KEY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                "source_lines": "L288",
                "source_section": "10. Scheduler Trigger"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_KEY",
                "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.CONFIGURATION_KEY",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_KEY"
            },
            "configuration_sources": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                "source_type": "SOURCE_LITERAL",
                "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
              },
              "identifier": "BRD-WS-17-R002.CONFIGURATION_SOURCES",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                "source_lines": "L288",
                "source_section": "10. Scheduler Trigger"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
                "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.CONFIGURATION_SOURCES",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
            },
            "expected_value": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-17-R002.CANONICAL.CONFIGURATION.VALUE"
                ],
                "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                "source_type": "SOURCE_LITERAL",
                "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
              },
              "identifier": "BRD-WS-17-R002.CANONICAL.CONFIGURATION.VALUE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                "source_lines": "L288",
                "source_section": "10. Scheduler Trigger"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.CANONICAL.CONFIGURATION.VALUE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "resolved_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                "source_type": "SOURCE_LITERAL",
                "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
              },
              "identifier": "BRD-WS-17-R002.RESOLVED_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                "source_lines": "L288",
                "source_section": "10. Scheduler Trigger"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_SOURCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.RESOLVED_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_SOURCE_ID"
            },
            "source_versions": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
                    "source_type": "SOURCE_LITERAL",
                    "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
                  },
                  "identifier": "BRD-WS-17-R002.SOURCE_VERSIONS.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-17.md",
                    "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                    "source_lines": "L288",
                    "source_section": "10. Scheduler Trigger"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "POLICY_VERSION",
                    "resolver_id": "RESOLVE.BRD-WS-17-R002.BRD-WS-17-R002.SOURCE_VERSIONS.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "POLICY_VERSION"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
                "source_lines": "L288",
                "source_section": "10. Scheduler Trigger"
              },
              "semantic_type": "SET_OF<POLICY_VERSION>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Platform invariant changes remain governed separately; operational scheduling remains configurable"
      ],
      "contract_ast_sha256": "073012d9ad7a4b11410534d1dac6e3a792e532c7c68fa76a208b0118866f5a2e",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-17-R002",
      "criticality": "NORMAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-17.md#10. Scheduler Trigger",
            "source_type": "SOURCE_LITERAL",
            "version": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677"
          },
          "identifier": "BRD-WS-17-R002.BRD-WS-17-R002.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-17-R002.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-17.md",
            "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
            "source_lines": "L288",
            "source_section": "10. Scheduler Trigger"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-17-R002.BRD-WS-17-R002.BRD-WS-17-R002.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-17-R002.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.TRIGGER_ID",
          "FIELD.CONFIGURATION_BEFORE",
          "FIELD.CONFIGURATION_AFTER",
          "FIELD.CODE_DIFF",
          "FIELD.AUTHORIZATION",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "BRD-WS-17-R002.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-17-R002.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.TRIGGER_ID",
          "FIELD.CONFIGURATION_BEFORE",
          "FIELD.CONFIGURATION_AFTER",
          "FIELD.CODE_DIFF",
          "FIELD.AUTHORIZATION",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "BRD-WS-17-R002.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-17-R002.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-17-R002.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-EFBEAA632EE4DF7C066F",
        "P2C-C4-FX-A6538B23452ED4614296",
        "P2C-C4-FX-4F8D7AAFF644138B8024"
      ],
      "high_risk_audit_subset": false,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Changing trigger behavior requires source-code modification or bypasses configuration"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-17-R002-O001",
          "obligation_text": "Scheduler Trigger được cấu hình và có thể thay đổi mà không cần sửa mã nguồn"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-17-R002.O1.1.CONFIGURATION_RESOLVES"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-17-R002-O001"
        }
      ],
      "operator_composition": [
        "CONFIGURATION_RESOLVES"
      ],
      "positive_oracles": [
        "Trigger behavior changes through configuration without source-code modification"
      ],
      "preconditions": [
        "The actor is authorized and configuration version is valid"
      ],
      "prohibitions": [
        "Changing trigger behavior requires source-code modification or bypasses configuration"
      ],
      "requirement_id": "BRD-WS-17-R002",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-17.md",
        "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
        "source_lines": "L288",
        "source_section": "10. Scheduler Trigger"
      },
      "source_statement": "Scheduler Trigger được cấu hình và có thể thay đổi mà không cần sửa mã nguồn.",
      "surrounding_source_context": "### BRD-WS-17-R002 — Scheduler Trigger được cấu hình và có thể thay đổi mà không cần sửa mã nguồn"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-17-R002",
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
        "BRD-WS-17-R002-AC001",
        "BRD-WS-17-R002-AC002",
        "BRD-WS-17-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R002-O001",
      "obligation_text": "Scheduler Trigger được cấu hình và có thể thay đổi mà không cần sửa mã nguồn"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Scheduler Trigger được cấu hình và có thể thay đổi mà không cần sửa mã nguồn.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-002",
    "previous_temporary_key": "TMP-BRD-WS-17-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Scheduler Trigger",
    "source_context_sha256": "c6119caa8d765ea8c152715c930f2749ca218179059862a8e99b83b2dec2d395",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "dc57ad841afe185bd3463dd10e976f5d73faa947b4bb7dd672459f478f250677",
    "source_lines": "L4504-L5603",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R002"
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
  "stable_id": "BRD-WS-17-R002",
  "title": "Scheduler Trigger được cấu hình và có thể thay đổi mà không cần sửa mã nguồn",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R003 — Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-17-R003",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "1478d8ae4653f0b2e8679dd61d41e04ed7ae6cea584187c4c2546b0990fdbbe7"
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
        "BRD-WS-17-R003-AC001",
        "BRD-WS-17-R003-AC002",
        "BRD-WS-17-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R003-O001",
      "obligation_text": "Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R003-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R003 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-003",
    "previous_temporary_key": "TMP-BRD-WS-17-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "14. Operation Retry",
    "source_context_sha256": "9532dadb38743befd53f646d6a673b9e3caeeaf24daca6f85ac9dff6efff8fa0",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "1478d8ae4653f0b2e8679dd61d41e04ed7ae6cea584187c4c2546b0990fdbbe7",
    "source_lines": "L5605-L5719",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R003"
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
  "stable_id": "BRD-WS-17-R003",
  "title": "Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R004 —  Auto Scaling (Future Version)

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-17-R004",
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
  "normative_statement": "- Auto Scaling (Future Version)",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-004",
    "previous_temporary_key": "TMP-BRD-WS-17-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Capacity Policy",
    "source_context_sha256": "35b46362ca2e055de876727569c50112df05ff0fe3cbeaf3ca4fc668418aefaa",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "e7904b528d9a6fbee267e2fdb0f2cd63f6094a124e442a430d96c522bf31e23b",
    "source_lines": "L5721-L5779",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R004"
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
  "stable_id": "BRD-WS-17-R004",
  "title": " Auto Scaling (Future Version)",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R006 — Maintenance phải gửi Notification trước khi bắt đầu

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-004"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-17-R006",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "8bef3cbd28dc1442900398f96a31bb8cc3bb94f392c4102172cd08cfaad34413"
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
        "BRD-WS-17-R006-AC001",
        "BRD-WS-17-R006-AC002",
        "BRD-WS-17-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R006-O001",
      "obligation_text": "Maintenance phải gửi Notification trước khi bắt đầu"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Maintenance phải gửi Notification trước khi bắt đầu.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-004"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-006",
    "previous_temporary_key": "TMP-BRD-WS-17-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Maintenance Notification",
    "source_context_sha256": "56deb435130e3cb1321717655401f7570e5c7f83c05f16e5b38fd02b838c71eb",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "8bef3cbd28dc1442900398f96a31bb8cc3bb94f392c4102172cd08cfaad34413",
    "source_lines": "L5781-L5860",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R006"
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
  "stable_id": "BRD-WS-17-R006",
  "title": "Maintenance phải gửi Notification trước khi bắt đầu",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R007 — Business Critical Job luôn được ưu tiên

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
      "requirement_id": "BRD-WS-17-R007",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "7a791da18ef300931d66290da3513663adfb7afa4665bb6e1b313ac9ec206a52"
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
        "BRD-WS-17-R007-AC001",
        "BRD-WS-17-R007-AC002",
        "BRD-WS-17-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R007-O001",
      "obligation_text": "Business Critical Job luôn được ưu tiên"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Critical Job luôn được ưu tiên.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-007",
    "previous_temporary_key": "TMP-BRD-WS-17-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Scheduler Priority",
    "source_context_sha256": "ee849292348f3551510bfd40a7a6460b6f49278dea438ab576df64843cb65a03",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "7a791da18ef300931d66290da3513663adfb7afa4665bb6e1b313ac9ec206a52",
    "source_lines": "L5862-L5937",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R007"
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
  "stable_id": "BRD-WS-17-R007",
  "title": "Business Critical Job luôn được ưu tiên",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R008 — Operational Audit tuân thủ Security Policy

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
      "requirement_id": "BRD-WS-17-R008",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "6a3e985b004030dba0d688881419fbc53afd181a2cb945687b454df456c61465"
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
        "BRD-WS-17-R008-AC001",
        "BRD-WS-17-R008-AC002",
        "BRD-WS-17-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R008-O001",
      "obligation_text": "Operational Audit tuân thủ Security Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R008-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R008-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R008-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R008 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operational Audit tuân thủ Security Policy.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-008",
    "previous_temporary_key": "TMP-BRD-WS-17-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "24. Operational Audit",
    "source_context_sha256": "cc4ae75b5a2eaf34a905c3c16264813f494f23dd4c3606f917d75c14ec1e36e5",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "6a3e985b004030dba0d688881419fbc53afd181a2cb945687b454df456c61465",
    "source_lines": "L5939-L6049",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R008"
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
  "stable_id": "BRD-WS-17-R008",
  "title": "Operational Audit tuân thủ Security Policy",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R009 — Audit không được phép chỉnh sửa

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
      "requirement_id": "BRD-WS-17-R009",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "b8c4a9f6d3d9e3a88468f0c11410ed311a06fcbac64398c0584dac0ec439f1c4"
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
        "BRD-WS-17-R009-AC001",
        "BRD-WS-17-R009-AC002",
        "BRD-WS-17-R009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R009-O001",
      "obligation_text": "Audit không được phép chỉnh sửa"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R009 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R009 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R009 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R009-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R009-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R009 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Audit không được phép chỉnh sửa.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-009",
    "previous_temporary_key": "TMP-BRD-WS-17-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "24. Operational Audit",
    "source_context_sha256": "cc4ae75b5a2eaf34a905c3c16264813f494f23dd4c3606f917d75c14ec1e36e5",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "b8c4a9f6d3d9e3a88468f0c11410ed311a06fcbac64398c0584dac0ec439f1c4",
    "source_lines": "L6051-L6159",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R009"
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
  "stable_id": "BRD-WS-17-R009",
  "title": "Audit không được phép chỉnh sửa",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R010 — Operation Policy không được Hard-code

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
      "requirement_id": "BRD-WS-17-R010",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "35a32976cbaeb0e2f67ba64f6dc74c37b7755b992055bed46dfb2e4b44f66359"
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
        "BRD-WS-17-R010-AC001",
        "BRD-WS-17-R010-AC002",
        "BRD-WS-17-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R010-O001",
      "obligation_text": "Operation Policy không được Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operation Policy không được Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-010",
    "previous_temporary_key": "TMP-BRD-WS-17-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Operation Policy",
    "source_context_sha256": "60c1917802a618eff2f187c3e98750eecbc31c464cb1885596ecb0b29b871998",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "35a32976cbaeb0e2f67ba64f6dc74c37b7755b992055bed46dfb2e4b44f66359",
    "source_lines": "L6161-L6236",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R010"
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
  "stable_id": "BRD-WS-17-R010",
  "title": "Operation Policy không được Hard-code",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R011 — Business Scheduler giúp tự động hóa quy trình nghiệp vụ mà không cần lập trình bổ sung

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
      "requirement_id": "BRD-WS-17-R011",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "2cb6912c4c0dda41dd1ce554823d7617d5b37ef0692c578bada05b13ab078dab"
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
        "BRD-WS-17-R011-AC001",
        "BRD-WS-17-R011-AC002",
        "BRD-WS-17-R011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R011-O001",
      "obligation_text": "Business Scheduler giúp tự động hóa quy trình nghiệp vụ mà không cần lập trình bổ sung"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Scheduler giúp tự động hóa quy trình nghiệp vụ mà không cần lập trình bổ sung.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-011",
    "previous_temporary_key": "TMP-BRD-WS-17-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. Business Scheduler",
    "source_context_sha256": "ad179cdf9dfbeeb1ce566ff2c261073edaa9553c1610d0d7e5f9f224475f81a6",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "2cb6912c4c0dda41dd1ce554823d7617d5b37ef0692c578bada05b13ab078dab",
    "source_lines": "L6238-L6313",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R011"
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
  "stable_id": "BRD-WS-17-R011",
  "title": "Business Scheduler giúp tự động hóa quy trình nghiệp vụ mà không cần lập trình bổ sung",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R012 — Organization chỉ được xem các thông tin Monitoring được Platform chia sẻ theo Permission

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
      "requirement_id": "BRD-WS-17-R012",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "2d0c094a633795fe359c4b1690973719c1215c942aadc96a7370b833f55a7637"
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
        "BRD-WS-17-R012-AC001",
        "BRD-WS-17-R012-AC002",
        "BRD-WS-17-R012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R012-O001",
      "obligation_text": "Organization chỉ được xem các thông tin Monitoring được Platform chia sẻ theo Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R012-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R012-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R012-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R012 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization chỉ được xem các thông tin Monitoring được Platform chia sẻ theo Permission.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-012",
    "previous_temporary_key": "TMP-BRD-WS-17-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Organization Operations",
    "source_context_sha256": "1e9b4e7ab644e83d0662c572ab048fcb697c1a0d4d26c255f4781c9c840f27bb",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "2d0c094a633795fe359c4b1690973719c1215c942aadc96a7370b833f55a7637",
    "source_lines": "L6315-L6425",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R012"
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
  "stable_id": "BRD-WS-17-R012",
  "title": "Organization chỉ được xem các thông tin Monitoring được Platform chia sẻ theo Permission",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R013 — Enterprise Operations composite parent

```json
{
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "Composite parent coverage is satisfied only through ALL_CHILDREN; the parent is not an acceptance unit.",
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
      "exception_id": "P2-CRIT-EXC-023",
      "selected_disposition": "COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN"
    }
  ],
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi tác vụ vận hành phải đáp ứng toàn bộ các hợp đồng Enterprise Operations được liên kết bên dưới.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-013",
    "previous_temporary_key": "TMP-BRD-WS-17-013",
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Enterprise Operations Principle",
    "source_context_sha256": "f4b6aeebc35c74925667ca32adae5d22b689e2ba373fa7cae75a6f8c6fe8ee2a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "e1d040c6778da69d2e91e9f4155a5a0c8cb1d335f2097728f95682c03d440c5b",
    "source_lines": "L6427-L6494",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R013"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-17-R026",
      "BRD-WS-17-R027",
      "BRD-WS-17-R028",
      "BRD-WS-17-R029",
      "BRD-WS-17-R030",
      "BRD-WS-17-R031"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R013",
  "title": "Enterprise Operations composite parent",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R014 —  A/B Testing (Future)

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-17-R014",
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
  "normative_statement": "- A/B Testing (Future)",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-014",
    "previous_temporary_key": "TMP-BRD-WS-17-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "32. Feature Flag & Kill Switch",
    "source_context_sha256": "b1fab09e2bbba39c1dc093b64eb36cf0b05d880b5fc3ee672e3b591743889301",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "7e038f8589bcdd2b065f23deb2aa88573b2487c3fca823dd13e0f539f6adede0",
    "source_lines": "L6496-L6554",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R014"
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
  "stable_id": "BRD-WS-17-R014",
  "title": " A/B Testing (Future)",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R015 — Không cần Deploy lại hệ thống

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
      "requirement_id": "BRD-WS-17-R015",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "5cc3dee11d43504e5b59a94962000a27e91ad7c086815db1c9974c5ddab0c3a3"
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
        "BRD-WS-17-R015-AC001",
        "BRD-WS-17-R015-AC002",
        "BRD-WS-17-R015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R015-O001",
      "obligation_text": "Không cần Deploy lại hệ thống"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cần Deploy lại hệ thống.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-015",
    "previous_temporary_key": "TMP-BRD-WS-17-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "32. Feature Flag & Kill Switch",
    "source_context_sha256": "b1fab09e2bbba39c1dc093b64eb36cf0b05d880b5fc3ee672e3b591743889301",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "5cc3dee11d43504e5b59a94962000a27e91ad7c086815db1c9974c5ddab0c3a3",
    "source_lines": "L6556-L6631",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R015"
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
  "stable_id": "BRD-WS-17-R015",
  "title": "Không cần Deploy lại hệ thống",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R016 — Mọi thao tác yêu cầu: - Permission

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
      "requirement_id": "BRD-WS-17-R016",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "e8cfc87088db14d2f89cb2249b5028d1ad941c11d9f1c621e84f0f126e30e121"
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
        "BRD-WS-17-R016-AC001",
        "BRD-WS-17-R016-AC002",
        "BRD-WS-17-R016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R016-O001",
      "obligation_text": "Mọi thao tác yêu cầu: - Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R016-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R016 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R016 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R016-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R016-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R016 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thao tác yêu cầu: - Permission",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-016",
    "previous_temporary_key": "TMP-BRD-WS-17-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "33. Operational Command Center",
    "source_context_sha256": "074268adc5f33a1a97020d3107da534eb5dfc62ce3bea438d4c3a1d39abe7664",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "e8cfc87088db14d2f89cb2249b5028d1ad941c11d9f1c621e84f0f126e30e121",
    "source_lines": "L6633-L6743",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R016"
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
  "stable_id": "BRD-WS-17-R016",
  "title": "Mọi thao tác yêu cầu: - Permission",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R017 — Mọi thao tác yêu cầu: - Audit

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
      "requirement_id": "BRD-WS-17-R017",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "c6df0a9f58e48d6bf50ca4a3d43c34221cb71518395e446dcf833dc0270ea6eb"
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
        "BRD-WS-17-R017-AC001",
        "BRD-WS-17-R017-AC002",
        "BRD-WS-17-R017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R017-O001",
      "obligation_text": "Mọi thao tác yêu cầu: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R017 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R017 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R017 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R017-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R017-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R017 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thao tác yêu cầu: - Audit",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-017",
    "previous_temporary_key": "TMP-BRD-WS-17-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "33. Operational Command Center",
    "source_context_sha256": "074268adc5f33a1a97020d3107da534eb5dfc62ce3bea438d4c3a1d39abe7664",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "c6df0a9f58e48d6bf50ca4a3d43c34221cb71518395e446dcf833dc0270ea6eb",
    "source_lines": "L6745-L6853",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R017"
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
  "stable_id": "BRD-WS-17-R017",
  "title": "Mọi thao tác yêu cầu: - Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R018 — Mọi thao tác yêu cầu: - Runbook (nếu có)

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-004"
      ],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-015",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-17-R018",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "3301044192559d18d5fb73956b72ebd76088bb59006e7b29b33cf8b372b776e6"
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
        "BRD-WS-17-R018-AC001",
        "BRD-WS-17-R018-AC002",
        "BRD-WS-17-R018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R018-O001",
      "obligation_text": "Mọi thao tác yêu cầu: - Runbook (nếu có)"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thao tác yêu cầu: - Runbook (nếu có)",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-004"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-018",
    "previous_temporary_key": "TMP-BRD-WS-17-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "33. Operational Command Center",
    "source_context_sha256": "074268adc5f33a1a97020d3107da534eb5dfc62ce3bea438d4c3a1d39abe7664",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "3301044192559d18d5fb73956b72ebd76088bb59006e7b29b33cf8b372b776e6",
    "source_lines": "L6855-L6938",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R018"
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
  "stable_id": "BRD-WS-17-R018",
  "title": "Mọi thao tác yêu cầu: - Runbook (nếu có)",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R019 — Replay giúp xử lý các trường hợp lỗi mà không cần viết Script hoặc thao tác trực tiếp trên Datab…

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
      "requirement_id": "BRD-WS-17-R019",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "f5cfd574986664a91b67439ea300127f8091f0bad99077f1cfcbe224a00fc040"
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
        "BRD-WS-17-R019-AC001",
        "BRD-WS-17-R019-AC002",
        "BRD-WS-17-R019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R019-O001",
      "obligation_text": "Replay giúp xử lý các trường hợp lỗi mà không cần viết Script hoặc thao tác trực tiếp trên Database"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Replay giúp xử lý các trường hợp lỗi mà không cần viết Script hoặc thao tác trực tiếp trên Database.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-019",
    "previous_temporary_key": "TMP-BRD-WS-17-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "34. Replay Platform",
    "source_context_sha256": "e3b46ff8ab39ade87f8ba8a9f09000c1364d0d744774b2b40fb23ec7c966c147",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "f5cfd574986664a91b67439ea300127f8091f0bad99077f1cfcbe224a00fc040",
    "source_lines": "L6940-L7015",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R019"
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
  "stable_id": "BRD-WS-17-R019",
  "title": "Replay giúp xử lý các trường hợp lỗi mà không cần viết Script hoặc thao tác trực tiếp trên Datab…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R020 — Replay chỉ được thực hiện bởi Operator có Permission phù hợp

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
      "requirement_id": "BRD-WS-17-R020",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "c9677296a14f6a3523d046d3051b0b9b6e6fdfa119b34e433afe8082ff6bdb07"
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
        "BRD-WS-17-R020-AC001",
        "BRD-WS-17-R020-AC002",
        "BRD-WS-17-R020-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R020-O001",
      "obligation_text": "Replay chỉ được thực hiện bởi Operator có Permission phù hợp"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R020-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R020 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R020 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R020-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R020-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R020 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Replay chỉ được thực hiện bởi Operator có Permission phù hợp.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-020",
    "previous_temporary_key": "TMP-BRD-WS-17-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "34. Replay Platform",
    "source_context_sha256": "e3b46ff8ab39ade87f8ba8a9f09000c1364d0d744774b2b40fb23ec7c966c147",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "c9677296a14f6a3523d046d3051b0b9b6e6fdfa119b34e433afe8082ff6bdb07",
    "source_lines": "L7017-L7127",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R020"
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
  "stable_id": "BRD-WS-17-R020",
  "title": "Replay chỉ được thực hiện bởi Operator có Permission phù hợp",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R021 — Mọi thao tác đều: - Kiểm tra Permission

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
      "requirement_id": "BRD-WS-17-R021",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "ed8ea67d43c881192de2ed7048f2964a9424d5b92cd120498543fb394cfebd3f"
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
        "BRD-WS-17-R021-AC001",
        "BRD-WS-17-R021-AC002",
        "BRD-WS-17-R021-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R021-O001",
      "obligation_text": "Mọi thao tác đều: - Kiểm tra Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R021-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R021 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R021 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R021-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R021-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R021 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thao tác đều: - Kiểm tra Permission",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-17-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-021",
    "previous_temporary_key": "TMP-BRD-WS-17-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Operation Permission",
    "source_context_sha256": "6d40656f50a9ead910dd75e3bc79e99ac8f3f397474048d45d6a87a735d3271d",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "ed8ea67d43c881192de2ed7048f2964a9424d5b92cd120498543fb394cfebd3f",
    "source_lines": "L7129-L7242",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R021"
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
  "stable_id": "BRD-WS-17-R021",
  "title": "Mọi thao tác đều: - Kiểm tra Permission",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R022 — Mọi thao tác đều: - Ghi Audit

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
      "requirement_id": "BRD-WS-17-R022",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "b4ee276b1597c86a8e08f5d6b4a715a27a5a898d7cb4135d1258535b2e241b8f"
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
        "BRD-WS-17-R022-AC001",
        "BRD-WS-17-R022-AC002",
        "BRD-WS-17-R022-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R022-O001",
      "obligation_text": "Mọi thao tác đều: - Ghi Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R022 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R022 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R022 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R022-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R022-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R022 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thao tác đều: - Ghi Audit",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-17-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-022",
    "previous_temporary_key": "TMP-BRD-WS-17-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Operation Permission",
    "source_context_sha256": "6d40656f50a9ead910dd75e3bc79e99ac8f3f397474048d45d6a87a735d3271d",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "b4ee276b1597c86a8e08f5d6b4a715a27a5a898d7cb4135d1258535b2e241b8f",
    "source_lines": "L7244-L7355",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R022"
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
  "stable_id": "BRD-WS-17-R022",
  "title": "Mọi thao tác đều: - Ghi Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R023 — Mọi thao tác đều: - Tuân thủ Security Policy

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
      "requirement_id": "BRD-WS-17-R023",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "2b5884ab755c0b6c3d1dac9084900f87075dc6736d7cf972e025ddc1d1b7909d"
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
        "BRD-WS-17-R023-AC001",
        "BRD-WS-17-R023-AC002",
        "BRD-WS-17-R023-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R023-O001",
      "obligation_text": "Mọi thao tác đều: - Tuân thủ Security Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R023-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R023 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R023 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R023-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R023-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R023 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thao tác đều: - Tuân thủ Security Policy",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-17-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-023",
    "previous_temporary_key": "TMP-BRD-WS-17-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Operation Permission",
    "source_context_sha256": "6d40656f50a9ead910dd75e3bc79e99ac8f3f397474048d45d6a87a735d3271d",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "2b5884ab755c0b6c3d1dac9084900f87075dc6736d7cf972e025ddc1d1b7909d",
    "source_lines": "L7357-L7470",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R023"
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
  "stable_id": "BRD-WS-17-R023",
  "title": "Mọi thao tác đều: - Tuân thủ Security Policy",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R024 — Version hiện tại chưa triển khai tự động mở rộng tài nguyên

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-17-R024",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version hiện tại chưa triển khai tự động mở rộng tài nguyên.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "docs/BRD/BRD-WS-17.md:L612"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-024",
    "previous_temporary_key": "TMP-BRD-WS-17-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Auto Scaling",
    "source_context_sha256": "bcf29d688f47334aa40500bdc112e9bfc515f9f4e3da2b5333277f4b6d7b29cf",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "15c04dacca91afb1cbccef27e95d9cbce439040ae79f49897d89b77d79599660",
    "source_lines": "L7472-L7533",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R024"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-17-R024",
  "title": "Version hiện tại chưa triển khai tự động mở rộng tài nguyên",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R025 — Version hiện tại chưa triển khai

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-17-R025",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Version hiện tại chưa triển khai.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "docs/BRD/BRD-WS-17.md:L922"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-17-025",
    "previous_temporary_key": "TMP-BRD-WS-17-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "35. Chaos Readiness",
    "source_context_sha256": "7ad31828e1954900121ef58910f0778d0e86628804d20e1962c93b86018944b1",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "c1b028d739304fa3ded7b96da5a24d694ea7261810de5d4769abd4de3499712e",
    "source_lines": "L7535-L7596",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R025"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-17-R025",
  "title": "Version hiện tại chưa triển khai",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R026 — Observable operational task

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-004",
        "P2-DEC-010"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-17-R026",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "a79af721e98177ae2ee4ce93043222408069001dbfc98fdc120b80c6fb2c3180"
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
        "BRD-WS-17-R026-AC001",
        "BRD-WS-17-R026-AC002",
        "BRD-WS-17-R026-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R026-O001",
      "obligation_text": "Mọi tác vụ vận hành phải có khả năng quan sát được thông qua trạng thái, kết quả và tín hiệu vận hành phù hợp"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi tác vụ vận hành phải có khả năng quan sát được thông qua trạng thái, kết quả và tín hiệu vận hành phù hợp.",
  "provenance": {
    "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-004",
      "P2-DEC-010"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Enterprise Operations Principle",
    "source_context_sha256": "f4b6aeebc35c74925667ca32adae5d22b689e2ba373fa7cae75a6f8c6fe8ee2a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "a79af721e98177ae2ee4ce93043222408069001dbfc98fdc120b80c6fb2c3180",
    "source_lines": "L7598-L7685",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R026"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-WS-17-R013"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-WS-17-R013"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R026",
  "title": "Observable operational task",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R027 — Auditable operational task

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-004",
        "P2-DEC-010"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-17-R027",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "d0b6531f91b7878c18a3753a5c57abc40619fa6b16f3246e1d5206fa687c9a78"
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
        "BRD-WS-17-R027-AC001",
        "BRD-WS-17-R027-AC002",
        "BRD-WS-17-R027-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R027-O001",
      "obligation_text": "Mọi tác vụ vận hành phải tạo bằng chứng audit bất biến, gắn với actor, thời điểm, phạm vi và kết quả"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R027-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R027 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R027 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R027-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R027-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R027 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi tác vụ vận hành phải tạo bằng chứng audit bất biến, gắn với actor, thời điểm, phạm vi và kết quả.",
  "provenance": {
    "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
    "approved_decision_contracts": {
      "P2-DEC-004": {
        "decision_id": "P2-DEC-004",
        "sections": [
          {
            "heading": "Mandatory event types",
            "items": [
              "operations.operation.started",
              "operations.operation.completed",
              "operations.operation.failed",
              "operations.operation.cancelled",
              "operations.retry.scheduled",
              "operations.retry.exhausted",
              "operations.manual_resolution.required",
              "operations.manual_resolution.resolved",
              "operations.maintenance.scheduled",
              "operations.maintenance.started",
              "operations.maintenance.completed",
              "operations.maintenance.cancelled",
              "operations.runbook.started",
              "operations.runbook.completed",
              "operations.runbook.failed",
              "operations.recovery.started",
              "operations.recovery.completed",
              "operations.recovery.failed"
            ]
          },
          {
            "heading": "Ownership and payload",
            "items": [
              "The owning capability publishes operation lifecycle events.",
              "Operations Platform publishes retry/exhaustion, maintenance, runbook, and recovery events when it owns the transition.",
              "Attempt telemetry remains metric/trace unless an attempt is materially scheduled or exhausted.",
              "The shared envelope is defined by P2-DEC-002.",
              "Additional fields are operation_id/type, state_before/after, attempt counters, deadline, outcome, reason_code, and runbook/recovery/maintenance references."
            ]
          },
          {
            "heading": "Transition contract",
            "items": [
              "The state transition is durable before publication.",
              "Delivery is at least once and consumers deduplicate by event_id.",
              "Sequence is monotonic per operation; there is no global ordering.",
              "A terminal state must not silently return to a non-terminal state.",
              "Manual resolution requires owner, reason, SLA reference, and audit.",
              "Transport topology remains architecture-owned."
            ]
          }
        ],
        "selected_option": 1,
        "status": "DECIDED_PENDING_PACK_APPROVAL",
        "title": "Mandatory Operations Platform events"
      }
    },
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-004",
      "P2-DEC-010"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Enterprise Operations Principle",
    "source_context_sha256": "f4b6aeebc35c74925667ca32adae5d22b689e2ba373fa7cae75a6f8c6fe8ee2a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "d0b6531f91b7878c18a3753a5c57abc40619fa6b16f3246e1d5206fa687c9a78",
    "source_lines": "L7687-L7863",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R027"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-WS-17-R013"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-WS-17-R013"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R027",
  "title": "Auditable operational task",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R028 — Configurable operational task

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-004",
        "P2-DEC-010"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-17-R028",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "18dc80c3f8c8bd92977150986277835851309786421785ccef304dbe30789c6b"
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
        "BRD-WS-17-R028-AC001",
        "BRD-WS-17-R028-AC002",
        "BRD-WS-17-R028-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R028-O001",
      "obligation_text": "Mọi tác vụ vận hành phải được cấu hình bằng policy có version thay vì hard-code quyết định vận hành"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi tác vụ vận hành phải được cấu hình bằng policy có version thay vì hard-code quyết định vận hành.",
  "provenance": {
    "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-004",
      "P2-DEC-010"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Enterprise Operations Principle",
    "source_context_sha256": "f4b6aeebc35c74925667ca32adae5d22b689e2ba373fa7cae75a6f8c6fe8ee2a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "18dc80c3f8c8bd92977150986277835851309786421785ccef304dbe30789c6b",
    "source_lines": "L7865-L7952",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R028"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-WS-17-R013"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-WS-17-R013"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R028",
  "title": "Configurable operational task",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R029 — Recoverable operational task

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-004",
        "P2-DEC-010"
      ],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-016",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-17-R029",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "fc5f7ec5de6d8864e25caf5d82f93c916e2337015ffdf40ff18590f73a07aa05"
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
        "BRD-WS-17-R029-AC001",
        "BRD-WS-17-R029-AC002",
        "BRD-WS-17-R029-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R029-O001",
      "obligation_text": "Mọi tác vụ vận hành phải có đường khôi phục xác định, có thể đối soát kết quả và bảo toàn bất biến khi thất bại"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R029-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R029 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R029 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R029-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R029-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R029 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi tác vụ vận hành phải có đường khôi phục xác định, có thể đối soát kết quả và bảo toàn bất biến khi thất bại.",
  "provenance": {
    "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
    "approved_decision_contracts": {
      "P2-DEC-003": {
        "decision_id": "P2-DEC-003",
        "sections": [
          {
            "heading": "Ownership and budget",
            "items": [
              "Connector Retry handles transient transport/provider failure inside one operation attempt.",
              "Operation Retry owns persisted business state, total SLA, fallback, compensation, and manual resolution.",
              "Each operation has one absolute deadline and one retry budget.",
              "The Connector receives only the remaining sub-budget.",
              "operation_attempt and connector_attempt counters are separate and share one correlation context.",
              "Provider SDK retries are disabled or counted in the shared budget.",
              "Side effects use a stable operation idempotency key."
            ]
          },
          {
            "heading": "Error classes",
            "items": [
              "TRANSIENT",
              "RATE_LIMITED",
              "TERMINAL",
              "AMBIGUOUS_OUTCOME",
              "POLICY_BLOCKED",
              "CANCELLED/DEADLINE_EXCEEDED"
            ]
          },
          {
            "heading": "Failure behavior",
            "items": [
              "Ambiguous payment, procurement, allocation, or fulfillment outcomes are queried/reconciled before side effects are repeated.",
              "Blind retry is prohibited and no exactly-once claim is made.",
              "On exhaustion, control returns to Operation; policy then selects fallback, compensation, DLQ, or manual resolution.",
              "Partial fulfillment continues to manual resolution and does not trigger automatic refund.",
              "Numeric budgets reference P2-DEC-010."
            ]
          }
        ],
        "selected_option": 1,
        "status": "DECIDED_PENDING_PACK_APPROVAL",
        "title": "Two-layer shared-budget retry ownership"
      },
      "P2-DEC-010": {
        "decision_id": "P2-DEC-010",
        "sections": [
          {
            "heading": "Service tiers",
            "items": [
              "T0_INTEGRITY_CRITICAL: availability 99.95%, RTO 15m, RPO 0 committed business records.",
              "T1_CUSTOMER_CRITICAL: availability 99.90%, RTO 1h, RPO 5m.",
              "T2_OPERATIONAL: availability 99.50%, RTO 4h, RPO 1h.",
              "T3_ANALYTICAL_BATCH: availability 99.00%, RTO 24h, RPO 24h."
            ]
          },
          {
            "heading": "Latency p95/p99",
            "items": [
              "Interactive read: 500ms / 1.5s.",
              "Local transactional command: 750ms / 2s.",
              "Async command acceptance: 1s / 3s.",
              "Operational search/table: 2s / 5s.",
              "Large report/export submission: 1s / 3s."
            ]
          },
          {
            "heading": "Timeout defaults",
            "items": [
              "Internal interactive hop: 2s.",
              "Public interactive request: 10s.",
              "External connect: 3s.",
              "External response: 15s, with synchronous hard cap 30s.",
              "Async acknowledgement: 1s p95.",
              "Inquiry/reconciliation: 15s."
            ]
          },
          {
            "heading": "Reservation",
            "items": [
              "Online default is 15m.",
              "Payment policy is configurable from 5m to 30m.",
              "Total with extension is at most 30m unless an approved method policy says otherwise.",
              "Extension is allowed only while provider state is PENDING.",
              "Inventory and promotion reservations share the payment-attempt lifecycle.",
              "Offline confirmation after expiry requires price, promotion, inventory, procurement, and fulfillment revalidation.",
              "Previously approved retry, refund, and manual-resolution rules remain effective."
            ]
          },
          {
            "heading": "Connector health",
            "items": [
              "Evaluation uses a rolling 5m window with a traffic floor of 20 attempts.",
              "DEGRADED: error at least 5%, p95 above SLO, or rate-limit at least 10%.",
              "UNHEALTHY: error at least 20%, three failed probes, circuit open, or credential/trust failure.",
              "RECOVERING: five successful probes and error below 5%, maintained for 10m.",
              "Business rejection is not connector technical failure.",
              "Routing does not select an UNHEALTHY connector."
            ]
          },
          {
            "heading": "Freshness",
            "items": [
              "F0_LIVE: p95 at most 60s, hard stale 5m.",
              "F1_NEAR_REAL_TIME: p95 at most 5m, hard stale 15m.",
              "F2_HOURLY: at most 60m.",
              "F3_DAILY: at most 24h and before 06:00 local business time.",
              "Every report/export includes data_as_of, generated_at, timezone, freshness tier, completeness/provisional state, filters, and snapshot identity."
            ]
          },
          {
            "heading": "Governance",
            "items": [
              "SLO uses a rolling 30-day window with burn-rate monitoring.",
              "Correctness/integrity is not an availability error-budget allowance.",
              "User-impacting planned maintenance counts unless explicitly contracted.",
              "Missing telemetry is failure.",
              "A configuration override requires owner, reason, expiry, approval, and audit.",
              "RTO/RPO is tested through drills.",
              "SLA is used only when contractual consequences exist."
            ]
          },
          {
            "heading": "References",
            "items": [
              "https://sre.google/sre-book/service-level-objectives/",
              "https://sre.google/workbook/implementing-slos/"
            ]
          }
        ],
        "selected_option": 1,
        "status": "DECIDED_PENDING_PACK_APPROVAL",
        "title": "Reliability, timeout, and freshness matrices"
      }
    },
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-004",
      "P2-DEC-010"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Enterprise Operations Principle",
    "source_context_sha256": "f4b6aeebc35c74925667ca32adae5d22b689e2ba373fa7cae75a6f8c6fe8ee2a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "fc5f7ec5de6d8864e25caf5d82f93c916e2337015ffdf40ff18590f73a07aa05",
    "source_lines": "L7954-L8213",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R029"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-WS-17-R013"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-WS-17-R013"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R029",
  "title": "Recoverable operational task",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R030 — Automatable operational task

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
  "normative_statement": "Mọi tác vụ vận hành phải có contract cho phép tự động hóa có kiểm soát, permission và audit.",
  "provenance": {
    "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-004",
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Enterprise Operations Principle",
    "source_context_sha256": "f4b6aeebc35c74925667ca32adae5d22b689e2ba373fa7cae75a6f8c6fe8ee2a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "998ff8a61e478a1159db77563dc727563b24e3850e7ffaf90f8ab44da6ed004e",
    "source_fingerprint_before_c3": null,
    "source_lines": "L8215-L8282",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R030"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [
      "BRD-WS-17-R013"
    ],
    "derived_requirements": [
      "BRD-WS-17-R041",
      "BRD-WS-17-R042",
      "BRD-WS-17-R043"
    ],
    "satisfies_composite_parents": [
      "BRD-WS-17-R013"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R030",
  "title": "Automatable operational task",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R031 — No direct infrastructure manipulation

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-004",
        "P2-DEC-010"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-17-R031",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "6cb5dec3517d16a8f4fbc8c9bd5d5509b5da04093f49c55dd9b1ba000f7f58de"
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
        "BRD-WS-17-R031-AC001",
        "BRD-WS-17-R031-AC002",
        "BRD-WS-17-R031-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R031-O001",
      "obligation_text": "Operator không được thao tác trực tiếp trên hạ tầng khi Platform đã cung cấp thao tác tương ứng"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R031-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R031 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R031 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R031-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-17-R031-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-17-R031 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operator không được thao tác trực tiếp trên hạ tầng khi Platform đã cung cấp thao tác tương ứng.",
  "provenance": {
    "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-004",
      "P2-DEC-010"
    ],
    "identity_origin": "PHASE_2C_NEW_ALLOCATION",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Enterprise Operations Principle",
    "source_context_sha256": "f4b6aeebc35c74925667ca32adae5d22b689e2ba373fa7cae75a6f8c6fe8ee2a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "6cb5dec3517d16a8f4fbc8c9bd5d5509b5da04093f49c55dd9b1ba000f7f58de",
    "source_lines": "L8284-L8406",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R031"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-WS-17-R013"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-WS-17-R013"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R031",
  "title": "No direct infrastructure manipulation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R032 — Alert Rule là Business Object

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
      "requirement_id": "BRD-WS-17-R032",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "b757bac6b5a2073797eea638dd84e0f3faecfc0b75240c3a4bc28be82a2d968a"
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
        "BRD-WS-17-R032-AC001",
        "BRD-WS-17-R032-AC002",
        "BRD-WS-17-R032-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R032-O001",
      "obligation_text": "Alert Rule là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Alert Rule là Business Object.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-17-005",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R032",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Alert Rule",
    "source_context_sha256": "20268973697bfc64bdd4536c7deca7ea62de0777e79a4ef2903bd3f315dcad18",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "b757bac6b5a2073797eea638dd84e0f3faecfc0b75240c3a4bc28be82a2d968a",
    "source_fingerprint_before_c3": "b757bac6b5a2073797eea638dd84e0f3faecfc0b75240c3a4bc28be82a2d968a",
    "source_lines": "L8408-L8500",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R032"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-17-005"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-17-005"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R032",
  "title": "Alert Rule là Business Object",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R033 — Alert Rule được cấu hình

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
      "requirement_id": "BRD-WS-17-R033",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "9464c3992afb49e38d16abdace1d46e27152f00917da3e5c813875d64aa750f0"
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
        "BRD-WS-17-R033-AC001",
        "BRD-WS-17-R033-AC002",
        "BRD-WS-17-R033-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R033-O001",
      "obligation_text": "Alert Rule được cấu hình"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Alert Rule được cấu hình.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-17-005",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R033",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Alert Rule",
    "source_context_sha256": "20268973697bfc64bdd4536c7deca7ea62de0777e79a4ef2903bd3f315dcad18",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "9464c3992afb49e38d16abdace1d46e27152f00917da3e5c813875d64aa750f0",
    "source_fingerprint_before_c3": "9464c3992afb49e38d16abdace1d46e27152f00917da3e5c813875d64aa750f0",
    "source_lines": "L8502-L8594",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R033"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-17-005"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-17-005"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R033",
  "title": "Alert Rule được cấu hình",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R034 — Không Hard-code

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
      "requirement_id": "BRD-WS-17-R034",
      "source_document": "docs/BRD/BRD-WS-17.md",
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
        "BRD-WS-17-R034-AC001",
        "BRD-WS-17-R034-AC002",
        "BRD-WS-17-R034-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R034-O001",
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
    "derived_from_parent": "BD-17-005",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R034",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Alert Rule",
    "source_context_sha256": "20268973697bfc64bdd4536c7deca7ea62de0777e79a4ef2903bd3f315dcad18",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "4a4f9fc70196c62582583bd1f5a465fcfd49191969988f4db3f00452e0acf501",
    "source_fingerprint_before_c3": "4a4f9fc70196c62582583bd1f5a465fcfd49191969988f4db3f00452e0acf501",
    "source_lines": "L8596-L8688",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R034"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-17-005"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-17-005"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R034",
  "title": "Không Hard-code",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R035 — Alert được gửi theo Notification Preference

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
      "requirement_id": "BRD-WS-17-R035",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "9456566f656a118dc88dc9ce0b35336606c7775fa6a64cc9c220f791388e07f6"
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
        "BRD-WS-17-R035-AC001",
        "BRD-WS-17-R035-AC002",
        "BRD-WS-17-R035-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R035-O001",
      "obligation_text": "Alert được gửi theo Notification Preference"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Alert được gửi theo Notification Preference.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-17-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R035",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-006",
    "source_context_sha256": "da00372cb2b839eb3d3445a3cb7fb61416558a5cc85f95e72c2bf933f422f32b",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "9456566f656a118dc88dc9ce0b35336606c7775fa6a64cc9c220f791388e07f6",
    "source_fingerprint_before_c3": "9456566f656a118dc88dc9ce0b35336606c7775fa6a64cc9c220f791388e07f6",
    "source_lines": "L8690-L8782",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R035"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-17-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-17-006"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R035",
  "title": "Alert được gửi theo Notification Preference",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R036 — Personal Inbox luôn là kênh nhận mặc định

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
      "requirement_id": "BRD-WS-17-R036",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "f35e2a44d8dd5c489d011c36443261322d385378594d1030bc2bb9f131914df8"
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
        "BRD-WS-17-R036-AC001",
        "BRD-WS-17-R036-AC002",
        "BRD-WS-17-R036-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R036-O001",
      "obligation_text": "Personal Inbox luôn là kênh nhận mặc định"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Personal Inbox luôn là kênh nhận mặc định.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-17-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R036",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-006",
    "source_context_sha256": "da00372cb2b839eb3d3445a3cb7fb61416558a5cc85f95e72c2bf933f422f32b",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "f35e2a44d8dd5c489d011c36443261322d385378594d1030bc2bb9f131914df8",
    "source_fingerprint_before_c3": "f35e2a44d8dd5c489d011c36443261322d385378594d1030bc2bb9f131914df8",
    "source_lines": "L8784-L8876",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R036"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-17-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-17-006"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R036",
  "title": "Personal Inbox luôn là kênh nhận mặc định",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R037 — Scheduler là Business Object. Scheduler hỗ trợ: Cron

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
      "requirement_id": "BRD-WS-17-R037",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "2e4110182479f13f22ccf98ee8454161bc787af581700a985eb5fb387a45ec72"
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
        "BRD-WS-17-R037-AC001",
        "BRD-WS-17-R037-AC003",
        "BRD-WS-17-R037-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R037-O001",
      "obligation_text": "Scheduler là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-17-R037-AC002",
        "BRD-WS-17-R037-AC003",
        "BRD-WS-17-R037-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R037-O002",
      "obligation_text": "Scheduler hỗ trợ: Cron"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Scheduler là Business Object. Scheduler hỗ trợ: Cron.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-17-007",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R037",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Scheduler",
    "source_context_sha256": "867847cfa5f35a218d9ca4c09054fad6f3806ef2db0bd26361426efbaad00983",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "2e4110182479f13f22ccf98ee8454161bc787af581700a985eb5fb387a45ec72",
    "source_fingerprint_before_c3": "2e4110182479f13f22ccf98ee8454161bc787af581700a985eb5fb387a45ec72",
    "source_lines": "L8878-L8980",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R037"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-17-007"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-17-007"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R037",
  "title": "Scheduler là Business Object. Scheduler hỗ trợ: Cron",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R038 — Scheduler là Business Object. Scheduler hỗ trợ: Fixed Interval

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
      "requirement_id": "BRD-WS-17-R038",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "62abd614da4eed656b0387b9709829ced44755c94fb894e61658d82b6f982fdc"
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
        "BRD-WS-17-R038-AC001",
        "BRD-WS-17-R038-AC003",
        "BRD-WS-17-R038-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R038-O001",
      "obligation_text": "Scheduler là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-17-R038-AC002",
        "BRD-WS-17-R038-AC003",
        "BRD-WS-17-R038-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R038-O002",
      "obligation_text": "Scheduler hỗ trợ: Fixed Interval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Scheduler là Business Object. Scheduler hỗ trợ: Fixed Interval.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-17-007",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R038",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Scheduler",
    "source_context_sha256": "867847cfa5f35a218d9ca4c09054fad6f3806ef2db0bd26361426efbaad00983",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "62abd614da4eed656b0387b9709829ced44755c94fb894e61658d82b6f982fdc",
    "source_fingerprint_before_c3": "62abd614da4eed656b0387b9709829ced44755c94fb894e61658d82b6f982fdc",
    "source_lines": "L8982-L9084",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R038"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-17-007"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-17-007"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R038",
  "title": "Scheduler là Business Object. Scheduler hỗ trợ: Fixed Interval",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R039 — Scheduler là Business Object. Scheduler hỗ trợ: Manual Trigger

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
      "requirement_id": "BRD-WS-17-R039",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "112d2e1b18471752254f132009692c975c3c30f772fbda2f83e927954671c55a"
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
        "BRD-WS-17-R039-AC001",
        "BRD-WS-17-R039-AC003",
        "BRD-WS-17-R039-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R039-O001",
      "obligation_text": "Scheduler là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-17-R039-AC002",
        "BRD-WS-17-R039-AC003",
        "BRD-WS-17-R039-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R039-O002",
      "obligation_text": "Scheduler hỗ trợ: Manual Trigger"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Scheduler là Business Object. Scheduler hỗ trợ: Manual Trigger.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-17-007",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R039",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Scheduler",
    "source_context_sha256": "867847cfa5f35a218d9ca4c09054fad6f3806ef2db0bd26361426efbaad00983",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "112d2e1b18471752254f132009692c975c3c30f772fbda2f83e927954671c55a",
    "source_fingerprint_before_c3": "112d2e1b18471752254f132009692c975c3c30f772fbda2f83e927954671c55a",
    "source_lines": "L9086-L9188",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R039"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-17-007"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-17-007"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R039",
  "title": "Scheduler là Business Object. Scheduler hỗ trợ: Manual Trigger",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R040 — Scheduler là Business Object. Scheduler hỗ trợ: Business Event Trigger

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
      "requirement_id": "BRD-WS-17-R040",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "2d15fd0c813776d2977f859c14d2ce9c3fb5b85c9e6869495788d86d4a3df639"
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
        "BRD-WS-17-R040-AC001",
        "BRD-WS-17-R040-AC003",
        "BRD-WS-17-R040-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R040-O001",
      "obligation_text": "Scheduler là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-17-R040-AC002",
        "BRD-WS-17-R040-AC003",
        "BRD-WS-17-R040-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R040-O002",
      "obligation_text": "Scheduler hỗ trợ: Business Event Trigger"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Scheduler là Business Object. Scheduler hỗ trợ: Business Event Trigger.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-17-007",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R040",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Scheduler",
    "source_context_sha256": "867847cfa5f35a218d9ca4c09054fad6f3806ef2db0bd26361426efbaad00983",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "2d15fd0c813776d2977f859c14d2ce9c3fb5b85c9e6869495788d86d4a3df639",
    "source_fingerprint_before_c3": "2d15fd0c813776d2977f859c14d2ce9c3fb5b85c9e6869495788d86d4a3df639",
    "source_lines": "L9190-L9292",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R040"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-17-007"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-17-007"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R040",
  "title": "Scheduler là Business Object. Scheduler hỗ trợ: Business Event Trigger",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R041 — Tác vụ vận hành phải có contract automation có kiểm soát

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-004",
        "P2-DEC-010",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-17-R041",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "a5c4b6af38c37fd6ef1ab9f6d3c1b6f33bd1c66585ebab7f363f005af22c1e54"
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
        "BRD-WS-17-R041-AC001",
        "BRD-WS-17-R041-AC002",
        "BRD-WS-17-R041-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R041-O001",
      "obligation_text": "Tác vụ vận hành phải có contract automation có kiểm soát"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Tác vụ vận hành phải có contract automation có kiểm soát.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-004",
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BRD-WS-17-R030",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R041",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Enterprise Operations Principle",
    "source_context_sha256": "f4b6aeebc35c74925667ca32adae5d22b689e2ba373fa7cae75a6f8c6fe8ee2a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "a5c4b6af38c37fd6ef1ab9f6d3c1b6f33bd1c66585ebab7f363f005af22c1e54",
    "source_fingerprint_before_c3": "a5c4b6af38c37fd6ef1ab9f6d3c1b6f33bd1c66585ebab7f363f005af22c1e54",
    "source_lines": "L9294-L9392",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R041"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-WS-17-R030"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-WS-17-R030"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R041",
  "title": "Tác vụ vận hành phải có contract automation có kiểm soát",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R042 — Automation tác vụ vận hành phải enforce Permission

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-004",
        "P2-DEC-010",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-17-R042",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "73361f533504bbec94510cb62b67e7b108183eb70337c013640cbf6f59ae94d1"
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
        "BRD-WS-17-R042-AC001",
        "BRD-WS-17-R042-AC002",
        "BRD-WS-17-R042-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R042-O001",
      "obligation_text": "Automation tác vụ vận hành phải enforce Permission"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Automation tác vụ vận hành phải enforce Permission.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-004",
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BRD-WS-17-R030",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R042",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Enterprise Operations Principle",
    "source_context_sha256": "f4b6aeebc35c74925667ca32adae5d22b689e2ba373fa7cae75a6f8c6fe8ee2a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "73361f533504bbec94510cb62b67e7b108183eb70337c013640cbf6f59ae94d1",
    "source_fingerprint_before_c3": "73361f533504bbec94510cb62b67e7b108183eb70337c013640cbf6f59ae94d1",
    "source_lines": "L9394-L9492",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R042"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-WS-17-R030"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-WS-17-R030"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R042",
  "title": "Automation tác vụ vận hành phải enforce Permission",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R043 — Automation tác vụ vận hành phải tạo Audit evidence

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-004",
        "P2-DEC-010",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-17-R043",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "7c5ee629b2853e0f983e6775abb68e3d772d7bf793b41333127feffd27779dfd"
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
        "BRD-WS-17-R043-AC001",
        "BRD-WS-17-R043-AC002",
        "BRD-WS-17-R043-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R043-O001",
      "obligation_text": "Automation tác vụ vận hành phải tạo Audit evidence"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Automation tác vụ vận hành phải tạo Audit evidence.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-004",
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BRD-WS-17-R030",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-17-R043",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Enterprise Operations Principle",
    "source_context_sha256": "f4b6aeebc35c74925667ca32adae5d22b689e2ba373fa7cae75a6f8c6fe8ee2a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "7c5ee629b2853e0f983e6775abb68e3d772d7bf793b41333127feffd27779dfd",
    "source_fingerprint_before_c3": "7c5ee629b2853e0f983e6775abb68e3d772d7bf793b41333127feffd27779dfd",
    "source_lines": "L9494-L9592",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-17-R043"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-WS-17-R030"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-WS-17-R030"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-17-R043",
  "title": "Automation tác vụ vận hành phải tạo Audit evidence",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-17-001 — Platform Operations được quản lý tập trung thông qua Platform Operations Center

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-020",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-17-001",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "fee1a2f6f49163a911ab0e0b6572734fab1456866d77a59d914f21d143872033"
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
        "EP-17-001-AC001",
        "EP-17-001-AC002",
        "EP-17-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-001-O001",
      "obligation_text": "Platform Operations được quản lý tập trung thông qua Platform Operations Center"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform Operations được quản lý tập trung thông qua Platform Operations Center.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-17-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-17-001",
    "source_context_sha256": "c579432cbfd1b21e18bda6a2a172c5080577cc9674839abd731ab2582202cc37",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "fee1a2f6f49163a911ab0e0b6572734fab1456866d77a59d914f21d143872033",
    "source_lines": "L9594-L9673",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-17-001"
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
  "stable_id": "EP-17-001",
  "title": "Platform Operations được quản lý tập trung thông qua Platform Operations Center",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-17-002 — Monitoring phải bao phủ toàn Platform

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "A deliberately excluded non-platform dependency is documented and not counted as a platform component"
    ],
    "concrete_bindings": [
      {
        "actual_set": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "MONITORING.REGISTRATION.OBSERVED.COMPONENT.SET",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "YSIM.MONITORING_COVERAGE.OBSERVED_COMPONENT_COVERAGE.RUNTIME_OBSERVED",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-17-002-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-17.md",
            "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
            "source_lines": "L1241-L1244",
            "source_section": "38. Enterprise Design Principles > EP-17-002"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "OBSERVE.EP-17-002.MONITORING.REGISTRATION.OBSERVED.COMPONENT.SET",
            "version": "1.0.0"
          },
          "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
        },
        "expected_set": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "PLATFORM.COMPONENT.INVENTORY.ACTIVE.SET",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "YSIM.PLATFORM_COMPONENT_INVENTORY.ACTIVE_COMPONENT_SET.CANONICAL_REGISTRY",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-17-002-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-17.md",
            "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
            "source_lines": "L1241-L1244",
            "source_section": "38. Enterprise Design Principles > EP-17-002"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "RESOLVE.EP-17-002.PLATFORM.COMPONENT.INVENTORY.ACTIVE.SET",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
        }
      },
      {
        "evidence_object": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-17-002.EVIDENCE_OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.EVIDENCE_OBJECT.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-17-002-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-17.md",
            "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
            "source_lines": "L1241-L1244",
            "source_section": "38. Enterprise Design Principles > EP-17-002"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.EP-17-002.EP-17-002.EVIDENCE_OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "required_fields": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.PLATFORM_COMPONENT_INVENTORY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-17-002-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                "source_lines": "L1241-L1244",
                "source_section": "38. Enterprise Design Principles > EP-17-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.EP-17-002.FIELD.PLATFORM_COMPONENT_INVENTORY",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.MONITORED_COMPONENT_IDS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-17-002-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                "source_lines": "L1241-L1244",
                "source_section": "38. Enterprise Design Principles > EP-17-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.EP-17-002.FIELD.MONITORED_COMPONENT_IDS",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.REQUIRED_SIGNALS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-17-002-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                "source_lines": "L1241-L1244",
                "source_section": "38. Enterprise Design Principles > EP-17-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.EP-17-002.FIELD.REQUIRED_SIGNALS",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "FIELD.COVERAGE_RESULT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-17-002-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                "source_lines": "L1241-L1244",
                "source_section": "38. Enterprise Design Principles > EP-17-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.EP-17-002.FIELD.COVERAGE_RESULT",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          ],
          "origin": {
            "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-17-002-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-17.md",
            "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
            "source_lines": "L1241-L1244",
            "source_section": "38. Enterprise Design Principles > EP-17-002"
          },
          "semantic_type": "SET_OF<FIELD_ID>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.EP-17-002",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "A platform component has no required monitoring evidence"
    ],
    "operator_composition": [
      "SET_EQUALS",
      "EVIDENCE_FIELD_PRESENT"
    ],
    "positive_oracle": [
      "Monitoring covers every platform component in the inventory"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2C-OBT-C1-EP-17-002-OPT-1"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
      "source_lines": "L1241-L1244",
      "source_section": "38. Enterprise Design Principles > EP-17-002"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
          "source_type": "APPROVED_DECISION",
          "version": "2026-07-16"
        },
        "identifier": "EP-17-002.EP-17-002.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "EP-17-002.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2C-OBT-C1-EP-17-002-OPT-1"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-17.md",
          "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
          "source_lines": "L1241-L1244",
          "source_section": "38. Enterprise Design Principles > EP-17-002"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.EP-17-002.EP-17-002.EP-17-002.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "EP-17-002.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PLATFORM_COMPONENT_INVENTORY",
        "FIELD.MONITORED_COMPONENT_IDS",
        "FIELD.REQUIRED_SIGNALS",
        "FIELD.COVERAGE_RESULT"
      ],
      "producer": "EP-17-002.EVIDENCE.PRODUCER",
      "required_collection_origin": "EP-17-002.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PLATFORM_COMPONENT_INVENTORY",
        "FIELD.MONITORED_COMPONENT_IDS",
        "FIELD.REQUIRED_SIGNALS",
        "FIELD.COVERAGE_RESULT"
      ],
      "required_values_or_hashes": [
        "EP-17-002.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "EP-17-002.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "EP-17-002.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "EP-17-002-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": {
        "meaning": "A versioned Platform Component Inventory and component-class monitoring profiles define coverage and required signals.",
        "non_inferences": [
          "No component or signal list is invented.",
          "Non-critical components are not excluded from monitoring."
        ],
        "option_id": "P2C-OBT-C1-EP-17-002-OPT-1"
      },
      "assertions": [
        {
          "assertion_id": "EP-17-002.O1.1.SET_EQUALS",
          "evaluator_consumed_bindings": [
            "actual_set",
            "expected_set"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "EP-17-002.EP-17-002.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-17-002.O1.1.SET_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-17-002-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-17.md",
              "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
              "source_lines": "L1241-L1244",
              "source_section": "38. Enterprise Design Principles > EP-17-002"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.EP-17-002.EP-17-002.EP-17-002.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-17-002.O1.1.SET_EQUALS.AUTHORITY.ORIGIN.MEMBER.1",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-17-002-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                  "source_lines": "L1241-L1244",
                  "source_section": "38. Enterprise Design Principles > EP-17-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.EP-17-002.EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "EP-17-002.O1.1.SET_EQUALS.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-17-002-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-17.md",
              "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
              "source_lines": "L1241-L1244",
              "source_section": "38. Enterprise Design Principles > EP-17-002"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "MONITORING.REGISTRATION.OBSERVED.COMPONENT.SET",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "YSIM.MONITORING_COVERAGE.OBSERVED_COMPONENT_COVERAGE.RUNTIME_OBSERVED",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-17-002-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                  "source_lines": "L1241-L1244",
                  "source_section": "38. Enterprise Design Principles > EP-17-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "OBSERVE.EP-17-002.MONITORING.REGISTRATION.OBSERVED.COMPONENT.SET",
                  "version": "1.0.0"
                },
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
              },
              "expected_set": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "PLATFORM.COMPONENT.INVENTORY.ACTIVE.SET",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "YSIM.PLATFORM_COMPONENT_INVENTORY.ACTIVE_COMPONENT_SET.CANONICAL_REGISTRY",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-17-002-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                  "source_lines": "L1241-L1244",
                  "source_section": "38. Enterprise Design Principles > EP-17-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "RESOLVE.EP-17-002.PLATFORM.COMPONENT.INVENTORY.ACTIVE.SET",
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
                        "EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "EP-17-002.O1.1.SET_EQUALS.AUTHORITY.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-EP-17-002-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-17.md",
                      "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                      "source_lines": "L1241-L1244",
                      "source_section": "38. Enterprise Design Principles > EP-17-002"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.EP-17-002.EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "EP-17-002.O1.1.SET_EQUALS.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-17-002-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                  "source_lines": "L1241-L1244",
                  "source_section": "38. Enterprise Design Principles > EP-17-002"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "EP-17-002.O1.1.SET_EQUALS.OBSERVED.ORIGIN.MEMBER.1",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-EP-17-002-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-17.md",
                      "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                      "source_lines": "L1241-L1244",
                      "source_section": "38. Enterprise Design Principles > EP-17-002"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "OBSERVE.EP-17-002.EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "EP-17-002.O1.1.SET_EQUALS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-17-002-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                  "source_lines": "L1241-L1244",
                  "source_section": "38. Enterprise Design Principles > EP-17-002"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-17-002.EP-17-002.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-17-002.O1.1.SET_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-17-002-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                "source_lines": "L1241-L1244",
                "source_section": "38. Enterprise Design Principles > EP-17-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.EP-17-002.EP-17-002.EP-17-002.O1.1.SET_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SET_EQUALS"
          },
          "obligation_id": "EP-17-002-O001",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-17-002.O1.1.SET_EQUALS.OBSERVED.ORIGIN.MEMBER.1",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-17-002-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                  "source_lines": "L1241-L1244",
                  "source_section": "38. Enterprise Design Principles > EP-17-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.EP-17-002.EP-17-002.EP-17-002.O1.1.SET_EQUALS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "EP-17-002.O1.1.SET_EQUALS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-17-002-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-17.md",
              "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
              "source_lines": "L1241-L1244",
              "source_section": "38. Enterprise Design Principles > EP-17-002"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "operator_id": "SET_EQUALS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_set": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "MONITORING.REGISTRATION.OBSERVED.COMPONENT.SET",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "YSIM.MONITORING_COVERAGE.OBSERVED_COMPONENT_COVERAGE.RUNTIME_OBSERVED",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-17-002-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                "source_lines": "L1241-L1244",
                "source_section": "38. Enterprise Design Principles > EP-17-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "OBSERVE.EP-17-002.MONITORING.REGISTRATION.OBSERVED.COMPONENT.SET",
                "version": "1.0.0"
              },
              "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
            },
            "expected_set": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "PLATFORM.COMPONENT.INVENTORY.ACTIVE.SET",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "YSIM.PLATFORM_COMPONENT_INVENTORY.ACTIVE_COMPONENT_SET.CANONICAL_REGISTRY",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-17-002-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                "source_lines": "L1241-L1244",
                "source_section": "38. Enterprise Design Principles > EP-17-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "RESOLVE.EP-17-002.PLATFORM.COMPONENT.INVENTORY.ACTIVE.SET",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
            }
          }
        },
        {
          "assertion_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT",
          "evaluator_consumed_bindings": [
            "evidence_object",
            "required_fields"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-17-002-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-17.md",
              "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
              "source_lines": "L1241-L1244",
              "source_section": "38. Enterprise Design Principles > EP-17-002"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.EP-17-002.EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-17-002-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-17.md",
              "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
              "source_lines": "L1241-L1244",
              "source_section": "38. Enterprise Design Principles > EP-17-002"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "RESOLVE.EP-17-002.EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "evidence_object": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-17-002.EVIDENCE_OBJECT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.EVIDENCE_OBJECT.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-17-002-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                  "source_lines": "L1241-L1244",
                  "source_section": "38. Enterprise Design Principles > EP-17-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.EP-17-002.EP-17-002.EVIDENCE_OBJECT",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "required_fields": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.PLATFORM_COMPONENT_INVENTORY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-EP-17-002-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-17.md",
                      "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                      "source_lines": "L1241-L1244",
                      "source_section": "38. Enterprise Design Principles > EP-17-002"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.EP-17-002.FIELD.PLATFORM_COMPONENT_INVENTORY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.MONITORED_COMPONENT_IDS",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-EP-17-002-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-17.md",
                      "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                      "source_lines": "L1241-L1244",
                      "source_section": "38. Enterprise Design Principles > EP-17-002"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.EP-17-002.FIELD.MONITORED_COMPONENT_IDS",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.REQUIRED_SIGNALS",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-EP-17-002-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-17.md",
                      "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                      "source_lines": "L1241-L1244",
                      "source_section": "38. Enterprise Design Principles > EP-17-002"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.EP-17-002.FIELD.REQUIRED_SIGNALS",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "FIELD.COVERAGE_RESULT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-EP-17-002-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-17.md",
                      "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                      "source_lines": "L1241-L1244",
                      "source_section": "38. Enterprise Design Principles > EP-17-002"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.EP-17-002.FIELD.COVERAGE_RESULT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  }
                ],
                "origin": {
                  "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-17-002-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                  "source_lines": "L1241-L1244",
                  "source_section": "38. Enterprise Design Principles > EP-17-002"
                },
                "semantic_type": "SET_OF<FIELD_ID>"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-17-002-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                  "source_lines": "L1241-L1244",
                  "source_section": "38. Enterprise Design Principles > EP-17-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.EP-17-002.EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-EP-17-002-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-17.md",
                  "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                  "source_lines": "L1241-L1244",
                  "source_section": "38. Enterprise Design Principles > EP-17-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "OBSERVE.EP-17-002.EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-17-002-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                "source_lines": "L1241-L1244",
                "source_section": "38. Enterprise Design Principles > EP-17-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.EP-17-002.EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "EVIDENCE_FIELD_PRESENT"
          },
          "obligation_id": "EP-17-002-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-EP-17-002-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-17.md",
              "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
              "source_lines": "L1241-L1244",
              "source_section": "38. Enterprise Design Principles > EP-17-002"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.EP-17-002.EP-17-002.EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "operator_id": "EVIDENCE_FIELD_PRESENT",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "EP-17-002.EVIDENCE_OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.EVIDENCE_OBJECT.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-17-002-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                "source_lines": "L1241-L1244",
                "source_section": "38. Enterprise Design Principles > EP-17-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.EP-17-002.EP-17-002.EVIDENCE_OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "required_fields": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.PLATFORM_COMPONENT_INVENTORY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-EP-17-002-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-17.md",
                    "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                    "source_lines": "L1241-L1244",
                    "source_section": "38. Enterprise Design Principles > EP-17-002"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.EP-17-002.FIELD.PLATFORM_COMPONENT_INVENTORY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.MONITORED_COMPONENT_IDS",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-EP-17-002-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-17.md",
                    "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                    "source_lines": "L1241-L1244",
                    "source_section": "38. Enterprise Design Principles > EP-17-002"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.EP-17-002.FIELD.MONITORED_COMPONENT_IDS",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.REQUIRED_SIGNALS",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-EP-17-002-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-17.md",
                    "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                    "source_lines": "L1241-L1244",
                    "source_section": "38. Enterprise Design Principles > EP-17-002"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.EP-17-002.FIELD.REQUIRED_SIGNALS",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "FIELD.COVERAGE_RESULT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-EP-17-002-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-17.md",
                    "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                    "source_lines": "L1241-L1244",
                    "source_section": "38. Enterprise Design Principles > EP-17-002"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.EP-17-002.FIELD.COVERAGE_RESULT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                }
              ],
              "origin": {
                "origin_id": "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT.REQUIRED_FIELDS.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-EP-17-002-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-17.md",
                "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
                "source_lines": "L1241-L1244",
                "source_section": "38. Enterprise Design Principles > EP-17-002"
              },
              "semantic_type": "SET_OF<FIELD_ID>"
            }
          }
        }
      ],
      "boundary_cases": [
        "A deliberately excluded non-platform dependency is documented and not counted as a platform component"
      ],
      "contract_ast_sha256": "313b95662d21a3c1b59e0509142a49f3614c9123a10d5a09f11c8ad68faeda17",
      "contract_id": "P2C.C4.CONTRACT.EP-17-002",
      "criticality": "HIGH",
      "disposition": "SOURCE_CLARIFICATION_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-EP-17-002-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "EP-17-002.EP-17-002.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-17-002.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-EP-17-002-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-17.md",
            "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
            "source_lines": "L1241-L1244",
            "source_section": "38. Enterprise Design Principles > EP-17-002"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.EP-17-002.EP-17-002.EP-17-002.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "EP-17-002.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PLATFORM_COMPONENT_INVENTORY",
          "FIELD.MONITORED_COMPONENT_IDS",
          "FIELD.REQUIRED_SIGNALS",
          "FIELD.COVERAGE_RESULT"
        ],
        "producer": "EP-17-002.EVIDENCE.PRODUCER",
        "required_collection_origin": "EP-17-002.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PLATFORM_COMPONENT_INVENTORY",
          "FIELD.MONITORED_COMPONENT_IDS",
          "FIELD.REQUIRED_SIGNALS",
          "FIELD.COVERAGE_RESULT"
        ],
        "required_values_or_hashes": [
          "EP-17-002.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "EP-17-002.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "EP-17-002.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-300697729CFCEE4B02FF",
        "P2C-C4-FX-345D50832AD7F98EAC4B",
        "P2C-C4-FX-6ED7BEE40AF8B656BF26"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "A platform component has no required monitoring evidence"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "EP-17-002-O001",
          "obligation_text": "Monitoring phải bao phủ toàn Platform"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "EP-17-002.O1.1.SET_EQUALS",
            "EP-17-002.O1.2.EVIDENCE_FIELD_PRESENT"
          ],
          "coverage_count": 1,
          "obligation_id": "EP-17-002-O001"
        }
      ],
      "operator_composition": [
        "SET_EQUALS",
        "EVIDENCE_FIELD_PRESENT"
      ],
      "positive_oracles": [
        "Monitoring covers every platform component in the inventory"
      ],
      "preconditions": [
        "The platform component and required signal inventory are known"
      ],
      "prohibitions": [
        "A platform component has no required monitoring evidence"
      ],
      "requirement_id": "EP-17-002",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2C-OBT-C1-EP-17-002-OPT-1"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-17.md",
        "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
        "source_lines": "L1241-L1244",
        "source_section": "38. Enterprise Design Principles > EP-17-002"
      },
      "source_statement": "Monitoring phải bao phủ toàn Platform.",
      "surrounding_source_context": "## EP-17-002\n\nMonitoring phải bao phủ toàn Platform.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.EP-17-002",
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
        "EP-17-002-AC001",
        "EP-17-002-AC002",
        "EP-17-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-002-O001",
      "obligation_text": "Monitoring phải bao phủ toàn Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Monitoring phải bao phủ toàn Platform.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-17-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-17-002",
    "source_context_sha256": "a1f3d85143538f7507ebddc1e9c8776c3c8e65af9444d037c4b7db118ede67fd",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "9870dcf79fa9da8ff65867613c8c87ad7c1f0d31d941e6967149cc3d765b08df",
    "source_lines": "L9675-L11350",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-17-002"
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
  "stable_id": "EP-17-002",
  "title": "Monitoring phải bao phủ toàn Platform",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-17-003 — Scheduler, Queue, Worker, Alert và Runbook đều là Business Object

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-004"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-17-003",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "020e64b9fa842a249d4fd7b90c78cf97ade8be49f8eecf9899417584da42710b"
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
        "EP-17-003-AC001",
        "EP-17-003-AC002",
        "EP-17-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-003-O001",
      "obligation_text": "Scheduler, Queue, Worker, Alert và Runbook đều là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Scheduler, Queue, Worker, Alert và Runbook đều là Business Object.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-004"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-17-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-17-003",
    "source_context_sha256": "01c18a016ddd50a1a330ee5eaa51f2c3dc58f401da9da07e8877b7baf1414919",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "020e64b9fa842a249d4fd7b90c78cf97ade8be49f8eecf9899417584da42710b",
    "source_lines": "L11352-L11431",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-17-003"
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
  "stable_id": "EP-17-003",
  "title": "Scheduler, Queue, Worker, Alert và Runbook đều là Business Object",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-17-004 — Operation Policy được cấu hình. Không Hard-code

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
      "requirement_id": "EP-17-004",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "79a0a441ad070432dfd6679096a2e90aed5b912fbee60f3abd8d7fb418a7d444"
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
        "EP-17-004-AC001",
        "EP-17-004-AC003",
        "EP-17-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-004-O001",
      "obligation_text": "Operation Policy được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "EP-17-004-AC002",
        "EP-17-004-AC003",
        "EP-17-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-004-O002",
      "obligation_text": "Không Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Operation Policy được cấu hình. Không Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-17-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-17-004",
    "source_context_sha256": "4f33c9551ddfcc74d47aa024ed35d03e368761bd5d0a29ee368db82f59701245",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "79a0a441ad070432dfd6679096a2e90aed5b912fbee60f3abd8d7fb418a7d444",
    "source_lines": "L11433-L11518",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-17-004"
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
  "stable_id": "EP-17-004",
  "title": "Operation Policy được cấu hình. Không Hard-code",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-17-005 — Operation Retry độc lập Connector Retry

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
  "normative_statement": "Operation Retry độc lập Connector Retry.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-17-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-011",
    "source_context_sha256": "2aebb9cc529851f28c32018d00f73946f21a29a8a0cf36843bbafce05b2b2f8a",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "2182c0fb868876035b46a98a806d187921bb0de85494a038eca637e05bb86701",
    "source_lines": "L11520-L11571",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-17-005"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "BD-17-011",
    "aliases": [],
    "coverage_mode": "CANONICAL",
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-17-005",
  "title": "Operation Retry độc lập Connector Retry",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-17-006 — Platform hỗ trợ Replay và Recoverable Operation

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
      "requirement_id": "EP-17-006",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "3d07d835beb40c78d0d9c55ed6a7f1af6c1c1b8a4982bed021f375cde50fc4ae"
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
        "EP-17-006-AC001",
        "EP-17-006-AC002",
        "EP-17-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-006-O001",
      "obligation_text": "Platform hỗ trợ Replay và Recoverable Operation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Replay và Recoverable Operation.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-17-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-17-006",
    "source_context_sha256": "e93cf78b940b2adb594c58ae14d5f885f98e854c8114343571ef7505d32b5034",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "3d07d835beb40c78d0d9c55ed6a7f1af6c1c1b8a4982bed021f375cde50fc4ae",
    "source_lines": "L11573-L11648",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-17-006"
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
  "stable_id": "EP-17-006",
  "title": "Platform hỗ trợ Replay và Recoverable Operation",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-17-007 — Platform hỗ trợ Feature Flag và Kill Switch. Không cần Deploy để bật hoặc tắt chức năng

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
      "requirement_id": "EP-17-007",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "1b975c77a3b95b713430925ca8e8881870b17bfd185ecdca68b51066e03523cb"
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
        "EP-17-007-AC001",
        "EP-17-007-AC003",
        "EP-17-007-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-007-O001",
      "obligation_text": "Platform hỗ trợ Feature Flag và Kill Switch"
    },
    {
      "acceptance_criterion_references": [
        "EP-17-007-AC002",
        "EP-17-007-AC003",
        "EP-17-007-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-007-O002",
      "obligation_text": "Không cần Deploy để bật hoặc tắt chức năng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Feature Flag và Kill Switch. Không cần Deploy để bật hoặc tắt chức năng.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-17-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-028",
    "source_context_sha256": "0f20242bcc1e11401db1c54c141059ce5ca4305fc42048118296482ad058af16",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "1b975c77a3b95b713430925ca8e8881870b17bfd185ecdca68b51066e03523cb",
    "source_lines": "L11650-L11735",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-17-007"
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
  "stable_id": "EP-17-007",
  "title": "Platform hỗ trợ Feature Flag và Kill Switch. Không cần Deploy để bật hoặc tắt chức năng",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-17-008 — Mọi thao tác Operations đều phải: - Kiểm tra Permission - Ghi Audit - Tuân thủ Runbook (nếu có)

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-004"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-17-008",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "source_fingerprint": "62eedfdc6201f555db88426ffa39dae934e3f515213c3826477e9f37e909fd13"
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
        "EP-17-008-AC001",
        "EP-17-008-AC004",
        "EP-17-008-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-008-O001",
      "obligation_text": "Mọi thao tác Operations đều phải: Kiểm tra Permission"
    },
    {
      "acceptance_criterion_references": [
        "EP-17-008-AC002",
        "EP-17-008-AC004",
        "EP-17-008-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-008-O002",
      "obligation_text": "Mọi thao tác Operations đều phải: Ghi Audit"
    },
    {
      "acceptance_criterion_references": [
        "EP-17-008-AC003",
        "EP-17-008-AC004",
        "EP-17-008-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-008-O003",
      "obligation_text": "Mọi thao tác Operations đều phải: Tuân thủ Runbook (nếu có)"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-17-008-AC005"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-17-008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-17-008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-17-008-AC004"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-17-008-AC001",
        "EP-17-008-AC002",
        "EP-17-008-AC003"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-17-008 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thao tác Operations đều phải: - Kiểm tra Permission - Ghi Audit - Tuân thủ Runbook (nếu có)",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-004"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-17-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-17-008",
    "source_context_sha256": "2951251016fb55d5b0c8e04e306c118e26d4e099102b021292494fbe29321b0e",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "62eedfdc6201f555db88426ffa39dae934e3f515213c3826477e9f37e909fd13",
    "source_lines": "L11737-L11873",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-17-008"
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
  "stable_id": "EP-17-008",
  "title": "Mọi thao tác Operations đều phải: - Kiểm tra Permission - Ghi Audit - Tuân thủ Runbook (nếu có)",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-17-009 — Operations Platform Publish Business Event

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
  "normative_statement": "Operations Platform Publish Business Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-17-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "29. Operation Business Events",
    "source_context_sha256": "ab56286c8a4ab9a35eda380fb856a41d2c3038d4f5c35c93c36835f9e4844bc8",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "2d6ab7828fff5926a1ff83d7a6f945bb080760411b88cf84663dd41e02544bbc",
    "source_lines": "L11875-L11923",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-17-009"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "BD-17-026",
    "aliases": [],
    "coverage_mode": "CANONICAL",
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-17-009",
  "title": "Operations Platform Publish Business Event",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-17-010 — Mọi tác vụ vận hành của Platform phải bảo đảm: - Observable - Auditable - Configurable - Recover…

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
  "normative_statement": "Mọi tác vụ vận hành của Platform phải bảo đảm: - Observable - Auditable - Configurable - Recoverable - Automatable Operator không thao tác trực tiếp trên hạ tầng nếu Platform đã hỗ trợ chức năng tương ứng.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-17-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-17-010",
    "source_context_sha256": "8bbd86f847b6f174ba6c408149c3fa2dc3d29b7aaf4d7bc53b16778d0a1742ea",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "9c6bda5c6145ed4ec157297dec2a535d303603ca28b80fb067735e891b4857f7",
    "source_lines": "L11925-L11973",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-17-010"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "BRD-WS-17-R013",
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-17-010",
  "title": "Mọi tác vụ vận hành của Platform phải bảo đảm: - Observable - Auditable - Configurable - Recover…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
