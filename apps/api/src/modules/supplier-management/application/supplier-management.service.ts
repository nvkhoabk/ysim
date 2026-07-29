import {
  BadRequestException,
  ConflictException,
  Injectable,
  NotFoundException,
  UnprocessableEntityException,
} from '@nestjs/common';
import type {
  CreateSupplierPlanMappingRequest,
  CreateSupplierPlanMappingResponse,
  ImportGigagoPlanRequest,
  ImportGigagoPlanResponse,
  ListActiveSupplierPlanMappingsResponse,
  ListSupplierEnvironmentProfilesResponse,
  SupplierEnvironment,
  SupplierPlanMappingTransitionResponse,
} from '@ysim/contracts';

import {
  GigagoPlanNormalizationError,
  normalizeGigagoPlan,
} from '../domain/gigago-plan-normalizer.js';
import { assessSupplierPlanMapping } from '../domain/supplier-plan-mapping-policy.js';
import { CatalogOfferReader } from '../infrastructure/catalog-offer-reader.js';
import { SupplierManagementRepository } from '../infrastructure/supplier-management.repository.js';

const uuidPattern =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu;

function requireUuid(value: unknown, field: string): string {
  if (typeof value !== 'string' || !uuidPattern.test(value)) {
    throw new BadRequestException(`${field} must be a valid UUID`);
  }

  return value.toLowerCase();
}

function requireEnvironment(value: unknown): SupplierEnvironment {
  if (value !== 'SANDBOX' && value !== 'PRODUCTION') {
    throw new BadRequestException(
      'environment must be SANDBOX or PRODUCTION',
    );
  }

  return value;
}

function isUniqueViolation(error: unknown): boolean {
  return (
    typeof error === 'object' &&
    error !== null &&
    'code' in error &&
    error.code === '23505'
  );
}

@Injectable()
export class SupplierManagementService {
  constructor(
    private readonly repository: SupplierManagementRepository,
    private readonly catalogOfferReader: CatalogOfferReader,
  ) {}

  async listGigagoEnvironments(): Promise<ListSupplierEnvironmentProfilesResponse> {
    return {
      items: await this.repository.listGigagoEnvironments(),
    };
  }

  async importGigagoPlan(
    request: ImportGigagoPlanRequest,
    actorIdentityId: string,
  ): Promise<ImportGigagoPlanResponse> {
    try {
      const normalized = normalizeGigagoPlan(
        request.payload,
        requireEnvironment(request.environment),
        request.observedAt,
      );

      const plan = await this.repository.upsertGigagoPlan(
        normalized,
        requireUuid(actorIdentityId, 'actorIdentityId'),
      );

      if (!plan) {
        throw new NotFoundException(
          'Gigago supplier environment was not found',
        );
      }

      return { plan };
    } catch (error) {
      if (error instanceof GigagoPlanNormalizationError) {
        throw new BadRequestException(error.message);
      }

      throw error;
    }
  }

  async createMapping(
    request: CreateSupplierPlanMappingRequest,
    actorIdentityId: string,
  ): Promise<CreateSupplierPlanMappingResponse> {
    const supplierPlanId = requireUuid(
      request.supplierPlanId,
      'supplierPlanId',
    );
    const productOfferId = requireUuid(
      request.productOfferId,
      'productOfferId',
    );

    const [plan, offer] = await Promise.all([
      this.repository.findPlan(supplierPlanId),
      this.catalogOfferReader.findOffer(productOfferId),
    ]);

    if (!plan) {
      throw new NotFoundException('Supplier plan was not found');
    }

    if (!offer) {
      throw new NotFoundException(
        'Canonical Product Offer was not found',
      );
    }

    const assessment = assessSupplierPlanMapping(plan, offer);

    if (!assessment.compatible) {
      throw new UnprocessableEntityException({
        statusCode: 422,
        error: 'Unprocessable Entity',
        code: 'SUPPLIER_PLAN_INCOMPATIBLE',
        assessment,
      });
    }

    try {
      const mapping = await this.repository.createMapping({
        supplierPlanId,
        productOfferId,
        assessment,
        actorIdentityId: requireUuid(
          actorIdentityId,
          'actorIdentityId',
        ),
      });

      if (!mapping) {
        throw new NotFoundException('Supplier plan was not found');
      }

      return { mapping };
    } catch (error) {
      if (isUniqueViolation(error)) {
        throw new ConflictException(
          'Supplier plan mapping already exists',
        );
      }

      throw error;
    }
  }

  async activateMapping(
    mappingId: string,
    actorIdentityId: string,
  ): Promise<SupplierPlanMappingTransitionResponse> {
    try {
      const result = await this.repository.activateMapping(
        requireUuid(mappingId, 'mappingId'),
        requireUuid(actorIdentityId, 'actorIdentityId'),
      );

      if (result.kind === 'NOT_FOUND') {
        throw new NotFoundException(
          'Supplier plan mapping was not found',
        );
      }

      if (result.kind === 'ENVIRONMENT_UNCONFIRMED') {
        throw new ConflictException({
          statusCode: 409,
          error: 'Conflict',
          code: 'SUPPLIER_ENVIRONMENT_NOT_CONFIRMED',
          message:
            'Production supplier contract must be probed before activation',
        });
      }

      return { mapping: result.mapping };
    } catch (error) {
      if (isUniqueViolation(error)) {
        throw new ConflictException(
          'An active Gigago mapping already exists for this Product Offer and environment',
        );
      }

      throw error;
    }
  }

  async listActiveMappings(
    productOfferId: string,
    environment: unknown,
  ): Promise<ListActiveSupplierPlanMappingsResponse> {
    return {
      items: await this.repository.listActiveMappings(
        requireUuid(productOfferId, 'productOfferId'),
        requireEnvironment(environment),
      ),
    };
  }
}
