import { randomUUID } from 'node:crypto';

import { Injectable } from '@nestjs/common';
import type { QueryResultRow } from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';
import type {
  CreateProcurementRequestInput,
} from '../domain/procurement-request-policy.js';

interface ProcurementRequestRow extends QueryResultRow {
  id: string;
  source_event_id: string;
  payment_intent_id: string;
  order_id: string;
  request_fingerprint: string;
  status: string;
}

export type CreateProcurementRequestResult =
  | {
      kind: 'CREATED' | 'REPLAY';
      requestId: string;
      status: 'PENDING_SUPPLIER';
    }
  | {
      kind: 'CONFLICT';
    };

@Injectable()
export class ProcurementRequestRepository {
  constructor(
    private readonly database: PostgresService,
  ) {}

  async createFromPaymentSuccess(
    input: CreateProcurementRequestInput,
  ): Promise<CreateProcurementRequestResult> {
    return this.database.transaction(
      async (client) => {
        await client.query(
          `SELECT pg_advisory_xact_lock(
             hashtextextended($1::text, 0)
           )`,
          [input.orderId],
        );

        const existing =
          await client.query<ProcurementRequestRow>(
            `SELECT
               id::text,
               source_event_id::text,
               payment_intent_id::text,
               order_id::text,
               request_fingerprint,
               status
             FROM procurement.requests
            WHERE source_event_id = $1::uuid
               OR payment_intent_id = $2::uuid
               OR order_id = $3::uuid
            FOR UPDATE`,
            [
              input.sourceEventId,
              input.paymentIntentId,
              input.orderId,
            ],
          );

        const current = existing.rows[0];
        if (current) {
          if (
            current.source_event_id ===
              input.sourceEventId &&
            current.payment_intent_id ===
              input.paymentIntentId &&
            current.order_id ===
              input.orderId &&
            current.request_fingerprint ===
              input.requestFingerprint &&
            current.status ===
              'PENDING_SUPPLIER'
          ) {
            return {
              kind: 'REPLAY',
              requestId: current.id,
              status: 'PENDING_SUPPLIER',
            };
          }
          return { kind: 'CONFLICT' };
        }

        const requestId = randomUUID();
        await client.query(
          `INSERT INTO procurement.requests (
             id,
             source_event_id,
             payment_intent_id,
             order_id,
             order_number,
             product_offer_id,
             supplier_plan_mapping_id,
             supplier_environment_id,
             supplier_plan_id,
             supplier_code,
             supplier_environment,
             external_plan_id,
             quantity,
             status,
             request_fingerprint,
             created_at,
             updated_at
           ) VALUES (
             $1::uuid,
             $2::uuid,
             $3::uuid,
             $4::uuid,
             $5::varchar(40),
             $6::uuid,
             $7::uuid,
             $8::uuid,
             $9::uuid,
             $10::varchar(64),
             $11::text,
             $12::varchar(128),
             $13::integer,
             $14::text,
             $15::char(64),
             $16::timestamptz,
             $16::timestamptz
           )`,
          [
            requestId,
            input.sourceEventId,
            input.paymentIntentId,
            input.orderId,
            input.orderNumber,
            input.productOfferId,
            input.supplierPlanMappingId,
            input.supplierEnvironmentId,
            input.supplierPlanId,
            input.supplierCode,
            input.supplierEnvironment,
            input.externalPlanId,
            input.quantity,
            input.status,
            input.requestFingerprint,
            input.createdAt,
          ],
        );

        return {
          kind: 'CREATED',
          requestId,
          status: 'PENDING_SUPPLIER',
        };
      },
    );
  }
}
