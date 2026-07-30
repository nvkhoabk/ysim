import { randomUUID } from 'node:crypto';

import {
  BadRequestException,
  ConflictException,
  GoneException,
  Injectable,
  NotFoundException,
  ServiceUnavailableException,
  UnauthorizedException,
} from '@nestjs/common';
import type {
  CreateSalesOrderRequest,
  CreateSalesOrderResponse,
  GetSalesOrderResponse,
  SalesOrderContract,
} from '@ysim/contracts';

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
  requireSalesOrderLocale,
  requireUuid,
  resolveRecipientEmail,
  SalesOrderPolicyError,
} from '../domain/sales-order-policy.js';
import {
  SalesOrderRepository,
  type PersistedSalesOrder,
} from '../infrastructure/sales-order.repository.js';

@Injectable()
export class SalesOrderService {
  constructor(
    private readonly repository: SalesOrderRepository,
  ) {}

  async createOrder(
    request: CreateSalesOrderRequest,
    idempotencyHeader: string | undefined,
  ): Promise<CreateSalesOrderResponse> {
    try {
      const quoteId = requireUuid(
        request.quoteId,
        'quoteId',
      );
      const idempotencyKey =
        normalizeIdempotencyKey(idempotencyHeader);
      const customerName = normalizeCustomerName(
        request.customerName,
      );
      const customerEmail = normalizeEmail(
        request.customerEmail,
        'customerEmail',
      );
      const recipientEmail = resolveRecipientEmail(
        request.recipientEmail,
        customerEmail,
      );
      const locale = requireSalesOrderLocale(request.locale);
      const secret = this.configuredAccessSecret();
      const proposedOrderId = randomUUID();
      const createdAt = new Date().toISOString();
      const proposedOrderNumber = deriveOrderNumber(
        proposedOrderId,
        createdAt,
      );
      const idempotencyKeyHash =
        hashIdempotencyKey(idempotencyKey);
      const requestFingerprint = createRequestFingerprint({
        quoteId,
        customerName,
        customerEmail,
        recipientEmail,
        locale,
      });
      const proposedAccessToken = deriveOrderAccessToken(
        secret,
        proposedOrderId,
        idempotencyKey,
      );

      const result = await this.repository.convertQuote({
        proposedOrderId,
        proposedOrderNumber,
        quoteId,
        idempotencyKeyHash,
        requestFingerprint,
        orderAccessTokenHash: hashOrderAccessToken(
          proposedAccessToken,
        ),
        customerName,
        customerEmail,
        recipientEmail,
        locale,
        createdAt,
      });

      switch (result.kind) {
        case 'QUOTE_NOT_FOUND':
          throw new NotFoundException(
            'Pricing Quote was not found',
          );
        case 'QUOTE_EXPIRED':
          throw new GoneException(
            'Pricing Quote has expired',
          );
        case 'CHANNEL_NOT_SUPPORTED':
          throw new BadRequestException(
            'Only B2C Pricing Quotes can use the public order route',
          );
        case 'QUOTE_ALREADY_CONVERTED':
          throw new ConflictException(
            'Pricing Quote has already been converted with different request data',
          );
        case 'CREATED':
        case 'REPLAY': {
          const orderAccessToken = deriveOrderAccessToken(
            secret,
            result.order.id,
            idempotencyKey,
          );

          if (
            !accessTokenHashMatches(
              orderAccessToken,
              result.order.orderAccessTokenHash,
            )
          ) {
            throw new Error(
              'SALES_ORDER_ACCESS_TOKEN_INTEGRITY_FAILURE',
            );
          }

          return {
            order: this.toPublicOrder(result.order),
            orderAccessToken,
            idempotentReplay: result.kind === 'REPLAY',
          };
        }
      }
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  async getOrder(
    orderIdValue: string,
    orderAccessToken: string | undefined,
  ): Promise<GetSalesOrderResponse> {
    try {
      const orderId = requireUuid(orderIdValue, 'orderId');
      if (
        typeof orderAccessToken !== 'string' ||
        orderAccessToken.length < 32 ||
        orderAccessToken.length > 256
      ) {
        throw new UnauthorizedException(
          'x-ysim-order-access-token header is required',
        );
      }

      const order = await this.repository.findOrder(
        orderId,
        hashOrderAccessToken(orderAccessToken),
      );

      if (!order) {
        throw new NotFoundException(
          'Sales Order was not found',
        );
      }

      return {
        order: this.toPublicOrder(order),
      };
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  private configuredAccessSecret(): string {
    try {
      return requireOrderAccessSecret(
        process.env.YSIM_ORDER_ACCESS_SECRET,
      );
    } catch {
      throw new ServiceUnavailableException(
        'YSIM_ORDER_ACCESS_SECRET must be configured',
      );
    }
  }

  private toPublicOrder(
    order: PersistedSalesOrder,
  ): SalesOrderContract {
    const {
      orderAccessTokenHash: _tokenHash,
      idempotencyKeyHash: _idempotencyHash,
      requestFingerprint: _fingerprint,
      ...publicOrder
    } = order;

    return {
      ...publicOrder,
      currencyExponent: currencyExponent(
        publicOrder.currency,
      ),
    };
  }

  private rethrowKnownError(error: unknown): never {
    if (
      error instanceof BadRequestException ||
      error instanceof ConflictException ||
      error instanceof GoneException ||
      error instanceof NotFoundException ||
      error instanceof ServiceUnavailableException ||
      error instanceof UnauthorizedException
    ) {
      throw error;
    }

    if (error instanceof SalesOrderPolicyError) {
      throw new BadRequestException(error.message);
    }

    throw error;
  }
}
