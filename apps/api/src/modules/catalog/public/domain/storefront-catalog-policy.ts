import type {
  StorefrontCatalogLocale,
  StorefrontSupplierEnvironment,
} from '@ysim/contracts';

const publicCodePattern = /^[A-Z][A-Z0-9_-]{1,63}$/u;

export const STOREFRONT_CATALOG_CACHE_CONTROL =
  'public, max-age=60, stale-while-revalidate=300';

export class StorefrontCatalogPolicyError extends Error {}

export function resolveStorefrontLocale(
  queryLocale: unknown,
  acceptLanguage: unknown,
): StorefrontCatalogLocale {
  if (queryLocale !== undefined) {
    if (typeof queryLocale !== 'string') {
      throw new StorefrontCatalogPolicyError(
        'locale must be en, vi or lo',
      );
    }

    const normalized = queryLocale.trim().toLowerCase();
    if (
      normalized !== 'en' &&
      normalized !== 'vi' &&
      normalized !== 'lo'
    ) {
      throw new StorefrontCatalogPolicyError(
        'locale must be en, vi or lo',
      );
    }

    return normalized;
  }

  if (typeof acceptLanguage === 'string') {
    for (const token of acceptLanguage.split(',')) {
      const language = token
        .split(';')[0]
        ?.trim()
        .toLowerCase()
        .split('-')[0];

      if (
        language === 'en' ||
        language === 'vi' ||
        language === 'lo'
      ) {
        return language;
      }
    }
  }

  return 'en';
}

export function requireStorefrontEnvironment(
  value: unknown,
): StorefrontSupplierEnvironment {
  if (value === 'SANDBOX' || value === 'PRODUCTION') {
    return value;
  }

  throw new StorefrontCatalogPolicyError(
    'YSIM_CATALOG_SUPPLIER_ENVIRONMENT must be SANDBOX or PRODUCTION',
  );
}

export function normalizePublicCatalogCode(
  value: unknown,
  field: string,
): string {
  if (typeof value !== 'string') {
    throw new StorefrontCatalogPolicyError(
      `${field} must be a string`,
    );
  }

  const normalized = value.trim().toUpperCase();
  if (!publicCodePattern.test(normalized)) {
    throw new StorefrontCatalogPolicyError(
      `${field} must contain 2 to 64 uppercase letters, digits, underscores or hyphens`,
    );
  }

  return normalized;
}
