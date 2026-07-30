import { createHash } from 'node:crypto';

import type {
  PaymentIntentStatus,
  PaymentProvider,
  PricingCurrency,
  PricingCurrencyExponent,
  TestPaymentEventStatus,
} from '@ysim/contracts';

export class PaymentPolicyError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'PaymentPolicyError';
  }
}

const UUID_PATTERN =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;
const EVENT_ID_PATTERN = /^[A-Za-z0-9][A-Za-z0-9._:-]{7,99}$/u;

export const requirePaymentUuid = (
  value: string,
  field: string,
): string => {
  const normalized = value.trim().toLowerCase();
  if (!UUID_PATTERN.test(normalized)) {
    throw new PaymentPolicyError(`${field} must be a UUID`);
  }
  return normalized;
};

export const normalizePaymentIdempotencyKey = (
  value: string | undefined,
): string => {
  if (typeof value !== 'string') {
    throw new PaymentPolicyError(
      'Idempotency-Key header is required',
    );
  }

  const normalized = value.trim();
  if (
    normalized.length < 16 ||
    normalized.length > 128 ||
    /[\u0000-\u001f\u007f]/u.test(normalized)
  ) {
    throw new PaymentPolicyError(
      'Idempotency-Key must contain 16 to 128 visible characters',
    );
  }

  return normalized;
};

export const requirePaymentAccessToken = (
  value: string | undefined,
): string => {
  if (
    typeof value !== 'string' ||
    value.length < 32 ||
    value.length > 256
  ) {
    throw new PaymentPolicyError(
      'x-ysim-order-access-token header is required',
    );
  }
  return value;
};

export const requirePaymentProvider = (
  value: PaymentProvider | string,
): PaymentProvider => {
  if (value !== 'TEST') {
    throw new PaymentPolicyError(
      'Only the normalized TEST provider is available in VS-R1-008',
    );
  }
  return value;
};

export const normalizeTestPaymentEventId = (
  value: string,
): string => {
  const normalized = value.trim();
  if (!EVENT_ID_PATTERN.test(normalized)) {
    throw new PaymentPolicyError(
      'eventId must contain 8 to 100 stable provider characters',
    );
  }
  return normalized;
};

export const requireTestPaymentEventStatus = (
  value: TestPaymentEventStatus | string,
): TestPaymentEventStatus => {
  if (
    value !== 'PENDING' &&
    value !== 'SUCCEEDED' &&
    value !== 'FAILED' &&
    value !== 'EXPIRED'
  ) {
    throw new PaymentPolicyError(
      'Unsupported normalized payment event status',
    );
  }
  return value;
};

export const sha256PaymentValue = (value: string): string =>
  createHash('sha256').update(value, 'utf8').digest('hex');

export const createPaymentRequestFingerprint = (input: {
  orderId: string;
  provider: PaymentProvider;
}): string => sha256PaymentValue(
  JSON.stringify({
    orderId: input.orderId,
    provider: input.provider,
  }),
);

export const createPaymentEventFingerprint = (input: {
  intentId: string;
  eventId: string;
  status: TestPaymentEventStatus;
}): string => sha256PaymentValue(
  JSON.stringify({
    eventId: input.eventId,
    intentId: input.intentId,
    status: input.status,
  }),
);

export const deriveTestProviderReference = (
  intentId: string,
): string => `TST-${intentId.replaceAll('-', '').slice(0, 24).toUpperCase()}`;

export const derivePaymentIntentExpiry = (
  createdAt: string,
): string => {
  const parsed = Date.parse(createdAt);
  if (!Number.isFinite(parsed)) {
    throw new PaymentPolicyError(
      'Payment Intent createdAt must be an ISO timestamp',
    );
  }
  return new Date(parsed + 15 * 60 * 1_000).toISOString();
};

export const resolvePaymentTransition = (
  current: PaymentIntentStatus,
  incoming: TestPaymentEventStatus,
): PaymentIntentStatus => {
  if (current === incoming) return current;

  if (
    current === 'SUCCEEDED' ||
    current === 'FAILED' ||
    current === 'EXPIRED'
  ) {
    throw new PaymentPolicyError(
      `Payment Intent ${current} is terminal`,
    );
  }

  if (current === 'CREATED' || current === 'PENDING') {
    return incoming;
  }

  throw new PaymentPolicyError(
    `Unsupported payment transition ${current} -> ${incoming}`,
  );
};

export const paymentCurrencyExponent = (
  currency: PricingCurrency,
): PricingCurrencyExponent => currency === 'USD' ? 2 : 0;
