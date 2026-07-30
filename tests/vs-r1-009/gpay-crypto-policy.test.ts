import {
  generateKeyPairSync,
} from 'node:crypto';
import { resolve } from 'node:path';

import { describe, expect, it } from 'vitest';

import {
  GPayConfigError,
  joinGPayUrl,
  loadGPayProbeConfig,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.config.js';
import {
  assertGPayKeyPair,
  canonicalGPayProbeRequest,
  GPayCryptoError,
  signGPayCanonical,
  stableGPayJson,
  verifyGPayCanonical,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.crypto.js';

const keyPair = () => generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: {
    type: 'spki',
    format: 'pem',
  },
  privateKeyEncoding: {
    type: 'pkcs8',
    format: 'pem',
  },
});

const validEnvironment = (): Record<string, string> => ({
  YSIM_GPAY_ENABLED: 'true',
  YSIM_GPAY_ENVIRONMENT: 'SANDBOX',
  YSIM_GPAY_CONTRACT_STATUS: 'PROBED',
  YSIM_GPAY_CONTRACT_PROFILE: 'GATEWAY_V1',
  YSIM_GPAY_BASE_URL: 'https://sandbox.example.test/v1',
  YSIM_GPAY_PROBE_PATH: '/contract/probe',
  YSIM_GPAY_CLIENT_ID: 'ysim-client-0001',
  YSIM_GPAY_PRIVATE_KEY_PATH: resolve('/tmp/ysim-gpay-private.pem'),
  YSIM_GPAY_CERTIFICATE_PATH: resolve('/tmp/ysim-gpay-cert.pem'),
  YSIM_GPAY_VERIFY_CERTIFICATE_PATH: resolve('/tmp/ysim-gpay-verify.pem'),
  YSIM_GPAY_REQUEST_TIMEOUT_MS: '15000',
});

describe('GPay adapter policy and crypto', () => {
  it('stable JSON canonicalizes object key order', () => {
    expect(stableGPayJson({ b: 2, a: 1 }))
      .toBe(stableGPayJson({ a: 1, b: 2 }));
  });

  it('creates a stable request canonical string', () => {
    const input = {
      requestId: '11111111-1111-4111-8111-111111111111',
      timestamp: '2026-07-30T12:00:00.000Z',
      path: '/contract/probe',
      body: {
        operation: 'CONTRACT_PROBE' as const,
        profile: 'GATEWAY_V1' as const,
        requestId: '11111111-1111-4111-8111-111111111111',
        clientId: 'ysim-client-0001',
        requestedAt: '2026-07-30T12:00:00.000Z',
        nonce: 'abcdefghijklmnop',
      },
    };
    expect(canonicalGPayProbeRequest(input))
      .toBe(canonicalGPayProbeRequest(input));
  });

  it('signs and verifies RSA-SHA256 canonical data', () => {
    const pair = keyPair();
    const signature = signGPayCanonical('canonical', pair.privateKey);
    expect(verifyGPayCanonical(
      'canonical',
      signature,
      pair.publicKey,
    )).toBe(true);
  });

  it('rejects a tampered canonical payload', () => {
    const pair = keyPair();
    const signature = signGPayCanonical('canonical', pair.privateKey);
    expect(verifyGPayCanonical(
      'tampered',
      signature,
      pair.publicKey,
    )).toBe(false);
  });

  it('accepts a matching merchant key pair', () => {
    const pair = keyPair();
    expect(() => assertGPayKeyPair(
      pair.privateKey,
      pair.publicKey,
    )).not.toThrow();
  });

  it('rejects a mismatched merchant key pair', () => {
    const first = keyPair();
    const second = keyPair();
    expect(() => assertGPayKeyPair(
      first.privateKey,
      second.publicKey,
    )).toThrow(GPayCryptoError);
  });

  it('requires explicit adapter enablement', () => {
    const environment = validEnvironment();
    environment.YSIM_GPAY_ENABLED = 'false';
    expect(() => loadGPayProbeConfig(environment))
      .toThrow(GPayConfigError);
  });

  it('blocks production activation in this slice', () => {
    const environment = validEnvironment();
    environment.YSIM_GPAY_ENVIRONMENT = 'PRODUCTION';
    expect(() => loadGPayProbeConfig(environment))
      .toThrow(/production activation is blocked/u);
  });

  it('requires a probed contract status', () => {
    const environment = validEnvironment();
    environment.YSIM_GPAY_CONTRACT_STATUS = 'UNVERIFIED';
    expect(() => loadGPayProbeConfig(environment))
      .toThrow(/must be PROBED/u);
  });

  it('rejects insecure non-loopback HTTP endpoints', () => {
    const environment = validEnvironment();
    environment.YSIM_GPAY_BASE_URL = 'http://sandbox.example.test';
    expect(() => loadGPayProbeConfig(environment))
      .toThrow(/must use HTTPS/u);
  });

  it('allows HTTP only for loopback runtime fixtures', () => {
    const environment = validEnvironment();
    environment.YSIM_GPAY_BASE_URL = 'http://127.0.0.1:3000/v1';
    expect(loadGPayProbeConfig(environment).baseUrl.origin)
      .toBe('http://127.0.0.1:3000');
  });

  it('joins base and probe paths without duplicate separators', () => {
    expect(joinGPayUrl(
      new URL('https://sandbox.example.test/v1/'),
      '/contract/probe',
    ).toString()).toBe(
      'https://sandbox.example.test/v1/contract/probe',
    );
  });
});
