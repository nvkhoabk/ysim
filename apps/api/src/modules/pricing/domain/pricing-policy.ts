import type {
  PricingChannel,
  PricingCurrency,
  PricingCurrencyExponent,
  PricingMarket,
  PricingQuoteStatus,
  PricingSupplierEnvironment,
} from '@ysim/contracts';

export class PricingPolicyError extends Error {}

const codePattern = /^[A-Z][A-Z0-9_-]{2,63}$/u;
const uuidPattern =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;
const hashPattern = /^[0-9a-f]{64}$/u;
const moneyPattern = /^[1-9][0-9]{0,17}$/u;

const expectedCurrencyByMarket: Record<
  PricingMarket,
  PricingCurrency
> = {
  VN: 'VND',
  LA: 'LAK',
  INTERNATIONAL: 'USD',
};

export function normalizePricingCode(
  value: unknown,
  field: string,
): string {
  if (typeof value !== 'string') {
    throw new PricingPolicyError(`${field} must be a string`);
  }

  const normalized = value.trim().toUpperCase();
  if (!codePattern.test(normalized)) {
    throw new PricingPolicyError(
      `${field} must match ${codePattern.source}`,
    );
  }

  return normalized;
}

export function requireUuid(value: unknown, field: string): string {
  if (typeof value !== 'string' || !uuidPattern.test(value)) {
    throw new PricingPolicyError(`${field} must be a UUID`);
  }

  return value.toLowerCase();
}

export function requirePricingMarket(value: unknown): PricingMarket {
  if (value === 'VN' || value === 'LA' || value === 'INTERNATIONAL') {
    return value;
  }

  throw new PricingPolicyError('market is not supported');
}

export function requirePricingCurrency(
  value: unknown,
): PricingCurrency {
  if (value === 'VND' || value === 'LAK' || value === 'USD') {
    return value;
  }

  throw new PricingPolicyError('currency is not supported');
}

export function requirePricingChannel(value: unknown): PricingChannel {
  if (value === 'B2C' || value === 'AGENCY') {
    return value;
  }

  throw new PricingPolicyError('channel is not supported');
}

export function requireSupplierEnvironment(
  value: unknown,
): PricingSupplierEnvironment {
  if (value === 'SANDBOX' || value === 'PRODUCTION') {
    return value;
  }

  throw new PricingPolicyError(
    'supplier environment must be SANDBOX or PRODUCTION',
  );
}

export function requireMarketCurrencyPair(
  marketValue: unknown,
  currencyValue: unknown,
): {
  market: PricingMarket;
  currency: PricingCurrency;
} {
  const market = requirePricingMarket(marketValue);
  const currency = requirePricingCurrency(currencyValue);

  if (expectedCurrencyByMarket[market] !== currency) {
    throw new PricingPolicyError(
      `${market} price books must use ${expectedCurrencyByMarket[market]}`,
    );
  }

  return { market, currency };
}

export function currencyExponent(
  currency: PricingCurrency,
): PricingCurrencyExponent {
  return currency === 'USD' ? 2 : 0;
}

export function requireMoneyMinor(
  value: unknown,
  field: string,
): string {
  if (typeof value !== 'string' || !moneyPattern.test(value)) {
    throw new PricingPolicyError(
      `${field} must be a positive integer string with at most 18 digits`,
    );
  }

  return BigInt(value).toString();
}

export function requireQuantity(value: unknown): number {
  if (!Number.isInteger(value) || Number(value) < 1 || Number(value) > 20) {
    throw new PricingPolicyError(
      'quantity must be an integer between 1 and 20',
    );
  }

  return Number(value);
}

export function requireQuoteTtlSeconds(value: unknown): number {
  if (value === undefined) return 600;

  if (!Number.isInteger(value) || Number(value) < 1 || Number(value) > 900) {
    throw new PricingPolicyError(
      'ttlSeconds must be an integer between 1 and 900',
    );
  }

  return Number(value);
}

export function requireIsoTimestamp(
  value: unknown,
  field: string,
): string {
  if (typeof value !== 'string') {
    throw new PricingPolicyError(`${field} must be an ISO timestamp`);
  }

  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    throw new PricingPolicyError(`${field} must be an ISO timestamp`);
  }

  return date.toISOString();
}

export function requireEffectivePeriod(
  validFromValue: unknown,
  validToValue: unknown,
): { validFrom: string; validTo: string } {
  const validFrom = requireIsoTimestamp(validFromValue, 'validFrom');
  const validTo = requireIsoTimestamp(validToValue, 'validTo');
  const fromMs = Date.parse(validFrom);
  const toMs = Date.parse(validTo);

  if (toMs <= fromMs) {
    throw new PricingPolicyError('validTo must be later than validFrom');
  }

  if (toMs - fromMs > 10 * 365 * 24 * 60 * 60 * 1000) {
    throw new PricingPolicyError(
      'price-book effective period cannot exceed 10 years',
    );
  }

  return { validFrom, validTo };
}

export function requireSnapshotHash(value: unknown): string {
  if (typeof value !== 'string' || !hashPattern.test(value)) {
    throw new PricingPolicyError(
      'sourceSnapshotHash must be a lowercase SHA-256 hash',
    );
  }

  return value;
}

export function calculateQuoteAmounts(
  unitAmountMinor: string,
  quantity: number,
): {
  subtotalAmountMinor: string;
  totalAmountMinor: string;
} {
  const normalizedUnit = requireMoneyMinor(
    unitAmountMinor,
    'unitAmountMinor',
  );
  const normalizedQuantity = requireQuantity(quantity);
  const total = BigInt(normalizedUnit) * BigInt(normalizedQuantity);

  return {
    subtotalAmountMinor: total.toString(),
    totalAmountMinor: total.toString(),
  };
}

export function resolveQuoteExpiration(
  issuedAtValue: string,
  ttlSeconds: number,
  priceBookValidToValue: string,
): string {
  const issuedAt = requireIsoTimestamp(issuedAtValue, 'issuedAt');
  const priceBookValidTo = requireIsoTimestamp(
    priceBookValidToValue,
    'priceBookValidTo',
  );
  const requestedExpiry =
    Date.parse(issuedAt) + requireQuoteTtlSeconds(ttlSeconds) * 1000;
  const expiresAt = Math.min(
    requestedExpiry,
    Date.parse(priceBookValidTo),
  );

  if (expiresAt <= Date.parse(issuedAt)) {
    throw new PricingPolicyError(
      'price book expires before the quote can be issued',
    );
  }

  return new Date(expiresAt).toISOString();
}

export function quoteStatus(
  expiresAtValue: string,
  nowValue = new Date().toISOString(),
): PricingQuoteStatus {
  const expiresAt = requireIsoTimestamp(expiresAtValue, 'expiresAt');
  const now = requireIsoTimestamp(nowValue, 'now');

  return Date.parse(now) >= Date.parse(expiresAt)
    ? 'EXPIRED'
    : 'ACTIVE';
}
