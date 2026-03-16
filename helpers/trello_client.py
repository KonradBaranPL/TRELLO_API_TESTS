import requests
import uuid

from config.config import API_KEY, API_TOKEN, BASE_URL


class TrelloClient:
    "Client for interacting with the Trello API"

    def __init__(self):
        """Initialize API client with authentication credentials."""

        self.key = API_KEY
        self.token = API_TOKEN
        self.base_url = BASE_URL
    

    def create_board(self, name):
        """Create a new Trello board"""

        params = {"name": name, "key": self.key,"token": self.token}
        return requests.post(f"{self.base_url}boards/", params=params)
    

    def get_board(self, board_id):
        """Retrieve information about a specific Trello board"""

        params = {"key": self.key,"token": self.token}
        return requests.get(f"{self.base_url}boards/{board_id}", params=params)
    

    def update_board(self, board_id, fields_to_update):
        """Update one or more fields fo Trello board"""

        params = {**fields_to_update, "key": self.key, "token": self.token}
        return requests.put(f"{self.base_url}boards/{board_id}", params=params)


    def delete_board(self, board_id):
        """Delete a Trello board"""

        params = {"key": self.key,"token": self.token}
        return requests.delete(f"{self.base_url}boards/{board_id}", params=params)
    

    def unique_board_name(self):
        """Create board name ending with 8-character unique identifier"""

        unique_id = str(uuid.uuid4().hex)[:8]
        board_name = f"board_{unique_id}"
        return board_name