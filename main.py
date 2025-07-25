#!/usr/bin/env python3
"""
Main script to demonstrate the SimplificationAPI functionality.
Run this to see the API in action with various algebraic expressions.
"""

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from support.page_objects.api.simplification_api import SimplificationAPI

def main():
    """
    Main function to demonstrate the SimplificationAPI capabilities.
    """
    try:
        print("🧮 SimplificationAPI Demo")
        print("=" * 40)
        print("This demo shows how to use the Newton API to simplify algebraic expressions.")
        
        # Initialize the API client
        api = SimplificationAPI()
        
        # Demo 1: Random generated expression
        print("\n🎲 Demo 1: Random Generated Expression")
        print("-" * 40)
        result1 = api.simplify_generated_expression(num_terms=3, min_value=2, max_value=8)
        print(f"Generated: {result1['original_expression']}")
        print(f"Simplified: {result1['response']['result']}")
        
        # Demo 2: Custom expressions showcase
        print("\n� Demo 2: Custom Expression Examples")
        print("-" * 40)
        
        custom_expressions = [
            "x^2 + 2x + 1",     # Perfect square
            "x^2 - 1",          # Difference of squares
            "2x + 4",           # Simple factoring
            "2x",               # Simple linear expression
            "2"                 # Constant expression, should return as is
        ]
        
        for expr in custom_expressions:
            result = api.simplify_custom_expression(expr)
            print(f"Expression: {expr}")
            print(f"Simplified: {result['response']['result']}")
            print()
        
        # Demo 3: Complex generated expression
        print("� Demo 3: More Complex Generated Expression")
        print("-" * 40)
        result3 = api.simplify_generated_expression(num_terms=4, min_value=1, max_value=6)
        print(f"Generated: {result3['original_expression']}")
        print(f"Simplified: {result3['response']['result']}")
        
        print("\n✨ Demo completed! The Newton API successfully simplified all expressions.")
        print("\n💡 To run tests, use: python -m pytest tests/")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        print("Please check your internet connection and try again.")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
