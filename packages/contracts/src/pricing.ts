export type PricingMarket = 'VN' | 'LA' | 'INTERNATIONAL';
export type PricingCurrency = 'VND' | 'LAK' | 'USD';
export type PricingChannel = 'B2C' | 'AGENCY';
export type PriceBookStatus = 'DRAFT' | 'ACTIVE' | 'SUSPENDED';
export type PricingSupplierEnvironment = 'SANDBOX' | 'PRODUCTION';
export type PricingQuoteStatus = 'ACTIVE' | 'EXPIRED';
export type PricingCurrencyExponent = 0 | 2;

export interface PriceBookContract {
  id: string;
  code: string;
  market: PricingMarket;
  currency: PricingCurrency;
  channel: PricingChannel;
  status: PriceBookStatus;
  validFrom: string;
  validTo: string;
  version: number;
  createdAt: string;
  activatedAt: string | null;
  suspendedAt: string | null;
}

export interface CreatePriceBookRequest {
  code: string;
  market: PricingMarket;
  currency: PricingCurrency;
  channel: PricingChannel;
  validFrom: string;
  validTo: string;
}

export interface CreatePriceBookResponse {
  priceBook: PriceBookContract;
}

export interface SupplierCostSnapshotContract {
  id: string;
  supplierPlanMappingId: string;
  productOfferId: string;
  supplierEnvironment: PricingSupplierEnvironment;
  currency: PricingCurrency;
  unitCostAmountMinor: string;
  observedAt: string;
  sourceSnapshotHash: string;
  createdAt: string;
}

export interface CreateSupplierCostSnapshotRequest {
  supplierPlanMappingId: string;
  currency: PricingCurrency;
  unitCostAmountMinor: string;
  observedAt: string;
  sourceSnapshotHash: string;
}

export interface CreateSupplierCostSnapshotResponse {
  costSnapshot: SupplierCostSnapshotContract;
}

export interface PriceBookEntryContract {
  id: string;
  priceBookId: string;
  productOfferId: string;
  offerCode: string;
  unitAmountMinor: string;
  supplierCostSnapshotId: string;
  version: number;
  createdAt: string;
}

export interface CreatePriceBookEntryRequest {
  productOfferId: string;
  unitAmountMinor: string;
  supplierCostSnapshotId: string;
}

export interface CreatePriceBookEntryResponse {
  entry: PriceBookEntryContract;
}

export interface PriceBookTransitionResponse {
  priceBook: PriceBookContract;
}

export interface CreatePricingQuoteRequest {
  offerCode: string;
  market: PricingMarket;
  currency: PricingCurrency;
  channel: PricingChannel;
  quantity: number;
  ttlSeconds?: number;
}

export interface PricingQuoteContract {
  id: string;
  offerCode: string;
  market: PricingMarket;
  currency: PricingCurrency;
  currencyExponent: PricingCurrencyExponent;
  channel: PricingChannel;
  unitAmountMinor: string;
  quantity: number;
  subtotalAmountMinor: string;
  totalAmountMinor: string;
  priceBookCode: string;
  priceBookVersion: number;
  priceBookEntryVersion: number;
  issuedAt: string;
  expiresAt: string;
  status: PricingQuoteStatus;
}

export interface CreatePricingQuoteResponse {
  quote: PricingQuoteContract;
}

export interface GetPricingQuoteResponse {
  quote: PricingQuoteContract;
}
