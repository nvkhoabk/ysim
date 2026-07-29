export type OrganizationType = 'PLATFORM' | 'AGENCY';
export type OrganizationStatus = 'DRAFT' | 'ACTIVE' | 'SUSPENDED';
export type MarketCode = 'VN' | 'LA';

export type MembershipRole =
  | 'PLATFORM_ADMIN'
  | 'OPERATIONS'
  | 'SUPPORT'
  | 'FINANCE_READ_ONLY'
  | 'AGENCY_ADMIN'
  | 'AGENCY_USER';

export type MembershipStatus = 'ACTIVE' | 'REVOKED';

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

export interface AgencyProfileContract {
  organizationId: string;
  agencyCode: string;
  contactEmail: string | null;
  createdAt: string;
  updatedAt: string;
}

export interface CreateAgencyRequest {
  organizationCode: string;
  agencyCode: string;
  legalName: string;
  displayName: string;
  defaultMarket: MarketCode;
  contactEmail?: string | null;
}

export interface CreateAgencyResponse {
  organization: OrganizationContract;
  agencyProfile: AgencyProfileContract;
}

export interface ActivateAgencyResponse {
  organization: OrganizationContract;
}

export interface GrantMembershipRequest {
  identityId: string;
  role: MembershipRole;
}

export interface MembershipContract {
  id: string;
  organizationId: string;
  identityId: string;
  role: MembershipRole;
  status: MembershipStatus;
  createdAt: string;
  revokedAt: string | null;
}

export interface GrantMembershipResponse {
  membership: MembershipContract;
}

export interface OrganizationContextResponse {
  organization: OrganizationContract;
  membership: MembershipContract;
}
