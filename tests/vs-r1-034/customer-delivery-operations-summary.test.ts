import { readFileSync } from 'node:fs';
import { describe, expect, it, vi } from 'vitest';
import { CustomerDeliveryOperationsSummaryService } from '../../apps/api/src/modules/delivery/application/customer-delivery-operations-summary.service.js';

const now = new Date('2026-08-01T03:00:00.000Z');
const counts = {
  pending: 7,
  failed: 2,
  published: 31,
  inFlight: 1,
  actionable: 5,
  oldestActionableAt: '2026-08-01T02:45:00.000Z',
};
const make = (value: unknown = counts) => {
  const repository = { load: vi.fn(async () => value) };
  return {
    service: new CustomerDeliveryOperationsSummaryService(repository as never),
    repository,
  };
};
const repositorySource = readFileSync(
  new URL('../../apps/api/src/modules/delivery/infrastructure/customer-delivery-operations-summary.repository.ts', import.meta.url),
  'utf8',
);
const moduleSource = readFileSync(
  new URL('../../apps/api/src/modules/delivery/delivery.module.ts', import.meta.url),
  'utf8',
);

describe('VS-R1-034 read-only delivery operations summary (12)', () => {
  it('returns a bounded operational summary', async () => expect(make().service.snapshot(now)).resolves.toEqual({ available: true, summary: { generatedAt: now.toISOString(), ...counts } }));
  it('passes the exact observation time to the repository', async () => { const x = make(); await x.service.snapshot(now); expect(x.repository.load).toHaveBeenCalledOnce(); expect(x.repository.load).toHaveBeenCalledWith(now); });
  it('accepts a null oldest actionable timestamp', async () => expect(make({ ...counts, actionable: 0, oldestActionableAt: null }).service.snapshot(now)).resolves.toMatchObject({ available: true, summary: { oldestActionableAt: null } }));
  it('fails closed when the repository throws', async () => { const x = make(); x.repository.load.mockRejectedValue(new Error('database endpoint and recipient secret')); await expect(x.service.snapshot(now)).resolves.toEqual({ available: false, reason: 'SUMMARY_UNAVAILABLE' }); });
  it('does not query for an invalid observation time', async () => { const x = make(); await expect(x.service.snapshot(new Date('invalid'))).resolves.toEqual({ available: false, reason: 'SUMMARY_UNAVAILABLE' }); expect(x.repository.load).not.toHaveBeenCalled(); });
  it('rejects negative counters', async () => expect(make({ ...counts, failed: -1 }).service.snapshot(now)).resolves.toEqual({ available: false, reason: 'SUMMARY_UNAVAILABLE' }));
  it('rejects non-integer counters', async () => expect(make({ ...counts, pending: 1.5 }).service.snapshot(now)).resolves.toEqual({ available: false, reason: 'SUMMARY_UNAVAILABLE' }));
  it('rejects contradictory actionable and in-flight counters', async () => expect(make({ ...counts, pending: 1, failed: 0, inFlight: 1, actionable: 1 }).service.snapshot(now)).resolves.toEqual({ available: false, reason: 'SUMMARY_UNAVAILABLE' }));
  it('rejects an invalid oldest actionable timestamp', async () => expect(make({ ...counts, oldestActionableAt: 'not-a-date' }).service.snapshot(now)).resolves.toEqual({ available: false, reason: 'SUMMARY_UNAVAILABLE' }));
  it('exposes no recipient, order, token, lease token or error detail', async () => { const output = JSON.stringify(await make().service.snapshot(now)); expect(output).not.toMatch(/recipient|orderNumber|token|lastError|leaseToken|database endpoint/i); expect(Object.keys((await make().service.snapshot(now) as { summary: object }).summary).sort()).toEqual(['actionable', 'failed', 'generatedAt', 'inFlight', 'oldestActionableAt', 'pending', 'published']); });
  it('uses a single read-only aggregate query without sensitive columns', () => { expect(repositorySource.match(/database\.query/g)).toHaveLength(1); expect(repositorySource).toMatch(/SELECT[\s\S]+FROM delivery\.integration_outbox/); expect(repositorySource).not.toMatch(/\b(INSERT|UPDATE|DELETE|TRUNCATE|recipient_email|order_number|payload|last_error)\b/i); });
  it('registers and exports the summary providers without adding a controller', () => { expect(moduleSource).toContain('CustomerDeliveryOperationsSummaryRepository'); expect(moduleSource).toContain('CustomerDeliveryOperationsSummaryService'); expect(moduleSource.match(/controllers:\s*\[CustomerDeliveryOperatorStatusController\]/g)).toHaveLength(1); });
});
