const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function searchStandards(query: string, filters?: Record<string, unknown>) {
  const res = await fetch(`${API_BASE}/api/search`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, filters }),
  });
  if (!res.ok) throw new Error(`Search failed: ${res.statusText}`);
  return res.json();
}

export async function uploadFile(file: File) {
  const formData = new FormData();
  formData.append('file', file);
  const res = await fetch(`${API_BASE}/api/upload-file`, {
    method: 'POST',
    body: formData,
  });
  if (!res.ok) throw new Error(`Upload failed: ${res.statusText}`);
  return res.json();
}

export async function transcribeAudio(blob: Blob) {
  const formData = new FormData();
  formData.append('file', blob, 'recording.webm');
  const res = await fetch(`${API_BASE}/api/transcribe-audio`, {
    method: 'POST',
    body: formData,
  });
  if (!res.ok) throw new Error(`Transcription failed: ${res.statusText}`);
  return res.json();
}

export async function getStandardDetail(isCode: string) {
  const res = await fetch(`${API_BASE}/api/standard/${encodeURIComponent(isCode)}`);
  if (!res.ok) throw new Error(`Detail fetch failed: ${res.statusText}`);
  return res.json();
}
