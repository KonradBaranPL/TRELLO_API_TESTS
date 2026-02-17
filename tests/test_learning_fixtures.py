import os
import requests

from dotenv import load_dotenv
import pytest


load_dotenv()

BASE_URL = "https://api.trello.com/1/"

API_KEY = os.environ["TRELLO_API_KEY"]

API_TOKEN = os.environ["TRELLO_TOKEN"]

ENDPOINT = "boards/"


@pytest.fixture
def new_board():
    board_name = "fixture test board 1.00"

    query_params_post = {
        "name": board_name,
        "key": API_KEY,
        "token": API_TOKEN,
        "defaultLists": "false"
    }

    response_post = requests.post(
        BASE_URL + ENDPOINT,
        params=query_params_post
    )

    assert response_post.status_code == 200

    board_id = response_post.json()["id"]
    # board_name = response_post.json("name")

    yield board_id
    # yield board_name

    query_params_delete = {
        "key": API_KEY,
        "token": API_TOKEN
    }

    requests.delete(f"{BASE_URL}boards/{board_id}", params=query_params_delete)

def test_get_board_details(new_board):

    query_params_post = {
        "key": API_KEY,
        "token": API_TOKEN,
    }

    board_id = new_board

    response_get = requests.get(f"{BASE_URL}boards/{board_id}")

    assert response_get.status_code == 200

    assert response_get.json["name"] == "fixture test board 1.00"
















# def test_get_list_of_boards():

#     querry_params = {
#         "key": API_KEY,
#         "token": API_TOKEN
#     }

#     response_get = requests.get(f"{BASE_URL}members/me/boards", params=querry_params)

#     print(response_get.elapsed.microseconds / 1000000)

#     assert response_get.status_code == 200

# def test_create_and_delete_board():
    
#     board_name = "Python test board 07/02/2026 t.2"

#     query_params_post = {
#         "name": board_name,
#         "key": API_KEY,
#         "token": API_TOKEN
#     }

#     response_post = requests.post(
#         BASE_URL + ENDPOINT,
#         params=query_params_post
#     )

#     response_post_json = response_post.json()

#     assert response_post.status_code == 200

#     assert response_post_json["name"] == board_name

#     board_id = response_post_json["id"]


#     querry_params_delete = {
#         "key": API_KEY,
#         "token": API_TOKEN
#     }

#     response_delete = requests.delete(
#         BASE_URL + ENDPOINT + board_id,
#         params=querry_params_delete
#     )

#     assert response_delete.status_code == 200

# def test_update_board():
    
#     board_id = "68ceafb047a42bdf704cb0c7"

#     board_name = "API test 88 updated"

#     querry_params_put = {
#         "key": API_KEY,
#         "token": API_TOKEN,
#         "name": board_name
#     }

#     response_put = requests.put(f"{BASE_URL}{ENDPOINT}{board_id}", params=querry_params_put)

#     response_put_json = response_put.json()
#     print(response_put_json)

#     assert response_put.status_code == 200

#     assert response_put_json["name"] == board_name
