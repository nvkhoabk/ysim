import { createHash } from 'node:crypto';

import {
  loadCommissioningReadinessConfig,
} from '../domain/commissioning-readiness-policy.js';
import {
  createPaymentSucceededIntegrationEvent,
} from '../../payment/domain/payment-integration-event.js';
import {
  parseClaimedPaymentIntegrationEvent,
} from '../../payment/domain/payment-outbox-policy.js';
import {
  buildProcurementRequest,
  type ProcurementSourceSnapshot,
} from '../../procurement/domain/procurement-request-policy.js';

type Environment = Record<string, string | undefined>;

export interface CommissioningSyntheticCheckpoint {
  schemaVersion: 1;
  sliceId: 'VS-R1-042';
  proofKind: 'SYNTHETIC_ORDER_OUTBOX';
  runNamespace: string;
  correlationId: string;
  transactionCount: 1;
  order: {
    id: string;
    number: string;
    status: 'CONFIRMED';
    paymentStatus: 'PAID';
    fulfillmentStatus: 'UNFULFILLED';
  };
  payment: {
    intentId: string;
    provider: 'TEST';
    status: 'SUCCEEDED';
  };
  outbox: {
    eventId: string;
    eventType: 'payment.succeeded.v1';
    aggregateId: string;
    deduplicationKey: string;
    syntheticClaimAttemptCount: 1;
    consumerResult: 'PENDING_SUPPLIER';
  };
  procurement: {
    requestId: string;
    requestFingerprint: string;
    supplierEnvironment: 'SANDBOX';
    status: 'PENDING_SUPPLIER';
    quantity: 1;
  };
  allowlist: {
    count: number;
    fingerprint: string;
  };
  safety: {
    gpayExecutionEnabled: false;
    gigagoSubmitEnabled: false;
    customerEmailEnabled: false;
    databaseMutationPerformed: false;
    redisCommandsPerformed: false;
    externalProviderCalls: 0;
    customerEmailsSent: 0;
  };
  checkpointSha256: string;
}

const sha256 = (value: string): string =>
  createHash('sha256')
    .update(value, 'utf8')
    .digest('hex');

const deriveUuid = (
  runNamespace: string,
  label: string,
): string => {
  const hex = sha256(`${runNamespace}:${label}`)
    .slice(0, 32)
    .split('');
  hex[12] = '5';
  hex[16] = (
    (Number.parseInt(hex[16] ?? '0', 16) & 0x3) |
    0x8
  ).toString(16);
  const value = hex.join('');
  return [
    value.slice(0, 8),
    value.slice(8, 12),
    value.slice(12, 16),
    value.slice(16, 20),
    value.slice(20),
  ].join('-');
};

const freezeCheckpoint = (
  checkpoint: CommissioningSyntheticCheckpoint,
): CommissioningSyntheticCheckpoint => {
  Object.freeze(checkpoint.order);
  Object.freeze(checkpoint.payment);
  Object.freeze(checkpoint.outbox);
  Object.freeze(checkpoint.procurement);
  Object.freeze(checkpoint.allowlist);
  Object.freeze(checkpoint.safety);
  return Object.freeze(checkpoint);
};

