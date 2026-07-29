import { Injectable } from '@nestjs/common';
import type {
  CatalogOfferForSupplierMappingContract,
  DataPolicy,
  ProductOfferStatus,
} from '@ysim/contracts';
import type { QueryResultRow } from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';

interface CatalogOfferRow extends QueryResultRow {
  id: string;
  code: string;
  status: ProductOfferStatus;
  duration_days: number;
  data_policy: DataPolicy;
  data_amount_mb: number | null;
  daily_data_amount_mb: number | null;
  fair_use_data_amount_mb: number | null;
  hotspot_supported: boolean;
  phone_number_included: boolean;
  destination_codes: string[];
}

@Injectable()
export class CatalogOfferReader {
  constructor(private readonly database: PostgresService) {}

  async findOffer(
    productOfferId: string,
  ): Promise<CatalogOfferForSupplierMappingContract | null> {
    const result = await this.database.query<CatalogOfferRow>(
      `SELECT
         o.id,
         o.code,
         o.status,
         o.duration_days,
         o.data_policy,
         o.data_amount_mb,
         o.daily_data_amount_mb,
         o.fair_use_data_amount_mb,
         o.hotspot_supported,
         o.phone_number_included,
         ARRAY_AGG(d.code ORDER BY d.code) AS destination_codes
       FROM catalog.product_offers o
       JOIN catalog.product_offer_destinations pod
         ON pod.product_offer_id = o.id
       JOIN catalog.destinations d
         ON d.id = pod.destination_id
      WHERE o.id = $1
      GROUP BY
         o.id,
         o.code,
         o.status,
         o.duration_days,
         o.data_policy,
         o.data_amount_mb,
         o.daily_data_amount_mb,
         o.fair_use_data_amount_mb,
         o.hotspot_supported,
         o.phone_number_included`,
      [productOfferId],
    );

    const row = result.rows[0];
    if (!row) return null;

    return {
      id: row.id,
      code: row.code,
      status: row.status,
      durationDays: row.duration_days,
      dataPolicy: row.data_policy,
      dataAmountMb: row.data_amount_mb,
      dailyDataAmountMb: row.daily_data_amount_mb,
      fairUseDataAmountMb: row.fair_use_data_amount_mb,
      hotspotSupported: row.hotspot_supported,
      phoneNumberIncluded: row.phone_number_included,
      destinationCodes: row.destination_codes,
    };
  }
}
