import { createHash } from 'node:crypto';

import type {
  GigagoOperatorInput,
  GigagoPlanPayload,
  SupplierEnvironment,
  SupplierOperatorNetworkContract,
  SupplierPlanContract,
} from '@ysim/contracts';

export class GigagoPlanNormalizationError extends Error {}

export interface NormalizedGigagoPlan {
  environment: SupplierEnvironment;
  externalPlanId: string;
  name: string;
  parentGroupId: string | null;
  parentGroupName: string | null;
  apn: string | null;
  networkType: string | null;
  countryCodes: string[];
  operatorNetworks: SupplierOperatorNetworkContract[];
  dataPolicy: 'FIXED' | 'DAILY' | 'UNLIMITED';
  dataAmountMb: number | null;
  dailyDataAmountMb: number | null;
  fairUseDataAmountMb: number | null;
  durationDays: number;
  hotspotSupported: boolean;
  phoneNumberIncluded: boolean;
  topupSupported: boolean;
  rawSnapshot: GigagoPlanPayload;
  rawSnapshotHash: string;
  observedAt: string;
}

const planIdPattern = /^[A-Z0-9][A-Z0-9_-]{2,127}$/u;
const countryCodePattern = /^[A-Z]{2}$/u;

function requireString(
  value: unknown,
  field: string,
  maximumLength = 500,
): string {
  if (typeof value !== 'string') {
    throw new GigagoPlanNormalizationError(`${field} must be a string`);
  }

  const normalized = value.trim();
  if (!normalized || normalized.length > maximumLength) {
    throw new GigagoPlanNormalizationError(
      `${field} must contain 1 to ${maximumLength} characters`,
    );
  }

  return normalized;
}

function optionalString(
  value: unknown,
  field: string,
  maximumLength = 500,
): string | null {
  if (value === undefined || value === null || value === '') {
    return null;
  }

  return requireString(value, field, maximumLength);
}

function normalizePlanId(value: unknown): string {
  const normalized = requireString(value, 'ggg_plan_id', 128).toUpperCase();
  if (!planIdPattern.test(normalized)) {
    throw new GigagoPlanNormalizationError(
      'ggg_plan_id contains unsupported characters',
    );
  }

  return normalized;
}

function parseYesNo(value: unknown, field: string): boolean {
  const normalized = requireString(value, field, 20).toLowerCase();

  if (['yes', 'true', '1'].includes(normalized)) return true;
  if (['no', 'false', '0'].includes(normalized)) return false;

  throw new GigagoPlanNormalizationError(
    `${field} must be Yes or No`,
  );
}

function parseJsonArray(value: unknown, field: string): unknown[] {
  const text = requireString(value, field, 20_000);

  let parsed: unknown;
  try {
    parsed = JSON.parse(text);
  } catch {
    throw new GigagoPlanNormalizationError(
      `${field} must contain a valid JSON array`,
    );
  }

  if (!Array.isArray(parsed)) {
    throw new GigagoPlanNormalizationError(
      `${field} must contain a JSON array`,
    );
  }

  return parsed;
}

function normalizeCountries(value: unknown): string[] {
  const countries = parseJsonArray(value, 'countries');
  const normalized = countries.map((country, index) => {
    if (typeof country !== 'string') {
      throw new GigagoPlanNormalizationError(
        `countries[${index}] must be a string`,
      );
    }

    const code = country.trim().toUpperCase();
    if (!countryCodePattern.test(code)) {
      throw new GigagoPlanNormalizationError(
        `countries[${index}] must be an ISO Alpha-2 code`,
      );
    }

    return code;
  });

  const unique = [...new Set(normalized)].sort();
  if (unique.length === 0) {
    throw new GigagoPlanNormalizationError(
      'countries must contain at least one country',
    );
  }

  return unique;
}

