import { describe, expect, it } from 'vitest';

import {
  runSyntheticOrderOutboxHarness,
} from '../../apps/api/src/modules/commissioning/application/synthetic-order-outbox-harness.js';

const baseline = {
  YSIM_COMMISSIONING_MODE: 'SANDBOX',
  YSIM_COMMISSIONING_RUN_NAMESPACE:
    'vs-r1-042-synthetic-a1b2c3d4',
  YSIM_COMMISSIONING_TRANSACTION_CAP: '1',
  YSIM_COMMISSIONING_EMAIL_ALLOWLIST:
    'qa1@example.test,qa2@example.test,qa3@example.test',
  DATABASE_URL: 'postgresql://redacted',
  YSIM_REDIS_URL: 'redis://redacted',
  YSIM_GPAY_EXECUTION_ENABLED: 'false',
  YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED: 'false',
  YSIM_CUSTOMER_EMAIL_ENABLED: 'false',
  YSIM_CUSTOMER_EMAIL_MODE: 'disabled',
};

describe('VS-R1-042 synthetic order/outbox harness', () => {
  it('proves one synthetic path to pending procurement', () => {
    const checkpoint =
      runSyntheticOrderOutboxHarness(baseline);

    expect(checkpoint).toMatchObject({
      schemaVersion: 1,
      sliceId: 'VS-R1-042',
      proofKind: 'SYNTHETIC_ORDER_OUTBOX',
      transactionCount: 1,
      order: {
        status: 'CONFIRMED',
        paymentStatus: 'PAID',
        fulfillmentStatus: 'UNFULFILLED',
      },
      payment: {
        provider: 'TEST',
        status: 'SUCCEEDED',
      },
      outbox: {
        eventType: 'payment.succeeded.v1',
        syntheticClaimAttemptCount: 1,
        consumerResult: 'PENDING_SUPPLIER',
      },
      procurement: {
        supplierEnvironment: 'SANDBOX',
        status: 'PENDING_SUPPLIER',
        quantity: 1,
      },
    });
    expect(checkpoint.checkpointSha256)
      .toMatch(/^[0-9a-f]{64}$/u);
  });

  it('is deterministic and returns an immutable checkpoint', () => {
    const first =
      runSyntheticOrderOutboxHarness(baseline);
    const second =
      runSyntheticOrderOutboxHarness(baseline);

    expect(first).toEqual(second);
    expect(Object.isFrozen(first)).toBe(true);
    expect(Object.isFrozen(first.order)).toBe(true);
    expect(Object.isFrozen(first.outbox)).toBe(true);
    expect(Object.isFrozen(first.procurement)).toBe(true);
  });

  it('changes correlation identities for another run namespace', () => {
    const first =
      runSyntheticOrderOutboxHarness(baseline);
    const second = runSyntheticOrderOutboxHarness({
      ...baseline,
      YSIM_COMMISSIONING_RUN_NAMESPACE:
        'vs-r1-042-synthetic-b2c3d4e5',
    });

    expect(second.correlationId)
      .not.toBe(first.correlationId);
    expect(second.order.id).not.toBe(first.order.id);
    expect(second.checkpointSha256)
      .not.toBe(first.checkpointSha256);
  });

  it.each([
    'YSIM_GPAY_EXECUTION_ENABLED',
    'YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED',
    'YSIM_CUSTOMER_EMAIL_ENABLED',
  ])('fails before proof when %s is enabled', (name) => {
    expect(() => runSyntheticOrderOutboxHarness({
      ...baseline,
      [name]: 'true',
    })).toThrow(`${name} must be false`);
  });

  it('fails when the transaction cap is not exactly one', () => {
    expect(() => runSyntheticOrderOutboxHarness({
      ...baseline,
      YSIM_COMMISSIONING_TRANSACTION_CAP: '2',
    })).toThrow(
      'YSIM_COMMISSIONING_TRANSACTION_CAP must be 1',
    );
  });

  it('records zero external effects without exposing environment values', () => {
    const checkpoint =
      runSyntheticOrderOutboxHarness(baseline);
    const serialized = JSON.stringify(checkpoint);

    expect(checkpoint.safety).toEqual({
      gpayExecutionEnabled: false,
      gigagoSubmitEnabled: false,
      customerEmailEnabled: false,
      databaseMutationPerformed: false,
      redisCommandsPerformed: false,
      externalProviderCalls: 0,
      customerEmailsSent: 0,
    });
    expect(serialized).not.toContain('qa1@example.test');
    expect(serialized).not.toContain('postgresql://');
    expect(serialized).not.toContain('redis://');
  });
});
