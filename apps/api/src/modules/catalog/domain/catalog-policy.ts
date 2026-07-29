import type {
  ActivationPolicy,
  CatalogLocale,
  CatalogLocalizationInput,
  DataPolicy,
  ProductKind,
  ProductOfferLocalizationInput,
  ProductOfferStatus,
} from '@ysim/contracts';

const codePattern = /^[A-Z][A-Z0-9_-]{1,63}$/u;
const uuidPattern =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;
const locales = new Set<CatalogLocale>(['en', 'vi', 'lo']);
const offerStatuses = new Set<ProductOfferStatus>([
  'DRAFT',
  'PUBLISHED',
  'SUSPENDED',
]);
const productKinds = new Set<ProductKind>(['ESIM_DATA']);
const activationPolicies = new Set<ActivationPolicy>([
  'FIRST_NETWORK_CONNECTION',
  'INSTALLATION',
]);
const dataPolicies = new Set<DataPolicy>([
  'FIXED',
  'DAILY',
  'UNLIMITED',
]);

export class CatalogPolicyError extends Error {}

export function normalizeCatalogCode(
  value: unknown,
  field = 'code',
): string {
  if (typeof value !== 'string') {
    throw new CatalogPolicyError(`${field} must be a string`);
  }

  const normalized = value.trim().toUpperCase();
  if (!codePattern.test(normalized)) {
    throw new CatalogPolicyError(
      `${field} must contain 2 to 64 uppercase letters, digits, underscores or hyphens`,
    );
  }

  return normalized;
}

export function requireUuid(value: unknown, field: string): string {
  if (typeof value !== 'string' || !uuidPattern.test(value)) {
    throw new CatalogPolicyError(`${field} must be a valid UUID`);
  }

  return value.toLowerCase();
}

export function requireUuidList(
  value: unknown,
  field: string,
): string[] {
  if (!Array.isArray(value) || value.length === 0) {
    throw new CatalogPolicyError(`${field} must contain at least one UUID`);
  }

  const normalized = value.map((item) => requireUuid(item, field));
  const unique = [...new Set(normalized)];

  if (unique.length !== normalized.length) {
    throw new CatalogPolicyError(`${field} must not contain duplicates`);
  }

  return unique;
}

export function requireCatalogLocale(value: unknown): CatalogLocale {
  if (typeof value !== 'string' || !locales.has(value as CatalogLocale)) {
    throw new CatalogPolicyError('locale must be en, vi or lo');
  }

  return value as CatalogLocale;
}

export function requireOfferStatus(
  value: unknown,
): ProductOfferStatus {
  if (
    typeof value !== 'string' ||
    !offerStatuses.has(value as ProductOfferStatus)
  ) {
    throw new CatalogPolicyError(
      'status must be DRAFT, PUBLISHED or SUSPENDED',
    );
  }

  return value as ProductOfferStatus;
}

export function requireProductKind(value: unknown): ProductKind {
  if (
    typeof value !== 'string' ||
    !productKinds.has(value as ProductKind)
  ) {
    throw new CatalogPolicyError('kind must be ESIM_DATA');
  }

  return value as ProductKind;
}

export function requireActivationPolicy(
  value: unknown,
): ActivationPolicy {
  if (
    typeof value !== 'string' ||
    !activationPolicies.has(value as ActivationPolicy)
  ) {
    throw new CatalogPolicyError(
      'activationPolicy must be FIRST_NETWORK_CONNECTION or INSTALLATION',
    );
  }

  return value as ActivationPolicy;
}

export function requireText(
  value: unknown,
  field: string,
  maximum = 200,
): string {
  if (typeof value !== 'string') {
    throw new CatalogPolicyError(`${field} must be a string`);
  }

  const normalized = value.trim();
  if (normalized.length < 1 || normalized.length > maximum) {
    throw new CatalogPolicyError(
      `${field} must contain 1 to ${maximum} characters`,
    );
  }

  return normalized;
}

export function optionalText(
  value: unknown,
  field: string,
  maximum = 500,
): string | null {
  if (value === undefined || value === null || value === '') {
    return null;
  }

  return requireText(value, field, maximum);
}

export function requirePositiveInteger(
  value: unknown,
  field: string,
  maximum = 1_000_000,
): number {
  if (
    typeof value !== 'number' ||
    !Number.isInteger(value) ||
    value < 1 ||
    value > maximum
  ) {
    throw new CatalogPolicyError(
      `${field} must be an integer from 1 through ${maximum}`,
    );
  }

  return value;
}

function optionalPositiveInteger(
  value: unknown,
  field: string,
): number | null {
  if (value === undefined || value === null) return null;
  return requirePositiveInteger(value, field);
}

