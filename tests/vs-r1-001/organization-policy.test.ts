import { describe, expect, it } from 'vitest';

import {
  normalizeAgencyCode,
  normalizeOrganizationCode,
  optionalEmail,
  OrganizationPolicyError,
  requireMarket,
  requireMembershipRole,
  requireName,
  requireUuid,
} from '../../apps/api/src/modules/organization-agency/domain/organization-policy.js';

describe('organization policy', () => {
  it('normalizes organization and agency codes', () => {
    expect(normalizeOrganizationCode(' agency-vn ')).toBe('AGENCY-VN');
    expect(normalizeAgencyCode(' lao_partner ')).toBe('LAO_PARTNER');
  });

  it('rejects unsafe codes', () => {
    expect(() => normalizeOrganizationCode('a')).toThrow(
      OrganizationPolicyError,
    );
    expect(() => normalizeAgencyCode('agency.vn')).toThrow(
      OrganizationPolicyError,
    );
  });

  it('validates names, markets, roles, UUIDs and email', () => {
    expect(requireName(' Pilot Agency ', 'displayName')).toBe('Pilot Agency');
    expect(requireMarket('VN')).toBe('VN');
    expect(requireMembershipRole('AGENCY_ADMIN')).toBe('AGENCY_ADMIN');
    expect(
      requireUuid(
        '10000000-0000-4000-8000-000000000001',
        'identityId',
      ),
    ).toBe('10000000-0000-4000-8000-000000000001');
    expect(optionalEmail(' ADMIN@EXAMPLE.COM ')).toBe('admin@example.com');
    expect(optionalEmail(null)).toBeNull();
  });

  it('rejects unsupported values', () => {
    expect(() => requireMarket('US')).toThrow(OrganizationPolicyError);
    expect(() => requireMembershipRole('OWNER')).toThrow(
      OrganizationPolicyError,
    );
    expect(() => requireUuid('not-a-uuid', 'identityId')).toThrow(
      OrganizationPolicyError,
    );
    expect(() => optionalEmail('invalid')).toThrow(OrganizationPolicyError);
  });
});
