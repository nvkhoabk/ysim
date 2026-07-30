# VS-R1-009 — Slice Specification

## Purpose

Establish a provider-specific GPay adapter boundary and executable signed-transport harness before enabling GPay commercial payment traffic.

## Executable outcome

A protected internal API can execute the YSim-normalized `GATEWAY_V1` signed contract harness against a loopback or explicitly approved sandbox test endpoint and verify the signed response without exposing key, certificate, signature or provider payload material.

## Scope

- Sandbox-only GPay adapter configuration.
- YSim-normalized signed transport harness; no claim that GPay publishes `/contract/probe`.
- Explicit `UNVERIFIED` versus `PROBED` contract status.
- RSA-SHA256 request signing.
- Provider response-signature verification.
- Merchant private-key and certificate/public-key coherence check.
- HTTPS enforcement, except loopback runtime fixtures.
- Timeout and response-identity validation.
- Protected internal probe endpoint.
- Safe boolean/label evidence only.
- Production activation block.

## Non-scope

- No `PaymentProvider = GPAY` commercial intent creation.
- No customer redirect or QR action.
- No live GPay order initialization.
- No GPay payment webhook business effect.
- No refund or reconciliation worker.
- No procurement or fulfillment.
- No database migration.
- No secrets or certificates in source control.

## Security rules

- Private keys and certificates are loaded only from absolute server-side paths.
- Raw signatures, key material and certificate contents are never returned by the API.
- Production is blocked in this slice even when configuration values are present.
- Non-loopback HTTP endpoints are rejected.
- Probe request and response identifiers must match exactly.

## Follow-on

A later slice may bind the adapter to confirmed GPay sandbox initialization/query/webhook endpoints only after this harness is accepted and the actual provider contract is reviewed.
