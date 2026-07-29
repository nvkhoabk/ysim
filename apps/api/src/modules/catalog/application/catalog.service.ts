import {
  BadRequestException,
  ConflictException,
  Injectable,
  NotFoundException,
} from '@nestjs/common';
import type {
  CreateDestinationRequest,
  CreateDestinationResponse,
  CreateProductOfferRequest,
  CreateProductOfferResponse,
  CreateProductRequest,
  CreateProductResponse,
  CreateRegionRequest,
  CreateRegionResponse,
  ListProductOffersResponse,
  LocalizedProductOfferContract,
  ProductOfferTransitionResponse,
} from '@ysim/contracts';

import {
  CatalogPolicyError,
  normalizeCatalogCode,
  normalizeCatalogLocalizations,
  normalizeDataPolicy,
  normalizeOfferLocalizations,
  requireActivationPolicy,
  requireCatalogLocale,
  requireOfferStatus,
  requirePositiveInteger,
  requireProductKind,
  requireText,
  requireUuid,
  requireUuidList,
} from '../domain/catalog-policy.js';
import { CatalogRepository } from '../infrastructure/catalog.repository.js';

const isUniqueViolation = (error: unknown): boolean =>
  typeof error === 'object' &&
  error !== null &&
  'code' in error &&
  error.code === '23505';

@Injectable()
export class CatalogService {
  constructor(private readonly repository: CatalogRepository) {}

  async createRegion(
    request: CreateRegionRequest,
    actorIdentityId: string,
  ): Promise<CreateRegionResponse> {
    try {
      const region = await this.repository.createRegion({
        code: normalizeCatalogCode(request.code, 'code'),
        localizations: normalizeCatalogLocalizations(
          request.localizations,
        ),
        actorIdentityId: requireUuid(
          actorIdentityId,
          'actorIdentityId',
        ),
      });

      return { region };
    } catch (error) {
      this.rethrowKnownError(error, 'Region code already exists');
    }
  }

  async createDestination(
    request: CreateDestinationRequest,
    actorIdentityId: string,
  ): Promise<CreateDestinationResponse> {
    try {
      const destination = await this.repository.createDestination({
        code: normalizeCatalogCode(request.code, 'code'),
        regionId: requireUuid(request.regionId, 'regionId'),
        localizations: normalizeCatalogLocalizations(
          request.localizations,
        ),
        actorIdentityId: requireUuid(
          actorIdentityId,
          'actorIdentityId',
        ),
      });

      if (!destination) {
        throw new NotFoundException(
          'Active catalog region was not found',
        );
      }

      return { destination };
    } catch (error) {
      this.rethrowKnownError(
        error,
        'Destination code already exists',
      );
    }
  }

  async createProduct(
    request: CreateProductRequest,
    actorIdentityId: string,
  ): Promise<CreateProductResponse> {
    try {
      const product = await this.repository.createProduct({
        code: normalizeCatalogCode(request.code, 'code'),
        kind: requireProductKind(request.kind),
        actorIdentityId: requireUuid(
          actorIdentityId,
          'actorIdentityId',
        ),
      });

      return { product };
    } catch (error) {
      this.rethrowKnownError(error, 'Product code already exists');
    }
  }

  async createOffer(
    request: CreateProductOfferRequest,
    actorIdentityId: string,
  ): Promise<CreateProductOfferResponse> {
    try {
      const dataPolicy = normalizeDataPolicy(request);
      const offer = await this.repository.createOffer({
        code: normalizeCatalogCode(request.code, 'code'),
        productId: requireUuid(request.productId, 'productId'),
        destinationIds: requireUuidList(
          request.destinationIds,
          'destinationIds',
        ),
        durationDays: requirePositiveInteger(
          request.durationDays,
          'durationDays',
          365,
        ),
        ...dataPolicy,
        activationPolicy: requireActivationPolicy(
          request.activationPolicy,
        ),
        hotspotSupported: this.requireBoolean(
          request.hotspotSupported,
          'hotspotSupported',
        ),
        phoneNumberIncluded: this.requireBoolean(
          request.phoneNumberIncluded,
          'phoneNumberIncluded',
        ),
        networkName: requireText(
          request.networkName,
          'networkName',
          200,
        ),
        localizations: normalizeOfferLocalizations(
          request.localizations,
        ),
        actorIdentityId: requireUuid(
          actorIdentityId,
          'actorIdentityId',
        ),
      });

      if (!offer) {
        throw new NotFoundException(
          'Product or active destination was not found',
        );
      }

      return { offer };
    } catch (error) {
      this.rethrowKnownError(
        error,
        'Product Offer code already exists',
      );
    }
  }

  async publishOffer(
    offerId: string,
    actorIdentityId: string,
  ): Promise<ProductOfferTransitionResponse> {
    try {
      const offer = await this.repository.publishOffer(
        requireUuid(offerId, 'offerId'),
        requireUuid(actorIdentityId, 'actorIdentityId'),
      );

      if (!offer) {
        throw new NotFoundException('Product Offer was not found');
      }

      return { offer };
    } catch (error) {
      if (
        error instanceof Error &&
        error.message === 'CATALOG_INVALID_PUBLISH_TRANSITION'
      ) {
        throw new BadRequestException(
          'Only a draft Product Offer can be published',
        );
      }

      this.rethrowKnownError(error);
    }
  }

  async suspendOffer(
    offerId: string,
    actorIdentityId: string,
  ): Promise<ProductOfferTransitionResponse> {
    try {
      const offer = await this.repository.suspendOffer(
        requireUuid(offerId, 'offerId'),
        requireUuid(actorIdentityId, 'actorIdentityId'),
      );

      if (!offer) {
        throw new NotFoundException('Product Offer was not found');
      }

      return { offer };
    } catch (error) {
      if (
        error instanceof Error &&
        error.message === 'CATALOG_INVALID_SUSPEND_TRANSITION'
      ) {
        throw new BadRequestException(
          'Only a published Product Offer can be suspended',
        );
      }

      this.rethrowKnownError(error);
    }
  }

  async getOffer(
    offerId: string,
    locale: string | undefined,
  ): Promise<LocalizedProductOfferContract> {
    try {
      const offer = await this.repository.findLocalizedOffer(
        requireUuid(offerId, 'offerId'),
        requireCatalogLocale(locale ?? 'en'),
      );

      if (!offer) {
        throw new NotFoundException('Product Offer was not found');
      }

      return offer;
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  async listOffers(
    status: string | undefined,
    locale: string | undefined,
  ): Promise<ListProductOffersResponse> {
    try {
      const items = await this.repository.listLocalizedOffers(
        requireOfferStatus(status ?? 'PUBLISHED'),
        requireCatalogLocale(locale ?? 'en'),
      );

      return { items };
    } catch (error) {
      this.rethrowKnownError(error);
    }
  }

  private requireBoolean(value: unknown, field: string): boolean {
    if (typeof value !== 'boolean') {
      throw new CatalogPolicyError(`${field} must be a boolean`);
    }

    return value;
  }

  private rethrowKnownError(
    error: unknown,
    conflictMessage = 'Catalog code already exists',
  ): never {
    if (
      error instanceof BadRequestException ||
      error instanceof NotFoundException ||
      error instanceof ConflictException
    ) {
      throw error;
    }

    if (error instanceof CatalogPolicyError) {
      throw new BadRequestException(error.message);
    }

    if (isUniqueViolation(error)) {
      throw new ConflictException(conflictMessage);
    }

    throw error;
  }
}
