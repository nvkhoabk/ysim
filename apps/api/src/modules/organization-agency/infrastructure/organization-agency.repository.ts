import { randomUUID } from 'node:crypto';

import { Injectable } from '@nestjs/common';
import type {
  AgencyProfileContract,
  MembershipContract,
  MembershipRole,
  OrganizationContract,
} from '@ysim/contracts';
import type { PoolClient, QueryResultRow } from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';

interface OrganizationRow extends QueryResultRow {
  id: string;
  code: string;
  type: 'PLATFORM' | 'AGENCY';
  status: 'DRAFT' | 'ACTIVE' | 'SUSPENDED';
  legal_name: string;
  display_name: string;
  default_market: 'VN' | 'LA';
  created_at: Date;
  updated_at: Date;
  version: number;
}

interface AgencyProfileRow extends QueryResultRow {
  organization_id: string;
  agency_code: string;
  contact_email: string | null;
  created_at: Date;
  updated_at: Date;
}

interface MembershipRow extends QueryResultRow {
  id: string;
  organization_id: string;
  identity_id: string;
  role: MembershipRole;
  status: 'ACTIVE' | 'REVOKED';
  created_at: Date;
  revoked_at: Date | null;
}

export interface CreateAgencyRecord {
  organizationCode: string;
  agencyCode: string;
  legalName: string;
  displayName: string;
  defaultMarket: 'VN' | 'LA';
  contactEmail: string | null;
  actorIdentityId: string;
}

const mapOrganization = (row: OrganizationRow): OrganizationContract => ({
  id: row.id,
  code: row.code,
  type: row.type,
  status: row.status,
  legalName: row.legal_name,
  displayName: row.display_name,
  defaultMarket: row.default_market,
  createdAt: row.created_at.toISOString(),
  updatedAt: row.updated_at.toISOString(),
  version: row.version,
});

const mapProfile = (row: AgencyProfileRow): AgencyProfileContract => ({
  organizationId: row.organization_id,
  agencyCode: row.agency_code,
  contactEmail: row.contact_email,
  createdAt: row.created_at.toISOString(),
  updatedAt: row.updated_at.toISOString(),
});

const mapMembership = (row: MembershipRow): MembershipContract => ({
  id: row.id,
  organizationId: row.organization_id,
  identityId: row.identity_id,
  role: row.role,
  status: row.status,
  createdAt: row.created_at.toISOString(),
  revokedAt: row.revoked_at?.toISOString() ?? null,
});

async function appendActivity(
  client: PoolClient,
  input: {
    organizationId: string;
    actorIdentityId: string;
    action: string;
    subjectType: string;
    subjectId: string;
    metadata?: Record<string, unknown>;
  },
): Promise<void> {
  await client.query(
    `INSERT INTO organization_agency.organization_activity (
       id,
       organization_id,
       actor_identity_id,
       action,
       subject_type,
       subject_id,
       metadata
     ) VALUES ($1, $2, $3, $4, $5, $6, $7::jsonb)`,
    [
      randomUUID(),
      input.organizationId,
      input.actorIdentityId,
      input.action,
      input.subjectType,
      input.subjectId,
      JSON.stringify(input.metadata ?? {}),
    ],
  );
}

@Injectable()
export class OrganizationAgencyRepository {
  constructor(private readonly database: PostgresService) {}

  async createAgency(
    input: CreateAgencyRecord,
  ): Promise<{
    organization: OrganizationContract;
    agencyProfile: AgencyProfileContract;
  }> {
    return this.database.transaction(async (client) => {
      const organizationId = randomUUID();

      const organizationResult = await client.query<OrganizationRow>(
        `INSERT INTO organization_agency.organizations (
           id,
           code,
           type,
           status,
           legal_name,
           display_name,
           default_market
         ) VALUES ($1, $2, 'AGENCY', 'DRAFT', $3, $4, $5)
         RETURNING *`,
        [
          organizationId,
          input.organizationCode,
          input.legalName,
          input.displayName,
          input.defaultMarket,
        ],
      );

      const profileResult = await client.query<AgencyProfileRow>(
        `INSERT INTO organization_agency.agency_profiles (
           organization_id,
           agency_code,
           contact_email
         ) VALUES ($1, $2, $3)
         RETURNING *`,
        [organizationId, input.agencyCode, input.contactEmail],
      );

      await appendActivity(client, {
        organizationId,
        actorIdentityId: input.actorIdentityId,
        action: 'AGENCY_CREATED',
        subjectType: 'Organization',
        subjectId: organizationId,
        metadata: {
          agencyCode: input.agencyCode,
          organizationCode: input.organizationCode,
        },
      });

      return {
        organization: mapOrganization(organizationResult.rows[0]),
        agencyProfile: mapProfile(profileResult.rows[0]),
      };
    });
  }

