import type {
  GPayGatewayNormalizedStatus,
} from './gpay.gateway.types.js';

export type GPayGatewaySessionStatus =
  | 'NEW'
  | 'INIT_ATTEMPTED'
  | 'INITIALIZED'
  | 'PENDING'
  | 'SUCCEEDED'
  | 'FAILED'
  | 'CANCELLED'
  | 'EXPIRED';

export interface GPayGatewaySessionState {
  runNamespace: string;
  paymentIntentId: string;
  merchantOrderId: string;
  status: GPayGatewaySessionStatus;
  initAttemptCount: 0 | 1;
  billId?: string;
  evidenceFingerprints: readonly string[];
}

export class GPayGatewaySessionPolicyError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'GPayGatewaySessionPolicyError';
  }
}

const freeze = (
  state: GPayGatewaySessionState,
): GPayGatewaySessionState => Object.freeze({
  ...state,
  evidenceFingerprints: Object.freeze([
    ...state.evidenceFingerprints,
  ]),
});

export const createGPayGatewaySession = (
  input: Pick<
    GPayGatewaySessionState,
    'runNamespace' | 'paymentIntentId' | 'merchantOrderId'
  >,
): GPayGatewaySessionState => freeze({
  ...input,
  status: 'NEW',
  initAttemptCount: 0,
  evidenceFingerprints: [],
});

export const beginGPayGatewayInitAttempt = (
  current: GPayGatewaySessionState,
): GPayGatewaySessionState => {
  if (current.status !== 'NEW' || current.initAttemptCount !== 0) {
    throw new GPayGatewaySessionPolicyError(
      'GPay init-order external-effect budget is already consumed',
    );
  }
  return freeze({
    ...current,
    status: 'INIT_ATTEMPTED',
    initAttemptCount: 1,
  });
};

export const bindGPayGatewayInitResult = (
  current: GPayGatewaySessionState,
  billId: string,
): GPayGatewaySessionState => {
  if (
    current.status !== 'INIT_ATTEMPTED' ||
    current.initAttemptCount !== 1 ||
    !billId.trim()
  ) {
    throw new GPayGatewaySessionPolicyError(
      'GPay init-order result cannot be bound to this session',
    );
  }
  return freeze({
    ...current,
    status: 'INITIALIZED',
    billId: billId.trim(),
  });
};

const sessionStatus = (
  status: GPayGatewayNormalizedStatus,
): Exclude<GPayGatewaySessionStatus, 'NEW' | 'INIT_ATTEMPTED' | 'INITIALIZED'> => {
  switch (status) {
    case 'SUCCESS':
      return 'SUCCEEDED';
    case 'FAILED':
      return 'FAILED';
    case 'CANCELLED':
      return 'CANCELLED';
    case 'EXPIRED':
      return 'EXPIRED';
    case 'PENDING':
      return 'PENDING';
  }
};

export const applyGPayGatewayEvidence = (
  current: GPayGatewaySessionState,
  input: {
    billId: string;
    normalizedStatus: GPayGatewayNormalizedStatus;
    evidenceFingerprint: string;
  },
): GPayGatewaySessionState => {
  if (
    current.initAttemptCount !== 1 ||
    !current.billId ||
    current.billId !== input.billId
  ) {
    throw new GPayGatewaySessionPolicyError(
      'GPay authoritative evidence does not match the bound bill',
    );
  }
  if (!/^[0-9a-f]{64}$/u.test(input.evidenceFingerprint)) {
    throw new GPayGatewaySessionPolicyError(
      'GPay authoritative evidence fingerprint is invalid',
    );
  }
  if (current.evidenceFingerprints.includes(input.evidenceFingerprint)) {
    return current;
  }
  if (
    current.status === 'SUCCEEDED' ||
    current.status === 'FAILED' ||
    current.status === 'CANCELLED' ||
    current.status === 'EXPIRED'
  ) {
    throw new GPayGatewaySessionPolicyError(
      'GPay authoritative evidence conflicts with the terminal session',
    );
  }
  return freeze({
    ...current,
    status: sessionStatus(input.normalizedStatus),
    evidenceFingerprints: [
      ...current.evidenceFingerprints,
      input.evidenceFingerprint,
    ],
  });
};
