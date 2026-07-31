import { Controller, Get, Header, Headers } from '@nestjs/common';
import {
  CustomerDeliveryOperatorOperationsSummaryQueryResult,
  CustomerDeliveryOperatorOperationsSummaryQueryService,
} from './application/customer-delivery-operator-operations-summary-query.service.js';

@Controller('internal/delivery')
export class CustomerDeliveryOperatorOperationsSummaryController {
  constructor(
    private readonly operationsSummaryQuery: CustomerDeliveryOperatorOperationsSummaryQueryService,
  ) {}

  @Get('operations-summary')
  @Header('Cache-Control', 'no-store')
  getOperationsSummary(
    @Headers('x-ysim-operator-token') presentedCredential: string | undefined,
  ): Promise<CustomerDeliveryOperatorOperationsSummaryQueryResult> {
    return this.operationsSummaryQuery.query(presentedCredential ?? '');
  }
}
