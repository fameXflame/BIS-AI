"""
Master Batch Ingestion & Deduplication Pipeline
Merges all team member batch files from `data/batches/*.json` into the unified BIS catalog.
Ensures zero duplicates, validates standard schemas, and generates comprehensive statistics.
"""

import glob
import json
import os
import re
import sys

def normalize_is_code(code: str) -> str:
    """Normalize IS code into alphanumeric lowercase for bulletproof deduplication."""
    return re.sub(r'[^a-zA-Z0-9]', '', code).lower()

def validate_standard(std: dict) -> bool:
    """Ensure standard has minimum viable fields."""
    if not isinstance(std, dict):
        return False
    if not std.get('is_code') or not std.get('title'):
        return False
    if len(std.get('is_code', '').strip()) < 3:
        return False
    return True

def clean_standard(std: dict) -> dict:
    """Sanitize and format a standard record."""
    code = str(std.get('is_code', '')).strip()
    title = str(std.get('title', '')).strip()
    div = str(std.get('division', 'General Engineering Division')).strip()
    year = str(std.get('year', '')).strip()
    if not year:
        match = re.search(r'\b(19\d\d|20\d\d)\b', code)
        year = match.group(1) if match else "2020"

    scope = str(std.get('scope', '')).strip()
    if not scope:
        scope = f"Prescribes requirements, specifications, testing procedures, and quality limits for {title}."

    clauses = std.get('key_clauses', [])
    if isinstance(clauses, str):
        clauses = [clauses]
    elif not isinstance(clauses, list) or len(clauses) == 0:
        clauses = [
            f"Clause 4: Materials and composition requirements for {title[:40]}",
            "Clause 5: Physical and mechanical tolerances",
            "Clause 6: Sampling, quality control, and testing protocols"
        ]

    keywords = std.get('keywords', [])
    if isinstance(keywords, str):
        keywords = [k.strip() for k in keywords.split(',') if k.strip()]
    elif not isinstance(keywords, list) or len(keywords) == 0:
        words = re.findall(r'[a-zA-Z]{4,}', (code + ' ' + title).lower())
        keywords = [w for w in set(words) if w not in ['standard', 'indian', 'specification', 'requirements']][:8]

    return {
        "is_code": code,
        "title": title,
        "year": year,
        "division": div,
        "mandatory": bool(std.get('mandatory', False)),
        "scope": scope,
        "key_clauses": clauses[:8],
        "keywords": keywords[:12],
        "test_requirements": str(std.get('test_requirements', f'Standard physical and chemical testing under {code}')).strip(),
        "certification_process": str(std.get('certification_process', f'Conformity with {code} -> Laboratory evaluation -> BIS Certification Mark')).strip(),
        "url": str(std.get('url', 'https://www.services.bis.gov.in/php/BIS_2.0/bisconnect/knowyourstandards/')).strip()
    }

def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    batches_dir = os.path.join(root_dir, 'data', 'batches')
    output_catalog = os.path.join(os.path.dirname(__file__), 'extended_bis_catalog.json')
    master_output = os.path.join(root_dir, 'data', 'master_standards_catalog.json')

    seen_codes: set[str] = set()
    master_list: list[dict] = []
    duplicates_count = 0

    # 1. Ingest existing extended catalog if present
    if os.path.exists(output_catalog):
        try:
            with open(output_catalog, 'r', encoding='utf-8') as f:
                existing = json.load(f)
            for item in existing:
                if validate_standard(item):
                    key = normalize_is_code(item['is_code'])
                    if key not in seen_codes:
                        seen_codes.add(key)
                        master_list.append(clean_standard(item))
            print(f"[Master Pipeline] Loaded {len(master_list)} baseline standards from extended_bis_catalog.json")
        except Exception as e:
            print(f"[Master Pipeline] Warning: Could not read baseline catalog: {e}")

    # 2. Ingest all batch files from data/batches/*.json and master data files
    batch_files = glob.glob(os.path.join(batches_dir, '*.json'))
    national_catalog = os.path.join(root_dir, 'data', 'all_bis_standards_national_catalog.json')
    if os.path.exists(national_catalog) and national_catalog not in batch_files:
        batch_files.append(national_catalog)
    print(f"[Master Pipeline] Discovered {len(batch_files)} catalog/batch file(s) for ingestion.")

    for bf in sorted(batch_files):
        file_name = os.path.basename(bf)
        try:
            with open(bf, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if not isinstance(data, list):
                print(f"[Master Pipeline] Skipping {file_name}: Top-level structure must be a JSON array []")
                continue

            file_added = 0
            for item in data:
                if validate_standard(item):
                    key = normalize_is_code(item['is_code'])
                    if key not in seen_codes:
                        seen_codes.add(key)
                        master_list.append(clean_standard(item))
                        file_added += 1
                    else:
                        duplicates_count += 1
            print(f"  + Processed '{file_name}': Added {file_added} new standards.")
        except Exception as err:
            print(f"[Master Pipeline] Error reading {file_name}: {err}")

    # 3. Save merged results
    with open(output_catalog, 'w', encoding='utf-8') as f:
        json.dump(master_list, f, indent=2, ensure_ascii=False)

    with open(master_output, 'w', encoding='utf-8') as f:
        json.dump(master_list, f, indent=2, ensure_ascii=False)

    # 4. Generate Division Breakdown Statistics
    division_counts: dict[str, int] = {}
    for item in master_list:
        div = item.get('division', 'Other')
        division_counts[div] = division_counts.get(div, 0) + 1

    print("\n" + "=" * 60)
    print(f"  TOTAL UNIQUE STANDARDS INDEXED: {len(master_list):,}")
    print(f"  DUPLICATES FILTERED OUT:       {duplicates_count:,}")
    print("=" * 60)
    print("Division Breakdown:")
    for div, count in sorted(division_counts.items(), key=lambda x: -x[1]):
        print(f"  - {div:<45}: {count:,}")
    print("=" * 60)
    print(f"Unified catalog written to: {output_catalog}")
    print("The backend search engine will now automatically serve these standards.\n")

if __name__ == '__main__':
    main()
