import { randomUUID } from 'node:crypto';

import { Injectable } from '@nestjs/common';
import type {
  QueryResultRow,
} from 'pg';

import {
  PostgresService,
} from '../../../platform/database/postgres.service.js';
import type {
  EncryptedEsimPayload,
} from './esim-asset.crypto.js';

export interface PreparedEsimAssetRecord {
  procurementRequestId: string;
  supplierSubmissionId: string;
  supplierCode: 'GIGAGO';
  supplierEnvironment: 'SANDBOX';
  supplierOrderId: string;
  supplierDetailId: number;
  providerRequestId: string;
  planId: string;
  dataLabel: string;
  validityLabel: string;
  iccidFingerprint: string;
  encryptedPayload:
    EncryptedEsimPayload;
  capturedAt: string;
}

export type PersistEsimAssetBatchResult =
  | {
      kind: 'CREATED';
      assetIds: string[];
      assetCount: number;
    }
  | {
      kind: 'REPLAY';
      assetIds: string[];
      assetCount: number;
    }
  | {
      kind: 'CONFLICT';
    };

interface ExistingAssetRow
  extends QueryResultRow {
  id: string;
  procurement_request_id: string;
  supplier_submission_id: string;
  supplier_code: string;
  supplier_environment: string;
  supplier_order_id: string;
  supplier_detail_id:
    number | string;
  provider_request_id: string;
  plan_id: string;
  data_label: string;
  validity_label: string;
  iccid_fingerprint: string;
  status: string;
}

const isUniqueViolation = (
  error: unknown,
): boolean =>
  typeof error === 'object' &&
  error !== null &&
  'code' in error &&
  (
    error as {
      code?: unknown;
    }
  ).code === '23505';

const exactReplay = (
  existing: ExistingAssetRow[],
  records: PreparedEsimAssetRecord[],
): boolean => {
  if (
    existing.length !==
    records.length
  ) {
    return false;
  }

  const orderedRows =
    [...existing].sort(
      (left, right) =>
        Number(
          left.supplier_detail_id,
        ) -
        Number(
          right.supplier_detail_id,
        ),
    );
  const orderedRecords =
    [...records].sort(
      (left, right) =>
        left.supplierDetailId -
        right.supplierDetailId,
    );

  return orderedRows.every(
    (row, index) => {
      const record =
        orderedRecords[index];

      return (
        row.procurement_request_id ===
          record.procurementRequestId &&
        row.supplier_submission_id ===
          record.supplierSubmissionId &&
        row.supplier_code ===
          record.supplierCode &&
        row.supplier_environment ===
          record.supplierEnvironment &&
        row.supplier_order_id ===
          record.supplierOrderId &&
        Number(
          row.supplier_detail_id,
        ) ===
          record.supplierDetailId &&
        row.provider_request_id ===
          record.providerRequestId &&
        row.plan_id ===
          record.planId &&
        row.data_label ===
          record.dataLabel &&
        row.validity_label ===
          record.validityLabel &&
        row.iccid_fingerprint ===
          record.iccidFingerprint &&
        row.status === 'READY'
      );
    },
  );
};

@Injectable()
export class EsimAssetRepository {
  constructor(
    private readonly database:
      PostgresService,
  ) {}

