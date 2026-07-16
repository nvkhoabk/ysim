# Operator Binding Source Clarification Decision Pack

- Candidate: `V23-P2C-OPERATOR-BINDING-TYPE-MODEL-C1`
- All decisions: `PENDING_HUMAN_APPROVAL`

## P2C-OBT-C1-DEC-BD-05-009 — BD-05-009

What approval and lifecycle govern a Price Change Set?

Recommended: `OPT-1`

### P2C-OBT-C1-BD-05-009-OPT-1

- Meaning: A Price Change Set follows DRAFT, SUBMITTED, APPROVED, REJECTED and EFFECTIVE states; only a valid APPROVED set may change a Price Book.
- Exact proposed wording: Price Book chỉ được thay đổi bởi Price Change Set có trạng thái APPROVED còn hiệu lực. Price Change Set phải đi qua DRAFT, SUBMITTED, APPROVED hoặc REJECTED; approver, quyết định, thời điểm và policy version phải được ghi nhận.
- Consequence: Requires versioned approval policy and approval evidence before effectiveness.

### P2C-OBT-C1-BD-05-009-OPT-2

- Meaning: Price Change Set requires deterministic validation and publication but no human approval.
- Exact proposed wording: Price Book chỉ được thay đổi bởi Price Change Set đã vượt qua validation và được publish; v2.3 không yêu cầu human approval trừ khi policy riêng quy định.
- Consequence: Removes universal approval; policy-specific approval remains possible.

- Resulting operators: APPROVAL_REQUIRED, STATE_TRANSITION_ALLOWED, EVIDENCE_FIELD_PRESENT
- Criticality: CRITICAL
- Runtime impact: Price lifecycle, approval service and effective-state gate.
- Non-inferences: No approver role is inferred.; No SLA is inferred.

## P2C-OBT-C1-DEC-BRD-WS-02-R003 — BRD-WS-02-R003

What is the authoritative eSIM capability set and resolution rule?

Recommended: `OPT-1`

### P2C-OBT-C1-BRD-WS-02-R003-OPT-1

- Meaning: A versioned eSIM Capability Registry is canonical; Product Specification declarations equal independently resolved operational capabilities.
- Exact proposed wording: Product Specification phải khai báo các eSIM Capability bằng ID trong eSIM Capability Registry có version. Tập capability khai báo phải khớp tập capability được resolver xác định độc lập từ profile/provider và policy đang hiệu lực.
- Consequence: Creates canonical registry and two independent resolvers.

### P2C-OBT-C1-BRD-WS-02-R003-OPT-2

- Meaning: Each provider owns a versioned capability schema mapped to a common YSim capability taxonomy.
- Exact proposed wording: Khả năng eSIM thực tế được xác định theo provider capability schema có version và được map sang YSim capability taxonomy trước khi đối chiếu Product Specification.
- Consequence: Adds provider mapping and reconciliation complexity.

- Resulting operators: SET_EQUALS, REFERENCE_TARGET_VALID, EVIDENCE_FIELD_PRESENT
- Criticality: HIGH
- Runtime impact: Capability registry, provider resolver and validation evidence.
- Non-inferences: No capability members are invented.; No provider schema is assumed.

## P2C-OBT-C1-DEC-BRD-WS-07-R005 — BRD-WS-07-R005

What approval and lifecycle govern Identity merge?

Recommended: `OPT-1`

### P2C-OBT-C1-BRD-WS-07-R005-OPT-1

- Meaning: Merge is a governed proposal requiring approval; no automatic merge.
- Exact proposed wording: Identity Merge phải được tạo dưới dạng Merge Proposal, được authorized reviewer APPROVE hoặc REJECT, và chỉ proposal APPROVED mới được áp dụng. Source identities, canonical target, reason, decision và audit evidence phải được giữ lại.
- Consequence: Requires merge proposal, authorization and audit lifecycle.

### P2C-OBT-C1-BRD-WS-07-R005-OPT-2

- Meaning: Identity merge is deferred; v2.3 only records possible links.
- Exact proposed wording: V2.3 không thực hiện Identity Merge; Platform chỉ ghi nhận possible-duplicate linkage để review trong baseline tương lai.
- Consequence: No active merge workflow; duplicate resolution remains deferred.

