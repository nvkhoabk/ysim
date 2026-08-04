import {
  generateKeyPairSync,
} from 'node:crypto';
import { resolve } from 'node:path';

import { describe, expect, it, vi } from 'vitest';

import {
  GPayGatewayClient,
  GPayGatewayClientError,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.gateway.client.js';
import {
  verifyGPayCanonical,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.crypto.js';

const keys = generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: { type: 'spki', format: 'pem' },
  privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
});

const environment = (): Record<string, string> => ({
  NODE_ENV: 'test',
  YSIM_GPAY_TEST_ALLOW_LOOPBACK: 'true',
  YSIM_GPAY_ENABLED: 'true',
  YSIM_GPAY_ENVIRONMENT: 'SANDBOX',
  YSIM_GPAY_CONTRACT_STATUS: 'BOUND',
  YSIM_GPAY_BASE_URL: 'http://127.0.0.1:3109/v1',
  YSIM_GPAY_CLIENT_ID: 'ysim-client-0001',
  YSIM_GPAY_CLIENT_SECRET_PATH: resolve('/tmp/gpay-client-secret'),
  YSIM_GPAY_PRIVATE_KEY_PATH: resolve('/tmp/gpay-private.pem'),
  YSIM_GPAY_CERTIFICATE_PATH: resolve('/tmp/gpay-certificate.pem'),
  YSIM_GPAY_VERIFY_CERTIFICATE_PATH: resolve('/tmp/gpay-provider.pem'),
  YSIM_COMMISSIONING_MODE: 'SANDBOX',
  YSIM_COMMISSIONING_RUN_NAMESPACE: 'vs-r1-043-gateway-test-0001',
  YSIM_COMMISSIONING_TRANSACTION_CAP: '1',
  YSIM_COMMISSIONING_MARKET: 'VN',
  YSIM_COMMISSIONING_CURRENCY: 'VND',
  YSIM_GPAY_EXECUTION_ENABLED: 'true',
  YSIM_GPAY_QUERY_CAP: '12',
  YSIM_GPAY_CALLBACK_URL:
    'https://portal.ysim.vn/api/platform/api/r1/payments/gpay/gateway/callback',
  YSIM_GPAY_WEBHOOK_URL:
    'https://portal.ysim.vn/api/platform/api/r1/payments/gpay/gateway/webhook',
  YSIM_GPAY_COMMISSIONING_CUSTOMER_ID:
    'vs-r1-043-sandbox-customer',
  YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED: 'false',
  YSIM_CUSTOMER_EMAIL_ENABLED: 'false',
  YSIM_CUSTOMER_EMAIL_MODE: 'disabled',
  YSIM_CATALOG_SUPPLIER_ENVIRONMENT: 'SANDBOX',
});

const response = (body: unknown): Response => new Response(
  JSON.stringify(body),
  {
    status: 200,
    headers: { 'content-type': 'application/json' },
  },
);

const client = (fetchMock: ReturnType<typeof vi.fn>) =>
  new GPayGatewayClient({
    environment: environment(),
    fetch: fetchMock as typeof fetch,
    now: () => 1_785_600_000_000,
    requestId: () => '11111111-1111-4111-8111-111111111111',
    readText: async (path) => {
      if (path.endsWith('private.pem')) return keys.privateKey;
      if (path.endsWith('certificate.pem')) return keys.publicKey;
      if (path.endsWith('client-secret')) return 'sandbox-secret';
      return keys.publicKey;
    },
  });

