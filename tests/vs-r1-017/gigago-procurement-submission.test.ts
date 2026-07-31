import {
  describe,
  expect,
  it,
  vi,
} from 'vitest';

import {
  GigagoProcurementSubmissionService,
} from '../../apps/api/src/modules/procurement/application/gigago-procurement-submission.service.js';

const now =
  new Date(
    '2026-07-31T11:00:00.000Z',
  );
const source = {
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

class FakeReader {
  result: typeof source | null =
    source;

  async findById() {
    return this.result;
  }
}

class FakeRepository {
  claimResult: any = {
    kind: 'CLAIMED',
    submissionId:
      '30000000-0000-4000-8000-000000000017',
    attemptCount: 1,
  };
  submitted = true;
  failed = true;
  claims: unknown[] = [];
  completions: unknown[] = [];
  failures: unknown[] = [];

  async claim(input: unknown) {
    this.claims.push(input);
    return this.claimResult;
  }

  async markSubmitted(input: unknown) {
    this.completions.push(input);
    return this.submitted;
  }

  async markFailed(input: unknown) {
    this.failures.push(input);
    return this.failed;
  }
}

class FakeClient {
  calls: unknown[] = [];
  error: Error | null = null;

  async createPartnerOrder(
    input: unknown,
  ) {
    this.calls.push(input);
    if (this.error) throw this.error;
    return {
      request_id:
        'ysim-sbx-' +
        'a'.repeat(32),
      agency_order_id: 23,
      code:
        '80a27da6-3edc-4538-9800-784106298e30',
      status: 10,
      order_status: 'PROCESSING',
    };
  }
}

const createService = (
  reader = new FakeReader(),
  repository = new FakeRepository(),
  client = new FakeClient(),
) => ({
  service:
    new GigagoProcurementSubmissionService(
      reader as never,
      repository as never,
      client as never,
    ),
  reader,
  repository,
  client,
});

const options = {
  now,
  environment: {
    YSIM_SUPPLIER_SUBMISSION_LEASE_SECONDS:
      '30',
  },
};

describe('Gigago Procurement submission service', () => {
  it('submits one claimed request', async () => {
    const context = createService();
    const result =
      await context.service.submit(
        source.procurementRequestId,
        'https://sandbox.ysim.vn/gigago/callback',
        options,
      );

    expect(result.kind).toBe(
      'SUBMITTED',
    );
    expect(context.client.calls)
      .toHaveLength(1);
    expect(context.repository.completions)
      .toHaveLength(1);
  });

  it('passes a deterministic provider request ID', async () => {
    const context = createService();
    await context.service.submit(
      source.procurementRequestId,
      'https://sandbox.ysim.vn/gigago/callback',
      options,
    );

    const claim =
      context.repository.claims[0] as {
        providerRequestId: string;
        requestPayloadHash: string;
      };
    expect(
      claim.providerRequestId,
    ).toMatch(
      /^ysim-sbx-[0-9a-f]{32}$/u,
    );
    expect(
      claim.requestPayloadHash,
    ).toMatch(/^[0-9a-f]{64}$/u);
  });

  it('returns an existing replay without calling Gigago', async () => {
    const context = createService();
    context.repository.claimResult = {
      kind: 'REPLAY',
      submissionId:
        '30000000-0000-4000-8000-000000000017',
      attemptCount: 1,
      providerRequestId:
        'ysim-sbx-' +
        'a'.repeat(32),
      providerOrderId: 23,
      providerCode:
        '80a27da6-3edc-4538-9800-784106298e30',
      providerStatus: 10,
      providerOrderStatus:
        'PROCESSING',
    };

    const result =
      await context.service.submit(
        source.procurementRequestId,
        'https://sandbox.ysim.vn/gigago/callback',
        options,
      );

    expect(result.kind).toBe('REPLAY');
    expect(context.client.calls)
      .toHaveLength(0);
  });

  it('returns BUSY without calling Gigago', async () => {
    const context = createService();
    context.repository.claimResult = {
      kind: 'BUSY',
      availableAt:
        '2026-07-31T11:00:30.000Z',
    };

    const result =
      await context.service.submit(
        source.procurementRequestId,
        'https://sandbox.ysim.vn/gigago/callback',
        options,
      );

    expect(result.kind).toBe('BUSY');
    expect(context.client.calls)
      .toHaveLength(0);
  });

  it('fails closed when the source is unavailable', async () => {
    const context = createService();
    context.reader.result = null;

    const result =
      await context.service.submit(
        source.procurementRequestId,
        'https://sandbox.ysim.vn/gigago/callback',
        options,
      );

    expect(result).toEqual({
      kind: 'CONFLICT',
    });
  });

  it('returns CONFLICT without a provider call', async () => {
    const context = createService();
    context.repository.claimResult = {
      kind: 'CONFLICT',
    };

    const result =
      await context.service.submit(
        source.procurementRequestId,
        'https://sandbox.ysim.vn/gigago/callback',
        options,
      );

    expect(result.kind).toBe(
      'CONFLICT',
    );
    expect(context.client.calls)
      .toHaveLength(0);
  });

  it('records a sanitized failure and retry time', async () => {
    const context = createService();
    context.client.error =
      new Error(
        'api_key=secret-value temporary failure',
      );

    const result =
      await context.service.submit(
        source.procurementRequestId,
        'https://sandbox.ysim.vn/gigago/callback',
        options,
      );

    expect(result).toMatchObject({
      kind: 'FAILED',
      retryAt:
        '2026-07-31T11:00:10.000Z',
    });
    expect(
      JSON.stringify(
        context.repository.failures,
      ),
    ).not.toContain('secret-value');
  });

  it('reports a lost completion lease', async () => {
    const context = createService();
    context.repository.submitted =
      false;

    const result =
      await context.service.submit(
        source.procurementRequestId,
        'https://sandbox.ysim.vn/gigago/callback',
        options,
      );

    expect(result.kind).toBe(
      'LEASE_LOST',
    );
  });

  it('reports a lost failure lease', async () => {
    const context = createService();
    context.client.error =
      new Error('temporary failure');
    context.repository.failed = false;

    const result =
      await context.service.submit(
        source.procurementRequestId,
        'https://sandbox.ysim.vn/gigago/callback',
        options,
      );

    expect(result.kind).toBe(
      'LEASE_LOST',
    );
  });

  it('does not start a scheduler', () => {
    const text =
      GigagoProcurementSubmissionService
        .toString();
    expect(text).not.toMatch(
      /setInterval|setTimeout/iu,
    );
  });
});
