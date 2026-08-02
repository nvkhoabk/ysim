import { cookies } from 'next/headers';

import {
  OPERATOR_SESSION_COOKIE,
  type OperatorSessionPayload,
  verifyOperatorSessionToken,
} from './operator-session';
import { readOperatorCredentialConfig } from './operator-credential';

export type OperatorPortalAccess =
  | {
      authorized: true;
      session: OperatorSessionPayload;
    }
  | {
      authorized: false;
      reason:
        | 'CONFIG_INVALID'
        | 'SESSION_REQUIRED'
        | 'SESSION_INVALID'
        | 'SESSION_REVOKED';
    };

interface OperatorCookieStore {
  get(name: string): { value: string } | undefined;
}

export type OperatorCookieReader = () => Promise<OperatorCookieStore>;

export async function resolveOperatorPortalAccess(
  env: NodeJS.ProcessEnv = process.env,
  readCookies: OperatorCookieReader = cookies,
): Promise<OperatorPortalAccess> {
  const config = readOperatorCredentialConfig(env);
  if (!config) {
    return { authorized: false, reason: 'CONFIG_INVALID' };
  }

  const cookieStore = await readCookies();
  const token = cookieStore.get(OPERATOR_SESSION_COOKIE)?.value;
  if (!token) {
    return { authorized: false, reason: 'SESSION_REQUIRED' };
  }

  try {
    const session = verifyOperatorSessionToken(token, config.sessionSecret);
    if (!session) return { authorized: false, reason: 'SESSION_INVALID' };
    if (session.revocationVersion !== config.revocationVersion) {
      return { authorized: false, reason: 'SESSION_REVOKED' };
    }
    if (
      session.identityId !== config.identityId ||
      session.role !== config.role ||
      session.locale !== config.locale
    ) {
      return { authorized: false, reason: 'SESSION_REVOKED' };
    }
    return { authorized: true, session };
  } catch {
    return { authorized: false, reason: 'CONFIG_INVALID' };
  }
}
