import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'BIS-AI | Indian Standards Intelligence Engine (SIH26108)',
  description: 'AI-native Indian Standards search engine indexing 22,446 national standards with sub-600ms hybrid retrieval and clause verification.',
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
