import type { PaymentProvider } from './payment.js';
import type { PricingCurrency } from './pricing.js';

export type PaymentIntegrationEventType =
  'payment.succeeded.v1';

export interface PaymentSucceededIntegrationPayloadV1 {
  paymentIntentId: string;
  orderId: string;
  orderNumber: string;
  provider: PaymentProvider;
  providerReference: string;
  amountMinor: string;
  currency: PricingCurrency;
  occurredAt: string;
}

export interface PaymentSucceededIntegrationEventV1 {
  eventId: string;
  eventType: PaymentIntegrationEventType;
  aggregateType: 'PaymentIntent';
  aggregateId: string;
  orderId: string;
  deduplicationKey: string;
  payload: PaymentSucceededIntegrationPayloadV1;
  occurredAt: string;
}
