import { randomUUID } from 'node:crypto';

import { Injectable } from '@nestjs/common';
import type {
  GPayCommissioningSessionStatus,
  PricingCurrency,
  SalesOrderPaymentStatus,
  SalesOrderStatus,
} from '@ysim/contracts';
import type { QueryResultRow } from 'pg';

import { PostgresService } from '../../../../platform/database/postgres.service.js';
import type {
  GPayGatewayNormalizedStatus,
} from './gpay.gateway.types.js';

export const VS_R1_043_SLICE_ID = 'VS-R1-043' as const;

interface CandidateRow extends QueryResultRow {
  payment_intent_id: string;
  merchant_order_id: string;
  amount_minor: string;
  currency: PricingCurrency;
  intent_status: string;
  order_status: SalesOrderStatus;
  order_payment_status: SalesOrderPaymentStatus;
  fulfillment_status: string;
}

interface SessionRow extends QueryResultRow {
  slice_id: typeof VS_R1_043_SLICE_ID;
  run_namespace: string;
  payment_intent_id: string;
  merchant_order_id: string;
  actor_identity_id: string;
  amount_minor: string;
  currency: 'VND';
  status: GPayCommissioningSessionStatus;
  init_attempt_count: 1;
  query_attempt_count: number;
  query_cap: number;
  bill_id: string | null;
  bill_url: string | null;
  expired_at: string | Date | null;
  created_at: string | Date;
  updated_at: string | Date;
  version: number;
}

interface EvidenceRow extends QueryResultRow {
  source: 'CALLBACK' | 'QUERY';
  provider_event_id: string;
  evidence_fingerprint: string;
  normalized_status: GPayGatewayNormalizedStatus;
}

export interface PersistedGPayCommissioningSession {
  sliceId: typeof VS_R1_043_SLICE_ID;
  runNamespace: string;
  paymentIntentId: string;
  merchantOrderId: string;
  actorIdentityId: string;
  amountMinor: string;
  currency: 'VND';
  status: GPayCommissioningSessionStatus;
  initAttemptCount: 1;
  queryAttemptCount: number;
  queryCap: number;
  billId?: string;
  billUrl?: string;
  expiredTime?: string;
  createdAt: string;
  updatedAt: string;
  version: number;
}

export type ReserveGPayInitAttemptResult =
  | {
      kind: 'RESERVED';
      session: PersistedGPayCommissioningSession;
    }
  | {
      kind:
        | 'BUDGET_ALREADY_CONSUMED'
        | 'INTENT_NOT_FOUND'
        | 'INTENT_NOT_ELIGIBLE';
    };

export type ReserveGPayQueryResult =
  | {
      kind: 'RESERVED';
      session: PersistedGPayCommissioningSession;
    }
  | {
      kind:
        | 'SESSION_NOT_FOUND'
        | 'SESSION_NOT_INITIALIZED'
        | 'SESSION_TERMINAL'
        | 'QUERY_BUDGET_CONSUMED';
    };

export type RecordGPayEvidenceResult =
  | {
      kind: 'APPLIED' | 'DUPLICATE';
      session: PersistedGPayCommissioningSession;
    }
  | {
      kind:
        | 'SESSION_NOT_FOUND'
        | 'IDENTITY_CONFLICT'
        | 'EVIDENCE_CONFLICT'
        | 'TERMINAL_CONFLICT';
    };

const toIso = (value: string | Date): string =>
  new Date(value).toISOString();

const mapSession = (
  row: SessionRow,
): PersistedGPayCommissioningSession => ({
  sliceId: row.slice_id,
  runNamespace: row.run_namespace,
  paymentIntentId: row.payment_intent_id,
  merchantOrderId: row.merchant_order_id,
  actorIdentityId: row.actor_identity_id,
  amountMinor: row.amount_minor,
  currency: row.currency,
  status: row.status,
  initAttemptCount: row.init_attempt_count,
  queryAttemptCount: row.query_attempt_count,
  queryCap: row.query_cap,
  ...(row.bill_id ? { billId: row.bill_id } : {}),
  ...(row.bill_url ? { billUrl: row.bill_url } : {}),
  ...(row.expired_at ? {
    expiredTime: toIso(row.expired_at),
  } : {}),
  createdAt: toIso(row.created_at),
  updatedAt: toIso(row.updated_at),
  version: row.version,
});

const terminal = (
  status: GPayCommissioningSessionStatus,
): boolean => [
  'SUCCEEDED',
  'FAILED',
  'CANCELLED',
  'EXPIRED',
].includes(status);

const sessionStatus = (
  status: GPayGatewayNormalizedStatus,
): Exclude<
  GPayCommissioningSessionStatus,
  'INIT_ATTEMPTED' | 'INITIALIZED'
> => {
  switch (status) {
    case 'SUCCESS':
      return 'SUCCEEDED';
    case 'FAILED':
      return 'FAILED';
    case 'CANCELLED':
      return 'CANCELLED';
    case 'EXPIRED':
      return 'EXPIRED';
    case 'PENDING':
      return 'PENDING';
  }
};

