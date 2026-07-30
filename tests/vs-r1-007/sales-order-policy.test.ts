import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

import { describe, expect, it } from 'vitest';

import {
  accessTokenHashMatches,
  createRequestFingerprint,
  currencyExponent,
  deriveOrderAccessToken,
  deriveOrderNumber,
  hashIdempotencyKey,
  hashOrderAccessToken,
  normalizeCustomerName,
  normalizeEmail,
  normalizeIdempotencyKey,
  requireOrderAccessSecret,
  requirePublicQuoteChannel,
  requireSalesOrderLocale,
  requireUuid,
  resolveRecipientEmail,
  SalesOrderPolicyError,
} from '../../apps/api/src/modules/sales-order/domain/sales-order-policy.js';

describe('sales order policy', () => {
  it('normalizes UUID values', () => {
    expect(
      requireUuid(
        'A0000000-0000-4000-8000-000000000001',
        'quoteId',
      ),
    ).toBe('a0000000-0000-4000-8000-000000000001');
  });

  it('rejects invalid UUID values', () => {
    expect(() => requireUuid('quote-1', 'quoteId'))
      .toThrow(SalesOrderPolicyError);
  });

  it('normalizes stable idempotency keys', () => {
    expect(
      normalizeIdempotencyKey(
        '  checkout-session-0001  ',
      ),
    ).toBe('checkout-session-0001');
  });

  it('rejects short or unsafe idempotency keys', () => {
    expect(() => normalizeIdempotencyKey('short'))
      .toThrow(SalesOrderPolicyError);
    expect(() =>
      normalizeIdempotencyKey('unsafe key with spaces'),
    ).toThrow(SalesOrderPolicyError);
  });

  it('normalizes customer names', () => {
    expect(
      normalizeCustomerName('  Nguyễn   Văn   Khoa  '),
    ).toBe('Nguyễn Văn Khoa');
  });

  it('rejects invalid customer names', () => {
    expect(() => normalizeCustomerName('A'))
      .toThrow(SalesOrderPolicyError);
    expect(() => normalizeCustomerName('Bad\u0000Name'))
      .toThrow(SalesOrderPolicyError);
  });

  it('normalizes email addresses', () => {
    expect(
      normalizeEmail(
        '  Khoa.Example@YSIM.VN ',
        'customerEmail',
      ),
    ).toBe('khoa.example@ysim.vn');
  });

  it('uses customer email as recipient fallback', () => {
    expect(
      resolveRecipientEmail(
        undefined,
        'customer@example.com',
      ),
    ).toBe('customer@example.com');
    expect(
      resolveRecipientEmail(
        'Recipient@Example.com',
        'customer@example.com',
      ),
    ).toBe('recipient@example.com');
  });

  it('defaults locale to English and accepts R1 locales', () => {
    expect(requireSalesOrderLocale(undefined)).toBe('en');
    expect(requireSalesOrderLocale('vi')).toBe('vi');
    expect(requireSalesOrderLocale('lo')).toBe('lo');
  });

  it('rejects unsupported locales', () => {
    expect(() => requireSalesOrderLocale('fr'))
      .toThrow(SalesOrderPolicyError);
  });

  it('limits the public conversion route to B2C quotes', () => {
    expect(requirePublicQuoteChannel('B2C')).toBe('B2C');
    expect(() => requirePublicQuoteChannel('AGENCY'))
      .toThrow(SalesOrderPolicyError);
  });

  it('creates deterministic idempotency and request hashes', () => {
    expect(hashIdempotencyKey('checkout-session-0001'))
      .toMatch(/^[0-9a-f]{64}$/u);

    const input = {
      quoteId: 'a0000000-0000-4000-8000-000000000001',
      customerName: 'Nguyễn Văn Khoa',
      customerEmail: 'khoa@example.com',
      recipientEmail: 'recipient@example.com',
      locale: 'vi' as const,
    };

    expect(createRequestFingerprint(input))
      .toBe(createRequestFingerprint(input));
    expect(
      createRequestFingerprint({
        ...input,
        recipientEmail: 'other@example.com',
      }),
    ).not.toBe(createRequestFingerprint(input));
  });

  it('derives and verifies stable order access tokens', () => {
    const secret = requireOrderAccessSecret(
      'order-access-secret-that-is-long-enough-0001',
    );
    const token = deriveOrderAccessToken(
      secret,
      'a0000000-0000-4000-8000-000000000001',
      'checkout-session-0001',
    );
    const hash = hashOrderAccessToken(token);

    expect(token.length).toBeGreaterThan(32);
    expect(hash).toMatch(/^[0-9a-f]{64}$/u);
    expect(accessTokenHashMatches(token, hash)).toBe(true);
    expect(
      accessTokenHashMatches(`${token}x`, hash),
    ).toBe(false);
  });

  it('derives stable order numbers and currency exponents', () => {
    expect(
      deriveOrderNumber(
        'a0000000-0000-4000-8000-000000000001',
        '2026-07-30T06:00:00.000Z',
      ),
    ).toBe('YS-20260730-A00000000000');

    expect(currencyExponent('VND')).toBe(0);
    expect(currencyExponent('LAK')).toBe(0);
    expect(currencyExponent('USD')).toBe(2);
  });
  it('uses the declared supplier mapping fixture in runtime proof', () => {
    const runtimeProof = readFileSync(
      resolve(
        process.cwd(),
        'scripts/vs-r1-007/runtime-proof.mjs',
      ),
      'utf8',
    );
    const eslintConfig = readFileSync(
      resolve(
        process.cwd(),
        'scripts/vs-r1-007/eslint.config.mjs',
      ),
      'utf8',
    );

    expect(runtimeProof).toContain(
      'supplierPlanMappingId: supplierMappingId',
    );
    expect(runtimeProof).not.toContain(
      '          supplierPlanMappingId,\n',
    );
    expect(eslintConfig).toContain(
      "'no-undef': 'error'",
    );
  });

});
