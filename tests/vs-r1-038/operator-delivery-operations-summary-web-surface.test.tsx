import { readFileSync } from 'node:fs';
import { renderToStaticMarkup } from '../../apps/web/node_modules/react-dom/server.js';
import { beforeEach, describe, expect, it, vi } from 'vitest';

const readers = vi.hoisted(() => ({
  readStatus: vi.fn(),
  readOperations: vi.fn(),
}));

vi.mock(
  '../../apps/web/app/operator/delivery-status/operator-delivery-status.js',
  () => ({ readOperatorDeliveryStatus: readers.readStatus }),
);
vi.mock(
  '../../apps/web/app/operator/delivery-status/operator-delivery-operations-summary.js',
  () => ({ readOperatorDeliveryOperationsSummary: readers.readOperations }),
);

import OperatorDeliveryStatusPage from '../../apps/web/app/operator/delivery-status/page.js';

const runtime = {
  authorized: true,
  status: {
    state: 'INACTIVE',
    reason: 'SAFE_REVIEW_MODE',
    schedulerEnabled: false,
    emailMode: 'disabled',
  },
} as const;
const operations = {
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
const pageSource = readFileSync(
  new URL('../../apps/web/app/operator/delivery-status/page.tsx', import.meta.url),
  'utf8',
);
const cssSource = readFileSync(
  new URL('../../apps/web/app/operator/delivery-status/status.module.css', import.meta.url),
  'utf8',
);

const renderPage = async () => renderToStaticMarkup(await OperatorDeliveryStatusPage());

describe('VS-R1-038 read-only operations summary web surface (12)', () => {
  beforeEach(() => {
    readers.readStatus.mockReset().mockResolvedValue(runtime);
    readers.readOperations.mockReset().mockResolvedValue(operations);
  });

  it('reads runtime status and operations summary exactly once', async () => {
    await renderPage();
    expect(readers.readStatus).toHaveBeenCalledTimes(1);
    expect(readers.readOperations).toHaveBeenCalledTimes(1);
  });

  it('starts both independent read-only readers before awaiting results', () => {
    expect(pageSource).toMatch(/Promise\.all\(\s*\[\s*readOperatorDeliveryStatus\(\),\s*readOperatorDeliveryOperationsSummary\(\)/s);
  });

  it('renders the bounded runtime snapshot', async () => {
    const html = await renderPage();
    expect(html).toContain('Trạng thái hệ thống');
    expect(html).toContain('INACTIVE');
    expect(html).toContain('SAFE_REVIEW_MODE');
    expect(html).toContain('Đã tắt');
    expect(html).toContain('disabled');
  });

  it('renders all five bounded operations metrics', async () => {
    const html = await renderPage();
    for (const label of ['Đang chờ', 'Thất bại', 'Đã gửi', 'Đang xử lý', 'Có thể xử lý']) {
      expect(html).toContain(label);
    }
    for (const value of ['>7<', '>2<', '>31<', '>1<', '>5<']) expect(html).toContain(value);
  });

  it('renders machine-readable freshness timestamps', async () => {
    const html = await renderPage();
    expect(html).toContain('dateTime="2026-08-01T03:00:00.000Z"');
    expect(html).toContain('dateTime="2026-08-01T02:45:00.000Z"');
  });

  it('keeps the summary visible when runtime access is denied', async () => {
    readers.readStatus.mockResolvedValue({ authorized: false, reason: 'ACCESS_DENIED' });
    const html = await renderPage();
    expect(html).toContain('Không thể đọc trạng thái runtime');
    expect(html).toContain('Tổng hợp vận hành');
    expect(html).toContain('>31<');
  });

  it('keeps runtime status visible when summary access is denied', async () => {
    readers.readOperations.mockResolvedValue({ authorized: false, reason: 'ACCESS_DENIED' });
    const html = await renderPage();
    expect(html).toContain('SAFE_REVIEW_MODE');
    expect(html).toContain('Không thể đọc tổng hợp vận hành');
    expect(html).toContain('ACCESS_DENIED');
  });

  it('shows a bounded unavailable reason without fabricating metrics', async () => {
    readers.readOperations.mockResolvedValue({ authorized: true, available: false, reason: 'SUMMARY_UNAVAILABLE' });
    const html = await renderPage();
    expect(html).toContain('SUMMARY_UNAVAILABLE');
    expect(html).not.toContain('>31<');
  });

  it('renders the empty actionable timestamp as a bounded state', async () => {
    readers.readOperations.mockResolvedValue({
      ...operations,
      summary: { ...operations.summary, oldestActionableAt: null },
    });
    expect(await renderPage()).toContain('Không có');
  });

  it('contains no control, form or mutation surface', async () => {
    const html = await renderPage();
    expect(html).not.toMatch(/<(button|form|input|select|textarea)\b/i);
    expect(pageSource).not.toMatch(/\b(POST|PUT|PATCH|DELETE|retry|sendEmail|activate|deactivate)\b/i);
  });

  it('does not render credentials, PII or internal payload fields', async () => {
    const html = await renderPage();
    expect(html).not.toMatch(/CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN|operator-token|recipient|email@example/i);
  });

  it('keeps dynamic server rendering and responsive desktop/mobile grids', () => {
    expect(pageSource).toMatch(/export const dynamic\s*=\s*['"]force-dynamic['"]/);
    expect(cssSource).toMatch(/grid-template-columns:\s*repeat\(5,/);
    expect(cssSource).toMatch(/@media \(max-width: 36rem\)/);
    expect(cssSource).toMatch(/\.grid, \.metrics \{ grid-template-columns: 1fr; \}/);
  });
});
