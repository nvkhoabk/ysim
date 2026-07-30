import { Module } from '@nestjs/common';

import { PostgresService } from '../../platform/database/postgres.service.js';
import { PaymentService } from './application/payment.service.js';
import { PaymentRepository } from './infrastructure/payment.repository.js';
import { TestPaymentProvider } from './infrastructure/test-payment.provider.js';
import { PaymentPublicController } from './presentation/payment-public.controller.js';
import { PaymentTestProviderController } from './presentation/payment-test-provider.controller.js';

@Module({
  controllers: [
    PaymentPublicController,
    PaymentTestProviderController,
  ],
  providers: [
    PostgresService,
    PaymentRepository,
    TestPaymentProvider,
    PaymentService,
  ],
})
export class PaymentModule {}
