import { randomUUID } from 'node:crypto';

import { Injectable } from '@nestjs/common';
import type {
  SupplierEnvironment,
  SupplierEnvironmentContractStatus,
  SupplierEnvironmentProfileContract,
  SupplierHttpMethod,
  SupplierPlanContract,
  SupplierPlanMappingAssessmentContract,
  SupplierPlanMappingContract,
  SupplierPlanMappingStatus,
} from '@ysim/contracts';
import type {
  PoolClient,
  QueryResult,
  QueryResultRow,
} from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';
import type { NormalizedGigagoPlan } from '../domain/gigago-plan-normalizer.js';

interface EnvironmentRow extends QueryResultRow {
  id: string;
  supplier_code: 'GIGAGO';
  environment: SupplierEnvironment;
  base_url: string;
  credential_ref: string;
  contract_status: SupplierEnvironmentContractStatus;
  get_packages_method: SupplierHttpMethod;
  create_order_method: SupplierHttpMethod;
  documented_get_my_orders_method: SupplierHttpMethod;
  confirmed_get_my_orders_method: SupplierHttpMethod | null;
}

interface PlanRow extends QueryResultRow {
  id: string;
  supplier_environment_id: string;
  supplier_code: 'GIGAGO';
  environment: SupplierEnvironment;
  external_plan_id: string;
  name: string;
  parent_group_id: string | null;
  parent_group_name: string | null;
  apn: string | null;
  network_type: string | null;
  country_codes: string[];
  operator_networks: unknown;
  data_policy: 'FIXED' | 'DAILY' | 'UNLIMITED';
  data_amount_mb: number | null;
  daily_data_amount_mb: number | null;
  fair_use_data_amount_mb: number | null;
  duration_days: number;
  hotspot_supported: boolean;
  phone_number_included: boolean;
  topup_supported: boolean;
  raw_snapshot_hash: string;
  observed_at: Date;
  status: 'ACTIVE' | 'SUSPENDED';
  created_at: Date;
  updated_at: Date;
  version: number;
}

interface MappingRow extends QueryResultRow {
  id: string;
  supplier_plan_id: string;
  supplier_environment_id: string;
  supplier_code: 'GIGAGO';
  environment: SupplierEnvironment;
  product_offer_id: string;
  status: SupplierPlanMappingStatus;
  compatibility_issues: unknown;
  compatibility_warnings: unknown;
  created_by: string;
  created_at: Date;
  activated_at: Date | null;
  suspended_at: Date | null;
  version: number;
  contract_status: SupplierEnvironmentContractStatus;
}

export type ActivateMappingResult =
  | { kind: 'NOT_FOUND' }
  | { kind: 'ENVIRONMENT_UNCONFIRMED' }
  | { kind: 'SUCCESS'; mapping: SupplierPlanMappingContract };

function asJsonArray<T>(value: unknown): T[] {
  return Array.isArray(value) ? (value as T[]) : [];
}

function mapEnvironment(
  row: EnvironmentRow,
): SupplierEnvironmentProfileContract {
  return {
    supplierCode: row.supplier_code,
    environment: row.environment,
    baseUrl: row.base_url,
    credentialRef: row.credential_ref,
    contractStatus: row.contract_status,
    getPackagesMethod: row.get_packages_method,
    createOrderMethod: row.create_order_method,
    documentedGetMyOrdersMethod:
      row.documented_get_my_orders_method,
    confirmedGetMyOrdersMethod:
      row.confirmed_get_my_orders_method,
  };
}

function mapPlan(row: PlanRow): SupplierPlanContract {
  return {
    id: row.id,
    supplierCode: row.supplier_code,
    environment: row.environment,
    externalPlanId: row.external_plan_id,
    name: row.name,
    parentGroupId: row.parent_group_id,
    parentGroupName: row.parent_group_name,
    apn: row.apn,
    networkType: row.network_type,
    countryCodes: row.country_codes,
    operatorNetworks: asJsonArray(row.operator_networks),
    dataPolicy: row.data_policy,
    dataAmountMb: row.data_amount_mb,
    dailyDataAmountMb: row.daily_data_amount_mb,
    fairUseDataAmountMb: row.fair_use_data_amount_mb,
    durationDays: row.duration_days,
    hotspotSupported: row.hotspot_supported,
    phoneNumberIncluded: row.phone_number_included,
    topupSupported: row.topup_supported,
    rawSnapshotHash: row.raw_snapshot_hash,
    observedAt: row.observed_at.toISOString(),
    status: row.status,
    createdAt: row.created_at.toISOString(),
    updatedAt: row.updated_at.toISOString(),
    version: row.version,
  };
}

