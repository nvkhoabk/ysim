import { randomUUID } from 'node:crypto';

import { Injectable } from '@nestjs/common';
import type {
  PriceBookContract,
  PriceBookEntryContract,
  PricingChannel,
  PricingCurrency,
  PricingMarket,
  PricingQuoteContract,
  PricingSupplierEnvironment,
  SupplierCostSnapshotContract,
} from '@ysim/contracts';
import type { PoolClient, QueryResultRow } from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';

interface PriceBookRow extends QueryResultRow {
  id: string;
  code: string;
  market: PricingMarket;
  currency: PricingCurrency;
  channel: PricingChannel;
  status: 'DRAFT' | 'ACTIVE' | 'SUSPENDED';
  valid_from: string | Date;
  valid_to: string | Date;
  version: number;
  created_at: string | Date;
  activated_at: string | Date | null;
  suspended_at: string | Date | null;
}

interface SupplierCostSnapshotRow extends QueryResultRow {
  id: string;
  supplier_plan_mapping_id: string;
  product_offer_id: string;
  supplier_environment: PricingSupplierEnvironment;
  currency: PricingCurrency;
  unit_cost_amount_minor: string;
  observed_at: string | Date;
  source_snapshot_hash: string;
  created_at: string | Date;
}

interface PriceBookEntryRow extends QueryResultRow {
  id: string;
  price_book_id: string;
  product_offer_id: string;
  offer_code: string;
  unit_amount_minor: string;
  supplier_cost_snapshot_id: string;
  version: number;
  created_at: string | Date;
}

interface MappingSourceRow extends QueryResultRow {
  mapping_id: string;
  product_offer_id: string;
  supplier_environment: PricingSupplierEnvironment;
  raw_snapshot_hash: string;
}

interface QuoteSourceRow extends QueryResultRow {
  product_offer_id: string;
  offer_code: string;
  price_book_id: string;
  price_book_code: string;
  price_book_version: number;
  price_book_valid_to: string | Date;
  price_book_entry_id: string;
  price_book_entry_version: number;
  unit_amount_minor: string;
  supplier_cost_snapshot_id: string;
  supplier_unit_cost_amount_minor: string;
  supplier_cost_currency: PricingCurrency;
}

interface PricingQuoteRow extends QueryResultRow {
  id: string;
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

export interface CreatePriceBookInput {
  code: string;
  market: PricingMarket;
  currency: PricingCurrency;
  channel: PricingChannel;
  validFrom: string;
  validTo: string;
  actorIdentityId: string;
}

export interface CreateSupplierCostSnapshotInput {
  supplierPlanMappingId: string;
  currency: PricingCurrency;
  unitCostAmountMinor: string;
  observedAt: string;
  sourceSnapshotHash: string;
  actorIdentityId: string;
}

export interface CreatePriceBookEntryInput {
  priceBookId: string;
  productOfferId: string;
  unitAmountMinor: string;
  supplierCostSnapshotId: string;
  actorIdentityId: string;
}

export interface QuoteSource {
  productOfferId: string;
  offerCode: string;
  priceBookId: string;
  priceBookCode: string;
  priceBookVersion: number;
  priceBookValidTo: string;
  priceBookEntryId: string;
  priceBookEntryVersion: number;
  unitAmountMinor: string;
  supplierCostSnapshotId: string;
  supplierUnitCostAmountMinor: string;
  supplierCostCurrency: PricingCurrency;
}

export interface PersistQuoteInput {
  source: QuoteSource;
  market: PricingMarket;
  currency: PricingCurrency;
  channel: PricingChannel;
  supplierEnvironment: PricingSupplierEnvironment;
  quantity: number;
  subtotalAmountMinor: string;
  totalAmountMinor: string;
  issuedAt: string;
  expiresAt: string;
}

const toIso = (value: string | Date): string =>
  new Date(value).toISOString();

const toNullableIso = (value: string | Date | null): string | null =>
  value === null ? null : toIso(value);

const mapPriceBook = (row: PriceBookRow): PriceBookContract => ({
  id: row.id,
  code: row.code,
  market: row.market,
  currency: row.currency,
  channel: row.channel,
  status: row.status,
  validFrom: toIso(row.valid_from),
  validTo: toIso(row.valid_to),
  version: row.version,
  createdAt: toIso(row.created_at),
  activatedAt: toNullableIso(row.activated_at),
  suspendedAt: toNullableIso(row.suspended_at),
});

const mapCostSnapshot = (
  row: SupplierCostSnapshotRow,
): SupplierCostSnapshotContract => ({
  id: row.id,
  supplierPlanMappingId: row.supplier_plan_mapping_id,
  productOfferId: row.product_offer_id,
  supplierEnvironment: row.supplier_environment,
  currency: row.currency,
  unitCostAmountMinor: row.unit_cost_amount_minor,
  observedAt: toIso(row.observed_at),
  sourceSnapshotHash: row.source_snapshot_hash,
  createdAt: toIso(row.created_at),
});

const mapEntry = (row: PriceBookEntryRow): PriceBookEntryContract => ({
  id: row.id,
  priceBookId: row.price_book_id,
  productOfferId: row.product_offer_id,
  offerCode: row.offer_code,
  unitAmountMinor: row.unit_amount_minor,
  supplierCostSnapshotId: row.supplier_cost_snapshot_id,
  version: row.version,
  createdAt: toIso(row.created_at),
});

@Injectable()
export class PricingRepository {
  constructor(private readonly database: PostgresService) {}

