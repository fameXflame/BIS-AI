'use client';

import { useState, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import WormholeStars from '@/components/WormholeStars';
import Header from '@/components/Header';
import ChatInput from '@/components/ChatInput';
import SuggestionPills from '@/components/SuggestionPills';
import AIResponse from '@/components/AIResponse';
import StandardCard from '@/components/StandardCard';
import StandardDetailModal from '@/components/StandardDetailModal';
import Sidebar from '@/components/Sidebar';
import SearchProgress from '@/components/SearchProgress';
import type { SearchResult, StandardResult, ChatMessage } from '@/lib/types';

/* ------------------------------------------------------------------ */
/*  Demo data — replaced by real API calls in Phase 4                  */
/* ------------------------------------------------------------------ */
const MOCK_RESULTS: SearchResult = {
  summary:
    "Great question! Manufacturing an electric kettle in India requires compliance with several BIS standards covering product safety, electromagnetic compatibility, and material specifications. I've identified 6 key standards — the top three (IS 302 and IS 4250) are mandatory for obtaining BIS certification under the Compulsory Registration Scheme (CRS). Here's your complete compliance roadmap.",
  query_magnified:
    'electric kettle manufacturing, IS 302 safety, household electrical appliances, heating liquids, BIS certification, ISI mark, EMC compliance, compulsory registration scheme, type testing, boil-dry protection',
  standards: [
    {
      is_code: 'IS 302 (Part 2/Sec 15) : 2009',
      title: 'Safety of Household and Similar Electrical Appliances — Particular Requirements for Appliances for Heating Liquids',
      confidence: 98,
      confidence_tier: 'high',
      highlight_reason:
        'This is your PRIMARY compliance standard — specifically written for kettles, coffee makers, and liquid heating appliances. Covers boil-dry protection, thermal cutoffs, spill resistance, and handle temperature limits during operation.',
      key_clauses: ['Clause 15.101: Boil-dry Protection', 'Clause 19: Abnormal Operation Tests', 'Clause 22: Construction Requirements', 'Clause 30: Heat Resistance'],
      division: 'Electrotechnical',
      year: 2009,
      abstract_scope:
        'This standard specifies safety requirements for electric appliances intended for heating liquids, such as kettles, coffee makers, and similar devices. It covers protection against electric shock, fire, mechanical hazards, and thermal dangers during both normal use and foreseeable misuse. Tests include thermal endurance, moisture resistance, leakage current, dielectric strength, and mechanical strength of handles and lids.',
    },
    {
      is_code: 'IS 302 (Part 1) : 2008',
      title: 'Safety of Household and Similar Electrical Appliances — General Requirements',
      confidence: 95,
      confidence_tier: 'high',
      highlight_reason:
        'The foundational safety standard for ALL household electrical appliances in India. Must be read alongside Part 2/Sec 15. Covers insulation classes, grounding continuity, leakage current limits, power input tolerance, and mandatory marking requirements.',
      key_clauses: ['Clause 8: Protection Against Electric Shock', 'Clause 10: Power Input & Current', 'Clause 13: Leakage Current at Operating Temperature', 'Clause 25: Supply Connection'],
      division: 'Electrotechnical',
      year: 2008,
      abstract_scope:
        'General requirements for the safety of household and similar electrical appliances with rated voltage not exceeding 250V for single-phase and 480V for other appliances. This standard is to be used in conjunction with the relevant Part 2 section for the specific appliance type. It establishes the baseline for electrical safety, thermal safety, mechanical safety, and fire hazard prevention.',
    },
    {
      is_code: 'IS 4250 : 1980',
      title: 'Specification for Electric Kettles',
      confidence: 92,
      confidence_tier: 'high',
      highlight_reason:
        'India-specific product specification standard for electric kettles — defines capacity ratings (up to 3L), water level markings, element wattage ranges, lid design requirements, and materials in contact with drinking water must be food-grade safe.',
      key_clauses: ['Clause 4: Capacity and Rating', 'Clause 5: Materials & Food Safety', 'Clause 6: Construction & Finish', 'Clause 8: Marking Requirements'],
      division: 'Electrotechnical',
      year: 1980,
      abstract_scope:
        'This standard covers requirements for electric kettles with rated capacity up to 3 litres intended for domestic use. It specifies construction requirements, performance parameters, materials (particularly those in contact with potable water), wattage ratings, and marking. The standard ensures kettles are safe, durable, and suitable for boiling drinking water.',
    },
    {
      is_code: 'IS 13252 (Part 1) : 2010',
      title: 'Electromagnetic Compatibility (EMC) — Limits for Harmonic Current Emissions',
      confidence: 76,
      confidence_tier: 'moderate',
      highlight_reason:
        'EMC compliance is mandatory under the BIS Compulsory Registration Scheme (CRS). Your kettle\'s heating element and any electronic controls (auto-shutoff circuits, LED indicators) must meet harmonic emission limits to prevent electrical interference on the power grid.',
      key_clauses: ['Clause 6: Emission Limits', 'Clause 7: Test Conditions & Setup', 'Table 1: Maximum Permissible Harmonic Currents'],
      division: 'Electrotechnical',
      year: 2010,
      abstract_scope:
        'This standard specifies limits for harmonic currents injected into the public supply system by electrical equipment with rated input current up to 16A per phase. It applies to all electrical and electronic equipment connected to public low-voltage distribution systems. Equipment must be tested under specified operating conditions to verify compliance.',
    },
    {
      is_code: 'IS 1293 : 2019',
      title: 'Plugs and Socket-Outlets of Rated Voltage up to 250V and Rated Current up to 16A',
      confidence: 63,
      confidence_tier: 'moderate',
      highlight_reason:
        'The power plug and cord-set supplied with your kettle must comply with this standard. Covers Indian 3-pin plug dimensions, insulation requirements, earth pin specifications, and rated current capacity for the 6A/16A configurations commonly used with kettles.',
      key_clauses: ['Clause 10: Plug Dimensions', 'Clause 14: Insulation Resistance & Dielectric Strength', 'Clause 16: Breaking Capacity'],
      division: 'Electrotechnical',
      year: 2019,
      abstract_scope:
        'This standard covers plugs and socket-outlets for household and similar purposes for AC circuits of rated voltage up to and including 250V and rated current up to and including 16A. It specifies dimensional requirements, material specifications, electrical ratings, and test methods for Indian-standard plugs.',
    },
    {
      is_code: 'IS 15885 : 2010',
      title: 'Electric Kettles and Food Preparation Appliances — Marking and Labelling Requirements',
      confidence: 48,
      confidence_tier: 'low',
      highlight_reason:
        'Supplementary standard covering mandatory product labelling — rated wattage, voltage, ISI mark placement, batch identification, manufacturer details, and safety warnings that must appear on the kettle body and packaging.',
      key_clauses: ['Clause 4: Mandatory Markings on Appliance', 'Clause 5: Packaging Label Requirements', 'Clause 6: Safety Warning Symbols'],
      division: 'Electrotechnical',
      year: 2010,
      abstract_scope:
        'This standard specifies the marking and labelling requirements for electric kettles and food preparation appliances sold in India. It covers placement, durability, and content of product labels including rated parameters, safety symbols, manufacturer information, and ISI certification mark display.',
    },
  ],
};

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

    // Simulate multi-step pipeline
    const delays = [900, 1300, 1000];
    for (let i = 0; i < delays.length; i++) {
      await new Promise((r) => setTimeout(r, delays[i]));
      setLoadingStep(i + 1);
    }

    // TODO Phase 4: Replace with real API call
    // const data = await searchStandards(query);
    setResults(MOCK_RESULTS);
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
    <main className="relative h-screen w-screen overflow-hidden bg-black">
      {/* Wormhole starfield background */}
      <WormholeStars />

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
                <h1 className="text-3xl md:text-[2.5rem] font-extralight text-white/90 tracking-tight leading-tight mb-2.5">
                  BIS{' '}
                  <span className="bg-gradient-to-r from-cyan-400 via-blue-400 to-indigo-400 bg-clip-text text-transparent font-normal">
                    AI
                  </span>
                </h1>
                <p className="text-[13px] text-white/25 max-w-sm mx-auto leading-relaxed">
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
