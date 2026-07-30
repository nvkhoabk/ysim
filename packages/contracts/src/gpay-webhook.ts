import type { PricingCurrency } from './pricing.js';
import type { TestPaymentEventStatus } from './payment.js';

export type GPayWebhookStatus =
  | 'PENDING'
  | 'SUCCESS'
  | 'FAILED'
  | 'EXPIRED';

export interface GPayWebhookBody {
  providerReference: string;
  status: GPayWebhookStatus;
  amountMinor: string;
  currency: PricingCurrency;
  occurredAt: string;
}

export interface VerifiedGPayWebhookContract {
  eventId: string;
  providerReference: string;
  normalizedStatus: TestPaymentEventStatus;
  amountMinor: string;
  currency: PricingCurrency;
  occurredAt: string;
  actorIdentityId: string;
}
