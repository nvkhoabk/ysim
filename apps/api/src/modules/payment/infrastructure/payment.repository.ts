import { randomUUID } from 'node:crypto';

import { Injectable } from '@nestjs/common';
import type {
  PaymentIntentStatus,
  PaymentProvider,
  PricingCurrency,
  SalesOrderPaymentStatus,
  SalesOrderStatus,
  TestPaymentEventStatus,
} from '@ysim/contracts';
import type { PoolClient, QueryResultRow } from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';
import {
  PaymentPolicyError,
  resolvePaymentTransition,
} from '../domain/payment-policy.js';

interface PayableOrderRow extends QueryResultRow {
  id: string;
  order_number: string;
  total_amount_minor: string;
  currency: PricingCurrency;
  status: SalesOrderStatus;
  payment_status: SalesOrderPaymentStatus;
  fulfillment_status: string;
}

interface PaymentIntentRow extends QueryResultRow {
  id: string;
  order_id: string;
  order_number: string;
  provider: PaymentProvider;
  provider_reference: string;
  attempt_number: number;
  amount_minor: string;
  currency: PricingCurrency;
  status: PaymentIntentStatus;
  idempotency_key_hash: string;
  request_fingerprint: string;
  created_at: string | Date;
  expires_at: string | Date;
  updated_at: string | Date;
  version: number;
}

interface ProviderEventRow extends QueryResultRow {
  payment_intent_id: string;
  event_fingerprint: string;
  normalized_status: TestPaymentEventStatus;
}

export interface PersistedPaymentIntent {
  id: string;
  orderId: string;
  orderNumber: string;
  provider: PaymentProvider;
  providerReference: string;
  attemptNumber: number;
  amountMinor: string;
  currency: PricingCurrency;
  status: PaymentIntentStatus;
  createdAt: string;
  expiresAt: string;
  updatedAt: string;
  version: number;
  idempotencyKeyHash: string;
  requestFingerprint: string;
}

export interface CreatePaymentIntentInput {
  proposedIntentId: string;
  orderId: string;
  orderAccessTokenHash: string;
  provider: PaymentProvider;
  providerReference: string;
  idempotencyKeyHash: string;
  requestFingerprint: string;
  createdAt: string;
  expiresAt: string;
}

export type CreatePaymentIntentResult =
  | {
      kind: 'CREATED' | 'REPLAY';
      intent: PersistedPaymentIntent;
    }
  | {
      kind:
        | 'ORDER_NOT_FOUND'
        | 'ORDER_NOT_PAYABLE'
        | 'ACTIVE_INTENT_EXISTS'
        | 'IDEMPOTENCY_CONFLICT';
    };

export interface ApplyPaymentEventInput {
  intentId: string;
  provider: PaymentProvider;
  providerEventId: string;
  eventFingerprint: string;
  normalizedStatus: TestPaymentEventStatus;
  actorIdentityId: string;
  occurredAt: string;
}

export type ApplyPaymentEventResult =
  | {
      kind: 'APPLIED' | 'DUPLICATE';
      intent: PersistedPaymentIntent;
      orderStatus: SalesOrderStatus;
      orderPaymentStatus: SalesOrderPaymentStatus;
    }
  | {
      kind:
        | 'INTENT_NOT_FOUND'
        | 'EVENT_CONFLICT'
        | 'ILLEGAL_TRANSITION';
    };

const toIso = (value: string | Date): string =>
  new Date(value).toISOString();

const mapIntent = (
  row: PaymentIntentRow,
): PersistedPaymentIntent => ({
  id: row.id,
  orderId: row.order_id,
  orderNumber: row.order_number,
  provider: row.provider,
  providerReference: row.provider_reference,
  attemptNumber: row.attempt_number,
  amountMinor: row.amount_minor,
  currency: row.currency,
  status: row.status,
  createdAt: toIso(row.created_at),
  expiresAt: toIso(row.expires_at),
  updatedAt: toIso(row.updated_at),
  version: row.version,
  idempotencyKeyHash: row.idempotency_key_hash,
  requestFingerprint: row.request_fingerprint,
});

@Injectable()
export class PaymentRepository {
  constructor(private readonly database: PostgresService) {}