  async createPriceBook(
    input: CreatePriceBookInput,
  ): Promise<PriceBookContract> {
    const id = randomUUID();

    return this.database.transaction(async (client) => {
      const inserted = await client.query<PriceBookRow>(
        `INSERT INTO pricing.price_books (
           id,
           code,
           market,
           currency,
           channel,
           status,
           valid_from,
           valid_to,
           created_by
         ) VALUES ($1, $2, $3, $4, $5, 'DRAFT', $6, $7, $8)
         RETURNING *`,
        [
          id,
          input.code,
          input.market,
          input.currency,
          input.channel,
          input.validFrom,
          input.validTo,
          input.actorIdentityId,
        ],
      );

      await this.recordActivity(client, {
        actorIdentityId: input.actorIdentityId,
        action: 'PRICE_BOOK_CREATED',
        subjectType: 'PriceBook',
        subjectId: id,
        metadata: {
          code: input.code,
          market: input.market,
          currency: input.currency,
          channel: input.channel,
        },
      });

      return mapPriceBook(inserted.rows[0]);
    });
  }

  async createSupplierCostSnapshot(
    input: CreateSupplierCostSnapshotInput,
  ): Promise<SupplierCostSnapshotContract | null> {
    const id = randomUUID();

    return this.database.transaction(async (client) => {
      const source = await client.query<MappingSourceRow>(
        `SELECT
           spm.id AS mapping_id,
           spm.product_offer_id,
           se.environment AS supplier_environment,
           sp.raw_snapshot_hash
         FROM supplier_management.supplier_plan_mappings spm
         JOIN supplier_management.supplier_environments se
           ON se.id = spm.supplier_environment_id
         JOIN supplier_management.suppliers s
           ON s.id = se.supplier_id
         JOIN supplier_management.supplier_plans sp
           ON sp.id = spm.supplier_plan_id
        WHERE spm.id = $1
          AND spm.status = 'ACTIVE'
          AND se.contract_status = 'PROBED'
          AND s.status = 'ACTIVE'
          AND sp.status = 'ACTIVE'
        FOR SHARE OF spm, se, s, sp`,
        [input.supplierPlanMappingId],
      );

      const mapping = source.rows[0];
      if (!mapping) return null;

      if (mapping.raw_snapshot_hash !== input.sourceSnapshotHash) {
        throw new Error('PRICING_SUPPLIER_SNAPSHOT_HASH_MISMATCH');
      }

      const inserted = await client.query<SupplierCostSnapshotRow>(
        `INSERT INTO pricing.supplier_cost_snapshots (
           id,
           supplier_plan_mapping_id,
           product_offer_id,
           supplier_environment,
           currency,
           unit_cost_amount_minor,
           observed_at,
           source_snapshot_hash,
           created_by
         ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
         RETURNING *`,
        [
          id,
          input.supplierPlanMappingId,
          mapping.product_offer_id,
          mapping.supplier_environment,
          input.currency,
          input.unitCostAmountMinor,
          input.observedAt,
          input.sourceSnapshotHash,
          input.actorIdentityId,
        ],
      );

      await this.recordActivity(client, {
        actorIdentityId: input.actorIdentityId,
        action: 'SUPPLIER_COST_SNAPSHOT_CREATED',
        subjectType: 'SupplierCostSnapshot',
        subjectId: id,
        metadata: {
          supplierPlanMappingId: input.supplierPlanMappingId,
          productOfferId: mapping.product_offer_id,
          supplierEnvironment: mapping.supplier_environment,
          currency: input.currency,
        },
      });

      return mapCostSnapshot(inserted.rows[0]);
    });
  }

