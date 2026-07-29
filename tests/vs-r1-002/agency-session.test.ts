import { describe, expect, it } from 'vitest';

import {
  createAgencySessionToken,
  verifyAgencySessionToken,
} from '../../apps/web/lib/agency-session';

const secret = 'test-secret-that-is-long-enough-for-hmac-signing';
const payload = {
  identityId: '10000000-0000-4000-8000-000000000010',
  organizationId: '10000000-0000-4000-8000-000000000020',
  locale: 'vi' as const,
  expiresAt: 2_000_000_000,
};

describe('agency session token', () => {
  it('round-trips a valid signed session', () => {
    const token = createAgencySessionToken(payload, secret);
    expect(verifyAgencySessionToken(token, secret, 1_900_000_000)).toEqual(
      payload,
    );
  });

  it('rejects a modified token', () => {
    const token = createAgencySessionToken(payload, secret);
    const modified = `${token.slice(0, -1)}x`;

    expect(
      verifyAgencySessionToken(modified, secret, 1_900_000_000),
    ).toBeNull();
  });

  it('rejects an expired token', () => {
    const token = createAgencySessionToken(payload, secret);

    expect(
      verifyAgencySessionToken(token, secret, payload.expiresAt),
    ).toBeNull();
  });

  it('requires a sufficiently strong server secret', () => {
    expect(() => createAgencySessionToken(payload, 'short')).toThrow(
      /at least 32 characters/u,
    );
  });
});
