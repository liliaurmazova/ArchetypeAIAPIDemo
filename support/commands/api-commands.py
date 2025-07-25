import requests
from helpers.api_helper import ApiHelper
from helpers.data_generator import ArithmeticExpressionGenerator

def api_get(endpoint, base_url, headers=None):
    url = ApiHelper.build_url(base_url, endpoint)
    api_helper = ApiHelper()
    headers = api_helper.build_headers()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def api_post(endpoint, body, base_url, headers=None):
    response = requests.post(f"{base_url}{endpoint}", json=body, headers=headers)
    response.raise_for_status()
    return response.json()

def api_delete(endpoint, base_url, headers=None):
    response = requests.delete(f"{base_url}{endpoint}", headers=headers)
    response.raise_for_status()
    return response.json()