  async createPriceBookEntry(
    input: CreatePriceBookEntryInput,
  ): Promise<PriceBookEntryContract | null> {
    const id = randomUUID();

    return this.database.transaction(async (client) => {
      const priceBookResult = await client.query<PriceBookRow>(
        `SELECT *
           FROM pricing.price_books
          WHERE id = $1
          FOR UPDATE`,
        [input.priceBookId],
      );

      const priceBook = priceBookResult.rows[0];
      if (!priceBook) return null;
      if (priceBook.status !== 'DRAFT') {
        throw new Error('PRICING_PRICE_BOOK_NOT_DRAFT');
      }

      const source = await client.query<
        QueryResultRow & { offer_code: string }
      >(
        `SELECT po.code AS offer_code
           FROM catalog.product_offers po
           JOIN pricing.supplier_cost_snapshots scs
             ON scs.id = $2
            AND scs.product_offer_id = po.id
          WHERE po.id = $1
            AND po.status = 'PUBLISHED'
            AND scs.currency = $3`,
        [
          input.productOfferId,
          input.supplierCostSnapshotId,
          priceBook.currency,
        ],
      );

      const offerCode = source.rows[0]?.offer_code;
      if (!offerCode) {
        throw new Error('PRICING_OFFER_OR_COST_SNAPSHOT_UNAVAILABLE');
      }

      const inserted = await client.query<PriceBookEntryRow>(
        `INSERT INTO pricing.price_book_entries (
           id,
           price_book_id,
           product_offer_id,
           offer_code,
           unit_amount_minor,
           supplier_cost_snapshot_id,
           created_by
         ) VALUES ($1, $2, $3, $4, $5, $6, $7)
         RETURNING *`,
        [
          id,
          input.priceBookId,
          input.productOfferId,
          offerCode,
          input.unitAmountMinor,
          input.supplierCostSnapshotId,
          input.actorIdentityId,
        ],
      );

      await this.recordActivity(client, {
        actorIdentityId: input.actorIdentityId,
        action: 'PRICE_BOOK_ENTRY_CREATED',
        subjectType: 'PriceBookEntry',
        subjectId: id,
        metadata: {
          priceBookId: input.priceBookId,
          productOfferId: input.productOfferId,
          offerCode,
        },
      });

      return mapEntry(inserted.rows[0]);
    });
  }

