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

  // High-contrast vibrant colors that POP
  const confidenceStyle = {
    high: {
      badge: 'bg-emerald-600 text-white',
      bar: 'bg-emerald-500',
    },
    moderate: {
      badge: 'bg-amber-600 text-white',
      bar: 'bg-amber-500',
    },
    low: {
      badge: 'bg-slate-700 text-white',
      bar: 'bg-slate-500',
    },
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
      className="bg-white dark:bg-black rounded-xl cursor-pointer overflow-hidden group border-[1.5px] border-slate-300 dark:border-neutral-800 hover:border-slate-500 dark:hover:border-neutral-700 shadow-sm hover:shadow-md transition-all"
    >
      <div className="p-4">
        {/* Top row: rank badge + IS code + copy + confidence badge */}
        <div className="flex items-center gap-2 mb-2">
          <span className="text-[11px] font-bold text-slate-400 dark:text-neutral-500 w-4 text-center">
            #{rank}
          </span>
          <span className="text-[13px] font-bold text-blue-700 dark:text-blue-400 tracking-wide">
            {standard.is_code}
          </span>
          {standard.mandatory && (
            <span className="text-[9.5px] font-bold px-1.5 py-0.2 rounded bg-rose-50 dark:bg-rose-950/50 text-rose-700 dark:text-rose-400 border border-rose-200 dark:border-rose-800 uppercase tracking-wider">
              Mandatory
            </span>
          )}
          <button
            onClick={handleCopy}
            className="p-1 rounded-md text-slate-400 dark:text-neutral-400 hover:text-slate-700 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-neutral-900 transition-all"
            title="Copy standard code"
          >
            {copied ? <Check size={12} className="text-emerald-500" /> : <Copy size={12} />}
          </button>
          <div className="ml-auto flex items-center gap-1.5">
            <span className={`text-[11px] font-bold px-2.5 py-0.5 rounded-md shadow-xs tracking-wide ${confidenceStyle.badge}`}>
              {standard.confidence}% match
            </span>
          </div>
        </div>

        {/* Title */}
        <h3 className="text-[13.5px] font-semibold text-slate-900 dark:text-white mb-1.5 leading-snug pl-6">
          {standard.title}
        </h3>

        {/* Highlight reason */}
        <p className="text-[11.5px] text-slate-700 dark:text-neutral-300 leading-relaxed mb-3 pl-6">
          {standard.highlight_reason}
        </p>

        {/* Key clauses pills */}
        {standard.key_clauses.length > 0 && (
          <div className="flex flex-wrap gap-1.5 mb-3 pl-6">
            {standard.key_clauses.slice(0, 3).map((clause) => (
              <span
                key={clause}
                className="px-2 py-0.5 rounded-md text-[9.5px] font-medium bg-slate-100 dark:bg-neutral-900 border border-slate-300 dark:border-neutral-800 text-slate-700 dark:text-neutral-300"
              >
                {clause}
              </span>
            ))}
          </div>
        )}

        {/* Explore action */}
        <div className="flex items-center justify-between pl-6 pt-1">
          <span className="text-[11px] font-semibold text-slate-600 dark:text-neutral-400 group-hover:text-slate-900 dark:group-hover:text-white transition-colors flex items-center gap-1">
            Explore standard <ArrowRight size={11} className="group-hover:translate-x-0.5 transition-transform text-blue-600 dark:text-blue-400" />
          </span>
        </div>
      </div>

      {/* High-visibility confidence bar at bottom */}
      <div className="h-[3.5px] bg-slate-200 dark:bg-neutral-800 w-full">
        <div
          className={`h-full ${confidenceStyle.bar} transition-all duration-500`}
          style={{ width: `${standard.confidence}%` }}
        />
      </div>
    </motion.div>
  );
}
