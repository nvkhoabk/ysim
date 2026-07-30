import { randomUUID } from 'node:crypto';

import {
  BadRequestException,
  ConflictException,
  Injectable,
  NotFoundException,
  ServiceUnavailableException,
  UnauthorizedException,
} from '@nestjs/common';
import type {
  ApplyTestPaymentEventRequest,
  ApplyTestPaymentEventResponse,
  CreatePaymentIntentRequest,
  CreatePaymentIntentResponse,
  GetPaymentIntentResponse,
  PaymentIntentContract,
} from '@ysim/contracts';

import {
  createPaymentEventFingerprint,
  createPaymentRequestFingerprint,
  normalizePaymentIdempotencyKey,
  normalizeTestPaymentEventId,
  paymentCurrencyExponent,
  PaymentPolicyError,
  requirePaymentAccessToken,
  requirePaymentProvider,
  requirePaymentUuid,
  requireTestPaymentEventStatus,
  sha256PaymentValue,
} from '../domain/payment-policy.js';
import {
  PaymentRepository,
  type PersistedPaymentIntent,
} from '../infrastructure/payment.repository.js';
import { TestPaymentProvider } from '../infrastructure/test-payment.provider.js';

@Injectable()
export class PaymentService {
  constructor(
    private readonly repository: PaymentRepository,
    private readonly testProvider: TestPaymentProvider,
  ) {}

  async createIntent(
    request: CreatePaymentIntentRequest,
    idempotencyHeader: string | undefined,
    orderAccessTokenHeader: string | undefined,
  ): Promise<CreatePaymentIntentResponse> {
    try {
      const orderId = requirePaymentUuid(
        request.orderId,
        'orderId',
      );
      const provider = requirePaymentProvider(
        request.provider,
      );
      const idempotencyKey =
        normalizePaymentIdempotencyKey(
          idempotencyHeader,
        );
      const orderAccessToken =
        requirePaymentAccessToken(
          orderAccessTokenHeader,
        );
      const proposedIntentId = randomUUID();
      const createdAt = new Date().toISOString();
      const providerSession =
        this.testProvider.createIntent({
          intentId: proposedIntentId,
          createdAt,
        });

      const result = await this.repository.createIntent({
        proposedIntentId,
        orderId,
        orderAccessTokenHash:
          sha256PaymentValue(orderAccessToken),
        provider,
        providerReference:
          providerSession.providerReference,
        idempotencyKeyHash:
          sha256PaymentValue(idempotencyKey),
        requestFingerprint:
          createPaymentRequestFingerprint({
            orderId,
            provider,
          }),
        createdAt,
        expiresAt: providerSession.expiresAt,
      });

      switch (result.kind) {
        case 'ORDER_NOT_FOUND':
          throw new NotFoundException(
            'Sales Order was not found',
          );
        case 'ORDER_NOT_PAYABLE':
          throw new ConflictException(
            'Sales Order is not payable',
          );
        case 'ACTIVE_INTENT_EXISTS':
          throw new ConflictException(
            'An active Payment Intent already exists for this Sales Order',
          );
        case 'IDEMPOTENCY_CONFLICT':
          throw new ConflictException(
            'Idempotency-Key was already used with different payment data',
          );
        case 'CREATED':
        case 'REPLAY':
          return {
            intent: this.toPublicIntent(result.intent),
            idempotentReplay: result.kind === 'REPLAY',
          };
      }
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  async getIntent(
    intentIdValue: string,
    orderAccessTokenHeader: string | undefined,
  ): Promise<GetPaymentIntentResponse> {
    try {
      const intentId = requirePaymentUuid(
        intentIdValue,
        'intentId',
      );
      const orderAccessToken =
        requirePaymentAccessToken(
          orderAccessTokenHeader,
        );
      const intent = await this.repository.findIntent(
        intentId,
        sha256PaymentValue(orderAccessToken),
      );

      if (!intent) {
        throw new NotFoundException(
          'Payment Intent was not found',
        );
      }

      return {
        intent: this.toPublicIntent(intent),
      };
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  async applyTestEvent(
    intentIdValue: string,
    request: ApplyTestPaymentEventRequest,
    actorIdentityId: string,
  ): Promise<ApplyTestPaymentEventResponse> {
    try {
      const intentId = requirePaymentUuid(
        intentIdValue,
        'intentId',
      );
      const eventId = normalizeTestPaymentEventId(
        request.eventId,
      );
      const status = requireTestPaymentEventStatus(
        request.status,
      );
      const actorId = requirePaymentUuid(
        actorIdentityId,
        'x-ysim-actor-id',
      );
      const occurredAt = new Date().toISOString();
      const result = await this.repository.applyEvent({
        intentId,
        provider: 'TEST',
        providerEventId: eventId,
        eventFingerprint:
          createPaymentEventFingerprint({
            intentId,
            eventId,
            status,
          }),
        normalizedStatus: status,
        actorIdentityId: actorId,
        occurredAt,
      });

      switch (result.kind) {
        case 'INTENT_NOT_FOUND':
          throw new NotFoundException(
            'Payment Intent was not found',
          );
        case 'EVENT_CONFLICT':
          throw new ConflictException(
            'Provider event identifier conflicts with an existing event',
          );
        case 'ILLEGAL_TRANSITION':
          throw new ConflictException(
            'Payment Intent cannot accept this event transition',
          );
        case 'APPLIED':
        case 'DUPLICATE':
          return {
            intent: this.toPublicIntent(result.intent),
            duplicateEvent: result.kind === 'DUPLICATE',
            orderStatus: result.orderStatus,
            orderPaymentStatus:
              result.orderPaymentStatus,
          };
      }
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  private toPublicIntent(
    intent: PersistedPaymentIntent,
  ): PaymentIntentContract {
    const {
      idempotencyKeyHash: _idempotencyHash,
      requestFingerprint: _fingerprint,
      ...publicIntent
    } = intent;

    return {
      ...publicIntent,
      currencyExponent: paymentCurrencyExponent(
        publicIntent.currency,
      ),
    };
  }

  private rethrowKnownError(error: unknown): never {
    if (
      error instanceof BadRequestException ||
      error instanceof ConflictException ||
      error instanceof NotFoundException ||
      error instanceof UnauthorizedException
    ) {
      throw error;
    }

    if (error instanceof PaymentPolicyError) {
      if (
        error.message ===
        'TEST payment provider is disabled'
      ) {
        throw new ServiceUnavailableException(
          error.message,
        );
      }
      if (
        error.message.includes(
          'x-ysim-order-access-token',
        )
      ) {
        throw new UnauthorizedException(error.message);
      }
      throw new BadRequestException(error.message);
    }

    throw error;
  }
}
