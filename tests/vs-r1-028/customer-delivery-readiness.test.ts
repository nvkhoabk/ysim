import { describe, expect, it } from 'vitest';
import { CustomerDeliveryReadinessService } from '../../apps/api/src/modules/delivery/application/customer-delivery-readiness.service.js';

const service = new CustomerDeliveryReadinessService();
const live = {
  YSIM_CUSTOMER_DELIVERY_SCHEDULER_ENABLED: 'true',
  YSIM_CUSTOMER_EMAIL_MODE: 'live',
  YSIM_CUSTOMER_EMAIL_ENDPOINT: 'https://mail.example/send',
  YSIM_CUSTOMER_EMAIL_TOKEN: 'secret',
};

describe('VS-R1-028 customer delivery runtime readiness gate', () => {
  it('is not ready by default', () => expect(service.evaluate({})).toMatchObject({ ready: false, reason: 'SCHEDULER_DISABLED' }));
  it('rejects disabled scheduler with live email', () => expect(service.evaluate({ ...live, YSIM_CUSTOMER_DELIVERY_SCHEDULER_ENABLED: 'false' })).toMatchObject({ ready: false, reason: 'SCHEDULER_DISABLED' }));
  it('rejects enabled scheduler with disabled email', () => expect(service.evaluate({ YSIM_CUSTOMER_DELIVERY_SCHEDULER_ENABLED: 'true' })).toMatchObject({ ready: false, reason: 'EMAIL_PROVIDER_NOT_LIVE', emailMode: 'disabled' }));
  it('rejects enabled scheduler with dry-run email', () => expect(service.evaluate({ YSIM_CUSTOMER_DELIVERY_SCHEDULER_ENABLED: 'true', YSIM_CUSTOMER_EMAIL_MODE: 'dry-run' })).toMatchObject({ ready: false, reason: 'EMAIL_PROVIDER_NOT_LIVE', emailMode: 'dry-run' }));
  it('reports ready for bounded scheduler and valid live email', () => expect(service.evaluate(live)).toEqual({ ready: true, reason: 'READY', schedulerEnabled: true, emailMode: 'live' }));
  it('fails closed for invalid scheduler enable value', () => expect(service.evaluate({ ...live, YSIM_CUSTOMER_DELIVERY_SCHEDULER_ENABLED: 'yes' })).toMatchObject({ ready: false, reason: 'CONFIG_INVALID' }));
  it('fails closed for invalid scheduler interval', () => expect(service.evaluate({ ...live, YSIM_CUSTOMER_DELIVERY_SCHEDULER_INTERVAL_MS: '999' })).toMatchObject({ ready: false, reason: 'CONFIG_INVALID' }));
  it('fails closed for invalid scheduler batch size', () => expect(service.evaluate({ ...live, YSIM_CUSTOMER_DELIVERY_SCHEDULER_BATCH_SIZE: '101' })).toMatchObject({ ready: false, reason: 'CONFIG_INVALID' }));
  it('fails closed for missing live token', () => { const { YSIM_CUSTOMER_EMAIL_TOKEN: _, ...env } = live; expect(service.evaluate(env)).toMatchObject({ ready: false, reason: 'CONFIG_INVALID' }); });
  it('fails closed for non-HTTPS live endpoint', () => expect(service.evaluate({ ...live, YSIM_CUSTOMER_EMAIL_ENDPOINT: 'http://mail.example/send' })).toMatchObject({ ready: false, reason: 'CONFIG_INVALID' }));
  it('does not expose configuration values', () => expect(JSON.stringify(service.evaluate({ ...live, YSIM_CUSTOMER_EMAIL_ENDPOINT: 'http://buyer@example.com/secret', YSIM_CUSTOMER_EMAIL_TOKEN: 'top-secret' }))).not.toMatch(/buyer|secret|http:/));
  it('is deterministic and side-effect free', () => expect(service.evaluate(live)).toEqual(service.evaluate(live)));
});
