import {
  createHash,
  createSign,
  createVerify,
  timingSafeEqual,
} from 'node:crypto';

import type {
  GPayProbeEnvelope,
  GPayProbeProviderResponse,
} from './gpay.types.js';

export class GPayCryptoError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'GPayCryptoError';
  }
}

const normalizeJson = (value: unknown): unknown => {
  if (Array.isArray(value)) {
    return value.map(normalizeJson);
  }
  if (typeof value === 'object' && value !== null) {
    const record = value as Record<string, unknown>;
    return Object.fromEntries(
      Object.keys(record)
        .sort()
        .map((key) => [key, normalizeJson(record[key])]),
    );
  }
  return value;
};

export const stableGPayJson = (value: unknown): string =>
  JSON.stringify(normalizeJson(value));

export const sha256GPayHex = (value: string): string =>
  createHash('sha256').update(value, 'utf8').digest('hex');

export const canonicalGPayProbeRequest = (input: {
  requestId: string;
  timestamp: string;
  path: string;
  body: GPayProbeEnvelope;
}): string => [
  input.timestamp,
  input.requestId,
  'POST',
  input.path,
  sha256GPayHex(stableGPayJson(input.body)),
].join('\n');

export const canonicalGPayProbeResponse = (input: {
  requestId: string;
  timestamp: string;
  body: GPayProbeProviderResponse;
}): string => [
  input.timestamp,
  input.requestId,
  sha256GPayHex(stableGPayJson(input.body)),
].join('\n');

export const signGPayCanonical = (
  canonical: string,
  privateKeyPem: string,
): string => {
  try {
    const signer = createSign('RSA-SHA256');
    signer.update(canonical, 'utf8');
    signer.end();
    return signer.sign(privateKeyPem, 'base64');
  } catch {
    throw new GPayCryptoError('GPay canonical signing failed');
  }
};

export const verifyGPayCanonical = (
  canonical: string,
  signatureBase64: string,
  certificateOrPublicKeyPem: string,
): boolean => {
  try {
    const verifier = createVerify('RSA-SHA256');
    verifier.update(canonical, 'utf8');
    verifier.end();
    return verifier.verify(
      certificateOrPublicKeyPem,
      signatureBase64,
      'base64',
    );
  } catch {
    return false;
  }
};

export const assertGPayKeyPair = (
  privateKeyPem: string,
  certificateOrPublicKeyPem: string,
): void => {
  const challenge = 'ysim-gpay-key-pair-check-vs-r1-009';
  const signature = signGPayCanonical(challenge, privateKeyPem);
  if (!verifyGPayCanonical(
    challenge,
    signature,
    certificateOrPublicKeyPem,
  )) {
    throw new GPayCryptoError(
      'GPay private key does not match merchant certificate/public key',
    );
  }
};

export const safeGPayEqual = (
  left: string,
  right: string,
): boolean => {
  const leftBuffer = Buffer.from(left, 'utf8');
  const rightBuffer = Buffer.from(right, 'utf8');
  return leftBuffer.length === rightBuffer.length &&
    timingSafeEqual(leftBuffer, rightBuffer);
};
