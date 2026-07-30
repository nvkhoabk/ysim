import { Module } from '@nestjs/common';

import { HealthController } from './health.controller.js';
import { CatalogModule } from './modules/catalog/catalog.module.js';
import { OrganizationAgencyModule } from './modules/organization-agency/organization-agency.module.js';
import { PaymentModule } from './modules/payment/payment.module.js';
import { PricingModule } from './modules/pricing/pricing.module.js';
import { SalesOrderModule } from './modules/sales-order/sales-order.module.js';
import { SupplierManagementModule } from './modules/supplier-management/supplier-management.module.js';

@Module({
  imports: [
    OrganizationAgencyModule,
    CatalogModule,
    SupplierManagementModule,
    PricingModule,
    SalesOrderModule,
    PaymentModule,
  ],
  controllers: [HealthController],
})
export class AppModule {}
