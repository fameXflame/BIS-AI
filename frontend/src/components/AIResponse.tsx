'use client';

import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Bot,
  Zap,
  Compass,
  AlertCircle,
  ArrowRight,
  ShieldCheck,
  FileText,
  MessageSquare,
  Send,
  Loader2,
  ChevronDown,
  ChevronUp,
  Sparkles,
  CheckCircle2,
} from 'lucide-react';
import { directGeminiGenerate } from '@/lib/geminiClient';

interface AIResponseProps {
  summary: string;
  magnifiedQuery: string;
  isBisRelated?: boolean;
  aiWalkalong?: string;
  currentQuery?: string;
  standards?: any[];
  onSuggestionClick?: (query: string) => void;
}

/**
 * Strips raw LaTeX delimiters and translates LaTeX math syntax into clean Unicode symbols.
 */
function cleanLatexMath(raw: string): string {
  if (!raw) return '';
  let t = raw;

  // 1. Convert LaTeX text tags: \text{...} -> ...
  t = t.replace(/\\text\{([^}]+)\}/g, '$1');

  // 2. Convert common LaTeX symbols to clean Unicode
  t = t.replace(/\^\\circ|\^\{\\circ\}|\\degree|\\circ/g, '°');
  t = t.replace(/\\pm/g, '±');
  t = t.replace(/\\leq|\\le/g, '≤');
  t = t.replace(/\\geq|\\ge/g, '≥');
  t = t.replace(/\\neq|\\ne/g, '≠');
  t = t.replace(/\\times/g, '×');
  t = t.replace(/\\approx/g, '≈');
  t = t.replace(/\\mu/g, 'µ');
  t = t.replace(/\\Omega|\\ohm/g, 'Ω');
  t = t.replace(/\\cdot/g, '·');
  t = t.replace(/\\Delta/g, 'Δ');
  t = t.replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, '$1/$2');
  t = t.replace(/\^2|\^\{2\}/g, '²');
  t = t.replace(/\^3|\^\{3\}/g, '³');

  // 3. Strip $...$ math delimiters
  t = t.replace(/\$([^$]+)\$/g, '$1');

  // 4. Strip stray backslashes
  t = t.replace(/\\([a-zA-Z]+)/g, '$1');
  t = t.replace(/\\/g, '');

  // 5. Clean up degree and unit spacings
  t = t.replace(/(\d+)\s*°\s*C\b/g, '$1°C');
  t = t.replace(/°\s*C\b/g, '°C');
  t = t.replace(/\s+/g, ' ');

  return t.trim();
}

/**
 * Renders markdown bolding (**...**), bullet points, and cleans math syntax.
 */
function FormattedText({ text }: { text: string }) {
  const cleaned = cleanLatexMath(text);
  const lines = cleaned.split('\n').map((l) => l.trim()).filter(Boolean);

  return (
    <div className="space-y-2 leading-relaxed text-[12.5px] text-slate-800 dark:text-neutral-200">
      {lines.map((line, lIdx) => {
        const isBullet = line.startsWith('•') || line.startsWith('-') || line.startsWith('*');
        const content = isBullet ? line.replace(/^[•\-\*]\s*/, '') : line;

        // Split by **bold** tags
        const segments = content.split(/(\*\*[^*]+\*\*)/g);

        const renderedSegments = segments.map((seg, sIdx) => {
          if (seg.startsWith('**') && seg.endsWith('**')) {
            return (
              <strong key={sIdx} className="font-semibold text-slate-900 dark:text-white">
                {seg.slice(2, -2)}
              </strong>
            );
          }
          return <span key={sIdx}>{seg}</span>;
        });

        if (isBullet) {
          return (
            <div key={lIdx} className="flex items-start gap-2 pl-1">
              <span className="text-cyan-600 dark:text-cyan-400 font-bold mt-0.5">•</span>
              <div className="flex-1">{renderedSegments}</div>
            </div>
          );
        }

        return <p key={lIdx}>{renderedSegments}</p>;
      })}
    </div>
  );
}

