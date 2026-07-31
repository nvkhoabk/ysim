import { Buffer } from 'node:buffer';

import {
  createCipheriv,
  createDecipheriv,
  createHmac,
  randomBytes,
} from 'node:crypto';

import { Injectable } from '@nestjs/common';

export class EsimAssetCryptoError
  extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'EsimAssetCryptoError';
  }
}

export interface EsimInstallationData {
  iccid: string;
  qrCode: string | null;
  shortLink: string | null;
  phoneNumber: string | null;
}

export interface EncryptedEsimPayload {
  schemaVersion:
    'ysim.esim-installation/v1';
  algorithm: 'AES-256-GCM';
  keyId: string;
  iv: string;
  ciphertext: string;
  authTag: string;
}

export interface EsimAssetKeyConfig {
  keyId: string;
  encryptionKey: Buffer;
  fingerprintKey: Buffer;
}

type Environment =
  Record<string, string | undefined>;

const KEY_ID_PATTERN =
  /^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$/u;
const BASE64_PATTERN =
  /^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/u;

const decodeKey = (
  value: string | undefined,
  field: string,
): Buffer => {
  if (
    typeof value !== 'string' ||
    !BASE64_PATTERN.test(value)
  ) {
    throw new EsimAssetCryptoError(
      `${field} must be canonical base64`,
    );
  }

  const decoded =
    Buffer.from(value, 'base64');
  if (
    decoded.length !== 32 ||
    decoded.toString('base64') !==
      value
  ) {
    throw new EsimAssetCryptoError(
      `${field} must decode to 32 bytes`,
    );
  }
  return decoded;
};

export const loadEsimAssetKeyConfig = (
  environment: Environment =
    process.env,
): EsimAssetKeyConfig => {
  const keyId =
    environment
      .YSIM_ESIM_ASSET_KEY_ID;

  if (
    typeof keyId !== 'string' ||
    !KEY_ID_PATTERN.test(keyId)
  ) {
    throw new EsimAssetCryptoError(
      'YSIM_ESIM_ASSET_KEY_ID is invalid',
    );
  }

  return {
    keyId,
    encryptionKey: decodeKey(
      environment
        .YSIM_ESIM_ASSET_ENCRYPTION_KEY_B64,
      'YSIM_ESIM_ASSET_ENCRYPTION_KEY_B64',
    ),
    fingerprintKey: decodeKey(
      environment
        .YSIM_ESIM_ASSET_FINGERPRINT_KEY_B64,
      'YSIM_ESIM_ASSET_FINGERPRINT_KEY_B64',
    ),
  };
};

const canonicalInstallationJson = (
  data: EsimInstallationData,
): string =>
  JSON.stringify({
    iccid: data.iccid,
    phoneNumber:
      data.phoneNumber,
    qrCode: data.qrCode,
    shortLink:
      data.shortLink,
  });

const validateEnvelope = (
  envelope: EncryptedEsimPayload,
): void => {
  if (
    envelope.schemaVersion !==
      'ysim.esim-installation/v1' ||
    envelope.algorithm !==
      'AES-256-GCM' ||
    !KEY_ID_PATTERN.test(
      envelope.keyId,
    )
  ) {
    throw new EsimAssetCryptoError(
      'Encrypted eSIM envelope is invalid',
    );
  }

  for (const [
    field,
    value,
    expectedLength,
  ] of [
    ['iv', envelope.iv, 12],
    [
      'authTag',
      envelope.authTag,
      16,
    ],
  ] as const) {
    if (
      !BASE64_PATTERN.test(value) ||
      Buffer.from(
        value,
        'base64',
      ).length !==
        expectedLength
    ) {
      throw new EsimAssetCryptoError(
        `${field} is invalid`,
      );
    }
  }

  if (
    !BASE64_PATTERN.test(
      envelope.ciphertext,
    ) ||
    Buffer.from(
      envelope.ciphertext,
      'base64',
    ).length < 1
  ) {
    throw new EsimAssetCryptoError(
      'ciphertext is invalid',
    );
  }
};

