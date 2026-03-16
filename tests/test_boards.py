import pytest
from helpers.trello_client import TrelloClient


def test_create_board_and_delete(trello_client):
    board_name = f"test_{trello_client.unique_board_name()}"
    response = trello_client.create_board(board_name)
    assert response.status_code == 200
    assert response.json()["name"] == board_name

    board_id = response.json()["id"]
    delete_response = trello_client.delete_board(board_id)
    assert delete_response.status_code == 200


def test_create_board(new_board, trello_client):
    response = trello_client.get_board(new_board)
    assert response.status_code == 200


def test_delete_board(board_to_delete, trello_client):
    board_id = board_to_delete
    response = trello_client.delete_board(board_id)
    assert response.status_code == 200


def test_update_board(new_board, trello_client):
    board_id = new_board
    new_board_name = f"updated_{trello_client.unique_board_name()}"
    fields_to_update = {"name": new_board_name}
    response = trello_client.update_board(board_id, fields_to_update)
    assert response.status_code == 200
    assert response.json()["name"] == new_board_name
