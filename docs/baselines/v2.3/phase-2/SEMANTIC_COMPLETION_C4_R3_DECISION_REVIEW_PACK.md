# Semantic Completion C4-R3 Decision Review Pack

- Candidate: `V23-P2C-SEMANTIC-COMPLETION-C4-R3`
- Selection status: `PENDING_HUMAN_APPROVAL`

| Decision | Requirement | Criticality | Recommended | Audit | Dependencies |
|---|---|---:|---|---|---|
| `P2C-SC-C1-DEC-001` | `BD-04-001` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-001 — BD-04-001

Source: `docs/BRD/BRD-WS-04.md:L523-L530` — 24. Business Decisions (Locked) > BD-04-001

## BD-04-001

YSim sử dụng mô hình Four-Level Catalog:

- Supplier Catalog
- Master Catalog
- Sales Catalog
- Storefront Catalog

Recommendation: `OPT-AST` — Exact membership and declared sequence replace under-constrained SET_CONTAINS.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-002` | `BD-07-014` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-002 — BD-07-014

Source: `docs/BRD/BRD-WS-07.md:L718-L720` — 24. Business Decisions (Locked) > BD-07-014

## BD-07-014

Một Sales Order có thể phát sinh nhiều Purchase Order.

Recommendation: `OPT-AST` — Reference validity and one-to-many cardinality are both explicit.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-003` | `BD-09-014` | CRITICAL | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-003 — BD-09-014

Source: `docs/BRD/BRD-WS-09.md:L642-L644` — 25. Business Decisions (Locked) > BD-09-014

## BD-09-014

Fulfillment hoàn thành khi Delivery thành công.

Recommendation: `OPT-AST` — Canonical states plus prerequisite and terminal prohibition are retained.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-004` | `BD-16-027` | CRITICAL | `OPT-A` | `BUSINESS_DECISION_OPTION_READY` | None |

## P2C-SC-C1-DEC-004 — BD-16-027

Source: `docs/BRD/BRD-WS-16.md:L1033-L1035` — 31. Business Decisions (Locked) > BD-16-027

## BD-16-027

Security Platform Publish Business Event.

Recommendation: `OPT-A` — Source lacks exact event governance; three mutually exclusive business choices are exposed.

Options:
- `OPT-A` → `BUSINESS_DECISION_THEN_OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve a versioned Security Event Catalog defining canonical event type, trigger, correlation and payload contract.
- `OPT-B` → `BUSINESS_DECISION_THEN_OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Require a governed Security Business Event while exact type and trigger resolve from versioned policy.
- `OPT-C` → `SEPARATE_SECURITY_EVENT_GOVERNANCE_AND_HUMAN_PROCEDURE`: Defer event taxonomy to separate security-event governance and use a human procedure meanwhile.
| `P2C-SC-C1-DEC-005` | `BD-17-016` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-005 — BD-17-016

Source: `docs/BRD/BRD-WS-17.md:L1121-L1123` — 37. Business Decisions (Locked) > BD-17-016

## BD-17-016

Platform có Operational Dashboard dành riêng cho Operator.

Recommendation: `OPT-AST` — Availability and both access boundaries are independently evidenced.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-006` | `BRD-UPDATE-01-R028` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-006 — BRD-UPDATE-01-R028

Source: `docs/BRD/BRD-UPDATE-01.md:L907-L919` — 17. Business Principles > API First

# 17. Business Principles

Commerce Experience Platform tuân thủ:

- Commerce First
- Configuration over Customization
- White-label by Default
- Publish in Minutes
- Multi-tenant
- Multi-brand
- Multi-language
- Multi-country
- API First

Recommendation: `OPT-AST` — A compound architecture-conformance AST replaces CAPABILITY_AVAILABLE.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-007` | `BRD-WS-02-R004` | NORMAL | `OPT-CLARIFY` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-007 — BRD-WS-02-R004

Source: `docs/BRD/BRD-WS-02.md:L286-L300` — 11. Inventory Strategy

- Product Item
- QR Code
- ICCID
- Activation Code
- Supplier Reference
- Purchase Cost
- Current Owner
- Inventory Status
- Lifecycle

Inventory luôn tồn tại.

Ngay cả khi Product Item được mua tức thời từ Supplier để phục vụ một đơn hàng cụ thể.

Inventory là cơ sở cho:

Recommendation: `OPT-CLARIFY` — Clarification preserves every named field without silently choosing universal Product Item cardinality.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-CLARIFY` → `EXACT_SOURCE_CLARIFICATION_THEN_OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the exact source clarification, preserve the requirement ID, then use the attached provisional AST; no source edit occurs in this candidate.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-008` | `BRD-WS-04-R011` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-008 — BRD-WS-04-R011

Source: `docs/BRD/BRD-WS-04.md:L337-L348` — 16. Product Version

Nếu Supplier thay đổi:

- Product Policy
- Product Specification
- Activation Rule
- Product Behavior

YSim tạo Product Version mới.

Version luôn đi kèm Publish Workflow.

Không Publish tự động.

