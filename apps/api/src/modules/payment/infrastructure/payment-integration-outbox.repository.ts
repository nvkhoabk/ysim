import { Injectable } from '@nestjs/common';
import type { QueryResultRow } from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';
import type {
  ClaimedPaymentIntegrationOutboxRecord,
} from '../domain/payment-outbox-policy.js';

interface PaymentOutboxRow extends QueryResultRow {
  id: string;
  event_type: string;
  aggregate_type: string;
  aggregate_id: string;
  order_id: string;
  deduplication_key: string;
  payload: unknown;
  occurred_at: string | Date;
  attempt_count: number;
}

const toIso = (
  value: string | Date,
): string => new Date(value).toISOString();

const mapRow = (
  row: PaymentOutboxRow,
): ClaimedPaymentIntegrationOutboxRecord => ({
  id: row.id,
  eventType: row.event_type,
  aggregateType: row.aggregate_type,
  aggregateId: row.aggregate_id,
  orderId: row.order_id,
  deduplicationKey:
    row.deduplication_key,
  payload: row.payload,
  occurredAt: toIso(row.occurred_at),
  attemptCount: row.attempt_count,
});

@Injectable()
export class PaymentIntegrationOutboxRepository {
  constructor(
    private readonly database: PostgresService,
  ) {}

  async claimNext(input: {
    now: string;
    leaseUntil: string;
  }): Promise<
    ClaimedPaymentIntegrationOutboxRecord | null
  > {
    return this.database.transaction(
      async (client) => {
        const selected =
          await client.query<PaymentOutboxRow>(
            `SELECT
               id,
               event_type,
               aggregate_type,
               aggregate_id::text,
               order_id::text,
               deduplication_key,
               payload,
               occurred_at,
               attempt_count
             FROM payment.integration_outbox
             WHERE published_at IS NULL
               AND available_at <= $1::timestamptz
             ORDER BY available_at, occurred_at, id
             FOR UPDATE SKIP LOCKED
             LIMIT 1`,
            [input.now],
          );

        const row = selected.rows[0];
        if (!row) return null;

        const claimed =
          await client.query<PaymentOutboxRow>(
            `UPDATE payment.integration_outbox
                SET attempt_count = attempt_count + 1,
                    available_at = $2::timestamptz,
                    last_error = NULL
              WHERE id = $1::uuid
                AND published_at IS NULL
              RETURNING
                id,
                event_type,
                aggregate_type,
                aggregate_id::text,
                order_id::text,
                deduplication_key,
                payload,
                occurred_at,
                attempt_count`,
            [
              row.id,
              input.leaseUntil,
            ],
          );

        const claimedRow = claimed.rows[0];
        if (!claimedRow) {
          throw new Error(
            'PAYMENT_OUTBOX_CLAIM_CONFLICT',
          );
        }
        return mapRow(claimedRow);
      },
    );
  }

  async markPublished(input: {
    eventId: string;
    attemptCount: number;
    publishedAt: string;
  }): Promise<boolean> {
    const result = await this.database.query(
      `UPDATE payment.integration_outbox
          SET published_at = $3::timestamptz,
              available_at = $3::timestamptz,
              last_error = NULL
        WHERE id = $1::uuid
          AND attempt_count = $2::integer
          AND published_at IS NULL`,
      [
        input.eventId,
        input.attemptCount,
        input.publishedAt,
      ],
    );
    return result.rowCount === 1;
  }

  async markFailed(input: {
    eventId: string;
    attemptCount: number;
    retryAt: string;
    lastError: string;
  }): Promise<boolean> {
    const result = await this.database.query(
      `UPDATE payment.integration_outbox
          SET available_at = $3::timestamptz,
              last_error = $4::text
        WHERE id = $1::uuid
          AND attempt_count = $2::integer
          AND published_at IS NULL`,
      [
        input.eventId,
        input.attemptCount,
        input.retryAt,
        input.lastError,
      ],
    );
    return result.rowCount === 1;
  }
}
