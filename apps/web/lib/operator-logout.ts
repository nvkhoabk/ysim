import { NextRequest, NextResponse } from 'next/server';

import { OPERATOR_SESSION_COOKIE } from './operator-session';

function verifiedRequestOrigin(request: NextRequest): string | null {
  const origin = request.headers.get('origin');
  if (!origin) return null;

  const requestUrl = new URL(request.url);
  const host =
    request.headers.get('x-forwarded-host') ??
    request.headers.get('host') ??
    requestUrl.host;
  const protocol =
    request.headers.get('x-forwarded-proto') ??
    requestUrl.protocol.slice(0, -1);

  try {
    const parsedOrigin = new URL(origin);
    return parsedOrigin.origin === `${protocol}://${host}`
      ? parsedOrigin.origin
      : null;
  } catch {
    return null;
  }
}

export function operatorLogoutResponse(request: NextRequest): NextResponse {
  const verifiedOrigin = verifiedRequestOrigin(request);
  if (!verifiedOrigin) {
    return new NextResponse(null, {
      status: 403,
      headers: { 'Cache-Control': 'no-store' },
    });
  }

  const target = new URL('/operator/login', verifiedOrigin);
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
