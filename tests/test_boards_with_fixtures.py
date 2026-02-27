import os
import requests

from dotenv import load_dotenv
import pytest


load_dotenv()

BASE_URL = "https://api.trello.com/1/"

API_KEY = os.environ["TRELLO_API_KEY"]

API_TOKEN = os.environ["TRELLO_TOKEN"]

INVALID_TOKEN = "ATTAf82e8f88f07b695c04c41009be80d41ccf80a8080cb60844eb6842158b4e054bC85AF46A"


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

@pytest.fixture
def auth():
    return {"key": API_KEY, "token": API_TOKEN}

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

    new_board_name = "test board updated"

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

    querry_params_del = {
        "key": API_KEY,
        "token": API_TOKEN,
    }

    response_del = requests.delete(f"{BASE_URL}boards/{board_id}", params=querry_params_del)

    assert response_del.status_code == 200

    response_get = requests.get(f"{BASE_URL}boards/{board_id}", params=querry_params_del)

    assert response_get.status_code == 404


#PARAMETERIZED TESTS:

@pytest.mark.parametrize(
        "board_name",
        [
            "Nazwa z polskimi znakami: ąęśćżźńłó",
            "Board with numbers 123",
            "!@#$%^&*()",
        ],
)
def test_create_board_with_different_names(board_name, auth):

    url = f"{BASE_URL}boards/"

    query_params_post = {
        **auth,
        "name": board_name
    }

    response_post = requests.post(url, query_params_post)

    assert response_post.status_code == 200

    response_json = response_post.json()

    assert response_json["name"] == board_name

    board_id = response_json["id"]


    query_params_del = {
        "key": API_KEY,
        "token": API_TOKEN,
    }

    requests.delete(f"{url}{board_id}", params=query_params_del)


# NEGATIVE TESTS:

@pytest.mark.parametrize(
        "non_existent_id",
        [
            "010101010101010101010101",
            "aaaaaaaaaaaaBBBBBBBBBBBB",
            "699ae269ca2fedf41c98afb1",
        ],
)
def test_get_non_existent_board_returns_404(non_existent_id):
    
    # non_existent_id = "010101010101010101010101"

    url = f"{BASE_URL}boards/{non_existent_id}"

    query_params_get = {
        "key": API_KEY,
        "token": API_TOKEN
    }

    response_get = requests.get(url, params=query_params_get)

    assert response_get.status_code == 404


def test_get_board_details_missing_api_key(new_board):
    
    board_id, _ = new_board

    url = f"{BASE_URL}boards/{board_id}"

    query_params_get = {
        "key": None,
        "token": API_TOKEN,
    }

    response_get = requests.get(url, params=query_params_get)

    assert response_get.status_code == 401


@pytest.mark.parametrize(
        "board_id",
            [
                pytest.param("699ae269ca2fedf41c98afb", id="23-characters length"),
                pytest.param("699ae269ca2fedf41c98afb6a", id="25-characters length"),
                pytest.param("699ae269ca2fedf41c98afZ6", id="contains Z letter"),
                pytest.param("699ae269ca2fedf41c98afb?", id="contains special character"),
                pytest.param("", id="empty string"),
            ],
)
def test_get_board_details_incorrect_id_format(board_id):

    url = f"{BASE_URL}boards/{board_id}"

    query_params_get = {
        "key": API_KEY,
        "token": API_TOKEN,
    }

    response_get = requests.get(url, params=query_params_get)
    print(response_get.text)   

    assert response_get.status_code == 400


def test_create_board_with_invalid_token_returns_401():

    board_name = "test board 1.00"

    url = f"{BASE_URL}boards/"

    query_params_post = {
        "key": API_KEY,
        "token": INVALID_TOKEN,
        "name": board_name
    }

    response_post = requests.post(url, params=query_params_post)

    assert response_post.status_code == 401


def test_create_board_without_name():

    board_name = None

    url = f"{BASE_URL}boards/"

    query_params_post = {
        "key": API_KEY,
        "token": API_TOKEN,
        "name": board_name
    }

    response_post = requests.post(url, params=query_params_post)

    assert response_post.status_code == 400


def test_create_board_empty_name():

    board_name = ""

    url = f"{BASE_URL}boards/"

    query_params_post = {
        "key": API_KEY,
        "token": API_TOKEN,
        "name": board_name
    }

    response_post = requests.post(url, params=query_params_post)

    assert response_post.status_code == 400


# $ pytest test_boards_with_fixtures.py::get_non_existent_board_returns_404 -v
# $ pytest test_boards_with_fixtures.py -v -s -k format