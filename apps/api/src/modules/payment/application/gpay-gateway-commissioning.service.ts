import { createHash } from 'node:crypto';

import {
  BadRequestException,
  ConflictException,
  Injectable,
  NotFoundException,
  ServiceUnavailableException,
} from '@nestjs/common';
import type {
  ApplyGPayWebhookResponse,
  InitializeGPayCommissioningResponse,
  ReconcileGPayCommissioningResponse,
  VerifiedGPayWebhookContract,
} from '@ysim/contracts';

import {
  authoritativeEventFromGPayCallback,
  authoritativeEventFromGPayQuery,
  GPayGatewayAuthoritativeError,
} from '../infrastructure/gpay/gpay.gateway.authoritative.js';
import {
  normalizeGPayGatewayStatus,
  verifyGPayGatewayCallback,
  GPayGatewayCallbackError,
} from '../infrastructure/gpay/gpay.gateway.callback.js';
import {
  GPayGatewayClient,
  GPayGatewayClientError,
} from '../infrastructure/gpay/gpay.gateway.client.js';
import {
  GPayGatewayConfigError,
} from '../infrastructure/gpay/gpay.gateway.config.js';
import {
  GPayCryptoError,
} from '../infrastructure/gpay/gpay.crypto.js';
import {
  loadGPayGatewayExecutionPolicy,
  GPayGatewayExecutionPolicyError,
} from '../infrastructure/gpay/gpay.gateway.execution-policy.js';
import {
  GPayGatewaySessionRepository,
  type PersistedGPayCommissioningSession,
} from '../infrastructure/gpay/gpay.gateway.session.repository.js';
import type {
  GPayGatewayQueryOrderResult,
  VerifiedGPayGatewayCallback,
} from '../infrastructure/gpay/gpay.gateway.types.js';
import { GPayWebhookApplicationService } from './gpay-webhook-application.service.js';

const UUID_PATTERN =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;

const requireUuid = (value: string, name: string): string => {
  if (!UUID_PATTERN.test(value)) {
    throw new BadRequestException(`${name} must be a UUID`);
  }
  return value.toLowerCase();
};

const evidenceFingerprint = (
  event: VerifiedGPayWebhookContract,
): string => createHash('sha256')
  .update(JSON.stringify(event), 'utf8')
  .digest('hex');

const safeAmount = (value: string): number => {
  const amount = Number(value);
  if (!Number.isSafeInteger(amount) || amount <= 0) {
    throw new ConflictException(
      'GPay Payment Intent amount is outside the safe execution boundary',
    );
  }
  return amount;
};

@Injectable()
export class GPayGatewayCommissioningService {
  constructor(
    private readonly repository: GPayGatewaySessionRepository,
    private readonly client: GPayGatewayClient,
    private readonly webhookApplication:
      GPayWebhookApplicationService,
  ) {}

