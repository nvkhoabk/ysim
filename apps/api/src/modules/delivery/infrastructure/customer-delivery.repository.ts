import { randomUUID } from 'node:crypto';

import { Injectable } from '@nestjs/common';
import type {
  QueryResultRow,
} from 'pg';

import {
  PostgresService,
} from '../../../platform/database/postgres.service.js';
import {
  bindDeliveryRequestId,
  type NormalizedCustomerDeliveryRequest,
} from '../domain/customer-delivery-policy.js';

interface ExistingRequestRow
  extends QueryResultRow {
  id: string;
  sales_order_id: string;
  order_number: string;
  channel: string;
  locale: string;
  delivery_version: number;
  expected_asset_count: number;
  asset_set_hash: string;
  status: string;
}

interface ExistingAssetRow
  extends QueryResultRow {
  asset_id: string;
  position: number;
}

interface ExistingOutboxRow
  extends QueryResultRow {
  id: string;
  deduplication_key: string;
  status: string;
}

export type PersistCustomerDeliveryResult =
  | {
      kind: 'CREATED';
      deliveryRequestId: string;
      outboxId: string;
      assetCount: number;
      requestStatus: 'READY';
      outboxStatus: 'PENDING';
    }
  | {
      kind: 'REPLAY';
      deliveryRequestId: string;
      outboxId: string;
      assetCount: number;
      requestStatus: 'READY';
      outboxStatus:
        | 'PENDING'
        | 'PUBLISHED'
        | 'FAILED';
    }
  | {
      kind: 'CONFLICT';
    };

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
  request: ExistingRequestRow,
  assets: ExistingAssetRow[],
  outbox: ExistingOutboxRow | undefined,
  input: NormalizedCustomerDeliveryRequest,
): boolean => {
  if (
    request.sales_order_id !==
      input.salesOrderId ||
    request.order_number !==
      input.orderNumber ||
    request.channel !==
      input.channel ||
    request.locale !==
      input.locale ||
    request.delivery_version !==
      input.deliveryVersion ||
    request.expected_asset_count !==
      input.expectedAssetCount ||
    request.asset_set_hash !==
      input.assetSetHash ||
    request.status !== 'READY' ||
    outbox === undefined ||
    outbox.deduplication_key !==
      input.deduplicationKey
  ) {
    return false;
  }

  const orderedAssets =
    [...assets].sort(
      (left, right) =>
        left.position -
        right.position,
    );

  if (
    orderedAssets.length !==
    input.assetIds.length
  ) {
    return false;
  }

  return orderedAssets.every(
    (row, index) =>
      row.position ===
        index + 1 &&
      row.asset_id ===
        input.assetIds[index],
  );
};

@Injectable()
export class CustomerDeliveryRepository {
  constructor(
    private readonly database:
      PostgresService,
  ) {}

  async persist(
    input:
      NormalizedCustomerDeliveryRequest,
  ): Promise<
    PersistCustomerDeliveryResult
  > {
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
                input.salesOrderId,
              ],
            );

            const existing =
              await client
                .query<ExistingRequestRow>(
                  `SELECT
                     id::text,
                     sales_order_id::text,
                     order_number,
                     channel,
                     locale,
                     delivery_version,
                     expected_asset_count,
                     asset_set_hash,
                     status
                   FROM
                     delivery.customer_delivery_requests
                  WHERE sales_order_id =
                        $1::uuid
                    AND channel =
                        $2::text
                    AND delivery_version =
                        $3::integer
                  FOR UPDATE`,
                  [
                    input.salesOrderId,
                    input.channel,
                    input.deliveryVersion,
                  ],
                );

            const current =
              existing.rows[0];

            if (current) {
              const assets =
                await client
                  .query<ExistingAssetRow>(
                    `SELECT
                       asset_id::text,
                       position
                     FROM
                       delivery.customer_delivery_assets
                    WHERE delivery_request_id =
                          $1::uuid
                    ORDER BY position
                    FOR UPDATE`,
                    [current.id],
                  );
              const outbox =
                await client
                  .query<ExistingOutboxRow>(
                    `SELECT
                       id::text,
                       deduplication_key,
                       status
                     FROM
                       delivery.integration_outbox
                    WHERE delivery_request_id =
                          $1::uuid
                    FOR UPDATE`,
                    [current.id],
                  );
              const outboxRow =
                outbox.rows[0];

              if (
                !exactReplay(
                  current,
                  assets.rows,
                  outboxRow,
                  input,
                )
              ) {
                return {
                  kind: 'CONFLICT',
                };
              }

              return {
                kind: 'REPLAY',
                deliveryRequestId:
                  current.id,
                outboxId:
                  outboxRow.id,
                assetCount:
                  assets.rows.length,
                requestStatus:
                  'READY',
                outboxStatus:
                  outboxRow.status as
                    | 'PENDING'
                    | 'PUBLISHED'
                    | 'FAILED',
              };
            }

            const deliveryRequestId =
              randomUUID();
            const outboxId =
              randomUUID();

            await client.query(
              `INSERT INTO
                 delivery.customer_delivery_requests (
                   id,
                   sales_order_id,
                   order_number,
                   channel,
                   locale,
                   delivery_version,
                   expected_asset_count,
                   asset_set_hash,
                   status,
                   requested_at,
                   created_at,
                   updated_at
                 ) VALUES (
                   $1::uuid,
                   $2::uuid,
                   $3::varchar(64),
                   $4::text,
                   $5::text,
                   $6::integer,
                   $7::integer,
                   $8::char(64),
                   'READY',
                   $9::timestamptz,
                   $9::timestamptz,
                   $9::timestamptz
                 )`,
              [
                deliveryRequestId,
                input.salesOrderId,
                input.orderNumber,
                input.channel,
                input.locale,
                input.deliveryVersion,
                input.expectedAssetCount,
                input.assetSetHash,
                input.requestedAt,
              ],
            );

            for (
              const [
                index,
                assetId,
              ]
              of input.assetIds.entries()
            ) {
              await client.query(
                `INSERT INTO
                   delivery.customer_delivery_assets (
                     delivery_request_id,
                     asset_id,
                     position,
                     created_at
                   ) VALUES (
                     $1::uuid,
                     $2::uuid,
                     $3::integer,
                     $4::timestamptz
                   )`,
                [
                  deliveryRequestId,
                  assetId,
                  index + 1,
                  input.requestedAt,
                ],
              );
            }

            const payload =
              bindDeliveryRequestId(
                deliveryRequestId,
                input.outboxPayload,
              );

            await client.query(
              `INSERT INTO
                 delivery.integration_outbox (
                   id,
                   delivery_request_id,
                   event_type,
                   deduplication_key,
                   payload,
                   status,
                   available_at,
                   created_at,
                   updated_at
                 ) VALUES (
                   $1::uuid,
                   $2::uuid,
                   'delivery.customer_esim_requested.v1',
                   $3::char(64),
                   $4::jsonb,
                   'PENDING',
                   $5::timestamptz,
                   $5::timestamptz,
                   $5::timestamptz
                 )`,
              [
                outboxId,
                deliveryRequestId,
                input.deduplicationKey,
                JSON.stringify(payload),
                input.requestedAt,
              ],
            );

            return {
              kind: 'CREATED',
              deliveryRequestId,
              outboxId,
              assetCount:
                input.assetIds.length,
              requestStatus:
                'READY',
              outboxStatus:
                'PENDING',
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
