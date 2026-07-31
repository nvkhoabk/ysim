import {
  describe,
  expect,
  it,
} from 'vitest';

import {
  buildSupplierSubmissionCommand,
  loadSupplierSubmissionLeaseSeconds,
  sanitizeSupplierSubmissionError,
  SupplierSubmissionPolicyError,
  supplierSubmissionLeaseUntil,
  supplierSubmissionRetryAt,
} from '../../apps/api/src/modules/procurement/domain/supplier-submission-policy.js';

const snapshot = {
  procurementRequestId:
    '10000000-0000-4000-8000-000000000017',
  orderId:
    '20000000-0000-4000-8000-000000000017',
  orderNumber:
    'YS-20260731-017ABCDEF017',
  supplierCode: 'GIGAGO',
  supplierEnvironment: 'SANDBOX',
  externalPlanId:
    'GIGAGO_JP_FIXED_5GB_7D',
  quantity: 2,
  status: 'PENDING_SUPPLIER',
};

describe('Supplier submission policy', () => {
  it('builds a stable command fingerprint', () => {
    const first =
      buildSupplierSubmissionCommand(
        snapshot,
        'https://sandbox.ysim.vn/gigago/callback',
      );
    const second =
      buildSupplierSubmissionCommand(
        snapshot,
        'https://sandbox.ysim.vn/gigago/callback',
      );

    expect(
      first.requestPayloadHash,
    ).toBe(second.requestPayloadHash);
    expect(
      first.requestPayloadHash,
    ).toMatch(/^[0-9a-f]{64}$/u);
  });

  it('uses the deterministic provider request ID', () => {
    const command =
      buildSupplierSubmissionCommand(
        snapshot,
        'https://sandbox.ysim.vn/gigago/callback',
      );
    expect(
      command.providerRequestId,
    ).toMatch(
      /^ysim-sbx-[0-9a-f]{32}$/u,
    );
    expect(
      command.providerRequestId,
    ).toBe(command.input.request_id);
  });

  it('uses a thirty-second default lease', () => {
    expect(
      loadSupplierSubmissionLeaseSeconds(
        {},
      ),
    ).toBe(30);
  });

  it('accepts a bounded custom lease', () => {
    expect(
      loadSupplierSubmissionLeaseSeconds({
        YSIM_SUPPLIER_SUBMISSION_LEASE_SECONDS:
          '60',
      }),
    ).toBe(60);
  });

  it('rejects an unsafe lease', () => {
    expect(() =>
      loadSupplierSubmissionLeaseSeconds({
        YSIM_SUPPLIER_SUBMISSION_LEASE_SECONDS:
          '2',
      }),
    ).toThrow(
      SupplierSubmissionPolicyError,
    );
  });

  it('derives the lease expiry', () => {
    expect(
      supplierSubmissionLeaseUntil(
        '2026-07-31T11:00:00.000Z',
        30,
      ),
    ).toBe(
      '2026-07-31T11:00:30.000Z',
    );
  });

  it('uses a ten-second first retry', () => {
    expect(
      supplierSubmissionRetryAt(
        '2026-07-31T11:00:00.000Z',
        1,
      ),
    ).toBe(
      '2026-07-31T11:00:10.000Z',
    );
  });

  it('uses exponential retry growth', () => {
    expect(
      supplierSubmissionRetryAt(
        '2026-07-31T11:00:00.000Z',
        4,
      ),
    ).toBe(
      '2026-07-31T11:01:20.000Z',
    );
  });

  it('caps retry at fifteen minutes', () => {
    expect(
      supplierSubmissionRetryAt(
        '2026-07-31T11:00:00.000Z',
        20,
      ),
    ).toBe(
      '2026-07-31T11:15:00.000Z',
    );
  });

  it('redacts secrets from failure evidence', () => {
    const safe =
      sanitizeSupplierSubmissionError(
        new Error(
          'Bearer abc.def api_key=secret-value\nfailed',
        ),
      );
    expect(safe).toContain(
      'Bearer [REDACTED]',
    );
    expect(safe).toContain(
      'api_key=[REDACTED]',
    );
    expect(safe).not.toContain(
      'secret-value',
    );
    expect(safe).not.toContain('\n');
  });
});
