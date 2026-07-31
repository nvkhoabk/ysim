import { describe, expect, it, vi } from 'vitest';

import { ProcurementOutboxConsumerService } from '../../apps/api/src/modules/procurement/application/procurement-outbox-consumer.service.js';
import { ProcurementPaymentSuccessSink } from '../../apps/api/src/modules/procurement/application/procurement-payment-success.sink.js';

const occurredAt = '2026-07-31T03:00:00.000Z';
const event = {
  eventId: '10000000-0000-4000-8000-000000000015',
  eventType: 'payment.succeeded.v1' as const,
  aggregateType: 'PaymentIntent' as const,
  aggregateId: '20000000-0000-4000-8000-000000000015',
  orderId: '30000000-0000-4000-8000-000000000015',
  deduplicationKey: 'a'.repeat(64),
  payload: {
    paymentIntentId: '20000000-0000-4000-8000-000000000015',
    orderId: '30000000-0000-4000-8000-000000000015',
    orderNumber: 'YS-20260731-015ABCDEF015',
    provider: 'GPAY' as const,
    providerReference: 'GPY-20000000000040008000000000000015',
    amountMinor: '338000',
    currency: 'VND' as const,
    occurredAt,
  },
  occurredAt,
};

const source = {
  orderId: event.orderId,
  orderNumber: event.payload.orderNumber,
  productOfferId: '40000000-0000-4000-8000-000000000015',
  quantity: 2,
  totalAmountMinor: '338000',
  currency: 'VND' as const,
  orderStatus: 'CONFIRMED',
  orderPaymentStatus: 'PAID',
  fulfillmentStatus: 'UNFULFILLED',
  supplierPlanMappingId: '50000000-0000-4000-8000-000000000015',
  supplierEnvironmentId: '60000000-0000-4000-8000-000000000015',
  supplierPlanId: '70000000-0000-4000-8000-000000000015',
  supplierCode: 'GIGAGO',
  supplierEnvironment: 'SANDBOX' as const,
  supplierContractStatus: 'PROBED',
  supplierCreateOrderMethod: 'PUT',
  externalPlanId: 'GIGAGO_JP_FIXED_5GB_7D',
};

class FakeReader {
  result: typeof source | null = source;
  async findReadySource() {
    return this.result;
  }
}

class FakeRepository {
  result: any = {
    kind: 'CREATED',
    requestId: '80000000-0000-4000-8000-000000000015',
    status: 'PENDING_SUPPLIER',
  };
  calls: unknown[] = [];
  async createFromPaymentSuccess(input: unknown) {
    this.calls.push(input);
    return this.result;
  }
}

const sinkWith = (
  reader = new FakeReader(),
  repository = new FakeRepository(),
) => new ProcurementPaymentSuccessSink(
  reader as never,
  repository as never,
);

describe('Procurement Payment Success sink', () => {
  it('creates one Procurement Request', async () => {
    const result = await sinkWith().consume(event);
    expect(result.kind).toBe('CREATED');
    expect(result.status).toBe('PENDING_SUPPLIER');
  });

  it('accepts an idempotent replay', async () => {
    const repository = new FakeRepository();
    repository.result = {
      kind: 'REPLAY',
      requestId: '80000000-0000-4000-8000-000000000015',
      status: 'PENDING_SUPPLIER',
    };
    expect((await sinkWith(
      new FakeReader(),
      repository,
    ).consume(event)).kind).toBe('REPLAY');
  });

  it('fails when the source snapshot is unavailable', async () => {
    const reader = new FakeReader();
    reader.result = null;
    await expect(
      sinkWith(reader).consume(event),
    ).rejects.toThrow('PROCUREMENT_SOURCE_NOT_READY');
  });

  it('fails closed on a repository conflict', async () => {
    const repository = new FakeRepository();
    repository.result = { kind: 'CONFLICT' };
    await expect(
      sinkWith(new FakeReader(), repository).consume(event),
    ).rejects.toThrow('PROCUREMENT_REQUEST_CONFLICT');
  });

  it('passes the immutable supplier mapping snapshot', async () => {
    const repository = new FakeRepository();
    await sinkWith(new FakeReader(), repository).consume(event);
    expect(repository.calls[0]).toMatchObject({
      supplierCode: 'GIGAGO',
      supplierEnvironment: 'SANDBOX',
      externalPlanId: 'GIGAGO_JP_FIXED_5GB_7D',
      quantity: 2,
    });
  });

  it('exposes the sink-compatible publish method', async () => {
    await expect(
      sinkWith().publish(event),
    ).resolves.toBeUndefined();
  });

  it('does not perform an external request', async () => {
    const fetchSpy = vi.fn();
    vi.stubGlobal('fetch', fetchSpy);
    await sinkWith().consume(event);
    expect(fetchSpy).not.toHaveBeenCalled();
    vi.unstubAllGlobals();
  });

  it('delegates one outbox item through the consumer', async () => {
    const publisher = {
      publishNext: vi.fn().mockResolvedValue({
        kind: 'PUBLISHED',
        eventId: event.eventId,
        attemptCount: 1,
        publishedAt: occurredAt,
      }),
    };
    const sink = sinkWith();
    const consumer = new ProcurementOutboxConsumerService(
      publisher as never,
      sink,
    );
    const result = await consumer.processNext({
      now: new Date(occurredAt),
    });
    expect(result.kind).toBe('PUBLISHED');
    expect(publisher.publishNext).toHaveBeenCalledWith(
      sink,
      { now: new Date(occurredAt) },
    );
  });

  it('preserves an IDLE publisher result', async () => {
    const publisher = {
      publishNext: vi.fn().mockResolvedValue({
        kind: 'IDLE',
      }),
    };
    const consumer = new ProcurementOutboxConsumerService(
      publisher as never,
      sinkWith(),
    );
    expect((await consumer.processNext()).kind).toBe('IDLE');
  });

  it('does not start a scheduler', () => {
    const sourceText =
      ProcurementOutboxConsumerService.toString();
    expect(sourceText).not.toMatch(
      /setInterval|setTimeout/iu,
    );
  });
});
