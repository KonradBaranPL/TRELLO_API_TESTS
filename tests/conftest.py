"""
Pytest fixture definitions for the Trello API test suite.
Provides BoardsClient instance and temporary board setup/teardown.
"""

import pytest

from api_clients.boards_client import BoardsClient


@pytest.fixture
def boards_client():
    """Returns an instance of BoardsClient class"""
    return BoardsClient()

@pytest.fixture
def temp_board(boards_client):
    """Creates a new board and deletes it at the end of the test. Returns board id"""
    name = boards_client.unique_board_name()
    response = boards_client.create_board(name)
    assert response.status_code == 200, (
        f"Failure at setup. Board creation failed. Response: {response.text}"
    )
    board_id = response.json()["id"]
    yield board_id
    delete_response = boards_client.delete_board(board_id)
    assert delete_response.status_code == 200, (
        f"Failure at teardown. Board deletion failed. Response: {delete_response.text}"
    )

@pytest.fixture
def board_to_delete(boards_client):
    """Creates a board without deleting it at the end of the test. Returns board_id"""
    name = boards_client.unique_board_name()
    response = boards_client.create_board(name)
    assert response.status_code == 200, f"Setup failed: {response.text}"
    board_id = response.json()["id"]
    yield board_id



# @pytest.fixture
# def new_board(trello_client: TrelloClient):
#     """Creates a new board and deletes it at the end of the test. Returns board id"""
#     board_name = f"fixture_{trello_client.unique_board_name()}"
#     response = trello_client.create_board(board_name)
#     board_id = response.json()["id"]
#     yield board_id

#     response = trello_client.delete_board(board_id)
#     assert response.status_code == 200


# @pytest.fixture
# def board_to_delete(trello_client: TrelloClient):
#     """Creates a board without deleting it at the end of the test. Returns board_id"""

#     board_name = f"fixture_{trello_client.unique_board_name()}"
#     response = trello_client.create_board(board_name)
#     assert response.status_code == 200
#     board_id = response.json()["id"]
#     yield board_id