import {
  BadRequestException,
  Injectable,
  NotFoundException,
  ServiceUnavailableException,
} from '@nestjs/common';
import type {
  ListStorefrontDestinationsResponse,
  ListStorefrontOffersResponse,
  StorefrontCatalogOfferContract,
} from '@ysim/contracts';

import {
  normalizePublicCatalogCode,
  requireStorefrontEnvironment,
  resolveStorefrontLocale,
  StorefrontCatalogPolicyError,
} from '../domain/storefront-catalog-policy.js';
import { StorefrontCatalogRepository } from '../infrastructure/storefront-catalog.repository.js';

@Injectable()
export class StorefrontCatalogService {
  constructor(
    private readonly repository: StorefrontCatalogRepository,
  ) {}

  async listDestinations(
    locale: unknown,
    acceptLanguage: unknown,
  ): Promise<ListStorefrontDestinationsResponse> {
    const context = this.resolveContext(locale, acceptLanguage);
    const items = await this.repository.listDestinations(
      context.locale,
      context.environment,
    );

    return { items };
  }

  async listOffersByDestination(
    destinationCode: unknown,
    locale: unknown,
    acceptLanguage: unknown,
  ): Promise<ListStorefrontOffersResponse> {
    const context = this.resolveContext(locale, acceptLanguage);
    const normalizedCode = this.normalizeCode(
      destinationCode,
      'destinationCode',
    );

    const items =
      await this.repository.listOffersByDestination(
        normalizedCode,
        context.locale,
        context.environment,
      );

    return { items };
  }

  async getOffer(
    offerCode: unknown,
    locale: unknown,
    acceptLanguage: unknown,
  ): Promise<StorefrontCatalogOfferContract> {
    const context = this.resolveContext(locale, acceptLanguage);
    const normalizedCode = this.normalizeCode(
      offerCode,
      'offerCode',
    );

    const offer = await this.repository.findOfferByCode(
      normalizedCode,
      context.locale,
      context.environment,
    );

    if (!offer) {
      throw new NotFoundException(
        'Published and supplier-mapped Product Offer was not found',
      );
    }

    return offer;
  }

  private resolveContext(
    locale: unknown,
    acceptLanguage: unknown,
  ): {
    locale: 'en' | 'vi' | 'lo';
    environment: 'SANDBOX' | 'PRODUCTION';
  } {
    try {
      return {
        locale: resolveStorefrontLocale(
          locale,
          acceptLanguage,
        ),
        environment: requireStorefrontEnvironment(
          process.env.YSIM_CATALOG_SUPPLIER_ENVIRONMENT,
        ),
      };
    } catch (error) {
      if (error instanceof StorefrontCatalogPolicyError) {
        if (
          error.message.startsWith(
            'YSIM_CATALOG_SUPPLIER_ENVIRONMENT',
          )
        ) {
          throw new ServiceUnavailableException(error.message);
        }

        throw new BadRequestException(error.message);
      }

      throw error;
    }
  }

  private normalizeCode(
    value: unknown,
    field: string,
  ): string {
    try {
      return normalizePublicCatalogCode(value, field);
    } catch (error) {
      if (error instanceof StorefrontCatalogPolicyError) {
        throw new BadRequestException(error.message);
      }

      throw error;
    }
  }
}