function mapMapping(row: MappingRow): SupplierPlanMappingContract {
  return {
    id: row.id,
    supplierPlanId: row.supplier_plan_id,
    supplierCode: row.supplier_code,
    environment: row.environment,
    productOfferId: row.product_offer_id,
    status: row.status,
    assessment: {
      compatible: asJsonArray(row.compatibility_issues).length === 0,
      issues: asJsonArray(row.compatibility_issues),
      warnings: asJsonArray(row.compatibility_warnings),
    },
    createdBy: row.created_by,
    createdAt: row.created_at.toISOString(),
    activatedAt: row.activated_at?.toISOString() ?? null,
    suspendedAt: row.suspended_at?.toISOString() ?? null,
    version: row.version,
  };
}

async function appendActivity(
  client: PoolClient,
  input: {
    actorIdentityId: string;
    action: string;
    subjectType: string;
    subjectId: string;
    metadata?: Record<string, unknown>;
  },
): Promise<void> {
  await client.query(
    `INSERT INTO supplier_management.supplier_activity (
       id,
       actor_identity_id,
       action,
       subject_type,
       subject_id,
       metadata
     ) VALUES ($1, $2, $3, $4, $5, $6::jsonb)`,
    [
      randomUUID(),
      input.actorIdentityId,
      input.action,
      input.subjectType,
      input.subjectId,
      JSON.stringify(input.metadata ?? {}),
    ],
  );
}

@Injectable()
export class SupplierManagementRepository {
  constructor(private readonly database: PostgresService) {}

  async listGigagoEnvironments(): Promise<
    SupplierEnvironmentProfileContract[]
  > {
    const result = await this.database.query<EnvironmentRow>(
      `SELECT
         se.id,
         s.code AS supplier_code,
         se.environment,
         se.base_url,
         se.credential_ref,
         se.contract_status,
         se.get_packages_method,
         se.create_order_method,
         se.documented_get_my_orders_method,
         se.confirmed_get_my_orders_method
       FROM supplier_management.supplier_environments se
       JOIN supplier_management.suppliers s
         ON s.id = se.supplier_id
      WHERE s.code = 'GIGAGO'
      ORDER BY se.environment`,
    );

    return result.rows.map(mapEnvironment);
  }

