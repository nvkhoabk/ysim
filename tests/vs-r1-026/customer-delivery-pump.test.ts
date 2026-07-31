import { describe, expect, it, vi } from 'vitest';
import { CustomerDeliveryPumpService } from '../../apps/api/src/modules/delivery/application/customer-delivery-pump.service.js';

const idle = () => ({ kind: 'IDLE' as const });
const fenced = () => ({ kind: 'FENCED' as const });
const published = (sequence = 1) => ({
  kind: 'PUBLISHED' as const,
  outboxId: `outbox-${sequence}`,
  messageId: `message-${sequence}`,
});
const failed = (sequence = 1) => ({
  kind: 'FAILED' as const,
  outboxId: `outbox-${sequence}`,
  retryAt: '2026-07-31T00:00:00.000Z',
  error: 'provider unavailable',
});

describe('VS-R1-026 bounded customer delivery pump', () => {
  it('stops immediately on IDLE', async () => {
    const processNext = vi.fn().mockResolvedValue(idle());
    await expect(new CustomerDeliveryPumpService({ processNext } as never).runBatch()).resolves.toEqual({ attempted: 1, published: 0, failed: 0, stopReason: 'IDLE' });
    expect(processNext).toHaveBeenCalledTimes(1);
  });

  it('stops immediately on FENCED', async () => {
    const processNext = vi.fn().mockResolvedValue(fenced());
    await expect(new CustomerDeliveryPumpService({ processNext } as never).runBatch()).resolves.toMatchObject({ attempted: 1, stopReason: 'FENCED' });
  });

  it('counts PUBLISHED results', async () => {
    const processNext = vi.fn().mockResolvedValueOnce(published()).mockResolvedValueOnce(idle());
    await expect(new CustomerDeliveryPumpService({ processNext } as never).runBatch()).resolves.toEqual({ attempted: 2, published: 1, failed: 0, stopReason: 'IDLE' });
  });

  it('counts FAILED results and continues', async () => {
    const processNext = vi.fn().mockResolvedValueOnce(failed()).mockResolvedValueOnce(idle());
    await expect(new CustomerDeliveryPumpService({ processNext } as never).runBatch()).resolves.toEqual({ attempted: 2, published: 0, failed: 1, stopReason: 'IDLE' });
  });

  it('stops at the requested budget', async () => {
    const processNext = vi.fn().mockResolvedValue(published());
    await expect(new CustomerDeliveryPumpService({ processNext } as never).runBatch(3)).resolves.toEqual({ attempted: 3, published: 3, failed: 0, stopReason: 'BUDGET_EXHAUSTED' });
    expect(processNext).toHaveBeenCalledTimes(3);
  });

  it.each([0, -1, 101, 1.5, Number.NaN])('rejects an invalid budget: %s', async (value) => {
    const processNext = vi.fn();
    await expect(new CustomerDeliveryPumpService({ processNext } as never).runBatch(value)).rejects.toThrow(RangeError);
    expect(processNext).not.toHaveBeenCalled();
  });

  it('propagates an unexpected dispatch rejection', async () => {
    const processNext = vi.fn().mockRejectedValue(new Error('unexpected'));
    await expect(new CustomerDeliveryPumpService({ processNext } as never).runBatch()).rejects.toThrow('unexpected');
  });

  it('does not overlap calls within one batch', async () => {
    let active = 0;
    let peak = 0;
    const processNext = vi.fn(async () => {
      active += 1;
      peak = Math.max(peak, active);
      await Promise.resolve();
      active -= 1;
      return published();
    });
    await new CustomerDeliveryPumpService({ processNext } as never).runBatch(4);
    expect(peak).toBe(1);
  });
});
