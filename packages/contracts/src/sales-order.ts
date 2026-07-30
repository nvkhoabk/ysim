import type {
  PricingChannel,
  PricingCurrency,
  PricingCurrencyExponent,
  PricingMarket,
} from './pricing.js';

export type SalesOrderLocale = 'en' | 'vi' | 'lo';
export type SalesOrderSource = 'STOREFRONT';
export type SalesOrderStatus =
  | 'PENDING_PAYMENT'
  | 'CONFIRMED'
  | 'CANCELLED';
export type SalesOrderPaymentStatus =
  | 'UNPAID'
  | 'PAID'
  | 'FAILED'
  | 'REFUNDED';
export type SalesOrderFulfillmentStatus =
  | 'UNFULFILLED'
  | 'PROCESSING'
  | 'FULFILLED'
  | 'FAILED';

export interface CreateSalesOrderRequest {
  quoteId: string;
  customerName: string;
  customerEmail: string;
  recipientEmail?: string;
  locale?: SalesOrderLocale;
}

export interface SalesOrderContract {
  id: string;
  orderNumber: string;
  quoteId: string;
  offerCode: string;
  market: PricingMarket;
  currency: PricingCurrency;
  currencyExponent: PricingCurrencyExponent;
  channel: PricingChannel;
  unitAmountMinor: string;
  quantity: number;
  subtotalAmountMinor: string;
  totalAmountMinor: string;
  status: SalesOrderStatus;
  paymentStatus: SalesOrderPaymentStatus;
  fulfillmentStatus: SalesOrderFulfillmentStatus;
  source: SalesOrderSource;
  customerName: string;
  customerEmail: string;
  recipientEmail: string;
  locale: SalesOrderLocale;
  quoteIssuedAt: string;
  quoteExpiresAt: string;
  createdAt: string;
  version: number;
}

export interface CreateSalesOrderResponse {
  order: SalesOrderContract;
  orderAccessToken: string;
  idempotentReplay: boolean;
}

export interface GetSalesOrderResponse {
  order: SalesOrderContract;
}
