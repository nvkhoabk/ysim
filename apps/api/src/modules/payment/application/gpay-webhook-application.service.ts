import { createHash } from 'node:crypto';

import {
  BadRequestException,
  ConflictException,
  Injectable,
  NotFoundException,
  ServiceUnavailableException,
  UnauthorizedException,
} from '@nestjs/common';
import type {
  ApplyGPayWebhookResponse,
  VerifiedGPayWebhookContract,
} from '@ysim/contracts';

import {
  PaymentRepository,
  type PersistedPaymentIntent,
} from '../infrastructure/payment.repository.js';
import {
  GPayWebhookError,
  GPayWebhookVerifier,
  type GPayWebhookHeaders,
} from '../infrastructure/gpay/gpay.webhook.js';

const createGPayEventFingerprint = (
  intentId: string,
  event: VerifiedGPayWebhookContract,
): string => createHash('sha256').update(
  JSON.stringify({
    intentId,
    eventId: event.eventId,
    providerReference: event.providerReference,
    normalizedStatus: event.normalizedStatus,
    amountMinor: event.amountMinor,
    currency: event.currency,
    occurredAt: event.occurredAt,
  }),
  'utf8',
).digest('hex');

@Injectable()
export class GPayWebhookApplicationService {
  private readonly verifier = new GPayWebhookVerifier();

  constructor(
    private readonly repository: PaymentRepository,
  ) {}

  async apply(
    headers: GPayWebhookHeaders,
    rawBody: unknown,
  ): Promise<ApplyGPayWebhookResponse> {
    try {
      const verified = await this.verifier.verify(
        headers,
        rawBody,
      );
      return await this.applyVerifiedEvent(verified);
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  async applyVerifiedEvent(
    verified: VerifiedGPayWebhookContract,
  ): Promise<ApplyGPayWebhookResponse> {
    const intent =
      await this.repository.findIntentByProviderReference(
        'GPAY',
        verified.providerReference,
      );

    if (!intent) {
      throw new NotFoundException(
        'GPay Payment Intent was not found',
      );
    }

    this.assertCommercialSnapshot(intent, verified);

    const result = await this.repository.applyEvent({
      intentId: intent.id,
      provider: 'GPAY',
      providerEventId: verified.eventId,
      eventFingerprint: createGPayEventFingerprint(
        intent.id,
        verified,
      ),
      normalizedStatus: verified.normalizedStatus,
      actorIdentityId: verified.actorIdentityId,
      occurredAt: verified.occurredAt,
    });

    switch (result.kind) {
      case 'INTENT_NOT_FOUND':
        throw new NotFoundException(
          'GPay Payment Intent was not found',
        );
      case 'EVENT_CONFLICT':
        throw new ConflictException(
          'GPay event identifier conflicts with an existing event',
        );
      case 'ILLEGAL_TRANSITION':
        throw new ConflictException(
          'Payment Intent cannot accept this GPay event transition',
        );
      case 'APPLIED':
      case 'DUPLICATE':
        return {
          accepted: true,
          duplicateEvent: result.kind === 'DUPLICATE',
          paymentIntentId: result.intent.id,
          paymentIntentStatus: result.intent.status,
          orderStatus: result.orderStatus,
          orderPaymentStatus: result.orderPaymentStatus,
        };
    }
  }

  private assertCommercialSnapshot(
    intent: PersistedPaymentIntent,
    verified: VerifiedGPayWebhookContract,
  ): void {
    if (
      intent.amountMinor !== verified.amountMinor ||
      intent.currency !== verified.currency
    ) {
      throw new ConflictException(
        'GPay webhook amount or currency does not match the Payment Intent snapshot',
      );
    }
  }

  private rethrowKnownError(error: unknown): never {
    if (
      error instanceof BadRequestException ||
      error instanceof ConflictException ||
      error instanceof NotFoundException ||
      error instanceof UnauthorizedException ||
      error instanceof ServiceUnavailableException
    ) {
      throw error;
    }

    if (error instanceof GPayWebhookError) {
      switch (error.kind) {
        case 'BAD_REQUEST':
          throw new BadRequestException(error.message);
        case 'UNAUTHORIZED':
          throw new UnauthorizedException(error.message);
        case 'UNAVAILABLE':
          throw new ServiceUnavailableException(error.message);
      }
    }

    throw error;
  }
}
