import { describe, expect, it, vi } from 'vitest';

import { resolveOperatorPortalAccess } from '../../apps/web/lib/operator-access';
import {
  OPERATOR_SESSION_AUDIENCE,
  OPERATOR_SESSION_VERSION,
  createOperatorSessionToken,
} from '../../apps/web/lib/operator-session';
import { operatorEnv, operatorSecret } from './fixtures';

const now = Math.floor(Date.now() / 1_000);
const payload = {
  version: OPERATOR_SESSION_VERSION,
  audience: OPERATOR_SESSION_AUDIENCE,
  identityId: operatorEnv.YSIM_OPERATOR_IDENTITY_ID,
  role: 'OPERATIONS' as const,
  locale: 'vi' as const,
  revocationVersion: 7,
  issuedAt: now - 30,
  expiresAt: now + 3600,
};

const cookieReader = (token: string) =>
  vi.fn(async () => ({ get: () => ({ value: token }) }));

describe('VS-R1-040 operator session revocation', () => {
  it('accepts a session matching the current credential contract', async () => {
    const token = createOperatorSessionToken(payload, operatorSecret);
    await expect(
      resolveOperatorPortalAccess(operatorEnv, cookieReader(token)),
    ).resolves.toEqual({ authorized: true, session: payload });
  });

  it('revokes all existing sessions when the environment version increments', async () => {
    const token = createOperatorSessionToken(payload, operatorSecret);
    await expect(
      resolveOperatorPortalAccess(
        { ...operatorEnv, YSIM_OPERATOR_REVOCATION_VERSION: '8' },
        cookieReader(token),
      ),
    ).resolves.toEqual({ authorized: false, reason: 'SESSION_REVOKED' });
  });

  it('revokes a session when the configured role changes', async () => {
    const token = createOperatorSessionToken(payload, operatorSecret);
    await expect(
      resolveOperatorPortalAccess(
        { ...operatorEnv, YSIM_OPERATOR_ROLE: 'PLATFORM_ADMIN' },
        cookieReader(token),
      ),
    ).resolves.toEqual({ authorized: false, reason: 'SESSION_REVOKED' });
  });

  it('rejects an expired session before protected content is read', async () => {
    const token = createOperatorSessionToken(
      { ...payload, issuedAt: now - 120, expiresAt: now - 1 },
      operatorSecret,
    );
    await expect(
      resolveOperatorPortalAccess(operatorEnv, cookieReader(token)),
    ).resolves.toEqual({ authorized: false, reason: 'SESSION_INVALID' });
  });
});
