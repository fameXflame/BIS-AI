'use client';

import { motion } from 'framer-motion';
import { ArrowRight, Copy, Check } from 'lucide-react';
import { useState } from 'react';
import type { StandardResult } from '@/lib/types';

interface StandardCardProps {
  standard: StandardResult;
  rank: number;
  onClick: () => void;
}

export default function StandardCard({ standard, rank, onClick }: StandardCardProps) {
  const [copied, setCopied] = useState(false);

  const confidenceColor = {
    high: { bar: 'bg-emerald-400', text: 'text-emerald-400/70', glow: 'shadow-emerald-500/10' },
    moderate: { bar: 'bg-amber-400', text: 'text-amber-400/70', glow: 'shadow-amber-500/10' },
    low: { bar: 'bg-cyan-400', text: 'text-cyan-400/70', glow: 'shadow-cyan-500/10' },
  }[standard.confidence_tier];

  const handleCopy = (e: React.MouseEvent) => {
    e.stopPropagation();
    navigator.clipboard.writeText(standard.is_code);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  return (
    <motion.div
      whileHover={{ scale: 1.008, y: -1 }}
      transition={{ type: 'spring', stiffness: 400, damping: 25 }}
      onClick={onClick}
      className="glass-panel-hover rounded-xl cursor-pointer overflow-hidden group"
    >
      <div className="p-3.5">
        {/* Top row: rank badge + IS code + copy + confidence */}
        <div className="flex items-center gap-2 mb-2">
          <span className="text-[10px] font-semibold text-white/20 w-4 text-center">
            #{rank}
          </span>
          <span className="text-[12px] font-semibold text-cyan-400/80 tracking-wide">
            {standard.is_code}
          </span>
          <button
            onClick={handleCopy}
            className="p-1 rounded-md text-white/20 hover:text-white/50 hover:bg-white/[0.05] transition-all"
            title="Copy standard code"
          >
            {copied ? <Check size={11} className="text-emerald-400" /> : <Copy size={11} />}
          </button>
          <div className="ml-auto flex items-center gap-1.5">
            <span className={`text-[10px] font-medium ${confidenceColor.text}`}>
              {standard.confidence}% match
            </span>
          </div>
        </div>

        {/* Title */}
        <h3 className="text-[13px] font-medium text-white/75 mb-1.5 leading-snug pl-6">
          {standard.title}
        </h3>

        {/* Highlight reason */}
        <p className="text-[11px] text-white/35 leading-relaxed mb-3 pl-6">
          {standard.highlight_reason}
        </p>

        {/* Key clauses pills */}
        {standard.key_clauses.length > 0 && (
          <div className="flex flex-wrap gap-1.5 mb-3 pl-6">
            {standard.key_clauses.slice(0, 3).map((clause) => (
              <span
                key={clause}
                className="px-2 py-0.5 rounded-md text-[9px] bg-white/[0.03] border border-white/[0.05] text-white/25"
              >
                {clause}
              </span>
            ))}
          </div>
        )}

        {/* Explore action */}
        <div className="flex items-center justify-between pl-6">
          <span className="text-[10px] text-white/20 group-hover:text-white/40 transition-colors flex items-center gap-1">
            Explore standard <ArrowRight size={10} className="group-hover:translate-x-0.5 transition-transform" />
          </span>
        </div>
      </div>

      {/* Confidence bar at bottom */}
      <div className="h-[2px] bg-white/[0.03] w-full">
        <div
          className={`h-full ${confidenceColor.bar} confidence-bar-fill opacity-60 ${confidenceColor.glow}`}
          style={{ width: `${standard.confidence}%` }}
        />
      </div>
    </motion.div>
  );
}
