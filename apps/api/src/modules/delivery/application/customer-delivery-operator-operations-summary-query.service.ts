import { Injectable } from '@nestjs/common';
import {
  CustomerDeliveryOperatorStatusQueryResult,
  CustomerDeliveryOperatorStatusQueryService,
} from './customer-delivery-operator-status-query.service.js';
import {
  CustomerDeliveryOperationsSummaryResult,
  CustomerDeliveryOperationsSummaryService,
} from './customer-delivery-operations-summary.service.js';

type OperatorAccessDenied = Extract<
  CustomerDeliveryOperatorStatusQueryResult,
  { authorized: false }
>;

export type CustomerDeliveryOperatorOperationsSummaryQueryResult =
  | OperatorAccessDenied
  | ({ authorized: true } & CustomerDeliveryOperationsSummaryResult);

@Injectable()
export class CustomerDeliveryOperatorOperationsSummaryQueryService {
  constructor(
    private readonly operatorStatus: CustomerDeliveryOperatorStatusQueryService,
    private readonly operationsSummary: CustomerDeliveryOperationsSummaryService,
  ) {}

  async query(
    presentedCredential: string,
    env: NodeJS.ProcessEnv = process.env,
    now: Date = new Date(),
  ): Promise<CustomerDeliveryOperatorOperationsSummaryQueryResult> {
    const access = this.operatorStatus.query(presentedCredential, env);
    if (!access.authorized) return access;

    const result = await this.operationsSummary.snapshot(now);
    return { authorized: true, ...result };
  }
}
