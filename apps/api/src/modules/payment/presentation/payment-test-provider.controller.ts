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
  ApplyTestPaymentEventRequest,
  ApplyTestPaymentEventResponse,
} from '@ysim/contracts';

import { PaymentService } from '../application/payment.service.js';

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

const requireTestProviderEnabled = (): void => {
  if (
    process.env.YSIM_PAYMENT_TEST_PROVIDER_ENABLED !==
    'true'
  ) {
    throw new ServiceUnavailableException(
      'TEST payment provider is disabled',
    );
  }
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
    !timingSafeEqual(
      configuredBuffer,
      suppliedBuffer,
    )
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

@Controller('internal/r1/payments/test-provider')
export class PaymentTestProviderController {
  constructor(private readonly service: PaymentService) {}

  @Post('intents/:intentId/events')
  @HttpCode(200)
  applyEvent(
    @Headers() headers: RequestHeaders,
    @Param('intentId') intentId: string,
    @Body() request: ApplyTestPaymentEventRequest,
  ): Promise<ApplyTestPaymentEventResponse> {
    requireTestProviderEnabled();
    requireBootstrapToken(headers);
    return this.service.applyTestEvent(
      intentId,
      request,
      requireActorIdentityId(headers),
    );
  }
}
