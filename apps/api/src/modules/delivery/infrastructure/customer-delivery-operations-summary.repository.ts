import { Injectable } from '@nestjs/common';
import type { QueryResultRow } from 'pg';
import { PostgresService } from '../../../platform/database/postgres.service.js';

export interface CustomerDeliveryOperationsCounts {
  pending: number;
  failed: number;
  published: number;
  inFlight: number;
  actionable: number;
  oldestActionableAt: string | null;
}

interface OperationsCountsRow extends QueryResultRow {
  pending: number;
  failed: number;
  published: number;
  inFlight: number;
  actionable: number;
  oldestActionableAt: Date | string | null;
}

@Injectable()
export class CustomerDeliveryOperationsSummaryRepository {
  constructor(private readonly database: PostgresService) {}

  async load(now: Date): Promise<CustomerDeliveryOperationsCounts> {
    const result = await this.database.query<OperationsCountsRow>(
      `SELECT
         count(*) FILTER (WHERE status = 'PENDING')::integer AS "pending",
         count(*) FILTER (WHERE status = 'FAILED')::integer AS "failed",
         count(*) FILTER (WHERE status = 'PUBLISHED')::integer AS "published",
         count(*) FILTER (
           WHERE status IN ('PENDING', 'FAILED') AND lease_until > $1::timestamptz
         )::integer AS "inFlight",
         count(*) FILTER (
           WHERE status IN ('PENDING', 'FAILED')
             AND available_at <= $1::timestamptz
             AND (lease_until IS NULL OR lease_until <= $1::timestamptz)
         )::integer AS "actionable",
         min(available_at) FILTER (
           WHERE status IN ('PENDING', 'FAILED')
             AND available_at <= $1::timestamptz
             AND (lease_until IS NULL OR lease_until <= $1::timestamptz)
         ) AS "oldestActionableAt"
       FROM delivery.integration_outbox`,
      [now.toISOString()],
    );
    const row = result.rows[0];
    if (!row) throw new Error('Delivery operations summary row is unavailable');
    return {
      pending: row.pending,
      failed: row.failed,
      published: row.published,
      inFlight: row.inFlight,
      actionable: row.actionable,
      oldestActionableAt:
        row.oldestActionableAt === null
          ? null
          : new Date(row.oldestActionableAt).toISOString(),
    };
  }
}
