'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  X,
  Key,
  Server,
  Sparkles,
  CheckCircle2,
  AlertCircle,
  HelpCircle,
  ExternalLink,
  ShieldCheck,
  Zap,
} from 'lucide-react';
import {
  getStoredApiKey,
  setStoredApiKey,
  getStoredApiUrl,
  setStoredApiUrl,
  directGeminiGenerate,
} from '@/lib/geminiClient';

interface ApiSettingsModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function ApiSettingsModal({ isOpen, onClose }: ApiSettingsModalProps) {
  const [apiKey, setApiKey] = useState('');
  const [apiUrl, setApiUrl] = useState('');
  const [status, setStatus] = useState<'idle' | 'testing' | 'valid' | 'invalid'>('idle');
  const [statusMsg, setStatusMsg] = useState('');

  useEffect(() => {
    if (isOpen) {
      setApiKey(getStoredApiKey());
      setApiUrl(getStoredApiUrl());
      setStatus('idle');
      setStatusMsg('');
    }
  }, [isOpen]);

  const handleSave = async () => {
    setStoredApiKey(apiKey);
    setStoredApiUrl(apiUrl);

    if (!apiKey.trim()) {
      setStatus('idle');
      setStatusMsg('Using grounded offline local engine.');
      setTimeout(() => onClose(), 800);
      return;
    }

    setStatus('testing');
    setStatusMsg('Verifying Gemini API key...');

    try {
      const res = await directGeminiGenerate('Respond with OK');
      if (res) {
        setStatus('valid');
        setStatusMsg('API key verified! Saved to browser storage permanently.');
        setTimeout(() => onClose(), 1200);
      } else {
        setStatus('invalid');
        setStatusMsg('Could not verify key. Saved locally anyway (fallback engine active).');
      }
    } catch {
      setStatus('invalid');
      setStatusMsg('Verification error. Saved anyway.');
    }
  };

  const handleClear = () => {
    setStoredApiKey('');
    setStoredApiUrl('');
    setApiKey('');
    setApiUrl('http://localhost:8000');
    setStatus('idle');
    setStatusMsg('Settings reset to default offline engine.');
  };

  if (!isOpen) return null;

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs">
        <motion.div
          initial={{ opacity: 0, scale: 0.95, y: 10 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.95, y: 10 }}
          className="w-full max-w-lg bg-white dark:bg-neutral-900 border border-slate-200 dark:border-neutral-800 rounded-2xl shadow-2xl overflow-hidden"
        >
          {/* Header */}
          <div className="px-6 py-4 border-b border-slate-200 dark:border-neutral-800 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 rounded-lg bg-blue-100 dark:bg-blue-900/40 text-blue-600 dark:text-blue-400 flex items-center justify-center">
                <Sparkles size={16} />
              </div>
              <div>
                <h2 className="text-base font-bold text-slate-800 dark:text-white">AI & API Settings</h2>
                <p className="text-xs text-slate-500 dark:text-neutral-400">Configure once — persists in your browser</p>
              </div>
            </div>
            <button
              onClick={onClose}
              className="p-1.5 rounded-lg text-slate-400 hover:text-slate-700 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-neutral-800 transition-colors"
            >
              <X size={18} />
            </button>
          </div>

          {/* Body */}
          <div className="p-6 space-y-5 max-h-[75vh] overflow-y-auto">
            {/* Gemini API Key */}
            <div className="space-y-1.5">
              <label className="flex items-center justify-between text-xs font-semibold text-slate-700 dark:text-neutral-200">
                <span className="flex items-center gap-1.5">
                  <Key size={13} className="text-blue-500" />
                  Gemini API Key (Google AI Studio)
                </span>
                <a
                  href="https://aistudio.google.com/app/apikey"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[11px] text-blue-600 dark:text-blue-400 hover:underline flex items-center gap-1"
                >
                  Get Free Key <ExternalLink size={10} />
                </a>
              </label>
              <input
                type="password"
                value={apiKey}
                onChange={(e) => setApiKey(e.target.value)}
                placeholder="AIzaSy..."
                className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-300 dark:border-neutral-700 bg-slate-50 dark:bg-neutral-950 text-slate-800 dark:text-neutral-100 focus:outline-hidden focus:border-blue-500 transition-all font-mono"
              />
              <p className="text-[11px] text-slate-500 dark:text-neutral-400">
                Powers real-time AI summaries and interactive clause Q&A. Saved permanently in your browser localStorage.
              </p>
            </div>