@Injectable()
export class GPayGatewaySessionRepository {
  constructor(private readonly database: PostgresService) {}

  async reserveInitAttempt(input: {
    paymentIntentId: string;
    runNamespace: string;
    actorIdentityId: string;
    queryCap: number;
    occurredAt: string;
  }): Promise<ReserveGPayInitAttemptResult> {
    return this.database.transaction(async (client) => {
      await client.query(
        `SELECT pg_advisory_xact_lock(
           hashtextextended('VS-R1-043', 0)
         )`,
      );

      const existing = await client.query<SessionRow>(
        `SELECT *
           FROM payment.gpay_commissioning_sessions
          WHERE slice_id = 'VS-R1-043'`,
      );
      if (existing.rows[0]) {
        return { kind: 'BUDGET_ALREADY_CONSUMED' };
      }

      const candidateResult = await client.query<CandidateRow>(
        `SELECT
           pi.id AS payment_intent_id,
           pi.provider_reference AS merchant_order_id,
           pi.amount_minor::text AS amount_minor,
           pi.currency,
           pi.status AS intent_status,
           so.status AS order_status,
           so.payment_status AS order_payment_status,
           so.fulfillment_status
         FROM payment.payment_intents pi
         JOIN sales_order.orders so
           ON so.id = pi.order_id
        WHERE pi.id = $1::uuid
          AND pi.provider = 'GPAY'
        FOR UPDATE OF pi, so`,
        [input.paymentIntentId],
      );
      const candidate = candidateResult.rows[0];
      if (!candidate) {
        return { kind: 'INTENT_NOT_FOUND' };
      }
      if (
        candidate.currency !== 'VND' ||
        !['CREATED', 'PENDING'].includes(
          candidate.intent_status,
        ) ||
        candidate.order_status !== 'PENDING_PAYMENT' ||
        !['UNPAID', 'FAILED'].includes(
          candidate.order_payment_status,
        ) ||
        candidate.fulfillment_status !== 'UNFULFILLED'
      ) {
        return { kind: 'INTENT_NOT_ELIGIBLE' };
      }

      const inserted = await client.query<SessionRow>(
        `INSERT INTO payment.gpay_commissioning_sessions (
           slice_id,
           run_namespace,
           payment_intent_id,
           merchant_order_id,
           actor_identity_id,
           amount_minor,
           currency,
           status,
           init_attempt_count,
           query_attempt_count,
           query_cap,
           created_at,
           updated_at
         ) VALUES (
           'VS-R1-043',
           $1::varchar(80),
           $2::uuid,
           $3::varchar(80),
           $4::uuid,
           $5::numeric(20, 0),
           'VND',
           'INIT_ATTEMPTED',
           1,
           0,
           $6::smallint,
           $7::timestamptz,
           $7::timestamptz
         )
         RETURNING *`,
        [
          input.runNamespace,
          candidate.payment_intent_id,
          candidate.merchant_order_id,
          input.actorIdentityId,
          candidate.amount_minor,
          input.queryCap,
          input.occurredAt,
        ],
      );

      await client.query(
        `INSERT INTO payment.payment_activity (
           id,
           actor_identity_id,
           action,
           subject_type,
           subject_id,
           metadata,
           created_at
         ) VALUES (
           $1::uuid,
           $2::uuid,
           'GPAY_COMMISSIONING_INIT_ATTEMPT_RESERVED',
           'PaymentIntent',
           $3::uuid,
           jsonb_build_object(
             'sliceId', 'VS-R1-043',
             'runNamespace', $4::text,
             'transactionCap', 1
           ),
           $5::timestamptz
         )`,
        [
          randomUUID(),
          input.actorIdentityId,
          input.paymentIntentId,
          input.runNamespace,
          input.occurredAt,
        ],
      );

      return {
        kind: 'RESERVED',
        session: mapSession(inserted.rows[0]),
      };
    });
  }

  async bindInitResult(input: {
    paymentIntentId: string;
    merchantOrderId: string;
    billId: string;
    billUrl: string;
    expiredTime: string;
    occurredAt: string;
  }): Promise<PersistedGPayCommissioningSession | null> {
    const result = await this.database.query<SessionRow>(
      `UPDATE payment.gpay_commissioning_sessions
          SET status = 'INITIALIZED',
              bill_id = $3::varchar(100),
              bill_url = $4::text,
              expired_at = $5::timestamptz,
              updated_at = $6::timestamptz,
              version = version + 1
        WHERE slice_id = 'VS-R1-043'
          AND payment_intent_id = $1::uuid
          AND merchant_order_id = $2::varchar(80)
          AND status = 'INIT_ATTEMPTED'
          AND init_attempt_count = 1
          AND bill_id IS NULL
        RETURNING *`,
      [
        input.paymentIntentId,
        input.merchantOrderId,
        input.billId,
        input.billUrl,
        input.expiredTime,
        input.occurredAt,
      ],
    );
    const row = result.rows[0];
    return row ? mapSession(row) : null;
  }

