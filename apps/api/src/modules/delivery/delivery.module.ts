import { Module } from '@nestjs/common';
import { PostgresService } from '../../platform/database/postgres.service.js';
import { EsimAssetCrypto } from '../fulfillment/infrastructure/esim-asset.crypto.js';
import { CustomerDeliveryActivationService } from './application/customer-delivery-activation.service.js';
import { CustomerDeliveryOperatorStatusQueryService } from './application/customer-delivery-operator-status-query.service.js';
import { CustomerDeliveryOperationsSummaryService } from './application/customer-delivery-operations-summary.service.js';
import { CustomerDeliveryDispatchService } from './application/customer-delivery-dispatch.service.js';
import { CustomerDeliveryPumpService } from './application/customer-delivery-pump.service.js';
import { CustomerDeliveryReadinessService } from './application/customer-delivery-readiness.service.js';
import { CustomerDeliveryRequestService } from './application/customer-delivery-request.service.js';
import { CustomerDeliveryRuntimeStatusService } from './application/customer-delivery-runtime-status.service.js';
import { CustomerDeliverySchedulerService } from './application/customer-delivery-scheduler.service.js';
import { CustomerDeliveryWorkerService } from './application/customer-delivery-worker.service.js';
import { CustomerDeliveryRepository } from './infrastructure/customer-delivery.repository.js';
import { CustomerDeliveryOperationsSummaryRepository } from './infrastructure/customer-delivery-operations-summary.repository.js';
import { CustomerDeliverySchedulerConfig } from './infrastructure/customer-delivery-scheduler.config.js';
import { CustomerDeliveryWorkerRepository } from './infrastructure/customer-delivery-worker.repository.js';
import { HttpCustomerEmailProvider } from './infrastructure/http-customer-email.provider.js';
import { CustomerDeliveryOperatorStatusController } from './customer-delivery-operator-status.controller.js';

@Module({
  controllers: [CustomerDeliveryOperatorStatusController],
  providers: [PostgresService, EsimAssetCrypto, CustomerDeliveryRepository, CustomerDeliveryWorkerRepository, CustomerDeliveryOperationsSummaryRepository, CustomerDeliveryRequestService, CustomerDeliveryWorkerService, HttpCustomerEmailProvider, CustomerDeliveryDispatchService, CustomerDeliveryPumpService, CustomerDeliverySchedulerConfig, CustomerDeliverySchedulerService, CustomerDeliveryReadinessService, CustomerDeliveryActivationService, CustomerDeliveryRuntimeStatusService, CustomerDeliveryOperatorStatusQueryService, CustomerDeliveryOperationsSummaryService],
  exports: [CustomerDeliveryRequestService, CustomerDeliveryWorkerService, HttpCustomerEmailProvider, CustomerDeliveryDispatchService, CustomerDeliveryPumpService, CustomerDeliverySchedulerConfig, CustomerDeliverySchedulerService, CustomerDeliveryReadinessService, CustomerDeliveryActivationService, CustomerDeliveryRuntimeStatusService, CustomerDeliveryOperatorStatusQueryService, CustomerDeliveryOperationsSummaryService],
})
export class DeliveryModule {}
