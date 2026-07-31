import { Injectable, OnModuleDestroy, OnModuleInit } from '@nestjs/common';
import { CustomerDeliverySchedulerConfig } from '../infrastructure/customer-delivery-scheduler.config.js';
import { CustomerDeliveryPumpService, CustomerDeliveryPumpSummary } from './customer-delivery-pump.service.js';

@Injectable()
export class CustomerDeliverySchedulerService implements OnModuleInit, OnModuleDestroy {
  private timer: ReturnType<typeof setTimeout> | undefined;
  private inFlight: Promise<CustomerDeliveryPumpSummary> | undefined;
  private stopped = true;

  constructor(private readonly pump: CustomerDeliveryPumpService, private readonly config: CustomerDeliverySchedulerConfig) {}

  onModuleInit(): void {
    if (this.config.enabled) this.start();
  }

  onModuleDestroy(): void {
    this.stop();
  }

  start(): void {
    if (!this.stopped) return;
    this.stopped = false;
    this.scheduleNext();
  }

  stop(): void {
    this.stopped = true;
    if (this.timer !== undefined) clearTimeout(this.timer);
    this.timer = undefined;
  }

  triggerNow(): Promise<CustomerDeliveryPumpSummary> {
    if (this.inFlight) return this.inFlight;
    const running = this.pump.runBatch(this.config.batchSize);
    this.inFlight = running;
    void running.finally(() => {
      if (this.inFlight === running) this.inFlight = undefined;
    }).catch(() => undefined);
    return running;
  }

  private scheduleNext(): void {
    if (this.stopped || this.timer !== undefined) return;
    this.timer = setTimeout(() => {
      this.timer = undefined;
      void this.triggerNow().catch(() => undefined).finally(() => this.scheduleNext());
    }, this.config.intervalMs);
    this.timer.unref?.();
  }
}
