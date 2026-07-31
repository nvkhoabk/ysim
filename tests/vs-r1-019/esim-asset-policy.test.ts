import {
  describe,
  expect,
  it,
  vi,
} from 'vitest';

import {
  EsimAssetIngestionService,
} from '../../apps/api/src/modules/fulfillment/application/esim-asset-ingestion.service.js';
import {
  buildEsimAssetAad,
  EsimAssetPolicyError,
  normalizeEsimAssetBatch,
  type DeliverableEsimBatchInput,
} from '../../apps/api/src/modules/fulfillment/domain/esim-asset-policy.js';

const batch:
  DeliverableEsimBatchInput = {
    procurementRequestId:
      '10000000-0000-4000-8000-000000000019',
    supplierSubmissionId:
      '20000000-0000-4000-8000-000000000019',
    supplierCode: 'GIGAGO',
    supplierEnvironment:
      'SANDBOX',
    expectedCount: 2,
    capturedAt:
      '2026-07-31T15:00:00.000Z',
    esims: [
      {
        detailId: 1820422,
        supplierOrderId:
          'G000493.1',
        providerRequestId:
          'ysim-sbx-' +
          'a'.repeat(32),
        status: 'DELIVERED',
        iccid:
          '8988211000000000001',
        phoneNumber: null,
        planId:
          'GIGAGO_JP_FIXED_5GB_7D',
        data: '5GB',
        validity: '7 days',
        qrCode:
          'LPA:1$rspeu.demo.net$CODE01',
        shortLink: 'asset_01',
      },
      {
        detailId: 1820423,
        supplierOrderId:
          'G000493.1',
        providerRequestId:
          'ysim-sbx-' +
          'a'.repeat(32),
        status: 'DELIVERED',
        iccid:
          '8988211000000000002',
        phoneNumber: null,
        planId:
          'GIGAGO_JP_FIXED_5GB_7D',
        data: '5GB',
        validity: '7 days',
        qrCode: null,
        shortLink: 'asset_02',
      },
    ],
  };

describe('eSIM Asset policy', () => {
  it('normalizes a deliverable batch', () => {
    const result =
      normalizeEsimAssetBatch(
        batch,
      );

    expect(result).toMatchObject({
      expectedCount: 2,
      supplierCode: 'GIGAGO',
      supplierEnvironment:
        'SANDBOX',
    });
    expect(result.assets)
      .toHaveLength(2);
  });

  it('requires the exact expected count', () => {
    expect(() =>
      normalizeEsimAssetBatch({
        ...batch,
        expectedCount: 1,
      }),
    ).toThrow(
      'Deliverable eSIM count mismatch',
    );
  });

  it('rejects duplicate supplier detail IDs', () => {
    expect(() =>
      normalizeEsimAssetBatch({
        ...batch,
        esims: [
          batch.esims[0],
          {
            ...batch.esims[1],
            detailId:
              batch.esims[0]
                .detailId,
          },
        ],
      }),
    ).toThrow(
      'Supplier detail ID is duplicated',
    );
  });

  it('rejects duplicate ICCIDs', () => {
    expect(() =>
      normalizeEsimAssetBatch({
        ...batch,
        esims: [
          batch.esims[0],
          {
            ...batch.esims[1],
            iccid:
              batch.esims[0]
                .iccid,
          },
        ],
      }),
    ).toThrow(
      'ICCID is duplicated',
    );
  });

  it('rejects a non-delivered eSIM', () => {
    expect(() =>
      normalizeEsimAssetBatch({
        ...batch,
        esims: [
          {
            ...batch.esims[0],
            status:
              'PROCESSING',
          } as never,
          batch.esims[1],
        ],
      }),
    ).toThrow(
      'Only Delivered eSIMs',
    );
  });

  it('rejects missing installation data', () => {
    expect(() =>
      normalizeEsimAssetBatch({
        ...batch,
        esims: [
          {
            ...batch.esims[0],
            qrCode: null,
            shortLink: null,
          },
          batch.esims[1],
        ],
      }),
    ).toThrow(
      'Installation data is missing',
    );
  });

  it('rejects an invalid ICCID', () => {
    expect(() =>
      normalizeEsimAssetBatch({
        ...batch,
        esims: [
          {
            ...batch.esims[0],
            iccid: '123',
          },
          batch.esims[1],
        ],
      }),
    ).toThrow(
      EsimAssetPolicyError,
    );
  });

  it('rejects invalid or inconsistent provider request IDs', () => {
    expect(() =>
      normalizeEsimAssetBatch({
        ...batch,
        esims: [
          {
            ...batch.esims[0],
            providerRequestId:
              'invalid',
          },
          batch.esims[1],
        ],
      }),
    ).toThrow(
      'providerRequestId is invalid',
    );

    expect(() =>
      normalizeEsimAssetBatch({
        ...batch,
        esims: [
          batch.esims[0],
          {
            ...batch.esims[1],
            providerRequestId:
              'ysim-sbx-' +
              'b'.repeat(32),
          },
        ],
      }),
    ).toThrow(
      'Provider request ID is inconsistent',
    );
  });

  it('builds stable AAD without sensitive values', () => {
    const asset =
      normalizeEsimAssetBatch(
        batch,
      ).assets[0];
    const aad =
      buildEsimAssetAad(asset);

    expect(aad).toContain(
      'ysim.esim-asset/v1',
    );
    expect(aad).toContain(
      String(asset.detailId),
    );
    expect(aad).not.toContain(
      asset.iccid,
    );
    expect(aad).not.toContain(
      asset.qrCode,
    );
  });

  it('ingests only encrypted prepared records', async () => {
    const persistBatch =
      vi.fn().mockResolvedValue({
        kind: 'CREATED',
        assetIds: [
          '30000000-0000-4000-8000-000000000019',
          '40000000-0000-4000-8000-000000000019',
        ],
        assetCount: 2,
      });
    const encrypt =
      vi.fn().mockReturnValue({
        schemaVersion:
          'ysim.esim-installation/v1',
        algorithm:
          'AES-256-GCM',
        keyId: 'test-v1',
        iv: 'AAAAAAAAAAAAAAAA',
        ciphertext: 'AQ==',
        authTag:
          'AAAAAAAAAAAAAAAAAAAAAA==',
      });
    const service =
      new EsimAssetIngestionService(
        {
          persistBatch,
        } as never,
        {
          fingerprintIccid:
            vi.fn().mockReturnValue(
              'f'.repeat(64),
            ),
          encrypt,
        } as never,
      );

    const result =
      await service.ingest(batch);
    const prepared =
      persistBatch.mock
        .calls[0][0];

    expect(result).toMatchObject({
      kind: 'CREATED',
      assetCount: 2,
    });
    expect(prepared)
      .toHaveLength(2);
    expect(prepared[0])
      .not.toHaveProperty('iccid');
    expect(prepared[0])
      .not.toHaveProperty('qrCode');
    expect(
      JSON.stringify(
        prepared,
      ),
    ).not.toContain(
      batch.esims[0].iccid,
    );
    expect(encrypt)
      .toHaveBeenCalledTimes(2);
  });
});
