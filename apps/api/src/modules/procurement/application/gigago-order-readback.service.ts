import { Injectable } from '@nestjs/common';

import {
  assessGigagoDeliveryReadiness,
  normalizeGigagoAgencyOrders,
  normalizeGigagoOrderDetails,
  type GigagoDeliveryReadiness,
} from '../domain/gigago-order-readback-policy.js';
import {
  GigagoOrderReadbackClient,
} from '../infrastructure/gigago/gigago.client.js';

@Injectable()
export class GigagoOrderReadbackService {
  constructor(
    private readonly client:
      GigagoOrderReadbackClient,
  ) {}

  async read(
    requestId: string,
    expectedCount: number,
  ): Promise<GigagoDeliveryReadiness> {
    const [
      agencyOrderResult,
      detailResult,
    ] = await Promise.all([
      this.client
        .getMyOrdersAgency(requestId),
      this.client
        .getOrderDetailAgency(
          requestId,
        ),
    ]);

    const orders =
      normalizeGigagoAgencyOrders(
        agencyOrderResult,
        requestId,
      );
    const details =
      normalizeGigagoOrderDetails(
        detailResult,
        requestId,
      );

    return assessGigagoDeliveryReadiness(
      orders,
      details,
      expectedCount,
    );
  }
}
