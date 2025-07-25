"""
Integration tests for the SimplificationAPI.
These tests make real API calls - use sparingly to avoid rate limiting.
"""

import pytest
from support.page_objects.api.simplification_api import SimplificationAPI
from tests.data import TestScenarios, TestDataLoader, GeneratorParams


class TestSimplificationAPIIntegration:
    """
    Integration tests that make real API calls.
    Mark with @pytest.mark.integration to run separately.
    """
    
    @pytest.mark.integration
    def test_real_api_call_simple_expression(self):
        """Test a real API call with a simple expression."""
        api = SimplificationAPI()
        # Use test data from constants
        expression = TestScenarios.INTEGRATION_SAFE[1]  # "2x^2 + 4x^2"
        
        result = api.simplify_custom_expression(expression)
        
        assert result['original_expression'] == expression
        assert 'response' in result
        assert result['response']['operation'] == 'simplify'
        assert 'result' in result['response']
    
    @pytest.mark.integration
    def test_real_api_call_complex_expression(self):
        """Test a real API call with a more complex expression."""
        api = SimplificationAPI()
        # Use predefined complex expression
        expression = "x^2 + 2x + 1"
        
        result = api.simplify_custom_expression(expression)
        
        assert result['original_expression'] == expression
        assert 'response' in result
        assert result['response']['operation'] == 'simplify'
        # The result might be simplified or factored
        assert len(result['response']['result']) > 0
    
    @pytest.mark.integration
    def test_real_api_call_generated_expression(self):
        """Test a real API call with a generated expression."""
        api = SimplificationAPI()
        # Use test data for generator parameters
        params = GeneratorParams.SMALL_RANGE
        
        result = api.simplify_generated_expression(
            num_terms=params["num_terms"][0], 
            min_value=params["min_value"][0], 
            max_value=params["max_value"][0]
        )
        
        assert 'original_expression' in result
        assert 'response' in result
        assert result['response']['operation'] == 'simplify'
        assert 'result' in result['response']
    
    @pytest.mark.integration
    @pytest.mark.parametrize("expression", TestDataLoader.get_integration_test_data())
    def test_real_api_various_expressions(self, expression):
        """Test real API calls with various expressions from test data."""
        api = SimplificationAPI()
        
        result = api.simplify_custom_expression(expression)
        
        assert result['original_expression'] == expression
        assert 'response' in result
        assert result['response']['operation'] == 'simplify'
    
    @pytest.mark.integration
    def test_api_response_structure(self):
        """Test that the API response has the expected structure."""
        api = SimplificationAPI()
        # Use test data
        expression = TestScenarios.INTEGRATION_SAFE[-1]  # "2x + 3x"
        
        result = api.simplify_custom_expression(expression)
        
        # Check response structure
        response = result['response']
        assert isinstance(response, dict)
        assert 'operation' in response
        assert 'expression' in response
        assert 'result' in response
        
        # Check values
        assert response['operation'] == 'simplify'
        assert response['expression'] == expression
        assert isinstance(response['result'], str)
    
    
    @pytest.mark.integration
    @pytest.mark.parametrize("params", GeneratorParams.EDGE_PARAMS)
    def test_generated_expressions_with_edge_params(self, params):
        """Test generated expressions with edge case parameters."""
        api = SimplificationAPI()
        
        result = api.simplify_generated_expression(**params)
        
        assert 'original_expression' in result
        assert 'response' in result
        assert result['response']['operation'] == 'simplify'
        assert 'result' in result['response']
