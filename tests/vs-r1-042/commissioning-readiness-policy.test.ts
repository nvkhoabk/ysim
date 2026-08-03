import { describe, expect, it } from 'vitest';

import {
  CommissioningReadinessError,
  isCommissioningRecipientAllowed,
  loadCommissioningReadinessConfig,
} from '../../apps/api/src/modules/commissioning/domain/commissioning-readiness-policy.js';

const baseline = {
  YSIM_COMMISSIONING_MODE: 'SANDBOX',
  YSIM_COMMISSIONING_RUN_NAMESPACE: 'vs-r1-042-synthetic-a1b2c3d4',
  YSIM_COMMISSIONING_TRANSACTION_CAP: '1',
  YSIM_COMMISSIONING_EMAIL_ALLOWLIST: 'qa1@example.test,qa2@example.test,qa3@example.test',
  DATABASE_URL: 'postgresql://redacted',
  YSIM_REDIS_URL: 'redis://redacted',
  YSIM_GPAY_EXECUTION_ENABLED: 'false',
  YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED: 'false',
  YSIM_CUSTOMER_EMAIL_ENABLED: 'false',
  YSIM_CUSTOMER_EMAIL_MODE: 'disabled',
};

describe('VS-R1-042 commissioning readiness policy', () => {
  it('accepts one bounded sandbox run without exposing allowlist values', () => {
    const config = loadCommissioningReadinessConfig(baseline);
    expect(config).toMatchObject({
      mode: 'SANDBOX', transactionCap: 1, allowlistCount: 3,
      gpayExecutionEnabled: false, gigagoSubmitEnabled: false,
      customerEmailEnabled: false,
    });
    expect(config.allowlistFingerprint).toMatch(/^[a-f0-9]{64}$/);
    expect(JSON.stringify(config)).not.toContain('qa1@example.test');
  });

  it.each([
    'YSIM_GPAY_EXECUTION_ENABLED',
    'YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED',
    'YSIM_CUSTOMER_EMAIL_ENABLED',
  ])('fails closed when %s is enabled', (name) => {
    expect(() => loadCommissioningReadinessConfig({ ...baseline, [name]: 'true' }))
      .toThrow(CommissioningReadinessError);
  });

  it('requires exactly three unique allowlisted recipients', () => {
    expect(() => loadCommissioningReadinessConfig({
      ...baseline,
      YSIM_COMMISSIONING_EMAIL_ALLOWLIST: 'qa1@example.test,qa1@example.test',
    })).toThrow(CommissioningReadinessError);
  });

  it('rejects recipients outside the allowlist before provider use', () => {
    expect(isCommissioningRecipientAllowed('qa2@example.test', baseline)).toBe(true);
    expect(isCommissioningRecipientAllowed('customer@example.test', baseline)).toBe(false);
  });
});