  async upsertGigagoPlan(
    plan: NormalizedGigagoPlan,
    actorIdentityId: string,
  ): Promise<SupplierPlanContract | null> {
    return this.database.transaction(async (client) => {
      const environment = await client.query<EnvironmentRow>(
        `SELECT
           se.id,
           s.code AS supplier_code,
           se.environment,
           se.base_url,
           se.credential_ref,
           se.contract_status,
           se.get_packages_method,
           se.create_order_method,
           se.documented_get_my_orders_method,
           se.confirmed_get_my_orders_method
         FROM supplier_management.supplier_environments se
         JOIN supplier_management.suppliers s
           ON s.id = se.supplier_id
        WHERE s.code = 'GIGAGO'
          AND se.environment = $1
          AND s.status = 'ACTIVE'
        FOR UPDATE OF se`,
        [plan.environment],
      );

      const environmentRow = environment.rows[0];
      if (!environmentRow) return null;

      const id = randomUUID();
      const result = await client.query<PlanRow>(
        `INSERT INTO supplier_management.supplier_plans (
           id,
           supplier_environment_id,
           external_plan_id,
           name,
           parent_group_id,
           parent_group_name,
           apn,
           network_type,
           country_codes,
           operator_networks,
           data_policy,
           data_amount_mb,
           daily_data_amount_mb,
           fair_use_data_amount_mb,
           duration_days,
           hotspot_supported,
           phone_number_included,
           topup_supported,
           raw_snapshot,
           raw_snapshot_hash,
           observed_at,
           status
         ) VALUES (
           $1,
           $2,
           $3,
           $4,
           $5,
           $6,
           $7,
           $8,
           $9::text[],
           $10::jsonb,
           $11,
           $12,
           $13,
           $14,
           $15,
           $16,
           $17,
           $18,
           $19::jsonb,
           $20,
           $21,
           'ACTIVE'
         )
         ON CONFLICT (
           supplier_environment_id,
           external_plan_id
         ) DO UPDATE
           SET name = EXCLUDED.name,
               parent_group_id = EXCLUDED.parent_group_id,
               parent_group_name = EXCLUDED.parent_group_name,
               apn = EXCLUDED.apn,
               network_type = EXCLUDED.network_type,
               country_codes = EXCLUDED.country_codes,
               operator_networks = EXCLUDED.operator_networks,
               data_policy = EXCLUDED.data_policy,
               data_amount_mb = EXCLUDED.data_amount_mb,
               daily_data_amount_mb = EXCLUDED.daily_data_amount_mb,
               fair_use_data_amount_mb = EXCLUDED.fair_use_data_amount_mb,
               duration_days = EXCLUDED.duration_days,
               hotspot_supported = EXCLUDED.hotspot_supported,
               phone_number_included = EXCLUDED.phone_number_included,
               topup_supported = EXCLUDED.topup_supported,
               raw_snapshot = EXCLUDED.raw_snapshot,
               raw_snapshot_hash = EXCLUDED.raw_snapshot_hash,
               observed_at = EXCLUDED.observed_at,
               status = 'ACTIVE',
               updated_at = CURRENT_TIMESTAMP,
               version = supplier_management.supplier_plans.version + 1
         RETURNING
           *,
           $22::text AS supplier_code,
           $23::text AS environment`,
        [
          id,
          environmentRow.id,
          plan.externalPlanId,
          plan.name,
          plan.parentGroupId,
          plan.parentGroupName,
          plan.apn,
          plan.networkType,
          plan.countryCodes,
          JSON.stringify(plan.operatorNetworks),
          plan.dataPolicy,
          plan.dataAmountMb,
          plan.dailyDataAmountMb,
          plan.fairUseDataAmountMb,
          plan.durationDays,
          plan.hotspotSupported,
          plan.phoneNumberIncluded,
          plan.topupSupported,
          JSON.stringify(plan.rawSnapshot),
          plan.rawSnapshotHash,
          plan.observedAt,
          environmentRow.supplier_code,
          environmentRow.environment,
        ],
      );

      const row = result.rows[0];

      await appendActivity(client, {
        actorIdentityId,
        action: 'SUPPLIER_PLAN_IMPORTED',
        subjectType: 'SupplierPlan',
        subjectId: row.id,
        metadata: {
          environment: plan.environment,
          externalPlanId: plan.externalPlanId,
          rawSnapshotHash: plan.rawSnapshotHash,
        },
      });

      return mapPlan(row);
    });
  }

  async findPlan(
    supplierPlanId: string,
  ): Promise<SupplierPlanContract | null> {
    const result = await this.database.query<PlanRow>(
      `SELECT
         sp.*,
         s.code AS supplier_code,
         se.environment
       FROM supplier_management.supplier_plans sp
       JOIN supplier_management.supplier_environments se
         ON se.id = sp.supplier_environment_id
       JOIN supplier_management.suppliers s
         ON s.id = se.supplier_id
      WHERE sp.id = $1`,
      [supplierPlanId],
    );

    const row = result.rows[0];
    return row ? mapPlan(row) : null;
  }

