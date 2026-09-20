'use client';

import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X, ArrowRightLeft, ShieldCheck, Scale, CheckCircle2, AlertCircle, Loader2 } from 'lucide-react';
import type { StandardResult } from '@/lib/types';
import { compareStandards } from '@/lib/api';

interface ComparisonModalProps {
  initialStandardA?: StandardResult | null;
  allStandards: StandardResult[];
  onClose: () => void;
}

export default function ComparisonModal({
  initialStandardA,
  allStandards,
  onClose,
}: ComparisonModalProps) {
  const [codeA, setCodeA] = useState<string>(
    initialStandardA?.is_code || allStandards[0]?.is_code || 'IS 269: 1989'
  );
  const [codeB, setCodeB] = useState<string>(
    allStandards.length > 1 ? allStandards[1]?.is_code : 'IS 8112: 1989'
  );

  const [loading, setLoading] = useState(false);
  const [comparisonData, setComparisonData] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const handleRunComparison = async (targetA = codeA, targetB = codeB) => {
    if (!targetA || !targetB) return;
    setLoading(true);
    setError(null);
    try {
      const data = await compareStandards(targetA, targetB);
      setComparisonData(data);
    } catch (err: any) {
      setError(err.message || 'Comparison failed. Standards may not exist.');
    } finally {
      setLoading(false);
    }
  };

  // Pre-configured popular comparisons
  const presets = [
    { label: 'IS 269 (33 Grade) vs IS 8112 (43 Grade)', a: 'IS 269: 1989', b: 'IS 8112: 1989' },
    { label: 'IS 8112 (43 Grade) vs IS 12269 (53 Grade)', a: 'IS 8112: 1989', b: 'IS 12269: 1987' },
    { label: 'IS 7098 P1 (LV) vs IS 7098 P2 (HT) Cables', a: 'IS 7098 (Part 1): 1988', b: 'IS 7098 (Part 2): 2011' },
    { label: 'IS 4984 (PE Water) vs IS 4985 (uPVC Water)', a: 'IS 4984: 2016', b: 'IS 4985: 2021' },
  ];

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
        {/* Backdrop */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
          className="fixed inset-0 bg-slate-900/40 dark:bg-black/70 backdrop-blur-xs"
        />

        {/* Modal Window */}
        <motion.div
          initial={{ opacity: 0, scale: 0.95, y: 15 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.95, y: 15 }}
          className="
            relative z-10 w-full max-w-4xl max-h-[90vh]
            bg-white dark:bg-black rounded-2xl shadow-2xl border border-slate-300 dark:border-neutral-800
            flex flex-col overflow-hidden transition-colors
          "
        >
          {/* Header */}
          <div className="p-4 border-b border-slate-200 dark:border-neutral-800 flex items-center justify-between bg-slate-50/70 dark:bg-neutral-950">
            <div className="flex items-center gap-2.5">
              <div className="w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center shadow-xs">
                <ArrowRightLeft size={16} />
              </div>
              <div>
                <h2 className="text-base font-bold text-slate-900 dark:text-white">RAG Cross-Standard Comparison</h2>
                <p className="text-xs text-slate-500 dark:text-neutral-400">Side-by-side technical specification & legal compliance analysis</p>
              </div>
            </div>
            <button
              onClick={onClose}
              className="p-1.5 rounded-lg text-slate-400 dark:text-neutral-400 hover:text-slate-700 dark:hover:text-white hover:bg-slate-200 dark:hover:bg-neutral-900 transition-colors"
            >
              <X size={18} />
            </button>
          </div>

          {/* Selector Bar & Quick Presets */}
          <div className="p-4 border-b border-slate-200 dark:border-neutral-800 bg-white dark:bg-black space-y-3">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
              <div>
                <label className="block text-[11px] font-bold text-slate-600 dark:text-neutral-400 uppercase tracking-wider mb-1">
                  Primary Standard (A)
                </label>
                <input
                  type="text"
                  value={codeA}
                  onChange={(e) => setCodeA(e.target.value)}
                  placeholder="e.g. IS 269: 1989"
                  className="w-full px-3 py-2 text-xs font-semibold rounded-lg border border-slate-300 dark:border-neutral-800 focus:border-blue-500 focus:outline-hidden bg-slate-50/50 dark:bg-neutral-950 text-slate-800 dark:text-neutral-100"
                />
              </div>

              <div>
                <label className="block text-[11px] font-bold text-slate-600 dark:text-neutral-400 uppercase tracking-wider mb-1">
                  Comparison Standard (B)
                </label>
                <input
                  type="text"
                  value={codeB}
                  onChange={(e) => setCodeB(e.target.value)}
                  placeholder="e.g. IS 8112: 1989"
                  className="w-full px-3 py-2 text-xs font-semibold rounded-lg border border-slate-300 dark:border-neutral-800 focus:border-blue-500 focus:outline-hidden bg-slate-50/50 dark:bg-neutral-950 text-slate-800 dark:text-neutral-100"
                />
              </div>
            </div>

            {/* Action button + Presets */}
            <div className="flex flex-wrap items-center justify-between gap-2 pt-1">
              <div className="flex flex-wrap items-center gap-1.5">
                <span className="text-[11px] text-slate-400 dark:text-neutral-500 font-medium">Try benchmark presets:</span>
                {presets.map((p, idx) => (
                  <button
                    key={idx}
                    onClick={() => {
                      setCodeA(p.a);
                      setCodeB(p.b);
                      handleRunComparison(p.a, p.b);
                    }}
                    className="text-[10.5px] font-medium px-2 py-1 rounded bg-slate-100 dark:bg-neutral-900 hover:bg-blue-50 dark:hover:bg-neutral-800 hover:text-blue-700 dark:hover:text-blue-300 text-slate-600 dark:text-neutral-300 border border-slate-200 dark:border-neutral-800 transition-colors"
                  >
                    {p.label}
                  </button>
                ))}
              </div>

              <button
                onClick={() => handleRunComparison()}
                disabled={loading}
                className="
                  px-4 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 text-white
                  text-xs font-semibold shadow-xs flex items-center gap-2 cursor-pointer
                  disabled:opacity-60
                "
              >
                {loading ? <Loader2 size={14} className="animate-spin" /> : <Scale size={14} />}
                <span>{loading ? 'Analyzing Parameters...' : 'Compare Specifications'}</span>
              </button>
            </div>
          </div>

          {/* Results Display */}
          <div className="flex-1 overflow-y-auto custom-scrollbar p-5 space-y-4">
            {error && (
              <div className="p-3.5 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-800 text-xs text-rose-800 dark:text-rose-300 flex items-center gap-2">
                <AlertCircle size={16} className="shrink-0 text-rose-600" />
                <span>{error}</span>
              </div>
            )}

            {!comparisonData && !loading && !error && (
              <div className="py-12 text-center text-slate-400 dark:text-slate-500 space-y-2">
                <ArrowRightLeft size={32} className="mx-auto text-slate-300 dark:text-slate-600" />
                <p className="text-sm font-medium text-slate-600 dark:text-slate-300">Select two standards or click a preset above to inspect differences</p>
                <p className="text-xs text-slate-400 dark:text-slate-500">Compares physical limits, test mandates, voltage tiers, and QCO enforceability</p>
              </div>
            )}

            {comparisonData && (
              <div className="space-y-4">
                {/* Side by side cards */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {/* Standard A */}
                  <div className="p-4 rounded-xl border-2 border-blue-200 dark:border-blue-900/60 bg-blue-50/30 dark:bg-blue-950/30 space-y-2">
                    <div className="flex items-center justify-between">
                      <span className="text-sm font-bold text-blue-800 dark:text-blue-300">
                        {comparisonData.standard_a?.is_code}
                      </span>
                      <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                        comparisonData.standard_a?.mandatory ? 'bg-rose-100 text-rose-800' : 'bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
                      }`}>
                        {comparisonData.standard_a?.mandatory ? 'MANDATORY QCO' : 'VOLUNTARY'}
                      </span>
                    </div>
                    <h4 className="text-xs font-semibold text-slate-900 dark:text-slate-100 leading-snug">
                      {comparisonData.standard_a?.title}
                    </h4>
                    <p className="text-[11.5px] text-slate-600 dark:text-slate-300 leading-relaxed">
                      {comparisonData.standard_a?.scope || comparisonData.standard_a?.abstract_scope}
                    </p>
                  </div>

                  {/* Standard B */}
                  <div className="p-4 rounded-xl border-2 border-indigo-200 dark:border-indigo-900/60 bg-indigo-50/30 dark:bg-indigo-950/30 space-y-2">
                    <div className="flex items-center justify-between">
                      <span className="text-sm font-bold text-indigo-800 dark:text-indigo-300">
                        {comparisonData.standard_b?.is_code}
                      </span>
                      <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                        comparisonData.standard_b?.mandatory ? 'bg-rose-100 text-rose-800' : 'bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
                      }`}>
                        {comparisonData.standard_b?.mandatory ? 'MANDATORY QCO' : 'VOLUNTARY'}
                      </span>
                    </div>
                    <h4 className="text-xs font-semibold text-slate-900 dark:text-slate-100 leading-snug">
                      {comparisonData.standard_b?.title}
                    </h4>
                    <p className="text-[11.5px] text-slate-600 dark:text-slate-300 leading-relaxed">
                      {comparisonData.standard_b?.scope || comparisonData.standard_b?.abstract_scope}
                    </p>
                  </div>
                </div>

                {/* Key Differences Bulletins */}
                {comparisonData.key_differences?.length > 0 && (
                  <div className="p-4 rounded-xl bg-amber-50/60 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/60 space-y-2">
                    <h4 className="text-xs font-bold text-amber-900 dark:text-amber-300 uppercase tracking-wider flex items-center gap-1.5">
                      <CheckCircle2 size={14} className="text-amber-700 dark:text-amber-400" />
                      Key Technical & Regulatory Distinctions
                    </h4>
                    <ul className="space-y-1.5">
                      {comparisonData.key_differences.map((diff: string, i: number) => (
                        <li key={i} className="text-[12px] text-amber-950 dark:text-amber-200 flex items-start gap-2">
                          <span className="text-amber-600 dark:text-amber-400 font-bold">•</span>
                          <span>{diff}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Detailed Comparison Table */}
                <div className="border border-slate-200 dark:border-slate-800 rounded-xl overflow-hidden">
                  <table className="w-full text-left text-xs border-collapse">
                    <thead>
                      <tr className="bg-slate-100 dark:bg-slate-800 border-b border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300">
                        <th className="p-3 font-bold w-1/4">Parameter</th>
                        <th className="p-3 font-bold w-1/3 text-blue-900 dark:text-blue-400">{comparisonData.standard_a?.is_code}</th>
                        <th className="p-3 font-bold w-1/3 text-indigo-900 dark:text-indigo-400">{comparisonData.standard_b?.is_code}</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-200 dark:divide-slate-800">
                      {comparisonData.comparison_points?.map((row: any, idx: number) => (
                        <tr key={idx} className="hover:bg-slate-50/70 dark:hover:bg-slate-800/60 transition-colors">
                          <td className="p-3 font-semibold text-slate-800 dark:text-slate-200 bg-slate-50/40 dark:bg-slate-850/40">
                            {row.parameter}
                          </td>
                          <td className="p-3 text-slate-700 dark:text-slate-300 font-medium">
                            {row.standard_a}
                          </td>
                          <td className="p-3 text-slate-700 dark:text-slate-300 font-medium">
                            {row.standard_b}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            )}
          </div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
}
