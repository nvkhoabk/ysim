import { cookies } from 'next/headers';

import {
  OPERATOR_SESSION_COOKIE,
  type OperatorSessionPayload,
  verifyOperatorSessionToken,
} from './operator-session';

export type OperatorPortalAccess =
  | {
      authorized: true;
      session: OperatorSessionPayload;
    }
  | {
      authorized: false;
      reason: 'CONFIG_INVALID' | 'SESSION_REQUIRED' | 'SESSION_INVALID';
    };

interface OperatorCookieStore {
  get(name: string): { value: string } | undefined;
}

export type OperatorCookieReader = () => Promise<OperatorCookieStore>;

export async function resolveOperatorPortalAccess(
  env: NodeJS.ProcessEnv = process.env,
  readCookies: OperatorCookieReader = cookies,
): Promise<OperatorPortalAccess> {
  const secret = env.YSIM_PORTAL_SESSION_SECRET;
  if (!secret || secret.length < 32) {
    return { authorized: false, reason: 'CONFIG_INVALID' };
  }

  const cookieStore = await readCookies();
  const token = cookieStore.get(OPERATOR_SESSION_COOKIE)?.value;
  if (!token) {
    return { authorized: false, reason: 'SESSION_REQUIRED' };
  }

  try {
    const session = verifyOperatorSessionToken(token, secret);
    return session
      ? { authorized: true, session }
      : { authorized: false, reason: 'SESSION_INVALID' };
  } catch {
    return { authorized: false, reason: 'CONFIG_INVALID' };
  }
}
