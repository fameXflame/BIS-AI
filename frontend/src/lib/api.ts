import { getStoredApiUrl } from './geminiClient';

function getApiBase(): string {
  return getStoredApiUrl();
}

export async function searchStandards(query: string, division?: string) {
  const res = await fetch(`${getApiBase()}/api/search`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query,
      division: division && division !== 'All' ? division : undefined,
    }),
  });
  if (!res.ok) throw new Error(`Search failed: ${res.statusText}`);
  return res.json();
}

export async function getDivisions(): Promise<{ division: string; count: number }[]> {
  const res = await fetch(`${getApiBase()}/api/divisions`);
  if (!res.ok) throw new Error(`Failed to fetch divisions: ${res.statusText}`);
  return res.json();
}

export async function uploadFile(file: File) {
  const formData = new FormData();
  formData.append('file', file);
  const res = await fetch(`${getApiBase()}/api/upload-file`, {
    method: 'POST',
    body: formData,
  });
  if (!res.ok) throw new Error(`Upload failed: ${res.statusText}`);
  return res.json();
}

export async function transcribeAudio(blob: Blob) {
  const formData = new FormData();
  formData.append('file', blob, 'recording.webm');
  const res = await fetch(`${getApiBase()}/api/transcribe-audio`, {
    method: 'POST',
    body: formData,
  });
  if (!res.ok) throw new Error(`Transcription failed: ${res.statusText}`);
  return res.json();
}

export async function getStandardDetail(isCode: string) {
  const res = await fetch(`${getApiBase()}/api/standard/${encodeURIComponent(isCode)}`);
  if (!res.ok) throw new Error(`Detail fetch failed: ${res.statusText}`);
  return res.json();
}

export async function exportDossierPdf(query: string, searchResults: any): Promise<Blob> {
  const res = await fetch(`${getApiBase()}/api/export-pdf`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      query,
      search_results: searchResults,
    }),
  });
  if (!res.ok) throw new Error(`PDF Generation failed: ${res.statusText}`);
  return res.blob();
}

export async function compareStandards(standardA: string, standardB: string) {
  const res = await fetch(`${getApiBase()}/api/compare`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      standard_a: standardA,
      standard_b: standardB,
    }),
  });
  if (!res.ok) throw new Error(`Comparison failed: ${res.statusText}`);
  return res.json();
}

export async function askClauseQA(isCode: string, question: string) {
  const res = await fetch(`${getApiBase()}/api/clause-qa`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      is_code: isCode,
      question: question,
    }),
  });
  if (!res.ok) throw new Error(`Clause Q&A failed: ${res.statusText}`);
  return res.json();
}