export function normalizeCatalogLocalizations(
  value: unknown,
): CatalogLocalizationInput[] {
  if (!Array.isArray(value)) {
    throw new CatalogPolicyError('localizations must be an array');
  }

  const normalized = value.map((item, index) => {
    if (typeof item !== 'object' || item === null) {
      throw new CatalogPolicyError(
        `localizations[${index}] must be an object`,
      );
    }

    const record = item as Record<string, unknown>;
    return {
      locale: requireCatalogLocale(record.locale),
      name: requireText(record.name, `localizations[${index}].name`),
    };
  });

  validateRequiredLocales(normalized.map((entry) => entry.locale));
  return normalized;
}

export function normalizeOfferLocalizations(
  value: unknown,
): ProductOfferLocalizationInput[] {
  if (!Array.isArray(value)) {
    throw new CatalogPolicyError('localizations must be an array');
  }

  const normalized = value.map((item, index) => {
    if (typeof item !== 'object' || item === null) {
      throw new CatalogPolicyError(
        `localizations[${index}] must be an object`,
      );
    }

    const record = item as Record<string, unknown>;
    return {
      locale: requireCatalogLocale(record.locale),
      title: requireText(
        record.title,
        `localizations[${index}].title`,
      ),
      shortDescription: optionalText(
        record.shortDescription,
        `localizations[${index}].shortDescription`,
      ),
    };
  });

  validateRequiredLocales(normalized.map((entry) => entry.locale));
  return normalized;
}

function validateRequiredLocales(values: CatalogLocale[]): void {
  const unique = new Set(values);
  if (unique.size !== values.length) {
    throw new CatalogPolicyError(
      'localizations must not contain duplicate locales',
    );
  }

  if (!unique.has('en') || !unique.has('vi')) {
    throw new CatalogPolicyError(
      'localizations must include canonical en and mandatory vi',
    );
  }
}

export interface NormalizedDataPolicy {
  dataPolicy: DataPolicy;
  dataAmountMb: number | null;
  dailyDataAmountMb: number | null;
  fairUseDataAmountMb: number | null;
}

export function normalizeDataPolicy(input: {
  dataPolicy: unknown;
  dataAmountMb?: unknown;
  dailyDataAmountMb?: unknown;
  fairUseDataAmountMb?: unknown;
}): NormalizedDataPolicy {
  if (
    typeof input.dataPolicy !== 'string' ||
    !dataPolicies.has(input.dataPolicy as DataPolicy)
  ) {
    throw new CatalogPolicyError(
      'dataPolicy must be FIXED, DAILY or UNLIMITED',
    );
  }

  const dataPolicy = input.dataPolicy as DataPolicy;
  const dataAmountMb = optionalPositiveInteger(
    input.dataAmountMb,
    'dataAmountMb',
  );
  const dailyDataAmountMb = optionalPositiveInteger(
    input.dailyDataAmountMb,
    'dailyDataAmountMb',
  );
  const fairUseDataAmountMb = optionalPositiveInteger(
    input.fairUseDataAmountMb,
    'fairUseDataAmountMb',
  );

  if (
    dataPolicy === 'FIXED' &&
    (dataAmountMb === null ||
      dailyDataAmountMb !== null ||
      fairUseDataAmountMb !== null)
  ) {
    throw new CatalogPolicyError(
      'FIXED dataPolicy requires only dataAmountMb',
    );
  }

  if (
    dataPolicy === 'DAILY' &&
    (dailyDataAmountMb === null ||
      dataAmountMb !== null ||
      fairUseDataAmountMb !== null)
  ) {
    throw new CatalogPolicyError(
      'DAILY dataPolicy requires only dailyDataAmountMb',
    );
  }

  if (
    dataPolicy === 'UNLIMITED' &&
    (dataAmountMb !== null || dailyDataAmountMb !== null)
  ) {
    throw new CatalogPolicyError(
      'UNLIMITED dataPolicy allows only optional fairUseDataAmountMb',
    );
  }

  return {
    dataPolicy,
    dataAmountMb,
    dailyDataAmountMb,
    fairUseDataAmountMb,
  };
}

export function selectLocalization<
  T extends { locale: CatalogLocale },
>(
  entries: readonly T[],
  requestedLocale: CatalogLocale,
): { value: T; sourceLocale: CatalogLocale } {
  const selected =
    entries.find((entry) => entry.locale === requestedLocale) ??
    entries.find((entry) => entry.locale === 'en');

  if (!selected) {
    throw new CatalogPolicyError(
      'canonical English localization is missing',
    );
  }

  return {
    value: selected,
    sourceLocale: selected.locale,
  };
}
