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
  issuedAt: now - 60,
  expiresAt: now + 3_600,
};

function signUntrustedPayload(payload: unknown): string {
  const encodedPayload = Buffer.from(JSON.stringify(payload), 'utf8').toString(
    'base64url',
  );
  const signature = createHmac('sha256', secret)
    .update('ysim:operator-session:v1\0')
    .update(encodedPayload)
    .digest('base64url');
  return `${encodedPayload}.${signature}`;
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

  it('rejects a modified signature', () => {
    const token = createOperatorSessionToken(basePayload, secret);
    const modified = `${token.slice(0, -1)}x`;
    expect(verifyOperatorSessionToken(modified, secret, now)).toBeNull();
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
