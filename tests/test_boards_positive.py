"""empty module docstring"""

def test_create_and_delete_board(boards_client):
    """User can create a new board and delete it"""
    name = boards_client.unique_board_name()
    response = boards_client.create_board(name)
    assert response.status_code == 200, (
        f"Expected response status code 200 when creating a board, got {response.status_code}"
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
        f"Expected response status code 404 whent trying to get deleted board, got {response_get.status_code}"
    )
# $ pytest tests\test_boards_positive.py -v