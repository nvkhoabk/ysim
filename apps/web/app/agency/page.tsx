import { cookies } from 'next/headers';

import { agencyNavigation } from '../../lib/agency-navigation';
import {
  AGENCY_SESSION_COOKIE,
  verifyAgencySessionToken,
} from '../../lib/agency-session';
import { resolveAgencyPortalContext } from '../../lib/ysim-platform';
import styles from './agency.module.css';

export const dynamic = 'force-dynamic';

const copy = {
  vi: {
    brand: 'YSim Agency Portal',
    signInRequired: 'Cần đăng nhập',
    signInMessage:
      'Phiên truy cập đại lý không hợp lệ hoặc đã hết hạn.',
    accessDenied: 'Không có quyền truy cập',
    accessDeniedMessage:
      'Tài khoản này không có quyền truy cập organization đã chọn.',
    organizationInactive: 'Organization chưa sẵn sàng',
    draftMessage:
      'Đại lý đang ở trạng thái khởi tạo. Vui lòng liên hệ YSim để kích hoạt.',
    suspendedMessage:
      'Đại lý đang bị tạm ngưng. Vui lòng liên hệ bộ phận vận hành YSim.',
    unavailable: 'Portal tạm thời không khả dụng',
    unavailableMessage:
      'Không thể xác minh organization context vào lúc này.',
    organization: 'Organization',
    role: 'Vai trò',
    market: 'Thị trường',
    welcome: 'Xin chào',
    emptyTitle: 'Portal đã sẵn sàng',
    emptyMessage:
      'Chưa có dữ liệu doanh thu, đơn hàng hoặc hoa hồng trong slice này.',
    revenue: 'Doanh thu',
    orders: 'Đơn hàng',
    commission: 'Hoa hồng',
    noData: 'Chưa có dữ liệu',
    status: 'Trạng thái',
  },
  en: {
    brand: 'YSim Agency Portal',
    signInRequired: 'Sign in required',
    signInMessage:
      'The agency access session is invalid or has expired.',
    accessDenied: 'Access denied',
    accessDeniedMessage:
      'This identity cannot access the selected organization.',
    organizationInactive: 'Organization unavailable',
    draftMessage:
      'The agency is still being prepared. Contact YSim for activation.',
    suspendedMessage:
      'The agency is suspended. Contact YSim Operations.',
    unavailable: 'Portal temporarily unavailable',
    unavailableMessage:
      'The organization context cannot be verified right now.',
    organization: 'Organization',
    role: 'Role',
    market: 'Market',
    welcome: 'Welcome',
    emptyTitle: 'Portal shell ready',
    emptyMessage:
      'Revenue, order and commission data are intentionally empty in this slice.',
    revenue: 'Revenue',
    orders: 'Orders',
    commission: 'Commission',
    noData: 'No data yet',
    status: 'Status',
  },
} as const;

function StatePanel({
  state,
  title,
  message,
  detail,
}: Readonly<{
  state: string;
  title: string;
  message: string;
  detail?: string;
}>) {
  return (
    <main className={styles.statePage} data-portal-state={state}>
      <section className={styles.stateCard}>
        <p className={styles.eyebrow}>YSim Agency Portal</p>
        <h1>{title}</h1>
        <p>{message}</p>
        {detail ? <p className={styles.detail}>{detail}</p> : null}
      </section>
    </main>
  );
}

export default async function AgencyPortalPage() {
  const sessionSecret = process.env.YSIM_PORTAL_SESSION_SECRET;
  if (!sessionSecret) {
    return (
      <StatePanel
        state="unavailable"
        title={copy.en.unavailable}
        message={copy.en.unavailableMessage}
        detail="Missing session configuration"
      />
    );
  }

  const cookieStore = await cookies();
  const token = cookieStore.get(AGENCY_SESSION_COOKIE)?.value;
  const session = verifyAgencySessionToken(token, sessionSecret);
  const locale = session?.locale ?? 'vi';
  const dictionary = copy[locale];

  if (!session) {
    return (
      <StatePanel
        state="unauthenticated"
        title={dictionary.signInRequired}
        message={dictionary.signInMessage}
      />
    );
  }

  const result = await resolveAgencyPortalContext(session);

  if (result.state === 'denied') {
    return (
      <StatePanel
        state="denied"
        title={dictionary.accessDenied}
        message={dictionary.accessDeniedMessage}
      />
    );
  }

  if (result.state === 'organization-inactive') {
    const suspended = result.organization.status === 'SUSPENDED';
    return (
      <StatePanel
        state={suspended ? 'suspended' : 'organization-inactive'}
        title={dictionary.organizationInactive}
        message={
          suspended
            ? dictionary.suspendedMessage
            : dictionary.draftMessage
        }
        detail={`${dictionary.status}: ${result.organization.status}`}
      />
    );
  }

  if (result.state === 'unavailable') {
    return (
      <StatePanel
        state="unavailable"
        title={dictionary.unavailable}
        message={dictionary.unavailableMessage}
        detail={result.reason}
      />
    );
  }

  const { organization, membership } = result.context;
  const navigation = agencyNavigation(membership.role, locale);

  return (
    <main className={styles.portal} data-portal-state="ready">
      <aside className={styles.sidebar}>
        <div>
          <p className={styles.eyebrow}>{dictionary.brand}</p>
          <h1 className={styles.organizationName}>
            {organization.displayName}
          </h1>
          <p className={styles.organizationCode}>
            {organization.code}
          </p>
        </div>

        <nav aria-label="Agency navigation">
          <ul className={styles.navigation}>
            {navigation.map((item, index) => (
              <li key={item.id}>
                <a
                  aria-current={index === 0 ? 'page' : undefined}
                  className={index === 0 ? styles.activeLink : undefined}
                  href={item.href}
                >
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        </nav>

        <dl className={styles.identity}>
          <div>
            <dt>{dictionary.role}</dt>
            <dd data-portal-role={membership.role}>
              {membership.role}
            </dd>
          </div>
          <div>
            <dt>{dictionary.market}</dt>
            <dd>{organization.defaultMarket}</dd>
          </div>
        </dl>
      </aside>

      <section className={styles.content}>
        <header className={styles.header}>
          <div>
            <p className={styles.eyebrow}>{dictionary.welcome}</p>
            <h2>{organization.displayName}</h2>
          </div>
          <span className={styles.statusBadge}>
            {organization.status}
          </span>
        </header>

        <section className={styles.emptyState}>
          <h3>{dictionary.emptyTitle}</h3>
          <p>{dictionary.emptyMessage}</p>
        </section>

        <section
          aria-label="Agency dashboard placeholders"
          className={styles.metrics}
        >
          {[
            dictionary.revenue,
            dictionary.orders,
            dictionary.commission,
          ].map((label) => (
            <article className={styles.metricCard} key={label}>
              <p>{label}</p>
              <strong>—</strong>
              <span>{dictionary.noData}</span>
            </article>
          ))}
        </section>
      </section>
    </main>
  );
}
