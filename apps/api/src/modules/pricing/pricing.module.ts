import { Module } from '@nestjs/common';

import { PostgresService } from '../../platform/database/postgres.service.js';
import { PricingService } from './application/pricing.service.js';
import { PricingRepository } from './infrastructure/pricing.repository.js';
import { PricingAdminController } from './presentation/pricing-admin.controller.js';
import { PricingPublicController } from './presentation/pricing-public.controller.js';

@Module({
  controllers: [PricingAdminController, PricingPublicController],
  providers: [PostgresService, PricingRepository, PricingService],
})
export class PricingModule {}