  async createIntent(
    input: CreatePaymentIntentInput,
  ): Promise<CreatePaymentIntentResult> {
    return this.database.transaction(async (client) => {
      const orderResult = await client.query<PayableOrderRow>(
        `SELECT
           id,
           order_number,
           total_amount_minor::text,
           currency,
           status,
           payment_status,
           fulfillment_status
         FROM sales_order.orders
         WHERE id = $1::uuid
           AND order_access_token_hash = $2::char(64)
         FOR UPDATE`,
        [input.orderId, input.orderAccessTokenHash],
      );
      const order = orderResult.rows[0];

      if (!order) {
        return { kind: 'ORDER_NOT_FOUND' };
      }

      const replayResult = await client.query<PaymentIntentRow>(
        `SELECT pi.*, so.order_number
           FROM payment.payment_intents pi
           JOIN sales_order.orders so
             ON so.id = pi.order_id
          WHERE pi.order_id = $1::uuid
            AND pi.idempotency_key_hash = $2::char(64)`,
        [input.orderId, input.idempotencyKeyHash],
      );
      const replay = replayResult.rows[0];

      if (replay) {
        if (
          replay.request_fingerprint !==
          input.requestFingerprint
        ) {
          return { kind: 'IDEMPOTENCY_CONFLICT' };
        }
        return {
          kind: 'REPLAY',
          intent: mapIntent(replay),
        };
      }

      if (
        order.status !== 'PENDING_PAYMENT' ||
        order.payment_status === 'PAID' ||
        order.payment_status === 'REFUNDED' ||
        order.fulfillment_status !== 'UNFULFILLED'
      ) {
        return { kind: 'ORDER_NOT_PAYABLE' };
      }

      const activeResult = await client.query<QueryResultRow>(
        `SELECT 1
           FROM payment.payment_intents
          WHERE order_id = $1::uuid
            AND status IN ('CREATED', 'PENDING')
          LIMIT 1`,
        [input.orderId],
      );

      if (activeResult.rowCount && activeResult.rowCount > 0) {
        return { kind: 'ACTIVE_INTENT_EXISTS' };
      }

      const attemptResult = await client.query<
        QueryResultRow & { attempt_number: number }
      >(
        `SELECT COALESCE(MAX(attempt_number), 0)::int + 1
           AS attempt_number
           FROM payment.payment_intents
          WHERE order_id = $1::uuid`,
        [input.orderId],
      );
      const attemptNumber =
        attemptResult.rows[0]?.attempt_number ?? 1;

      if (order.payment_status === 'FAILED') {
        await client.query(
          `UPDATE sales_order.orders
              SET payment_status = 'UNPAID',
                  version = version + 1
            WHERE id = $1::uuid`,
          [input.orderId],
        );
      }

      const inserted = await client.query<PaymentIntentRow>(
        `INSERT INTO payment.payment_intents (
           id,
           order_id,
           provider,
           provider_reference,
           attempt_number,
           amount_minor,
           currency,
           status,
           idempotency_key_hash,
           request_fingerprint,
           created_at,
           expires_at,
           updated_at
         ) VALUES (
           $1::uuid,
           $2::uuid,
           $3::text,
           $4::varchar(80),
           $5::integer,
           $6::numeric(20, 0),
           $7::char(3),
           'CREATED',
           $8::char(64),
           $9::char(64),
           $10::timestamptz,
           $11::timestamptz,
           $10::timestamptz
         )
         RETURNING *,
           $12::varchar(40) AS order_number`,
        [
          input.proposedIntentId,
          input.orderId,
          input.provider,
          input.providerReference,
          attemptNumber,
          order.total_amount_minor,
          order.currency,
          input.idempotencyKeyHash,
          input.requestFingerprint,
          input.createdAt,
          input.expiresAt,
          order.order_number,
        ],
      );

      await this.recordPaymentActivity(client, {
        action: 'PAYMENT_INTENT_CREATED',
        subjectId: input.proposedIntentId,
        metadata: {
          orderId: input.orderId,
          orderNumber: order.order_number,
          provider: input.provider,
          attemptNumber,
          amountMinor: order.total_amount_minor,
          currency: order.currency,
        },
      });

      return {
        kind: 'CREATED',
        intent: mapIntent(inserted.rows[0]),
      };
    });
  }

  async findIntent(
    intentId: string,
    orderAccessTokenHash: string,
  ): Promise<PersistedPaymentIntent | null> {
    const result = await this.database.query<PaymentIntentRow>(
      `SELECT pi.*, so.order_number
         FROM payment.payment_intents pi
         JOIN sales_order.orders so
           ON so.id = pi.order_id
        WHERE pi.id = $1::uuid
          AND so.order_access_token_hash = $2::char(64)`,
      [intentId, orderAccessTokenHash],
    );
    const row = result.rows[0];
    return row ? mapIntent(row) : null;
  }

