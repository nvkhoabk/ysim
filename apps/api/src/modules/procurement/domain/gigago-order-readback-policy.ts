import type {
  GigagoAgencyOrderRaw,
  GigagoOrderDetailRaw,
} from '../infrastructure/gigago/gigago.types.js';

export class GigagoOrderReadbackPolicyError
  extends Error {
  constructor(message: string) {
    super(message);
    this.name =
      'GigagoOrderReadbackPolicyError';
  }
}

export type GigagoAgencyOrderStatus =
  | 'PENDING'
  | 'COMPLETED'
  | 'CANCELLED'
  | 'PROCESSING';

export type GigagoDetailStatus =
  | 'PROCESSING'
  | 'DELIVERED'
  | 'RECALLED';

export interface GigagoAgencyOrder {
  id: string;
  requestId: string;
  totalEsims: number;
  completedEsims: number;
  status: GigagoAgencyOrderStatus;
  statusCode: 0 | 1 | 2 | 10;
  currency: string;
}

export interface GigagoDeliveredEsim {
  detailId: number;
  orderId: string;
  requestId: string;
  status: GigagoDetailStatus;
  statusCode: 0 | 1 | 2;
  iccid: string | null;
  phoneNumber: string | null;
  planId: string;
  data: string;
  validity: string;
  qrCode: string | null;
  shortLink: string | null;
}

export type GigagoDeliveryReadiness =
  | {
      kind: 'PROCESSING';
      reason:
        | 'ORDER_PROCESSING'
        | 'DETAIL_PROCESSING'
        | 'NO_ORDER_DATA';
      expectedCount: number;
      completedCount: number;
      returnedCount: number;
      deliveredCount: number;
      installableCount: number;
      esims: GigagoDeliveredEsim[];
    }
  | {
      kind: 'DELIVERABLE';
      expectedCount: number;
      completedCount: number;
      returnedCount: number;
      deliveredCount: number;
      installableCount: number;
      esims: GigagoDeliveredEsim[];
    }
  | {
      kind: 'ACTION_REQUIRED';
      reason:
        | 'ORDER_PENDING_ERROR'
        | 'ORDER_CANCELLED'
        | 'DETAIL_RECALLED'
        | 'COMPLETED_COUNT_MISMATCH'
        | 'DELIVERED_COUNT_MISMATCH'
        | 'INSTALL_DATA_MISSING';
      expectedCount: number;
      completedCount: number;
      returnedCount: number;
      deliveredCount: number;
      installableCount: number;
      esims: GigagoDeliveredEsim[];
    };

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

const record = (
  value: unknown,
  field: string,
): Record<string, unknown> => {
  if (
    typeof value !== 'object' ||
    value === null ||
    Array.isArray(value)
  ) {
    throw new GigagoOrderReadbackPolicyError(
      `${field} must be an object`,
    );
  }
  return value as Record<
    string,
    unknown
  >;
};

const string = (
  value: unknown,
  field: string,
  maximum = 300,
): string => {
  if (
    typeof value !== 'string' ||
    !value.trim() ||
    value.length > maximum
  ) {
    throw new GigagoOrderReadbackPolicyError(
      `${field} is invalid`,
    );
  }
  return value.trim();
};

const nullableString = (
  value: unknown,
  maximum = 500,
): string | null => {
  if (
    value === null ||
    value === undefined ||
    value === ''
  ) {
    return null;
  }
  if (
    typeof value !== 'string' ||
    value.length > maximum
  ) {
    throw new GigagoOrderReadbackPolicyError(
      'Optional string is invalid',
    );
  }
  return value.trim() || null;
};

const integer = (
  value: unknown,
  field: string,
  minimum = 0,
  maximum = 1_000_000,
): number => {
  const parsed = Number(value);
  if (
    !Number.isInteger(parsed) ||
    parsed < minimum ||
    parsed > maximum
  ) {
    throw new GigagoOrderReadbackPolicyError(
      `${field} is invalid`,
    );
  }
  return parsed;
};

const orderStatus = (
  value: unknown,
): {
  status: GigagoAgencyOrderStatus;
  statusCode: 0 | 1 | 2 | 10;
} => {
  const code = integer(
    value,
    'order_status',
    0,
    10,
  );
  const mapping = {
    0: 'PENDING',
    1: 'COMPLETED',
    2: 'CANCELLED',
    10: 'PROCESSING',
  } as const;
  if (!(code in mapping)) {
    throw new GigagoOrderReadbackPolicyError(
      'Gigago agency order status is unsupported',
    );
  }
  return {
    status:
      mapping[
        code as keyof typeof mapping
      ],
    statusCode:
      code as 0 | 1 | 2 | 10,
  };
};

