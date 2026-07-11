---
document_code: SGP-06
document_name: Sprint Metrics & Reporting
project: YSim v2.0
document_set: Sprint Governance Pack
version: 1.0
status: FROZEN
language: en-US
---

# Sprint Metrics & Reporting

## SGP-06

---

# 1. Purpose

Sprint Metrics & Reporting định nghĩa mô hình đo lường và báo cáo hiệu quả Sprint trong nền tảng YSim.

Tài liệu này chuẩn hóa:

- Sprint Metrics
- AI Metrics
- Quality Metrics
- Architecture Metrics
- Governance Metrics
- Reporting Model
- Continuous Improvement

Metrics được sử dụng để cải tiến quy trình phát triển.

Metrics không được sử dụng để đánh giá cảm tính.

---

# 2. Principles

Sprint Metrics tuân thủ các nguyên tắc:

- Evidence Driven
- Objective
- Repeatable
- Traceable
- Comparable
- Actionable

Mọi Metrics đều phải có nguồn dữ liệu xác định.

---

# 3. Metrics Categories

Platform chuẩn hóa các nhóm Metrics.

| Category | Purpose |
|----------|----------|
| Delivery Metrics | Tiến độ Sprint |
| Quality Metrics | Chất lượng |
| Architecture Metrics | Tuân thủ kiến trúc |
| AI Metrics | Hiệu quả AI |
| Governance Metrics | Hiệu quả quản trị |
| Operations Metrics | Khả năng Release |

---

# 4. Delivery Metrics

Theo dõi:

- Sprint Duration
- Planned Work Items
- Completed Work Items
- Sprint Throughput
- Lead Time
- Cycle Time

Delivery Metrics phản ánh khả năng hoàn thành Sprint.

---

# 5. Quality Metrics

Theo dõi:

- Build Success Rate
- Test Pass Rate
- Test Coverage
- Defect Count
- Regression Count
- Rework Count

Quality Metrics phản ánh chất lượng kỹ thuật.

---

# 6. Architecture Metrics

Theo dõi:

- Architecture Compliance Rate
- Dependency Violations
- Boundary Violations
- ACP Count
- Registry Compliance
- Technical Debt Introduced

Architecture Metrics phản ánh mức độ tuân thủ Architecture Baseline.

---

# 7. AI Metrics

Theo dõi:

- Repository Discovery Duration
- Planning Duration
- Code Generation Duration
- Verification Duration
- Evidence Generation Duration
- AI Success Rate
- AI Rework Rate
- AI Acceptance Rate

AI Metrics phản ánh hiệu quả của AI Coding Assistant.

---

# 8. Governance Metrics

Theo dõi:

- Governance Checkpoint Pass Rate
- Quality Gate Pass Rate
- Review Duration
- Approval Duration
- Acceptance Duration
- Decision Turnaround Time

Governance Metrics phản ánh hiệu quả quản trị Sprint.

---

# 9. Operations Metrics

Theo dõi:

- Release Readiness
- Rollback Readiness
- Deployment Success Rate
- Production Acceptance
- Post-release Incidents

Operations Metrics phản ánh mức độ sẵn sàng đưa Sprint vào Production.

---

# 10. KPI & SLI

Platform phân biệt:

## KPI

Đo hiệu quả quản trị.

Ví dụ:

- Sprint On-time Rate
- Acceptance Rate
- AI Productivity
- Delivery Throughput

## SLI

Đo chất lượng hệ thống.

Ví dụ:

- Build Success
- Test Success
- Verification Success
- Release Success

---

# 11. Reporting Levels

Platform hỗ trợ báo cáo ở nhiều cấp.

| Level | Description |
|---------|-------------|
| Sprint | Một Sprint |
| Release | Một Release |
| Project | Toàn dự án |
| Portfolio | Nhiều dự án |

---

# 12. Reporting Dashboard

Dashboard chuẩn bao gồm:

- Sprint Status
- Progress
- Risks
- Issues
- Metrics
- Quality Gates
- Governance Checkpoints
- AI Performance

Dashboard phải cập nhật theo thời gian gần thực.

---

# 13. Reporting Schedule

Hệ thống hỗ trợ:

- Real-time Dashboard
- Daily Summary
- Weekly Report
- Sprint Report
- Release Report
- Monthly Trend

---

# 14. Continuous Improvement

Metrics được sử dụng để:

- xác định Bottleneck;
- cải thiện AI Planning;
- tối ưu Sprint Lifecycle;
- cải thiện Governance;
- nâng cao chất lượng.

Metrics không dùng để thay thế Human Review.

---

# 15. Metrics Rules

MR-001 — Mọi Metrics phải có nguồn dữ liệu.

MR-002 — Metrics phải truy vết được.

MR-003 — Dashboard phản ánh dữ liệu thực tế.

MR-004 — KPI và SLI phải được tách biệt.

MR-005 — Governance Metrics là bắt buộc.

MR-006 — AI Metrics là bắt buộc.

MR-007 — Architecture Metrics là bắt buộc.

MR-008 — Metrics không được chỉnh sửa thủ công.

MR-009 — Reporting phải hỗ trợ Audit.

MR-010 — Metrics phải phục vụ Continuous Improvement.

---

# 16. Sprint Metrics Resolution Pipeline (SMRP)

```text
Sprint Activities
        │
        ▼
Metrics Collection
        │
        ▼
Metrics Aggregation
        │
        ▼
KPI & SLI Calculation
        │
        ▼
Dashboard Update
        │
        ▼
Reporting
        │
        ▼
Continuous Improvement
```

---

# 17. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0601 | Delivery Metrics đầy đủ |
| ACC-0602 | Quality Metrics đầy đủ |
| ACC-0603 | Architecture Metrics đầy đủ |
| ACC-0604 | AI Metrics đầy đủ |
| ACC-0605 | Governance Metrics đầy đủ |
| ACC-0606 | Operations Metrics đầy đủ |
| ACC-0607 | Dashboard hoạt động |
| ACC-0608 | Reports được sinh |
| ACC-0609 | Metrics hỗ trợ Audit |
| ACC-0610 | Metrics phục vụ Continuous Improvement |

---

# 18. Relationship to Other Documents

SGP-06 liên kết với:

- SGP-04 Sprint Execution Governance
- SGP-05 Sprint Review & Acceptance
- ABP-10 Observability Architecture
- ABP-13 Testing Architecture
- AAP-05 AI Evidence Model
- ROP (Release & Operations Pack)

Metrics & Reporting cung cấp dữ liệu cho Governance, Release và Continuous Improvement.

---

# 19. Document Status

**Status: FROZEN**

SGP-06 là tài liệu nền tảng quy định mô hình đo lường và báo cáo Sprint của YSim.

Mọi Sprint phải tạo đầy đủ Metrics và Reports theo quy định của Sprint Governance Pack.

---