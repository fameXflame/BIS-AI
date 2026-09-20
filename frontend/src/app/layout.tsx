import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'BIS AI',
  description: 'AI-powered Bureau of Indian Standards search engine with semantic understanding',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
