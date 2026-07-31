import { Injectable } from '@nestjs/common';

export interface CustomerDeliverySchedulerOptions {
  enabled: boolean;
  intervalMs: number;
  batchSize: number;
}

function parseBoundedInteger(name: string, raw: string | undefined, fallback: number, min: number, max: number): number {
  if (raw === undefined || raw === '') return fallback;
  if (!/^\d+$/.test(raw)) throw new Error(`${name} must be an integer between ${min} and ${max}`);
  const value = Number(raw);
  if (!Number.isSafeInteger(value) || value < min || value > max) {
    throw new Error(`${name} must be an integer between ${min} and ${max}`);
  }
  return value;
}

@Injectable()
export class CustomerDeliverySchedulerConfig implements CustomerDeliverySchedulerOptions {
  readonly enabled: boolean;
  readonly intervalMs: number;
  readonly batchSize: number;

  constructor(env: NodeJS.ProcessEnv = process.env) {
    const mode = env.YSIM_CUSTOMER_DELIVERY_SCHEDULER_ENABLED ?? 'false';
    if (mode !== 'true' && mode !== 'false') {
      throw new Error('YSIM_CUSTOMER_DELIVERY_SCHEDULER_ENABLED must be true or false');
    }
    this.enabled = mode === 'true';
    this.intervalMs = parseBoundedInteger('YSIM_CUSTOMER_DELIVERY_SCHEDULER_INTERVAL_MS', env.YSIM_CUSTOMER_DELIVERY_SCHEDULER_INTERVAL_MS, 30000, 1000, 3600000);
    this.batchSize = parseBoundedInteger('YSIM_CUSTOMER_DELIVERY_SCHEDULER_BATCH_SIZE', env.YSIM_CUSTOMER_DELIVERY_SCHEDULER_BATCH_SIZE, 25, 1, 100);
  }
}
