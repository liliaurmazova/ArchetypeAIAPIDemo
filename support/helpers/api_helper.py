from urllib.parse import urlencode, urljoin
from support.constants.api_constants import ApiConstants

class ApiHelper:

    BASE_URL = ApiConstants.BASE_URL
    API_VERSION = ApiConstants.API_VERSION

    
    def build_url(self, endpoint, params=None):
        base = urljoin(ApiHelper.BASE_URL, ApiHelper.API_VERSION)
        url = urljoin(base, endpoint)
        if params:
            url = f"{url}?{urlencode(params)}"
        return url

        
    def build_headers(self, token=None):
        headers = {
            'Content-Type': 'application/json',
        }
        if token:
            headers['Authorization'] = f"Bearer {token}"
        return headers


