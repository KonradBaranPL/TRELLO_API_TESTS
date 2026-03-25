"""empty module docstring"""

def test_create_and_delete_board(boards_client):
    """User can create a new board and delete it"""
    name = boards_client.unique_board_name()
    response = boards_client.create_board(name)
    assert response.status_code == 200, (
        f"Expected response status code 200 when creating a board, got {response.status_code}"
    )
    response_body = response.json()
    assert response_body["name"] == name, (
        f"Expected board name to be {name}, got {response_body["name"]}"
    )
    id = response_body["id"]
    delete_response = boards_client.delete_board(id)
    assert delete_response.status_code == 200, (
        f"Expected response status code 200 when deleting a board, got {delete_response.status_code}"    
    )

def test_delete_board(boards_client, board_to_delete):
    """User can delete existing board"""
    board_id = board_to_delete
    response = boards_client.delete_board(board_id)
    assert response.status_code == 200, (
    f"Expected response status code 200 when deleting a board, got {response.status_code}"    
    )
    response_get = boards_client.get_board(board_id)
    assert response_get.status_code == 404, (
        f"Expected response status code 404 when trying to get deleted board, got {response_get.status_code}"
    )

def test_get_board(boards_client, temp_board):  # przykład testu z jak największą liczbą asercji
    """User can get detailed data of a single board"""
    board_id = temp_board
    response = boards_client.get_board(board_id)
    assert response.status_code == 200, (
        f"Expected response status code 200 when getting a board, got {response.status_code}"
    )
    assert "application/json" in response.headers["Content-Type"], (
        f"Expected JSON response, got {response.headers["Content-Type"]}"
    )
    response_body = response.json()
    for field in ["id", "name", "desc", "descData", "closed", "url", "prefs"]:
        assert field in response_body, f"Missing field {field} in response body"
    assert response_body["id"] == board_id, (
        f"Expected id of the requested board, got {response_body["id"]}"
    )
    assert response_body["closed"] is False, (
        f"Expected 'closed' status of the board is False, got {response_body["closed"]}" 
    )
    assert isinstance(response_body["id"], str), f"Expected field 'id' to ba a string"
    assert isinstance(response_body["closed"], bool), f" Expected field 'closed' to ba a bool"

def test_update_board_name(boards_client, temp_board):
    """User can update an existing board by id"""
    pass
# $ pytest tests\test_boards_positive.py -v