Recommendation: `OPT-AST` — Existing source is sufficient; direct compound AST is recommended.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-009` | `BRD-WS-07-R001` | CRITICAL | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-009 — BRD-WS-07-R001

Source: `docs/BRD/BRD-WS-07.md:L120-L125` — 4. Order Taxonomy > Purchase Order (PO)

## Purchase Order (PO)

Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier.

PO là giao dịch giữa:


Recommendation: `OPT-AST` — Conditional custom AST avoids inventing a policy ID or canonical outcome.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-010` | `BRD-WS-11-R009` | NORMAL | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-010 — BRD-WS-11-R009

Source: `docs/BRD/BRD-WS-11.md:L480-L496` — 20. Satisfaction Survey

# 20. Satisfaction Survey

Platform hỗ trợ:

- CSAT
- CES
- NPS
- Rating
- Emoji Rating

Có thể cấu hình:

- Always
- Random
- Disabled

Organization có thể chủ động câu hình thiết lập các Satisfaction Survey này hoặc sử dụng từ Parent.

Recommendation: `OPT-AST` — Configuration resolution and enum validity are independently asserted.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-011` | `BRD-WS-13-R003` | HIGH | `OPT-CLARIFY` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-011 — BRD-WS-13-R003

Source: `docs/BRD/BRD-WS-13.md:L108-L118` — 4. Dashboard Widget

- Saved Dashboard Layout

Widget có thể tái sử dụng tại:

- Dashboard
- Workspace
- Admin Portal
- Organization Portal
- Customer Portal

Widget Library cho phép Organization lựa chọn Widget cần hiển thị hoặc ẩn.

Recommendation: `OPT-CLARIFY` — All five source-named surfaces, including independent Customer Portal, are retained.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-CLARIFY` → `EXACT_SOURCE_CLARIFICATION_THEN_OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the exact source clarification, preserve the requirement ID, then use the attached provisional AST; no source edit occurs in this candidate.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-012` | `BRD-WS-13-R021` | NORMAL | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-012 — BRD-WS-13-R021

Source: `docs/BRD/BRD-WS-13.md:L648-L658` — 25. Widget Library

- Notification Widget
- Dashboard Shortcut Widget

Widget có thể:

- Enable
- Disable
- Override Configuration
- Configure Parameter

Organization có thể lựa chọn Widget cần hiển thị.

Recommendation: `OPT-AST` — No unsupported permission qualifier is injected; adjacent obligations are explicitly preserved.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-013` | `BRD-WS-14-R013` | NORMAL | `OPT-A` | `BUSINESS_DECISION_OPTION_READY` | None |

## P2C-SC-C1-DEC-013 — BRD-WS-14-R013

Source: `docs/BRD/BRD-WS-14.md:L419-L435` — 15. Configuration Version


↓

Published

↓

Effective
```

Version cũ luôn được lưu lại.

Không ghi đè dữ liệu.

Configuration Version áp dụng cho:

- Configuration

Recommendation: `OPT-A` — Choices distinguish append-only history from policy-governed or separately decided duration.

Options:
- `OPT-A` → `APPEND_ONLY_VERSION_HISTORY_AST_RUNTIME_ADAPTER_PENDING`: Old versions remain addressable and overwrite is prohibited; no finite duration is inferred.
- `OPT-B` → `VERSIONED_RETENTION_POLICY_THEN_AST_RUNTIME_ADAPTER_PENDING`: Retention duration resolves from a separately versioned policy; overwrite remains prohibited.
- `OPT-C` → `SEPARATE_RETENTION_DURATION_BUSINESS_DECISION_REQUIRED`: No duration is selected; exact retention duration is deferred to a separate business decision.
| `P2C-SC-C1-DEC-014` | `BRD-WS-14-R025` | NORMAL | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-014 — BRD-WS-14-R025

Source: `docs/BRD/BRD-WS-14.md:L590-L599` — 22. Configuration Rollback


Rollback không được làm mất:

- Audit
- Version History
- Approval History

Rollback luôn tạo một Version mới.

Không ghi đè Version cũ.

Recommendation: `OPT-AST` — All rollback clauses are mapped exactly once.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-015` | `BRD-WS-17-R018` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-015 — BRD-WS-17-R018

Source: `docs/BRD/BRD-WS-17.md:L883-L897` — 33. Operational Command Center

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

Recommendation: `OPT-AST` — Source is sufficient; conditional applicability resolver enables a direct AST.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-016` | `BRD-WS-17-R029` | CRITICAL | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-016 — BRD-WS-17-R029

Source: `docs/BRD/BRD-WS-17.md:L798-L810` — 30. Enterprise Operations Principle

# 30. Enterprise Operations Principle

Platform áp dụng nguyên lý:

**Mọi tác vụ vận hành phải có khả năng:**

- Observable
- Auditable
- Configurable
- Recoverable
- Automatable

Operator không thao tác trực tiếp trên hạ tầng nếu Platform đã cung cấp chức năng tương ứng.

