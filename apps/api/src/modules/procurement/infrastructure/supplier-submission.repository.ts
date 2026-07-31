import { randomUUID } from 'node:crypto';

import { Injectable } from '@nestjs/common';
import type {
  PoolClient,
  QueryResultRow,
} from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';

interface SupplierSubmissionRow
  extends QueryResultRow {
  id: string;
  procurement_request_id: string;
  provider_request_id: string;
  request_payload_hash: string;
  status: string;
  attempt_count: number;
  lease_until: string | Date | null;
  next_retry_at: string | Date;
  provider_order_id:
    number | string | null;
  provider_code: string | null;
  provider_status: number | null;
  provider_order_status: string | null;
}

export type ClaimSupplierSubmissionResult =
  | {
      kind: 'CLAIMED';
      submissionId: string;
      attemptCount: number;
    }
  | {
      kind: 'REPLAY';
      submissionId: string;
      attemptCount: number;
      providerRequestId: string;
      providerOrderId: number;
      providerCode: string;
      providerStatus: number;
      providerOrderStatus: string;
    }
  | {
      kind: 'BUSY';
      availableAt: string;
    }
  | {
      kind: 'CONFLICT';
    };

const toIso = (
  value: string | Date,
): string =>
  new Date(value).toISOString();

const replay = (
  row: SupplierSubmissionRow,
): ClaimSupplierSubmissionResult => {
  if (
    row.provider_order_id === null ||
    row.provider_code === null ||
    row.provider_status === null ||
    row.provider_order_status === null
  ) {
    return { kind: 'CONFLICT' };
  }

  return {
    kind: 'REPLAY',
    submissionId: row.id,
    attemptCount: row.attempt_count,
    providerRequestId:
      row.provider_request_id,
    providerOrderId:
      Number(row.provider_order_id),
    providerCode: row.provider_code,
    providerStatus:
      row.provider_status,
    providerOrderStatus:
      row.provider_order_status,
  };
};

@Injectable()
export class SupplierSubmissionRepository {
  constructor(
    private readonly database:
      PostgresService,
  ) {}

  async claim(input: {
    procurementRequestId: string;
    supplierCode: 'GIGAGO';
    supplierEnvironment: 'SANDBOX';
    providerRequestId: string;
    requestPayloadHash: string;
    claimedAt: string;
    leaseUntil: string;
  }): Promise<
    ClaimSupplierSubmissionResult
  > {
    return this.database.transaction(
      async (client) => {
        await client.query(
          `SELECT pg_advisory_xact_lock(
             hashtextextended($1::text, 0)
           )`,
          [input.procurementRequestId],
        );

        const request =
          await client.query<{
            status: string;
          } & QueryResultRow>(
            `SELECT status
               FROM procurement.requests
              WHERE id = $1::uuid
              FOR UPDATE`,
            [input.procurementRequestId],
          );

        const requestStatus =
          request.rows[0]?.status;
        if (!requestStatus) {
          return { kind: 'CONFLICT' };
        }

        const existing =
          await client
            .query<SupplierSubmissionRow>(
              `SELECT
                 id::text,
                 procurement_request_id::text,
                 provider_request_id,
                 request_payload_hash,
                 status,
                 attempt_count,
                 lease_until,
                 next_retry_at,
                 provider_order_id,
                 provider_code::text,
                 provider_status,
                 provider_order_status
               FROM procurement.supplier_submissions
              WHERE procurement_request_id =
                    $1::uuid
              FOR UPDATE`,
              [
                input
                  .procurementRequestId,
              ],
            );

        const row = existing.rows[0];

        if (requestStatus === 'SUBMITTED') {
          return row
            ? replay(row)
            : { kind: 'CONFLICT' };
        }
        if (
          requestStatus !==
            'PENDING_SUPPLIER'
        ) {
          return { kind: 'CONFLICT' };
        }

        if (!row) {
          const submissionId =
            randomUUID();
          await client.query(
            `INSERT INTO
               procurement.supplier_submissions (
                 id,
                 procurement_request_id,
                 supplier_code,
                 supplier_environment,
                 provider_request_id,
                 request_payload_hash,
                 status,
                 attempt_count,
                 lease_until,
                 next_retry_at,
                 created_at,
                 updated_at
               ) VALUES (
                 $1::uuid,
                 $2::uuid,
                 $3::varchar(64),
                 $4::text,
                 $5::varchar(64),
                 $6::char(64),
                 'IN_PROGRESS',
                 1,
                 $7::timestamptz,
                 $8::timestamptz,
                 $8::timestamptz,
                 $8::timestamptz
               )`,
            [
              submissionId,
              input
                .procurementRequestId,
              input.supplierCode,
              input
                .supplierEnvironment,
              input.providerRequestId,
              input
                .requestPayloadHash,
              input.leaseUntil,
              input.claimedAt,
            ],
          );

          return {
            kind: 'CLAIMED',
            submissionId,
            attemptCount: 1,
          };
        }

        if (
          row.provider_request_id !==
            input.providerRequestId ||
          row.request_payload_hash !==
            input.requestPayloadHash
        ) {
          return { kind: 'CONFLICT' };
        }

        if (row.status === 'SUBMITTED') {
          return replay(row);
        }

        const now =
          Date.parse(input.claimedAt);
        const availableAt =
          row.status === 'IN_PROGRESS'
            ? row.lease_until
            : row.next_retry_at;

        if (
          availableAt !== null &&
          Date.parse(
            toIso(availableAt),
          ) > now
        ) {
          return {
            kind: 'BUSY',
            availableAt:
              toIso(availableAt),
          };
        }

        const attemptCount =
          row.attempt_count + 1;
        const updated =
          await client.query(
            `UPDATE
               procurement.supplier_submissions
                SET status = 'IN_PROGRESS',
                    attempt_count =
                      $2::integer,
                    lease_until =
                      $3::timestamptz,
                    next_retry_at =
                      $4::timestamptz,
                    last_error = NULL,
                    updated_at =
                      $4::timestamptz,
                    version = version + 1
              WHERE id = $1::uuid
                AND attempt_count =
                    $5::integer`,
            [
              row.id,
              attemptCount,
              input.leaseUntil,
              input.claimedAt,
              row.attempt_count,
            ],
          );

        if (updated.rowCount !== 1) {
          return { kind: 'CONFLICT' };
        }

        return {
          kind: 'CLAIMED',
          submissionId: row.id,
          attemptCount,
        };
      },
    );
  }

