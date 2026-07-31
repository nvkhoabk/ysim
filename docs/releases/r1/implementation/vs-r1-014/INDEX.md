# VS-R1-014 — Payment Integration Outbox Publisher and Retry Policy

Status: Proposed candidate.

This slice turns the accepted Payment Success outbox into a safely
claimable and publishable background-work boundary.

It provides one-event publication, bounded leases, retry scheduling,
stale-attempt protection and sanitized failure evidence. It does not
schedule a worker automatically and does not call Gigago.
