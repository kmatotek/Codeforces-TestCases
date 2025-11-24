import json
import os
from pathlib import Path
import re

def normalize_problem_id(json_key):
    """Convert JSON key like '2172-L' to directory name '2172L' or '2172-L'"""
    # Try both formats: with and without hyphen
    return [json_key.replace('-', ''), json_key]

def load_limits(limits_path):
    """Load time and memory limits from limits.json"""
    try:
        with open(limits_path, 'r', encoding='utf-8') as f:
            limits = json.load(f)
            return {
                'cpu': limits.get('time_limit'),
                'memory': limits.get('memory_limit')
            }
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(f"  ⚠️  Error parsing {limits_path}: {e}")
        return None

def load_statement(statement_path):
    """Load problem statement from statement.md, removing the initial header"""
    try:
        with open(statement_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove "# Problem Description" header (case-insensitive, flexible spacing)
            content = re.sub(r'^#\s*Problem\s+Description\s*\n+', '', content, flags=re.IGNORECASE)
            return content.strip()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"  ⚠️  Error reading {statement_path}: {e}")
        return None

def load_test_cases(problem_dir):
    """Load all test cases from tc* directories"""
    test_cases = {}
    tc_dirs = sorted([d for d in problem_dir.iterdir() if d.is_dir() and d.name.startswith('tc')])
    
    for i, tc_dir in enumerate(tc_dirs, 1):
        input_path = tc_dir / 'input.txt'
        output_path = tc_dir / 'output.txt'
        
        try:
            if input_path.exists() and output_path.exists():
                with open(input_path, 'r', encoding='utf-8') as f:
                    test_cases[f'{i}.in'] = f.read()
                with open(output_path, 'r', encoding='utf-8') as f:
                    test_cases[f'{i}.ans'] = f.read()
            else:
                print(f"  ⚠️  Missing input.txt or output.txt in {tc_dir}")
        except Exception as e:
            print(f"  ⚠️  Error reading test case from {tc_dir}: {e}")
    
    return test_cases if test_cases else None

def enrich_problems(json_path, problems_root):
    """Main function to enrich the JSON file with problem data"""
    problems_root = Path(problems_root)
    
    # Load existing JSON
    print(f"📖 Loading JSON from {json_path}...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"✓ Loaded {len(data)} problems\n")
    
    enriched_count = 0
    missing_dirs = []
    
    # Process each problem
    for problem_id, problem_data in data.items():
        print(f"Processing {problem_id}...", end=' ')
        
        # Try to find the problem directory
        possible_names = normalize_problem_id(problem_id)
        problem_dir = None
        
        for name in possible_names:
            candidate = problems_root / name
            if candidate.exists():
                problem_dir = candidate
                break
        
        if not problem_dir:
            print(f"⚠️  Directory not found (tried: {', '.join(possible_names)})")
            missing_dirs.append(problem_id)
            continue
        
        # Load limits
        limits = load_limits(problem_dir / 'limits.json')
        if limits:
            problem_data['cpu'] = limits['cpu']
            problem_data['memory'] = limits['memory']
        else:
            print(f"\n  ⚠️  limits.json not found or invalid")
            problem_data['cpu'] = None
            problem_data['memory'] = None
        
        # Load statement
        statement = load_statement(problem_dir / 'statement.md')
        if statement:
            problem_data['text'] = statement
        else:
            print(f"\n  ⚠️  statement.md not found or invalid")
        
        # Load test cases
        test_cases = load_test_cases(problem_dir)
        if test_cases:
            problem_data.update(test_cases)
        else:
            print(f"\n  ⚠️  No test cases found")
        
        if limits or statement or test_cases:
            enriched_count += 1
            print("✓")
        else:
            print("✗ No data added")
    
    # Save enriched JSON
    print(f"\n💾 Saving enriched data to {json_path}...")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"✅ Enrichment complete!")
    print(f"   - Total problems: {len(data)}")
    print(f"   - Successfully enriched: {enriched_count}")
    print(f"   - Missing directories: {len(missing_dirs)}")
    if missing_dirs:
        print(f"   - Missing: {', '.join(missing_dirs[:10])}")
        if len(missing_dirs) > 10:
            print(f"     ... and {len(missing_dirs) - 10} more")
    print(f"{'='*60}")

if __name__ == '__main__':
    # Configuration
    JSON_FILE = './codeforces_problems_2025.json'  # Path to your JSON file
    PROBLEMS_DIR = './problems'  # Root directory containing problem folders
    
    # Run enrichment
    enrich_problems(JSON_FILE, PROBLEMS_DIR)