export default function AIResponse({
  summary,
  magnifiedQuery,
  isBisRelated = true,
  aiWalkalong,
  currentQuery = '',
  standards = [],
  onSuggestionClick,
}: AIResponseProps) {
  const keywords = magnifiedQuery ? magnifiedQuery.split(',').map((k) => k.trim()).filter(Boolean) : [];

  // Full Technical Breakdown State
  const [fullDesc, setFullDesc] = useState<string | null>(null);
  const [fullDescLoading, setFullDescLoading] = useState(false);
  const [showFullDesc, setShowFullDesc] = useState(false);

  // Conversational Chat Follow-up State
  const [chatOpen, setChatOpen] = useState(false);
  const [chatInput, setChatInput] = useState('');
  const [chatLoading, setChatLoading] = useState(false);
  const [messages, setMessages] = useState<Array<{ role: 'user' | 'assistant'; text: string }>>([]);

  const suggestedQueries = [
    'Electric kettle manufacturing testing requirements',
    'Domestic pressure cooker safety and burst tests',
    'Permissible limits for lead and nitrate in drinking water',
    'Gold hallmarking and HUID guidelines in India',
    'Seismic structural building design IS 1893',
  ];

  const followUpSuggestions = [
    'What are the mandatory laboratory test limits?',
    'What testing equipment is required for compliance?',
    'Explain the factory inspection and ISI license roadmap.',
    'Are imported products also subject to mandatory QCO?',
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

  const matchedStandardsSummary = standards && standards.length > 0
    ? standards.slice(0, 5).map((s) => `${s.is_code}: ${s.title}`).join('; ')
    : magnifiedQuery || 'Relevant Indian Standards';

  // Handler: Generate or Toggle Full Technical Description
  const handleToggleFullDescription = async () => {
    if (fullDesc) {
      setShowFullDesc(!showFullDesc);
      return;
    }

    setFullDescLoading(true);
    setShowFullDesc(true);

    try {
      const prompt = `You are the Bureau of Indian Standards (BIS) Senior Technical Advisor.
User Query: "${currentQuery || magnifiedQuery}"
Executive Summary: "${cleanSummary}"
Matched Standards: ${matchedStandardsSummary}

Provide an authoritative, detailed technical breakdown:
1. Regulatory Framework & Statutory Classification (cite exact IS codes, publication years, and technical divisions).
2. Key Mandatory Clauses & Critical Engineering Thresholds (temperatures, allowable tolerances, voltages, limits, maximum percentages).
3. Quality Control Order (QCO) Status & Legal Penalties for non-compliance in India.
4. Prescribed Laboratory Testing Protocols & Required Apparatus (e.g. NABL testing, dielectric strength, tensile, endurance).
5. Certification Workflow: Step-by-step ISI Mark / CRS roadmap.

Do NOT output raw LaTeX math syntax (do NOT write $550^\\circ\\text{C}$, $\\pm$, \\text{...}, or $ math delimiters). Use clean, standard symbols and readable units directly (e.g. 550°C, ± 0.2 N, < 0.2 A, 5 mm, 20 N).
Format with clear bold section headings, bullet points, and crisp paragraphs.`;

      const result = await directGeminiGenerate(prompt, 1000);
      if (result) {
        setFullDesc(result);
      } else {
        setFullDesc(
          `Detailed Technical Analysis for ${currentQuery || 'Query'}:\n\n` +
          `• Primary Reference Standards: ${matchedStandardsSummary}\n` +
          `• Scope & Applicability: Prescribes mandatory material quality, design parameters, and safety criteria under the Bureau of Indian Standards Act.\n` +
          `• Verification Protocols: Requires NABL-accredited laboratory evaluation, physical and chemical conformity checks, and strict adherence to statutory Quality Control Orders (QCO).\n` +
          `• Certification Process: Manufacturer application → Factory inspection & sample drawing → Independent testing → Grant of BIS Certification Mark license.`
        );
      }
    } catch (err) {
      console.error('Full description error:', err);
      setFullDesc('Detailed technical breakdown could not be generated. Please consult the individual standard cards below.');
    } finally {
      setFullDescLoading(false);
    }
  };

  // Handler: Interactive Chat Follow-up
  const handleSendChat = async (userPrompt: string) => {
    const q = userPrompt.trim();
    if (!q || chatLoading) return;

    const newHistory = [...messages, { role: 'user' as const, text: q }];
    setMessages(newHistory);
    setChatInput('');
    setChatLoading(true);

    try {
      const conversationContext = newHistory
        .map((m) => `${m.role === 'user' ? 'User' : 'BIS AI'}: ${m.text}`)
        .join('\n');

      const prompt = `You are BIS AI, an authoritative Technical Compliance Assistant for the Bureau of Indian Standards.
Context:
Query: "${currentQuery || magnifiedQuery}"
Summary: "${cleanSummary}"
Standards: ${matchedStandardsSummary}

Chat History:
${conversationContext}

User Question: "${q}"

Provide a concise, highly specific engineering response:
1. Directly answer the user's question referencing the relevant Indian Standard(s).
2. Cite clause numbers, exact test parameters, tolerances, and statutory requirements where applicable.
3. Do NOT output raw LaTeX math syntax (do NOT write $550^\\circ\\text{C}$, $\\pm$, \\text{...}, or $ math tags). Use clean, standard symbols and readable units directly (e.g. 550°C, ± 0.2 N, < 0.2 A, 5 mm, 20 N).
4. Format with bold terms and clear bullet points. Keep under 3 concise paragraphs.`;

      const reply = await directGeminiGenerate(prompt, 600);
      if (reply) {
        setMessages([...newHistory, { role: 'assistant', text: reply }]);
      } else {
        setMessages([
          ...newHistory,
          {
            role: 'assistant',
            text: `Under the Bureau of Indian Standards framework for ${currentQuery || 'this product'}, compliance with ${matchedStandardsSummary} is governed by statutory testing and quality assurance procedures. Refer to the specific clause requirements in the details panel for exact tolerance limits.`,
          },
        ]);
      }
    } catch (err) {
      console.error('Chat error:', err);
      setMessages([
        ...newHistory,
        { role: 'assistant', text: 'Unable to process follow-up query at this time. Please check your network connection.' },
      ]);
    } finally {
      setChatLoading(false);
    }
  };

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
          <div
            className={`w-6 h-6 rounded-lg flex items-center justify-center shadow-xs ${
              isBisRelated
                ? 'bg-gradient-to-br from-cyan-500 to-indigo-600 text-white'
                : 'bg-blue-100 dark:bg-blue-950/40 text-blue-700 dark:text-blue-400 border border-blue-300 dark:border-blue-800'
            }`}
          >
            {isBisRelated ? <Bot size={14} /> : <AlertCircle size={14} />}
          </div>
          <span
            className={`text-[11px] font-semibold uppercase tracking-wider ${
              isBisRelated ? 'text-slate-700 dark:text-neutral-200' : 'text-slate-700 dark:text-neutral-300'
            }`}
          >
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
        <div
          className={`my-3 p-3 rounded-xl border text-[12px] leading-relaxed ${
            isBisRelated
              ? 'bg-slate-50/90 dark:bg-neutral-950/80 border-slate-200/80 dark:border-neutral-800 text-slate-700 dark:text-neutral-300'
              : 'bg-slate-50 dark:bg-neutral-950 border-slate-200 dark:border-neutral-800 text-slate-600 dark:text-neutral-400'
          }`}
        >
          <div className="flex items-center gap-1.5 font-semibold mb-1 text-[11px] uppercase tracking-wider text-slate-700 dark:text-neutral-300">
            <Compass size={13} className="text-blue-600 dark:text-blue-400" />
            <span>{isBisRelated ? 'Compliance Walk-Along' : 'Search Recommendation'}</span>
          </div>
          <div className="mt-1 text-slate-600 dark:text-neutral-400 leading-normal">{cleanWalkalong}</div>
        </div>
      )}

      {/* Action Bar: Full Breakdown & Interactive Follow-up Chat */}
      {isBisRelated && (
        <div className="mt-3 pt-3 border-t border-slate-200/80 dark:border-neutral-800 flex flex-wrap items-center justify-between gap-2">
          <div className="flex items-center gap-2">
            {/* Button: Detailed Technical Breakdown */}
            <button
              onClick={handleToggleFullDescription}
              disabled={fullDescLoading}
              className="
                inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl
                bg-blue-50 dark:bg-blue-950/40 hover:bg-blue-100 dark:hover:bg-blue-900/60
                text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800
                text-[11.5px] font-semibold shadow-2xs hover:shadow-xs transition-all cursor-pointer disabled:opacity-60
              "
              title="Generate comprehensive regulatory & clause analysis"
            >
              {fullDescLoading ? (
                <>
                  <Loader2 size={13} className="animate-spin text-blue-600 dark:text-blue-400" />
                  <span>Synthesizing Full Analysis...</span>
                </>
              ) : (
                <>
                  <FileText size={13} className="text-blue-600 dark:text-blue-400" />
                  <span>{showFullDesc ? 'Hide Full Technical Analysis' : 'Full Technical Breakdown'}</span>
                  {showFullDesc ? <ChevronUp size={12} /> : <ChevronDown size={12} />}
                </>
              )}
            </button>

            {/* Button: Toggle Follow-up Chat */}
            <button
              onClick={() => setChatOpen(!chatOpen)}
              className={`
                inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl
                border text-[11.5px] font-semibold shadow-2xs hover:shadow-xs transition-all cursor-pointer
                ${
                  chatOpen
                    ? 'bg-cyan-600 text-white border-cyan-600 dark:bg-cyan-600 dark:border-cyan-600'
                    : 'bg-slate-100 dark:bg-neutral-900 hover:bg-slate-200 dark:hover:bg-neutral-800 text-slate-700 dark:text-neutral-300 border-slate-200 dark:border-neutral-800'
                }
              `}
              title="Text furthermore with the AI about these standards"
            >
              <MessageSquare size={13} />
              <span>Ask AI Follow-Up</span>
              {chatOpen ? <ChevronUp size={12} /> : <ChevronDown size={12} />}
            </button>
          </div>

          <span className="text-[10.5px] text-slate-500 dark:text-neutral-500 font-medium">
            Live AI Assistant
          </span>
        </div>
      )}

      {/* Expandable: Full Technical Breakdown Panel */}
      <AnimatePresence>
        {showFullDesc && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.3 }}
            className="overflow-hidden mt-3"
          >
            <div className="p-3.5 rounded-xl bg-slate-50 dark:bg-neutral-900/90 border border-slate-200 dark:border-neutral-800 shadow-xs">
              <div className="flex items-center justify-between pb-2 mb-2 border-b border-slate-200 dark:border-neutral-800">
                <div className="flex items-center gap-1.5 text-[11px] font-bold text-blue-700 dark:text-blue-300 uppercase tracking-wider">
                  <Sparkles size={13} className="text-blue-600 dark:text-blue-400" />
                  <span>Comprehensive Standards & Compliance Breakdown</span>
                </div>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-blue-100/70 dark:bg-blue-950 text-blue-700 dark:text-blue-300 font-semibold">
                  Multi-Clause Synthesis
                </span>
              </div>

              {fullDescLoading ? (
                <div className="flex items-center justify-center py-6 gap-2 text-slate-500 dark:text-neutral-400 text-xs font-medium">
                  <Loader2 size={16} className="animate-spin text-blue-600 dark:text-blue-400" />
                  <span>Synthesizing statutory clauses and laboratory test limits...</span>
                </div>
              ) : (
                fullDesc && <FormattedText text={fullDesc} />
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Expandable: Interactive Follow-up Chat Stream */}
      <AnimatePresence>
        {chatOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.3 }}
            className="overflow-hidden mt-3"
          >
            <div className="p-3.5 rounded-xl bg-slate-50 dark:bg-neutral-950 border border-slate-200 dark:border-neutral-800 shadow-xs space-y-3">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-1.5 text-[11px] font-bold text-cyan-800 dark:text-cyan-300 uppercase tracking-wider">
                  <MessageSquare size={13} className="text-cyan-600 dark:text-cyan-400" />
                  <span>Interactive Compliance Chat</span>
                </div>
                <span className="text-[10px] text-slate-500 dark:text-neutral-400">
                  Grounded on {matchedStandardsSummary.split(';')[0]}
                </span>
              </div>

              {/* Follow-up Quick Prompt Chips */}
              <div className="flex flex-wrap gap-1.5">
                {followUpSuggestions.map((suggestion, sIdx) => (
                  <button
                    key={sIdx}
                    onClick={() => handleSendChat(suggestion)}
                    disabled={chatLoading}
                    className="
                      text-[10.5px] px-2.5 py-1 rounded-lg bg-white dark:bg-neutral-900
                      hover:bg-cyan-50 dark:hover:bg-neutral-800 border border-slate-200 dark:border-neutral-800
                      text-slate-700 dark:text-neutral-300 hover:text-cyan-800 dark:hover:text-cyan-300
                      font-medium transition-colors text-left shadow-2xs disabled:opacity-50
                    "
                  >
                    {suggestion}
                  </button>
                ))}
              </div>

              {/* Chat Messages Stream */}
              {messages.length > 0 && (
                <div className="space-y-2.5 max-h-64 overflow-y-auto custom-scrollbar p-1">
                  {messages.map((msg, mIdx) => (
                    <div
                      key={mIdx}
                      className={`flex flex-col ${msg.role === 'user' ? 'items-end' : 'items-start'}`}
                    >
                      <div className="text-[9.5px] font-bold uppercase tracking-wider mb-1 text-slate-500 dark:text-neutral-400 px-1">
                        {msg.role === 'user' ? 'You' : 'BIS Technical Assistant'}
                      </div>
                      <div
                        className={`
                          p-3 rounded-xl max-w-[92%] leading-relaxed text-[12px] shadow-2xs
                          ${
                            msg.role === 'user'
                              ? 'bg-cyan-600 text-white font-medium rounded-tr-none'
                              : 'bg-white dark:bg-neutral-900 border border-slate-200 dark:border-neutral-800 text-slate-800 dark:text-neutral-200 rounded-tl-none'
                          }
                        `}
                      >
                        {msg.role === 'user' ? (
                          <p>{msg.text}</p>
                        ) : (
                          <FormattedText text={msg.text} />
                        )}
                      </div>
                    </div>
                  ))}
                  {chatLoading && (
                    <div className="flex items-center gap-2 p-2.5 rounded-xl bg-white dark:bg-neutral-900 border border-slate-200 dark:border-neutral-800 text-slate-500 dark:text-neutral-400 text-xs">
                      <Loader2 size={13} className="animate-spin text-cyan-600 dark:text-cyan-400" />
                      <span>Synthesizing response...</span>
                    </div>
                  )}
                </div>
              )}

              {/* Chat Input Form */}
              <form
                onSubmit={(e) => {
                  e.preventDefault();
                  handleSendChat(chatInput);
                }}
                className="flex items-center gap-1.5 pt-1"
              >
                <input
                  type="text"
                  value={chatInput}
                  onChange={(e) => setChatInput(e.target.value)}
                  placeholder="Ask a follow-up question regarding these standards..."
                  className="
                    flex-1 px-3 py-2 text-[12px] rounded-xl
                    border border-slate-300 dark:border-neutral-700
                    focus:border-cyan-500 focus:outline-hidden
                    bg-white dark:bg-neutral-900 text-slate-800 dark:text-neutral-100
                    placeholder:text-slate-400 dark:placeholder:text-neutral-500 shadow-2xs
                  "
                />
                <button
                  type="submit"
                  disabled={chatLoading || !chatInput.trim()}
                  className="
                    p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-700 disabled:opacity-50
                    text-white cursor-pointer transition-all shadow-xs shrink-0
                  "
                  title="Send follow-up question"
                >
                  {chatLoading ? <Loader2 size={14} className="animate-spin" /> : <Send size={14} />}
                </button>
              </form>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

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
        <div className="flex items-start gap-2 pt-2.5 mt-3 border-t border-slate-100 dark:border-neutral-800">
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
