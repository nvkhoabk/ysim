import { createHash } from 'node:crypto';

import type {
  GigagoCreateOrderExtra,
  GigagoCreatePartnerOrderInput,
} from '../infrastructure/gigago/gigago.types.js';

export class GigagoCreateOrderPolicyError
  extends Error {
  constructor(message: string) {
    super(message);
    this.name =
      'GigagoCreateOrderPolicyError';
  }
}

export interface GigagoProcurementSnapshot {
  procurementRequestId: string;
  orderId: string;
  orderNumber: string;
  supplierCode: string;
  supplierEnvironment: string;
  externalPlanId: string;
  quantity: number;
  status: string;
}

const UUID_PATTERN =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;
const ORDER_NUMBER_PATTERN =
  /^YS-[0-9]{8}-[0-9A-F]{12}$/u;
const PLAN_PATTERN =
  /^[A-Z0-9][A-Z0-9_-]{2,127}$/u;
const REQUEST_PATTERN =
  /^ysim-sbx-[0-9a-f]{32}$/u;

const requireUuid = (
  value: string,
  field: string,
): string => {
  if (!UUID_PATTERN.test(value)) {
    throw new GigagoCreateOrderPolicyError(
      `${field} must be a UUID`,
    );
  }
  return value.toLowerCase();
};

export const buildGigagoRequestId = (
  procurementRequestId: string,
): string => {
  const normalized = requireUuid(
    procurementRequestId,
    'procurementRequestId',
  );
  return (
    'ysim-sbx-' +
    createHash('sha256')
      .update(
        `gigago:create-order:${normalized}`,
        'utf8',
      )
      .digest('hex')
      .slice(0, 32)
  );
};

export const buildGigagoCreateOrderInput = (
  snapshot: GigagoProcurementSnapshot,
  notifyUrl: string,
): GigagoCreatePartnerOrderInput => {
  requireUuid(
    snapshot.procurementRequestId,
    'procurementRequestId',
  );
  requireUuid(snapshot.orderId, 'orderId');

  if (
    snapshot.supplierCode !== 'GIGAGO' ||
    snapshot.supplierEnvironment !==
      'SANDBOX' ||
    snapshot.status !== 'PENDING_SUPPLIER'
  ) {
    throw new GigagoCreateOrderPolicyError(
      'Procurement Request is not eligible for Gigago sandbox submission',
    );
  }
  if (
    !ORDER_NUMBER_PATTERN.test(
      snapshot.orderNumber,
    )
  ) {
    throw new GigagoCreateOrderPolicyError(
      'orderNumber is invalid',
    );
  }
  if (
    !PLAN_PATTERN.test(
      snapshot.externalPlanId,
    )
  ) {
    throw new GigagoCreateOrderPolicyError(
      'externalPlanId is invalid',
    );
  }
  if (
    !Number.isInteger(snapshot.quantity) ||
    snapshot.quantity < 1 ||
    snapshot.quantity > 20
  ) {
    throw new GigagoCreateOrderPolicyError(
      'quantity must be 1..20',
    );
  }

  let parsed: URL;
  try {
    parsed = new URL(notifyUrl);
  } catch {
    throw new GigagoCreateOrderPolicyError(
      'notifyUrl is invalid',
    );
  }
  if (
    parsed.protocol !== 'https:' ||
    parsed.username ||
    parsed.password ||
    parsed.hash
  ) {
    throw new GigagoCreateOrderPolicyError(
      'notifyUrl must be an HTTPS callback URL',
    );
  }

  return {
    request_id: buildGigagoRequestId(
      snapshot.procurementRequestId,
    ),
    orders: [
      {
        ggg_plan_id:
          snapshot.externalPlanId,
        amount: snapshot.quantity,
      },
    ],
    metadata: {
      note:
        `YSim order ${snapshot.orderNumber}`,
      url_notify: parsed.toString(),
    },
  };
};

export const normalizeGigagoCreateOrderExtra = (
  value: unknown,
  expectedRequestId: string,
): GigagoCreateOrderExtra => {
  if (
    typeof value !== 'object' ||
    value === null ||
    Array.isArray(value)
  ) {
    throw new GigagoCreateOrderPolicyError(
      'Gigago create-order extra is invalid',
    );
  }
  const extra = value as Record<
    string,
    unknown
  >;

  if (
    typeof extra.request_id !== 'string' ||
    extra.request_id !==
      expectedRequestId ||
    !REQUEST_PATTERN.test(extra.request_id)
  ) {
    throw new GigagoCreateOrderPolicyError(
      'Gigago request_id mismatch',
    );
  }
  if (
    !Number.isInteger(
      extra.agency_order_id,
    ) ||
    Number(extra.agency_order_id) <= 0
  ) {
    throw new GigagoCreateOrderPolicyError(
      'Gigago agency_order_id is invalid',
    );
  }
  if (
    typeof extra.code !== 'string' ||
    !UUID_PATTERN.test(extra.code)
  ) {
    throw new GigagoCreateOrderPolicyError(
      'Gigago response code is invalid',
    );
  }
  if (
    !Number.isInteger(extra.status) ||
    Number(extra.status) < 0
  ) {
    throw new GigagoCreateOrderPolicyError(
      'Gigago status is invalid',
    );
  }
  if (
    typeof extra.order_status !==
      'string' ||
    !extra.order_status.trim()
  ) {
    throw new GigagoCreateOrderPolicyError(
      'Gigago order_status is invalid',
    );
  }
  if (
    extra.notes !== undefined &&
    typeof extra.notes !== 'string'
  ) {
    throw new GigagoCreateOrderPolicyError(
      'Gigago notes are invalid',
    );
  }

  return {
    request_id: extra.request_id,
    agency_order_id:
      Number(extra.agency_order_id),
    code: extra.code.toLowerCase(),
    notes:
      typeof extra.notes === 'string'
        ? extra.notes.slice(0, 300)
        : undefined,
    status: Number(extra.status),
    order_status:
      extra.order_status
        .trim()
        .toUpperCase(),
  };
};
