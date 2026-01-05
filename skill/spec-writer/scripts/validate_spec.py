#!/usr/bin/env python3
"""
Requirements specification validation tool

Validates requirements documents for completeness and consistency
"""

import re
import sys
from typing import Dict, List, Optional


def validate_requirements_spec(spec: str) -> Dict[str, bool]:
    """Validate requirements specification structure"""
    required_sections = [
        '## 1. Overview',
        '### 1.1 Problem Statement',
        '### 1.2 User Stories',
        '### 1.3 Success Criteria',
        '## 2. Functional Requirements',
        '### 2.1 Core Requirements',
        '### 2.2 Non-Functional Requirements',
        '## 3. User Flows',
        '### 3.1 Happy Path',
        '### 3.2 Error Scenarios',
        '## 4. Test Scenarios',
        '## 5. Out of Scope',
    ]
    
    results = {}
    for section in required_sections:
        section_key = section.lower().replace(' ', '_').replace('.', '').replace('#', '')
        results[section_key] = section in spec
    
    # Additional validations
    results['has_user_story_format'] = 'As a' in spec and 'I want' in spec and 'So that' in spec
    results['has_success_criteria'] = '- [ ]' in spec or '- [x]' in spec
    results['has_user_flows'] = '→' in spec or '->' in spec
    results['has_core_requirements'] = 'must' in spec.lower()
    results['has_non_functional'] = ('Performance:' in spec or 'Security:' in spec or 
                                      'Scalability:' in spec)
    results['has_error_scenarios'] = 'error' in spec.lower() or 'invalid' in spec.lower()
    results['has_out_of_scope'] = 'out of scope' in spec.lower() or 'not doing' in spec.lower()
    results['has_test_scenarios'] = '| Scenario' in spec or 'Test' in spec
    
    return results


def validate_user_story(story: str) -> Dict[str, bool]:
    """Validate user story format"""
    return {
        'has_role': 'As a' in story,
        'has_feature': 'I want' in story,
        'has_benefit': 'So that' in story,
        'complete_format': ('As a' in story and 'I want' in story and 'So that' in story)
    }


def validate_user_flows(flows: str) -> Dict[str, bool]:
    """Validate user flows quality"""
    results = {
        'has_flow_arrows': '→' in flows or '->' in flows,
        'has_user_actions': 'User' in flows or 'user' in flows,
        'has_system_responses': 'System' in flows or 'system' in flows,
        'has_error_scenarios': 'error' in flows.lower() or 'invalid' in flows.lower(),
        'has_edge_cases': 'edge' in flows.lower() or 'what if' in flows.lower()
    }
    return results


def print_results(results: Dict[str, bool], spec_type: str):
    """Print validation results"""
    print(f"\nValidation results for {spec_type} specification:\n")
    
    passed = []
    failed = []
    
    for check, result in results.items():
        status = "✓" if result else "✗"
        check_name = check.replace('_', ' ').title()
        
        if result:
            passed.append(f"  {status} {check_name}")
        else:
            failed.append(f"  {status} {check_name}")
    
    # Print passed checks
    if passed:
        print("Passed:")
        for line in passed:
            print(line)
    
    # Print failed checks
    if failed:
        print("\nFailed:")
        for line in failed:
            print(line)
    
    all_passed = all(results.values())
    if all_passed:
        print("\n✓ All checks passed!")
        return 0
    else:
        print("\n✗ Some checks failed. Please review the specification.")
        return 1


def main():
    if len(sys.argv) < 3:
        print("Usage: validate_spec.py <spec_type> <file_path>")
        print("  spec_type: requirements, user-story, user-flows")
        print("\nExamples:")
        print("  validate_spec.py requirements thoughts/shared/specs/my-spec.md")
        print("  validate_spec.py user-story story.md")
        print("  validate_spec.py user-flows flows.md")
        sys.exit(1)
    
    spec_type = sys.argv[1]
    file_path = sys.argv[2]
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        if spec_type == 'user-story':
            results = validate_user_story(content)
        elif spec_type == 'user-flows':
            results = validate_user_flows(content)
        elif spec_type == 'requirements':
            results = validate_requirements_spec(content)
        else:
            print(f"Unknown spec type: {spec_type}")
            print("Valid types: requirements, user-story, user-flows")
            sys.exit(1)
        
        return print_results(results, spec_type)
            
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return 1
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
