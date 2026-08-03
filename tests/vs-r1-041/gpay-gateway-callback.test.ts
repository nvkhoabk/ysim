import { generateKeyPairSync } from 'node:crypto';
import { resolve } from 'node:path';

import { describe, expect, it } from 'vitest';

import {
  canonicalGPayGatewayCallback,
  parseGPayGatewayCallback,
  verifyGPayGatewayCallback,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.gateway.callback.js';
import {
  signGPayCanonical,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.crypto.js';

const keys = generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: { type: 'spki', format: 'pem' },
  privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
});

const environment = {
  YSIM_GPAY_ENABLED: 'true',
  YSIM_GPAY_ENVIRONMENT: 'SANDBOX',
  YSIM_GPAY_CONTRACT_STATUS: 'BOUND',
  YSIM_GPAY_BASE_URL: 'https://openapi-sandbox.g-pay.vn/v1',
  YSIM_GPAY_CLIENT_ID: 'ysim-client-0001',
  YSIM_GPAY_CLIENT_SECRET_PATH: resolve('/tmp/gpay-client-secret'),
  YSIM_GPAY_PRIVATE_KEY_PATH: resolve('/tmp/gpay-private.pem'),
  YSIM_GPAY_CERTIFICATE_PATH: resolve('/tmp/gpay-certificate.pem'),
  YSIM_GPAY_VERIFY_CERTIFICATE_PATH: resolve('/tmp/gpay-provider.pem'),
};

describe('GPay confirmed callback contract', () => {
  it('uses the confirmed field order and verifies ORDER_SUCCESS', async () => {
    const rawCallback: Record<string, unknown> = {
      merchant_order_id: 'YSIM-ORDER-0001',
      gpay_trans_id: 'GPAY-TRANS-0001',
      gpay_bill_id: 'GPAY-BILL-0001',
      status: 'ORDER_SUCCESS',
      embed_data: '{"orderId":"order-0001"}',
      user_payment_method: 'QR_PAYMENT',
    };
    const callback = parseGPayGatewayCallback(rawCallback);
    rawCallback.signature = signGPayCanonical(
      canonicalGPayGatewayCallback(callback),
      keys.privateKey,
    );
    await expect(verifyGPayGatewayCallback(rawCallback, {
      environment,
      readText: async () => keys.publicKey,
    })).resolves.toMatchObject({
      verified: true,
      contractVersion: 'GPAY_ALL_IN_ONE_CALLBACK_V1',
      normalizedStatus: 'SUCCESS',
      merchantOrderId: 'YSIM-ORDER-0001',
      gpayBillId: 'GPAY-BILL-0001',
    });
  });

  it('rejects a tampered callback signature', async () => {
    const input = {
      merchant_order_id: 'YSIM-ORDER-0001',
      gpay_trans_id: '',
      gpay_bill_id: 'GPAY-BILL-0001',
      status: 'ORDER_SUCCESS',
      embed_data: '',
      user_payment_method: '',
      signature: 'invalid-signature',
    };
    await expect(verifyGPayGatewayCallback(input, {
      environment,
      readText: async () => keys.publicKey,
    })).rejects.toThrow(/signature verification failed/u);
  });
});
