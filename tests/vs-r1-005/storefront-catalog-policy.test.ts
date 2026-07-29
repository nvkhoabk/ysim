import { describe, expect, it } from 'vitest';

import {
  normalizePublicCatalogCode,
  requireStorefrontEnvironment,
  resolveStorefrontLocale,
  STOREFRONT_CATALOG_CACHE_CONTROL,
  StorefrontCatalogPolicyError,
} from '../../apps/api/src/modules/catalog/public/domain/storefront-catalog-policy.js';

describe('storefront catalog policy', () => {
  it('uses an explicit supported locale', () => {
    expect(resolveStorefrontLocale('vi', 'en-US')).toBe('vi');
    expect(resolveStorefrontLocale(' LO ', undefined)).toBe('lo');
  });

  it('reads the first supported Accept-Language entry', () => {
    expect(
      resolveStorefrontLocale(
        undefined,
        'fr-FR;q=0.9, vi-VN;q=0.8, en;q=0.7',
      ),
    ).toBe('vi');
  });

  it('defaults to English when no supported locale is present', () => {
    expect(resolveStorefrontLocale(undefined, 'fr-FR')).toBe('en');
    expect(resolveStorefrontLocale(undefined, undefined)).toBe('en');
  });

  it('rejects an unsupported explicit locale', () => {
    expect(() => resolveStorefrontLocale('fr', 'vi')).toThrow(
      StorefrontCatalogPolicyError,
    );
  });

  it('requires an explicit supplier environment', () => {
    expect(requireStorefrontEnvironment('SANDBOX')).toBe(
      'SANDBOX',
    );
    expect(requireStorefrontEnvironment('PRODUCTION')).toBe(
      'PRODUCTION',
    );
    expect(() => requireStorefrontEnvironment(undefined)).toThrow(
      StorefrontCatalogPolicyError,
    );
  });

  it('normalizes stable public Catalog codes', () => {
    expect(
      normalizePublicCatalogCode(' jp ', 'destinationCode'),
    ).toBe('JP');
    expect(
      normalizePublicCatalogCode(
        'jp_fixed_5gb_7d',
        'offerCode',
      ),
    ).toBe('JP_FIXED_5GB_7D');
  });

  it('rejects invalid public Catalog codes', () => {
    expect(() =>
      normalizePublicCatalogCode('j', 'destinationCode'),
    ).toThrow(StorefrontCatalogPolicyError);
    expect(() =>
      normalizePublicCatalogCode('jp.vn', 'destinationCode'),
    ).toThrow(StorefrontCatalogPolicyError);
  });

  it('uses the accepted public cache contract', () => {
    expect(STOREFRONT_CATALOG_CACHE_CONTROL).toBe(
      'public, max-age=60, stale-while-revalidate=300',
    );
  });
});
