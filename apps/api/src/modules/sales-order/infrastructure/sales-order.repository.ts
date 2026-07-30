import { randomUUID } from 'node:crypto';

import { Injectable } from '@nestjs/common';
import type {
  PricingChannel,
  PricingCurrency,
  PricingMarket,
  SalesOrderContract,
  SalesOrderFulfillmentStatus,
  SalesOrderLocale,
  SalesOrderPaymentStatus,
  SalesOrderSource,
  SalesOrderStatus,
} from '@ysim/contracts';
import type {
  PoolClient,
  QueryResultRow,
} from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';

interface PricingQuoteRow extends QueryResultRow {
  id: string;
  product_offer_id: string;
  offer_code: string;
  market: PricingMarket;
  currency: PricingCurrency;
  channel: PricingChannel;
  unit_amount_minor: string;
  quantity: number;
  subtotal_amount_minor: string;
  total_amount_minor: string;
  price_book_code: string;
  price_book_version: number;
  price_book_entry_version: number;
  issued_at: string | Date;
  expires_at: string | Date;
}

interface SalesOrderRow extends QueryResultRow {
  id: string;
  order_number: string;
  pricing_quote_id: string;
  offer_code: string;
  market: PricingMarket;
  currency: PricingCurrency;
  channel: PricingChannel;
  unit_amount_minor: string;
  quantity: number;
  subtotal_amount_minor: string;
  total_amount_minor: string;
  status: SalesOrderStatus;
  payment_status: SalesOrderPaymentStatus;
  fulfillment_status: SalesOrderFulfillmentStatus;
  source: SalesOrderSource;
  customer_name: string;
  customer_email: string;
  recipient_email: string;
  locale: SalesOrderLocale;
  quote_issued_at: string | Date;
  quote_expires_at: string | Date;
  idempotency_key_hash: string;
  request_fingerprint: string;
  order_access_token_hash: string;
  created_at: string | Date;
  version: number;
}

export type PersistedSalesOrder = Omit<
  SalesOrderContract,
  'currencyExponent'
> & {
  orderAccessTokenHash: string;
  idempotencyKeyHash: string;
  requestFingerprint: string;
};

export interface ConvertQuoteInput {
  proposedOrderId: string;
  proposedOrderNumber: string;
  quoteId: string;
  idempotencyKeyHash: string;
  requestFingerprint: string;
  orderAccessTokenHash: string;
  customerName: string;
  customerEmail: string;
  recipientEmail: string;
  locale: SalesOrderLocale;
  createdAt: string;
}

export type ConvertQuoteResult =
  | {
      kind: 'CREATED' | 'REPLAY';
      order: PersistedSalesOrder;
    }
  | {
      kind:
        | 'QUOTE_NOT_FOUND'
        | 'QUOTE_EXPIRED'
        | 'CHANNEL_NOT_SUPPORTED'
        | 'QUOTE_ALREADY_CONVERTED';
    };

const toIso = (value: string | Date): string =>
  new Date(value).toISOString();

const mapOrder = (
  row: SalesOrderRow,
): PersistedSalesOrder => ({
  id: row.id,
  orderNumber: row.order_number,
  quoteId: row.pricing_quote_id,
  offerCode: row.offer_code,
  market: row.market,
  currency: row.currency,
  channel: row.channel,
  unitAmountMinor: row.unit_amount_minor,
  quantity: row.quantity,
  subtotalAmountMinor: row.subtotal_amount_minor,
  totalAmountMinor: row.total_amount_minor,
  status: row.status,
  paymentStatus: row.payment_status,
  fulfillmentStatus: row.fulfillment_status,
  source: row.source,
  customerName: row.customer_name,
  customerEmail: row.customer_email,
  recipientEmail: row.recipient_email,
  locale: row.locale,
  quoteIssuedAt: toIso(row.quote_issued_at),
  quoteExpiresAt: toIso(row.quote_expires_at),
  createdAt: toIso(row.created_at),
  version: row.version,
  orderAccessTokenHash: row.order_access_token_hash,
  idempotencyKeyHash: row.idempotency_key_hash,
  requestFingerprint: row.request_fingerprint,
});

@Injectable()
export class SalesOrderRepository {
  constructor(private readonly database: PostgresService) {}

