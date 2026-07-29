import { describe, expect, it } from 'vitest';

import { agencyNavigation } from '../../apps/web/lib/agency-navigation';

describe('agency navigation', () => {
  it('shows team management only to agency administrators', () => {
    const adminItems = agencyNavigation('AGENCY_ADMIN', 'en');
    const userItems = agencyNavigation('AGENCY_USER', 'en');

    expect(adminItems.map((item) => item.id)).toContain('team');
    expect(userItems.map((item) => item.id)).not.toContain('team');
  });

  it('provides Vietnamese labels', () => {
    const items = agencyNavigation('AGENCY_ADMIN', 'vi');

    expect(items.find((item) => item.id === 'dashboard')?.label).toBe(
      'Tổng quan',
    );
    expect(items.find((item) => item.id === 'team')?.label).toBe(
      'Thành viên',
    );
  });
});
