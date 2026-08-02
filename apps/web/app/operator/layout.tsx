import type { ReactNode } from 'react';

import { resolveOperatorPortalAccess } from '../../lib/operator-access';
import { OperatorAccessState } from './operator-access-state';

export const dynamic = 'force-dynamic';

export default async function OperatorLayout({
  children,
}: Readonly<{ children: ReactNode }>) {
  const access = await resolveOperatorPortalAccess();

  if (!access.authorized) {
    return <OperatorAccessState reason={access.reason} />;
  }

  return children;
}
