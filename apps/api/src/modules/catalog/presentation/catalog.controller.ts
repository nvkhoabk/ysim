import { timingSafeEqual } from 'node:crypto';

import {
  Body,
  Controller,
  Get,
  Headers,
  HttpCode,
  Param,
  Post,
  Query,
  ServiceUnavailableException,
  UnauthorizedException,
} from '@nestjs/common';
import type {
  CreateDestinationRequest,
  CreateDestinationResponse,
  CreateProductOfferRequest,
  CreateProductOfferResponse,
  CreateProductRequest,
  CreateProductResponse,
  CreateRegionRequest,
  CreateRegionResponse,
  ListProductOffersResponse,
  LocalizedProductOfferContract,
  ProductOfferTransitionResponse,
} from '@ysim/contracts';

import { CatalogService } from '../application/catalog.service.js';

type RequestHeaders = Record<string, string | string[] | undefined>;

function singleHeader(
  headers: RequestHeaders,
  name: string,
): string | undefined {
  const value = headers[name];
  return Array.isArray(value) ? value[0] : value;
}

function requireBootstrapToken(headers: RequestHeaders): void {
  const configured = process.env.YSIM_BOOTSTRAP_TOKEN;
  if (!configured || configured.length < 24) {
    throw new ServiceUnavailableException(
      'YSIM_BOOTSTRAP_TOKEN must be configured with at least 24 characters',
    );
  }

  const supplied = singleHeader(headers, 'x-ysim-bootstrap-token');
  if (!supplied) {
    throw new UnauthorizedException('Bootstrap token is required');
  }

  const configuredBuffer = Buffer.from(configured);
  const suppliedBuffer = Buffer.from(supplied);

  if (
    configuredBuffer.length !== suppliedBuffer.length ||
    !timingSafeEqual(configuredBuffer, suppliedBuffer)
  ) {
    throw new UnauthorizedException('Bootstrap token is invalid');
  }
}

function requiredHeader(
  headers: RequestHeaders,
  name: string,
): string {
  const value = singleHeader(headers, name);
  if (!value) {
    throw new UnauthorizedException(`${name} header is required`);
  }

  return value;
}

@Controller('internal/r1/catalog')
export class CatalogController {
  constructor(private readonly service: CatalogService) {}

  @Post('regions')
  createRegion(
    @Headers() headers: RequestHeaders,
    @Body() request: CreateRegionRequest,
  ): Promise<CreateRegionResponse> {
    requireBootstrapToken(headers);
    return this.service.createRegion(
      request,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Post('destinations')
  createDestination(
    @Headers() headers: RequestHeaders,
    @Body() request: CreateDestinationRequest,
  ): Promise<CreateDestinationResponse> {
    requireBootstrapToken(headers);
    return this.service.createDestination(
      request,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Post('products')
  createProduct(
    @Headers() headers: RequestHeaders,
    @Body() request: CreateProductRequest,
  ): Promise<CreateProductResponse> {
    requireBootstrapToken(headers);
    return this.service.createProduct(
      request,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Post('offers')
  createOffer(
    @Headers() headers: RequestHeaders,
    @Body() request: CreateProductOfferRequest,
  ): Promise<CreateProductOfferResponse> {
    requireBootstrapToken(headers);
    return this.service.createOffer(
      request,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Post('offers/:offerId/publish')
  @HttpCode(200)
  publishOffer(
    @Headers() headers: RequestHeaders,
    @Param('offerId') offerId: string,
  ): Promise<ProductOfferTransitionResponse> {
    requireBootstrapToken(headers);
    return this.service.publishOffer(
      offerId,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Post('offers/:offerId/suspend')
  @HttpCode(200)
  suspendOffer(
    @Headers() headers: RequestHeaders,
    @Param('offerId') offerId: string,
  ): Promise<ProductOfferTransitionResponse> {
    requireBootstrapToken(headers);
    return this.service.suspendOffer(
      offerId,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Get('offers/:offerId')
  getOffer(
    @Headers() headers: RequestHeaders,
    @Param('offerId') offerId: string,
    @Query('locale') locale?: string,
  ): Promise<LocalizedProductOfferContract> {
    requireBootstrapToken(headers);
    return this.service.getOffer(offerId, locale);
  }

  @Get('offers')
  listOffers(
    @Headers() headers: RequestHeaders,
    @Query('status') status?: string,
    @Query('locale') locale?: string,
  ): Promise<ListProductOffersResponse> {
    requireBootstrapToken(headers);
    return this.service.listOffers(status, locale);
  }
}
