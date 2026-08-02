import { NextRequest } from '../../apps/web/node_modules/next/server.js';
import { describe, expect, it } from 'vitest';

import { operatorLogoutResponse } from '../../apps/web/lib/operator-logout';

function request(origin: string): NextRequest {
  return new NextRequest('https://sandbox.ysim.vn/operator/logout', {
    method: 'POST',
    headers: { host: 'sandbox.ysim.vn', origin },
  });
}

function reverseProxyRequest(origin: string): NextRequest {
  return new NextRequest('https://localhost:3102/operator/logout', {
    method: 'POST',
    headers: {
      host: 'localhost:3102',
      origin,
      'x-forwarded-host': 'portal.ysim.vn',
      'x-forwarded-proto': 'https',
    },
  });
}

describe('VS-R1-040 operator logout', () => {
  it('expires the exact secure operator cookie and redirects to login', () => {
    const response = operatorLogoutResponse(
      request('https://sandbox.ysim.vn'),
    );
    expect(response.status).toBe(303);
    expect(response.headers.get('location')).toBe(
      'https://sandbox.ysim.vn/operator/login?state=SIGNED_OUT',
    );
    const setCookie = response.headers.get('set-cookie') ?? '';
    expect(setCookie).toContain('ysim_operator_session=');
    expect(setCookie).toContain('Max-Age=0');
    expect(setCookie).toContain('Path=/operator');
    expect(setCookie).toContain('HttpOnly');
    expect(setCookie).toContain('Secure');
    expect(setCookie).toMatch(/SameSite=Strict/iu);
  });

  it('uses the verified public origin behind the reverse proxy', () => {
    const response = operatorLogoutResponse(
      reverseProxyRequest('https://portal.ysim.vn'),
    );

    expect(response.status).toBe(303);
    expect(response.headers.get('location')).toBe(
      'https://portal.ysim.vn/operator/login?state=SIGNED_OUT',
    );
    expect(response.headers.get('location')).not.toContain('localhost:3102');
  });

  it('rejects cross-origin logout without touching the cookie', () => {
    const response = operatorLogoutResponse(request('https://attacker.example'));
    expect(response.status).toBe(403);
    expect(response.headers.get('set-cookie')).toBeNull();
  });
});
