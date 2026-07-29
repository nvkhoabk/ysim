import {
  Controller,
  Get,
  Header,
  Headers,
  Param,
  Query,
} from '@nestjs/common';
import type {
  ListStorefrontDestinationsResponse,
  ListStorefrontOffersResponse,
  StorefrontCatalogOfferContract,
} from '@ysim/contracts';

import { StorefrontCatalogService } from '../application/storefront-catalog.service.js';
import { STOREFRONT_CATALOG_CACHE_CONTROL } from '../domain/storefront-catalog-policy.js';

@Controller('api/r1/catalog')
export class StorefrontCatalogController {
  constructor(
    private readonly service: StorefrontCatalogService,
  ) {}

  @Get('destinations')
  @Header('Cache-Control', STOREFRONT_CATALOG_CACHE_CONTROL)
  @Header('Vary', 'Accept-Language')
  listDestinations(
    @Query('locale') locale?: string,
    @Headers('accept-language') acceptLanguage?: string,
  ): Promise<ListStorefrontDestinationsResponse> {
    return this.service.listDestinations(
      locale,
      acceptLanguage,
    );
  }

  @Get('destinations/:destinationCode/offers')
  @Header('Cache-Control', STOREFRONT_CATALOG_CACHE_CONTROL)
  @Header('Vary', 'Accept-Language')
  listOffersByDestination(
    @Param('destinationCode') destinationCode: string,
    @Query('locale') locale?: string,
    @Headers('accept-language') acceptLanguage?: string,
  ): Promise<ListStorefrontOffersResponse> {
    return this.service.listOffersByDestination(
      destinationCode,
      locale,
      acceptLanguage,
    );
  }

  @Get('offers/:offerCode')
  @Header('Cache-Control', STOREFRONT_CATALOG_CACHE_CONTROL)
  @Header('Vary', 'Accept-Language')
  getOffer(
    @Param('offerCode') offerCode: string,
    @Query('locale') locale?: string,
    @Headers('accept-language') acceptLanguage?: string,
  ): Promise<StorefrontCatalogOfferContract> {
    return this.service.getOffer(
      offerCode,
      locale,
      acceptLanguage,
    );
  }
}
