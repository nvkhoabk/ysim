'use client';

import styles from './agency.module.css';

export default function AgencyPortalError({
  reset,
}: Readonly<{ reset: () => void }>) {
  return (
    <main
      className={styles.statePage}
      data-portal-state="error"
      role="alert"
    >
      <section className={styles.stateCard}>
        <p className={styles.eyebrow}>YSim Agency Portal</p>
        <h1>Portal shell unavailable</h1>
        <p>The agency shell encountered an unexpected error.</p>
        <button className={styles.retryButton} onClick={reset} type="button">
          Retry
        </button>
      </section>
    </main>
  );
}
