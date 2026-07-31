import {
  describe,
  expect,
  it,
  vi,
} from 'vitest';

import {
  GigagoClientError,
  GigagoOrderReadbackClient,
} from '../../apps/api/src/modules/procurement/infrastructure/gigago/gigago.client.js';
import {
  loadGigagoCreateOrderConfig,
} from '../../apps/api/src/modules/procurement/infrastructure/gigago/gigago.config.js';
import {
  GigagoOrderReadbackService,
} from '../../apps/api/src/modules/procurement/application/gigago-order-readback.service.js';

const requestId =
  'ysim-sbx-0123456789abcdef0123456789abcdef';
const config = {
  environment: 'SANDBOX' as const,
  baseUrl:
    'https://sandbox-partners-api.gigago.com',
  apiKey:
    'sandbox-key-for-controlled-tests',
  endpoint:
    '/api/partner/createPartnerOrder' as const,
  method: 'PUT' as const,
  timeoutMs: 10000,
  myOrdersEndpoint:
    '/api/partner/getMyOrdersAgency' as const,
  myOrdersMethod: 'POST' as const,
  orderDetailEndpoint:
    '/api/partner/getOrderDetailAgency' as const,
  orderDetailMethod: 'POST' as const,
};

const envelope = (
  result: unknown[],
) => ({
  code: 200,
  message: 'success!',
  totalRecords: result.length,
  result,
  extra: null,
});

describe('Gigago order readback client', () => {
  it('loads probed POST methods for sandbox', () => {
    expect(
      loadGigagoCreateOrderConfig({
        YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED:
          'true',
        YSIM_GIGAGO_ENVIRONMENT:
          'SANDBOX',
        YSIM_GIGAGO_CONTRACT_STATUS:
          'PROBED',
        GIGAGO_SANDBOX_API_KEY:
          'sandbox-key-for-controlled-tests',
      }),
    ).toMatchObject({
      myOrdersMethod: 'POST',
      orderDetailMethod: 'POST',
    });
  });

  it('rejects documented PUT in sandbox', () => {
    expect(() =>
      loadGigagoCreateOrderConfig({
        YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED:
          'true',
        YSIM_GIGAGO_ENVIRONMENT:
          'SANDBOX',
        YSIM_GIGAGO_CONTRACT_STATUS:
          'PROBED',
        GIGAGO_SANDBOX_API_KEY:
          'sandbox-key-for-controlled-tests',
        GIGAGO_GET_MY_ORDERS_METHOD:
          'PUT',
      }),
    ).toThrow(
      'must use probed POST',
    );
  });

  it('calls getMyOrdersAgency with POST', async () => {
    const request = vi.fn()
      .mockResolvedValue({
        status: 200,
        body: envelope([]),
      });
    await new GigagoOrderReadbackClient(
      { request },
      config,
    ).getMyOrdersAgency(requestId);

    expect(request).toHaveBeenCalledWith(
      expect.objectContaining({
        url:
          config.baseUrl +
          config.myOrdersEndpoint,
        method: 'POST',
        headers:
          expect.objectContaining({
            apiKey: config.apiKey,
          }),
      }),
    );
  });

  it('calls getOrderDetailAgency with POST', async () => {
    const request = vi.fn()
      .mockResolvedValue({
        status: 200,
        body: envelope([]),
      });
    await new GigagoOrderReadbackClient(
      { request },
      config,
    ).getOrderDetailAgency(
      requestId,
    );

    expect(request).toHaveBeenCalledWith(
      expect.objectContaining({
        url:
          config.baseUrl +
          config.orderDetailEndpoint,
        method: 'POST',
      }),
    );
  });

  it('sends the canonical request filter', async () => {
    const request = vi.fn()
      .mockResolvedValue({
        status: 200,
        body: envelope([]),
      });
    await new GigagoOrderReadbackClient(
      { request },
      config,
    ).getMyOrdersAgency(requestId);

    const body = JSON.parse(
      request.mock.calls[0][0].body,
    );
    expect(body).toEqual({
      columnFilters: {
        request_id: requestId,
      },
      sort: [],
      page: 1,
      pageSize: 100,
    });
  });

  it('rejects a count mismatch', async () => {
    await expect(
      new GigagoOrderReadbackClient(
        {
          async request() {
            return {
              status: 200,
              body: {
                ...envelope([]),
                totalRecords: 1,
              },
            };
          },
        },
        config,
      ).getMyOrdersAgency(requestId),
    ).rejects.toMatchObject({
      code:
        'GIGAGO_RESPONSE_INVALID',
    });
  });

  it('rejects an HTTP-200 failed envelope', async () => {
    await expect(
      new GigagoOrderReadbackClient(
        {
          async request() {
            return {
              status: 200,
              body: {
                code: 200,
                message: 'failed',
                totalRecords: 0,
                result: null,
                extra: null,
              },
            };
          },
        },
        config,
      ).getOrderDetailAgency(
        requestId,
      ),
    ).rejects.toMatchObject({
      code: 'GIGAGO_API_REJECTED',
    });
  });

  it('rejects a non-array result', async () => {
    await expect(
      new GigagoOrderReadbackClient(
        {
          async request() {
            return {
              status: 200,
              body: {
                code: 200,
                message: 'success!',
                totalRecords: 1,
                result: {},
                extra: null,
              },
            };
          },
        },
        config,
      ).getMyOrdersAgency(requestId),
    ).rejects.toBeInstanceOf(
      GigagoClientError,
    );
  });

  it('combines both endpoints in the service', async () => {
    const client = {
      getMyOrdersAgency:
        vi.fn().mockResolvedValue([]),
      getOrderDetailAgency:
        vi.fn().mockResolvedValue([]),
    };
    const result =
      await new GigagoOrderReadbackService(
        client as never,
      ).read(requestId, 1);

    expect(result).toMatchObject({
      kind: 'PROCESSING',
      reason: 'NO_ORDER_DATA',
    });
    expect(
      client.getMyOrdersAgency,
    ).toHaveBeenCalledTimes(1);
    expect(
      client.getOrderDetailAgency,
    ).toHaveBeenCalledTimes(1);
  });

  it('does not start an automatic poller', () => {
    expect(
      GigagoOrderReadbackService
        .toString(),
    ).not.toMatch(
      /setInterval|setTimeout/iu,
    );
  });
});
