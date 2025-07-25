"""
Unit tests for SimplificationAPI class.
Tests all methods with mocked HTTP responses.
"""

import pytest
import requests
from unittest.mock import Mock, patch, MagicMock
from support.page_objects.api.simplification_api import SimplificationAPI


class TestSimplificationAPI:
    
    def test_initialization(self):
        """Test that SimplificationAPI initializes correctly."""
        api = SimplificationAPI()
        assert api.api_helper is not None
        assert api.expression_generator is not None
    
    @patch('support.page_objects.api.simplification_api.requests.get')
    def test_simplify_generated_expression_success(self, mock_get, mock_successful_response):
        """Test successful simplification of generated expression."""
        # Setup
        mock_get.return_value = mock_successful_response
        api = SimplificationAPI()
        
        # Execute
        result = api.simplify_generated_expression(num_terms=2, min_value=1, max_value=5)
        
        # Verify
        assert 'original_expression' in result
        assert 'response' in result
        assert result['response']['operation'] == 'simplify'
        mock_get.assert_called_once()
    
    @patch('support.page_objects.api.simplification_api.requests.get')
    def test_simplify_custom_expression_success(self, mock_get, mock_successful_response):
        """Test successful simplification of custom expression."""
        # Setup
        mock_get.return_value = mock_successful_response
        api = SimplificationAPI()
        expression = "x^2 + 2x + 1"
        
        # Execute
        result = api.simplify_custom_expression(expression)
        
        # Verify
        assert result['original_expression'] == expression
        assert 'response' in result
        assert result['response']['operation'] == 'simplify'
        mock_get.assert_called_once()
    
    def test_simplify_generated_expression_invalid_params(self):
        """Test parameter validation for generated expression."""
        api = SimplificationAPI()
        
        # Test num_terms <= 0
        with pytest.raises(ValueError, match="num_terms must be greater than 0"):
            api.simplify_generated_expression(num_terms=0)
        
        # Test min_value >= max_value
        with pytest.raises(ValueError, match="min_value must be less than max_value"):
            api.simplify_generated_expression(min_value=10, max_value=5)
        
        # Test negative values
        with pytest.raises(ValueError, match="min_value and max_value must be non-negative"):
            api.simplify_generated_expression(min_value=-1, max_value=5)
    
    def test_simplify_custom_expression_invalid_input(self):
        """Test validation for custom expression input."""
        api = SimplificationAPI()
        
        # Test None expression
        with pytest.raises(ValueError, match="Expression cannot be None or empty"):
            api.simplify_custom_expression(None)
        
        # Test empty expression
        with pytest.raises(ValueError, match="Expression cannot be None or empty"):
            api.simplify_custom_expression("")
        
        # Test whitespace-only expression
        with pytest.raises(ValueError, match="Expression cannot be None or empty"):
            api.simplify_custom_expression("   ")
    
    @patch('support.page_objects.api.simplification_api.requests.get')
    def test_http_error_handling(self, mock_get):
        """Test handling of HTTP errors."""
        # Setup
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        api = SimplificationAPI()
        
        # Execute & Verify
        with pytest.raises(requests.RequestException, match="HTTP error 404"):
            api.simplify_custom_expression("x + 1")
    
    @patch('support.page_objects.api.simplification_api.requests.get')
    def test_timeout_error_handling(self, mock_get):
        """Test handling of timeout errors."""
        # Setup
        mock_get.side_effect = requests.exceptions.Timeout("Request timed out")
        api = SimplificationAPI()
        
        # Execute & Verify
        with pytest.raises(requests.RequestException, match="Request timed out"):
            api.simplify_custom_expression("x + 1")
    
    @patch('support.page_objects.api.simplification_api.requests.get')
    def test_connection_error_handling(self, mock_get):
        """Test handling of connection errors."""
        # Setup
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection failed")
        api = SimplificationAPI()
        
        # Execute & Verify
        with pytest.raises(requests.RequestException, match="Connection failed"):
            api.simplify_custom_expression("x + 1")
    
    @pytest.mark.parametrize("expression,expected_cleaned", [
        ("  x^2 + 1  ", "x^2 + 1"),
        ("\tx + 1\n", "x + 1"),
        ("2x^2 + 3x + 1", "2x^2 + 3x + 1"),
    ])
    def test_expression_cleaning(self, expression, expected_cleaned):
        """Test that expressions are properly cleaned of whitespace."""
        api = SimplificationAPI()
        
        with patch('support.page_objects.api.simplification_api.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {'operation': 'simplify', 'expression': expected_cleaned, 'result': expected_cleaned}
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response
            
            result = api.simplify_custom_expression(expression)
            assert result['original_expression'] == expected_cleaned
    
    @pytest.mark.parametrize("num_terms,min_val,max_val", [
        (1, 1, 5),
        (3, 1, 10),
        (5, 0, 20),
        (2, 5, 15),
    ])
    def test_generated_expression_parameters(self, num_terms, min_val, max_val):
        """Test different parameter combinations for generated expressions."""
        api = SimplificationAPI()
        
        with patch('support.page_objects.api.simplification_api.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {'operation': 'simplify', 'expression': 'test', 'result': 'test'}
            mock_response.raise_for_status.return_value = None
            mock_get.return_value = mock_response
            
            result = api.simplify_generated_expression(num_terms=num_terms, min_value=min_val, max_value=max_val)
            assert 'original_expression' in result
            assert 'response' in result
