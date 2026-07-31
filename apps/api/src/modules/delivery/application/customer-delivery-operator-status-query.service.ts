import { createHash, timingSafeEqual } from 'node:crypto';
import { Injectable } from '@nestjs/common';
import { CustomerDeliveryRuntimeStatus, CustomerDeliveryRuntimeStatusService } from './customer-delivery-runtime-status.service.js';

export type CustomerDeliveryOperatorStatusQueryResult =
  | { authorized: true; status: CustomerDeliveryRuntimeStatus }
  | { authorized: false; reason: 'ACCESS_DENIED' | 'CONFIG_INVALID' | 'STATUS_UNAVAILABLE' };

@Injectable()
export class CustomerDeliveryOperatorStatusQueryService {
  constructor(private readonly runtimeStatus: CustomerDeliveryRuntimeStatusService) {}

  query(presentedCredential: string, env: NodeJS.ProcessEnv = process.env): CustomerDeliveryOperatorStatusQueryResult {
    const configuredCredential = env.CUSTOMER_DELIVERY_OPERATOR_STATUS_TOKEN;
    if (typeof configuredCredential !== 'string' || configuredCredential.length < 32) {
      return { authorized: false, reason: 'CONFIG_INVALID' };
    }
    if (typeof presentedCredential !== 'string' || presentedCredential.length === 0 || !this.matches(presentedCredential, configuredCredential)) {
      return { authorized: false, reason: 'ACCESS_DENIED' };
    }
    try {
      return { authorized: true, status: this.runtimeStatus.snapshot(env) };
    } catch {
      return { authorized: false, reason: 'STATUS_UNAVAILABLE' };
    }
  }

  private matches(presented: string, configured: string): boolean {
    const digest = (value: string) => createHash('sha256').update(value, 'utf8').digest();
    return timingSafeEqual(digest(presented), digest(configured));
  }
}
