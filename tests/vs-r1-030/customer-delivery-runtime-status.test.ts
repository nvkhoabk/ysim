import { describe, expect, it, vi } from 'vitest';
import { CustomerDeliveryRuntimeStatusService } from '../../apps/api/src/modules/delivery/application/customer-delivery-runtime-status.service.js';

const ready = { ready: true, reason: 'READY', schedulerEnabled: true, emailMode: 'live' } as const;
const make = (report: unknown = ready, active = false) => {
  const readiness = { evaluate: vi.fn(() => report) };
  const activation = { isActive: vi.fn(() => active), activate: vi.fn(), deactivate: vi.fn() };
  return { service: new CustomerDeliveryRuntimeStatusService(readiness as never, activation as never), readiness, activation };
};

describe('VS-R1-030 safe customer delivery runtime status (12)', () => {
  it('reports INACTIVE when ready but not activated', () => expect(make().service.snapshot()).toEqual({ state: 'INACTIVE', reason: 'READY', schedulerEnabled: true, emailMode: 'live' }));
  it('reports ACTIVE when ready and activated', () => expect(make(ready, true).service.snapshot()).toEqual({ state: 'ACTIVE', reason: 'READY', schedulerEnabled: true, emailMode: 'live' }));
  it('reports scheduler disabled as BLOCKED', () => expect(make({ ready: false, reason: 'SCHEDULER_DISABLED', schedulerEnabled: false, emailMode: 'live' }).service.snapshot().state).toBe('BLOCKED'));
  it('reports non-live email as BLOCKED', () => expect(make({ ready: false, reason: 'EMAIL_PROVIDER_NOT_LIVE', schedulerEnabled: true, emailMode: 'dry-run' }).service.snapshot()).toMatchObject({ state: 'BLOCKED', reason: 'EMAIL_PROVIDER_NOT_LIVE' }));
  it('reports invalid config as BLOCKED', () => expect(make({ ready: false, reason: 'CONFIG_INVALID', schedulerEnabled: false, emailMode: 'invalid' }).service.snapshot()).toMatchObject({ state: 'BLOCKED', reason: 'CONFIG_INVALID' }));
  it('fails closed when readiness throws', () => { const x = make(); x.readiness.evaluate.mockImplementation(() => { throw new Error('secret'); }); expect(x.service.snapshot()).toEqual({ state: 'ERROR', reason: 'READINESS_ERROR', schedulerEnabled: false, emailMode: 'invalid' }); });
  it('fails closed for active but not ready contradiction', () => expect(make({ ready: false, reason: 'SCHEDULER_DISABLED', schedulerEnabled: false, emailMode: 'live' }, true).service.snapshot().state).toBe('ERROR'));
  it('fails closed for malformed ready reason', () => expect(make({ ready: true, reason: 'CONFIG_INVALID', schedulerEnabled: true, emailMode: 'live' }).service.snapshot().state).toBe('ERROR'));
  it('passes explicit environment to readiness', () => { const x = make(); const env = { CUSTOMER_DELIVERY_SCHEDULER_ENABLED: 'false' }; x.service.snapshot(env); expect(x.readiness.evaluate).toHaveBeenCalledWith(env); });
  it('does not activate while observing', () => { const x = make(); x.service.snapshot(); expect(x.activation.activate).not.toHaveBeenCalled(); });
  it('does not deactivate while observing', () => { const x = make(); x.service.snapshot(); expect(x.activation.deactivate).not.toHaveBeenCalled(); });
  it('returns only redacted bounded fields', () => expect(Object.keys(make().service.snapshot()).sort()).toEqual(['emailMode', 'reason', 'schedulerEnabled', 'state']));
});
