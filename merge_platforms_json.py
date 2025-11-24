import json
import re
from typing import Dict, Any, Optional

def has_test_cases_codeforces(problem: Dict[str, Any]) -> bool:
    """Check if a Codeforces problem has test cases (N.in and N.ans fields)"""
    return any(key.endswith('.in') for key in problem.keys())

def has_test_cases_kattis(problem: Dict[str, Any]) -> bool:
    """Check if a Kattis problem has test cases in the files object"""
    if 'files' not in problem or not problem['files']:
        return False
    
    # Check if any file zip contains test cases
    for file_data in problem['files'].values():
        if any(key.endswith('.in') for key in file_data.keys()):
            return True
    return False

def flatten_kattis_test_cases(problem: Dict[str, Any]) -> Dict[str, str]:
    """Flatten Kattis test cases from nested files structure to flat structure"""
    test_cases = {}
    
    if 'files' in problem and problem['files']:
        for file_data in problem['files'].values():
            for key, value in file_data.items():
                if key.endswith('.in') or key.endswith('.ans'):
                    test_cases[key] = value
    
    return test_cases

def extract_year_from_string(text: str) -> Optional[int]:
    """Extract a 4-digit year from a string (e.g., '2025' from 'Competition 2025')"""
    if not text:
        return None
    
    # Look for 4-digit years (1900-2099)
    match = re.search(r'\b(19|20)\d{2}\b', text)
    if match:
        return int(match.group(0))
    return None

def normalize_kattis_problem(problem_id: str, problem: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize a Kattis problem to match the expected structure"""
    normalized = {
        'id': problem_id,
        'title': problem.get('title'),  # Kattis might not have this, will be null
        'contest': problem.get('source'),  # Map source to contest
        'year': extract_year_from_string(problem.get('source', '')),
        'rating': None,  # Kattis doesn't have rating
        'tags': problem.get('tags', []),  # Keep tags if they exist
        'url': f"https://open.kattis.com/problems/{problem_id}",
        'difficulty': problem.get('difficulty'),  # Keep Kattis numeric difficulty
        'category': problem.get('category'),
        'source': problem.get('source'),
        'text': problem.get('text'),
        'cpu': problem.get('cpu'),
        'memory': problem.get('memory')
    }
    
    # Add flattened test cases
    test_cases = flatten_kattis_test_cases(problem)
    normalized.update(test_cases)
    
    return normalized

def process_codeforces(data: Dict[str, Any]) -> tuple[Dict[str, Any], int, int]:
    """Process Codeforces problems, filtering out those without text or test cases"""
    processed = {}
    omitted = 0
    total = len(data)
    
    for problem_id, problem in data.items():
        # Check if text is null or no test cases exist
        if problem.get('text') is None:
            print(f"  ⚠️  Omitting Codeforces {problem_id}: text is null")
            omitted += 1
            continue
        
        if not has_test_cases_codeforces(problem):
            print(f"  ⚠️  Omitting Codeforces {problem_id}: no test cases found")
            omitted += 1
            continue
        
        processed[problem_id] = problem
    
    return processed, total, omitted

def process_kattis(data: Dict[str, Any]) -> tuple[Dict[str, Any], int, int]:
    """Process Kattis problems, filtering and normalizing"""
    processed = {}
    omitted = 0
    total = len(data)
    
    for problem_id, problem in data.items():
        # Check if no test cases exist
        if not has_test_cases_kattis(problem):
            print(f"  ⚠️  Omitting Kattis {problem_id}: no test cases found")
            omitted += 1
            continue
        
        # Normalize the problem structure
        normalized = normalize_kattis_problem(problem_id, problem)
        processed[problem_id] = normalized
    
    return processed, total, omitted

def check_id_collisions(cf_data: Dict[str, Any], kattis_data: Dict[str, Any]) -> None:
    """Check for ID collisions between datasets"""
    cf_ids = set(cf_data.keys())
    kattis_ids = set(kattis_data.keys())
    collisions = cf_ids & kattis_ids
    
    if collisions:
        print(f"\n⚠️  WARNING: Found {len(collisions)} ID collision(s):")
        for collision_id in collisions:
            print(f"    - {collision_id} exists in both datasets (skipping Kattis version)")
        print()

def merge_datasets(cf_path: str, kattis_path: str, output_path: str):
    """Main function to merge Codeforces and Kattis datasets"""
    
    print("="*70)
    print("🔗 DATASET MERGER - Codeforces + Kattis")
    print("="*70)
    
    # Load datasets
    print("\n📖 Loading datasets...")
    with open(cf_path, 'r', encoding='utf-8') as f:
        cf_data = json.load(f)
    print(f"  ✓ Loaded {len(cf_data)} Codeforces problems")
    
    with open(kattis_path, 'r', encoding='utf-8') as f:
        kattis_data = json.load(f)
    print(f"  ✓ Loaded {len(kattis_data)} Kattis problems")
    
    # Process Codeforces
    print("\n🔍 Processing Codeforces problems...")
    cf_processed, cf_total, cf_omitted = process_codeforces(cf_data)
    print(f"  ✓ Kept {len(cf_processed)}/{cf_total} problems ({cf_omitted} omitted)")
    
    # Process Kattis
    print("\n🔍 Processing Kattis problems...")
    kattis_processed, kattis_total, kattis_omitted = process_kattis(kattis_data)
    print(f"  ✓ Kept {len(kattis_processed)}/{kattis_total} problems ({kattis_omitted} omitted)")
    
    # Check for collisions
    print("\n🔎 Checking for ID collisions...")
    check_id_collisions(cf_processed, kattis_processed)
    
    # Remove collisions from Kattis (keep Codeforces version)
    collision_ids = set(cf_processed.keys()) & set(kattis_processed.keys())
    for collision_id in collision_ids:
        del kattis_processed[collision_id]
    
    # Create merged dataset with separate sections
    merged = {
        'codeforces': cf_processed,
        'kattis': kattis_processed
    }
    
    # Save merged dataset
    print(f"💾 Saving merged dataset to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)
    
    # Summary
    print("\n" + "="*70)
    print("✅ MERGE COMPLETE!")
    print("="*70)
    print(f"📊 Final Statistics:")
    print(f"  • Codeforces problems: {len(cf_processed)}")
    print(f"  • Kattis problems: {len(kattis_processed)}")
    print(f"  • Total problems: {len(cf_processed) + len(kattis_processed)}")
    print(f"  • Total omitted: {cf_omitted + kattis_omitted + len(collision_ids)}")
    print("="*70)

if __name__ == '__main__':
    # Configuration
    CODEFORCES_JSON = 'codeforces_problems_2025.json'
    KATTIS_JSON = 'kattis_problems_2025.json'
    OUTPUT_JSON = 'merged_problems.json'
    
    # Run merge
    merge_datasets(CODEFORCES_JSON, KATTIS_JSON, OUTPUT_JSON)