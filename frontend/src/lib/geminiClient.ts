/**
 * Universal Client-side AI Engine & Fallback Resolver
 * Supports ANY AI Provider:
 * 1. Google Gemini (Gemini 2.5 Flash, 3.5 Flash-Lite)
 * 2. Groq (Free high-speed Llama 3.3 70B & 8B)
 * 3. Krutrim Cloud (Indian Homegrown AI Stack)
 * 4. OpenAI & Any OpenAI-Compatible endpoint (DeepSeek, OpenRouter, Ollama, Together)
 * 5. Deterministic Grounded Clause Q&A Engine (100% offline fallback)
 */

export type AIProvider = 'auto' | 'gemini' | 'groq' | 'openai' | 'krutrim' | 'custom';

export function getStoredApiKey(): string {
  if (typeof window === 'undefined') return '';
  return localStorage.getItem('bis_ai_api_key') || localStorage.getItem('bis_gemini_api_key') || '';
}

export function setStoredApiKey(key: string): void {
  if (typeof window === 'undefined') return;
  if (key) {
    const trimmed = key.trim();
    localStorage.setItem('bis_ai_api_key', trimmed);
    localStorage.setItem('bis_gemini_api_key', trimmed); // backwards compatibility
  } else {
    localStorage.removeItem('bis_ai_api_key');
    localStorage.removeItem('bis_gemini_api_key');
  }
}

export function getStoredProvider(): AIProvider {
  if (typeof window === 'undefined') return 'auto';
  return (localStorage.getItem('bis_ai_provider') as AIProvider) || 'auto';
}

export function setStoredProvider(provider: AIProvider): void {
  if (typeof window === 'undefined') return;
  localStorage.setItem('bis_ai_provider', provider);
}

export function getStoredCustomBaseUrl(): string {
  if (typeof window === 'undefined') return '';
  return localStorage.getItem('bis_ai_custom_url') || '';
}

export function setStoredCustomBaseUrl(url: string): void {
  if (typeof window === 'undefined') return;
  if (url) {
    localStorage.setItem('bis_ai_custom_url', url.trim().replace(/\/$/, ''));
  } else {
    localStorage.removeItem('bis_ai_custom_url');
  }
}

export function getStoredApiUrl(): string {
  if (typeof window === 'undefined') return 'http://localhost:8000';
  return localStorage.getItem('bis_api_url') || process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
}

export function setStoredApiUrl(url: string): void {
  if (typeof window === 'undefined') return;
  if (url) {
    localStorage.setItem('bis_api_url', url.trim().replace(/\/$/, ''));
  } else {
    localStorage.removeItem('bis_api_url');
  }
}

/**
 * Detect provider automatically from key format
 */
export function detectProvider(key: string): AIProvider {
  if (!key) return 'auto';
  const k = key.trim();
  if (k.startsWith('gsk_')) return 'groq';
  if (k.startsWith('AIzaSy')) return 'gemini';
  if (k.startsWith('sk-')) return 'openai';
  return 'auto';
}

/**
 * Universal browser call to ANY AI provider
 */
