import { createHmac } from 'node:crypto';

import { describe, expect, it } from 'vitest';

import { createAgencySessionToken } from '../../apps/web/lib/agency-session';
import {
  OPERATOR_SESSION_AUDIENCE,
  OPERATOR_SESSION_MAX_TTL_SECONDS,
  OPERATOR_SESSION_VERSION,
  createOperatorSessionToken,
  verifyOperatorSessionToken,
} from '../../apps/web/lib/operator-session';

const secret = 'test-secret-that-is-long-enough-for-hmac-signing';
const now = 1_900_000_000;
const basePayload = {
  version: OPERATOR_SESSION_VERSION,
  audience: OPERATOR_SESSION_AUDIENCE,
  identityId: '10000000-0000-4000-8000-000000000039',
  role: 'OPERATIONS' as const,
  locale: 'vi' as const,
  revocationVersion: 1,
  issuedAt: now - 60,
  expiresAt: now + 3_600,
};
const base64UrlAlphabet =
  'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';

function signUntrustedPayload(payload: unknown): string {
  const encodedPayload = Buffer.from(JSON.stringify(payload), 'utf8').toString(
    'base64url',
  );
  const signature = createHmac('sha256', secret)
    .update('ysim:operator-session:v2\0')
    .update(encodedPayload)
    .digest('base64url');
  return `${encodedPayload}.${signature}`;
}

function tamperSignatureBytes(token: string): string {
  const [encodedPayload, encodedSignature] = token.split('.');
  if (!encodedPayload || !encodedSignature) {
    throw new Error('Expected a two-part operator session token');
  }

  const changedFirstCharacter = encodedSignature[0] === 'A' ? 'B' : 'A';
  return `${encodedPayload}.${changedFirstCharacter}${encodedSignature.slice(1)}`;
}

function makeSignatureEncodingNonCanonical(token: string): string {
  const [encodedPayload, encodedSignature] = token.split('.');
  if (!encodedPayload || !encodedSignature) {
    throw new Error('Expected a two-part operator session token');
  }

  const finalIndex = base64UrlAlphabet.indexOf(encodedSignature.at(-1) ?? '');
  if (finalIndex < 0 || finalIndex % 4 !== 0 || finalIndex === 63) {
    throw new Error('Expected a canonical 32-byte base64url signature');
  }

  const nonCanonicalSignature =
    encodedSignature.slice(0, -1) + base64UrlAlphabet[finalIndex + 1];
  if (
    !Buffer.from(nonCanonicalSignature, 'base64url').equals(
      Buffer.from(encodedSignature, 'base64url'),
    )
  ) {
    throw new Error('Expected an equivalent non-canonical signature encoding');
  }

  return `${encodedPayload}.${nonCanonicalSignature}`;
}

describe('VS-R1-039 operator session token', () => {
  it.each(['PLATFORM_ADMIN', 'OPERATIONS'] as const)(
    'round-trips an allowed %s session',
    (role) => {
      const payload = { ...basePayload, role };
      const token = createOperatorSessionToken(payload, secret);
      expect(verifyOperatorSessionToken(token, secret, now)).toEqual(payload);
    },
  );

  it('rejects modified signature bytes across different payload signatures', () => {
    for (let offset = 0; offset < 256; offset += 1) {
      const token = createOperatorSessionToken(
        {
          ...basePayload,
          issuedAt: basePayload.issuedAt - offset,
        },
        secret,
      );
      expect(
        verifyOperatorSessionToken(tamperSignatureBytes(token), secret, now),
      ).toBeNull();
    }
  });

  it('rejects a non-canonical encoding of the same signature bytes', () => {
    const token = createOperatorSessionToken(basePayload, secret);
    expect(
      verifyOperatorSessionToken(
        makeSignatureEncodingNonCanonical(token),
        secret,
        now,
      ),
    ).toBeNull();
  });

  it('rejects an expired session', () => {
    const token = createOperatorSessionToken(basePayload, secret);
    expect(
      verifyOperatorSessionToken(token, secret, basePayload.expiresAt),
    ).toBeNull();
  });

  it('rejects a correctly signed but unsupported role', () => {
    const token = signUntrustedPayload({
      ...basePayload,
      role: 'AGENCY_ADMIN',
    });
    expect(verifyOperatorSessionToken(token, secret, now)).toBeNull();
  });

  it('rejects an agency session even when both portals share the secret', () => {
    const agencyToken = createAgencySessionToken(
      {
        identityId: basePayload.identityId,
        organizationId: '10000000-0000-4000-8000-000000000002',
        locale: 'vi',
        expiresAt: now + 3_600,
      },
      secret,
    );
    expect(verifyOperatorSessionToken(agencyToken, secret, now)).toBeNull();
  });

  it('rejects a token issued too far in the future', () => {
    const token = createOperatorSessionToken(
      {
        ...basePayload,
        issuedAt: now + 61,
        expiresAt: now + 3_661,
      },
      secret,
    );
    expect(verifyOperatorSessionToken(token, secret, now)).toBeNull();
  });

  it('rejects an excessive session lifetime', () => {
    expect(() =>
      createOperatorSessionToken(
        {
          ...basePayload,
          expiresAt:
            basePayload.issuedAt + OPERATOR_SESSION_MAX_TTL_SECONDS + 1,
        },
        secret,
      ),
    ).toThrow(/payload is invalid/u);
  });

  it('requires a sufficiently strong server secret', () => {
    expect(() => createOperatorSessionToken(basePayload, 'short')).toThrow(
      /at least 32 characters/u,
    );
  });
});
