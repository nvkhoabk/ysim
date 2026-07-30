# VS-R1-012 — GPay Payment Intent Reservation and Provider Routing

Status: Proposed candidate.

This slice enables normalized `GPAY` Payment Intent creation without
inventing or calling a live GPay checkout API.

It adds a sandbox-only GPay reservation adapter, routes Payment Intent
creation by normalized provider, preserves TEST-provider behavior and
proves that the resulting `GPY-...` reference can be completed through
the already accepted signed webhook application path.