  async activateAgency(
    organizationId: string,
    actorIdentityId: string,
  ): Promise<OrganizationContract | null> {
    return this.database.transaction(async (client) => {
      const current = await client.query<OrganizationRow>(
        `SELECT *
           FROM organization_agency.organizations
          WHERE id = $1
            AND type = 'AGENCY'
          FOR UPDATE`,
        [organizationId],
      );

      const row = current.rows[0];
      if (!row) return null;
      if (row.status === 'ACTIVE') return mapOrganization(row);

      const updated = await client.query<OrganizationRow>(
        `UPDATE organization_agency.organizations
            SET status = 'ACTIVE',
                updated_at = CURRENT_TIMESTAMP,
                version = version + 1
          WHERE id = $1
          RETURNING *`,
        [organizationId],
      );

      await appendActivity(client, {
        organizationId,
        actorIdentityId,
        action: 'AGENCY_ACTIVATED',
        subjectType: 'Organization',
        subjectId: organizationId,
      });

      return mapOrganization(updated.rows[0]);
    });
  }

  async grantMembership(
    organizationId: string,
    identityId: string,
    role: MembershipRole,
    actorIdentityId: string,
  ): Promise<MembershipContract | null> {
    return this.database.transaction(async (client) => {
      const organization = await client.query<OrganizationRow>(
        `SELECT *
           FROM organization_agency.organizations
          WHERE id = $1
            AND type = 'AGENCY'
          FOR UPDATE`,
        [organizationId],
      );

      if (!organization.rows[0]) return null;

      const membershipId = randomUUID();
      const membership = await client.query<MembershipRow>(
        `INSERT INTO organization_agency.organization_memberships (
           id,
           organization_id,
           identity_id,
           role,
           status
         ) VALUES ($1, $2, $3, $4, 'ACTIVE')
         RETURNING *`,
        [membershipId, organizationId, identityId, role],
      );

      await appendActivity(client, {
        organizationId,
        actorIdentityId,
        action: 'MEMBERSHIP_GRANTED',
        subjectType: 'OrganizationMembership',
        subjectId: membershipId,
        metadata: { identityId, role },
      });

      return mapMembership(membership.rows[0]);
    });
  }

  async resolveContext(
    organizationId: string,
    identityId: string,
  ): Promise<{
    organization: OrganizationContract;
    membership: MembershipContract;
  } | null> {
    const result = await this.database.query<
      OrganizationRow & {
        membership_id: string;
        membership_identity_id: string;
        membership_role: MembershipRole;
        membership_status: 'ACTIVE' | 'REVOKED';
        membership_created_at: Date;
        membership_revoked_at: Date | null;
      }
    >(
      `SELECT
         o.*,
         m.id AS membership_id,
         m.identity_id AS membership_identity_id,
         m.role AS membership_role,
         m.status AS membership_status,
         m.created_at AS membership_created_at,
         m.revoked_at AS membership_revoked_at
       FROM organization_agency.organizations o
       JOIN organization_agency.organization_memberships m
         ON m.organization_id = o.id
      WHERE o.id = $1
        AND o.status = 'ACTIVE'
        AND m.identity_id = $2
        AND m.status = 'ACTIVE'
      ORDER BY m.created_at
      LIMIT 1`,
      [organizationId, identityId],
    );

    const row = result.rows[0];
    if (!row) return null;

    return {
      organization: mapOrganization(row),
      membership: mapMembership({
        id: row.membership_id,
        organization_id: row.id,
        identity_id: row.membership_identity_id,
        role: row.membership_role,
        status: row.membership_status,
        created_at: row.membership_created_at,
        revoked_at: row.membership_revoked_at,
      }),
    };
  }
}
