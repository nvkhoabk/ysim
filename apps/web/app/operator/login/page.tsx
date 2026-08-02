import type { Metadata } from 'next';
import { redirect } from 'next/navigation';

import { resolveOperatorPortalAccess } from '../../../lib/operator-access';
import styles from './login.module.css';

export const metadata: Metadata = { title: 'Đăng nhập vận hành' };
export const dynamic = 'force-dynamic';

const messages = {
  INVALID_CREDENTIALS: 'Thông tin đăng nhập không hợp lệ.',
  RETRY_LATER: 'Có quá nhiều lần thử. Vui lòng đợi rồi thử lại.',
  UNAVAILABLE: 'Đăng nhập tạm thời không khả dụng.',
  SIGNED_OUT: 'Bạn đã đăng xuất an toàn.',
} as const;

type LoginMessage = keyof typeof messages;

function knownMessage(value: string | undefined): LoginMessage | null {
  return value && value in messages ? (value as LoginMessage) : null;
}

function safeNext(value: string | undefined): string {
  return value?.startsWith('/operator/') && !value.startsWith('//')
    ? value
    : '/operator/delivery-status';
}

export default async function OperatorLoginPage({
  searchParams,
}: Readonly<{
  searchParams: Promise<{
    error?: string;
    next?: string;
    state?: string;
  }>;
}>) {
  const access = await resolveOperatorPortalAccess();
  if (access.authorized) redirect('/operator/delivery-status');

  const params = await searchParams;
  const messageKey = knownMessage(params.error) ?? knownMessage(params.state);
  const nextPath = safeNext(params.next);

  return (
    <main className={styles.page} data-operator-login="ready">
      <section className={styles.card}>
        <p className={styles.eyebrow}>YSim Operator Portal</p>
        <h1>Đăng nhập vận hành</h1>
        <p className={styles.lead}>
          Khu vực nội bộ dành cho tài khoản Platform Admin và Operations.
        </p>

        {messageKey ? (
          <p
            className={
              messageKey === 'SIGNED_OUT' ? styles.success : styles.error
            }
            role="status"
          >
            {messages[messageKey]}
          </p>
        ) : null}

        <form action="/api/operator/session" method="post">
          <input name="next" type="hidden" value={nextPath} />
          <label>
            <span>Tài khoản</span>
            <input
              autoCapitalize="none"
              autoComplete="username"
              maxLength={128}
              name="loginId"
              required
              spellCheck={false}
              type="text"
            />
          </label>
          <label>
            <span>Mật khẩu</span>
            <input
              autoComplete="current-password"
              maxLength={256}
              name="password"
              required
              type="password"
            />
          </label>
          <button type="submit">Đăng nhập</button>
        </form>

        <p className={styles.notice}>
          Không có chức năng đăng ký công khai hoặc khôi phục mật khẩu trên
          portal này.
        </p>
      </section>
    </main>
  );
}
