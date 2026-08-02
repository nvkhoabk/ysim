import type { ReactNode } from 'react';

import { resolveOperatorPortalAccess } from '../../../lib/operator-access';
import { OperatorAccessState } from '../operator-access-state';
import { OperatorSessionShell } from '../operator-session-shell';

export const dynamic = 'force-dynamic';

export default async function ProtectedOperatorLayout({
  children,
}: Readonly<{ children: ReactNode }>) {
  const access = await resolveOperatorPortalAccess();
  if (!access.authorized) {
    return <OperatorAccessState reason={access.reason} />;
  }

  return (
    <OperatorSessionShell role={access.session.role}>
      {children}
    </OperatorSessionShell>
  );
}