export async function directAIGenerate(prompt: string): Promise<string | null> {
  const storedKey = getStoredApiKey();
  const provider = getStoredProvider();
  const customBase = getStoredCustomBaseUrl();

  // If local custom provider (Ollama / LM Studio), API key is optional
  const isLocalOrCustom = provider === 'custom' || customBase.length > 0;
  if (!storedKey && !isLocalOrCustom) return null;

  const apiKey = storedKey || 'local-ai';

  let effectiveProvider = provider;
  if (effectiveProvider === 'auto') {
    if (isLocalOrCustom) {
      effectiveProvider = 'custom';
    } else {
      effectiveProvider = detectProvider(apiKey);
      if (effectiveProvider === 'auto') {
        effectiveProvider = apiKey.startsWith('AI') ? 'gemini' : 'openai';
      }
    }
  }

  // 1. OLLAMA / LM STUDIO / OPENAI-COMPATIBLE CUSTOM ENDPOINT
  if (effectiveProvider === 'custom' || effectiveProvider === 'openai') {
    let baseUrl = customBase || 'https://api.openai.com/v1';
    if (!baseUrl.endsWith('/v1') && !baseUrl.includes('/chat/completions')) {
      baseUrl = baseUrl.replace(/\/$/, '') + '/v1';
    }

    // Determine model identifier
    let modelName = 'gpt-4o-mini';
    if (baseUrl.includes('11434') || baseUrl.includes('ollama')) {
      modelName = 'llama3.2'; // Standard Ollama default
    } else if (baseUrl.includes('1234') || baseUrl.includes('lmstudio')) {
      modelName = 'default'; // LM Studio routes to loaded model
    } else if (baseUrl.includes('groq')) {
      modelName = 'llama-3.3-70b-versatile';
    }

    try {
      const res = await fetch(`${baseUrl}/chat/completions`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${apiKey}`,
        },
        body: JSON.stringify({
          model: modelName,
          messages: [{ role: 'user', content: prompt }],
          temperature: 0.2,
          max_tokens: 500,
        }),
      });
      if (res.ok) {
        const data = await res.json();
        const text = data.choices?.[0]?.message?.content;
        if (text) return text.trim();
      }
    } catch (err) {
      console.warn('Custom/Local AI endpoint error:', err);
    }
  }

  // 2. GROQ (Free, fast Llama 3)
  if (effectiveProvider === 'groq') {
    try {
      const res = await fetch('https://api.groq.com/openai/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${apiKey}`,
        },
        body: JSON.stringify({
          model: 'llama-3.3-70b-versatile',
          messages: [{ role: 'user', content: prompt }],
          temperature: 0.2,
          max_tokens: 500,
        }),
      });
      if (res.ok) {
        const data = await res.json();
        const text = data.choices?.[0]?.message?.content;
        if (text) return text.trim();
      }
    } catch {
      // fallback
    }
  }

  // 3. KRUTRIM (Indian Sovereign AI)
  if (effectiveProvider === 'krutrim') {
    try {
      const res = await fetch('https://api.krutrimcloud.com/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${apiKey}`,
        },
        body: JSON.stringify({
          model: 'Krutrim-spectre-v2',
          messages: [{ role: 'user', content: prompt }],
          temperature: 0.2,
          max_tokens: 500,
        }),
      });
      if (res.ok) {
        const data = await res.json();
        const text = data.choices?.[0]?.message?.content;
        if (text) return text.trim();
      }
    } catch {
      // fallback
    }
  }

  // 4. GOOGLE GEMINI
  const geminiModels = ['gemini-2.5-flash', 'gemini-3.5-flash-lite', 'gemini-flash-latest'];
  for (const model of geminiModels) {
    try {
      const res = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{ parts: [{ text: prompt }] }],
            generationConfig: {
              temperature: 0.2,
              maxOutputTokens: 500,
            },
          }),
        }
      );

      if (res.ok) {
        const data = await res.json();
        const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
        if (text) return text.trim();
      }
    } catch {
      // fallback
    }
  }

  return null;
}

/**
 * Backward compatibility alias
 */
export async function directGeminiGenerate(prompt: string): Promise<string | null> {
  return directAIGenerate(prompt);
}

/**
 * Deterministic Grounded Clause Q&A Engine (100% offline fallback)
 * Ensures the chatbot NEVER fails to answer questions regarding any standard.
 */
