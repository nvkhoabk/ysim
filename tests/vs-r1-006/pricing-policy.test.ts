import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

import { describe, expect, it } from 'vitest';

import {
  calculateQuoteAmounts,
  currencyExponent,
  normalizePricingCode,
  PricingPolicyError,
  quoteStatus,
  requireEffectivePeriod,
  requireMarketCurrencyPair,
  requireMoneyMinor,
  requireQuantity,
  requireQuoteTtlSeconds,
  requireSnapshotHash,
  resolveQuoteExpiration,
} from '../../apps/api/src/modules/pricing/domain/pricing-policy.js';

describe('pricing policy', () => {
  it('normalizes stable Pricing codes', () => {
    expect(normalizePricingCode(' vn_b2c_2026 ', 'code')).toBe(
      'VN_B2C_2026',
    );
  });

  it('rejects invalid Pricing codes', () => {
    expect(() => normalizePricingCode('x', 'code')).toThrow(
      PricingPolicyError,
    );
    expect(() => normalizePricingCode('vn.price', 'code')).toThrow(
      PricingPolicyError,
    );
  });

  it('accepts only supported market and currency pairs', () => {
    expect(requireMarketCurrencyPair('VN', 'VND')).toEqual({
      market: 'VN',
      currency: 'VND',
    });
    expect(requireMarketCurrencyPair('LA', 'LAK')).toEqual({
      market: 'LA',
      currency: 'LAK',
    });
    expect(
      requireMarketCurrencyPair('INTERNATIONAL', 'USD'),
    ).toEqual({
      market: 'INTERNATIONAL',
      currency: 'USD',
    });
  });

  it('rejects mismatched market and currency pairs', () => {
    expect(() => requireMarketCurrencyPair('VN', 'USD')).toThrow(
      PricingPolicyError,
    );
    expect(() => requireMarketCurrencyPair('LA', 'VND')).toThrow(
      PricingPolicyError,
    );
  });

  it('requires integer-string money values', () => {
    expect(requireMoneyMinor('169000', 'amount')).toBe('169000');
    expect(() => requireMoneyMinor('000169000', 'amount')).toThrow(
      PricingPolicyError,
    );
    expect(() => requireMoneyMinor(169000, 'amount')).toThrow(
      PricingPolicyError,
    );
    expect(() => requireMoneyMinor('1.50', 'amount')).toThrow(
      PricingPolicyError,
    );
  });

  it('uses zero-decimal VND and LAK and two-decimal USD', () => {
    expect(currencyExponent('VND')).toBe(0);
    expect(currencyExponent('LAK')).toBe(0);
    expect(currencyExponent('USD')).toBe(2);
  });

  it('limits quote quantity', () => {
    expect(requireQuantity(1)).toBe(1);
    expect(requireQuantity(20)).toBe(20);
    expect(() => requireQuantity(0)).toThrow(PricingPolicyError);
    expect(() => requireQuantity(21)).toThrow(PricingPolicyError);
  });

  it('limits quote TTL and supplies a default', () => {
    expect(requireQuoteTtlSeconds(undefined)).toBe(600);
    expect(requireQuoteTtlSeconds(1)).toBe(1);
    expect(requireQuoteTtlSeconds(900)).toBe(900);
    expect(() => requireQuoteTtlSeconds(901)).toThrow(
      PricingPolicyError,
    );
  });

  it('calculates quote totals with BigInt precision', () => {
    expect(calculateQuoteAmounts('9007199254740991', 20)).toEqual({
      subtotalAmountMinor: '180143985094819820',
      totalAmountMinor: '180143985094819820',
    });
  });

  it('caps quote expiry at the Price Book valid-to timestamp', () => {
    expect(
      resolveQuoteExpiration(
        '2026-07-30T00:00:00.000Z',
        900,
        '2026-07-30T00:05:00.000Z',
      ),
    ).toBe('2026-07-30T00:05:00.000Z');
  });

  it('validates Price Book periods and source hashes', () => {
    expect(
      requireEffectivePeriod(
        '2026-07-30T00:00:00.000Z',
        '2026-08-30T00:00:00.000Z',
      ),
    ).toEqual({
      validFrom: '2026-07-30T00:00:00.000Z',
      validTo: '2026-08-30T00:00:00.000Z',
    });
    expect(
      requireSnapshotHash('a'.repeat(64)),
    ).toBe('a'.repeat(64));
    expect(() => requireSnapshotHash('A'.repeat(64))).toThrow(
      PricingPolicyError,
    );
  });

  it('derives quote expiry status from immutable timestamps', () => {
    expect(
      quoteStatus(
        '2026-07-30T00:10:00.000Z',
        '2026-07-30T00:09:59.999Z',
      ),
    ).toBe('ACTIVE');
    expect(
      quoteStatus(
        '2026-07-30T00:10:00.000Z',
        '2026-07-30T00:10:00.000Z',
      ),
    ).toBe('EXPIRED');
  });
  it('casts every persisted quote parameter for PostgreSQL', () => {
    const repository = readFileSync(
      resolve(
        process.cwd(),
        'apps/api/src/modules/pricing/infrastructure/pricing.repository.ts',
      ),
      'utf8',
    );

    for (const requiredCast of [
      '$1::uuid',
      '$2::uuid',
      '$3::varchar(64)',
      '$4::text',
      '$5::char(3)',
      '$6::text',
      '$7::numeric(20, 0)',
      '$8::integer',
      '$9::numeric(20, 0)',
      '$10::numeric(20, 0)',
      '$11::numeric(20, 0)',
      '$12::char(3)',
      '$13::uuid',
      '$14::varchar(64)',
      '$15::integer',
      '$16::uuid',
      '$17::integer',
      '$18::uuid',
      '$19::timestamptz',
      '$20::timestamptz',
      '$21::text',
    ]) {
      expect(repository).toContain(requiredCast);
    }
  });

});
