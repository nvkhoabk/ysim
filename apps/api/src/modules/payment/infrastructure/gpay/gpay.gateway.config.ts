import { isAbsolute } from 'node:path';

import type {
  GPayGatewayConfig,
} from './gpay.gateway.types.js';

type Environment = Record<string, string | undefined>;

export const GPAY_SANDBOX_BASE_URL =
  'https://openapi-sandbox.g-pay.vn/v1';
export const GPAY_TOKEN_PATH = '/auth/token';
export const GPAY_INIT_ORDER_PATH =
  '/payments/gateway/init-order';
export const GPAY_QUERY_ORDER_PATH =
  '/payments/gateway/query-order';

export class GPayGatewayConfigError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'GPayGatewayConfigError';
  }
}

const required = (
  environment: Environment,
  name: string,
): string => {
  const value = environment[name]?.trim();
  if (!value) {
    throw new GPayGatewayConfigError(`${name} is required`);
  }
  return value;
};

const absolutePath = (
  environment: Environment,
  name: string,
): string => {
  const value = required(environment, name);
  if (!isAbsolute(value)) {
    throw new GPayGatewayConfigError(`${name} must be an absolute path`);
  }
  return value;
};

const integer = (
  value: string | undefined,
  fallback: number,
  minimum: number,
  maximum: number,
  name: string,
): number => {
  const parsed = Number(value ?? String(fallback));
  if (
    !Number.isInteger(parsed) ||
    parsed < minimum ||
    parsed > maximum
  ) {
    throw new GPayGatewayConfigError(
      `${name} must be an integer from ${minimum} to ${maximum}`,
    );
  }
  return parsed;
};

const baseUrl = (
  environment: Environment,
): URL => {
  const raw = required(environment, 'YSIM_GPAY_BASE_URL');
  let parsed: URL;
  try {
    parsed = new URL(raw);
  } catch {
    throw new GPayGatewayConfigError(
      'YSIM_GPAY_BASE_URL must be a valid URL',
    );
  }

  if (
    parsed.username ||
    parsed.password ||
    parsed.search ||
    parsed.hash
  ) {
    throw new GPayGatewayConfigError(
      'YSIM_GPAY_BASE_URL must not include credentials, query data, or fragments',
    );
  }

  const normalized = parsed.toString().replace(/\/$/u, '');
  const loopback =
    parsed.hostname === '127.0.0.1' ||
    parsed.hostname === 'localhost' ||
    parsed.hostname === '::1';
  const testLoopback =
    environment.NODE_ENV === 'test' &&
    environment.YSIM_GPAY_TEST_ALLOW_LOOPBACK === 'true' &&
    loopback &&
    parsed.protocol === 'http:';

  if (normalized !== GPAY_SANDBOX_BASE_URL && !testLoopback) {
    throw new GPayGatewayConfigError(
      'YSIM_GPAY_BASE_URL must equal the confirmed GPay sandbox OpenAPI v1 URL',
    );
  }
  return parsed;
};

export const joinGPayGatewayUrl = (
  root: URL,
  path: string,
): URL => {
  const joined = new URL(root.toString());
  joined.pathname = `${joined.pathname.replace(/\/$/u, '')}${path}`;
  return joined;
};

export const loadGPayGatewayConfig = (
  environment: Environment = process.env,
): GPayGatewayConfig => {
  if (environment.YSIM_GPAY_ENABLED !== 'true') {
    throw new GPayGatewayConfigError('GPay gateway is disabled');
  }
  if (environment.YSIM_GPAY_ENVIRONMENT !== 'SANDBOX') {
    throw new GPayGatewayConfigError(
      'Only the GPay SANDBOX contract is bound in VS-R1-041',
    );
  }
  if (environment.YSIM_GPAY_CONTRACT_STATUS !== 'BOUND') {
    throw new GPayGatewayConfigError(
      'YSIM_GPAY_CONTRACT_STATUS must be BOUND',
    );
  }

  const clientId = required(environment, 'YSIM_GPAY_CLIENT_ID');
  if (clientId.length < 8 || clientId.length > 100) {
    throw new GPayGatewayConfigError(
      'YSIM_GPAY_CLIENT_ID must contain 8 to 100 characters',
    );
  }

  return {
    enabled: true,
    environment: 'SANDBOX',
    contractStatus: 'BOUND',
    baseUrl: baseUrl(environment),
    clientId,
    clientSecretPath: absolutePath(
      environment,
      'YSIM_GPAY_CLIENT_SECRET_PATH',
    ),
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
    requestTimeoutMs: integer(
      environment.YSIM_GPAY_REQUEST_TIMEOUT_MS,
      15_000,
      1_000,
      30_000,
      'YSIM_GPAY_REQUEST_TIMEOUT_MS',
    ),
    tokenRefreshBufferSeconds: integer(
      environment.YSIM_GPAY_TOKEN_REFRESH_BUFFER_SECONDS,
      120,
      30,
      600,
      'YSIM_GPAY_TOKEN_REFRESH_BUFFER_SECONDS',
    ),
  };
};
