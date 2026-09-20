export interface StandardResult {
  is_code: string;
  title: string;
  confidence: number;
  confidence_tier: 'high' | 'moderate' | 'low';
  highlight_reason: string;
  key_clauses: string[];
  division?: string;
  year?: number | string;
  abstract_scope?: string;
  scope?: string;
  mandatory?: boolean;
  test_requirements?: string;
  certification_process?: string;
  url?: string;
}

export interface SearchResult {
  summary: string;
  query_magnified: string;
  is_bis_related?: boolean;
  ai_walkalong?: string;
  standards: StandardResult[];
}

export interface ChatMessage {
  id: string;
  query: string;
  timestamp: Date;
  result?: SearchResult;
}
