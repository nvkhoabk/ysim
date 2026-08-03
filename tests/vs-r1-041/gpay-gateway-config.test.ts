import { resolve } from 'node:path';

import { describe, expect, it } from 'vitest';

import {
  GPAY_INIT_ORDER_PATH,
  GPAY_QUERY_ORDER_PATH,
  GPAY_SANDBOX_BASE_URL,
  GPAY_TOKEN_PATH,
  GPayGatewayConfigError,
  joinGPayGatewayUrl,
  loadGPayGatewayConfig,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.gateway.config.js';

const environment = (): Record<string, string> => ({
  YSIM_GPAY_ENABLED: 'true',
  YSIM_GPAY_ENVIRONMENT: 'SANDBOX',
  YSIM_GPAY_CONTRACT_STATUS: 'BOUND',
  YSIM_GPAY_BASE_URL: GPAY_SANDBOX_BASE_URL,
  YSIM_GPAY_CLIENT_ID: 'ysim-client-0001',
  YSIM_GPAY_CLIENT_SECRET_PATH: resolve('/tmp/gpay-client-secret'),
  YSIM_GPAY_PRIVATE_KEY_PATH: resolve('/tmp/gpay-private.pem'),
  YSIM_GPAY_CERTIFICATE_PATH: resolve('/tmp/gpay-certificate.pem'),
  YSIM_GPAY_VERIFY_CERTIFICATE_PATH: resolve('/tmp/gpay-provider.pem'),
});

describe('GPay All-in-one gateway configuration', () => {
  it('pins the confirmed sandbox paths', () => {
    const root = loadGPayGatewayConfig(environment()).baseUrl;
    expect(joinGPayGatewayUrl(root, GPAY_TOKEN_PATH).toString())
      .toBe('https://openapi-sandbox.g-pay.vn/v1/auth/token');
    expect(joinGPayGatewayUrl(root, GPAY_INIT_ORDER_PATH).pathname)
      .toBe('/v1/payments/gateway/init-order');
    expect(joinGPayGatewayUrl(root, GPAY_QUERY_ORDER_PATH).pathname)
      .toBe('/v1/payments/gateway/query-order');
  });

  it('requires explicit enablement and BOUND status', () => {
    const disabled = environment();
    disabled.YSIM_GPAY_ENABLED = 'false';
    expect(() => loadGPayGatewayConfig(disabled))
      .toThrow(GPayGatewayConfigError);

    const unverified = environment();
    unverified.YSIM_GPAY_CONTRACT_STATUS = 'UNVERIFIED';
    expect(() => loadGPayGatewayConfig(unverified))
      .toThrow(/BOUND/u);
  });

  it('blocks production and endpoint substitution', () => {
    const production = environment();
    production.YSIM_GPAY_ENVIRONMENT = 'PRODUCTION';
    expect(() => loadGPayGatewayConfig(production))
      .toThrow(/SANDBOX/u);

    const substitute = environment();
    substitute.YSIM_GPAY_BASE_URL = 'https://example.test/v1';
    expect(() => loadGPayGatewayConfig(substitute))
      .toThrow(/confirmed GPay sandbox/u);
  });

  it('permits loopback only with both test gates', () => {
    const fixture = environment();
    fixture.NODE_ENV = 'test';
    fixture.YSIM_GPAY_TEST_ALLOW_LOOPBACK = 'true';
    fixture.YSIM_GPAY_BASE_URL = 'http://127.0.0.1:3109/v1';
    expect(loadGPayGatewayConfig(fixture).baseUrl.origin)
      .toBe('http://127.0.0.1:3109');
  });
});
