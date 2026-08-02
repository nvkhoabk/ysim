import styles from './operator-access.module.css';

const copy = {
  CONFIG_INVALID: {
    title: 'Portal tạm thời không khả dụng',
    message: 'Không thể xác minh phiên vận hành vào lúc này.',
  },
  SESSION_REQUIRED: {
    title: 'Cần đăng nhập',
    message: 'Cần có phiên operator hợp lệ để truy cập khu vực vận hành.',
  },
  SESSION_INVALID: {
    title: 'Phiên truy cập không hợp lệ',
    message: 'Phiên operator không hợp lệ hoặc đã hết hạn.',
  },
} as const;

export type OperatorAccessFailureReason = keyof typeof copy;

export function OperatorAccessState({
  reason,
}: Readonly<{ reason: OperatorAccessFailureReason }>) {
  const state = copy[reason];

  return (
    <main className={styles.page} data-operator-access="denied">
      <section className={styles.card} role="status">
        <p className={styles.eyebrow}>YSim Operator Portal</p>
        <h1>{state.title}</h1>
        <p>{state.message}</p>
        <p className={styles.reference}>Mã tham chiếu: {reason}</p>
      </section>
    </main>
  );
}
