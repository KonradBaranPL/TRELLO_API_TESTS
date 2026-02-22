import os
import requests

from dotenv import load_dotenv
import pytest


load_dotenv()

BASE_URL = "https://api.trello.com/1/"

API_KEY = os.environ["TRELLO_API_KEY"]

API_TOKEN = os.environ["TRELLO_TOKEN"]


@pytest.fixture
def new_board():
    """Creates a new board and deletes it at the end of the test. Returns board id"""
    
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

    requests.delete(f"{BASE_URL}boards/{board_id}", params=query_params_delete)

    assert response_post.status_code == 200

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


def test_get_board_details(new_board):
    
    board_id, current_board_name = new_board

    query_params_get = {
        "key": API_KEY,
        "token": API_TOKEN,
    }

    response_get = requests.get(f"{BASE_URL}boards/{board_id}", params=query_params_get)

    assert response_get.status_code == 200

    assert response_get.json()["name"] == current_board_name


def test_update_board(new_board):
    
    board_id, _ = new_board

    new_board_name = "testing board updated"

    querry_params_put = {
        "key": API_KEY,
        "token": API_TOKEN,
        "name": new_board_name
    }

    response_put = requests.put(f"{BASE_URL}boards/{board_id}", params=querry_params_put)

    # response_put_json = response_put.json()

    assert response_put.status_code == 200

    assert response_put.json()["name"] == new_board_name


def test_delete_board(board_to_delete):
    
    board_id = board_to_delete
    print(board_id)

    querry_params_del = {
        "key": API_KEY,
        "token": API_TOKEN,
    }

    response_del = requests.delete(f"{BASE_URL}boards/{board_id}", params=querry_params_del)

    assert response_del.status_code == 200


# NEGATIVE TESTS:
def test_get_non_existent_board_returns_404():
    
    non_existent_id = "010101010101010101010101"

    url = f"{BASE_URL}boards/{non_existent_id}"

    query_params_get = {
        "key": API_KEY,
        "token": API_TOKEN
    }

    response_get = requests.get(url, params=query_params_get)

    assert response_get.status_code == 404


def test_create_board_wrong_token():

    board_name = "test board 1.00"

    url = f"{BASE_URL}boards/"

    query_params_post = {
        "key": API_KEY,
        "token": "ATTAf00e0f00f00b000c00c00000be00d00ccf00a0000cb00000eb0000000b0e000bC00AF00E",
        "name": board_name
    }

    response_post = requests.post(url, params=query_params_post)

    assert response_post.status_code == 401


# $ pytest test_boards_with_fixtures.py::get_non_existent_board_returns_404 -v
# $ pytest test_boards_with_fixtures.py -v -s