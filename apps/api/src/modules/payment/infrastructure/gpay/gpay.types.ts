export type GPayEnvironment = 'SANDBOX' | 'PRODUCTION';
export type GPayContractStatus = 'UNVERIFIED' | 'PROBED';
export type GPayContractProfile = 'GATEWAY_V1';

export interface GPayProbeConfig {
  enabled: boolean;
  environment: GPayEnvironment;
  contractStatus: GPayContractStatus;
  profile: GPayContractProfile;
  baseUrl: URL;
  probePath: string;
  clientId: string;
  privateKeyPath: string;
  certificatePath: string;
  verifyCertificatePath: string;
  requestTimeoutMs: number;
}

export interface GPayProbeEnvelope {
  operation: 'CONTRACT_PROBE';
  profile: GPayContractProfile;
  requestId: string;
  clientId: string;
  requestedAt: string;
  nonce: string;
}

export interface GPayProbeProviderResponse {
  accepted: boolean;
  profile: GPayContractProfile;
  requestId: string;
  respondedAt: string;
  providerNonce: string;
}

export interface GPaySafeProbeResult {
  environment: 'SANDBOX';
  profile: GPayContractProfile;
  contractStatus: 'PROBED';
  endpointOrigin: string;
  requestSigned: true;
  responseSignatureVerified: true;
  merchantCertificateLoaded: true;
  providerVerificationCertificateLoaded: true;
  requestId: string;
  probedAt: string;
}
