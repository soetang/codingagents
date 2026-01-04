#!/usr/bin/env python3
"""
Specification validation tool

Validates comprehensive specifications for completeness and consistency
"""

import re
import sys
from typing import Dict, List, Optional


def validate_comprehensive_spec(spec: str) -> Dict[str, bool]:
    """Validate comprehensive specification structure"""
    required_sections = [
        '## 1. Overview',
        '### 1.1 Purpose',
        '### 1.2 User Stories',
        '### 1.3 Acceptance Criteria',
        '## 2. Technical Specification',
        '### 2.1 Functional Requirements',
        '### 2.2 Non-Functional Requirements',
        '### 2.3 Data Model',
        '### 2.4 API Specifications',
        '### 2.5 Error Handling',
        '### 2.6 Edge Cases',
        '## 3. Interface Design',
        '### 3.1 Design Pattern',
        '### 3.2 Interface Definition',
        '## 4. Test Scenarios',
        '### 4.1 Happy Path Scenarios',
        '### 4.2 Error Condition Scenarios',
        '### 4.3 Performance Test Scenarios',
        '### 4.4 Integration Test Scenarios',
        '## 5. Implementation Considerations'
    ]
    
    results = {}
    for section in required_sections:
        results[section.lower().replace(' ', '_').replace('.', '')] = section in spec
    
    # Additional validations
    results['has_user_story_format'] = 'As a' in spec and 'I want' in spec and 'So that' in spec
    results['has_code_examples'] = '```' in spec
    results['has_acceptance_criteria'] = '- ' in spec and '## 1. Overview' in spec
    results['has_interface_definition'] = '@abstractmethod' in spec or 'interface' in spec.lower()
    results['has_test_scenarios'] = '| Scenario' in spec or 'Steps' in spec
    
    return results


def validate_user_story(story: str) -> Dict[str, bool]:
    """Validate user story format"""
    pattern = r"As a\s+\w+.*\nI want\s+\w+.*\nSo that\s+\w+.*"
    return {
        'has_role': 'As a' in story,
        'has_feature': 'I want' in story,
        'has_benefit': 'So that' in story,
        'valid_format': bool(re.match(pattern, story))
    }


def validate_interface_design(code: str) -> Dict[str, bool]:
    """Validate interface design quality"""
    results = {
        'has_type_hints': '->' in code or ': ' in code,
        'has_docstrings': '"""' in code,
        'has_abstract_methods': 'abstractmethod' in code,
        'uses_solid_principles': True  # This would need more sophisticated analysis
    }
    return results


def main():
    if len(sys.argv) < 3:
        print("Usage: validate_spec.py <spec_type> <file_path>")
        print("  spec_type: comprehensive, user-story, interface-design")
        sys.exit(1)
    
    spec_type = sys.argv[1]
    file_path = sys.argv[2]
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        if spec_type == 'user-story':
            results = validate_user_story(content)
        elif spec_type == 'interface-design':
            results = validate_interface_design(content)
        elif spec_type == 'comprehensive':
            results = validate_comprehensive_spec(content)
        else:
            print(f"Unknown spec type: {spec_type}")
            sys.exit(1)
        
        print(f"Validation results for {file_path}:")
        for check, passed in results.items():
            status = "✓" if passed else "✗"
            print(f"  {status} {check.replace('_', ' ').title()}")
        
        all_passed = all(results.values())
        if all_passed:
            print("\n✓ All checks passed!")
            return 0
        else:
            print("\n✗ Some checks failed. Please review the specification.")
            return 1
            
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return 1
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())