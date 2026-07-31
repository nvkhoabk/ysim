import { Module } from '@nestjs/common';

import { PostgresService } from '../../platform/database/postgres.service.js';
import { PaymentModule } from '../payment/payment.module.js';
import { ProcurementOutboxConsumerService } from './application/procurement-outbox-consumer.service.js';
import { ProcurementPaymentSuccessSink } from './application/procurement-payment-success.sink.js';
import { ProcurementRequestRepository } from './infrastructure/procurement-request.repository.js';
import { ProcurementSourceReader } from './infrastructure/procurement-source.reader.js';

@Module({
  imports: [PaymentModule],
  providers: [
    PostgresService,
    ProcurementSourceReader,
    ProcurementRequestRepository,
    ProcurementPaymentSuccessSink,
    ProcurementOutboxConsumerService,
  ],
  exports: [
    ProcurementPaymentSuccessSink,
    ProcurementOutboxConsumerService,
  ],
})
export class ProcurementModule {}
