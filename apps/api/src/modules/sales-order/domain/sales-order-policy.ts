import {
  createHash,
  createHmac,
  timingSafeEqual,
} from 'node:crypto';

import type {
  PricingChannel,
  PricingCurrency,
  PricingCurrencyExponent,
  SalesOrderLocale,
} from '@ysim/contracts';

export class SalesOrderPolicyError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'SalesOrderPolicyError';
  }
}

const uuidPattern =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;
const idempotencyPattern = /^[A-Za-z0-9._:-]{16,128}$/u;
const emailPattern =
  /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/u;

export function requireUuid(
  value: unknown,
  fieldName: string,
): string {
  if (typeof value !== 'string' || !uuidPattern.test(value)) {
    throw new SalesOrderPolicyError(
      `${fieldName} must be a valid UUID`,
    );
  }

  return value.toLowerCase();
}

export function normalizeIdempotencyKey(
  value: unknown,
): string {
  if (typeof value !== 'string') {
    throw new SalesOrderPolicyError(
      'Idempotency-Key header is required',
    );
  }

  const normalized = value.trim();
  if (!idempotencyPattern.test(normalized)) {
    throw new SalesOrderPolicyError(
      'Idempotency-Key must contain 16-128 stable characters',
    );
  }

  return normalized;
}

export function normalizeCustomerName(
  value: unknown,
): string {
  if (typeof value !== 'string') {
    throw new SalesOrderPolicyError(
      'customerName is required',
    );
  }

  const normalized = value.trim().replace(/\s+/gu, ' ');
  if (
    normalized.length < 2 ||
    normalized.length > 120 ||
    /[\u0000-\u001f\u007f]/u.test(normalized)
  ) {
    throw new SalesOrderPolicyError(
      'customerName must contain 2-120 printable characters',
    );
  }

  return normalized;
}

export function normalizeEmail(
  value: unknown,
  fieldName: string,
): string {
  if (typeof value !== 'string') {
    throw new SalesOrderPolicyError(
      `${fieldName} is required`,
    );
  }

  const normalized = value.trim().toLowerCase();
  if (
    normalized.length > 254 ||
    !emailPattern.test(normalized)
  ) {
    throw new SalesOrderPolicyError(
      `${fieldName} must be a valid email address`,
    );
  }

  return normalized;
}

export function resolveRecipientEmail(
  value: unknown,
  customerEmail: string,
): string {
  if (value === undefined || value === null || value === '') {
    return customerEmail;
  }

  return normalizeEmail(value, 'recipientEmail');
}

export function requireSalesOrderLocale(
  value: unknown,
): SalesOrderLocale {
  if (value === undefined || value === null || value === '') {
    return 'en';
  }

  if (value === 'en' || value === 'vi' || value === 'lo') {
    return value;
  }

  throw new SalesOrderPolicyError(
    'locale must be one of en, vi or lo',
  );
}

export function requirePublicQuoteChannel(
  value: PricingChannel,
): 'B2C' {
  if (value !== 'B2C') {
    throw new SalesOrderPolicyError(
      'Only B2C Pricing Quotes can use the public order route',
    );
  }

  return value;
}

export function currencyExponent(
  currency: PricingCurrency,
): PricingCurrencyExponent {
  return currency === 'USD' ? 2 : 0;
}

export function hashIdempotencyKey(
  idempotencyKey: string,
): string {
  return createHash('sha256')
    .update(idempotencyKey, 'utf8')
    .digest('hex');
}

export interface SalesOrderFingerprintInput {
  quoteId: string;
  customerName: string;
  customerEmail: string;
  recipientEmail: string;
  locale: SalesOrderLocale;
}

export function createRequestFingerprint(
  input: SalesOrderFingerprintInput,
): string {
  const canonical = JSON.stringify({
    quoteId: input.quoteId,
    customerName: input.customerName,
    customerEmail: input.customerEmail,
    recipientEmail: input.recipientEmail,
    locale: input.locale,
  });

  return createHash('sha256')
    .update(canonical, 'utf8')
    .digest('hex');
}

export function requireOrderAccessSecret(
  value: unknown,
): string {
  if (
    typeof value !== 'string' ||
    Buffer.byteLength(value, 'utf8') < 32
  ) {
    throw new SalesOrderPolicyError(
      'YSIM_ORDER_ACCESS_SECRET must contain at least 32 bytes',
    );
  }

  return value;
}

export function deriveOrderAccessToken(
  secret: string,
  orderId: string,
  idempotencyKey: string,
): string {
  return createHmac('sha256', secret)
    .update('ysim-order-access-v1\0', 'utf8')
    .update(orderId, 'utf8')
    .update('\0', 'utf8')
    .update(idempotencyKey, 'utf8')
    .digest('base64url');
}

export function hashOrderAccessToken(
  token: string,
): string {
  return createHash('sha256')
    .update(token, 'utf8')
    .digest('hex');
}

export function accessTokenHashMatches(
  token: string,
  expectedHash: string,
): boolean {
  const actual = Buffer.from(
    hashOrderAccessToken(token),
    'hex',
  );
  const expected = Buffer.from(expectedHash, 'hex');

  return (
    actual.length === expected.length &&
    timingSafeEqual(actual, expected)
  );
}

export function deriveOrderNumber(
  orderId: string,
  createdAt: string,
): string {
  const normalizedId = requireUuid(orderId, 'orderId')
    .replaceAll('-', '')
    .slice(0, 12)
    .toUpperCase();
  const date = new Date(createdAt);

  if (Number.isNaN(date.getTime())) {
    throw new SalesOrderPolicyError(
      'createdAt must be a valid timestamp',
    );
  }

  const datePart = date
    .toISOString()
    .slice(0, 10)
    .replaceAll('-', '');

  return `YS-${datePart}-${normalizedId}`;
}
