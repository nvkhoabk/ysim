import { readFileSync } from 'node:fs';

import { renderToStaticMarkup } from '../../apps/web/node_modules/react-dom/server.js';
import { beforeEach, describe, expect, it, vi } from 'vitest';

const access = vi.hoisted(() => ({ resolve: vi.fn() }));

vi.mock(
  '../../apps/web/lib/operator-access.js',
  () => ({ resolveOperatorPortalAccess: access.resolve }),
);

import ProtectedOperatorLayout from '../../apps/web/app/operator/(protected)/layout.js';
import OperatorLoginPage from '../../apps/web/app/operator/login/page.js';

const loginSource = readFileSync(
  new URL('../../apps/web/app/operator/login/page.tsx', import.meta.url),
  'utf8',
);
const sessionRouteSource = readFileSync(
  new URL(
    '../../apps/web/app/api/operator/session/route.ts',
    import.meta.url,
  ),
  'utf8',
);

describe('VS-R1-040 operator login browser surface', () => {
  beforeEach(() => {
    access.resolve.mockReset().mockResolvedValue({
      authorized: false,
      reason: 'SESSION_REQUIRED',
    });
  });

  it('renders a bounded password form without registration or recovery', async () => {
    const html = renderToStaticMarkup(
      await OperatorLoginPage({ searchParams: Promise.resolve({}) }),
    );
    expect(html).toContain('data-operator-login="ready"');
    expect(html).toContain('action="/api/operator/session"');
    expect(html).toContain('name="loginId"');
    expect(html).toContain('name="password"');
    expect(html).toContain('type="password"');
    expect(html).toContain('Không có chức năng đăng ký công khai');
    expect(html).not.toMatch(/name="(role|identityId|revocationVersion)"/u);
  });

  it('renders only allowlisted status messages from query parameters', async () => {
    const known = renderToStaticMarkup(
      await OperatorLoginPage({
        searchParams: Promise.resolve({ error: 'INVALID_CREDENTIALS' }),
      }),
    );
    expect(known).toContain('Thông tin đăng nhập không hợp lệ.');

    const unknown = renderToStaticMarkup(
      await OperatorLoginPage({
        searchParams: Promise.resolve({ error: 'LEAK_INTERNAL_DETAIL' }),
      }),
    );
    expect(unknown).not.toContain('LEAK_INTERNAL_DETAIL');
  });

  it('shows the authenticated role and logout control only after access succeeds', async () => {
    access.resolve.mockResolvedValue({
      authorized: true,
      session: {
        version: 2,
        audience: 'ysim-operator-portal',
        identityId: '10000000-0000-4000-8000-000000000040',
        role: 'OPERATIONS',
        locale: 'vi',
        revocationVersion: 7,
        issuedAt: 1_900_000_000,
        expiresAt: 1_900_003_600,
      },
    });
    const html = renderToStaticMarkup(
      await ProtectedOperatorLayout({ children: 'PROTECTED_CONTENT' }),
    );
    expect(html).toContain('data-operator-authenticated="true"');
    expect(html).toContain('OPERATIONS');
    expect(html).toContain('action="/operator/logout"');
    expect(html).toContain('PROTECTED_CONTENT');
  });

  it('does not expose protected children for a revoked session', async () => {
    access.resolve.mockResolvedValue({
      authorized: false,
      reason: 'SESSION_REVOKED',
    });
    const html = renderToStaticMarkup(
      await ProtectedOperatorLayout({ children: 'PROTECTED_CONTENT' }),
    );
    expect(html).toContain('SESSION_REVOKED');
    expect(html).not.toContain('PROTECTED_CONTENT');
  });

  it('keeps login issuance independent of API, provider and email execution', () => {
    const boundedSource = `${loginSource}\n${sessionRouteSource}`;
    expect(boundedSource).not.toMatch(
      /GPay|Gigago|scheduler|sendEmail|CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN/u,
    );
  });
});
