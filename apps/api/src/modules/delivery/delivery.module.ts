import { Module } from '@nestjs/common';
import { PostgresService } from '../../platform/database/postgres.service.js';
import { EsimAssetCrypto } from '../fulfillment/infrastructure/esim-asset.crypto.js';
import { CustomerDeliveryRequestService } from './application/customer-delivery-request.service.js';
import { CustomerDeliveryWorkerService } from './application/customer-delivery-worker.service.js';
import { CustomerDeliveryRepository } from './infrastructure/customer-delivery.repository.js';
import { CustomerDeliveryWorkerRepository } from './infrastructure/customer-delivery-worker.repository.js';

@Module({providers:[PostgresService,EsimAssetCrypto,CustomerDeliveryRepository,CustomerDeliveryWorkerRepository,
  CustomerDeliveryRequestService,CustomerDeliveryWorkerService],exports:[CustomerDeliveryRequestService,CustomerDeliveryWorkerService]})
export class DeliveryModule {}
