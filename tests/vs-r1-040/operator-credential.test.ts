import { describe, expect, it } from 'vitest';

import {
  authenticateOperatorCredentials,
  normalizeOperatorLoginId,
  readOperatorCredentialConfig,
} from '../../apps/web/lib/operator-credential';
import {
  operatorConfig,
  operatorEnv,
  operatorPassword,
} from './fixtures';

describe('VS-R1-040 operator credential verification', () => {
  it('loads the bounded environment-backed operator identity', () => {
    expect(readOperatorCredentialConfig(operatorEnv)).toEqual(operatorConfig);
  });

  it('normalizes the login identifier without changing the configured identity', () => {
    expect(normalizeOperatorLoginId('  Operations@Example.Test ')).toBe(
      'operations@example.test',
    );
  });

  it('authenticates the configured scrypt credential', async () => {
    await expect(
      authenticateOperatorCredentials(
        'Operations@Example.Test',
        operatorPassword,
        operatorEnv,
      ),
    ).resolves.toEqual({ authenticated: true, config: operatorConfig });
  });

  it.each([
    ['wrong login', 'other@example.test', operatorPassword],
    ['wrong password', operatorEnv.YSIM_OPERATOR_LOGIN_ID, 'not-the-password'],
  ])('returns one generic result for %s', async (_label, loginId, password) => {
    await expect(
      authenticateOperatorCredentials(loginId, password, operatorEnv),
    ).resolves.toEqual({
      authenticated: false,
      reason: 'INVALID_CREDENTIALS',
    });
  });

  it.each([
    ['missing hash', { ...operatorEnv, YSIM_OPERATOR_PASSWORD_SCRYPT: '' }],
    ['short secret', { ...operatorEnv, YSIM_PORTAL_SESSION_SECRET: 'short' }],
    ['unsupported role', { ...operatorEnv, YSIM_OPERATOR_ROLE: 'AGENCY_ADMIN' }],
    ['zero revocation version', { ...operatorEnv, YSIM_OPERATOR_REVOCATION_VERSION: '0' }],
    ['excessive TTL', { ...operatorEnv, YSIM_OPERATOR_SESSION_TTL_SECONDS: '28801' }],
  ])('fails closed for %s', async (_label, env) => {
    expect(readOperatorCredentialConfig(env)).toBeNull();
    await expect(
      authenticateOperatorCredentials(
        operatorEnv.YSIM_OPERATOR_LOGIN_ID,
        operatorPassword,
        env,
      ),
    ).resolves.toEqual({ authenticated: false, reason: 'CONFIG_INVALID' });
  });
});
