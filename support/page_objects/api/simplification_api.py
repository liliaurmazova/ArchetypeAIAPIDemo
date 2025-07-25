import requests
import logging
from support.helpers.api_helper import ApiHelper
from support.helpers.data_generator import ArithmeticExpressionGenerator
from support.constants.api_constants import ApiConstants

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SimplificationAPI:
    
    def __init__(self):
        try:
            self.api_helper = ApiHelper()
            self.expression_generator = ArithmeticExpressionGenerator()
            logger.info("SimplificationAPI initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize SimplificationAPI: {str(e)}")
            raise
    
    def simplify_generated_expression(self, num_terms=3, min_value=1, max_value=20):
        """
        Generate a random algebraic expression and send it to the simplify endpoint.
        
        Args:
            num_terms: Number of terms in the expression (default: 3)
            min_value: Minimum value for coefficients (default: 1)
            max_value: Maximum value for coefficients (default: 20)
            
        Returns:
            dict: API response containing the simplified expression
            
        Raises:
            ValueError: If invalid parameters are provided
            requests.RequestException: If API request fails
            Exception: For any other unexpected errors
        """
        try:
            logger.info(f"Generating expression with {num_terms} terms, values {min_value}-{max_value}")
            
            # Validate input parameters
            if num_terms <= 0:
                raise ValueError("num_terms must be greater than 0")
            if min_value >= max_value:
                raise ValueError("min_value must be less than max_value")
            if min_value < 0 or max_value < 0:
                raise ValueError("min_value and max_value must be non-negative")
            
            # Generate a random algebraic expression
            expression = self.expression_generator.generate_expression(num_terms, min_value, max_value)
            logger.info(f"Generated expression: {expression}")
            
            # Build the URL with the expression as part of the path
            endpoint = f"{ApiConstants.SIMPLIFY_URL}/{expression}"
            url = self.api_helper.build_url(endpoint)
            logger.info(f"Built API URL: {url}")
            
            # Build headers
            headers = self.api_helper.build_headers()
            logger.debug(f"Request headers: {headers}")
            
            # Send GET request
            logger.info(f"Sending GET request to simplify endpoint")
            response = requests.get(url, headers=headers, timeout=ApiConstants.TIMEOUT/1000)
            response.raise_for_status()
            
            response_data = response.json()
            logger.info(f"Successfully received response for expression: {expression}")
            logger.debug(f"Response data: {response_data}")
            
            return {
                'original_expression': expression,
                'response': response_data
            }
            
        except ValueError as e:
            logger.error(f"Invalid parameters provided: {str(e)}")
            raise
        except requests.exceptions.Timeout as e:
            logger.error(f"Request timeout for expression '{expression}': {str(e)}")
            raise requests.RequestException(f"Request timed out: {str(e)}")
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error for expression '{expression}': {str(e)}")
            raise requests.RequestException(f"Connection failed: {str(e)}")
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error {response.status_code} for expression '{expression}': {str(e)}")
            raise requests.RequestException(f"HTTP error {response.status_code}: {str(e)}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed for expression '{expression}': {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in simplify_generated_expression: {str(e)}")
            raise Exception(f"Unexpected error occurred: {str(e)}")
    
    def simplify_custom_expression(self, expression):
        """
        Send a custom expression to the simplify endpoint.
        
        Args:
            expression: The algebraic expression to simplify
            
        Returns:
            dict: API response containing the simplified expression
            
        Raises:
            ValueError: If expression is None or empty
            requests.RequestException: If API request fails
            Exception: For any other unexpected errors
        """
        try:
            logger.info(f"Simplifying custom expression: {expression}")
            
            # Validate input
            if not expression or not expression.strip():
                raise ValueError("Expression cannot be None or empty")
            
            expression = expression.strip()
            logger.debug(f"Cleaned expression: {expression}")
            
            # Build the URL with the expression as part of the path
            endpoint = f"{ApiConstants.SIMPLIFY_URL}/{expression}"
            url = self.api_helper.build_url(endpoint)
            logger.info(f"Built API URL: {url}")
            
            # Build headers
            headers = self.api_helper.build_headers()
            logger.debug(f"Request headers: {headers}")
            
            # Send GET request
            logger.info(f"Sending GET request to simplify endpoint")
            response = requests.get(url, headers=headers, timeout=ApiConstants.TIMEOUT/1000)
            response.raise_for_status()
            
            response_data = response.json()
            logger.info(f"Successfully received response for expression: {expression}")
            logger.debug(f"Response data: {response_data}")
            
            return {
                'original_expression': expression,
                'response': response_data
            }
            
        except ValueError as e:
            logger.error(f"Invalid expression provided: {str(e)}")
            raise
        except requests.exceptions.Timeout as e:
            logger.error(f"Request timeout for expression '{expression}': {str(e)}")
            raise requests.RequestException(f"Request timed out: {str(e)}")
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error for expression '{expression}': {str(e)}")
            raise requests.RequestException(f"Connection failed: {str(e)}")
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error {response.status_code} for expression '{expression}': {str(e)}")
            raise requests.RequestException(f"HTTP error {response.status_code}: {str(e)}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed for expression '{expression}': {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in simplify_custom_expression: {str(e)}")
            raise Exception(f"Unexpected error occurred: {str(e)}")