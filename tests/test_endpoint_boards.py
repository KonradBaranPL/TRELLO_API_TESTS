import os
import requests

from dotenv import load_dotenv
import json
import pytest


load_dotenv()

BASE_URL = "https://api.trello.com/1/"

API_KEY = os.environ["TRELLO_API_KEY"]

API_TOKEN = os.environ["TRELLO_TOKEN"]

ENDPOINT = "boards/"


def test_create_and_delete_board():
    
    board_name = "Python test board 07-02-2026 t.2"

    query_params_post = {
        "name": board_name,
        "key": API_KEY,
        "token": API_TOKEN
    }

    response_post = requests.post(
        BASE_URL + ENDPOINT,
        params=query_params_post
    )

    response_post_json = response_post.json()

    assert response_post.status_code == 200

    assert response_post_json["name"] == board_name

    board_id = response_post_json["id"]


    querry_params_delete = {
        "key": API_KEY,
        "token": API_TOKEN
    }

    response_delete = requests.delete(
        BASE_URL + ENDPOINT + board_id,
        params=querry_params_delete
    )

    assert response_delete.status_code == 200

def test_update_board():
    
    board_id = "68ceafb047a42bdf704cb0c7"

    board_name = "API test 88 updated"

    querry_params_put = {
        "key": API_KEY,
        "token": API_TOKEN,
        "name": board_name
    }

    response_put = requests.put(f"{BASE_URL}{ENDPOINT}{board_id}", params=querry_params_put)

    response_put_json = response_put.json()
    print(response_put_json)

    assert response_put.status_code == 200

    assert response_put_json["name"] == board_name

def test_update_board_2():

    board_id = "68ceafb047a42bdf704cb0c7"

    querry_params_put = {
        "key": API_KEY,
        "token": API_TOKEN,
    }

    response_get = requests.get(f"{BASE_URL}{ENDPOINT}{board_id}", params=querry_params_put)

    response_json = response_get.json()
    print(response_json)
    print(json.dumps(json.loads(response_get.text), sort_keys=True, indent=4, separators=(",", ": ")))

test_update_board_2()