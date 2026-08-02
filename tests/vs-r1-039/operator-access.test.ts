import { createHmac } from 'node:crypto';

import { describe, expect, it, vi } from 'vitest';

import { createAgencySessionToken } from '../../apps/web/lib/agency-session';
import { resolveOperatorPortalAccess } from '../../apps/web/lib/operator-access';
import {
  OPERATOR_SESSION_AUDIENCE,
  OPERATOR_SESSION_COOKIE,
  OPERATOR_SESSION_VERSION,
  createOperatorSessionToken,
} from '../../apps/web/lib/operator-session';

const secret = 'test-secret-that-is-long-enough-for-hmac-signing';
const now = Math.floor(Date.now() / 1000);
const payload = {
  version: OPERATOR_SESSION_VERSION,
  audience: OPERATOR_SESSION_AUDIENCE,
  identityId: '10000000-0000-4000-8000-000000000039',
  role: 'PLATFORM_ADMIN' as const,
  locale: 'vi' as const,
  issuedAt: now - 60,
  expiresAt: now + 3_600,
};

const cookieReader = (value?: string) =>
  vi.fn(async () => ({
    get: (name: string) =>
      name === OPERATOR_SESSION_COOKIE && value ? { value } : undefined,
  }));

function signedWrongRoleToken(): string {
  const encodedPayload = Buffer.from(
    JSON.stringify({ ...payload, role: 'AGENCY_ADMIN' }),
    'utf8',
  ).toString('base64url');
  const signature = createHmac('sha256', secret)
    .update('ysim:operator-session:v1\0')
    .update(encodedPayload)
    .digest('base64url');
  return `${encodedPayload}.${signature}`;
}

describe('VS-R1-039 operator access resolver', () => {
  it('fails closed before reading cookies when session configuration is absent', async () => {
    const readCookies = cookieReader();
    await expect(resolveOperatorPortalAccess({}, readCookies)).resolves.toEqual(
      { authorized: false, reason: 'CONFIG_INVALID' },
    );
    expect(readCookies).not.toHaveBeenCalled();
  });

  it('requires the dedicated operator cookie', async () => {
    await expect(
      resolveOperatorPortalAccess(
        { YSIM_PORTAL_SESSION_SECRET: secret },
        cookieReader(),
      ),
    ).resolves.toEqual({ authorized: false, reason: 'SESSION_REQUIRED' });
  });

  it('accepts a valid signed operator session', async () => {
    const token = createOperatorSessionToken(payload, secret);
    await expect(
      resolveOperatorPortalAccess(
        { YSIM_PORTAL_SESSION_SECRET: secret },
        cookieReader(token),
      ),
    ).resolves.toEqual({ authorized: true, session: payload });
  });

  it('rejects a tampered session', async () => {
    const token = createOperatorSessionToken(payload, secret);
    await expect(
      resolveOperatorPortalAccess(
        { YSIM_PORTAL_SESSION_SECRET: secret },
        cookieReader(`${token.slice(0, -1)}x`),
      ),
    ).resolves.toEqual({ authorized: false, reason: 'SESSION_INVALID' });
  });

  it('rejects a signed session with an agency role', async () => {
    await expect(
      resolveOperatorPortalAccess(
        { YSIM_PORTAL_SESSION_SECRET: secret },
        cookieReader(signedWrongRoleToken()),
      ),
    ).resolves.toEqual({ authorized: false, reason: 'SESSION_INVALID' });
  });

  it('does not accept the agency session cookie or token as operator access', async () => {
    const agencyToken = createAgencySessionToken(
      {
        identityId: payload.identityId,
        organizationId: '10000000-0000-4000-8000-000000000002',
        locale: 'vi',
        expiresAt: now + 3_600,
      },
      secret,
    );
    await expect(
      resolveOperatorPortalAccess(
        { YSIM_PORTAL_SESSION_SECRET: secret },
        cookieReader(agencyToken),
      ),
    ).resolves.toEqual({ authorized: false, reason: 'SESSION_INVALID' });
  });
});