@Injectable()
export class EsimAssetCrypto {
  private readonly configProvider:
    () => EsimAssetKeyConfig;

  constructor(
    config:
      | EsimAssetKeyConfig
      | (() => EsimAssetKeyConfig) =
        loadEsimAssetKeyConfig,
    private readonly randomSource:
      (size: number) => Buffer =
        randomBytes,
  ) {
    this.configProvider =
      typeof config === 'function'
        ? config
        : () => config;
  }

  fingerprintIccid(
    iccid: string,
  ): string {
    const config =
      this.configProvider();

    return createHmac(
      'sha256',
      config.fingerprintKey,
    )
      .update(
        'ysim:esim-asset:iccid:v1:',
        'utf8',
      )
      .update(iccid, 'utf8')
      .digest('hex');
  }

  encrypt(
    data: EsimInstallationData,
    aad: string,
  ): EncryptedEsimPayload {
    const config =
      this.configProvider();
    const iv =
      this.randomSource(12);

    if (
      !Buffer.isBuffer(iv) ||
      iv.length !== 12
    ) {
      throw new EsimAssetCryptoError(
        'AES-GCM IV source is invalid',
      );
    }

    const cipher =
      createCipheriv(
        'aes-256-gcm',
        config.encryptionKey,
        iv,
      );
    cipher.setAAD(
      Buffer.from(aad, 'utf8'),
    );

    const ciphertext =
      Buffer.concat([
        cipher.update(
          canonicalInstallationJson(
            data,
          ),
          'utf8',
        ),
        cipher.final(),
      ]);
    const authTag =
      cipher.getAuthTag();

    return {
      schemaVersion:
        'ysim.esim-installation/v1',
      algorithm: 'AES-256-GCM',
      keyId: config.keyId,
      iv: iv.toString('base64'),
      ciphertext:
        ciphertext.toString(
          'base64',
        ),
      authTag:
        authTag.toString('base64'),
    };
  }

  decrypt(
    envelope: EncryptedEsimPayload,
    aad: string,
  ): EsimInstallationData {
    validateEnvelope(envelope);

    const config =
      this.configProvider();
    if (
      envelope.keyId !==
      config.keyId
    ) {
      throw new EsimAssetCryptoError(
        'Encrypted eSIM key ID is unavailable',
      );
    }

    try {
      const decipher =
        createDecipheriv(
          'aes-256-gcm',
          config.encryptionKey,
          Buffer.from(
            envelope.iv,
            'base64',
          ),
        );
      decipher.setAAD(
        Buffer.from(aad, 'utf8'),
      );
      decipher.setAuthTag(
        Buffer.from(
          envelope.authTag,
          'base64',
        ),
      );

      const plaintext =
        Buffer.concat([
          decipher.update(
            Buffer.from(
              envelope.ciphertext,
              'base64',
            ),
          ),
          decipher.final(),
        ]).toString('utf8');

      const value =
        JSON.parse(plaintext) as
          Partial<
            EsimInstallationData
          >;

      if (
        typeof value.iccid !==
          'string' ||
        !(
          value.qrCode === null ||
          typeof value.qrCode ===
            'string'
        ) ||
        !(
          value.shortLink === null ||
          typeof value.shortLink ===
            'string'
        ) ||
        !(
          value.phoneNumber === null ||
          typeof value.phoneNumber ===
            'string'
        )
      ) {
        throw new Error(
          'Invalid decrypted shape',
        );
      }

      return {
        iccid: value.iccid,
        qrCode: value.qrCode,
        shortLink:
          value.shortLink,
        phoneNumber:
          value.phoneNumber,
      };
    } catch {
      throw new EsimAssetCryptoError(
        'Encrypted eSIM payload authentication failed',
      );
    }
  }
}
