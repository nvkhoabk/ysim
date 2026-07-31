import { randomUUID } from 'node:crypto';
import { Injectable } from '@nestjs/common';
import type { QueryResultRow } from 'pg';
import { PostgresService } from '../../../platform/database/postgres.service.js';
import type { EncryptedEsimPayload } from '../../fulfillment/infrastructure/esim-asset.crypto.js';

export interface ClaimedDelivery {
  outboxId: string; deliveryRequestId: string; orderNumber: string;
  locale: 'vi'|'lo'|'en'; expectedAssetCount: number; leaseToken: string; version: number;
}
export interface ClaimedAsset {
  position: number; planId: string; dataLabel: string; validityLabel: string;
  encryptedPayload: EncryptedEsimPayload; aad: string;
}
interface ClaimRow extends QueryResultRow { id:string; delivery_request_id:string; order_number:string; locale:'vi'|'lo'|'en'; expected_asset_count:number; version:number }

@Injectable()
export class CustomerDeliveryWorkerRepository {
  constructor(private readonly database: PostgresService) {}

  async claim(now: Date, leaseSeconds = 30): Promise<ClaimedDelivery|null> {
    return this.database.transaction(async client => {
      const selected = await client.query<ClaimRow>(`SELECT o.id::text, o.delivery_request_id::text,
        r.order_number, r.locale, r.expected_asset_count, o.version
        FROM delivery.integration_outbox o JOIN delivery.customer_delivery_requests r ON r.id=o.delivery_request_id
        WHERE o.status IN ('PENDING','FAILED') AND o.available_at <= $1::timestamptz
          AND (o.lease_until IS NULL OR o.lease_until <= $1::timestamptz)
        ORDER BY o.available_at,o.id FOR UPDATE OF o SKIP LOCKED LIMIT 1`, [now.toISOString()]);
      const row=selected.rows[0]; if(!row) return null;
      const leaseToken=randomUUID();
      const updated=await client.query(`UPDATE delivery.integration_outbox SET lease_token=$2::uuid,
        lease_until=$3::timestamptz, attempt_count=attempt_count+1, version=version+1, updated_at=$1::timestamptz
        WHERE id=$4::uuid AND version=$5::integer RETURNING version`,
        [now.toISOString(),leaseToken,new Date(now.getTime()+leaseSeconds*1000).toISOString(),row.id,row.version]);
      if(updated.rowCount!==1) return null;
      return {outboxId:row.id,deliveryRequestId:row.delivery_request_id,orderNumber:row.order_number,
        locale:row.locale,expectedAssetCount:row.expected_asset_count,leaseToken,version:updated.rows[0].version};
    });
  }

  async loadAssets(deliveryRequestId:string): Promise<ClaimedAsset[]> {
    const result=await this.database.query(`SELECT a.position,e.plan_id AS "planId",e.data_label AS "dataLabel",
      e.validity_label AS "validityLabel",e.encrypted_payload AS "encryptedPayload",
      concat(e.supplier_code,':',e.supplier_environment,':',e.supplier_detail_id) AS aad
      FROM delivery.customer_delivery_assets a JOIN fulfillment.esim_assets e ON e.id=a.asset_id
      WHERE a.delivery_request_id=$1::uuid AND e.status='READY' ORDER BY a.position`,[deliveryRequestId]);
    return result.rows as ClaimedAsset[];
  }

  async published(claim:ClaimedDelivery,messageId:string,now:Date):Promise<boolean>{
    const r=await this.database.query(`UPDATE delivery.integration_outbox SET status='PUBLISHED',published_at=$1,
      provider_message_id=$2,last_error=NULL,lease_until=NULL,lease_token=NULL,updated_at=$1,version=version+1
      WHERE id=$3::uuid AND lease_token=$4::uuid AND version=$5::integer`,
      [now.toISOString(),messageId,claim.outboxId,claim.leaseToken,claim.version]); return r.rowCount===1;
  }

  async failed(claim:ClaimedDelivery,error:string,retryAt:Date,now:Date):Promise<boolean>{
    const r=await this.database.query(`UPDATE delivery.integration_outbox SET status='FAILED',available_at=$1,last_error=$2,
      lease_until=NULL,lease_token=NULL,updated_at=$3,version=version+1
      WHERE id=$4::uuid AND lease_token=$5::uuid AND version=$6::integer`,
      [retryAt.toISOString(),error,now.toISOString(),claim.outboxId,claim.leaseToken,claim.version]); return r.rowCount===1;
  }
}
