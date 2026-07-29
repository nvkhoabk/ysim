export type CatalogLocale = 'en' | 'vi' | 'lo';
export type CatalogEntityStatus = 'ACTIVE' | 'SUSPENDED';
export type ProductKind = 'ESIM_DATA';
export type ProductOfferStatus = 'DRAFT' | 'PUBLISHED' | 'SUSPENDED';
export type DataPolicy = 'FIXED' | 'DAILY' | 'UNLIMITED';
export type ActivationPolicy =
  | 'FIRST_NETWORK_CONNECTION'
  | 'INSTALLATION';

export interface CatalogLocalizationInput {
  locale: CatalogLocale;
  name: string;
}

export interface ProductOfferLocalizationInput {
  locale: CatalogLocale;
  title: string;
  shortDescription?: string | null;
}

export interface RegionContract {
  id: string;
  code: string;
  status: CatalogEntityStatus;
  localizations: CatalogLocalizationInput[];
  createdAt: string;
}

export interface CreateRegionRequest {
  code: string;
  localizations: CatalogLocalizationInput[];
}

export interface CreateRegionResponse {
  region: RegionContract;
}

export interface DestinationContract {
  id: string;
  code: string;
  regionId: string;
  status: CatalogEntityStatus;
  localizations: CatalogLocalizationInput[];
  createdAt: string;
}

export interface CreateDestinationRequest {
  code: string;
  regionId: string;
  localizations: CatalogLocalizationInput[];
}

export interface CreateDestinationResponse {
  destination: DestinationContract;
}

export interface ProductContract {
  id: string;
  code: string;
  kind: ProductKind;
  createdAt: string;
}

export interface CreateProductRequest {
  code: string;
  kind: ProductKind;
}

export interface CreateProductResponse {
  product: ProductContract;
}

export interface ProductOfferContract {
  id: string;
  code: string;
  productId: string;
  productCode: string;
  status: ProductOfferStatus;
  durationDays: number;
  dataPolicy: DataPolicy;
  dataAmountMb: number | null;
  dailyDataAmountMb: number | null;
  fairUseDataAmountMb: number | null;
  activationPolicy: ActivationPolicy;
  hotspotSupported: boolean;
  phoneNumberIncluded: boolean;
  networkName: string;
  destinationIds: string[];
  localizations: ProductOfferLocalizationInput[];
  publishedAt: string | null;
  createdAt: string;
  updatedAt: string;
  version: number;
}

export interface CreateProductOfferRequest {
  code: string;
  productId: string;
  destinationIds: string[];
  durationDays: number;
  dataPolicy: DataPolicy;
  dataAmountMb?: number | null;
  dailyDataAmountMb?: number | null;
  fairUseDataAmountMb?: number | null;
  activationPolicy: ActivationPolicy;
  hotspotSupported: boolean;
  phoneNumberIncluded: boolean;
  networkName: string;
  localizations: ProductOfferLocalizationInput[];
}

export interface CreateProductOfferResponse {
  offer: ProductOfferContract;
}

export interface ProductOfferTransitionResponse {
  offer: ProductOfferContract;
}

export interface LocalizedDestinationContract {
  id: string;
  code: string;
  name: string;
  requestedLocale: CatalogLocale;
  sourceLocale: CatalogLocale;
}

export interface LocalizedProductOfferContract {
  id: string;
  code: string;
  productId: string;
  productCode: string;
  status: ProductOfferStatus;
  durationDays: number;
  dataPolicy: DataPolicy;
  dataAmountMb: number | null;
  dailyDataAmountMb: number | null;
  fairUseDataAmountMb: number | null;
  activationPolicy: ActivationPolicy;
  hotspotSupported: boolean;
  phoneNumberIncluded: boolean;
  networkName: string;
  title: string;
  shortDescription: string | null;
  requestedLocale: CatalogLocale;
  sourceLocale: CatalogLocale;
  destinations: LocalizedDestinationContract[];
  publishedAt: string | null;
  createdAt: string;
  updatedAt: string;
  version: number;
}

export interface ListProductOffersResponse {
  items: LocalizedProductOfferContract[];
}