  async persistBatch(
    records: PreparedEsimAssetRecord[],
  ): Promise<
    PersistEsimAssetBatchResult
  > {
    if (records.length < 1) {
      return {
        kind: 'CONFLICT',
      };
    }

    const procurementRequestId =
      records[0]
        .procurementRequestId;

    try {
      return await this.database
        .transaction(
          async (client) => {
            await client.query(
              `SELECT
                 pg_advisory_xact_lock(
                   hashtextextended(
                     $1::text,
                     0
                   )
                 )`,
              [
                procurementRequestId,
              ],
            );

            const current =
              await client
                .query<ExistingAssetRow>(
                  `SELECT
                     id::text,
                     procurement_request_id::text,
                     supplier_submission_id::text,
                     supplier_code,
                     supplier_environment,
                     supplier_order_id,
                     supplier_detail_id,
                     provider_request_id,
                     plan_id,
                     data_label,
                     validity_label,
                     iccid_fingerprint,
                     status
                   FROM fulfillment.esim_assets
                  WHERE procurement_request_id =
                        $1::uuid
                  ORDER BY
                    supplier_detail_id
                  FOR UPDATE`,
                  [
                    procurementRequestId,
                  ],
                );

            if (
              current.rows.length > 0
            ) {
              if (
                !exactReplay(
                  current.rows,
                  records,
                )
              ) {
                return {
                  kind: 'CONFLICT',
                };
              }

              return {
                kind: 'REPLAY',
                assetIds:
                  current.rows.map(
                    (row) => row.id,
                  ),
                assetCount:
                  current.rows.length,
              };
            }

            const detailIds =
              records.map(
                (record) =>
                  record
                    .supplierDetailId,
              );
            const fingerprints =
              records.map(
                (record) =>
                  record
                    .iccidFingerprint,
              );
            const supplierCode =
              records[0].supplierCode;
            const environment =
              records[0]
                .supplierEnvironment;

            const collisions =
              await client.query(
                `SELECT id
                   FROM
                     fulfillment.esim_assets
                  WHERE (
                    supplier_code =
                      $1::varchar(64)
                    AND
                    supplier_environment =
                      $2::text
                    AND
                    supplier_detail_id =
                      ANY($3::bigint[])
                  )
                  OR (
                    supplier_code =
                      $1::varchar(64)
                    AND
                    supplier_environment =
                      $2::text
                    AND
                    iccid_fingerprint =
                      ANY($4::char(64)[])
                  )
                  FOR UPDATE`,
                [
                  supplierCode,
                  environment,
                  detailIds,
                  fingerprints,
                ],
              );

            if (
              collisions.rows.length > 0
            ) {
              return {
                kind: 'CONFLICT',
              };
            }

            const assetIds: string[] =
              [];

            for (
              const record
              of records
            ) {
              const assetId =
                randomUUID();

              await client.query(
                `INSERT INTO
                   fulfillment.esim_assets (
                     id,
                     procurement_request_id,
                     supplier_submission_id,
                     supplier_code,
                     supplier_environment,
                     supplier_order_id,
                     supplier_detail_id,
                     provider_request_id,
                     plan_id,
                     data_label,
                     validity_label,
                     iccid_fingerprint,
                     encrypted_payload,
                     status,
                     captured_at,
                     created_at,
                     updated_at
                   ) VALUES (
                     $1::uuid,
                     $2::uuid,
                     $3::uuid,
                     $4::varchar(64),
                     $5::text,
                     $6::varchar(80),
                     $7::bigint,
                     $8::varchar(80),
                     $9::varchar(128),
                     $10::varchar(100),
                     $11::varchar(100),
                     $12::char(64),
                     $13::jsonb,
                     'READY',
                     $14::timestamptz,
                     $14::timestamptz,
                     $14::timestamptz
                   )`,
                [
                  assetId,
                  record
                    .procurementRequestId,
                  record
                    .supplierSubmissionId,
                  record.supplierCode,
                  record
                    .supplierEnvironment,
                  record
                    .supplierOrderId,
                  record
                    .supplierDetailId,
                  record
                    .providerRequestId,
                  record.planId,
                  record.dataLabel,
                  record.validityLabel,
                  record
                    .iccidFingerprint,
                  JSON.stringify(
                    record
                      .encryptedPayload,
                  ),
                  record.capturedAt,
                ],
              );

              assetIds.push(assetId);
            }

            return {
              kind: 'CREATED',
              assetIds,
              assetCount:
                assetIds.length,
            };
          },
        );
    } catch (error) {
      if (isUniqueViolation(error)) {
        return {
          kind: 'CONFLICT',
        };
      }
      throw error;
    }
  }
}
