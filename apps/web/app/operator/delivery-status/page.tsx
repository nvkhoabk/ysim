import type { Metadata } from 'next';
import { readOperatorDeliveryStatus } from './operator-delivery-status';
import styles from './status.module.css';

export const metadata: Metadata = { title: 'Trạng thái giao eSIM' };
export const dynamic = 'force-dynamic';

export default async function OperatorDeliveryStatusPage() {
  const result = await readOperatorDeliveryStatus();
  return (
    <main className={styles.page}>
      <section className={styles.card} aria-labelledby="delivery-status-title">
        <p className={styles.eyebrow}>Vận hành nội bộ · chỉ đọc</p>
        <h1 id="delivery-status-title">Trạng thái giao eSIM</h1>
        {result.authorized ? (
          <dl className={styles.grid}>
            <div><dt>Trạng thái</dt><dd data-state={result.status.state}>{result.status.state}</dd></div>
            <div><dt>Lý do</dt><dd>{result.status.reason}</dd></div>
            <div><dt>Scheduler</dt><dd>{result.status.schedulerEnabled ? 'Đã bật' : 'Đã tắt'}</dd></div>
            <div><dt>Chế độ email</dt><dd>{result.status.emailMode}</dd></div>
          </dl>
        ) : (
          <div className={styles.notice} role="status">
            Không thể đọc trạng thái vận hành. Mã: <code>{result.reason}</code>
          </div>
        )}
        <p className={styles.caption}>Trang này không cung cấp thao tác thay đổi scheduler hoặc gửi email.</p>
      </section>
    </main>
  );
}
