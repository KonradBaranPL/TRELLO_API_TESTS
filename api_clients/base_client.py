"""Client module for interacting with the Trello API."""

import requests

from config.config import API_KEY, API_TOKEN, BASE_URL


class BaseClient:
    """Client for interacting with the Trello API."""

    def __init__(self):
        """Initialize API client with authentication credentials."""
        self.key = API_KEY
        self.token = API_TOKEN
        self.auth_params = {"key": API_KEY, "token": API_TOKEN}
        self.base_url = BASE_URL

    def get(self, endpoint: str, params=None):
        """Send a GET request to a specific API endpoint with authentication."""
        url = f"{self.base_url}{endpoint}"
        query_params = self.auth_params.copy()
        if params:
            query_params.update(params)
        response = requests.get(url, params=query_params)
        return response

    def post(self, endpoint: str, params=None):
        """Send a POST request to a specific API endpoint with authentication."""
        url = f"{self.base_url}{endpoint}"
        query_params = self.auth_params.copy()
        if params:
            query_params.update(params)
        response = requests.post(url, params=query_params)
        return response

    def put(self, endpoint: str, params=None):
        """Send a PUT request to a specific API endpoint with authentication."""
        url = f"{self.base_url}{endpoint}"
        query_params = self.auth_params.copy()
        if params:
            query_params.update(params)
        response = requests.put(url, params=query_params)
        return response

    def delete(self, endpoint: str, params=None):
        """Send a DELETE request to a specific API endpoint with authentication."""
        url = f"{self.base_url}{endpoint}"
        query_params = self.auth_params.copy()
        if params:
            query_params.update(params)
        response = requests.delete(url, params=query_params)
        return response
