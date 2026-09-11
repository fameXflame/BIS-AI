'use client';

import { motion, AnimatePresence } from 'framer-motion';
import { X, ExternalLink, BookOpen, Calendar, Layers, Copy, Check } from 'lucide-react';
import { useState } from 'react';
import type { StandardResult } from '@/lib/types';

interface StandardDetailModalProps {
  standard: StandardResult | null;
  onClose: () => void;
}

export default function StandardDetailModal({ standard, onClose }: StandardDetailModalProps) {
  const [copied, setCopied] = useState(false);

  if (!standard) return null;

  const handleCopy = () => {
    navigator.clipboard.writeText(standard.is_code);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  const confidenceColor = {
    high: 'text-emerald-400 bg-emerald-500/10 border-emerald-500/20',
    moderate: 'text-amber-400 bg-amber-500/10 border-amber-500/20',
    low: 'text-cyan-400 bg-cyan-500/10 border-cyan-500/20',
  }[standard.confidence_tier];

  const barColor = {
    high: 'bg-emerald-400',
    moderate: 'bg-amber-400',
    low: 'bg-cyan-400',
  }[standard.confidence_tier];

  return (
    <AnimatePresence>
      {standard && (
        <>
          {/* Backdrop */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm"
          />

          {/* Drawer */}
          <motion.div
            initial={{ x: '100%', opacity: 0.8 }}
            animate={{ x: 0, opacity: 1 }}
            exit={{ x: '100%', opacity: 0 }}
            transition={{ type: 'spring', damping: 30, stiffness: 300 }}
            className="
              fixed right-0 top-0 bottom-0 z-50
              w-full max-w-md
              glass-panel border-l border-white/[0.08]
              flex flex-col
              overflow-hidden
            "
            style={{ background: 'rgba(8, 10, 18, 0.95)' }}
          >
            {/* Header */}
            <div className="flex items-center justify-between p-4 border-b border-white/[0.06]">
              <div className="flex items-center gap-2">
                <BookOpen size={16} className="text-cyan-400/60" />
                <span className="text-sm font-medium text-white/70">Standard Detail</span>
              </div>
              <button
                onClick={onClose}
                className="p-1.5 rounded-lg text-white/30 hover:text-white/70 hover:bg-white/[0.06] transition-all"
              >
                <X size={16} />
              </button>
            </div>

            {/* Content */}
            <div className="flex-1 overflow-y-auto custom-scrollbar p-4 space-y-5">
              {/* IS Code + Copy */}
              <div className="flex items-center gap-2">
                <span className="text-lg font-semibold text-cyan-400/90 tracking-wide">
                  {standard.is_code}
                </span>
                <button
                  onClick={handleCopy}
                  className="p-1 rounded-md text-white/25 hover:text-white/60 hover:bg-white/[0.05] transition-all"
                >
                  {copied ? <Check size={13} className="text-emerald-400" /> : <Copy size={13} />}
                </button>
              </div>

              {/* Title */}
              <h2 className="text-[15px] font-medium text-white/80 leading-relaxed">
                {standard.title}
              </h2>

              {/* Confidence badge */}
              <div className={`inline-flex items-center gap-2 px-3 py-1.5 rounded-lg border text-xs font-medium ${confidenceColor}`}>
                <div className={`w-2 h-2 rounded-full ${barColor}`} />
                {standard.confidence}% Confidence Match
              </div>

              {/* Meta info */}
              <div className="grid grid-cols-2 gap-3">
                {standard.division && (
                  <div className="p-3 rounded-xl bg-white/[0.03] border border-white/[0.05]">
                    <div className="flex items-center gap-1.5 mb-1">
                      <Layers size={11} className="text-white/25" />
                      <span className="text-[10px] text-white/25 uppercase tracking-wider">Division</span>
                    </div>
                    <p className="text-[12px] text-white/55">{standard.division}</p>
                  </div>
                )}
                {standard.year && (
                  <div className="p-3 rounded-xl bg-white/[0.03] border border-white/[0.05]">
                    <div className="flex items-center gap-1.5 mb-1">
                      <Calendar size={11} className="text-white/25" />
                      <span className="text-[10px] text-white/25 uppercase tracking-wider">Year</span>
                    </div>
                    <p className="text-[12px] text-white/55">{standard.year}</p>
                  </div>
                )}
              </div>

              {/* Highlight reason */}
              <div>
                <h3 className="text-[11px] text-white/30 uppercase tracking-wider mb-2">Why This Standard</h3>
                <p className="text-[13px] text-white/55 leading-relaxed">
                  {standard.highlight_reason}
                </p>
              </div>

              {/* Key clauses */}
              {standard.key_clauses.length > 0 && (
                <div>
                  <h3 className="text-[11px] text-white/30 uppercase tracking-wider mb-2">Key Clauses</h3>
                  <div className="space-y-1.5">
                    {standard.key_clauses.map((clause) => (
                      <div
                        key={clause}
                        className="flex items-center gap-2 px-3 py-2 rounded-lg bg-white/[0.02] border border-white/[0.04]"
                      >
                        <div className="w-1 h-1 rounded-full bg-cyan-400/40 shrink-0" />
                        <span className="text-[12px] text-white/45">{clause}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Abstract / Scope */}
              {standard.abstract_scope && (
                <div>
                  <h3 className="text-[11px] text-white/30 uppercase tracking-wider mb-2">Scope & Abstract</h3>
                  <p className="text-[12px] text-white/40 leading-relaxed">
                    {standard.abstract_scope}
                  </p>
                </div>
              )}

              {/* External link */}
              {standard.url && (
                <a
                  href={standard.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="
                    inline-flex items-center gap-2 px-4 py-2.5 rounded-xl
                    glass-button text-[12px] text-white/50 hover:text-white/80
                  "
                >
                  <ExternalLink size={13} />
                  View on BIS Portal
                </a>
              )}
            </div>

            {/* Bottom confidence bar */}
            <div className="h-[2px] bg-white/[0.03]">
              <div
                className={`h-full ${barColor} confidence-bar-fill opacity-50`}
                style={{ width: `${standard.confidence}%` }}
              />
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}
