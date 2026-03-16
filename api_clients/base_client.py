import requests

from config.config import API_KEY, API_TOKEN, BASE_URL


class BaseClient:
    "Client for interacting with the Trello API"

    def __init__(self):
        """Initialize API client with authentication credentials."""
        
        self.key = API_KEY
        self.token = API_TOKEN
        self.auth_params = {"key": API_KEY, "token": API_TOKEN}
        self.base_url = BASE_URL