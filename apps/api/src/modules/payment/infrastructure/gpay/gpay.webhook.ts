import { readFile } from 'node:fs/promises';
import { isAbsolute } from 'node:path';

import type {
  GPayWebhookBody,
  GPayWebhookStatus,
  PricingCurrency,
  TestPaymentEventStatus,
  VerifiedGPayWebhookContract,
} from '@ysim/contracts';

import {
  stableGPayJson,
  verifyGPayCanonical,
} from './gpay.crypto.js';

const EVENT_ID_PATTERN =
  /^[A-Za-z0-9][A-Za-z0-9._:-]{7,99}$/u;
const REFERENCE_PATTERN =
  /^GPY-[A-Z0-9][A-Z0-9_-]{11,75}$/u;
const AMOUNT_PATTERN = /^[1-9][0-9]{0,19}$/u;
const UUID_PATTERN =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;

type Environment = Record<string, string | undefined>;

export class GPayWebhookError extends Error {
  constructor(
    message: string,
    readonly kind:
      | 'BAD_REQUEST'
      | 'UNAUTHORIZED'
      | 'UNAVAILABLE',
  ) {
    super(message);
    this.name = 'GPayWebhookError';
  }
}

export interface GPayWebhookConfig {
  actorIdentityId: string;
  verifyCertificatePath: string;
  maxSkewSeconds: number;
}

export interface GPayWebhookHeaders {
  eventId: string | undefined;
  timestamp: string | undefined;
  signature: string | undefined;
}

const required = (
  environment: Environment,
  name: string,
): string => {
  const value = environment[name]?.trim();
  if (!value) {
    throw new GPayWebhookError(
      `${name} is required`,
      'UNAVAILABLE',
    );
  }
  return value;
};

const parseSkew = (
  value: string | undefined,
): number => {
  const parsed = Number(value ?? '300');
  if (
    !Number.isInteger(parsed) ||
    parsed < 60 ||
    parsed > 900
  ) {
    throw new GPayWebhookError(
      'YSIM_GPAY_WEBHOOK_MAX_SKEW_SECONDS must be an integer from 60 to 900',
      'UNAVAILABLE',
    );
  }
  return parsed;
};

export const loadGPayWebhookConfig = (
  environment: Environment = process.env,
): GPayWebhookConfig => {
  if (
    environment.YSIM_GPAY_WEBHOOK_ENABLED !== 'true'
  ) {
    throw new GPayWebhookError(
      'GPay webhook is disabled',
      'UNAVAILABLE',
    );
  }
  if (environment.YSIM_GPAY_ENVIRONMENT !== 'SANDBOX') {
    throw new GPayWebhookError(
      'Only GPay SANDBOX webhook verification is available in VS-R1-010',
      'UNAVAILABLE',
    );
  }
  if (
    environment.YSIM_GPAY_CONTRACT_STATUS !== 'PROBED'
  ) {
    throw new GPayWebhookError(
      'GPay contract must be PROBED before webhook verification',
      'UNAVAILABLE',
    );
  }

  const verifyCertificatePath = required(
    environment,
    'YSIM_GPAY_VERIFY_CERTIFICATE_PATH',
  );
  if (!isAbsolute(verifyCertificatePath)) {
    throw new GPayWebhookError(
      'YSIM_GPAY_VERIFY_CERTIFICATE_PATH must be absolute',
      'UNAVAILABLE',
    );
  }

  const actorIdentityId = required(
    environment,
    'YSIM_GPAY_WEBHOOK_ACTOR_ID',
  ).toLowerCase();
  if (!UUID_PATTERN.test(actorIdentityId)) {
    throw new GPayWebhookError(
      'YSIM_GPAY_WEBHOOK_ACTOR_ID must be a UUID',
      'UNAVAILABLE',
    );
  }

  return {
    actorIdentityId,
    verifyCertificatePath,
    maxSkewSeconds: parseSkew(
      environment.YSIM_GPAY_WEBHOOK_MAX_SKEW_SECONDS,
    ),
  };
};

const parseStatus = (
  value: unknown,
): GPayWebhookStatus => {
  if (
    value !== 'PENDING' &&
    value !== 'SUCCESS' &&
    value !== 'FAILED' &&
    value !== 'EXPIRED'
  ) {
    throw new GPayWebhookError(
      'GPay webhook status is unsupported',
      'BAD_REQUEST',
    );
  }
  return value;
};

const parseCurrency = (
  value: unknown,
): PricingCurrency => {
  if (
    value !== 'VND' &&
    value !== 'LAK' &&
    value !== 'USD'
  ) {
    throw new GPayWebhookError(
      'GPay webhook currency is unsupported',
      'BAD_REQUEST',
    );
  }
  return value;
};