  async createMapping(
    input: {
      supplierPlanId: string;
      productOfferId: string;
      assessment: SupplierPlanMappingAssessmentContract;
      actorIdentityId: string;
    },
  ): Promise<SupplierPlanMappingContract | null> {
    return this.database.transaction(async (client) => {
      const plan = await client.query<PlanRow>(
        `SELECT
           sp.*,
           s.code AS supplier_code,
           se.environment
         FROM supplier_management.supplier_plans sp
         JOIN supplier_management.supplier_environments se
           ON se.id = sp.supplier_environment_id
         JOIN supplier_management.suppliers s
           ON s.id = se.supplier_id
        WHERE sp.id = $1
          AND sp.status = 'ACTIVE'
        FOR UPDATE OF sp`,
        [input.supplierPlanId],
      );

      const planRow = plan.rows[0];
      if (!planRow) return null;

      const id = randomUUID();
      const result = await client.query<MappingRow>(
        `INSERT INTO supplier_management.supplier_plan_mappings (
           id,
           supplier_plan_id,
           supplier_environment_id,
           product_offer_id,
           status,
           compatibility_issues,
           compatibility_warnings,
           created_by
         ) VALUES (
           $1,
           $2,
           $3,
           $4,
           'DRAFT',
           $5::jsonb,
           $6::jsonb,
           $7
         )
         RETURNING
           *,
           $8::text AS supplier_code,
           $9::text AS environment,
           'DOCUMENTED_UNVERIFIED'::text AS contract_status`,
        [
          id,
          input.supplierPlanId,
          planRow.supplier_environment_id,
          input.productOfferId,
          JSON.stringify(input.assessment.issues),
          JSON.stringify(input.assessment.warnings),
          input.actorIdentityId,
          planRow.supplier_code,
          planRow.environment,
        ],
      );

      await appendActivity(client, {
        actorIdentityId: input.actorIdentityId,
        action: 'SUPPLIER_PLAN_MAPPING_CREATED',
        subjectType: 'SupplierPlanMapping',
        subjectId: id,
        metadata: {
          supplierPlanId: input.supplierPlanId,
          productOfferId: input.productOfferId,
          environment: planRow.environment,
        },
      });

      return mapMapping(result.rows[0]);
    });
  }

  async activateMapping(
    mappingId: string,
    actorIdentityId: string,
  ): Promise<ActivateMappingResult> {
    return this.database.transaction(async (client) => {
      const current = await client.query<MappingRow>(
        `SELECT
           spm.*,
           s.code AS supplier_code,
           se.environment,
           se.contract_status
         FROM supplier_management.supplier_plan_mappings spm
         JOIN supplier_management.supplier_environments se
           ON se.id = spm.supplier_environment_id
         JOIN supplier_management.suppliers s
           ON s.id = se.supplier_id
        WHERE spm.id = $1
        FOR UPDATE OF spm`,
        [mappingId],
      );

      const row = current.rows[0];
      if (!row) return { kind: 'NOT_FOUND' };

      if (row.status === 'ACTIVE') {
        return { kind: 'SUCCESS', mapping: mapMapping(row) };
      }

      if (row.contract_status !== 'PROBED') {
        return { kind: 'ENVIRONMENT_UNCONFIRMED' };
      }

      const result = await client.query<MappingRow>(
        `UPDATE supplier_management.supplier_plan_mappings
            SET status = 'ACTIVE',
                activated_at = CURRENT_TIMESTAMP,
                suspended_at = NULL,
                version = version + 1
          WHERE id = $1
          RETURNING
            *,
            $2::text AS supplier_code,
            $3::text AS environment,
            $4::text AS contract_status`,
        [
          mappingId,
          row.supplier_code,
          row.environment,
          row.contract_status,
        ],
      );

      await appendActivity(client, {
        actorIdentityId,
        action: 'SUPPLIER_PLAN_MAPPING_ACTIVATED',
        subjectType: 'SupplierPlanMapping',
        subjectId: mappingId,
        metadata: {
          supplierPlanId: row.supplier_plan_id,
          productOfferId: row.product_offer_id,
          environment: row.environment,
        },
      });

      return {
        kind: 'SUCCESS',
        mapping: mapMapping(result.rows[0]),
      };
    });
  }

  async listActiveMappings(
    productOfferId: string,
    environment: SupplierEnvironment,
  ): Promise<SupplierPlanMappingContract[]> {
    const result = await this.database.query<MappingRow>(
      `SELECT
         spm.*,
         s.code AS supplier_code,
         se.environment,
         se.contract_status
       FROM supplier_management.supplier_plan_mappings spm
       JOIN supplier_management.supplier_environments se
         ON se.id = spm.supplier_environment_id
       JOIN supplier_management.suppliers s
         ON s.id = se.supplier_id
      WHERE spm.product_offer_id = $1
        AND se.environment = $2
        AND spm.status = 'ACTIVE'
      ORDER BY spm.created_at`,
      [productOfferId, environment],
    );

    return result.rows.map(mapMapping);
  }
}
