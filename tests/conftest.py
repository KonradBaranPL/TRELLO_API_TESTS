import requests
import uuid
from config import API_KEY, API_TOKEN, BASE_URL
from typing import Generator

import pytest


@pytest.fixture
def auth_params() -> dict[str, str]:
    """Return Trello API key and token for authenticated requests."""
    return {"key": API_KEY, "token": API_TOKEN}


@pytest.fixture
def new_board(auth_params: dict[str, str]) -> Generator[dict[str, str], None, None]:
    """Creates a new board and deletes it at the end of the test. Returns board id and board name"""

    unique_id = str(uuid.uuid4())[:6]
    unique_board_name = f"test_board_{unique_id}"
    url = f"{BASE_URL}boards/"
    query_params_post = {**auth_params, "name": unique_board_name}

    response_post = requests.post(url, params=query_params_post)
    assert response_post.status_code == 200
    board_id = response_post.json()["id"]
    board_name = response_post.json()["name"]
    yield {"id": board_id, "name": board_name}

    query_params_delete = {**auth_params}
    response_del = requests.delete(f"{url}{board_id}", params=query_params_delete)
    assert response_del.status_code == 200


@pytest.fixture
def board_to_delete(auth_params: dict[str, str]) -> Generator[str, None, None]:
    """Creates a board without deleting it at the end of the test. Returns board_id"""

    unique_id = uuid.uuid4().hex[:8]
    board_name = f"test_board_{unique_id}"
    url = f"{BASE_URL}boards/"
    query_params = {**auth_params, "name": board_name}

    response_post = requests.post(url, params=query_params)
    assert response_post.status_code == 200
    board_id = response_post.json()["id"]
    yield board_id