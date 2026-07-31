import { Module } from '@nestjs/common';

import {
  PostgresService,
} from '../../platform/database/postgres.service.js';
import {
  CustomerDeliveryRequestService,
} from './application/customer-delivery-request.service.js';
import {
  CustomerDeliveryRepository,
} from './infrastructure/customer-delivery.repository.js';

@Module({
  providers: [
    PostgresService,
    CustomerDeliveryRepository,
    CustomerDeliveryRequestService,
  ],
  exports: [
    CustomerDeliveryRequestService,
  ],
})
export class DeliveryModule {}
