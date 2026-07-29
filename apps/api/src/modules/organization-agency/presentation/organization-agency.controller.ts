import { timingSafeEqual } from 'node:crypto';

import {
  Body,
  Controller,
  Get,
  Headers,
  HttpCode,
  Param,
  Post,
  ServiceUnavailableException,
  UnauthorizedException,
} from '@nestjs/common';
import type {
  ActivateAgencyResponse,
  AgencyPortalContextResponse,
  CreateAgencyRequest,
  CreateAgencyResponse,
  GrantMembershipRequest,
  GrantMembershipResponse,
  OrganizationContextResponse,
  SuspendAgencyResponse,
} from '@ysim/contracts';

import { OrganizationAgencyService } from '../application/organization-agency.service.js';

type RequestHeaders = Record<string, string | string[] | undefined>;

function singleHeader(
  headers: RequestHeaders,
  name: string,
): string | undefined {
  const value = headers[name];
  return Array.isArray(value) ? value[0] : value;
}

function requireBootstrapToken(headers: RequestHeaders): void {
  const configured = process.env.YSIM_BOOTSTRAP_TOKEN;
  if (!configured || configured.length < 24) {
    throw new ServiceUnavailableException(
      'YSIM_BOOTSTRAP_TOKEN must be configured with at least 24 characters',
    );
  }

  const supplied = singleHeader(headers, 'x-ysim-bootstrap-token');
  if (!supplied) {
    throw new UnauthorizedException('Bootstrap token is required');
  }

  const configuredBuffer = Buffer.from(configured);
  const suppliedBuffer = Buffer.from(supplied);
  if (
    configuredBuffer.length !== suppliedBuffer.length ||
    !timingSafeEqual(configuredBuffer, suppliedBuffer)
  ) {
    throw new UnauthorizedException('Bootstrap token is invalid');
  }
}

function requiredHeader(headers: RequestHeaders, name: string): string {
  const value = singleHeader(headers, name);
  if (!value) {
    throw new UnauthorizedException(`${name} header is required`);
  }
  return value;
}

@Controller('internal/r1/organizations')
export class OrganizationAgencyController {
  constructor(private readonly service: OrganizationAgencyService) {}

  @Post('agencies')
  createAgency(
    @Headers() headers: RequestHeaders,
    @Body() request: CreateAgencyRequest,
  ): Promise<CreateAgencyResponse> {
    requireBootstrapToken(headers);
    return this.service.createAgency(
      request,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Post(':organizationId/activate')
  @HttpCode(200)
  activateAgency(
    @Headers() headers: RequestHeaders,
    @Param('organizationId') organizationId: string,
  ): Promise<ActivateAgencyResponse> {
    requireBootstrapToken(headers);
    return this.service.activateAgency(
      organizationId,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Post(':organizationId/suspend')
  @HttpCode(200)
  suspendAgency(
    @Headers() headers: RequestHeaders,
    @Param('organizationId') organizationId: string,
  ): Promise<SuspendAgencyResponse> {
    requireBootstrapToken(headers);
    return this.service.suspendAgency(
      organizationId,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Post(':organizationId/memberships')
  grantMembership(
    @Headers() headers: RequestHeaders,
    @Param('organizationId') organizationId: string,
    @Body() request: GrantMembershipRequest,
  ): Promise<GrantMembershipResponse> {
    requireBootstrapToken(headers);
    return this.service.grantMembership(
      organizationId,
      request,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Get('context')
  resolveContext(
    @Headers() headers: RequestHeaders,
  ): Promise<OrganizationContextResponse> {
    requireBootstrapToken(headers);
    return this.service.resolveContext(
      requiredHeader(headers, 'x-ysim-organization-id'),
      requiredHeader(headers, 'x-ysim-identity-id'),
    );
  }

  @Get('portal-context')
  resolvePortalContext(
    @Headers() headers: RequestHeaders,
  ): Promise<AgencyPortalContextResponse> {
    requireBootstrapToken(headers);
    return this.service.resolvePortalContext(
      requiredHeader(headers, 'x-ysim-organization-id'),
      requiredHeader(headers, 'x-ysim-identity-id'),
    );
  }
}