  async convertQuote(
    input: ConvertQuoteInput,
  ): Promise<ConvertQuoteResult> {
    return this.database.transaction(async (client) => {
      const quoteResult = await client.query<PricingQuoteRow>(
        `SELECT
           id,
           product_offer_id,
           offer_code,
           market,
           currency,
           channel,
           unit_amount_minor::text,
           quantity,
           subtotal_amount_minor::text,
           total_amount_minor::text,
           price_book_code,
           price_book_version,
           price_book_entry_version,
           issued_at,
           expires_at
         FROM pricing.pricing_quotes
         WHERE id = $1::uuid
         FOR UPDATE`,
        [input.quoteId],
      );
      const quote = quoteResult.rows[0];

      if (!quote) {
        return { kind: 'QUOTE_NOT_FOUND' };
      }

      const existingResult = await client.query<SalesOrderRow>(
        `SELECT *
           FROM sales_order.orders
          WHERE pricing_quote_id = $1::uuid`,
        [input.quoteId],
      );
      const existing = existingResult.rows[0];

      if (existing) {
        if (
          existing.idempotency_key_hash ===
            input.idempotencyKeyHash &&
          existing.request_fingerprint ===
            input.requestFingerprint
        ) {
          return {
            kind: 'REPLAY',
            order: mapOrder(existing),
          };
        }

        return { kind: 'QUOTE_ALREADY_CONVERTED' };
      }

      if (quote.channel !== 'B2C') {
        return { kind: 'CHANNEL_NOT_SUPPORTED' };
      }

      const clock = await client.query<
        QueryResultRow & { active: boolean }
      >(
        `SELECT $1::timestamptz > CURRENT_TIMESTAMP AS active`,
        [quote.expires_at],
      );

      if (!clock.rows[0]?.active) {
        return { kind: 'QUOTE_EXPIRED' };
      }

      const inserted = await client.query<SalesOrderRow>(
        `INSERT INTO sales_order.orders (
           id,
           order_number,
           pricing_quote_id,
           product_offer_id,
           offer_code,
           market,
           currency,
           channel,
           unit_amount_minor,
           quantity,
           subtotal_amount_minor,
           total_amount_minor,
           price_book_code,
           price_book_version,
           price_book_entry_version,
           quote_issued_at,
           quote_expires_at,
           status,
           payment_status,
           fulfillment_status,
           source,
           customer_name,
           customer_email,
           recipient_email,
           locale,
           idempotency_key_hash,
           request_fingerprint,
           order_access_token_hash,
           created_at
         ) VALUES (
           $1::uuid,
           $2::varchar(40),
           $3::uuid,
           $4::uuid,
           $5::varchar(64),
           $6::text,
           $7::char(3),
           $8::text,
           $9::numeric(20, 0),
           $10::integer,
           $11::numeric(20, 0),
           $12::numeric(20, 0),
           $13::varchar(64),
           $14::integer,
           $15::integer,
           $16::timestamptz,
           $17::timestamptz,
           'PENDING_PAYMENT',
           'UNPAID',
           'UNFULFILLED',
           'STOREFRONT',
           $18::varchar(120),
           $19::varchar(254),
           $20::varchar(254),
           $21::char(2),
           $22::char(64),
           $23::char(64),
           $24::char(64),
           $25::timestamptz
         )
         RETURNING *`,
        [
          input.proposedOrderId,
          input.proposedOrderNumber,
          quote.id,
          quote.product_offer_id,
          quote.offer_code,
          quote.market,
          quote.currency,
          quote.channel,
          quote.unit_amount_minor,
          quote.quantity,
          quote.subtotal_amount_minor,
          quote.total_amount_minor,
          quote.price_book_code,
          quote.price_book_version,
          quote.price_book_entry_version,
          quote.issued_at,
          quote.expires_at,
          input.customerName,
          input.customerEmail,
          input.recipientEmail,
          input.locale,
          input.idempotencyKeyHash,
          input.requestFingerprint,
          input.orderAccessTokenHash,
          input.createdAt,
        ],
      );

      await this.recordActivity(client, {
        action: 'ORDER_CREATED_FROM_QUOTE',
        subjectId: input.proposedOrderId,
        metadata: {
          orderNumber: input.proposedOrderNumber,
          pricingQuoteId: quote.id,
          offerCode: quote.offer_code,
          market: quote.market,
          currency: quote.currency,
          channel: quote.channel,
          quantity: quote.quantity,
          totalAmountMinor: quote.total_amount_minor,
        },
      });

      return {
        kind: 'CREATED',
        order: mapOrder(inserted.rows[0]),
      };
    });
  }

  async findOrder(
    orderId: string,
    orderAccessTokenHash: string,
  ): Promise<PersistedSalesOrder | null> {
    const result = await this.database.query<SalesOrderRow>(
      `SELECT *
         FROM sales_order.orders
        WHERE id = $1::uuid
          AND order_access_token_hash = $2::char(64)`,
      [orderId, orderAccessTokenHash],
    );

    const row = result.rows[0];
    return row ? mapOrder(row) : null;
  }

  private async recordActivity(
    client: PoolClient,
    input: {
      action: string;
      subjectId: string;
      metadata: Record<string, unknown>;
    },
  ): Promise<void> {
    await client.query(
      `INSERT INTO sales_order.order_activity (
         id,
         action,
         subject_type,
         subject_id,
         metadata
       ) VALUES (
         $1::uuid,
         $2::varchar(100),
         'SalesOrder',
         $3::uuid,
         $4::jsonb
       )`,
      [
        randomUUID(),
        input.action,
        input.subjectId,
        JSON.stringify(input.metadata),
      ],
    );
  }
}