  async activatePriceBook(
    priceBookId: string,
    actorIdentityId: string,
  ): Promise<PriceBookContract | null> {
    return this.database.transaction(async (client) => {
      const bookResult = await client.query<PriceBookRow>(
        `SELECT *
           FROM pricing.price_books
          WHERE id = $1
          FOR UPDATE`,
        [priceBookId],
      );

      const book = bookResult.rows[0];
      if (!book) return null;
      if (book.status !== 'DRAFT') {
        throw new Error('PRICING_INVALID_ACTIVATE_TRANSITION');
      }

      const activationClock = await client.query<
        QueryResultRow & { can_activate: boolean }
      >(
        `SELECT $1::timestamptz > CURRENT_TIMESTAMP AS can_activate`,
        [book.valid_to],
      );

      if (!activationClock.rows[0].can_activate) {
        throw new Error('PRICING_PRICE_BOOK_EXPIRED');
      }

      const entries = await client.query<
        QueryResultRow & { entry_count: number }
      >(
        `SELECT COUNT(*)::int AS entry_count
           FROM pricing.price_book_entries
          WHERE price_book_id = $1`,
        [priceBookId],
      );

      if (entries.rows[0].entry_count === 0) {
        throw new Error('PRICING_PRICE_BOOK_EMPTY');
      }

      await client.query(
        `SELECT pg_advisory_xact_lock(
           hashtext($1::text || ':' || $2::text || ':' || $3::text)
         )`,
        [book.market, book.currency, book.channel],
      );

      const overlap = await client.query<
        QueryResultRow & { id: string }
      >(
        `SELECT id
           FROM pricing.price_books
          WHERE id <> $1
            AND market = $2
            AND currency = $3
            AND channel = $4
            AND status = 'ACTIVE'
            AND valid_from < $6::timestamptz
            AND valid_to > $5::timestamptz
          LIMIT 1`,
        [
          priceBookId,
          book.market,
          book.currency,
          book.channel,
          book.valid_from,
          book.valid_to,
        ],
      );

      if (overlap.rows.length > 0) {
        throw new Error('PRICING_ACTIVE_BOOK_OVERLAP');
      }

      const updated = await client.query<PriceBookRow>(
        `UPDATE pricing.price_books
            SET status = 'ACTIVE',
                activated_at = CURRENT_TIMESTAMP,
                version = version + 1
          WHERE id = $1
          RETURNING *`,
        [priceBookId],
      );

      await this.recordActivity(client, {
        actorIdentityId,
        action: 'PRICE_BOOK_ACTIVATED',
        subjectType: 'PriceBook',
        subjectId: priceBookId,
        metadata: {},
      });

      return mapPriceBook(updated.rows[0]);
    });
  }

  async suspendPriceBook(
    priceBookId: string,
    actorIdentityId: string,
  ): Promise<PriceBookContract | null> {
    return this.database.transaction(async (client) => {
      const updated = await client.query<PriceBookRow>(
        `UPDATE pricing.price_books
            SET status = 'SUSPENDED',
                suspended_at = CURRENT_TIMESTAMP,
                version = version + 1
          WHERE id = $1
            AND status = 'ACTIVE'
          RETURNING *`,
        [priceBookId],
      );

      if (updated.rows.length === 0) {
        const exists = await client.query(
          `SELECT 1 FROM pricing.price_books WHERE id = $1`,
          [priceBookId],
        );

        if (exists.rows.length === 0) return null;
        throw new Error('PRICING_INVALID_SUSPEND_TRANSITION');
      }

      await this.recordActivity(client, {
        actorIdentityId,
        action: 'PRICE_BOOK_SUSPENDED',
        subjectType: 'PriceBook',
        subjectId: priceBookId,
        metadata: {},
      });

      return mapPriceBook(updated.rows[0]);
    });
  }

