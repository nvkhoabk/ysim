import {
  createHash,
  scrypt,
  timingSafeEqual,
} from 'node:crypto';

import {
  OPERATOR_SESSION_MAX_TTL_SECONDS,
  type OperatorPortalLocale,
  type OperatorPortalRole,
} from './operator-session';

const SCRYPT_PREFIX = 'scrypt';
const SCRYPT_COST = 16_384;
const SCRYPT_BLOCK_SIZE = 8;
const SCRYPT_PARALLELIZATION = 1;
const SCRYPT_KEY_LENGTH = 32;
const SCRYPT_MAX_MEMORY = 64 * 1024 * 1024;
const DEFAULT_SESSION_TTL_SECONDS = 60 * 60;

const uuidPattern =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;
const loginIdPattern = /^[a-z0-9][a-z0-9._@-]{2,127}$/u;

export interface OperatorCredentialConfig {
  identityId: string;
  locale: OperatorPortalLocale;
  loginId: string;
  passwordHash: string;
  revocationVersion: number;
  role: OperatorPortalRole;
  sessionSecret: string;
  sessionTtlSeconds: number;
}

export type OperatorAuthenticationResult =
  | { authenticated: true; config: OperatorCredentialConfig }
  | { authenticated: false; reason: 'CONFIG_INVALID' | 'INVALID_CREDENTIALS' };

interface ParsedPasswordHash {
  digest: Buffer;
  salt: Buffer;
}

function parsePositiveInteger(value: string | undefined): number | null {
  if (!value || !/^[1-9][0-9]*$/u.test(value)) return null;
  const parsed = Number(value);
  return Number.isSafeInteger(parsed) ? parsed : null;
}

function parsePasswordHash(value: string): ParsedPasswordHash | null {
  const [prefix, cost, blockSize, parallelization, salt, digest, extra] =
    value.split('$');

  if (
    prefix !== SCRYPT_PREFIX ||
    cost !== String(SCRYPT_COST) ||
    blockSize !== String(SCRYPT_BLOCK_SIZE) ||
    parallelization !== String(SCRYPT_PARALLELIZATION) ||
    !salt ||
    !digest ||
    extra !== undefined
  ) {
    return null;
  }

  try {
    const decodedSalt = Buffer.from(salt, 'base64url');
    const decodedDigest = Buffer.from(digest, 'base64url');
    if (
      decodedSalt.length < 16 ||
      decodedSalt.length > 64 ||
      decodedDigest.length !== SCRYPT_KEY_LENGTH
    ) {
      return null;
    }
    return { digest: decodedDigest, salt: decodedSalt };
  } catch {
    return null;
  }
}

function derivePassword(password: string, salt: Buffer): Promise<Buffer> {
  return new Promise((resolve, reject) => {
    scrypt(
      password,
      salt,
      SCRYPT_KEY_LENGTH,
      {
        N: SCRYPT_COST,
        p: SCRYPT_PARALLELIZATION,
        r: SCRYPT_BLOCK_SIZE,
        maxmem: SCRYPT_MAX_MEMORY,
      },
      (error, derivedKey) => {
        if (error) reject(error);
        else resolve(derivedKey);
      },
    );
  });
}

function fixedLengthLoginDigest(loginId: string): Buffer {
  return createHash('sha256').update(loginId, 'utf8').digest();
}

export function normalizeOperatorLoginId(value: string): string {
  return value.trim().toLowerCase();
}

export function readOperatorCredentialConfig(
  env: NodeJS.ProcessEnv = process.env,
): OperatorCredentialConfig | null {
  const loginId = normalizeOperatorLoginId(env.YSIM_OPERATOR_LOGIN_ID ?? '');
  const identityId = env.YSIM_OPERATOR_IDENTITY_ID?.toLowerCase() ?? '';
  const role = env.YSIM_OPERATOR_ROLE;
  const locale = env.YSIM_OPERATOR_LOCALE;
  const passwordHash = env.YSIM_OPERATOR_PASSWORD_SCRYPT ?? '';
  const sessionSecret = env.YSIM_PORTAL_SESSION_SECRET ?? '';
  const revocationVersion = parsePositiveInteger(
    env.YSIM_OPERATOR_REVOCATION_VERSION,
  );
  const sessionTtlSeconds = env.YSIM_OPERATOR_SESSION_TTL_SECONDS
    ? parsePositiveInteger(env.YSIM_OPERATOR_SESSION_TTL_SECONDS)
    : DEFAULT_SESSION_TTL_SECONDS;

  if (
    !loginIdPattern.test(loginId) ||
    !uuidPattern.test(identityId) ||
    (role !== 'PLATFORM_ADMIN' && role !== 'OPERATIONS') ||
    (locale !== 'vi' && locale !== 'en') ||
    !parsePasswordHash(passwordHash) ||
    sessionSecret.length < 32 ||
    !revocationVersion ||
    !sessionTtlSeconds ||
    sessionTtlSeconds > OPERATOR_SESSION_MAX_TTL_SECONDS
  ) {
    return null;
  }

  return {
    identityId,
    locale,
    loginId,
    passwordHash,
    revocationVersion,
    role,
    sessionSecret,
    sessionTtlSeconds,
  };
}

export async function authenticateOperatorCredentials(
  presentedLoginId: string,
  presentedPassword: string,
  env: NodeJS.ProcessEnv = process.env,
): Promise<OperatorAuthenticationResult> {
  const config = readOperatorCredentialConfig(env);
  if (!config) return { authenticated: false, reason: 'CONFIG_INVALID' };

  if (presentedPassword.length < 1 || presentedPassword.length > 256) {
    return { authenticated: false, reason: 'INVALID_CREDENTIALS' };
  }

  const parsedHash = parsePasswordHash(config.passwordHash);
  if (!parsedHash) return { authenticated: false, reason: 'CONFIG_INVALID' };

  try {
    const derived = await derivePassword(presentedPassword, parsedHash.salt);
    const loginMatches = timingSafeEqual(
      fixedLengthLoginDigest(normalizeOperatorLoginId(presentedLoginId)),
      fixedLengthLoginDigest(config.loginId),
    );
    const passwordMatches = timingSafeEqual(derived, parsedHash.digest);

    return loginMatches && passwordMatches
      ? { authenticated: true, config }
      : { authenticated: false, reason: 'INVALID_CREDENTIALS' };
  } catch {
    return { authenticated: false, reason: 'CONFIG_INVALID' };
  }
}

export const operatorPasswordHashContract = {
  blockSize: SCRYPT_BLOCK_SIZE,
  cost: SCRYPT_COST,
  keyLength: SCRYPT_KEY_LENGTH,
  parallelization: SCRYPT_PARALLELIZATION,
  prefix: SCRYPT_PREFIX,
} as const;
