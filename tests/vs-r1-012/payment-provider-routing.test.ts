import { describe, expect, it } from 'vitest';

import { PaymentService } from '../../apps/api/src/modules/payment/application/payment.service.js';
import {
  createPaymentRequestFingerprint,
  PaymentPolicyError,
} from '../../apps/api/src/modules/payment/domain/payment-policy.js';
import type {
  CreatePaymentIntentInput,
  CreatePaymentIntentResult,
  PersistedPaymentIntent,
} from '../../apps/api/src/modules/payment/infrastructure/payment.repository.js';

type HttpErrorLike = {
  getStatus?: () => unknown;
  status?: unknown;
  statusCode?: unknown;
};

const readHttpStatus = (
  error: unknown,
): number | undefined => {
  if (typeof error !== 'object' || error === null) {
    return undefined;
  }
  const candidate = error as HttpErrorLike;
  if (typeof candidate.getStatus === 'function') {
    const value = candidate.getStatus();
    return typeof value === 'number'
      ? value
      : undefined;
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
  expect(readHttpStatus(observed)).toBe(
    expectedStatus,
  );
};

const orderId =
  '1458c5f0-21ad-4e75-9ec6-0a9641e81866';
const accessToken = 'x'.repeat(43);

class FakeRepository {
  lastInput: CreatePaymentIntentInput | undefined;
  replayIntent: PersistedPaymentIntent | undefined;

  async createIntent(
    input: CreatePaymentIntentInput,
  ): Promise<CreatePaymentIntentResult> {
    this.lastInput = input;

    if (this.replayIntent) {
      return {
        kind: 'REPLAY',
        intent: this.replayIntent,
      };
    }

    return {
      kind: 'CREATED',
      intent: {
        id: input.proposedIntentId,
        orderId: input.orderId,
        orderNumber: 'YS-20260730-ROUTING000001',
        provider: input.provider,
        providerReference: input.providerReference,
        attemptNumber: 1,
        amountMinor: '338000',
        currency: 'VND',
        status: 'CREATED',
        createdAt: input.createdAt,
        expiresAt: input.expiresAt,
        updatedAt: input.createdAt,
        version: 1,
        idempotencyKeyHash:
          input.idempotencyKeyHash,
        requestFingerprint:
          input.requestFingerprint,
      },
    };
  }

  async findIntent(): Promise<null> {
    return null;
  }

  async applyEvent(): Promise<never> {
    throw new Error('not used');
  }
}

class FakeTestProvider {
  calls = 0;
  createIntent(input: {
    intentId: string;
    createdAt: string;
  }) {
    this.calls += 1;
    return {
      providerReference:
        `TST-${input.intentId
          .replaceAll('-', '')
          .slice(0, 24)
          .toUpperCase()}`,
      expiresAt: new Date(
        Date.parse(input.createdAt) + 900_000,
      ).toISOString(),
    };
  }
}

class FakeGPayProvider {
  calls = 0;
  error: PaymentPolicyError | undefined;

  createIntent(input: {
    intentId: string;
    createdAt: string;
  }) {
    this.calls += 1;
    if (this.error) {
      throw this.error;
    }
    return {
      providerReference:
        `GPY-${input.intentId
          .replaceAll('-', '')
          .toUpperCase()}`,
      expiresAt: new Date(
        Date.parse(input.createdAt) + 900_000,
      ).toISOString(),
    };
  }
}

const serviceWith = (
  repository: FakeRepository,
  testProvider = new FakeTestProvider(),
  gpayProvider = new FakeGPayProvider(),
): PaymentService => new PaymentService(
  repository as never,
  testProvider as never,
  gpayProvider as never,
);

describe('payment provider routing', () => {
  it('routes TEST intents to the TEST provider', async () => {
    const repository = new FakeRepository();
    const testProvider = new FakeTestProvider();
    const gpayProvider = new FakeGPayProvider();

    const response = await serviceWith(
      repository,
      testProvider,
      gpayProvider,
    ).createIntent(
      { orderId, provider: 'TEST' },
      'provider-routing-test-0001',
      accessToken,
    );

    expect(testProvider.calls).toBe(1);
    expect(gpayProvider.calls).toBe(0);
    expect(response.intent.provider).toBe('TEST');
    expect(response.intent.providerReference)
      .toMatch(/^TST-/u);
  });

  it('routes GPAY intents to the GPAY provider', async () => {
    const repository = new FakeRepository();
    const testProvider = new FakeTestProvider();
    const gpayProvider = new FakeGPayProvider();

    const response = await serviceWith(
      repository,
      testProvider,
      gpayProvider,
    ).createIntent(
      { orderId, provider: 'GPAY' },
      'provider-routing-gpay-0001',
      accessToken,
    );

    expect(testProvider.calls).toBe(0);
    expect(gpayProvider.calls).toBe(1);
    expect(response.intent.provider).toBe('GPAY');
    expect(response.intent.providerReference)
      .toMatch(/^GPY-[0-9A-F]{32}$/u);
  });

  it('does not depend on TEST availability for GPAY', async () => {
    const testProvider = new FakeTestProvider();
    testProvider.createIntent = () => {
      throw new PaymentPolicyError(
        'TEST payment provider is disabled',
      );
    };

    const response = await serviceWith(
      new FakeRepository(),
      testProvider,
      new FakeGPayProvider(),
    ).createIntent(
      { orderId, provider: 'GPAY' },
      'provider-routing-gpay-0002',
      accessToken,
    );

    expect(response.intent.provider).toBe('GPAY');
  });

  it('persists the GPAY request fingerprint', async () => {
    const repository = new FakeRepository();

    await serviceWith(repository).createIntent(
      { orderId, provider: 'GPAY' },
      'provider-routing-gpay-0003',
      accessToken,
    );

    expect(repository.lastInput?.requestFingerprint)
      .toBe(createPaymentRequestFingerprint({
        orderId,
        provider: 'GPAY',
      }));
    expect(repository.lastInput?.provider).toBe(
      'GPAY',
    );
  });

  it('returns the existing intent on replay', async () => {
    const repository = new FakeRepository();
    repository.replayIntent = {
      id: '2458c5f0-21ad-4e75-9ec6-0a9641e81866',
      orderId,
      orderNumber: 'YS-20260730-REPLAY000001',
      provider: 'GPAY',
      providerReference:
        'GPY-2458C5F021AD4E759EC60A9641E81866',
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

    const response = await serviceWith(
      repository,
    ).createIntent(
      { orderId, provider: 'GPAY' },
      'provider-routing-gpay-0004',
      accessToken,
    );

    expect(response.idempotentReplay).toBe(true);
    expect(response.intent.providerReference).toBe(
      repository.replayIntent.providerReference,
    );
  });

  it('maps a disabled GPAY provider to 503', async () => {
    const gpayProvider = new FakeGPayProvider();
    gpayProvider.error = new PaymentPolicyError(
      'GPAY payment provider is disabled',
    );

    await expectHttpStatus(
      serviceWith(
        new FakeRepository(),
        new FakeTestProvider(),
        gpayProvider,
      ).createIntent(
        { orderId, provider: 'GPAY' },
        'provider-routing-gpay-0005',
        accessToken,
      ),
      503,
    );
  });

  it('maps production activation to 503', async () => {
    const gpayProvider = new FakeGPayProvider();
    gpayProvider.error = new PaymentPolicyError(
      'GPAY payment intent reservation is sandbox-only in VS-R1-012',
    );

    await expectHttpStatus(
      serviceWith(
        new FakeRepository(),
        new FakeTestProvider(),
        gpayProvider,
      ).createIntent(
        { orderId, provider: 'GPAY' },
        'provider-routing-gpay-0006',
        accessToken,
      ),
      503,
    );
  });

  it('maps an unprobed GPAY contract to 503', async () => {
    const gpayProvider = new FakeGPayProvider();
    gpayProvider.error = new PaymentPolicyError(
      'GPAY contract must be PROBED before payment intent reservation',
    );

    await expectHttpStatus(
      serviceWith(
        new FakeRepository(),
        new FakeTestProvider(),
        gpayProvider,
      ).createIntent(
        { orderId, provider: 'GPAY' },
        'provider-routing-gpay-0007',
        accessToken,
      ),
      503,
    );
  });

  it('rejects unknown normalized providers', async () => {
    await expectHttpStatus(
      serviceWith(
        new FakeRepository(),
      ).createIntent(
        {
          orderId,
          provider: 'UNKNOWN' as never,
        },
        'provider-routing-unknown-0001',
        accessToken,
      ),
      400,
    );
  });

  it('returns no provider credentials or request hashes', async () => {
    const response = await serviceWith(
      new FakeRepository(),
    ).createIntent(
      { orderId, provider: 'GPAY' },
      'provider-routing-gpay-0008',
      accessToken,
    );

    const serialized = JSON.stringify(response);

    expect(response.intent).not.toHaveProperty(
      'idempotencyKeyHash',
    );
    expect(response.intent).not.toHaveProperty(
      'requestFingerprint',
    );
    expect(serialized).not.toMatch(
      /private|certificate|credential|secret/iu,
    );
  });
});
