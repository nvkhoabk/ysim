import { createHash } from 'node:crypto';

export class CustomerDeliveryPolicyError extends Error { constructor(message:string){super(message);this.name='CustomerDeliveryPolicyError';} }
export type CustomerDeliveryChannel='EMAIL';
export type CustomerDeliveryLocale='vi'|'lo'|'en';
export interface CustomerDeliveryRequestInput { salesOrderId:string; orderNumber:string; channel:CustomerDeliveryChannel; locale:CustomerDeliveryLocale; deliveryVersion:number; expectedAssetCount:number; assetIds:string[]; requestedAt:string; }
export interface NormalizedCustomerDeliveryRequest { salesOrderId:string; orderNumber:string; channel:CustomerDeliveryChannel; locale:CustomerDeliveryLocale; deliveryVersion:number; expectedAssetCount:number; assetIds:string[]; assetSetHash:string; deduplicationKey:string; requestedAt:string; recipientEmail?:string; outboxPayload:{schemaVersion:'ysim.customer-delivery-request/v1';salesOrderId:string;orderNumber:string;channel:CustomerDeliveryChannel;locale:CustomerDeliveryLocale;deliveryVersion:number;assetCount:number}; }
const UUID_PATTERN=/^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;
const ORDER_NUMBER_PATTERN=/^YS-[0-9]{8}-[0-9A-F]{12}$/u;
const sha256=(value:string)=>createHash('sha256').update(value,'utf8').digest('hex');
const normalizeUuid=(value:string,field:string)=>{if(typeof value!=='string'||!UUID_PATTERN.test(value))throw new CustomerDeliveryPolicyError(`${field} must be a UUID`);return value.toLowerCase();};
const normalizeTimestamp=(value:string)=>{const parsed=Date.parse(value);if(!Number.isFinite(parsed))throw new CustomerDeliveryPolicyError('requestedAt must be an ISO timestamp');return new Date(parsed).toISOString();};
export const normalizeCustomerDeliveryRequest=(input:CustomerDeliveryRequestInput):NormalizedCustomerDeliveryRequest=>{
  const salesOrderId=normalizeUuid(input.salesOrderId,'salesOrderId');
  if(typeof input.orderNumber!=='string'||!ORDER_NUMBER_PATTERN.test(input.orderNumber))throw new CustomerDeliveryPolicyError('orderNumber is invalid');
  if(input.channel!=='EMAIL')throw new CustomerDeliveryPolicyError('Only EMAIL delivery is supported');
  if(!['vi','lo','en'].includes(input.locale))throw new CustomerDeliveryPolicyError('locale is invalid');
  if(!Number.isInteger(input.deliveryVersion)||input.deliveryVersion<1||input.deliveryVersion>100)throw new CustomerDeliveryPolicyError('deliveryVersion must be 1..100');
  if(!Number.isInteger(input.expectedAssetCount)||input.expectedAssetCount<1||input.expectedAssetCount>20)throw new CustomerDeliveryPolicyError('expectedAssetCount must be 1..20');
  if(!Array.isArray(input.assetIds)||input.assetIds.length!==input.expectedAssetCount)throw new CustomerDeliveryPolicyError('Delivery Asset count mismatch');
  const seen=new Set<string>();const assetIds=input.assetIds.map((value,index)=>{const normalized=normalizeUuid(value,`assetIds[${index}]`);if(seen.has(normalized))throw new CustomerDeliveryPolicyError('Delivery Asset ID is duplicated');seen.add(normalized);return normalized;});
  const requestedAt=normalizeTimestamp(input.requestedAt);const assetSetHash=sha256(JSON.stringify(assetIds));
  const deduplicationKey=sha256(['delivery.customer_esim_requested.v1',salesOrderId,input.channel,String(input.deliveryVersion),assetSetHash].join('|'));
  return {salesOrderId,orderNumber:input.orderNumber,channel:input.channel,locale:input.locale,deliveryVersion:input.deliveryVersion,expectedAssetCount:input.expectedAssetCount,assetIds,assetSetHash,deduplicationKey,requestedAt,outboxPayload:{schemaVersion:'ysim.customer-delivery-request/v1',salesOrderId,orderNumber:input.orderNumber,channel:input.channel,locale:input.locale,deliveryVersion:input.deliveryVersion,assetCount:input.expectedAssetCount}};
};
export const bindDeliveryRequestId=(requestId:string,payload:NormalizedCustomerDeliveryRequest['outboxPayload'])=>({...payload,deliveryRequestId:normalizeUuid(requestId,'deliveryRequestId')});
