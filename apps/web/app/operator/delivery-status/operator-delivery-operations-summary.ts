export type OperatorDeliveryOperationsSummary =
  | {
      authorized: true;
      available: true;
      summary: {
        generatedAt: string;
        pending: number;
        failed: number;
        published: number;
        inFlight: number;
        actionable: number;
        oldestActionableAt: string | null;
      };
    }
  | { authorized: true; available: false; reason: 'SUMMARY_UNAVAILABLE' }
  | {
      authorized: false;
      reason: 'ACCESS_DENIED' | 'CONFIG_INVALID' | 'STATUS_UNAVAILABLE';
    };

const denied = (
  reason: 'CONFIG_INVALID' | 'STATUS_UNAVAILABLE',
): OperatorDeliveryOperationsSummary => ({ authorized: false, reason });

const validCount = (value: unknown): value is number =>
  typeof value === 'number' &&
  Number.isSafeInteger(value) &&
  value >= 0 &&
  value <= 1_000_000_000;

const validTimestamp = (value: unknown): value is string =>
  typeof value === 'string' && Number.isFinite(Date.parse(value));

export async function readOperatorDeliveryOperationsSummary(
  env: NodeJS.ProcessEnv = process.env,
  request: typeof fetch = fetch,
): Promise<OperatorDeliveryOperationsSummary> {
  const baseUrl = env.YSIM_API_INTERNAL_BASE_URL;
  const token = env.CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN;
  if (!baseUrl || !token || token.length < 32) return denied('CONFIG_INVALID');

  let endpoint: URL;
  try {
    endpoint = new URL('/internal/delivery/operations-summary', baseUrl);
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
    if (!value || typeof value !== 'object' || !('authorized' in value)) {
      return denied('STATUS_UNAVAILABLE');
    }
    const result = value as Record<string, unknown>;
    if (
      result.authorized === false &&
      ['ACCESS_DENIED', 'CONFIG_INVALID', 'STATUS_UNAVAILABLE'].includes(
        String(result.reason),
      )
    ) {
      return {
        authorized: false,
        reason: result.reason as
          | 'ACCESS_DENIED'
          | 'CONFIG_INVALID'
          | 'STATUS_UNAVAILABLE',
      };
    }
    if (
      result.authorized === true &&
      result.available === false &&
      result.reason === 'SUMMARY_UNAVAILABLE'
    ) {
      return { authorized: true, available: false, reason: 'SUMMARY_UNAVAILABLE' };
    }

    const summary = result.summary as Record<string, unknown> | undefined;
    const oldestActionableAt = summary?.oldestActionableAt;
    if (
      result.authorized !== true ||
      result.available !== true ||
      !summary ||
      !validTimestamp(summary.generatedAt) ||
      !validCount(summary.pending) ||
      !validCount(summary.failed) ||
      !validCount(summary.published) ||
      !validCount(summary.inFlight) ||
      !validCount(summary.actionable) ||
      (oldestActionableAt !== null && !validTimestamp(oldestActionableAt)) ||
      summary.inFlight > summary.pending + summary.failed ||
      summary.actionable > summary.pending + summary.failed ||
      summary.inFlight + summary.actionable > summary.pending + summary.failed
    ) {
      return denied('STATUS_UNAVAILABLE');
    }

    return {
      authorized: true,
      available: true,
      summary: {
        generatedAt: summary.generatedAt,
        pending: summary.pending,
        failed: summary.failed,
        published: summary.published,
        inFlight: summary.inFlight,
        actionable: summary.actionable,
        oldestActionableAt: oldestActionableAt as string | null,
      },
    };
  } catch {
    return denied('STATUS_UNAVAILABLE');
  }
}
