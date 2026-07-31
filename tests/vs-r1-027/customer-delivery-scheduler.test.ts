import { afterEach, describe, expect, it, vi } from 'vitest';
import { CustomerDeliverySchedulerService } from '../../apps/api/src/modules/delivery/application/customer-delivery-scheduler.service.js';
import { CustomerDeliverySchedulerConfig } from '../../apps/api/src/modules/delivery/infrastructure/customer-delivery-scheduler.config.js';

const summary = { attempted: 1, published: 0, failed: 0, stopReason: 'IDLE' as const };
const options = (enabled = false) => ({ enabled, intervalMs: 1000, batchSize: 7 });

afterEach(() => vi.useRealTimers());

describe('VS-R1-027 customer delivery scheduler adapter', () => {
  it('is disabled by default', () => expect(new CustomerDeliverySchedulerConfig({})).toMatchObject({ enabled: false, intervalMs: 30000, batchSize: 25 }));
  it('parses bounded configuration', () => expect(new CustomerDeliverySchedulerConfig({ YSIM_CUSTOMER_DELIVERY_SCHEDULER_ENABLED: 'true', YSIM_CUSTOMER_DELIVERY_SCHEDULER_INTERVAL_MS: '5000', YSIM_CUSTOMER_DELIVERY_SCHEDULER_BATCH_SIZE: '10' })).toMatchObject({ enabled: true, intervalMs: 5000, batchSize: 10 }));
  it.each([
    ['YSIM_CUSTOMER_DELIVERY_SCHEDULER_ENABLED', 'yes'],
    ['YSIM_CUSTOMER_DELIVERY_SCHEDULER_INTERVAL_MS', '999'],
    ['YSIM_CUSTOMER_DELIVERY_SCHEDULER_INTERVAL_MS', '1.5'],
    ['YSIM_CUSTOMER_DELIVERY_SCHEDULER_BATCH_SIZE', '0'],
    ['YSIM_CUSTOMER_DELIVERY_SCHEDULER_BATCH_SIZE', '101'],
  ])('rejects invalid %s', (key, value) => expect(() => new CustomerDeliverySchedulerConfig({ [key]: value })).toThrow());
  it('does not schedule on module init when disabled', () => { vi.useFakeTimers(); const runBatch = vi.fn(); new CustomerDeliverySchedulerService({ runBatch } as never, options() as never).onModuleInit(); vi.advanceTimersByTime(5000); expect(runBatch).not.toHaveBeenCalled(); });
  it('runs with configured batch size after the interval', async () => { vi.useFakeTimers(); const runBatch = vi.fn().mockResolvedValue(summary); const service = new CustomerDeliverySchedulerService({ runBatch } as never, options(true) as never); service.onModuleInit(); await vi.advanceTimersByTimeAsync(1000); expect(runBatch).toHaveBeenCalledWith(7); service.onModuleDestroy(); });
  it('prevents overlapping manual triggers', async () => { let resolve!: (value: typeof summary) => void; const pending = new Promise<typeof summary>((done) => { resolve = done; }); const runBatch = vi.fn().mockReturnValue(pending); const service = new CustomerDeliverySchedulerService({ runBatch } as never, options() as never); const first = service.triggerNow(); const second = service.triggerNow(); expect(runBatch).toHaveBeenCalledTimes(1); resolve(summary); await expect(Promise.all([first, second])).resolves.toEqual([summary, summary]); });
  it('allows a later trigger after completion', async () => { const runBatch = vi.fn().mockResolvedValue(summary); const service = new CustomerDeliverySchedulerService({ runBatch } as never, options() as never); await service.triggerNow(); await service.triggerNow(); expect(runBatch).toHaveBeenCalledTimes(2); });
  it('stops future ticks on shutdown', async () => { vi.useFakeTimers(); const runBatch = vi.fn().mockResolvedValue(summary); const service = new CustomerDeliverySchedulerService({ runBatch } as never, options(true) as never); service.onModuleInit(); service.onModuleDestroy(); await vi.advanceTimersByTimeAsync(5000); expect(runBatch).not.toHaveBeenCalled(); });
  it('continues scheduling after a rejected tick', async () => { vi.useFakeTimers(); const runBatch = vi.fn().mockRejectedValueOnce(new Error('provider details')).mockResolvedValue(summary); const service = new CustomerDeliverySchedulerService({ runBatch } as never, options(true) as never); service.onModuleInit(); await vi.advanceTimersByTimeAsync(2000); expect(runBatch).toHaveBeenCalledTimes(2); service.onModuleDestroy(); });
});