const detailStatus = (
  value: unknown,
): {
  status: GigagoDetailStatus;
  statusCode: 0 | 1 | 2;
} => {
  const code = integer(
    value,
    'detail.status',
    0,
    2,
  );
  const mapping = {
    0: 'PROCESSING',
    1: 'DELIVERED',
    2: 'RECALLED',
  } as const;
  return {
    status:
      mapping[
        code as keyof typeof mapping
      ],
    statusCode:
      code as 0 | 1 | 2,
  };
};

export const normalizeGigagoAgencyOrders = (
  value: unknown,
  expectedRequestId: string,
): GigagoAgencyOrder[] => {
  if (
    !REQUEST_ID_PATTERN.test(
      expectedRequestId,
    )
  ) {
    throw new GigagoOrderReadbackPolicyError(
      'Expected request ID is invalid',
    );
  }
  if (!Array.isArray(value)) {
    throw new GigagoOrderReadbackPolicyError(
      'Gigago agency-order result must be an array',
    );
  }
  if (value.length > 100) {
    throw new GigagoOrderReadbackPolicyError(
      'Gigago agency-order result is too large',
    );
  }

  return value.map(
    (item, index) => {
      const row = record(
        item,
        `agencyOrders[${index}]`,
      );
      const id = string(
        row.id,
        `agencyOrders[${index}].id`,
        80,
      );
      if (!ORDER_ID_PATTERN.test(id)) {
        throw new GigagoOrderReadbackPolicyError(
          'Gigago agency order ID is invalid',
        );
      }
      const requestId = string(
        row.request_id,
        'request_id',
        80,
      );
      if (
        requestId !==
        expectedRequestId
      ) {
        throw new GigagoOrderReadbackPolicyError(
          'Gigago agency-order request ID mismatch',
        );
      }
      const normalized =
        orderStatus(row.order_status);

      return {
        id,
        requestId,
        totalEsims: integer(
          row.total_esims,
          'total_esims',
          1,
          20,
        ),
        completedEsims: integer(
          row.total_esim_completed,
          'total_esim_completed',
          0,
          20,
        ),
        status: normalized.status,
        statusCode:
          normalized.statusCode,
        currency: string(
          row.currency,
          'currency',
          12,
        ).toUpperCase(),
      };
    },
  );
};

export const normalizeGigagoOrderDetails = (
  value: unknown,
  expectedRequestId: string,
): GigagoDeliveredEsim[] => {
  if (
    !REQUEST_ID_PATTERN.test(
      expectedRequestId,
    )
  ) {
    throw new GigagoOrderReadbackPolicyError(
      'Expected request ID is invalid',
    );
  }
  if (!Array.isArray(value)) {
    throw new GigagoOrderReadbackPolicyError(
      'Gigago detail result must be an array',
    );
  }
  if (value.length > 100) {
    throw new GigagoOrderReadbackPolicyError(
      'Gigago detail result is too large',
    );
  }

  const seenIccids = new Set<string>();

  return value.map(
    (item, index) => {
      const row = record(
        item,
        `details[${index}]`,
      );
      const requestId = string(
        row.request_id,
        'detail.request_id',
        80,
      );
      if (
        requestId !==
        expectedRequestId
      ) {
        throw new GigagoOrderReadbackPolicyError(
          'Gigago detail request ID mismatch',
        );
      }
      const orderId = string(
        row.order_id,
        'detail.order_id',
        80,
      );
      if (
        !ORDER_ID_PATTERN.test(
          orderId,
        )
      ) {
        throw new GigagoOrderReadbackPolicyError(
          'Gigago detail order ID is invalid',
        );
      }
      const normalized =
        detailStatus(row.status);
      const iccid =
        nullableString(
          row.iccid,
          32,
        );
      if (
        iccid !== null &&
        !ICCID_PATTERN.test(iccid)
      ) {
        throw new GigagoOrderReadbackPolicyError(
          'Gigago ICCID is invalid',
        );
      }
      if (
        iccid !== null &&
        seenIccids.has(iccid)
      ) {
        throw new GigagoOrderReadbackPolicyError(
          'Gigago ICCID is duplicated',
        );
      }
      if (iccid !== null) {
        seenIccids.add(iccid);
      }

      const planId = string(
        row.ggg_plan_id,
        'detail.ggg_plan_id',
        128,
      );
      if (!PLAN_PATTERN.test(planId)) {
        throw new GigagoOrderReadbackPolicyError(
          'Gigago detail plan ID is invalid',
        );
      }

      const qrCode =
        nullableString(
          row.qr_code,
          1_000,
        );
      const shortLink =
        nullableString(
          row.short_link,
          200,
        );
      if (
        shortLink !== null &&
        !SHORT_LINK_PATTERN.test(
          shortLink,
        )
      ) {
        throw new GigagoOrderReadbackPolicyError(
          'Gigago short link is invalid',
        );
      }

      return {
        detailId: integer(
          row.id,
          'detail.id',
          1,
          Number.MAX_SAFE_INTEGER,
        ),
        orderId,
        requestId,
        status: normalized.status,
        statusCode:
          normalized.statusCode,
        iccid,
        phoneNumber:
          nullableString(
            row.phone_number,
            80,
          ),
        planId,
        data:
          nullableString(
            row.data,
            100,
          ) ?? '',
        validity:
          nullableString(
            row.validity,
            100,
          ) ?? '',
        qrCode,
        shortLink,
      };
    },
  );
};

