export type OperatorDeliveryStatus =
  | {
      authorized: true;
      status: {
        state: 'ACTIVE' | 'INACTIVE' | 'BLOCKED' | 'ERROR';
        reason: string;
        schedulerEnabled: boolean;
        emailMode: 'disabled' | 'dry-run' | 'live' | 'invalid';
      };
    }
  | { authorized: false; reason: 'ACCESS_DENIED' | 'CONFIG_INVALID' | 'STATUS_UNAVAILABLE' };

const denied = (reason: 'CONFIG_INVALID' | 'STATUS_UNAVAILABLE'): OperatorDeliveryStatus => ({
  authorized: false,
  reason,
});

export async function readOperatorDeliveryStatus(
  env: NodeJS.ProcessEnv = process.env,
  request: typeof fetch = fetch,
): Promise<OperatorDeliveryStatus> {
  const baseUrl = env.YSIM_API_INTERNAL_BASE_URL;
  const token = env.CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN;
  if (!baseUrl || !token || token.length < 32) return denied('CONFIG_INVALID');

  let endpoint: URL;
  try {
    endpoint = new URL('/internal/delivery/runtime-status', baseUrl);
  } catch {
    return denied('CONFIG_INVALID');
  }

  try {
    const response = await request(endpoint, {
      method: 'GET',
      cache: 'no-store',
      headers: { 'x-ysim-operator-token': token },
    });
    if (!response.ok) return denied('STATUS_UNAVAILABLE');
    const value: unknown = await response.json();
    if (!value || typeof value !== 'object' || !("authorized" in value)) return denied('STATUS_UNAVAILABLE');
    const result = value as Record<string, unknown>;
    if (result.authorized === false && ['ACCESS_DENIED', 'CONFIG_INVALID', 'STATUS_UNAVAILABLE'].includes(String(result.reason))) {
      return { authorized: false, reason: result.reason as 'ACCESS_DENIED' | 'CONFIG_INVALID' | 'STATUS_UNAVAILABLE' };
    }
    const status = result.status as Record<string, unknown> | undefined;
    if (result.authorized !== true || !status || !['ACTIVE', 'INACTIVE', 'BLOCKED', 'ERROR'].includes(String(status.state)) || typeof status.reason !== 'string' || typeof status.schedulerEnabled !== 'boolean' || !['disabled', 'dry-run', 'live', 'invalid'].includes(String(status.emailMode))) {
      return denied('STATUS_UNAVAILABLE');
    }
    return {
      authorized: true,
      status: {
        state: status.state as 'ACTIVE' | 'INACTIVE' | 'BLOCKED' | 'ERROR',
        reason: status.reason,
        schedulerEnabled: status.schedulerEnabled,
        emailMode: status.emailMode as 'disabled' | 'dry-run' | 'live' | 'invalid',
      },
    };
  } catch {
    return denied('STATUS_UNAVAILABLE');
  }
}
