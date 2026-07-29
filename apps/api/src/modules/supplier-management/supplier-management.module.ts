import { Module } from '@nestjs/common';

import { PostgresService } from '../../platform/database/postgres.service.js';
import { SupplierManagementService } from './application/supplier-management.service.js';
import { CatalogOfferReader } from './infrastructure/catalog-offer-reader.js';
import { SupplierManagementRepository } from './infrastructure/supplier-management.repository.js';
import { SupplierManagementController } from './presentation/supplier-management.controller.js';

@Module({
  controllers: [SupplierManagementController],
  providers: [
    PostgresService,
    CatalogOfferReader,
    SupplierManagementRepository,
    SupplierManagementService,
  ],
})
export class SupplierManagementModule {}
