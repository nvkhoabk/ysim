import { NextRequest, NextResponse } from 'next/server';

import { OPERATOR_SESSION_COOKIE } from './operator-session';

function isSameOrigin(request: NextRequest): boolean {
  const origin = request.headers.get('origin');
  if (!origin) return false;

  const requestUrl = new URL(request.url);
  const host =
    request.headers.get('x-forwarded-host') ??
    request.headers.get('host') ??
    requestUrl.host;
  const protocol =
    request.headers.get('x-forwarded-proto') ??
    requestUrl.protocol.slice(0, -1);

  try {
    return new URL(origin).origin === `${protocol}://${host}`;
  } catch {
    return false;
  }
}

export function operatorLogoutResponse(request: NextRequest): NextResponse {
  if (!isSameOrigin(request)) {
    return new NextResponse(null, {
      status: 403,
      headers: { 'Cache-Control': 'no-store' },
    });
  }

  const target = new URL('/operator/login', request.url);
  target.searchParams.set('state', 'SIGNED_OUT');
  const response = NextResponse.redirect(target, 303);
  response.headers.set('Cache-Control', 'no-store');
  response.headers.set('Referrer-Policy', 'no-referrer');
  response.cookies.set(OPERATOR_SESSION_COOKIE, '', {
    expires: new Date(0),
    httpOnly: true,
    maxAge: 0,
    path: '/operator',
    sameSite: 'strict',
    secure: true,
  });
  return response;
}
