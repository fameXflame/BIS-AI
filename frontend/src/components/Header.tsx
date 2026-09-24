'use client';

import { motion } from 'framer-motion';
import { Menu } from 'lucide-react';

interface HeaderProps {
  onToggleSidebar: () => void;
  hasHistory: boolean;
}

export default function Header({ onToggleSidebar, hasHistory }: HeaderProps) {
  return (
    <motion.header
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: 'easeOut' }}
      className="
        relative z-20 flex items-center justify-between
        px-6 py-4 w-full
      "
    >
      {/* Left: Minimal circular Menu toggle */}
      <button
        onClick={onToggleSidebar}
        className="
          w-10 h-10 rounded-full 
          bg-white/90 hover:bg-white dark:bg-black dark:hover:bg-neutral-900
          shadow-xs border border-slate-200/80 dark:border-neutral-800
          flex items-center justify-center 
          text-slate-700 hover:text-slate-900 dark:text-neutral-300 dark:hover:text-white
          transition-all duration-200 cursor-pointer hover:scale-105 active:scale-95
        "
        title="Menu & History"
      >
        <Menu size={18} />
      </button>

      {/* Right: BUILT FOR A STRONGER INDIA + Tiranga Accent */}
      <div className="flex items-center gap-2.5">
        <div className="text-right">
          <span className="block text-[9.5px] font-bold tracking-[0.2em] text-slate-500 dark:text-neutral-400 uppercase">
            BUILT FOR A
          </span>
          <span className="block text-[10px] font-extrabold tracking-[0.22em] text-slate-700 dark:text-neutral-200 uppercase">
            STRONGER INDIA
          </span>
        </div>
        {/* Tricolor badge line */}
        <div className="flex flex-col gap-[2px] justify-center pl-1">
          <div className="w-4 h-[2px] rounded-full bg-[#FF9933]" />
          <div className="w-4 h-[2px] rounded-full bg-white dark:bg-neutral-200 border-[0.5px] border-slate-200 dark:border-neutral-700" />
          <div className="w-4 h-[2px] rounded-full bg-[#128807]" />
        </div>
      </div>
    </motion.header>
  );
}
