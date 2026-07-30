import { describe, expect, it } from 'vitest';

import { PaymentService } from '../../apps/api/src/modules/payment/application/payment.service.js';
import type {
  ApplyPaymentEventResult,
  CreatePaymentIntentResult,
  PersistedPaymentIntent,
} from '../../apps/api/src/modules/payment/infrastructure/payment.repository.js';
import { TestPaymentProvider } from '../../apps/api/src/modules/payment/infrastructure/test-payment.provider.js';

type HttpErrorLike = {
  getStatus?: () => unknown;
  status?: unknown;
  statusCode?: unknown;
};

const readHttpStatus = (error: unknown): number | undefined => {
  if (typeof error !== 'object' || error === null) {
    return undefined;
  }
  const candidate = error as HttpErrorLike;
  if (typeof candidate.getStatus === 'function') {
    const value = candidate.getStatus();
    return typeof value === 'number' ? value : undefined;
  }
  if (typeof candidate.status === 'number') {
    return candidate.status;
  }
  return typeof candidate.statusCode === 'number'
    ? candidate.statusCode
    : undefined;
};

const expectHttpStatus = async (
  operation: Promise<unknown>,
  expectedStatus: number,
): Promise<void> => {
  let observed: unknown;
  try {
    await operation;
  } catch (error) {
    observed = error;
  }
  expect(observed).toBeDefined();
  expect(readHttpStatus(observed)).toBe(expectedStatus);
};

process.env.YSIM_PAYMENT_TEST_PROVIDER_ENABLED = 'true';

const orderId = '1458c5f0-21ad-4e75-9ec6-0a9641e81866';
const intentId = '2458c5f0-21ad-4e75-9ec6-0a9641e81866';
const actorId = '3458c5f0-21ad-4e75-9ec6-0a9641e81866';
const accessToken = 'x'.repeat(43);

const intent: PersistedPaymentIntent = {
  id: intentId,
  orderId,
  orderNumber: 'YS-20260730-1458C5F021AD',
  provider: 'TEST',
  providerReference: 'TST-2458C5F021AD4E759EC60A96',
  attemptNumber: 1,
  amountMinor: '338000',
  currency: 'VND',
  status: 'CREATED',
  createdAt: '2026-07-30T08:00:00.000Z',
  expiresAt: '2026-07-30T08:15:00.000Z',
  updatedAt: '2026-07-30T08:00:00.000Z',
  version: 1,
  idempotencyKeyHash: 'a'.repeat(64),
  requestFingerprint: 'b'.repeat(64),
};

class FakeRepository {
  createResult: CreatePaymentIntentResult = {
    kind: 'CREATED',
    intent,
  };
  findResult: PersistedPaymentIntent | null = intent;
  eventResult: ApplyPaymentEventResult = {
    kind: 'APPLIED',
    intent: {
      ...intent,
      status: 'SUCCEEDED',
      version: 2,
    },
    orderStatus: 'CONFIRMED',
    orderPaymentStatus: 'PAID',
  };

  async createIntent(): Promise<CreatePaymentIntentResult> {
    return this.createResult;
  }

  async findIntent(): Promise<PersistedPaymentIntent | null> {
    return this.findResult;
  }

  async applyEvent(): Promise<ApplyPaymentEventResult> {
    return this.eventResult;
  }
}

const serviceWith = (repository: FakeRepository): PaymentService =>
  new PaymentService(
    repository as never,
    new TestPaymentProvider(),
  );

describe('payment service', () => {
  it('creates a public intent from the order-owned amount', async () => {
    const service = serviceWith(new FakeRepository());
    const response = await service.createIntent(
      { orderId, provider: 'TEST' },
      'payment-checkout-0001',
      accessToken,
    );
    expect(response.idempotentReplay).toBe(false);
    expect(response.intent.amountMinor).toBe('338000');
    expect(response.intent.currencyExponent).toBe(0);
    expect(response.intent).not.toHaveProperty('idempotencyKeyHash');
    expect(response.intent).not.toHaveProperty('requestFingerprint');
  });

  it('returns an idempotent replay', async () => {
    const repository = new FakeRepository();
    repository.createResult = { kind: 'REPLAY', intent };
    const response = await serviceWith(repository).createIntent(
      { orderId, provider: 'TEST' },
      'payment-checkout-0001',
      accessToken,
    );
    expect(response.idempotentReplay).toBe(true);
    expect(response.intent.id).toBe(intentId);
  });

  it('requires the guest order access token', async () => {
    await expectHttpStatus(
      serviceWith(new FakeRepository()).createIntent(
        { orderId, provider: 'TEST' },
        'payment-checkout-0001',
        undefined,
      ),
      401,
    );
  });

  it('hides an inaccessible order as not found', async () => {
    const repository = new FakeRepository();
    repository.createResult = { kind: 'ORDER_NOT_FOUND' };
    await expectHttpStatus(
      serviceWith(repository).createIntent(
        { orderId, provider: 'TEST' },
        'payment-checkout-0001',
        accessToken,
      ),
      404,
    );
  });

  it('rejects a second active intent', async () => {
    const repository = new FakeRepository();
    repository.createResult = { kind: 'ACTIVE_INTENT_EXISTS' };
    await expectHttpStatus(
      serviceWith(repository).createIntent(
        { orderId, provider: 'TEST' },
        'payment-checkout-0002',
        accessToken,
      ),
      409,
    );
  });

  it('rejects changed idempotent payment data', async () => {
    const repository = new FakeRepository();
    repository.createResult = { kind: 'IDEMPOTENCY_CONFLICT' };
    await expectHttpStatus(
      serviceWith(repository).createIntent(
        { orderId, provider: 'TEST' },
        'payment-checkout-0001',
        accessToken,
      ),
      409,
    );
  });

  it('reads an intent with the protected order token', async () => {
    const response = await serviceWith(
      new FakeRepository(),
    ).getIntent(intentId, accessToken);
    expect(response.intent.id).toBe(intentId);
    expect(response.intent).not.toHaveProperty('requestFingerprint');
  });

  it('hides an intent when the token hash does not match', async () => {
    const repository = new FakeRepository();
    repository.findResult = null;
    await expectHttpStatus(
      serviceWith(repository).getIntent(
        intentId,
        accessToken,
      ),
      404,
    );
  });

  it('applies a normalized success event', async () => {
    const response = await serviceWith(
      new FakeRepository(),
    ).applyTestEvent(
      intentId,
      {
        eventId: 'test:event-success-0001',
        status: 'SUCCEEDED',
      },
      actorId,
    );
    expect(response.duplicateEvent).toBe(false);
    expect(response.intent.status).toBe('SUCCEEDED');
    expect(response.orderStatus).toBe('CONFIRMED');
    expect(response.orderPaymentStatus).toBe('PAID');
  });

  it('reports a duplicate provider event without another effect', async () => {
    const repository = new FakeRepository();
    repository.eventResult = {
      kind: 'DUPLICATE',
      intent: {
        ...intent,
        status: 'PENDING',
      },
      orderStatus: 'PENDING_PAYMENT',
      orderPaymentStatus: 'UNPAID',
    };
    const response = await serviceWith(
      repository,
    ).applyTestEvent(
      intentId,
      {
        eventId: 'test:event-pending-0001',
        status: 'PENDING',
      },
      actorId,
    );
    expect(response.duplicateEvent).toBe(true);
  });
});