  async markSubmitted(input: {
    procurementRequestId: string;
    submissionId: string;
    attemptCount: number;
    providerOrderId: number;
    providerCode: string;
    providerStatus: number;
    providerOrderStatus: string;
    submittedAt: string;
  }): Promise<boolean> {
    return this.database.transaction(
      async (client) => {
        const updated =
          await client.query(
            `UPDATE
               procurement.supplier_submissions
                SET status = 'SUBMITTED',
                    provider_order_id =
                      $4::bigint,
                    provider_code =
                      $5::uuid,
                    provider_status =
                      $6::integer,
                    provider_order_status =
                      $7::varchar(80),
                    lease_until = NULL,
                    last_error = NULL,
                    submitted_at =
                      $8::timestamptz,
                    updated_at =
                      $8::timestamptz,
                    version = version + 1
              WHERE id = $1::uuid
                AND procurement_request_id =
                    $2::uuid
                AND attempt_count =
                    $3::integer
                AND status = 'IN_PROGRESS'`,
            [
              input.submissionId,
              input.procurementRequestId,
              input.attemptCount,
              input.providerOrderId,
              input.providerCode,
              input.providerStatus,
              input.providerOrderStatus,
              input.submittedAt,
            ],
          );

        if (updated.rowCount !== 1) {
          return false;
        }

        const requestUpdated =
          await client.query(
            `UPDATE procurement.requests
                SET status = 'SUBMITTED',
                    updated_at =
                      $2::timestamptz,
                    version = version + 1
              WHERE id = $1::uuid
                AND status =
                    'PENDING_SUPPLIER'`,
            [
              input.procurementRequestId,
              input.submittedAt,
            ],
          );

        if (
          requestUpdated.rowCount !== 1
        ) {
          throw new Error(
            'PROCUREMENT_SUBMISSION_STATUS_CONFLICT',
          );
        }
        return true;
      },
    );
  }

  async markFailed(input: {
    submissionId: string;
    attemptCount: number;
    failedAt: string;
    retryAt: string;
    lastError: string;
  }): Promise<boolean> {
    const result =
      await this.database.query(
        `UPDATE
           procurement.supplier_submissions
            SET status = 'FAILED',
                lease_until = NULL,
                next_retry_at =
                  $3::timestamptz,
                last_error =
                  $4::varchar(500),
                updated_at =
                  $5::timestamptz,
                version = version + 1
          WHERE id = $1::uuid
            AND attempt_count =
                $2::integer
            AND status = 'IN_PROGRESS'`,
        [
          input.submissionId,
          input.attemptCount,
          input.retryAt,
          input.lastError,
          input.failedAt,
        ],
      );

    return result.rowCount === 1;
  }
}