  async applyEvent(
    input: ApplyPaymentEventInput,
  ): Promise<ApplyPaymentEventResult> {
    return this.database.transaction(async (client) => {
      await client.query(
        `SELECT pg_advisory_xact_lock(
           hashtextextended(
             $1::text || ':' || $2::text,
             0
           )
         )`,
        [input.provider, input.providerEventId],
      );

      const intentResult = await client.query<
        PaymentIntentRow & {
          order_status: SalesOrderStatus;
          order_payment_status: SalesOrderPaymentStatus;
        }
      >(
        `SELECT
           pi.*,
           so.order_number,
           so.status AS order_status,
           so.payment_status AS order_payment_status
         FROM payment.payment_intents pi
         JOIN sales_order.orders so
           ON so.id = pi.order_id
        WHERE pi.id = $1::uuid
          AND pi.provider = $2::text
        FOR UPDATE OF pi, so`,
        [input.intentId, input.provider],
      );
      const current = intentResult.rows[0];

      if (!current) {
        return { kind: 'INTENT_NOT_FOUND' };
      }

      const existingEventResult =
        await client.query<ProviderEventRow>(
          `SELECT
             payment_intent_id,
             event_fingerprint,
             normalized_status
           FROM payment.provider_events
          WHERE provider = $1::text
            AND provider_event_id = $2::varchar(100)`,
          [input.provider, input.providerEventId],
        );
      const existingEvent = existingEventResult.rows[0];

      if (existingEvent) {
        if (
          existingEvent.payment_intent_id !== input.intentId ||
          existingEvent.event_fingerprint !==
            input.eventFingerprint ||
          existingEvent.normalized_status !==
            input.normalizedStatus
        ) {
          return { kind: 'EVENT_CONFLICT' };
        }

        return {
          kind: 'DUPLICATE',
          intent: mapIntent(current),
          orderStatus: current.order_status,
          orderPaymentStatus:
            current.order_payment_status,
        };
      }

      let nextStatus: PaymentIntentStatus;
      try {
        nextStatus = resolvePaymentTransition(
          current.status,
          input.normalizedStatus,
        );
      } catch (error) {
        if (error instanceof PaymentPolicyError) {
          return { kind: 'ILLEGAL_TRANSITION' };
        }
        throw error;
      }

      if (
        nextStatus === 'SUCCEEDED' &&
        (
          current.order_status !== 'PENDING_PAYMENT' ||
          (
            current.order_payment_status !== 'UNPAID' &&
            current.order_payment_status !== 'FAILED'
          )
        )
      ) {
        return { kind: 'ILLEGAL_TRANSITION' };
      }

      await client.query(
        `INSERT INTO payment.provider_events (
           id,
           provider,
           provider_event_id,
           payment_intent_id,
           normalized_status,
           event_fingerprint,
           received_at,
           processed_at
         ) VALUES (
           $1::uuid,
           $2::text,
           $3::varchar(100),
           $4::uuid,
           $5::text,
           $6::char(64),
           $7::timestamptz,
           $7::timestamptz
         )`,
        [
          randomUUID(),
          input.provider,
          input.providerEventId,
          input.intentId,
          input.normalizedStatus,
          input.eventFingerprint,
          input.occurredAt,
        ],
      );

      let updatedIntent: PaymentIntentRow = current;
      if (nextStatus !== current.status) {
        const updateResult = await client.query<PaymentIntentRow>(
          `UPDATE payment.payment_intents
              SET status = $2::text,
                  updated_at = $3::timestamptz,
                  version = version + 1
            WHERE id = $1::uuid
            RETURNING *,
              $4::varchar(40) AS order_number`,
          [
            input.intentId,
            nextStatus,
            input.occurredAt,
            current.order_number,
          ],
        );
        updatedIntent = updateResult.rows[0];
      }

      let orderStatus = current.order_status;
      let orderPaymentStatus =
        current.order_payment_status;

      if (nextStatus === 'PENDING') {
        const orderUpdate = await client.query<PayableOrderRow>(
          `UPDATE sales_order.orders
              SET payment_status = 'UNPAID',
                  version = version + 1
            WHERE id = $1::uuid
              AND status = 'PENDING_PAYMENT'
              AND payment_status = 'FAILED'
            RETURNING
              id,
              order_number,
              total_amount_minor::text,
              currency,
              status,
              payment_status,
              fulfillment_status`,
          [current.order_id],
        );
        if (orderUpdate.rows[0]) {
          orderStatus = orderUpdate.rows[0].status;
          orderPaymentStatus =
            orderUpdate.rows[0].payment_status;
        }
      }

      if (nextStatus === 'FAILED') {
        const orderUpdate = await client.query<PayableOrderRow>(
          `UPDATE sales_order.orders
              SET payment_status = 'FAILED',
                  version = version + 1
            WHERE id = $1::uuid
              AND status = 'PENDING_PAYMENT'
              AND payment_status = 'UNPAID'
            RETURNING
              id,
              order_number,
              total_amount_minor::text,
              currency,
              status,
              payment_status,
              fulfillment_status`,
          [current.order_id],
        );
        if (orderUpdate.rows[0]) {
          orderStatus = orderUpdate.rows[0].status;
          orderPaymentStatus =
            orderUpdate.rows[0].payment_status;
        }
      }

      if (nextStatus === 'SUCCEEDED') {
        const orderUpdate = await client.query<PayableOrderRow>(
          `UPDATE sales_order.orders
              SET status = 'CONFIRMED',
                  payment_status = 'PAID',
                  version = version + 1
            WHERE id = $1::uuid
              AND status = 'PENDING_PAYMENT'
              AND payment_status IN ('UNPAID', 'FAILED')
            RETURNING
              id,
              order_number,
              total_amount_minor::text,
              currency,
              status,
              payment_status,
              fulfillment_status`,
          [current.order_id],
        );
        const paidOrder = orderUpdate.rows[0];
        if (!paidOrder) {
          throw new Error(
            'PAYMENT_ORDER_PROJECTION_CONFLICT',
          );
        }
        orderStatus = paidOrder.status;
        orderPaymentStatus = paidOrder.payment_status;

        await this.recordOrderActivity(client, {
          actorIdentityId: input.actorIdentityId,
          action: 'PAYMENT_SUCCEEDED',
          subjectId: current.order_id,
          metadata: {
            paymentIntentId: input.intentId,
            provider: input.provider,
            providerReference:
              current.provider_reference,
            amountMinor: current.amount_minor,
            currency: current.currency,
          },
        });
      }

      await this.recordPaymentActivity(client, {
        actorIdentityId: input.actorIdentityId,
        action: `PAYMENT_EVENT_${input.normalizedStatus}`,
        subjectId: input.intentId,
        metadata: {
          provider: input.provider,
          providerEventId: input.providerEventId,
          previousStatus: current.status,
          nextStatus,
          orderId: current.order_id,
        },
      });

      return {
        kind: 'APPLIED',
        intent: mapIntent(updatedIntent),
        orderStatus,
        orderPaymentStatus,
      };
    });
  }

