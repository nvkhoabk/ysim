import {
  BadRequestException,
  ConflictException,
  Injectable,
  NotFoundException,
  ServiceUnavailableException,
} from '@nestjs/common';
import type {
  CreatePriceBookEntryRequest,
  CreatePriceBookEntryResponse,
  CreatePriceBookRequest,
  CreatePriceBookResponse,
  CreatePricingQuoteRequest,
  CreatePricingQuoteResponse,
  CreateSupplierCostSnapshotRequest,
  CreateSupplierCostSnapshotResponse,
  GetPricingQuoteResponse,
  PriceBookTransitionResponse,
  PricingQuoteContract,
} from '@ysim/contracts';

import {
  calculateQuoteAmounts,
  currencyExponent,
  normalizePricingCode,
  PricingPolicyError,
  quoteStatus,
  requireEffectivePeriod,
  requireIsoTimestamp,
  requireMarketCurrencyPair,
  requireMoneyMinor,
  requirePricingChannel,
  requirePricingCurrency,
  requireQuantity,
  requireQuoteTtlSeconds,
  requireSnapshotHash,
  requireSupplierEnvironment,
  requireUuid,
  resolveQuoteExpiration,
} from '../domain/pricing-policy.js';
import { PricingRepository } from '../infrastructure/pricing.repository.js';

const isUniqueViolation = (error: unknown): boolean =>
  typeof error === 'object' &&
  error !== null &&
  'code' in error &&
  error.code === '23505';

@Injectable()
export class PricingService {
  constructor(private readonly repository: PricingRepository) {}

  async createPriceBook(
    request: CreatePriceBookRequest,
    actorIdentityId: string,
  ): Promise<CreatePriceBookResponse> {
    try {
      const pair = requireMarketCurrencyPair(
        request.market,
        request.currency,
      );
      const period = requireEffectivePeriod(
        request.validFrom,
        request.validTo,
      );

      const priceBook = await this.repository.createPriceBook({
        code: normalizePricingCode(request.code, 'code'),
        ...pair,
        channel: requirePricingChannel(request.channel),
        ...period,
        actorIdentityId: requireUuid(
          actorIdentityId,
          'actorIdentityId',
        ),
      });

      return { priceBook };
    } catch (error) {
      this.rethrowKnownError(error, 'Price Book code already exists');
    }
  }

  async createSupplierCostSnapshot(
    request: CreateSupplierCostSnapshotRequest,
    actorIdentityId: string,
  ): Promise<CreateSupplierCostSnapshotResponse> {
    try {
      const costSnapshot =
        await this.repository.createSupplierCostSnapshot({
          supplierPlanMappingId: requireUuid(
            request.supplierPlanMappingId,
            'supplierPlanMappingId',
          ),
          currency: requirePricingCurrency(request.currency),
          unitCostAmountMinor: requireMoneyMinor(
            request.unitCostAmountMinor,
            'unitCostAmountMinor',
          ),
          observedAt: requireIsoTimestamp(
            request.observedAt,
            'observedAt',
          ),
          sourceSnapshotHash: requireSnapshotHash(
            request.sourceSnapshotHash,
          ),
          actorIdentityId: requireUuid(
            actorIdentityId,
            'actorIdentityId',
          ),
        });

      if (!costSnapshot) {
        throw new NotFoundException(
          'Active Supplier Plan Mapping was not found',
        );
      }

      return { costSnapshot };
    } catch (error) {
      if (
        error instanceof Error &&
        error.message === 'PRICING_SUPPLIER_SNAPSHOT_HASH_MISMATCH'
      ) {
        throw new BadRequestException(
          'Supplier snapshot hash does not match the active Supplier Plan',
        );
      }

      this.rethrowKnownError(
        error,
        'Supplier cost snapshot already exists',
      );
    }
  }

  async createPriceBookEntry(
    priceBookId: string,
    request: CreatePriceBookEntryRequest,
    actorIdentityId: string,
  ): Promise<CreatePriceBookEntryResponse> {
    try {
      const entry = await this.repository.createPriceBookEntry({
        priceBookId: requireUuid(priceBookId, 'priceBookId'),
        productOfferId: requireUuid(
          request.productOfferId,
          'productOfferId',
        ),
        unitAmountMinor: requireMoneyMinor(
          request.unitAmountMinor,
          'unitAmountMinor',
        ),
        supplierCostSnapshotId: requireUuid(
          request.supplierCostSnapshotId,
          'supplierCostSnapshotId',
        ),
        actorIdentityId: requireUuid(
          actorIdentityId,
          'actorIdentityId',
        ),
      });

      if (!entry) {
        throw new NotFoundException('Price Book was not found');
      }

      return { entry };
    } catch (error) {
      if (
        error instanceof Error &&
        error.message === 'PRICING_PRICE_BOOK_NOT_DRAFT'
      ) {
        throw new BadRequestException(
          'Entries can only be added to a draft Price Book',
        );
      }

      if (
        error instanceof Error &&
        error.message ===
          'PRICING_OFFER_OR_COST_SNAPSHOT_UNAVAILABLE'
      ) {
        throw new BadRequestException(
          'Published Product Offer and matching supplier cost snapshot are required',
        );
      }

      this.rethrowKnownError(
        error,
        'Price Book already contains this Product Offer',
      );
    }
  }

