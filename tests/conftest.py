"""
Shared pytest fixtures for the test suite.
"""

import pytest
import sys
import os
from unittest.mock import Mock, patch

# Add project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from support.page_objects.api.simplification_api import SimplificationAPI
from support.helpers.api_helper import ApiHelper
from support.helpers.data_generator import ArithmeticExpressionGenerator
from tests.data import TestExpressions, ExpectedResponses, TestDataLoader


@pytest.fixture
def api_helper():
    """Fixture for ApiHelper instance."""
    return ApiHelper()


@pytest.fixture
def expression_generator():
    """Fixture for ArithmeticExpressionGenerator instance."""
    return ArithmeticExpressionGenerator()


@pytest.fixture
def simplification_api():
    """Fixture for SimplificationAPI instance."""
    return SimplificationAPI()


@pytest.fixture
def sample_expressions():
    """Fixture providing sample algebraic expressions for testing."""
    return TestExpressions.SIMPLE + TestExpressions.QUADRATIC[:3]


@pytest.fixture
def integration_test_expressions():
    """Fixture providing safe expressions for integration testing.""" 
    return TestDataLoader.get_integration_test_data()


@pytest.fixture
def mock_api_response():
    """Fixture providing a mock API response."""
    return ExpectedResponses.SAMPLE_RESPONSES["x + x"]


@pytest.fixture
def mock_requests_get():
    """Fixture for mocking requests.get calls."""
    with patch('requests.get') as mock_get:
        yield mock_get


@pytest.fixture
def mock_successful_response(mock_api_response):
    """Fixture for a successful HTTP response."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_api_response
    mock_response.raise_for_status.return_value = None
    return mock_response
