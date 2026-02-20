import os
import requests

from dotenv import load_dotenv
import pytest


load_dotenv()

BASE_URL = "https://api.trello.com/1/"

API_KEY = os.environ["TRELLO_API_KEY"]

API_TOKEN = os.environ["TRELLO_TOKEN"]


# $ pytest test_learning_fixtures.py -v -s

@pytest.fixture
def new_board():
    """Creates a new board and deletes it at the end of the test. Returns board id"""
    
    board_name = "fixture test board 1.00"

    query_params_post = {
        "name": board_name,
        "key": API_KEY,
        "token": API_TOKEN,
        "defaultLists": "false"
    }

    response_post = requests.post(f"{BASE_URL}boards/", params=query_params_post)

    assert response_post.status_code == 200

    board_id = response_post.json()["id"]

    yield board_id

    query_params_delete = {
        "key": API_KEY,
        "token": API_TOKEN
    }

    requests.delete(f"{BASE_URL}boards/{board_id}", params=query_params_delete)

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

<<<<<<<< HEAD:tests/test_boards_with_fixtures.py
def test_create_new_board(new_board):
========
def test_create_new_board():
>>>>>>>> 3f758f070faf49fe27c69697290a9a96e49755dc:tests/test_learning_fixtures.py

    board_name = "test board XYZ"

    url = f"{BASE_URL}boards/"

    query_params = {
        "name": board_name,
        "key": API_KEY,
        "token": API_TOKEN
    }
    pass

def test_get_board_details(new_board):

    query_params_get = {
        "key": API_KEY,
        "token": API_TOKEN,
    }

    board_id = new_board

    response_get = requests.get(f"{BASE_URL}boards/{board_id}", params=query_params_get)

    assert response_get.status_code == 200

    assert response_get.json()["name"] == "fixture test board 1.00"

def test_update_board(new_board):
    
    board_id = new_board

    board_name = "testing board updated"

    querry_params_put = {
        "key": API_KEY,
        "token": API_TOKEN,
        "name": board_name
    }

    response_put = requests.put(f"{BASE_URL}boards/{board_id}", params=querry_params_put)

    response_put_json = response_put.json()

    assert response_put.status_code == 200

    assert response_put_json["name"] == board_name

def test_delete_board(board_to_delete):
    
    board_id = board_to_delete
    print(board_id)

    querry_params_del = {
        "key": API_KEY,
        "token": API_TOKEN,
    }

    response_del = requests.delete(f"{BASE_URL}boards/{board_id}", params=querry_params_del)

    assert response_del.status_code == 200