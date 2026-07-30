import { Module } from '@nestjs/common';

import { PostgresService } from '../../platform/database/postgres.service.js';
import { SalesOrderService } from './application/sales-order.service.js';
import { SalesOrderRepository } from './infrastructure/sales-order.repository.js';
import { SalesOrderPublicController } from './presentation/sales-order-public.controller.js';

@Module({
  controllers: [SalesOrderPublicController],
  providers: [
    PostgresService,
    SalesOrderRepository,
    SalesOrderService,
  ],
})
export class SalesOrderModule {}
