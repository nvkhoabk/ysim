import { createHash } from 'node:crypto';

import {
  buildGigagoCreateOrderInput,
  type GigagoProcurementSnapshot,
} from './gigago-create-order-policy.js';
import type {
  GigagoCreatePartnerOrderInput,
} from '../infrastructure/gigago/gigago.types.js';

export class SupplierSubmissionPolicyError
  extends Error {
  constructor(message: string) {
    super(message);
    this.name =
      'SupplierSubmissionPolicyError';
  }
}

type Environment =
  Record<string, string | undefined>;

export interface SupplierSubmissionCommand {
  snapshot: GigagoProcurementSnapshot;
  input: GigagoCreatePartnerOrderInput;
  providerRequestId: string;
  requestPayloadHash: string;
}

const sha256 = (value: string): string =>
  createHash('sha256')
    .update(value, 'utf8')
    .digest('hex');

export const buildSupplierSubmissionCommand = (
  snapshot: GigagoProcurementSnapshot,
  notifyUrl: string,
): SupplierSubmissionCommand => {
  if (
    snapshot.status !==
      'PENDING_SUPPLIER' &&
    snapshot.status !== 'SUBMITTED'
  ) {
    throw new SupplierSubmissionPolicyError(
      'Procurement Request is not eligible for supplier submission',
    );
  }

  const input =
    buildGigagoCreateOrderInput(
      {
        ...snapshot,
        status: 'PENDING_SUPPLIER',
      },
      notifyUrl,
    );
  const body = JSON.stringify(input);

  return {
    snapshot,
    input,
    providerRequestId:
      input.request_id,
    requestPayloadHash:
      sha256(body),
  };
};

export const loadSupplierSubmissionLeaseSeconds = (
  environment: Environment = process.env,
): number => {
  const value =
    environment
      .YSIM_SUPPLIER_SUBMISSION_LEASE_SECONDS ??
    '30';
  const parsed = Number(value);

  if (
    !Number.isInteger(parsed) ||
    parsed < 5 ||
    parsed > 300
  ) {
    throw new SupplierSubmissionPolicyError(
      'YSIM_SUPPLIER_SUBMISSION_LEASE_SECONDS must be 5..300',
    );
  }
  return parsed;
};

export const supplierSubmissionLeaseUntil = (
  claimedAt: string,
  leaseSeconds: number,
): string => {
  const timestamp = Date.parse(claimedAt);
  if (!Number.isFinite(timestamp)) {
    throw new SupplierSubmissionPolicyError(
      'claimedAt must be an ISO timestamp',
    );
  }
  if (
    !Number.isInteger(leaseSeconds) ||
    leaseSeconds < 5 ||
    leaseSeconds > 300
  ) {
    throw new SupplierSubmissionPolicyError(
      'leaseSeconds must be 5..300',
    );
  }
  return new Date(
    timestamp + leaseSeconds * 1_000,
  ).toISOString();
};

export const supplierSubmissionRetryAt = (
  failedAt: string,
  attemptCount: number,
): string => {
  const timestamp = Date.parse(failedAt);
  if (!Number.isFinite(timestamp)) {
    throw new SupplierSubmissionPolicyError(
      'failedAt must be an ISO timestamp',
    );
  }
  if (
    !Number.isInteger(attemptCount) ||
    attemptCount < 1
  ) {
    throw new SupplierSubmissionPolicyError(
      'attemptCount must be positive',
    );
  }
  const delaySeconds = Math.min(
    10 * (2 ** (attemptCount - 1)),
    900,
  );
  return new Date(
    timestamp + delaySeconds * 1_000,
  ).toISOString();
};

export const sanitizeSupplierSubmissionError = (
  error: unknown,
): string => {
  const source = error instanceof Error
    ? error.message
    : String(error);

  return source
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
    .slice(0, 500) ||
    'Unknown supplier submission failure';
};
