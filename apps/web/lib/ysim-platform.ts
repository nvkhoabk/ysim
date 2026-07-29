import type {
  AgencyPortalContextResponse,
  OrganizationContract,
  OrganizationInactiveError,
} from './agency-contracts';

import type { AgencySessionPayload } from './agency-session';

export type AgencyPortalContextResult =
  | {
      state: 'ready';
      context: AgencyPortalContextResponse;
    }
  | {
      state: 'denied';
    }
  | {
      state: 'organization-inactive';
      organization: OrganizationContract;
    }
  | {
      state: 'unavailable';
      reason: string;
    };

const isOrganizationInactiveError = (
  value: unknown,
): value is OrganizationInactiveError => {
  if (typeof value !== 'object' || value === null) return false;
  const candidate = value as Partial<OrganizationInactiveError>;
  return (
    candidate.statusCode === 423 &&
    candidate.code === 'ORGANIZATION_INACTIVE' &&
    typeof candidate.organization === 'object' &&
    candidate.organization !== null
  );
};

export async function resolveAgencyPortalContext(
  session: AgencySessionPayload,
): Promise<AgencyPortalContextResult> {
  const apiUrl = process.env.YSIM_PLATFORM_API_URL?.replace(/\/+$/u, '');
  const bootstrapToken = process.env.YSIM_BOOTSTRAP_TOKEN;

  if (!apiUrl || !bootstrapToken) {
    return {
      state: 'unavailable',
      reason: 'Portal server configuration is incomplete',
    };
  }

  try {
    const response = await fetch(
      `${apiUrl}/internal/r1/organizations/portal-context`,
      {
        cache: 'no-store',
        headers: {
          'x-ysim-bootstrap-token': bootstrapToken,
          'x-ysim-identity-id': session.identityId,
          'x-ysim-organization-id': session.organizationId,
        },
        signal: AbortSignal.timeout(5_000),
      },
    );

    if (response.ok) {
      return {
        state: 'ready',
        context: (await response.json()) as AgencyPortalContextResponse,
      };
    }

    if (response.status === 401 || response.status === 403) {
      return { state: 'denied' };
    }

    if (response.status === 423) {
      const body: unknown = await response.json().catch(() => null);
      if (isOrganizationInactiveError(body)) {
        return {
          state: 'organization-inactive',
          organization: body.organization,
        };
      }
    }

    return {
      state: 'unavailable',
      reason: `Platform API returned ${response.status}`,
    };
  } catch (error) {
    return {
      state: 'unavailable',
      reason:
        error instanceof Error
          ? error.message
          : 'Platform API request failed',
    };
  }
}
