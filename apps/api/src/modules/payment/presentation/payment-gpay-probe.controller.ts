import { timingSafeEqual } from 'node:crypto';

import {
  Controller,
  Headers,
  HttpCode,
  Post,
  ServiceUnavailableException,
  UnauthorizedException,
} from '@nestjs/common';
import type {
  GPayContractProbeResponse,
} from '@ysim/contracts';

import { GPayContractProbeService } from '../application/gpay-contract-probe.service.js';

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

const requireActorIdentity = (
  headers: RequestHeaders,
): void => {
  const actor = singleHeader(headers, 'x-ysim-actor-id');
  if (!actor || !/^[0-9a-f-]{36}$/iu.test(actor)) {
    throw new UnauthorizedException(
      'x-ysim-actor-id header is required',
    );
  }
};

@Controller('internal/r1/payments/gpay')
export class PaymentGPayProbeController {
  constructor(
    private readonly service: GPayContractProbeService,
  ) {}

  @Post('contract-probe')
  @HttpCode(200)
  probe(
    @Headers() headers: RequestHeaders,
  ): Promise<GPayContractProbeResponse> {
    requireBootstrapToken(headers);
    requireActorIdentity(headers);
    return this.service.probe();
  }
}
