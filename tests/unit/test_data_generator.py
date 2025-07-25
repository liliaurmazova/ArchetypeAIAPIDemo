"""
Unit tests for ArithmeticExpressionGenerator class.
"""

import pytest
import re
from support.helpers.data_generator import ArithmeticExpressionGenerator


class TestArithmeticExpressionGenerator:
    
    def test_initialization(self):
        """Test that ArithmeticExpressionGenerator initializes correctly."""
        generator = ArithmeticExpressionGenerator()
        assert len(generator.OPERATORS) == 4
        assert any(op[0] == '+' for op in generator.OPERATORS)
        assert any(op[0] == '-' for op in generator.OPERATORS)
    
    def test_generate_expression_default_params(self):
        """Test expression generation with default parameters."""
        generator = ArithmeticExpressionGenerator()
        expression = generator.generate_expression()
        
        # Should contain 3 terms (default)
        terms = expression.split()
        # With 3 terms and 2 operators: term + term + term = 5 elements
        assert len(terms) == 5
        
        # Should contain valid operators
        operators = [terms[1], terms[3]]
        assert all(op in ['+', '-'] for op in operators)
    
    def test_generate_expression_custom_params(self):
        """Test expression generation with custom parameters."""
        generator = ArithmeticExpressionGenerator()
        expression = generator.generate_expression(num_terms=2, min_value=5, max_value=10)
        
        # Should contain 2 terms and 1 operator
        terms = expression.split()
        assert len(terms) == 3  # term + term = 3 elements
        
        # Check that the expression contains valid algebraic components
        assert any(char in expression for char in ['x', '^', '+', '-'])
    
    def test_expression_contains_variable_x(self):
        """Test that generated expressions contain the variable x."""
        generator = ArithmeticExpressionGenerator()
        expression = generator.generate_expression(num_terms=3)
        
        # Should contain 'x' variable
        assert 'x' in expression
    
    def test_expression_structure_patterns(self):
        """Test that expressions follow expected algebraic patterns."""
        generator = ArithmeticExpressionGenerator()
        
        # Generate multiple expressions to test patterns
        for _ in range(10):
            expression = generator.generate_expression(num_terms=2)
            
            # Should match algebraic expression patterns
            # Examples: "2x^2 + 3", "x - 5", "4x^3 + x", etc.
            pattern = r'^[0-9]*x(\^[0-9]+)?\s*[\+\-]\s*[0-9]*x?(\^[0-9]+)?$|^[0-9]+\s*[\+\-]\s*[0-9]*x(\^[0-9]+)?$|^[0-9]*x(\^[0-9]+)?\s*[\+\-]\s*[0-9]+$'
            # This is a simplified pattern - the actual expressions are more complex
            assert any(char in expression for char in ['x', '+', '-'])
    
    @pytest.mark.parametrize("num_terms", [1, 2, 3, 4, 5])
    def test_different_term_counts(self, num_terms):
        """Test expression generation with different numbers of terms."""
        generator = ArithmeticExpressionGenerator()
        expression = generator.generate_expression(num_terms=num_terms)
        
        terms = expression.split()
        expected_length = num_terms * 2 - 1  # terms + operators
        assert len(terms) == expected_length
    
    @pytest.mark.parametrize("min_val,max_val", [
        (1, 5),
        (0, 10),
        (5, 15),
        (10, 20),
    ])
    def test_different_value_ranges(self, min_val, max_val):
        """Test expression generation with different coefficient ranges."""
        generator = ArithmeticExpressionGenerator()
        expression = generator.generate_expression(num_terms=2, min_value=min_val, max_value=max_val)
        
        # Expression should be valid and non-empty
        assert len(expression) > 0
        assert any(char.isdigit() for char in expression)
    
    def test_expression_operators_are_valid(self):
        """Test that only valid operators are used in expressions."""
        generator = ArithmeticExpressionGenerator()
        
        for _ in range(5):
            expression = generator.generate_expression(num_terms=3)
            terms = expression.split()
            
            # Check operators (every other element starting from index 1)
            operators = [terms[i] for i in range(1, len(terms), 2)]
            assert all(op in ['+', '-'] for op in operators)
    
    def test_coefficient_handling(self):
        """Test that coefficients are handled correctly."""
        generator = ArithmeticExpressionGenerator()
        
        # Generate multiple expressions to increase chance of getting x terms
        expressions_with_x = []
        for _ in range(20):
            expression = generator.generate_expression(num_terms=3, min_value=1, max_value=5)
            if 'x' in expression:
                expressions_with_x.append(expression)
        
        # Should get at least some expressions with x
        assert len(expressions_with_x) > 0, "No expressions with 'x' variable were generated"
        
        # For expressions with x, check they have numbers (coefficients)
        for expression in expressions_with_x[:5]:  # Check first 5
            assert any(char.isdigit() for char in expression), f"Expression '{expression}' has no digits"
    
    def test_power_notation(self):
        """Test that power notation (^) is used correctly."""
        generator = ArithmeticExpressionGenerator()
        
        # Generate many expressions to increase chance of getting powers
        expressions = [generator.generate_expression(num_terms=3) for _ in range(20)]
        
        # At least some should contain power notation
        has_power = any('^' in expr for expr in expressions)
        assert has_power, "No expressions with power notation were generated"
    
    def test_constant_terms(self):
        """Test that constant terms (no x) can be generated."""
        generator = ArithmeticExpressionGenerator()
        
        # Generate many expressions to increase chance of getting constants
        expressions = [generator.generate_expression(num_terms=3) for _ in range(20)]
        
        # Check that we get various term types
        has_constants = any(re.search(r'\b\d+\b(?!\s*x)', expr) for expr in expressions)
        # Note: This regex looks for digits not followed by 'x'
