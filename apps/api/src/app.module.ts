import { Module } from '@nestjs/common';

import { HealthController } from './health.controller.js';
import { CatalogModule } from './modules/catalog/catalog.module.js';
import { OrganizationAgencyModule } from './modules/organization-agency/organization-agency.module.js';

@Module({
  imports: [
    OrganizationAgencyModule,
    CatalogModule,
  ],
  controllers: [HealthController],
})
export class AppModule {}
