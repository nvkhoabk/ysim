import type {
  DataPolicy,
  ProductOfferStatus,
} from './catalog.js';

export type SupplierCode = 'GIGAGO';
export type SupplierEnvironment = 'SANDBOX' | 'PRODUCTION';
export type SupplierStatus = 'ACTIVE' | 'SUSPENDED';
export type SupplierEnvironmentContractStatus =
  | 'PROBED'
  | 'DOCUMENTED_UNVERIFIED';
export type SupplierPlanStatus = 'ACTIVE' | 'SUSPENDED';
export type SupplierPlanMappingStatus =
  | 'DRAFT'
  | 'ACTIVE'
  | 'SUSPENDED';
export type SupplierHttpMethod = 'GET' | 'POST' | 'PUT';

export interface GigagoOperatorInput {
  country_code: string;
  networks: string[];
}

export interface GigagoPlanPayload {
  ggg_plan_id: string;
  apn?: string | null;
  price?: number | null;
  name: string;
  package_description?: string | null;
  hotspot: string;
  network_type?: string | null;
  phone_number: string;
  topup_extension?: string | null;
  data: string;
  validity: string;
  countries: string;
  operator?: string | null;
  parent_group_id?: string | null;
  parent_group_name?: string | null;
}

export interface SupplierOperatorNetworkContract {
  countryCode: string;
  networks: string[];
}

export interface SupplierEnvironmentProfileContract {
  supplierCode: SupplierCode;
  environment: SupplierEnvironment;
  baseUrl: string;
  credentialRef: string;
  contractStatus: SupplierEnvironmentContractStatus;
  getPackagesMethod: SupplierHttpMethod;
  createOrderMethod: SupplierHttpMethod;
  documentedGetMyOrdersMethod: SupplierHttpMethod;
  confirmedGetMyOrdersMethod: SupplierHttpMethod | null;
}

export interface ListSupplierEnvironmentProfilesResponse {
  items: SupplierEnvironmentProfileContract[];
}

export interface SupplierPlanContract {
  id: string;
  supplierCode: SupplierCode;
  environment: SupplierEnvironment;
  externalPlanId: string;
  name: string;
  parentGroupId: string | null;
  parentGroupName: string | null;
  apn: string | null;
  networkType: string | null;
  countryCodes: string[];
  operatorNetworks: SupplierOperatorNetworkContract[];
  dataPolicy: DataPolicy;
  dataAmountMb: number | null;
  dailyDataAmountMb: number | null;
  fairUseDataAmountMb: number | null;
  durationDays: number;
  hotspotSupported: boolean;
  phoneNumberIncluded: boolean;
  topupSupported: boolean;
  rawSnapshotHash: string;
  observedAt: string;
  status: SupplierPlanStatus;
  createdAt: string;
  updatedAt: string;
  version: number;
}

export interface ImportGigagoPlanRequest {
  environment: SupplierEnvironment;
  payload: GigagoPlanPayload;
  observedAt?: string;
}

export interface ImportGigagoPlanResponse {
  plan: SupplierPlanContract;
}

export type SupplierPlanMappingIssueCode =
  | 'OFFER_NOT_PUBLISHED'
  | 'DURATION_MISMATCH'
  | 'DATA_POLICY_MISMATCH'
  | 'DATA_AMOUNT_MISMATCH'
  | 'DAILY_DATA_AMOUNT_MISMATCH'
  | 'FAIR_USE_AMOUNT_MISMATCH'
  | 'MISSING_DESTINATION'
  | 'HOTSPOT_NOT_SUPPORTED'
  | 'PHONE_NUMBER_NOT_INCLUDED';

export type SupplierPlanMappingWarningCode =
  | 'EXTRA_DESTINATION'
  | 'ACTIVATION_POLICY_UNVERIFIED'
  | 'NETWORK_SELECTION_UNVERIFIED';

export interface SupplierPlanMappingIssueContract {
  code: SupplierPlanMappingIssueCode;
  message: string;
  expected?: unknown;
  observed?: unknown;
}

export interface SupplierPlanMappingWarningContract {
  code: SupplierPlanMappingWarningCode;
  message: string;
  expected?: unknown;
  observed?: unknown;
}

export interface SupplierPlanMappingAssessmentContract {
  compatible: boolean;
  issues: SupplierPlanMappingIssueContract[];
  warnings: SupplierPlanMappingWarningContract[];
}

export interface CatalogOfferForSupplierMappingContract {
  id: string;
  code: string;
  status: ProductOfferStatus;
  durationDays: number;
  dataPolicy: DataPolicy;
  dataAmountMb: number | null;
  dailyDataAmountMb: number | null;
  fairUseDataAmountMb: number | null;
  hotspotSupported: boolean;
  phoneNumberIncluded: boolean;
  destinationCodes: string[];
}

export interface SupplierPlanMappingContract {
  id: string;
  supplierPlanId: string;
  supplierCode: SupplierCode;
  environment: SupplierEnvironment;
  productOfferId: string;
  status: SupplierPlanMappingStatus;
  assessment: SupplierPlanMappingAssessmentContract;
  createdBy: string;
  createdAt: string;
  activatedAt: string | null;
  suspendedAt: string | null;
  version: number;
}

export interface CreateSupplierPlanMappingRequest {
  supplierPlanId: string;
  productOfferId: string;
}

export interface CreateSupplierPlanMappingResponse {
  mapping: SupplierPlanMappingContract;
}

export interface SupplierPlanMappingTransitionResponse {
  mapping: SupplierPlanMappingContract;
}

export interface ListActiveSupplierPlanMappingsResponse {
  items: SupplierPlanMappingContract[];
}
