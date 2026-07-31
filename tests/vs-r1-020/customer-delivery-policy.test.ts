import {
  describe,
  expect,
  it,
} from 'vitest';

import {
  CustomerDeliveryPolicyError,
  normalizeCustomerDeliveryRequest,
  type CustomerDeliveryRequestInput,
} from '../../apps/api/src/modules/delivery/domain/customer-delivery-policy.js';

const input:
  CustomerDeliveryRequestInput = {
    salesOrderId:
      '10000000-0000-4000-8000-000000000020',
    orderNumber:
      'YS-20260731-020ABCDEF020',
    channel: 'EMAIL',
    locale: 'vi',
    deliveryVersion: 1,
    expectedAssetCount: 2,
    assetIds: [
      '20000000-0000-4000-8000-000000000020',
      '30000000-0000-4000-8000-000000000020',
    ],
    requestedAt:
      '2026-07-31T19:00:00.000Z',
  };

describe('Customer Delivery policy', () => {
  it('normalizes a safe email delivery request', () => {
    const result =
      normalizeCustomerDeliveryRequest(
        input,
      );

    expect(result).toMatchObject({
      salesOrderId:
        input.salesOrderId,
      orderNumber:
        input.orderNumber,
      channel: 'EMAIL',
      locale: 'vi',
      deliveryVersion: 1,
      expectedAssetCount: 2,
      requestedAt:
        '2026-07-31T19:00:00.000Z',
    });
    expect(result.assetIds)
      .toEqual(input.assetIds);
  });

  it('requires the exact Asset count', () => {
    expect(() =>
      normalizeCustomerDeliveryRequest({
        ...input,
        expectedAssetCount: 1,
      }),
    ).toThrow(
      'Delivery Asset count mismatch',
    );
  });

  it('rejects duplicated Asset IDs', () => {
    expect(() =>
      normalizeCustomerDeliveryRequest({
        ...input,
        assetIds: [
          input.assetIds[0],
          input.assetIds[0],
        ],
      }),
    ).toThrow(
      'Delivery Asset ID is duplicated',
    );
  });

  it('rejects an invalid Asset UUID', () => {
    expect(() =>
      normalizeCustomerDeliveryRequest({
        ...input,
        assetIds: [
          'invalid',
          input.assetIds[1],
        ],
      }),
    ).toThrow(
      CustomerDeliveryPolicyError,
    );
  });

  it('rejects an invalid order number', () => {
    expect(() =>
      normalizeCustomerDeliveryRequest({
        ...input,
        orderNumber: 'ORDER-20',
      }),
    ).toThrow(
      'orderNumber is invalid',
    );
  });

  it('rejects an unsupported locale', () => {
    expect(() =>
      normalizeCustomerDeliveryRequest({
        ...input,
        locale: 'fr' as never,
      }),
    ).toThrow(
      'locale is invalid',
    );
  });

  it('requires a bounded delivery version', () => {
    expect(() =>
      normalizeCustomerDeliveryRequest({
        ...input,
        deliveryVersion: 0,
      }),
    ).toThrow(
      'deliveryVersion must be 1..100',
    );
  });

  it('creates stable Asset and deduplication hashes', () => {
    const first =
      normalizeCustomerDeliveryRequest(
        input,
      );
    const second =
      normalizeCustomerDeliveryRequest(
        input,
      );

    expect(first.assetSetHash)
      .toBe(second.assetSetHash);
    expect(first.deduplicationKey)
      .toBe(
        second.deduplicationKey,
      );
    expect(first.assetSetHash)
      .toMatch(/^[0-9a-f]{64}$/u);
    expect(first.deduplicationKey)
      .toMatch(/^[0-9a-f]{64}$/u);
  });

  it('treats Asset ordering as delivery identity', () => {
    const first =
      normalizeCustomerDeliveryRequest(
        input,
      );
    const reversed =
      normalizeCustomerDeliveryRequest({
        ...input,
        assetIds:
          [...input.assetIds].reverse(),
      });

    expect(first.assetSetHash)
      .not.toBe(
        reversed.assetSetHash,
      );
    expect(first.deduplicationKey)
      .not.toBe(
        reversed.deduplicationKey,
      );
  });

  it('keeps the outbox payload reference-only', () => {
    const result =
      normalizeCustomerDeliveryRequest(
        input,
      );
    const serialized =
      JSON.stringify(
        result.outboxPayload,
      );

    expect(
      result.outboxPayload,
    ).toEqual({
      schemaVersion:
        'ysim.customer-delivery-request/v1',
      salesOrderId:
        input.salesOrderId,
      orderNumber:
        input.orderNumber,
      channel: 'EMAIL',
      locale: 'vi',
      deliveryVersion: 1,
      assetCount: 2,
    });
    expect(serialized)
      .not.toContain(
        input.assetIds[0],
      );
    expect(serialized)
      .not.toContain('iccid');
    expect(serialized)
      .not.toContain('qrCode');
    expect(serialized)
      .not.toContain('shortLink');
  });
});
