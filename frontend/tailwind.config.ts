import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        surface: {
          DEFAULT: 'rgba(255, 255, 255, 0.72)',
          hover: 'rgba(255, 255, 255, 0.85)',
          active: 'rgba(255, 255, 255, 0.95)',
          border: 'rgba(226, 232, 240, 0.6)',
        },
        glass: {
          low: 'rgba(255, 255, 255, 0.55)',
          mid: 'rgba(255, 255, 255, 0.72)',
          high: 'rgba(255, 255, 255, 0.85)',
          border: 'rgba(226, 232, 240, 0.7)',
        },
        accent: {
          cyan: '#06B6D4',
          blue: '#3B82F6',
          emerald: '#10B981',
          amber: '#F59E0B',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
      },
      animation: {
        'pulse-glow': 'pulse-glow 2s ease-in-out infinite',
        'slide-up': 'slide-up 0.5s ease-out',
        'fade-in': 'fade-in 0.3s ease-out',
      },
      keyframes: {
        'pulse-glow': {
          '0%, 100%': { boxShadow: '0 0 20px rgba(6, 182, 212, 0.08)' },
          '50%': { boxShadow: '0 0 40px rgba(6, 182, 212, 0.15)' },
        },
        'slide-up': {
          '0%': { transform: 'translateY(16px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        'fade-in': {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
};

export default config;
