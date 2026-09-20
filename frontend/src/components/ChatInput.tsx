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
    <motion.div layout className="w-full max-w-[680px] mx-auto">
      {/* Attached file chip */}
      <AnimatePresence>
        {attachedFile && (
          <motion.div
            initial={{ opacity: 0, y: 6, height: 0 }}
            animate={{ opacity: 1, y: 0, height: 'auto' }}
            exit={{ opacity: 0, y: -4, height: 0 }}
            className="mb-2"
          >
            <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-slate-100 border border-slate-200 text-xs text-slate-600">
              <FileText size={13} className="text-cyan-500" />
              <span className="truncate max-w-[200px]">{attachedFile.name}</span>
              <button
                onClick={() => setAttachedFile(null)}
                className="ml-1 text-slate-400 hover:text-slate-700 transition-colors"
              >
                <X size={13} />
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Main input container */}
      <div className="glass-input rounded-2xl">
        <div className="flex items-end gap-1 p-2.5">
          {/* Left action buttons */}
          <div className="flex items-center gap-0.5 pb-[3px]">
            <input
              type="file"
              ref={fileInputRef}
              onChange={handleFileChange}
              accept=".pdf,.docx,.doc,.txt,.csv"
              className="hidden"
            />
            <button
              onClick={() => fileInputRef.current?.click()}
              className="p-1.5 rounded-lg text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-all duration-200"
              title="Attach document"
            >
              <Paperclip size={16} />
            </button>
            <button
              onClick={toggleRecording}
              className={`p-1.5 rounded-lg transition-all duration-200 ${
                isRecording
                  ? 'text-red-400 bg-red-500/10 recording-pulse'
                  : 'text-slate-400 hover:text-slate-600 hover:bg-slate-100'
              }`}
              title={isRecording ? 'Stop recording' : 'Voice input'}
            >
              {isRecording ? <MicOff size={16} /> : <Mic size={16} />}
            </button>
          </div>

          {/* Textarea */}
          <textarea
            ref={textareaRef}
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onInput={handleInput}
            onKeyDown={handleKeyDown}
            placeholder="Ask about BIS standards — try 'electric kettle manufacturing requirements'..."
            rows={1}
            disabled={isLoading}
            className="
              flex-1 bg-transparent resize-none
              text-[13px] leading-relaxed text-slate-800
              placeholder:text-slate-400
              outline-none
              min-h-[32px] py-1.5
              disabled:opacity-40
            "
          />

          {/* Send button */}
          <button
            onClick={handleSubmit}
            disabled={!canSubmit}
            className={`
              p-2 rounded-xl mb-[1px]
              transition-all duration-200
              ${canSubmit
                ? 'bg-gradient-to-r from-cyan-500/70 to-blue-500/70 text-white shadow-lg shadow-cyan-500/15 hover:from-cyan-400/80 hover:to-blue-400/80 hover:shadow-cyan-500/25'
                : 'bg-slate-100 text-slate-300 cursor-not-allowed'
              }
            `}
          >
            <Send size={14} />
          </button>
        </div>
      </div>
    </motion.div>
  );
}
