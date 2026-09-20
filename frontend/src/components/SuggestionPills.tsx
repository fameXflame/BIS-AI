'use client';

import { motion } from 'framer-motion';
import { Coffee, Droplets, Building2, PackageCheck } from 'lucide-react';

const FEATURED_SUGGESTIONS = [
  {
    icon: Coffee,
    line1: 'Electric kettle',
    line2: 'manufacturing standards',
    query: 'Electric kettle manufacturing standards',
    iconBg: 'bg-amber-500/10 text-amber-600 border border-amber-500/20 group-hover:bg-amber-500/20',
  },
  {
    icon: Droplets,
    line1: 'Drinking water',
    line2: 'quality limits',
    query: 'Drinking water quality limits',
    iconBg: 'bg-blue-500/10 text-blue-600 border border-blue-500/20 group-hover:bg-blue-500/20',
  },
  {
    icon: Building2,
    line1: 'Earthquake resistant',
    line2: 'building codes',
    query: 'Earthquake resistant building codes',
    iconBg: 'bg-indigo-500/10 text-indigo-600 border border-indigo-500/20 group-hover:bg-indigo-500/20',
  },
  {
    icon: PackageCheck,
    line1: 'Food safety',
    line2: 'packaging norms',
    query: 'Food safety packaging norms',
    iconBg: 'bg-emerald-500/10 text-emerald-600 border border-emerald-500/20 group-hover:bg-emerald-500/20',
  },
];

interface SuggestionPillsProps {
  onSelect: (suggestion: string) => void;
}

export default function SuggestionPills({ onSelect }: SuggestionPillsProps) {
  return (
    <div className="w-full max-w-[740px] mx-auto mt-7">
      {/* "Try asking" label with subtle lines */}
      <div className="flex items-center justify-center gap-3 mb-3.5">
        <div className="h-[1px] w-12 bg-slate-200 dark:bg-neutral-800" />
        <span className="text-[11px] font-semibold text-slate-400 dark:text-neutral-500 tracking-wider uppercase">Try asking</span>
        <div className="h-[1px] w-12 bg-slate-200 dark:bg-neutral-800" />
      </div>

      {/* 4 Cards Grid with refined contrast */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        {FEATURED_SUGGESTIONS.map((item, idx) => {
          const Icon = item.icon;
          return (
            <motion.button
              key={idx}
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.35 + idx * 0.05, duration: 0.4 }}
              onClick={() => onSelect(item.query)}
              className="
                flex items-center gap-2.5 p-2.5 rounded-2xl
                bg-white hover:bg-slate-50/90 dark:bg-black dark:hover:bg-neutral-900
                border border-slate-200/90 dark:border-neutral-800 hover:border-slate-300 dark:hover:border-neutral-700
                shadow-[0_2px_10px_rgba(15,23,42,0.04),0_1px_3px_rgba(15,23,42,0.02)]
                dark:shadow-[0_4px_16px_rgba(0,0,0,0.8)]
                hover:shadow-[0_8px_24px_rgba(15,23,42,0.08),0_2px_6px_rgba(15,23,42,0.04)]
                transition-all duration-200 text-left group cursor-pointer
                hover:-translate-y-0.5
              "
            >
              <div className={`w-8 h-8 rounded-xl flex items-center justify-center shrink-0 transition-colors ${item.iconBg}`}>
                <Icon size={16} />
              </div>
              <div className="min-w-0 flex-1 leading-tight">
                <div className="text-[11.5px] font-semibold text-slate-800 dark:text-neutral-200 truncate group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
                  {item.line1}
                </div>
                <div className="text-[10px] font-medium text-slate-500 dark:text-neutral-400 truncate">
                  {item.line2}
                </div>
              </div>
            </motion.button>
          );
        })}
      </div>
    </div>
  );
}
