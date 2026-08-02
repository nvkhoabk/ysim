import type { ReactNode } from 'react';

export const dynamic = 'force-dynamic';

export default async function OperatorLayout({
  children,
}: Readonly<{ children: ReactNode }>) {
  return children;
}
