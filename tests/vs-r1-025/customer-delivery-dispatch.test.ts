import { describe, expect, it, vi } from 'vitest';
import { CustomerDeliveryDispatchService } from '../../apps/api/src/modules/delivery/application/customer-delivery-dispatch.service.js';

const instant = new Date('2026-07-31T14:00:00.000Z');

const fixture = (result: unknown = { kind: 'IDLE' }) => {
  const provider = { send: vi.fn() };
  const worker = { processNext: vi.fn().mockResolvedValue(result) };
  const service = new CustomerDeliveryDispatchService(worker as never, provider as never);
  return { provider, service, worker };
};

describe('VS-R1-025 customer delivery runtime composition', () => {
  it('delegates to the worker with the configured provider', async () => {
    const { provider, service, worker } = fixture();
    await service.processNext(instant);
    expect(worker.processNext).toHaveBeenCalledWith(provider, instant);
  });

  it('delegates exactly once per invocation', async () => {
    const { service, worker } = fixture();
    await service.processNext(instant);
    expect(worker.processNext).toHaveBeenCalledTimes(1);
  });

  it('returns IDLE without changing the result', async () => {
    const { service } = fixture({ kind: 'IDLE' });
    await expect(service.processNext(instant)).resolves.toEqual({ kind: 'IDLE' });
  });

  it('returns PUBLISHED receipts without changing them', async () => {
    const result = { kind: 'PUBLISHED', outboxId: 'outbox-1', messageIds: ['msg-1'] };
    const { service } = fixture(result);
    await expect(service.processNext(instant)).resolves.toBe(result);
  });

  it('returns FAILED retry metadata without changing it', async () => {
    const result = { kind: 'FAILED', outboxId: 'outbox-1', retryAt: instant.toISOString(), error: 'disabled' };
    const { service } = fixture(result);
    await expect(service.processNext(instant)).resolves.toBe(result);
  });

  it('returns FENCED without changing the result', async () => {
    const result = { kind: 'FENCED' };
    const { service } = fixture(result);
    await expect(service.processNext(instant)).resolves.toBe(result);
  });

  it('propagates an unexpected worker rejection', async () => {
    const failure = new Error('worker boundary failed');
    const { service, worker } = fixture();
    worker.processNext.mockRejectedValueOnce(failure);
    await expect(service.processNext(instant)).rejects.toBe(failure);
  });

  it('does not call the provider directly', async () => {
    const { provider, service } = fixture();
    await service.processNext(instant);
    expect(provider.send).not.toHaveBeenCalled();
  });

  it('creates a Date when no clock value is supplied', async () => {
    const { service, worker } = fixture();
    await service.processNext();
    expect(worker.processNext.mock.calls[0][1]).toBeInstanceOf(Date);
  });

  it('keeps the provider identity stable across invocations', async () => {
    const { provider, service, worker } = fixture();
    await service.processNext(instant);
    await service.processNext(instant);
    expect(worker.processNext.mock.calls.map((call) => call[0])).toEqual([provider, provider]);
  });
});
