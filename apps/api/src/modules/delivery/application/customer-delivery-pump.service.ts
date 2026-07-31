import { Injectable } from '@nestjs/common';
import { CustomerDeliveryDispatchService } from './customer-delivery-dispatch.service.js';

export interface CustomerDeliveryPumpSummary {
  attempted: number;
  published: number;
  failed: number;
  stopReason: 'IDLE' | 'FENCED' | 'BUDGET_EXHAUSTED';
}

/** Bounded runtime entry point for an external scheduler or worker process. */
@Injectable()
export class CustomerDeliveryPumpService {
  constructor(private readonly dispatch: CustomerDeliveryDispatchService) {}

  async runBatch(maxItems = 25): Promise<CustomerDeliveryPumpSummary> {
    if (!Number.isSafeInteger(maxItems) || maxItems < 1 || maxItems > 100) {
      throw new RangeError('maxItems must be an integer between 1 and 100');
    }

    let published = 0;
    let failed = 0;

    for (let attempted = 1; attempted <= maxItems; attempted += 1) {
      const result = await this.dispatch.processNext();

      switch (result.kind) {
        case 'IDLE':
        case 'FENCED':
          return { attempted, published, failed, stopReason: result.kind };
        case 'PUBLISHED':
          published += 1;
          break;
        case 'FAILED':
          failed += 1;
          break;
      }
    }

    return { attempted: maxItems, published, failed, stopReason: 'BUDGET_EXHAUSTED' };
  }
}
