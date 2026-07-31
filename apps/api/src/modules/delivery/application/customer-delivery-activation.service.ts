import { Injectable, OnModuleDestroy, OnModuleInit } from '@nestjs/common';
import { CustomerDeliveryReadinessReason, CustomerDeliveryReadinessService } from './customer-delivery-readiness.service.js';
import { CustomerDeliverySchedulerService } from './customer-delivery-scheduler.service.js';

export type CustomerDeliveryActivationReport =
  | { active: true; reason: 'READY' }
  | { active: false; reason: Exclude<CustomerDeliveryReadinessReason, 'READY'> | 'READINESS_ERROR' };

@Injectable()
export class CustomerDeliveryActivationService implements OnModuleInit, OnModuleDestroy {
  private active = false;

  constructor(
    private readonly readiness: CustomerDeliveryReadinessService,
    private readonly scheduler: CustomerDeliverySchedulerService,
  ) {}

  onModuleInit(): void {
    this.activate();
  }

  onModuleDestroy(): void {
    this.deactivate();
  }

  activate(env: NodeJS.ProcessEnv = process.env): CustomerDeliveryActivationReport {
    if (this.active) return { active: true, reason: 'READY' };
    try {
      const report = this.readiness.evaluate(env);
      if (!report.ready) {
        switch (report.reason) {
          case 'CONFIG_INVALID':
          case 'SCHEDULER_DISABLED':
          case 'EMAIL_PROVIDER_NOT_LIVE':
            return { active: false, reason: report.reason };
          default:
            return { active: false, reason: 'READINESS_ERROR' };
        }
      }
      if (report.reason !== 'READY') {
        return { active: false, reason: 'READINESS_ERROR' };
      }
      this.scheduler.start();
      this.active = true;
      return { active: true, reason: 'READY' };
    } catch {
      return { active: false, reason: 'READINESS_ERROR' };
    }
  }

  deactivate(): void {
    this.scheduler.stop();
    this.active = false;
  }
}
