'use client';

import { motion } from 'framer-motion';
import { Bot, Zap, Compass, AlertCircle, ArrowRight, ShieldCheck } from 'lucide-react';

interface AIResponseProps {
  summary: string;
  magnifiedQuery: string;
  isBisRelated?: boolean;
  aiWalkalong?: string;
  onSuggestionClick?: (query: string) => void;
}

export default function AIResponse({
  summary,
  magnifiedQuery,
  isBisRelated = true,
  aiWalkalong,
  onSuggestionClick,
}: AIResponseProps) {
  const keywords = magnifiedQuery ? magnifiedQuery.split(',').map((k) => k.trim()).filter(Boolean) : [];

  const suggestedQueries = [
    'Electric kettle manufacturing testing requirements',
    'Domestic pressure cooker safety and burst tests',
    'Permissible limits for lead and nitrate in drinking water',
    'Gold hallmarking and HUID guidelines in India',
    'Seismic structural building design IS 1893',
  ];

  const cleanSummary = summary
    ? summary
        .replace(/#{1,6}\s*/g, '')
        .replace(/\*\*/g, '')
        .replace(/---/g, '')
        .replace(/^\*\s+/gm, '')
        .trim()
    : '';

  const cleanWalkalong = aiWalkalong
    ? aiWalkalong
        .replace(/\*\*/g, '')
        .replace(/#{1,6}\s*/g, '')
        .replace(/`{1,3}/g, '')
        .replace(/---/g, '')
        .trim()
    : '';

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, ease: 'easeOut' }}
      className="bg-white dark:bg-black rounded-2xl p-4 md:p-5 border-[1.5px] border-slate-300 dark:border-neutral-800 shadow-sm transition-colors"
    >
      {/* Header Badge */}
      <div className="flex items-center justify-between gap-2 mb-3">
        <div className="flex items-center gap-2">
          <div className={`w-6 h-6 rounded-lg flex items-center justify-center shadow-xs ${
            isBisRelated
              ? 'bg-gradient-to-br from-cyan-500 to-indigo-600 text-white'
              : 'bg-blue-100 dark:bg-blue-950/40 text-blue-700 dark:text-blue-400 border border-blue-300 dark:border-blue-800'
          }`}>
            {isBisRelated ? <Bot size={14} /> : <AlertCircle size={14} />}
          </div>
          <span className={`text-[11px] font-semibold uppercase tracking-wider ${
            isBisRelated ? 'text-slate-700 dark:text-neutral-200' : 'text-slate-700 dark:text-neutral-300'
          }`}>
            {isBisRelated ? 'BIS Technical Synthesis' : 'Product Search Advisory'}
          </span>
        </div>

        {isBisRelated ? (
          <span className="text-[10px] px-2 py-0.5 rounded-full bg-slate-100 dark:bg-black border border-slate-200 dark:border-neutral-800 text-slate-500 dark:text-neutral-400 font-medium">
            Standard Compliance
          </span>
        ) : (
          <span className="text-[10px] px-2 py-0.5 rounded-full bg-slate-100 dark:bg-neutral-900 border border-slate-200 dark:border-neutral-800 text-slate-600 dark:text-neutral-400 font-medium">
            Search Guidance
          </span>
        )}
      </div>

      {/* Summary text */}
      <p className="text-[13.5px] leading-relaxed text-slate-800 dark:text-neutral-100 font-normal mb-3">
        {cleanSummary}
      </p>

      {/* AI Walk-Along Advisory Box */}
      {cleanWalkalong && (
        <div className={`my-3 p-3 rounded-xl border text-[12px] leading-relaxed ${
          isBisRelated
            ? 'bg-slate-50/90 dark:bg-neutral-950/80 border-slate-200/80 dark:border-neutral-800 text-slate-700 dark:text-neutral-300'
            : 'bg-slate-50 dark:bg-neutral-950 border-slate-200 dark:border-neutral-800 text-slate-600 dark:text-neutral-400'
        }`}>
          <div className="flex items-center gap-1.5 font-semibold mb-1 text-[11px] uppercase tracking-wider text-slate-700 dark:text-neutral-300">
            <Compass size={13} className="text-blue-600 dark:text-blue-400" />
            <span>{isBisRelated ? 'Compliance Walk-Along' : 'Search Recommendation'}</span>
          </div>
          <div className="mt-1 text-slate-600 dark:text-neutral-400 leading-normal">{cleanWalkalong}</div>
        </div>
      )}

      {/* Suggested queries when out of scope */}
      {!isBisRelated && onSuggestionClick && (
        <div className="mt-4 pt-3 border-t border-slate-200/60 dark:border-neutral-800">
          <p className="text-[11px] font-semibold text-slate-500 dark:text-neutral-400 mb-2 flex items-center gap-1">
            <ShieldCheck size={13} className="text-blue-600 dark:text-blue-400" />
            <span>Try searching official Indian Standards topics:</span>
          </p>
          <div className="flex flex-wrap gap-1.5">
            {suggestedQueries.map((sq) => (
              <button
                key={sq}
                onClick={() => onSuggestionClick(sq)}
                className="
                  inline-flex items-center gap-1 text-[11px] text-slate-700 dark:text-neutral-300
                  bg-white dark:bg-black hover:bg-slate-100 dark:hover:bg-neutral-900 border border-slate-300/80 dark:border-neutral-800 hover:border-slate-400
                  px-2.5 py-1 rounded-lg font-medium transition-all shadow-xs text-left
                "
              >
                <span>{sq}</span>
                <ArrowRight size={10} className="text-slate-400 dark:text-neutral-500" />
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Magnified keywords */}
      {isBisRelated && keywords.length > 0 && (
        <div className="flex items-start gap-2 pt-2 border-t border-slate-100 dark:border-neutral-800">
          <Zap size={12} className="text-amber-500 mt-0.5 shrink-0" />
          <div className="flex flex-wrap gap-1.5">
            {keywords.map((kw) => (
              <span
                key={kw}
                className="px-2 py-0.5 rounded-md text-[10px] bg-slate-100 dark:bg-neutral-950 border border-slate-300 dark:border-neutral-800 text-slate-600 dark:text-neutral-300 font-medium"
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