  async initialize(
    paymentIntentIdValue: string,
    actorIdentityIdValue: string,
  ): Promise<InitializeGPayCommissioningResponse> {
    const paymentIntentId = requireUuid(
      paymentIntentIdValue,
      'paymentIntentId',
    );
    const actorIdentityId = requireUuid(
      actorIdentityIdValue,
      'x-ysim-actor-id',
    );

    try {
      const policy = loadGPayGatewayExecutionPolicy();
      const occurredAt = new Date().toISOString();
      const reservation = await this.repository.reserveInitAttempt({
        paymentIntentId,
        runNamespace: policy.runNamespace,
        actorIdentityId,
        queryCap: policy.queryCap,
        occurredAt,
      });
      switch (reservation.kind) {
        case 'BUDGET_ALREADY_CONSUMED':
          throw new ConflictException(
            'VS-R1-043 GPay transaction budget is already consumed',
          );
        case 'INTENT_NOT_FOUND':
          throw new NotFoundException(
            'Eligible GPay Payment Intent was not found',
          );
        case 'INTENT_NOT_ELIGIBLE':
          throw new ConflictException(
            'GPay Payment Intent is outside the VN/VND commissioning boundary',
          );
        case 'RESERVED':
          break;
      }

      const session = reservation.session;
      const result = await this.client.initOrder({
        amount: safeAmount(session.amountMinor),
        callbackUrl: policy.callbackUrl,
        customerId: policy.customerId,
        embedData: JSON.stringify({
          sliceId: session.sliceId,
          runNamespace: session.runNamespace,
          paymentIntentId: session.paymentIntentId,
        }),
        merchantOrderId: session.merchantOrderId,
        webhookUrl: policy.webhookUrl,
        description: 'YSim VS-R1-043 GPay sandbox commissioning',
        title: 'YSim sandbox payment',
      });
      const bound = await this.repository.bindInitResult({
        paymentIntentId: session.paymentIntentId,
        merchantOrderId: result.merchantOrderId,
        billId: result.billId,
        billUrl: result.billUrl,
        expiredTime: result.expiredTime,
        occurredAt: new Date().toISOString(),
      });
      if (!bound?.billId || !bound.billUrl || !bound.expiredTime) {
        throw new ConflictException(
          'GPay init result could not be bound; the transaction budget remains consumed',
        );
      }

      return {
        sliceId: bound.sliceId,
        runNamespace: bound.runNamespace,
        paymentIntentId: bound.paymentIntentId,
        merchantOrderId: bound.merchantOrderId,
        billId: bound.billId,
        billUrl: bound.billUrl,
        expiredTime: bound.expiredTime,
        sessionStatus: 'INITIALIZED',
        initAttemptCount: 1,
        queryAttemptCount: bound.queryAttemptCount,
        queryCap: bound.queryCap,
      };
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  async applyCallback(
    input: URLSearchParams | Record<string, unknown>,
    fallbackSignature?: string,
  ): Promise<ApplyGPayWebhookResponse> {
    try {
      const verified = await verifyGPayGatewayCallback(input, {
        fallbackSignature,
      });
      const result = await this.applyVerifiedCallback(verified);
      return result.application;
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  async applyVerifiedCallback(
    callback: VerifiedGPayGatewayCallback,
  ): Promise<{
    application: ApplyGPayWebhookResponse;
    session: PersistedGPayCommissioningSession;
  }> {
    const session = await this.requireSession({
      merchantOrderId: callback.merchantOrderId,
      billId: callback.gpayBillId,
    });
    const event = authoritativeEventFromGPayCallback(
      this.binding(session),
      callback,
    );
    const application =
      await this.webhookApplication.applyVerifiedEvent(event);
    const recorded = await this.repository.recordEvidence({
      merchantOrderId: callback.merchantOrderId,
      billId: callback.gpayBillId,
      source: 'CALLBACK',
      providerEventId: event.eventId,
      evidenceFingerprint: evidenceFingerprint(event),
      normalizedStatus: callback.normalizedStatus,
      occurredAt: new Date().toISOString(),
    });
    return {
      application,
      session: this.requireRecorded(recorded),
    };
  }

  async reconcile(
    paymentIntentIdValue: string,
  ): Promise<ReconcileGPayCommissioningResponse> {
    const paymentIntentId = requireUuid(
      paymentIntentIdValue,
      'paymentIntentId',
    );
    try {
      loadGPayGatewayExecutionPolicy();
      const reservation =
        await this.repository.reserveQueryAttempt(
          paymentIntentId,
          new Date().toISOString(),
        );
      switch (reservation.kind) {
        case 'SESSION_NOT_FOUND':
          throw new NotFoundException(
            'GPay commissioning session was not found',
          );
        case 'SESSION_NOT_INITIALIZED':
          throw new ConflictException(
            'GPay init result is uncertain; reconciliation cannot start automatically',
          );
        case 'SESSION_TERMINAL':
          throw new ConflictException(
            'GPay commissioning session is already terminal',
          );
        case 'QUERY_BUDGET_CONSUMED':
          throw new ConflictException(
            'GPay query-order reconciliation budget is consumed',
          );
        case 'RESERVED':
          break;
      }
      const session = reservation.session;
      if (!session.billId) {
        throw new ConflictException(
          'GPay commissioning session has no bound bill',
        );
      }
      const query = await this.client.queryOrder({
        gpayBillId: session.billId,
        merchantOrderId: session.merchantOrderId,
      });
      const result = await this.applyQuery(session, query);
      return {
        sliceId: result.session.sliceId,
        runNamespace: result.session.runNamespace,
        paymentIntentId: result.session.paymentIntentId,
        sessionStatus: result.session.status,
        paymentIntentStatus:
          result.application.paymentIntentStatus,
        orderStatus: result.application.orderStatus,
        orderPaymentStatus:
          result.application.orderPaymentStatus,
        duplicateEvent: result.application.duplicateEvent,
        queryAttemptCount: result.session.queryAttemptCount,
        queryCap: result.session.queryCap,
      };
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  private async applyQuery(
    session: PersistedGPayCommissioningSession,
    query: GPayGatewayQueryOrderResult,
  ): Promise<{
    application: ApplyGPayWebhookResponse;
    session: PersistedGPayCommissioningSession;
  }> {
    const event = authoritativeEventFromGPayQuery(
      this.binding(session),
      query,
    );
    const application =
      await this.webhookApplication.applyVerifiedEvent(event);
    const recorded = await this.repository.recordEvidence({
      merchantOrderId: query.merchantOrderId,
      billId: query.gpayBillId,
      source: 'QUERY',
      providerEventId: event.eventId,
      evidenceFingerprint: evidenceFingerprint(event),
      normalizedStatus: normalizeGPayGatewayStatus(
        query.status ?? '',
      ),
      occurredAt: new Date().toISOString(),
    });
    return {
      application,
      session: this.requireRecorded(recorded),
    };
  }

  private binding(
    session: PersistedGPayCommissioningSession,
  ) {
    if (!session.billId) {
      throw new ConflictException(
        'GPay commissioning session has no bound bill',
      );
    }
    return {
      merchantOrderId: session.merchantOrderId,
      billId: session.billId,
      amountMinor: session.amountMinor,
      currency: session.currency,
      actorIdentityId: session.actorIdentityId,
      occurredAt: session.createdAt,
    };
  }

  private requireSession(input: {
    merchantOrderId: string;
    billId: string;
  }): Promise<PersistedGPayCommissioningSession> {
    return this.repository.findByProviderIdentity(input).then(
      (session) => {
        if (!session) {
          throw new NotFoundException(
            'GPay commissioning session was not found',
          );
        }
        return session;
      },
    );
  }

  private requireRecorded(
    result: Awaited<ReturnType<
      GPayGatewaySessionRepository['recordEvidence']
    >>,
  ): PersistedGPayCommissioningSession {
    switch (result.kind) {
      case 'APPLIED':
      case 'DUPLICATE':
        return result.session;
      case 'SESSION_NOT_FOUND':
        throw new NotFoundException(
          'GPay commissioning session was not found',
        );
      case 'IDENTITY_CONFLICT':
      case 'EVIDENCE_CONFLICT':
      case 'TERMINAL_CONFLICT':
        throw new ConflictException(
          'GPay authoritative evidence conflicts with the commissioning ledger',
        );
    }
  }

  private rethrowKnownError(error: unknown): never {
    if (
      error instanceof BadRequestException ||
      error instanceof ConflictException ||
      error instanceof NotFoundException ||
      error instanceof ServiceUnavailableException
    ) {
      throw error;
    }
    if (
      error instanceof GPayGatewayExecutionPolicyError ||
      error instanceof GPayGatewayClientError ||
      error instanceof GPayGatewayConfigError ||
      error instanceof GPayCryptoError
    ) {
      throw new ServiceUnavailableException(error.message);
    }
    if (
      error instanceof GPayGatewayCallbackError ||
      error instanceof GPayGatewayAuthoritativeError
    ) {
      throw new BadRequestException(error.message);
    }
    throw error;
  }
}
