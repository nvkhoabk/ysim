import { Injectable } from '@nestjs/common';
import { EsimAssetCrypto } from '../../fulfillment/infrastructure/esim-asset.crypto.js';
import { assertOrderedAssets, retryDelayMilliseconds, sanitizeDeliveryError, type CustomerEmailProvider } from '../domain/customer-delivery-worker-policy.js';
import { CustomerDeliveryWorkerRepository } from '../infrastructure/customer-delivery-worker.repository.js';

@Injectable()
export class CustomerDeliveryWorkerService {
  constructor(private readonly repository:CustomerDeliveryWorkerRepository, private readonly crypto:EsimAssetCrypto) {}
  async processNext(provider:CustomerEmailProvider, now=new Date()) {
    const claim=await this.repository.claim(now); if(!claim) return {kind:'IDLE'} as const;
    try {
      const encrypted=await this.repository.loadAssets(claim.deliveryRequestId);
      const assets=encrypted.map(asset=>({position:asset.position,planId:asset.planId,dataLabel:asset.dataLabel,
        validityLabel:asset.validityLabel,...this.crypto.decrypt(asset.encryptedPayload,asset.aad)}));
      assertOrderedAssets(assets,claim.expectedAssetCount);
      const receipt=await provider.send({deliveryRequestId:claim.deliveryRequestId,orderNumber:claim.orderNumber,locale:claim.locale,assets});
      if(!receipt.messageId) throw new Error('Email provider receipt is invalid');
      if(!await this.repository.published(claim,receipt.messageId,now)) return {kind:'FENCED'} as const;
      return {kind:'PUBLISHED',outboxId:claim.outboxId,messageId:receipt.messageId} as const;
    } catch(error) {
      const message=sanitizeDeliveryError(error);
      const retryAt=new Date(now.getTime()+retryDelayMilliseconds(claim.version));
      if(!await this.repository.failed(claim,message,retryAt,now)) return {kind:'FENCED'} as const;
      return {kind:'FAILED',outboxId:claim.outboxId,retryAt:retryAt.toISOString(),error:message} as const;
    }
  }
}
