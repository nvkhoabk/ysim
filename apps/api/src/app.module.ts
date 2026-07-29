import { Module } from '@nestjs/common';

import { HealthController } from './health.controller.js';
import { OrganizationAgencyModule } from './modules/organization-agency/organization-agency.module.js';

@Module({
  imports: [OrganizationAgencyModule],
  controllers: [HealthController],
})
export class AppModule {}
