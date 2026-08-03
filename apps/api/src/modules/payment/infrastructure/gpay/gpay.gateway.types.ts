export type GPayGatewayEnvironment = 'SANDBOX';
export type GPayGatewayContractStatus = 'BOUND';

export interface GPayGatewayConfig {
  enabled: true;
  environment: GPayGatewayEnvironment;
  contractStatus: GPayGatewayContractStatus;
  baseUrl: URL;
  clientId: string;
  clientSecretPath: string;
  privateKeyPath: string;
  certificatePath: string;
  verifyCertificatePath: string;
  requestTimeoutMs: number;
  tokenRefreshBufferSeconds: number;
}

export interface GPayGatewayMeta {
  code?: string | number;
  msg?: string;
  message?: string;
  internal_msg?: string;
}

export interface GPayGatewayInitOrderInput {
  amount: number;
  callbackUrl: string;
  customerId: string;
  embedData: string;
  merchantOrderId: string;
  webhookUrl: string;
  address?: string;
  customerName?: string;
  description?: string;
  email?: string;
  paymentMethod?: string;
  phone?: string;
  title?: string;
}

export interface GPayGatewayInitOrderResult {
  provider: 'GPAY';
  billId: string;
  billUrl: string;
  expiredTime: string;
  merchantOrderId: string;
  securityRequestId: string;
  tokenCached: boolean;
}

export interface GPayGatewayQueryOrderInput {
  gpayBillId: string;
  merchantOrderId: string;
}

export interface GPayGatewayQueryOrderResult {
  provider: 'GPAY';
  gpayBillId: string;
  merchantOrderId: string;
  gpayTransactionId?: string;
  status?: string;
  userPaymentMethod?: string;
  embedData?: string;
  securityRequestId: string;
  tokenCached: boolean;
}

export interface GPayGatewayCallbackData {
  merchantOrderId: string;
  gpayTransactionId: string;
  gpayBillId: string;
  status: string;
  embedData: string;
  userPaymentMethod: string;
  signature: string;
}

export type GPayGatewayNormalizedStatus =
  | 'SUCCESS'
  | 'FAILED'
  | 'CANCELLED'
  | 'EXPIRED'
  | 'PENDING';

export interface VerifiedGPayGatewayCallback {
  verified: true;
  contractVersion: 'GPAY_ALL_IN_ONE_CALLBACK_V1';
  merchantOrderId: string;
  gpayBillId: string;
  gpayTransactionId: string | undefined;
  normalizedStatus: GPayGatewayNormalizedStatus;
  userPaymentMethod: string | undefined;
  canonicalSha256: string;
}
