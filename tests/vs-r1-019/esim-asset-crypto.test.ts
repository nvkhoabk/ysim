import { Buffer } from 'node:buffer';

import {
  describe,
  expect,
  it,
} from 'vitest';

import {
  EsimAssetCrypto,
  EsimAssetCryptoError,
  loadEsimAssetKeyConfig,
  type EsimAssetKeyConfig,
} from '../../apps/api/src/modules/fulfillment/infrastructure/esim-asset.crypto.js';

const encryptionKey =
  Buffer.alloc(32, 0x11);
const fingerprintKey =
  Buffer.alloc(32, 0x22);

const config:
  EsimAssetKeyConfig = {
    keyId: 'runtime-v1',
    encryptionKey,
    fingerprintKey,
  };

const installation = {
  iccid:
    '8988211000000000001',
  qrCode:
    'LPA:1$rspeu.demo.net$CODE01',
  shortLink: 'asset_01',
  phoneNumber: null,
};

describe('eSIM Asset cryptography', () => {
  it('loads canonical 32-byte keys', () => {
    expect(
      loadEsimAssetKeyConfig({
        YSIM_ESIM_ASSET_KEY_ID:
          'key-v1',
        YSIM_ESIM_ASSET_ENCRYPTION_KEY_B64:
          encryptionKey
            .toString('base64'),
        YSIM_ESIM_ASSET_FINGERPRINT_KEY_B64:
          fingerprintKey
            .toString('base64'),
      }),
    ).toMatchObject({
      keyId: 'key-v1',
    });
  });

  it('rejects a missing key identity', () => {
    expect(() =>
      loadEsimAssetKeyConfig({
        YSIM_ESIM_ASSET_ENCRYPTION_KEY_B64:
          encryptionKey
            .toString('base64'),
        YSIM_ESIM_ASSET_FINGERPRINT_KEY_B64:
          fingerprintKey
            .toString('base64'),
      }),
    ).toThrow(
      EsimAssetCryptoError,
    );
  });

  it('rejects a short encryption key', () => {
    expect(() =>
      loadEsimAssetKeyConfig({
        YSIM_ESIM_ASSET_KEY_ID:
          'key-v1',
        YSIM_ESIM_ASSET_ENCRYPTION_KEY_B64:
          Buffer.alloc(16)
            .toString('base64'),
        YSIM_ESIM_ASSET_FINGERPRINT_KEY_B64:
          fingerprintKey
            .toString('base64'),
      }),
    ).toThrow(
      'must decode to 32 bytes',
    );
  });

  it('creates a deterministic ICCID fingerprint', () => {
    const crypto =
      new EsimAssetCrypto(
        config,
      );

    expect(
      crypto.fingerprintIccid(
        installation.iccid,
      ),
    ).toBe(
      crypto.fingerprintIccid(
        installation.iccid,
      ),
    );
  });

  it('separates different ICCID fingerprints', () => {
    const crypto =
      new EsimAssetCrypto(
        config,
      );

    expect(
      crypto.fingerprintIccid(
        '8988211000000000001',
      ),
    ).not.toBe(
      crypto.fingerprintIccid(
        '8988211000000000002',
      ),
    );
  });

  it('encrypts without retaining plaintext', () => {
    const crypto =
      new EsimAssetCrypto(
        config,
        () =>
          Buffer.alloc(
            12,
            0x33,
          ),
      );
    const envelope =
      crypto.encrypt(
        installation,
        'asset-aad',
      );
    const serialized =
      JSON.stringify(envelope);

    expect(envelope).toMatchObject({
      schemaVersion:
        'ysim.esim-installation/v1',
      algorithm:
        'AES-256-GCM',
      keyId: 'runtime-v1',
    });
    expect(serialized).not.toContain(
      installation.iccid,
    );
    expect(serialized).not.toContain(
      installation.qrCode,
    );
    expect(serialized).not.toContain(
      installation.shortLink,
    );
  });

  it('decrypts an authenticated payload', () => {
    const crypto =
      new EsimAssetCrypto(
        config,
        () =>
          Buffer.alloc(
            12,
            0x44,
          ),
      );
    const envelope =
      crypto.encrypt(
        installation,
        'asset-aad',
      );

    expect(
      crypto.decrypt(
        envelope,
        'asset-aad',
      ),
    ).toEqual(installation);
  });

  it('rejects an AAD mismatch', () => {
    const crypto =
      new EsimAssetCrypto(
        config,
        () =>
          Buffer.alloc(
            12,
            0x55,
          ),
      );
    const envelope =
      crypto.encrypt(
        installation,
        'asset-aad',
      );

    expect(() =>
      crypto.decrypt(
        envelope,
        'different-aad',
      ),
    ).toThrow(
      'authentication failed',
    );
  });

  it('rejects an unavailable key identity', () => {
    const first =
      new EsimAssetCrypto(
        config,
        () =>
          Buffer.alloc(
            12,
            0x66,
          ),
      );
    const second =
      new EsimAssetCrypto({
        ...config,
        keyId: 'runtime-v2',
      });
    const envelope =
      first.encrypt(
        installation,
        'asset-aad',
      );

    expect(() =>
      second.decrypt(
        envelope,
        'asset-aad',
      ),
    ).toThrow(
      'key ID is unavailable',
    );
  });

  it('uses a unique IV for repeated encryption', () => {
    let marker = 0;
    const crypto =
      new EsimAssetCrypto(
        config,
        (size) => {
          marker += 1;
          return Buffer.alloc(
            size,
            marker,
          );
        },
      );
    const first =
      crypto.encrypt(
        installation,
        'asset-aad',
      );
    const second =
      crypto.encrypt(
        installation,
        'asset-aad',
      );

    expect(first.iv).not.toBe(
      second.iv,
    );
    expect(
      first.ciphertext,
    ).not.toBe(
      second.ciphertext,
    );
  });
});
