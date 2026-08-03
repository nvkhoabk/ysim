import { Module } from '@nestjs/common';

import { PostgresService } from '../../platform/database/postgres.service.js';
import { GPayWebhookApplicationService } from './application/gpay-webhook-application.service.js';
import { PaymentIntegrationOutboxPublisher } from './application/payment-integration-outbox.publisher.js';
import { PaymentService } from './application/payment.service.js';
import { GPayGatewayClient } from './infrastructure/gpay/gpay.gateway.client.js';
import { GPayIntentProvider } from './infrastructure/gpay/gpay-intent.provider.js';
import { PaymentIntegrationOutboxRepository } from './infrastructure/payment-integration-outbox.repository.js';
import { PaymentRepository } from './infrastructure/payment.repository.js';
import { TestPaymentProvider } from './infrastructure/test-payment.provider.js';
import { PaymentGPayWebhookController } from './presentation/payment-gpay-webhook.controller.js';
import { PaymentPublicController } from './presentation/payment-public.controller.js';
import { PaymentTestProviderController } from './presentation/payment-test-provider.controller.js';

@Module({
  controllers: [
    PaymentPublicController,
    PaymentTestProviderController,
    PaymentGPayWebhookController,
  ],
  providers: [
    PostgresService,
    PaymentRepository,
    PaymentIntegrationOutboxRepository,
    PaymentIntegrationOutboxPublisher,
    TestPaymentProvider,
    PaymentService,
    {
      provide: GPayGatewayClient,
      useFactory: () => new GPayGatewayClient(),
    },
    GPayIntentProvider,
    GPayWebhookApplicationService,
  ],
  exports: [
    PaymentIntegrationOutboxPublisher,
  ],
})
export class PaymentModule {}
