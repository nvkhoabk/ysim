import {
  generateKeyPairSync,
} from 'node:crypto';
import {
  mkdtemp,
  rm,
  writeFile,
} from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

import {
  afterEach,
  describe,
  expect,
  it,
} from 'vitest';

import {
  canonicalGPayWebhook,
  GPayWebhookVerifier,
  loadGPayWebhookConfig,
  normalizeGPayWebhookStatus,
  parseGPayWebhookBody,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.webhook.js';
import {
  signGPayCanonical,
} from '../../apps/api/src/modules/payment/infrastructure/gpay/gpay.crypto.js';

const original = { ...process.env };
const directories: string[] = [];

afterEach(async () => {
  process.env = { ...original };
  await Promise.all(
    directories.splice(0).map(
      async (directory) => {
        await rm(directory, {
          recursive: true,
          force: true,
        });
      },
    ),
  );
});

const body = {
  providerReference: 'GPY-RUNTIMEPAYMENT0001',
  status: 'SUCCESS' as const,
  amountMinor: '338000',
  currency: 'VND' as const,
  occurredAt: '2026-07-30T13:00:00.000Z',
};

const fixture = async () => {
  const keyPair = generateKeyPairSync('rsa', {
    modulusLength: 2048,
    publicKeyEncoding: {
      type: 'spki',
      format: 'pem',
    },
    privateKeyEncoding: {
      type: 'pkcs8',
      format: 'pem',
    },
  });
  const directory = await mkdtemp(
    join(tmpdir(), 'ysim-gpay-webhook-'),
  );
  directories.push(directory);
  const certificatePath = join(
    directory,
    'provider-public.pem',
  );
  await writeFile(
    certificatePath,
    keyPair.publicKey,
    'utf8',
  );

  process.env.YSIM_GPAY_WEBHOOK_ENABLED = 'true';
  process.env.YSIM_GPAY_ENVIRONMENT = 'SANDBOX';
  process.env.YSIM_GPAY_CONTRACT_STATUS = 'PROBED';
  process.env.YSIM_GPAY_VERIFY_CERTIFICATE_PATH =
    certificatePath;
  process.env.YSIM_GPAY_WEBHOOK_ACTOR_ID =
    '10000000-0000-4000-8000-000000000001';
  process.env.YSIM_GPAY_WEBHOOK_MAX_SKEW_SECONDS =
    '300';

  return {
    verifier: new GPayWebhookVerifier(),
    privateKey: keyPair.privateKey,
  };
};

describe('GPay webhook verification policy', () => {
  it('loads sandbox configuration', () => {
    process.env.YSIM_GPAY_WEBHOOK_ENABLED = 'true';
    process.env.YSIM_GPAY_ENVIRONMENT = 'SANDBOX';
    process.env.YSIM_GPAY_CONTRACT_STATUS = 'PROBED';
    process.env.YSIM_GPAY_VERIFY_CERTIFICATE_PATH =
      '/tmp/provider.pem';
    process.env.YSIM_GPAY_WEBHOOK_ACTOR_ID =
      '10000000-0000-4000-8000-000000000001';

    expect(loadGPayWebhookConfig()).toMatchObject({
      maxSkewSeconds: 300,
    });
  });

  it('blocks production', () => {
    process.env.YSIM_GPAY_WEBHOOK_ENABLED = 'true';
    process.env.YSIM_GPAY_ENVIRONMENT = 'PRODUCTION';
    process.env.YSIM_GPAY_CONTRACT_STATUS = 'PROBED';
    process.env.YSIM_GPAY_VERIFY_CERTIFICATE_PATH =
      '/tmp/provider.pem';
    process.env.YSIM_GPAY_WEBHOOK_ACTOR_ID =
      '10000000-0000-4000-8000-000000000001';

    expect(() => loadGPayWebhookConfig())
      .toThrow(/SANDBOX/u);
  });

  it('requires PROBED contract status', () => {
    process.env.YSIM_GPAY_WEBHOOK_ENABLED = 'true';
    process.env.YSIM_GPAY_ENVIRONMENT = 'SANDBOX';
    process.env.YSIM_GPAY_CONTRACT_STATUS = 'UNVERIFIED';
    process.env.YSIM_GPAY_VERIFY_CERTIFICATE_PATH =
      '/tmp/provider.pem';
    process.env.YSIM_GPAY_WEBHOOK_ACTOR_ID =
      '10000000-0000-4000-8000-000000000001';

    expect(() => loadGPayWebhookConfig())
      .toThrow(/PROBED/u);
  });

  it('requires an absolute certificate path', () => {
    process.env.YSIM_GPAY_WEBHOOK_ENABLED = 'true';
    process.env.YSIM_GPAY_ENVIRONMENT = 'SANDBOX';
    process.env.YSIM_GPAY_CONTRACT_STATUS = 'PROBED';
    process.env.YSIM_GPAY_VERIFY_CERTIFICATE_PATH =
      'provider.pem';
    process.env.YSIM_GPAY_WEBHOOK_ACTOR_ID =
      '10000000-0000-4000-8000-000000000001';

    expect(() => loadGPayWebhookConfig())
      .toThrow(/absolute/u);
  });

  it('accepts the exact body', () => {
    expect(parseGPayWebhookBody(body)).toEqual(body);
  });

  it('rejects unknown body fields', () => {
    expect(() => parseGPayWebhookBody({
      ...body,
      rawPayload: 'forbidden',
    })).toThrow(/unsupported fields/u);
  });

  it('rejects invalid provider reference', () => {
    expect(() => parseGPayWebhookBody({
      ...body,
      providerReference: 'bad',
    })).toThrow(/providerReference/u);
  });

  it('normalizes all statuses', () => {
    expect([
      normalizeGPayWebhookStatus('PENDING'),
      normalizeGPayWebhookStatus('SUCCESS'),
      normalizeGPayWebhookStatus('FAILED'),
      normalizeGPayWebhookStatus('EXPIRED'),
    ]).toEqual([
      'PENDING',
      'SUCCEEDED',
      'FAILED',
      'EXPIRED',
    ]);
  });

  it('produces deterministic canonical text', () => {
    expect(canonicalGPayWebhook({
      eventId: 'gpay:event:0001',
      timestamp: body.occurredAt,
      body,
    })).toContain(
      'GPAY-WEBHOOK-V1\ngpay:event:0001',
    );
  });

  it('verifies a signed event', async () => {
    const { verifier, privateKey } =
      await fixture();
    const eventId = 'gpay:event:0001';
    const signature = signGPayCanonical(
      canonicalGPayWebhook({
        eventId,
        timestamp: body.occurredAt,
        body,
      }),
      privateKey,
    );

    await expect(verifier.verify(
      {
        eventId,
        timestamp: body.occurredAt,
        signature,
      },
      body,
      new Date(body.occurredAt),
    )).resolves.toMatchObject({
      normalizedStatus: 'SUCCEEDED',
      amountMinor: '338000',
      currency: 'VND',
    });
  });

  it('rejects invalid signature', async () => {
    const { verifier } = await fixture();

    await expect(verifier.verify(
      {
        eventId: 'gpay:event:0001',
        timestamp: body.occurredAt,
        signature: 'x'.repeat(64),
      },
      body,
      new Date(body.occurredAt),
    )).rejects.toThrow(/signature/u);
  });

  it('rejects stale timestamp', async () => {
    const { verifier, privateKey } =
      await fixture();
    const eventId = 'gpay:event:0001';
    const signature = signGPayCanonical(
      canonicalGPayWebhook({
        eventId,
        timestamp: body.occurredAt,
        body,
      }),
      privateKey,
    );

    await expect(verifier.verify(
      {
        eventId,
        timestamp: body.occurredAt,
        signature,
      },
      body,
      new Date('2026-07-30T13:10:01.000Z'),
    )).rejects.toThrow(/replay window/u);
  });
});