Recommendation: `OPT-AST` — Compound AST preserves P2-DEC-003/004/010 and does not collapse to audit alone.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-017` | `EP-12-003` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-017 — EP-12-003

Source: `docs/BRD/BRD-WS-12.md:L766-L768` — 33. Enterprise Design Principles > EP-12-003

## EP-12-003

Communication Matrix quyết định toàn bộ hành vi gửi Notification.

Recommendation: `OPT-AST` — Four delivery dimensions and versioned evidence replace one generic policy outcome.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-018` | `EP-13-001` | CRITICAL | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-018 — EP-13-001

Source: `docs/BRD/BRD-WS-13.md:L993-L999` — 30. Enterprise Design Principles > EP-13-001

# 30. Enterprise Design Principles

## EP-13-001

Dashboard là cửa ngõ truy cập nhanh tới Business Object.

Mọi Widget đều hỗ trợ Drill-down tới dữ liệu chi tiết theo Permission.

Recommendation: `OPT-AST` — Access, universal drill-down and both permission boundaries are explicit.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-019` | `EP-14-010` | NORMAL | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-019 — EP-14-010

Source: `docs/BRD/BRD-WS-14.md:L1252-L1254` — 32. Enterprise Design Principles > EP-14-010

## EP-14-010

Organization được khởi tạo bằng Template nhằm giảm thời gian Onboarding.

Recommendation: `OPT-AST` — Reduced onboarding time remains rationale, not an unmeasured oracle.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-020` | `EP-17-001` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-020 — EP-17-001

Source: `docs/BRD/BRD-WS-17.md:L1235-L1239` — 38. Enterprise Design Principles > EP-17-001

# 38. Enterprise Design Principles

## EP-17-001

Platform Operations được quản lý tập trung thông qua Platform Operations Center.

Recommendation: `OPT-AST` — Central-management boundary replaces ACTOR_AUTHORIZED-only mapping.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-021` | `UXF-002` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-021 — UXF-002

Source: `docs/UXF/UXF-00.md:L612-L614` — 20. Architectural Principles > UXF-002

### UXF-002

Storefronts represent commercial experiences rather than websites.

Recommendation: `OPT-AST` — First dependency establishes commercial-experience identity without a fictional policy outcome.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-022` | `UXF-003` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | P2C-SC-C1-DEC-021 |

## P2C-SC-C1-DEC-022 — UXF-003

Source: `docs/UXF/UXF-00.md:L618-L620` — 20. Architectural Principles > UXF-003

### UXF-003

Storefronts consume YSim Products only.

Recommendation: `OPT-AST` — Canonical product boundary follows Storefront identity.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-023` | `UXF-008` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-023 — UXF-008

Source: `docs/UXF/UXF-00.md:L648-L650` — 20. Architectural Principles > UXF-008

### UXF-008

Localization defines customer experience, not only language.

Recommendation: `OPT-AST` — P2-DEC-008 dimensions are materialized; locale inventory is not inferred.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-024` | `UXF-02-R009` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | None |

## P2C-SC-C1-DEC-024 — UXF-02-R009

Source: `docs/UXF/UXF-02.md:L535-L543` — 18. Design Accessibility


- Keyboard Navigation
- Screen Readers
- Responsive Layout
- High Contrast
- Focus Indicators
- Touch Interaction

Accessibility cannot be disabled by Themes.

Recommendation: `OPT-AST` — UXD-07 supplies shared standard; this record remains the theme invariant.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-025` | `UXF-209` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | P2C-SC-C1-DEC-024 |

## P2C-SC-C1-DEC-025 — UXF-209

Source: `docs/UXF/UXF-02.md:L613-L615` — 20. Design Principles > UXF-209

### UXF-209

Accessibility is mandatory.

Recommendation: `OPT-AST` — UXD-07 supplies shared standard; this remains distinct from the theme invariant.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-026` | `UXF-301` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | P2C-SC-C1-DEC-021, P2C-SC-C1-DEC-022 |

## P2C-SC-C1-DEC-026 — UXF-301

Source: `docs/UXF/UXF-03.md:L628-L632` — 22. Architectural Principles > UXF-301

# 22. Architectural Principles

### UXF-301

Storefronts are runtime experiences.

Recommendation: `OPT-AST` — Runtime boundary follows commercial identity and product boundary.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
| `P2C-SC-C1-DEC-027` | `UXF-302` | HIGH | `OPT-AST` | `SAFE_TO_APPROVE_RECOMMENDED_OPTION` | P2C-SC-C1-DEC-021, P2C-SC-C1-DEC-022, P2C-SC-C1-DEC-026 |

## P2C-SC-C1-DEC-027 — UXF-302

Source: `docs/UXF/UXF-03.md:L636-L638` — 22. Architectural Principles > UXF-302

### UXF-302

Templates define structure only.

Recommendation: `OPT-AST` — Final dependency separates template structure from runtime/business behavior.

Options:
- `OPT-AST` → `OPERATOR_AST_RUNTIME_ADAPTER_PENDING`: Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.
- `OPT-HUMAN` → `CONCRETE_HUMAN_VERIFICATION_PROCEDURE`: No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.
