import { describe,expect,it,vi } from 'vitest';
import { CustomerDeliveryWorkerService } from '../../apps/api/src/modules/delivery/application/customer-delivery-worker.service.js';
import { deliveryPartIdempotencyKey,normalizeRecipientEmail,sanitizeDeliveryError } from '../../apps/api/src/modules/delivery/domain/customer-delivery-worker-policy.js';

const claim={outboxId:'00000000-0000-4000-8000-000000000001',deliveryRequestId:'00000000-0000-4000-8000-000000000002',orderNumber:'YS-20260731-023ABCDEF023',recipientEmail:'buyer@example.com',locale:'vi' as const,expectedAssetCount:6,leaseToken:'00000000-0000-4000-8000-000000000003',version:1};
const encrypted=Array.from({length:6},(_,index)=>({position:index+1,planId:'JP-7D',dataLabel:'5 GB/ngày',validityLabel:'7 ngày',encryptedPayload:{} as never,aad:`GIGAGO:SANDBOX:${index+1}`}));
const decrypted={iccid:'89012345678901234567',qrCode:'LPA:1$sm-dp.example$activation',shortLink:null,phoneNumber:null};

describe('VS-R1-023 recipient snapshot and multipart dispatch',()=>{
 it('normalizes recipient snapshot',()=>expect(normalizeRecipientEmail(' Buyer@Example.COM ')).toBe('buyer@example.com'));
 it('rejects invalid recipient snapshot',()=>expect(()=>normalizeRecipientEmail('not-email')).toThrow());
 it('creates stable per-part idempotency keys',()=>expect(deliveryPartIdempotencyKey(claim.deliveryRequestId,1)).toBe(deliveryPartIdempotencyKey(claim.deliveryRequestId,1)));
 it('uses different keys for different parts',()=>expect(deliveryPartIdempotencyKey(claim.deliveryRequestId,1)).not.toBe(deliveryPartIdempotencyKey(claim.deliveryRequestId,2)));
 it('rejects invalid part numbers',()=>expect(()=>deliveryPartIdempotencyKey(claim.deliveryRequestId,0)).toThrow());
 it('redacts recipient email from persisted errors',()=>expect(sanitizeDeliveryError(new Error('send buyer@example.com failed'))).not.toContain('buyer@example.com'));
 it('dispatches six assets as two parts with recipient and keys',async()=>{
  const receipts:any[]=[];const repository={claim:vi.fn().mockResolvedValue(claim),loadAssets:vi.fn().mockResolvedValue(encrypted),loadPartReceipts:vi.fn().mockResolvedValue([]),recordPartReceipt:vi.fn(async(_:unknown,email:any,key:string,messageId:string)=>{receipts.push({part:email.part,key,messageId});return true;}),published:vi.fn().mockResolvedValue(true),failed:vi.fn().mockResolvedValue(true)};
  const provider={send:vi.fn(async(message:any)=>({messageId:`provider-${message.part}`}))};const service=new CustomerDeliveryWorkerService(repository as never,{decrypt:()=>decrypted} as never);const result=await service.processNext(provider);
  expect(result.kind).toBe('PUBLISHED');expect(provider.send).toHaveBeenCalledTimes(2);expect(provider.send.mock.calls[0][0].to).toBe('buyer@example.com');expect(provider.send.mock.calls.map(call=>call[0].idempotencyKey)).toEqual(receipts.map(x=>x.key));
 });
 it('persists each receipt before publishing the request',async()=>{
	  const order:string[]=[];const repository={claim:async()=>claim,loadAssets:async()=>encrypted,loadPartReceipts:async()=>[],recordPartReceipt:async(_:unknown,email:any)=>{order.push(`receipt-${email.part}`);return true;},published:async()=>{order.push('published');return true;},failed:async()=>true};const provider={send:async(message:any)=>{order.push(`send-${message.part}`);return {messageId:`m-${message.part}`};}};await new CustomerDeliveryWorkerService(repository as never,{decrypt:()=>decrypted} as never).processNext(provider);expect(order).toEqual(['send-1','receipt-1','send-2','receipt-2','published']);
 });
 it('retry skips a part that already has a receipt',async()=>{
  const prior={part:1,idempotencyKey:deliveryPartIdempotencyKey(claim.deliveryRequestId,1),messageId:'provider-1'};const repository={claim:async()=>claim,loadAssets:async()=>encrypted,loadPartReceipts:async()=>[prior],recordPartReceipt:vi.fn().mockResolvedValue(true),published:vi.fn().mockResolvedValue(true),failed:vi.fn().mockResolvedValue(true)};const provider={send:vi.fn(async(message:any)=>({messageId:`provider-${message.part}`}))};const result=await new CustomerDeliveryWorkerService(repository as never,{decrypt:()=>decrypted} as never).processNext(provider);expect(result.kind).toBe('PUBLISHED');expect(provider.send).toHaveBeenCalledTimes(1);expect(provider.send.mock.calls[0][0].part).toBe(2);
 });
 it('partial failure records failure without publishing',async()=>{
  const repository={claim:async()=>claim,loadAssets:async()=>encrypted,loadPartReceipts:async()=>[],recordPartReceipt:vi.fn().mockResolvedValue(true),published:vi.fn().mockResolvedValue(true),failed:vi.fn().mockResolvedValue(true)};const provider={send:vi.fn(async(message:any)=>{if(message.part===2)throw new Error('provider unavailable');return {messageId:'provider-1'};})};const result=await new CustomerDeliveryWorkerService(repository as never,{decrypt:()=>decrypted} as never).processNext(provider);expect(result.kind).toBe('FAILED');expect(repository.recordPartReceipt).toHaveBeenCalledTimes(1);expect(repository.published).not.toHaveBeenCalled();expect(repository.failed).toHaveBeenCalledTimes(1);
 });
 it('fails closed on empty provider receipt',async()=>{const repository={claim:async()=>({...claim,expectedAssetCount:1}),loadAssets:async()=>encrypted.slice(0,1),loadPartReceipts:async()=>[],recordPartReceipt:vi.fn(),published:vi.fn(),failed:vi.fn().mockResolvedValue(true)};const result=await new CustomerDeliveryWorkerService(repository as never,{decrypt:()=>decrypted} as never).processNext({send:async()=>({messageId:''})});expect(result.kind).toBe('FAILED');expect(repository.recordPartReceipt).not.toHaveBeenCalled();});
 it('returns fenced when receipt persistence loses the lease',async()=>{const repository={claim:async()=>({...claim,expectedAssetCount:1}),loadAssets:async()=>encrypted.slice(0,1),loadPartReceipts:async()=>[],recordPartReceipt:async()=>false,published:vi.fn(),failed:vi.fn()};const result=await new CustomerDeliveryWorkerService(repository as never,{decrypt:()=>decrypted} as never).processNext({send:async()=>({messageId:'m-1'})});expect(result.kind).toBe('FENCED');expect(repository.published).not.toHaveBeenCalled();});
});