function normalizeOperators(
  value: unknown,
): SupplierOperatorNetworkContract[] {
  if (value === undefined || value === null || value === '') {
    return [];
  }

  const operators = parseJsonArray(value, 'operator');
  const normalized = operators.map((item, index) => {
    if (
      typeof item !== 'object' ||
      item === null ||
      Array.isArray(item)
    ) {
      throw new GigagoPlanNormalizationError(
        `operator[${index}] must be an object`,
      );
    }

    const candidate = item as Partial<GigagoOperatorInput>;
    const countryCode = requireString(
      candidate.country_code,
      `operator[${index}].country_code`,
      2,
    ).toUpperCase();

    if (!countryCodePattern.test(countryCode)) {
      throw new GigagoPlanNormalizationError(
        `operator[${index}].country_code must be an ISO Alpha-2 code`,
      );
    }

    if (!Array.isArray(candidate.networks)) {
      throw new GigagoPlanNormalizationError(
        `operator[${index}].networks must be an array`,
      );
    }

    const networks = candidate.networks.map((network, networkIndex) =>
      requireString(
        network,
        `operator[${index}].networks[${networkIndex}]`,
        200,
      ),
    );

    return {
      countryCode,
      networks: [...new Set(networks)].sort(),
    };
  });

  return normalized.sort((left, right) =>
    left.countryCode.localeCompare(right.countryCode),
  );
}

function toMegabytes(value: number, unit: string): number {
  const multiplier = unit.toUpperCase() === 'GB' ? 1024 : 1;
  return Math.round(value * multiplier);
}

function parseData(value: unknown): Pick<
  NormalizedGigagoPlan,
  | 'dataPolicy'
  | 'dataAmountMb'
  | 'dailyDataAmountMb'
  | 'fairUseDataAmountMb'
> {
  const normalized = requireString(value, 'data', 100)
    .replaceAll(/\s+/gu, ' ')
    .trim();

  if (/^unlimited(?:\s+data)?$/iu.test(normalized)) {
    return {
      dataPolicy: 'UNLIMITED',
      dataAmountMb: null,
      dailyDataAmountMb: null,
      fairUseDataAmountMb: null,
    };
  }

  const daily = normalized.match(
    /^(\d+(?:\.\d+)?)\s*(MB|GB)\s*(?:\/|per\s+)?(?:day|daily)$/iu,
  );

  if (daily) {
    const amount = Number(daily[1]);
    if (!Number.isFinite(amount) || amount <= 0) {
      throw new GigagoPlanNormalizationError(
        'daily data amount must be greater than zero',
      );
    }

    return {
      dataPolicy: 'DAILY',
      dataAmountMb: null,
      dailyDataAmountMb: toMegabytes(amount, daily[2]),
      fairUseDataAmountMb: null,
    };
  }

  const fixed = normalized.match(
    /^(\d+(?:\.\d+)?)\s*(MB|GB)$/iu,
  );

  if (fixed) {
    const amount = Number(fixed[1]);
    if (!Number.isFinite(amount) || amount < 0) {
      throw new GigagoPlanNormalizationError(
        'fixed data amount must be zero or greater',
      );
    }

    return {
      dataPolicy: 'FIXED',
      dataAmountMb: toMegabytes(amount, fixed[2]),
      dailyDataAmountMb: null,
      fairUseDataAmountMb: null,
    };
  }

  throw new GigagoPlanNormalizationError(
    `Unsupported Gigago data format: ${normalized}`,
  );
}

function parseValidity(value: unknown): number {
  const normalized = requireString(value, 'validity', 100);
  const match = normalized.match(/^(\d+)\s*days?$/iu);

  if (!match) {
    throw new GigagoPlanNormalizationError(
      `Unsupported Gigago validity format: ${normalized}`,
    );
  }

  const days = Number(match[1]);
  if (!Number.isInteger(days) || days <= 0 || days > 3650) {
    throw new GigagoPlanNormalizationError(
      'validity days must be an integer between 1 and 3650',
    );
  }

  return days;
}

