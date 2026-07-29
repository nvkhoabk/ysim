import { randomUUID } from 'node:crypto';

import { Injectable } from '@nestjs/common';
import type {
  CatalogLocale,
  CatalogLocalizationInput,
  DestinationContract,
  LocalizedDestinationContract,
  LocalizedProductOfferContract,
  ProductContract,
  ProductKind,
  ProductOfferContract,
  ProductOfferLocalizationInput,
  ProductOfferStatus,
  RegionContract,
} from '@ysim/contracts';
import type {
  PoolClient,
  QueryResult,
  QueryResultRow,
} from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';
import { selectLocalization } from '../domain/catalog-policy.js';

interface RegionRow extends QueryResultRow {
  id: string;
  code: string;
  status: 'ACTIVE' | 'SUSPENDED';
  created_at: Date;
}

interface DestinationRow extends QueryResultRow {
  id: string;
  code: string;
  region_id: string;
  status: 'ACTIVE' | 'SUSPENDED';
  created_at: Date;
}

interface ProductRow extends QueryResultRow {
  id: string;
  code: string;
  kind: ProductKind;
  created_at: Date;
}

interface OfferRow extends QueryResultRow {
  id: string;
  code: string;
  product_id: string;
  product_code: string;
  status: ProductOfferStatus;
  duration_days: number;
  data_policy: 'FIXED' | 'DAILY' | 'UNLIMITED';
  data_amount_mb: number | null;
  daily_data_amount_mb: number | null;
  fair_use_data_amount_mb: number | null;
  activation_policy: 'FIRST_NETWORK_CONNECTION' | 'INSTALLATION';
  hotspot_supported: boolean;
  phone_number_included: boolean;
  network_name: string;
  published_at: Date | null;
  created_at: Date;
  updated_at: Date;
  version: number;
}

interface LocalizationRow extends QueryResultRow {
  locale: CatalogLocale;
  name: string;
}

interface OfferLocalizationRow extends QueryResultRow {
  locale: CatalogLocale;
  title: string;
  short_description: string | null;
}

interface DestinationViewRow extends QueryResultRow {
  id: string;
  code: string;
  requested_name: string | null;
  english_name: string | null;
}

export interface CreateRegionRecord {
  code: string;
  localizations: CatalogLocalizationInput[];
  actorIdentityId: string;
}

export interface CreateDestinationRecord {
  code: string;
  regionId: string;
  localizations: CatalogLocalizationInput[];
  actorIdentityId: string;
}

export interface CreateProductRecord {
  code: string;
  kind: ProductKind;
  actorIdentityId: string;
}

export interface CreateOfferRecord {
  code: string;
  productId: string;
  destinationIds: string[];
  durationDays: number;
  dataPolicy: 'FIXED' | 'DAILY' | 'UNLIMITED';
  dataAmountMb: number | null;
  dailyDataAmountMb: number | null;
  fairUseDataAmountMb: number | null;
  activationPolicy: 'FIRST_NETWORK_CONNECTION' | 'INSTALLATION';
  hotspotSupported: boolean;
  phoneNumberIncluded: boolean;
  networkName: string;
  localizations: ProductOfferLocalizationInput[];
  actorIdentityId: string;
}

