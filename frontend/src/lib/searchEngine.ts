import { BIS_TOPIC_DATASETS, TopicData } from './standardsData';
import type { SearchResult, StandardResult } from './types';

/**
 * Stopwords to filter out during query tokenization
 */
const STOPWORDS = new Set([
  'i', 'want', 'to', 'in', 'india', 'what', 'which', 'are', 'the', 'for',
  'how', 'do', 'get', 'it', 'a', 'an', 'and', 'or', 'of', 'on', 'with',
  'is', 'by', 'as', 'at', 'be', 'this', 'that', 'from', 'required', 'applies',
  'apply', 'tell', 'me', 'about', 'find', 'standards', 'standard', 'bis'
]);

/**
 * Tokenize and normalize user input
 */
function tokenize(text: string): string[] {
  return text
    .toLowerCase()
    .replace(/[^\w\s-]/g, ' ')
    .split(/\s+/)
    .filter((word) => word.length > 1 && !STOPWORDS.has(word));
}

/**
 * Intelligent Client-side Search Engine for BIS AI Prototype
 */
export function searchBISStandards(rawQuery: string): SearchResult {
  const query = rawQuery.trim().toLowerCase();
  const tokens = tokenize(query);

  let bestTopic: TopicData | null = null;
  let highestScore = -1;

  // Evaluate matching score against each topic
  for (const topic of Object.values(BIS_TOPIC_DATASETS)) {
    let score = 0;

    // 1. Exact or substring match on sample queries
    for (const sample of topic.sampleQueries) {
      const sampleLower = sample.toLowerCase();
      if (sampleLower === query) {
        score += 100;
      } else if (query.includes(sampleLower) || sampleLower.includes(query)) {
        score += 50;
      }
    }

    // 2. Keyword matching with weighting
    for (const kw of topic.keywords) {
      const kwLower = kw.toLowerCase();
      if (query.includes(kwLower)) {
        score += 25;
      }
      for (const token of tokens) {
        if (kwLower === token) {
          score += 15;
        } else if (kwLower.includes(token) || token.includes(kwLower)) {
          score += 5;
        }
      }
    }

    // 3. IS code direct hit (e.g. "IS 10500" or "IS 800")
    for (const std of topic.data.standards) {
      const isNum = std.is_code.toLowerCase();
      if (query.includes(isNum.split(':')[0].trim())) {
        score += 40;
      }
    }

    if (score > highestScore) {
      highestScore = score;
      bestTopic = topic;
    }
  }

  // Default to electric kettle if score is 0 or query is very generic
  const chosenTopic = (highestScore > 0 && bestTopic) ? bestTopic : BIS_TOPIC_DATASETS.electric_kettle;

  // Deep clone so we can dynamically re-rank / adjust based on specific query nuances
  const clonedData: SearchResult = JSON.parse(JSON.stringify(chosenTopic.data));

  // Dynamic re-ranking: if user specifically asked for a sub-topic
  // e.g. "fire extinguisher" should rank IS 2190 #1
  // e.g. "sprinkler" should rank IS 15105 #1
  // e.g. "TDS" should rank IS 10500 #1
  // e.g. "ductile detailing" should rank IS 13920 #1
  clonedData.standards.forEach((std: StandardResult) => {
    let bonus = 0;
    const stdText = `${std.is_code} ${std.title} ${std.highlight_reason} ${std.abstract_scope || ''}`.toLowerCase();

    for (const token of tokens) {
      if (stdText.includes(token)) {
        bonus += 4;
      }
    }

    // Adjust confidence score dynamically between 45% and 99%
    std.confidence = Math.min(99, Math.max(45, std.confidence + bonus));

    // Update confidence tier
    if (std.confidence >= 80) {
      std.confidence_tier = 'high';
    } else if (std.confidence >= 55) {
      std.confidence_tier = 'moderate';
    } else {
      std.confidence_tier = 'low';
    }
  });

  // Sort standards descending by confidence
  clonedData.standards.sort((a, b) => b.confidence - a.confidence);

  return clonedData;
}