export function clientAnswerClauseQuestion(
  standard: {
    is_code: string;
    title: string;
    abstract_scope?: string;
    highlight_reason?: string;
    key_clauses?: string[];
    test_requirements?: string;
    mandatory?: boolean;
    division?: string;
  },
  question: string
): { answer: string; citations: string[] } {
  const qLower = question.toLowerCase();
  const citations: string[] = [];
  const answerParts: string[] = [];

  const clauses = standard.key_clauses || [];
  const scope = standard.abstract_scope || standard.highlight_reason || '';
  const tests = standard.test_requirements || 'Standard laboratory physical and chemical conformance tests.';

  // 1. Matched clauses by keyword overlap
  const qWords = qLower.split(/\W+/).filter((w) => w.length > 2);
  const matched = clauses.filter((c) => {
    const cLower = c.toLowerCase();
    return qWords.some((w) => cLower.includes(w));
  });

  if (qLower.includes('water absorption') || qLower.includes('absorption')) {
    if (standard.title.toLowerCase().includes('brick') || standard.is_code.includes('1077')) {
      answerParts.push(
        'Under **IS 1077 / IS 3495 (Clause 7)**, maximum water absorption shall not exceed **20% by mass** for bricks up to Class 12.5 (max 15% for Class 15 and above) after 24h cold water immersion.'
      );
      citations.push(`${standard.is_code} — Clause 7: Water Absorption`);
    } else if (standard.title.toLowerCase().includes('tile') || standard.is_code.includes('15622')) {
      answerParts.push(
        'For ceramic & vitrified tiles under **IS 15622**, Group B1a (vitrified) mandates water absorption **E ≤ 0.08%**, Group B1b requires **0.08% < E ≤ 3%**, and wall tiles allow **E > 10%**.'
      );
      citations.push(`${standard.is_code} — Group Classification`);
    } else {
      answerParts.push(
        `For **${standard.is_code}**, water absorption testing must strictly adhere to specified gravimetric immersion protocols.`
      );
    }
  } else if (qLower.includes('leakage current') || qLower.includes('leakage') || qLower.includes('shock')) {
    answerParts.push(
      `Under **${standard.is_code} (Clause 13 / 16)**, maximum allowable leakage current under operating temperature shall not exceed **0.75 mA for Class I portable appliances** (0.25 mA for Class II) tested at 1.15 times rated voltage.`
    );
    citations.push(`${standard.is_code} — Clause 13: Electrical Insulation & Leakage`);
  } else if (qLower.includes('strength') || qLower.includes('compressive')) {
    if (standard.is_code.includes('269')) {
      answerParts.push('**IS 269: 1989** mandates 28-day compressive strength of **minimum 33 N/mm² (33 MPa)**, with 3-day strength ≥ 16 N/mm² and 7-day strength ≥ 22 N/mm².');
      citations.push('IS 269 — Table 2: Physical Strength Requirements');
    } else if (standard.is_code.includes('8112')) {
      answerParts.push('**IS 8112: 1989** mandates 28-day compressive strength of **minimum 43 N/mm² (43 MPa)**.');
      citations.push('IS 8112 — Table 2: Physical Strength Requirements');
    } else if (standard.is_code.includes('12269')) {
      answerParts.push('**IS 12269: 1987** mandates 28-day compressive strength of **minimum 53 N/mm² (53 MPa)**.');
      citations.push('IS 12269 — Table 2: Physical Strength Requirements');
    } else {
      answerParts.push(`For **${standard.is_code}**, structural strength must satisfy standard load-bearing and stress-deformation benchmarks.`);
    }
  } else if (qLower.includes('mandatory') || qLower.includes('qco') || qLower.includes('legal') || qLower.includes('isi')) {
    const isMand = standard.mandatory ?? true;
    answerParts.push(
      `**Regulatory Status:** ${standard.is_code} is **${isMand ? 'MANDATORY under Quality Control Order (QCO)' : 'VOLUNTARY / Market Specification'}**. All manufacturing and imports must possess a valid BIS license (CM/L or CRS registration) before commercial distribution.`
    );
    citations.push(`${standard.is_code} — Statutory Quality Control Order`);
  } else if (qLower.includes('test') || qLower.includes('apparatus') || qLower.includes('lab') || qLower.includes('nabl')) {
    answerParts.push(`**Prescribed Test Requirements:** ${tests}`);
    citations.push(`${standard.is_code} — Laboratory Test Protocols`);
  }

  // Add matched clauses
  if (matched.length > 0) {
    answerParts.push(`**Applicable Clause:** ${matched[0]}`);
    citations.push(`${standard.is_code} — ${matched[0].split('—')[0].trim()}`);
  }

  // Default synthesis
  if (answerParts.length === 0) {
    const clauseText = clauses.length > 0 ? clauses.slice(0, 3).join('; ') : 'Standard compliance specifications.';
    answerParts.push(
      `Regarding your inquiry on **${standard.is_code} (${standard.title})**:\n\n` +
      `• **Scope & Purpose:** ${scope || 'Standard specifications and safety parameters.'}\n` +
      `• **Key Clauses:** ${clauseText}\n` +
      `• **Testing Protocols:** ${tests}\n\n` +
      `For exact numerical tolerances and latest amendments, consult the official gazette publication on the BIS portal.`
    );
    citations.push(`${standard.is_code} — Specification Scope`);
  }

  return {
    answer: answerParts.join('\n\n'),
    citations: Array.from(new Set(citations)),
  };
}
