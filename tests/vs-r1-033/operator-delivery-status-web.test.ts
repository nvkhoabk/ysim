import { describe, expect, it, vi } from 'vitest';
import { readFileSync } from 'node:fs';
import { readOperatorDeliveryStatus } from '../../apps/web/app/operator/delivery-status/operator-delivery-status.js';

const token = 'operator-token-that-is-at-least-32-characters';
const env = { YSIM_API_INTERNAL_BASE_URL: 'http://api.internal:3000', CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN: token };
const active = { authorized: true, status: { state: 'ACTIVE', reason: 'READY', schedulerEnabled: true, emailMode: 'live' } } as const;
const response = (body: unknown, ok = true) => ({ ok, json: vi.fn(async () => body) }) as never;
const pageSource = readFileSync(new URL('../../apps/web/app/operator/(protected)/delivery-status/page.tsx', import.meta.url), 'utf8');

describe('VS-R1-033 read-only operator delivery status web surface (12)', () => {
  it('calls the bounded internal status endpoint with GET and no-store', async () => { const request = vi.fn(async () => response(active)); await readOperatorDeliveryStatus(env, request as never); expect(String(request.mock.calls[0]?.[0])).toBe('http://api.internal:3000/internal/delivery/runtime-status'); expect(request.mock.calls[0]?.[1]).toMatchObject({ method: 'GET', cache: 'no-store' }); });
  it('presents the operator token only in the server request header', async () => { const request = vi.fn(async () => response(active)); await readOperatorDeliveryStatus(env, request as never); expect(request.mock.calls[0]?.[1]).toMatchObject({ headers: { 'x-ysim-operator-token': token } }); expect(pageSource).not.toContain('CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN'); });
  it('returns an authorized bounded snapshot', async () => expect(readOperatorDeliveryStatus(env, vi.fn(async () => response(active)) as never)).resolves.toEqual(active));
  it('passes through a bounded access denial', async () => expect(readOperatorDeliveryStatus(env, vi.fn(async () => response({ authorized: false, reason: 'ACCESS_DENIED' })) as never)).resolves.toEqual({ authorized: false, reason: 'ACCESS_DENIED' }));
  it('fails closed when base URL is missing', async () => expect(readOperatorDeliveryStatus({ CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN: token }, vi.fn() as never)).resolves.toEqual({ authorized: false, reason: 'CONFIG_INVALID' }));
  it('fails closed when token is missing or short', async () => expect(readOperatorDeliveryStatus({ YSIM_API_INTERNAL_BASE_URL: 'http://api.internal' }, vi.fn() as never)).resolves.toEqual({ authorized: false, reason: 'CONFIG_INVALID' }));
  it('maps a non-success HTTP response to unavailable', async () => expect(readOperatorDeliveryStatus(env, vi.fn(async () => response({}, false)) as never)).resolves.toEqual({ authorized: false, reason: 'STATUS_UNAVAILABLE' }));
  it('maps transport failures to unavailable without exposing details', async () => expect(readOperatorDeliveryStatus(env, vi.fn(async () => { throw new Error(`secret ${token}`); }) as never)).resolves.toEqual({ authorized: false, reason: 'STATUS_UNAVAILABLE' }));
  it('rejects an unbounded provider response', async () => expect(readOperatorDeliveryStatus(env, vi.fn(async () => response({ authorized: true, status: { secret: token } })) as never)).resolves.toEqual({ authorized: false, reason: 'STATUS_UNAVAILABLE' }));
  it('forces dynamic server rendering', () => expect(pageSource).toMatch(/export const dynamic\s*=\s*['"]force-dynamic['"]/));
  it('contains no runtime control action', () => expect(pageSource).not.toMatch(/(retry|activate|deactivate|enable|disable|sendEmail)\s*\(/));
  it('does not render the operator credential', () => expect(pageSource).not.toContain(token));
});
