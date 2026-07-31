import type { Metadata } from 'next';
import { readOperatorDeliveryOperationsSummary } from './operator-delivery-operations-summary';
import { readOperatorDeliveryStatus } from './operator-delivery-status';
import styles from './status.module.css';

export const metadata: Metadata = { title: 'Trạng thái giao eSIM' };
export const dynamic = 'force-dynamic';

const formatTimestamp = (value: string) =>
  new Intl.DateTimeFormat('vi-VN', {
    dateStyle: 'short',
    timeStyle: 'medium',
    timeZone: 'Asia/Ho_Chi_Minh',
  }).format(new Date(value));

export default async function OperatorDeliveryStatusPage() {
  const [runtime, operations] = await Promise.all([
    readOperatorDeliveryStatus(),
    readOperatorDeliveryOperationsSummary(),
  ]);

  return (
    <main className={styles.page}>
      <div className={styles.shell}>
        <header className={styles.header}>
          <p className={styles.eyebrow}>Vận hành nội bộ · chỉ đọc</p>
          <h1 id="delivery-status-title">Trạng thái giao eSIM</h1>
          <p className={styles.lead}>
            Theo dõi trạng thái runtime và khối lượng yêu cầu giao eSIM mà không
            cung cấp thao tác thay đổi hệ thống.
          </p>
        </header>

        <section className={styles.card} aria-labelledby="runtime-status-title">
          <div className={styles.sectionHeading}>
            <div>
              <p className={styles.kicker}>Runtime</p>
              <h2 id="runtime-status-title">Trạng thái hệ thống</h2>
            </div>
            <span className={styles.readOnlyBadge}>Chỉ đọc</span>
          </div>
          {runtime.authorized ? (
            <dl className={styles.grid}>
              <div><dt>Trạng thái</dt><dd data-state={runtime.status.state}>{runtime.status.state}</dd></div>
              <div><dt>Lý do</dt><dd>{runtime.status.reason}</dd></div>
              <div><dt>Scheduler</dt><dd>{runtime.status.schedulerEnabled ? 'Đã bật' : 'Đã tắt'}</dd></div>
              <div><dt>Chế độ email</dt><dd>{runtime.status.emailMode}</dd></div>
            </dl>
          ) : (
            <div className={styles.notice} role="status">
              Không thể đọc trạng thái runtime. Mã: <code>{runtime.reason}</code>
            </div>
          )}
        </section>

        <section className={styles.card} aria-labelledby="operations-summary-title">
          <div className={styles.sectionHeading}>
            <div>
              <p className={styles.kicker}>Delivery operations</p>
              <h2 id="operations-summary-title">Tổng hợp vận hành</h2>
            </div>
            {operations.authorized && operations.available ? (
              <p className={styles.generatedAt}>
                Cập nhật{' '}
                <time dateTime={operations.summary.generatedAt}>
                  {formatTimestamp(operations.summary.generatedAt)}
                </time>
              </p>
            ) : null}
          </div>

          {operations.authorized && operations.available ? (
            <>
              <dl className={styles.metrics}>
                <div data-tone="pending"><dt>Đang chờ</dt><dd>{operations.summary.pending}</dd></div>
                <div data-tone="failed"><dt>Thất bại</dt><dd>{operations.summary.failed}</dd></div>
                <div data-tone="published"><dt>Đã gửi</dt><dd>{operations.summary.published}</dd></div>
                <div data-tone="in-flight"><dt>Đang xử lý</dt><dd>{operations.summary.inFlight}</dd></div>
                <div data-tone="actionable"><dt>Có thể xử lý</dt><dd>{operations.summary.actionable}</dd></div>
              </dl>
              <div className={styles.oldestActionable}>
                <span>Yêu cầu cũ nhất cần xử lý</span>
                {operations.summary.oldestActionableAt ? (
                  <time dateTime={operations.summary.oldestActionableAt}>
                    {formatTimestamp(operations.summary.oldestActionableAt)}
                  </time>
                ) : (
                  <strong>Không có</strong>
                )}
              </div>
            </>
          ) : (
            <div className={styles.notice} role="status">
              Không thể đọc tổng hợp vận hành. Mã:{' '}
              <code>{operations.reason}</code>
            </div>
          )}
        </section>

        <p className={styles.caption}>
          Trang này không cung cấp thao tác thay đổi scheduler, xử lý lại yêu cầu
          hoặc gửi email.
        </p>
      </div>
    </main>
  );
}
