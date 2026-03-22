"""Module for interaction with "boards/" endpoint of Trello API"""

from api_clients.base_client import BaseClient


class BoardsClient(BaseClient):
    """Class for interaction with "boards/" endpoint of Trello API"""

    def __init__(self,):
        """Initialize BoardsClient and set the endpoint to 'boards/'."""
        super().__init__()
        self.endpoint = "boards/"

    def create_board(self, board_name: str):
        """Create a new Trello board"""
        name = {"name": board_name}
        response = self.post(self.endpoint, params=name)
        return response

    def get_board(self, board_id: str):
        """Get details about a specific single Trello board"""
        response = self.get(f"{self.endpoint}{board_id}")
        return response
    
    def update_board(self, board_id: str):
        return None

    def delete_board(self, board_id: str):
        """empty"""
        response = self.delete()
        return None
