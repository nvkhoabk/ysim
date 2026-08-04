import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

import {
  afterEach,
  beforeEach,
  describe,
  expect,
  it,
  vi,
} from 'vitest';

import { GPayGatewayCommissioningService } from '../../apps/api/src/modules/payment/application/gpay-gateway-commissioning.service.js';
import { GPayGatewayClientError } from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.gateway.client.js';
import type { PersistedGPayCommissioningSession } from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.gateway.session.repository.js';

const root = resolve(import.meta.dirname, '../..');
const paymentIntentId =
  '11111111-1111-4111-8111-111111111111';
const actorIdentityId =
  '22222222-2222-4222-8222-222222222222';

const environment = (): Record<string, string> => ({
  YSIM_COMMISSIONING_MODE: 'SANDBOX',
  YSIM_COMMISSIONING_RUN_NAMESPACE:
    'vs-r1-043-persistent-a1b2c3d4',
  YSIM_COMMISSIONING_TRANSACTION_CAP: '1',
  YSIM_COMMISSIONING_MARKET: 'VN',
  YSIM_COMMISSIONING_CURRENCY: 'VND',
  YSIM_GPAY_EXECUTION_ENABLED: 'true',
  YSIM_GPAY_QUERY_CAP: '12',
  YSIM_GPAY_CALLBACK_URL:
    'https://portal.ysim.vn/api/platform/api/r1/payments/gpay/gateway/callback',
  YSIM_GPAY_WEBHOOK_URL:
    'https://portal.ysim.vn/api/platform/api/r1/payments/gpay/gateway/webhook',
  YSIM_GPAY_COMMISSIONING_CUSTOMER_ID:
    'vs-r1-043-sandbox-customer',
  YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED: 'false',
  YSIM_CUSTOMER_EMAIL_ENABLED: 'false',
  YSIM_CUSTOMER_EMAIL_MODE: 'disabled',
  YSIM_CATALOG_SUPPLIER_ENVIRONMENT: 'SANDBOX',
});

const session = (
  overrides: Partial<PersistedGPayCommissioningSession> = {},
): PersistedGPayCommissioningSession => ({
  sliceId: 'VS-R1-043',
  runNamespace: environment().YSIM_COMMISSIONING_RUN_NAMESPACE,
  paymentIntentId,
  merchantOrderId: 'GPY-11111111111141118111111111111111',
  actorIdentityId,
  amountMinor: '169000',
  currency: 'VND',
  status: 'INITIALIZED',
  initAttemptCount: 1,
  queryAttemptCount: 0,
  queryCap: 12,
  billId: 'GPAY-BILL-0001',
  billUrl: 'https://sandbox.gpay.vn/bill/0001',
  expiredTime: '2026-08-04T02:00:00.000Z',
  createdAt: '2026-08-04T00:00:00.000Z',
  updatedAt: '2026-08-04T00:00:01.000Z',
  version: 2,
  ...overrides,
});

const applicationResult = (
  duplicateEvent = false,
) => ({
  accepted: true as const,
  duplicateEvent,
  paymentIntentId,
  paymentIntentStatus: 'PENDING' as const,
  orderStatus: 'PENDING_PAYMENT' as const,
  orderPaymentStatus: 'UNPAID' as const,
});

beforeEach(() => {
  for (const [name, value] of Object.entries(environment())) {
    vi.stubEnv(name, value);
  }
});

afterEach(() => {
  vi.unstubAllEnvs();
  vi.restoreAllMocks();
});