export const assessGigagoDeliveryReadiness = (
  orders: GigagoAgencyOrder[],
  esims: GigagoDeliveredEsim[],
  expectedCount: number,
): GigagoDeliveryReadiness => {
  if (
    !Number.isInteger(expectedCount) ||
    expectedCount < 1 ||
    expectedCount > 20
  ) {
    throw new GigagoOrderReadbackPolicyError(
      'Expected eSIM count is invalid',
    );
  }

  const completedCount =
    orders.reduce(
      (total, order) =>
        total +
        order.completedEsims,
      0,
    );
  const returnedCount =
    esims.length;
  const deliveredCount =
    esims.filter(
      (item) =>
        item.status === 'DELIVERED',
    ).length;
  const installableCount =
    esims.filter(
      (item) =>
        item.status ===
          'DELIVERED' &&
        item.iccid !== null &&
        (
          item.qrCode !== null ||
          item.shortLink !== null
        ),
    ).length;

  const result = {
    expectedCount,
    completedCount,
    returnedCount,
    deliveredCount,
    installableCount,
    esims,
  };

  if (orders.length === 0) {
    return {
      kind: 'PROCESSING',
      reason: 'NO_ORDER_DATA',
      ...result,
    };
  }
  if (
    orders.some(
      (order) =>
        order.status ===
        'PENDING',
    )
  ) {
    return {
      kind: 'ACTION_REQUIRED',
      reason: 'ORDER_PENDING_ERROR',
      ...result,
    };
  }
  if (
    orders.some(
      (order) =>
        order.status ===
        'CANCELLED',
    )
  ) {
    return {
      kind: 'ACTION_REQUIRED',
      reason: 'ORDER_CANCELLED',
      ...result,
    };
  }
  if (
    esims.some(
      (item) =>
        item.status === 'RECALLED',
    )
  ) {
    return {
      kind: 'ACTION_REQUIRED',
      reason: 'DETAIL_RECALLED',
      ...result,
    };
  }
  if (
    orders.some(
      (order) =>
        order.status ===
        'PROCESSING',
    )
  ) {
    return {
      kind: 'PROCESSING',
      reason: 'ORDER_PROCESSING',
      ...result,
    };
  }
  if (
    esims.some(
      (item) =>
        item.status ===
        'PROCESSING',
    )
  ) {
    return {
      kind: 'PROCESSING',
      reason: 'DETAIL_PROCESSING',
      ...result,
    };
  }
  if (
    completedCount !==
    expectedCount
  ) {
    return {
      kind: 'ACTION_REQUIRED',
      reason:
        'COMPLETED_COUNT_MISMATCH',
      ...result,
    };
  }
  if (
    returnedCount !==
      expectedCount ||
    deliveredCount !==
      expectedCount
  ) {
    return {
      kind: 'ACTION_REQUIRED',
      reason:
        'DELIVERED_COUNT_MISMATCH',
      ...result,
    };
  }
  if (
    installableCount !==
    expectedCount
  ) {
    return {
      kind: 'ACTION_REQUIRED',
      reason:
        'INSTALL_DATA_MISSING',
      ...result,
    };
  }

  return {
    kind: 'DELIVERABLE',
    ...result,
  };
};
