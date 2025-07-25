"""
Test data constants for integration and unit tests.
Contains sample expressions, expected responses, and test scenarios.
"""

class TestExpressions:
    """Constants for test expressions organized by complexity and type."""
    
    # Simple expressions for basic testing
    SIMPLE = [
        "x + x",
        "2x + 2x", 
        "3x + 6",
        "2x + 4",
    ]
    
    # Quadratic expressions
    QUADRATIC = [
        "x^2 + 2x + 1",    # Perfect square
        "4x^2 + 4x + 1",   # Perfect square
        "x^2 - 1",         # Difference of squares
        "x^2 - 4",         # Difference of squares
        "2x^2 + 4x^2",     # Like terms
    ]
    
    # Polynomial expressions
    POLYNOMIAL = [
        "x^3 - x",
        "2x^3 + 4x^2 - 6x",
        "x^3 + x^2 + x + 1",
        "5x^2 + 10x + 5",
    ]
    
    # Complex expressions for advanced testing
    COMPLEX = [
        "2x^3 - 4x^2 + 6x - 8",
        "3x^4 + 2x^3 - x^2 + 5x - 10",
        "x^5 + x^4 + x^3 + x^2 + x + 1",
    ]
    
    # Single term expressions
    SINGLE_TERM = [
        "x",
        "2x",
        "x^2", 
        "5x^3",
        "42",      # Constant
    ]
    
    # All expressions combined for comprehensive testing
    ALL = SIMPLE + QUADRATIC + POLYNOMIAL + COMPLEX + SINGLE_TERM


class TestScenarios:
    """Test scenarios organized by purpose."""
    
    # Integration test expressions (safe for real API calls)
    INTEGRATION_SAFE = [
        "x + x",
        "2x^2 + 4x^2", 
        "3x + 6",
        "x^2 - 1",
        "2x + 3x",
    ]
    
    # Edge case expressions
    EDGE_CASES = [
        "0",           # Zero
        "1",           # One  
        "x",           # Single variable
        "-x",          # Negative variable
        "x^0",         # Zero power
    ]


class ExpectedResponses:
    """Expected API responses for known expressions."""
    
    SAMPLE_RESPONSES = {
        "x + x": {
            "operation": "simplify",
            "expression": "x + x",
            "result": "2 x"
        },
        "x^2 + 2x + 1": {
            "operation": "simplify", 
            "expression": "x^2 + 2x + 1",
            "result": "(x + 1)^2"
        },
        "2x^3 + 4x^2 - 6x": {
            "operation": "simplify",
            "expression": "2x^3 + 4x^2 - 6x", 
            "result": "2 x (x^2 + 2 x - 3)"
        },
        "3x + 6": {
            "operation": "simplify",
            "expression": "3x + 6",
            "result": "3 (x + 2)"
        },
        "2x + 4": {
            "operation": "simplify",
            "expression": "2x + 4",
            "result": "2 (x + 2)"
        }
    }


class ErrorScenarios:
    """Test data for error handling scenarios."""
    
    # Invalid expressions that should cause API errors
    INVALID_EXPRESSIONS = [
        "2x + + 3",      # Double operator
        "x^",            # Incomplete power
        "2x + 3y",       # Multiple variables (if not supported)
        "",              # Empty string
        "   ",           # Whitespace only
    ]
    
    # Malformed expressions
    MALFORMED = [
        "x + ",          # Trailing operator
        "+ x",           # Leading operator
        "x ^ ^ 2",       # Double power operator
        "((x))",         # Unbalanced parentheses (if not supported)
    ]


class GeneratorParams:
    """Parameters for expression generator testing."""
    
    # Safe parameter ranges for testing
    SMALL_RANGE = {
        "num_terms": [1, 2, 3],
        "min_value": [1, 2],
        "max_value": [5, 10]
    }
    
    MEDIUM_RANGE = {
        "num_terms": [2, 3, 4],
        "min_value": [1, 5],
        "max_value": [10, 15] 
    }
    
    LARGE_RANGE = {
        "num_terms": [3, 4, 5],
        "min_value": [5, 10],
        "max_value": [15, 20]
    }
    
    # Edge case parameters
    EDGE_PARAMS = [
        {"num_terms": 1, "min_value": 1, "max_value": 2},
        {"num_terms": 5, "min_value": 0, "max_value": 20},
        {"num_terms": 2, "min_value": 10, "max_value": 15},
    ]
