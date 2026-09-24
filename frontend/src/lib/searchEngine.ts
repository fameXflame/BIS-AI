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
 * Intelligent contextual response generator for queries outside indexed datasets
 */
export function generateSmartFallbackSummary(rawQuery: string): string {
  const q = rawQuery.trim().toLowerCase();

  // Food / Agriculture / Bakery / Dairy / Honey / Spices / Water
  if (/\b(food|bakery|biscuit|bread|milk|dairy|oil|tea|coffee|spice|honey|water|packaged drinking|rice|wheat|flour|sugar|grain)\b/i.test(q)) {
    return `In India, food commodities and commercial food processing are regulated under Food Safety and Standards Authority of India (FSSAI) guidelines, supported by dedicated BIS standards for raw material purity, hygiene, and packaging safety.`;
  }

  // Electronics / IT / Telecom / Battery / Mobile / Gadgets / Software / AI
  if (/\b(phone|mobile|laptop|computer|software|ai|battery|charger|gadget|camera|display|cable|wire|electronic|it|telecom|smart|watch)\b/i.test(q)) {
    return `Electronic and IT equipment are governed by the Compulsory Registration Scheme (CRS) administered by MeitY and BIS, enforcing safety benchmarks (such as IS 13252 for equipment safety and IS 16046 for lithium battery cells) prior to commercial sale.`;
  }

  // Automotive / Vehicles / Mobility / Helmets / Tyres
  if (/\b(car|bike|motorcycle|vehicle|auto|automotive|ev|electric vehicle|helmet|tyre|tire|brake|airbag)\b/i.test(q)) {
    return `Automotive assemblies, EVs, and personal mobility safety equipment follow Automotive Industry Standards (AIS) and mandatory BIS safety certifications, such as IS 4151 for motorcycle helmets and IS 15633 for pneumatic tires.`;
  }

  // Toys / Children / Games
  if (/\b(toy|toys|game|doll|puzzle|baby|infant|child|children)\b/i.test(q)) {
    return `All toys in India fall under mandatory BIS Quality Control Orders (QCOs), requiring strict conformity to IS 9873 (mechanical, flammability, and heavy metal safety) and IS 15644 (safety of electric toys).`;
  }

  // Pharma / Medical / Health / Cosmetics
  if (/\b(medicine|drug|pharma|medical|health|hospital|doctor|cosmetic|soap|detergent|shampoo|skincare)\b/i.test(q)) {
    return `Pharmaceuticals and medical devices in India are regulated under CDSCO and the Medical Device Rules, while cosmetics and personal hygiene products follow BIS formulation limits (such as IS 4707 for cosmetic safety).`;
  }

  // Steel / Metals / Construction / Cement / Pipes / Plumbing
  if (/\b(steel|iron|metal|pipe|tube|tmt|rebar|cement|concrete|brick|plywood|wood|timber|glass|roof|building|construction)\b/i.test(q)) {
    return `Construction and structural materials in India operate under mandatory BIS Quality Control Orders (including IS 1786 for high-strength steel rebars and IS 2062 for structural steel) to ensure structural safety under the National Building Code.`;
  }

  // Textiles / Apparel / Garments
  if (/\b(textile|fabric|cloth|cotton|silk|wool|garment|apparel|yarn|mask|ppes)\b/i.test(q)) {
    return `Textiles and protective apparel are standardized by the BIS Textile Division (TXD), covering tensile strength, colorfastness, and mandatory QCOs for technical textiles and geotextiles.`;
  }

  // Procedures / Licensing / ISI mark / Hallmark / HUID / CRS / Certification
  if (/\b(license|licence|certificate|certification|isi mark|hallmark|huid|apply|process|fee|cost|registration|manakonline)\b/i.test(q)) {
    return `To obtain BIS certification (ISI mark or CRS registration), manufacturers must apply through the Manakonline portal, submit standard test certificates from BIS-recognized labs, and fulfill designated factory quality audit schemes.`;
  }

  // Questions (what, how, why, can, does, is, where, who)
  if (/^(what|how|why|can|does|is|where|who|which)\b/i.test(q)) {
    return `Regarding "${rawQuery.trim()}": Indian Standards define exact engineering tolerances, product safety thresholds, and quality benchmarks for manufacturing. While this inquiry may span multiple cross-sectoral guidelines, the BIS standards catalog outlines the applicable specifications.`;
  }

  // General catch-all for any other keyword
  return `Regarding "${rawQuery.trim()}": Manufacturing and quality benchmarks for this sector in India are guided by BIS technical committee standards and national Quality Control Orders to ensure consumer safety and product reliability.`;
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

  // If no match found or query is out of scope / greeting, do NOT default to kettle!
  if (highestScore <= 0 || !bestTopic) {
    const isGreeting = /^(hi+|hello+|hey+|hola|howdy|namaste|greetings)\b/i.test(query);
    if (isGreeting) {
      return {
        summary: "Hello! I am BIS AI — your search engine for Bureau of Indian Standards (BIS) regulations, product safety norms, and manufacturing compliance.",
        query_magnified: "",
        is_bis_related: false,
        ai_walkalong: "Search for any manufactured product or IS code to discover applicable Indian Standards, mandatory test protocols, and certification roadmaps.",
        standards: [],
      };
    }

    return {
      summary: generateSmartFallbackSummary(rawQuery),
      query_magnified: "",
      is_bis_related: false,
      ai_walkalong: "Try searching by a specific product category (such as paints, cement, electric kettles, drinking water, or solar modules) or enter an IS code directly.",
      standards: [],
    };
  }

  const chosenTopic = bestTopic;
  const clonedData: SearchResult = JSON.parse(JSON.stringify(chosenTopic.data));
  clonedData.is_bis_related = true;

  // Dynamic re-ranking: if user specifically asked for a sub-topic
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
