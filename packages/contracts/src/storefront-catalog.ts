export type StorefrontCatalogLocale = 'en' | 'vi' | 'lo';
export type StorefrontSupplierEnvironment =
  | 'SANDBOX'
  | 'PRODUCTION';

export interface StorefrontCatalogDestinationContract {
  code: string;
  regionCode: string;
  name: string;
  requestedLocale: StorefrontCatalogLocale;
  sourceLocale: StorefrontCatalogLocale;
  availableOfferCount: number;
}

export interface StorefrontCatalogOfferDestinationContract {
  code: string;
  name: string;
  requestedLocale: StorefrontCatalogLocale;
  sourceLocale: StorefrontCatalogLocale;
}

export interface StorefrontCatalogOfferContract {
  code: string;
  productCode: string;
  durationDays: number;
  dataPolicy: 'FIXED' | 'DAILY' | 'UNLIMITED';
  dataAmountMb: number | null;
  dailyDataAmountMb: number | null;
  fairUseDataAmountMb: number | null;
  activationPolicy:
    | 'FIRST_NETWORK_CONNECTION'
    | 'INSTALLATION';
  hotspotSupported: boolean;
  phoneNumberIncluded: boolean;
  networkName: string;
  title: string;
  shortDescription: string | null;
  requestedLocale: StorefrontCatalogLocale;
  sourceLocale: StorefrontCatalogLocale;
  destinations: StorefrontCatalogOfferDestinationContract[];
  catalogVersion: number;
}

export interface ListStorefrontDestinationsResponse {
  items: StorefrontCatalogDestinationContract[];
}

export interface ListStorefrontOffersResponse {
  items: StorefrontCatalogOfferContract[];
}
