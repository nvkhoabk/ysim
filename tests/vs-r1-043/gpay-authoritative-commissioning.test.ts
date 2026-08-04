import { createHash } from 'node:crypto';

import { describe, expect, it } from 'vitest';

import {
  authoritativeEventFromGPayCallback,
  authoritativeEventFromGPayQuery,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.gateway.authoritative.js';
import {
  loadGPayGatewayExecutionPolicy,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.gateway.execution-policy.js';
import {
  applyGPayGatewayEvidence,
  beginGPayGatewayInitAttempt,
  bindGPayGatewayInitResult,
  createGPayGatewaySession,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.gateway.session-policy.js';

const environment = (): Record<string, string> => ({
  YSIM_COMMISSIONING_MODE: 'SANDBOX',
  YSIM_COMMISSIONING_RUN_NAMESPACE: 'vs-r1-043-authoritative-a1b2c3d4',
  YSIM_COMMISSIONING_TRANSACTION_CAP: '1',
  YSIM_COMMISSIONING_MARKET: 'VN',
  YSIM_COMMISSIONING_CURRENCY: 'VND',
  YSIM_GPAY_EXECUTION_ENABLED: 'true',
  YSIM_GPAY_QUERY_CAP: '12',
  YSIM_GPAY_CALLBACK_URL:
    'https://portal.ysim.vn/api/platform/api/r1/payments/gpay/gateway/callback',
  YSIM_GPAY_WEBHOOK_URL:
    'https://portal.ysim.vn/api/platform/api/r1/payments/gpay/gateway/webhook',
  YSIM_GPAY_COMMISSIONING_CUSTOMER_ID:
    'vs-r1-043-sandbox-customer',
  YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED: 'false',
  YSIM_CUSTOMER_EMAIL_ENABLED: 'false',
  YSIM_CUSTOMER_EMAIL_MODE: 'disabled',
  YSIM_CATALOG_SUPPLIER_ENVIRONMENT: 'SANDBOX',
});

const binding = {
  merchantOrderId: 'GPY-11111111111141118111111111111111',
  billId: 'GPAY-BILL-0001',
  amountMinor: '169000',
  currency: 'VND' as const,
  actorIdentityId: '11111111-1111-4111-8111-111111111111',
  occurredAt: '2026-08-04T00:00:00.000Z',
};

describe('VS-R1-043 authoritative GPay commissioning', () => {
  it('requires the exact bounded Vietnam/VND execution policy', () => {
    expect(loadGPayGatewayExecutionPolicy(environment()))
      .toMatchObject({
        mode: 'SANDBOX',
        transactionCap: 1,
        queryCap: 12,
        market: 'VN',
        currency: 'VND',
        customerId: 'vs-r1-043-sandbox-customer',
        gpayExecutionEnabled: true,
        gigagoSubmitEnabled: false,
        customerEmailEnabled: false,
      });

    for (const [name, value] of [
      ['YSIM_COMMISSIONING_TRANSACTION_CAP', '2'],
      ['YSIM_GPAY_EXECUTION_ENABLED', 'false'],
      ['YSIM_GIGAGO_ORDER_SUBMISSION_ENABLED', 'true'],
      ['YSIM_CUSTOMER_EMAIL_ENABLED', 'true'],
      ['YSIM_COMMISSIONING_MARKET', 'LA'],
      ['YSIM_COMMISSIONING_CURRENCY', 'USD'],
      ['YSIM_GPAY_CALLBACK_URL', 'http://portal.ysim.vn/api/r1/payments/gpay/gateway/callback'],
      ['YSIM_GPAY_WEBHOOK_URL', 'https://evil.example/api/r1/payments/gpay/gateway/webhook'],
    ]) {
      expect(() => loadGPayGatewayExecutionPolicy({
        ...environment(),
        [name]: value,
      })).toThrow();
    }
  });

  it('allows exactly one init attempt and treats an uncertain attempt as consumed', () => {
    const fresh = createGPayGatewaySession({
      runNamespace: environment().YSIM_COMMISSIONING_RUN_NAMESPACE,
      paymentIntentId: '11111111-1111-4111-8111-111111111111',
      merchantOrderId: binding.merchantOrderId,
    });
    const attempted = beginGPayGatewayInitAttempt(fresh);
    expect(attempted).toMatchObject({
      status: 'INIT_ATTEMPTED',
      initAttemptCount: 1,
    });
    expect(() => beginGPayGatewayInitAttempt(attempted))
      .toThrow(/budget/u);
    const initialized = bindGPayGatewayInitResult(
      attempted,
      binding.billId,
    );
    expect(initialized.status).toBe('INITIALIZED');
  });

  it('maps a verified callback into deterministic authoritative payment evidence', () => {
    const callback = {
      verified: true as const,
      contractVersion: 'GPAY_ALL_IN_ONE_CALLBACK_V1' as const,
      merchantOrderId: binding.merchantOrderId,
      gpayBillId: binding.billId,
      gpayTransactionId: 'GPAY-TRANS-0001',
      normalizedStatus: 'SUCCESS' as const,
      userPaymentMethod: 'QR_PAYMENT',
      canonicalSha256: 'a'.repeat(64),
    };
    const first = authoritativeEventFromGPayCallback(binding, callback);
    const second = authoritativeEventFromGPayCallback(binding, callback);
    expect(first).toEqual(second);
    expect(first).toMatchObject({
      providerReference: binding.merchantOrderId,
      normalizedStatus: 'SUCCEEDED',
      amountMinor: '169000',
      currency: 'VND',
    });
    expect(Object.isFrozen(first)).toBe(true);
  });

  it('maps provider query evidence and rejects mismatched identities', () => {
    const query = {
      provider: 'GPAY' as const,
      gpayBillId: binding.billId,
      merchantOrderId: binding.merchantOrderId,
      gpayTransactionId: 'GPAY-TRANS-0001',
      status: 'ORDER_SUCCESS',
      userPaymentMethod: 'QR_PAYMENT',
      securityRequestId: 'request-0001',
      tokenCached: true,
    };
    expect(authoritativeEventFromGPayQuery(binding, query).normalizedStatus)
      .toBe('SUCCEEDED');
    expect(() => authoritativeEventFromGPayQuery(binding, {
      ...query,
      gpayBillId: 'DIFFERENT',
    })).toThrow(/identity/u);
  });

  it('deduplicates identical evidence and rejects conflicting evidence', () => {
    const attempted = beginGPayGatewayInitAttempt(
      createGPayGatewaySession({
        runNamespace: environment().YSIM_COMMISSIONING_RUN_NAMESPACE,
        paymentIntentId: '11111111-1111-4111-8111-111111111111',
        merchantOrderId: binding.merchantOrderId,
      }),
    );
    const initialized = bindGPayGatewayInitResult(
      attempted,
      binding.billId,
    );
    const fingerprint = createHash('sha256')
      .update('accepted', 'utf8')
      .digest('hex');
    const accepted = applyGPayGatewayEvidence(initialized, {
      billId: binding.billId,
      normalizedStatus: 'SUCCESS',
      evidenceFingerprint: fingerprint,
    });
    expect(accepted.status).toBe('SUCCEEDED');
    expect(applyGPayGatewayEvidence(accepted, {
      billId: binding.billId,
      normalizedStatus: 'SUCCESS',
      evidenceFingerprint: fingerprint,
    })).toBe(accepted);
    expect(() => applyGPayGatewayEvidence(accepted, {
      billId: binding.billId,
      normalizedStatus: 'FAILED',
      evidenceFingerprint: 'b'.repeat(64),
    })).toThrow(/terminal/u);
  });

  it('allows bounded reconciliation to progress from pending to success', () => {
    const initialized = bindGPayGatewayInitResult(
      beginGPayGatewayInitAttempt(
        createGPayGatewaySession({
          runNamespace: environment().YSIM_COMMISSIONING_RUN_NAMESPACE,
          paymentIntentId: '11111111-1111-4111-8111-111111111111',
          merchantOrderId: binding.merchantOrderId,
        }),
      ),
      binding.billId,
    );
    const pending = applyGPayGatewayEvidence(initialized, {
      billId: binding.billId,
      normalizedStatus: 'PENDING',
      evidenceFingerprint: 'a'.repeat(64),
    });
    const succeeded = applyGPayGatewayEvidence(pending, {
      billId: binding.billId,
      normalizedStatus: 'SUCCESS',
      evidenceFingerprint: 'b'.repeat(64),
    });
    expect(pending.status).toBe('PENDING');
    expect(succeeded).toMatchObject({
      status: 'SUCCEEDED',
      evidenceFingerprints: ['a'.repeat(64), 'b'.repeat(64)],
    });
  });
});