- Resulting operators: APPROVAL_REQUIRED, STATE_TRANSITION_ALLOWED, AUDIT_IMMUTABLE
- Criticality: CRITICAL
- Runtime impact: Identity merge workflow or deferred-link store.
- Non-inferences: No automatic matching threshold is inferred.; No legal identity consolidation is inferred.

## P2C-OBT-C1-DEC-EP-08-006 — EP-08-006

Does v2.3 define a universal payment retry limit?

Recommended: `OPT-1`

### P2C-OBT-C1-EP-08-006-OPT-1

- Meaning: No universal numeric limit is asserted here; every retry creates a new PaymentAttempt and any limit comes from versioned payment policy.
- Exact proposed wording: Mỗi lần retry phải tạo PaymentAttempt mới. Retry limit, nếu áp dụng, phải được lấy từ Payment Retry Policy có version; requirement này không quy định một limit cố định.
- Consequence: Removes unsupported value 3 and requires policy-driven limits.

### P2C-OBT-C1-EP-08-006-OPT-2

- Meaning: A universal maximum of three attempts is normative.
- Exact proposed wording: Mỗi lần retry phải tạo PaymentAttempt mới và tổng số PaymentAttempt cho một PaymentSession không được vượt quá 3 trước terminal failure.
- Consequence: Introduces an explicit global limit of three.

- Resulting operators: REFERENCE_TARGET_VALID, RETRY_LIMIT_NOT_EXCEEDED
- Criticality: CRITICAL
- Runtime impact: PaymentAttempt identity and policy-based or fixed retry enforcement.
- Non-inferences: The value 3 is not retained unless OPT-2 is selected.; No gateway retry topology is inferred.

## P2C-OBT-C1-DEC-EP-17-002 — EP-17-002

What inventory and signals define Platform monitoring coverage?

Recommended: `OPT-1`

### P2C-OBT-C1-EP-17-002-OPT-1

- Meaning: A versioned Platform Component Inventory and component-class signal profile are authoritative.
- Exact proposed wording: Monitoring coverage phải được đối chiếu với Platform Component Inventory có version. Mỗi active component phải có các mandatory signals theo component-class Monitoring Profile; inventory IDs và observed signal evidence phải được resolve độc lập.
- Consequence: Defines canonical inventory and mandatory signal profiles.

### P2C-OBT-C1-EP-17-002-OPT-2

- Meaning: Only critical Platform components require mandatory signal coverage in v2.3.
- Exact proposed wording: V2.3 bắt buộc monitoring signal coverage cho các Platform component được phân loại CRITICAL; coverage cho component khác theo approved monitoring policy.
- Consequence: Narrows the original whole-Platform obligation.

- Resulting operators: SET_EQUALS, EVIDENCE_FIELD_PRESENT
- Criticality: HIGH
- Runtime impact: Component inventory, signal profiles and coverage reconciliation.
- Non-inferences: No component or signal list is invented.; External dependencies are not automatically Platform components.

## P2C-OBT-C1-DEC-UXF-405 — UXF-405

What governed precedence resolves inherited Organization and Storefront configuration?

Recommended: `OPT-1`

### P2C-OBT-C1-UXF-405-OPT-1

- Meaning: Platform/security invariants override jurisdiction/market, then Organization, then Storefront configuration.
- Exact proposed wording: Storefront kế thừa Organization configuration. Effective configuration được resolve theo thứ tự: Platform và Security Invariants; Jurisdiction/Market policy; Organization; Storefront. Override chỉ hợp lệ tại layer được policy cho phép và phải versioned, observable, auditable.
- Consequence: Defines a fixed governed precedence and override boundary.

### P2C-OBT-C1-UXF-405-OPT-2

- Meaning: Organization supplies defaults and Storefront overrides them except immutable platform/security invariants.
- Exact proposed wording: Storefront kế thừa Organization defaults và có thể override các key được phép; Platform/Security invariants không thể bị override. Effective source và version phải observable và auditable.
- Consequence: Leaves jurisdiction/market precedence to separate policy.

- Resulting operators: CONFIGURATION_PRECEDENCE, CONFIGURATION_RESOLVES, EVIDENCE_FIELD_PRESENT
- Criticality: HIGH
- Runtime impact: Versioned configuration layers, resolver and effective-source evidence.
- Non-inferences: No configuration keys are invented.; No override is allowed unless its layer policy permits it.
