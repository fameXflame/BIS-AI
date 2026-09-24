'use client';

import { useState, useRef, useCallback, KeyboardEvent, ChangeEvent } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Send, Paperclip, Mic, MicOff, X, FileText } from 'lucide-react';

interface ChatInputProps {
  onSubmit: (query: string) => void;
  onFileUpload: (file: File) => void;
  onAudioSubmit: (blob: Blob) => void;
  isLoading: boolean;
  compact?: boolean;
}

export default function ChatInput({
  onSubmit,
  onFileUpload,
  onAudioSubmit,
  isLoading,
  compact = false,
}: ChatInputProps) {
  const [query, setQuery] = useState('');
  const [isRecording, setIsRecording] = useState(false);
  const [attachedFile, setAttachedFile] = useState<File | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  const handleSubmit = useCallback(() => {
    const trimmed = query.trim();
    if (!trimmed && !attachedFile) return;
    if (isLoading) return;
    if (attachedFile) {
      onFileUpload(attachedFile);
      setAttachedFile(null);
    }
    if (trimmed) {
      onSubmit(trimmed);
      setQuery('');
    }
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
    }
  }, [query, attachedFile, isLoading, onSubmit, onFileUpload]);

  const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  const handleInput = () => {
    const el = textareaRef.current;
    if (el) {
      el.style.height = 'auto';
      el.style.height = Math.min(el.scrollHeight, compact ? 80 : 140) + 'px';
    }
  };

  const toggleRecording = async () => {
    if (isRecording) {
      mediaRecorderRef.current?.stop();
      setIsRecording(false);
    } else {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        const recorder = new MediaRecorder(stream);
        chunksRef.current = [];
        recorder.ondataavailable = (e) => {
          if (e.data.size > 0) chunksRef.current.push(e.data);
        };
        recorder.onstop = () => {
          const blob = new Blob(chunksRef.current, { type: 'audio/webm' });
          onAudioSubmit(blob);
          stream.getTracks().forEach((t) => t.stop());
        };
        recorder.start();
        mediaRecorderRef.current = recorder;
        setIsRecording(true);
      } catch {
        console.error('Microphone access denied');
      }
    }
  };

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setAttachedFile(file);
      e.target.value = '';
    }
  };

  const canSubmit = (query.trim().length > 0 || attachedFile !== null) && !isLoading;

  return (
    <motion.div layout className="w-full max-w-[740px] mx-auto">
      {/* Attached file chip */}
      <AnimatePresence>
        {attachedFile && (
          <motion.div
            initial={{ opacity: 0, y: 6, height: 0 }}
            animate={{ opacity: 1, y: 0, height: 'auto' }}
            exit={{ opacity: 0, y: -4, height: 0 }}
            className="mb-2"
          >
            <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-100 dark:bg-black border border-slate-200 dark:border-neutral-800 text-xs text-slate-600 dark:text-neutral-300">
              <FileText size={13} className="text-cyan-500" />
              <span className="truncate max-w-[200px]">{attachedFile.name}</span>
              <button
                onClick={() => setAttachedFile(null)}
                className="ml-1 text-slate-400 dark:text-neutral-400 hover:text-slate-700 dark:hover:text-white transition-colors"
              >
                <X size={13} />
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Main pill input container highlighted with distinct border & subtle glow */}
      <div className="
        bg-white dark:bg-black rounded-full 
        border border-slate-300/90 dark:border-neutral-800 hover:border-blue-500/70 dark:hover:border-blue-500/80 focus-within:border-blue-600 dark:focus-within:border-blue-500
        ring-1 ring-slate-900/5 dark:ring-neutral-800 hover:ring-2 hover:ring-blue-500/10 focus-within:ring-3 focus-within:ring-blue-500/20
        shadow-[0_8px_30px_rgba(15,23,42,0.07),0_2px_6px_rgba(15,23,42,0.04)]
        dark:shadow-[0_0_16px_rgba(59,130,246,0.18)]
        hover:shadow-[0_12px_36px_rgba(37,99,235,0.12),0_4px_12px_rgba(15,23,42,0.05)]
        dark:hover:shadow-[0_0_22px_rgba(59,130,246,0.28)]
        focus-within:shadow-[0_14px_44px_rgba(37,99,235,0.22),0_4px_12px_rgba(15,23,42,0.06)]
        dark:focus-within:shadow-[0_0_28px_rgba(59,130,246,0.35)]
        transition-all duration-300
      ">
        <div className="flex items-center gap-1.5 sm:gap-2 px-2.5 sm:px-4 py-1.5 sm:py-2.5">
          {/* Left action buttons */}
          <div className="flex items-center gap-0.5 sm:gap-1">
            <input
              type="file"
              ref={fileInputRef}
              onChange={handleFileChange}
              accept=".pdf,.docx,.doc,.txt,.csv"
              className="hidden"
            />
            <button
              onClick={() => fileInputRef.current?.click()}
              className="p-1.5 sm:p-2 rounded-full text-slate-400 dark:text-neutral-400 hover:text-slate-700 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-neutral-900 transition-all duration-200 cursor-pointer"
              title="Attach document / specification sheet"
            >
              <Paperclip size={15} className="sm:w-[17px] sm:h-[17px]" />
            </button>
            <button
              onClick={toggleRecording}
              className={`p-1.5 sm:p-2 rounded-full transition-all duration-200 cursor-pointer ${
                isRecording
                  ? 'text-red-500 bg-red-50 dark:bg-red-950/40 recording-pulse'
                  : 'text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 hover:bg-blue-50/60 dark:hover:bg-neutral-900'
              }`}
              title={isRecording ? 'Stop recording' : 'Voice search'}
            >
              {isRecording ? (
                <MicOff size={15} className="sm:w-[17px] sm:h-[17px]" />
              ) : (
                <Mic size={15} className="sm:w-[17px] sm:h-[17px]" />
              )}
            </button>
          </div>

          {/* Textarea without square focus outline */}
          <textarea
            ref={textareaRef}
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onInput={handleInput}
            onKeyDown={handleKeyDown}
            placeholder={compact ? "Ask BIS AI..." : "Ask BIS AI — e.g. 'electric kettle safety'..."}
            rows={1}
            disabled={isLoading}
            style={{ outline: 'none', boxShadow: 'none', border: 'none' }}
            className="
              flex-1 bg-transparent resize-none
              text-[12.5px] sm:text-[13.5px] leading-normal text-slate-800 dark:text-neutral-100
              placeholder:text-slate-400 dark:placeholder:text-neutral-500 font-normal
              border-0 outline-none ring-0
              focus:outline-none focus:ring-0 focus:border-0
              py-0.5 sm:py-1
              disabled:opacity-40
            "
          />

          {/* Vibrant Blue Send Button */}
          <button
            onClick={handleSubmit}
            disabled={!canSubmit}
            className={`
              w-8 h-8 sm:w-10 sm:h-10 rounded-full flex items-center justify-center shrink-0
              transition-all duration-200 shadow-md
              ${canSubmit
                ? 'bg-[#2563eb] hover:bg-[#1d4ed8] text-white shadow-blue-500/25 hover:scale-105 active:scale-95 cursor-pointer'
                : 'bg-slate-100 dark:bg-neutral-900 text-slate-300 dark:text-neutral-600 cursor-not-allowed'
              }
            `}
            title="Search Standards"
          >
            <Send size={13} className={`sm:w-[15px] sm:h-[15px] ${canSubmit ? 'translate-x-[1px]' : ''}`} />
          </button>
        </div>
      </div>
    </motion.div>
  );
}
