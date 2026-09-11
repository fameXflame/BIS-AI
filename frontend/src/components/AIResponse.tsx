'use client';

import { motion } from 'framer-motion';
import { Bot, Zap } from 'lucide-react';

interface AIResponseProps {
  summary: string;
  magnifiedQuery: string;
}

export default function AIResponse({ summary, magnifiedQuery }: AIResponseProps) {
  const keywords = magnifiedQuery.split(',').map((k) => k.trim()).filter(Boolean);

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: 'easeOut' }}
      className="glass-panel rounded-2xl p-4"
    >
      {/* AI avatar + label */}
      <div className="flex items-center gap-2 mb-3">
        <div className="w-6 h-6 rounded-lg bg-gradient-to-br from-cyan-500/60 to-indigo-500/60 flex items-center justify-center">
          <Bot size={13} className="text-white" />
        </div>
        <span className="text-[11px] font-medium text-white/40 uppercase tracking-wider">AI Analysis</span>
      </div>

      {/* Summary text */}
      <p className="text-[13px] leading-relaxed text-white/65 mb-3">
        {summary}
      </p>

      {/* Magnified keywords */}
      {keywords.length > 0 && (
        <div className="flex items-start gap-2">
          <Zap size={12} className="text-amber-400/50 mt-0.5 shrink-0" />
          <div className="flex flex-wrap gap-1.5">
            {keywords.map((kw) => (
              <span
                key={kw}
                className="px-2 py-0.5 rounded-md text-[10px] bg-white/[0.04] border border-white/[0.06] text-white/35"
              >
                {kw}
              </span>
            ))}
          </div>
        </div>
      )}
    </motion.div>
  );
}
