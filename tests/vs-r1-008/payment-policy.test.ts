import { describe, expect, it } from 'vitest';

import {
  createPaymentEventFingerprint,
  createPaymentRequestFingerprint,
  derivePaymentIntentExpiry,
  deriveTestProviderReference,
  normalizePaymentIdempotencyKey,
  normalizeTestPaymentEventId,
  paymentCurrencyExponent,
  PaymentPolicyError,
  requirePaymentAccessToken,
  requirePaymentProvider,
  requirePaymentUuid,
  requireTestPaymentEventStatus,
  resolvePaymentTransition,
  sha256PaymentValue,
} from '../../apps/api/src/modules/payment/domain/payment-policy.js';

const uuid = '1458c5f0-21ad-4e75-9ec6-0a9641e81866';

describe('payment policy', () => {
  it('normalizes stable idempotency keys', () => {
    expect(normalizePaymentIdempotencyKey(
      '  payment-checkout-0001  ',
    )).toBe('payment-checkout-0001');
  });

  it('rejects short idempotency keys', () => {
    expect(() => normalizePaymentIdempotencyKey('short'))
      .toThrow(PaymentPolicyError);
  });

  it('requires a protected order access token', () => {
    expect(requirePaymentAccessToken('x'.repeat(43)))
      .toHaveLength(43);
    expect(() => requirePaymentAccessToken('short'))
      .toThrow(PaymentPolicyError);
  });

  it('accepts only the normalized test provider', () => {
    expect(requirePaymentProvider('TEST')).toBe('TEST');
    expect(() => requirePaymentProvider('GPAY'))
      .toThrow(PaymentPolicyError);
  });

  it('normalizes provider event identifiers', () => {
    expect(normalizeTestPaymentEventId(
      ' test:event-0001 ',
    )).toBe('test:event-0001');
  });

  it('rejects unstable provider event identifiers', () => {
    expect(() => normalizeTestPaymentEventId('bad id'))
      .toThrow(PaymentPolicyError);
  });

  it('accepts normalized provider statuses', () => {
    expect(requireTestPaymentEventStatus('PENDING'))
      .toBe('PENDING');
    expect(requireTestPaymentEventStatus('SUCCEEDED'))
      .toBe('SUCCEEDED');
  });

  it('rejects unsupported provider statuses', () => {
    expect(() => requireTestPaymentEventStatus('CREATED'))
      .toThrow(PaymentPolicyError);
  });

  it('normalizes UUIDs', () => {
    expect(requirePaymentUuid(uuid.toUpperCase(), 'id'))
      .toBe(uuid);
  });

  it('hashes sensitive values without storing the raw value', () => {
    const raw = 'payment-checkout-0001';
    const hash = sha256PaymentValue(raw);
    expect(hash).toMatch(/^[0-9a-f]{64}$/u);
    expect(hash).not.toBe(raw);
  });

  it('creates stable request fingerprints', () => {
    const input = { orderId: uuid, provider: 'TEST' as const };
    expect(createPaymentRequestFingerprint(input))
      .toBe(createPaymentRequestFingerprint(input));
  });

  it('creates event fingerprints from intent event and status', () => {
    expect(createPaymentEventFingerprint({
      intentId: uuid,
      eventId: 'test:event-0001',
      status: 'PENDING',
    })).not.toBe(createPaymentEventFingerprint({
      intentId: uuid,
      eventId: 'test:event-0001',
      status: 'SUCCEEDED',
    }));
  });

  it('derives an opaque normalized provider reference', () => {
    expect(deriveTestProviderReference(uuid))
      .toBe('TST-1458C5F021AD4E759EC60A96');
  });

  it('derives a fifteen-minute provider expiry', () => {
    expect(derivePaymentIntentExpiry(
      '2026-07-30T08:00:00.000Z',
    )).toBe('2026-07-30T08:15:00.000Z');
  });

  it('moves created and pending intents through controlled states', () => {
    expect(resolvePaymentTransition('CREATED', 'PENDING'))
      .toBe('PENDING');
    expect(resolvePaymentTransition('PENDING', 'SUCCEEDED'))
      .toBe('SUCCEEDED');
  });

  it('treats the same normalized state as a no-op', () => {
    expect(resolvePaymentTransition('PENDING', 'PENDING'))
      .toBe('PENDING');
  });

  it('rejects transitions from terminal states', () => {
    expect(() => resolvePaymentTransition(
      'SUCCEEDED',
      'FAILED',
    )).toThrow(PaymentPolicyError);
  });

  it('uses accepted currency exponents', () => {
    expect(paymentCurrencyExponent('VND')).toBe(0);
    expect(paymentCurrencyExponent('LAK')).toBe(0);
    expect(paymentCurrencyExponent('USD')).toBe(2);
  });
});