describe('VS-R1-043 persistent commissioning orchestration', () => {
  it('defines one durable transaction budget for the entire slice', () => {
    const migration = readFileSync(
      resolve(
        root,
        'database/migrations/20260804060000_vs_r1_043_gpay_commissioning_ledger/migration.sql',
      ),
      'utf8',
    );
    expect(migration).toContain(
      'slice_id VARCHAR(20) PRIMARY KEY',
    );
    expect(migration).toContain(
      "CHECK (slice_id = 'VS-R1-043')",
    );
    expect(migration).toContain(
      'CHECK (init_attempt_count = 1)',
    );
    expect(migration).toContain(
      'query_attempt_count BETWEEN 0 AND query_cap',
    );
    expect(migration).toContain(
      'payment_intent_id UUID NOT NULL UNIQUE',
    );
  });

  it('persists the consumed init attempt before external I/O', async () => {
    const order: string[] = [];
    const reserved = session({
      status: 'INIT_ATTEMPTED',
      billId: undefined,
      billUrl: undefined,
      expiredTime: undefined,
      version: 1,
    });
    const repository = {
      reserveInitAttempt: vi.fn(async () => {
        order.push('reserve');
        return { kind: 'RESERVED', session: reserved } as const;
      }),
      bindInitResult: vi.fn(async () => {
        order.push('bind');
        return session();
      }),
    };
    const client = {
      initOrder: vi.fn(async (input: Record<string, unknown>) => {
        order.push('external');
        expect(input).not.toHaveProperty('email');
        expect(input).not.toHaveProperty('phone');
        expect(input).toMatchObject({
          amount: 169000,
          merchantOrderId: reserved.merchantOrderId,
          customerId: 'vs-r1-043-sandbox-customer',
        });
        return {
          provider: 'GPAY' as const,
          billId: 'GPAY-BILL-0001',
          billUrl: 'https://sandbox.gpay.vn/bill/0001',
          expiredTime: '2026-08-04T02:00:00.000Z',
          merchantOrderId: reserved.merchantOrderId,
          securityRequestId: 'request-1',
          tokenCached: false,
        };
      }),
    };
    const service = new GPayGatewayCommissioningService(
      repository as never,
      client as never,
      {} as never,
    );

    await expect(service.initialize(
      paymentIntentId,
      actorIdentityId,
    )).resolves.toMatchObject({
      sliceId: 'VS-R1-043',
      sessionStatus: 'INITIALIZED',
      initAttemptCount: 1,
    });
    expect(order).toEqual(['reserve', 'external', 'bind']);
  });

  it('keeps an uncertain init attempt consumed and never binds it', async () => {
    const repository = {
      reserveInitAttempt: vi.fn(async () => ({
        kind: 'RESERVED' as const,
        session: session({
          status: 'INIT_ATTEMPTED',
          billId: undefined,
          billUrl: undefined,
          expiredTime: undefined,
        }),
      })),
      bindInitResult: vi.fn(),
    };
    const client = {
      initOrder: vi.fn(async () => {
        throw new GPayGatewayClientError(
          'GPay request timed out',
        );
      }),
    };
    const service = new GPayGatewayCommissioningService(
      repository as never,
      client as never,
      {} as never,
    );

    await expect(service.initialize(
      paymentIntentId,
      actorIdentityId,
    )).rejects.toThrow(/timed out/u);
    expect(repository.reserveInitAttempt).toHaveBeenCalledOnce();
    expect(repository.bindInitResult).not.toHaveBeenCalled();
  });

  it('blocks provider I/O when the persistent slice budget exists', async () => {
    const repository = {
      reserveInitAttempt: vi.fn(async () => ({
        kind: 'BUDGET_ALREADY_CONSUMED' as const,
      })),
    };
    const client = { initOrder: vi.fn() };
    const service = new GPayGatewayCommissioningService(
      repository as never,
      client as never,
      {} as never,
    );

    await expect(service.initialize(
      paymentIntentId,
      actorIdentityId,
    )).rejects.toThrow(/already consumed/u);
    expect(client.initOrder).not.toHaveBeenCalled();
  });

  it('consumes a persistent query slot before reconciliation I/O', async () => {
    const order: string[] = [];
    const queried = session({
      queryAttemptCount: 1,
      version: 3,
    });
    const applied = session({
      status: 'PENDING',
      queryAttemptCount: 1,
      version: 4,
    });
    const repository = {
      reserveQueryAttempt: vi.fn(async () => {
        order.push('reserve-query');
        return { kind: 'RESERVED', session: queried } as const;
      }),
      recordEvidence: vi.fn(async () => {
        order.push('record-evidence');
        return { kind: 'APPLIED', session: applied } as const;
      }),
    };
    const client = {
      queryOrder: vi.fn(async () => {
        order.push('external-query');
        return {
          provider: 'GPAY' as const,
          gpayBillId: queried.billId!,
          merchantOrderId: queried.merchantOrderId,
          status: 'ORDER_PENDING',
          securityRequestId: 'request-2',
          tokenCached: true,
        };
      }),
    };
    const webhook = {
      applyVerifiedEvent: vi.fn(async () => {
        order.push('apply-payment');
        return applicationResult();
      }),
    };
    const service = new GPayGatewayCommissioningService(
      repository as never,
      client as never,
      webhook as never,
    );

    await expect(service.reconcile(paymentIntentId))
      .resolves.toMatchObject({
        sessionStatus: 'PENDING',
        queryAttemptCount: 1,
        queryCap: 12,
      });
    expect(order).toEqual([
      'reserve-query',
      'external-query',
      'apply-payment',
      'record-evidence',
    ]);
  });

  it('applies verified callbacks deterministically and records evidence', async () => {
    const current = session();
    const applied = session({ status: 'SUCCEEDED', version: 3 });
    const events: unknown[] = [];
    const repository = {
      findByProviderIdentity: vi.fn(async () => current),
      recordEvidence: vi.fn(async () => ({
        kind: 'APPLIED' as const,
        session: applied,
      })),
    };
    const webhook = {
      applyVerifiedEvent: vi.fn(async (event: unknown) => {
        events.push(event);
        return applicationResult();
      }),
    };
    const service = new GPayGatewayCommissioningService(
      repository as never,
      {} as never,
      webhook as never,
    );
    const callback = {
      verified: true as const,
      contractVersion: 'GPAY_ALL_IN_ONE_CALLBACK_V1' as const,
      merchantOrderId: current.merchantOrderId,
      gpayBillId: current.billId!,
      gpayTransactionId: 'GPAY-TRANS-0001',
      normalizedStatus: 'SUCCESS' as const,
      userPaymentMethod: 'QR_PAYMENT',
      canonicalSha256: 'a'.repeat(64),
    };

    await service.applyVerifiedCallback(callback);
    await service.applyVerifiedCallback(callback);
    expect(events[0]).toEqual(events[1]);
    expect(repository.recordEvidence).toHaveBeenCalledTimes(2);
    expect(repository.recordEvidence.mock.calls[0]?.[0])
      .toMatchObject({
        source: 'CALLBACK',
        normalizedStatus: 'SUCCESS',
      });
  });

  it('rejects a verified callback outside the persisted identity binding', async () => {
    const repository = {
      findByProviderIdentity: vi.fn(async () => null),
    };
    const service = new GPayGatewayCommissioningService(
      repository as never,
      {} as never,
      {} as never,
    );
    await expect(service.applyVerifiedCallback({
      verified: true,
      contractVersion: 'GPAY_ALL_IN_ONE_CALLBACK_V1',
      merchantOrderId: 'GPY-11111111111141118111111111111111',
      gpayBillId: 'UNKNOWN',
      gpayTransactionId: undefined,
      normalizedStatus: 'PENDING',
      userPaymentMethod: undefined,
      canonicalSha256: 'b'.repeat(64),
    })).rejects.toThrow(/not found/u);
  });

  it('keeps commissioning endpoints internal while provider callbacks remain signature-bound', () => {
    const controller = readFileSync(
      resolve(
        root,
        'apps/api/src/modules/payment/presentation/payment-gpay-gateway.controller.ts',
      ),
      'utf8',
    );
    expect(controller).toContain(
      "@Controller('internal/r1/payments/gpay/commissioning')",
    );
    expect(controller).toContain(
      "@Controller('api/r1/payments/gpay/gateway')",
    );
    expect(controller).toContain('requireBootstrapToken(headers)');
    expect(controller).toContain('this.service.applyCallback');
    expect(controller).not.toMatch(/customerEmail|gigago/iu);
  });
});
