---
document_code: AFM-00
document_name: AI Factory Manual
project: YSim v2.1
document_set: AI Factory Manual
version: 2.1
status: FROZEN
language: en-US
---

# AI Factory Manual

## AFM-00

---

# 1. Purpose

AI Factory Manual (AFM) là tài liệu giới thiệu tổng thể về YSim AI Software Factory.

AFM định nghĩa:

- Triết lý phát triển.
- Kiến trúc framework.
- Vòng đời phát triển.
- Mối quan hệ giữa các bộ tài liệu.
- Nguyên tắc phối hợp giữa AI và con người.

Đây là tài liệu đầu tiên cần đọc trước khi tham gia dự án.

---

# 2. Vision

YSim AI Software Factory hướng tới một quy trình phát triển phần mềm:

- AI-Driven
- Business-Driven
- Architecture-Driven
- Sprint-Driven
- Experience-Driven
- Quality-Driven
- Traceable
- Continuously Improving

Mọi thay đổi đều phải có nguồn gốc, bằng chứng và khả năng kiểm chứng.

---

# 3. Core Principles

Framework tuân thủ các nguyên tắc:

- Business First
- Architecture First
- Experience First
- Sprint Driven
- Full-stack Capability Delivery
- AI Assisted
- Engineering by Standards
- Configuration over Customization
- Governance by Evidence
- Continuous Improvement

---

# 4. Framework Architecture

```text
Business Layer
────────────────────────
BRD
YADF

↓

Architecture Layer
────────────────────────
ABP

↓

AI & Governance Layer
────────────────────────
AAP
SGP

↓

Engineering Layer
────────────────────────
ESP

↓

Implementation Layer
────────────────────────
DIP

↓

Verification Layer
────────────────────────
VAP

↓

Operations Layer
────────────────────────
ROP
```

Mỗi bộ tài liệu có trách nhiệm riêng và đóng vai trò là một phần của chuỗi phát triển thống nhất.

---

# 5. Sprint Lifecycle

```text
Business

↓

Architecture

↓

Sprint Planning

↓

Backend
   +
Frontend

↓

Integration

↓

Capability Demonstration

↓

Verification

↓

Release

↓

Operations

↓

Continuous Improvement
```

Một Sprint chỉ hoàn thành khi Capability đã được Demonstration và Verification thành công.

---

# 6. Roles

| Role | Responsibility |
|------|----------------|
| Business Owner | Định nghĩa Business |
| Architect | Thiết kế Architecture |
| AI Agent | Sinh Artifact theo Standards |
| Developer | Hiện thực và Review |
| QA | Verification |
| Operations | Production Operations |

---

# 7. AI Working Principles

AI phải:

- đọc đúng tài liệu;
- tuân thủ Standards;
- không tự thay đổi Architecture;
- không vượt Sprint Scope;
- luôn tạo Evidence;
- luôn đảm bảo Traceability;
- triển khai Backend và Frontend đồng thời;
- sinh Seed Data phục vụ kiểm thử;
- tạo Capability Demonstration Surface;
- không hoàn thành Capability khi chưa có Demonstration.

AI là thành viên của Factory, không phải người quyết định kiến trúc.

---

# 8. Engineering Philosophy

Framework coi mọi đầu ra đều là Engineering Asset.

Bao gồm:

- Source Code
- API
- Documentation
- Migration
- Test
- Configuration
- Release
- Runbook
- Storefront
- Portal
- Landing Page
- Component Library
- Design System
- Capability Demonstration Surface

Mọi Asset đều có vòng đời, version và khả năng truy vết.

---

# 9. Continuous Improvement

Sau mỗi Sprint và mỗi Release:

- Lessons Learned
- Operational Feedback
- Incident Review
- Architecture Review

được sử dụng để cải tiến Framework và hệ thống.

---

# 10. Success Criteria

Một Sprint được coi là thành công khi:

- Business Requirement được đáp ứng;
- Architecture được tuân thủ;
- Standards được tuân thủ;
- Capability Demonstration PASS;
- Verification PASS;
- Release thành công;
- Operations tiếp nhận;
- Lessons Learned được ghi nhận.

---

# 11. Relationship to Other Documents

Chuỗi tài liệu của AI Factory:

```text
BRD
    ↓
YADF
    ↓
ABP
    ↓
AAP
    ↓
SGP
    ↓
ESP
    ↓
DIP
    ↓
VAP
    ↓
ROP
```

Mỗi bộ tài liệu không chỉ định nghĩa yêu cầu kỹ thuật mà còn tạo thành chuỗi hướng dẫn để AI chuyển đổi từ Business Requirement sang Sprint Implementation một cách có khả năng truy vết.

---

# 12. Document Status

**Status: FROZEN**

AFM là tài liệu định hướng cao nhất của YSim AI Software Factory và phản ánh trạng thái kiến trúc hiện hành của phiên bản v2.1.
