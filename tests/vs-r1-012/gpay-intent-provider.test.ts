import {
  afterEach,
  describe,
  expect,
  it,
  vi,
} from 'vitest';

import {
  deriveGPayProviderReference,
  GPayIntentProvider,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay-intent.provider.js';
import { PaymentPolicyError } from '../../apps/api/src/modules/payment/domain/payment-policy.js';

const intentId =
  '1458c5f0-21ad-4e75-9ec6-0a9641e81866';
const createdAt = '2026-07-30T08:00:00.000Z';
const enabled = {
  YSIM_GPAY_PAYMENT_ENABLED: 'true',
  YSIM_GPAY_ENVIRONMENT: 'SANDBOX',
  YSIM_GPAY_CONTRACT_STATUS: 'PROBED',
};

afterEach(() => {
  vi.unstubAllGlobals();
});

describe('GPay intent reservation provider', () => {
  it('creates a normalized GPAY provider reference', () => {
    const session = new GPayIntentProvider().createIntent(
      { intentId, createdAt },
      enabled,
    );

    expect(session.providerReference).toBe(
      'GPY-1458C5F021AD4E759EC60A9641E81866',
    );
    expect(session.providerReference).toMatch(
      /^GPY-[0-9A-F]{32}$/u,
    );
  });

  it('derives a fifteen-minute expiry', () => {
    const session = new GPayIntentProvider().createIntent(
      { intentId, createdAt },
      enabled,
    );

    expect(session.expiresAt).toBe(
      '2026-07-30T08:15:00.000Z',
    );
  });

  it('uses the full normalized UUID entropy', () => {
    expect(deriveGPayProviderReference(intentId)).not.toBe(
      deriveGPayProviderReference(
        '1458c5f0-21ad-4e75-9ec6-0a9641e81867',
      ),
    );
  });

  it('fails closed when GPAY payment is disabled', () => {
    expect(() => new GPayIntentProvider().createIntent(
      { intentId, createdAt },
      {
        ...enabled,
        YSIM_GPAY_PAYMENT_ENABLED: 'false',
      },
    )).toThrow(PaymentPolicyError);
  });

  it('blocks production reservation', () => {
    expect(() => new GPayIntentProvider().createIntent(
      { intentId, createdAt },
      {
        ...enabled,
        YSIM_GPAY_ENVIRONMENT: 'PRODUCTION',
      },
    )).toThrow(
      'GPAY payment intent reservation is sandbox-only',
    );
  });

  it('requires an accepted PROBED contract', () => {
    expect(() => new GPayIntentProvider().createIntent(
      { intentId, createdAt },
      {
        ...enabled,
        YSIM_GPAY_CONTRACT_STATUS: 'UNVERIFIED',
      },
    )).toThrow(
      'GPAY contract must be PROBED',
    );
  });

  it('returns only the approved safe session fields', () => {
    const session = new GPayIntentProvider().createIntent(
      { intentId, createdAt },
      enabled,
    );

    expect(Object.keys(session).sort()).toEqual([
      'expiresAt',
      'providerReference',
    ]);
    expect(JSON.stringify(session)).not.toMatch(
      /private|certificate|signature|credential|secret/iu,
    );
  });

  it('does not perform an outbound network request', () => {
    const fetchSpy = vi.fn();
    vi.stubGlobal('fetch', fetchSpy);

    new GPayIntentProvider().createIntent(
      { intentId, createdAt },
      enabled,
    );

    expect(fetchSpy).not.toHaveBeenCalled();
  });
});
