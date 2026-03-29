"""Module for interaction with "boards/" endpoint of Trello API"""

import uuid
from api_clients.base_client import BaseClient


class BoardsClient(BaseClient):
    """Class for interaction with "boards/" endpoint of Trello API"""

    def __init__(self):
        """Initialize BoardsClient and set the endpoint to 'boards/'."""
        super().__init__()
        self.endpoint = "boards/"

    def create_board(self, board_name: str, **kwargs):
        """Create a new board"""
        params = {"name": board_name}
        params.update(kwargs)
        response = self.post(self.endpoint, params=params)
        return response

    def get_board(self, board_id: str):
        """Get details about a specific single board"""
        response = self.get(f"{self.endpoint}{board_id}")
        return response

    def update_board(self, board_id: str, **kwargs):
        """Update one or more fields of an existing board by id"""
        response = self.put(f"{self.endpoint}{board_id}", params=kwargs)
        return response

    def delete_board(self, board_id: str):
        """Deleta a board"""
        response = self.delete(f"{self.endpoint}{board_id}")
        return response

    def unique_board_name(self):
        """Create board name ending with 8-character unique identifier"""
        unique_id = str(uuid.uuid4())[:8]
        board_name = f"board_{unique_id}"
        return board_name
