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
            className="fixed inset-0 z-30 bg-black/50 backdrop-blur-sm"
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
              glass-panel border-r border-white/[0.08]
              flex flex-col
            "
            style={{ background: 'rgba(8, 10, 18, 0.95)' }}
          >
            {/* Header */}
            <div className="flex items-center justify-between p-4 border-b border-white/[0.06]">
              <div className="flex items-center gap-2">
                <Clock size={14} className="text-white/30" />
                <span className="text-sm font-medium text-white/60">History</span>
              </div>
              <button
                onClick={onClose}
                className="p-1.5 rounded-lg text-white/30 hover:text-white/70 hover:bg-white/[0.06] transition-all"
              >
                <X size={15} />
              </button>
            </div>

            {/* History list */}
            <div className="flex-1 overflow-y-auto custom-scrollbar p-3 space-y-1.5">
              {history.length === 0 ? (
                <p className="text-[11px] text-white/20 text-center mt-8">
                  No search history yet
                </p>
              ) : (
                [...history].reverse().map((msg) => (
                  <button
                    key={msg.id}
                    onClick={() => onSelectQuery(msg.query)}
                    className="
                      w-full text-left p-2.5 rounded-xl
                      hover:bg-white/[0.04] group
                      transition-all duration-200
                    "
                  >
                    <p className="text-[12px] text-white/50 group-hover:text-white/70 truncate leading-snug">
                      {msg.query}
                    </p>
                    <div className="flex items-center gap-1.5 mt-1">
                      <span className="text-[9px] text-white/15">
                        {msg.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                      </span>
                      <RotateCcw size={9} className="text-white/10 group-hover:text-white/30 transition-colors" />
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
