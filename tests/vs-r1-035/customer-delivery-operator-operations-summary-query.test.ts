import { readFileSync } from 'node:fs';
import { describe, expect, it, vi } from 'vitest';
import { CustomerDeliveryOperatorOperationsSummaryQueryService } from '../../apps/api/src/modules/delivery/application/customer-delivery-operator-operations-summary-query.service.js';

const token = 'operator-token-that-is-at-least-32-characters';
const env = { CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN: token };
const now = new Date('2026-08-01T03:00:00.000Z');
const summaryResult = {
  available: true as const,
  summary: {
    generatedAt: now.toISOString(),
    pending: 7,
    failed: 2,
    published: 31,
    inFlight: 1,
    actionable: 5,
    oldestActionableAt: '2026-08-01T02:45:00.000Z',
  },
};

const make = (
  accessResult: unknown = {
    authorized: true,
    status: {
      state: 'INACTIVE',
      reason: 'SAFE_REVIEW_MODE',
      schedulerEnabled: false,
      emailMode: 'disabled',
    },
  },
  result: unknown = summaryResult,
) => {
  const operatorStatus = { query: vi.fn(() => accessResult) };
  const operationsSummary = { snapshot: vi.fn(async () => result) };
  return {
    service: new CustomerDeliveryOperatorOperationsSummaryQueryService(
      operatorStatus as never,
      operationsSummary as never,
    ),
    operatorStatus,
    operationsSummary,
  };
};

const serviceSource = readFileSync(
  new URL('../../apps/api/src/modules/delivery/application/customer-delivery-operator-operations-summary-query.service.ts', import.meta.url),
  'utf8',
);
const moduleSource = readFileSync(
  new URL('../../apps/api/src/modules/delivery/delivery.module.ts', import.meta.url),
  'utf8',
);

describe('VS-R1-035 guarded operator delivery operations summary query (12)', () => {
  it('returns the bounded summary after authorization', async () => {
    await expect(make().service.query(token, env, now)).resolves.toEqual({
      authorized: true,
      ...summaryResult,
    });
  });

  it('passes the exact credential and environment to the existing guard', async () => {
    const x = make();
    await x.service.query(token, env, now);
    expect(x.operatorStatus.query).toHaveBeenCalledOnce();
    expect(x.operatorStatus.query).toHaveBeenCalledWith(token, env);
  });

  it('passes the exact observation time to the summary service', async () => {
    const x = make();
    await x.service.query(token, env, now);
    expect(x.operationsSummary.snapshot).toHaveBeenCalledOnce();
    expect(x.operationsSummary.snapshot).toHaveBeenCalledWith(now);
  });

  it('does not read the summary after access denial', async () => {
    const denied = { authorized: false, reason: 'ACCESS_DENIED' } as const;
    const x = make(denied);
    await expect(x.service.query('wrong', env, now)).resolves.toEqual(denied);
    expect(x.operationsSummary.snapshot).not.toHaveBeenCalled();
  });

  it('does not read the summary after invalid guard configuration', async () => {
    const denied = { authorized: false, reason: 'CONFIG_INVALID' } as const;
    const x = make(denied);
    await expect(x.service.query(token, {}, now)).resolves.toEqual(denied);
    expect(x.operationsSummary.snapshot).not.toHaveBeenCalled();
  });

  it('does not read the summary when guarded runtime status is unavailable', async () => {
    const denied = { authorized: false, reason: 'STATUS_UNAVAILABLE' } as const;
    const x = make(denied);
    await expect(x.service.query(token, env, now)).resolves.toEqual(denied);
    expect(x.operationsSummary.snapshot).not.toHaveBeenCalled();
  });

  it('preserves the bounded fail-closed summary result', async () => {
    const unavailable = { available: false, reason: 'SUMMARY_UNAVAILABLE' } as const;
    await expect(make(undefined, unavailable).service.query(token, env, now)).resolves.toEqual({
      authorized: true,
      ...unavailable,
    });
  });

  it('does not expose the runtime status used by the authorization guard', async () => {
    expect(JSON.stringify(await make().service.query(token, env, now))).not.toMatch(/SAFE_REVIEW_MODE|schedulerEnabled|emailMode|status/);
  });

  it('does not expose the presented credential', async () => {
    expect(JSON.stringify(await make().service.query(token, env, now))).not.toContain(token);
  });

  it('returns only bounded top-level fields', async () => {
    expect(Object.keys(await make().service.query(token, env, now)).sort()).toEqual([
      'authorized',
      'available',
      'summary',
    ]);
  });

  it('contains no runtime-control or write operation', () => {
    expect(serviceSource).not.toMatch(/\b(start|stop|activate|deactivate|retry|send|publish|INSERT|UPDATE|DELETE|PATCH|POST|PUT)\b/i);
  });

  it('registers and exports the guarded query without adding a controller', () => {
    expect(moduleSource).toContain('CustomerDeliveryOperatorOperationsSummaryQueryService');
    expect(moduleSource.match(/controllers:\s*\[CustomerDeliveryOperatorStatusController\]/g)).toHaveLength(1);
  });
});
