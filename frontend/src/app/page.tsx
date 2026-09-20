'use client';

import { useState, useCallback } from 'react';
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
import type { SearchResult, StandardResult, ChatMessage } from '@/lib/types';
import { searchBISStandards } from '@/lib/searchEngine';

export default function Home() {
  const [view, setView] = useState<'landing' | 'loading' | 'results'>('landing');
  const [results, setResults] = useState<SearchResult | null>(null);
  const [selectedStandard, setSelectedStandard] = useState<StandardResult | null>(null);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [history, setHistory] = useState<ChatMessage[]>([]);
  const [currentQuery, setCurrentQuery] = useState('');
  const [loadingStep, setLoadingStep] = useState(0);

  const handleSearch = useCallback(async (query: string) => {
    setCurrentQuery(query);
    setView('loading');
    setLoadingStep(0);

    // Multi-step query magnification & search simulation
    const delays = [700, 1000, 800];
    for (let i = 0; i < delays.length; i++) {
      await new Promise((r) => setTimeout(r, delays[i]));
      setLoadingStep(i + 1);
    }

    // Resolve standards dynamically using intelligent BIS search engine
    const searchData = searchBISStandards(query);
    setResults(searchData);
    setHistory((prev) => [
      ...prev,
      { id: Date.now().toString(), query, timestamp: new Date() },
    ]);
    setView('results');
  }, []);

  const handleFileUpload = useCallback(
    (file: File) => {
      handleSearch(`Analyze requirements from: ${file.name}`);
    },
    [handleSearch],
  );

  const handleAudioSubmit = useCallback(
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    (_blob: Blob) => {
      handleSearch('Voice query — transcription pending');
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
    <main className="relative h-screen w-screen overflow-hidden bg-white">
      {/* Interactive particle background */}
      <ParticleBackground />

      {/* App chrome */}
      <div className="relative z-10 h-full flex flex-col">
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
              className="flex-1 flex flex-col items-center justify-center px-4 pb-24"
            >
              {/* Hero text */}
              <motion.div
                initial={{ opacity: 0, y: 16 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.15, duration: 0.6 }}
                className="text-center mb-7"
              >
                <h1 className="text-3xl md:text-[2.5rem] font-extralight text-slate-800 tracking-tight leading-tight mb-2.5">
                  BIS{' '}
                  <span className="bg-gradient-to-r from-cyan-500 via-blue-500 to-indigo-500 bg-clip-text text-transparent font-normal">
                    AI
                  </span>
                </h1>
                <p className="text-[13px] text-slate-400 max-w-sm mx-auto leading-relaxed">
                  AI-powered search across 25,000+ Bureau of Indian Standards
                </p>
              </motion.div>

              {/* Input */}
              <motion.div
                initial={{ opacity: 0, y: 16 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3, duration: 0.6 }}
                className="w-full"
              >
                <ChatInput
                  onSubmit={handleSearch}
                  onFileUpload={handleFileUpload}
                  onAudioSubmit={handleAudioSubmit}
                  isLoading={false}
                />
              </motion.div>

              {/* Suggestions */}
              <SuggestionPills onSelect={handleSuggestion} />
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
                  {/* AI summary */}
                  <AIResponse
                    summary={results.summary}
                    magnifiedQuery={results.query_magnified}
                  />

                  {/* Standard cards */}
                  <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 0.25 }}
                    className="space-y-2.5"
                  >
                    {results.standards.map((std, idx) => (
                      <motion.div
                        key={std.is_code}
                        initial={{ opacity: 0, y: 14 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.35 + idx * 0.08 }}
                      >
                        <StandardCard
                          standard={std}
                          rank={idx + 1}
                          onClick={() => setSelectedStandard(std)}
                        />
                      </motion.div>
                    ))}
                  </motion.div>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
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
    </main>
  );
}
