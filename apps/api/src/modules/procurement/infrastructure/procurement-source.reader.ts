import { Injectable } from '@nestjs/common';
import type { QueryResultRow } from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';
import type {
  ProcurementSourceSnapshot,
} from '../domain/procurement-request-policy.js';

interface ProcurementSourceRow extends QueryResultRow {
  order_id: string;
  order_number: string;
  product_offer_id: string;
  quantity: number;
  total_amount_minor: string;
  currency: 'VND' | 'LAK' | 'USD';
  order_status: string;
  order_payment_status: string;
  fulfillment_status: string;
  supplier_plan_mapping_id: string;
  supplier_environment_id: string;
  supplier_plan_id: string;
  supplier_code: string;
  supplier_environment:
    'SANDBOX' | 'PRODUCTION';
  supplier_contract_status: string;
  supplier_create_order_method: string;
  external_plan_id: string;
}

@Injectable()
export class ProcurementSourceReader {
  constructor(
    private readonly database: PostgresService,
  ) {}

  async findReadySource(
    orderId: string,
  ): Promise<ProcurementSourceSnapshot | null> {
    const result =
      await this.database.query<ProcurementSourceRow>(
        `SELECT
           so.id::text AS order_id,
           so.order_number,
           so.product_offer_id::text,
           so.quantity,
           so.total_amount_minor::text,
           so.currency,
           so.status AS order_status,
           so.payment_status AS order_payment_status,
           so.fulfillment_status,
           spm.id::text AS supplier_plan_mapping_id,
           spm.supplier_environment_id::text,
           sp.id::text AS supplier_plan_id,
           s.code AS supplier_code,
           se.environment AS supplier_environment,
           se.contract_status AS supplier_contract_status,
           se.create_order_method AS supplier_create_order_method,
           sp.external_plan_id
         FROM sales_order.orders so
         JOIN supplier_management.supplier_plan_mappings spm
           ON spm.product_offer_id = so.product_offer_id
          AND spm.status = 'ACTIVE'
         JOIN supplier_management.supplier_plans sp
           ON sp.id = spm.supplier_plan_id
          AND sp.supplier_environment_id =
              spm.supplier_environment_id
          AND sp.status = 'ACTIVE'
         JOIN supplier_management.supplier_environments se
           ON se.id = spm.supplier_environment_id
          AND se.environment = 'SANDBOX'
          AND se.contract_status = 'PROBED'
         JOIN supplier_management.suppliers s
           ON s.id = se.supplier_id
          AND s.status = 'ACTIVE'
        WHERE so.id = $1::uuid
          AND so.status = 'CONFIRMED'
          AND so.payment_status = 'PAID'
          AND so.fulfillment_status = 'UNFULFILLED'`,
        [orderId],
      );

    const row = result.rows[0];
    if (!row) return null;

    return {
      orderId: row.order_id,
      orderNumber: row.order_number,
      productOfferId: row.product_offer_id,
      quantity: row.quantity,
      totalAmountMinor:
        row.total_amount_minor,
      currency: row.currency,
      orderStatus: row.order_status,
      orderPaymentStatus:
        row.order_payment_status,
      fulfillmentStatus:
        row.fulfillment_status,
      supplierPlanMappingId:
        row.supplier_plan_mapping_id,
      supplierEnvironmentId:
        row.supplier_environment_id,
      supplierPlanId:
        row.supplier_plan_id,
      supplierCode: row.supplier_code,
      supplierEnvironment:
        row.supplier_environment,
      supplierContractStatus:
        row.supplier_contract_status,
      supplierCreateOrderMethod:
        row.supplier_create_order_method,
      externalPlanId:
        row.external_plan_id,
    };
  }
}
