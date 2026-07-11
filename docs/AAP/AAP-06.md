---
document_code: AAP-06
document_name: Architecture Change Proposal Model
project: YSim v2.1
document_set: AI Architecture Pack
version: 2.1
status: FROZEN
language: en-US
---

# Architecture Change Proposal Model

## AAP-06

---

# 1. Purpose

Architecture Change Proposal (ACP) Model định nghĩa quy trình đề xuất thay đổi kiến trúc trong quá trình AI triển khai Sprint.

AI không được tự thay đổi Architecture Baseline.

Mọi thay đổi kiến trúc đều phải thông qua ACP.

---

# 2. Principles

ACP tuân thủ các nguyên tắc:

- Architecture First
- Human Governed
- Proposal Before Change
- Impact Driven
- Evidence Based
- Traceable
- Versioned
- Full-stack Impact Analysis
- Experience-aware Governance

ACP không phải Implementation.

ACP là Proposal.

---

# 3. ACP Objectives

ACP được sử dụng khi:

- Sprint Contract không thể thực hiện.
- Architecture Baseline có mâu thuẫn.
- Dependency không còn phù hợp.
- Thiết kế hiện tại gây rủi ro lớn.
- Có giải pháp tốt hơn nhưng ảnh hưởng Architecture.

ACP không được dùng cho thay đổi nhỏ trong phạm vi Sprint.

---

# 4. ACP Trigger Conditions

AI phải tạo ACP khi gặp một trong các trường hợp:

- Vi phạm Module Boundary.
- Vi phạm Dependency Rules.
- Cần tạo Business Object mới.
- Cần thay đổi Registry.
- Cần thay đổi Event Contract.
- Cần thay đổi Snapshot Contract.
- Cần thay đổi Public API.
- Cần thay đổi Frontend Contract.
- Cần thay đổi Design System Foundation.
- Cần thay đổi Experience Composition.
- Cần thay đổi Ownership.

Nếu không thuộc các trường hợp trên thì không tạo ACP.

---

# 5. ACP Structure

ACP bao gồm:

```text
Proposal Metadata

↓

Problem Statement

↓

Current Architecture

↓

Proposed Change

↓

Impact Analysis

↓

Alternative Options

↓

Recommendation

↓

Decision
```

---

# 6. Proposal Metadata

Bao gồm:

- ACP ID
- Sprint ID
- Version
- Status
- Created By
- Created Time

ACP có Version độc lập.

---

# 7. Problem Statement

ACP phải mô tả rõ:

- vấn đề là gì;
- xảy ra ở đâu;
- vì sao không thể tiếp tục;
- ảnh hưởng tới Sprint nào.

Không mô tả chung chung.

---

# 8. Current Architecture

ACP phải chỉ rõ:

- Module
- Capability
- Business Object
- API
- Event
- Snapshot
- Frontend
- Design System
- Experience Composition
- Dependency

đang bị ảnh hưởng.

---

# 9. Proposed Change

ACP mô tả:

- thay đổi đề xuất;
- phạm vi;
- Architecture Component liên quan;
- Registry cần cập nhật (nếu có).

Proposal không chứa Source Code.

---

# 10. Impact Analysis

ACP đánh giá ảnh hưởng tới:

- Business Capability
- Module
- Domain
- API
- Event
- Snapshot
- Database
- Integration
- Security
- Testing
- Deployment
- Frontend
- Design System
- Customer Experience

Impact phải đầy đủ.

---

# 10A. Full-stack Impact Assessment

Đối với Capability có giao diện người dùng, ACP phải đánh giá đồng thời tác động đến:

- Backend Architecture
- API Contract
- Frontend Pages
- UI Components
- Design System
- Storefront Runtime
- Capability Demonstration
- Test Strategy

Không được đánh giá thay đổi kiến trúc chỉ ở Backend nếu thay đổi đó ảnh hưởng Experience.

---

# 11. Alternative Options

ACP phải có tối thiểu:

