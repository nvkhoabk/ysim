import { Module } from '@nestjs/common';

import { HealthController } from './health.controller.js';
import { CatalogModule } from './modules/catalog/catalog.module.js';
import { OrganizationAgencyModule } from './modules/organization-agency/organization-agency.module.js';
import { PricingModule } from './modules/pricing/pricing.module.js';
import { SupplierManagementModule } from './modules/supplier-management/supplier-management.module.js';

@Module({
  imports: [
    OrganizationAgencyModule,
    CatalogModule,
    SupplierManagementModule,
    PricingModule,
  ],
  controllers: [HealthController],
})
export class AppModule {}
