import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';

import {
  loadGPayGatewayConfig,
} from './gpay.gateway.config.js';
import type {
  GPayGatewayCallbackData,
  GPayGatewayNormalizedStatus,
  VerifiedGPayGatewayCallback,
} from './gpay.gateway.types.js';
import {
  verifyGPayCanonical,
} from './gpay.crypto.js';

type Environment = Record<string, string | undefined>;

export class GPayGatewayCallbackError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'GPayGatewayCallbackError';
  }
}

const value = (input: unknown): string =>
  typeof input === 'string'
    ? input
    : input == null
      ? ''
      : String(input);

export const parseGPayGatewayCallback = (
  input: URLSearchParams | Record<string, unknown>,
  fallbackSignature?: string,
): GPayGatewayCallbackData => {
  const record = input instanceof URLSearchParams
    ? Object.fromEntries(input.entries())
    : input;
  return {
    merchantOrderId: value(record.merchant_order_id),
    gpayTransactionId: value(record.gpay_trans_id),
    gpayBillId: value(record.gpay_bill_id),
    status: value(record.status),
    embedData: value(record.embed_data),
    userPaymentMethod: value(record.user_payment_method),
    signature: value(record.signature) || value(fallbackSignature),
  };
};

export const canonicalGPayGatewayCallback = (
  callback: GPayGatewayCallbackData,
): string => [
  ['merchant_order_id', callback.merchantOrderId],
  ['gpay_trans_id', callback.gpayTransactionId],
  ['gpay_bill_id', callback.gpayBillId],
  ['status', callback.status],
  ['embed_data', callback.embedData],
  ['user_payment_method', callback.userPaymentMethod],
].map(([key, item]) => `${key}=${item}`).join('&');

export const normalizeGPayGatewayStatus = (
  status: string,
): GPayGatewayNormalizedStatus => {
  switch (status.trim().toUpperCase()) {
    case 'ORDER_SUCCESS':
      return 'SUCCESS';
    case 'ORDER_FAILED':
      return 'FAILED';
    case 'ORDER_CANCELLED':
    case 'ORDER_CANCELED':
      return 'CANCELLED';
    case 'ORDER_EXPIRED':
      return 'EXPIRED';
    default:
      return 'PENDING';
  }
};

export const verifyGPayGatewayCallback = async (
  input: URLSearchParams | Record<string, unknown>,
  options: {
    fallbackSignature?: string;
    environment?: Environment;
    readText?: (path: string) => Promise<string>;
  } = {},
): Promise<VerifiedGPayGatewayCallback> => {
  const callback = parseGPayGatewayCallback(
    input,
    options.fallbackSignature,
  );
  if (
    !callback.merchantOrderId.trim() ||
    !callback.gpayBillId.trim() ||
    !callback.status.trim() ||
    !callback.signature.trim()
  ) {
    throw new GPayGatewayCallbackError(
      'GPay callback identity, status, and signature are required',
    );
  }

  const config = loadGPayGatewayConfig(
    options.environment ?? process.env,
  );
  let providerCertificate: string;
  try {
    providerCertificate = await (
      options.readText ?? (async (path) => readFile(path, 'utf8'))
    )(config.verifyCertificatePath);
  } catch {
    throw new GPayGatewayCallbackError(
      'GPay provider verification certificate could not be loaded',
    );
  }
  const canonical = canonicalGPayGatewayCallback(callback);
  if (!verifyGPayCanonical(
    canonical,
    callback.signature.replaceAll(' ', '+'),
    providerCertificate,
  )) {
    throw new GPayGatewayCallbackError(
      'GPay callback signature verification failed',
    );
  }
  return {
    verified: true,
    contractVersion: 'GPAY_ALL_IN_ONE_CALLBACK_V1',
    merchantOrderId: callback.merchantOrderId,
    gpayBillId: callback.gpayBillId,
    gpayTransactionId:
      callback.gpayTransactionId.trim() || undefined,
    normalizedStatus: normalizeGPayGatewayStatus(callback.status),
    userPaymentMethod:
      callback.userPaymentMethod.trim() || undefined,
    canonicalSha256: createHash('sha256')
      .update(canonical, 'utf8')
      .digest('hex'),
  };
};
