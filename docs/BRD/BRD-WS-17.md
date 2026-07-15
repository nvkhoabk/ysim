---
document_code: "BRD-WS-17"
title: "Platform Operations, Monitoring, Scheduler & Background Processing"
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

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-001 — Platform có một Platform Operations Center thống nhất. Operations Center là trung tâm điều hành …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-001-AC001",
      "given": "an operational task within the scope of Platform có một Platform Operations Center thống nhất. Operations Center là trung tâm điều hành …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-001-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-001-AC002",
      "given": "an operational task within the scope of Platform có một Platform Operations Center thống nhất. Operations Center là trung tâm điều hành …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-001-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-001-AC003",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Platform có một Platform Operations Center thống nhất. Operations Center là trung tâm điều hành …",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-001-O001",
        "BD-17-001-O002"
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
        "BD-17-001-AC001",
        "BD-17-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-001-O001",
      "obligation_text": "Platform có một Platform Operations Center thống nhất"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-001-AC002",
        "BD-17-001-AC003"
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
    "source_fingerprint": "7471a04fa66239d0bba59aa3f84120358482520b7a7dbd29ad2c4448a7c78473",
    "source_lines": "L967-L972",
    "source_section": "37. Business Decisions (Locked) > BD-17-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-002-AC001",
      "given": "an operational task within the scope of Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-002-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-002-AC002",
      "given": "an operational task within the scope of Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-002-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-002-AC003",
      "given": "an operational task within the scope of Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-002-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-002-AC004",
      "given": "an operational task within the scope of Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-002-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-002-AC005",
      "given": "an operational task within the scope of Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-002-O005"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-002-AC006",
      "given": "an operational task within the scope of Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-002-O006"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-002-AC007",
      "given": "an operational task within the scope of Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-002-O007"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-002-AC008",
      "given": "an operational task within the scope of Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-002-O008"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-002-AC009",
      "given": "an operational task within the scope of Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-002-O009"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-002-AC010",
      "given": "an operational task within the scope of Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-002-O010"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-002-AC011",
      "given": "an operational task within the scope of Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-002-O011"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-002-AC012",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Monitoring bao phủ toàn Platform. Bao gồm: - Business - API - Queue - Worker - Scheduler - Conne…",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-002-O001",
        "BD-17-002-O002",
        "BD-17-002-O003",
        "BD-17-002-O004",
        "BD-17-002-O005",
        "BD-17-002-O006",
        "BD-17-002-O007",
        "BD-17-002-O008",
        "BD-17-002-O009",
        "BD-17-002-O010",
        "BD-17-002-O011"
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
        "BD-17-002-AC001",
        "BD-17-002-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O001",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Business."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC002",
        "BD-17-002-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O002",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: API."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC003",
        "BD-17-002-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O003",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Queue."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC004",
        "BD-17-002-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O004",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Worker."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC005",
        "BD-17-002-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O005",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Scheduler."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC006",
        "BD-17-002-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O006",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Connector."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC007",
        "BD-17-002-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O007",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Payment."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC008",
        "BD-17-002-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O008",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Notification."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC009",
        "BD-17-002-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O009",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Database."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC010",
        "BD-17-002-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O010",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Cache."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-002-AC011",
        "BD-17-002-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-002-O011",
      "obligation_text": "Monitoring bao phủ toàn Platform. Bao gồm: Infrastructure."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-17-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-17-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-17-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-17-002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
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
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-17-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "982d9c3416dda4d7295348e3cb4c4484ef8fa0a11b44f43e39cec3a0163aea6d",
    "source_lines": "L975-L992",
    "source_section": "37. Business Decisions (Locked) > BD-17-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-003-AC001",
      "given": "the applicable business context, actor, and input for Health Check hỗ trợ đầy đủ các thành phần của Platform. Health Status được chuẩn hóa",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-17-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-003-AC002",
      "given": "the applicable business context, actor, and input for Health Check hỗ trợ đầy đủ các thành phần của Platform. Health Status được chuẩn hóa",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the resulting business state equals the declared destination for a valid transition and records the prior state, triggering input, and transition reason",
      "verifies": [
        "BD-17-003-O002"
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
        "BD-17-003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-003-O001",
      "obligation_text": "Health Check hỗ trợ đầy đủ các thành phần của Platform"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-003-AC002"
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
    "source_fingerprint": "52ae28cabe782c14be55149392b59b09a04d9b8264ecd77ec6689d0e8789ee55",
    "source_lines": "L995-L1000",
    "source_section": "37. Business Decisions (Locked) > BD-17-003"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-004-AC001",
      "given": "an operational task within the scope of Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: - Dashboard - Alert - Capacity Planning - …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-004-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-004-AC002",
      "given": "an operational task within the scope of Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: - Dashboard - Alert - Capacity Planning - …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-004-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-004-AC003",
      "given": "an operational task within the scope of Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: - Dashboard - Alert - Capacity Planning - …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-004-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-004-AC004",
      "given": "an operational task within the scope of Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: - Dashboard - Alert - Capacity Planning - …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-004-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-004-AC005",
      "given": "an operational task within the scope of Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: - Dashboard - Alert - Capacity Planning - …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-004-O005"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-004-AC006",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: - Dashboard - Alert - Capacity Planning - …",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-004-O001",
        "BD-17-004-O002",
        "BD-17-004-O003",
        "BD-17-004-O004",
        "BD-17-004-O005"
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
        "BD-17-004-AC001",
        "BD-17-004-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-004-O001",
      "obligation_text": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: Dashboard."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-004-AC002",
        "BD-17-004-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-004-O002",
      "obligation_text": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: Alert."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-004-AC003",
        "BD-17-004-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-004-O003",
      "obligation_text": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: Capacity Planning."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-004-AC004",
        "BD-17-004-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-004-O004",
      "obligation_text": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: SLO."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-004-AC005",
        "BD-17-004-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-004-O005",
      "obligation_text": "Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: SLA."
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
    "source_fingerprint": "30eb38829b83a50e215a3858b5fee45312b024032dee17e01a31762da2dc9ed4",
    "source_lines": "L1003-L1014",
    "source_section": "37. Business Decisions (Locked) > BD-17-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-005-AC001",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule được cấu hình. Không Hard-code",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-005-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-005-AC002",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule được cấu hình. Không Hard-code",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-005-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-005-AC003",
      "given": "an operational task within the scope of Alert Rule là Business Object. Alert Rule được cấu hình. Không Hard-code",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-005-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-005-AC004",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Alert Rule là Business Object. Alert Rule được cấu hình. Không Hard-code",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-005-O001",
        "BD-17-005-O002",
        "BD-17-005-O003"
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
        "BD-17-005-AC001",
        "BD-17-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-005-O001",
      "obligation_text": "Alert Rule là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-005-AC002",
        "BD-17-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-005-O002",
      "obligation_text": "Alert Rule được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-005-AC003",
        "BD-17-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-005-O003",
      "obligation_text": "Không Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Alert Rule là Business Object. Alert Rule được cấu hình. Không Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Alert Rule",
    "source_context_sha256": "20268973697bfc64bdd4536c7deca7ea62de0777e79a4ef2903bd3f315dcad18",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "d7d2758777eb46a2c6e43cfba30bdcfe3d106c345ac8a6d1fa325b2610e98c87",
    "source_lines": "L1017-L1024",
    "source_section": "37. Business Decisions (Locked) > BD-17-005"
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
  "stable_id": "BD-17-005",
  "title": "Alert Rule là Business Object. Alert Rule được cấu hình. Không Hard-code",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-006 — Alert được gửi theo Notification Preference. Personal Inbox luôn là kênh nhận mặc định

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-006-AC001",
      "given": "an operational task within the scope of Alert được gửi theo Notification Preference. Personal Inbox luôn là kênh nhận mặc định",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-006-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-006-AC002",
      "given": "an operational task within the scope of Alert được gửi theo Notification Preference. Personal Inbox luôn là kênh nhận mặc định",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-006-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-006-AC003",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Alert được gửi theo Notification Preference. Personal Inbox luôn là kênh nhận mặc định",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-006-O001",
        "BD-17-006-O002"
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
        "BD-17-006-AC001",
        "BD-17-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-006-O001",
      "obligation_text": "Alert được gửi theo Notification Preference"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-006-AC002",
        "BD-17-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-006-O002",
      "obligation_text": "Personal Inbox luôn là kênh nhận mặc định"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Alert được gửi theo Notification Preference. Personal Inbox luôn là kênh nhận mặc định.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-17-006",
    "source_context_sha256": "da00372cb2b839eb3d3445a3cb7fb61416558a5cc85f95e72c2bf933f422f32b",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "667c30202eebbbf2c1922910c1f6b9da85f46983123ed38501eb73dec81196c7",
    "source_lines": "L1027-L1032",
    "source_section": "37. Business Decisions (Locked) > BD-17-006"
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
  "stable_id": "BD-17-006",
  "title": "Alert được gửi theo Notification Preference. Personal Inbox luôn là kênh nhận mặc định",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-007 — Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Busin…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-007-AC001",
      "given": "a candidate Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Busin… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-007-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-007-AC002",
      "given": "a candidate Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Busin… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-007-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-007-AC003",
      "given": "a candidate Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Busin… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-007-O003"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-007-AC004",
      "given": "a candidate Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Busin… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-007-O004"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-17-007-AC005",
      "given": "a Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Busin… candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-17-007-O001",
        "BD-17-007-O002",
        "BD-17-007-O003",
        "BD-17-007-O004"
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
        "BD-17-007-AC001",
        "BD-17-007-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-007-O001",
      "obligation_text": "Scheduler là Business Object. Scheduler hỗ trợ: Cron."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-007-AC002",
        "BD-17-007-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-007-O002",
      "obligation_text": "Scheduler là Business Object. Scheduler hỗ trợ: Fixed Interval."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-007-AC003",
        "BD-17-007-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-007-O003",
      "obligation_text": "Scheduler là Business Object. Scheduler hỗ trợ: Manual Trigger."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-007-AC004",
        "BD-17-007-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-007-O004",
      "obligation_text": "Scheduler là Business Object. Scheduler hỗ trợ: Business Event Trigger."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Business Event Trigger",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-17-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Scheduler",
    "source_context_sha256": "867847cfa5f35a218d9ca4c09054fad6f3806ef2db0bd26361426efbaad00983",
    "source_document": "docs/BRD/BRD-WS-17.md",
    "source_fingerprint": "11ffc66ac3a680ed0c555ce7ca04285c49e6868880290ea13a6f46af400d5cd3",
    "source_lines": "L1035-L1045",
    "source_section": "37. Business Decisions (Locked) > BD-17-007"
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
  "stable_id": "BD-17-007",
  "title": "Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Busin…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-17-008 — Job Execution là Business Object. Mọi Job đều sinh Job Execution

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-008-AC001",
      "given": "a candidate Job Execution là Business Object. Mọi Job đều sinh Job Execution record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-008-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-008-AC002",
      "given": "a candidate Job Execution là Business Object. Mọi Job đều sinh Job Execution record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-008-O002"
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
        "BD-17-008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-008-O001",
      "obligation_text": "Job Execution là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-008-AC002"
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
    "source_fingerprint": "2ce810bed5e4f372b7a36e9397495157502e1e889224f18c743d4fb8a586903a",
    "source_lines": "L1048-L1053",
    "source_section": "37. Business Decisions (Locked) > BD-17-008"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-009-AC001",
      "given": "a candidate Worker là Business Object. Một Job có thể được xử lý bởi nhiều Worker record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-009-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-009-AC002",
      "given": "a candidate Worker là Business Object. Một Job có thể được xử lý bởi nhiều Worker record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-009-O002"
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
        "BD-17-009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-009-O001",
      "obligation_text": "Worker là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-009-AC002"
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
    "source_fingerprint": "fddfc5b010a454632100a735029dfd1ba87d74cb7ec2469e25d7e2136ede544d",
    "source_lines": "L1056-L1061",
    "source_section": "37. Business Decisions (Locked) > BD-17-009"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-010-AC001",
      "given": "an operational task within the scope of Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: - Pending - Processing - Completed - Retry - …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-010-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-010-AC002",
      "given": "an operational task within the scope of Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: - Pending - Processing - Completed - Retry - …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-010-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-010-AC003",
      "given": "an operational task within the scope of Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: - Pending - Processing - Completed - Retry - …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-010-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-010-AC004",
      "given": "an operational task within the scope of Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: - Pending - Processing - Completed - Retry - …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-010-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-010-AC005",
      "given": "an operational task within the scope of Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: - Pending - Processing - Completed - Retry - …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-010-O005"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-010-AC006",
      "given": "an operational task within the scope of Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: - Pending - Processing - Completed - Retry - …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-010-O006"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-010-AC007",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: - Pending - Processing - Completed - Retry - …",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-010-O001",
        "BD-17-010-O002",
        "BD-17-010-O003",
        "BD-17-010-O004",
        "BD-17-010-O005",
        "BD-17-010-O006"
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
        "BD-17-010-AC001",
        "BD-17-010-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O001",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: Pending."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-010-AC002",
        "BD-17-010-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O002",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: Processing."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-010-AC003",
        "BD-17-010-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O003",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: Completed."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-010-AC004",
        "BD-17-010-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O004",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: Retry."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-010-AC005",
        "BD-17-010-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O005",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: Failed."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-010-AC006",
        "BD-17-010-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-010-O006",
      "obligation_text": "Queue Monitoring hỗ trợ nhiều trạng thái. Bao gồm: DLQ."
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
    "source_fingerprint": "2fdd75e0efeb59f7d76525e431b8b00a60765df506259f03c4bd077158de858a",
    "source_lines": "L1064-L1076",
    "source_section": "37. Business Decisions (Locked) > BD-17-010"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-011-AC001",
      "given": "an operational task within the scope of Operation Retry độc lập Connector Retry",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-011-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-011-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Operation Retry độc lập Connector Retry",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-011-O001"
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
        "BD-17-011-AC001",
        "BD-17-011-AC002"
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
    "source_fingerprint": "c63e0bbffcb52c28a1fbaf53e6fb917c1ca1ce77d8491cd62b81587fbb7f4c88",
    "source_lines": "L1079-L1082",
    "source_section": "37. Business Decisions (Locked) > BD-17-011"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-012-AC001",
      "given": "a candidate Maintenance Window là Business Object. Maintenance hỗ trợ nhiều cấp record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-012-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-012-AC002",
      "given": "a candidate Maintenance Window là Business Object. Maintenance hỗ trợ nhiều cấp record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-012-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-17-012-AC003",
      "given": "a Maintenance Window là Business Object. Maintenance hỗ trợ nhiều cấp candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-17-012-O001",
        "BD-17-012-O002"
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
        "BD-17-012-AC001",
        "BD-17-012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-012-O001",
      "obligation_text": "Maintenance Window là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-012-AC002",
        "BD-17-012-AC003"
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
    "source_fingerprint": "b79f3b809789831b77ab5d5356dbf276029ec82bbaf5082f716cc623e96948af",
    "source_lines": "L1085-L1090",
    "source_section": "37. Business Decisions (Locked) > BD-17-012"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-013-AC001",
      "given": "an operational task within the scope of Backup Policy là Business Object",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-013-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-013-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Backup Policy là Business Object",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-013-O001"
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
        "BD-17-013-AC001",
        "BD-17-013-AC002"
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
    "source_fingerprint": "68821decdd0a8e08f95f4a1c5f6b01006368d7a83a5aa2a1eb0efcd6ceda6793",
    "source_lines": "L1093-L1096",
    "source_section": "37. Business Decisions (Locked) > BD-17-013"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-014-AC001",
      "given": "an operational task within the scope of Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: - Manual - Semi Automatic - Automatic",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-014-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-014-AC002",
      "given": "an operational task within the scope of Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: - Manual - Semi Automatic - Automatic",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-014-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-014-AC003",
      "given": "an operational task within the scope of Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: - Manual - Semi Automatic - Automatic",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-014-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-014-AC004",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: - Manual - Semi Automatic - Automatic",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-014-O001",
        "BD-17-014-O002",
        "BD-17-014-O003"
      ],
      "when": "operational verification is performed"
    },
    {
      "case": "RECOVERY",
      "controlled_contract": "EXPLICIT_RECOVERY_CONTRACT_V1",
      "criterion_id": "BD-17-014-AC005",
      "given": "a failed or interrupted case for which Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: - Manual - Semi Automatic - Automatic explicitly defines recovery, restore, rollback, or fallback behavior",
      "observable_evidence": "pre-failure state, recovery action, resulting state, outcome, and recovery evidence named by the obligation",
      "then": "the resulting state and outcome follow the requirement-specific recovery obligation and expose whether recovery completed or failed",
      "verifies": [
        "BD-17-014-O001",
        "BD-17-014-O002",
        "BD-17-014-O003"
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
        "BD-17-014-AC001",
        "BD-17-014-AC004",
        "BD-17-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-014-O001",
      "obligation_text": "Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: Manual."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-014-AC002",
        "BD-17-014-AC004",
        "BD-17-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-014-O002",
      "obligation_text": "Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: Semi Automatic."
    },
    {
      "acceptance_criterion_references": [
        "BD-17-014-AC003",
        "BD-17-014-AC004",
        "BD-17-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-014-O003",
      "obligation_text": "Platform hỗ trợ Disaster Recovery. Kiến trúc hỗ trợ: Automatic."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-17-014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-17-014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-17-014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-17-014 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-17-014-AC001",
        "BD-17-014-AC002",
        "BD-17-014-AC003"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [
        "BD-17-014-AC005"
      ],
      "status": "APPLICABLE"
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
    "source_fingerprint": "1823643f650dffd3c92a8362c8f7b4516ad95534f249d7b87ff419e50d7ce1c2",
    "source_lines": "L1099-L1108",
    "source_section": "37. Business Decisions (Locked) > BD-17-014"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-015-AC001",
      "given": "a candidate Capacity Policy là Business Object. Kiến trúc hỗ trợ Auto Scaling trong tương lai record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-015-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-015-AC002",
      "given": "a candidate Capacity Policy là Business Object. Kiến trúc hỗ trợ Auto Scaling trong tương lai record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-015-O002"
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
        "BD-17-015-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-015-O001",
      "obligation_text": "Capacity Policy là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-015-AC002"
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
    "source_fingerprint": "a9ab188559afbfa6b89deaae23d4c7237a8c02f344d4b3e73ccdc028d5d666f0",
    "source_lines": "L1111-L1116",
    "source_section": "37. Business Decisions (Locked) > BD-17-015"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-016-AC001",
      "given": "an operational task within the scope of Platform có Operational Dashboard dành riêng cho Operator",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-016-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-016-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Platform có Operational Dashboard dành riêng cho Operator",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-016-O001"
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
        "BD-17-016-AC001",
        "BD-17-016-AC002"
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
    "source_fingerprint": "17e38bcd71e76d2fe1ef49a7f95fcf01e1dd856afed132ee752c4889990a0012",
    "source_lines": "L1119-L1122",
    "source_section": "37. Business Decisions (Locked) > BD-17-016"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-17-017-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Operator sử dụng Permission riêng. Mọi thao tác đều được Security Platform kiểm soát",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-17-017-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-17-017-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Operator sử dụng Permission riêng. Mọi thao tác đều được Security Platform kiểm soát",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-17-017-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-17-017-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Operator sử dụng Permission riêng. Mọi thao tác đều được Security Platform kiểm soát",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-17-017-O001",
        "BD-17-017-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-17-017-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Operator sử dụng Permission riêng. Mọi thao tác đều được Security Platform kiểm soát",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-17-017-O001",
        "BD-17-017-O002"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-17-017-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Operator sử dụng Permission riêng. Mọi thao tác đều được Security Platform kiểm soát",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-17-017-O001",
        "BD-17-017-O002"
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
        "BD-17-017-AC001",
        "BD-17-017-AC003",
        "BD-17-017-AC004",
        "BD-17-017-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-017-O001",
      "obligation_text": "Operator sử dụng Permission riêng"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-017-AC002",
        "BD-17-017-AC003",
        "BD-17-017-AC004",
        "BD-17-017-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-017-O002",
      "obligation_text": "Mọi thao tác đều được Security Platform kiểm soát"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-17-017-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-17-017 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-17-017 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-17-017-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-17-017-AC001",
        "BD-17-017-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-17-017 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "1c9bbaf545761d347eb3730c3f3564c4f2dadf1aa4df524c32a6676b9e42fbe3",
    "source_lines": "L1125-L1130",
    "source_section": "37. Business Decisions (Locked) > BD-17-017"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-018-AC001",
      "given": "the applicable business context, actor, and input for Maintenance phải gửi Notification trước khi thực hiện",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-17-018-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-17-018-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Maintenance phải gửi Notification trước khi thực hiện",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-17-018-O001"
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
        "BD-17-018-AC001",
        "BD-17-018-AC002"
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
    "source_fingerprint": "18361f3e827b4345a10b6ba1d44498fd42c171f818ee8a0a614ad60beceedcf0",
    "source_lines": "L1133-L1136",
    "source_section": "37. Business Decisions (Locked) > BD-17-018"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-019-AC001",
      "given": "the applicable business context, actor, and input for Scheduler hỗ trợ Priority. Business Critical Job luôn được ưu tiên",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-17-019-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-019-AC002",
      "given": "the applicable business context, actor, and input for Scheduler hỗ trợ Priority. Business Critical Job luôn được ưu tiên",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-17-019-O002"
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
        "BD-17-019-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-019-O001",
      "obligation_text": "Scheduler hỗ trợ Priority"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-019-AC002"
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
    "source_fingerprint": "6d378a72b0286b79212b1925c27595fa145c5a822132275dd59a0218d48ac617",
    "source_lines": "L1139-L1144",
    "source_section": "37. Business Decisions (Locked) > BD-17-019"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SCOPE_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-17-020-AC001",
      "given": "the v2.3 capability inventory and conformance evidence for Kiến trúc hỗ trợ Auto Scaling. Version hiện tại chưa triển khai",
      "observable_evidence": "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
      "then": "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
      "verifies": [
        "BD-17-020-O001"
      ],
      "when": "the capability is inspected at the active baseline boundary"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SCOPE_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-17-020-AC002",
      "given": "the v2.3 capability inventory and conformance evidence for Kiến trúc hỗ trợ Auto Scaling. Version hiện tại chưa triển khai",
      "observable_evidence": "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
      "then": "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
      "verifies": [
        "BD-17-020-O002"
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
        "BD-17-020-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-020-O001",
      "obligation_text": "Kiến trúc hỗ trợ Auto Scaling"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-020-AC002"
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
    "source_fingerprint": "3ea335bf379ee684322e2da3b69c917694a7bdf95b1375aa3ba9decb3de6a911",
    "source_lines": "L1147-L1152",
    "source_section": "37. Business Decisions (Locked) > BD-17-020"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-021-AC001",
      "given": "an operational task within the scope of Operational Audit ghi nhận toàn bộ thao tác vận hành",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-021-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-021-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Operational Audit ghi nhận toàn bộ thao tác vận hành",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-021-O001"
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
        "BD-17-021-AC001",
        "BD-17-021-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-021-O001",
      "obligation_text": "Operational Audit ghi nhận toàn bộ thao tác vận hành"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-17-021 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-17-021 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-17-021 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-17-021 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-17-021-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-17-021 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "cc0f6602d8a490995fc827ad99617aa74edc17df97ffeefc2588450e09b24f6a",
    "source_lines": "L1155-L1158",
    "source_section": "37. Business Decisions (Locked) > BD-17-021"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-022-AC001",
      "given": "an operational task within the scope of Operation Policy là Business Object. Operation Policy được Versioning",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-022-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-022-AC002",
      "given": "an operational task within the scope of Operation Policy là Business Object. Operation Policy được Versioning",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-022-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-022-AC003",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Operation Policy là Business Object. Operation Policy được Versioning",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-022-O001",
        "BD-17-022-O002"
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
        "BD-17-022-AC001",
        "BD-17-022-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-022-O001",
      "obligation_text": "Operation Policy là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-022-AC002",
        "BD-17-022-AC003"
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
    "source_fingerprint": "e19ec9da6d152e046328c0d0826326eddb1f42be97b2676298cd18f4767ca41c",
    "source_lines": "L1161-L1166",
    "source_section": "37. Business Decisions (Locked) > BD-17-022"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-023-AC001",
      "given": "the applicable business context, actor, and input for Scheduler hỗ trợ Business Event Trigger",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-17-023-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-17-023-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Scheduler hỗ trợ Business Event Trigger",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-17-023-O001"
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
        "BD-17-023-AC001",
        "BD-17-023-AC002"
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
    "source_fingerprint": "0cee25d0714e6bf9b8e340627650bb42fb7f72264b73cbfabd714d7604373c0a",
    "source_lines": "L1169-L1172",
    "source_section": "37. Business Decisions (Locked) > BD-17-023"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-024-AC001",
      "given": "an operational task within the scope of Organization không có Operations Capability. Operations chỉ thuộc Platform",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-024-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-024-AC002",
      "given": "an operational task within the scope of Organization không có Operations Capability. Operations chỉ thuộc Platform",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-024-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-024-AC003",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Organization không có Operations Capability. Operations chỉ thuộc Platform",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-024-O001",
        "BD-17-024-O002"
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
        "BD-17-024-AC001",
        "BD-17-024-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-024-O001",
      "obligation_text": "Organization không có Operations Capability"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-024-AC002",
        "BD-17-024-AC003"
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
    "source_fingerprint": "545c27e8a48744d1afcbe33837e0840d51a7267cda3a5b2f382ab563e3f0dc39",
    "source_lines": "L1175-L1180",
    "source_section": "37. Business Decisions (Locked) > BD-17-024"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-025-AC001",
      "given": "the applicable business context, actor, and input for Maintenance hỗ trợ nhiều Scope",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-17-025-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-17-025-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Maintenance hỗ trợ nhiều Scope",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-17-025-O001"
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
        "BD-17-025-AC001",
        "BD-17-025-AC002"
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
    "source_fingerprint": "e5c7c0795da6409edb0d23c91e5c70e85d8fdef340ee5db3ac5e6e3bf237b561",
    "source_lines": "L1183-L1186",
    "source_section": "37. Business Decisions (Locked) > BD-17-025"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-026-AC001",
      "given": "an operational task within the scope of Operations Platform Publish Business Event",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-026-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-026-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Operations Platform Publish Business Event",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-026-O001"
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
        "BD-17-026-AC001",
        "BD-17-026-AC002"
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
    "source_fingerprint": "b840e626d6693864672ac166cb63f493aba25b734f3fddc9c8232bc96a0a8ebb",
    "source_lines": "L1189-L1192",
    "source_section": "37. Business Decisions (Locked) > BD-17-026"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-17-027-AC001",
      "given": "a candidate Runbook là Business Object record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-17-027-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-17-027-AC002",
      "given": "a Runbook là Business Object candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-17-027-O001"
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
        "BD-17-027-AC001",
        "BD-17-027-AC002"
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
    "source_fingerprint": "26bc1a2acf8d5762786c180eea2c57586ce2463e45f3d4becfb55c60be7ba473",
    "source_lines": "L1195-L1198",
    "source_section": "37. Business Decisions (Locked) > BD-17-027"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-028-AC001",
      "given": "the applicable business context, actor, and input for Platform hỗ trợ Feature Flag và Kill Switch",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-17-028-O001"
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
        "BD-17-028-AC001"
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
    "source_fingerprint": "96195d890597e852763886782925f6189742340c3517c3e003913c870d72c1c4",
    "source_lines": "L1201-L1204",
    "source_section": "37. Business Decisions (Locked) > BD-17-028"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-029-AC001",
      "given": "an operational task within the scope of Platform hỗ trợ Operational Command Center",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-029-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-029-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Platform hỗ trợ Operational Command Center",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-029-O001"
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
        "BD-17-029-AC001",
        "BD-17-029-AC002"
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
    "source_fingerprint": "68cee7db78de1fb72a50164752a4954080bb8ff9115e82db925e230cd1dcad15",
    "source_lines": "L1207-L1210",
    "source_section": "37. Business Decisions (Locked) > BD-17-029"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-030-AC001",
      "given": "an operational task within the scope of Platform hỗ trợ Replay",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-030-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-030-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Platform hỗ trợ Replay",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-030-O001"
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
        "BD-17-030-AC001",
        "BD-17-030-AC002"
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
    "source_fingerprint": "cbdc7e348e5efee0c404b3f6f37acac6e5c016c06b59166ded293e3927fb8171",
    "source_lines": "L1213-L1216",
    "source_section": "37. Business Decisions (Locked) > BD-17-030"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SCOPE_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-17-031-AC001",
      "given": "the v2.3 capability inventory and conformance evidence for Kiến trúc hỗ trợ Chaos Readiness. Version hiện tại chưa triển khai",
      "observable_evidence": "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
      "then": "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
      "verifies": [
        "BD-17-031-O001"
      ],
      "when": "the capability is inspected at the active baseline boundary"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SCOPE_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-17-031-AC002",
      "given": "the v2.3 capability inventory and conformance evidence for Kiến trúc hỗ trợ Chaos Readiness. Version hiện tại chưa triển khai",
      "observable_evidence": "baseline capability inventory, exposed action or API surface, conformance trace, implementation-status evidence, and future-scope marker",
      "then": "implemented behavior and exposed actions match the statement's active versus future boundary; future-only behavior is not presented as available in v2.3",
      "verifies": [
        "BD-17-031-O002"
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
        "BD-17-031-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-17-031-O001",
      "obligation_text": "Kiến trúc hỗ trợ Chaos Readiness"
    },
    {
      "acceptance_criterion_references": [
        "BD-17-031-AC002"
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
    "source_fingerprint": "18ecc2ef97afc4605e672bfb712bca8e20e6dac0e74a0625c4aaaefea42feaf8",
    "source_lines": "L1219-L1224",
    "source_section": "37. Business Decisions (Locked) > BD-17-031"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-17-032-AC001",
      "given": "an operational task within the scope of Platform hỗ trợ SLO và SLA Monitoring",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-17-032-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-17-032-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Platform hỗ trợ SLO và SLA Monitoring",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-17-032-O001"
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
        "BD-17-032-AC001",
        "BD-17-032-AC002"
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
    "source_fingerprint": "5661f1a7f2176424645465c184f00f4137cb210b70ad56ba73023445fb553eee",
    "source_lines": "L1227-L1230",
    "source_section": "37. Business Decisions (Locked) > BD-17-032"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R001-AC001",
      "given": "the applicable business context, actor, and input for Personal Inbox là kênh bắt buộc",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-17-R001-O001"
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
        "BRD-WS-17-R001-AC001"
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
    "source_lines": "L234",
    "source_section": "8. Alert Channel"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R002-AC001",
      "given": "the applicable business context, actor, and input for Scheduler Trigger được cấu hình và có thể thay đổi mà không cần sửa mã nguồn",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-17-R002-O001"
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
        "BRD-WS-17-R002-AC001"
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
    "source_lines": "L288",
    "source_section": "10. Scheduler Trigger"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R003-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-17-R003-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R003-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-17-R003-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R003-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-17-R003-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "IDEMPOTENCY",
      "controlled_contract": "EXPLICIT_IDEMPOTENCY_CONTRACT_V1",
      "criterion_id": "BRD-WS-17-R003-AC004",
      "given": "a repeated request, retry, replay, or duplicate explicitly governed by Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp",
      "observable_evidence": "original and repeated action identities, both outcomes, side-effect count, and resulting business state",
      "then": "the repeated action produces the requirement-specific stable result without an additional prohibited side effect",
      "verifies": [
        "BRD-WS-17-R003-O001"
      ],
      "when": "the same governed action is presented again under the declared identity or deduplication boundary"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-17-R003-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-17-R003-O001"
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
        "BRD-WS-17-R003-AC001",
        "BRD-WS-17-R003-AC002",
        "BRD-WS-17-R003-AC003",
        "BRD-WS-17-R003-AC004",
        "BRD-WS-17-R003-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R003-O001",
      "obligation_text": "Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-17-R003-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [
        "BRD-WS-17-R003-AC004"
      ],
      "status": "APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-17-R003-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L386",
    "source_section": "14. Operation Retry"
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
    "source_lines": "L494",
    "source_section": "18. Capacity Policy"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R006-AC001",
      "given": "the applicable business context, actor, and input for Maintenance phải gửi Notification trước khi bắt đầu",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-17-R006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-17-R006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Maintenance phải gửi Notification trước khi bắt đầu",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-17-R006-O001"
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
        "BRD-WS-17-R006-AC001",
        "BRD-WS-17-R006-AC002"
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
    "source_lines": "L555",
    "source_section": "21. Maintenance Notification"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R007-AC001",
      "given": "the applicable business context, actor, and input for Business Critical Job luôn được ưu tiên",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-17-R007-O001"
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
        "BRD-WS-17-R007-AC001"
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
    "source_lines": "L589",
    "source_section": "22. Scheduler Priority"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R008-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Operational Audit tuân thủ Security Policy",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-17-R008-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R008-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Operational Audit tuân thủ Security Policy",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-17-R008-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R008-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Operational Audit tuân thủ Security Policy",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-17-R008-O001"
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
      "criterion_references": [],
      "rationale": "BRD-WS-17-R008 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-17-R008-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R008-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L654",
    "source_section": "24. Operational Audit"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R009-AC001",
      "given": "an operational task within the scope of Audit không được phép chỉnh sửa",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-17-R009-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-17-R009-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Audit không được phép chỉnh sửa",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-17-R009-O001"
      ],
      "when": "operational verification is performed"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R009-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Audit không được phép chỉnh sửa",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-17-R009-O001"
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
      "criterion_references": [],
      "rationale": "BRD-WS-17-R009 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R009 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R009 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-17-R009-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R009-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R009 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L656",
    "source_section": "24. Operational Audit"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R010-AC001",
      "given": "an operational task within the scope of Operation Policy không được Hard-code",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-17-R010-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-17-R010-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Operation Policy không được Hard-code",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-17-R010-O001"
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
        "BRD-WS-17-R010-AC001",
        "BRD-WS-17-R010-AC002"
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
    "source_lines": "L685",
    "source_section": "25. Operation Policy"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R011-AC001",
      "given": "the applicable business context, actor, and input for Business Scheduler giúp tự động hóa quy trình nghiệp vụ mà không cần lập trình bổ sung",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-17-R011-O001"
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
        "BRD-WS-17-R011-AC001"
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
    "source_lines": "L719",
    "source_section": "26. Business Scheduler"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R012-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Organization chỉ được xem các thông tin Monitoring được Platform chia sẻ theo Permission",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the actor can retrieve only customer identities attributed to that actor; a customer attributed to another actor is absent and access to it is denied",
      "verifies": [
        "BRD-WS-17-R012-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R012-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Organization chỉ được xem các thông tin Monitoring được Platform chia sẻ theo Permission",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-17-R012-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R012-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Organization chỉ được xem các thông tin Monitoring được Platform chia sẻ theo Permission",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-17-R012-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-17-R012-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Organization chỉ được xem các thông tin Monitoring được Platform chia sẻ theo Permission",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-17-R012-O001"
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
        "BRD-WS-17-R012-AC001",
        "BRD-WS-17-R012-AC002",
        "BRD-WS-17-R012-AC003",
        "BRD-WS-17-R012-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R012-O001",
      "obligation_text": "Organization chỉ được xem các thông tin Monitoring được Platform chia sẻ theo Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-17-R012-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R012 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R012 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-17-R012-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R012-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R012 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L739",
    "source_section": "27. Organization Operations"
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
  "acceptance_contract": [],
  "acceptance_rationale": "Composite parent coverage is satisfied only through ALL_CHILDREN; the parent is not an acceptance unit.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
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
    "source_fingerprint": "3a8f29c73a1ed34989919fa2841f9b35d9a7bd34e0d192c28fbd07e3c0c670a1",
    "source_lines": "L798-L800",
    "source_section": "30. Enterprise Operations Principle"
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
    "source_lines": "L855",
    "source_section": "32. Feature Flag & Kill Switch"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R015-AC001",
      "given": "the applicable business context, actor, and input for Không cần Deploy lại hệ thống",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-17-R015-O001"
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
        "BRD-WS-17-R015-AC001"
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
    "source_lines": "L866",
    "source_section": "32. Feature Flag & Kill Switch"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R016-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Mọi thao tác yêu cầu: - Permission",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-17-R016-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R016-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Mọi thao tác yêu cầu: - Permission",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-17-R016-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R016-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Mọi thao tác yêu cầu: - Permission",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-17-R016-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-17-R016-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Mọi thao tác yêu cầu: - Permission",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-17-R016-O001"
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
        "BRD-WS-17-R016-AC001",
        "BRD-WS-17-R016-AC002",
        "BRD-WS-17-R016-AC003",
        "BRD-WS-17-R016-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R016-O001",
      "obligation_text": "Mọi thao tác yêu cầu: - Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-17-R016-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R016 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R016 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-17-R016-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R016-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R016 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L891-L893",
    "source_section": "33. Operational Command Center"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R017-AC001",
      "given": "an operational task within the scope of Mọi thao tác yêu cầu: - Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-17-R017-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-17-R017-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi thao tác yêu cầu: - Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-17-R017-O001"
      ],
      "when": "operational verification is performed"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R017-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Mọi thao tác yêu cầu: - Audit",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-17-R017-O001"
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
      "criterion_references": [],
      "rationale": "BRD-WS-17-R017 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R017 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R017 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-17-R017-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R017-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R017 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "c45736bd62f283d9b0cf99d73847444881aeb69221470655ccb78c797730351b",
    "source_lines": "L891-L894",
    "source_section": "33. Operational Command Center"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R018-AC001",
      "given": "the applicable business context, actor, and input for Mọi thao tác yêu cầu: - Runbook (nếu có)",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-17-R018-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-17-R018-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Mọi thao tác yêu cầu: - Runbook (nếu có)",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-17-R018-O001"
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
        "BRD-WS-17-R018-AC001",
        "BRD-WS-17-R018-AC002"
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
    "source_fingerprint": "57dd50fec5957bdc57ef356fe966ca977458ee75a1c1e22a218c545a0186684d",
    "source_lines": "L891-L895",
    "source_section": "33. Operational Command Center"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R019-AC001",
      "given": "an operational task within the scope of Replay giúp xử lý các trường hợp lỗi mà không cần viết Script hoặc thao tác trực tiếp trên Datab…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-17-R019-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-17-R019-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Replay giúp xử lý các trường hợp lỗi mà không cần viết Script hoặc thao tác trực tiếp trên Datab…",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-17-R019-O001"
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
        "BRD-WS-17-R019-AC001",
        "BRD-WS-17-R019-AC002"
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
    "source_lines": "L912",
    "source_section": "34. Replay Platform"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R020-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Replay chỉ được thực hiện bởi Operator có Permission phù hợp",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-17-R020-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R020-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Replay chỉ được thực hiện bởi Operator có Permission phù hợp",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-17-R020-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R020-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Replay chỉ được thực hiện bởi Operator có Permission phù hợp",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-17-R020-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "IDEMPOTENCY",
      "controlled_contract": "EXPLICIT_IDEMPOTENCY_CONTRACT_V1",
      "criterion_id": "BRD-WS-17-R020-AC004",
      "given": "a repeated request, retry, replay, or duplicate explicitly governed by Replay chỉ được thực hiện bởi Operator có Permission phù hợp",
      "observable_evidence": "original and repeated action identities, both outcomes, side-effect count, and resulting business state",
      "then": "the repeated action produces the requirement-specific stable result without an additional prohibited side effect",
      "verifies": [
        "BRD-WS-17-R020-O001"
      ],
      "when": "the same governed action is presented again under the declared identity or deduplication boundary"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-17-R020-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Replay chỉ được thực hiện bởi Operator có Permission phù hợp",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-17-R020-O001"
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
        "BRD-WS-17-R020-AC001",
        "BRD-WS-17-R020-AC002",
        "BRD-WS-17-R020-AC003",
        "BRD-WS-17-R020-AC004",
        "BRD-WS-17-R020-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R020-O001",
      "obligation_text": "Replay chỉ được thực hiện bởi Operator có Permission phù hợp"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-17-R020-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R020 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [
        "BRD-WS-17-R020-AC004"
      ],
      "status": "APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-17-R020-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R020-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R020 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L914",
    "source_section": "34. Replay Platform"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R021-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Mọi thao tác đều: - Kiểm tra Permission",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-17-R021-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R021-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Mọi thao tác đều: - Kiểm tra Permission",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-17-R021-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R021-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Mọi thao tác đều: - Kiểm tra Permission",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-17-R021-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-17-R021-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Mọi thao tác đều: - Kiểm tra Permission",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-17-R021-O001"
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
        "BRD-WS-17-R021-AC001",
        "BRD-WS-17-R021-AC002",
        "BRD-WS-17-R021-AC003",
        "BRD-WS-17-R021-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R021-O001",
      "obligation_text": "Mọi thao tác đều: - Kiểm tra Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-17-R021-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R021 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R021 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-17-R021-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R021-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R021 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "d218c6fa7e3720fab8613bd35f68b36cf4fff1e944a728a6136a18f14d45d453",
    "source_lines": "L545-L549",
    "source_section": "20. Operation Permission"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R022-AC001",
      "given": "an operational task within the scope of Mọi thao tác đều: - Ghi Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-17-R022-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-17-R022-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi thao tác đều: - Ghi Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-17-R022-O001"
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
        "BRD-WS-17-R022-AC001",
        "BRD-WS-17-R022-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R022-O001",
      "obligation_text": "Mọi thao tác đều: - Ghi Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R022 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R022 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R022 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R022 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R022-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R022 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "d218c6fa7e3720fab8613bd35f68b36cf4fff1e944a728a6136a18f14d45d453",
    "source_lines": "L545-L549",
    "source_section": "20. Operation Permission"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R023-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Mọi thao tác đều: - Tuân thủ Security Policy",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-17-R023-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R023-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Mọi thao tác đều: - Tuân thủ Security Policy",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-17-R023-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R023-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Mọi thao tác đều: - Tuân thủ Security Policy",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-17-R023-O001"
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
      "criterion_references": [],
      "rationale": "BRD-WS-17-R023 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R023 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R023 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-17-R023-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R023-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R023 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "d218c6fa7e3720fab8613bd35f68b36cf4fff1e944a728a6136a18f14d45d453",
    "source_lines": "L545-L549",
    "source_section": "20. Operation Permission"
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
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
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
    "source_lines": "L612",
    "source_section": "23. Auto Scaling"
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
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
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
    "source_lines": "L922",
    "source_section": "35. Chaos Readiness"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_TASK_OBSERVABILITY_V1",
      "criterion_id": "BRD-WS-17-R026-AC001",
      "given": "a running operational task",
      "observable_evidence": "operation identity, running state, signal names and values, and observation time",
      "then": "current running state and the relevant operational signals are available",
      "verifies": [
        "BRD-WS-17-R026-O001"
      ],
      "when": "an operator inspects the task"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_TASK_OBSERVABILITY_V1",
      "criterion_id": "BRD-WS-17-R026-AC002",
      "given": "a completed operational task",
      "observable_evidence": "operation identity, completed state, outcome, completion time, and evidence reference",
      "then": "terminal completion state and outcome evidence are available",
      "verifies": [
        "BRD-WS-17-R026-O002"
      ],
      "when": "an operator inspects the task"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_TASK_OBSERVABILITY_V1",
      "criterion_id": "BRD-WS-17-R026-AC003",
      "given": "a failed operational task",
      "observable_evidence": "operation identity, failed state, reason, diagnostic signal, and observation time",
      "then": "failed state, failure outcome, and relevant diagnostic signal are available",
      "verifies": [
        "BRD-WS-17-R026-O003"
      ],
      "when": "an operator inspects the task"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_OBSERVABILITY_VERIFICATION_V1",
      "criterion_id": "BRD-WS-17-R026-AC004",
      "given": "an operational task missing required state, outcome, or signal evidence",
      "observable_evidence": "failed verification result, operation identity, and missing-evidence identifiers",
      "then": "verification produces a detectable failure naming the missing evidence",
      "verifies": [
        "BRD-WS-17-R026-O004"
      ],
      "when": "operational observability is verified"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-17-R026-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R026-O001",
      "obligation_text": "A running operational task exposes its current state and relevant operational signals."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-17-R026-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R026-O002",
      "obligation_text": "A completed operational task exposes its outcome and completion evidence."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-17-R026-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R026-O003",
      "obligation_text": "A failed operational task exposes its failure outcome and relevant diagnostic signal."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-17-R026-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R026-O004",
      "obligation_text": "Missing required observability evidence produces a detectable operational verification failure."
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
    "source_document": "docs/BRD/BRD-WS-17.md"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R027-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Auditable operational task",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-17-R027-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R027-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Auditable operational task",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-17-R027-O001"
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
        "BRD-WS-17-R027-AC001",
        "BRD-WS-17-R027-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R027-O001",
      "obligation_text": "Mọi tác vụ vận hành phải tạo bằng chứng audit bất biến, gắn với actor, thời điểm, phạm vi và kết quả"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R027 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R027 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R027 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R027 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R027-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R027 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_document": "docs/BRD/BRD-WS-17.md"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R028-AC001",
      "given": "an operational task within the scope of Configurable operational task",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-17-R028-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-17-R028-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Configurable operational task",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-17-R028-O001"
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
        "BRD-WS-17-R028-AC001",
        "BRD-WS-17-R028-AC002"
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
    "source_document": "docs/BRD/BRD-WS-17.md"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R029-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Recoverable operational task",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-17-R029-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R029-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Recoverable operational task",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-17-R029-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "RECOVERY",
      "controlled_contract": "EXPLICIT_RECOVERY_CONTRACT_V1",
      "criterion_id": "BRD-WS-17-R029-AC003",
      "given": "a failed or interrupted case for which Recoverable operational task explicitly defines recovery, restore, rollback, or fallback behavior",
      "observable_evidence": "pre-failure state, recovery action, resulting state, outcome, and recovery evidence named by the obligation",
      "then": "the resulting state and outcome follow the requirement-specific recovery obligation and expose whether recovery completed or failed",
      "verifies": [
        "BRD-WS-17-R029-O001"
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
      "criterion_references": [],
      "rationale": "BRD-WS-17-R029 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R029 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R029 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R029 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R029-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [
        "BRD-WS-17-R029-AC003"
      ],
      "status": "APPLICABLE"
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
    "source_document": "docs/BRD/BRD-WS-17.md"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R030-AC001",
      "given": "an operational task within the scope of Automatable operational task",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-17-R030-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-17-R030-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Automatable operational task",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-17-R030-O001"
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
        "BRD-WS-17-R030-AC001",
        "BRD-WS-17-R030-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-17-R030-O001",
      "obligation_text": "Mọi tác vụ vận hành phải có contract cho phép tự động hóa có kiểm soát, permission và audit"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi tác vụ vận hành phải có contract cho phép tự động hóa có kiểm soát, permission và audit.",
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
    "source_document": "docs/BRD/BRD-WS-17.md"
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
  "stable_id": "BRD-WS-17-R030",
  "title": "Automatable operational task",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-17-R031 — No direct infrastructure manipulation

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-17-R031-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for No direct infrastructure manipulation",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the prohibited security decision path produces no effective permission or protected-state change, and conformance evidence identifies the attempted bypass",
      "verifies": [
        "BRD-WS-17-R031-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R031-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for No direct infrastructure manipulation",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-17-R031-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-17-R031-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by No direct infrastructure manipulation",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-17-R031-O001"
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
      "criterion_references": [],
      "rationale": "BRD-WS-17-R031 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R031 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R031 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-17-R031-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-17-R031-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-17-R031 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_document": "docs/BRD/BRD-WS-17.md"
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
### EP-17-001 — Platform Operations được quản lý tập trung thông qua Platform Operations Center

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-17-001-AC001",
      "given": "an operational task within the scope of Platform Operations được quản lý tập trung thông qua Platform Operations Center",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-17-001-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EP-17-001-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Platform Operations được quản lý tập trung thông qua Platform Operations Center",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EP-17-001-O001"
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
        "EP-17-001-AC001",
        "EP-17-001-AC002"
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
    "source_fingerprint": "3432d499946cd991216482e77997e52d778909b7efef8aeec8995e90921cdb93",
    "source_lines": "L1235-L1238",
    "source_section": "38. Enterprise Design Principles > EP-17-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-17-002-AC001",
      "given": "an operational task within the scope of Monitoring phải bao phủ toàn Platform",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-17-002-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EP-17-002-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Monitoring phải bao phủ toàn Platform",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EP-17-002-O001"
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
        "EP-17-002-AC001",
        "EP-17-002-AC002"
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
    "source_fingerprint": "117cb8abdc971d858c33dbdfc3361ec33c2eb3865b73b255329488772567fcae",
    "source_lines": "L1241-L1244",
    "source_section": "38. Enterprise Design Principles > EP-17-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-17-003-AC001",
      "given": "an operational task within the scope of Scheduler, Queue, Worker, Alert và Runbook đều là Business Object",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-17-003-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EP-17-003-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Scheduler, Queue, Worker, Alert và Runbook đều là Business Object",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EP-17-003-O001"
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
        "EP-17-003-AC001",
        "EP-17-003-AC002"
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
    "source_fingerprint": "c996ee6a618001b3961799eed54d812457ede0b5a5d447f8e2f7cbcb3e35ccd0",
    "source_lines": "L1247-L1250",
    "source_section": "38. Enterprise Design Principles > EP-17-003"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-17-004-AC001",
      "given": "an operational task within the scope of Operation Policy được cấu hình. Không Hard-code",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-17-004-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-17-004-AC002",
      "given": "an operational task within the scope of Operation Policy được cấu hình. Không Hard-code",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-17-004-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EP-17-004-AC003",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Operation Policy được cấu hình. Không Hard-code",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EP-17-004-O001",
        "EP-17-004-O002"
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
        "EP-17-004-AC001",
        "EP-17-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-004-O001",
      "obligation_text": "Operation Policy được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "EP-17-004-AC002",
        "EP-17-004-AC003"
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
    "source_fingerprint": "d57225268437c97036fba2bc3d1fdcbfb16fe62d9c72bb8d89c821c7d4715236",
    "source_lines": "L1253-L1258",
    "source_section": "38. Enterprise Design Principles > EP-17-004"
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
    "source_fingerprint": "9313a99369183fb8b855c9455e4efe1d97cfe662128432bc48831edb443f5ee9",
    "source_lines": "L1261-L1264",
    "source_section": "38. Enterprise Design Principles > EP-17-005"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-17-006-AC001",
      "given": "an operational task within the scope of Platform hỗ trợ Replay và Recoverable Operation",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-17-006-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EP-17-006-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Platform hỗ trợ Replay và Recoverable Operation",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EP-17-006-O001"
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
        "EP-17-006-AC001",
        "EP-17-006-AC002"
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
    "source_fingerprint": "7e0e518153fc987d1131b56137195013bf63e10afac016afc5714e854e806e80",
    "source_lines": "L1267-L1270",
    "source_section": "38. Enterprise Design Principles > EP-17-006"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-17-007-AC001",
      "given": "the applicable business context, actor, and input for Platform hỗ trợ Feature Flag và Kill Switch. Không cần Deploy để bật hoặc tắt chức năng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-17-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-17-007-AC002",
      "given": "the applicable business context, actor, and input for Platform hỗ trợ Feature Flag và Kill Switch. Không cần Deploy để bật hoặc tắt chức năng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-17-007-O002"
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
        "EP-17-007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-007-O001",
      "obligation_text": "Platform hỗ trợ Feature Flag và Kill Switch"
    },
    {
      "acceptance_criterion_references": [
        "EP-17-007-AC002"
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
    "source_fingerprint": "05a58a4b0d7303384b6489d3d62585a5a71f3b8b147f0afdbb5b97ad572c6b41",
    "source_lines": "L1273-L1278",
    "source_section": "38. Enterprise Design Principles > EP-17-007"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-17-008-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Mọi thao tác Operations đều phải: - Kiểm tra Permission - Ghi Audit - Tuân thủ Runbook (nếu có)",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "EP-17-008-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-17-008-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Mọi thao tác Operations đều phải: - Kiểm tra Permission - Ghi Audit - Tuân thủ Runbook (nếu có)",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "EP-17-008-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-17-008-AC003",
      "given": "an identified principal, applicable assurance context, and policy inputs for Mọi thao tác Operations đều phải: - Kiểm tra Permission - Ghi Audit - Tuân thủ Runbook (nếu có)",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "EP-17-008-O003"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "EP-17-008-AC004",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Mọi thao tác Operations đều phải: - Kiểm tra Permission - Ghi Audit - Tuân thủ Runbook (nếu có)",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "EP-17-008-O001",
        "EP-17-008-O002",
        "EP-17-008-O003"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-17-008-AC005",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Mọi thao tác Operations đều phải: - Kiểm tra Permission - Ghi Audit - Tuân thủ Runbook (nếu có)",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-17-008-O001",
        "EP-17-008-O002",
        "EP-17-008-O003"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "EP-17-008-AC006",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Mọi thao tác Operations đều phải: - Kiểm tra Permission - Ghi Audit - Tuân thủ Runbook (nếu có)",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "EP-17-008-O001",
        "EP-17-008-O002",
        "EP-17-008-O003"
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
        "EP-17-008-AC001",
        "EP-17-008-AC004",
        "EP-17-008-AC005",
        "EP-17-008-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-008-O001",
      "obligation_text": "Mọi thao tác Operations đều phải: Kiểm tra Permission."
    },
    {
      "acceptance_criterion_references": [
        "EP-17-008-AC002",
        "EP-17-008-AC004",
        "EP-17-008-AC005",
        "EP-17-008-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-008-O002",
      "obligation_text": "Mọi thao tác Operations đều phải: Ghi Audit."
    },
    {
      "acceptance_criterion_references": [
        "EP-17-008-AC003",
        "EP-17-008-AC004",
        "EP-17-008-AC005",
        "EP-17-008-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-17-008-O003",
      "obligation_text": "Mọi thao tác Operations đều phải: Tuân thủ Runbook (nếu có)."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "EP-17-008-AC006"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-17-008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-17-008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-17-008-AC005"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-17-008-AC001",
        "EP-17-008-AC002",
        "EP-17-008-AC003"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-17-008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "d18721d8104078b547e0a74ad90edb869a5df8ff48e6239bd848aeb1ad145557",
    "source_lines": "L1281-L1288",
    "source_section": "38. Enterprise Design Principles > EP-17-008"
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
    "source_fingerprint": "8e1054b5bb2c417f617b4b858ed09073bf623a101f309e0fee4f719651fcdec7",
    "source_lines": "L1291-L1294",
    "source_section": "38. Enterprise Design Principles > EP-17-009"
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
    "source_fingerprint": "91d2c85595883c6b57ca20d80a33b50464d99620c94641cbcecbcd91f6c59a7a",
    "source_lines": "L1297-L1308",
    "source_section": "38. Enterprise Design Principles > EP-17-010"
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
