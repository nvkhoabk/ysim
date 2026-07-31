import { Injectable } from '@nestjs/common';
import { CustomerDeliveryActivationService } from './customer-delivery-activation.service.js';
import { CustomerDeliveryReadinessReason, CustomerDeliveryReadinessService } from './customer-delivery-readiness.service.js';

export type CustomerDeliveryRuntimeState = 'ACTIVE' | 'INACTIVE' | 'BLOCKED' | 'ERROR';
export type CustomerDeliveryRuntimeReason = CustomerDeliveryReadinessReason | 'READINESS_ERROR';

export interface CustomerDeliveryRuntimeStatus {
  state: CustomerDeliveryRuntimeState;
  reason: CustomerDeliveryRuntimeReason;
  schedulerEnabled: boolean;
  emailMode: 'disabled' | 'dry-run' | 'live' | 'invalid';
}

@Injectable()
export class CustomerDeliveryRuntimeStatusService {
  constructor(
    private readonly readiness: CustomerDeliveryReadinessService,
    private readonly activation: CustomerDeliveryActivationService,
  ) {}

  snapshot(env: NodeJS.ProcessEnv = process.env): CustomerDeliveryRuntimeStatus {
    try {
      const report = this.readiness.evaluate(env);
      const active = this.activation.isActive();
      if (active) {
        return report.ready && report.reason === 'READY'
          ? { state: 'ACTIVE', reason: 'READY', schedulerEnabled: true, emailMode: 'live' }
          : { state: 'ERROR', reason: 'READINESS_ERROR', schedulerEnabled: false, emailMode: 'invalid' };
      }
      if (report.ready) {
        return report.reason === 'READY'
          ? { state: 'INACTIVE', reason: 'READY', schedulerEnabled: true, emailMode: 'live' }
          : { state: 'ERROR', reason: 'READINESS_ERROR', schedulerEnabled: false, emailMode: 'invalid' };
      }
      switch (report.reason) {
        case 'CONFIG_INVALID':
        case 'SCHEDULER_DISABLED':
        case 'EMAIL_PROVIDER_NOT_LIVE':
          return { state: 'BLOCKED', reason: report.reason, schedulerEnabled: report.schedulerEnabled, emailMode: report.emailMode };
        default:
          return { state: 'ERROR', reason: 'READINESS_ERROR', schedulerEnabled: false, emailMode: 'invalid' };
      }
    } catch {
      return { state: 'ERROR', reason: 'READINESS_ERROR', schedulerEnabled: false, emailMode: 'invalid' };
    }
  }
}
