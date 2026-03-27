"""missing docstring"""

import requests

import pytest

def test_get_non_existent_board_returns_404(boards_client):
    """
    Verifies that getting a board with valid-format but non-existent id
    returns status code 404
    """
    non_existent_id = "1234567890abcdefABCDEF12"  # "aaaaaaaaaaaaaaaaaaaaaaaa" "1234567890abcdefABCDEF12" "aB12aB12aB12aB12aB12aB12" "111111111111111111111111"
    response = boards_client.get_board(non_existent_id)
    assert response.status_code == 404, (
        f"Expected status code 404, got {response.status_code}"
    )

# nie potrafiłem usunąć token z metody get w klasie BaseClient
def test_get_board_with_missing_token_returns_401(boards_client, temp_board):
    """
    Verifies that getting a board without api token in params
    returns status code 401
    """
    board_id = temp_board
    url = f"{boards_client.base_url}boards/{board_id}"
    params = {"key": boards_client.key}
    response = requests.get(url, params=params)
    assert response.status_code == 401

# parametryzacja w mojej oryginalnej wersji, zostawiłem do porównania
@pytest.mark.parametrize(
        "board_id",
        [
            pytest.param(
                "699ae269ca2fedf41c98afb",
                 id="too short, 23-character length"
            ),
            pytest.param(
                "699ae269ca2fedf41c98afb6a",
                id="too long, 25-character length"
            ),
            pytest.param(
                "Z99ae269ca2fedf41c98afb6",
                id="correct length but contains letter 'Z' inconsistent with pattern"
            ),
            pytest.param(
                "?99ae269ca2fedf41c98afb6",
                id="correct length but contains special character '?' inconsistent with pattern"
            )
        ]
)
def test_get_board_incorrect_id_format(board_id, boards_client):
    """
    Verifies that getting a board using id in incorrect format
    returns status code 400
    """
    response = boards_client.get_board(board_id)
    assert response.status_code == 400

# parametryzacja poprawiona wg. ChatGPT
@pytest.mark.parametrize(
        "board_id",
        [
            pytest.param("699ae269ca2fedf41c98afb", id="len=23"),
            pytest.param("699ae269ca2fedf41c98afb6a", id="len=25"),
            pytest.param("Z99ae269ca2fedf41c98afb6", id="non-hex char"),
            pytest.param("?99ae269ca2fedf41c98afb6", id="non-alnum char")
        ],
)
def test_get_board_incorrect_id_format(board_id, boards_client):
    """
    Verifies that getting a board using id in incorrect format
    returns status code 400
    """
    response = boards_client.get_board(board_id)
    assert response.status_code == 400




# $ pytest tests\test_boards_negative.py -v