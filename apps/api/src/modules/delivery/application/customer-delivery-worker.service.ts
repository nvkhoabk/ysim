import { Injectable } from '@nestjs/common';
import { EsimAssetCrypto } from '../../fulfillment/infrastructure/esim-asset.crypto.js';
import { buildCustomerDeliveryEmails } from '../domain/customer-delivery-email.js';
import { assertOrderedAssets,deliveryPartIdempotencyKey,retryDelayMilliseconds,sanitizeDeliveryError,type CustomerEmailProvider } from '../domain/customer-delivery-worker-policy.js';
import { CustomerDeliveryWorkerRepository } from '../infrastructure/customer-delivery-worker.repository.js';
@Injectable()
export class CustomerDeliveryWorkerService {
 constructor(private readonly repository:CustomerDeliveryWorkerRepository,private readonly crypto:EsimAssetCrypto){}
 async processNext(provider:CustomerEmailProvider,now=new Date()){
  const claim=await this.repository.claim(now);if(!claim)return {kind:'IDLE'} as const;
  try{
   const encrypted=await this.repository.loadAssets(claim.deliveryRequestId);const assets=encrypted.map(asset=>({position:asset.position,planId:asset.planId,dataLabel:asset.dataLabel,validityLabel:asset.validityLabel,...this.crypto.decrypt(asset.encryptedPayload,asset.aad)}));assertOrderedAssets(assets,claim.expectedAssetCount);
   const emails=await buildCustomerDeliveryEmails({deliveryRequestId:claim.deliveryRequestId,orderNumber:claim.orderNumber,locale:claim.locale,assets});
   const existing=new Map((await this.repository.loadPartReceipts(claim.deliveryRequestId)).map(receipt=>[receipt.part,receipt]));const messageIds:string[]=[];
   for(const email of emails){const idempotencyKey=deliveryPartIdempotencyKey(claim.deliveryRequestId,email.part);const prior=existing.get(email.part);if(prior){if(prior.idempotencyKey!==idempotencyKey)throw new Error('Stored delivery part receipt is inconsistent');messageIds.push(prior.messageId);continue;}
    const receipt=await provider.send({to:claim.recipientEmail,idempotencyKey,deliveryRequestId:claim.deliveryRequestId,part:email.part,partCount:email.partCount,assetStart:email.assetStart,assetEnd:email.assetEnd,subject:email.subject,text:email.text,html:email.html,attachments:email.attachments});if(!receipt.messageId?.trim())throw new Error('Email provider receipt is invalid');if(!await this.repository.recordPartReceipt(claim,email,idempotencyKey,receipt.messageId,now))return {kind:'FENCED'} as const;messageIds.push(receipt.messageId);
   }
   if(!await this.repository.published(claim,emails.length,now))return {kind:'FENCED'} as const;return {kind:'PUBLISHED',outboxId:claim.outboxId,messageIds} as const;
  }catch(error){const message=sanitizeDeliveryError(error);const retryAt=new Date(now.getTime()+retryDelayMilliseconds(claim.version));if(!await this.repository.failed(claim,message,retryAt,now))return {kind:'FENCED'} as const;return {kind:'FAILED',outboxId:claim.outboxId,retryAt:retryAt.toISOString(),error:message} as const;}
 }
}
