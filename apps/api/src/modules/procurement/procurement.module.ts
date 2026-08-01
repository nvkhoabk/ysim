import { Module } from '@nestjs/common';

import { PostgresService } from '../../platform/database/postgres.service.js';
import { PaymentModule } from '../payment/payment.module.js';
import { GigagoOrderReadbackService } from './application/gigago-order-readback.service.js';
import { GigagoProcurementSubmissionService } from './application/gigago-procurement-submission.service.js';
import { ProcurementOutboxConsumerService } from './application/procurement-outbox-consumer.service.js';
import { ProcurementPaymentSuccessSink } from './application/procurement-payment-success.sink.js';
import { GigagoCreateOrderClient, GigagoOrderReadbackClient } from './infrastructure/gigago/gigago.client.js';
import { ProcurementRequestRepository } from './infrastructure/procurement-request.repository.js';
import { ProcurementSourceReader } from './infrastructure/procurement-source.reader.js';
import { ProcurementSubmissionReader } from './infrastructure/procurement-submission.reader.js';
import { SupplierSubmissionRepository } from './infrastructure/supplier-submission.repository.js';

@Module({
  imports: [PaymentModule],
  providers: [
    PostgresService,
    ProcurementSourceReader,
    ProcurementRequestRepository,
    ProcurementPaymentSuccessSink,
    ProcurementOutboxConsumerService,
    ProcurementSubmissionReader,
    SupplierSubmissionRepository,
    {
      provide:
        GigagoCreateOrderClient,
      useFactory: () =>
        new GigagoCreateOrderClient(),
    },
    {
      provide:
        GigagoOrderReadbackClient,
      useFactory: () =>
        new GigagoOrderReadbackClient(),
    },
    GigagoProcurementSubmissionService,
    GigagoOrderReadbackService,
  ],
  exports: [
    ProcurementPaymentSuccessSink,
    ProcurementOutboxConsumerService,
    GigagoProcurementSubmissionService,
    GigagoOrderReadbackService,
  ],
})
export class ProcurementModule {}
