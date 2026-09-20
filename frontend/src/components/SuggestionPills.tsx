'use client';

import { motion } from 'framer-motion';

const SUGGESTIONS = [
  'Electric kettle manufacturing standards',
  'Drinking water quality limits',
  'Earthquake resistant building codes',
  'Fire safety standards for buildings',
  'Steel structural design',
  'Food safety packaging norms',
];

interface SuggestionPillsProps {
  onSelect: (suggestion: string) => void;
}

export default function SuggestionPills({ onSelect }: SuggestionPillsProps) {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: 0.6, duration: 0.5 }}
      className="flex flex-wrap justify-center gap-2 mt-5 max-w-[600px] px-4"
    >
      {SUGGESTIONS.map((s, i) => (
        <motion.button
          key={s}
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.7 + i * 0.06, duration: 0.3 }}
          onClick={() => onSelect(s)}
          className="
            px-3 py-1.5 rounded-full
            text-[11px] text-slate-500
            bg-white/80 border border-slate-200/60
            hover:bg-white hover:border-slate-300 hover:text-slate-700
            backdrop-blur-sm shadow-sm hover:shadow-md
            transition-all duration-200
            cursor-pointer
          "
        >
          {s}
        </motion.button>
      ))}
    </motion.div>
  );
}
