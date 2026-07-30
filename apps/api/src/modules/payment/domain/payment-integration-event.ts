import { createHash } from 'node:crypto';

import type {
  PaymentProvider,
  PaymentSucceededIntegrationEventV1,
  PricingCurrency,
} from '@ysim/contracts';

const sha256 = (value: string): string =>
  createHash('sha256')
    .update(value, 'utf8')
    .digest('hex');

export interface CreatePaymentSucceededIntegrationEventInput {
  eventId: string;
  paymentIntentId: string;
  orderId: string;
  orderNumber: string;
  provider: PaymentProvider;
  providerReference: string;
  amountMinor: string;
  currency: PricingCurrency;
  occurredAt: string;
}

export const createPaymentSucceededIntegrationEvent = (
  input: CreatePaymentSucceededIntegrationEventInput,
): PaymentSucceededIntegrationEventV1 => {
  const eventType = 'payment.succeeded.v1' as const;
  const deduplicationKey = sha256(
    `${eventType}:${input.paymentIntentId}`,
  );

  return {
    eventId: input.eventId,
    eventType,
    aggregateType: 'PaymentIntent',
    aggregateId: input.paymentIntentId,
    orderId: input.orderId,
    deduplicationKey,
    payload: {
      paymentIntentId: input.paymentIntentId,
      orderId: input.orderId,
      orderNumber: input.orderNumber,
      provider: input.provider,
      providerReference: input.providerReference,
      amountMinor: input.amountMinor,
      currency: input.currency,
      occurredAt: input.occurredAt,
    },
    occurredAt: input.occurredAt,
  };
};
