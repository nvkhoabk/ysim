import { Injectable } from '@nestjs/common';

import {
  loadPaymentOutboxLeaseSeconds,
  parseClaimedPaymentIntegrationEvent,
  paymentOutboxLeaseUntil,
  paymentOutboxRetryAt,
  sanitizePaymentOutboxError,
} from '../domain/payment-outbox-policy.js';
import { PaymentIntegrationOutboxRepository } from '../infrastructure/payment-integration-outbox.repository.js';
import type {
  PaymentIntegrationEventSink,
} from './ports/payment-integration-event.sink.js';

type Environment =
  Record<string, string | undefined>;

export type PublishPaymentOutboxResult =
  | {
      kind: 'IDLE';
    }
  | {
      kind: 'PUBLISHED';
      eventId: string;
      attemptCount: number;
      publishedAt: string;
    }
  | {
      kind: 'FAILED';
      eventId: string;
      attemptCount: number;
      retryAt: string;
      error: string;
    }
  | {
      kind: 'LEASE_LOST';
      eventId: string;
      attemptCount: number;
    };

export interface PublishPaymentOutboxOptions {
  now?: Date;
  environment?: Environment;
}

@Injectable()
export class PaymentIntegrationOutboxPublisher {
  constructor(
    private readonly repository:
      PaymentIntegrationOutboxRepository,
  ) {}

  async publishNext(
    sink: PaymentIntegrationEventSink,
    options: PublishPaymentOutboxOptions = {},
  ): Promise<PublishPaymentOutboxResult> {
    const now =
      options.now ?? new Date();
    const nowIso = now.toISOString();
    const leaseSeconds =
      loadPaymentOutboxLeaseSeconds(
        options.environment,
      );
    const claimed =
      await this.repository.claimNext({
        now: nowIso,
        leaseUntil: paymentOutboxLeaseUntil(
          nowIso,
          leaseSeconds,
        ),
      });

    if (!claimed) return { kind: 'IDLE' };

    try {
      const event =
        parseClaimedPaymentIntegrationEvent(
          claimed,
        );
      await sink.publish(event);

      const marked =
        await this.repository.markPublished({
          eventId: claimed.id,
          attemptCount:
            claimed.attemptCount,
          publishedAt: nowIso,
        });

      if (!marked) {
        return {
          kind: 'LEASE_LOST',
          eventId: claimed.id,
          attemptCount:
            claimed.attemptCount,
        };
      }

      return {
        kind: 'PUBLISHED',
        eventId: claimed.id,
        attemptCount:
          claimed.attemptCount,
        publishedAt: nowIso,
      };
    } catch (error) {
      const safeError =
        sanitizePaymentOutboxError(error);
      const retryAt =
        paymentOutboxRetryAt(
          nowIso,
          claimed.attemptCount,
        );
      const marked =
        await this.repository.markFailed({
          eventId: claimed.id,
          attemptCount:
            claimed.attemptCount,
          retryAt,
          lastError: safeError,
        });

      if (!marked) {
        return {
          kind: 'LEASE_LOST',
          eventId: claimed.id,
          attemptCount:
            claimed.attemptCount,
        };
      }

      return {
        kind: 'FAILED',
        eventId: claimed.id,
        attemptCount:
          claimed.attemptCount,
        retryAt,
        error: safeError,
      };
    }
  }
}
