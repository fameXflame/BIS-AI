'use client';

import { motion, AnimatePresence } from 'framer-motion';
import { X, Clock, RotateCcw } from 'lucide-react';
import type { ChatMessage } from '@/lib/types';

interface SidebarProps {
  isOpen: boolean;
  onClose: () => void;
  history: ChatMessage[];
  onSelectQuery: (query: string) => void;
}

export default function Sidebar({ isOpen, onClose, history, onSelectQuery }: SidebarProps) {
  return (
    <AnimatePresence>
      {isOpen && (
        <>
          {/* Backdrop */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 z-30 bg-slate-900/30 dark:bg-black/70"
          />

          {/* Panel */}
          <motion.div
            initial={{ x: '-100%', opacity: 0.8 }}
            animate={{ x: 0, opacity: 1 }}
            exit={{ x: '-100%', opacity: 0 }}
            transition={{ type: 'spring', damping: 30, stiffness: 300 }}
            className="
              fixed left-0 top-0 bottom-0 z-40
              w-72
              bg-white dark:bg-black border-r border-slate-200 dark:border-neutral-800
              shadow-xl flex flex-col transition-colors
            "
          >
            {/* Header */}
            <div className="flex items-center justify-between p-4 border-b border-slate-200 dark:border-neutral-800">
              <div className="flex items-center gap-2">
                <Clock size={14} className="text-slate-400 dark:text-neutral-400" />
                <span className="text-sm font-medium text-slate-700 dark:text-neutral-200">History</span>
              </div>
              <button
                onClick={onClose}
                className="p-1.5 rounded-lg text-slate-400 dark:text-neutral-400 hover:text-slate-700 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-neutral-900 transition-all"
              >
                <X size={15} />
              </button>
            </div>

            {/* History list */}
            <div className="flex-1 overflow-y-auto custom-scrollbar p-3 space-y-1.5">
              {history.length === 0 ? (
                <p className="text-[11px] text-slate-400 dark:text-neutral-500 text-center mt-8">
                  No search history yet
                </p>
              ) : (
                [...history].reverse().map((msg) => (
                  <button
                    key={msg.id}
                    onClick={() => onSelectQuery(msg.query)}
                    className="
                      w-full text-left p-2.5 rounded-xl
                      hover:bg-slate-50 dark:hover:bg-neutral-900 group
                      transition-all duration-200
                    "
                  >
                    <p className="text-[12px] text-slate-700 dark:text-neutral-300 group-hover:text-slate-900 dark:group-hover:text-white truncate leading-snug">
                      {msg.query}
                    </p>
                    <div className="flex items-center gap-1.5 mt-1">
                      <span className="text-[9px] text-slate-400 dark:text-neutral-500">
                        {msg.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                      </span>
                      <RotateCcw size={9} className="text-slate-300 dark:text-neutral-600 group-hover:text-slate-500 dark:group-hover:text-neutral-400 transition-colors" />
                    </div>
                  </button>
                ))
              )}
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}
