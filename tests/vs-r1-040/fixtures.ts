import type { OperatorCredentialConfig } from '../../apps/web/lib/operator-credential';

export const operatorSecret =
  'test-secret-that-is-long-enough-for-hmac-signing';
export const operatorPassword = 'correct horse battery staple';
export const operatorPasswordHash =
  'scrypt$16384$8$1$MDEyMzQ1Njc4OWFiY2RlZg$tjK03tRvEjqCcPwmgtddMkgjlXrk8U_b9rIvfeBMKCc';

export const operatorEnv = {
  YSIM_OPERATOR_IDENTITY_ID: '10000000-0000-4000-8000-000000000040',
  YSIM_OPERATOR_LOCALE: 'vi',
  YSIM_OPERATOR_LOGIN_ID: 'operations@example.test',
  YSIM_OPERATOR_PASSWORD_SCRYPT: operatorPasswordHash,
  YSIM_OPERATOR_REVOCATION_VERSION: '7',
  YSIM_OPERATOR_ROLE: 'OPERATIONS',
  YSIM_OPERATOR_SESSION_TTL_SECONDS: '3600',
  YSIM_PORTAL_SESSION_SECRET: operatorSecret,
};

export const operatorConfig: OperatorCredentialConfig = {
  identityId: operatorEnv.YSIM_OPERATOR_IDENTITY_ID,
  locale: 'vi',
  loginId: operatorEnv.YSIM_OPERATOR_LOGIN_ID,
  passwordHash: operatorPasswordHash,
  revocationVersion: 7,
  role: 'OPERATIONS',
  sessionSecret: operatorSecret,
  sessionTtlSeconds: 3600,
};
