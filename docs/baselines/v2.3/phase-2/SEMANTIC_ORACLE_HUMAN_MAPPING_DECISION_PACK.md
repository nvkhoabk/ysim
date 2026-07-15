# Semantic Oracle Human Mapping Decision Pack

- Candidate: `V23-P2C-SEMANTIC-ORACLE-MODEL-C2`
- Decisions: `27`
- Selected: `0`
- Approval scope: `EXCLUDED_FROM_C2_MODEL_APPROVAL`

## P2C-SO-C2-HOMR-001 — BD-04-001

- Criticality: `HIGH`
- Statement: YSim sử dụng mô hình Four-Level Catalog: - Supplier Catalog - Master Catalog - Sales Catalog - Storefront Catalog
- Recommended (not selected): `P2C-SO-C2-HOMR-001-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-002 — BD-07-014

- Criticality: `HIGH`
- Statement: Một Sales Order có thể phát sinh nhiều Purchase Order.
- Recommended (not selected): `P2C-SO-C2-HOMR-002-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-003 — BD-09-014

- Criticality: `CRITICAL`
- Statement: Fulfillment hoàn thành khi Delivery thành công.
- Recommended (not selected): `P2C-SO-C2-HOMR-003-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-004 — BD-16-027

- Criticality: `CRITICAL`
- Statement: Security Platform Publish Business Event.
- Recommended (not selected): `P2C-SO-C2-HOMR-004-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `ACTOR_AUTHORIZED, ACTOR_DENIED, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-005 — BD-17-016

- Criticality: `HIGH`
- Statement: Platform có Operational Dashboard dành riêng cho Operator.
- Recommended (not selected): `P2C-SO-C2-HOMR-005-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `DELIVERY_TERMINAL_STATE, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-006 — BRD-UPDATE-01-R028

- Criticality: `HIGH`
- Statement: Commerce Experience Platform tuân thủ: - API First
- Recommended (not selected): `P2C-SO-C2-HOMR-006-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `REFERENCE_TARGET_VALID, DELIVERY_TERMINAL_STATE`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-007 — BRD-WS-02-R004

- Criticality: `NORMAL`
- Statement: Inventory luôn tồn tại.
- Recommended (not selected): `P2C-SO-C2-HOMR-007-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-008 — BRD-WS-04-R011

- Criticality: `HIGH`
- Statement: Version luôn đi kèm Publish Workflow.
- Recommended (not selected): `P2C-SO-C2-HOMR-008-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-009 — BRD-WS-07-R001

- Criticality: `CRITICAL`
- Statement: Purchase Order phát sinh khi YSim cần nhập Product Item từ Supplier.
- Recommended (not selected): `P2C-SO-C2-HOMR-009-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-010 — BRD-WS-11-R009

- Criticality: `NORMAL`
- Statement: Có thể cấu hình: - Always - Random - Disabled
- Recommended (not selected): `P2C-SO-C2-HOMR-010-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-011 — BRD-WS-13-R003

- Criticality: `HIGH`
- Statement: Widget Library cho phép Organization lựa chọn Widget cần hiển thị hoặc ẩn.
- Recommended (not selected): `P2C-SO-C2-HOMR-011-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-012 — BRD-WS-13-R021

- Criticality: `NORMAL`
- Statement: Organization có thể lựa chọn Widget cần hiển thị.
- Recommended (not selected): `P2C-SO-C2-HOMR-012-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-013 — BRD-WS-14-R013

- Criticality: `NORMAL`
- Statement: Version cũ luôn được lưu lại.
- Recommended (not selected): `P2C-SO-C2-HOMR-013-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-014 — BRD-WS-14-R025

- Criticality: `NORMAL`
- Statement: Rollback luôn tạo một Version mới.
- Recommended (not selected): `P2C-SO-C2-HOMR-014-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-015 — BRD-WS-17-R018

- Criticality: `HIGH`
- Statement: Mọi thao tác yêu cầu: - Runbook (nếu có)
- Recommended (not selected): `P2C-SO-C2-HOMR-015-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-016 — BRD-WS-17-R029

- Criticality: `CRITICAL`
- Statement: Mọi tác vụ vận hành phải có đường khôi phục xác định, có thể đối soát kết quả và bảo toàn bất biến khi thất bại.
- Recommended (not selected): `P2C-SO-C2-HOMR-016-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `ACTOR_AUTHORIZED, ACTOR_DENIED, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-017 — EP-12-003

- Criticality: `HIGH`
- Statement: Communication Matrix quyết định toàn bộ hành vi gửi Notification.
- Recommended (not selected): `P2C-SO-C2-HOMR-017-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-018 — EP-13-001

- Criticality: `CRITICAL`
- Statement: Dashboard là cửa ngõ truy cập nhanh tới Business Object. Mọi Widget đều hỗ trợ Drill-down tới dữ liệu chi tiết theo Permission.
- Recommended (not selected): `P2C-SO-C2-HOMR-018-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `ACTOR_AUTHORIZED, ACTOR_DENIED, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-019 — EP-14-010

- Criticality: `NORMAL`
- Statement: Organization được khởi tạo bằng Template nhằm giảm thời gian Onboarding.
- Recommended (not selected): `P2C-SO-C2-HOMR-019-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-020 — EP-17-001

- Criticality: `HIGH`
- Statement: Platform Operations được quản lý tập trung thông qua Platform Operations Center.
- Recommended (not selected): `P2C-SO-C2-HOMR-020-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `DELIVERY_TERMINAL_STATE, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-021 — UXF-002

- Criticality: `HIGH`
- Statement: Storefronts represent commercial experiences rather than websites.
- Recommended (not selected): `P2C-SO-C2-HOMR-021-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `STATE_TRANSITION_ALLOWED, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-022 — UXF-003

- Criticality: `HIGH`
- Statement: Storefronts consume YSim Products only.
- Recommended (not selected): `P2C-SO-C2-HOMR-022-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `STATE_TRANSITION_ALLOWED, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-023 — UXF-008

- Criticality: `HIGH`
- Statement: Localization defines customer experience, not only language.
- Recommended (not selected): `P2C-SO-C2-HOMR-023-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `STATE_TRANSITION_ALLOWED, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-024 — UXF-02-R009

- Criticality: `HIGH`
- Statement: Accessibility cannot be disabled by Themes.
- Recommended (not selected): `P2C-SO-C2-HOMR-024-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-025 — UXF-209

- Criticality: `HIGH`
- Statement: Accessibility is mandatory.
- Recommended (not selected): `P2C-SO-C2-HOMR-025-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-026 — UXF-301

- Criticality: `HIGH`
- Statement: Storefronts are runtime experiences.
- Recommended (not selected): `P2C-SO-C2-HOMR-026-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `STATE_TRANSITION_ALLOWED, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`

## P2C-SO-C2-HOMR-027 — UXF-302

- Criticality: `HIGH`
- Statement: Templates define structure only.
- Recommended (not selected): `P2C-SO-C2-HOMR-027-OPT-1`
- Option 1: `AUTHOR_SOURCE_GROUNDED_OPERATOR_AST` → `STATE_TRANSITION_ALLOWED, EVIDENCE_FIELD_PRESENT`
- Option 2: `SOURCE_SEMANTICS_BLOCKED`
