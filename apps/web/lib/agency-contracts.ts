export type OrganizationType = 'PLATFORM' | 'AGENCY';
export type OrganizationStatus = 'DRAFT' | 'ACTIVE' | 'SUSPENDED';
export type MarketCode = 'VN' | 'LA';
export type MembershipStatus = 'ACTIVE' | 'REVOKED';
export type AgencyPortalRole = 'AGENCY_ADMIN' | 'AGENCY_USER';

export interface OrganizationContract {
  id: string;
  code: string;
  type: OrganizationType;
  status: OrganizationStatus;
  legalName: string;
  displayName: string;
  defaultMarket: MarketCode;
  createdAt: string;
  updatedAt: string;
  version: number;
}

export interface AgencyPortalMembershipContract {
  id: string;
  organizationId: string;
  identityId: string;
  role: AgencyPortalRole;
  status: MembershipStatus;
  createdAt: string;
  revokedAt: string | null;
}

export interface AgencyPortalContextResponse {
  organization: OrganizationContract;
  membership: AgencyPortalMembershipContract;
}

export interface OrganizationInactiveError {
  statusCode: 423;
  error: 'Locked';
  code: 'ORGANIZATION_INACTIVE';
  organization: OrganizationContract;
}
