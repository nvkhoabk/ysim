import { describe, expect, it } from 'vitest';

import { createPaymentSucceededIntegrationEvent } from '../../apps/api/src/modules/payment/domain/payment-integration-event.js';

const input = {
  eventId: '1458c5f0-21ad-4e75-9ec6-0a9641e81866',
  paymentIntentId:
    '2458c5f0-21ad-4e75-9ec6-0a9641e81866',
  orderId: '3458c5f0-21ad-4e75-9ec6-0a9641e81866',
  orderNumber: 'YS-20260730-013ABCDEF013',
  provider: 'GPAY' as const,
  providerReference:
    'GPY-2458C5F021AD4E759EC60A9641E81866',
  amountMinor: '338000',
  currency: 'VND' as const,
  occurredAt: '2026-07-30T16:30:00.000Z',
};

describe('Payment Success integration event', () => {
  it('uses the versioned event type', () => {
    expect(
      createPaymentSucceededIntegrationEvent(input)
        .eventType,
    ).toBe('payment.succeeded.v1');
  });

  it('uses PaymentIntent as aggregate type', () => {
    expect(
      createPaymentSucceededIntegrationEvent(input)
        .aggregateType,
    ).toBe('PaymentIntent');
  });

  it('uses the Payment Intent as aggregate identity', () => {
    expect(
      createPaymentSucceededIntegrationEvent(input)
        .aggregateId,
    ).toBe(input.paymentIntentId);
  });

  it('creates a deterministic deduplication key', () => {
    const first =
      createPaymentSucceededIntegrationEvent(input);
    const second =
      createPaymentSucceededIntegrationEvent({
        ...input,
        eventId:
          '4458c5f0-21ad-4e75-9ec6-0a9641e81866',
      });
    expect(first.deduplicationKey).toBe(
      second.deduplicationKey,
    );
  });

  it('uses a lowercase SHA-256 deduplication key', () => {
    expect(
      createPaymentSucceededIntegrationEvent(input)
        .deduplicationKey,
    ).toMatch(/^[0-9a-f]{64}$/u);
  });

  it('changes deduplication for another Payment Intent', () => {
    const first =
      createPaymentSucceededIntegrationEvent(input);
    const second =
      createPaymentSucceededIntegrationEvent({
        ...input,
        paymentIntentId:
          '5458c5f0-21ad-4e75-9ec6-0a9641e81866',
      });
    expect(first.deduplicationKey).not.toBe(
      second.deduplicationKey,
    );
  });

  it('contains the immutable commercial snapshot', () => {
    const event =
      createPaymentSucceededIntegrationEvent(input);
    expect(event.payload).toEqual({
      paymentIntentId: input.paymentIntentId,
      orderId: input.orderId,
      orderNumber: input.orderNumber,
      provider: 'GPAY',
      providerReference: input.providerReference,
      amountMinor: '338000',
      currency: 'VND',
      occurredAt: input.occurredAt,
    });
  });

  it('contains only approved top-level fields', () => {
    expect(
      Object.keys(
        createPaymentSucceededIntegrationEvent(input),
      ).sort(),
    ).toEqual([
      'aggregateId',
      'aggregateType',
      'deduplicationKey',
      'eventId',
      'eventType',
      'occurredAt',
      'orderId',
      'payload',
    ]);
  });

  it('does not expose customer or secret material', () => {
    expect(
      JSON.stringify(
        createPaymentSucceededIntegrationEvent(input),
      ),
    ).not.toMatch(
      /email|access.?token|private|certificate|signature|secret/iu,
    );
  });

  it('preserves the trusted occurrence timestamp', () => {
    expect(
      createPaymentSucceededIntegrationEvent(input)
        .occurredAt,
    ).toBe(input.occurredAt);
  });
});
