import { describe, expect, it } from 'vitest';

import type {
  VerifiedGPayWebhookContract,
} from '../../packages/contracts/src/index.js';
import {
  GPayWebhookApplicationService,
} from '../../apps/api/src/modules/payment/application/gpay-webhook-application.service.js';

const intent = {
  id: '10000000-0000-4000-8000-000000000001',
  orderId: '20000000-0000-4000-8000-000000000001',
  orderNumber: 'YS-20260730-ABCDEF123456',
  provider: 'GPAY' as const,
  providerReference: 'GPY-RUNTIMEPAYMENT0001',
  attemptNumber: 1,
  amountMinor: '338000',
  currency: 'VND' as const,
  status: 'PENDING' as const,
  createdAt: '2026-07-30T00:00:00.000Z',
  expiresAt: '2026-07-30T00:15:00.000Z',
  updatedAt: '2026-07-30T00:00:00.000Z',
  version: 1,
  idempotencyKeyHash: 'a'.repeat(64),
  requestFingerprint: 'b'.repeat(64),
};

const verified = (
  overrides: Partial<VerifiedGPayWebhookContract> = {},
): VerifiedGPayWebhookContract => ({
  eventId: 'gpay:event:application-0001',
  providerReference: intent.providerReference,
  normalizedStatus: 'SUCCEEDED',
  amountMinor: intent.amountMinor,
  currency: intent.currency,
  occurredAt: '2026-07-30T00:01:00.000Z',
  actorIdentityId:
    '30000000-0000-4000-8000-000000000001',
  ...overrides,
});

const repository = (options: {
  found?: boolean;
  kind?: 'APPLIED' | 'DUPLICATE'
    | 'INTENT_NOT_FOUND'
    | 'EVENT_CONFLICT'
    | 'ILLEGAL_TRANSITION';
} = {}) => {
  const calls: unknown[] = [];
  return {
    calls,
    async findIntentByProviderReference() {
      return options.found === false ? null : intent;
    },
    async applyEvent(input: unknown) {
      calls.push(input);
      const kind = options.kind ?? 'APPLIED';
      if (
        kind === 'INTENT_NOT_FOUND' ||
        kind === 'EVENT_CONFLICT' ||
        kind === 'ILLEGAL_TRANSITION'
      ) {
        return { kind };
      }
      return {
        kind,
        intent: {
          ...intent,
          status: 'SUCCEEDED' as const,
        },
        orderStatus: 'CONFIRMED' as const,
        orderPaymentStatus: 'PAID' as const,
      };
    },
  };
};

describe('GPay webhook application service', () => {
  it('applies a verified event to the matching GPay intent', async () => {
    const fake = repository();
    const service = new GPayWebhookApplicationService(
      fake as never,
    );
    const result = await service.applyVerifiedEvent(
      verified(),
    );
    expect(result).toEqual({
      accepted: true,
      duplicateEvent: false,
      paymentIntentId: intent.id,
      paymentIntentStatus: 'SUCCEEDED',
      orderStatus: 'CONFIRMED',
      orderPaymentStatus: 'PAID',
    });
    expect(fake.calls).toHaveLength(1);
  });

  it('reports an exact duplicate', async () => {
    const service = new GPayWebhookApplicationService(
      repository({ kind: 'DUPLICATE' }) as never,
    );
    const result = await service.applyVerifiedEvent(
      verified(),
    );
    expect(result.duplicateEvent).toBe(true);
  });

  it('rejects an unknown provider reference', async () => {
    const service = new GPayWebhookApplicationService(
      repository({ found: false }) as never,
    );
    await expect(
      service.applyVerifiedEvent(verified()),
    ).rejects.toMatchObject({ status: 404 });
  });

  it('rejects amount mismatch before persistence', async () => {
    const fake = repository();
    const service = new GPayWebhookApplicationService(
      fake as never,
    );
    await expect(
      service.applyVerifiedEvent(
        verified({ amountMinor: '337999' }),
      ),
    ).rejects.toMatchObject({ status: 409 });
    expect(fake.calls).toHaveLength(0);
  });

  it('rejects currency mismatch before persistence', async () => {
    const fake = repository();
    const service = new GPayWebhookApplicationService(
      fake as never,
    );
    await expect(
      service.applyVerifiedEvent(
        verified({ currency: 'USD' }),
      ),
    ).rejects.toMatchObject({ status: 409 });
    expect(fake.calls).toHaveLength(0);
  });

  it('maps event conflict to HTTP 409', async () => {
    const service = new GPayWebhookApplicationService(
      repository({ kind: 'EVENT_CONFLICT' }) as never,
    );
    await expect(
      service.applyVerifiedEvent(verified()),
    ).rejects.toMatchObject({ status: 409 });
  });

  it('maps illegal transition to HTTP 409', async () => {
    const service = new GPayWebhookApplicationService(
      repository({ kind: 'ILLEGAL_TRANSITION' }) as never,
    );
    await expect(
      service.applyVerifiedEvent(verified()),
    ).rejects.toMatchObject({ status: 409 });
  });

  it('creates a stable 64-character fingerprint', async () => {
    const fake = repository();
    const service = new GPayWebhookApplicationService(
      fake as never,
    );
    await service.applyVerifiedEvent(verified());
    expect(fake.calls[0]).toMatchObject({
      eventFingerprint:
        expect.stringMatching(/^[0-9a-f]{64}$/u),
    });
  });
});
