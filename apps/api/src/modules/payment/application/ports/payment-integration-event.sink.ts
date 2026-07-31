import type {
  PaymentSucceededIntegrationEventV1,
} from '@ysim/contracts';

export interface PaymentIntegrationEventSink {
  publish(
    event: PaymentSucceededIntegrationEventV1,
  ): Promise<void>;
}
