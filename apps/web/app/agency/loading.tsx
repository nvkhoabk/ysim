import styles from './agency.module.css';

export default function AgencyPortalLoading() {
  return (
    <main
      aria-live="polite"
      className={styles.statePage}
      data-portal-state="loading"
    >
      <section className={styles.stateCard}>
        <p className={styles.eyebrow}>YSim Agency Portal</p>
        <h1>Loading organization context…</h1>
      </section>
    </main>
  );
}
