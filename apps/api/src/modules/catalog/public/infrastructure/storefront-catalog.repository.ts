import { Injectable } from '@nestjs/common';
import type {
  StorefrontCatalogLocale,
  StorefrontCatalogOfferContract,
  StorefrontCatalogDestinationContract,
  StorefrontSupplierEnvironment,
} from '@ysim/contracts';
import type { QueryResultRow } from 'pg';

import { PostgresService } from '../../../../platform/database/postgres.service.js';

interface DestinationSummaryRow extends QueryResultRow {
  code: string;
  region_code: string;
  name: string;
  source_locale: StorefrontCatalogLocale;
  available_offer_count: number;
}

interface OfferSummaryRow extends QueryResultRow {
  id: string;
  code: string;
  product_code: string;
  duration_days: number;
  data_policy: 'FIXED' | 'DAILY' | 'UNLIMITED';
  data_amount_mb: number | null;
  daily_data_amount_mb: number | null;
  fair_use_data_amount_mb: number | null;
  activation_policy:
    | 'FIRST_NETWORK_CONNECTION'
    | 'INSTALLATION';
  hotspot_supported: boolean;
  phone_number_included: boolean;
  network_name: string;
  title: string;
  short_description: string | null;
  source_locale: StorefrontCatalogLocale;
  version: number;
}

interface OfferDestinationRow extends QueryResultRow {
  product_offer_id: string;
  code: string;
  name: string;
  source_locale: StorefrontCatalogLocale;
}

const availabilitySql = `
  EXISTS (
    SELECT 1
      FROM supplier_management.supplier_plan_mappings spm
      JOIN supplier_management.supplier_environments se
        ON se.id = spm.supplier_environment_id
      JOIN supplier_management.suppliers s
        ON s.id = se.supplier_id
      JOIN supplier_management.supplier_plans sp
        ON sp.id = spm.supplier_plan_id
     WHERE spm.product_offer_id = po.id
       AND spm.status = 'ACTIVE'
       AND se.environment = $2
       AND se.contract_status = 'PROBED'
       AND s.status = 'ACTIVE'
       AND sp.status = 'ACTIVE'
  )
`;

@Injectable()
export class StorefrontCatalogRepository {
  constructor(private readonly database: PostgresService) {}

  async listDestinations(
    locale: StorefrontCatalogLocale,
    environment: StorefrontSupplierEnvironment,
  ): Promise<StorefrontCatalogDestinationContract[]> {
    const result = await this.database.query<DestinationSummaryRow>(
      `SELECT
         d.code,
         r.code AS region_code,
         COALESCE(dl_requested.name, dl_english.name) AS name,
         CASE
           WHEN dl_requested.destination_id IS NOT NULL
             THEN $1::text
           ELSE 'en'
         END AS source_locale,
         COUNT(DISTINCT po.id)::int AS available_offer_count
       FROM catalog.destinations d
       JOIN catalog.regions r
         ON r.id = d.region_id
       JOIN catalog.destination_localizations dl_english
         ON dl_english.destination_id = d.id
        AND dl_english.locale = 'en'
       LEFT JOIN catalog.destination_localizations dl_requested
         ON dl_requested.destination_id = d.id
        AND dl_requested.locale = $1
       JOIN catalog.product_offer_destinations pod
         ON pod.destination_id = d.id
       JOIN catalog.product_offers po
         ON po.id = pod.product_offer_id
      WHERE d.status = 'ACTIVE'
        AND r.status = 'ACTIVE'
        AND po.status = 'PUBLISHED'
        AND ${availabilitySql}
      GROUP BY
        d.code,
        r.code,
        dl_requested.destination_id,
        dl_requested.name,
        dl_english.name
      ORDER BY d.code`,
      [locale, environment],
    );

    return result.rows.map((row) => ({
      code: row.code,
      regionCode: row.region_code,
      name: row.name,
      requestedLocale: locale,
      sourceLocale: row.source_locale,
      availableOfferCount: row.available_offer_count,
    }));
  }

  async listOffersByDestination(
    destinationCode: string,
    locale: StorefrontCatalogLocale,
    environment: StorefrontSupplierEnvironment,
  ): Promise<StorefrontCatalogOfferContract[]> {
    return this.listOffers(
      locale,
      environment,
      destinationCode,
      null,
    );
  }

  async findOfferByCode(
    offerCode: string,
    locale: StorefrontCatalogLocale,
    environment: StorefrontSupplierEnvironment,
  ): Promise<StorefrontCatalogOfferContract | null> {
    const offers = await this.listOffers(
      locale,
      environment,
      null,
      offerCode,
    );

    return offers[0] ?? null;
  }

