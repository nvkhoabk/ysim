import type {
  PaymentProvider,
  PaymentSucceededIntegrationEventV1,
  PricingCurrency,
} from '@ysim/contracts';

export class PaymentOutboxPolicyError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'PaymentOutboxPolicyError';
  }
}

type Environment =
  Record<string, string | undefined>;

export interface ClaimedPaymentIntegrationOutboxRecord {
  id: string;
  eventType: string;
  aggregateType: string;
  aggregateId: string;
  orderId: string;
  deduplicationKey: string;
  payload: unknown;
  occurredAt: string;
  attemptCount: number;
}

const UUID_PATTERN =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;
const HASH_PATTERN = /^[0-9a-f]{64}$/u;
const ORDER_NUMBER_PATTERN =
  /^YS-[0-9]{8}-[0-9A-F]{12}$/u;
const AMOUNT_PATTERN = /^[0-9]{1,20}$/u;

const payloadKeys = [
  'amountMinor',
  'currency',
  'occurredAt',
  'orderId',
  'orderNumber',
  'paymentIntentId',
  'provider',
  'providerReference',
].sort();

const asRecord = (
  value: unknown,
  field: string,
): Record<string, unknown> => {
  if (
    typeof value !== 'object' ||
    value === null ||
    Array.isArray(value)
  ) {
    throw new PaymentOutboxPolicyError(
      `${field} must be an object`,
    );
  }
  return value as Record<string, unknown>;
};

const requireString = (
  record: Record<string, unknown>,
  field: string,
): string => {
  const value = record[field];
  if (
    typeof value !== 'string' ||
    value.length === 0
  ) {
    throw new PaymentOutboxPolicyError(
      `${field} must be a non-empty string`,
    );
  }
  return value;
};

const requireUuid = (
  value: string,
  field: string,
): string => {
  if (!UUID_PATTERN.test(value)) {
    throw new PaymentOutboxPolicyError(
      `${field} must be a UUID`,
    );
  }
  return value.toLowerCase();
};

const requireIso = (
  value: string,
  field: string,
): string => {
  const parsed = Date.parse(value);
  if (!Number.isFinite(parsed)) {
    throw new PaymentOutboxPolicyError(
      `${field} must be an ISO timestamp`,
    );
  }
  return new Date(parsed).toISOString();
};

const requireProvider = (
  value: string,
): PaymentProvider => {
  if (value !== 'TEST' && value !== 'GPAY') {
    throw new PaymentOutboxPolicyError(
      'payload.provider is unsupported',
    );
  }
  return value;
};

const requireCurrency = (
  value: string,
): PricingCurrency => {
  if (
    value !== 'VND' &&
    value !== 'LAK' &&
    value !== 'USD'
  ) {
    throw new PaymentOutboxPolicyError(
      'payload.currency is unsupported',
    );
  }
  return value;
};

export const loadPaymentOutboxLeaseSeconds = (
  environment: Environment = process.env,
): number => {
  const value =
    environment.YSIM_PAYMENT_OUTBOX_LEASE_SECONDS ??
    '30';
  const parsed = Number(value);
  if (
    !Number.isInteger(parsed) ||
    parsed < 5 ||
    parsed > 300
  ) {
    throw new PaymentOutboxPolicyError(
      'YSIM_PAYMENT_OUTBOX_LEASE_SECONDS must be an integer from 5 to 300',
    );
  }
  return parsed;
};

export const paymentOutboxLeaseUntil = (
  now: string,
  leaseSeconds: number,
): string => {
  const timestamp = Date.parse(now);
  if (!Number.isFinite(timestamp)) {
    throw new PaymentOutboxPolicyError(
      'Outbox claim time must be an ISO timestamp',
    );
  }
  if (
    !Number.isInteger(leaseSeconds) ||
    leaseSeconds < 5 ||
    leaseSeconds > 300
  ) {
    throw new PaymentOutboxPolicyError(
      'Outbox lease seconds are invalid',
    );
  }
  return new Date(
    timestamp + leaseSeconds * 1_000,
  ).toISOString();
};

export const paymentOutboxRetryAt = (
  failedAt: string,
  attemptCount: number,
): string => {
  const timestamp = Date.parse(failedAt);
  if (!Number.isFinite(timestamp)) {
    throw new PaymentOutboxPolicyError(
      'Outbox failure time must be an ISO timestamp',
    );
  }
  if (
    !Number.isInteger(attemptCount) ||
    attemptCount < 1
  ) {
    throw new PaymentOutboxPolicyError(
      'Outbox attempt count must be positive',
    );
  }
  const delaySeconds = Math.min(
    5 * (2 ** (attemptCount - 1)),
    900,
  );
  return new Date(
    timestamp + delaySeconds * 1_000,
  ).toISOString();
};