describe('GPay All-in-one gateway client', () => {
  it('gets a token and signs the exact init-order JSON', async () => {
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(response({
        meta: { code: '200' },
        data: { access_token: 'sandbox-token', expires_in: 3600 },
      }))
      .mockResolvedValueOnce(response({
        meta: { code: '200' },
        data: {
          bill_id: 'GPAY-BILL-0001',
          bill_url: 'https://sandbox.g-pay.vn/pay/GPAY-BILL-0001',
          expired_time: '2026-08-03T12:15:00.000Z',
          request_id: 'YSIM-ORDER-0001',
        },
      }));

    const result = await client(fetchMock).initOrder({
      amount: 338000,
      callbackUrl: 'https://sandbox.ysim.vn/payment/return',
      customerId: 'customer-0001',
      embedData: '{"orderId":"order-0001"}',
      merchantOrderId: 'YSIM-ORDER-0001',
      webhookUrl: 'https://sandbox.ysim.vn/api/r1/payments/gpay/webhook',
    });

    expect(fetchMock).toHaveBeenCalledTimes(2);
    const [tokenUrl, tokenInit] = fetchMock.mock.calls[0] as [URL, RequestInit];
    expect(tokenUrl.pathname).toBe('/v1/auth/token');
    expect(tokenInit.body).toContain('sandbox-secret');

    const [gatewayUrl, gatewayInit] = fetchMock.mock.calls[1] as [URL, RequestInit];
    expect(gatewayUrl.pathname).toBe('/v1/payments/gateway/init-order');
    const headers = gatewayInit.headers as Record<string, string>;
    const body = String(gatewayInit.body);
    expect(headers.authorization).toBe('Bearer sandbox-token');
    expect(headers['x-certificate']).not.toMatch(/BEGIN|END|\s/u);
    expect(verifyGPayCanonical(
      `${headers['x-timestamp']}${headers['x-requests-id']}${body}`,
      headers.signature,
      keys.publicKey,
    )).toBe(true);
    expect(result).toMatchObject({
      provider: 'GPAY',
      billId: 'GPAY-BILL-0001',
      merchantOrderId: 'YSIM-ORDER-0001',
      tokenCached: false,
    });
    expect(JSON.stringify(result)).not.toContain('sandbox-token');
    expect(JSON.stringify(result)).not.toContain('sandbox-secret');
  });

  it('reuses the token and enforces query identity', async () => {
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(response({
        meta: { code: '200' },
        data: { access_token: 'sandbox-token', expires_in: 3600 },
      }))
      .mockResolvedValueOnce(response({
        meta: { code: '200' },
        data: {
          gpay_bill_id: 'GPAY-BILL-0001',
          merchant_order_id: 'YSIM-ORDER-0001',
          gpay_trans_id: 'GPAY-TRANS-0001',
          status: 'ORDER_SUCCESS',
        },
      }))
      .mockResolvedValueOnce(response({
        meta: { code: '200' },
        data: {
          gpay_bill_id: 'GPAY-BILL-0001',
          merchant_order_id: 'YSIM-ORDER-0001',
          status: 'ORDER_SUCCESS',
        },
      }));
    const gateway = client(fetchMock);
    await gateway.queryOrder({
      gpayBillId: 'GPAY-BILL-0001',
      merchantOrderId: 'YSIM-ORDER-0001',
    });
    const second = await gateway.queryOrder({
      gpayBillId: 'GPAY-BILL-0001',
      merchantOrderId: 'YSIM-ORDER-0001',
    });
    expect(fetchMock).toHaveBeenCalledTimes(3);
    expect(second.tokenCached).toBe(true);
    expect((fetchMock.mock.calls[1]?.[0] as URL).pathname)
      .toBe('/v1/payments/gateway/query-order');
  });

  it('fails closed on rejected or mismatched responses', async () => {
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(response({
        meta: { code: '200' },
        data: { access_token: 'sandbox-token', expires_in: 3600 },
      }))
      .mockResolvedValueOnce(response({
        meta: { code: '200' },
        data: {
          gpay_bill_id: 'DIFFERENT',
          merchant_order_id: 'YSIM-ORDER-0001',
        },
      }));
    await expect(client(fetchMock).queryOrder({
      gpayBillId: 'GPAY-BILL-0001',
      merchantOrderId: 'YSIM-ORDER-0001',
    })).rejects.toBeInstanceOf(GPayGatewayClientError);
  });

  it('consumes the init-order budget before the first network call', async () => {
    const fetchMock = vi.fn().mockRejectedValue(new Error('network'));
    const gateway = client(fetchMock);
    const input = {
      amount: 338000,
      callbackUrl: 'https://sandbox.ysim.vn/payment/return',
      customerId: 'customer-0001',
      embedData: '{"orderId":"order-0001"}',
      merchantOrderId: 'YSIM-ORDER-0001',
      webhookUrl: 'https://sandbox.ysim.vn/api/r1/payments/gpay/webhook',
    };
    await expect(gateway.initOrder(input)).rejects.toThrow(/request failed/u);
    const countAfterFailure = fetchMock.mock.calls.length;
    await expect(gateway.initOrder(input)).rejects.toThrow(/budget/u);
    expect(fetchMock).toHaveBeenCalledTimes(countAfterFailure);
  });

  it('rejects an invalid or already expired init-order lifetime', async () => {
    const fetchMock = vi.fn()
      .mockResolvedValueOnce(response({
        meta: { code: '200' },
        data: { access_token: 'sandbox-token', expires_in: 3600 },
      }))
      .mockResolvedValueOnce(response({
        meta: { code: '200' },
        data: {
          bill_id: 'GPAY-BILL-0001',
          bill_url: 'https://sandbox.g-pay.vn/pay/GPAY-BILL-0001',
          expired_time: '2026-08-01T15:59:59.000Z',
          request_id: 'YSIM-ORDER-0001',
        },
      }));
    await expect(client(fetchMock).initOrder({
      amount: 338000,
      callbackUrl: 'https://sandbox.ysim.vn/payment/return',
      customerId: 'customer-0001',
      embedData: '{"orderId":"order-0001"}',
      merchantOrderId: 'YSIM-ORDER-0001',
      webhookUrl: 'https://sandbox.ysim.vn/api/r1/payments/gpay/webhook',
    })).rejects.toThrow(/future ISO timestamp/u);
  });
});
