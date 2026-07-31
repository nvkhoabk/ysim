import { Module } from '@nestjs/common';
import { PostgresService } from '../../platform/database/postgres.service.js';
import { EsimAssetCrypto } from '../fulfillment/infrastructure/esim-asset.crypto.js';
import { CustomerDeliveryDispatchService } from './application/customer-delivery-dispatch.service.js';
import { CustomerDeliveryPumpService } from './application/customer-delivery-pump.service.js';
import { CustomerDeliveryRequestService } from './application/customer-delivery-request.service.js';
import { CustomerDeliverySchedulerService } from './application/customer-delivery-scheduler.service.js';
import { CustomerDeliveryWorkerService } from './application/customer-delivery-worker.service.js';
import { CustomerDeliveryRepository } from './infrastructure/customer-delivery.repository.js';
import { CustomerDeliverySchedulerConfig } from './infrastructure/customer-delivery-scheduler.config.js';
import { CustomerDeliveryWorkerRepository } from './infrastructure/customer-delivery-worker.repository.js';
import { HttpCustomerEmailProvider } from './infrastructure/http-customer-email.provider.js';

@Module({
  providers: [PostgresService, EsimAssetCrypto, CustomerDeliveryRepository, CustomerDeliveryWorkerRepository, CustomerDeliveryRequestService, CustomerDeliveryWorkerService, HttpCustomerEmailProvider, CustomerDeliveryDispatchService, CustomerDeliveryPumpService, CustomerDeliverySchedulerConfig, CustomerDeliverySchedulerService],
  exports: [CustomerDeliveryRequestService, CustomerDeliveryWorkerService, HttpCustomerEmailProvider, CustomerDeliveryDispatchService, CustomerDeliveryPumpService, CustomerDeliverySchedulerConfig, CustomerDeliverySchedulerService],
})
export class DeliveryModule {}
