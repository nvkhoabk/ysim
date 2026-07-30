import { Injectable } from '@nestjs/common';

import {
  derivePaymentIntentExpiry,
  PaymentPolicyError,
} from '../../domain/payment-policy.js';

type Environment = Record<string, string | undefined>;

const UUID_HEX_PATTERN = /^[0-9A-F]{32}$/u;

export interface CreateGPayProviderIntentInput {
  intentId: string;
  createdAt: string;
}

export interface GPayProviderIntentSession {
  providerReference: string;
  expiresAt: string;
}

export const deriveGPayProviderReference = (
  intentId: string,
): string => {
  const normalized = intentId
    .replaceAll('-', '')
    .toUpperCase();

  if (!UUID_HEX_PATTERN.test(normalized)) {
    throw new PaymentPolicyError(
      'GPAY intentId must be a UUID',
    );
  }

  return `GPY-${normalized}`;
};

const requireGPayIntentReservationPolicy = (
  environment: Environment,
): void => {
  if (
    environment.YSIM_GPAY_PAYMENT_ENABLED !== 'true'
  ) {
    throw new PaymentPolicyError(
      'GPAY payment provider is disabled',
    );
  }

  if (environment.YSIM_GPAY_ENVIRONMENT !== 'SANDBOX') {
    throw new PaymentPolicyError(
      'GPAY payment intent reservation is sandbox-only in VS-R1-012',
    );
  }

  if (
    environment.YSIM_GPAY_CONTRACT_STATUS !== 'PROBED'
  ) {
    throw new PaymentPolicyError(
      'GPAY contract must be PROBED before payment intent reservation',
    );
  }
};

@Injectable()
export class GPayIntentProvider {
  createIntent(
    input: CreateGPayProviderIntentInput,
    environment: Environment = process.env,
  ): GPayProviderIntentSession {
    requireGPayIntentReservationPolicy(environment);

    return {
      providerReference:
        deriveGPayProviderReference(input.intentId),
      expiresAt: derivePaymentIntentExpiry(
        input.createdAt,
      ),
    };
  }
}