  private async listOffers(
    locale: StorefrontCatalogLocale,
    environment: StorefrontSupplierEnvironment,
    destinationCode: string | null,
    offerCode: string | null,
  ): Promise<StorefrontCatalogOfferContract[]> {
    const offerResult = await this.database.query<OfferSummaryRow>(
      `SELECT
         po.id,
         po.code,
         p.code AS product_code,
         po.duration_days,
         po.data_policy,
         po.data_amount_mb,
         po.daily_data_amount_mb,
         po.fair_use_data_amount_mb,
         po.activation_policy,
         po.hotspot_supported,
         po.phone_number_included,
         po.network_name,
         COALESCE(pol_requested.title, pol_english.title) AS title,
         COALESCE(
           pol_requested.short_description,
           pol_english.short_description
         ) AS short_description,
         CASE
           WHEN pol_requested.product_offer_id IS NOT NULL
             THEN $1::text
           ELSE 'en'
         END AS source_locale,
         po.version
       FROM catalog.product_offers po
       JOIN catalog.products p
         ON p.id = po.product_id
       JOIN catalog.product_offer_localizations pol_english
         ON pol_english.product_offer_id = po.id
        AND pol_english.locale = 'en'
       LEFT JOIN catalog.product_offer_localizations pol_requested
         ON pol_requested.product_offer_id = po.id
        AND pol_requested.locale = $1
      WHERE po.status = 'PUBLISHED'
        AND ${availabilitySql}
        AND (
          $3::text IS NULL
          OR EXISTS (
            SELECT 1
              FROM catalog.product_offer_destinations pod_filter
              JOIN catalog.destinations d_filter
                ON d_filter.id = pod_filter.destination_id
              JOIN catalog.regions r_filter
                ON r_filter.id = d_filter.region_id
             WHERE pod_filter.product_offer_id = po.id
               AND d_filter.code = $3
               AND d_filter.status = 'ACTIVE'
               AND r_filter.status = 'ACTIVE'
          )
        )
        AND (
          $4::text IS NULL
          OR po.code = $4
        )
      ORDER BY po.code`,
      [locale, environment, destinationCode, offerCode],
    );

    if (offerResult.rows.length === 0) {
      return [];
    }

    const offerIds = offerResult.rows.map((row) => row.id);
    const destinationResult =
      await this.database.query<OfferDestinationRow>(
        `SELECT
           pod.product_offer_id,
           d.code,
           COALESCE(dl_requested.name, dl_english.name) AS name,
           CASE
             WHEN dl_requested.destination_id IS NOT NULL
               THEN $1::text
             ELSE 'en'
           END AS source_locale
         FROM catalog.product_offer_destinations pod
         JOIN catalog.destinations d
           ON d.id = pod.destination_id
         JOIN catalog.regions r
           ON r.id = d.region_id
         JOIN catalog.destination_localizations dl_english
           ON dl_english.destination_id = d.id
          AND dl_english.locale = 'en'
         LEFT JOIN catalog.destination_localizations dl_requested
           ON dl_requested.destination_id = d.id
          AND dl_requested.locale = $1
        WHERE pod.product_offer_id = ANY($2::uuid[])
          AND d.status = 'ACTIVE'
          AND r.status = 'ACTIVE'
        ORDER BY pod.product_offer_id, d.code`,
        [locale, offerIds],
      );

    const destinations = new Map<
      string,
      StorefrontCatalogOfferContract['destinations']
    >();

    for (const row of destinationResult.rows) {
      const current = destinations.get(row.product_offer_id) ?? [];
      current.push({
        code: row.code,
        name: row.name,
        requestedLocale: locale,
        sourceLocale: row.source_locale,
      });
      destinations.set(row.product_offer_id, current);
    }

    return offerResult.rows.map((row) => ({
      code: row.code,
      productCode: row.product_code,
      durationDays: row.duration_days,
      dataPolicy: row.data_policy,
      dataAmountMb: row.data_amount_mb,
      dailyDataAmountMb: row.daily_data_amount_mb,
      fairUseDataAmountMb: row.fair_use_data_amount_mb,
      activationPolicy: row.activation_policy,
      hotspotSupported: row.hotspot_supported,
      phoneNumberIncluded: row.phone_number_included,
      networkName: row.network_name,
      title: row.title,
      shortDescription: row.short_description,
      requestedLocale: locale,
      sourceLocale: row.source_locale,
      destinations: destinations.get(row.id) ?? [],
      catalogVersion: row.version,
    }));
  }
}
