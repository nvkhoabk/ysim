import { Injectable } from '@nestjs/common';
import { HttpCustomerEmailProvider } from '../infrastructure/http-customer-email.provider.js';
import { CustomerDeliveryWorkerService } from './customer-delivery-worker.service.js';

/** Runtime composition boundary for customer-delivery dispatch.
 *
 * The worker keeps its provider-explicit API for deterministic tests and
 * alternative adapters. Runtime callers use this service, which always routes
 * through the configured safe provider introduced by VS-R1-024.
 */
@Injectable()
export class CustomerDeliveryDispatchService {
  constructor(
    private readonly worker: CustomerDeliveryWorkerService,
    private readonly provider: HttpCustomerEmailProvider,
  ) {}

  async processNext(now = new Date()) {
    return this.worker.processNext(this.provider, now);
  }
}
