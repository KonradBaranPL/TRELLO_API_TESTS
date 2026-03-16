import requests

import pytest
from config import API_KEY, API_TOKEN, BASE_URL


def test_get_board_details(new_board, auth_params):    
    board_id = new_board["id"]
    current_board_name = new_board["name"]
    url = f"{BASE_URL}boards/"
    query_params = {**auth_params}

    response_get = requests.get(f"{url}{board_id}", params=query_params)
    assert response_get.status_code == 200
    assert response_get.json()["name"] == current_board_name


def test_update_board(new_board, auth_params):    
    board_id = new_board["id"]
    new_board_name = "test board updated"
    url = f"{BASE_URL}boards/"
    query_params = {**auth_params, "name": new_board_name}

    response_put = requests.put(f"{url}{board_id}", params=query_params)

    assert response_put.status_code == 200
    assert response_put.json()["name"] == new_board_name


def test_delete_board(board_to_delete, auth_params):    
    board_id = board_to_delete
    url = f"{BASE_URL}boards/"
    query_params = {**auth_params}

    response_del = requests.delete(f"{url}{board_id}", params=query_params)
    assert response_del.status_code == 200

    response_get = requests.get(f"{url}{board_id}", params=query_params)
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
def test_create_board_with_different_names(board_name, auth_params):
    url = f"{BASE_URL}boards/"
    query_params_post = {**auth_params, "name": board_name}

    response_post = requests.post(url, params=query_params_post)
    assert response_post.status_code == 200
    response_json = response_post.json()
    assert response_json["name"] == board_name
    board_id = response_json["id"]

    query_params_del = {**auth_params}
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
def test_get_non_existent_board_returns_404(non_existent_id, auth_params):
    url = f"{BASE_URL}boards/{non_existent_id}"
    query_params = {**auth_params}

    response_get = requests.get(url, params=query_params)
    assert response_get.status_code == 404


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
def test_get_board_details_incorrect_id_format(board_id, auth_params):
    url = f"{BASE_URL}boards/{board_id}"
    query_params_get = {**auth_params}

    response_get = requests.get(url, params=query_params_get)
    assert response_get.status_code == 400


def test_get_board_details_missing_api_key(new_board):    
    board_id = new_board["id"]
    url = f"{BASE_URL}boards/{board_id}"
    query_params_get = {"key": None, "token": API_TOKEN}

    response_get = requests.get(url, params=query_params_get)
    assert response_get.status_code == 401


def test_get_board_details_without_api_key(new_board):    
    board_id = new_board["id"]
    url = f"{BASE_URL}boards/{board_id}"
    query_params_get = {"token": API_TOKEN}

    response_get = requests.get(url, params=query_params_get)
    assert response_get.status_code == 401


def test_create_board_with_invalid_token_returns_401():
    board_name = "board_name_example"
    url = f"{BASE_URL}boards/"
    invalid_token = "invalid_token_exaple"
    query_params = {
        "key": API_KEY,
        "token": invalid_token,
        "name": board_name
    }

    response = requests.post(url, params=query_params)
    assert response.status_code == 401



def test_create_board_without_name(auth_params):
    board_name = None
    url = f"{BASE_URL}boards/"
    query_params = {
        **auth_params,
        "name": board_name
    }

    response = requests.post(url, params=query_params)
    assert response.status_code == 400


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