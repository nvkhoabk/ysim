export type GPayContractProfile = 'GATEWAY_V1';
export type GPayContractStatus = 'PROBED';
export type GPayEnvironment = 'SANDBOX';

export interface GPaySafeContractProbe {
  environment: GPayEnvironment;
  profile: GPayContractProfile;
  contractStatus: GPayContractStatus;
  endpointOrigin: string;
  requestSigned: true;
  responseSignatureVerified: true;
  merchantCertificateLoaded: true;
  providerVerificationCertificateLoaded: true;
  requestId: string;
  probedAt: string;
}

export interface GPayContractProbeResponse {
  probe: GPaySafeContractProbe;
}
