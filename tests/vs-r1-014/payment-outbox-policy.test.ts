import {
  describe,
  expect,
  it,
} from 'vitest';

import {
  loadPaymentOutboxLeaseSeconds,
  parseClaimedPaymentIntegrationEvent,
  PaymentOutboxPolicyError,
  paymentOutboxLeaseUntil,
  paymentOutboxRetryAt,
  sanitizePaymentOutboxError,
  type ClaimedPaymentIntegrationOutboxRecord,
} from '../../apps/api/src/modules/payment/domain/payment-outbox-policy.js';

const occurredAt =
  '2026-07-30T10:00:00.000Z';
const record:
  ClaimedPaymentIntegrationOutboxRecord = {
    id: '10000000-0000-4000-8000-000000000014',
    eventType: 'payment.succeeded.v1',
    aggregateType: 'PaymentIntent',
    aggregateId:
      '20000000-0000-4000-8000-000000000014',
    orderId:
      '30000000-0000-4000-8000-000000000014',
    deduplicationKey: 'a'.repeat(64),
    payload: {
      paymentIntentId:
        '20000000-0000-4000-8000-000000000014',
      orderId:
        '30000000-0000-4000-8000-000000000014',
      orderNumber:
        'YS-20260730-014ABCDEF014',
      provider: 'GPAY',
      providerReference:
        'GPY-20000000000040008000000000000014',
      amountMinor: '338000',
      currency: 'VND',
      occurredAt,
    },
    occurredAt,
    attemptCount: 1,
  };

describe('Payment outbox policy', () => {
  it('uses a thirty-second default lease', () => {
    expect(
      loadPaymentOutboxLeaseSeconds({}),
    ).toBe(30);
  });

  it('accepts a bounded configured lease', () => {
    expect(
      loadPaymentOutboxLeaseSeconds({
        YSIM_PAYMENT_OUTBOX_LEASE_SECONDS:
          '60',
      }),
    ).toBe(60);
  });

  it('rejects an unsafe lease duration', () => {
    expect(() =>
      loadPaymentOutboxLeaseSeconds({
        YSIM_PAYMENT_OUTBOX_LEASE_SECONDS:
          '2',
      }),
    ).toThrow(PaymentOutboxPolicyError);
  });

  it('derives a deterministic lease expiry', () => {
    expect(
      paymentOutboxLeaseUntil(
        occurredAt,
        30,
      ),
    ).toBe('2026-07-30T10:00:30.000Z');
  });

  it('uses a five-second first retry', () => {
    expect(
      paymentOutboxRetryAt(
        occurredAt,
        1,
      ),
    ).toBe('2026-07-30T10:00:05.000Z');
  });

  it('uses exponential retry growth', () => {
    expect(
      paymentOutboxRetryAt(
        occurredAt,
        4,
      ),
    ).toBe('2026-07-30T10:00:40.000Z');
  });

  it('caps retries at fifteen minutes', () => {
    expect(
      paymentOutboxRetryAt(
        occurredAt,
        20,
      ),
    ).toBe('2026-07-30T10:15:00.000Z');
  });

  it('redacts secrets and control characters', () => {
    const safe = sanitizePaymentOutboxError(
      new Error(
        'Bearer abc.def token=secret-value\nfailed',
      ),
    );
    expect(safe).toContain(
      'Bearer [REDACTED]',
    );
    expect(safe).toContain(
      'token=[REDACTED]',
    );
    expect(safe).not.toContain(
      'secret-value',
    );
    expect(safe).not.toContain('\n');
  });

  it('parses an accepted Payment Success event', () => {
    const event =
      parseClaimedPaymentIntegrationEvent(
        record,
      );
    expect(event.eventId).toBe(record.id);
    expect(event.payload.provider).toBe(
      'GPAY',
    );
    expect(event.payload.amountMinor).toBe(
      '338000',
    );
  });

  it('rejects an unsafe or mismatched payload', () => {
    expect(() =>
      parseClaimedPaymentIntegrationEvent({
        ...record,
        payload: {
          ...(record.payload as object),
          customerEmail:
            'customer@example.com',
        },
      }),
    ).toThrow(PaymentOutboxPolicyError);
  });
});
