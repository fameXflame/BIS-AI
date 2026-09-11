'use client';

import { motion, AnimatePresence } from 'framer-motion';
import { Search, Brain, BarChart3, Loader2 } from 'lucide-react';

const STEPS = [
  { icon: Brain, label: 'Magnifying technical terms...', detail: 'Expanding query with domain keywords' },
  { icon: Search, label: 'Scanning BIS catalog...', detail: 'Running hybrid BM25 + semantic search' },
  { icon: BarChart3, label: 'Ranking by confidence...', detail: 'Applying reciprocal rank fusion' },
];

interface SearchProgressProps {
  step: number;
  query: string;
}

export default function SearchProgress({ step, query }: SearchProgressProps) {
  return (
    <div className="w-full max-w-md mx-auto">
      {/* Query display */}
      <motion.div
        initial={{ opacity: 0, y: 8 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center mb-8"
      >
        <p className="text-[11px] text-white/25 mb-1">Searching for</p>
        <p className="text-sm text-white/60 font-medium">&ldquo;{query}&rdquo;</p>
      </motion.div>

      {/* Progress steps */}
      <div className="space-y-3">
        {STEPS.map((s, i) => {
          const Icon = s.icon;
          const isActive = step === i + 1;
          const isDone = step > i + 1;
          const isPending = step < i + 1;

          return (
            <motion.div
              key={i}
              initial={{ opacity: 0, x: -12 }}
              animate={{ opacity: isPending ? 0.3 : 1, x: 0 }}
              transition={{ delay: i * 0.15, duration: 0.4 }}
              className={`
                flex items-center gap-3 px-4 py-2.5 rounded-xl
                transition-all duration-300
                ${isActive ? 'glass-panel' : ''}
                ${isDone ? 'opacity-50' : ''}
              `}
            >
              <div className={`
                w-7 h-7 rounded-lg flex items-center justify-center
                ${isActive ? 'bg-cyan-500/15' : isDone ? 'bg-emerald-500/10' : 'bg-white/[0.03]'}
              `}>
                {isActive ? (
                  <Loader2 size={14} className="text-cyan-400 animate-spin" />
                ) : isDone ? (
                  <Icon size={14} className="text-emerald-400/60" />
                ) : (
                  <Icon size={14} className="text-white/20" />
                )}
              </div>
              <div>
                <p className={`text-[12px] font-medium ${
                  isActive ? 'text-white/70' : isDone ? 'text-white/40' : 'text-white/20'
                }`}>
                  {isDone ? s.label.replace('...', '') : s.label}
                </p>
                <AnimatePresence>
                  {isActive && (
                    <motion.p
                      initial={{ opacity: 0, height: 0 }}
                      animate={{ opacity: 1, height: 'auto' }}
                      exit={{ opacity: 0, height: 0 }}
                      className="text-[10px] text-white/25 mt-0.5"
                    >
                      {s.detail}
                    </motion.p>
                  )}
                </AnimatePresence>
              </div>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}
