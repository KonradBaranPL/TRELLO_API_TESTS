import requests
import uuid

from config import API_KEY, API_TOKEN, BASE_URL
import pytest


@pytest.fixture
def auth_params():
    """Return Trello API key and token for authenticated requests."""
    return {"key": API_KEY, "token": API_TOKEN}


@pytest.fixture
def new_board(auth_params):
    """Creates a new board and deletes it at the end of the test. Returns board id and board name"""

    unique_id = uuid.uuid4[:6]
    board_name = f"test_board_{unique_id}"
    url = f"{BASE_URL}board/"
    query_params_post = {**auth_params, "name": board_name}

    response_post = requests.post(url, params=query_params_post)
    assert response_post.status_code == 200
    board_id = response_post.json()["id"]
    yield board_id, board_name

    query_params_delete = {**auth_params}
    response_del = requests.delete(f"{url}{board_id}", params=query_params_delete)
    assert response_del.status_code == 200


@pytest.fixture
def board_to_delete(auth_params):
    """Creates a board without deleting it at the end of the test. Returns board_id"""

    unique_id = uuid.uuid4[:6]
    board_name = f"test_board_{unique_id}"
    url = f"{BASE_URL}boards/"
    query_params = {**auth_params, "name": board_name}

    response_post = requests.post(url, params=query_params)
    assert response_post.status_code == 200
    board_id = response_post.json()["id"]
    yield board_id