export const sanitizePaymentOutboxError = (
  error: unknown,
): string => {
  const source = error instanceof Error
    ? error.message
    : String(error);
  return source
    .replace(
      /-----BEGIN[\s\S]*?-----END [^-]+-----/giu,
      '[REDACTED_PEM]',
    )
    .replace(
      /\bBearer\s+[A-Za-z0-9._~+/-]+=*/giu,
      'Bearer [REDACTED]',
    )
    .replace(
      /\b(api[_-]?key|token|secret|password)\s*[:=]\s*[^\s,;]+/giu,
      '$1=[REDACTED]',
    )
    .replace(/[\u0000-\u001f\u007f]+/gu, ' ')
    .replace(/\s+/gu, ' ')
    .trim()
    .slice(0, 500) || 'Unknown outbox publication failure';
};

export const parseClaimedPaymentIntegrationEvent = (
  record: ClaimedPaymentIntegrationOutboxRecord,
): PaymentSucceededIntegrationEventV1 => {
  const eventId = requireUuid(
    record.id,
    'eventId',
  );
  if (
    record.eventType !==
    'payment.succeeded.v1'
  ) {
    throw new PaymentOutboxPolicyError(
      'Unsupported integration event type',
    );
  }
  if (record.aggregateType !== 'PaymentIntent') {
    throw new PaymentOutboxPolicyError(
      'Unsupported integration aggregate type',
    );
  }
  const aggregateId = requireUuid(
    record.aggregateId,
    'aggregateId',
  );
  const orderId = requireUuid(
    record.orderId,
    'orderId',
  );
  if (
    !HASH_PATTERN.test(
      record.deduplicationKey,
    )
  ) {
    throw new PaymentOutboxPolicyError(
      'deduplicationKey must be a SHA-256 value',
    );
  }
  if (
    !Number.isInteger(record.attemptCount) ||
    record.attemptCount < 1
  ) {
    throw new PaymentOutboxPolicyError(
      'attemptCount must be positive',
    );
  }

  const payload = asRecord(
    record.payload,
    'payload',
  );
  const actualPayloadKeys =
    Object.keys(payload).sort();
  if (
    JSON.stringify(actualPayloadKeys) !==
    JSON.stringify(payloadKeys)
  ) {
    throw new PaymentOutboxPolicyError(
      'Payment Success payload shape is invalid',
    );
  }

  const paymentIntentId = requireUuid(
    requireString(payload, 'paymentIntentId'),
    'payload.paymentIntentId',
  );
  const payloadOrderId = requireUuid(
    requireString(payload, 'orderId'),
    'payload.orderId',
  );
  const orderNumber = requireString(
    payload,
    'orderNumber',
  );
  if (!ORDER_NUMBER_PATTERN.test(orderNumber)) {
    throw new PaymentOutboxPolicyError(
      'payload.orderNumber is invalid',
    );
  }
  const provider = requireProvider(
    requireString(payload, 'provider'),
  );
  const providerReference = requireString(
    payload,
    'providerReference',
  );
  if (providerReference.length > 80) {
    throw new PaymentOutboxPolicyError(
      'payload.providerReference is too long',
    );
  }
  const amountMinor = requireString(
    payload,
    'amountMinor',
  );
  if (!AMOUNT_PATTERN.test(amountMinor)) {
    throw new PaymentOutboxPolicyError(
      'payload.amountMinor is invalid',
    );
  }
  const currency = requireCurrency(
    requireString(payload, 'currency'),
  );
  const payloadOccurredAt = requireIso(
    requireString(payload, 'occurredAt'),
    'payload.occurredAt',
  );
  const occurredAt = requireIso(
    record.occurredAt,
    'occurredAt',
  );

  if (
    paymentIntentId !== aggregateId ||
    payloadOrderId !== orderId ||
    payloadOccurredAt !== occurredAt
  ) {
    throw new PaymentOutboxPolicyError(
      'Integration event envelope does not match payload',
    );
  }

  return {
    eventId,
    eventType: 'payment.succeeded.v1',
    aggregateType: 'PaymentIntent',
    aggregateId,
    orderId,
    deduplicationKey:
      record.deduplicationKey,
    payload: {
      paymentIntentId,
      orderId,
      orderNumber,
      provider,
      providerReference,
      amountMinor,
      currency,
      occurredAt,
    },
    occurredAt,
  };
};