async function appendActivity(
  client: PoolClient,
  input: {
    actorIdentityId: string;
    action: string;
    subjectType: string;
    subjectId: string;
    metadata?: Record<string, unknown>;
  },
): Promise<void> {
  await client.query(
    `INSERT INTO catalog.catalog_activity (
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
      JSON.stringify(input.metadata ?? {}),
    ],
  );
}

const mapProduct = (row: ProductRow): ProductContract => ({
  id: row.id,
  code: row.code,
  kind: row.kind,
  createdAt: row.created_at.toISOString(),
});

@Injectable()
export class CatalogRepository {
  constructor(private readonly database: PostgresService) {}

  async createRegion(input: CreateRegionRecord): Promise<RegionContract> {
    return this.database.transaction(async (client) => {
      const id = randomUUID();
      const regionResult = await client.query<RegionRow>(
        `INSERT INTO catalog.regions (
           id,
           code,
           status
         ) VALUES ($1, $2, 'ACTIVE')
         RETURNING *`,
        [id, input.code],
      );

      for (const localization of input.localizations) {
        await client.query(
          `INSERT INTO catalog.region_localizations (
             region_id,
             locale,
             name
           ) VALUES ($1, $2, $3)`,
          [id, localization.locale, localization.name],
        );
      }

      await appendActivity(client, {
        actorIdentityId: input.actorIdentityId,
        action: 'REGION_CREATED',
        subjectType: 'Region',
        subjectId: id,
        metadata: { code: input.code },
      });

      const row = regionResult.rows[0];
      return {
        id: row.id,
        code: row.code,
        status: row.status,
        localizations: input.localizations,
        createdAt: row.created_at.toISOString(),
      };
    });
  }

  async createDestination(
    input: CreateDestinationRecord,
  ): Promise<DestinationContract | null> {
    return this.database.transaction(async (client) => {
      const region = await client.query<RegionRow>(
        `SELECT *
           FROM catalog.regions
          WHERE id = $1
            AND status = 'ACTIVE'`,
        [input.regionId],
      );

      if (!region.rows[0]) return null;

      const id = randomUUID();
      const destinationResult = await client.query<DestinationRow>(
        `INSERT INTO catalog.destinations (
           id,
           code,
           region_id,
           status
         ) VALUES ($1, $2, $3, 'ACTIVE')
         RETURNING *`,
        [id, input.code, input.regionId],
      );

      for (const localization of input.localizations) {
        await client.query(
          `INSERT INTO catalog.destination_localizations (
             destination_id,
             locale,
             name
           ) VALUES ($1, $2, $3)`,
          [id, localization.locale, localization.name],
        );
      }

      await appendActivity(client, {
        actorIdentityId: input.actorIdentityId,
        action: 'DESTINATION_CREATED',
        subjectType: 'Destination',
        subjectId: id,
        metadata: {
          code: input.code,
          regionId: input.regionId,
        },
      });

      const row = destinationResult.rows[0];
      return {
        id: row.id,
        code: row.code,
        regionId: row.region_id,
        status: row.status,
        localizations: input.localizations,
        createdAt: row.created_at.toISOString(),
      };
    });
  }

  async createProduct(
    input: CreateProductRecord,
  ): Promise<ProductContract> {
    return this.database.transaction(async (client) => {
      const id = randomUUID();
      const result = await client.query<ProductRow>(
        `INSERT INTO catalog.products (
           id,
           code,
           kind
         ) VALUES ($1, $2, $3)
         RETURNING *`,
        [id, input.code, input.kind],
      );

      await appendActivity(client, {
        actorIdentityId: input.actorIdentityId,
        action: 'PRODUCT_CREATED',
        subjectType: 'Product',
        subjectId: id,
        metadata: {
          code: input.code,
          kind: input.kind,
        },
      });

      return mapProduct(result.rows[0]);
    });
  }

  async createOffer(
    input: CreateOfferRecord,
  ): Promise<ProductOfferContract | null> {
    return this.database.transaction(async (client) => {
      const product = await client.query<ProductRow>(
        `SELECT *
           FROM catalog.products
          WHERE id = $1`,
        [input.productId],
      );

      const productRow = product.rows[0];
      if (!productRow) return null;

      const destinations = await client.query<DestinationRow>(
        `SELECT *
           FROM catalog.destinations
          WHERE id = ANY($1::uuid[])
            AND status = 'ACTIVE'
          ORDER BY code`,
        [input.destinationIds],
      );

      if (destinations.rows.length !== input.destinationIds.length) {
        return null;
      }

      const id = randomUUID();
      const offerResult = await client.query<OfferRow>(
        `INSERT INTO catalog.product_offers (
           id,
           code,
           product_id,
           status,
           duration_days,
           data_policy,
           data_amount_mb,
           daily_data_amount_mb,
           fair_use_data_amount_mb,
           activation_policy,
           hotspot_supported,
           phone_number_included,
           network_name
         ) VALUES (
           $1,
           $2,
           $3,
           'DRAFT',
           $4,
           $5,
           $6,
           $7,
           $8,
           $9,
           $10,
           $11,
           $12
         )
         RETURNING
           *,
           $13::text AS product_code`,
        [
          id,
          input.code,
          input.productId,
          input.durationDays,
          input.dataPolicy,
          input.dataAmountMb,
          input.dailyDataAmountMb,
          input.fairUseDataAmountMb,
          input.activationPolicy,
          input.hotspotSupported,
          input.phoneNumberIncluded,
          input.networkName,
          productRow.code,
        ],
      );

      for (const destinationId of input.destinationIds) {
        await client.query(
          `INSERT INTO catalog.product_offer_destinations (
             product_offer_id,
             destination_id
           ) VALUES ($1, $2)`,
          [id, destinationId],
        );
      }

      for (const localization of input.localizations) {
        await client.query(
          `INSERT INTO catalog.product_offer_localizations (
             product_offer_id,
             locale,
             title,
             short_description
           ) VALUES ($1, $2, $3, $4)`,
          [
            id,
            localization.locale,
            localization.title,
            localization.shortDescription ?? null,
          ],
        );
      }

      await appendActivity(client, {
        actorIdentityId: input.actorIdentityId,
        action: 'PRODUCT_OFFER_CREATED',
        subjectType: 'ProductOffer',
        subjectId: id,
        metadata: {
          code: input.code,
          productId: input.productId,
          destinationIds: input.destinationIds,
        },
      });

      return this.mapOffer(
        offerResult.rows[0],
        input.destinationIds,
        input.localizations,
      );
    });
  }

  async publishOffer(
    offerId: string,
    actorIdentityId: string,
  ): Promise<ProductOfferContract | null> {
    return this.database.transaction(async (client) => {
      const current = await this.findOfferRow(client, offerId, true);
      if (!current) return null;

      if (current.status === 'PUBLISHED') {
        return this.loadOfferContract(client, current);
      }

      if (current.status !== 'DRAFT') {
        throw new Error('CATALOG_INVALID_PUBLISH_TRANSITION');
      }

      const result = await client.query<OfferRow>(
        `UPDATE catalog.product_offers
            SET status = 'PUBLISHED',
                published_at = CURRENT_TIMESTAMP,
                updated_at = CURRENT_TIMESTAMP,
                version = version + 1
          WHERE id = $1
          RETURNING
            *,
            $2::text AS product_code`,
        [offerId, current.product_code],
      );

      await appendActivity(client, {
        actorIdentityId,
        action: 'PRODUCT_OFFER_PUBLISHED',
        subjectType: 'ProductOffer',
        subjectId: offerId,
      });

      return this.loadOfferContract(client, result.rows[0]);
    });
  }

  async suspendOffer(
    offerId: string,
    actorIdentityId: string,
  ): Promise<ProductOfferContract | null> {
    return this.database.transaction(async (client) => {
      const current = await this.findOfferRow(client, offerId, true);
      if (!current) return null;

      if (current.status === 'SUSPENDED') {
        return this.loadOfferContract(client, current);
      }

      if (current.status !== 'PUBLISHED') {
        throw new Error('CATALOG_INVALID_SUSPEND_TRANSITION');
      }

      const result = await client.query<OfferRow>(
        `UPDATE catalog.product_offers
            SET status = 'SUSPENDED',
                updated_at = CURRENT_TIMESTAMP,
                version = version + 1
          WHERE id = $1
          RETURNING
            *,
            $2::text AS product_code`,
        [offerId, current.product_code],
      );

      await appendActivity(client, {
        actorIdentityId,
        action: 'PRODUCT_OFFER_SUSPENDED',
        subjectType: 'ProductOffer',
        subjectId: offerId,
      });

      return this.loadOfferContract(client, result.rows[0]);
    });
  }

  async findLocalizedOffer(
    offerId: string,
    requestedLocale: CatalogLocale,
  ): Promise<LocalizedProductOfferContract | null> {
    const row = await this.findOfferRow(this.database, offerId, false);
    if (!row) return null;

    return this.loadLocalizedOffer(row, requestedLocale);
  }

  async listLocalizedOffers(
    status: ProductOfferStatus,
    requestedLocale: CatalogLocale,
  ): Promise<LocalizedProductOfferContract[]> {
    const rows = await this.database.query<OfferRow>(
      `SELECT
         o.*,
         p.code AS product_code
       FROM catalog.product_offers o
       JOIN catalog.products p
         ON p.id = o.product_id
      WHERE o.status = $1
      ORDER BY o.code`,
      [status],
    );

    return Promise.all(
      rows.rows.map((row) =>
        this.loadLocalizedOffer(row, requestedLocale),
      ),
    );
  }

  private async findOfferRow(
    queryable: PostgresService | PoolClient,
    offerId: string,
    lock: boolean,
  ): Promise<OfferRow | null> {
    const result = await this.query<OfferRow>(
      queryable,
      `SELECT
         o.*,
         p.code AS product_code
       FROM catalog.product_offers o
       JOIN catalog.products p
         ON p.id = o.product_id
      WHERE o.id = $1
      ${lock ? 'FOR UPDATE OF o' : ''}`,
      [offerId],
    );

    return result.rows[0] ?? null;
  }

  private async loadOfferContract(
    queryable: PostgresService | PoolClient,
    row: OfferRow,
  ): Promise<ProductOfferContract> {
    const destinations = await this.query<{ destination_id: string }>(
      queryable,
      `SELECT destination_id
         FROM catalog.product_offer_destinations
        WHERE product_offer_id = $1
        ORDER BY destination_id`,
      [row.id],
    );

    const localizations = await this.query<OfferLocalizationRow>(
      queryable,
      `SELECT
         locale,
         title,
         short_description
       FROM catalog.product_offer_localizations
      WHERE product_offer_id = $1
      ORDER BY locale`,
      [row.id],
    );

    return this.mapOffer(
      row,
      destinations.rows.map((item) => item.destination_id),
      localizations.rows.map((item) => ({
        locale: item.locale,
        title: item.title,
        shortDescription: item.short_description,
      })),
    );
  }

  private async loadLocalizedOffer(
    row: OfferRow,
    requestedLocale: CatalogLocale,
  ): Promise<LocalizedProductOfferContract> {
    const localizations = await this.database.query<OfferLocalizationRow>(
      `SELECT
         locale,
         title,
         short_description
       FROM catalog.product_offer_localizations
      WHERE product_offer_id = $1
      ORDER BY locale`,
      [row.id],
    );

    const selected = selectLocalization(
      localizations.rows,
      requestedLocale,
    );

    const destinationRows =
      await this.database.query<DestinationViewRow>(
        `SELECT
           d.id,
           d.code,
           requested.name AS requested_name,
           english.name AS english_name
         FROM catalog.product_offer_destinations pod
         JOIN catalog.destinations d
           ON d.id = pod.destination_id
         LEFT JOIN catalog.destination_localizations requested
           ON requested.destination_id = d.id
          AND requested.locale = $2
         LEFT JOIN catalog.destination_localizations english
           ON english.destination_id = d.id
          AND english.locale = 'en'
        WHERE pod.product_offer_id = $1
        ORDER BY d.code`,
        [row.id, requestedLocale],
      );

    const destinations: LocalizedDestinationContract[] =
      destinationRows.rows.map((destination) => ({
        id: destination.id,
        code: destination.code,
        name:
          destination.requested_name ??
          destination.english_name ??
          destination.code,
        requestedLocale,
        sourceLocale:
          destination.requested_name !== null
            ? requestedLocale
            : 'en',
      }));

    return {
      id: row.id,
      code: row.code,
      productId: row.product_id,
      productCode: row.product_code,
      status: row.status,
      durationDays: row.duration_days,
      dataPolicy: row.data_policy,
      dataAmountMb: row.data_amount_mb,
      dailyDataAmountMb: row.daily_data_amount_mb,
      fairUseDataAmountMb: row.fair_use_data_amount_mb,
      activationPolicy: row.activation_policy,
      hotspotSupported: row.hotspot_supported,
      phoneNumberIncluded: row.phone_number_included,
      networkName: row.network_name,
      title: selected.value.title,
      shortDescription: selected.value.short_description,
      requestedLocale,
      sourceLocale: selected.sourceLocale,
      destinations,
      publishedAt: row.published_at?.toISOString() ?? null,
      createdAt: row.created_at.toISOString(),
      updatedAt: row.updated_at.toISOString(),
      version: row.version,
    };
  }

  private query<T extends QueryResultRow>(
    queryable: PostgresService | PoolClient,
    text: string,
    values: readonly unknown[] = [],
  ): Promise<QueryResult<T>> {
    const execute = queryable.query.bind(queryable) as unknown as (
      queryText: string,
      queryValues: unknown[],
    ) => Promise<QueryResult<T>>;

    return execute(text, [...values]);
  }

  private mapOffer(
    row: OfferRow,
    destinationIds: string[],
    localizations: ProductOfferLocalizationInput[],
  ): ProductOfferContract {
    return {
      id: row.id,
      code: row.code,
      productId: row.product_id,
      productCode: row.product_code,
      status: row.status,
      durationDays: row.duration_days,
      dataPolicy: row.data_policy,
      dataAmountMb: row.data_amount_mb,
      dailyDataAmountMb: row.daily_data_amount_mb,
      fairUseDataAmountMb: row.fair_use_data_amount_mb,
      activationPolicy: row.activation_policy,
      hotspotSupported: row.hotspot_supported,
      phoneNumberIncluded: row.phone_number_included,
      networkName: row.network_name,
      destinationIds,
      localizations,
      publishedAt: row.published_at?.toISOString() ?? null,
      createdAt: row.created_at.toISOString(),
      updatedAt: row.updated_at.toISOString(),
      version: row.version,
    };
  }
}
