'use client';

export default function ErrorState({ reset }: Readonly<{ reset: () => void }>) {
  return (
    <main role="alert">
      <h1>Commissioning shell unavailable</h1>
      <button type="button" onClick={reset}>Retry process check</button>
    </main>
  );
}
