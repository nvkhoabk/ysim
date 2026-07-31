import { Injectable } from '@nestjs/common';
import type {
  PaymentSucceededIntegrationEventV1,
} from '@ysim/contracts';

import type {
  PaymentIntegrationEventSink,
} from '../../payment/application/ports/payment-integration-event.sink.js';
import {
  buildProcurementRequest,
} from '../domain/procurement-request-policy.js';
import {
  ProcurementRequestRepository,
} from '../infrastructure/procurement-request.repository.js';
import {
  ProcurementSourceReader,
} from '../infrastructure/procurement-source.reader.js';

export type ConsumePaymentSuccessResult = {
  kind: 'CREATED' | 'REPLAY';
  requestId: string;
  status: 'PENDING_SUPPLIER';
};

@Injectable()
export class ProcurementPaymentSuccessSink
  implements PaymentIntegrationEventSink {
  constructor(
    private readonly sourceReader:
      ProcurementSourceReader,
    private readonly repository:
      ProcurementRequestRepository,
  ) {}

  async consume(
    event: PaymentSucceededIntegrationEventV1,
  ): Promise<ConsumePaymentSuccessResult> {
    const source =
      await this.sourceReader.findReadySource(
        event.orderId,
      );

    if (!source) {
      throw new Error(
        'PROCUREMENT_SOURCE_NOT_READY',
      );
    }

    const request =
      buildProcurementRequest(
        event,
        source,
      );
    const result =
      await this.repository
        .createFromPaymentSuccess(request);

    if (result.kind === 'CONFLICT') {
      throw new Error(
        'PROCUREMENT_REQUEST_CONFLICT',
      );
    }

    return result;
  }

  async publish(
    event: PaymentSucceededIntegrationEventV1,
  ): Promise<void> {
    await this.consume(event);
  }
}
