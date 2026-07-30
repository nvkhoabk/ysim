import { Module } from '@nestjs/common';

import { PostgresService } from '../../platform/database/postgres.service.js';
import { GPayContractProbeService } from './application/gpay-contract-probe.service.js';
import { GPayWebhookApplicationService } from './application/gpay-webhook-application.service.js';
import { PaymentService } from './application/payment.service.js';
import { GPayClient } from './infrastructure/gpay/gpay.client.js';
import { GPayIntentProvider } from './infrastructure/gpay/gpay-intent.provider.js';
import { PaymentRepository } from './infrastructure/payment.repository.js';
import { TestPaymentProvider } from './infrastructure/test-payment.provider.js';
import { PaymentGPayProbeController } from './presentation/payment-gpay-probe.controller.js';
import { PaymentGPayWebhookController } from './presentation/payment-gpay-webhook.controller.js';
import { PaymentPublicController } from './presentation/payment-public.controller.js';
import { PaymentTestProviderController } from './presentation/payment-test-provider.controller.js';

@Module({
  controllers: [
    PaymentPublicController,
    PaymentTestProviderController,
    PaymentGPayProbeController,
    PaymentGPayWebhookController,
  ],
  providers: [
    PostgresService,
    PaymentRepository,
    TestPaymentProvider,
    PaymentService,
    GPayClient,
    GPayIntentProvider,
    GPayContractProbeService,
    GPayWebhookApplicationService,
  ],
})
export class PaymentModule {}
