import type { PricingCurrency } from './pricing.js';
import type {
  PaymentIntentStatus,
  TestPaymentEventStatus,
} from './payment.js';
import type {
  SalesOrderPaymentStatus,
  SalesOrderStatus,
} from './sales-order.js';

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

export interface ApplyGPayWebhookResponse {
  accepted: true;
  duplicateEvent: boolean;
  paymentIntentId: string;
  paymentIntentStatus: PaymentIntentStatus;
  orderStatus: SalesOrderStatus;
  orderPaymentStatus: SalesOrderPaymentStatus;
}
