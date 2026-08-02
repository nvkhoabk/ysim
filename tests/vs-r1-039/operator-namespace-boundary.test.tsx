import { existsSync, readFileSync } from 'node:fs';

import { renderToStaticMarkup } from '../../apps/web/node_modules/react-dom/server.js';
import { beforeEach, describe, expect, it, vi } from 'vitest';

const access = vi.hoisted(() => ({ resolve: vi.fn() }));
const readers = vi.hoisted(() => ({
  readStatus: vi.fn(),
  readOperations: vi.fn(),
}));

vi.mock(
  '../../apps/web/lib/operator-access.js',
  () => ({ resolveOperatorPortalAccess: access.resolve }),
);
vi.mock(
  '../../apps/web/app/operator/delivery-status/operator-delivery-status.js',
  () => ({ readOperatorDeliveryStatus: readers.readStatus }),
);
vi.mock(
  '../../apps/web/app/operator/delivery-status/operator-delivery-operations-summary.js',
  () => ({ readOperatorDeliveryOperationsSummary: readers.readOperations }),
);

import OperatorLayout from '../../apps/web/app/operator/layout.js';
import OperatorDeliveryStatusPage from '../../apps/web/app/operator/delivery-status/page.js';

const pageSource = readFileSync(
  new URL(
    '../../apps/web/app/operator/delivery-status/page.tsx',
    import.meta.url,
  ),
  'utf8',
);
const layoutSource = readFileSync(
  new URL('../../apps/web/app/operator/layout.tsx', import.meta.url),
  'utf8',
);

describe('VS-R1-039 operator namespace boundary', () => {
  beforeEach(() => {
    access.resolve.mockReset();
    readers.readStatus.mockReset().mockResolvedValue({
      authorized: true,
      status: {
        state: 'BLOCKED',
        reason: 'SCHEDULER_DISABLED',
        schedulerEnabled: false,
        emailMode: 'disabled',
      },
    });
    readers.readOperations.mockReset().mockResolvedValue({
      authorized: true,
      available: true,
      summary: {
        generatedAt: '2026-08-02T09:00:00.000Z',
        pending: 0,
        failed: 0,
        published: 0,
        inFlight: 0,
        actionable: 0,
        oldestActionableAt: null,
      },
    });
  });

  it.each([
    'CONFIG_INVALID',
    'SESSION_REQUIRED',
    'SESSION_INVALID',
  ] as const)(
    'blocks %s before either internal reader is invoked',
    async (reason) => {
      access.resolve.mockResolvedValue({ authorized: false, reason });
      const html = renderToStaticMarkup(await OperatorDeliveryStatusPage());
      expect(html).toContain('data-operator-access="denied"');
      expect(html).toContain(reason);
      expect(html).not.toContain('Trạng thái giao eSIM');
      expect(readers.readStatus).not.toHaveBeenCalled();
      expect(readers.readOperations).not.toHaveBeenCalled();
    },
  );

  it('allows an authorized operator to reach both read-only readers', async () => {
    access.resolve.mockResolvedValue({
      authorized: true,
      session: {
        version: 1,
        audience: 'ysim-operator-portal',
        identityId: '10000000-0000-4000-8000-000000000039',
        role: 'OPERATIONS',
        locale: 'vi',
        issuedAt: 1_900_000_000,
        expiresAt: 1_900_003_600,
      },
    });
    const html = renderToStaticMarkup(await OperatorDeliveryStatusPage());
    expect(html).toContain('Trạng thái giao eSIM');
    expect(readers.readStatus).toHaveBeenCalledOnce();
    expect(readers.readOperations).toHaveBeenCalledOnce();
  });

  it('protects the complete operator namespace through its route layout', async () => {
    access.resolve.mockResolvedValue({
      authorized: false,
      reason: 'SESSION_REQUIRED',
    });
    const result = await OperatorLayout({
      children: 'SENSITIVE_OPERATOR_CHILD',
    });
    const html = renderToStaticMarkup(result);
    expect(html).toContain('SESSION_REQUIRED');
    expect(html).not.toContain('SENSITIVE_OPERATOR_CHILD');
    expect(layoutSource).toMatch(/resolveOperatorPortalAccess\(\)/u);
    expect(layoutSource).toMatch(/if \(!access\.authorized\)/u);
  });

  it('checks page access before starting the internal readers', () => {
    const guardIndex = pageSource.indexOf(
      'const access = await resolveOperatorPortalAccess()',
    );
    const readerIndex = pageSource.indexOf(
      'readOperatorDeliveryStatus()',
    );
    expect(guardIndex).toBeGreaterThanOrEqual(0);
    expect(readerIndex).toBeGreaterThan(guardIndex);
  });

  it('adds no public login or session issuance endpoint', () => {
    const webRoot = new URL('../../apps/web/', import.meta.url);
    expect(
      existsSync(new URL('app/operator/login/page.tsx', webRoot)),
    ).toBe(false);
    expect(
      existsSync(new URL('app/api/operator/session/route.ts', webRoot)),
    ).toBe(false);
  });
});
