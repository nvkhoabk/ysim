import {
  describe,
  expect,
  it,
  vi,
} from 'vitest';

import {
  CustomerDeliveryRequestService,
} from '../../apps/api/src/modules/delivery/application/customer-delivery-request.service.js';
import type {
  CustomerDeliveryRequestInput,
  NormalizedCustomerDeliveryRequest,
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

const created = {
  kind: 'CREATED' as const,
  deliveryRequestId:
    '40000000-0000-4000-8000-000000000020',
  outboxId:
    '50000000-0000-4000-8000-000000000020',
  assetCount: 2,
  requestStatus:
    'READY' as const,
  outboxStatus:
    'PENDING' as const,
};

const createService = (
  result: unknown = created,
) => {
  const persist =
    vi.fn().mockResolvedValue(
      result,
    );
  const service =
    new CustomerDeliveryRequestService(
      { persist } as never,
    );

  return {
    service,
    persist,
  };
};

describe('Customer Delivery request service', () => {
  it('creates a delivery request', async () => {
    const context =
      createService();

    await expect(
      context.service.request(
        input,
      ),
    ).resolves.toEqual(
      created,
    );
    expect(context.persist)
      .toHaveBeenCalledTimes(1);
  });

  it('passes normalized immutable identity', async () => {
    const context =
      createService();

    await context.service.request(
      input,
    );
    const normalized =
      context.persist.mock
        .calls[0][0] as
          NormalizedCustomerDeliveryRequest;

    expect(normalized).toMatchObject({
      salesOrderId:
        input.salesOrderId,
      orderNumber:
        input.orderNumber,
      channel: 'EMAIL',
      locale: 'vi',
      deliveryVersion: 1,
      expectedAssetCount: 2,
    });
  });

  it('preserves the ordered Asset references', async () => {
    const context =
      createService();

    await context.service.request(
      input,
    );
    const normalized =
      context.persist.mock
        .calls[0][0] as
          NormalizedCustomerDeliveryRequest;

    expect(normalized.assetIds)
      .toEqual(input.assetIds);
  });

  it('passes a reference-only outbox payload', async () => {
    const context =
      createService();

    await context.service.request(
      input,
    );
    const normalized =
      context.persist.mock
        .calls[0][0] as
          NormalizedCustomerDeliveryRequest;
    const payload =
      JSON.stringify(
        normalized.outboxPayload,
      );

    expect(payload)
      .not.toContain(
        input.assetIds[0],
      );
    expect(payload)
      .not.toMatch(
        /iccid|qrCode|shortLink|ciphertext/iu,
      );
  });

  it('returns an idempotent replay', async () => {
    const replay = {
      ...created,
      kind: 'REPLAY' as const,
      outboxStatus:
        'PUBLISHED' as const,
    };
    const context =
      createService(replay);

    await expect(
      context.service.request(
        input,
      ),
    ).resolves.toEqual(
      replay,
    );
  });

  it('returns a persistence conflict', async () => {
    const conflict = {
      kind: 'CONFLICT' as const,
    };
    const context =
      createService(conflict);

    await expect(
      context.service.request(
        input,
      ),
    ).resolves.toEqual(
      conflict,
    );
  });

  it('rejects validation asynchronously before repository access', async () => {
    const context =
      createService();
    const rejection =
      context.service.request({
        ...input,
        expectedAssetCount: 1,
      });

    expect(rejection)
      .toBeInstanceOf(Promise);
    await expect(rejection)
      .rejects.toThrow(
        'Delivery Asset count mismatch',
      );
    expect(context.persist)
      .not.toHaveBeenCalled();
  });

  it('normalizes the request timestamp', async () => {
    const context =
      createService();

    await context.service.request({
      ...input,
      requestedAt:
        '2026-07-31T21:00:00+02:00',
    });
    const normalized =
      context.persist.mock
        .calls[0][0] as
          NormalizedCustomerDeliveryRequest;

    expect(normalized.requestedAt)
      .toBe(
        '2026-07-31T19:00:00.000Z',
      );
  });

  it('preserves the selected locale', async () => {
    const context =
      createService();

    await context.service.request({
      ...input,
      locale: 'lo',
    });
    const normalized =
      context.persist.mock
        .calls[0][0] as
          NormalizedCustomerDeliveryRequest;

    expect(normalized.locale)
      .toBe('lo');
  });

  it('does not send email or start a worker', () => {
    const source =
      CustomerDeliveryRequestService
        .toString();

    expect(source).not.toMatch(
      /sendMail|fetch|setInterval|setTimeout/iu,
    );
  });
});
