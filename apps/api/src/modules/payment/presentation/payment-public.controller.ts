import {
  Body,
  Controller,
  Get,
  Header,
  Headers,
  Param,
  Post,
} from '@nestjs/common';
import type {
  CreatePaymentIntentRequest,
  CreatePaymentIntentResponse,
  GetPaymentIntentResponse,
} from '@ysim/contracts';

import { PaymentService } from '../application/payment.service.js';

@Controller('api/r1/payments')
export class PaymentPublicController {
  constructor(private readonly service: PaymentService) {}

  @Post('intents')
  @Header('Cache-Control', 'private, no-store')
  createIntent(
    @Headers('idempotency-key')
    idempotencyKey: string | undefined,
    @Headers('x-ysim-order-access-token')
    orderAccessToken: string | undefined,
    @Body() request: CreatePaymentIntentRequest,
  ): Promise<CreatePaymentIntentResponse> {
    return this.service.createIntent(
      request,
      idempotencyKey,
      orderAccessToken,
    );
  }

  @Get('intents/:intentId')
  @Header('Cache-Control', 'private, no-store')
  getIntent(
    @Param('intentId') intentId: string,
    @Headers('x-ysim-order-access-token')
    orderAccessToken: string | undefined,
  ): Promise<GetPaymentIntentResponse> {
    return this.service.getIntent(
      intentId,
      orderAccessToken,
    );
  }
}
