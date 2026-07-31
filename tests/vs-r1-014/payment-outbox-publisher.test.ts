import {
  describe,
  expect,
  it,
  vi,
} from 'vitest';

import {
  PaymentIntegrationOutboxPublisher,
} from '../../apps/api/src/modules/payment/application/payment-integration-outbox.publisher.js';
import type {
  ClaimedPaymentIntegrationOutboxRecord,
} from '../../apps/api/src/modules/payment/domain/payment-outbox-policy.js';

const occurredAt =
  '2026-07-30T10:00:00.000Z';
const claimed:
  ClaimedPaymentIntegrationOutboxRecord = {
    id: '10000000-0000-4000-8000-000000000014',
    eventType: 'payment.succeeded.v1',
    aggregateType: 'PaymentIntent',
    aggregateId:
      '20000000-0000-4000-8000-000000000014',
    orderId:
      '30000000-0000-4000-8000-000000000014',
    deduplicationKey: 'a'.repeat(64),
    payload: {
      paymentIntentId:
        '20000000-0000-4000-8000-000000000014',
      orderId:
        '30000000-0000-4000-8000-000000000014',
      orderNumber:
        'YS-20260730-014ABCDEF014',
      provider: 'GPAY',
      providerReference:
        'GPY-20000000000040008000000000000014',
      amountMinor: '338000',
      currency: 'VND',
      occurredAt,
    },
    occurredAt,
    attemptCount: 1,
  };

class FakeRepository {
  claimed:
    ClaimedPaymentIntegrationOutboxRecord | null =
      claimed;
  published = true;
  failed = true;
  claimInputs: unknown[] = [];
  publishInputs: unknown[] = [];
  failureInputs: unknown[] = [];

  async claimNext(input: unknown) {
    this.claimInputs.push(input);
    const value = this.claimed;
    this.claimed = null;
    return value;
  }

  async markPublished(input: unknown) {
    this.publishInputs.push(input);
    return this.published;
  }

  async markFailed(input: unknown) {
    this.failureInputs.push(input);
    return this.failed;
  }
}

const publisherWith = (
  repository: FakeRepository,
): PaymentIntegrationOutboxPublisher =>
  new PaymentIntegrationOutboxPublisher(
    repository as never,
  );

const options = {
  now: new Date(occurredAt),
  environment: {
    YSIM_PAYMENT_OUTBOX_LEASE_SECONDS:
      '30',
  },
};

describe('Payment Integration Outbox publisher', () => {
  it('returns IDLE when no event is available', async () => {
    const repository = new FakeRepository();
    repository.claimed = null;

    const result =
      await publisherWith(
        repository,
      ).publishNext(
        { publish: vi.fn() },
        options,
      );

    expect(result).toEqual({
      kind: 'IDLE',
    });
  });

  it('publishes a claimed event', async () => {
    const repository = new FakeRepository();
    const sink = {
      publish: vi.fn().mockResolvedValue(
        undefined,
      ),
    };

    const result =
      await publisherWith(
        repository,
      ).publishNext(sink, options);

    expect(result.kind).toBe('PUBLISHED');
    expect(sink.publish).toHaveBeenCalledTimes(
      1,
    );
  });

  it('passes the normalized event to the sink', async () => {
    const repository = new FakeRepository();
    const received: unknown[] = [];

    await publisherWith(
      repository,
    ).publishNext(
      {
        async publish(event) {
          received.push(event);
        },
      },
      options,
    );

    expect(received).toHaveLength(1);
    expect(received[0]).toMatchObject({
      eventType: 'payment.succeeded.v1',
      aggregateType: 'PaymentIntent',
    });
  });

  it('claims with a bounded lease', async () => {
    const repository = new FakeRepository();

    await publisherWith(
      repository,
    ).publishNext(
      { publish: vi.fn() },
      options,
    );

    expect(repository.claimInputs[0])
      .toEqual({
        now: occurredAt,
        leaseUntil:
          '2026-07-30T10:00:30.000Z',
      });
  });

  it('marks the exact claimed attempt published', async () => {
    const repository = new FakeRepository();

    await publisherWith(
      repository,
    ).publishNext(
      { publish: vi.fn() },
      options,
    );

    expect(repository.publishInputs[0])
      .toEqual({
        eventId: claimed.id,
        attemptCount: 1,
        publishedAt: occurredAt,
      });
  });

  it('records a retry when the sink fails', async () => {
    const repository = new FakeRepository();

    const result =
      await publisherWith(
        repository,
      ).publishNext(
        {
          async publish() {
            throw new Error(
              'temporary failure',
            );
          },
        },
        options,
      );

    expect(result.kind).toBe('FAILED');
    expect(repository.failureInputs)
      .toHaveLength(1);
    expect(repository.publishInputs)
      .toHaveLength(0);
  });

  it('stores only a sanitized retry error', async () => {
    const repository = new FakeRepository();

    const result =
      await publisherWith(
        repository,
      ).publishNext(
        {
          async publish() {
            throw new Error(
              'Bearer abc token=secret-value',
            );
          },
        },
        options,
      );

    expect(result).toMatchObject({
      kind: 'FAILED',
      retryAt:
        '2026-07-30T10:00:05.000Z',
    });
    const failure =
      repository.failureInputs[0] as {
        lastError: string;
      };
    expect(failure.lastError).not.toContain(
      'secret-value',
    );
  });

  it('reports a lost publish lease', async () => {
    const repository = new FakeRepository();
    repository.published = false;

    const result =
      await publisherWith(
        repository,
      ).publishNext(
        { publish: vi.fn() },
        options,
      );

    expect(result).toEqual({
      kind: 'LEASE_LOST',
      eventId: claimed.id,
      attemptCount: 1,
    });
  });

  it('reports a lost failure lease', async () => {
    const repository = new FakeRepository();
    repository.failed = false;

    const result =
      await publisherWith(
        repository,
      ).publishNext(
        {
          async publish() {
            throw new Error('failed');
          },
        },
        options,
      );

    expect(result.kind).toBe(
      'LEASE_LOST',
    );
  });

  it('fails a malformed event without calling the sink', async () => {
    const repository = new FakeRepository();
    repository.claimed = {
      ...claimed,
      eventType: 'payment.failed.v1',
    };
    const sink = {
      publish: vi.fn(),
    };

    const result =
      await publisherWith(
        repository,
      ).publishNext(sink, options);

    expect(result.kind).toBe('FAILED');
    expect(sink.publish).not.toHaveBeenCalled();
    expect(repository.failureInputs)
      .toHaveLength(1);
  });
});
