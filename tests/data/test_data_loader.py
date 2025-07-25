"""
Test data loader and utilities.
Provides easy access to test data and helper functions.
"""

import json
import os
from typing import Dict, List, Any

from .test_constants import (
    TestExpressions, 
    TestScenarios, 
    ExpectedResponses, 
    ErrorScenarios,
    GeneratorParams
)


class TestDataLoader:
    """Utility class to load and manage test data."""
    
    @staticmethod
    def get_expressions_by_type(expression_type: str) -> List[str]:
        """Get expressions by type (simple, quadratic, polynomial, etc.)."""
        type_mapping = {
            'simple': TestExpressions.SIMPLE,
            'quadratic': TestExpressions.QUADRATIC,
            'polynomial': TestExpressions.POLYNOMIAL,
            'complex': TestExpressions.COMPLEX,
            'single_term': TestExpressions.SINGLE_TERM,
            'all': TestExpressions.ALL,
        }
        return type_mapping.get(expression_type.lower(), [])
    
    @staticmethod
    def get_integration_test_data() -> List[str]:
        """Get safe expressions for integration testing."""
        return TestScenarios.INTEGRATION_SAFE
    
    
    @staticmethod
    def get_edge_cases() -> List[str]:
        """Get edge case expressions."""
        return TestScenarios.EDGE_CASES
    
    @staticmethod
    def get_expected_response(expression: str) -> Dict[str, Any] | None:
        """Get expected API response for a known expression."""
        return ExpectedResponses.SAMPLE_RESPONSES.get(expression)
    
    @staticmethod
    def get_invalid_expressions() -> List[str]:
        """Get invalid expressions for error testing."""
        return ErrorScenarios.INVALID_EXPRESSIONS
    
    @staticmethod
    def get_malformed_expressions() -> List[str]:
        """Get malformed expressions for error testing."""
        return ErrorScenarios.MALFORMED
    
    @staticmethod
    def get_generator_params(size: str = 'medium') -> Dict[str, List[int]]:
        """Get parameter ranges for expression generator testing."""
        size_mapping = {
            'small': GeneratorParams.SMALL_RANGE,
            'medium': GeneratorParams.MEDIUM_RANGE,
            'large': GeneratorParams.LARGE_RANGE,
        }
        return size_mapping.get(size.lower(), GeneratorParams.MEDIUM_RANGE)
    
    @staticmethod
    def get_edge_params() -> List[Dict[str, int]]:
        """Get edge case parameters for generator testing."""
        return GeneratorParams.EDGE_PARAMS


class TestDataValidator:
    """Utility to validate test data integrity."""
    
    @staticmethod
    def validate_expressions(expressions: List[str]) -> List[str]:
        """Validate that expressions are properly formatted."""
        valid_expressions = []
        for expr in expressions:
            if expr and isinstance(expr, str) and expr.strip():
                valid_expressions.append(expr.strip())
        return valid_expressions
    
    @staticmethod
    def count_test_data() -> Dict[str, int]:
        """Return counts of different test data categories."""
        return {
            'simple_expressions': len(TestExpressions.SIMPLE),
            'quadratic_expressions': len(TestExpressions.QUADRATIC),
            'polynomial_expressions': len(TestExpressions.POLYNOMIAL),
            'complex_expressions': len(TestExpressions.COMPLEX),
            'single_term_expressions': len(TestExpressions.SINGLE_TERM),
            'total_expressions': len(TestExpressions.ALL),
            'integration_safe': len(TestScenarios.INTEGRATION_SAFE),
            'edge_cases': len(TestScenarios.EDGE_CASES),
            'expected_responses': len(ExpectedResponses.SAMPLE_RESPONSES),
            'invalid_expressions': len(ErrorScenarios.INVALID_EXPRESSIONS),
            'malformed_expressions': len(ErrorScenarios.MALFORMED),
        }
