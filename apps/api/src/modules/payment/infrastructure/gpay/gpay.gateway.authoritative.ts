import { createHash } from 'node:crypto';

import type {
  PricingCurrency,
  TestPaymentEventStatus,
  VerifiedGPayWebhookContract,
} from '@ysim/contracts';

import {
  normalizeGPayGatewayStatus,
} from './gpay.gateway.callback.js';
import type {
  GPayGatewayQueryOrderResult,
  VerifiedGPayGatewayCallback,
} from './gpay.gateway.types.js';

export class GPayGatewayAuthoritativeError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'GPayGatewayAuthoritativeError';
  }
}

export interface GPayGatewayAuthoritativeBinding {
  merchantOrderId: string;
  billId: string;
  amountMinor: string;
  currency: PricingCurrency;
  actorIdentityId: string;
  occurredAt: string;
}

const paymentStatus = (
  status: ReturnType<typeof normalizeGPayGatewayStatus>,
): TestPaymentEventStatus => {
  switch (status) {
    case 'SUCCESS':
      return 'SUCCEEDED';
    case 'FAILED':
    case 'CANCELLED':
      return 'FAILED';
    case 'EXPIRED':
      return 'EXPIRED';
    case 'PENDING':
      return 'PENDING';
  }
};

const assertBinding = (
  binding: GPayGatewayAuthoritativeBinding,
  merchantOrderId: string,
  billId: string,
): void => {
  if (
    merchantOrderId !== binding.merchantOrderId ||
    billId !== binding.billId
  ) {
    throw new GPayGatewayAuthoritativeError(
      'GPay authoritative identity does not match the bound session',
    );
  }
  if (
    binding.currency !== 'VND' ||
    !/^[1-9][0-9]{0,19}$/u.test(binding.amountMinor) ||
    !/^[0-9a-f-]{36}$/iu.test(binding.actorIdentityId) ||
    Number.isNaN(Date.parse(binding.occurredAt))
  ) {
    throw new GPayGatewayAuthoritativeError(
      'GPay authoritative commercial binding is invalid',
    );
  }
};

const toEvent = (
  binding: GPayGatewayAuthoritativeBinding,
  input: {
    merchantOrderId: string;
    billId: string;
    normalizedStatus: ReturnType<typeof normalizeGPayGatewayStatus>;
    evidenceCanonical: string;
  },
): VerifiedGPayWebhookContract => {
  assertBinding(binding, input.merchantOrderId, input.billId);
  const fingerprint = createHash('sha256')
    .update(input.evidenceCanonical, 'utf8')
    .digest('hex');
  return Object.freeze({
    eventId: `gpay:gateway:${fingerprint}`,
    providerReference: binding.merchantOrderId,
    normalizedStatus: paymentStatus(input.normalizedStatus),
    amountMinor: binding.amountMinor,
    currency: binding.currency,
    occurredAt: new Date(binding.occurredAt).toISOString(),
    actorIdentityId: binding.actorIdentityId.toLowerCase(),
  });
};

export const authoritativeEventFromGPayCallback = (
  binding: GPayGatewayAuthoritativeBinding,
  callback: VerifiedGPayGatewayCallback,
): VerifiedGPayWebhookContract => toEvent(binding, {
  merchantOrderId: callback.merchantOrderId,
  billId: callback.gpayBillId,
  normalizedStatus: callback.normalizedStatus,
  evidenceCanonical: [
    'callback',
    callback.contractVersion,
    callback.merchantOrderId,
    callback.gpayBillId,
    callback.gpayTransactionId ?? '',
    callback.normalizedStatus,
    callback.canonicalSha256,
  ].join('\n'),
});

export const authoritativeEventFromGPayQuery = (
  binding: GPayGatewayAuthoritativeBinding,
  query: GPayGatewayQueryOrderResult,
): VerifiedGPayWebhookContract => toEvent(binding, {
  merchantOrderId: query.merchantOrderId,
  billId: query.gpayBillId,
  normalizedStatus: normalizeGPayGatewayStatus(query.status ?? ''),
  evidenceCanonical: [
    'query',
    query.merchantOrderId,
    query.gpayBillId,
    query.gpayTransactionId ?? '',
    normalizeGPayGatewayStatus(query.status ?? ''),
    query.userPaymentMethod ?? '',
  ].join('\n'),
});
