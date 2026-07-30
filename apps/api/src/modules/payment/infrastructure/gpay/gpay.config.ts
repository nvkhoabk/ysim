import { isAbsolute } from 'node:path';

import type {
  GPayContractProfile,
  GPayContractStatus,
  GPayEnvironment,
  GPayProbeConfig,
} from './gpay.types.js';

export class GPayConfigError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'GPayConfigError';
  }
}

type Environment = Record<string, string | undefined>;

const required = (
  environment: Environment,
  name: string,
): string => {
  const value = environment[name]?.trim();
  if (!value) {
    throw new GPayConfigError(`${name} is required`);
  }
  return value;
};

const environmentValue = (
  value: string,
): GPayEnvironment => {
  if (value !== 'SANDBOX' && value !== 'PRODUCTION') {
    throw new GPayConfigError(
      'YSIM_GPAY_ENVIRONMENT must be SANDBOX or PRODUCTION',
    );
  }
  return value;
};

const contractStatusValue = (
  value: string,
): GPayContractStatus => {
  if (value !== 'UNVERIFIED' && value !== 'PROBED') {
    throw new GPayConfigError(
      'YSIM_GPAY_CONTRACT_STATUS must be UNVERIFIED or PROBED',
    );
  }
  return value;
};

const profileValue = (
  value: string,
): GPayContractProfile => {
  if (value !== 'GATEWAY_V1') {
    throw new GPayConfigError(
      'YSIM_GPAY_CONTRACT_PROFILE must be GATEWAY_V1',
    );
  }
  return value;
};

const absolutePath = (
  environment: Environment,
  name: string,
): string => {
  const value = required(environment, name);
  if (!isAbsolute(value)) {
    throw new GPayConfigError(`${name} must be an absolute path`);
  }
  return value;
};

const timeoutValue = (value: string | undefined): number => {
  const parsed = Number(value ?? '15000');
  if (!Number.isInteger(parsed) || parsed < 1000 || parsed > 30000) {
    throw new GPayConfigError(
      'YSIM_GPAY_REQUEST_TIMEOUT_MS must be an integer from 1000 to 30000',
    );
  }
  return parsed;
};

const probePathValue = (value: string): string => {
  if (
    !value.startsWith('/') ||
    value.includes('..') ||
    value.includes('?') ||
    value.includes('#')
  ) {
    throw new GPayConfigError(
      'YSIM_GPAY_PROBE_PATH must be an absolute URL path without traversal or query data',
    );
  }
  return value.replace(/\/{2,}/gu, '/');
};

const baseUrlValue = (value: string): URL => {
  let parsed: URL;
  try {
    parsed = new URL(value);
  } catch {
    throw new GPayConfigError('YSIM_GPAY_BASE_URL must be a valid URL');
  }

  const loopback =
    parsed.hostname === '127.0.0.1' ||
    parsed.hostname === 'localhost' ||
    parsed.hostname === '::1';

  if (parsed.protocol !== 'https:' && !(loopback && parsed.protocol === 'http:')) {
    throw new GPayConfigError(
      'YSIM_GPAY_BASE_URL must use HTTPS except for loopback contract tests',
    );
  }

  if (parsed.username || parsed.password || parsed.search || parsed.hash) {
    throw new GPayConfigError(
      'YSIM_GPAY_BASE_URL must not include credentials, query data, or fragments',
    );
  }

  return parsed;
};

export const joinGPayUrl = (
  baseUrl: URL,
  path: string,
): URL => {
  const normalizedBase = new URL(baseUrl.toString());
  normalizedBase.pathname = normalizedBase.pathname.replace(/\/$/u, '');
  const normalizedPath = probePathValue(path);
  normalizedBase.pathname = `${normalizedBase.pathname}${normalizedPath}`
    .replace(/\/{2,}/gu, '/');
  return normalizedBase;
};

export const loadGPayProbeConfig = (
  environment: Environment = process.env,
): GPayProbeConfig => {
  if (environment.YSIM_GPAY_ENABLED !== 'true') {
    throw new GPayConfigError('GPay adapter is disabled');
  }

  const gpayEnvironment = environmentValue(
    required(environment, 'YSIM_GPAY_ENVIRONMENT'),
  );
  if (gpayEnvironment === 'PRODUCTION') {
    throw new GPayConfigError(
      'GPay production activation is blocked in VS-R1-009',
    );
  }

  const contractStatus = contractStatusValue(
    required(environment, 'YSIM_GPAY_CONTRACT_STATUS'),
  );
  if (contractStatus !== 'PROBED') {
    throw new GPayConfigError(
      'GPay contract must be PROBED before adapter execution',
    );
  }

  const clientId = required(environment, 'YSIM_GPAY_CLIENT_ID');
  if (clientId.length < 8 || clientId.length > 100) {
    throw new GPayConfigError(
      'YSIM_GPAY_CLIENT_ID must contain 8 to 100 characters',
    );
  }

  return {
    enabled: true,
    environment: gpayEnvironment,
    contractStatus,
    profile: profileValue(
      environment.YSIM_GPAY_CONTRACT_PROFILE ?? 'GATEWAY_V1',
    ),
    baseUrl: baseUrlValue(required(environment, 'YSIM_GPAY_BASE_URL')),
    probePath: probePathValue(
      environment.YSIM_GPAY_PROBE_PATH ?? '/contract/probe',
    ),
    clientId,
    privateKeyPath: absolutePath(
      environment,
      'YSIM_GPAY_PRIVATE_KEY_PATH',
    ),
    certificatePath: absolutePath(
      environment,
      'YSIM_GPAY_CERTIFICATE_PATH',
    ),
    verifyCertificatePath: absolutePath(
      environment,
      'YSIM_GPAY_VERIFY_CERTIFICATE_PATH',
    ),
    requestTimeoutMs: timeoutValue(
      environment.YSIM_GPAY_REQUEST_TIMEOUT_MS,
    ),
  };
};
