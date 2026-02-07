import os
import requests

from dotenv import load_dotenv
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

    assert response_post.status_code == 200

    response_post_json = response_post.json()

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