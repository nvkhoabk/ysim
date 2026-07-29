import type { MarketCode, MembershipRole } from '@ysim/contracts';

const organizationCodePattern = /^[A-Z][A-Z0-9_-]{2,31}$/u;
const agencyCodePattern = /^[A-Z][A-Z0-9_-]{2,31}$/u;
const uuidPattern =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;
const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/u;

const roles = new Set<MembershipRole>([
  'PLATFORM_ADMIN',
  'OPERATIONS',
  'SUPPORT',
  'FINANCE_READ_ONLY',
  'AGENCY_ADMIN',
  'AGENCY_USER',
]);

export class OrganizationPolicyError extends Error {}

export function normalizeOrganizationCode(value: unknown): string {
  if (typeof value !== 'string') {
    throw new OrganizationPolicyError('organizationCode must be a string');
  }

  const normalized = value.trim().toUpperCase();
  if (!organizationCodePattern.test(normalized)) {
    throw new OrganizationPolicyError(
      'organizationCode must contain 3 to 32 uppercase letters, digits, underscores or hyphens',
    );
  }
  return normalized;
}

export function normalizeAgencyCode(value: unknown): string {
  if (typeof value !== 'string') {
    throw new OrganizationPolicyError('agencyCode must be a string');
  }

  const normalized = value.trim().toUpperCase();
  if (!agencyCodePattern.test(normalized)) {
    throw new OrganizationPolicyError(
      'agencyCode must contain 3 to 32 uppercase letters, digits, underscores or hyphens',
    );
  }
  return normalized;
}

export function requireName(value: unknown, field: string): string {
  if (typeof value !== 'string') {
    throw new OrganizationPolicyError(`${field} must be a string`);
  }

  const normalized = value.trim();
  if (normalized.length < 2 || normalized.length > 200) {
    throw new OrganizationPolicyError(`${field} must contain 2 to 200 characters`);
  }
  return normalized;
}

export function requireMarket(value: unknown): MarketCode {
  if (value !== 'VN' && value !== 'LA') {
    throw new OrganizationPolicyError('defaultMarket must be VN or LA');
  }
  return value;
}

export function optionalEmail(value: unknown): string | null {
  if (value === undefined || value === null || value === '') {
    return null;
  }
  if (typeof value !== 'string') {
    throw new OrganizationPolicyError('contactEmail must be a string or null');
  }

  const normalized = value.trim().toLowerCase();
  if (normalized.length > 254 || !emailPattern.test(normalized)) {
    throw new OrganizationPolicyError('contactEmail is invalid');
  }
  return normalized;
}

export function requireUuid(value: unknown, field: string): string {
  if (typeof value !== 'string' || !uuidPattern.test(value)) {
    throw new OrganizationPolicyError(`${field} must be a valid UUID`);
  }
  return value.toLowerCase();
}

export function requireMembershipRole(value: unknown): MembershipRole {
  if (typeof value !== 'string' || !roles.has(value as MembershipRole)) {
    throw new OrganizationPolicyError('role is not supported');
  }
  return value as MembershipRole;
}
