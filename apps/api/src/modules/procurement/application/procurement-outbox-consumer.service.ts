import { Injectable } from '@nestjs/common';

import {
  PaymentIntegrationOutboxPublisher,
  type PublishPaymentOutboxOptions,
  type PublishPaymentOutboxResult,
} from '../../payment/application/payment-integration-outbox.publisher.js';
import {
  ProcurementPaymentSuccessSink,
} from './procurement-payment-success.sink.js';

@Injectable()
export class ProcurementOutboxConsumerService {
  constructor(
    private readonly publisher:
      PaymentIntegrationOutboxPublisher,
    private readonly sink:
      ProcurementPaymentSuccessSink,
  ) {}

  processNext(
    options: PublishPaymentOutboxOptions = {},
  ): Promise<PublishPaymentOutboxResult> {
    return this.publisher.publishNext(
      this.sink,
      options,
    );
  }
}
