import { Injectable } from '@nestjs/common';
import type { QueryResultRow } from 'pg';

import { PostgresService } from '../../../platform/database/postgres.service.js';
import type {
  GigagoProcurementSnapshot,
} from '../domain/gigago-create-order-policy.js';

interface SubmissionSourceRow
  extends QueryResultRow {
  id: string;
  order_id: string;
  order_number: string;
  supplier_code: string;
  supplier_environment: string;
  external_plan_id: string;
  quantity: number;
  status: string;
}

@Injectable()
export class ProcurementSubmissionReader {
  constructor(
    private readonly database:
      PostgresService,
  ) {}

  async findById(
    procurementRequestId: string,
  ): Promise<
    GigagoProcurementSnapshot | null
  > {
    const result =
      await this.database
        .query<SubmissionSourceRow>(
          `SELECT
             id::text,
             order_id::text,
             order_number,
             supplier_code,
             supplier_environment,
             external_plan_id,
             quantity,
             status
           FROM procurement.requests
          WHERE id = $1::uuid
            AND supplier_code = 'GIGAGO'
            AND supplier_environment =
                'SANDBOX'
            AND status IN (
              'PENDING_SUPPLIER',
              'SUBMITTED'
            )`,
          [procurementRequestId],
        );

    const row = result.rows[0];
    if (!row) return null;

    return {
      procurementRequestId: row.id,
      orderId: row.order_id,
      orderNumber: row.order_number,
      supplierCode: row.supplier_code,
      supplierEnvironment:
        row.supplier_environment,
      externalPlanId:
        row.external_plan_id,
      quantity: row.quantity,
      status: row.status,
    };
  }
}
