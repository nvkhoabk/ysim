import { describe, expect, it, vi } from 'vitest';
import { CustomerDeliveryOperatorStatusQueryService } from '../../apps/api/src/modules/delivery/application/customer-delivery-operator-status-query.service.js';

const token = 'operator-token-that-is-at-least-32-characters';
const active = { state: 'ACTIVE', reason: 'READY', schedulerEnabled: true, emailMode: 'live' } as const;
const make = (snapshot: unknown = active) => {
  const status = { snapshot: vi.fn(() => snapshot) };
  return { service: new CustomerDeliveryOperatorStatusQueryService(status as never), status };
};
const env = { CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN: token };

describe('VS-R1-031 guarded operator delivery status query (12)', () => {
  it('returns the bounded snapshot for a valid credential', () => expect(make().service.query(token, env)).toEqual({ authorized: true, status: active }));
  it('rejects a wrong credential', () => expect(make().service.query('wrong-credential-value-that-is-long-enough', env)).toEqual({ authorized: false, reason: 'ACCESS_DENIED' }));
  it('rejects an empty presented credential', () => expect(make().service.query('', env)).toEqual({ authorized: false, reason: 'ACCESS_DENIED' }));
  it('fails closed when the configured credential is missing', () => expect(make().service.query(token, {})).toEqual({ authorized: false, reason: 'CONFIG_INVALID' }));
  it('fails closed when the configured credential is too short', () => expect(make().service.query(token, { CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN: 'short' })).toEqual({ authorized: false, reason: 'CONFIG_INVALID' }));
  it('does not read status after access denial', () => { const x = make(); x.service.query('wrong-credential-value-that-is-long-enough', env); expect(x.status.snapshot).not.toHaveBeenCalled(); });
  it('does not read status after invalid configuration', () => { const x = make(); x.service.query(token, {}); expect(x.status.snapshot).not.toHaveBeenCalled(); });
  it('passes the explicit environment to runtime status', () => { const x = make(); x.service.query(token, env); expect(x.status.snapshot).toHaveBeenCalledWith(env); });
  it('maps runtime status failures to a bounded error', () => { const x = make(); x.status.snapshot.mockImplementation(() => { throw new Error('secret endpoint and token'); }); expect(x.service.query(token, env)).toEqual({ authorized: false, reason: 'STATUS_UNAVAILABLE' }); });
  it('does not include the presented credential in an authorized result', () => expect(JSON.stringify(make().service.query(token, env))).not.toContain(token));
  it('does not include the configured credential in a denied result', () => expect(JSON.stringify(make().service.query('wrong-credential-value-that-is-long-enough', env))).not.toContain(token));
  it('returns only bounded top-level fields', () => expect(Object.keys(make().service.query(token, env)).sort()).toEqual(['authorized', 'status']));
});
