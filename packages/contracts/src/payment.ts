import type {
  PricingCurrency,
  PricingCurrencyExponent,
} from './pricing.js';
import type {
  SalesOrderPaymentStatus,
  SalesOrderStatus,
} from './sales-order.js';

export type PaymentProvider = 'TEST' | 'GPAY';
export type PaymentIntentStatus =
  | 'CREATED'
  | 'PENDING'
  | 'SUCCEEDED'
  | 'FAILED'
  | 'EXPIRED';
export type TestPaymentEventStatus = Exclude<
  PaymentIntentStatus,
  'CREATED'
>;

export interface CreatePaymentIntentRequest {
  orderId: string;
  provider: PaymentProvider;
}

export interface PaymentIntentContract {
  id: string;
  orderId: string;
  orderNumber: string;
  provider: PaymentProvider;
  providerReference: string;
  attemptNumber: number;
  amountMinor: string;
  currency: PricingCurrency;
  currencyExponent: PricingCurrencyExponent;
  status: PaymentIntentStatus;
  createdAt: string;
  expiresAt: string;
  updatedAt: string;
  version: number;
}

export interface CreatePaymentIntentResponse {
  intent: PaymentIntentContract;
  idempotentReplay: boolean;
}

export interface GetPaymentIntentResponse {
  intent: PaymentIntentContract;
}

export interface ApplyTestPaymentEventRequest {
  eventId: string;
  status: TestPaymentEventStatus;
}

export interface ApplyTestPaymentEventResponse {
  intent: PaymentIntentContract;
  duplicateEvent: boolean;
  orderStatus: SalesOrderStatus;
  orderPaymentStatus: SalesOrderPaymentStatus;
}