  async findQuoteSource(input: {
    offerCode: string;
    market: PricingMarket;
    currency: PricingCurrency;
    channel: PricingChannel;
    supplierEnvironment: PricingSupplierEnvironment;
    issuedAt: string;
  }): Promise<QuoteSource | null> {
    const result = await this.database.query<QuoteSourceRow>(
      `SELECT
         po.id AS product_offer_id,
         po.code AS offer_code,
         pb.id AS price_book_id,
         pb.code AS price_book_code,
         pb.version AS price_book_version,
         pb.valid_to AS price_book_valid_to,
         pbe.id AS price_book_entry_id,
         pbe.version AS price_book_entry_version,
         pbe.unit_amount_minor::text,
         scs.id AS supplier_cost_snapshot_id,
         scs.unit_cost_amount_minor::text
           AS supplier_unit_cost_amount_minor,
         scs.currency AS supplier_cost_currency
       FROM pricing.price_books pb
       JOIN pricing.price_book_entries pbe
         ON pbe.price_book_id = pb.id
       JOIN catalog.product_offers po
         ON po.id = pbe.product_offer_id
       JOIN pricing.supplier_cost_snapshots scs
         ON scs.id = pbe.supplier_cost_snapshot_id
        AND scs.product_offer_id = po.id
       JOIN supplier_management.supplier_plan_mappings spm
         ON spm.id = scs.supplier_plan_mapping_id
        AND spm.product_offer_id = po.id
       JOIN supplier_management.supplier_environments se
         ON se.id = spm.supplier_environment_id
       JOIN supplier_management.suppliers s
         ON s.id = se.supplier_id
       JOIN supplier_management.supplier_plans sp
         ON sp.id = spm.supplier_plan_id
      WHERE po.code = $1
        AND po.status = 'PUBLISHED'
        AND pb.market = $2
        AND pb.currency = $3
        AND pb.channel = $4
        AND pb.status = 'ACTIVE'
        AND pb.valid_from <= $6::timestamptz
        AND pb.valid_to > $6::timestamptz
        AND scs.supplier_environment = $5
        AND scs.currency = pb.currency
        AND se.environment = $5
        AND se.contract_status = 'PROBED'
        AND spm.status = 'ACTIVE'
        AND s.status = 'ACTIVE'
        AND sp.status = 'ACTIVE'
      ORDER BY pb.valid_from DESC, pb.code
      LIMIT 1`,
      [
        input.offerCode,
        input.market,
        input.currency,
        input.channel,
        input.supplierEnvironment,
        input.issuedAt,
      ],
    );

    const row = result.rows[0];
    if (!row) return null;

    return {
      productOfferId: row.product_offer_id,
      offerCode: row.offer_code,
      priceBookId: row.price_book_id,
      priceBookCode: row.price_book_code,
      priceBookVersion: row.price_book_version,
      priceBookValidTo: toIso(row.price_book_valid_to),
      priceBookEntryId: row.price_book_entry_id,
      priceBookEntryVersion: row.price_book_entry_version,
      unitAmountMinor: row.unit_amount_minor,
      supplierCostSnapshotId: row.supplier_cost_snapshot_id,
      supplierUnitCostAmountMinor:
        row.supplier_unit_cost_amount_minor,
      supplierCostCurrency: row.supplier_cost_currency,
    };
  }

