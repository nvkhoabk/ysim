import {
  Body,
  Controller,
  Headers,
  HttpCode,
  Post,
} from '@nestjs/common';
import type {
  ApplyGPayWebhookResponse,
} from '@ysim/contracts';

import {
  GPayWebhookApplicationService,
} from '../application/gpay-webhook-application.service.js';

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

@Controller('api/r1/payments/gpay')
export class PaymentGPayWebhookController {
  constructor(
    private readonly service:
      GPayWebhookApplicationService,
  ) {}

  @Post('webhook')
  @HttpCode(200)
  applyWebhook(
    @Headers() headers: RequestHeaders,
    @Body() body: unknown,
  ): Promise<ApplyGPayWebhookResponse> {
    return this.service.apply(
      {
        eventId: singleHeader(
          headers,
          'x-gpay-event-id',
        ),
        timestamp: singleHeader(
          headers,
          'x-timestamp',
        ),
        signature: singleHeader(
          headers,
          'x-signature',
        ),
      },
      body,
    );
  }
}
