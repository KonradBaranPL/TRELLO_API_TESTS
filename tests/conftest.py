from helpers.trello_client import TrelloClient

import pytest


@pytest.fixture
def trello_client():
    """Returns an object of TrelloClient class"""
    return TrelloClient()


@pytest.fixture
def new_board(trello_client: TrelloClient):
    """Creates a new board and deletes it at the end of the test. Returns board id"""
    board_name = f"fixture_{trello_client.unique_board_name()}"
    response = trello_client.create_board(board_name)
    board_id = response.json()["id"]
    yield board_id

    response = trello_client.delete_board(board_id)
    assert response.status_code == 200


@pytest.fixture
def board_to_delete(trello_client: TrelloClient):
    """Creates a board without deleting it at the end of the test. Returns board_id"""

    board_name = f"fixture_{trello_client.unique_board_name()}"
    response = trello_client.create_board(board_name)
    assert response.status_code == 200
    board_id = response.json()["id"]
    yield board_id