  async persistQuote(
    input: PersistQuoteInput,
  ): Promise<PricingQuoteContract | null> {
    const id = randomUUID();

    return this.database.transaction(async (client) => {
      const inserted = await client.query<PricingQuoteRow>(
        `INSERT INTO pricing.pricing_quotes (
           id,
           product_offer_id,
           offer_code,
           market,
           currency,
           channel,
           unit_amount_minor,
           quantity,
           subtotal_amount_minor,
           total_amount_minor,
           supplier_unit_cost_amount_minor,
           supplier_cost_currency,
           price_book_id,
           price_book_code,
           price_book_version,
           price_book_entry_id,
           price_book_entry_version,
           supplier_cost_snapshot_id,
           issued_at,
           expires_at
         )
         SELECT
           $1::uuid,
           $2::uuid,
           $3::varchar(64),
           $4::text,
           $5::char(3),
           $6::text,
           $7::numeric(20, 0),
           $8::integer,
           $9::numeric(20, 0),
           $10::numeric(20, 0),
           $11::numeric(20, 0),
           $12::char(3),
           $13::uuid,
           $14::varchar(64),
           $15::integer,
           $16::uuid,
           $17::integer,
           $18::uuid,
           $19::timestamptz,
           $20::timestamptz
         WHERE EXISTS (
           SELECT 1
             FROM pricing.price_books pb
             JOIN pricing.price_book_entries pbe
               ON pbe.price_book_id = pb.id
             JOIN catalog.product_offers po
               ON po.id = pbe.product_offer_id
             JOIN pricing.supplier_cost_snapshots scs
               ON scs.id = pbe.supplier_cost_snapshot_id
              AND scs.product_offer_id = po.id
             JOIN supplier_management.supplier_plan_mappings spm
               ON spm.id = scs.supplier_plan_mapping_id
              AND spm.product_offer_id = po.id
             JOIN supplier_management.supplier_environments se
               ON se.id = spm.supplier_environment_id
             JOIN supplier_management.suppliers s
               ON s.id = se.supplier_id
             JOIN supplier_management.supplier_plans sp
               ON sp.id = spm.supplier_plan_id
            WHERE pb.id = $13::uuid
              AND pb.status = 'ACTIVE'
              AND pb.valid_from <= $19::timestamptz
              AND pb.valid_to >= $20::timestamptz
              AND pbe.id = $16::uuid
              AND pbe.product_offer_id = $2::uuid
              AND po.code = $3::varchar(64)
              AND po.status = 'PUBLISHED'
              AND scs.id = $18::uuid
              AND scs.currency = $5::char(3)
              AND scs.supplier_environment = $21::text
              AND spm.status = 'ACTIVE'
              AND se.environment = $21::text
              AND se.contract_status = 'PROBED'
              AND s.status = 'ACTIVE'
              AND sp.status = 'ACTIVE'
         )
         RETURNING
           id,
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
           expires_at`,
        [
          id,
          input.source.productOfferId,
          input.source.offerCode,
          input.market,
          input.currency,
          input.channel,
          input.source.unitAmountMinor,
          input.quantity,
          input.subtotalAmountMinor,
          input.totalAmountMinor,
          input.source.supplierUnitCostAmountMinor,
          input.source.supplierCostCurrency,
          input.source.priceBookId,
          input.source.priceBookCode,
          input.source.priceBookVersion,
          input.source.priceBookEntryId,
          input.source.priceBookEntryVersion,
          input.source.supplierCostSnapshotId,
          input.issuedAt,
          input.expiresAt,
          input.supplierEnvironment,
        ],
      );

      const row = inserted.rows[0];
      if (!row) return null;

      await this.recordActivity(client, {
        actorIdentityId: null,
        action: 'PRICING_QUOTE_ISSUED',
        subjectType: 'PricingQuote',
        subjectId: id,
        metadata: {
          offerCode: input.source.offerCode,
          market: input.market,
          currency: input.currency,
          channel: input.channel,
          quantity: input.quantity,
        },
      });

      return this.mapQuoteRow(row, 'ACTIVE');
    });
  }

  async findQuote(
    quoteId: string,
  ): Promise<Omit<PricingQuoteContract, 'status'> | null> {
    const result = await this.database.query<PricingQuoteRow>(
      `SELECT
         id,
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
      WHERE id = $1`,
      [quoteId],
    );

    const row = result.rows[0];
    if (!row) return null;

    const mapped = this.mapQuoteRow(row, 'ACTIVE');
    const { status: _status, ...withoutStatus } = mapped;
    return withoutStatus;
  }

  private mapQuoteRow(
    row: PricingQuoteRow,
    status: 'ACTIVE' | 'EXPIRED',
  ): PricingQuoteContract {
    return {
      id: row.id,
      offerCode: row.offer_code,
      market: row.market,
      currency: row.currency,
      currencyExponent: row.currency === 'USD' ? 2 : 0,
      channel: row.channel,
      unitAmountMinor: row.unit_amount_minor,
      quantity: row.quantity,
      subtotalAmountMinor: row.subtotal_amount_minor,
      totalAmountMinor: row.total_amount_minor,
      priceBookCode: row.price_book_code,
      priceBookVersion: row.price_book_version,
      priceBookEntryVersion: row.price_book_entry_version,
      issuedAt: toIso(row.issued_at),
      expiresAt: toIso(row.expires_at),
      status,
    };
  }

  private async recordActivity(
    client: PoolClient,
    input: {
      actorIdentityId: string | null;
      action: string;
      subjectType: string;
      subjectId: string;
      metadata: Record<string, unknown>;
    },
  ): Promise<void> {
    await client.query(
      `INSERT INTO pricing.pricing_activity (
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
        JSON.stringify(input.metadata),
      ],
    );
  }
}
