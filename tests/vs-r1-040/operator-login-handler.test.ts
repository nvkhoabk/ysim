import { NextRequest } from '../../apps/web/node_modules/next/server.js';
import { describe, expect, it, vi } from 'vitest';

import {
  BoundedOperatorLoginLimiter,
  createOperatorLoginHandler,
  safeOperatorNextPath,
} from '../../apps/web/lib/operator-login';
import { verifyOperatorSessionToken } from '../../apps/web/lib/operator-session';
import { operatorConfig } from './fixtures';

const now = 1_900_000_000;

function loginRequest(
  fields: Record<string, string> = {
    loginId: 'operations@example.test',
    password: 'correct horse battery staple',
  },
  origin = 'https://sandbox.ysim.vn',
  reverseProxy: Readonly<{
    forwardedHost: string;
    forwardedProto: string;
    requestUrl: string;
  }> | null = null,
): NextRequest {
  const body = new URLSearchParams(fields).toString();
  return new NextRequest(
    reverseProxy?.requestUrl ??
      'https://sandbox.ysim.vn/api/operator/session',
    {
      method: 'POST',
      headers: {
        'content-length': String(Buffer.byteLength(body)),
        'content-type': 'application/x-www-form-urlencoded',
        host: reverseProxy ? 'localhost:3102' : 'sandbox.ysim.vn',
        origin,
        ...(reverseProxy
          ? {
              'x-forwarded-host': reverseProxy.forwardedHost,
              'x-forwarded-proto': reverseProxy.forwardedProto,
            }
          : {}),
      },
      body,
    },
  );
}

