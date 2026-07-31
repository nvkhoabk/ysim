import { Injectable } from '@nestjs/common';

import {
  buildEsimAssetAad,
  normalizeEsimAssetBatch,
  type DeliverableEsimBatchInput,
} from '../domain/esim-asset-policy.js';
import {
  EsimAssetCrypto,
} from '../infrastructure/esim-asset.crypto.js';
import {
  EsimAssetRepository,
  type PersistEsimAssetBatchResult,
  type PreparedEsimAssetRecord,
} from '../infrastructure/esim-asset.repository.js';

@Injectable()
export class EsimAssetIngestionService {
  constructor(
    private readonly repository:
      EsimAssetRepository,
    private readonly crypto:
      EsimAssetCrypto,
  ) {}

  async ingest(
    input: DeliverableEsimBatchInput,
  ): Promise<
    PersistEsimAssetBatchResult
  > {
    const batch =
      normalizeEsimAssetBatch(input);

    const records:
      PreparedEsimAssetRecord[] =
        batch.assets.map(
          (asset) => {
            const aad =
              buildEsimAssetAad(
                asset,
              );

            return {
              procurementRequestId:
                asset
                  .procurementRequestId,
              supplierSubmissionId:
                asset
                  .supplierSubmissionId,
              supplierCode:
                asset.supplierCode,
              supplierEnvironment:
                asset
                  .supplierEnvironment,
              supplierOrderId:
                asset
                  .supplierOrderId,
              supplierDetailId:
                asset.detailId,
              providerRequestId:
                asset
                  .providerRequestId,
              planId:
                asset.planId,
              dataLabel:
                asset.data,
              validityLabel:
                asset.validity,
              iccidFingerprint:
                this.crypto
                  .fingerprintIccid(
                    asset.iccid,
                  ),
              encryptedPayload:
                this.crypto.encrypt(
                  {
                    iccid:
                      asset.iccid,
                    qrCode:
                      asset.qrCode,
                    shortLink:
                      asset.shortLink,
                    phoneNumber:
                      asset.phoneNumber,
                  },
                  aad,
                ),
              capturedAt:
                asset.capturedAt,
            };
          },
        );

    return this.repository
      .persistBatch(records);
  }
}
