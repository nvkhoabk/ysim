import { createHmac, timingSafeEqual } from 'node:crypto';

export const AGENCY_SESSION_COOKIE = 'ysim_agency_session';

export type AgencyPortalLocale = 'vi' | 'en';

export interface AgencySessionPayload {
  identityId: string;
  organizationId: string;
  locale: AgencyPortalLocale;
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

function isPayload(value: unknown): value is AgencySessionPayload {
  if (typeof value !== 'object' || value === null) return false;

  const candidate = value as Partial<AgencySessionPayload>;
  return (
    typeof candidate.identityId === 'string' &&
    uuidPattern.test(candidate.identityId) &&
    typeof candidate.organizationId === 'string' &&
    uuidPattern.test(candidate.organizationId) &&
    (candidate.locale === 'vi' || candidate.locale === 'en') &&
    typeof candidate.expiresAt === 'number' &&
    Number.isSafeInteger(candidate.expiresAt)
  );
}

function signatureFor(encodedPayload: string, secret: string): Buffer {
  return createHmac('sha256', secret).update(encodedPayload).digest();
}

export function createAgencySessionToken(
  payload: AgencySessionPayload,
  secret: string,
): string {
  requireSecret(secret);

  if (!isPayload(payload)) {
    throw new Error('Agency session payload is invalid');
  }

  const encodedPayload = Buffer.from(
    JSON.stringify(payload),
    'utf8',
  ).toString('base64url');

  return `${encodedPayload}.${signatureFor(encodedPayload, secret).toString('base64url')}`;
}

export function verifyAgencySessionToken(
  token: string | undefined,
  secret: string,
  nowSeconds = Math.floor(Date.now() / 1000),
): AgencySessionPayload | null {
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

  if (!isPayload(payload) || payload.expiresAt <= nowSeconds) {
    return null;
  }

  return {
    identityId: payload.identityId.toLowerCase(),
    organizationId: payload.organizationId.toLowerCase(),
    locale: payload.locale,
    expiresAt: payload.expiresAt,
  };
}
