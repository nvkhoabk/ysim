import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import { describe, expect, it } from 'vitest';

import type {
  CatalogOfferForSupplierMappingContract,
  GigagoPlanPayload,
  SupplierPlanContract,
} from '../../packages/contracts/src/index.js';
import {
  GigagoPlanNormalizationError,
  normalizeGigagoPlan,
  toSupplierPlanContract,
} from '../../apps/api/src/modules/supplier-management/domain/gigago-plan-normalizer.js';
import { assessSupplierPlanMapping } from '../../apps/api/src/modules/supplier-management/domain/supplier-plan-mapping-policy.js';

const currentDir = dirname(fileURLToPath(import.meta.url));
const fixtures = JSON.parse(
  readFileSync(
    resolve(currentDir, 'fixtures/gigago-plans.json'),
    'utf8',
  ),
) as Record<string, GigagoPlanPayload>;

function contract(
  fixture: GigagoPlanPayload,
): SupplierPlanContract {
  return toSupplierPlanContract(
    normalizeGigagoPlan(
      fixture,
      'SANDBOX',
      '2026-07-30T00:00:00.000Z',
    ),
    {
      id: '30000000-0000-4000-8000-000000000001',
      createdAt: '2026-07-30T00:00:00.000Z',
      updatedAt: '2026-07-30T00:00:00.000Z',
      version: 1,
    },
  );
}

function offer(
  overrides: Partial<CatalogOfferForSupplierMappingContract> = {},
): CatalogOfferForSupplierMappingContract {
  return {
    id: '40000000-0000-4000-8000-000000000001',
    code: 'JP_FIXED_5GB_7D',
    status: 'PUBLISHED',
    durationDays: 7,
    dataPolicy: 'FIXED',
    dataAmountMb: 5120,
    dailyDataAmountMb: null,
    fairUseDataAmountMb: null,
    hotspotSupported: true,
    phoneNumberIncluded: false,
    destinationCodes: ['JP'],
    ...overrides,
  };
}

describe('Gigago plan normalization', () => {
  it('normalizes a fixed-data plan', () => {
    const plan = contract(fixtures.japanFixed);

    expect(plan.externalPlanId).toBe('GIGA-JP-5GB-7D-TEST');
    expect(plan.dataPolicy).toBe('FIXED');
    expect(plan.dataAmountMb).toBe(5120);
    expect(plan.durationDays).toBe(7);
    expect(plan.countryCodes).toEqual(['JP']);
    expect(plan.hotspotSupported).toBe(true);
  });

  it('normalizes a daily-data plan', () => {
    const plan = contract(fixtures.asiaDaily);

    expect(plan.dataPolicy).toBe('DAILY');
    expect(plan.dailyDataAmountMb).toBe(1024);
    expect(plan.countryCodes).toEqual(['JP', 'KR', 'SG']);
  });

  it('normalizes an unlimited plan', () => {
    const plan = contract(fixtures.unlimited);

    expect(plan.dataPolicy).toBe('UNLIMITED');
    expect(plan.dataAmountMb).toBeNull();
    expect(plan.dailyDataAmountMb).toBeNull();
  });

  it('accepts the documented zero-data sandbox demo plan', () => {
    const plan = contract(fixtures.demo);

    expect(plan.dataPolicy).toBe('FIXED');
    expect(plan.dataAmountMb).toBe(0);
    expect(plan.durationDays).toBe(1);
    expect(plan.countryCodes).toEqual(['VN']);
  });

  it('rejects malformed country JSON', () => {
    expect(() =>
      normalizeGigagoPlan(
        {
          ...fixtures.japanFixed,
          countries: 'not-json',
        },
        'SANDBOX',
      ),
    ).toThrow(GigagoPlanNormalizationError);
  });

  it('rejects an unsupported data format', () => {
    expect(() =>
      normalizeGigagoPlan(
        {
          ...fixtures.japanFixed,
          data: '5 gigabytes',
        },
        'SANDBOX',
      ),
    ).toThrow('Unsupported Gigago data format');
  });
});

describe('supplier plan mapping policy', () => {
  it('accepts a matching published offer', () => {
    const assessment = assessSupplierPlanMapping(
      contract(fixtures.japanFixed),
      offer(),
    );

    expect(assessment.compatible).toBe(true);
    expect(assessment.issues).toEqual([]);
    expect(
      assessment.warnings.map((item) => item.code),
    ).toEqual([
      'ACTIVATION_POLICY_UNVERIFIED',
      'NETWORK_SELECTION_UNVERIFIED',
    ]);
  });

  it('rejects a draft canonical offer', () => {
    const assessment = assessSupplierPlanMapping(
      contract(fixtures.japanFixed),
      offer({ status: 'DRAFT' }),
    );

    expect(assessment.compatible).toBe(false);
    expect(
      assessment.issues.map((item) => item.code),
    ).toContain('OFFER_NOT_PUBLISHED');
  });

  it('rejects duration and data mismatches', () => {
    const assessment = assessSupplierPlanMapping(
      contract(fixtures.demo),
      offer(),
    );

    const codes = assessment.issues.map((item) => item.code);
    expect(codes).toContain('DURATION_MISMATCH');
    expect(codes).toContain('DATA_AMOUNT_MISMATCH');
    expect(codes).toContain('MISSING_DESTINATION');
  });

  it('rejects a missing hotspot capability', () => {
    const plan = {
      ...contract(fixtures.japanFixed),
      hotspotSupported: false,
    };

    const assessment = assessSupplierPlanMapping(plan, offer());

    expect(
      assessment.issues.map((item) => item.code),
    ).toContain('HOTSPOT_NOT_SUPPORTED');
  });

  it('rejects a missing phone number capability', () => {
    const assessment = assessSupplierPlanMapping(
      contract(fixtures.japanFixed),
      offer({ phoneNumberIncluded: true }),
    );

    expect(
      assessment.issues.map((item) => item.code),
    ).toContain('PHONE_NUMBER_NOT_INCLUDED');
  });

  it('reports extra supplier destinations as warnings', () => {
    const assessment = assessSupplierPlanMapping(
      contract(fixtures.asiaDaily),
      offer({
        durationDays: 10,
        dataPolicy: 'DAILY',
        dataAmountMb: null,
        dailyDataAmountMb: 1024,
      }),
    );

    expect(assessment.compatible).toBe(true);
    expect(
      assessment.warnings.map((item) => item.code),
    ).toContain('EXTRA_DESTINATION');
  });
});
