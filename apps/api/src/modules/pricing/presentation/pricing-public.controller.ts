import {
  Body,
  Controller,
  Get,
  Header,
  HttpCode,
  Param,
  Post,
} from '@nestjs/common';
import type {
  CreatePricingQuoteRequest,
  CreatePricingQuoteResponse,
  GetPricingQuoteResponse,
} from '@ysim/contracts';

import { PricingService } from '../application/pricing.service.js';

@Controller('api/r1/pricing')
export class PricingPublicController {
  constructor(private readonly service: PricingService) {}

  @Post('quotes')
  @HttpCode(201)
  @Header('Cache-Control', 'private, no-store')
  createQuote(
    @Body() request: CreatePricingQuoteRequest,
  ): Promise<CreatePricingQuoteResponse> {
    return this.service.createQuote(request);
  }

  @Get('quotes/:quoteId')
  @Header('Cache-Control', 'private, no-store')
  getQuote(
    @Param('quoteId') quoteId: string,
  ): Promise<GetPricingQuoteResponse> {
    return this.service.getQuote(quoteId);
  }
}
