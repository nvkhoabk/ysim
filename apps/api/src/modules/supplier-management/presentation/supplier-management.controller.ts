import { timingSafeEqual } from 'node:crypto';

import {
  Body,
  Controller,
  Get,
  Headers,
  HttpCode,
  Param,
  Post,
  Query,
  ServiceUnavailableException,
  UnauthorizedException,
} from '@nestjs/common';
import type {
  CreateSupplierPlanMappingRequest,
  CreateSupplierPlanMappingResponse,
  ImportGigagoPlanRequest,
  ImportGigagoPlanResponse,
  ListActiveSupplierPlanMappingsResponse,
  ListSupplierEnvironmentProfilesResponse,
  SupplierPlanMappingTransitionResponse,
} from '@ysim/contracts';

import { SupplierManagementService } from '../application/supplier-management.service.js';

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

function requiredHeader(
  headers: RequestHeaders,
  name: string,
): string {
  const value = singleHeader(headers, name);
  if (!value) {
    throw new UnauthorizedException(`${name} header is required`);
  }

  return value;
}

@Controller('internal/r1/suppliers/gigago')
export class SupplierManagementController {
  constructor(private readonly service: SupplierManagementService) {}

  @Get('environments')
  listEnvironments(
    @Headers() headers: RequestHeaders,
  ): Promise<ListSupplierEnvironmentProfilesResponse> {
    requireBootstrapToken(headers);
    return this.service.listGigagoEnvironments();
  }

  @Post('plans/import')
  importPlan(
    @Headers() headers: RequestHeaders,
    @Body() request: ImportGigagoPlanRequest,
  ): Promise<ImportGigagoPlanResponse> {
    requireBootstrapToken(headers);
    return this.service.importGigagoPlan(
      request,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Post('mappings')
  createMapping(
    @Headers() headers: RequestHeaders,
    @Body() request: CreateSupplierPlanMappingRequest,
  ): Promise<CreateSupplierPlanMappingResponse> {
    requireBootstrapToken(headers);
    return this.service.createMapping(
      request,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Post('mappings/:mappingId/activate')
  @HttpCode(200)
  activateMapping(
    @Headers() headers: RequestHeaders,
    @Param('mappingId') mappingId: string,
  ): Promise<SupplierPlanMappingTransitionResponse> {
    requireBootstrapToken(headers);
    return this.service.activateMapping(
      mappingId,
      requiredHeader(headers, 'x-ysim-actor-id'),
    );
  }

  @Get('mappings/by-offer/:productOfferId')
  listActiveMappings(
    @Headers() headers: RequestHeaders,
    @Param('productOfferId') productOfferId: string,
    @Query('environment') environment?: string,
  ): Promise<ListActiveSupplierPlanMappingsResponse> {
    requireBootstrapToken(headers);
    return this.service.listActiveMappings(
      productOfferId,
      environment,
    );
  }
}
