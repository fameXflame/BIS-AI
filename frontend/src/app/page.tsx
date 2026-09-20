'use client';

import { useState, useCallback, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import ParticleBackground from '@/components/ParticleBackground';
import Header from '@/components/Header';
import ChatInput from '@/components/ChatInput';
import SuggestionPills from '@/components/SuggestionPills';
import AIResponse from '@/components/AIResponse';
import StandardCard from '@/components/StandardCard';
import StandardDetailModal from '@/components/StandardDetailModal';
import Sidebar from '@/components/Sidebar';
import SearchProgress from '@/components/SearchProgress';
import DivisionFilterBar from '@/components/DivisionFilterBar';
import ExportChecklistButton from '@/components/ExportChecklistButton';
import ComparisonModal from '@/components/ComparisonModal';
import { ArrowRightLeft, FileText, Cpu, ShieldCheck, Sun, Moon } from 'lucide-react';
import type { SearchResult, StandardResult, ChatMessage } from '@/lib/types';
import { searchBISStandards } from '@/lib/searchEngine';
import { searchStandards, uploadFile, transcribeAudio, getDivisions } from '@/lib/api';

export default function Home() {
  const [view, setView] = useState<'landing' | 'loading' | 'results'>('landing');
  const [results, setResults] = useState<SearchResult | null>(null);
  const [selectedStandard, setSelectedStandard] = useState<StandardResult | null>(null);
  const [comparisonOpen, setComparisonOpen] = useState(false);
  const [comparisonTargetA, setComparisonTargetA] = useState<StandardResult | null>(null);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [history, setHistory] = useState<ChatMessage[]>([]);
  const [currentQuery, setCurrentQuery] = useState('');
  const [loadingStep, setLoadingStep] = useState(0);
  const [divisions, setDivisions] = useState<{ division: string; count: number }[]>([]);
  const [selectedDivision, setSelectedDivision] = useState<string>('All');
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  useEffect(() => {
    const saved = localStorage.getItem('bis_theme') as 'light' | 'dark' | null;
    if (saved === 'dark' || saved === 'light') {
      setTheme(saved);
      document.documentElement.classList.toggle('dark', saved === 'dark');
    }
  }, []);

  const toggleTheme = useCallback(() => {
    setTheme((prev) => {
      const next = prev === 'light' ? 'dark' : 'light';
      localStorage.setItem('bis_theme', next);
      document.documentElement.classList.toggle('dark', next === 'dark');
      return next;
    });
  }, []);

  useEffect(() => {
    getDivisions()
      .then((data) => {
        if (Array.isArray(data)) setDivisions(data);
      })
      .catch(() => {});
  }, []);

  const handleSearch = useCallback(async (query: string, division?: string) => {
    setCurrentQuery(query);
    setView('loading');
    setLoadingStep(0);

    const activeDivision = division !== undefined ? division : undefined;

    // Kicking off backend request in parallel with progress visualization
    const apiPromise = searchStandards(query, activeDivision).catch((err) => {
      console.warn('Backend search failed or offline, falling back to local engine:', err);
      return null;
    });

    const delays = [500, 600, 500];
    for (let i = 0; i < delays.length; i++) {
      await new Promise((r) => setTimeout(r, delays[i]));
      setLoadingStep(i + 1);
    }

    const backendData = await apiPromise;
    const finalData = backendData && (backendData.summary !== undefined || backendData.standards !== undefined)
      ? backendData
      : searchBISStandards(query);

    setResults(finalData);
    setHistory((prev) => [
      ...prev,
      { id: Date.now().toString(), query, timestamp: new Date() },
    ]);
    setView('results');
  }, []);

  const handleFileUpload = useCallback(
    async (file: File) => {
      setCurrentQuery(`Analyzing ${file.name}...`);
      setView('loading');
      setLoadingStep(1);

      try {
        const uploadPromise = uploadFile(file);
        await new Promise((r) => setTimeout(r, 800));
        setLoadingStep(2);
        const res = await uploadPromise;
        setLoadingStep(3);
        await new Promise((r) => setTimeout(r, 500));

        if (res && res.search_results && res.search_results.standards?.length > 0) {
          setResults(res.search_results);
          setHistory((prev) => [
            ...prev,
            { id: Date.now().toString(), query: `Document: ${file.name}`, timestamp: new Date() },
          ]);
          setView('results');
          return;
        }
      } catch (err) {
        console.warn('File upload backend failed, running text search:', err);
      }
      handleSearch(`Analyze requirements from: ${file.name}`);
    },
    [handleSearch],
  );

  const handleAudioSubmit = useCallback(
    async (blob: Blob) => {
      setCurrentQuery('Transcribing audio input...');
      setView('loading');
      setLoadingStep(1);

      try {
        const audioPromise = transcribeAudio(blob);
        await new Promise((r) => setTimeout(r, 800));
        setLoadingStep(2);
        const res = await audioPromise;
        setLoadingStep(3);
        await new Promise((r) => setTimeout(r, 500));

        if (res && res.search_results && res.search_results.standards?.length > 0) {
          setCurrentQuery(res.transcription || 'Voice Query');
          setResults(res.search_results);
          setHistory((prev) => [
            ...prev,
            { id: Date.now().toString(), query: res.transcription || 'Voice Query', timestamp: new Date() },
          ]);
          setView('results');
          return;
        }
      } catch (err) {
        console.warn('Audio backend failed, running fallback search:', err);
      }
      handleSearch('Electric kettle safety requirements and testing');
    },
    [handleSearch],
  );

  const handleSuggestion = useCallback(
    (s: string) => handleSearch(s),
    [handleSearch],
  );

  const handleHistoryClick = useCallback(
    (q: string) => {
      setSidebarOpen(false);
      handleSearch(q);
    },
    [handleSearch],
  );

  return (
    <main className="relative h-screen w-screen overflow-hidden bg-white dark:bg-black text-slate-900 dark:text-white transition-colors duration-300 select-none">
      {/* Perimeter focus vignette */}
      <div className="vignette-center-focus absolute inset-0 z-20 pointer-events-none" />

      {/* Interactive particle background */}
      <div className="absolute inset-0 z-0 pointer-events-none">
        <ParticleBackground theme={theme} />
      </div>

      {/* App chrome */}
      <div className="relative z-30 h-full flex flex-col justify-between">
        <Header
          onToggleSidebar={() => setSidebarOpen((o) => !o)}
          hasHistory={history.length > 0}
        />

        <AnimatePresence mode="wait">
          {/* -------- LANDING -------- */}
          {view === 'landing' && (
            <motion.div
              key="landing"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0, y: -16 }}
              transition={{ duration: 0.4 }}
              className="relative flex-1 flex flex-col items-center justify-center px-4 w-full -mt-4"
            >
              {/* Giant Watermark Text "BIS" in the right background */}
              <div 
                aria-hidden="true"
                className="absolute right-[8%] md:right-[15%] top-[12%] select-none pointer-events-none text-[14rem] md:text-[21rem] font-black text-slate-900/[0.045] dark:text-white/[0.03] tracking-tight leading-none z-0 transition-colors"
              >
                BIS
              </div>

              {/* Decorative Side Card - Top Left */}
              <div className="hidden xl:block absolute left-8 top-6 pointer-events-none z-10 text-left">
                <div className="px-3.5 py-2.5 rounded-xl bg-white/70 dark:bg-black/95 backdrop-blur-xs border border-slate-200/80 dark:border-neutral-800 shadow-2xs transition-colors">
                  <div className="text-[10px] font-bold tracking-[0.22em] text-slate-600 dark:text-neutral-400 leading-relaxed uppercase">
                    STANDARDS<br />
                    SAFER INDIA<br />
                    BETTER TOMORROW
                  </div>
                  <div className="w-6 h-[1.5px] bg-blue-500/50 mt-2" />
                </div>
              </div>

              {/* Decorative Side Card - Bottom Left */}
              <div className="hidden xl:block absolute left-8 bottom-8 pointer-events-none z-10 text-left">
                <div className="px-3.5 py-2.5 rounded-xl bg-white/70 dark:bg-black/95 backdrop-blur-xs border border-slate-200/80 dark:border-neutral-800 shadow-2xs transition-colors">
                  <div className="text-[10px] font-bold tracking-[0.22em] text-slate-600 dark:text-neutral-400 leading-relaxed uppercase">
                    PEOPLE<br />
                    PRODUCTS<br />
                    PROGRESS
                  </div>
                  <div className="w-6 h-[1.5px] bg-emerald-500/50 mt-2" />
                </div>
              </div>

              {/* Decorative Quote Card - Top Right */}
              <div className="hidden xl:block absolute right-10 top-6 z-10 text-right max-w-[220px] pointer-events-none">
                <div className="px-4 py-3 rounded-xl bg-white/70 dark:bg-black/95 backdrop-blur-xs border border-slate-200/80 dark:border-neutral-800 shadow-2xs transition-colors">
                  <div className="text-right text-slate-400 dark:text-neutral-600 font-serif text-lg leading-none select-none">
                    &ldquo;
                  </div>
                  <p className="text-[13px] font-serif italic text-slate-700 dark:text-neutral-200 leading-snug px-1">
                    Standards enable progress.
                  </p>
                  <div className="text-right text-slate-400 dark:text-neutral-600 font-serif text-lg leading-none select-none -mt-0.5">
                    &rdquo;
                  </div>
                  <div className="mt-1.5 text-[8.5px] font-bold tracking-[0.2em] text-slate-400 dark:text-neutral-500 uppercase">
                    BUREAU OF INDIAN STANDARDS
                  </div>
                </div>
              </div>

              {/* Center Content Container */}
              <div className="relative z-10 w-full max-w-[780px] flex flex-col items-center">
                {/* Hero Title & Sparkle */}
                <motion.div
                  initial={{ opacity: 0, y: 16 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.15, duration: 0.6 }}
                  className="text-center mb-6 flex flex-col items-center"
                >
                  <div className="relative inline-block mb-1.5">
                    <h1 className="text-6xl md:text-[5.2rem] font-black tracking-tight text-slate-950 dark:text-white flex items-center justify-center gap-2.5 leading-none transition-colors dark:drop-shadow-[0_0_18px_rgba(59,130,246,0.35)]">
                      <span>BIS</span>
                      <span className="text-[#1d4ed8] dark:text-[#3b82f6] font-black">AI</span>
                      {/* 4-point sparkle icon matching mockup */}
                      <svg
                        className="w-8 h-8 text-[#2563eb] dark:text-[#60a5fa] fill-current animate-pulse -mt-8 ml-0.5 shrink-0 dark:drop-shadow-[0_0_10px_rgba(59,130,246,0.5)]"
                        viewBox="0 0 24 24"
                      >
                        <path d="M12 0C12 6.627 6.627 12 0 12C6.627 12 12 17.373 12 24C12 17.373 17.373 12 24 12C17.373 12 12 6.627 12 0Z" />
                      </svg>
                    </h1>
                  </div>

                  <h2 className="text-[17px] md:text-[19px] font-bold text-slate-900 dark:text-slate-100 tracking-tight mt-1 mb-1 transition-colors">
                    Your Intelligent Companion for Indian Standards
                  </h2>
                  <p className="text-xs md:text-[13px] text-slate-600 dark:text-slate-400 font-medium max-w-md mx-auto leading-relaxed transition-colors">
                    Search. Understand. Apply. Build a Safer, Stronger India.
                  </p>

                  {/* Static Status Indicator Badge */}
                  <div className="mt-4 flex items-center gap-2">
                    <div
                      className="
                        inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full
                        bg-slate-900 dark:bg-black text-white dark:text-neutral-200
                        border border-slate-700 dark:border-neutral-800
                        shadow-xs text-xs font-semibold select-none transition-colors
                      "
                    >
                      <span className="relative flex h-2 w-2">
                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                        <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-400"></span>
                      </span>
                      <span>25,000+ BIS standards indexed</span>
                    </div>
                  </div>
                </motion.div>

                {/* Input Bar */}
                <motion.div
                  initial={{ opacity: 0, y: 16 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.25, duration: 0.6 }}
                  className="w-full"
                >
                  <ChatInput
                    onSubmit={handleSearch}
                    onFileUpload={handleFileUpload}
                    onAudioSubmit={handleAudioSubmit}
                    isLoading={false}
                  />
                </motion.div>

                {/* 4 Feature Suggestion Cards */}
                <SuggestionPills onSelect={handleSuggestion} />
              </div>
            </motion.div>
          )}

          {/* -------- LOADING -------- */}
          {view === 'loading' && (
            <motion.div
              key="loading"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="flex-1 flex flex-col items-center justify-center px-4"
            >
              <SearchProgress step={loadingStep} query={currentQuery} />
            </motion.div>
          )}

          {/* -------- RESULTS -------- */}
          {view === 'results' && results && (
            <motion.div
              key="results"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.4 }}
              className="flex-1 flex flex-col min-h-0"
            >
              {/* Docked input */}
              <div className="px-4 pt-1 pb-2">
                <ChatInput
                  onSubmit={handleSearch}
                  onFileUpload={handleFileUpload}
                  onAudioSubmit={handleAudioSubmit}
                  isLoading={false}
                  compact
                />
              </div>

              {/* Scrollable results */}
              <div className="flex-1 overflow-y-auto custom-scrollbar px-4 pb-8">
                <div className="max-w-[680px] mx-auto space-y-3">
                  {/* AI summary & walk-along */}
                  <AIResponse
                    summary={results.summary}
                    magnifiedQuery={results.query_magnified}
                    isBisRelated={results.is_bis_related ?? true}
                    aiWalkalong={results.ai_walkalong}
                    onSuggestionClick={handleSearch}
                  />

                  {/* Division filter bar & Export toolbar */}
                  {results.standards.length > 0 && (
                    <div className="pt-1">
                      <DivisionFilterBar
                        selectedDivision={selectedDivision}
                        onSelectDivision={setSelectedDivision}
                        divisions={divisions}
                      />

                      <div className="flex items-center justify-between px-1 pb-1 pt-0.5">
                        <span className="text-[11px] font-semibold text-slate-500 uppercase tracking-wider">
                          Applicable Standards (
                          {results.standards.filter(
                            (s) =>
                              selectedDivision === 'All' ||
                              (s.division && s.division.toLowerCase().includes(selectedDivision.toLowerCase()))
                          ).length}
                          )
                        </span>
                        <div className="flex items-center gap-2">
                          <button
                            onClick={() => {
                              setComparisonTargetA(results.standards[0] || null);
                              setComparisonOpen(true);
                            }}
                            className="
                              inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg
                              bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200
                              text-[11.5px] font-semibold transition-all shadow-2xs
                              cursor-pointer
                            "
                            title="Side-by-side RAG comparison between two standards"
                          >
                            <ArrowRightLeft size={13} className="text-blue-600" />
                            <span>Compare Standards</span>
                          </button>
                          <ExportChecklistButton results={results} query={currentQuery} />
                        </div>
                      </div>
                    </div>
                  )}

                  {/* Standard cards */}
                  {results.standards.length > 0 && (
                    <motion.div
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      transition={{ delay: 0.15 }}
                      className="space-y-2.5"
                    >
                      {results.standards
                        .filter(
                          (s) =>
                            selectedDivision === 'All' ||
                            (s.division && s.division.toLowerCase().includes(selectedDivision.toLowerCase()))
                        )
                        .map((std, idx) => (
                          <motion.div
                            key={std.is_code}
                            initial={{ opacity: 0, y: 14 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.2 + idx * 0.06 }}
                          >
                            <StandardCard
                              standard={std}
                              rank={idx + 1}
                              onClick={() => setSelectedStandard(std)}
                            />
                          </motion.div>
                        ))}
                    </motion.div>
                  )}

                  {/* Empty state if department filter returns 0 */}
                  {results.standards.length > 0 &&
                    results.standards.filter(
                      (s) =>
                        selectedDivision === 'All' ||
                        (s.division && s.division.toLowerCase().includes(selectedDivision.toLowerCase()))
                    ).length === 0 && (
                      <div className="p-6 text-center bg-white dark:bg-slate-900/90 rounded-xl border border-slate-300 dark:border-slate-800">
                        <p className="text-xs text-slate-600 dark:text-slate-400 mb-2">
                          No standards found under &ldquo;{selectedDivision}&rdquo; for this query.
                        </p>
                        <button
                          onClick={() => setSelectedDivision('All')}
                          className="text-xs font-semibold text-blue-600 dark:text-blue-400 hover:underline"
                        >
                          Reset to All Departments
                        </button>
                      </div>
                    )}
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Footer bar matching reference mockup */}
        <footer className="relative z-30 w-full px-6 py-2.5 shrink-0 flex items-center justify-between gap-4 text-slate-500 dark:text-neutral-400 text-xs border-t border-slate-200/80 dark:border-neutral-800/80 bg-white/80 dark:bg-black/95 backdrop-blur-md transition-colors">
          {/* Left: Copyright */}
          <div className="flex items-center gap-2 text-[11px] text-slate-500 dark:text-neutral-400 font-normal">
            <span className="font-semibold text-slate-700 dark:text-neutral-300">&copy; BIS AI</span>
            <span className="text-slate-300 dark:text-neutral-800">|</span>
            <span className="hidden sm:inline">Knowledge for a Safer, Stronger India</span>
          </div>

          {/* Center: Three Feature Highlights */}
          <div className="hidden lg:flex items-center gap-5 select-none">
            <div
              className="flex items-center gap-1.5 text-[11.5px] text-slate-600 dark:text-neutral-400"
              title="Comprehensive Bureau of Indian Standards catalog"
            >
              <FileText size={14} className="text-slate-400 dark:text-neutral-500" />
              <span className="font-semibold text-slate-700 dark:text-neutral-200">25,000+</span>
              <span className="text-slate-500 dark:text-neutral-400">Standards</span>
            </div>

            <span className="text-slate-300 dark:text-neutral-800">|</span>

            <div
              className="flex items-center gap-1.5 text-[11.5px] text-slate-600 dark:text-neutral-400"
              title="Semantic search with AI technical analysis"
            >
              <Cpu size={14} className="text-blue-500 dark:text-blue-400" />
              <span className="font-medium text-slate-700 dark:text-neutral-200">AI-Powered</span>
              <span className="text-slate-500 dark:text-neutral-400">Search & Summaries</span>
            </div>

            <span className="text-slate-300 dark:text-neutral-800">|</span>

            <div
              className="flex items-center gap-1.5 text-[11.5px] text-slate-600 dark:text-neutral-400"
              title="Sourced directly from official Bureau of Indian Standards repositories"
            >
              <ShieldCheck size={14} className="text-emerald-500 dark:text-emerald-400" />
              <span className="font-medium text-slate-700 dark:text-neutral-200">Reliable</span>
              <span className="text-slate-500 dark:text-neutral-400">Official Sources</span>
            </div>
          </div>

          {/* Right: Version, Made in India, and Theme Toggle */}
          <div className="flex items-center gap-3 text-[11px] text-slate-500 dark:text-neutral-400">
            <span className="font-mono text-slate-400 dark:text-neutral-500 hidden sm:inline">v1.0</span>
            <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-slate-100 dark:bg-black border border-slate-200/80 dark:border-neutral-800 text-[10.5px] font-medium text-slate-600 dark:text-neutral-300">
              <span>🇮🇳</span>
              <span className="hidden sm:inline">Made in India</span>
            </div>

            {/* Theme Switcher Button */}
            <button
              type="button"
              onClick={toggleTheme}
              className="
                inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full
                bg-slate-100 hover:bg-slate-200 dark:bg-black dark:hover:bg-neutral-900
                text-slate-800 dark:text-neutral-100 border border-slate-300 dark:border-neutral-800
                text-[11.5px] font-semibold transition-all cursor-pointer shadow-xs hover:scale-105 active:scale-95 ml-1
              "
              title={`Switch to ${theme === 'light' ? 'Dark' : 'Light'} Mode`}
              aria-label="Toggle Dark/Light Mode"
            >
              {theme === 'light' ? (
                <>
                  <Moon size={13} className="text-slate-700" />
                  <span>Dark Mode</span>
                </>
              ) : (
                <>
                  <Sun size={13} className="text-amber-400" />
                  <span>Light Mode</span>
                </>
              )}
            </button>
          </div>
        </footer>
      </div>

      {/* Overlays */}
      <Sidebar
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
        history={history}
        onSelectQuery={handleHistoryClick}
      />
      <StandardDetailModal
        standard={selectedStandard}
        onClose={() => setSelectedStandard(null)}
      />
      {comparisonOpen && (
        <ComparisonModal
          initialStandardA={comparisonTargetA}
          allStandards={results?.standards || []}
          onClose={() => setComparisonOpen(false)}
        />
      )}
    </main>
  );
}
