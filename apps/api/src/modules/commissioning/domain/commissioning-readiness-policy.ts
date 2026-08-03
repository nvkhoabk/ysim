import { createHash } from 'node:crypto';

export class CommissioningReadinessError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'CommissioningReadinessError';
  }
}

type Environment = Record<string, string | undefined>;

export interface CommissioningReadinessConfig {
  mode: 'SANDBOX';
  runNamespace: string;
  transactionCap: 1;
  allowlistCount: number;
  allowlistFingerprint: string;
  postgresConfigured: boolean;
  redisConfigured: boolean;
  gpayExecutionEnabled: false;
  gigagoSubmitEnabled: false;
  customerEmailEnabled: false;
}

const requireFalse = (env: Environment, name: string): false => {
  const value = (env[name] ?? 'false').trim().toLowerCase();
  if (value !== 'false') {
    throw new CommissioningReadinessError(`${name} must be false for VS-R1-042`);
  }
  return false;
};

const normalizeAllowlist = (value: string | undefined): string[] => {
  const entries = (value ?? '')
    .split(',')
    .map((entry) => entry.trim().toLowerCase())
    .filter(Boolean);
  if (entries.length !== 3 || new Set(entries).size !== 3) {
    throw new CommissioningReadinessError(
      'YSIM_COMMISSIONING_EMAIL_ALLOWLIST must contain exactly three unique addresses',
    );
  }
  for (const entry of entries) {
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(entry)) {
      throw new CommissioningReadinessError('Commissioning email allowlist is invalid');
    }
  }
  return entries.sort();
};

export const loadCommissioningReadinessConfig = (
  env: Environment = process.env,
): CommissioningReadinessConfig => {
  if (env.YSIM_COMMISSIONING_MODE !== 'SANDBOX') {
    throw new CommissioningReadinessError('YSIM_COMMISSIONING_MODE must be SANDBOX');
  }
  const runNamespace = (env.YSIM_COMMISSIONING_RUN_NAMESPACE ?? '').trim();
  if (!/^vs-r1-042-[a-z0-9-]{8,64}$/.test(runNamespace)) {
    throw new CommissioningReadinessError('YSIM_COMMISSIONING_RUN_NAMESPACE is invalid');
  }
  if (env.YSIM_COMMISSIONING_TRANSACTION_CAP !== '1') {
    throw new CommissioningReadinessError('YSIM_COMMISSIONING_TRANSACTION_CAP must be 1');
  }
  if (!env.DATABASE_URL) {
    throw new CommissioningReadinessError('DATABASE_URL is required');
  }
  if (!env.YSIM_REDIS_URL) {
    throw new CommissioningReadinessError('YSIM_REDIS_URL is required');
  }
  if ((env.YSIM_CUSTOMER_EMAIL_MODE ?? 'disabled').trim().toLowerCase() !== 'disabled') {
    throw new CommissioningReadinessError('YSIM_CUSTOMER_EMAIL_MODE must be disabled');
  }
  const allowlist = normalizeAllowlist(env.YSIM_COMMISSIONING_EMAIL_ALLOWLIST);
  return {
    mode: 'SANDBOX',
    runNamespace,
    transactionCap: 1,
    allowlistCount: allowlist.length,
    allowlistFingerprint: createHash('sha256').update(allowlist.join('\n')).digest('hex'),
    postgresConfigured: true,
    redisConfigured: true,
    gpayExecutionEnabled: requireFalse(env, 'YSIM_GPAY_EXECUTION_ENABLED'),
    gigagoSubmitEnabled: requireFalse(env, 'YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED'),
    customerEmailEnabled: requireFalse(env, 'YSIM_CUSTOMER_EMAIL_ENABLED'),
  };
};

export const isCommissioningRecipientAllowed = (
  recipient: string,
  env: Environment = process.env,
): boolean => normalizeAllowlist(env.YSIM_COMMISSIONING_EMAIL_ALLOWLIST)
  .includes(recipient.trim().toLowerCase());
