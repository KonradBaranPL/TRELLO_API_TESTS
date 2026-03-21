"""Module for interaction with "boards/" endpoint of Trello API"""

from api_clients.base_client import BaseClient


class BoardsClient(BaseClient):
    """Class for interaction with "boards/" endpoint of Trello API"""

    def __init__(self):
        """empty doctring"""
        self.endpoint = "boards/"

    def create_board(self, board_name: str):
        """Create a new Trello board"""
        name = {"name": board_name}
        response = self.post(self.endpoint, params=name)
        return response
    