export const runSyntheticOrderOutboxHarness = (
  env: Environment = process.env,
): CommissioningSyntheticCheckpoint => {
  const readiness = loadCommissioningReadinessConfig(env);
  const runNamespace = readiness.runNamespace;
  const occurredAt = '2026-08-04T00:00:00.000Z';
  const orderId = deriveUuid(runNamespace, 'order');
  const paymentIntentId = deriveUuid(
    runNamespace,
    'payment-intent',
  );
  const eventId = deriveUuid(runNamespace, 'outbox-event');
  const orderNumber = `YS-20260804-${sha256(
    `${runNamespace}:order-number`,
  ).slice(0, 12).toUpperCase()}`;

  const paymentEvent =
    createPaymentSucceededIntegrationEvent({
      eventId,
      paymentIntentId,
      orderId,
      orderNumber,
      provider: 'TEST',
      providerReference:
        `SYNTHETIC-${paymentIntentId}`,
      amountMinor: '1000',
      currency: 'VND',
      occurredAt,
    });

  const claimedEvent =
    parseClaimedPaymentIntegrationEvent({
      id: paymentEvent.eventId,
      eventType: paymentEvent.eventType,
      aggregateType: paymentEvent.aggregateType,
      aggregateId: paymentEvent.aggregateId,
      orderId: paymentEvent.orderId,
      deduplicationKey:
        paymentEvent.deduplicationKey,
      payload: paymentEvent.payload,
      occurredAt: paymentEvent.occurredAt,
      attemptCount: 1,
    });

  const source: ProcurementSourceSnapshot = {
    orderId,
    orderNumber,
    productOfferId: deriveUuid(
      runNamespace,
      'product-offer',
    ),
    quantity: 1,
    totalAmountMinor: '1000',
    currency: 'VND',
    orderStatus: 'CONFIRMED',
    orderPaymentStatus: 'PAID',
    fulfillmentStatus: 'UNFULFILLED',
    supplierPlanMappingId: deriveUuid(
      runNamespace,
      'supplier-plan-mapping',
    ),
    supplierEnvironmentId: deriveUuid(
      runNamespace,
      'supplier-environment',
    ),
    supplierPlanId: deriveUuid(
      runNamespace,
      'supplier-plan',
    ),
    supplierCode: 'GIGAGO',
    supplierEnvironment: 'SANDBOX',
    supplierContractStatus: 'PROBED',
    supplierCreateOrderMethod: 'PUT',
    externalPlanId: 'SYNTHETIC_VS_R1_042',
  };
  const procurement = buildProcurementRequest(
    claimedEvent,
    source,
  );

  const checkpointWithoutHash = {
    schemaVersion: 1 as const,
    sliceId: 'VS-R1-042' as const,
    proofKind: 'SYNTHETIC_ORDER_OUTBOX' as const,
    runNamespace,
    correlationId: deriveUuid(
      runNamespace,
      'correlation',
    ),
    transactionCount: 1 as const,
    order: {
      id: orderId,
      number: orderNumber,
      status: 'CONFIRMED' as const,
      paymentStatus: 'PAID' as const,
      fulfillmentStatus: 'UNFULFILLED' as const,
    },
    payment: {
      intentId: paymentIntentId,
      provider: 'TEST' as const,
      status: 'SUCCEEDED' as const,
    },
    outbox: {
      eventId: claimedEvent.eventId,
      eventType: claimedEvent.eventType,
      aggregateId: claimedEvent.aggregateId,
      deduplicationKey:
        claimedEvent.deduplicationKey,
      syntheticClaimAttemptCount: 1 as const,
      consumerResult: procurement.status,
    },
    procurement: {
      requestId: deriveUuid(
        runNamespace,
        'procurement-request',
      ),
      requestFingerprint:
        procurement.requestFingerprint,
      supplierEnvironment:
        procurement.supplierEnvironment,
      status: procurement.status,
      quantity: 1 as const,
    },
    allowlist: {
      count: readiness.allowlistCount,
      fingerprint:
        readiness.allowlistFingerprint,
    },
    safety: {
      gpayExecutionEnabled:
        readiness.gpayExecutionEnabled,
      gigagoSubmitEnabled:
        readiness.gigagoSubmitEnabled,
      customerEmailEnabled:
        readiness.customerEmailEnabled,
      databaseMutationPerformed: false as const,
      redisCommandsPerformed: false as const,
      externalProviderCalls: 0 as const,
      customerEmailsSent: 0 as const,
    },
  };
  const checkpoint: CommissioningSyntheticCheckpoint = {
    ...checkpointWithoutHash,
    checkpointSha256: sha256(
      JSON.stringify(checkpointWithoutHash),
    ),
  };

  return freezeCheckpoint(checkpoint);
};
