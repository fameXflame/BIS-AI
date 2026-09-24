'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import { Menu, Settings2 } from 'lucide-react';
import ApiSettingsModal from './ApiSettingsModal';

interface HeaderProps {
  onToggleSidebar: () => void;
  hasHistory: boolean;
}

export default function Header({ onToggleSidebar, hasHistory }: HeaderProps) {
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);

  return (
    <>
      <motion.header
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, ease: 'easeOut' }}
        className="
          relative z-20 flex items-center justify-between
          px-6 py-4 w-full
        "
      >
        {/* Left: Minimal circular Menu toggle & Settings button */}
        <div className="flex items-center gap-2.5">
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

          <button
            onClick={() => setIsSettingsOpen(true)}
            className="
              h-9 px-3 rounded-full 
              bg-white/90 hover:bg-white dark:bg-black dark:hover:bg-neutral-900
              shadow-xs border border-slate-200/80 dark:border-neutral-800
              flex items-center gap-1.5 
              text-slate-600 hover:text-blue-600 dark:text-neutral-300 dark:hover:text-blue-400
              text-[11.5px] font-medium
              transition-all duration-200 cursor-pointer hover:scale-105 active:scale-95
            "
            title="AI & API Key Configuration"
          >
            <Settings2 size={15} />
            <span className="hidden sm:inline">AI Settings</span>
          </button>
        </div>

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

      <ApiSettingsModal isOpen={isSettingsOpen} onClose={() => setIsSettingsOpen(false)} />
    </>
  );
}
