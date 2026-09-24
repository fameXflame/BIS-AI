'use client';

import { motion, AnimatePresence } from 'framer-motion';
import {
  X,
  ExternalLink,
  BookOpen,
  Calendar,
  Layers,
  Copy,
  Check,
  ChevronDown,
  ChevronUp,
  ShieldCheck,
  ShieldAlert,
  FlaskConical,
  CheckCircle2,
  Sparkles,
  MessageSquare,
  Send,
  Loader2,
} from 'lucide-react';
import { useState } from 'react';
import type { StandardResult } from '@/lib/types';
import { askClauseQA } from '@/lib/api';
import { directGeminiGenerate, clientAnswerClauseQuestion } from '@/lib/geminiClient';

interface StandardDetailModalProps {
  standard: StandardResult | null;
  onClose: () => void;
}

export default function StandardDetailModal({ standard, onClose }: StandardDetailModalProps) {
  const [copied, setCopied] = useState(false);
  const [expandedClause, setExpandedClause] = useState<number | null>(0);
  const [copiedClauseIdx, setCopiedClauseIdx] = useState<number | null>(null);

  // Interactive Clause Q&A state
  const [qaInput, setQaInput] = useState('');
  const [qaLoading, setQaLoading] = useState(false);
  const [qaHistory, setQaHistory] = useState<Array<{ question: string; answer: string; citations: string[] }>>([]);

  if (!standard) return null;

  const handleCopy = () => {
    navigator.clipboard.writeText(standard.is_code);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  const handleCopyClause = (clauseText: string, idx: number, e: React.MouseEvent) => {
    e.stopPropagation();
    navigator.clipboard.writeText(clauseText);
    setCopiedClauseIdx(idx);
    setTimeout(() => setCopiedClauseIdx(null), 1500);
  };

  const confidenceColor = {
    high: 'text-emerald-700 bg-emerald-50 border-emerald-300',
    moderate: 'text-amber-700 bg-amber-50 border-amber-300',
    low: 'text-slate-700 bg-slate-100 border-slate-300',
  }[standard.confidence_tier];

  const barColor = {
    high: 'bg-emerald-500',
    moderate: 'bg-amber-500',
    low: 'bg-slate-500',
  }[standard.confidence_tier];

  // Parse certification workflow steps
  const certSteps = standard.certification_process
    ? standard.certification_process.split('→').map((s) => s.trim()).filter(Boolean)
    : [];

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
            className="fixed inset-0 z-40 bg-slate-900/30 dark:bg-black/70"
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
              bg-white dark:bg-black border-l border-slate-200 dark:border-neutral-800
              shadow-2xl flex flex-col
              overflow-hidden transition-colors
            "
          >
            {/* Header */}
            <div className="flex items-center justify-between p-4 border-b border-slate-200 dark:border-neutral-800">
              <div className="flex items-center gap-2">
                <BookOpen size={16} className="text-cyan-500" />
                <span className="text-sm font-medium text-slate-800 dark:text-neutral-100">Standard Detail</span>
              </div>
              <button
                onClick={onClose}
                className="p-1.5 rounded-lg text-slate-400 dark:text-neutral-400 hover:text-slate-700 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-neutral-900 transition-all"
              >
                <X size={16} />
              </button>
            </div>

            {/* Content */}
            <div className="flex-1 overflow-y-auto custom-scrollbar p-4 space-y-5">
              {/* IS Code + Copy + Mandatory Badge */}
              <div className="space-y-2">
                <div className="flex items-center justify-between gap-2">
                  <div className="flex items-center gap-2">
                    <span className="text-xl font-bold text-blue-700 dark:text-blue-400 tracking-wide">
                      {standard.is_code}
                    </span>
                    <button
                      onClick={handleCopy}
                      className="p-1 rounded-md text-slate-400 dark:text-neutral-400 hover:text-slate-700 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-neutral-900 transition-all"
                      title="Copy IS Code"
                    >
                      {copied ? <Check size={14} className="text-emerald-600" /> : <Copy size={14} />}
                    </button>
                  </div>

                  <div className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg border text-xs font-semibold ${confidenceColor}`}>
                    <div className={`w-1.5 h-1.5 rounded-full ${barColor}`} />
                    {standard.confidence}% Match
                  </div>
                </div>

                {/* Regulatory Status Pill */}
                <div>
                  {standard.mandatory ? (
                    <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[11px] font-bold bg-rose-50 dark:bg-rose-950/50 border border-rose-200 dark:border-rose-800 text-rose-700 dark:text-rose-400">
                      <ShieldAlert size={13} className="text-rose-600 dark:text-rose-400" />
                      Mandatory Quality Control Order (QCO / ISI Mark)
                    </span>
                  ) : (
                    <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[11px] font-medium bg-slate-100 dark:bg-neutral-900 border border-slate-200 dark:border-neutral-800 text-slate-600 dark:text-neutral-300">
                      <ShieldCheck size={13} className="text-slate-500 dark:text-neutral-400" />
                      Voluntary BIS Standard Specification
                    </span>
                  )}
                </div>
              </div>

              {/* Title */}
              <h2 className="text-[15px] font-semibold text-slate-900 dark:text-white leading-snug">
                {standard.title}
              </h2>

              {/* Meta info */}
              <div className="grid grid-cols-2 gap-2.5">
                {standard.division && (
                  <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-neutral-950 border border-slate-200 dark:border-neutral-800">
                    <div className="flex items-center gap-1.5 mb-1">
                      <Layers size={11} className="text-slate-500 dark:text-neutral-400" />
                      <span className="text-[10px] text-slate-500 dark:text-neutral-400 uppercase tracking-wider font-semibold">Division</span>
                    </div>
                    <p className="text-[12px] font-medium text-slate-800 dark:text-neutral-200">{standard.division}</p>
                  </div>
                )}
                {standard.year && (
                  <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-neutral-950 border border-slate-200 dark:border-neutral-800">
                    <div className="flex items-center gap-1.5 mb-1">
                      <Calendar size={11} className="text-slate-500 dark:text-neutral-400" />
                      <span className="text-[10px] text-slate-500 dark:text-neutral-400 uppercase tracking-wider font-semibold">Year</span>
                    </div>
                    <p className="text-[12px] font-medium text-slate-800 dark:text-neutral-200">{standard.year}</p>
                  </div>
                )}
              </div>

              {/* Scope & Abstract */}
              {(standard.abstract_scope || standard.highlight_reason) && (
                <div>
                  <h3 className="text-[11px] font-semibold text-slate-500 dark:text-neutral-400 uppercase tracking-wider mb-1.5">Scope & Purpose</h3>
                  <p className="text-[12.5px] text-slate-700 dark:text-neutral-300 leading-relaxed bg-slate-50 dark:bg-neutral-950 p-3 rounded-xl border border-slate-200 dark:border-neutral-800">
                    {standard.abstract_scope || standard.highlight_reason}
                  </p>
                </div>
              )}

              {/* Interactive Clause Explorer */}
              {standard.key_clauses && standard.key_clauses.length > 0 && (
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <h3 className="text-[11px] font-semibold text-slate-500 dark:text-neutral-400 uppercase tracking-wider">
                      Interactive Clause Explorer ({standard.key_clauses.length})
                    </h3>
                    <span className="text-[10px] text-slate-400 dark:text-neutral-500">Click to expand requirements</span>
                  </div>

                  <div className="space-y-2">
                    {standard.key_clauses.map((clause, idx) => {
                      const isExpanded = expandedClause === idx;
                      const isCopied = copiedClauseIdx === idx;
                      const parts = clause.split('—');
                      const clauseTitle = parts[0]?.trim() || clause;
                      const clauseDetails = parts.slice(1).join('—').trim();

                      return (
                        <div
                          key={idx}
                          onClick={() => setExpandedClause(isExpanded ? null : idx)}
                          className={`
                            rounded-xl border transition-all cursor-pointer overflow-hidden
                            ${isExpanded ? 'bg-blue-50/40 dark:bg-blue-950/40 border-blue-300 dark:border-blue-700 shadow-xs' : 'bg-white dark:bg-neutral-950 border-slate-200 dark:border-neutral-800 hover:border-slate-300 dark:hover:border-neutral-700 hover:bg-slate-50/50 dark:hover:bg-neutral-900/50'}
                          `}
                        >
                          <div className="p-3 flex items-center justify-between gap-2">
                            <div className="flex items-center gap-2 min-w-0">
                              <span className="w-5 h-5 rounded-md bg-blue-100 dark:bg-blue-900/60 text-blue-700 dark:text-blue-300 text-[10px] font-bold flex items-center justify-center shrink-0">
                                {idx + 1}
                              </span>
                              <span className="text-[12.5px] font-semibold text-slate-800 dark:text-slate-200 truncate">
                                {clauseTitle}
                              </span>
                            </div>
                            <div className="flex items-center gap-1.5 shrink-0">
                              <button
                                onClick={(e) => handleCopyClause(clause, idx, e)}
                                className="p-1 rounded text-slate-400 dark:text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 hover:bg-slate-200/60 dark:hover:bg-slate-700 transition-all"
                                title="Copy clause text"
                              >
                                {isCopied ? <Check size={12} className="text-emerald-600" /> : <Copy size={12} />}
                              </button>
                              {isExpanded ? <ChevronUp size={14} className="text-blue-600 dark:text-blue-400" /> : <ChevronDown size={14} className="text-slate-400" />}
                            </div>
                          </div>

                          {isExpanded && (
                            <div className="px-3 pb-3 pt-1 border-t border-blue-100 dark:border-blue-900/60 text-[12px] text-slate-700 dark:text-slate-300 leading-relaxed space-y-2">
                              {clauseDetails ? (
                                <p className="text-slate-700 dark:text-slate-300">{clauseDetails}</p>
                              ) : (
                                <p className="text-slate-500 dark:text-slate-400 italic">Prescribes standardized specification limits and adherence criteria under this clause.</p>
                              )}
                              <div className="pt-1 flex items-center justify-between text-[11px] text-blue-600 dark:text-blue-400 font-medium">
                                <span>Status: Mandatory Audit Point</span>
                                <span className="text-slate-400 dark:text-slate-500">IS Ref: {standard.is_code}</span>
                              </div>
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}

              {/* Interactive Clause Q&A Assistant */}
              <div className="p-3.5 rounded-xl border border-cyan-200 dark:border-cyan-800/80 bg-cyan-50/40 dark:bg-cyan-950/30 space-y-3">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-1.5">
                    <Sparkles size={14} className="text-cyan-600 dark:text-cyan-400" />
                    <h3 className="text-xs font-bold text-slate-800 dark:text-slate-100">
                      Ask Technical Limits (Clause Q&A)
                    </h3>
                  </div>
                  <span className="text-[10px] font-semibold text-cyan-700 dark:text-cyan-300 bg-cyan-100/80 dark:bg-cyan-900/60 px-1.5 py-0.5 rounded">
                    RAG Grounded
                  </span>
                </div>

                <p className="text-[11px] text-slate-600 dark:text-slate-400">
                  Ask precise questions on tolerances, maximum percentages, or test apparatus for <strong className="text-slate-800 dark:text-slate-200">{standard.is_code}</strong>.
                </p>

                {/* Quick Prompts */}
                <div className="flex flex-wrap gap-1.5">
                  {[
                    'What is the maximum water absorption percentage?',
                    'What is the compressive strength requirement?',
                    'Is this standard mandatory under QCO?',
                    'What testing equipment is required?',
                  ].map((qPrompt, qIdx) => (
                    <button
                      key={qIdx}
                      onClick={async () => {
                        setQaInput(qPrompt);
                        setQaLoading(true);
                        try {
                          const res = await askClauseQA(standard.is_code, qPrompt);
                          setQaHistory((prev) => [
                            ...prev,
                            { question: qPrompt, answer: res.answer, citations: res.citations || [] },
                          ]);
                          setQaInput('');
                        } catch (err) {
                          console.error(err);
                        } finally {
                          setQaLoading(false);
                        }
                      }}
                      className="text-[10px] px-2 py-1 rounded bg-white dark:bg-slate-800 hover:bg-cyan-50 dark:hover:bg-slate-700 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:text-cyan-800 dark:hover:text-cyan-300 font-medium transition-colors text-left"
                    >
                      {qPrompt}
                    </button>
                  ))}
                </div>

                {/* Q&A Chat Stream */}
                {qaHistory.length > 0 && (
                  <div className="space-y-2.5 max-h-56 overflow-y-auto custom-scrollbar pt-1">
                    {qaHistory.map((item, idx) => (
                      <div key={idx} className="space-y-1.5">
                        <div className="text-[11px] font-semibold text-cyan-900 dark:text-cyan-200 bg-cyan-100/50 dark:bg-cyan-900/40 p-2 rounded-lg">
                          Q: {item.question}
                        </div>
                        <div className="text-[11.5px] text-slate-800 dark:text-slate-100 bg-white dark:bg-slate-850 p-2.5 rounded-lg border border-slate-200 dark:border-slate-700 shadow-2xs leading-relaxed whitespace-pre-line">
                          {item.answer}
                          {item.citations?.length > 0 && (
                            <div className="mt-2 pt-1.5 border-t border-slate-100 dark:border-slate-800 flex flex-wrap gap-1">
                              {item.citations.map((cite, cIdx) => (
                                <span
                                  key={cIdx}
                                  className="text-[9.5px] px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 font-medium"
                                >
                                  {cite}
                                </span>
                              ))}
                            </div>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>
                )}

                {/* Input box */}
                <form
                  onSubmit={async (e) => {
                    e.preventDefault();
                    if (!qaInput.trim() || qaLoading) return;
                    const question = qaInput.trim();
                    setQaLoading(true);
                    try {
                      let answer = '';
                      let citations: string[] = [];

                      // 1. Try calling the backend API
                      try {
                        const res = await askClauseQA(standard.is_code, question);
                        if (res && res.answer) {
                          answer = res.answer;
                          citations = res.citations || [];
                        }
                      } catch {
                        // Backend is offline or blocked on static host
                      }

                      // 2. If backend failed, try direct Gemini with stored key
                      if (!answer) {
                        try {
                          const directPrompt = `You are the Bureau of Indian Standards (BIS) Technical Assistant.
Standard: ${standard.is_code} - ${standard.title}
Scope: ${standard.abstract_scope || standard.highlight_reason || ''}
Key Clauses: ${(standard.key_clauses || []).join('; ')}
Test Requirements: ${standard.test_requirements || ''}
Mandatory QCO: ${standard.mandatory ? 'Yes' : 'No'}

Question: "${question}"
Provide a clear, grounded technical answer citing relevant clauses or test specifications. Keep under 2 paragraphs.`;

                          const geminiText = await directGeminiGenerate(directPrompt);
                          if (geminiText) {
                            answer = geminiText;
                            citations = [standard.is_code];
                          }
                        } catch {
                          // Gemini API error or no key
                        }
                      }

                      // 3. Fallback to deterministic grounded rule-engine (guaranteed answer)
                      if (!answer) {
                        const fallback = clientAnswerClauseQuestion(standard, question);
                        answer = fallback.answer;
                        citations = fallback.citations;
                      }

                      setQaHistory((prev) => [
                        ...prev,
                        { question, answer, citations },
                      ]);
                      setQaInput('');
                    } catch (err) {
                      console.error('QA processing error:', err);
                    } finally {
                      setQaLoading(false);
                    }
                  }}
                  className="flex items-center gap-1.5"
                >
                  <input
                    type="text"
                    value={qaInput}
                    onChange={(e) => setQaInput(e.target.value)}
                    placeholder="e.g. permissible lead ppm or curing time..."
                    className="flex-1 px-3 py-1.5 text-[11.5px] rounded-lg border border-slate-300 dark:border-slate-700 focus:border-cyan-500 focus:outline-hidden bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100"
                  />
                  <button
                    type="submit"
                    disabled={qaLoading || !qaInput.trim()}
                    className="p-2 rounded-lg bg-cyan-600 hover:bg-cyan-700 disabled:opacity-50 text-white cursor-pointer transition-colors shrink-0"
                    title="Ask Question"
                  >
                    {qaLoading ? <Loader2 size={13} className="animate-spin" /> : <Send size={13} />}
                  </button>
                </form>
              </div>

              {/* Laboratory Testing Protocols */}
              {standard.test_requirements && (
                <div>
                  <div className="flex items-center gap-1.5 mb-1.5">
                    <FlaskConical size={13} className="text-indigo-600 dark:text-indigo-400" />
                    <h3 className="text-[11px] font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">
                      Prescribed Testing Protocols & Equipment
                    </h3>
                  </div>
                  <div className="p-3 rounded-xl bg-indigo-50/50 dark:bg-indigo-950/40 border border-indigo-200 dark:border-indigo-800 text-[12px] text-indigo-950 dark:text-indigo-200 leading-relaxed">
                    {standard.test_requirements}
                  </div>
                </div>
              )}

              {/* Certification Roadmap Timeline */}
              {certSteps.length > 0 && (
                <div>
                  <div className="flex items-center gap-1.5 mb-2.5">
                    <CheckCircle2 size={13} className="text-emerald-600 dark:text-emerald-400" />
                    <h3 className="text-[11px] font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">
                      BIS Certification Roadmap ({certSteps.length} Milestones)
                    </h3>
                  </div>

                  <div className="space-y-2 relative before:absolute before:left-3 before:top-2 before:bottom-2 before:w-0.5 before:bg-slate-200 dark:before:bg-slate-700">
                    {certSteps.map((step, idx) => (
                      <div key={idx} className="relative flex items-start gap-3 pl-1">
                        <span className="w-5 h-5 rounded-full bg-emerald-600 text-white text-[10px] font-bold flex items-center justify-center shrink-0 z-10 shadow-xs">
                          {idx + 1}
                        </span>
                        <div className="flex-1 p-2.5 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-[11.5px] text-slate-800 dark:text-slate-200 leading-normal">
                          {step}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Official BIS Resources & Links */}
              <div className="pt-2 border-t border-slate-200 dark:border-slate-800 space-y-2.5">
                <h3 className="text-[11px] font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Official BIS Verification</h3>
                <div className="flex flex-col gap-2">
                  <a
                    href={`https://www.google.com/search?q=${encodeURIComponent(standard.is_code + ' ' + standard.title + ' site:bis.gov.in')}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="
                      flex items-center justify-between px-3.5 py-2.5 rounded-xl
                      bg-blue-50 dark:bg-blue-950/40 border border-blue-200 dark:border-blue-800 text-[12px] font-medium text-blue-700 dark:text-blue-300
                      hover:bg-blue-100 dark:hover:bg-blue-900/60 hover:border-blue-300 transition-all
                    "
                  >
                    <span className="flex items-center gap-2">
                      <ExternalLink size={13} className="text-blue-600 dark:text-blue-400" />
                      Find Official Gazette & PDF on bis.gov.in
                    </span>
                    <span className="text-[10px] text-blue-500 dark:text-blue-400 font-normal">Google Site Search</span>
                  </a>

                  <a
                    href="https://www.manakonline.in/MANAK/knowYourStandards"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="
                      flex items-center justify-between px-3.5 py-2.5 rounded-xl
                      bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-[12px] font-medium text-slate-700 dark:text-slate-200
                      hover:bg-slate-100 dark:hover:bg-slate-750 hover:border-slate-300 transition-all
                    "
                  >
                    <span className="flex items-center gap-2">
                      <BookOpen size={13} className="text-slate-500 dark:text-slate-400" />
                      Search on BIS Manakonline Portal
                    </span>
                    <span className="text-[10px] text-slate-500 dark:text-slate-400 font-normal">Official Portal</span>
                  </a>
                </div>
                <p className="text-[10.5px] text-slate-400 dark:text-slate-500 leading-normal">
                  Note: Direct internal URLs on services.bis.gov.in require an active government session cookie and often return 403 Forbidden. Use the verified links above to inspect full text & amendments.
                </p>
              </div>
            </div>

            {/* Bottom confidence bar */}
            <div className="h-[2px] bg-slate-100 dark:bg-slate-800">
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
