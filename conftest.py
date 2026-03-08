import requests

from config import API_KEY, API_TOKEN, BASE_URL
import pytest


@pytest.fixture
def auth():
    return {"key": API_KEY, "token": API_TOKEN}


@pytest.fixture
def new_board():
    """Creates a new board and deletes it at the end of the test. Returns board id and board name"""
    
    board_name = "fixture test board 1.0"

    query_params_post = {
        "name": board_name,
        "key": API_KEY,
        "token": API_TOKEN,
        "defaultLists": "false"
    }

    response_post = requests.post(f"{BASE_URL}boards/", params=query_params_post)

    assert response_post.status_code == 200

    board_id = response_post.json()["id"]

    yield board_id, board_name

    query_params_delete = {
        "key": API_KEY,
        "token": API_TOKEN
    }

    response_del = requests.delete(f"{BASE_URL}boards/{board_id}", params=query_params_delete)

    assert response_del.status_code == 200


@pytest.fixture
def board_to_delete():
    """Creates a board without deleting it at the end of the test. Returns board_id"""

    board_name = "board XYZ"

    query_params_post = {
        "key": API_KEY,
        "token": API_TOKEN,
        "name": board_name
    }

    response_post = requests.post(f"{BASE_URL}boards/", params=query_params_post)
    
    assert response_post.status_code == 200

    board_id = response_post.json()["id"]

    yield board_id