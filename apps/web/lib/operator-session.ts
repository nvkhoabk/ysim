import { createHmac, timingSafeEqual } from 'node:crypto';

export const OPERATOR_SESSION_COOKIE = 'ysim_operator_session';
export const OPERATOR_SESSION_AUDIENCE = 'ysim-operator-portal';
export const OPERATOR_SESSION_VERSION = 1;
export const OPERATOR_SESSION_MAX_TTL_SECONDS = 8 * 60 * 60;

const SIGNATURE_CONTEXT = 'ysim:operator-session:v1\0';
const CLOCK_SKEW_SECONDS = 60;

export type OperatorPortalLocale = 'vi' | 'en';
export type OperatorPortalRole = 'PLATFORM_ADMIN' | 'OPERATIONS';

export interface OperatorSessionPayload {
  version: typeof OPERATOR_SESSION_VERSION;
  audience: typeof OPERATOR_SESSION_AUDIENCE;
  identityId: string;
  role: OperatorPortalRole;
  locale: OperatorPortalLocale;
  issuedAt: number;
  expiresAt: number;
}

const uuidPattern =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;

function requireSecret(secret: string): void {
  if (secret.length < 32) {
    throw new Error(
      'YSIM_PORTAL_SESSION_SECRET must contain at least 32 characters',
    );
  }
}

function isPayload(value: unknown): value is OperatorSessionPayload {
  if (typeof value !== 'object' || value === null) return false;

  const candidate = value as Partial<OperatorSessionPayload>;
  return (
    candidate.version === OPERATOR_SESSION_VERSION &&
    candidate.audience === OPERATOR_SESSION_AUDIENCE &&
    typeof candidate.identityId === 'string' &&
    uuidPattern.test(candidate.identityId) &&
    (candidate.role === 'PLATFORM_ADMIN' || candidate.role === 'OPERATIONS') &&
    (candidate.locale === 'vi' || candidate.locale === 'en') &&
    typeof candidate.issuedAt === 'number' &&
    Number.isSafeInteger(candidate.issuedAt) &&
    typeof candidate.expiresAt === 'number' &&
    Number.isSafeInteger(candidate.expiresAt) &&
    candidate.issuedAt < candidate.expiresAt &&
    candidate.expiresAt - candidate.issuedAt <=
      OPERATOR_SESSION_MAX_TTL_SECONDS
  );
}

function signatureFor(encodedPayload: string, secret: string): Buffer {
  return createHmac('sha256', secret)
    .update(SIGNATURE_CONTEXT)
    .update(encodedPayload)
    .digest();
}

export function createOperatorSessionToken(
  payload: OperatorSessionPayload,
  secret: string,
): string {
  requireSecret(secret);

  if (!isPayload(payload)) {
    throw new Error('Operator session payload is invalid');
  }

  const encodedPayload = Buffer.from(
    JSON.stringify(payload),
    'utf8',
  ).toString('base64url');

  return `${encodedPayload}.${signatureFor(encodedPayload, secret).toString('base64url')}`;
}

export function verifyOperatorSessionToken(
  token: string | undefined,
  secret: string,
  nowSeconds = Math.floor(Date.now() / 1000),
): OperatorSessionPayload | null {
  requireSecret(secret);
  if (!token) return null;

  const [encodedPayload, encodedSignature, extra] = token.split('.');
  if (!encodedPayload || !encodedSignature || extra !== undefined) {
    return null;
  }

  let suppliedSignature: Buffer;
  let payload: unknown;

  try {
    suppliedSignature = Buffer.from(encodedSignature, 'base64url');
    payload = JSON.parse(
      Buffer.from(encodedPayload, 'base64url').toString('utf8'),
    );
  } catch {
    return null;
  }

  const expectedSignature = signatureFor(encodedPayload, secret);
  if (
    suppliedSignature.length !== expectedSignature.length ||
    !timingSafeEqual(suppliedSignature, expectedSignature)
  ) {
    return null;
  }

  if (
    !isPayload(payload) ||
    payload.issuedAt > nowSeconds + CLOCK_SKEW_SECONDS ||
    payload.expiresAt <= nowSeconds
  ) {
    return null;
  }

  return {
    ...payload,
    identityId: payload.identityId.toLowerCase(),
  };
}
