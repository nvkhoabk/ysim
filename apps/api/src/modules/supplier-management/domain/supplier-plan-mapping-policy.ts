import type {
  CatalogOfferForSupplierMappingContract,
  SupplierPlanContract,
  SupplierPlanMappingAssessmentContract,
  SupplierPlanMappingIssueContract,
  SupplierPlanMappingWarningContract,
} from '@ysim/contracts';

function issue(
  code: SupplierPlanMappingIssueContract['code'],
  message: string,
  expected?: unknown,
  observed?: unknown,
): SupplierPlanMappingIssueContract {
  return { code, message, expected, observed };
}

function warning(
  code: SupplierPlanMappingWarningContract['code'],
  message: string,
  expected?: unknown,
  observed?: unknown,
): SupplierPlanMappingWarningContract {
  return { code, message, expected, observed };
}

function sameNullableNumber(
  left: number | null,
  right: number | null,
): boolean {
  return left === right;
}

export function assessSupplierPlanMapping(
  plan: SupplierPlanContract,
  offer: CatalogOfferForSupplierMappingContract,
): SupplierPlanMappingAssessmentContract {
  const issues: SupplierPlanMappingIssueContract[] = [];
  const warnings: SupplierPlanMappingWarningContract[] = [];

  if (offer.status !== 'PUBLISHED') {
    issues.push(
      issue(
        'OFFER_NOT_PUBLISHED',
        'Canonical Product Offer must be published before mapping',
        'PUBLISHED',
        offer.status,
      ),
    );
  }

  if (offer.durationDays !== plan.durationDays) {
    issues.push(
      issue(
        'DURATION_MISMATCH',
        'Supplier validity must equal canonical offer duration',
        offer.durationDays,
        plan.durationDays,
      ),
    );
  }

  if (offer.dataPolicy !== plan.dataPolicy) {
    issues.push(
      issue(
        'DATA_POLICY_MISMATCH',
        'Supplier data policy must equal canonical offer data policy',
        offer.dataPolicy,
        plan.dataPolicy,
      ),
    );
  } else if (
    offer.dataPolicy === 'FIXED' &&
    !sameNullableNumber(offer.dataAmountMb, plan.dataAmountMb)
  ) {
    issues.push(
      issue(
        'DATA_AMOUNT_MISMATCH',
        'Supplier fixed allowance must equal canonical offer allowance',
        offer.dataAmountMb,
        plan.dataAmountMb,
      ),
    );
  } else if (
    offer.dataPolicy === 'DAILY' &&
    !sameNullableNumber(
      offer.dailyDataAmountMb,
      plan.dailyDataAmountMb,
    )
  ) {
    issues.push(
      issue(
        'DAILY_DATA_AMOUNT_MISMATCH',
        'Supplier daily allowance must equal canonical offer allowance',
        offer.dailyDataAmountMb,
        plan.dailyDataAmountMb,
      ),
    );
  } else if (
    offer.dataPolicy === 'UNLIMITED' &&
    !sameNullableNumber(
      offer.fairUseDataAmountMb,
      plan.fairUseDataAmountMb,
    )
  ) {
    issues.push(
      issue(
        'FAIR_USE_AMOUNT_MISMATCH',
        'Supplier fair-use allowance must equal canonical offer policy',
        offer.fairUseDataAmountMb,
        plan.fairUseDataAmountMb,
      ),
    );
  }

  const expectedDestinations = [...new Set(offer.destinationCodes)]
    .map((code) => code.toUpperCase())
    .sort();
  const observedDestinations = [...new Set(plan.countryCodes)]
    .map((code) => code.toUpperCase())
    .sort();

  for (const destination of expectedDestinations) {
    if (!observedDestinations.includes(destination)) {
      issues.push(
        issue(
          'MISSING_DESTINATION',
          `Supplier plan does not cover ${destination}`,
          destination,
          observedDestinations,
        ),
      );
    }
  }

  const extraDestinations = observedDestinations.filter(
    (destination) => !expectedDestinations.includes(destination),
  );

  if (extraDestinations.length > 0) {
    warnings.push(
      warning(
        'EXTRA_DESTINATION',
        'Supplier plan covers additional destinations not advertised by the canonical offer',
        expectedDestinations,
        extraDestinations,
      ),
    );
  }

  if (offer.hotspotSupported && !plan.hotspotSupported) {
    issues.push(
      issue(
        'HOTSPOT_NOT_SUPPORTED',
        'Canonical offer promises hotspot but supplier plan does not support it',
        true,
        false,
      ),
    );
  }

  if (offer.phoneNumberIncluded && !plan.phoneNumberIncluded) {
    issues.push(
      issue(
        'PHONE_NUMBER_NOT_INCLUDED',
        'Canonical offer promises a phone number but supplier plan does not include one',
        true,
        false,
      ),
    );
  }

  warnings.push(
    warning(
      'ACTIVATION_POLICY_UNVERIFIED',
      'Gigago package metadata does not prove the canonical activation policy',
    ),
  );

  warnings.push(
    warning(
      'NETWORK_SELECTION_UNVERIFIED',
      'Operator metadata is retained but network selection is not a blocking compatibility rule in VS-R1-004',
      offer.destinationCodes,
      plan.operatorNetworks,
    ),
  );

  return {
    compatible: issues.length === 0,
    issues,
    warnings,
  };
}
