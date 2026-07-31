import { Injectable } from '@nestjs/common';
import {
  CustomerDeliveryOperationsCounts,
  CustomerDeliveryOperationsSummaryRepository,
} from '../infrastructure/customer-delivery-operations-summary.repository.js';

export type CustomerDeliveryOperationsSummaryResult =
  | {
      available: true;
      summary: CustomerDeliveryOperationsCounts & { generatedAt: string };
    }
  | { available: false; reason: 'SUMMARY_UNAVAILABLE' };

const validCount = (value: number): boolean =>
  Number.isSafeInteger(value) && value >= 0 && value <= 1_000_000_000;

@Injectable()
export class CustomerDeliveryOperationsSummaryService {
  constructor(
    private readonly repository: CustomerDeliveryOperationsSummaryRepository,
  ) {}

  async snapshot(now: Date = new Date()): Promise<CustomerDeliveryOperationsSummaryResult> {
    if (!(now instanceof Date) || !Number.isFinite(now.getTime())) {
      return { available: false, reason: 'SUMMARY_UNAVAILABLE' };
    }
    try {
      const counts = await this.repository.load(now);
      const values = [
        counts.pending,
        counts.failed,
        counts.published,
        counts.inFlight,
        counts.actionable,
      ];
      if (
        !values.every(validCount) ||
        counts.inFlight > counts.pending + counts.failed ||
        counts.actionable > counts.pending + counts.failed ||
        counts.inFlight + counts.actionable > counts.pending + counts.failed
      ) {
        return { available: false, reason: 'SUMMARY_UNAVAILABLE' };
      }
      if (
        counts.oldestActionableAt !== null &&
        !Number.isFinite(Date.parse(counts.oldestActionableAt))
      ) {
        return { available: false, reason: 'SUMMARY_UNAVAILABLE' };
      }
      return {
        available: true,
        summary: {
          generatedAt: now.toISOString(),
          pending: counts.pending,
          failed: counts.failed,
          published: counts.published,
          inFlight: counts.inFlight,
          actionable: counts.actionable,
          oldestActionableAt: counts.oldestActionableAt,
        },
      };
    } catch {
      return { available: false, reason: 'SUMMARY_UNAVAILABLE' };
    }
  }
}