- Option A
- Option B

Nếu có thể:

- Option C

AI không chỉ đưa ra một phương án duy nhất.

---

# 12. Recommendation

AI đưa ra:

- Recommended Option
- Lý do
- Ưu điểm
- Rủi ro
- Điều kiện áp dụng

Recommendation phải giải thích được.

---

# 13. Decision Workflow

```text
Draft

↓

Architecture Review

↓

Business Review (if required)

↓

Approved / Rejected

↓

Architecture Baseline Update

↓

Sprint Resume
```

AI không được tự chuyển sang bước cuối.

---

# 14. Architecture Baseline Update

Nếu ACP được phê duyệt:

- cập nhật Architecture Baseline;
- cập nhật Registry;
- cập nhật Sprint Contract nếu cần.

Chỉ sau đó AI mới được tiếp tục triển khai.

---

# 15. ACP Traceability

ACP phải truy vết được tới:

- Sprint
- Capability
- Module
- Business Object
- Registry
- Architecture Baseline
- Decision
- Reviewer

---

# 16. ACP Rules

ACP-001 — AI không tự thay đổi Architecture.

ACP-002 — ACP phải có Impact Analysis.

ACP-003 — ACP phải có Alternative Options.

ACP-004 — ACP phải có Recommendation.

ACP-005 — ACP không chứa Source Code.

ACP-006 — ACP phải được Review.

ACP-007 — ACP phải được Version.

ACP-008 — ACP phải truy vết được.

ACP-009 — Sprint chỉ tiếp tục sau khi ACP được quyết định.

ACP-010 — ACP được lưu như một Architecture Artifact.

---

# 17. Architecture Change Resolution Pipeline (ACRP)

```text
Architecture Conflict
        │
        ▼
Full-stack Impact Identification
        │
        ▼
Problem Identification
        │
        ▼
Impact Analysis
        │
        ▼
Alternative Analysis
        │
        ▼
Recommendation
        │
        ▼
Architecture Review
        │
        ▼
Decision
        │
        ▼
Architecture Baseline Update
        │
        ▼
Sprint Resume
```

---

# 18. ACP Deliverables

Một ACP tối thiểu phải tạo:

- ACP Document
- Impact Analysis
- Architecture Diagram Update (nếu có)
- Registry Change Summary
- Frontend Impact Summary
- Demonstration Impact Summary
- Recommendation
- Decision Record

---

# 19. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0601 | ACP được tạo đúng điều kiện |
| ACC-0602 | Problem Statement rõ ràng |
| ACC-0603 | Impact Analysis đầy đủ |
| ACC-0604 | Alternative Options tồn tại |
| ACC-0605 | Recommendation có giải thích |
| ACC-0606 | ACP không chứa Source Code |
| ACC-0607 | Architecture Review hoàn thành |
| ACC-0608 | Decision được ghi nhận |
| ACC-0609 | Architecture Baseline được cập nhật (nếu Approved) |
| ACC-0610 | Sprint chỉ tiếp tục sau Decision |

---

# 20. Relationship to Other Documents

AAP-06 liên kết với:

- AAP-01 Repository Discovery Model
- AAP-02 Sprint Contract Model
- AAP-03 AI Planning Model
- AAP-04 AI Verification Model
- AAP-05 AI Evidence Model
- ABP-15 AI Implementation Architecture
- Architecture Baseline Pack (ABP)
- Sprint Governance Pack (SGP)

ACP là cơ chế quản trị mọi thay đổi kiến trúc phát sinh trong quá trình AI triển khai, bảo đảm mọi thay đổi đều được đánh giá trên cả Backend, Frontend và Experience.

---

# 21. Document Status

**Status: FROZEN**

AAP-06 là tài liệu nền tảng quy định mô hình đề xuất thay đổi kiến trúc của nền tảng YSim.

Mọi AI Coding Assistant phải sử dụng ACP khi phát hiện nhu cầu thay đổi Architecture Baseline.

---