import { Injectable } from '@nestjs/common';

import {
  normalizeCustomerDeliveryRequest,
  type CustomerDeliveryRequestInput,
} from '../domain/customer-delivery-policy.js';
import {
  CustomerDeliveryRepository,
  type PersistCustomerDeliveryResult,
} from '../infrastructure/customer-delivery.repository.js';

@Injectable()
export class CustomerDeliveryRequestService {
  constructor(
    private readonly repository:
      CustomerDeliveryRepository,
  ) {}

  async request(
    input: CustomerDeliveryRequestInput,
  ): Promise<
    PersistCustomerDeliveryResult
  > {
    const normalized =
      normalizeCustomerDeliveryRequest(
        input,
      );

    return this.repository.persist(
      normalized,
    );
  }
}
