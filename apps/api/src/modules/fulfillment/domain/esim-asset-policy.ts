export class EsimAssetPolicyError
  extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'EsimAssetPolicyError';
  }
}

export interface DeliverableEsimInput {
  detailId: number;
  supplierOrderId: string;
  providerRequestId: string;
  status: 'DELIVERED';
  iccid: string;
  phoneNumber: string | null;
  planId: string;
  data: string;
  validity: string;
  qrCode: string | null;
  shortLink: string | null;
}

export interface DeliverableEsimBatchInput {
  procurementRequestId: string;
  supplierSubmissionId: string;
  supplierCode: 'GIGAGO';
  supplierEnvironment: 'SANDBOX';
  expectedCount: number;
  capturedAt: string;
  esims: DeliverableEsimInput[];
}

export interface NormalizedEsimAsset {
  procurementRequestId: string;
  supplierSubmissionId: string;
  supplierCode: 'GIGAGO';
  supplierEnvironment: 'SANDBOX';
  detailId: number;
  supplierOrderId: string;
  providerRequestId: string;
  iccid: string;
  phoneNumber: string | null;
  planId: string;
  data: string;
  validity: string;
  qrCode: string | null;
  shortLink: string | null;
  capturedAt: string;
}

export interface NormalizedEsimAssetBatch {
  procurementRequestId: string;
  supplierSubmissionId: string;
  supplierCode: 'GIGAGO';
  supplierEnvironment: 'SANDBOX';
  expectedCount: number;
  capturedAt: string;
  assets: NormalizedEsimAsset[];
}

const UUID_PATTERN =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;
const REQUEST_ID_PATTERN =
  /^ysim-sbx-[0-9a-f]{32}$/u;
const ORDER_ID_PATTERN =
  /^G[0-9]{5,12}\.[0-9]+$/u;
const ICCID_PATTERN =
  /^[0-9]{18,22}$/u;
const PLAN_PATTERN =
  /^[A-Z0-9][A-Z0-9_-]{2,127}$/u;
const SHORT_LINK_PATTERN =
  /^[A-Za-z0-9_-]{1,200}$/u;

const normalizeUuid = (
  value: string,
  field: string,
): string => {
  if (!UUID_PATTERN.test(value)) {
    throw new EsimAssetPolicyError(
      `${field} must be a UUID`,
    );
  }
  return value.toLowerCase();
};

const normalizeString = (
  value: string,
  field: string,
  maximum: number,
): string => {
  if (
    typeof value !== 'string' ||
    !value.trim() ||
    value.length > maximum
  ) {
    throw new EsimAssetPolicyError(
      `${field} is invalid`,
    );
  }
  return value.trim();
};

const normalizeLabel = (
  value: string,
  field: string,
  maximum: number,
): string => {
  if (
    typeof value !== 'string' ||
    value.length > maximum
  ) {
    throw new EsimAssetPolicyError(
      `${field} is invalid`,
    );
  }
  return value.trim();
};

const normalizeOptional = (
  value: string | null,
  field: string,
  maximum: number,
): string | null => {
  if (
    value === null ||
    value === ''
  ) {
    return null;
  }
  if (
    typeof value !== 'string' ||
    value.length > maximum
  ) {
    throw new EsimAssetPolicyError(
      `${field} is invalid`,
    );
  }
  return value.trim() || null;
};

const normalizeTimestamp = (
  value: string,
): string => {
  const parsed = Date.parse(value);
  if (!Number.isFinite(parsed)) {
    throw new EsimAssetPolicyError(
      'capturedAt must be an ISO timestamp',
    );
  }
  return new Date(parsed).toISOString();
};