describe('VS-R1-040 operator login handler', () => {
  it('issues a bounded secure cookie and redirects to the protected route', async () => {
    const authenticate = vi.fn(async () => ({
      authenticated: true as const,
      config: operatorConfig,
    }));
    const handler = createOperatorLoginHandler({
      authenticate,
      env: {},
      limiter: new BoundedOperatorLoginLimiter(),
      now: () => now,
    });

    const response = await handler(loginRequest());
    expect(response.status).toBe(303);
    expect(response.headers.get('location')).toBe(
      'https://sandbox.ysim.vn/operator/delivery-status',
    );
    expect(response.headers.get('cache-control')).toBe('no-store');

    const setCookie = response.headers.get('set-cookie') ?? '';
    expect(setCookie).toContain('ysim_operator_session=');
    expect(setCookie).toContain('HttpOnly');
    expect(setCookie).toContain('Secure');
    expect(setCookie).toMatch(/SameSite=Strict/iu);
    expect(setCookie).toContain('Path=/operator');
    expect(setCookie).toContain('Max-Age=3600');

    const token = /ysim_operator_session=([^;]+)/u.exec(setCookie)?.[1];
    expect(
      verifyOperatorSessionToken(token, operatorConfig.sessionSecret, now),
    ).toEqual({
      version: 2,
      audience: 'ysim-operator-portal',
      identityId: operatorConfig.identityId,
      role: operatorConfig.role,
      locale: operatorConfig.locale,
      revocationVersion: operatorConfig.revocationVersion,
      issuedAt: now,
      expiresAt: now + operatorConfig.sessionTtlSeconds,
    });
  });

  it('uses the verified public origin for a successful reverse-proxy redirect', async () => {
    const handler = createOperatorLoginHandler({
      authenticate: vi.fn(async () => ({
        authenticated: true as const,
        config: operatorConfig,
      })),
      env: {},
      limiter: new BoundedOperatorLoginLimiter(),
      now: () => now,
    });

    const response = await handler(
      loginRequest(undefined, 'https://portal.ysim.vn', {
        forwardedHost: 'portal.ysim.vn',
        forwardedProto: 'https',
        requestUrl: 'https://localhost:3102/api/operator/session',
      }),
    );

    expect(response.status).toBe(303);
    expect(response.headers.get('location')).toBe(
      'https://portal.ysim.vn/operator/delivery-status',
    );
  });

  it('returns one generic redirect for invalid credentials without a cookie', async () => {
    const handler = createOperatorLoginHandler({
      authenticate: vi.fn(async () => ({
        authenticated: false as const,
        reason: 'INVALID_CREDENTIALS' as const,
      })),
      limiter: new BoundedOperatorLoginLimiter(),
      now: () => now,
    });
    const response = await handler(loginRequest());
    expect(response.status).toBe(303);
    expect(response.headers.get('location')).toContain(
      'error=INVALID_CREDENTIALS',
    );
    expect(response.headers.get('set-cookie')).toBeNull();
  });

  it('uses the verified public origin for a failed reverse-proxy redirect', async () => {
    const handler = createOperatorLoginHandler({
      authenticate: vi.fn(async () => ({
        authenticated: false as const,
        reason: 'INVALID_CREDENTIALS' as const,
      })),
      limiter: new BoundedOperatorLoginLimiter(),
      now: () => now,
    });

    const response = await handler(
      loginRequest(undefined, 'https://portal.ysim.vn', {
        forwardedHost: 'portal.ysim.vn',
        forwardedProto: 'https',
        requestUrl: 'https://localhost:3102/api/operator/session',
      }),
    );

    expect(response.status).toBe(303);
    expect(response.headers.get('location')).toBe(
      'https://portal.ysim.vn/operator/login?error=INVALID_CREDENTIALS&next=%2Foperator%2Fdelivery-status',
    );
    expect(response.headers.get('set-cookie')).toBeNull();
  });

  it('fails closed without exposing which configuration field is invalid', async () => {
    const handler = createOperatorLoginHandler({
      authenticate: vi.fn(async () => ({
        authenticated: false as const,
        reason: 'CONFIG_INVALID' as const,
      })),
      limiter: new BoundedOperatorLoginLimiter(),
      now: () => now,
    });
    const response = await handler(loginRequest());
    expect(response.headers.get('location')).toContain('error=UNAVAILABLE');
    expect(await response.text()).toBe('');
  });

  it('rejects cross-origin login before credential verification', async () => {
    const authenticate = vi.fn();
    const handler = createOperatorLoginHandler({ authenticate });
    const response = await handler(
      loginRequest(undefined, 'https://attacker.example'),
    );
    expect(response.status).toBe(403);
    expect(authenticate).not.toHaveBeenCalled();
  });

  it('prevents an external or login-loop next target', () => {
    expect(safeOperatorNextPath('//attacker.example')).toBe(
      '/operator/delivery-status',
    );
    expect(safeOperatorNextPath('/operator/login?next=%2F%2Fevil')).toBe(
      '/operator/delivery-status',
    );
    expect(safeOperatorNextPath('/operator/delivery-status')).toBe(
      '/operator/delivery-status',
    );
  });

  it('rejects an oversized body even when its header understates the size', async () => {
    const authenticate = vi.fn();
    const handler = createOperatorLoginHandler({ authenticate });
    const body = new URLSearchParams({
      loginId: 'operations@example.test',
      password: 'x'.repeat(5_000),
    }).toString();
    const response = await handler(
      new NextRequest('https://sandbox.ysim.vn/api/operator/session', {
        method: 'POST',
        headers: {
          'content-length': '1',
          'content-type': 'application/x-www-form-urlencoded',
          host: 'sandbox.ysim.vn',
          origin: 'https://sandbox.ysim.vn',
        },
        body,
      }),
    );
    expect(response.status).toBe(413);
    expect(authenticate).not.toHaveBeenCalled();
  });

  it('rate-limits the single bootstrap credential after five failures', async () => {
    const limiter = new BoundedOperatorLoginLimiter();
    const handler = createOperatorLoginHandler({
      authenticate: vi.fn(async () => ({
        authenticated: false as const,
        reason: 'INVALID_CREDENTIALS' as const,
      })),
      limiter,
      now: () => now,
    });

    for (let attempt = 0; attempt < 5; attempt += 1) {
      const response = await handler(loginRequest());
      expect(response.headers.get('location')).toContain(
        'error=INVALID_CREDENTIALS',
      );
    }

    const blocked = await handler(loginRequest());
    expect(blocked.headers.get('location')).toContain('error=RETRY_LATER');
    expect(blocked.headers.get('retry-after')).toBe('900');
  });

  it('starts a fresh failure window after the bounded interval', () => {
    const limiter = new BoundedOperatorLoginLimiter();
    for (let attempt = 0; attempt < 4; attempt += 1) {
      limiter.recordFailure(now);
    }
    limiter.recordFailure(now + 901);
    expect(limiter.isBlocked(now + 901)).toBe(false);
  });
});
