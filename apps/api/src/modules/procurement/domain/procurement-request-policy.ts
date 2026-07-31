import { createHash } from 'node:crypto';

import type {
  PaymentSucceededIntegrationEventV1,
  PricingCurrency,
} from '@ysim/contracts';

export class ProcurementRequestPolicyError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'ProcurementRequestPolicyError';
  }
}

export interface ProcurementSourceSnapshot {
  orderId: string;
  orderNumber: string;
  productOfferId: string;
  quantity: number;
  totalAmountMinor: string;
  currency: PricingCurrency;
  orderStatus: string;
  orderPaymentStatus: string;
  fulfillmentStatus: string;
  supplierPlanMappingId: string;
  supplierEnvironmentId: string;
  supplierPlanId: string;
  supplierCode: string;
  supplierEnvironment: 'SANDBOX' | 'PRODUCTION';
  supplierContractStatus: string;
  supplierCreateOrderMethod: string;
  externalPlanId: string;
}

export interface CreateProcurementRequestInput {
  sourceEventId: string;
  paymentIntentId: string;
  orderId: string;
  orderNumber: string;
  productOfferId: string;
  supplierPlanMappingId: string;
  supplierEnvironmentId: string;
  supplierPlanId: string;
  supplierCode: string;
  supplierEnvironment: 'SANDBOX';
  externalPlanId: string;
  quantity: number;
  status: 'PENDING_SUPPLIER';
  requestFingerprint: string;
  createdAt: string;
}

const UUID_PATTERN =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;
const ORDER_NUMBER_PATTERN =
  /^YS-[0-9]{8}-[0-9A-F]{12}$/u;
const SUPPLIER_CODE_PATTERN =
  /^[A-Z][A-Z0-9_-]{2,63}$/u;
const EXTERNAL_PLAN_PATTERN =
  /^[A-Z0-9][A-Z0-9_-]{2,127}$/u;
const AMOUNT_PATTERN = /^[0-9]{1,20}$/u;

const requireUuid = (
  value: string,
  field: string,
): string => {
  if (!UUID_PATTERN.test(value)) {
    throw new ProcurementRequestPolicyError(
      `${field} must be a UUID`,
    );
  }
  return value.toLowerCase();
};

const requireIso = (
  value: string,
  field: string,
): string => {
  const parsed = Date.parse(value);
  if (!Number.isFinite(parsed)) {
    throw new ProcurementRequestPolicyError(
      `${field} must be an ISO timestamp`,
    );
  }
  return new Date(parsed).toISOString();
};

const sha256 = (value: string): string =>
  createHash('sha256')
    .update(value, 'utf8')
    .digest('hex');

export const createProcurementRequestFingerprint = (
  input: Omit<
    CreateProcurementRequestInput,
    'requestFingerprint'
  >,
): string => sha256(JSON.stringify({
  sourceEventId: input.sourceEventId,
  paymentIntentId: input.paymentIntentId,
  orderId: input.orderId,
  orderNumber: input.orderNumber,
  productOfferId: input.productOfferId,
  supplierPlanMappingId:
    input.supplierPlanMappingId,
  supplierEnvironmentId:
    input.supplierEnvironmentId,
  supplierPlanId: input.supplierPlanId,
  supplierCode: input.supplierCode,
  supplierEnvironment:
    input.supplierEnvironment,
  externalPlanId: input.externalPlanId,
  quantity: input.quantity,
  status: input.status,
  createdAt: input.createdAt,
}));

export const buildProcurementRequest = (
  event: PaymentSucceededIntegrationEventV1,
  source: ProcurementSourceSnapshot,
): CreateProcurementRequestInput => {
  const eventId = requireUuid(
    event.eventId,
    'event.eventId',
  );
  const paymentIntentId = requireUuid(
    event.payload.paymentIntentId,
    'event.payload.paymentIntentId',
  );
  const orderId = requireUuid(
    event.payload.orderId,
    'event.payload.orderId',
  );
  const sourceOrderId = requireUuid(
    source.orderId,
    'source.orderId',
  );

  if (
    event.eventType !==
      'payment.succeeded.v1' ||
    event.aggregateType !==
      'PaymentIntent' ||
    event.aggregateId !== paymentIntentId ||
    event.orderId !== orderId
  ) {
    throw new ProcurementRequestPolicyError(
      'Payment Success envelope is inconsistent',
    );
  }

  if (
    orderId !== sourceOrderId ||
    event.payload.orderNumber !==
      source.orderNumber
  ) {
    throw new ProcurementRequestPolicyError(
      'Payment Success order does not match source order',
    );
  }

  if (
    !ORDER_NUMBER_PATTERN.test(
      source.orderNumber,
    )
  ) {
    throw new ProcurementRequestPolicyError(
      'Source order number is invalid',
    );
  }

  if (
    !AMOUNT_PATTERN.test(
      event.payload.amountMinor,
    ) ||
    event.payload.amountMinor !==
      source.totalAmountMinor ||
    event.payload.currency !==
      source.currency
  ) {
    throw new ProcurementRequestPolicyError(
      'Payment amount or currency does not match source order',
    );
  }

  if (
    source.orderStatus !== 'CONFIRMED' ||
    source.orderPaymentStatus !== 'PAID' ||
    source.fulfillmentStatus !== 'UNFULFILLED'
  ) {
    throw new ProcurementRequestPolicyError(
      'Order is not ready for procurement',
    );
  }

  if (
    source.supplierEnvironment !==
      'SANDBOX' ||
    source.supplierContractStatus !==
      'PROBED' ||
    source.supplierCreateOrderMethod !==
      'PUT'
  ) {
    throw new ProcurementRequestPolicyError(
      'Supplier mapping is not approved for sandbox procurement',
    );
  }

  if (
    !Number.isInteger(source.quantity) ||
    source.quantity < 1 ||
    source.quantity > 20
  ) {
    throw new ProcurementRequestPolicyError(
      'Procurement quantity is invalid',
    );
  }

  if (
    !SUPPLIER_CODE_PATTERN.test(
      source.supplierCode,
    ) ||
    !EXTERNAL_PLAN_PATTERN.test(
      source.externalPlanId,
    )
  ) {
    throw new ProcurementRequestPolicyError(
      'Supplier snapshot is invalid',
    );
  }

  const createdAt = requireIso(
    event.occurredAt,
    'event.occurredAt',
  );

  const withoutFingerprint = {
    sourceEventId: eventId,
    paymentIntentId,
    orderId,
    orderNumber: source.orderNumber,
    productOfferId: requireUuid(
      source.productOfferId,
      'source.productOfferId',
    ),
    supplierPlanMappingId: requireUuid(
      source.supplierPlanMappingId,
      'source.supplierPlanMappingId',
    ),
    supplierEnvironmentId: requireUuid(
      source.supplierEnvironmentId,
      'source.supplierEnvironmentId',
    ),
    supplierPlanId: requireUuid(
      source.supplierPlanId,
      'source.supplierPlanId',
    ),
    supplierCode: source.supplierCode,
    supplierEnvironment: 'SANDBOX' as const,
    externalPlanId: source.externalPlanId,
    quantity: source.quantity,
    status: 'PENDING_SUPPLIER' as const,
    createdAt,
  };

  return {
    ...withoutFingerprint,
    requestFingerprint:
      createProcurementRequestFingerprint(
        withoutFingerprint,
      ),
  };
};
