import { Module } from '@nestjs/common';

import { PostgresService } from '../../platform/database/postgres.service.js';
import { CatalogService } from './application/catalog.service.js';
import { StorefrontCatalogService } from './public/application/storefront-catalog.service.js';
import { CatalogRepository } from './infrastructure/catalog.repository.js';
import { StorefrontCatalogRepository } from './public/infrastructure/storefront-catalog.repository.js';
import { CatalogController } from './presentation/catalog.controller.js';
import { StorefrontCatalogController } from './public/presentation/storefront-catalog.controller.js';

@Module({
  controllers: [CatalogController, StorefrontCatalogController],
  providers: [
    PostgresService,
    CatalogRepository,
    CatalogService,
    StorefrontCatalogRepository,
    StorefrontCatalogService,
  ],
})
export class CatalogModule {}
