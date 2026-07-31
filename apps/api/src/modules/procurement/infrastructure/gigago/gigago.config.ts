export class GigagoConfigError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'GigagoConfigError';
  }
}

export interface GigagoCreateOrderConfig {
  environment: 'SANDBOX';
  baseUrl: string;
  apiKey: string;
  endpoint: '/api/partner/createPartnerOrder';
  method: 'PUT';
  timeoutMs: number;
}

type Environment =
  Record<string, string | undefined>;

const SANDBOX_BASE_URL =
  'https://sandbox-partners-api.gigago.com';

export const loadGigagoCreateOrderConfig = (
  environment: Environment = process.env,
): GigagoCreateOrderConfig => {
  const enabled =
    environment.YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED ===
    'true';
  const target =
    environment.YSIM_GIGAGO_ENVIRONMENT;
  const contractStatus =
    environment.YSIM_GIGAGO_CONTRACT_STATUS;
  const baseUrl =
    environment.YSIM_GIGAGO_BASE_URL ??
    SANDBOX_BASE_URL;
  const apiKey =
    environment.GIGAGO_SANDBOX_API_KEY;
  const timeoutValue =
    environment.YSIM_GIGAGO_TIMEOUT_MS ??
    '10000';
  const timeoutMs = Number(timeoutValue);

  if (!enabled) {
    throw new GigagoConfigError(
      'Gigago order submission is disabled',
    );
  }
  if (target !== 'SANDBOX') {
    throw new GigagoConfigError(
      'Only SANDBOX Gigago submission is allowed',
    );
  }
  if (contractStatus !== 'PROBED') {
    throw new GigagoConfigError(
      'Gigago sandbox contract must be PROBED',
    );
  }
  if (baseUrl !== SANDBOX_BASE_URL) {
    throw new GigagoConfigError(
      'Gigago sandbox base URL is not allowlisted',
    );
  }
  if (
    typeof apiKey !== 'string' ||
    apiKey.trim().length < 20
  ) {
    throw new GigagoConfigError(
      'GIGAGO_SANDBOX_API_KEY is required',
    );
  }
  if (
    !Number.isInteger(timeoutMs) ||
    timeoutMs < 1000 ||
    timeoutMs > 30000
  ) {
    throw new GigagoConfigError(
      'YSIM_GIGAGO_TIMEOUT_MS must be 1000..30000',
    );
  }

  return {
    environment: 'SANDBOX',
    baseUrl,
    apiKey: apiKey.trim(),
    endpoint:
      '/api/partner/createPartnerOrder',
    method: 'PUT',
    timeoutMs,
  };
};
