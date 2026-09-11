'use client';

import { motion } from 'framer-motion';
import { Menu, Sparkles } from 'lucide-react';

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
        px-5 py-3
      "
    >
      {/* Left: History toggle */}
      <button
        onClick={onToggleSidebar}
        className={`
          p-2 rounded-xl glass-button
          text-white/40 hover:text-white/80
          transition-colors duration-200
          ${!hasHistory ? 'opacity-40 pointer-events-none' : ''}
        `}
        title="Search history"
      >
        <Menu size={18} />
      </button>

      {/* Center: Logo */}
      <div className="flex items-center gap-2">
        <div className="w-7 h-7 rounded-lg bg-gradient-to-br from-cyan-500/80 to-blue-600/80 flex items-center justify-center shadow-lg shadow-cyan-500/10">
          <Sparkles size={14} className="text-white" />
        </div>
        <span className="text-sm font-medium text-white/70 tracking-wide">
          BIS AI
        </span>
        <span className="text-[10px] px-1.5 py-0.5 rounded-full bg-white/[0.06] border border-white/[0.08] text-white/30 font-medium">
          v1.0
        </span>
      </div>

      {/* Right: spacer for symmetry */}
      <div className="w-[42px]" />
    </motion.header>
  );
}
