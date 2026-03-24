"""empty module docstring"""

def test_create_and_delete_board(boards_client):
    """User can create a new board and delete it"""
    name = boards_client.unique_board_name()
    response = boards_client.create_board(name)
    assert response.status_code == 200, (
        f"Expected response status code 200 when creating a board, got {response.status_code}"
    )
    response_data = response.json()
    assert response_data["name"] == name, (
        f"Expected board name to be {name}, got {response_data["name"]}"
    )
    id = response_data["id"]
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

def test_get_board(boards_client, temp_board):
    """User can request a single board"""
    board_id = temp_board
    response = boards_client.get_board(board_id)
    assert response.status_code == 200  # dopisać komunikat w asercji

def test_update_board_name(boards_client, temp_board):
    """User can update an existing board by id"""
    pass
# $ pytest tests\test_boards_positive.py -v