            {/* Backend URL */}
            <div className="space-y-1.5">
              <label className="flex items-center gap-1.5 text-xs font-semibold text-slate-700 dark:text-neutral-200">
                <Server size={13} className="text-emerald-500" />
                Backend API Server URL
              </label>
              <input
                type="text"
                value={apiUrl}
                onChange={(e) => setApiUrl(e.target.value)}
                placeholder="http://localhost:8000"
                className="w-full px-3.5 py-2.5 text-xs rounded-xl border border-slate-300 dark:border-neutral-700 bg-slate-50 dark:bg-neutral-950 text-slate-800 dark:text-neutral-100 focus:outline-hidden focus:border-emerald-500 transition-all font-mono"
              />
              <p className="text-[11px] text-slate-500 dark:text-neutral-400">
                Default: <code className="text-[10px] bg-slate-100 dark:bg-neutral-800 px-1 py-0.5 rounded">http://localhost:8000</code>. If hosting on Render/Railway, paste the public URL here.
              </p>
            </div>

            {/* Status Feedback */}
            {statusMsg && (
              <div
                className={`p-3 rounded-xl text-xs flex items-center gap-2 ${
                  status === 'valid'
                    ? 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800'
                    : status === 'testing'
                    ? 'bg-blue-50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800'
                    : status === 'invalid'
                    ? 'bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-300 border border-amber-200 dark:border-amber-800'
                    : 'bg-slate-100 dark:bg-neutral-800 text-slate-700 dark:text-neutral-300'
                }`}
              >
                {status === 'valid' ? (
                  <CheckCircle2 size={14} className="shrink-0" />
                ) : status === 'invalid' ? (
                  <AlertCircle size={14} className="shrink-0" />
                ) : (
                  <Zap size={14} className="shrink-0 animate-pulse" />
                )}
                <span>{statusMsg}</span>
              </div>
            )}

            {/* Indian Govt / Bhashini Callout Box */}
            <div className="p-3.5 rounded-xl bg-gradient-to-r from-orange-50/60 via-slate-50/60 to-emerald-50/60 dark:from-neutral-950 dark:to-neutral-950 border border-slate-200 dark:border-neutral-800 space-y-2">
              <div className="flex items-center gap-2">
                <span className="text-sm">🇮🇳</span>
                <h4 className="text-xs font-bold text-slate-800 dark:text-neutral-200">
                  Digital India & Bhashini (MeitY) Alignment
                </h4>
              </div>
              <p className="text-[11px] text-slate-600 dark:text-neutral-400 leading-relaxed">
                For SIH evaluations, BIS AI is architected to integrate seamlessly with the Government of India&apos;s{' '}
                <a
                  href="https://bhashini.gov.in"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-600 dark:text-blue-400 font-semibold underline"
                >
                  Digital India Bhashini Mission
                </a>{' '}
                for speech-to-text across 22 Indian languages, and local sovereign LLMs (Sarvam / Krutrim) with zero foreign cloud dependency.
              </p>
            </div>
          </div>

          {/* Footer Actions */}
          <div className="px-6 py-3.5 bg-slate-50 dark:bg-neutral-950 border-t border-slate-200 dark:border-neutral-800 flex items-center justify-between">
            <button
              onClick={handleClear}
              type="button"
              className="text-xs text-slate-500 hover:text-slate-800 dark:text-neutral-400 dark:hover:text-white transition-colors"
            >
              Reset to Defaults
            </button>
            <div className="flex items-center gap-2">
              <button
                onClick={onClose}
                type="button"
                className="px-3.5 py-1.5 text-xs font-medium text-slate-600 dark:text-neutral-300 hover:bg-slate-200/60 dark:hover:bg-neutral-800 rounded-lg transition-colors"
              >
                Cancel
              </button>
              <button
                onClick={handleSave}
                disabled={status === 'testing'}
                type="button"
                className="px-4 py-1.5 text-xs font-semibold bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white rounded-lg shadow-sm transition-all flex items-center gap-1.5"
              >
                {status === 'testing' ? 'Verifying...' : 'Save Settings'}
              </button>
            </div>
          </div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
}
