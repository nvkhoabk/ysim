import { Injectable } from '@nestjs/common';

import {
  buildGigagoCreateOrderInput,
  type GigagoProcurementSnapshot,
} from '../domain/gigago-create-order-policy.js';
import {
  GigagoCreateOrderClient,
} from '../infrastructure/gigago/gigago.client.js';
import type {
  GigagoCreateOrderExtra,
} from '../infrastructure/gigago/gigago.types.js';

@Injectable()
export class GigagoOrderSubmissionService {
  constructor(
    private readonly client:
      GigagoCreateOrderClient,
  ) {}

  async submit(
    snapshot: GigagoProcurementSnapshot,
    notifyUrl: string,
  ): Promise<{
    requestId: string;
    providerOrderId: number;
    providerCode: string;
    providerStatus: number;
    providerOrderStatus: string;
  }> {
    const input =
      buildGigagoCreateOrderInput(
        snapshot,
        notifyUrl,
      );

    const extra:
      GigagoCreateOrderExtra =
        await this.client
          .createPartnerOrder(input);

    return {
      requestId: extra.request_id,
      providerOrderId:
        extra.agency_order_id,
      providerCode: extra.code,
      providerStatus: extra.status,
      providerOrderStatus:
        extra.order_status,
    };
  }
}
