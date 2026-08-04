import { timingSafeEqual } from 'node:crypto';

import {
  Body,
  Controller,
  Get,
  Header,
  Headers,
  HttpCode,
  Param,
  Post,
  Query,
  ServiceUnavailableException,
  UnauthorizedException,
} from '@nestjs/common';
import type {
  ApplyGPayWebhookResponse,
  InitializeGPayCommissioningRequest,
  InitializeGPayCommissioningResponse,
  ReconcileGPayCommissioningResponse,
} from '@ysim/contracts';

import { GPayGatewayCommissioningService } from '../application/gpay-gateway-commissioning.service.js';

type RequestHeaders = Record<
  string,
  string | string[] | undefined
>;

const singleHeader = (
  headers: RequestHeaders,
  name: string,
): string | undefined => {
  const value = headers[name];
  return Array.isArray(value) ? value[0] : value;
};

const requireBootstrapToken = (
  headers: RequestHeaders,
): void => {
  const configured = process.env.YSIM_BOOTSTRAP_TOKEN;
  if (!configured || configured.length < 24) {
    throw new ServiceUnavailableException(
      'YSIM_BOOTSTRAP_TOKEN must be configured with at least 24 characters',
    );
  }
  const supplied = singleHeader(
    headers,
    'x-ysim-bootstrap-token',
  );
  if (!supplied) {
    throw new UnauthorizedException(
      'Bootstrap token is required',
    );
  }
  const configuredBuffer = Buffer.from(configured);
  const suppliedBuffer = Buffer.from(supplied);
  if (
    configuredBuffer.length !== suppliedBuffer.length ||
    !timingSafeEqual(configuredBuffer, suppliedBuffer)
  ) {
    throw new UnauthorizedException(
      'Bootstrap token is invalid',
    );
  }
};

const requireActorIdentityId = (
  headers: RequestHeaders,
): string => {
  const actorIdentityId = singleHeader(
    headers,
    'x-ysim-actor-id',
  );
  if (!actorIdentityId) {
    throw new UnauthorizedException(
      'x-ysim-actor-id header is required',
    );
  }
  return actorIdentityId;
};

@Controller('internal/r1/payments/gpay/commissioning')
export class PaymentGPayCommissioningController {
  constructor(
    private readonly service:
      GPayGatewayCommissioningService,
  ) {}

  @Post('initialize')
  @HttpCode(200)
  @Header('Cache-Control', 'private, no-store')
  initialize(
    @Headers() headers: RequestHeaders,
    @Body() request: InitializeGPayCommissioningRequest,
  ): Promise<InitializeGPayCommissioningResponse> {
    requireBootstrapToken(headers);
    return this.service.initialize(
      request.paymentIntentId,
      requireActorIdentityId(headers),
    );
  }

  @Post('intents/:paymentIntentId/reconcile')
  @HttpCode(200)
  @Header('Cache-Control', 'private, no-store')
  reconcile(
    @Headers() headers: RequestHeaders,
    @Param('paymentIntentId') paymentIntentId: string,
  ): Promise<ReconcileGPayCommissioningResponse> {
    requireBootstrapToken(headers);
    requireActorIdentityId(headers);
    return this.service.reconcile(paymentIntentId);
  }
}

@Controller('api/r1/payments/gpay/gateway')
export class PaymentGPayGatewayCallbackController {
  constructor(
    private readonly service:
      GPayGatewayCommissioningService,
  ) {}

  @Get('callback')
  @HttpCode(200)
  @Header('Cache-Control', 'no-store')
  callback(
    @Query() query: Record<string, unknown>,
    @Headers() headers: RequestHeaders,
  ): Promise<ApplyGPayWebhookResponse> {
    return this.service.applyCallback(
      query,
      singleHeader(headers, 'x-signature'),
    );
  }

  @Post('webhook')
  @HttpCode(200)
  @Header('Cache-Control', 'no-store')
  webhook(
    @Body() body: Record<string, unknown>,
    @Headers() headers: RequestHeaders,
  ): Promise<ApplyGPayWebhookResponse> {
    return this.service.applyCallback(
      body,
      singleHeader(headers, 'x-signature'),
    );
  }
}