  async activatePriceBook(
    priceBookId: string,
    actorIdentityId: string,
  ): Promise<PriceBookTransitionResponse> {
    try {
      const priceBook = await this.repository.activatePriceBook(
        requireUuid(priceBookId, 'priceBookId'),
        requireUuid(actorIdentityId, 'actorIdentityId'),
      );

      if (!priceBook) {
        throw new NotFoundException('Price Book was not found');
      }

      return { priceBook };
    } catch (error) {
      if (
        error instanceof Error &&
        error.message === 'PRICING_INVALID_ACTIVATE_TRANSITION'
      ) {
        throw new BadRequestException(
          'Only a draft Price Book can be activated',
        );
      }

      if (
        error instanceof Error &&
        error.message === 'PRICING_PRICE_BOOK_EMPTY'
      ) {
        throw new BadRequestException(
          'Price Book must contain at least one entry',
        );
      }

      if (
        error instanceof Error &&
        error.message === 'PRICING_PRICE_BOOK_EXPIRED'
      ) {
        throw new BadRequestException(
          'Expired Price Book cannot be activated',
        );
      }

      if (
        error instanceof Error &&
        error.message === 'PRICING_ACTIVE_BOOK_OVERLAP'
      ) {
        throw new ConflictException(
          'An active overlapping Price Book already exists',
        );
      }

      this.rethrowKnownError(error);
    }
  }

  async suspendPriceBook(
    priceBookId: string,
    actorIdentityId: string,
  ): Promise<PriceBookTransitionResponse> {
    try {
      const priceBook = await this.repository.suspendPriceBook(
        requireUuid(priceBookId, 'priceBookId'),
        requireUuid(actorIdentityId, 'actorIdentityId'),
      );

      if (!priceBook) {
        throw new NotFoundException('Price Book was not found');
      }

      return { priceBook };
    } catch (error) {
      if (
        error instanceof Error &&
        error.message === 'PRICING_INVALID_SUSPEND_TRANSITION'
      ) {
        throw new BadRequestException(
          'Only an active Price Book can be suspended',
        );
      }

      this.rethrowKnownError(error);
    }
  }

  async createQuote(
    request: CreatePricingQuoteRequest,
  ): Promise<CreatePricingQuoteResponse> {
    try {
      const pair = requireMarketCurrencyPair(
        request.market,
        request.currency,
      );
      const channel = requirePricingChannel(request.channel);
      const quantity = requireQuantity(request.quantity);
      const ttlSeconds = requireQuoteTtlSeconds(request.ttlSeconds);
      const offerCode = normalizePricingCode(
        request.offerCode,
        'offerCode',
      );
      const supplierEnvironment = this.configuredEnvironment();
      const issuedAt = new Date().toISOString();

      const source = await this.repository.findQuoteSource({
        offerCode,
        ...pair,
        channel,
        supplierEnvironment,
        issuedAt,
      });

      if (!source) {
        throw new NotFoundException(
          'No active price is available for this Product Offer',
        );
      }

      const amounts = calculateQuoteAmounts(
        source.unitAmountMinor,
        quantity,
      );
      const expiresAt = resolveQuoteExpiration(
        issuedAt,
        ttlSeconds,
        source.priceBookValidTo,
      );

      const quote = await this.repository.persistQuote({
        source,
        ...pair,
        channel,
        supplierEnvironment,
        quantity,
        ...amounts,
        issuedAt,
        expiresAt,
      });

      if (!quote) {
        throw new ConflictException(
          'Pricing changed while the quote was being issued',
        );
      }

      return {
        quote: {
          ...quote,
          status: quoteStatus(quote.expiresAt),
        },
      };
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  async getQuote(quoteId: string): Promise<GetPricingQuoteResponse> {
    try {
      const quote = await this.repository.findQuote(
        requireUuid(quoteId, 'quoteId'),
      );

      if (!quote) {
        throw new NotFoundException('Pricing Quote was not found');
      }

      const result: PricingQuoteContract = {
        ...quote,
        currencyExponent: currencyExponent(quote.currency),
        status: quoteStatus(quote.expiresAt),
      };

      return { quote: result };
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  private configuredEnvironment(): 'SANDBOX' | 'PRODUCTION' {
    try {
      return requireSupplierEnvironment(
        process.env.YSIM_PRICING_SUPPLIER_ENVIRONMENT,
      );
    } catch {
      throw new ServiceUnavailableException(
        'YSIM_PRICING_SUPPLIER_ENVIRONMENT must be configured',
      );
    }
  }

  private rethrowKnownError(
    error: unknown,
    conflictMessage = 'Pricing resource already exists',
  ): never {
    if (
      error instanceof BadRequestException ||
      error instanceof NotFoundException ||
      error instanceof ConflictException ||
      error instanceof ServiceUnavailableException
    ) {
      throw error;
    }

    if (error instanceof PricingPolicyError) {
      throw new BadRequestException(error.message);
    }

    if (isUniqueViolation(error)) {
      throw new ConflictException(conflictMessage);
    }

    throw error;
  }
}
