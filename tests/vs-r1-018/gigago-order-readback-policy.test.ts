import {
  describe,
  expect,
  it,
} from 'vitest';

import {
  assessGigagoDeliveryReadiness,
  GigagoOrderReadbackPolicyError,
  normalizeGigagoAgencyOrders,
  normalizeGigagoOrderDetails,
} from '../../apps/api/src/modules/procurement/domain/gigago-order-readback-policy.js';

const requestId =
  'ysim-sbx-0123456789abcdef0123456789abcdef';

const completedOrder = {
  id: 'G000493.1',
  total_price: 2000,
  notes: 'test',
  currency: 'VND',
  total_esims: '2',
  request_id: requestId,
  order_detail: '[]',
  total_esim_completed: 2,
  order_date: '2026-07-31 12:00:00',
  agency_id: 83,
  agency_name: 'ysim',
  user_id: 140,
  order_status: 1,
  order_status_name: 'Completed',
};

const delivered = (
  id: number,
  iccid: string,
  overrides: Record<string, unknown> = {},
) => ({
  id,
  order_id: 'G000493.1',
  agency_id: 83,
  iccid,
  currency: 'VND',
  phone_number: '',
  channel_notes: 'test',
  request_id: requestId,
  status: 1,
  status_name: 'Delivered',
  price: 1000,
  ggg_plan_id:
    'GIGAGO_JP_FIXED_5GB_7D',
  data: '5GB',
  validity: '7 days',
  user_id: 140,
  username: 'ysim',
  order_date: '2026-07-31 12:00:00',
  qr_code:
    `LPA:1$rspeu.demo.net$CODE${id}`,
  short_link: `short_${id}`,
  ...overrides,
});

describe('Gigago order readback policy', () => {
  it('normalizes a completed agency order', () => {
    expect(
      normalizeGigagoAgencyOrders(
        [completedOrder],
        requestId,
      )[0],
    ).toMatchObject({
      id: 'G000493.1',
      totalEsims: 2,
      completedEsims: 2,
      status: 'COMPLETED',
      statusCode: 1,
    });
  });

  it('normalizes delivered eSIM details', () => {
    const items =
      normalizeGigagoOrderDetails(
        [
          delivered(
            1820422,
            '8988211000000000001',
          ),
        ],
        requestId,
      );
    expect(items[0]).toMatchObject({
      detailId: 1820422,
      status: 'DELIVERED',
      iccid:
        '8988211000000000001',
      planId:
        'GIGAGO_JP_FIXED_5GB_7D',
    });
  });

  it('classifies fully complete data as DELIVERABLE', () => {
    const orders =
      normalizeGigagoAgencyOrders(
        [completedOrder],
        requestId,
      );
    const details =
      normalizeGigagoOrderDetails(
        [
          delivered(
            1,
            '8988211000000000001',
          ),
          delivered(
            2,
            '8988211000000000002',
          ),
        ],
        requestId,
      );
    expect(
      assessGigagoDeliveryReadiness(
        orders,
        details,
        2,
      ),
    ).toMatchObject({
      kind: 'DELIVERABLE',
      expectedCount: 2,
      completedCount: 2,
      deliveredCount: 2,
      installableCount: 2,
    });
  });

  it('accepts short link when QR is absent', () => {
    const result =
      assessGigagoDeliveryReadiness(
        normalizeGigagoAgencyOrders(
          [completedOrder],
          requestId,
        ),
        normalizeGigagoOrderDetails(
          [
            delivered(
              1,
              '8988211000000000001',
              { qr_code: '' },
            ),
            delivered(
              2,
              '8988211000000000002',
              { qr_code: '' },
            ),
          ],
          requestId,
        ),
        2,
      );
    expect(result.kind).toBe(
      'DELIVERABLE',
    );
  });

  it('keeps a processing order non-terminal', () => {
    const result =
      assessGigagoDeliveryReadiness(
        normalizeGigagoAgencyOrders(
          [
            {
              ...completedOrder,
              order_status: 10,
              order_status_name:
                'Processing',
              total_esim_completed: 0,
            },
          ],
          requestId,
        ),
        [],
        2,
      );
    expect(result).toMatchObject({
      kind: 'PROCESSING',
      reason: 'ORDER_PROCESSING',
    });
  });

  it('treats Gigago Pending as action required', () => {
    const result =
      assessGigagoDeliveryReadiness(
        normalizeGigagoAgencyOrders(
          [
            {
              ...completedOrder,
              order_status: 0,
              order_status_name:
                'Pending',
              total_esim_completed: 0,
            },
          ],
          requestId,
        ),
        [],
        2,
      );
    expect(result).toMatchObject({
      kind: 'ACTION_REQUIRED',
      reason: 'ORDER_PENDING_ERROR',
    });
  });

  it('treats recalled eSIM as action required', () => {
    const result =
      assessGigagoDeliveryReadiness(
        normalizeGigagoAgencyOrders(
          [completedOrder],
          requestId,
        ),
        normalizeGigagoOrderDetails(
          [
            delivered(
              1,
              '8988211000000000001',
              {
                status: 2,
                status_name:
                  'Recalled',
              },
            ),
            delivered(
              2,
              '8988211000000000002',
            ),
          ],
          requestId,
        ),
        2,
      );
    expect(result).toMatchObject({
      kind: 'ACTION_REQUIRED',
      reason: 'DETAIL_RECALLED',
    });
  });

  it('rejects missing install data after completion', () => {
    const result =
      assessGigagoDeliveryReadiness(
        normalizeGigagoAgencyOrders(
          [completedOrder],
          requestId,
        ),
        normalizeGigagoOrderDetails(
          [
            delivered(
              1,
              '8988211000000000001',
              {
                qr_code: '',
                short_link: '',
              },
            ),
            delivered(
              2,
              '8988211000000000002',
            ),
          ],
          requestId,
        ),
        2,
      );
    expect(result).toMatchObject({
      kind: 'ACTION_REQUIRED',
      reason: 'INSTALL_DATA_MISSING',
    });
  });

  it('rejects duplicate ICCIDs', () => {
    expect(() =>
      normalizeGigagoOrderDetails(
        [
          delivered(
            1,
            '8988211000000000001',
          ),
          delivered(
            2,
            '8988211000000000001',
          ),
        ],
        requestId,
      ),
    ).toThrow(
      GigagoOrderReadbackPolicyError,
    );
  });

  it('rejects a request ID mismatch', () => {
    expect(() =>
      normalizeGigagoAgencyOrders(
        [
          {
            ...completedOrder,
            request_id:
              'ysim-sbx-' +
              'f'.repeat(32),
          },
        ],
        requestId,
      ),
    ).toThrow(
      'request ID mismatch',
    );
  });
});
