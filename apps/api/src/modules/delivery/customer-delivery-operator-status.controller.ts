import { Controller, Get, Header, Headers } from '@nestjs/common';
import {
  CustomerDeliveryOperatorStatusQueryResult,
  CustomerDeliveryOperatorStatusQueryService,
} from './application/customer-delivery-operator-status-query.service.js';

@Controller('internal/delivery')
export class CustomerDeliveryOperatorStatusController {
  constructor(private readonly statusQuery: CustomerDeliveryOperatorStatusQueryService) {}

  @Get('runtime-status')
  @Header('Cache-Control', 'no-store')
  getRuntimeStatus(
    @Headers('x-ysim-operator-token') presentedCredential: string | undefined,
  ): CustomerDeliveryOperatorStatusQueryResult {
    return this.statusQuery.query(presentedCredential ?? '');
  }
}
