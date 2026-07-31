import { describe, expect, it } from 'vitest';

import {
  buildProcurementRequest,
  createProcurementRequestFingerprint,
  ProcurementRequestPolicyError,
  type ProcurementSourceSnapshot,
} from '../../apps/api/src/modules/procurement/domain/procurement-request-policy.js';

const occurredAt = '2026-07-31T03:00:00.000Z';
const event = {
  eventId: '10000000-0000-4000-8000-000000000015',
  eventType: 'payment.succeeded.v1' as const,
  aggregateType: 'PaymentIntent' as const,
  aggregateId: '20000000-0000-4000-8000-000000000015',
  orderId: '30000000-0000-4000-8000-000000000015',
  deduplicationKey: 'a'.repeat(64),
  payload: {
    paymentIntentId: '20000000-0000-4000-8000-000000000015',
    orderId: '30000000-0000-4000-8000-000000000015',
    orderNumber: 'YS-20260731-015ABCDEF015',
    provider: 'GPAY' as const,
    providerReference: 'GPY-20000000000040008000000000000015',
    amountMinor: '338000',
    currency: 'VND' as const,
    occurredAt,
  },
  occurredAt,
};

const source: ProcurementSourceSnapshot = {
  orderId: event.orderId,
  orderNumber: event.payload.orderNumber,
  productOfferId: '40000000-0000-4000-8000-000000000015',
  quantity: 2,
  totalAmountMinor: '338000',
  currency: 'VND',
  orderStatus: 'CONFIRMED',
  orderPaymentStatus: 'PAID',
  fulfillmentStatus: 'UNFULFILLED',
  supplierPlanMappingId: '50000000-0000-4000-8000-000000000015',
  supplierEnvironmentId: '60000000-0000-4000-8000-000000000015',
  supplierPlanId: '70000000-0000-4000-8000-000000000015',
  supplierCode: 'GIGAGO',
  supplierEnvironment: 'SANDBOX',
  supplierContractStatus: 'PROBED',
  supplierCreateOrderMethod: 'PUT',
  externalPlanId: 'GIGAGO_JP_FIXED_5GB_7D',
};

describe('Procurement Request policy', () => {
  it('builds a pending sandbox request', () => {
    const request = buildProcurementRequest(event, source);
    expect(request.status).toBe('PENDING_SUPPLIER');
    expect(request.supplierEnvironment).toBe('SANDBOX');
    expect(request.quantity).toBe(2);
  });

  it('creates a stable SHA-256 fingerprint', () => {
    const request = buildProcurementRequest(event, source);
    expect(request.requestFingerprint).toMatch(/^[0-9a-f]{64}$/u);
    expect(request.requestFingerprint).toBe(
      createProcurementRequestFingerprint({
        ...request,
        requestFingerprint: undefined,
      } as never),
    );
  });

  it('rejects an order identity mismatch', () => {
    expect(() => buildProcurementRequest(event, {
      ...source,
      orderId: '30000000-0000-4000-8000-000000000016',
    })).toThrow(ProcurementRequestPolicyError);
  });

  it('rejects an amount mismatch', () => {
    expect(() => buildProcurementRequest(event, {
      ...source,
      totalAmountMinor: '337999',
    })).toThrow('Payment amount or currency');
  });

  it('rejects a currency mismatch', () => {
    expect(() => buildProcurementRequest(event, {
      ...source,
      currency: 'USD',
    })).toThrow('Payment amount or currency');
  });

  it('requires a confirmed paid unfulfilled order', () => {
    expect(() => buildProcurementRequest(event, {
      ...source,
      fulfillmentStatus: 'FULFILLED',
    })).toThrow('Order is not ready');
  });

  it('blocks production supplier environments', () => {
    expect(() => buildProcurementRequest(event, {
      ...source,
      supplierEnvironment: 'PRODUCTION',
    })).toThrow('not approved for sandbox procurement');
  });

  it('requires a probed supplier contract', () => {
    expect(() => buildProcurementRequest(event, {
      ...source,
      supplierContractStatus: 'DOCUMENTED_UNVERIFIED',
    })).toThrow('not approved for sandbox procurement');
  });

  it('requires the accepted create-order method', () => {
    expect(() => buildProcurementRequest(event, {
      ...source,
      supplierCreateOrderMethod: 'POST',
    })).toThrow('not approved for sandbox procurement');
  });

  it('rejects an invalid procurement quantity', () => {
    expect(() => buildProcurementRequest(event, {
      ...source,
      quantity: 21,
    })).toThrow('quantity is invalid');
  });
});
