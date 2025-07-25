# Test Data Structure Documentation

## Overview
The test data has been reorganized from inline constants and JSON files into a structured Python module located in `tests/data/`. This provides better organization, type safety, and easier maintenance.

## Directory Structure
```
tests/
├── data/
│   ├── __init__.py              # Module exports
│   ├── test_constants.py        # Core test data constants  
│   ├── test_data_loader.py      # Utilities for loading test data
│   └── README.md               # This file
├── fixtures/
│   └── api_responses.json       # Legacy (migrated to test_constants.py)
├── integration/
│   └── test_api_integration.py  # Updated to use new data structure
└── unit/
    └── ...                      # Unit tests (can also use new data)
```

## Usage Examples

### Basic Usage
```python
from tests.data import TestExpressions, TestScenarios, TestDataLoader

# Get expressions by type
simple_exprs = TestExpressions.SIMPLE
quadratic_exprs = TestExpressions.QUADRATIC

# Get expressions for specific test scenarios  
integration_exprs = TestScenarios.INTEGRATION_SAFE
performance_exprs = TestScenarios.PERFORMANCE

# Use the data loader for convenience
loader = TestDataLoader()
safe_expressions = loader.get_integration_test_data()
edge_cases = loader.get_edge_cases()
```

### In Parametrized Tests
```python
import pytest
from tests.data import TestDataLoader

@pytest.mark.parametrize("expression", TestDataLoader.get_integration_test_data())
def test_expressions(expression):
    # Test with safe expressions for integration testing
    pass
```

### Generator Parameters
```python
from tests.data import GeneratorParams

# Get parameter ranges for different test sizes
small_params = GeneratorParams.SMALL_RANGE
edge_params = GeneratorParams.EDGE_PARAMS
```

## Data Categories

### Expression Types (`TestExpressions`)
- **SIMPLE**: Basic expressions like "x + x", "2x + 4"
- **QUADRATIC**: Quadratic expressions like "x^2 + 2x + 1"  
- **POLYNOMIAL**: Higher-order polynomials
- **COMPLEX**: Complex multi-term expressions
- **SINGLE_TERM**: Single terms like "x", "2x", "42"
- **ALL**: Combined list of all expressions

### Test Scenarios (`TestScenarios`)
- **INTEGRATION_SAFE**: Expressions safe for real API calls
- **PERFORMANCE**: Expressions for performance testing
- **EDGE_CASES**: Edge case expressions

### Expected Responses (`ExpectedResponses`)
- **SAMPLE_RESPONSES**: Known API responses for specific expressions

### Error Scenarios (`ErrorScenarios`)  
- **INVALID_EXPRESSIONS**: Malformed expressions for error testing
- **MALFORMED**: Syntactically incorrect expressions

### Generator Parameters (`GeneratorParams`)
- **SMALL_RANGE**: Conservative parameter ranges
- **MEDIUM_RANGE**: Standard parameter ranges  
- **LARGE_RANGE**: Extensive parameter ranges
- **EDGE_PARAMS**: Edge case parameters

## Utilities

### TestDataLoader
Provides convenient methods to access test data:
- `get_expressions_by_type(type)`: Get expressions by category
- `get_integration_test_data()`: Get integration-safe expressions
- `get_performance_test_data()`: Get performance test expressions
- `get_expected_response(expr)`: Get expected API response
- `get_invalid_expressions()`: Get invalid expressions for error testing

### TestDataValidator  
Provides validation and utility methods:
- `validate_expressions(list)`: Validate expression list format
- `count_test_data()`: Get counts of all test data categories

## Migration from Old Structure

### Before (inline constants):
```python
@pytest.mark.parametrize("expression", [
    "x + x",
    "2x^2 + 4x^2", 
    "3x + 6",
    "x^2 - 1",
])
def test_expressions(expression):
    pass
```

### After (centralized data):
```python
from tests.data import TestDataLoader

@pytest.mark.parametrize("expression", TestDataLoader.get_integration_test_data())
def test_expressions(expression):
    pass
```

## Benefits

1. **Centralized**: All test data in one location
2. **Organized**: Logical grouping by type and use case
3. **Reusable**: Same data can be used across multiple test files
4. **Type Safe**: Python constants instead of JSON parsing
5. **Documented**: Clear documentation of what each data set contains
6. **Maintainable**: Easy to add new expressions or modify existing ones
7. **Discoverable**: Import autocomplete shows available data sets

## Adding New Test Data

To add new test expressions:

1. Open `tests/data/test_constants.py`
2. Add expressions to the appropriate class
3. Update any related expected responses if needed
4. The data will automatically be available via `TestDataLoader`

Example:
```python
class TestExpressions:
    SIMPLE = [
        "x + x",
        "2x + 4", 
        "your_new_expression_here"  # Add here
    ]
```
