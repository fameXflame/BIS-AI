export interface StandardResult {
  is_code: string;
  title: string;
  confidence: number;
  confidence_tier: 'high' | 'moderate' | 'low';
  highlight_reason: string;
  key_clauses: string[];
  division?: string;
  year?: number;
  abstract_scope?: string;
  url?: string;
}

export interface SearchResult {
  summary: string;
  query_magnified: string;
  standards: StandardResult[];
}

export interface ChatMessage {
  id: string;
  query: string;
  timestamp: Date;
  result?: SearchResult;
}
