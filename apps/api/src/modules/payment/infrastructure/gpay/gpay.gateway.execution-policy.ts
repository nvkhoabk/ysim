type Environment = Record<string, string | undefined>;

export class GPayGatewayExecutionPolicyError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'GPayGatewayExecutionPolicyError';
  }
}

export interface GPayGatewayExecutionPolicy {
  mode: 'SANDBOX';
  runNamespace: string;
  transactionCap: 1;
  queryCap: number;
  market: 'VN';
  currency: 'VND';
  callbackUrl: string;
  webhookUrl: string;
  customerId: string;
  gpayExecutionEnabled: true;
  gigagoSubmitEnabled: false;
  customerEmailEnabled: false;
}

const required = (
  environment: Environment,
  name: string,
): string => {
  const value = environment[name]?.trim();
  if (!value) {
    throw new GPayGatewayExecutionPolicyError(
      `${name} is required for VS-R1-043`,
    );
  }
  return value;
};

const requireExact = (
  environment: Environment,
  name: string,
  expected: string,
): void => {
  if (required(environment, name) !== expected) {
    throw new GPayGatewayExecutionPolicyError(
      `${name} must be ${expected} for VS-R1-043`,
    );
  }
};

const queryCap = (
  value: string | undefined,
): number => {
  const parsed = Number(value ?? '12');
  if (!Number.isInteger(parsed) || parsed < 1 || parsed > 20) {
    throw new GPayGatewayExecutionPolicyError(
      'YSIM_GPAY_QUERY_CAP must be an integer from 1 to 20',
    );
  }
  return parsed;
};

const publicGPayUrl = (
  environment: Environment,
  name: string,
  expectedSuffix: string,
): string => {
  let parsed: URL;
  try {
    parsed = new URL(required(environment, name));
  } catch {
    throw new GPayGatewayExecutionPolicyError(
      `${name} must be a valid URL`,
    );
  }
  if (
    parsed.protocol !== 'https:' ||
    parsed.hostname !== 'portal.ysim.vn' ||
    parsed.username ||
    parsed.password ||
    parsed.search ||
    parsed.hash ||
    !parsed.pathname.endsWith(expectedSuffix)
  ) {
    throw new GPayGatewayExecutionPolicyError(
      `${name} is outside the VS-R1-043 public callback boundary`,
    );
  }
  return parsed.toString();
};

export const loadGPayGatewayExecutionPolicy = (
  environment: Environment = process.env,
): GPayGatewayExecutionPolicy => {
  requireExact(environment, 'YSIM_COMMISSIONING_MODE', 'SANDBOX');
  requireExact(environment, 'YSIM_COMMISSIONING_TRANSACTION_CAP', '1');
  requireExact(environment, 'YSIM_COMMISSIONING_MARKET', 'VN');
  requireExact(environment, 'YSIM_COMMISSIONING_CURRENCY', 'VND');
  requireExact(environment, 'YSIM_GPAY_EXECUTION_ENABLED', 'true');
  requireExact(
    environment,
    'YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED',
    'false',
  );
  requireExact(environment, 'YSIM_CUSTOMER_EMAIL_ENABLED', 'false');
  requireExact(environment, 'YSIM_CUSTOMER_EMAIL_MODE', 'disabled');
  requireExact(
    environment,
    'YSIM_CATALOG_SUPPLIER_ENVIRONMENT',
    'SANDBOX',
  );

  const runNamespace = required(
    environment,
    'YSIM_COMMISSIONING_RUN_NAMESPACE',
  );
  if (!/^vs-r1-043-[a-z0-9-]{8,64}$/u.test(runNamespace)) {
    throw new GPayGatewayExecutionPolicyError(
      'YSIM_COMMISSIONING_RUN_NAMESPACE is invalid for VS-R1-043',
    );
  }

  const customerId = required(
    environment,
    'YSIM_GPAY_COMMISSIONING_CUSTOMER_ID',
  );
  if (!/^vs-r1-043-[a-z0-9-]{4,48}$/u.test(customerId)) {
    throw new GPayGatewayExecutionPolicyError(
      'YSIM_GPAY_COMMISSIONING_CUSTOMER_ID is invalid',
    );
  }

  return {
    mode: 'SANDBOX',
    runNamespace,
    transactionCap: 1,
    queryCap: queryCap(environment.YSIM_GPAY_QUERY_CAP),
    market: 'VN',
    currency: 'VND',
    callbackUrl: publicGPayUrl(
      environment,
      'YSIM_GPAY_CALLBACK_URL',
      '/api/r1/payments/gpay/gateway/callback',
    ),
    webhookUrl: publicGPayUrl(
      environment,
      'YSIM_GPAY_WEBHOOK_URL',
      '/api/r1/payments/gpay/gateway/webhook',
    ),
    customerId,
    gpayExecutionEnabled: true,
    gigagoSubmitEnabled: false,
    customerEmailEnabled: false,
  };
};