  async findByProviderIdentity(input: {
    merchantOrderId: string;
    billId: string;
  }): Promise<PersistedGPayCommissioningSession | null> {
    const result = await this.database.query<SessionRow>(
      `SELECT *
         FROM payment.gpay_commissioning_sessions
        WHERE slice_id = 'VS-R1-043'
          AND merchant_order_id = $1::varchar(80)
          AND bill_id = $2::varchar(100)`,
      [input.merchantOrderId, input.billId],
    );
    const row = result.rows[0];
    return row ? mapSession(row) : null;
  }

  async reserveQueryAttempt(
    paymentIntentId: string,
    occurredAt: string,
  ): Promise<ReserveGPayQueryResult> {
    return this.database.transaction(async (client) => {
      await client.query(
        `SELECT pg_advisory_xact_lock(
           hashtextextended('VS-R1-043', 0)
         )`,
      );
      const currentResult = await client.query<SessionRow>(
        `SELECT *
           FROM payment.gpay_commissioning_sessions
          WHERE slice_id = 'VS-R1-043'
            AND payment_intent_id = $1::uuid
          FOR UPDATE`,
        [paymentIntentId],
      );
      const current = currentResult.rows[0];
      if (!current) return { kind: 'SESSION_NOT_FOUND' };
      if (current.status === 'INIT_ATTEMPTED') {
        return { kind: 'SESSION_NOT_INITIALIZED' };
      }
      if (terminal(current.status)) {
        return { kind: 'SESSION_TERMINAL' };
      }
      if (current.query_attempt_count >= current.query_cap) {
        return { kind: 'QUERY_BUDGET_CONSUMED' };
      }

      const updated = await client.query<SessionRow>(
        `UPDATE payment.gpay_commissioning_sessions
            SET query_attempt_count = query_attempt_count + 1,
                updated_at = $2::timestamptz,
                version = version + 1
          WHERE slice_id = 'VS-R1-043'
            AND payment_intent_id = $1::uuid
          RETURNING *`,
        [paymentIntentId, occurredAt],
      );
      return {
        kind: 'RESERVED',
        session: mapSession(updated.rows[0]),
      };
    });
  }

  async recordEvidence(input: {
    merchantOrderId: string;
    billId: string;
    source: 'CALLBACK' | 'QUERY';
    providerEventId: string;
    evidenceFingerprint: string;
    normalizedStatus: GPayGatewayNormalizedStatus;
    occurredAt: string;
  }): Promise<RecordGPayEvidenceResult> {
    return this.database.transaction(async (client) => {
      await client.query(
        `SELECT pg_advisory_xact_lock(
           hashtextextended('VS-R1-043', 0)
         )`,
      );
      const currentResult = await client.query<SessionRow>(
        `SELECT *
           FROM payment.gpay_commissioning_sessions
          WHERE slice_id = 'VS-R1-043'
          FOR UPDATE`,
      );
      const current = currentResult.rows[0];
      if (!current) return { kind: 'SESSION_NOT_FOUND' };
      if (
        current.merchant_order_id !== input.merchantOrderId ||
        current.bill_id !== input.billId
      ) {
        return { kind: 'IDENTITY_CONFLICT' };
      }

      const existingResult = await client.query<EvidenceRow>(
        `SELECT
           source,
           provider_event_id,
           evidence_fingerprint,
           normalized_status
         FROM payment.gpay_commissioning_evidence
        WHERE provider_event_id = $1::varchar(100)
           OR evidence_fingerprint = $2::char(64)`,
        [input.providerEventId, input.evidenceFingerprint],
      );
      const existing = existingResult.rows[0];
      if (existing) {
        if (
          existing.source !== input.source ||
          existing.provider_event_id !== input.providerEventId ||
          existing.evidence_fingerprint !==
            input.evidenceFingerprint ||
          existing.normalized_status !== input.normalizedStatus
        ) {
          return { kind: 'EVIDENCE_CONFLICT' };
        }
        return {
          kind: 'DUPLICATE',
          session: mapSession(current),
        };
      }
      if (terminal(current.status)) {
        return { kind: 'TERMINAL_CONFLICT' };
      }

      await client.query(
        `INSERT INTO payment.gpay_commissioning_evidence (
           id,
           slice_id,
           source,
           provider_event_id,
           evidence_fingerprint,
           normalized_status,
           received_at
         ) VALUES (
           $1::uuid,
           'VS-R1-043',
           $2::varchar(16),
           $3::varchar(100),
           $4::char(64),
           $5::varchar(16),
           $6::timestamptz
         )`,
        [
          randomUUID(),
          input.source,
          input.providerEventId,
          input.evidenceFingerprint,
          input.normalizedStatus,
          input.occurredAt,
        ],
      );

      const updated = await client.query<SessionRow>(
        `UPDATE payment.gpay_commissioning_sessions
            SET status = $1::varchar(24),
                updated_at = $2::timestamptz,
                version = version + 1
          WHERE slice_id = 'VS-R1-043'
          RETURNING *`,
        [sessionStatus(input.normalizedStatus), input.occurredAt],
      );
      return {
        kind: 'APPLIED',
        session: mapSession(updated.rows[0]),
      };
    });
  }
}
