import {
  BadRequestException,
  ConflictException,
  ForbiddenException,
  Injectable,
  NotFoundException,
} from '@nestjs/common';
import type {
  ActivateAgencyResponse,
  CreateAgencyRequest,
  CreateAgencyResponse,
  GrantMembershipRequest,
  GrantMembershipResponse,
  OrganizationContextResponse,
} from '@ysim/contracts';

import {
  normalizeAgencyCode,
  normalizeOrganizationCode,
  optionalEmail,
  OrganizationPolicyError,
  requireMarket,
  requireMembershipRole,
  requireName,
  requireUuid,
} from '../domain/organization-policy.js';
import { OrganizationAgencyRepository } from '../infrastructure/organization-agency.repository.js';

const isUniqueViolation = (error: unknown): boolean =>
  typeof error === 'object' &&
  error !== null &&
  'code' in error &&
  error.code === '23505';

@Injectable()
export class OrganizationAgencyService {
  constructor(private readonly repository: OrganizationAgencyRepository) {}

  async createAgency(
    request: CreateAgencyRequest,
    actorIdentityId: string,
  ): Promise<CreateAgencyResponse> {
    try {
      return await this.repository.createAgency({
        organizationCode: normalizeOrganizationCode(request.organizationCode),
        agencyCode: normalizeAgencyCode(request.agencyCode),
        legalName: requireName(request.legalName, 'legalName'),
        displayName: requireName(request.displayName, 'displayName'),
        defaultMarket: requireMarket(request.defaultMarket),
        contactEmail: optionalEmail(request.contactEmail),
        actorIdentityId: requireUuid(actorIdentityId, 'actorIdentityId'),
      });
    } catch (error) {
      if (error instanceof OrganizationPolicyError) {
        throw new BadRequestException(error.message);
      }
      if (isUniqueViolation(error)) {
        throw new ConflictException('Organization code or agency code already exists');
      }
      throw error;
    }
  }

  async activateAgency(
    organizationId: string,
    actorIdentityId: string,
  ): Promise<ActivateAgencyResponse> {
    try {
      const organization = await this.repository.activateAgency(
        requireUuid(organizationId, 'organizationId'),
        requireUuid(actorIdentityId, 'actorIdentityId'),
      );

      if (!organization) {
        throw new NotFoundException('Agency organization was not found');
      }

      return { organization };
    } catch (error) {
      if (error instanceof OrganizationPolicyError) {
        throw new BadRequestException(error.message);
      }
      throw error;
    }
  }

  async grantMembership(
    organizationId: string,
    request: GrantMembershipRequest,
    actorIdentityId: string,
  ): Promise<GrantMembershipResponse> {
    try {
      const membership = await this.repository.grantMembership(
        requireUuid(organizationId, 'organizationId'),
        requireUuid(request.identityId, 'identityId'),
        requireMembershipRole(request.role),
        requireUuid(actorIdentityId, 'actorIdentityId'),
      );

      if (!membership) {
        throw new NotFoundException('Agency organization was not found');
      }

      return { membership };
    } catch (error) {
      if (error instanceof OrganizationPolicyError) {
        throw new BadRequestException(error.message);
      }
      if (isUniqueViolation(error)) {
        throw new ConflictException('Active membership already exists');
      }
      throw error;
    }
  }

  async resolveContext(
    organizationId: string,
    identityId: string,
  ): Promise<OrganizationContextResponse> {
    try {
      const context = await this.repository.resolveContext(
        requireUuid(organizationId, 'organizationId'),
        requireUuid(identityId, 'identityId'),
      );

      if (!context) {
        throw new ForbiddenException('Active organization membership is required');
      }

      return context;
    } catch (error) {
      if (error instanceof OrganizationPolicyError) {
        throw new BadRequestException(error.message);
      }
      throw error;
    }
  }
}
