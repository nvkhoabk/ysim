import type { Metadata } from 'next';
import type { ReactNode } from 'react';

import './styles.css';

export const metadata: Metadata = {
  title: {
    default: 'YSim Platform',
    template: '%s | YSim Platform',
  },
  description: 'YSim Global eSIM Commerce and Distribution Platform',
};

export default function RootLayout({
  children,
}: Readonly<{ children: ReactNode }>) {
  return (
    <html lang="vi">
      <body>{children}</body>
    </html>
  );
}
