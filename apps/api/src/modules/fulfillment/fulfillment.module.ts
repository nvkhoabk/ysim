import { Module } from '@nestjs/common';

import {
  PostgresService,
} from '../../platform/database/postgres.service.js';
import {
  EsimAssetIngestionService,
} from './application/esim-asset-ingestion.service.js';
import {
  EsimAssetCrypto,
} from './infrastructure/esim-asset.crypto.js';
import {
  EsimAssetRepository,
} from './infrastructure/esim-asset.repository.js';

@Module({
  providers: [
    PostgresService,
    {
      provide:
        EsimAssetCrypto,
      useFactory: () =>
        new EsimAssetCrypto(),
    },
    EsimAssetRepository,
    EsimAssetIngestionService,
  ],
  exports: [
    EsimAssetIngestionService,
  ],
})
export class FulfillmentModule {}
