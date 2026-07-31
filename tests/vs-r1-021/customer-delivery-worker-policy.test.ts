import { describe,expect,it } from 'vitest';
import { assertOrderedAssets,retryDelayMilliseconds,sanitizeDeliveryError } from '../../apps/api/src/modules/delivery/domain/customer-delivery-worker-policy.js';

describe('VS-R1-021 delivery worker policy',()=>{
  it('uses bounded exponential retry',()=>{expect(retryDelayMilliseconds(1)).toBe(5000);expect(retryDelayMilliseconds(3)).toBe(20000);expect(retryDelayMilliseconds(99)).toBe(300000)});
  it('rejects invalid attempts',()=>expect(()=>retryDelayMilliseconds(0)).toThrow());
  it('redacts bearer tokens',()=>expect(sanitizeDeliveryError(new Error('Bearer abc-secret'))).not.toContain('abc-secret'));
  it('redacts api keys',()=>expect(sanitizeDeliveryError(new Error('api_key=secret-value'))).not.toContain('secret-value'));
  it('redacts LPA values',()=>expect(sanitizeDeliveryError(new Error('LPA:1$server$token'))).not.toContain('server'));
  it('redacts ICCID-like values',()=>expect(sanitizeDeliveryError(new Error('89012345678901234567'))).not.toContain('89012345678901234567'));
  it('bounds persisted errors',()=>expect(sanitizeDeliveryError(new Error('x'.repeat(900))).length).toBe(500));
  it('accepts ordered complete assets',()=>expect(()=>assertOrderedAssets([{position:1} as never],1)).not.toThrow());
  it('rejects missing assets',()=>expect(()=>assertOrderedAssets([],1)).toThrow());
  it('rejects unordered assets',()=>expect(()=>assertOrderedAssets([{position:2} as never],1)).toThrow());
});
