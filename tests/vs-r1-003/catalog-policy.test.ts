import { describe, expect, it } from 'vitest';

import {
  CatalogPolicyError,
  normalizeCatalogCode,
  normalizeCatalogLocalizations,
  normalizeDataPolicy,
  normalizeOfferLocalizations,
  requireCatalogLocale,
  requireOfferStatus,
  requireUuidList,
  selectLocalization,
} from '../../apps/api/src/modules/catalog/domain/catalog-policy.js';

describe('catalog policy', () => {
  it('normalizes stable catalog codes', () => {
    expect(normalizeCatalogCode(' jp_fixed_5gb_7d ')).toBe(
      'JP_FIXED_5GB_7D',
    );
  });

  it('rejects invalid catalog codes', () => {
    expect(() => normalizeCatalogCode('jp.offer')).toThrow(
      CatalogPolicyError,
    );
  });

  it('requires English and Vietnamese localizations', () => {
    expect(
      normalizeCatalogLocalizations([
        { locale: 'en', name: 'Japan' },
        { locale: 'vi', name: 'Nhật Bản' },
      ]),
    ).toHaveLength(2);

    expect(() =>
      normalizeCatalogLocalizations([
        { locale: 'en', name: 'Japan' },
      ]),
    ).toThrow(CatalogPolicyError);
  });

  it('rejects duplicate localization locales', () => {
    expect(() =>
      normalizeOfferLocalizations([
        { locale: 'en', title: 'Offer A' },
        { locale: 'en', title: 'Offer B' },
        { locale: 'vi', title: 'Gói A' },
      ]),
    ).toThrow(CatalogPolicyError);
  });

  it('validates fixed and daily data shapes', () => {
    expect(
      normalizeDataPolicy({
        dataPolicy: 'FIXED',
        dataAmountMb: 5_120,
      }),
    ).toEqual({
      dataPolicy: 'FIXED',
      dataAmountMb: 5_120,
      dailyDataAmountMb: null,
      fairUseDataAmountMb: null,
    });

    expect(
      normalizeDataPolicy({
        dataPolicy: 'DAILY',
        dailyDataAmountMb: 1_024,
      }),
    ).toEqual({
      dataPolicy: 'DAILY',
      dataAmountMb: null,
      dailyDataAmountMb: 1_024,
      fairUseDataAmountMb: null,
    });
  });

  it('rejects mismatched data-policy fields', () => {
    expect(() =>
      normalizeDataPolicy({
        dataPolicy: 'FIXED',
        dailyDataAmountMb: 1_024,
      }),
    ).toThrow(CatalogPolicyError);

    expect(() =>
      normalizeDataPolicy({
        dataPolicy: 'UNLIMITED',
        dataAmountMb: 10_240,
      }),
    ).toThrow(CatalogPolicyError);
  });

  it('rejects duplicate destination identifiers', () => {
    const id = '10000000-0000-4000-8000-000000000001';

    expect(() =>
      requireUuidList([id, id], 'destinationIds'),
    ).toThrow(CatalogPolicyError);
  });

  it('falls back to canonical English localization', () => {
    const selected = selectLocalization(
      [
        { locale: 'en' as const, title: 'Japan offer' },
        { locale: 'vi' as const, title: 'Gói Nhật Bản' },
      ],
      requireCatalogLocale('lo'),
    );

    expect(selected.value.title).toBe('Japan offer');
    expect(selected.sourceLocale).toBe('en');
    expect(requireOfferStatus('PUBLISHED')).toBe('PUBLISHED');
  });
});
