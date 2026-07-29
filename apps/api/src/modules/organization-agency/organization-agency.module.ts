import { Module } from '@nestjs/common';

import { PostgresService } from '../../platform/database/postgres.service.js';
import { OrganizationAgencyService } from './application/organization-agency.service.js';
import { OrganizationAgencyRepository } from './infrastructure/organization-agency.repository.js';
import { OrganizationAgencyController } from './presentation/organization-agency.controller.js';

@Module({
  controllers: [OrganizationAgencyController],
  providers: [
    PostgresService,
    OrganizationAgencyRepository,
    OrganizationAgencyService,
  ],
})
export class OrganizationAgencyModule {}
