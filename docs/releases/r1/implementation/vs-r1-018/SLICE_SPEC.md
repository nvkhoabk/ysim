# VS-R1-018 Slice Specification

## Included

- Sandbox-only `getMyOrdersAgency` readback by request ID.
- Explicit provenance for documented PUT versus probed sandbox POST.
- `getOrderDetailAgency` POST readback.
- Strict envelope, record-count and array validation.
- Agency-order statuses: Pending, Completed, Cancelled, Processing.
- eSIM-detail statuses: Processing, Delivered, Recalled.
- ICCID format and duplicate validation.
- QR/LPA and short-link presence assessment.
- Expected/completed/returned/delivered/installable count checks.
- Readiness states: `PROCESSING`, `DELIVERABLE`, `ACTION_REQUIRED`.
- No raw ICCID, QR/LPA, or short-link values in runtime evidence.
- Human Review Manifest for delivery-readiness business rules.

## Delivery policy

`DELIVERABLE` requires:

- every agency order is Completed;
- completed count equals expected quantity;
- returned and Delivered detail counts equal expected quantity;
- every detail has ICCID;
- every detail has QR/LPA or short link.

Gigago Pending, Cancelled, Recalled, completed-count mismatch, delivered
count mismatch, or missing install data becomes `ACTION_REQUIRED`.
Processing remains non-terminal.

## Excluded

- No eSIM Asset persistence.
- No encrypted install-data storage.
- No automatic polling worker.
- No delivery email or customer portal.
- No live Gigago request in runtime proof.
- No production query-method assumption.
