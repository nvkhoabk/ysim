# VS-R1-016 — Gigago Sandbox Create-Order Adapter Boundary and Contract Harness

Status: Proposed candidate.

This slice implements the sandbox-only Gigago create-order boundary using the
accepted contract: `apiKey`, `PUT /api/partner/createPartnerOrder`,
`request_id + orders + metadata`, and normalized response `extra`.

No real Gigago request is executed during runtime proof.

The adapter is deliberately not registered as a Nest provider in this slice. Activation requires a later configuration and persistence slice.
