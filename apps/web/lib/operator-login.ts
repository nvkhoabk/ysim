import { NextRequest, NextResponse } from 'next/server';

import { authenticateOperatorCredentials } from './operator-credential';
import {
  OPERATOR_SESSION_AUDIENCE,
  OPERATOR_SESSION_COOKIE,
  OPERATOR_SESSION_VERSION,
  createOperatorSessionToken,
} from './operator-session';

const LOGIN_PATH = '/operator/login';
const DEFAULT_NEXT_PATH = '/operator/delivery-status';
const MAX_FORM_BYTES = 4_096;
const MAX_FAILED_ATTEMPTS = 5;
const LOCKOUT_SECONDS = 15 * 60;

type AuthenticationFunction = typeof authenticateOperatorCredentials;

export interface LoginAttemptLimiter {
  clear(): void;
  isBlocked(nowSeconds: number): boolean;
  recordFailure(nowSeconds: number): void;
  retryAfter(nowSeconds: number): number;
}

export class BoundedOperatorLoginLimiter implements LoginAttemptLimiter {
  private blockedUntil = 0;
  private failedAttempts = 0;
  private windowStartedAt = 0;

  clear(): void {
    this.blockedUntil = 0;
    this.failedAttempts = 0;
    this.windowStartedAt = 0;
  }

  isBlocked(nowSeconds: number): boolean {
    if (this.blockedUntil <= nowSeconds) {
      if (this.blockedUntil > 0) this.clear();
      return false;
    }
    return true;
  }

  recordFailure(nowSeconds: number): void {
    if (
      this.windowStartedAt === 0 ||
      nowSeconds - this.windowStartedAt >= LOCKOUT_SECONDS
    ) {
      this.failedAttempts = 0;
      this.windowStartedAt = nowSeconds;
    }
    this.failedAttempts += 1;
    if (this.failedAttempts >= MAX_FAILED_ATTEMPTS) {
      this.blockedUntil = nowSeconds + LOCKOUT_SECONDS;
    }
  }

  retryAfter(nowSeconds: number): number {
    return Math.max(1, this.blockedUntil - nowSeconds);
  }
}

const processLimiter = new BoundedOperatorLoginLimiter();

function verifiedRequestOrigin(request: NextRequest): string | null {
  const origin = request.headers.get('origin');
  const forwardedHost = request.headers.get('x-forwarded-host');
  const forwardedProto = request.headers.get('x-forwarded-proto');
  const requestUrl = new URL(request.url);
  const host = forwardedHost ?? request.headers.get('host') ?? requestUrl.host;
  const protocol = forwardedProto ?? requestUrl.protocol.slice(0, -1);

  if (!origin || !host || (protocol !== 'http' && protocol !== 'https')) {
    return null;
  }

  try {
    const parsedOrigin = new URL(origin);
    const expected = `${protocol}://${host}`;
    return parsedOrigin.origin === expected ? parsedOrigin.origin : null;
  } catch {
    return null;
  }
}

export function safeOperatorNextPath(value: string | null): string {
  if (!value) return DEFAULT_NEXT_PATH;
  if (
    !value.startsWith('/operator/') ||
    value.startsWith('//') ||
    value.startsWith(LOGIN_PATH) ||
    value.includes('\\') ||
    value.includes('\0')
  ) {
    return DEFAULT_NEXT_PATH;
  }
  return value;
}

function loginRedirect(
  verifiedOrigin: string,
  error: 'INVALID_CREDENTIALS' | 'RETRY_LATER' | 'UNAVAILABLE',
  nextPath: string,
): NextResponse {
  const target = new URL(LOGIN_PATH, verifiedOrigin);
  target.searchParams.set('error', error);
  target.searchParams.set('next', nextPath);
  const response = NextResponse.redirect(target, 303);
  response.headers.set('Cache-Control', 'no-store');
  response.headers.set('Referrer-Policy', 'no-referrer');
  return response;
}

export function createOperatorLoginHandler(
  options: Readonly<{
    authenticate?: AuthenticationFunction;
    env?: NodeJS.ProcessEnv;
    limiter?: LoginAttemptLimiter;
    now?: () => number;
  }> = {},
) {
  const authenticate = options.authenticate ?? authenticateOperatorCredentials;
  const env = options.env ?? process.env;
  const limiter = options.limiter ?? processLimiter;
  const now = options.now ?? (() => Math.floor(Date.now() / 1_000));

  return async function POST(request: NextRequest): Promise<NextResponse> {
    const verifiedOrigin = verifiedRequestOrigin(request);
    if (!verifiedOrigin) {
      return new NextResponse(null, {
        status: 403,
        headers: { 'Cache-Control': 'no-store' },
      });
    }

    const contentType = request.headers.get('content-type') ?? '';
    if (!contentType.startsWith('application/x-www-form-urlencoded')) {
      return new NextResponse(null, {
        status: 415,
        headers: { 'Cache-Control': 'no-store' },
      });
    }

    const contentLength = Number(request.headers.get('content-length') ?? '0');
    if (!Number.isFinite(contentLength) || contentLength > MAX_FORM_BYTES) {
      return new NextResponse(null, {
        status: 413,
        headers: { 'Cache-Control': 'no-store' },
      });
    }

    const encodedForm = await request.text();
    if (Buffer.byteLength(encodedForm, 'utf8') > MAX_FORM_BYTES) {
      return new NextResponse(null, {
        status: 413,
        headers: { 'Cache-Control': 'no-store' },
      });
    }

    const form = new URLSearchParams(encodedForm);
    const loginId = form.get('loginId');
    const password = form.get('password');
    const nextPath = safeOperatorNextPath(form.get('next'));
    const nowSeconds = now();

    if (limiter.isBlocked(nowSeconds)) {
      const response = loginRedirect(
        verifiedOrigin,
        'RETRY_LATER',
        nextPath,
      );
      response.headers.set(
        'Retry-After',
        String(limiter.retryAfter(nowSeconds)),
      );
      return response;
    }

    if (typeof loginId !== 'string' || typeof password !== 'string') {
      limiter.recordFailure(nowSeconds);
      return loginRedirect(verifiedOrigin, 'INVALID_CREDENTIALS', nextPath);
    }

    const result = await authenticate(loginId, password, env);
    if (!result.authenticated) {
      if (result.reason === 'CONFIG_INVALID') {
        return loginRedirect(verifiedOrigin, 'UNAVAILABLE', nextPath);
      }
      limiter.recordFailure(nowSeconds);
      return loginRedirect(verifiedOrigin, 'INVALID_CREDENTIALS', nextPath);
    }

    limiter.clear();
    const { config } = result;
    const token = createOperatorSessionToken(
      {
        version: OPERATOR_SESSION_VERSION,
        audience: OPERATOR_SESSION_AUDIENCE,
        identityId: config.identityId,
        role: config.role,
        locale: config.locale,
        revocationVersion: config.revocationVersion,
        issuedAt: nowSeconds,
        expiresAt: nowSeconds + config.sessionTtlSeconds,
      },
      config.sessionSecret,
    );

    const response = NextResponse.redirect(new URL(nextPath, verifiedOrigin), 303);
    response.headers.set('Cache-Control', 'no-store');
    response.headers.set('Referrer-Policy', 'no-referrer');
    response.cookies.set(OPERATOR_SESSION_COOKIE, token, {
      httpOnly: true,
      maxAge: config.sessionTtlSeconds,
      path: '/operator',
      sameSite: 'strict',
      secure: true,
    });
    return response;
  };
}
