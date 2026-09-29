'use client';

import { motion } from 'framer-motion';
import { Layers, Zap, Building2, ShieldCheck } from 'lucide-react';

const FEATURED_SUGGESTIONS = [
  {
    icon: Layers,
    line1: 'TMT Steel Rebars',
    line2: 'Fe 500D Tensile Norms (IS 1786)',
    query: 'TMT Steel Rebars Fe 500D IS 1786',
    iconBg: 'bg-blue-500/10 text-blue-600 dark:text-blue-400 border border-blue-500/20 group-hover:bg-blue-500/20',
  },
  {
    icon: Zap,
    line1: 'Power Cables',
    line2: 'Flame Retardant (IS 694 / 10810)',
    query: 'Fire Retardant Power Cables IS 694 IS 10810',
    iconBg: 'bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20 group-hover:bg-amber-500/20',
  },
  {
    icon: Building2,
    line1: 'Structural Cement',
    line2: 'OPC 53 Bridge Spec (IS 269)',
    query: 'Structural Cement OPC 53 Grade IS 269',
    iconBg: 'bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 border border-indigo-500/20 group-hover:bg-indigo-500/20',
  },
  {
    icon: ShieldCheck,
    line1: 'Mandatory QCOs',
    line2: 'Statutory Gazette Order List',
    query: 'Mandatory QCO Quality Control Orders Gazette',
    iconBg: 'bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 group-hover:bg-emerald-500/20',
  },
];

interface SuggestionPillsProps {
  onSelect: (suggestion: string) => void;
}

export default function SuggestionPills({ onSelect }: SuggestionPillsProps) {
  return (
    <div className="w-full max-w-[800px] mx-auto mt-4 sm:mt-7">
      {/* "Recommended Procurement Specs" label with subtle lines */}
      <div className="flex items-center justify-center gap-2 sm:gap-3 mb-2 sm:mb-3.5">
        <div className="h-[1px] w-8 sm:w-12 bg-slate-200 dark:bg-neutral-800" />
        <span className="text-[10px] sm:text-[11px] font-semibold text-slate-500 dark:text-neutral-400 tracking-wider uppercase">
          Try Procurement Queries
        </span>
        <div className="h-[1px] w-8 sm:w-12 bg-slate-200 dark:bg-neutral-800" />
      </div>

      {/* 4 Cards Grid with refined contrast & zero awkward text truncation */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-2 sm:gap-3">
        {FEATURED_SUGGESTIONS.map((item, idx) => {
          const Icon = item.icon;
          return (
            <motion.button
              key={idx}
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 + idx * 0.05, duration: 0.35 }}
              onClick={() => onSelect(item.query)}
              className="
                flex items-center gap-2 sm:gap-2.5 p-2 sm:p-2.5 rounded-xl sm:rounded-2xl
                bg-white hover:bg-slate-50/90 dark:bg-neutral-950 dark:hover:bg-neutral-900
                border border-slate-200/90 dark:border-neutral-800 hover:border-blue-400 dark:hover:border-blue-500
                shadow-[0_2px_8px_rgba(15,23,42,0.04),0_1px_2px_rgba(15,23,42,0.02)]
                dark:shadow-[0_4px_16px_rgba(0,0,0,0.6)]
                hover:shadow-[0_6px_20px_rgba(37,99,235,0.09)]
                transition-all duration-200 text-left group cursor-pointer
                hover:-translate-y-0.5
              "
            >
              <div
                className={`w-7 h-7 sm:w-8 sm:h-8 rounded-lg sm:rounded-xl flex items-center justify-center shrink-0 transition-colors ${item.iconBg}`}
              >
                <Icon size={14} className="sm:w-4 sm:h-4" />
              </div>
              <div className="min-w-0 flex-1 leading-tight overflow-hidden">
                <div className="text-[11px] sm:text-[12px] font-semibold text-slate-800 dark:text-neutral-100 truncate group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">
                  {item.line1}
                </div>
                <div className="text-[9px] sm:text-[10px] font-medium text-slate-500 dark:text-neutral-400 truncate">
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
