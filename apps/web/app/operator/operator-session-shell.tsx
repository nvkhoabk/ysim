import type { ReactNode } from 'react';

import type { OperatorPortalRole } from '../../lib/operator-session';
import styles from './operator-session-shell.module.css';

export function OperatorSessionShell({
  children,
  role,
}: Readonly<{ children: ReactNode; role: OperatorPortalRole }>) {
  return (
    <div className={styles.shell} data-operator-authenticated="true">
      <header className={styles.bar}>
        <p>
          Phiên vận hành · <strong>{role}</strong>
        </p>
        <form action="/operator/logout" method="post">
          <button type="submit">Đăng xuất</button>
        </form>
      </header>
      {children}
    </div>
  );
}
