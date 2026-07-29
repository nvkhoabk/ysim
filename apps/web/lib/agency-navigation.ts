import type { AgencyPortalRole } from './agency-contracts';

import type { AgencyPortalLocale } from './agency-session';

export interface AgencyNavigationItem {
  id: 'dashboard' | 'orders' | 'references' | 'team';
  href: string;
  label: string;
}

const labels = {
  vi: {
    dashboard: 'Tổng quan',
    orders: 'Đơn hàng',
    references: 'Reference QR',
    team: 'Thành viên',
  },
  en: {
    dashboard: 'Dashboard',
    orders: 'Orders',
    references: 'Reference QR',
    team: 'Team',
  },
} as const;

export function agencyNavigation(
  role: AgencyPortalRole,
  locale: AgencyPortalLocale,
): AgencyNavigationItem[] {
  const dictionary = labels[locale];

  const common: AgencyNavigationItem[] = [
    {
      id: 'dashboard',
      href: '/agency',
      label: dictionary.dashboard,
    },
    {
      id: 'orders',
      href: '/agency/orders',
      label: dictionary.orders,
    },
    {
      id: 'references',
      href: '/agency/references',
      label: dictionary.references,
    },
  ];

  if (role === 'AGENCY_ADMIN') {
    common.push({
      id: 'team',
      href: '/agency/team',
      label: dictionary.team,
    });
  }

  return common;
}
