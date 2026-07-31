import {
  describe,
  expect,
  it,
  vi,
} from 'vitest';

import {
  GigagoCreateOrderClient,
  GigagoClientError,
} from '../../apps/api/src/modules/procurement/infrastructure/gigago/gigago.client.js';
import {
  loadGigagoCreateOrderConfig,
} from '../../apps/api/src/modules/procurement/infrastructure/gigago/gigago.config.js';

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
};

const input = {
  request_id:
    'ysim-sbx-0123456789abcdef0123456789abcdef',
  orders: [
    {
      ggg_plan_id:
        'GIGAGO_JP_FIXED_5GB_7D',
      amount: 2,
    },
  ],
  metadata: {
    note:
      'YSim order YS-20260731-016ABCDEF016',
    url_notify:
      'https://sandbox.ysim.vn/callback',
  },
};

describe('Gigago create-order client', () => {
  it('loads a strictly sandbox configuration', () => {
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
      environment: 'SANDBOX',
      method: 'PUT',
      endpoint:
        '/api/partner/createPartnerOrder',
    });
  });

  it('blocks production activation', () => {
    expect(() =>
      loadGigagoCreateOrderConfig({
        YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED:
          'true',
        YSIM_GIGAGO_ENVIRONMENT:
          'PRODUCTION',
        YSIM_GIGAGO_CONTRACT_STATUS:
          'PROBED',
        GIGAGO_SANDBOX_API_KEY:
          'sandbox-key-for-controlled-tests',
      }),
    ).toThrow(
      'Only SANDBOX Gigago submission',
    );
  });

  it('sends PUT with apiKey and the exact endpoint', async () => {
    const request = vi.fn()
      .mockResolvedValue({
        status: 200,
        body: {
          code: 200,
          message: 'Success',
          totalRecords: 1,
          result: null,
          extra: {
            request_id:
              input.request_id,
            agency_order_id: 23,
            code:
              '80a27da6-3edc-4538-9800-784106298e30',
            status: 10,
            order_status:
              'PROCESSING',
          },
        },
      });

    await new GigagoCreateOrderClient(
      { request },
      config,
    ).createPartnerOrder(input);

    expect(request).toHaveBeenCalledWith({
      url:
        'https://sandbox-partners-api.gigago.com' +
        '/api/partner/createPartnerOrder',
      method: 'PUT',
      headers: {
        Accept: 'application/json',
        'Content-Type':
          'application/json',
        apiKey:
          'sandbox-key-for-controlled-tests',
      },
      body: JSON.stringify(input),
      timeoutMs: 10000,
    });
  });

  it('returns only normalized safe response fields', async () => {
    const result =
      await new GigagoCreateOrderClient(
        {
          async request() {
            return {
              status: 200,
              body: {
                code: 200,
                message: 'Success',
                totalRecords: 1,
                result: {
                  raw: 'not returned',
                },
                extra: {
                  request_id:
                    input.request_id,
                  agency_order_id: 23,
                  code:
                    '80a27da6-3edc-4538-9800-784106298e30',
                  notes: 'YSim',
                  status: 10,
                  order_status:
                    'processing',
                },
              },
            };
          },
        },
        config,
      ).createPartnerOrder(input);

    expect(result).toEqual({
      request_id: input.request_id,
      agency_order_id: 23,
      code:
        '80a27da6-3edc-4538-9800-784106298e30',
      notes: 'YSim',
      status: 10,
      order_status: 'PROCESSING',
    });
    expect(result).not.toHaveProperty(
      'raw',
    );
  });

  it('rejects a non-2xx HTTP response', async () => {
    await expect(
      new GigagoCreateOrderClient(
        {
          async request() {
            return {
              status: 500,
              body: null,
            };
          },
        },
        config,
      ).createPartnerOrder(input),
    ).rejects.toMatchObject({
      code: 'GIGAGO_HTTP_ERROR',
      status: 500,
    });
  });

  it('rejects malformed envelopes', async () => {
    await expect(
      new GigagoCreateOrderClient(
        {
          async request() {
            return {
              status: 200,
              body: {
                code: 200,
              },
            };
          },
        },
        config,
      ).createPartnerOrder(input),
    ).rejects.toBeInstanceOf(
      GigagoClientError,
    );
  });

  it('rejects HTTP-200 failed envelopes', async () => {
    await expect(
      new GigagoCreateOrderClient(
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
      ).createPartnerOrder(input),
    ).rejects.toMatchObject({
      code: 'GIGAGO_API_REJECTED',
    });
  });

  it('rejects missing response extra', async () => {
    await expect(
      new GigagoCreateOrderClient(
        {
          async request() {
            return {
              status: 200,
              body: {
                code: 200,
                message: 'Success',
                totalRecords: 0,
                result: null,
                extra: null,
              },
            };
          },
        },
        config,
      ).createPartnerOrder(input),
    ).rejects.toMatchObject({
      code:
        'GIGAGO_RESPONSE_INVALID',
    });
  });

  it('does not expose the API key in errors', async () => {
    try {
      await new GigagoCreateOrderClient(
        {
          async request() {
            throw new Error(
              'transport failed',
            );
          },
        },
        config,
      ).createPartnerOrder(input);
    } catch (error) {
      expect(String(error)).not.toContain(
        config.apiKey,
      );
    }
  });

  it('requires explicit enablement', () => {
    expect(() =>
      loadGigagoCreateOrderConfig({
        YSIM_GIGAGO_ENVIRONMENT:
          'SANDBOX',
        YSIM_GIGAGO_CONTRACT_STATUS:
          'PROBED',
        GIGAGO_SANDBOX_API_KEY:
          'sandbox-key-for-controlled-tests',
      }),
    ).toThrow(
      'Gigago order submission is disabled',
    );
  });
});
