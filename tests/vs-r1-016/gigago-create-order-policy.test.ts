import {
  describe,
  expect,
  it,
} from 'vitest';

import {
  buildGigagoCreateOrderInput,
  buildGigagoRequestId,
  GigagoCreateOrderPolicyError,
  normalizeGigagoCreateOrderExtra,
} from '../../apps/api/src/modules/procurement/domain/gigago-create-order-policy.js';

const snapshot = {
  procurementRequestId:
    '10000000-0000-4000-8000-000000000016',
  orderId:
    '20000000-0000-4000-8000-000000000016',
  orderNumber:
    'YS-20260731-016ABCDEF016',
  supplierCode: 'GIGAGO',
  supplierEnvironment: 'SANDBOX',
  externalPlanId:
    'GIGAGO_JP_FIXED_5GB_7D',
  quantity: 2,
  status: 'PENDING_SUPPLIER',
};

describe('Gigago create-order policy', () => {
  it('creates a deterministic request ID', () => {
    const first = buildGigagoRequestId(
      snapshot.procurementRequestId,
    );
    const second = buildGigagoRequestId(
      snapshot.procurementRequestId,
    );
    expect(first).toBe(second);
    expect(first).toMatch(
      /^ysim-sbx-[0-9a-f]{32}$/u,
    );
  });

  it('builds the accepted createPartnerOrder payload', () => {
    const input =
      buildGigagoCreateOrderInput(
        snapshot,
        'https://sandbox.ysim.vn/api/fulfillment/gigago/webhook',
      );
    expect(input.orders).toEqual([
      {
        ggg_plan_id:
          'GIGAGO_JP_FIXED_5GB_7D',
        amount: 2,
      },
    ]);
    expect(input.metadata.note).toBe(
      'YSim order YS-20260731-016ABCDEF016',
    );
  });

  it('requires the Gigago supplier', () => {
    expect(() =>
      buildGigagoCreateOrderInput(
        {
          ...snapshot,
          supplierCode: 'OTHER',
        },
        'https://sandbox.ysim.vn/callback',
      ),
    ).toThrow(
      GigagoCreateOrderPolicyError,
    );
  });

  it('blocks production supplier environments', () => {
    expect(() =>
      buildGigagoCreateOrderInput(
        {
          ...snapshot,
          supplierEnvironment:
            'PRODUCTION',
        },
        'https://sandbox.ysim.vn/callback',
      ),
    ).toThrow(
      'not eligible for Gigago sandbox',
    );
  });

  it('requires pending supplier status', () => {
    expect(() =>
      buildGigagoCreateOrderInput(
        {
          ...snapshot,
          status: 'SUBMITTED',
        },
        'https://sandbox.ysim.vn/callback',
      ),
    ).toThrow(
      'not eligible for Gigago sandbox',
    );
  });

  it('rejects an invalid quantity', () => {
    expect(() =>
      buildGigagoCreateOrderInput(
        {
          ...snapshot,
          quantity: 21,
        },
        'https://sandbox.ysim.vn/callback',
      ),
    ).toThrow('quantity must be 1..20');
  });

  it('requires an HTTPS notification URL', () => {
    expect(() =>
      buildGigagoCreateOrderInput(
        snapshot,
        'http://sandbox.ysim.vn/callback',
      ),
    ).toThrow(
      'notifyUrl must be an HTTPS',
    );
  });

  it('normalizes an accepted response extra', () => {
    const requestId =
      buildGigagoRequestId(
        snapshot.procurementRequestId,
      );
    expect(
      normalizeGigagoCreateOrderExtra(
        {
          request_id: requestId,
          agency_order_id: 23,
          code:
            '80A27DA6-3EDC-4538-9800-784106298E30',
          notes: 'YSim',
          status: 10,
          order_status: 'processing',
        },
        requestId,
      ),
    ).toEqual({
      request_id: requestId,
      agency_order_id: 23,
      code:
        '80a27da6-3edc-4538-9800-784106298e30',
      notes: 'YSim',
      status: 10,
      order_status: 'PROCESSING',
    });
  });

  it('rejects a mismatched provider request ID', () => {
    const requestId =
      buildGigagoRequestId(
        snapshot.procurementRequestId,
      );
    expect(() =>
      normalizeGigagoCreateOrderExtra(
        {
          request_id:
            'ysim-sbx-' + 'a'.repeat(32),
          agency_order_id: 23,
          code:
            '80a27da6-3edc-4538-9800-784106298e30',
          status: 10,
          order_status: 'PROCESSING',
        },
        requestId,
      ),
    ).toThrow(
      'Gigago request_id mismatch',
    );
  });

  it('rejects an invalid provider order ID', () => {
    const requestId =
      buildGigagoRequestId(
        snapshot.procurementRequestId,
      );
    expect(() =>
      normalizeGigagoCreateOrderExtra(
        {
          request_id: requestId,
          agency_order_id: 0,
          code:
            '80a27da6-3edc-4538-9800-784106298e30',
          status: 10,
          order_status: 'PROCESSING',
        },
        requestId,
      ),
    ).toThrow(
      'agency_order_id is invalid',
    );
  });
});