export const parseGPayWebhookBody = (
  value: unknown,
): GPayWebhookBody => {
  if (
    typeof value !== 'object' ||
    value === null ||
    Array.isArray(value)
  ) {
    throw new GPayWebhookError(
      'GPay webhook body must be an object',
      'BAD_REQUEST',
    );
  }

  const record = value as Record<string, unknown>;
  const keys = Object.keys(record).sort();
  const allowed = [
    'amountMinor',
    'currency',
    'occurredAt',
    'providerReference',
    'status',
  ].sort();

  if (
    keys.length !== allowed.length ||
    keys.some((key, index) => key !== allowed[index])
  ) {
    throw new GPayWebhookError(
      'GPay webhook body contains unsupported fields',
      'BAD_REQUEST',
    );
  }

  const providerReference =
    typeof record.providerReference === 'string'
      ? record.providerReference.trim().toUpperCase()
      : '';
  if (!REFERENCE_PATTERN.test(providerReference)) {
    throw new GPayWebhookError(
      'GPay providerReference is invalid',
      'BAD_REQUEST',
    );
  }

  const amountMinor =
    typeof record.amountMinor === 'string'
      ? record.amountMinor.trim()
      : '';
  if (!AMOUNT_PATTERN.test(amountMinor)) {
    throw new GPayWebhookError(
      'GPay amountMinor is invalid',
      'BAD_REQUEST',
    );
  }

  const occurredAt =
    typeof record.occurredAt === 'string'
      ? record.occurredAt.trim()
      : '';
  if (!Number.isFinite(Date.parse(occurredAt))) {
    throw new GPayWebhookError(
      'GPay occurredAt must be an ISO timestamp',
      'BAD_REQUEST',
    );
  }

  return {
    providerReference,
    status: parseStatus(record.status),
    amountMinor,
    currency: parseCurrency(record.currency),
    occurredAt: new Date(occurredAt).toISOString(),
  };
};

export const normalizeGPayWebhookStatus = (
  status: GPayWebhookStatus,
): TestPaymentEventStatus => {
  switch (status) {
    case 'PENDING':
      return 'PENDING';
    case 'SUCCESS':
      return 'SUCCEEDED';
    case 'FAILED':
      return 'FAILED';
    case 'EXPIRED':
      return 'EXPIRED';
  }
};

export const canonicalGPayWebhook = (input: {
  eventId: string;
  timestamp: string;
  body: GPayWebhookBody;
}): string => [
  'GPAY-WEBHOOK-V1',
  input.eventId,
  input.timestamp,
  stableGPayJson(input.body),
].join('\n');

export class GPayWebhookVerifier {
  async verify(
    headers: GPayWebhookHeaders,
    rawBody: unknown,
    now = new Date(),
  ): Promise<VerifiedGPayWebhookContract> {
    const config = loadGPayWebhookConfig();
    const eventId = headers.eventId?.trim() ?? '';
    if (!EVENT_ID_PATTERN.test(eventId)) {
      throw new GPayWebhookError(
        'x-gpay-event-id is invalid',
        'BAD_REQUEST',
      );
    }

    const timestamp = headers.timestamp?.trim() ?? '';
    const parsedTimestamp = Date.parse(timestamp);
    if (!Number.isFinite(parsedTimestamp)) {
      throw new GPayWebhookError(
        'x-timestamp is invalid',
        'UNAUTHORIZED',
      );
    }

    if (
      Math.abs(now.getTime() - parsedTimestamp) >
      config.maxSkewSeconds * 1_000
    ) {
      throw new GPayWebhookError(
        'GPay webhook timestamp is outside the replay window',
        'UNAUTHORIZED',
      );
    }

    const signature = headers.signature?.trim() ?? '';
    if (signature.length < 32) {
      throw new GPayWebhookError(
        'x-signature is required',
        'UNAUTHORIZED',
      );
    }

    const body = parseGPayWebhookBody(rawBody);
    let certificate: string;
    try {
      certificate = await readFile(
        config.verifyCertificatePath,
        'utf8',
      );
    } catch {
      throw new GPayWebhookError(
        'GPay verification certificate could not be loaded',
        'UNAVAILABLE',
      );
    }

    const canonical = canonicalGPayWebhook({
      eventId,
      timestamp: new Date(parsedTimestamp).toISOString(),
      body,
    });

    if (
      !verifyGPayCanonical(
        canonical,
        signature,
        certificate,
      )
    ) {
      throw new GPayWebhookError(
        'GPay webhook signature verification failed',
        'UNAUTHORIZED',
      );
    }

    return {
      eventId,
      providerReference: body.providerReference,
      normalizedStatus:
        normalizeGPayWebhookStatus(body.status),
      amountMinor: body.amountMinor,
      currency: body.currency,
      occurredAt: body.occurredAt,
      actorIdentityId: config.actorIdentityId,
    };
  }
}
