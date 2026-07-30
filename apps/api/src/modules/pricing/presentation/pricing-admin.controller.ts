import { timingSafeEqual } from 'node:crypto';

import {
  Body,
  Controller,
  Headers,
  HttpCode,
  Param,
  Post,
  ServiceUnavailableException,
  UnauthorizedException,
} from '@nestjs/common';
import type {
  CreatePriceBookEntryRequest,
  CreatePriceBookEntryResponse,
  CreatePriceBookRequest,
  CreatePriceBookResponse,
  CreateSupplierCostSnapshotRequest,
  CreateSupplierCostSnapshotResponse,
  PriceBookTransitionResponse,
} from '@ysim/contracts';

import { PricingService } from '../application/pricing.service.js';

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

function requireActorIdentityId(headers: RequestHeaders): string {
  const actorIdentityId = singleHeader(headers, 'x-ysim-actor-id');
  if (!actorIdentityId) {
    throw new UnauthorizedException(
      'x-ysim-actor-id header is required',
    );
  }

  return actorIdentityId;
}

@Controller('internal/r1/pricing')
export class PricingAdminController {
  constructor(private readonly service: PricingService) {}

  @Post('price-books')
  createPriceBook(
    @Headers() headers: RequestHeaders,
    @Body() request: CreatePriceBookRequest,
  ): Promise<CreatePriceBookResponse> {
    requireBootstrapToken(headers);
    return this.service.createPriceBook(
      request,
      requireActorIdentityId(headers),
    );
  }

  @Post('supplier-cost-snapshots')
  createSupplierCostSnapshot(
    @Headers() headers: RequestHeaders,
    @Body() request: CreateSupplierCostSnapshotRequest,
  ): Promise<CreateSupplierCostSnapshotResponse> {
    requireBootstrapToken(headers);
    return this.service.createSupplierCostSnapshot(
      request,
      requireActorIdentityId(headers),
    );
  }

  @Post('price-books/:priceBookId/entries')
  createPriceBookEntry(
    @Headers() headers: RequestHeaders,
    @Param('priceBookId') priceBookId: string,
    @Body() request: CreatePriceBookEntryRequest,
  ): Promise<CreatePriceBookEntryResponse> {
    requireBootstrapToken(headers);
    return this.service.createPriceBookEntry(
      priceBookId,
      request,
      requireActorIdentityId(headers),
    );
  }

  @Post('price-books/:priceBookId/activate')
  @HttpCode(200)
  activatePriceBook(
    @Headers() headers: RequestHeaders,
    @Param('priceBookId') priceBookId: string,
  ): Promise<PriceBookTransitionResponse> {
    requireBootstrapToken(headers);
    return this.service.activatePriceBook(
      priceBookId,
      requireActorIdentityId(headers),
    );
  }

  @Post('price-books/:priceBookId/suspend')
  @HttpCode(200)
  suspendPriceBook(
    @Headers() headers: RequestHeaders,
    @Param('priceBookId') priceBookId: string,
  ): Promise<PriceBookTransitionResponse> {
    requireBootstrapToken(headers);
    return this.service.suspendPriceBook(
      priceBookId,
      requireActorIdentityId(headers),
    );
  }
}
