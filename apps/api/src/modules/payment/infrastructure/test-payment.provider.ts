import { Injectable } from '@nestjs/common';

import {
  derivePaymentIntentExpiry,
  deriveTestProviderReference,
  PaymentPolicyError,
} from '../domain/payment-policy.js';

export interface CreateTestProviderIntentInput {
  intentId: string;
  createdAt: string;
}

export interface TestProviderIntentSession {
  providerReference: string;
  expiresAt: string;
}

@Injectable()
export class TestPaymentProvider {
  createIntent(
    input: CreateTestProviderIntentInput,
  ): TestProviderIntentSession {
    if (
      process.env.YSIM_PAYMENT_TEST_PROVIDER_ENABLED !==
      'true'
    ) {
      throw new PaymentPolicyError(
        'TEST payment provider is disabled',
      );
    }

    return {
      providerReference: deriveTestProviderReference(
        input.intentId,
      ),
      expiresAt: derivePaymentIntentExpiry(
        input.createdAt,
      ),
    };
  }
}
