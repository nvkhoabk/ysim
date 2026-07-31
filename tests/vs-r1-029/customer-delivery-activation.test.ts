import { describe, expect, it, vi } from 'vitest';
import { CustomerDeliveryActivationService } from '../../apps/api/src/modules/delivery/application/customer-delivery-activation.service.js';

const notReady = (reason = 'SCHEDULER_DISABLED') => ({ ready: false, reason, schedulerEnabled: false, emailMode: 'disabled' });
const ready = () => ({ ready: true, reason: 'READY', schedulerEnabled: true, emailMode: 'live' });

function subject(report: unknown = notReady()) {
  const readiness = { evaluate: vi.fn(() => report) };
  const scheduler = { start: vi.fn(), stop: vi.fn() };
  return { service: new CustomerDeliveryActivationService(readiness as never, scheduler as never), readiness, scheduler };
}

describe('VS-R1-029 readiness-guarded delivery activation', () => {
  it('does not start when scheduler is disabled', () => { const x = subject(); expect(x.service.activate()).toEqual({ active: false, reason: 'SCHEDULER_DISABLED' }); expect(x.scheduler.start).not.toHaveBeenCalled(); });
  it('does not start when email provider is not live', () => { const x = subject(notReady('EMAIL_PROVIDER_NOT_LIVE')); expect(x.service.activate()).toEqual({ active: false, reason: 'EMAIL_PROVIDER_NOT_LIVE' }); expect(x.scheduler.start).not.toHaveBeenCalled(); });
  it('does not start when configuration is invalid', () => { const x = subject(notReady('CONFIG_INVALID')); expect(x.service.activate()).toEqual({ active: false, reason: 'CONFIG_INVALID' }); expect(x.scheduler.start).not.toHaveBeenCalled(); });
  it('starts once when readiness is READY', () => { const x = subject(ready()); expect(x.service.activate()).toEqual({ active: true, reason: 'READY' }); expect(x.scheduler.start).toHaveBeenCalledTimes(1); });
  it('keeps activation idempotent', () => { const x = subject(ready()); x.service.activate(); x.service.activate(); expect(x.scheduler.start).toHaveBeenCalledTimes(1); expect(x.readiness.evaluate).toHaveBeenCalledTimes(1); });
  it('passes explicit environment to readiness', () => { const x = subject(); const env = { TEST: 'value' }; x.service.activate(env); expect(x.readiness.evaluate).toHaveBeenCalledWith(env); });
  it('fails closed when readiness throws', () => { const x = subject(); x.readiness.evaluate.mockImplementation(() => { throw new Error('secret'); }); expect(x.service.activate()).toEqual({ active: false, reason: 'READINESS_ERROR' }); expect(x.scheduler.start).not.toHaveBeenCalled(); });
  it('fails closed when scheduler start throws', () => { const x = subject(ready()); x.scheduler.start.mockImplementation(() => { throw new Error('secret'); }); expect(x.service.activate()).toEqual({ active: false, reason: 'READINESS_ERROR' }); });
  it('activates through module initialization', () => { const x = subject(ready()); x.service.onModuleInit(); expect(x.scheduler.start).toHaveBeenCalledTimes(1); });
  it('always stops on module shutdown', () => { const x = subject(); x.service.onModuleDestroy(); expect(x.scheduler.stop).toHaveBeenCalledTimes(1); });
  it('deactivation is idempotent', () => { const x = subject(ready()); x.service.activate(); x.service.deactivate(); x.service.deactivate(); expect(x.scheduler.stop).toHaveBeenCalledTimes(2); });
  it('can activate again after deactivation', () => { const x = subject(ready()); x.service.activate(); x.service.deactivate(); x.service.activate(); expect(x.scheduler.start).toHaveBeenCalledTimes(2); });
  it('returns only safe reason codes', () => { const x = subject(); x.readiness.evaluate.mockImplementation(() => { throw new Error('token=top-secret'); }); expect(JSON.stringify(x.service.activate())).not.toMatch(/token|secret/); });
});
