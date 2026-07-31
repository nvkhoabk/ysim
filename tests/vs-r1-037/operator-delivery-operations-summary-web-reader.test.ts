import { readFileSync } from 'node:fs';
import { describe, expect, it, vi } from 'vitest';
import { readOperatorDeliveryOperationsSummary } from '../../apps/web/app/operator/delivery-status/operator-delivery-operations-summary.js';

const token = 'operator-token-that-is-at-least-32-characters';
const env = {
  YSIM_API_INTERNAL_BASE_URL: 'http://api.internal:3000',
  CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN: token,
};
const available = {
  authorized: true,
  available: true,
  summary: {
    generatedAt: '2026-08-01T03:00:00.000Z',
    pending: 7,
    failed: 2,
    published: 31,
    inFlight: 1,
    actionable: 5,
    oldestActionableAt: '2026-08-01T02:45:00.000Z',
  },
} as const;
const response = (body: unknown, ok = true) =>
  ({ ok, json: vi.fn(async () => body) }) as never;
const source = readFileSync(
  new URL(
    '../../apps/web/app/operator/delivery-status/operator-delivery-operations-summary.ts',
    import.meta.url,
  ),
  'utf8',
);

describe('VS-R1-037 server-side operator operations summary web reader (12)', () => {
  it('calls the bounded internal summary endpoint with GET and no-store', async () => {
    const request = vi.fn(async () => response(available));
    await readOperatorDeliveryOperationsSummary(env, request as never);
    expect(String(request.mock.calls[0]?.[0])).toBe(
      'http://api.internal:3000/internal/delivery/operations-summary',
    );
    expect(request.mock.calls[0]?.[1]).toMatchObject({ method: 'GET', cache: 'no-store' });
  });

  it('presents the operator token only through the bounded server header', async () => {
    const request = vi.fn(async () => response(available));
    const result = await readOperatorDeliveryOperationsSummary(env, request as never);
    expect(request.mock.calls[0]?.[1]).toMatchObject({
      headers: { 'x-ysim-operator-token': token },
    });
    expect(JSON.stringify(result)).not.toContain(token);
  });

  it('returns an authorized bounded summary', async () => {
    await expect(
      readOperatorDeliveryOperationsSummary(
        env,
        vi.fn(async () => response(available)) as never,
      ),
    ).resolves.toEqual(available);
  });

  it('passes through a bounded access denial', async () => {
    await expect(
      readOperatorDeliveryOperationsSummary(
        env,
        vi.fn(async () => response({ authorized: false, reason: 'ACCESS_DENIED' })) as never,
      ),
    ).resolves.toEqual({ authorized: false, reason: 'ACCESS_DENIED' });
  });

  it('passes through a bounded unavailable summary', async () => {
    await expect(
      readOperatorDeliveryOperationsSummary(
        env,
        vi.fn(async () =>
          response({ authorized: true, available: false, reason: 'SUMMARY_UNAVAILABLE' }),
        ) as never,
      ),
    ).resolves.toEqual({ authorized: true, available: false, reason: 'SUMMARY_UNAVAILABLE' });
  });

  it('fails closed when the base URL is missing', async () => {
    await expect(
      readOperatorDeliveryOperationsSummary(
        { CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN: token },
        vi.fn() as never,
      ),
    ).resolves.toEqual({ authorized: false, reason: 'CONFIG_INVALID' });
  });

  it('fails closed when the credential is missing or short', async () => {
    await expect(
      readOperatorDeliveryOperationsSummary(
        { YSIM_API_INTERNAL_BASE_URL: 'http://api.internal' },
        vi.fn() as never,
      ),
    ).resolves.toEqual({ authorized: false, reason: 'CONFIG_INVALID' });
  });

  it('fails closed for an invalid internal base URL', async () => {
    await expect(
      readOperatorDeliveryOperationsSummary(
        { ...env, YSIM_API_INTERNAL_BASE_URL: 'not a url' },
        vi.fn() as never,
      ),
    ).resolves.toEqual({ authorized: false, reason: 'CONFIG_INVALID' });
  });

  it('maps a non-success HTTP response to unavailable', async () => {
    await expect(
      readOperatorDeliveryOperationsSummary(
        env,
        vi.fn(async () => response({}, false)) as never,
      ),
    ).resolves.toEqual({ authorized: false, reason: 'STATUS_UNAVAILABLE' });
  });

  it('maps transport failures to unavailable without exposing details', async () => {
    await expect(
      readOperatorDeliveryOperationsSummary(
        env,
        vi.fn(async () => {
          throw new Error(`internal secret ${token}`);
        }) as never,
      ),
    ).resolves.toEqual({ authorized: false, reason: 'STATUS_UNAVAILABLE' });
  });

  it('rejects malformed or contradictory summary data', async () => {
    const malformed = {
      ...available,
      summary: { ...available.summary, pending: 1, failed: 0, inFlight: 1, actionable: 1 },
    };
    await expect(
      readOperatorDeliveryOperationsSummary(
        env,
        vi.fn(async () => response(malformed)) as never,
      ),
    ).resolves.toEqual({ authorized: false, reason: 'STATUS_UNAVAILABLE' });
  });

  it('reconstructs a non-PII result and contains no runtime control operation', async () => {
    const result = await readOperatorDeliveryOperationsSummary(
      env,
      vi.fn(async () =>
        response({
          ...available,
          recipientEmail: 'hidden@example.invalid',
          token,
          retry: true,
        }),
      ) as never,
    );
    expect(result).toEqual(available);
    expect(JSON.stringify(result)).not.toMatch(/recipient|token|retry|hidden/i);
    expect(source).not.toMatch(/\b(POST|PUT|PATCH|DELETE|retry|sendEmail|activate|deactivate)\b/i);
  });
});
