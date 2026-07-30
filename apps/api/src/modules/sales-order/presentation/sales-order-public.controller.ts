import {
  Body,
  Controller,
  Get,
  Header,
  Headers,
  HttpCode,
  Param,
  Post,
} from '@nestjs/common';
import type {
  CreateSalesOrderRequest,
  CreateSalesOrderResponse,
  GetSalesOrderResponse,
} from '@ysim/contracts';

import { SalesOrderService } from '../application/sales-order.service.js';

@Controller('api/r1/orders')
export class SalesOrderPublicController {
  constructor(
    private readonly service: SalesOrderService,
  ) {}

  @Post()
  @HttpCode(201)
  @Header('Cache-Control', 'private, no-store')
  createOrder(
    @Headers('idempotency-key')
    idempotencyKey: string | undefined,
    @Body() request: CreateSalesOrderRequest,
  ): Promise<CreateSalesOrderResponse> {
    return this.service.createOrder(
      request,
      idempotencyKey,
    );
  }

  @Get(':orderId')
  @Header('Cache-Control', 'private, no-store')
  getOrder(
    @Param('orderId') orderId: string,
    @Headers('x-ysim-order-access-token')
    orderAccessToken: string | undefined,
  ): Promise<GetSalesOrderResponse> {
    return this.service.getOrder(
      orderId,
      orderAccessToken,
    );
  }
}
