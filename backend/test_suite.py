import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

test_queries = [
    'plastic chairs for schools',
    'electric kettle manufacturing',
    'wine factory requirements',
    'deodrant manufacturing'
]

for q in test_queries:
    r = requests.post('http://localhost:8000/api/search', json={'query': q}).json()
    print('=' * 60)
    print(f'QUERY: {q}')
    print('Walk-along:', r.get('ai_walkalong'))
    print(f"Total Standards: {r.get('total_results')}")
    for s in r.get('standards', [])[:4]:
        print(f"  * {s['is_code']} ({s['confidence']}%) — {s['title']}")
