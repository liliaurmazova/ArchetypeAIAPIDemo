"""
Unit tests for ApiHelper class.
"""

import pytest
from support.helpers.api_helper import ApiHelper
from support.constants.api_constants import ApiConstants


class TestApiHelper:
    
    def test_initialization(self):
        """Test that ApiHelper initializes with correct constants."""
        helper = ApiHelper()
        assert helper.BASE_URL == ApiConstants.BASE_URL
        assert helper.API_VERSION == ApiConstants.API_VERSION
    
    def test_build_url_without_params(self):
        """Test URL building without parameters."""
        helper = ApiHelper()
        endpoint = "simplify/x+1"
        
        url = helper.build_url(endpoint)
        
        expected = f"{ApiConstants.BASE_URL}{ApiConstants.API_VERSION}{endpoint}"
        assert url == expected
    
    def test_build_url_with_params(self):
        """Test URL building with query parameters."""
        helper = ApiHelper()
        endpoint = "test"
        params = {"param1": "value1", "param2": "value2"}
        
        url = helper.build_url(endpoint, params)
        
        # Should contain the base URL and endpoint
        assert f"{ApiConstants.BASE_URL}{ApiConstants.API_VERSION}{endpoint}" in url
        # Should contain the parameters
        assert "param1=value1" in url
        assert "param2=value2" in url
        # Should contain the query separator
        assert "?" in url
    
    def test_build_url_with_special_characters(self):
        """Test URL building with special characters in parameters."""
        helper = ApiHelper()
        endpoint = "test"
        params = {"expr": "x^2 + 2x + 1", "format": "json"}
        
        url = helper.build_url(endpoint, params)
        
        # Should be properly URL encoded
        assert "?" in url
        assert "expr=" in url
        assert "format=json" in url
    
    def test_build_headers_without_token(self):
        """Test header building without authentication token."""
        helper = ApiHelper()
        
        headers = helper.build_headers()
        
        expected_headers = {
            'Content-Type': 'application/json',
        }
        assert headers == expected_headers
    
    def test_build_headers_with_token(self):
        """Test header building with authentication token."""
        helper = ApiHelper()
        token = "test_token_123"
        
        headers = helper.build_headers(token=token)
        
        expected_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        assert headers == expected_headers
    
    @pytest.mark.parametrize("endpoint,expected_suffix", [
        ("simplify", "simplify"),
        ("factor", "factor"),
        ("derive", "derive"),
        ("integrate", "integrate"),
    ])
    def test_build_url_different_endpoints(self, endpoint, expected_suffix):
        """Test URL building with different endpoints."""
        helper = ApiHelper()
        
        url = helper.build_url(endpoint)
        
        assert url.endswith(expected_suffix)
        assert ApiConstants.BASE_URL in url
        assert ApiConstants.API_VERSION in url
    
    def test_build_url_empty_endpoint(self):
        """Test URL building with empty endpoint."""
        helper = ApiHelper()
        
        url = helper.build_url("")
        
        expected = f"{ApiConstants.BASE_URL}{ApiConstants.API_VERSION}"
        assert url == expected
    
    def test_build_headers_different_content_types(self):
        """Test that Content-Type is always application/json."""
        helper = ApiHelper()
        
        headers1 = helper.build_headers()
        headers2 = helper.build_headers(token="test")
        
        assert headers1['Content-Type'] == 'application/json'
        assert headers2['Content-Type'] == 'application/json'
    
    @pytest.mark.parametrize("token", [
        "simple_token",
        "complex_token_with_123_numbers",
        "token.with.dots",
        "token-with-dashes",
    ])
    def test_build_headers_various_tokens(self, token):
        """Test header building with various token formats."""
        helper = ApiHelper()
        
        headers = helper.build_headers(token=token)
        
        assert headers['Authorization'] == f'Bearer {token}'
        assert headers['Content-Type'] == 'application/json'
    
    def test_url_joining_correctness(self):
        """Test that URL components are joined correctly."""
        helper = ApiHelper()
        endpoint = "simplify/test"
        
        url = helper.build_url(endpoint)
        
        # Should not have double slashes (except after http:)
        url_without_protocol = url.replace('https://', '')
        assert '//' not in url_without_protocol
        
        # Should properly join all components
        assert url.count('/') >= 3  # https://domain/api/v2/endpoint