  private async recordPaymentActivity(
    client: PoolClient,
    input: {
      actorIdentityId?: string;
      action: string;
      subjectId: string;
      metadata: Record<string, unknown>;
    },
  ): Promise<void> {
    await client.query(
      `INSERT INTO payment.payment_activity (
         id,
         actor_identity_id,
         action,
         subject_type,
         subject_id,
         metadata
       ) VALUES (
         $1::uuid,
         $2::uuid,
         $3::varchar(100),
         'PaymentIntent',
         $4::uuid,
         $5::jsonb
       )`,
      [
        randomUUID(),
        input.actorIdentityId ?? null,
        input.action,
        input.subjectId,
        JSON.stringify(input.metadata),
      ],
    );
  }

  private async recordOrderActivity(
    client: PoolClient,
    input: {
      actorIdentityId?: string;
      action: string;
      subjectId: string;
      metadata: Record<string, unknown>;
    },
  ): Promise<void> {
    await client.query(
      `INSERT INTO sales_order.order_activity (
         id,
         actor_identity_id,
         action,
         subject_type,
         subject_id,
         metadata
       ) VALUES (
         $1::uuid,
         $2::uuid,
         $3::varchar(100),
         'SalesOrder',
         $4::uuid,
         $5::jsonb
       )`,
      [
        randomUUID(),
        input.actorIdentityId ?? null,
        input.action,
        input.subjectId,
        JSON.stringify(input.metadata),
      ],
    );
  }
}