export const normalizeEsimAssetBatch = (
  input: DeliverableEsimBatchInput,
): NormalizedEsimAssetBatch => {
  const procurementRequestId =
    normalizeUuid(
      input.procurementRequestId,
      'procurementRequestId',
    );
  const supplierSubmissionId =
    normalizeUuid(
      input.supplierSubmissionId,
      'supplierSubmissionId',
    );

  if (
    input.supplierCode !== 'GIGAGO' ||
    input.supplierEnvironment !==
      'SANDBOX'
  ) {
    throw new EsimAssetPolicyError(
      'Only Gigago sandbox assets are supported',
    );
  }
  if (
    !Number.isInteger(
      input.expectedCount,
    ) ||
    input.expectedCount < 1 ||
    input.expectedCount > 20
  ) {
    throw new EsimAssetPolicyError(
      'expectedCount must be 1..20',
    );
  }
  if (
    !Array.isArray(input.esims) ||
    input.esims.length !==
      input.expectedCount
  ) {
    throw new EsimAssetPolicyError(
      'Deliverable eSIM count mismatch',
    );
  }

  const capturedAt =
    normalizeTimestamp(
      input.capturedAt,
    );
  const detailIds =
    new Set<number>();
  const iccids =
    new Set<string>();
  const providerRequestIds =
    new Set<string>();
  const planIds =
    new Set<string>();

  const assets = input.esims.map(
    (item, index) => {
      if (
        !Number.isSafeInteger(
          item.detailId,
        ) ||
        item.detailId < 1
      ) {
        throw new EsimAssetPolicyError(
          `esims[${index}].detailId is invalid`,
        );
      }
      if (
        detailIds.has(
          item.detailId,
        )
      ) {
        throw new EsimAssetPolicyError(
          'Supplier detail ID is duplicated',
        );
      }
      detailIds.add(
        item.detailId,
      );

      if (
        item.status !==
        'DELIVERED'
      ) {
        throw new EsimAssetPolicyError(
          'Only Delivered eSIMs may become assets',
        );
      }

      const supplierOrderId =
        normalizeString(
          item.supplierOrderId,
          'supplierOrderId',
          80,
        );
      if (
        !ORDER_ID_PATTERN.test(
          supplierOrderId,
        )
      ) {
        throw new EsimAssetPolicyError(
          'supplierOrderId is invalid',
        );
      }

      const providerRequestId =
        normalizeString(
          item.providerRequestId,
          'providerRequestId',
          80,
        );
      if (
        !REQUEST_ID_PATTERN.test(
          providerRequestId,
        )
      ) {
        throw new EsimAssetPolicyError(
          'providerRequestId is invalid',
        );
      }
      providerRequestIds.add(
        providerRequestId,
      );

      const iccid =
        normalizeString(
          item.iccid,
          'iccid',
          32,
        );
      if (!ICCID_PATTERN.test(iccid)) {
        throw new EsimAssetPolicyError(
          'ICCID is invalid',
        );
      }
      if (iccids.has(iccid)) {
        throw new EsimAssetPolicyError(
          'ICCID is duplicated',
        );
      }
      iccids.add(iccid);

      const planId =
        normalizeString(
          item.planId,
          'planId',
          128,
        );
      if (!PLAN_PATTERN.test(planId)) {
        throw new EsimAssetPolicyError(
          'planId is invalid',
        );
      }
      planIds.add(planId);

      const qrCode =
        normalizeOptional(
          item.qrCode,
          'qrCode',
          1_000,
        );
      const shortLink =
        normalizeOptional(
          item.shortLink,
          'shortLink',
          200,
        );
      if (
        shortLink !== null &&
        !SHORT_LINK_PATTERN.test(
          shortLink,
        )
      ) {
        throw new EsimAssetPolicyError(
          'shortLink is invalid',
        );
      }
      if (
        qrCode === null &&
        shortLink === null
      ) {
        throw new EsimAssetPolicyError(
          'Installation data is missing',
        );
      }

      return {
        procurementRequestId,
        supplierSubmissionId,
        supplierCode:
          'GIGAGO' as const,
        supplierEnvironment:
          'SANDBOX' as const,
        detailId: item.detailId,
        supplierOrderId,
        providerRequestId,
        iccid,
        phoneNumber:
          normalizeOptional(
            item.phoneNumber,
            'phoneNumber',
            80,
          ),
        planId,
        data:
          normalizeLabel(
            item.data,
            'data',
            100,
          ),
        validity:
          normalizeLabel(
            item.validity,
            'validity',
            100,
          ),
        qrCode,
        shortLink,
        capturedAt,
      };
    },
  );

  if (
    providerRequestIds.size !== 1
  ) {
    throw new EsimAssetPolicyError(
      'Provider request ID is inconsistent',
    );
  }
  if (planIds.size !== 1) {
    throw new EsimAssetPolicyError(
      'Plan ID is inconsistent',
    );
  }

  return {
    procurementRequestId,
    supplierSubmissionId,
    supplierCode: 'GIGAGO',
    supplierEnvironment:
      'SANDBOX',
    expectedCount:
      input.expectedCount,
    capturedAt,
    assets,
  };
};

export const buildEsimAssetAad = (
  asset: Pick<
    NormalizedEsimAsset,
    | 'procurementRequestId'
    | 'supplierSubmissionId'
    | 'supplierCode'
    | 'supplierEnvironment'
    | 'detailId'
    | 'supplierOrderId'
    | 'providerRequestId'
    | 'planId'
  >,
): string =>
  [
    'ysim.esim-asset/v1',
    asset.procurementRequestId,
    asset.supplierSubmissionId,
    asset.supplierCode,
    asset.supplierEnvironment,
    String(asset.detailId),
    asset.supplierOrderId,
    asset.providerRequestId,
    asset.planId,
  ].join('|');
