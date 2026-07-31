import { createHash } from 'node:crypto';
import { Injectable } from '@nestjs/common';
import type { CustomerEmailProvider,DeliveryEmailReceipt,MultipartDeliveryEmail } from '../domain/customer-delivery-worker-policy.js';
import { loadCustomerEmailProviderConfig,type CustomerEmailProviderConfig } from './customer-email-provider.config.js';
export class CustomerEmailProviderError extends Error{constructor(public readonly category:'DISABLED'|'RETRYABLE'|'PERMANENT'|'INVALID_RECEIPT',message:string){super(message);this.name='CustomerEmailProviderError';}}
type FetchLike=(input:string,init:RequestInit)=>Promise<Pick<Response,'ok'|'status'|'json'>>;
@Injectable()
export class HttpCustomerEmailProvider implements CustomerEmailProvider{
 constructor(private readonly config:CustomerEmailProviderConfig=loadCustomerEmailProviderConfig(),private readonly request:FetchLike=fetch){}
 async send(message:MultipartDeliveryEmail):Promise<DeliveryEmailReceipt>{
  if(this.config.mode==='disabled')throw new CustomerEmailProviderError('DISABLED','Customer email delivery is disabled');
  if(this.config.mode==='dry-run')return {messageId:`dry-${createHash('sha256').update(message.idempotencyKey).digest('hex').slice(0,32)}`};
  const controller=new AbortController();const timer=setTimeout(()=>controller.abort(),this.config.timeoutMs);
  try{
   const response=await this.request(this.config.endpoint!,{method:'POST',headers:{authorization:`Bearer ${this.config.token}`,'content-type':'application/json','idempotency-key':message.idempotencyKey},body:JSON.stringify({...message,attachments:message.attachments.map(item=>({...item,content:item.content.toString('base64')}))}),signal:controller.signal});
   if(!response.ok)throw new CustomerEmailProviderError(response.status===408||response.status===429||response.status>=500?'RETRYABLE':'PERMANENT',`Customer email provider returned HTTP ${response.status}`);
   const body=await response.json() as {messageId?:unknown};if(typeof body.messageId!=='string'||!body.messageId.trim())throw new CustomerEmailProviderError('INVALID_RECEIPT','Customer email provider receipt is invalid');
   return {messageId:body.messageId.trim()};
  }catch(error){if(error instanceof CustomerEmailProviderError)throw error;throw new CustomerEmailProviderError('RETRYABLE',error instanceof Error&&error.name==='AbortError'?'Customer email provider timed out':'Customer email provider request failed');}
  finally{clearTimeout(timer);}
 }
}
