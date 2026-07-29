import { Module } from '@nestjs/common';

import { PostgresService } from '../../platform/database/postgres.service.js';
import { CatalogService } from './application/catalog.service.js';
import { CatalogRepository } from './infrastructure/catalog.repository.js';
import { CatalogController } from './presentation/catalog.controller.js';

@Module({
  controllers: [CatalogController],
  providers: [
    PostgresService,
    CatalogRepository,
    CatalogService,
  ],
})
export class CatalogModule {}
