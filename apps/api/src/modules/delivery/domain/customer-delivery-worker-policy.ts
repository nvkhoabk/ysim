import { createHash } from 'node:crypto';
import type { DeliveryEmailAttachment } from './customer-delivery-email.js';

export type DeliveryLocale = 'vi' | 'lo' | 'en';
export interface DeliveryEmailAsset { position:number; planId:string; dataLabel:string; validityLabel:string; iccid:string; qrCode:string|null; shortLink:string|null; phoneNumber:string|null; }
export interface DeliveryEmailMessage { deliveryRequestId:string; orderNumber:string; locale:DeliveryLocale; assets:DeliveryEmailAsset[]; }
export interface DeliveryEmailReceipt { messageId:string; }
export interface MultipartDeliveryEmail { to:string; idempotencyKey:string; deliveryRequestId:string; part:number; partCount:number; assetStart:number; assetEnd:number; subject:string; text:string; html:string; attachments:DeliveryEmailAttachment[]; }
export interface CustomerEmailProvider { send(message:MultipartDeliveryEmail):Promise<DeliveryEmailReceipt>; }

export const normalizeRecipientEmail=(value:string):string=>{
  if(typeof value!=='string') throw new Error('recipientEmail is invalid');
  const normalized=value.trim().toLowerCase();
  if(normalized.length<3||normalized.length>320||!/^\S+@\S+\.\S+$/u.test(normalized)) throw new Error('recipientEmail is invalid');
  return normalized;
};
export const deliveryPartIdempotencyKey=(deliveryRequestId:string,part:number):string=>{
  if(!Number.isInteger(part)||part<1) throw new Error('part must be positive');
  return createHash('sha256').update(`delivery-email-part-v1|${deliveryRequestId}|${part}`,'utf8').digest('hex');
};
export const retryDelayMilliseconds=(attempt:number):number=>{if(!Number.isInteger(attempt)||attempt<1)throw new Error('attempt must be positive');return Math.min(300_000,5_000*(2**Math.min(attempt-1,6)));};
export const sanitizeDeliveryError=(error:unknown):string=>{const raw=error instanceof Error?error.message:'Customer delivery failed';return raw.replace(/(bearer|api[_-]?key|token|secret|password)\s*[:=]?\s*[^\s,;]+/giu,'$1=[REDACTED]').replace(/LPA:1\$[^\s]+/giu,'[REDACTED_LPA]').replace(/\b89\d{16,20}\b/gu,'[REDACTED_ICCID]').replace(/[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}/gu,'[REDACTED_EMAIL]').slice(0,500);};
export const assertOrderedAssets=(assets:DeliveryEmailAsset[],expected:number):void=>{if(assets.length!==expected||assets.some((asset,index)=>asset.position!==index+1))throw new Error('Customer delivery asset set is incomplete or unordered');};
