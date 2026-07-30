import {
  generateKeyPairSync,
} from 'node:crypto';
import {
  mkdtemp,
  rm,
  writeFile,
} from 'node:fs/promises';
import { createServer } from 'node:http';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

import { afterEach, describe, expect, it } from 'vitest';

import {
  GPayClient,
  GPayClientError,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.client.js';
import {
  canonicalGPayProbeRequest,
  canonicalGPayProbeResponse,
  signGPayCanonical,
  stableGPayJson,
  verifyGPayCanonical,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.crypto.js';

const generatedDirectories: string[] = [];
const openServers: Array<ReturnType<typeof createServer>> = [];

const pair = () => generateKeyPairSync('rsa', {
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

const prepareFixture = async (mode: 'SUCCESS' | 'BAD_SIGNATURE' | 'BAD_ID' | 'TIMEOUT') => {
  const merchant = pair();
  const provider = pair();
  const directory = await mkdtemp(join(tmpdir(), 'ysim-gpay-test-'));
  generatedDirectories.push(directory);
  const privatePath = join(directory, 'merchant-private.pem');
  const certificatePath = join(directory, 'merchant-public.pem');
  const verifyPath = join(directory, 'provider-public.pem');
  await Promise.all([
    writeFile(privatePath, merchant.privateKey),
    writeFile(certificatePath, merchant.publicKey),
    writeFile(verifyPath, provider.publicKey),
  ]);

  let verifiedRequest = false;
  let certificateHeaderPresent = false;
  const server = createServer(async (request, response) => {
    const chunks: Buffer[] = [];
    for await (const chunk of request) {
      chunks.push(Buffer.from(chunk));
    }
    const raw = Buffer.concat(chunks).toString('utf8');
    const body = JSON.parse(raw) as {
      requestId: string;
      profile: 'GATEWAY_V1';
    };
    const requestId = String(request.headers['x-requests-id']);
    const timestamp = String(request.headers['x-timestamp']);
    const signature = String(request.headers['x-signature']);
    certificateHeaderPresent = typeof request.headers['x-certificate'] === 'string';
    verifiedRequest = verifyGPayCanonical(
      canonicalGPayProbeRequest({
        requestId,
        timestamp,
        path: '/v1/contract/probe',
        body: JSON.parse(raw),
      }),
      signature,
      merchant.publicKey,
    );

    if (mode === 'TIMEOUT') {
      await new Promise((resolve) => setTimeout(resolve, 1200));
      response.destroy();
      return;
    }

    const responseTimestamp = new Date().toISOString();
    const responseBody = {
      accepted: true as const,
      profile: 'GATEWAY_V1' as const,
      requestId: mode === 'BAD_ID' ? 'different-request-id' : body.requestId,
      respondedAt: responseTimestamp,
      providerNonce: 'provider-nonce-00000001',
    };
    const canonical = canonicalGPayProbeResponse({
      requestId,
      timestamp: responseTimestamp,
      body: responseBody,
    });
    const responseSignature = signGPayCanonical(
      canonical,
      mode === 'BAD_SIGNATURE' ? merchant.privateKey : provider.privateKey,
    );
    response.writeHead(200, {
      'content-type': 'application/json',
      'x-requests-id': requestId,
      'x-timestamp': responseTimestamp,
      'x-signature': responseSignature,
    });
    response.end(stableGPayJson(responseBody));
  });
  openServers.push(server);
  await new Promise<void>((resolve) => server.listen(0, '127.0.0.1', resolve));
  const address = server.address();
  if (!address || typeof address === 'string') throw new Error('No port');

  Object.assign(process.env, {
    YSIM_GPAY_ENABLED: 'true',
    YSIM_GPAY_ENVIRONMENT: 'SANDBOX',
    YSIM_GPAY_CONTRACT_STATUS: 'PROBED',
    YSIM_GPAY_CONTRACT_PROFILE: 'GATEWAY_V1',
    YSIM_GPAY_BASE_URL: `http://127.0.0.1:${address.port}/v1`,
    YSIM_GPAY_PROBE_PATH: '/contract/probe',
    YSIM_GPAY_CLIENT_ID: 'ysim-client-0001',
    YSIM_GPAY_PRIVATE_KEY_PATH: privatePath,
    YSIM_GPAY_CERTIFICATE_PATH: certificatePath,
    YSIM_GPAY_VERIFY_CERTIFICATE_PATH: verifyPath,
    YSIM_GPAY_REQUEST_TIMEOUT_MS: mode === 'TIMEOUT' ? '1000' : '5000',
  });

  return {
    verifiedRequest: () => verifiedRequest,
    certificateHeaderPresent: () => certificateHeaderPresent,
  };
};

afterEach(async () => {
  while (openServers.length > 0) {
    const server = openServers.pop();
    if (server) await new Promise<void>((resolve) => server.close(() => resolve()));
  }
  while (generatedDirectories.length > 0) {
    const directory = generatedDirectories.pop();
    if (directory) await rm(directory, { recursive: true, force: true });
  }
});

describe('GPay contract probe client', () => {
  it('executes a signed probe and verifies the provider response', async () => {
    const fixture = await prepareFixture('SUCCESS');
    const result = await new GPayClient().probe();
    expect(result.requestSigned).toBe(true);
    expect(result.responseSignatureVerified).toBe(true);
    expect(result.environment).toBe('SANDBOX');
    expect(fixture.verifiedRequest()).toBe(true);
  });

  it('sends the merchant certificate without returning it', async () => {
    const fixture = await prepareFixture('SUCCESS');
    const result = await new GPayClient().probe();
    expect(fixture.certificateHeaderPresent()).toBe(true);
    expect(result).not.toHaveProperty('certificate');
    expect(result).not.toHaveProperty('signature');
  });

  it('rejects an invalid provider response signature', async () => {
    await prepareFixture('BAD_SIGNATURE');
    await expect(new GPayClient().probe())
      .rejects.toThrow(/signature verification failed/u);
  });

  it('rejects a mismatched response request identifier', async () => {
    await prepareFixture('BAD_ID');
    await expect(new GPayClient().probe())
      .rejects.toThrow(/identifier does not match/u);
  });

  it('fails closed when the provider probe times out', async () => {
    await prepareFixture('TIMEOUT');
    await expect(new GPayClient().probe())
      .rejects.toBeInstanceOf(GPayClientError);
  });

  it('returns only the approved safe probe fields', async () => {
    await prepareFixture('SUCCESS');
    const result = await new GPayClient().probe();

    expect(Object.keys(result).sort()).toEqual([
      'contractStatus',
      'endpointOrigin',
      'environment',
      'merchantCertificateLoaded',
      'probedAt',
      'profile',
      'providerVerificationCertificateLoaded',
      'requestId',
      'requestSigned',
      'responseSignatureVerified',
    ].sort());

    expect(result.requestSigned).toBe(true);
    expect(result.responseSignatureVerified).toBe(true);
    expect(result.merchantCertificateLoaded).toBe(true);
    expect(result.providerVerificationCertificateLoaded).toBe(true);
    expect(result.endpointOrigin).toMatch(/^http:\/\/127\.0\.0\.1:/u);
    expect(result.requestId).toMatch(
      /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu,
    );
    expect(Number.isNaN(Date.parse(result.probedAt))).toBe(false);

    for (const forbiddenProperty of [
      'privateKey',
      'privateKeyPem',
      'certificate',
      'certificatePem',
      'providerCertificate',
      'providerCertificatePem',
      'signature',
      'signatureBase64',
      'rawPayload',
      'credential',
      'clientId',
      'providerNonce',
    ]) {
      expect(result).not.toHaveProperty(forbiddenProperty);
    }

    const serialized = JSON.stringify(result);
    expect(serialized).not.toMatch(
      /-----BEGIN [A-Z0-9 ]+-----|-----END [A-Z0-9 ]+-----/u,
    );
  });
});