function normalizeObservedAt(value: unknown): string {
  const candidate =
    value === undefined || value === null || value === ''
      ? new Date().toISOString()
      : requireString(value, 'observedAt', 100);

  const timestamp = Date.parse(candidate);
  if (!Number.isFinite(timestamp)) {
    throw new GigagoPlanNormalizationError(
      'observedAt must be an ISO date-time',
    );
  }

  return new Date(timestamp).toISOString();
}

function stableJson(value: unknown): string {
  if (Array.isArray(value)) {
    return `[${value.map((item) => stableJson(item)).join(',')}]`;
  }

  if (typeof value === 'object' && value !== null) {
    const entries = Object.entries(value as Record<string, unknown>)
      .sort(([left], [right]) => left.localeCompare(right))
      .map(
        ([key, item]) =>
          `${JSON.stringify(key)}:${stableJson(item)}`,
      );

    return `{${entries.join(',')}}`;
  }

  return JSON.stringify(value);
}

export function normalizeGigagoPlan(
  payload: GigagoPlanPayload,
  environment: SupplierEnvironment,
  observedAt?: string,
): NormalizedGigagoPlan {
  if (environment !== 'SANDBOX' && environment !== 'PRODUCTION') {
    throw new GigagoPlanNormalizationError(
      'environment must be SANDBOX or PRODUCTION',
    );
  }

  if (typeof payload !== 'object' || payload === null) {
    throw new GigagoPlanNormalizationError(
      'payload must be an object',
    );
  }

  const data = parseData(payload.data);
  const rawSnapshot = structuredClone(payload);

  return {
    environment,
    externalPlanId: normalizePlanId(payload.ggg_plan_id),
    name: requireString(payload.name, 'name', 300),
    parentGroupId: optionalString(
      payload.parent_group_id,
      'parent_group_id',
      128,
    ),
    parentGroupName: optionalString(
      payload.parent_group_name,
      'parent_group_name',
      300,
    ),
    apn: optionalString(payload.apn, 'apn', 200),
    networkType: optionalString(
      payload.network_type,
      'network_type',
      100,
    ),
    countryCodes: normalizeCountries(payload.countries),
    operatorNetworks: normalizeOperators(payload.operator),
    ...data,
    durationDays: parseValidity(payload.validity),
    hotspotSupported: parseYesNo(payload.hotspot, 'hotspot'),
    phoneNumberIncluded: parseYesNo(
      payload.phone_number,
      'phone_number',
    ),
    topupSupported: parseYesNo(
      payload.topup_extension ?? 'No',
      'topup_extension',
    ),
    rawSnapshot,
    rawSnapshotHash: createHash('sha256')
      .update(stableJson(rawSnapshot))
      .digest('hex'),
    observedAt: normalizeObservedAt(observedAt),
  };
}

export function toSupplierPlanContract(
  plan: NormalizedGigagoPlan,
  persistence: {
    id: string;
    createdAt: string;
    updatedAt: string;
    version: number;
  },
): SupplierPlanContract {
  return {
    id: persistence.id,
    supplierCode: 'GIGAGO',
    environment: plan.environment,
    externalPlanId: plan.externalPlanId,
    name: plan.name,
    parentGroupId: plan.parentGroupId,
    parentGroupName: plan.parentGroupName,
    apn: plan.apn,
    networkType: plan.networkType,
    countryCodes: plan.countryCodes,
    operatorNetworks: plan.operatorNetworks,
    dataPolicy: plan.dataPolicy,
    dataAmountMb: plan.dataAmountMb,
    dailyDataAmountMb: plan.dailyDataAmountMb,
    fairUseDataAmountMb: plan.fairUseDataAmountMb,
    durationDays: plan.durationDays,
    hotspotSupported: plan.hotspotSupported,
    phoneNumberIncluded: plan.phoneNumberIncluded,
    topupSupported: plan.topupSupported,
    rawSnapshotHash: plan.rawSnapshotHash,
    observedAt: plan.observedAt,
    status: 'ACTIVE',
    createdAt: persistence.createdAt,
    updatedAt: persistence.updatedAt,
    version: persistence.version,
  };
}
