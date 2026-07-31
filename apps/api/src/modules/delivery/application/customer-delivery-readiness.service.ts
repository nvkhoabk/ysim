import { Injectable } from '@nestjs/common';
import { loadCustomerEmailProviderConfig } from '../infrastructure/customer-email-provider.config.js';
import { CustomerDeliverySchedulerConfig } from '../infrastructure/customer-delivery-scheduler.config.js';

export type CustomerDeliveryReadinessReason =
  | 'READY'
  | 'CONFIG_INVALID'
  | 'SCHEDULER_DISABLED'
  | 'EMAIL_PROVIDER_NOT_LIVE';

export interface CustomerDeliveryReadinessReport {
  ready: boolean;
  reason: CustomerDeliveryReadinessReason;
  schedulerEnabled: boolean;
  emailMode: 'disabled' | 'dry-run' | 'live' | 'invalid';
}

@Injectable()
export class CustomerDeliveryReadinessService {
  evaluate(env: NodeJS.ProcessEnv = process.env): CustomerDeliveryReadinessReport {
    try {
      const scheduler = new CustomerDeliverySchedulerConfig(env);
      const email = loadCustomerEmailProviderConfig(env);
      if (!scheduler.enabled) {
        return { ready: false, reason: 'SCHEDULER_DISABLED', schedulerEnabled: false, emailMode: email.mode };
      }
      if (email.mode !== 'live') {
        return { ready: false, reason: 'EMAIL_PROVIDER_NOT_LIVE', schedulerEnabled: true, emailMode: email.mode };
      }
      return { ready: true, reason: 'READY', schedulerEnabled: true, emailMode: 'live' };
    } catch {
      return { ready: false, reason: 'CONFIG_INVALID', schedulerEnabled: false, emailMode: 'invalid' };
    }
  }
}
