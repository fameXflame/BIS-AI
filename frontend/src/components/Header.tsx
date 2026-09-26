'use client';

import { motion } from 'framer-motion';
import { Menu, Sun, Moon } from 'lucide-react';

interface HeaderProps {
  onToggleSidebar: () => void;
  hasHistory: boolean;
  theme?: 'light' | 'dark';
  onToggleTheme?: () => void;
}

export default function Header({
  onToggleSidebar,
  hasHistory,
  theme = 'light',
  onToggleTheme,
}: HeaderProps) {
  return (
    <motion.header
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: 'easeOut' }}
      className="
        relative z-20 flex items-center justify-between
        px-3 sm:px-6 py-2.5 sm:py-4 w-full
      "
    >
      {/* Left: Menu Toggle + Top-Left Theme Switcher */}
      <div className="flex items-center gap-2">
        <button
          onClick={onToggleSidebar}
          className="
            w-8 h-8 sm:w-10 sm:h-10 rounded-full 
            bg-white/90 hover:bg-white dark:bg-black dark:hover:bg-neutral-900
            shadow-xs border border-slate-200/80 dark:border-neutral-800
            flex items-center justify-center 
            text-slate-700 hover:text-slate-900 dark:text-neutral-300 dark:hover:text-white
            transition-all duration-200 cursor-pointer hover:scale-105 active:scale-95
          "
          title="Menu & History"
          aria-label="Open History Menu"
        >
          <Menu size={16} className="sm:w-[18px] sm:h-[18px]" />
        </button>

        {onToggleTheme && (
          <button
            type="button"
            onClick={onToggleTheme}
            className="
              h-8 sm:h-10 px-2.5 sm:px-3 rounded-full
              bg-white/90 hover:bg-white dark:bg-black dark:hover:bg-neutral-900
              text-slate-700 dark:text-neutral-200 border border-slate-200/80 dark:border-neutral-800
              text-[11px] sm:text-[11.5px] font-semibold transition-all cursor-pointer shadow-xs hover:scale-105 active:scale-95
              flex items-center gap-1.5
            "
            title={`Switch to ${theme === 'light' ? 'Dark' : 'Light'} Mode`}
            aria-label="Toggle Dark/Light Mode"
          >
            {theme === 'light' ? (
              <>
                <Moon size={14} className="text-slate-700 shrink-0" />
                <span className="hidden sm:inline">Dark</span>
              </>
            ) : (
              <>
                <Sun size={14} className="text-amber-400 shrink-0" />
                <span className="hidden sm:inline">Light</span>
              </>
            )}
          </button>
        )}
      </div>

      {/* Right: National Identity & Tiranga Accent (Quotes hidden on mobile phone) */}
      <div className="flex items-center gap-2 sm:gap-2.5">
        <div className="text-right hidden sm:block">
          <span className="block text-[9px] sm:text-[9.5px] font-bold tracking-[0.2em] text-slate-500 dark:text-neutral-400 uppercase">
            TEAM ZENICX • SIH26108
          </span>
          <span className="block text-[9.5px] sm:text-[10px] font-extrabold tracking-[0.22em] text-slate-700 dark:text-neutral-200 uppercase">
            STANDARDS INTELLIGENCE
          </span>
        </div>
        {/* Tricolor badge line */}
        <div className="flex flex-col gap-[2px] justify-center pl-1">
          <div className="w-3.5 sm:w-4 h-[2px] rounded-full bg-[#FF9933]" />
          <div className="w-3.5 sm:w-4 h-[2px] rounded-full bg-white dark:bg-neutral-200 border-[0.5px] border-slate-200 dark:border-neutral-700" />
          <div className="w-3.5 sm:w-4 h-[2px] rounded-full bg-[#128807]" />
        </div>
      </div>
    </motion.header>
  );
}
