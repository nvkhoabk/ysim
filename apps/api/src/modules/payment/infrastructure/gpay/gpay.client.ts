import { randomBytes, randomUUID } from 'node:crypto';
import { readFile } from 'node:fs/promises';

import { Injectable } from '@nestjs/common';

import {
  joinGPayUrl,
  loadGPayProbeConfig,
} from './gpay.config.js';
import {
  assertGPayKeyPair,
  canonicalGPayProbeRequest,
  canonicalGPayProbeResponse,
  safeGPayEqual,
  signGPayCanonical,
  stableGPayJson,
  verifyGPayCanonical,
} from './gpay.crypto.js';
import type {
  GPayProbeEnvelope,
  GPayProbeProviderResponse,
  GPaySafeProbeResult,
} from './gpay.types.js';

export class GPayClientError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'GPayClientError';
  }
}

const responseHeader = (
  headers: Headers,
  name: string,
): string => {
  const value = headers.get(name)?.trim();
  if (!value) {
    throw new GPayClientError(
      `GPay response header ${name} is required`,
    );
  }
  return value;
};

const parseProviderResponse = (
  value: unknown,
): GPayProbeProviderResponse => {
  if (typeof value !== 'object' || value === null) {
    throw new GPayClientError('GPay probe response must be an object');
  }
  const record = value as Record<string, unknown>;
  if (
    record.accepted !== true ||
    record.profile !== 'GATEWAY_V1' ||
    typeof record.requestId !== 'string' ||
    typeof record.respondedAt !== 'string' ||
    typeof record.providerNonce !== 'string' ||
    record.providerNonce.length < 16
  ) {
    throw new GPayClientError('GPay probe response is invalid');
  }
  return {
    accepted: true,
    profile: 'GATEWAY_V1',
    requestId: record.requestId,
    respondedAt: record.respondedAt,
    providerNonce: record.providerNonce,
  };
};

@Injectable()
export class GPayClient {
  async probe(): Promise<GPaySafeProbeResult> {
    const config = loadGPayProbeConfig();
    const [privateKeyPem, merchantCertificatePem, providerCertificatePem] =
      await Promise.all([
        readFile(config.privateKeyPath, 'utf8'),
        readFile(config.certificatePath, 'utf8'),
        readFile(config.verifyCertificatePath, 'utf8'),
      ]).catch(() => {
        throw new GPayClientError(
          'GPay key or certificate file could not be loaded',
        );
      });

    assertGPayKeyPair(privateKeyPem, merchantCertificatePem);

    const requestId = randomUUID();
    const timestamp = new Date().toISOString();
    const body: GPayProbeEnvelope = {
      operation: 'CONTRACT_PROBE',
      profile: config.profile,
      requestId,
      clientId: config.clientId,
      requestedAt: timestamp,
      nonce: randomBytes(18).toString('base64url'),
    };
    const endpoint = joinGPayUrl(config.baseUrl, config.probePath);
    const canonical = canonicalGPayProbeRequest({
      requestId,
      timestamp,
      path: endpoint.pathname,
      body,
    });
    const signature = signGPayCanonical(canonical, privateKeyPem);

    const abortController = new AbortController();
    const timeout = setTimeout(() => {
      abortController.abort();
    }, config.requestTimeoutMs);

    let response: Response;
    try {
      response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'x-client-id': config.clientId,
          'x-requests-id': requestId,
          'x-timestamp': timestamp,
          'x-signature': signature,
          'x-certificate': Buffer.from(
            merchantCertificatePem,
            'utf8',
          ).toString('base64'),
        },
        body: stableGPayJson(body),
        signal: abortController.signal,
      });
    } catch (error) {
      if (
        error instanceof Error &&
        error.name === 'AbortError'
      ) {
        throw new GPayClientError('GPay contract probe timed out');
      }
      throw new GPayClientError('GPay contract probe request failed');
    } finally {
      clearTimeout(timeout);
    }

    if (!response.ok) {
      throw new GPayClientError(
        `GPay contract probe returned HTTP ${response.status}`,
      );
    }

    const responseBody = parseProviderResponse(
      await response.json().catch(() => null),
    );
    const responseRequestId = responseHeader(
      response.headers,
      'x-requests-id',
    );
    const responseTimestamp = responseHeader(
      response.headers,
      'x-timestamp',
    );
    const responseSignature = responseHeader(
      response.headers,
      'x-signature',
    );

    if (
      !safeGPayEqual(responseRequestId, requestId) ||
      !safeGPayEqual(responseBody.requestId, requestId)
    ) {
      throw new GPayClientError(
        'GPay response request identifier does not match',
      );
    }

    const responseCanonical = canonicalGPayProbeResponse({
      requestId,
      timestamp: responseTimestamp,
      body: responseBody,
    });
    if (!verifyGPayCanonical(
      responseCanonical,
      responseSignature,
      providerCertificatePem,
    )) {
      throw new GPayClientError(
        'GPay response signature verification failed',
      );
    }

    return {
      environment: 'SANDBOX',
      profile: config.profile,
      contractStatus: 'PROBED',
      endpointOrigin: endpoint.origin,
      requestSigned: true,
      responseSignatureVerified: true,
      merchantCertificateLoaded: true,
      providerVerificationCertificateLoaded: true,
      requestId,
      probedAt: new Date().toISOString(),
    };
  }
}
