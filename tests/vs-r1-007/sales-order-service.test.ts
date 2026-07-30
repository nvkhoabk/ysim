import {
  GoneException,
  NotFoundException,
  UnauthorizedException,
} from '@nestjs/common';
import { afterEach, describe, expect, it } from 'vitest';

import { SalesOrderService } from '../../apps/api/src/modules/sales-order/application/sales-order.service.js';
import {
  deriveOrderAccessToken,
  hashIdempotencyKey,
  hashOrderAccessToken,
} from '../../apps/api/src/modules/sales-order/domain/sales-order-policy.js';
import type {
  ConvertQuoteInput,
  ConvertQuoteResult,
  PersistedSalesOrder,
} from '../../apps/api/src/modules/sales-order/infrastructure/sales-order.repository.js';

const secret =
  'order-access-secret-that-is-long-enough-for-tests';

const baseOrder = (
  id: string,
  accessTokenHash: string,
): PersistedSalesOrder => ({
  id,
  orderNumber: 'YS-20260730-A00000000000',
  quoteId: 'b0000000-0000-4000-8000-000000000001',
  offerCode: 'JP_FIXED_5GB_7D',
  market: 'VN',
  currency: 'VND',
  channel: 'B2C',
  unitAmountMinor: '169000',
  quantity: 2,
  subtotalAmountMinor: '338000',
  totalAmountMinor: '338000',
  status: 'PENDING_PAYMENT',
  paymentStatus: 'UNPAID',
  fulfillmentStatus: 'UNFULFILLED',
  source: 'STOREFRONT',
  customerName: 'Nguyễn Văn Khoa',
  customerEmail: 'khoa@example.com',
  recipientEmail: 'recipient@example.com',
  locale: 'vi',
  quoteIssuedAt: '2026-07-30T06:00:00.000Z',
  quoteExpiresAt: '2026-07-30T06:05:00.000Z',
  createdAt: '2026-07-30T06:01:00.000Z',
  version: 1,
  orderAccessTokenHash: accessTokenHash,
  idempotencyKeyHash: hashIdempotencyKey(
    'checkout-session-0001',
  ),
  requestFingerprint: 'a'.repeat(64),
});

class FakeRepository {
  conversionResult: ConvertQuoteResult = {
    kind: 'QUOTE_NOT_FOUND',
  };
  findResult: PersistedSalesOrder | null = null;
  lastConvertInput: ConvertQuoteInput | undefined;

  async convertQuote(
    input: ConvertQuoteInput,
  ): Promise<ConvertQuoteResult> {
    this.lastConvertInput = input;

    if (
      this.conversionResult.kind === 'CREATED' ||
      this.conversionResult.kind === 'REPLAY'
    ) {
      const token = deriveOrderAccessToken(
        secret,
        this.conversionResult.order.id,
        'checkout-session-0001',
      );
      return {
        ...this.conversionResult,
        order: {
          ...this.conversionResult.order,
          orderAccessTokenHash:
            hashOrderAccessToken(token),
        },
      };
    }

    return this.conversionResult;
  }

  async findOrder(): Promise<PersistedSalesOrder | null> {
    return this.findResult;
  }
}

const request = {
  quoteId: 'b0000000-0000-4000-8000-000000000001',
  customerName: 'Nguyễn Văn Khoa',
  customerEmail: 'Khoa@Example.com',
  recipientEmail: 'Recipient@Example.com',
  locale: 'vi' as const,
};

afterEach(() => {
  delete process.env.YSIM_ORDER_ACCESS_SECRET;
});

describe('sales order service', () => {
  it('creates a public order without internal hashes', async () => {
    process.env.YSIM_ORDER_ACCESS_SECRET = secret;
    const repository = new FakeRepository();
    repository.conversionResult = {
      kind: 'CREATED',
      order: baseOrder(
        'a0000000-0000-4000-8000-000000000001',
        '0'.repeat(64),
      ),
    };
    const service = new SalesOrderService(
      repository as never,
    );

    const response = await service.createOrder(
      request,
      'checkout-session-0001',
    );

    expect(response.idempotentReplay).toBe(false);
    expect(response.order.currencyExponent).toBe(0);
    expect(response.order.customerEmail)
      .toBe('khoa@example.com');
    expect(response.order.recipientEmail)
      .toBe('recipient@example.com');
    expect(response.orderAccessToken.length)
      .toBeGreaterThan(32);
    expect(response.order).not.toHaveProperty(
      'orderAccessTokenHash',
    );
    expect(repository.lastConvertInput?.customerEmail)
      .toBe('khoa@example.com');
  });

  it('returns the same deterministic token for a replay', async () => {
    process.env.YSIM_ORDER_ACCESS_SECRET = secret;
    const repository = new FakeRepository();
    repository.conversionResult = {
      kind: 'REPLAY',
      order: baseOrder(
        'a0000000-0000-4000-8000-000000000001',
        '0'.repeat(64),
      ),
    };
    const service = new SalesOrderService(
      repository as never,
    );

    const response = await service.createOrder(
      request,
      'checkout-session-0001',
    );

    expect(response.idempotentReplay).toBe(true);
    expect(response.order.id)
      .toBe('a0000000-0000-4000-8000-000000000001');
    expect(response.orderAccessToken).toBe(
      deriveOrderAccessToken(
        secret,
        response.order.id,
        'checkout-session-0001',
      ),
    );
  });

  it('maps an expired quote to Gone', async () => {
    process.env.YSIM_ORDER_ACCESS_SECRET = secret;
    const repository = new FakeRepository();
    repository.conversionResult = {
      kind: 'QUOTE_EXPIRED',
    };
    const service = new SalesOrderService(
      repository as never,
    );

    await expect(
      service.createOrder(
        request,
        'checkout-session-0001',
      ),
    ).rejects.toBeInstanceOf(GoneException);
  });

  it('requires an order access token on reads', async () => {
    const repository = new FakeRepository();
    const service = new SalesOrderService(
      repository as never,
    );

    await expect(
      service.getOrder(
        'a0000000-0000-4000-8000-000000000001',
        undefined,
      ),
    ).rejects.toBeInstanceOf(UnauthorizedException);
  });

  it('returns a token-protected order and hides internals', async () => {
    const repository = new FakeRepository();
    repository.findResult = baseOrder(
      'a0000000-0000-4000-8000-000000000001',
      'a'.repeat(64),
    );
    const service = new SalesOrderService(
      repository as never,
    );

    const result = await service.getOrder(
      'a0000000-0000-4000-8000-000000000001',
      'x'.repeat(43),
    );

    expect(result.order.totalAmountMinor).toBe('338000');
    expect(result.order.currencyExponent).toBe(0);
    expect(result.order).not.toHaveProperty(
      'requestFingerprint',
    );

    repository.findResult = null;
    await expect(
      service.getOrder(
        'a0000000-0000-4000-8000-000000000001',
        'x'.repeat(43),
      ),
    ).rejects.toBeInstanceOf(NotFoundException);
  });
});
